# Chapter 5 两资产 HANK 当前状态
更新：2026-09-12。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_RAW_RA0_ECONOMIC_SOURCE_RETAINED__HJB_PAYOFF_SCALE_AUTHORITY_AUDIT_ACTIVE`。

最新 accepted raw-payoff short-horizon safety candidate：`678860073d3d5b653b8863b71f494f569960ced7`。
最新 accepted zero-science forensic candidate：`cd5abea31cfbfcdb4170970df7e0504b394571d5`。
Reviewer acceptance：`docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_HJB_DRIFT_ZERO_SCIENCE_FORENSIC_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_HJB_PAYOFF_SCALE_AUTHORITY_ZERO_SCIENCE_AUDIT.md`。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

资本网络总体科学设计冻结稿：`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
K1 scoring/data 冻结稿：`docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`。
Payoff-return 冻结稿：`docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`。
Bootstrap/timing 冻结稿：`docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOOTSTRAP_TIMING_FREEZE_CURRENT.md`。
Payoff-scale / diagnostic-bound 冻结稿：`docs/CH5_MP4C_K1_PAYOFF_SCALE_MAPPING_AND_DIAGNOSTIC_BOUND_POLICY_FREEZE_CURRENT.md`。

## 旧系统与重建状态
旧多省份 MATLAB/source-faithful 数值系统继续保留为历史 provenance/reference，但其 private-capital allocation、household return aggregation、historical clipping 与 corrected-2018 empirical KFE 等若干关键合同已被接受证据证明存在结构缺陷、信息损失或未闭合科学问题，不能再作为最终 scientific authority。

新数值系统正在 gate-by-gate 重建。K1 bilateral capital network 的 accounting、home retained capital、same-`S` quantity/payoff 与 bounded dynamic transmission 已获得 accepted evidence；但 household payoff scale、长期 HJB 稳定性、empirical KFE、K1B/K2、steady state 与 Results 仍未完成。因此不能把新系统描述为已经最终建立。

## Raw payoff status
Owner 继续保留 raw firm `ra0` 作为最终 K1 household illiquid payoff 的经济 source object，但不再假定 firm-side raw numerical level 可一比一直接作为 household HJB `r_a`。Accepted short-horizon evidence 显示 direct raw-level mapping 会显著恶化 HJB convergence，并经 value-derivative -> transfer FOC -> quadratic adjustment-cost law放大；zero-science forensic 同时表明 stress 不是 boundary-only，且 Control 本身存在 baseline extremes。

下一步必须先审计 firm return 与 household continuous-time HJB 的 period/time-unit/numeraire authority，再决定 identity mapping、source-backed period conversion 或其他有明确来源的 mapping。当前不得人为选择 shrinkage、normalization、annualization、cap 或 smoothing。

## Owner debugging-bound policy
Owner 已明确授权：未来为建立可行稳态路线，可在 fresh exact runtime task 中使用硬性的 `ra`/`rah` 与 `wjt`/wage 等上下界作为**临时 numerical diagnostic scaffolding**，并在稳态路线稳定后按 preregistered ladder 逐步放宽乃至去除。

该授权不等于当前激活任何新 bound。未来每个 bound 必须在执行前明确对象、上下界与用途，记录 hit/saturation counts，不得观察同一 run 后调界限以强行获得 PASS；依赖 bound 的 steady state 只能标记为 provisional。历史 `[.02,.09]` 仍只是 `EMPIRICAL_NUMERICAL_SAFEGUARD`，不是最终 structural payoff law。

## 当前 active gate
`CH5_MP4C_K1_HJB_PAYOFF_SCALE_AUTHORITY_ZERO_SCIENCE_AUDIT` 新增 scientific/model call 预算全部为0。必须审计 `rho`、`r_b`、`r_a`、`delta`、`ra0`、productivity transition rates、wage/`wjt`、transfer/adjustment-cost law、annual/quarterly labels与 legacy MATLAB/dissertation authority，并 inventory 当前 hard bounds。

目标是判断是否存在 source-backed HJB payoff-scale mapping；本门不运行模型、不修改科学源码、不激活新 bounds。

## K1B / K2 / KFE
K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；其 z-scored raw `ra0` 只用于 destination attractiveness，不是 household payoff。K2不授权。

corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning 仍是独立 KFE blocker。当前任何 K1 结论均不构成 steady-state、KFE、annual/IRF/welfare 或 Results acceptance。
