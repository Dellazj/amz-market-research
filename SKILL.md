---
name: amz-market-research
description: |
  通用「产品 × 国家」亚马逊市场调研报告生成器。输入任意产品名 + 目标国家（如「直发梳 Straightener brush × 美国」、「空气炸锅 × 德国」），
  以资深产品开发经理视角产出结构化市场调研报告（角色设定 + 五大部分：①市场概况 ②产品介绍 ③受众分析 ④用户需求洞察 ⑤产品开发策略）。

  使用时机：
  - 用户给出「产品 + 国家」要求做市场调研（市场容量/趋势/竞争/TOP公司/波特五力/产品功能/受众/痛点/认证/专利/差异化/蓝海/FABE/SWOT/PEST）
  - 用户参考某框架要求做成可复用的选品市场调研 SKILL，产品名和国家可相应调整
  - 触发词：市场调研, 市场概况, 波特五力, SWOT, PEST, 产品开发策略, market research

  数据来源双轨（用户已确认）：
  - 线上：以 Sorftime MCP 能抓取的亚马逊实时数据为准（销量/价格/星级/评论/好评差评原声/关键词）
  - 线下：以公开信息为准，必须标注具体来源依据链接，并区分「事实/估算」
  - 所有数据点标注来源工具 + 估算标记，绝不编造假数据

  输出形式：单文件蓝灰商务风 HTML（纯 CSS 组件，见参考），产品名/关键词保留英文 + 中文翻译，汇报全程中文。
  定位：聚焦「角色设定的产品×国家市场调研」；如需类目粒度的细分类目报告，可配合其他通用类目调研 skill 使用（不在本包内）。
user-invocable: true
risk-level: low
---

# 通用产品 × 国家市场调研报告生成器

## 定位

以「资深产品开发经理」角色，对「任意产品 × 任意国家」产出一份结构化的市场调研 HTML 报告。**产品名 + 国家为可调参数**。

## 用户已确认的硬性需求

1. **角色设定**：资深产品开发经理视角，回答专业、客观、详细；不胡编乱造，不确定时明说「不知道」。
2. **可参数化**：产品名（中英）+ 国家随时可换。
3. **汇报语言**：全程中文；产品名/关键词保留英文 + 中文翻译。
4. **数据溯源双轨**：
   - 线上数据以 **Sorftime MCP** 抓取的亚马逊实时数据为准（绝不编造）
   - 线下数据以**公开信息**为准，**标注具体来源链接**
   - 每个数据点区分「事实 / 估算 / 需人工核实」
5. **线上线下的市场数据分开展示**（不要混在一起）。
6. **输出形式**：单文件蓝灰商务风 HTML（纯 CSS，无 ECharts），可部署 Cloudflare。

## 报告结构（五大部分，固定框架）

### 第一部分：市场概况
| 小节 | 内容要点 |
|------|---------|
| 市场容量 | 线上+线下年销售额/销量、头部卖家市场份额分布、市场集中度 CR3/CR5 |
| 市场趋势 | 生命周期阶段+判定依据+品类平均生命周期长度；近3年增长率及未来3年预测；旺季/淡季（可加「近12个月销量/销售额曲线」，**销量/销额两幅分开**，纯 CSS 做法见 `references/pure-css-trend-curves.md`） |
| 市场竞争 | 线上/线下线上竞争格局 |

> 📐 用户说「参考 B 报告优化 A 报告」时，结构对齐清单（emoji 标题 + section-sub + KPI四卡 + 头部卖家份额bar + 线上/线下拆解表 + 市场趋势①②③④ + 品牌线上%/整体%两列 + 波特五力三列）见 `references/report-generation-architecture.md` 末尾「参考 X 报告优化 Y 报告」节；跨片段 `sec()` 签名漂移坑同见该文件。
| TOP公司 | 头部品牌：所属国家/成立年份/公司背景/年收入/份额占比/核心竞争力（**表格**） |
| 波特五力模型 | 五力框架分析线上/线下现状与应对策略 |

### 第二部分：产品介绍
| 小节 | 内容要点 |
|------|---------|
| 产品认知 | 市场热销+新上架产品核心卖点提炼与分类 |
| 产品功能 | 款式/功能/平均成本/美国市场平均客单价 |
| 产品构成 | 材料+部件+成本占比（**表格**） |
| 使用场景 | 所有应用场景列表 |

### 第三部分：受众分析
| 小节 | 内容要点 |
|------|---------|
| 受众特征 | 性别/年龄/兴趣/职业/收入/教育/家庭情况 |
| 受众习惯 | 购物频次/消费金额/购物时间/购物方式 |
| 受众购买产品 | 互补产品+常购买其它产品 |
| 受众问题 | TOP20 常见问题 |
| 受众好评 | TOP20 好评按频次占比降序（另配「消费者原声」节：每条英文/法语原声**附中文翻译**） |
| 受众差评 | TOP20 差评按频次占比降序（同上，差评原声也**每条附中译**，法语差评保留+中译+法语tag） |

### 第四部分：用户需求洞察
| 小节 | 内容要点 |
|------|---------|
| 产品痛点 | 已解决痛点 + 未解决痛点 |
| 需求金字塔模型 | drill 需求模型表格（需求层级/具体表现/优先级/解决方案） |
| 应用场景与卖点关联 | 表格（场景类型/关键需求/核心卖点） |
| 人群画像与产品卖点匹配 | 表格（消费人群/核心需求/核心卖点） |

### 第五部分：产品开发策略
| 小节 | 内容要点 |
|------|---------|
| 产品认证 | 中国制造→目标国亚马逊所需认证，周期/费用的**表格** |
| 产品专利 | 专利侵权风险 + 规避方法 |
| 风险把控 | 开发设计中的风险点与应对，提高成功率 |
| 差异设计 | 材料/外观/功能/结构差异化设计建议 |
| 蓝海战略机会挖掘 | 表格（选品方向/具体策略/数据支撑及案例） |
| 新产品形态FABE对比 | 表格（特征F/优势A/利益B/证据E） |
| SWOT与PEST | 分别分析进入可行性 + 总结打分（满分10） |

## ⛔ 报告完整度（对标参考基准）

> ⛔ **首版必须是六大部分完整框架，绝不默认为精简结构（生产实证，用户发现后原话批评过两次）**：默认输出完整版、绝不因"够用""太长"而自行降级小节，是运行时最重要的一条规矩。完整框架红线为：**六大部分 + 每一部分的全部小节（即使感觉冗余）都必须齐全**。市场概况含 CR3产品/品牌/卖家三指标、#1单品占比、线上vs线下拆解表（分成两列）、波特五力三列、头部品牌线上%/整体%两列、销量/销额两幅独立曲线；产品介绍含1688实测成本表；受众含画像/习惯/互补品/TOP问答表 + 每条原声附中译；需求含痛点/金字塔/场景关联/画像匹配；开发策略含认证表(监管机构列)/专利具体品牌/风险应对表/差异设计/蓝海表/FABE/SWOT/PEST/可行性评分。

> 若你有线上参考基准报告，可把它的 URL（如 `<YOUR_REFERENCE_REPORT>.pages.dev/#s4`，任意完整版调研报告都可）作为「完整度示范」对照；**首版齐全度不够会被判「报告不全」**。生成任何调研报告前，先对照本 skill 的 `references/report-completeness-standard.md` 核对达标项（⭐=首版易漏，务必补齐）：
- 市场概况：CR3**产品/品牌/卖家三指标**、#1单品占比、高评分/高评论占比、线上vs线下拆分表、**新品销量占比**、月销额**换算人民币**
- 产品介绍：卖点**分类表**、款式/功能/线上价/**1688实测出厂成本**表
- 受众分析：详细画像表、购物习惯表、互补产品、**受众常见问题表**。
- 开发策略：认证表含监管机构列、专利风险**具体品牌**、**风险点与应对表**。
- **⚡ ①销量/销额曲线「分开显示」为两幅独立柱状图**（用户硬性要求）：市场趋势「④近12个月销量/销售额曲线」必须拆成**两张分开的图**——上图「月销量曲线(件)」下图「月销额曲线(CAD/美元, 销量×均价估算, tag-est)」，各自独立 `bar-item` 序列，**严禁混成一幅**。柱条格式：`blabel(月份)` + `btrack(bfill width%)` 值 `"27,782件"` + `bval "28K"`（销量图）；销额图 `$xx万` + `$x.xM`。
- **⚡ ②消费者原声「每条都附中文翻译」**（用户硬性要求）：P3「消费者原声（好评+差评）」的**每一条**评论原声都必须紧跟 `class="cn"` 中文翻译，格式：`<div class="review"><div class="stars">★…</div><div class="en">"英文/法语原文"</div><div class="cn">—— 中文翻译（产品标注）</div></div>`；好评绿标 `var(--green)`「■典型好评」、差评红标 `var(--red)`「■典型差评」分列两栏（grid-2）。**任何评论只有原文无中译，都会被用户判定为缺失**。法语差评保留原文 + 中文翻译 + 法语 tag。
- 每章开头 src-bar 标来源；重要洞察用 callout/insight-box 强调非平铺

> 📏 生成后如需核对线上参考报告的结构（`bar-item`/c​n 中译/锚点 s0-s5 等），可用 `curl` 拉取你的参考报告 HTML 后逐项对比 tag 配对与类名。

关键提取技术（一次 `category_report` 即得 CR3三share + Amazon自营 + 高评分/高评论share；新品占比=解析 online_date≤90天；出厂成本用 ali1688_similar_product 真实价格）——详见该 reference 文件。

## 数据采集工作流（Sorftime MCP）

> ⚙️ **数据源接入说明**：本 SKILL 依赖 Sorftime 电商数据。请通过你已配置好的 Sorftime MCP 工具（`mcp.sorftime.com`，SSE）调用以下工具；如你的 MCP 服务偶发不可达，可用一个轻量 Direct Client 脚本（SSE 调用 `tools/call`）替代，把下面示例命令里的 `<YOUR_DIRECT_CLIENT>` 换成你本地脚本路径即可：
> `<YOUR_DIRECT_CLIENT> <tool_name> '<json_args>'`（snake_case 参数，SSE 解析）。
> 工具名用 camelCase 的短名：`product_detail` / `product_reviews` / `category_report` / `category_search_from_product_name` / `product_traffic_terms` / `keyword_detail` 等（可用 `tools/list` 查询全部）。
> 参数名为 snake_case（如 `amz_site` 不是 `amzSite`，`review_type` 不是 `reviewType`）。

> ⛔ **Direct Client 返回格式不统一（生产实证）**：绝大多数工具（`category_report` / `category_trend` / `category_keywords` / `product_detail` / `product_reviews` / `product_traffic_terms`）返回 `{"result":{"content":[{"text":"<json字符串>","type":"text"}]}}`，需对 `content[0].text` 再 `json.loads` 一次取 `['data']`。但**个别工具直接返回纯文本字符串**：
> - `product_trend`：`text` 是明文 `"2025年04月=14,2025年05月=171,..."`（`YYYY年MM月=N` 逗号分隔）。对它 `json.loads(text)` 会报 `JSONDecodeError: Extra data`——**改用 `text.split(',')` 再按 `=` 拆键值**解析。
> - `get_time`：`text` 是明文含 `current_time`。
> 解析前先 `print(text[:200])` 看是真 JSON（以 `{` 开头）还是明文，再决定用 `json.loads` 还是字符串拆分。另注意 `product_detail` 的 `seller_name`/`top_category` 等字段含 `$`/`&` 需留意转义，`star_rating`/`price`/`review_count` 可能为 float/str 混用，转浮点时用 `try: float(x) except: 0.0` 兜底。

> ⛔ **`product_detail` 的 `attributes` 字段是 JSON 字符串，不是 dict（生产实证，直接 `.get()` 会崩）**：`ad.get('attributes')` 返回的是 `str`（形如 `"{\"Material\":\"Ceramic\",\"Power source\":\"Corded Electric\",...}"`），对它 `.get()` 报 `AttributeError: 'str' object has no attribute 'get'`。用前必须兜底解析：`a = ad.get('attributes'); a = json.loads(a) if isinstance(a,str) else (a or {})`，再 `a.get('Material','-')`。顺带可复用的健壮字段：经 `product_detail` 已直接给出 `fba_fee` / `gross_profit` / `gross_profit_rate` / `monthly_sales_amount` / `days_on_shelf` — 写成本测算与单品卡时优先用这些而非自己算。

### 类目定位 + 市场数据
> ⛔ **类目定位坑（同类目实证）**：`category_search_from_product_name` 常把产品归到**宽泛父类目**（如美发工具类下把品类归到均价过低的父类，与主流价格带严重不符，如标称 $30-70 的商品归到均价 $11 的父类）。**先核对返回均价/价格带是否吻合**；不吻合时用 `category_name_search` 换更精确的细分类目名。

| 数据 | 工具（短名） | 参数 |
|------|------------|------|
| 定位细分类目(初筛) | `category_search_from_product_name` | `product_name`, `amz_site` |
| 确认精确类目 | `category_name_search` | `category_name`(精确子类目名), `amz_site` |
| Top100榜单 | `category_report` | `node_id`, `amz_site`（输出大→重定向文件+Python解析） |
| 类目趋势 | `category_trend` | `node_id`, `trend_index=SalesCount` 等 |

> ⛔ **类目趋势没有直接月销额（SalesAmount）**：`category_trend` 的 `trend_index` 传 `"SalesAmount"` 会报错返回 `An error occurred invoking 'category_trend'`（有效枚举只有 SalesCount/AvgPrice/各 Share 占比等，**没有原始总销额**）。要「近12个月销售额曲线」时：分别拉 `SalesCount`（月销量）与 `AvgPrice`（当月均价），`月销额 = 月销量 × 当月均价` 计算；此列为**估算**，必须在图上/说明里用 `tag-est` 标注（销量与均价本身仍是 Sorftime 实时真数据，只有相乘这一步是推算）。
| 类目关键词 | `category_keywords` | `node_id` |
| 产品详情 | `product_detail` | `asin`, `amz_site` |
| 评论 | `product_reviews` | `asin`, `amz_site`, `review_type`(Both/Positive/Negative) |
| 反查关键词 | `product_traffic_terms` | `asin` |
| 关键词详情 | `keyword_detail` | `keyword`（周搜索量/CPC/趋势） |
| 供应商成本 | `ali1688_similar_product` / `ali1688_product_search` | `search_name` |
| 产品趋势 | `product_trend` | `asin`, `product_trend_type` |

### 变体评论过滤
- 用户指定的具体子体 ASIN → 严格按 `Asin` 字段过滤
- 父体 ASIN（有多个变体）→ 保留所有变体评论作为整体口碑
- 诊断：拉第一页后检查 `Counter(r.get('Asin'))`，目标ASIN占比<50%说明是父体

### 好评/差评频次统计（受众 TOP20 好评/差评）
- 用 `product_reviews` 拉 Positive + Negative 两部分真实评论
- 按星级/情感分组，统计高频话题/评价词出现频次占比，**降序输出**
- ⛔ 评论量不足以支撑 TOP20 时降级为 TOP10 并明确说明「样本量不足以支撑TOP20」，**绝不硬凑**

## 线下数据（公开信息溯源）

线下市场、公司背景、认证、专利、行业趋势等 Sorftime 覆盖不到的数据：
- 用公开信息 + 行业常识，**必须标注来源链接或「估算/需人工核实」**
- 公司年收入/市场份额 → 公开财报/行业报告 + 估算标注
- 认证周期费用 → 目标国监管机构（如美国 FCC/FDA/CPSC）官方信息 + 合理区间
- 专利风险 → 关键词检索提示 + 明确「需专业专利代理核实」

## 样式系统

⛔ 完整 CSS 组件库（蓝灰商务风，纯CSS无ECharts）见 `references/pure-css-trend-curves.md` 与本 SKILL 的生成器模板 `templates/generator_template.py`（内含 `CSS` 常量 + `kpi/bar/sec/note` 组件函数，可直接复用）：
- `kpi-grid/kpi-card`、`bar-item/bar-track/bar-fill`、`insight-box`、`verdict-box`、`table-wrap`、`detail-card`、`grid-2`、`tag-*`
- 默认主题：蓝灰商务风（--blue #2563eb，灰阶）

每个章节用 `<section>` + `div.section-title`；每个市场数据附带来源角标（Sorftime / 公开信息 / 估算）。

> ⛔ **生成器脚本：别用一个大 f-string 拼 HTML**
用 Python 脚本生成单文件 HTML 报告时，**不要 `HTML = f\"\"\"...{CSS}...{section(...)}...\"\"\"` 一个巨型 f-string**——CSS 里的字面大括号（`.bar-fill{...}`）和嵌套 f-string 会把外层解析器搅乱，报 `SyntaxError: f-string: single '}' is not allowed`。可靠做法（本 skill 生产证实）：
- CSS 存成普通（非 f）字符串变量，HTML 用**字符串拼接 `+`** 组装，而**不是 f-string**。
- kpi/bar/review/section 等小组件函数内部用 `%` 格式化（`'<div class=\"kpi-card %s\">...' % (cls, ...)`），组件函数本身自洽、不含 CSS 大括号，安全。
- 若 HTML 里个别处要插变量（如 `style=\"width:{pct}%\"`），用拼接或 `%` 传参，不要写进 f-string。

> ⛔ **`%`-format 字符串里中文正文的孤立 `%` 号会让 format 炸（生产实证）**：用 `'...' % (a,b,c)` 做 `%` 格式化时，若字符串**正文里还混有百分比字面量**（常见：`占44%销量`、`CR3 45.25%`、`新品销量占比3.2%`），那个 `%` 会被当成占位符，导致 `TypeError: not enough arguments for format string`（或者取到错误值，如中文 `4+星里97.43%` 中 `%` 前的 `4` 被误当转义、`97.43` 取不到）。**修法**：① 优先把该段改成**纯字符串拼接**（`'<b>'+('%.1f'%x)+'</b>…'`），把每个数字单独 `%` 格式化后 `+` 进长串，长串本体不再做一次 `%`；② 或全文 `%` 需要转义成 `%%`。**判断**：`%.1f%%` 里 `%%` 是对（转义出字面 `%`），但正文其它孤立 `%` 会错配——所以含中英混合百分比的大段落，**干脆不用 `%`-format，改拼接最省心**。

### ⛔ 英文评论原声里的撇号会炸掉单引号字符串（生产实证，必踩）
好评/差评**原声英文**几乎必然含缩写撇号：`I've` / `don't` / `didn't` / `it's`。若 append 行用外层单引号 `s.append('...I've...')`，撇号会**提前终止字符串**报 `SyntaxError: unterminated string literal`（报错行号常指到实际非问题行，难定位）。修复首选：
- **用 Unicode 转义写撇号**：`I\u2019ve`、`don\u2019t`（保持外层单引号，`\u2019` 是右单引号撇号，HTML 显示为 `'`）。
- 或整行改用外层双引号 `s.append("...I've...")`，此时内嵌的英文双引号（原文引用 `"..."`）需转义为 `\"`——更麻烦，`\u2019` 更省。
- **预防**：把英文原声统一在开头就用 `\u2019` 代替所有撇号；或把英文译文字符串先存成变量再 `.encode('unicode_escape')` 检查。写完脚本后先 `python3 file.py` 编译验证（生成前必跑），不要直接拼进报告。
- **同类相关**：中文翻译里通常没有撇号，但英文原声标点（`'`）一律用 `\u2019` 即可彻底规避。

### 多片段生成架构 + 锚点/目录/标签审计
大报告（5大板块25小节）别全塞进一个生成脚本——拆成 `part{N}.py`（各产出一个 `S{N}` HTML 字符串）+ 主拼接脚本（`importlib` 加载拼接）。目录锚点 id 注入、TOC 样式、生成后标签配对 audit 等**已验证模式**详见 `references/report-generation-architecture.md`。

> ⛔ **组件辅助函数是固定参数个数，多传位置参数会 Python TypeError（生产实证）**：`kpi(v, l, cls="")` 只有 3 个位置参数、`bar(label, val, pct)` 只有 3 个、`sec(num, title, body, emoji="", ssub="")` 最多 5 个。调用时若多写一个（如 `kpi(v, l, "sm", "g")` 传了 4 个，想在 `cls` 后再加颜色）会报 `TypeError: kpi() takes from 2 to 3 positional arguments but 4 were given`，且**报错发生在我拼接串联 `p1.src()+p2.src()+...` 那行**——真正出错在某个 `part{N}.py` 里的组件调用，堆栈会指到主脚本而非组件库，误导排查。**教训**：① 组件函数签名不支持临时加参，需要颜色时用默认 `cls` 字符串里已有的语义类（如 `"g"`/`"w"`/`"r"`），不要另传第 4 个；② 生成脚本写完后先 `python3 part{N}.py` / `python3 main.py` **先编译再跑**，让 TypeError 在编译/首跑就暴露，别等拼完 5 部分才发现。

## 部署

报告生成后可选发布到线上（Cloudflare Pages / 任意静态托管）。以下给出两种方式，均为**通用命令**，请把 `<YOUR_DEPLOY_CONFIG>` 等替换为你自己的路径/凭证：

**方式一：`wrangler` CLI（推荐，最可靠）**
```bash
# 先建项目（仅首次；把 <name> 换成你的项目名）
npx --yes wrangler@latest pages project create <name> --production-branch main
# 把报告复制为部署目录的 index.html，再部署目录
rm -rf /tmp/<name>_deploy && mkdir -p /tmp/<name>_deploy \
  && cp report.html /tmp/<name>_deploy/index.html \
  && npx --yes wrangler pages deploy /tmp/<name>_deploy --project-name <name>
```
- 记住 `wrangler pages deploy` 要传**目录**不是单文件（单文件报 `ENOTDIR`）
- 正式环境需登录/配置 `CLOUDFLARE_API_TOKEN`（env var），示例：`bash -c 'source <YOUR_CF_ENV_FILE> && npx --yes wrangler pages deploy ...'`，把 `<YOUR_CF_ENV_FILE>` 换成你本地存 token 的文件。
- 成功输出含 `https://<hash>.<name>.pages.dev`；若本机无法访问 *.pages.dev（沙箱常见），用生产域名 `https://<name>.pages.dev` 或 Cloudflare API 确认部署状态。
- Pages 项目不存在时先 create（报 `The Pages project "<name>" does not exist` 就是没建）。

> ⛔ **REST API 手动 direct-upload 必须带 `manifest` 字段（生产实证，漏了报错 8000096）**：不用 wrangler、直接 `POST /accounts/{acct}/pages/projects/{name}/deployments` 时，multipart 里必须含一个 `manifest` 字段，值为 `{"文件路径": "<sha256>"}` 的 JSON（哈希用 `sha256sum index.html` 取），且同名文件作为另一个表单字段一并提交。缺 `manifest` 报 `code 8000096 "A manifest field was expected in the request body"`。完整 multipart 顺序：`metadata`（`{"deployment_type":"direct"}`）→ `manifest`（hash 映射）→ 文件本体。若只想确认部署状态，`GET /accounts/{acct}/pages/projects/{name}/deployments` 查 `latest_deployment.url` 即可。

> ⛔ **manifest 文件 key 必须带前导 `/`（生产实证，漏了就根域名 404）**：manifest 的键必须是**以 `/` 开头的路径**（`{"/index.html": "<sha256>"}`），且 multipart 文件表单字段名也用 `/index.html`（`-F "/index.html=@index.html"`）。若写成 `{"index.html": sha}`（漏斜杠），Cloudflare 把文件 key 存成 `"index.html"`，根路由 `/` 匹配不到 → 浏览器访问 `https://<name>.pages.dev/` 得 **HTTP 404**（部署 API 仍 `success:True`、url 照给，极具迷惑性）。诊断：`GET .../deployments/{id}` 看 `result.files` 的 key 是否带 `/` 前缀。**部署健康唯一可靠验证 = Cloudflare API 的 `latest_deployment.latest_stage.status == success` + files key 带 `/`**；对外 curl/浏览器访问 pages.dev 出现 HTTP 500 / SSL 握手失败 / HTTP 000 往往是本机到边缘网络不稳，不能当部署失败判断，交浏览器验证。

> ⛔ **证信用 env var 别写**字面**占位（生产实证踩坑）**：手动 curl 时把认证头写成字面 `"Authorization: Bearer ***"`（或手敲 `***`）会返回 `code 9106 "Missing X-Auth-Key, X-Auth-Email or Authorization headers"` / `Authentication failed`——必须引用真实 env var（`"Authorization: Bearer ${CLOUDFLARE_API_TOKEN}"`）。注意：沙箱回显会把 `${CLOUDFLARE_API_TOKEN}` 显示成 `$CLOUD...EN`、把真实 token 显示成 `***`，这是**显示层遮罩**，磁盘/实际执行的脚本内容是正确的——不要因此误以为脚本写错而改成字面 `***`（改了就真 401）。判断标准看 token 到底有没有生效：部署 API 返回 `success:True` 即正确。
>
> ⛔ **但 write_file/patch 偶发把 token 变量名「写坏」在磁盘（生产实证，与上面显示遮罩不同）**：某些脚本 `read_file` 后发现磁盘上变量引用被截断成 `$CLOUD...KEN` 之类残缺名，导致同一逻辑这次 curl 报 9106、上次却正常。**别再和遮罩搏斗**——改用最可靠路径：在 Python 里直接从你的凭证文件（如 `cf_env.sh`，每行 `export KEY=value`）解析 token：`dict(l.strip().replace('export ','',1).split('=',1) for l in open('<YOUR_CF_ENV_FILE>'))`，用 urllib/requests 以 dict-header 发请求，完全不经过 shell 变量插值。

## 变更 Top100 取值类目（报告改造流程）

> 用户要求「换个类目」时（如 `<旧类目NODE> <旧类目名>` → `<新类目NODE> <新类目名>`），不是只改一个字段——**所有数据依赖段都要重取重写**，否则报告会出现旧类目数字与新类目标题混搭。

1. **重取数据**：对 newNode 重跑 `category_report`（Top100/stats）、`category_trend`（SalesCount/AvgPrice/新品占比）、`category_keywords`。重新挑该类目下的**直发梳/品类代表 ASIN** 拉 `product_reviews` 换掉好评差评样本。
2. **逐段重写数据依赖段**：市场容量（Top100/CR3/CR5/Amazon自营/均价）、市场趋势（生命周期阶段/**旺季淡季**/增速）、市场竞争（占比数字）、TOP品牌表（#1品牌与份额名次全变）、产品功能/成本、好评差评频次（样本数+话题占比）、以及四/五大部分里引用的差评#1/#2痛点、SWOT判断。
3. **全局检索残留旧类目**：生成后 grep HTML 的旧 `NodeID`、旧 #1 品牌名、旧样本数（如 `153 条`→`187 条`、`84 条`→`73 条`），逐个清理。注意「相对旧类目的对比句」（如"护城河弱于热风直发梳"）可保留作为上下文，但要确认非纯旧数据。
4. **口径说明**：报告中用 `<div class=note>` 注明"XX产品在亚马逊无独立节点，按要求归入 <newNode> Top100 取值；该类目包含 XX 细分产品"。换类目前先跟用户确认口径。

## 交付自检清单

- [ ] 五大部分 + 全部小节标题存在
- [ ] 产品名中英双语（产品名/关键词 + 中文翻译）
- [ ] 线上（Sorftime）/ 线下（公开信息标注链接）分开展示
- [ ] 每个市场数据有来源标注（Sorftime / 公信息 / 估算）
- [ ] 默认蓝灰商务风，纯 CSS 无 ECharts
- [ ] 若报告含目录导航，确认每节 `<div class="section-title">` 有唯一 `id` 且目录 `href` 与之对应（锚点注入别用朴素 replace 覆盖，见 `references/report-generation-architecture.md`）
- [ ] 页脚「分析负责人：<署名>」（请使用者自定义；默认可留空或填自己的名字）
- [ ] 数据来自真实输出（无编造）；好评/差评 TOP20 为真实频次或明确降级说明
- [ ] **曲线分开**：销量/销额是**两幅独立**柱状图非混排；**消费者原声每条都带 `class="cn"` 中译**（review 结构含 stars/en/cn 三段）
- [ ] **⚡ 生成后必跑标签配对 audit**（不止 5 章节齐全检查）：`<section>/<div>/<table>/<tr>/<td>/<th>/<ul>/<ol>/<li>/<b>/<span>` 各 `open==close`。否则一个丢 `</li>` 的小 bug（常因字符串字面量里误加尾随 `;` 导致，如 `'...。');` 少了 `</li>`）会静默破坏整节排版
- [ ] **⛔ 校验完整 CSS 在 `<style>` 内**（否则页面显示"源码标签"，见下方坑）：用 `re.findall(r'<style>(.*?)</style>', h, re.S)` 统计所有 `<style>` 块总长，**完整报告应数千字节**（纯样式几千 B）；若只有几百字节（如 700B）说明 CSS 拼错位置掉到 `<body>` 当裸文本了。同时确认 `</style>` 位置在 `<body>` 之前。

### ⛔ 坑：CSS 拼到 `</style>` 之后 → 页面显示"源码标签"（生产实证）
**症状**：浏览器/本地双击打开报告，显示一堆 `<div>` `<section>` 裸标签、完全无排版，像"源代码"；**不是乱码、不是编码、不是服务器**（服务器 `Content-Type: text/html; charset=utf-8` 正常）。
**根因**：多段字符串拼接 HTML 时，若 `CSS` 变量被拼进了字符串里**已存在的第一个 `</style>` 之后**（而非 `</style>` 之前），完整 CSS 就会掉进 `<body>` 当纯文本丢弃，只剩 `<head>` 里一小段（如目录样式）。从而正文所有 `class` 无样式 → 无排版 → 显示源码。
**修复**：把完整 `CSS` 插入 `<head>` 内 `<style>` 标签的**开头**——`html_head = '''...<style>\n''' + CSS + '''...toc...\n</style></head><body>'''`。生成后按上面自检项验证 `<style>` 内总长。
- [ ] 已部署并返回可用 URL（如用户要求）

## ⛔ 凭据卫生

每次产出物（HTML/data json/脚本）不得硬编码真实 API key、token、Account ID、邮箱。Cloudflare 证信用 env var（cf_env.sh）。分享/推送前对产出目录做一次凭据扫描（`ghp_`/`cfut_`/`?key=`/@gmail 等特征）。

## 🚀 公开分享 / GitHub 发布前脱敏清单

> 要发布 skill / 脚本到**公开 GitHub** 时，逐项自查——比"凭据扫描"更广，后者查不到内部路径泄露：

1. **改写内部绝对路径引用**：正文里形如 `python3 <LOCAL_PATH>/mcp_client.py ...`、`source <LOCAL_PATH>/cf_env.sh`、`/tmp/<your_deploy_dir>` 等全是**本机专属**，public 后别人照做即失败，还引导暴露内部文件——统一改为 `<YOUR_...>` 占位。
2. **剥离未随包发布的内部依赖**：如一个内含 API key 的 Direct Client 脚本不发布，SKILL 却引用它 → 改写为通用命令占位（「请接入你自己的 Sorftime MCP / Direct Client」）。
3. **确认排除 session 专属参考报告**：泛化失败的首次执行实证、内部抓取检查脚本等**用户私有产物**不应随包发布 → 从引用处一并删，别只删文件留着悬空链接。
4. **生成器脚本常是"品类专用"非通用模板**：docstring（如"某品类×某国"）、固定的数据常量、正文数字全是该品类硬编码——原样 public 等于泄品类报告。要发通用性，需先参数化/去品类化（产品名/国家/类目/NODE 做成变量），或只发 SKILL + 通用组件、脚本留本地。
5. **发布前先问用户三件事**：(a) 明确要发哪个文件集；(b) 哪个 session 专属报告要排除；(c) GitHub 认证权限——受限 PAT（如仅授一个 repo 的 fine-grained token）**不能新建/推其他 repo（403）**，需用户提供可建仓库的 token 或手动建好仓库名。发布是公开不可逆操作，先确认再动手。
6. **待发布物 vs 本地必须排除**：`state.db/logs/memories/.npm/.wrangler`/本地脚本/含 key 的凭证文件 一律不入库，用 gitignore 或只在独立发布目录组装。
7. **无 `gh`/git 时用 GitHub Contents API 直推**：若环境没装 `gh`、也不想在发布目录 git init，可用 REST API 逐个上传文件（见 `references/github-publish-contents-api.md`）。**先探测 PAT 权限**再动手：
   - `GET /user` 确认账号对得上；`GET /repos/{owner}/{repo}` 返回 200 = 有访问权，403/404 = 受限 PAT 无该 repo 权限（用户需把新 repo 加进 fine-grained token 的 Repository access，或手动建好仓库）。
   - **写权限探测**：`PUT /repos/{owner}/{repo}/contents/_perm_test.txt` 传临时内容，返回 201 = 有写权限，随后 DELETE 清理。**这一步必须做**——受限 PAT 可能只授 read（能 GET 仓库、不能 PUT 文件），直接推会中途失败。
   - 发布是公开不可逆操作：先把文件脱敏/排除清单跑完，再 push。

> ⛔ **脱敏是对 SKILL 自身做一次（把自己当待发布物）**：发布前把上面清单逐项套用到 SKILL 本体 + references。生产实证两个易漏项：
> - **内部 callout 纠错史也是指纹**：SKILL 里为「记住教训」写的批评史片段（"用户原话批评过两次"）、隐藏的内部参考报告 URL（如 `xxx.pages.dev`）、历史默认署名、以及具体品类名作例子——这些虽非真实凭据，但一发布就暴露你的私有部署/历史/习惯，**外人看到也一头雾水**。一律泛化为 `占位符`（`<YOUR_REFERENCE_REPORT>` / `<署名>` / `<产品名>×<国家>` / `OWNER/REPO`）。判断标准：这条信息是否**只对你本机有意义**？是→占位或删。
> - **别和破坏性命令保护硬碰：选择性组装发布目录**。待排除文件（首次执行实证、内部检查脚本、含 key 脚本）位于 skills 托管目录时，`rm` 可能被权限护栏拦下（超时未同意=未授权，不要重试/换命令硬删）。**正确做法**：新建独立发布目录，用 `cp` **只复制白名单文件**进去（SKILL.md + 泛化后的 references + 通用脚本），待排除文件留在原位即可——发布物 = 发布目录内容，与本地仓库解耦，天然不泄。这也符合清单第 6 条「只在独立发布目录组装」。

### ⚠️ patch 被拒：escape-drift 误报
对含引号/反斜杠的文件（markdown 里的 `"..."` 或代码里的转义序列）做 `patch` 时，若 new_string 里写了 `\"` 字面转义（如 `\"Hot-Air\"`），会触发 **"Escape-drift detected"** 拒绝，提示 old/new 含字面 `\"` 但文件里没有。修复：**先用 read_file 读原文，old_string/new_string 按原样传普通 `"`，不要加反斜杠**。
