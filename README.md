# amz-market-research

通用「**产品 × 国家**」亚马逊市场调研报告生成器（Hermes Agent Skill）。

输入任意产品名 + 目标国家，以「资深产品开发经理」视角产出结构化市场调研报告（单文件蓝灰商务风 HTML，纯 CSS、无 ECharts）。

## 用法

本目录是 Hermes Agent 的一个 Skill。安装后在对话中给出「产品 + 国家」即可触发，例如：

- 「直发梳 Straightener brush × 美国」
- 「空气炸锅 × 德国」
- 「电动牙刷 × 英国」

也可用包内参数化脚本 `templates/generator_template.py` 直接生成：

```bash
python3 templates/generator_template.py --product "Straightener brush" --product_cn "直发梳" \
    --country US --site US --node <YOUR_NODE_ID> --currency '$' \
    --report out/report.html
```

报告框架固定为五大部分：

| 部分 | 内容 |
|------|------|
| ① 市场概况 | 市场容量、市场趋势（含近12个月销量/销售额曲线）、市场竞争、TOP公司、波特五力 |
| ② 产品介绍 | 产品认知、产品功能、产品构成、使用场景 |
| ③ 受众分析 | 受众特征、习惯、购买、TOP20 好评/差评 |
| ④ 用户需求洞察 | 产品痛点、需求金字塔、场景-卖点关联、人群-卖点匹配 |
| ⑤ 产品开发策略 | 认证、专利、风险、差异设计、蓝海机会、FABE、SWOT/PEST |

## 数据来源（双轨）

- **线上**：Sorftime MCP 抓取的 Amazon 实时数据（销量/价格/星级/评论/好评差评原声/关键词），**绝不编造**
- **线下**：公开信息，**必须标注来源链接**，并区分「事实 / 估算 / 需人工核实」
- 线上、线下数据**分开展示**，每个数据点带来源角标（Sorftime / 公开信息 / 估算）

## 目录结构

```
amz-market-research/
├── SKILL.md                          # 技能主文档（方法论 + 数据采集工作流 + 样式 + 部署 + 脱敏）
├── README.md
├── .gitignore                        # 已排除凭据/内部路径
├── templates/
│   └── generator_template.py         # 参数化通用生成器脚本（产品/国家/类目/Node 全变量）
└── references/
    ├── pure-css-trend-curves.md        # 纯 CSS「近12个月销量/销售额曲线」组件实现
    ├── report-completeness-standard.md # 报告完整度对标基准（⭐ 首版易漏项）
    ├── report-generation-architecture.md # 多片段生成架构 + 锚点/目录/标签审计 + 结构对齐清单
    └── github-publish-contents-api.md  # 用 GitHub REST Contents API 直推发布的方法
```

## 输出样式

- 单文件 HTML，**蓝灰商务风**（--blue #2563eb + 灰阶）
- **纯 CSS** 组件（kpi-grid / bar-item / insight-box / verdict-box / table-wrap / tag 等），无 ECharts
- 可直接部署 Cloudflare Pages / GitHub Pages / Vercel 等静态托管

## 常见坑（详见 SKILL.md）

- ⛔ **CSS 拼到 `</style>` 之后 → 页面显示"源码标签"**：多片段字符串拼接 HTML 时，若完整 CSS 被拼进了字符串里第一个 `</style>` 之后，CSS 会掉进 `<body>` 当纯文本丢弃，页面只剩目录样式、其余全无排版、看起来像"源代码"。**生成后必校验** `<style>` 内总长（完整报告应数千字节）。
- ⛔ 生成器脚本**别用一个大 f-string 拼 HTML**（CSS 字面大括号会炸），改用字符串拼接 + `%` 格式化。
- ⛔ 英文评论原声的撇号（`I've` 等）用 `\u2019` 转义，避免炸掉单引号字符串。

## 重要约定

- ⛔ **凭据卫生**：产出物绝不硬编码 API key/token/邮箱；Cloudflare 等凭据一律走环境变量
- ⛔ **诚实数据**：好评/差评 TOP20 为真实频次，样本不足时降级 TOP10 并明确说明，绝不硬凑
- 页脚「分析负责人」可自定义或留空
- 公开分享前按 SKILL.md「发布前脱敏清单」检查内部路径与 session 专属报告，不要把含私有署名/私有数据的具体报告提交到公开仓库

## License

MIT
