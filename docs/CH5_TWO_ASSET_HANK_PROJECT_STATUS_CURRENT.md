# Chapter 5 两资产 HANK 当前状态
更新：2026-09-12。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_RAW_RA0_PAYOFF_SHORT_HORIZON_SAFETY_ACCEPTED__HJB_DRIFT_FORENSIC_ACTIVE`。

最新 accepted raw-payoff safety candidate：`678860073d3d5b653b8863b71f494f569960ced7`。
Reviewer acceptance：`docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_COMMON_TURN1_BOOTSTRAP_SAFETY_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_RAW_RA0_PAYOFF_HJB_DRIFT_ZERO_SCIENCE_FORENSIC.md`。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

资本网络总体科学设计冻结稿：`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
K1 scoring/data 冻结稿：`docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`。
Payoff-return 冻结稿：`docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`。
Bootstrap/timing 冻结稿：`docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOOTSTRAP_TIMING_FREEZE_CURRENT.md`。

## K1 capital network：已真实进入 bounded runtime
K1 bilateral capital network 已在 corrected-2018 bounded K1A route 中实际替换 capital allocation，destination-by-origin `S` 同时用于 private-capital quantity 与 household `rah`。equal-share `beta_distance=0` 与 pure-geographic `beta_distance=2` 的25-turn symmetric paths 已接受；capital conservation、home retention、same-`S` quantity/payoff、C1 residual-public-assets 与 source-faithful labor均闭合。Legacy allocator仅保留为source-faithful/reference route。

## Raw payoff contract 与 common bootstrap：已冻结
Owner 已冻结 raw `ra0` 为最终 K1 household illiquid payoff source object，解释为 per-model-time endogenous net productive-capital return；不做 calendar annualization，不宣称外部 market-return mapping。历史 `ra=clip(ra0,.02,.09)` 的 bounds 继续只属于 `EMPIRICAL_NUMERICAL_SAFEGUARD`。

Accepted initialization 不含 prior-completed `ra0`，因此 Owner 冻结 common turn-1 bootstrap：Control/Raw turn1 都使用 entering clipped/source-used `ra`；turn1 完成后各自获得 provenance-safe `ra0`；turn2起 Control 使用本路径 prior used `ra`，Raw 使用本路径 prior raw `ra0`。不允许 same-turn feedback 或 cross-path borrowing。

## Raw payoff short-horizon safety：已接受，但仅 narrow runtime-safety
Control/Raw 均完成5/5 turns；turn1 saved scientific state逐元素一致；Raw turns2-5 均使用本路径 immediately prior completed `ra0 @ S`。总 trajectory=2，HJB/KFE=310/310，scientific retry=0。所有310个province-turn的same-`S`、K1 capital conservation、C1 accounting、source-faithful labor保持；无NaN/Inf、scientific exception、same-turn feedback或provenance failure。

因此 `RAW_RA0_PAYOFF_SHORT_HORIZON_RUNTIME_SAFETY_SUPPORTED_WITH_COMMON_TURN1_BOOTSTRAP` 在“通过既有hard-stop且短期可执行”的狭义范围内被接受。

同时 numerical stress 明显：treatment turns2-5 HJB convergence Control=`49/124`，Raw=`12/124`；Raw turn5=`0/31` converged。Raw median entering `rah` 约为Control的5.3-5.6倍；max HJB statistic显著放大；Raw最大绝对liquid drift约`1.29e12`、最大illiquid transfer约`2.74e6`。这些有限值未触发先验hard-stop，但不能被解释为稳定数值解或quantitative policy evidence。

Reviewer裁定：上述严重非收敛和drift敏感性可以作为short-horizon mechanism evidence，因为payoff-source treatment被cleanly isolated且accounting/provenance保持；但不允许据此进入更长runtime或K1B。

## 当前 active gate：zero-science HJB/drift forensic
当前 exact task 不运行任何模型。只使用accepted persisted Control/Raw evidence与source code，定位raw payoff stress按province/turn/grid/boundary/policy label的集中位置，区分Control已有大drift与Raw incremental amplification，并追踪`rah/r_a`进入effective return、transfer/adjustment cost、drifts与boundary selector的source law。

目标是分类stress更接近payoff-scale exposure、specific boundary interaction，还是需要新的Owner scientific/numerical-authority decision。不得修改solver/tolerance/grid/cap/payoff mapping。

## K1B / K2 / KFE
K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；其 z-scored raw `ra0` 只用于 destination attractiveness，不是 payoff。K2不授权。

corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning 仍是独立 KFE blocker。全部相关 KFE 仍为 `DIAGNOSTIC_ONLY`。当前任何 K1 结论均不构成 steady-state、KFE、annual/IRF/welfare 或 Results acceptance。
