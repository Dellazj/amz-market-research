# 纯 CSS 蓝灰商务风「近12个月销量/销售额曲线」图（无 ECharts）

用户要的「曲线图」在蓝灰商务风报告里仍用纯 CSS `bar-item` 组件实现（用户偏好无 ECharts / 纯 CSS）。实证于某电子类目（Hair 类）报告的「③ 旺季与淡季」延伸出的「④ 近12个月销量/销售额曲线」小节。

## 样式与标注约定
- 每根 bar 用现有 `bfill` 颜色类：常规月份 `bfill blue`，**11-12 旺季/峰值月用 `bfill rd`（销量）或 `bfill amb`（销额）** 高亮。
- 整组栏位包在一个浅灰圆角面板里：`<div style="margin:10px 0;padding:14px;background:var(--gray-100);border-radius:10px;">`
- 月在条形标签显示为 `25/08`（跨年时标注年份 25/26，前 5 个为 25、后 7 个为 26），避免歧义。
- bar 宽度 = `round(当月值 / 12个月峰值 * 100)`，最小给 `45-50%` 以下自然成形。
- 栏内文字用紧凑单位：销量 `539K`（千件）、销额 `$28M`（百万美元）。
- 数据全部硬编码进生成器脚本的模块级常量（如 `VOL_CHART` / `AMT_CHART`，用 `"\n".join([...])` 拼 bar-item 行），在 f-string 里以 `{VOL_CHART}` 引用。

## 数据来源（两个真实序列）
- **销量**：`category_trend node_id=X trend_index=SalesCount`（真实 Sorftime 序列，单位件）。
- **销额**：`SalesAmount` 趋势不可用（见主 SKILL 缺陷标注），用 `AvgPrice` 趋势的当月均价 × 当月销量推算，**必须贴黄 `tag-est` 估算标签**：「Sorftime 类目趋势未直接输出类目总月销额，本曲线以当月月销量×当月均价估算得出（销量、均价均为 Sorftime 实时抓取）」。
- **取值窗口**：取最近 12 个完整月（去掉当月的部分数据月——当月趋势往往不完整）。

## 节奏结论（insight-box amb）
把峰值/低谷具体数字写进结论，例如：
"最旺季为 11-12 月（12月达全年峰值：销量 53X 万件、销额 $2,XXX 万，约为淡季的 2 倍，节庆礼赠驱动）；2 月为全年低谷。备货推广应聚焦 Q4。"（以实际抓取数值替换）

## 复用要点
每次换产品/类目时：重跑 SalesCount + AvgPrice 两条趋势 → 算月销额 → 按上面规则重生成 VOL_CHART / AMT_CHART 两个常量的 bar 行（可直接用 execute_code 打印后粘回脚本，需先确认 max 峰值用于归一化）。
