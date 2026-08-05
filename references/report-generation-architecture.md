# 多片段报告生成架构 + 目录/锚点注入（生产实证）

> 场景：5 大板块 × 25 小节的中文 HTML 报告，一次写成一个巨型生成脚本容易失控（单文件数千行、跨区细节难调、改一处要重跑全部）。此架构把一个报告拆成 **N 个片段脚本 + 1 个主拼接脚本**，已验证可行。

## 架构

单个 `part{K}.py` 产出该板块的 HTML 字符串到同名 py 模块：

```python
# <WORKDIR>/part2.py — 只负责「第二部分」
def src(t): ...   # 来源角标
def sub(t): ...   # 小节标题
def note(t): ...
def sec(num,title,srcbar,body): ...   # section 包裹
s2_body = []
s2_body.append('<div class="sub-title">...</div>')
# ... 组装该板块所有小节 ...
S2 = sec('二','产品介绍', S2_SRC, ''.join(s2_body))
with open('<WORKDIR>/part2.py','w') as f:
    f.write("S2 = " + repr(S2))
print("P2 完成, len:", len(S2))
```

主脚本 `importlib` 加载各片段得到 `S1..S5` 字符串，再拼 hero + 目录 + footer：

```python
spec = importlib.util.spec_from_file_location('p2','<WORKDIR>/part2.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
S2 = m.S2
html = html_head + S_SF + S1 + S2 + S3 + S4 + S5 + html_foot
```

- 每个 part 文件**自包含**必要的辅助函数（src/sec/sub/note），不要依赖跨文件 import——片段脚本被主脚本 `exec_module` 加载时不一定有其它模块的命名空间。
- CSS 定义放在**第一个 part（P1）顶层变量**（如 `CSS`），主脚本从 `m1.CSS` 取，避免重复维护。
- 片段脚本独立可跑（`python3 gen_curling_p2.py`），方便单板块调试；改完某板块只重跑该 part + 主拼接。

## ⚠️ 锚点/目录 id 注入：别用朴素 replace 覆盖

场景：要在每个 `<div class="section-title">` 上加 `id="s{N}"` 供目录平滑滚动。错误的做法——遍历所有 id 对同一字符串做多次 `replace('<div class="section-title">',...id...,1)`，会**反复命中同一位置**，最后被最后一个 id 覆盖（6 个 section 全变成 s5）。

正确做法：**先判断该 body 片段实际含哪个 no**，匹配到了才注入对应 id 并 break：

```python
sec_ids = {'★':'s0','一':'s1','二':'s2','三':'s3','四':'s4','五':'s5'}
def anchorize(body):
    for no, sid in sec_ids.items():
        if ('<div class="section-title"><span class="no">%s</span>' % no) in body:
            body = body.replace(
                '<div class="section-title"><span class="no">%s</span>' % no,
                '<div class="section-title" id="%s"><span class="no">%s</span>' % (sid, no), 1)
            break
    return body
S1 = anchorize(S1)   # 每个 section 片段各注入一次
```

## 目录（TOC）样式 + 平滑滚动

```css
.toc{background:var(--card);border:1px solid var(--brd);border-radius:14px;padding:22px 28px;margin:20px 0;}
.toc li{margin:7px 0;}
.toc a{display:flex;align-items:baseline;gap:10px;text-decoration:none;color:#334155;padding:7px 10px;border-radius:8px;}
.toc a:hover{background:#eff6ff;color:var(--blue-d);}
html{scroll-behavior:smooth;}
.section-title{scroll-margin-top:16px;}   /* 锚点定位不被吸到视口顶部 */
```

目录放 hero 之后、正文之前：`<div class="toc"><h3>📑 目录导航</h3><ol>...<li><a href="#s1"><span class="no">一</span><span class="t">市场概况</span></a></li>...</ol></div>`。

**用户偏好**：用户明确要求报告**带目录导航**；页脚/hero 署名用 **<署名>**（使用者在运行时指定；默认留空）。生成后校验 6 个 `id="s0..s5"` 与 6 个 `href="#s0..s5"` 一一对应。

## ⛔ 标签配对 audit（生成后必跑，防静默破坏）

只检查「5 大板块标题都在」不够——一个板块内某 `<li>` 未闭合会静默破坏整节排版但不报错。**每次生成后跑完全标签配对**：

```python
import re
html=open('<YOUR_REPORT>.html',encoding='utf-8').read()   # 换成你的报告文件
for tag in ['section','div','table','tr','td','th','ul','ol','li','b','span']:
    o=len(re.findall(r'<%s[\s>]'%tag,html)); c=len(re.findall(r'</%s>'%tag,html))
    print(f'<{tag}>: {o}/{c}', '✓' if o==c else '✗ MISMATCH')
```

- **常见根因**：字符串字面量里误加尾随分号切断了闭合标签。例：`s.append('<li>...一机多用+特殊卷型"。);` 结尾多一个 `);`，少写 `</li>` → 该 `<li>` 永不闭合，`<li>` 计数比 `</li>` 多 1。排查时按 `<section>` 切块逐段统计 `open/close`，快速定位到具体板块，再在源码里逐行 grep 该段落的 `<li>`。
- **`<br>` / `<li>` 的"不闭合"是假阳性**：`<br>` 是 void 元素、HTML5 中 `</li>` 可省略，audit 会报 `open≠close` 但**不是错误**。真正要盯的是 `<div>/<section>/<table>/<tr>/<td>/<th>/<span>` 这类**必须闭合**的容器标签。审的时候把这些排除在"必须配对"之外。
- **div 未闭合的定位法（stack 净深度扫描）**：对所有所有 `<div>` 做 `<(/?)(div)>` 正则 + 栈匹配，结束时栈里剩下的那个就是漏闭合的 `<div>`，打印其 start 位置 + 后续 400 字符上下文一眼看出漏在哪。再用各 section 锚点 id 切块逐段统计 `open/close`，net 非 0 的那段就是问题板块。**常见错**：`<div class="insight-box">`/`<div class="verdict-box">` 开了却忘在结尾补 `</div>`。
  - ⚠️ **分段统计的边界假象**：最后一段（S5 → `<foot>`）因为锚点 `id="s5"` 落在 section 内部、且不含开头容器也不含结尾 `</div>`，net 常显负值——**别慌，以"全文档 div open==close"为准**，它正确配平则无需处理。
  - ⚠️ **主容器 wrap 干扰**：content `<div class="wrap">` 由 html_foot 开头的 `</div>` 闭合；若做"从 wrap 到 foot 前"区间统计，净深度应为 +1（wrap 自身），+2 才表示板块内还有 1 个真漏。

## ⛔ 跨片段 `sec()` 签名漂移（emoji/section-sub 重构时必踩）

给多个片段脚本**统一加参数**（如 `sec()` 从 4 参扩到 6 参支持 `emoji, ssub`）时，**每个 part 文件都有自己的 `sec()` 定义 + `SX = sec(...)` 调用点**，必须**两者同步改**。只改定义不改调用、或反过来，立即 `TypeError: sec() takes 4 positional arguments but 6 were given`。

经验做法（生产实证）：用 Python 脚本批量处理所有 part 文件，对每个 part 同时做两处替换：
1. `def sec(...)` 定义体 → 加 `emoji="", ssub=""` 参数 + 注入 `<div class="section-sub">` 与 emoji；
2. 末尾 `SX = sec('X','标题', SRC, ''.join(body))` 调用 → 追加 `, '🗂️', '副标题'`。

调用点正则（变量名 `S2` 用数字、num 参数用中文『二』，别写错）：
```python
pat = re.compile(r"S%s = sec\('%s','[^']*', S%s_SRC, ''.join\(s%s_body\)\)" % (num, cn[num], num, num))
```
批量 patch 后**逐个 `python3 part{N}.py` 编译**验证（P1 的 `sec()` 常是 4 参旧版——若其它 part 已扩 6 参而 P1 漏改，主脚本 `importlib` 加载即报 TypeError）。

## 📐 "参考 X 报告优化 Y 报告"结构对齐清单

用户说「参考 B 报告优化 A 报告」时，不是调文字，而是要**把 A 的呈现结构对齐到 B**。逐项核对下面这组参考报告的结构要件（缺则补齐）：

- **板块标题带 emoji**（📊 市场概况 / 🧾 产品介绍 / 👥 受众分析 / 🎯 需求洞察 / 🚀 开发策略）+ 每板块开头 `div.section-sub` 标注「线上(Amazon US Sorftime实时) 与 线下(公开信息) 分开呈现」。
- **KPI 四卡**：Top100 月销量 / 月销额(≈人民币) / 平均客单价(+中位价) / 线上预估年销额。
- **头部卖家份额 bar**：Amazon 自营 / CR3 卖家 / CR3 品牌 / CR3 产品 四行。
- **线上 vs 线下规模拆解表**：年销额/年销量/主力渠道/主力玩家/价格带/数据口径，分行线上+线下双列。
- **市场趋势拆成 ①②③④ 四节**：
  ① 生命周期阶段 → verdict-box（结论 + 判定依据 + 品类平均生命周期长度）
  ② 近3年增长率 + 未来3年预测 → 数据表 + insight-box 预测 CAGR
  ③ 旺季与淡季 → 季节性指数 bar（12月/11月/7月/2月，年均为 1.0）
  ④ 近12个月销量 **+ 销售额** 双曲线（bar 逐月；销额=月销量×当月均价 估算，`tag-est` 标注；旺季月用不同色标）。
- **品牌表**要「线上% / 整体%」两列；**波特五力**用「线上现状 / 线下现状 / 应对策略」三列。
- 提炼历史数据：从 `category_trend`(SalesCount+AvgPrice) 算季节性指数（`月销量/该年月均`）、两连续12月窗口同比、近12月销量+销额曲线——数据点必须能从 raw JSON 验算，不能手写死。

> 结构对齐完，重跑 标签配对 audit + 锚点/目录 + 署名 + emoji/section-sub 计数，再部署。
