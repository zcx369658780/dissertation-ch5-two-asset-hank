# Chapter 5 两资产 HANK 当前状态
更新：2026-09-12。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_G1_VS_G2_MECHANISM_FORENSIC_ACCEPTED__INSTRUMENTED_HA_HJB_DIAGNOSTIC_ACTIVE`。

最新 accepted G1-vs-G2 runtime candidate：`ab6b19022d920a8929a2ee66cc5511be6f602557`。
最新 accepted zero-science mechanism candidate：`f7c52f061b9eb3666d26985602ad6527774b5bb2`。
Reviewer acceptance：`docs/CH5_MP4C_K1_G1_VS_G2_HA_HJB_MECHANISM_ZERO_SCIENCE_DIAGNOSTIC_ACCEPTANCE.md`。
Owner annual recalibration freeze：`docs/CH5_MP4C_K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_CONTRACT_FREEZE_CURRENT.md`。
Owner price-guard continuation freeze：`docs/CH5_MP4C_K1_PRICE_GUARD_CONTINUATION_AND_BOUNDARY_HIT_MONITORING_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_G1_VS_G2_HA_HJB_INSTRUMENTED_BOUNDED_DIAGNOSTIC.md`。
Results eligibility=`FALSE`。

## G1/G2 continuation result：已接受
G2 从 `[-.05,.20]` 放宽到 `[-.10,.35]` 后，return upper saturation 从 `124/124` 降到 `84/124`，恢复 `40/124` unsaturated province-turn，但 treatment HJB convergence 从 G1 `18/124` 降到 G2 `6/124`。G2 不支持 longer G2，也不授权 G3/G4。

wjt safeguard `[.8,1.3]` 仍高度绑定；G1/G2 treatment wage hits 分别为 `112/124` 与 `109/124`。所有 continuation runtime 继续必须逐省逐轮记录 return/wage 上下界撞界省份、counts、shares；最终目标仍为 `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。

## Zero-science mechanism forensic：已接受
Accepted classification：`G2_STRESS_MIXED_ACROSS_NEWLY_UNSATURATED_AND_STILL_SATURATED_RETURN_REGIMES__PATH_HISTORY_AND_WAGE_INTERACTION_NOT_IDENTIFIABLE_FROM_PERSISTED_EVIDENCE__BOUNDED_INSTRUMENTATION_TASK_REQUIRED`。

Forensic 显示：G2 stress 不是单一 newly-unsaturated 或 still-saturated return regime 的结果。`40/40` newly-unsaturated G2 observations 均 nonconverged，但最大 HJB statistic 与全局 transfer/cost/drift extrema 均落在 still-saturated partition。G2 top extreme cells 绝大多数是 interior；总 outward face hits 反而从 G1 `4362` 降到 G2 `3795`，因此不是 boundary-only failure。

G1 自身已存在巨大 extrema，且部分 G1 worst cells 在 G2 下显著改善。G1->G2 policy label 变化规模很大，但 accepted persisted evidence 没有 value derivatives、pre-selector candidate objects、iteration trace 或 standalone KKT residual，因此无法识别 return、wage、selector 与 path-history 的先后因果链。

## 当前 active gate
下一门只增加 task-bounded instrumentation，不改任何科学参数、guard、方程、grid、tolerance 或 solver。重新执行相同 annual G1/G2 short-horizon route，并重点持久化：
- HJB iteration trace；
- directional/value derivatives；
- pre-selector liquid/transfer candidates；
- raw candidate drifts/controls/costs；
- selector/branch transition与最终policy；
- turn2 common-state immediate response 与 turns3-5 path-history response分离。

G1/G2 guard、wjt `[.8,1.3]`、annual calibration、K1 network、C1、source-faithful labor保持完全不变。该任务不得用于调参，只用于定位 HA/HJB 机制。

## 数值系统重建状态
K1 bilateral capital network、annual time-base 与 bounded price-guard continuation 均已有 accepted runtime authority。当前主要 blocker 是 HA/HJB nonlinear mechanism 的数值稳定性与 price safeguards 高度绑定。只有机制定位后才决定是否调整 `chi0/chi1`、derivative safeguard、price-interface calibration 或其他科学合同；不得由 Builder擅自改参。

## K1B / K2 / KFE
K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；K2不授权。corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning仍是独立KFE blocker；KFE=`DIAGNOSTIC_ONLY`。当前任何K1结论均不构成steady-state、annual/IRF/welfare或Results acceptance。
