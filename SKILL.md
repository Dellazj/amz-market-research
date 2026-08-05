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
6. **输出形式**：单文件蓝灰商务风 HTML（纯 CSS，无 ECharts），可部署 Cloudflare。

## 报告结构（五大部分，固定框架）

### 第一部分：市场概况
| 小节 | 内容要点 |
|------|---------|
| 市场容量 | 线上+线下年销售额/销量、头部卖家市场份额分布、市场集中度 CR3/CR5 |
| 市场趋势 | 生命周期阶段+判定依据+品类平均生命周期长度；近3年增长率及未来3年预测；旺季/淡季（可加「近12个月销量/销售额曲线」，纯 CSS 做法见 `references/pure-css-trend-curves.md`） |
| 市场竞争 | 线上/线下线上竞争格局 |
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

## 数据采集工作流（Sorftime MCP Direct Client）

> ⛔ **本机关键**：Sorftime MCP 服务器有时不可达（MCP 工具会超时），**优先使用 Direct Client**：
> 直接调用 Sorftime MCP 的 SSE 接口（`tools/call` 方法，snake_case 参数）。工具名用短名：`product_detail` / `product_reviews` / `category_report` / `category_search_from_product_name` / `product_traffic_terms` / `keyword_detail` 等（可用 `tools/list` 查询全部）。
> 参数名为 snake_case（如 `amz_site` 不是 `amzSite`，`review_type` 不是 `reviewType`）。

### 类目定位 + 市场数据
> ⛔ **类目定位坑（首次执行实证）**：`category_search_from_product_name` 常把产品归到**宽泛父类目**（如 straightener brush → Hair Brushes 均价$11，错误）。**先核对返回均价/价格带是否吻合**（直发梳主流 $30-70，均价绝不可能 $11）；不吻合时用 `category_name_search` 换更精确的细分类目名（如 "Straighteners" → Node 11058261）。

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

⛔ 完整 CSS 组件库见 amazon-category-report skill 的 `references/style_component_library.md`（蓝灰商务风，纯CSS无ECharts）：
- `kpi-grid/kpi-card`、`bar-item/bar-track/bar-fill`、`insight-box`、`verdict-box`、`table-wrap`、`detail-card`、`grid-2`、`tag-*`
- 默认主题：蓝灰商务风（--blue #2563eb，灰阶）

每个章节用 `<section>` + `div.section-title`；每个市场数据附带来源角标（Sorftime / 公开信息 / 估算）。

## 部署

生成的单文件 HTML 可用任意静态托管（Cloudflare Pages / GitHub Pages / Vercel 等）。

若用 Cloudflare Pages + `wrangler`，**凭据务必走环境变量**（如 `CLOUDFLARE_API_TOKEN` / `CLOUDFLARE_ACCOUNT_ID`），绝不硬编码进脚本或提交到仓库。

⛔ **`wrangler pages deploy` 单文件坑**：直接 `npx wrangler pages deploy report.html` 会报 `ENOTDIR`（wrangler 要求传**目录**）。手动直发时必须先把 HTML 复制为目录里的 `index.html`：
```bash
rm -rf ./deploy_dir && mkdir -p ./deploy_dir \
  && cp report.html ./deploy_dir/index.html \
  && CLOUDFLARE_ACCOUNT_ID=xxx CLOUDFLARE_API_TOKEN=xxx \
     npx --yes wrangler pages deploy ./deploy_dir --project-name <project>
```
成功输出含 `https://<hash>.<project>.pages.dev`。

## 变更 Top100 取值类目（报告改造流程）

> 用户要求「换个类目」时（如 11058221 Hot-Air Brushes → 11058261 Straighteners），不是只改一个字段——**所有数据依赖段都要重取重写**，否则报告会出现旧类目数字与新类目标题混搭。

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
- [ ] 页脚「分析负责人：Della」（可自定义/留空）
- [ ] 数据来自真实输出（无编造）；好评/差评 TOP20 为真实频次或明确降级说明
- [ ] 已部署并返回可用 URL（如用户要求）

## ⛔ 凭据卫生

每次产出物（HTML/data json/脚本）不得硬编码真实 API key、token、Account ID、邮箱。Cloudflare 等凭据一律走环境变量/密钥管理。分享/推送前对产出目录做一次凭据扫描（`ghp_`/`cfut_`/`?key=`/@gmail 等特征）以及**内部绝对路径**（如 `/opt/`、`/Users/<name>/`、`/tmp/`）检索。

## 🚀 公开分享 / GitHub 发布前脱敏清单

> 要发布 skill / 脚本到**公开 GitHub** 时，逐项自查——比"凭据扫描"更广，后者查不到内部路径泄露：

1. **删除/改写内部绝对路径引用**：正文里的 `python3 /opt/data/xxx.py ...`、`source /path/to/cf_env.sh`、`/tmp/deploy_dir` 等全是**作者机器专属**，public 后别人照做即失败，还引导暴露内部文件 → 改成相对路径或通用占位符（`./script.py`、`CLOUDFLARE_API_TOKEN`）。
2. **剥离未随包发布的内部依赖**：若脚本引用了含 API key 的本地客户端（如 MCP client），该文件不入库 → 将调用改写为通用命令/接口占位，或在 README 说明需用户自带凭据。
3. **确认排除 session 专属参考报告**：如某次执行排障留下的品类 first-run 实证文档，用户明确不发布 → **从 SKILL 引用处一并删**，别只删文件留着悬空链接。
4. **生成器脚本常是"品类专用"非通用模板**：脚本 docstring、数据常量、正文数字常硬编码了某个具体品类——原样 public 等于泄露该品类报告。要发通用性，需先参数化/去品类化，或只发 SKILL + 通用组件、脚本留本地。
5. **发布前先问用户三件事**：(a) 明确要发哪个文件集；(b) 哪个 session 专属报告要排除；(c) GitHub 认证权限——受限 fine-grained PAT 常只授一个 repo，**不能新建/推其他 repo（403）**，需用户提供可建仓库的 token 或手动建好仓库名。发布是公开不可逆操作，先确认再动手。
6. **待发布物 vs 本地必须排除**：进程目录/数据库/日志/凭据文件/旧品类报告等一律不入库，用 `.gitignore` 或只在独立发布目录组装后推送。
