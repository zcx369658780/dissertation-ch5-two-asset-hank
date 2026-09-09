# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`OFFICIAL_2018_DATA_IDENTITY_AUDIT_ACCEPTED__MANUAL_OFFICIAL_DATA_REQUIRED__SCIENCE_STILL_BLOCKED`。
最新接受候选：`729d2c13c5864e0f607ac6dc8fd863d19f02d3f7`。报告：`docs/CH5_MP4C_2018_OFFICIAL_DATA_IDENTITY_CLOSURE_REPORT.md`；Reviewer验收：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：无。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 已冻结并实现的年度合同
Owner冻结PLM rolling 10-year：`steady_year=2008+ii`；同年GDP/CAP/POP一基row=`ii+9`；PLM窗口=`steady_year-9:steady_year`；2018使用2009–2018；PLM estimator/workbook保持。Python annual/pre-model层已实现`CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`和same-year Zt、版本化metadata/source-hash fail-closed合同。

## 本轮官方身份审计接受结论
1. 安徽2018官方统计公报提供初步GDP=`30006.82`亿元、年末常住人口=`6323.6`万人；当前provisional workbook分别为`34010.91`亿元与`6076`万人。2019官方公报确认第四次全国经济普查后历史GDP发生修订，但本轮未取得可结构化核验的修订后2018精确GDP；人口也未取得足以解释`6323.6`与`6076`差异的后续官方修订谱系。因此两项仍未闭合，不能将任何一个值升级为最终官方身份。
2. 冻结资本递推`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`意味着`K2018`只需要`I2000..I2017`；`I2018`不进入K2018。安徽workbook这些投资值均为原始未填充值，但这只证明workbook lineage，不证明官方身份。
3. 官方材料确认2011年固定资产投资统计范围发生制度变更；本轮未取得一条可防御地直接拼接的2000–2017官方绝对值序列，也没有取得链接/回溯口径，因此`CAPITAL_CHAIN_OFFICIAL_CLOSURE_INCOMPLETE`成立。不得为了闭合而自行插值或拼接统计定义不一致的序列。
4. 当前2018 CAP=`1357314108.2013683`仍是workbook派生模型输入，不是官方资本存量。未来若官方投资链闭合，只能标记为`MODEL_DERIVED_FROM_OFFICIAL_INVESTMENT`。
5. 因官方GDP/人口修订身份和投资链未闭合，本轮没有生成candidate V2 correction package或candidate Zt。

## 现在需要Owner手工补充的最小官方资料
- 第四次全国经济普查后修订口径下的安徽2018现价GDP精确值、表名/版本/来源；
- 安徽2018年末常住人口的后续权威值与修订/调查口径，足以解释`6323.6`和`6076`的差异；
- 安徽2000–2017逐年固定资产投资绝对值及单位，并附2011统计制度变更的链接、回溯或可比口径说明。若官方没有可比连续序列，则需Owner另行决定资本存量重构方法，而不能静默拼接。

## 科学路线
在上述官方身份闭合前，不发布新的2018 household/HJB/KFE/firm/GE/annual科学运行，不调整GovInv/alpha收敛速度，不继续扩大bmax，不把当前provisional workbook值当最终官方事实。

2022–2023六个负资本/复数`log_pcap`仍是独立数据质量问题，不进入下一次2018小规模验证范围。历史rah=.09/.07、KFE边界、Qh负率、P32/sigma和b域实验仍只代表旧混合年份输入。

生产网格继续冻结I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。

下一步顺序：Owner手工补充官方资料 → Reviewer关闭2018 data identity并生成/验收候选V2输入（如需） → 真正2018单年小规模科学验证 → 若仍高收益/不收敛，再审计GovInv外层适应速度 → household/KFE数值有效性 → 必要有限省份验证 → 年度覆盖 → MP5/MP6动态路线。
