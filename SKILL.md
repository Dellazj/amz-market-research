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
  定位：与 zach-product-research（四件套）/ amazon-category-report（17章类目报告）互补，本 Skill 聚焦「角色设定的产品×国家市场调研」。
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
6. **输出形式**：单文件蓝灰商务风 HTML（纯 CSS，无 ECharts），可部署 Cloudflare Pages。

## 报告结构（五大部分，固定框架）

### 第一部分：市场概况
| 小节 | 内容要点 |
|------|---------|
| 市场容量 | 线上+线下年销售额/销量、头部卖家市场份额分布、市场集中度 CR3/CR5 |
| 市场趋势 | 生命周期阶段+判定依据+品类平均生命周期长度；近3年增长率及未来3年预测；旺季/淡季（可加「近12个月销量/销售额曲线」，纯 CSS 做法见 `references/pure-css-trend-curves.md`） |
| 市场竞争 | 线上/线下竞争格局 |
| TOP公司 | 头部品牌：所属国家/成立年份/公司背景/年收入/份额占比/核心竞争力（**表格**） |
| 波特五力模型 | 五力框架分析线上/线下现状与应对策略（**三列：线上现状/线下现状/应对策略**） |

> 📐 用户说「参考 B 报告优化 A 报告」时，结构对齐清单（emoji 标题 + section-sub + KPI四卡 + 头部卖家份额bar + 线上/线下拆解表 + 市场趋势①②③④ + 品牌线上%/整体%两列 + 波特五力三列）见 `references/report-generation-architecture.md` 末尾「参考 X 报告优化 Y 报告」节；跨片段 `sec()` 签名漂移坑同见该文件。

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
| 受众好评 | TOP20 好评按频次占比降序 |
| 受众差评 | TOP20 差评按频次占比降序 |

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

用户已多次产出参考基准 `market-research-styler.pages.dev`，**首版齐全度不够会被判「报告不全」**。生成任何调研报告前，先对照本 skill 的 `references/report-completeness-standard.md` 核对达标项（⭐=首版易漏，务必补齐）：
- 市场概况：CR3**产品/品牌/卖家三指标**、#1单品占比、高评分/高评论占比、线上vs线下拆分表、**新品销量占比**、月销额**换算人民币**
- 产品介绍：卖点**分类表**、款式/功能/线上价/**1688实测出厂成本**表
- 受众分析：详细画像表、购物习惯表、互补产品、**受众常见问题表**
- 开发策略：认证表含监管机构列、专利风险**具体品牌**、**风险点与应对表**
- 每章开头 src-bar 标来源；重要洞察用 callout/insight-box 强调非平铺

关键提取技术（一次 `category_report` 即得 CR3三share + Amazon自营 + 高评分/高评论share；新品占比=解析 online_date≤90天；出厂成本用 `ali1688_similar_product` 真实价格）——详见该 reference 文件。

## 数据采集工作流（Sorftime MCP）

> ⛔ **Sorftime MCP 服务器可能超时，优先用 Direct Client**（SSE 协议、snake_case 参数）。工具名用短名：`product_detail` / `product_reviews` / `category_report` / `category_search_from_product_name` / `product_traffic_terms` / `keyword_detail` 等。参数名为 snake_case（如 `amz_site` 不是 `amzSite`，`review_type` 不是 `reviewType`）。

### 类目定位 + 市场数据
> ⛔ **类目定位坑（首次执行实证）**：`category_search_from_product_name` 常把产品归到**宽泛父类目**（如 straightener brush → Hair Brushes 均价$11，错误）。**先核对返回均价/价格带是否吻合**（直发梳主流 $30-70，均价绝不可能 $11）；不吻合时用 `category_name_search` 换更精确的细分类目名（如 "Hot-Air Hair Brushes" → Node 11058221）。

| 数据 | 工具（短名） | 参数 |
|------|------------|------|
| 定位细分类目(初筛) | `category_search_from_product_name` | `product_name`, `amz_site` |
| 确认精确类目 | `category_name_search` | `category_name`(精确子类目名), `amz_site` |
| Top100榜单 | `category_report` | `node_id`, `amz_site`（输出大→重定向文件+Python解析） |
| 类目趋势 | `category_trend` | `node_id`, `trend_index=SalesCount` 等 |
| 类目关键词 | `category_keywords` | `node_id` |
| 产品详情 | `product_detail` | `asin`, `amz_site` |
| 评论 | `product_reviews` | `asin`, `amz_site`, `review_type`(Both/Positive/Negative) |
| 反查关键词 | `product_traffic_terms` | `asin` |
| 关键词详情 | `keyword_detail` | `keyword`（周搜索量/CPC/趋势） |
| 供应商成本 | `ali1688_similar_product` / `ali1688_product_search` | `search_name` |
| 产品趋势 | `product_trend` | `asin`, `product_trend_type` |

> ⛔ **类目趋势没有直接月销额（SalesAmount）**：`category_trend` 的 `trend_index` 传 `"SalesAmount"` 会报错（有效枚举只有 SalesCount/AvgPrice/各 Share 占比，**没有原始总销额**）。要「近12个月销售额曲线」时：分别拉 `SalesCount`（月销量）与 `AvgPrice`（当月均价），`月销额 = 月销量 × 当月均价` 计算；此列为**估算**，必须在图上/说明里用 `tag-est` 标注（销量与均价本身仍是 Sorftime 实时真数据，只有相乘这一步是推算）。

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

完整 CSS 组件库（蓝灰商务风，纯CSS无ECharts）：`kpi-grid/kpi-card`、`bar-item/bar-track/bar-fill`、`insight-box`、`verdict-box`、`table-wrap`、`detail-card`、`grid-2`、`tag-*`。默认主题：`--blue #2563eb`。每个章节用 `<section>` + `div.section-title`；每个市场数据附带来源角标（Sorftime / 公开信息 / 估算）。

> ⛔ **生成器脚本：别用一个大 f-string 拼 HTML**
用 Python 脚本生成单文件 HTML 报告时，**不要 `HTML = f"""...{CSS}...{section(...)}..."""` 一个巨型 f-string**——CSS 里的字面大括号（`.bar-fill{...}`）和嵌套 f-string 会把外层解析器搅乱，报 `SyntaxError: f-string: single '}' is not allowed`。可靠做法（本 skill 生产证实）：
- CSS 存成普通（非 f）字符串变量，HTML 用**字符串拼接 `+`** 组装，而**不是 f-string**。
- kpi/bar/review/section 等小组件函数内部用 `%` 格式化（`'<div class="kpi-card %s">...' % (cls, ...)`），组件函数本身自洽、不含 CSS 大括号，安全。
- 若 HTML 里个别处要插变量（如 `style="width:{pct}%"`），用拼接或 `%` 传参，不要写进 f-string。

### ⛔ 英文评论原声里的撇号会炸掉单引号字符串（生产实证，必踩）
好评/差评**原声英文**几乎必然含缩写撇号：`I've` / `don't` / `didn't` / `it's`。若 append 行用外层单引号 `s.append('...I've...')`，撇号会**提前终止字符串**报 `SyntaxError: unterminated string literal`（报错行号常指到实际非问题行，难定位）。修复首选：
- **用 Unicode 转义写撇号**：`I\u2019ve`、`don\u2019t`（保持外层单引号，`\u2019` 是右单引号撇号，HTML 显示为 `'`）。
- 或整行改用外层双引号 `s.append("...I've...")`，此时内嵌的英文双引号（原文引用 `"..."`）需转义为 `\"`——更麻烦，`\u2019` 更省。
- **预防**：把英文原声统一在开头就用 `\u2019` 代替所有撇号。写完脚本后先 `python3 file.py` 编译验证（生成前必跑）。

### 多片段生成架构 + 锚点/目录/标签审计
大报告（5大板块25小节）别全塞进一个生成脚本——拆成 `part{N}.py`（各产出一个 `S{N}` HTML 字符串）+ 主拼接脚本（`importlib` 加载拼接）。目录锚点 id 注入、TOC 样式、生成后标签配对 audit 等**已验证模式**详见 `references/report-generation-architecture.md`。

## 部署（Cloudflare Pages）

首选用 **amazon-category-report** skill 自带的 `scripts/deploy_report.py`（Cloudflare Pages 全自动）。证信用 env var（cf_env.sh 已配置 CF_API_TOKEN）。
若手动 `wrangler pages deploy`，注意：
- **单文件坑**：`wrangler pages deploy report.html` 会报 `ENOTDIR`（wrangler 要求传**目录**）。需先把 HTML 复制为目录里的 `index.html` 再部署。
- **Pages 项目不存在时须先 create**：对**新项目名**手动直发会报 `The Pages project "<name>" does not exist`。先 `wrangler@latest pages project create <name> --production-branch main` 再 deploy。
- ⛔ **每个品类/报告用语义专属的项目名**（如 `curling-iron-research`），**绝不复用/覆盖其它项目的名字**，否则链接混乱 + 浏览器缓存错位（详见 `references/report-generation-architecture.md`）。
- 生产 URL 固定为 `https://<name>.pages.dev`（创建后首个部署生效）；临时 hash URL 刚部署时 SSL 可能握手失败（curl HTTP 000），等缓存传播或直接用生产域名验证。

## 变更 Top100 取值类目（报告改造流程）

> 用户要求「换个类目」时（如 11058221 Hot-Air Brushes → 11058261 Straighteners），不是只改一个字段——**所有数据依赖段都要重取重写**，否则报告会出现旧类目数字与新类目标题混搭。

1. **重取数据**：对 newNode 重跑 `category_report`（Top100/stats）、`category_trend`（SalesCount/AvgPrice/新品占比）、`category_keywords`。重新挑该类目下的品类代表 ASIN 拉 `product_reviews` 换掉好评差评样本。
2. **逐段重写数据依赖段**：市场容量、市场趋势、市场竞争、TOP品牌表、产品功能/成本、好评差评频次、以及四/五大部分里引用的差评痛点、SWOT判断。
3. **全局检索残留旧类目**：生成后 grep HTML 的旧 `NodeID`、旧 #1 品牌名、旧样本数，逐个清理。
4. **口径说明**：报告中用 `<div class=note>` 注明商品的取值口径。

## 交付自检清单

- [ ] 五大部分 + 全部小节标题存在
- [ ] 产品名中英双语（产品名/关键词 + 中文翻译）
- [ ] 线上（Sorftime）/ 线下（公开信息标注链接）分开展示
- [ ] 每个市场数据有来源标注（Sorftime / 公开信息 / 估算）
- [ ] 默认蓝灰商务风，纯 CSS 无 ECharts
- [ ] 若报告含目录导航，确认每节 `<div class="section-title">` 有唯一 `id` 且目录 `href` 与之对应
- [ ] 页脚「分析负责人：Della」（可自定义/留空）
- [ ] 数据来自真实输出（无编造）；好评/差评 TOP20 为真实频次或明确降级说明
- [ ] **⚡ 生成后必跑标签配对 audit**：`<section>/<div>/<table>/<tr>/<td>/<th>/<ul>/<ol>/<li>/<b>/<span>` 各 `open==close`
- [ ] **⛔ 校验完整 CSS 在 `<style>` 内**（否则页面显示"源码标签"，见下方坑）：用 `re.findall(r'<style>(.*?)</style>', h, re.S)` 统计所有 `<style>` 块总长，**完整报告应数千字节**；若只有几百字节（如 700B）说明 CSS 拼错位置掉到 `<body>` 当裸文本了。同时确认 `</style>` 位置在 `<body>` 之前。
- [ ] 已部署并返回可用 URL（如用户要求）

### ⛔ 坑：CSS 拼到 `</style>` 之后 → 页面显示"源码标签"（卷发棒报告生产实证）
**症状**：浏览器/本地双击打开报告，显示一堆 `<div>` `<section>` 裸标签、完全无排版，像"源代码"；**不是乱码、不是编码、不是服务器**（服务器 `Content-Type: text/html; charset=utf-8` 正常）。
**根因**：多段字符串拼接 HTML 时，若 `CSS` 变量被拼进了字符串里**已存在的第一个 `</style>` 之后**（而非 `</style>` 之前），完整 CSS 就会掉进 `<body>` 当纯文本丢弃，只剩 `<head>` 里一小段（如目录样式）。从而正文所有 `class` 无样式 → 无排版 → 显示源码。
**修复**：把完整 `CSS` 插入 `<head>` 内 `<style>` 标签的**开头**——`html_head = '''...<style>\n''' + CSS + '''...toc...\n</style></head><body>'''`。生成后按上面自检项验证 `<style>` 内总长。
**参见**：`examples/curling-iron-report.html`（卷发棒正式报告样张）。

## ⛔ 凭据卫生

每次产出物（HTML/data json/脚本）不得硬编码真实 API key、token、Account ID、邮箱。Cloudflare 证信用 env var。分享/推送前对产出目录做一次凭据扫描（`ghp_`/`cfut_`/`?key=`/@gmail 等特征）。

## 🚀 公开分享 / GitHub 发布前脱敏清单

> 用户要发布 skill / 脚本到**公开 GitHub** 时，逐项自查——比"凭据扫描"更广，后者查不到内部路径泄露：

1. **删除/改写内部绝对路径引用**（如 `python3 ~/mcp_client.py`、`source <path>/cf_env.sh`、`<workdir>/deploy` 等本机专属路径），public 后别人照做即失败，还引导暴露内部文件。
2. **剥离未随包发布的内部依赖**：`mcp_client.py`（内含 API key）不发布，SKILL 却引用它 → 改写为通用命令占位。
3. **确认排除 session 专属参考报告**：不发布的 reference 要从 SKILL 引用处一并删，别只删文件留着悬空链接。
4. **生成器脚本常是"品类专用"非通用模板**：docstring、数据常量、正文数字全是该品类硬编码——原样 public 等于泄品类报告。要发通用性需先参数化/去品类化，或只发 SKILL + 通用组件、脚本留本地。
5. **发布前先问用户三件事**：(a) 明确要发哪个文件集；(b) 哪个 session 专属报告要排除；(c) GitHub 认证权限（受限 PAT 可能不能建/推新 repo，需用户提供或手动建好仓库名）。
6. **待发布物 vs 本地必须排除**：`state.db/logs/memories/.npm/.wrangler`/旧品类报告/`mcp_client.py`/`cf_env.sh` 一律不入库。
7. **无 `gh`/git 时用 GitHub Contents API 直推**（见 `references/github-publish-contents-api.md`）。**先探测 PAT 权限**再动手：`GET /user` 确认账号对得上；访问仓库返回 200 = 有权限，403/404 = 受限；**写权限探测**：`PUT .../contents/_perm_test.txt` 返回 201 = 有写权（随后 DELETE 清理）。发布是公开不可逆操作，先脱敏再 push。

### ⚠️ patch 被拒：escape-drift 误报
对含引号/反斜杠的文件（markdown 里的 `"..."` 或代码里的转义序列）做 `patch` 时，若 new_string 里写了 `\"` 字面转义，会触发 **"Escape-drift detected"** 拒绝。修复：**先用 read_file 读原文，old_string/new_string 按原样传普通 `"`，不要加反斜杠**。
