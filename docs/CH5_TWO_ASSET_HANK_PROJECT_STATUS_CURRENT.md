# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`REVISED_2018_GDP_AND_CANONICAL_WORKBOOK_ACTIVE__PIM_AND_POPULATION_CLOSED`。
最新接受候选：`0bfff9ff9f388e39812c6592f72d5eedd633ae18`。PIM报告：`docs/CH5_MP4C_2018_PIM_CAPITAL_CHAIN_CLOSURE_REPORT.md`；Reviewer验收：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_REVISED_GDP_AND_CANONICAL_DATA_WORKBOOK.md`。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 已冻结并闭合
- V2时间合同：PLM rolling 10-year；`steady_year=2008+ii`；同年level row=`ii+9`；2018=2009–2018；same-year Zt。
- 安徽2018常住人口已闭合为`6076`万人，依据2023《中国人口和就业统计年鉴》修订历史值。
- PIM资本链已闭合：冻结`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`，安徽`K2000..K2018`逐年binary64精确复现；`K2018=1357314108.2013683`，V2 CAP=`1357314108201.3684`。资本是model-derived calibration object，不是官方资本存量；2011投资统计定义断点继续保留为限制。

## 当前唯一2018数据blocker
第四次全国经济普查后修订口径下安徽2018现价GDP尚未闭合：provisional workbook=`34010.91`亿元，2018初步官方公报=`30006.82`亿元。Owner已授权从公开官方来源检索修订后精确值和revision provenance。

## 当前 active task
任务只做零科学调用的数据研究和统一数据工件建设：
1. 从国家统计局/安徽统计局/官方年鉴等公开来源关闭修订后安徽2018现价GDP身份；
2. 若GDP闭合，静态构造最终2018输入receipt和same-year Zt，不运行模型；
3. 生成外部版本化工作簿`CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`，集中保存年度绑定、31省GDP/POP/投资/PIM资本、PLM alpha、same-year Zt、安徽2018最终输入、来源provenance和数据质量标记，便于以后长期使用；
4. 原CNKI/付费/保护Excel、MATLAB、cache均只读、不覆盖。完整私有面板xlsx默认留在本地证据根，不提交GitHub。

所有MATLAB、household/HJB/KFE、root/solve、firm/one-turn/controller、stationary/GE/annual、IRF/Results调用均为0。

## 后续路线
GDP闭合 + canonical workbook验收 → 最终2018 V2 input验收 → 真正2018单年小规模科学验证 → 若仍高收益/不收敛，再审计GovInv外层适应速度 → household/KFE有效性 → 有限省份 → 年度覆盖 → MP5/MP6动态。

生产网格继续I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。2022–2023六个负资本/复数`log_pcap`继续保留为独立后续数据质量问题。