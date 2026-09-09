# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`REVISED_2018_GDP_AND_CANONICAL_WORKBOOK_ACCEPTED__2018_DATA_LAYER_CLOSED__SINGLE_TURN_VALIDATION_ACTIVE`。
最新接受候选：`7e363b2d228623d3b315f8c140cad6332a57104b`。报告：`docs/CH5_MP4C_2018_REVISED_GDP_AND_CANONICAL_DATA_WORKBOOK_REPORT.md`；Reviewer验收：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_CORRECTED_INPUT_SINGLE_TURN_VALIDATION.md`。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 2018数据层已闭合
- 修订后安徽2018现价GDP官方公布值=`34010.9`亿元，来源安徽省统计局四经普后2018 GDP修订公告。保护workbook=`34010.91`亿元，仅在官方一位小数精度下匹配；canonical final-use字段采用官方`34010.9`并保留源值及精度边界。
- 安徽2018常住人口=`6076`万人，依据2023《中国人口和就业统计年鉴》按2020人口普查修订的2011–2019历史序列。
- PIM资本方法冻结并闭合：`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`；安徽`K2000..K2018`逐年binary64精确复现，`K2018=1357314108.2013683`，V2 CAP=`1357314108201.3684`。资本是model-derived calibration object，不是官方资本存量；2011投资统计定义断点继续作为限制。
- 时间合同：PLM rolling 10-year；`steady_year=2008+ii`；同年level row=`ii+9`；2018 PLM vintage19/window2009–2018；same-year Zt。

## canonical workbook
私有长期数据工件：`CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`，外部证据路径`D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\`，SHA-256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`。Builder报告12/12 required sheets、744/744 PIM binary64一致、无公式/宏/外部链接；私有xlsx未提交GitHub，仓库仅保存hash-bound manifest/readback/receipts。

安徽2018最终静态输入：GDP=`34010.9`亿元 / `34010900.0` transformed；POP=`6076`万人 / `607600.0`；CAP=`1357314108.2013683` / `1357314108201.3684`；alpha=`0.772866243094144`；same-year `IND_Zt≈0.0006934644495858679`。该对象仅为pre-model input，不是Results。

## 当前 active task：corrected 2018 single-turn validation
执行一次且仅一次source-faithful 2018有序多省份turn。必须先验证canonical workbook精确hash；使用最终2018输入身份，不得fallback到旧混合年份状态或无版本cache。完整保留31省source order，但只运行一个turn，不进入稳态/GE/年度收敛。

任务捕获所有省份关键firm/household/controller观测以及安徽forensic record；旧mixed-year比较只能使用保存证据，不得重跑。任何household/HJB/KFE/firm失败均落盘并立即停止，不做科学重试，不调参数、GovInv、grid、rate、solver/tolerance或boundary law。

## 当前科学路线
corrected 2018单turn验证 → 若通过，再由Reviewer决定是否进入受控多turn/稳态前缀 → 若修正数据后仍出现高收益或轨迹不收敛，再审计GovInv外层适应速度 → household/KFE数值有效性 → 有限省份 → 年度覆盖 → MP5/MP6动态。

2022–2023六个非正资本/无效Zt记录继续作为独立未来年份数据质量问题，不影响2018单turn。生产网格继续I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。