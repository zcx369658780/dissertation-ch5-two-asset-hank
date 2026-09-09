# Chapter 5 Python 多省份两资产 HANK 路线
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前阶段
MP4已完成旧call725失败复现、rah=.07敏感性、KFE source/escape归因、b域压力测试、数据/插值审计、时间合同/Zt legacy审计、V2 pre-model实现、官方/付费数据审计、PIM资本链闭合，以及修订后2018 GDP身份闭合和canonical data workbook构建。Results=FALSE。

## 2018数据层已闭合
- 时间合同：`steady_year=2008+ii`；同年level row=`ii+9`；PLM rolling 10-year；2018=2009–2018；same-year Zt。
- GDP：安徽2018四经普后官方修订现价GDP=`34010.9`亿元；保护workbook=`34010.91`仅在官方0.1亿元精度下匹配。
- 人口：安徽2018=`6076`万人，后续官方年鉴按2020人口普查修订。
- 资本：冻结PIM `K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`，安徽K2000..K2018逐年binary64精确复现；K2018=`1357314108.2013683`，资本为model-derived calibration object。2011投资统计定义断点继续作为限制。
- canonical workbook：`CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`，SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`，私有本体不进GitHub。

## 当前 active task
`tasks/CH5_MP4C_2018_CORRECTED_INPUT_SINGLE_TURN_VALIDATION.md`

下一步首次进入修正数据后的科学运行：只执行1次2018 source-faithful ordered one-turn。完整保留31省顺序，但不进入稳态迭代。必须从hash匹配的canonical输入身份进入，不得fallback到旧mixed-year状态或legacy cache。

捕获全31省firm/household/controller关键观测，特别是安徽raw/used return、wage、household rah与HJB/KFE状态；旧mixed-year比较只使用保存证据。任何科学失败保存后立即停止，不重试、不调参数。

## 后续顺序
corrected 2018单turn → 若通过，受控多turn/稳态前缀 → 若仍高收益/不收敛，再审计GovInv外层适应速度 → household/KFE数值有效性 → 有限省份 → 年度覆盖 → MP5/MP6动态。

2022–2023六个非正资本/无效Zt继续作为独立未来年份数据问题。生产网格仍I20,b[-2,5]、J20,a[0,10]、Nz2,z[.8,1.3]。