# Chapter 5 两资产 HANK 当前状态
更新：2026-09-10。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`CORRECTED_2018_FIVE_TURN_DIAGNOSTIC_BLOCKER_ACCEPTED__KFE_LEAKAGE_ATTRIBUTION_ACTIVE`。
最新接受候选：`9864129dd2e97bae97238ab9cc588aea48682d29`。报告：`docs/CH5_MP4C_2018_CORRECTED_INPUT_FIVE_TURN_PREFIX_REPORT.md`；Reviewer验收：`docs/CH5_MP4C_2018_CORRECTED_INPUT_FIVE_TURN_PREFIX_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION.md`。Builder默认`gpt-5.6-sol / medium`。Results eligibility=FALSE。

## 2018数据层已闭合
Canonical workbook：`D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`，SHA256=`AEA5A12B5E6474056C1C3EF84BF0156BA88442EF54B0A4FB9C4C6F33CA963F67`。安徽final-use：GDP `34010.9`亿元；POP `6076`万人；PIM `K2018=1357314108.2013683`万元；PLM vintage19/window2009–2018；alpha=`.772866243094144`；same-year Zt约`.0006934644495858679`。资本为model-derived calibration object；2011投资统计定义断点继续作为限制。

## 已接受 corrected-2018 科学前缀
- turn1–3已建立 corrected firm `ra=.02` 经 native capital-allocation timing 直接进入 turn3 household `rah=.0184420457528848` 的传播证据；turn3安徽 raw `ra0=-.024968792977977675`、used `ra=.02`、HJB 11次。
- five-turn trajectory 完整执行5 turns / 155 province updates，scientific retries=0；turn1–3复现 mismatch=0。
- turn4首次 national max `nk_gap<.1`，turn4–5均触发 native Zt adjustment 和31省 `LOW_RA_DECREASE_0P9` GovInv action。

## 已接受 five-turn blocker
five-turn 不判普通 PASS。turn4/5 全31省 returned density 均为 `DIAGNOSTIC_ONLY`。近机器精度负 density 不是实质 blocker；实质 blocker 是：
- nonzero source-free stationarity residual；
- widespread upper-b outward leakage；
- turn4/5全国每轮620个 positive upper-b leak cells，max leak rate约2.2393；lower-b/lower-a/upper-a outward leak为0。
因此 C/L/A/B 只能作为 diagnostic quantities，不能作为 accepted economic moments。安徽turn3的 A/B/A+B sharp collapse 被保留，但与 leakage 的因果关系尚未闭合。

## 当前 active task：zero-science-call KFE leakage attribution
`tasks/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION.md`。
只允许读取five-turn已保存的 operator/density/drift 并做矩阵重建、代数和测试；所有 scientific/model calls 必须为0。目标是判断当前five-turn blocker是否与已接受 call725 `rah=.07` 的 finite-box upper-b leakage + KFE row-replacement/pinning implicit-source algebra 属于同一机制，并做全国turn4/5定量归因。

## 禁止边界
当前禁止 turn6+、new KFE solve、steady-state、GE、annual、MATLAB、IRF、Results，以及任何 production boundary/grid/source/pinning repair。D1–D3仍为 deferred redesign proposals，不得当作已采用方案。

## 验收后分叉
- 若 `SAME_FINITE_BOX_UPPER_B_LEAKAGE_AND_PINNING_MECHANISM_CONFIRMED`：Reviewer先做机制验收，再由Owner决定是否进入 boundary redesign / finite-box closure 设计任务；不得直接科学重跑。
- 若 `PARTIAL_MECHANISM_MATCH` 或 `DISTINCT`：先定位 additional residual source，再决定后续。
- 若 artifacts 不足：返回 bounded evidence gap，不允许为补证据重跑科学模型。

2022–2023六个非正资本/无效Zt继续作为独立未来年份数据质量问题。生产网格仍I20,b[-2,5]、J20,a[0,10]、Nz2,z[.8,1.3]。