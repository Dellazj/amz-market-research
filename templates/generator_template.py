#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
amz-market-research — 通用「产品 × 国家」亚马逊市场调研报告生成器（模板）
======================================================================

这是一个【完全参数化的】生成器模板：产品名 / 目标国家 / 类目 NodeID /
货币 / 语言 / 认证要求全部由 CLI 传入或顶部配置，不含任何单一品类的硬编码。

用法示例
--------
python3 generator_template.py --product "Straightener brush" --product_cn "直发梳" \
    --country US --site US --node <YOUR_NODE_ID> --currency '$' \
    --report out/us_straightener_brush.html

参数
----
--product …… 产品名（英文，用于数据检索与标题）
--product_cn …… 产品名（中文，用于中文报告）
--country ……… 目标国家（US/CA/DE/FR/…，中英报告与认证表用）
--site ………… 亚马逊站点简称（AMZ_SITE，与 Sorftime 站点一致）
--node ………… 亚马逊细分类目 NodeID（整型）
--currency …… 金额符号（'$'/'€'/'£'/…）
--lang …… 站点主语言（en/fr/de, 默认 en；法语差评 tag 用）
--report …… 输出 HTML 路径
--sign …… 页脚/hero 署名（默认留空，随使用者指定）

依赖
----
- 数据源：你自己的 Sorftime MCP / Direct Client（见 SKILL.md「数据接入」节）。
  本模板只定义 DATA 接口与占位，实际抓取请你接入自己的 Client。
- 纯 Python stdlib 即可运行；无第三方依赖。

完整方法论见 SKILL.md 及 references/ 下各文件：
  report-completeness-standard.md（六大部分全量 + 两条硬性要求）
  report-generation-architecture.md（多片段架构 + 锚点/目录注入 + 标签配对 audit）
  pure-css-trend-curves.md（销量/销额两幅独立曲线，纯 CSS）
运行完请务必重跑「标签配对 audit」。
"""
import argparse
import re
import sys

# ─────────────────────────── 0. 参数 ───────────────────────────
def parse_args():
    p = argparse.ArgumentParser(description="通用产品×国家市场调研报告生成器")
    p.add_argument("--product", required=True, help="产品名（英文）")
    p.add_argument("--product_cn", required=True, help="产品名（中文）")
    p.add_argument("--country", default="US", help="目标国家代码")
    p.add_argument("--site", default="US", help="亚马逊站点简称")
    p.add_argument("--node", required=True, help="类目 NodeID")
    p.add_argument("--currency", default="$", help="金额符号")
    p.add_argument("--lang", default="en", help="站点主语言")
    p.add_argument("--report", required=True, help="输出 HTML 路径")
    p.add_argument("--sign", default="", help="页脚署名（可留空）")
    return p.parse_args()

# ─────────────────────────── 1. 数据接入（占位）────────────────
# ⛔ 请接入你自己的 Sorftime MCP / Direct Client。SKILL 不随包发布含 key 的
#    client 脚本，这里只定义你要实现的数据接口契约。
def fetch_data_args(node, site, product):
    """返回一个 dict，key 固定，value 是你从 Sorftime 抓取的实时数据。
    对应 SKILL 各工具：category_report / category_trend / category_keywords /
    product_reviews / keyword_detail / ali1688_similar_product 等。"""
    raise NotImplementedError(
        "接入你自己的 Sorftime MCP / Direct Client（见 SKILL.md「数据接入」节），"
        "把下面的 D = {...} 填成真实数据。"
    )
    # 示例契约（务必替换成真实抓取值）——这就是你要实现的接口形状：
    D = {
        "top100_month_sales": 0,        # Top100 月销量（件）
        "top100_month_amount": 0.0,     # Top100 月销额
        "avg_price": 0.0, "median_price": 0.0,
        "cr3_product": 0.0, "cr3_brand": 0.0, "cr3_seller": 0.0,
        "amazon_owned": 0.0,            # Amazon 自营销量占比
        "top1_share": 0.0,
        "high_rating_share": 0.0, "high_comment_share": 0.0,
        "new_product_share": 0.0,       # 上架≤3月销量占比
        "top_brands": [],               # [{"name", "country", "founded", "revenue", "share", "core"}]
        "sales_trend": [],              # [{"month":"25/09","vol":int,"price":float}] 近12月
        "reviews_pos": [],              # [{"star","en","cn"}] 好评原声(中译)
        "reviews_neg": [],              # [{"star","en","cn"}] 差评原声(中译)
        "keywords": [],                 # [{"kw","sv","cpc","rank"}]
        "cost_1688": {"min": 0.0, "max": 0.0},  # 1688 出厂成本区间(当地币)
        "cert_requirements": [],        # [{"cert","agency","period","cost","note"}]
    }
    return D

# ─────────────────────────── 2. 组件函数（通用）────────────────
CSS = """
:root{--blue:#2563eb;--blue-d:#1e40af;--green:#16a34a;--red:#dc2626;--amb:#d97706;
      --gray-100:#f1f5f9;--card:#ffffff;--brd:#e2e8f0;--txt:#0f172a;}
body{font-family:-apple-system,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif;
     color:var(--txt);background:#f8fafc;margin:0;line-height:1.7}
.wrap{max-width:1100px;margin:0 auto;padding:28px}
.hero{background:linear-gradient(135deg,var(--blue),var(--blue-d));color:#fff;
      border-radius:16px;padding:36px 40px;margin-bottom:24px}
.hero h1{margin:0 0 8px;font-size:28px}
.kpi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;margin:20px 0}
.kpi{background:var(--card);border:1px solid var(--brd);border-radius:12px;padding:16px 18px}
.kpi .k{color:#64748b;font-size:13px}.kpi .v{font-size:22px;font-weight:700;color:var(--blue-d)}
.section-title{display:flex;align-items:center;gap:10px;background:var(--card);
      border:1px solid var(--brd);border-left:5px solid var(--blue);
      border-radius:10px;padding:14px 18px;margin:26px 0 14px;font-size:20px}
.section-title .no{background:var(--blue);color:#fff;border-radius:7px;
      padding:3px 10px;font-size:14px}
.sub-title{font-size:17px;font-weight:700;margin:20px 0 10px;color:var(--blue-d);
      border-bottom:2px solid var(--gray-100);padding-bottom:6px}
table{width:100%;border-collapse:collapse;margin:12px 0;background:var(--card);
      border:1px solid var(--brd);border-radius:10px;overflow:hidden}
th{background:#f1f5f9;text-align:left;padding:10px 12px;border-bottom:1px solid var(--brd)}
td{padding:10px 12px;border-bottom:1px solid var(--brd)}
.bar-item{display:flex;align-items:center;gap:10px;margin:8px 0}
.blabel{width:72px;color:#64748b;font-size:13px;text-align:right;flex-shrink:0}
.btrack{flex:1;background:var(--gray-100);border-radius:6px;height:26px;position:relative}
.bfill{height:26px;border-radius:6px}
.bfill.blue{background:var(--blue)}.bfill.rd{background:var(--red)}
.bfill.amb{background:var(--amb)}.bfill.green{background:var(--green)}
.bval{width:120px;font-size:13px;font-weight:600;flex-shrink:0}
.src-bar{font-size:12px;color:#64748b;background:var(--gray-100);
      border-radius:6px;padding:4px 10px;display:inline-block;margin-bottom:10px}
.insight-box{border:1px solid var(--blue);border-left:4px solid var(--blue);
      background:#eff6ff;border-radius:10px;padding:14px 18px;margin:14px 0}
.verdict-box{border:1px solid var(--green);border-left:4px solid var(--green);
      background:#f0fdf4;border-radius:10px;padding:14px 18px;margin:14px 0}
.callout{border:2px solid var(--amb);background:#fffbeb;border-radius:12px;
      padding:16px 20px;margin:16px 0}
.review{margin:10px 0;padding:12px 14px;border:1px solid var(--brd);border-radius:10px;background:var(--card)}
.review .stars{color:var(--amb);font-size:14px}
.review .en{font-style:italic;margin:6px 0}
.review .cn{color:var(--blue-d);font-size:13px}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:720px){.grid-2{grid-template-columns:1fr}}
.toc{background:var(--card);border:1px solid var(--brd);border-radius:14px;padding:22px 28px;margin:20px 0}
.toc a{text-decoration:none;color:#334155}
html{scroll-behavior:smooth}.section-title{scroll-margin-top:16px}
footer{margin-top:34px;padding-top:14px;border-top:1px solid var(--brd);
      color:#64748b;font-size:13px;text-align:center}
.badge{display:inline-block;background:var(--gray-100);border-radius:20px;
      padding:2px 10px;font-size:12px;color:#475569}
"""
def sec(no, title, src, body, ssub=""):
    s = '<div class="section-title"><span class="no">%s</span>%s</div>' % (no, title)
    if ssub:
        s += '<div class="section-sub" style="color:#64748b">%s</div>' % ssub
    s += '<div class="src-bar">数据来源：%s</div>' % src + body
    return s
def note(t): return '<div class="callout">%s</div>' % t
def kpi(k, v): return '<div class="kpi"><div class="k">%s</div><div class="v">%s</div></div>' % (k, v)

# ⚠️ 锚点/目录 id 注入——别覆盖（见 report-generation-architecture.md）
def anchorize(body, no, sid):
    if ('<div class="section-title"><span class="no">%s</span>' % no) in body:
        body = body.replace('<div class="section-title"><span class="no">%s</span>' % no,
                '<div class="section-title" id="%s"><span class="no">%s</span>' % (sid, no), 1)
    return body

# ─────────────────────────── 3. 六大板块构建（占位骨架）────────
def build_sections(A, D):
    """按 SKILL「六大部分全量小节」搭建 HTML 字符串。方法见
    references/report-completeness-standard.md；这里给骨架，正文请逐节填充。"""
    S = {}
    # ---- 核心洞察（AI 总结，锚点 s0）----
    s0_ai = note("<b>核心洞察（AI 总结）</b><br>① 市场：Top100 月销 %s 件 / 月销额 %s%.0f 万，均价 %s%.2f，CR3产品 %.1f%%。<br>"
          "② 竞争：Amazon 自营 %.1f%%，新进入者机会看 CR3 高低。<br>"
          "③ 需求：好评/差评核心痛点 → 详见受众分析。<br>"
          "④ 机会：蓝海/差异化/入局策略 → 详见产品开发策略。<br>"
          "⑤ 结论：综合可行性评分见文末 SWOT/PEST。"
          % (fmat(D["top100_month_sales"]), A.currency, D["top100_month_amount"]/10000,
             A.currency, D["avg_price"], D["cr3_product"]*100, D["amazon_owned"]*100))
    S["s0"] = sec("★", "核心洞察", "Sorftime 实时 + 评论归纳", s0_ai,
                  "AI 生成的五率核心要点，正文各节展开")

    # ---- 第一部分：市场概况 ----
    s1 = []
    s1.append('<div class="kpi-grid">'
              + kpi("Top100 月销量", "%s件" % fmat(D["top100_month_sales"]))
              + kpi("Top100 月销额", "%s%.0f万" % (A.currency, D["top100_month_amount"]/10000))
              + kpi("平均客单价", "%s%.2f" % (A.currency, D["avg_price"]))
              + kpi("中位价", "%s%.2f" % (A.currency, D["median_price"]))
              + '</div>')
    s1.append(note("<b>市场集中度</b>：CR3产品 %.1f%% / 品牌 %.1f%% / 卖家 %.1f%%；Amazon自营 %.1f%%。%s"
          % (D["cr3_product"]*100, D["cr3_brand"]*100, D["cr3_seller"]*100,
             D["amazon_owned"]*100,
             "CR3 偏高→门槛高" if D["cr3_product"] > 0.4 else "CR3 偏低→新进入者有机会")))
    # ...市场趋势(①②③④)、市场竞争、TOP公司表、波特五力——见 report-completeness-standard
    #   「④近12月销量/销额曲线」务必两幅独立 bar 序列（见 pure-css-trend-curves.md）
    #         销量图 bfill blue/旺季 rd；销额图 bfill amb；销额=月销×月均价 + tag-est
    S["s1"] = sec("一", "📊 市场概况", "Sorftime 实时", "".join(s1),
                  "线上(Amazon %s Sorftime实时) 与 线下(公开信息) 分开呈现" % A.site)

    # ---- 第二部分：产品介绍 ----（卖点分类表 / 款式功能 / 1688实测成本表 / 使用场景）
    S["s2"] = sec("二", "🧾 产品介绍", "Sorftime + 1688 实测", "<div class='sub-title'>产品功能与款式</div><table>...</table>",
                  "线上 %s 与 线下 分开呈现" % A.site)

    # ---- 第三部分：受众分析 ----（画像/习惯/互补品/TOP问答/好评差评原声+中译）
    pos = "".join('<div class="review"><div class="stars">%s</div><div class="en">"%s"</div>'
                  '<div class="cn">—— %s</div></div>' % ("★"*int(r["star"]), r["en"], r["cn"]) for r in D["reviews_pos"])
    neg = "".join('<div class="review"><div class="stars">%s</div><div class="en">"%s"</div>'
                  '<div class="cn">—— %s</div></div>' % ("★"*int(r["star"]), r["en"], r["cn"]) for r in D["reviews_neg"])
    s3_voices = ('<div class="grid-2"><div><h4 style="color:var(--green)">■ 典型好评</h4>' + pos
                 + '</div><div><h4 style="color:var(--red)">■ 典型差评</h4>' + neg + '</div></div>')
    S["s3"] = sec("三", "👥 受众分析", "Sorftime 好评差评 + 公开信息", s3_voices,
                  "线上 %s 与 线下 分开呈现" % A.site)

    # ---- 第四部分：用户需求洞察 ----（痛点/金字塔/场景关联/画像匹配）
    S["s4"] = sec("四", "🎯 需求洞察", "评论归纳 + 公开信息", "<div class='insight-box'>产品机会聚焦…</div><table>…</table>",
                  "线上 %s 与 线下 分开呈现" % A.site)

    # ---- 第五、六部分：产品开发策略（认证/专利/风险/差异/蓝海/FABE/SWOT/PEST）
    S["s5"] = sec("五", "🚀 开发策略", "公开信息", "<div class='sub-title'>认证</div><table>…监管机构…</table>",
                  "线上 %s 与 线下 分开呈现" % A.site)
    S["s6"] = sec("六", "🚩 SWOT 与 PEST", "公开信息", "<div class='sub-title'>SWOT</div><table>…</table><div class='verdict-box'>综合可行性评分（满分10）：…</div>",
                  "线上 %s 与 线下 分开呈现" % A.site)
    return S

def fmat(n):
    return "{:,}".format(int(n))

# ─────────────────────────── 4. 组稿 + 输出 ────────────────────
def toc_links():
    items = [("s0","★","核心洞察"),("s1","一","市场概况"),("s2","二","产品介绍"),
             ("s3","三","受众分析"),("s4","四","需求洞察"),("s5","五","开发策略"),("s6","六","SWOT与PEST")]
    return ''.join('<li><a href="#%s"><span class="no">%s</span> <span class="t">%s</span></a></li>' % (sid,no,t) for sid,no,t in items)

def assemble(A, D, S):
    hero = ('<div class="hero"><h1>%s（%s）× %s 市场调研报告</h1>'
            '<div>数据来源：Sorftime 实时抓取 + 公开信息 | 汇报语言：中文</div></div>' % (A.product, A.product_cn, A.country))
    toc = '<div class="toc"><h3>📑 目录导航</h3><ol>%s</ol></div>' % toc_links()
    foot = ('<footer>分析负责人：<b>%s</b> · 数据来源：Sorftime ProductRequest · 生成日期 %s · '
            '本报告基于公开与第三方平台数据，供内部选品参考，不做任何投资/采购承诺</footer>'
            % (A.sign or "（未署名）", __import__("datetime").date.today().isoformat()))
    body = hero + toc
    for no, sid in [("★","s0"),("一","s1"),("二","s2"),("三","s3"),("四","s4"),("五","s5"),("六","s6")]:
        frag = S.get(sid, "")
        body += anchorize(frag, no, sid)
    full = "<!DOCTYPE html><html lang='zh'><head><meta charset='utf-8'>" \
           "<meta name='viewport' content='width=device-width,initial-scale=1'>" \
           "<title>%s × %s 市场调研</title><style>%s</style></head><body>" \
           "<div class='wrap'>%s%s</div></body></html>" % (A.product, A.country, CSS, body, foot)
    return full

def audit(html):
    odd = []
    for tag in ['div','section','table','tr','td','th','ul','ol','span']:
        o=len(re.findall(r'<%s[\s>]'%tag,html)); c=len(re.findall(r'</%s>'%tag,html))
        if o!=c: odd.append("%s:%d/%d" % (tag,o,c))
    return odd

def main():
    A = parse_args()
    D = fetch_data_args(A.node, A.site, A.product)   # 接入你自己的数据源
    S = build_sections(A, D)                          # 填充六大部分
    html = assemble(A, D, S)
    with open(A.report, "w", encoding="utf-8") as f:
        f.write(html)
    bad = audit(html)
    print("✅ 已生成 %s（%d 字节）" % (A.report, len(html)))
    if bad:
        print("⚠️ 标签配对不平衡：", ", ".join(bad), "—— 请修复再部署")
    else:
        print("✅ 标签配对 audit 通过")
    print("📌 交付前请对照 references/report-completeness-standard.md 核对六大部分全量小节；"
          "部署方法与凭证卫生见 SKILL.md 部署节 + 发布前脱敏清单。")

if __name__ == "__main__":
    main()
