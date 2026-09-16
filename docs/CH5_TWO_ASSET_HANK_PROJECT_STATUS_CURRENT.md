# Chapter 5 两资产 HANK 当前状态

更新：2026-09-16。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`CORRECTED_HJB_OPTION_A_SEED_OWNER_ADOPTED__SINGLE_POLICY_MAP_DIRECT_STEP_ACTIVE__PRODUCTION_UNCHANGED`。
Results eligibility=`FALSE`。

## Accepted checkpoints

Owner-adopted D1/D2/D3 corrected diagnostic bundle、isolated static implementation、ten-cell fail-closed selector evidence、Cells 4/8/10 zero-science algebraic attribution，以及 corrected-HJB one-step design/input binding均已接受。Source-faithful/production paths remain frozen。

Cells 4/8/10 的 historical `NO_ADMISSIBLE_POLICY` 已归因为 frozen MATLAB-faithful derivative states 与 corrected D1-D3 contract 的结构性不相容；没有 selector branch omission。不得重复同一 historical-derivative panel，也不得把该结果解释为 corrected HJB/KFE/economic equilibrium 不存在。

## Owner seed adoption

Owner 于 2026-09-16 明确采用 Option A 作为第一次 corrected-target HJB one-step diagnostic 的数值 seed：

- `hjb100_initialization.mat:v0`
- file SHA-256 `1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81`
- field SHA-256 `564B95B818713477691389903C3CFF72B5A7F991B924D52FBEB23D5A3675D665`
- shape `(20,20,2)`, F-order。

Scientific rationale is provenance/path dependence: Option A is an accepted source-native numerical initialization and is not an endogenous output of the historical source-faithful boundary/operator trajectory. This choice does not claim proximity to the corrected fixed point or better expected convergence.

Owner adoption authority: `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_OPTION_A_SEED_OWNER_ADOPTION_ACCEPTANCE_20260916.md`。

## Active scientific gate

Current active Builder task:
`tasks/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_OPTION_A_SINGLE_POLICY_MAP_DIRECT_STEP_20260916.md`。

Exact ceiling: one complete 800-cell corrected policy map, <=800 real selector evaluations, <=264 scalar roots, one D2 assembly only after all 800 cells pass, and at most one sparse direct HJB solve. Retries=0. Any first failed cell stops before D2/direct solve.

No second policy map, nonlinear continuation, KFE, MATLAB, outer/firm/wage-return recalculation, GE, annual, shock, IRF or Results call is authorized. Even a PASS is only one-step diagnostic evidence, not HJB convergence/fixed-point or production/Results authority.
