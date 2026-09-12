# Chapter 5 两资产 HANK 当前状态
更新：2026-09-12。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_ANNUAL_HJB_G1_VS_G2_CONTINUATION_ACCEPTED__G2_RESTORES_PARTIAL_RETURN_HETEROGENEITY_BUT_DEGRADES_HJB__FOCUSED_HA_HJB_MECHANISM_DIAGNOSTIC_ACTIVE`。

最新 accepted continuation candidate：`ab6b19022d920a8929a2ee66cc5511be6f602557`。
Reviewer acceptance：`docs/CH5_MP4C_K1_ANNUAL_HJB_G1_VS_G2_PRICE_GUARD_CONTINUATION_DIAGNOSTIC_ACCEPTANCE.md`。
Owner annual recalibration freeze：`docs/CH5_MP4C_K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_CONTRACT_FREEZE_CURRENT.md`。
Owner price-guard continuation freeze：`docs/CH5_MP4C_K1_PRICE_GUARD_CONTINUATION_AND_BOUNDARY_HIT_MONITORING_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_G1_VS_G2_HA_HJB_MECHANISM_ZERO_SCIENCE_DIAGNOSTIC.md`。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

## Annual G1 vs G2：已接受
Annual contract、K1 same-S、capital conservation、C1、source-faithful labor与own-prior return provenance均保持闭合。G1 `[-.05,.20]` treatment return upper-hit `124/124`；G2 `[-.10,.35]` 降为 `84/124`，恢复 `40/124` unsaturated province-turns，HJB-consumed return distinct counts为 `14,10,10,10`。

但 G2 treatment HJB convergence 从 G1 `18/124` 降至 `6/124`，且若干 transfer、adjustment-cost、`mu_a/mu_b` 与 drift extrema 显著放大。因此 Reviewer 不授权 longer G2，也不进入 G3/G4。G2 证明单纯放宽 return safeguard 会恢复部分省际 payoff heterogeneity，但当前 HA/HJB nonlinear block 对这一放宽高度敏感。

## Wage safeguard monitoring
Legacy wage safeguard `[.8,1.3]` 继续固定。G1 treatment wage hits=`112/124`；G2=`109/124`，仍高度绑定。每个后续 runtime continuation task继续必须像 legacy MATLAB 一样逐省逐轮记录 `ra/rah` 与 `wjt/wage` upper/lower/unsaturated province names、counts与shares。长期理想目标仍为 `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。

## 当前 focused HA/HJB mechanism gate
当前 exact task 新增 scientific/model calls 全部为0，只分析已保存的 G1/G2 evidence 和 accepted HJB source。目标是定位 G1->G2 convergence loss 与 control/drift amplification 到具体 province/turn/grid cell、return saturation regime、wage-hit regime、policy branch、value-derivative/transfer-FOC chain 及 boundary/interior regime，并区分 G1 baseline stress 与 G2 incremental stress。

在该机制诊断完成前，不发布 longer G2，不进入G3/G4，不放宽 wage guard，不修改 `chi0/chi1`、derivative floor、solver/grid/tolerance，也不进入K1B/K2。

## 数值系统重建状态
K1 bilateral capital network与annual time-base已进入accepted bounded runtime。当前主要 blocker 是 HA/HJB nonlinear continuation：放宽return guard会恢复异质性但显著恶化HJB稳定性；wage safeguard也仍高度绑定。旧 MATLAB/source-faithful 数值系统继续仅保留 provenance/reference。

## K1B / K2 / KFE
K1B `beta_return=.5` 仍仅preregistered，不授权runtime；K2不授权。corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning仍是独立KFE blocker；KFE=`DIAGNOSTIC_ONLY`。当前任何K1结论均不构成steady-state、annual/IRF/welfare或Results acceptance。
