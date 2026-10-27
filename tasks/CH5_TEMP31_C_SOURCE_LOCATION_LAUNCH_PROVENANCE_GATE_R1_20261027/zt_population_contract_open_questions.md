# Zt与人口/就业合同：后续Owner决策清单

本轮只复核指定源码与固定前轮独立结论，不修复、不执行，不把不知道写成实测模型失败。

| 问题 | source-defined静态证据 | 仍需Owner提供/选择 | 本轮结论 |
| --- | --- | --- | --- |
| 历史Zt固定2020 vs 新steady-year | 历史固定2020保留为版本化已知事实；当前ANNUAL:198–207声明zt_source_calendar_year，228–230要求等于binding.calendar_year | 采用哪个版本/年口径、真实输入vintage与正式科学合同 | NEEDS_OWNER；不统一年份、不重命名字段 |
| 属性接口差异 | EMPIRICAL:101–105读取canonical.fixed_zt_calendar_year；固定前轮GPT审阅已确认当前ANNUAL全文无此属性 | 先定输入/版本与Zt合同，再另行决定是否修接口 | PROVEN_STATIC_REFERENCE，条件风险；NOT_RUN，无观察到AttributeError |
| 常住人口 vs 就业人数 | ANNUAL:439–447的primary pop来自常住人口；OWNER_A:28–35的POP_SHEET=就业人数 | 原表版本/单位、N采用的人口/就业含义、与z加权有效劳动/工时的完整桥 | 源表名不同可证；本轮不打开sheet、不决定N=就业/人口、不得N=P/3 |

工作地目的地tau_j及同税一次是已决目标，R2/R3保持隔离、D1/D2/D3为未闭合目标。gross/net、财政税基、sigma/phi/alphal、劳动/价格/期间单位等旧缺口不重审、不改公式。源码字段/群体定义差异不归责长会话或SSH故障；来源定位缺失也不等于HA/GE失败。
