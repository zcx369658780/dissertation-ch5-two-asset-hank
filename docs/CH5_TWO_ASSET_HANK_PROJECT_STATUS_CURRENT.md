# Chapter 5 两资产 HANK 当前状态
更新：2026-09-09。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`PIM_CAPITAL_CHAIN_CLOSURE_ACTIVE__EXISTING_PIM_METHOD_FROZEN__GDP_STILL_OPEN`。
最新接受候选：`4db5c0691535e92d34a86c67ee96c2b8978c1de2`。付费数据审计报告：`docs/CH5_MP4C_PURCHASED_DATASET_GAP_CLOSURE_AUDIT_REPORT.md`；Reviewer验收：同前缀 `_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_PIM_CAPITAL_CHAIN_CLOSURE.md`。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 已冻结并实现的年度合同
PLM rolling 10-year；`steady_year=2008+ii`；同年GDP/CAP/POP一基row=`ii+9`；2018使用2009–2018、PLM vintage19；Zt保持原公式并使用同年水平量。Python annual/pre-model层已实现`CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`和V2 metadata/source-hash fail-closed合同。

## 已闭合的数据身份
2018安徽常住人口已闭合为`6076`万人。依据为官方《中国人口和就业统计年鉴2023》表1-1；该表明确说明2011–2019年人口数据依据2020人口普查修订。权威是官方年鉴，付费包只是本地副本。

## Owner最新资本方法裁决
Owner明确裁决：不再以“取得官方资本存量”为目标；Chapter 5资本存量继续作为模型构造量，沿用现有永续盘存法（PIM）。现有PIM方法冻结：
- `K0=I0/0.1`；
- `Kt=(1-.096)K(t-1)+I(t-1)`；
- 折旧率0.096不变；
- 初始化规则不变；
- K2018只依赖I2000..I2017；
- 不因收敛问题改公式、折旧率或投资概念。

当前省级投资序列可作为`MODEL_CALIBRATION_SOURCE__CNKI_CURATED_PROVINCE_PANEL`使用，但不得冒充官方同口径连续统计序列。2011固定资产投资统计范围断点继续写入metadata和论文/模型限制，不在本任务中做桥接、回溯、拼接或插值。

## 当前 active task：PIM资本链闭合
`tasks/CH5_MP4C_2018_PIM_CAPITAL_CHAIN_CLOSURE.md`。

任务只做零科学调用的数据/方法闭合：
1. 按冻结源码时序，用安徽I2000..I2017静态重建K2018；
2. 核对是否精确复现现有workbook-derived CAP=`1357314108.2013683`；
3. 版本化PIM source/provenance、公式、参数、2011口径限制和K2018 receipt；
4. 付费`s​​j479`城市投资仅允许作方向/趋势二次交叉核验，不得在六项省级加总条件未闭合时求和或覆盖省级链。

若递推复现通过，本轮应关闭资本/PIM data-method blocker。资本仍必须标记为model-derived，不得写成官方资本存量。

## 剩余数据blocker
2018安徽修订后现价GDP仍未闭合：当前provisional workbook=`34010.91`亿元，2018初步官方=`30006.82`亿元，尚缺第四次全国经济普查后修订口径下2018精确官方值及修订表。

## 科学路线
PIM资本链闭合 → 修订后2018 GDP身份闭合 → 构造/验收最终2018 V2 candidate input → 真正2018单年小规模科学验证 → 若仍高收益/不收敛，再审计GovInv外层适应速度 → household/KFE有效性 → 有限省份 → 年度覆盖 → MP5/MP6动态。

当前不运行household/HJB/KFE/firm/GE/annual，不调整GovInv/alpha，不扩大bmax，不切换PLM。2022–2023六个负资本/复数`log_pcap`继续作为独立后续数据质量问题。生产网格继续冻结I20,b[-2,5]；J20,a[0,10]；Nz2,z[.8,1.3]。
