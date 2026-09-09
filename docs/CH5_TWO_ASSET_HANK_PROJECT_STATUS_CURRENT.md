# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`PIM_CAPITAL_CHAIN_ACCEPTED__2018_CAP_BINARY64_REPRODUCED__GDP_ONLY_DATA_BLOCKER_REMAINS`。
最新接受候选：`0bfff9ff9f388e39812c6592f72d5eedd633ae18`。报告：`docs/CH5_MP4C_2018_PIM_CAPITAL_CHAIN_CLOSURE_REPORT.md`；Reviewer验收：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：无。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 已冻结并实现的年度合同
PLM rolling 10-year；`steady_year=2008+ii`；同年GDP/CAP/POP一基row=`ii+9`；2018使用2009–2018、PLM vintage19；Zt保持原公式并使用同年水平量。Python annual/pre-model层已实现`CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`和V2 metadata/source-hash fail-closed合同。

## 已闭合的数据/方法身份
1. 2018安徽常住人口已闭合为`6076`万人，依据官方《中国人口和就业统计年鉴2023》表1-1；2011–2019人口按2020人口普查修订。
2. 资本存量方法已由Owner冻结为现有永续盘存法（PIM），不再追求不存在的“官方资本存量”对象。冻结公式：`K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)`；折旧率与初始化规则不改。
3. 候选`0bfff9ff...`已静态、逐年、binary64精确复现安徽`K2000..K2018`。`K2018=1357314108.2013683`，V2 transformed CAP=`1357314108201.3684`；绝对/相对差异均0，无首个差异年份，`I2018`不参与K2018。
4. 安徽`固定资产投资额!N2:N20`在raw与filled workbook中逐项binary64相同；本轮未做backcast、bridge、rescale、splice、interpolation或参数调整。
5. 资本存量继续标记为model-derived calibration object，来源分类`MODEL_CALIBRATION_SOURCE__CNKI_CURATED_PROVINCE_PANEL`，不得称官方资本存量。2011固定资产投资统计定义断点继续作为明确限制保留。
6. 付费城市投资仅作`SECONDARY_DIRECTIONAL_CROSSCHECK_ONLY`，未求和、未进入PIM。科学调用全部0。

## 剩余2018数据blocker
只剩第四次全国经济普查后修订口径下安徽2018现价GDP身份仍未闭合：当前provisional workbook=`34010.91`亿元，2018初步官方=`30006.82`亿元，尚缺修订后精确官方表值及revision provenance。

## 科学路线
修订后2018 GDP身份闭合 → 构造/验收最终2018 V2 candidate input → 真正2018单年小规模科学验证 → 若仍高收益/不收敛，再审计GovInv外层适应速度 → household/KFE有效性 → 有限省份 → 年度覆盖 → MP5/MP6动态。

当前不运行household/HJB/KFE/firm/GE/annual，不调整GovInv/alpha，不扩大bmax，不切换PLM。2022–2023六个负资本/复数`log_pcap`继续作为独立后续数据质量问题。生产网格继续冻结I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。
