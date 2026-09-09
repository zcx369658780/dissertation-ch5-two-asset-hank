# Chapter 5 当前交接
更新：2026-09-09。唯一仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。
Owner最终科学authority；ChatGPT Reviewer规划/验收/发布；Codex Builder默认`gpt-5.6-sol / medium`。

## 当前入口
先fresh读取live main、AGENTS、规则索引和当前状态。
当前状态：`OFFICIAL_2018_DATA_IDENTITY_AUDIT_ACCEPTED__MANUAL_OFFICIAL_DATA_REQUIRED__SCIENCE_STILL_BLOCKED`。
当前 active task：无。Results eligibility=FALSE。

## 已冻结并实现的合同
PLM使用rolling 10-year：2009=2000–2009、2018=2009–2018、2023=2014–2023；`steady_year=2008+ii`；同年level row=`ii+9`；PLM estimator/workbook保持；Zt公式保持但使用稳态同年GDP/CAP/POP。Python annual/pre-model层已实现`CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`和V2 metadata/source-hash fail-closed。

## 最新接受的官方身份审计
候选`729d2c13c5864e0f607ac6dc8fd863d19f02d3f7`已接受，主结论`PARTIAL_OFFICIAL_IDENTITY__MANUAL_DATA_REQUIRED`。

- 2018安徽官方统计公报的初步GDP=`30006.82`亿元，当前workbook=`34010.91`亿元；2019公报确认第四次经济普查后历史GDP修订，但修订后2018精确值尚未闭合。
- 2018安徽年末常住人口初步值=`6323.6`万人，当前workbook=`6076`万人；后续权威修订谱系尚未闭合。
- 冻结资本递推意味着K2018使用I2000..I2017，I2018不参与。安徽workbook投资值全部原始未填，但只证明lineage。
- 2011固定资产投资统计范围发生官方确认的制度断点；未取得可防御地拼接的2000–2017官方绝对值链，因此没有重算candidate CAP。
- 当前CAP=`1357314108.2013683`仍是workbook派生模型输入，不是官方资本存量；未来官方链闭合后只能称`MODEL_DERIVED_FROM_OFFICIAL_INVESTMENT`。
- 没有生成candidate V2 correction package或candidate Zt。科学调用全部0。

## Owner下一步手工资料
请补充或上传：
1. 第四次全国经济普查修订口径下安徽2018现价GDP精确值及官方表/版本；
2. 安徽2018年末常住人口的后续权威值与修订/调查口径，足以解释6323.6与6076差异；
3. 安徽2000–2017逐年固定资产投资绝对值、单位，以及2011制度变更的衔接/回溯/可比口径说明。

若官方没有一条可比连续投资链，不要静默拼接；需由Owner另行决定资本存量重构方法。

## 路线
Owner补充官方资料 → Reviewer关闭2018 data identity并生成/验收candidate V2输入（如需要） → 真正2018单年小规模科学验证 → 若仍高收益/不收敛，再审计GovInv外层适应速度。

在数据闭合前不运行新的2018 household/HJB/KFE/firm/GE/annual，不调GovInv/alpha，不继续扩大bmax。生产网格仍I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。
