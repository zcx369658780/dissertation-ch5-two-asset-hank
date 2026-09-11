# Chapter 5 两资产 HANK 当前状态
更新：2026-09-12。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_RAW_RA0_PAYOFF_BOOTSTRAP_TIMING_FROZEN__COMMON_TURN1_SAFETY_DIAGNOSTIC_ACTIVE`。

最新 accepted payoff-return re-audit candidate：`e6297bb19e10a77593e1c2c7876eb94f02c71533`。
Owner payoff contract：raw `ra0` 已冻结为最终 K1 household illiquid payoff source object，解释为 `MODEL_TIME_RETURN_RATE__CALENDAR_PERIOD_UNRESOLVED` 与 `INTERNAL_MODEL_PRODUCTIVE_CAPITAL_RETURN_NUMERAIRE__EXTERNAL_MARKET_MAPPING_UNRESOLVED`。
最新 pre-run blocked safety candidate：`2c29a38b153ee56e58c833297b7dad2da639d6e7`，已接受其 zero-science blocker evidence。
Owner bootstrap/timing freeze：`docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOOTSTRAP_TIMING_FREEZE_CURRENT.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC_WITH_COMMON_TURN1_BOOTSTRAP.md`。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

资本网络总体科学设计冻结稿：`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
K1 scoring/data 冻结稿：`docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`。
Payoff-return 冻结稿：`docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`。

## K1 capital network：已真实进入 bounded runtime
K1 bilateral capital network 已不是离线测试对象。Accepted K1A adapter/runner 已在 corrected-2018 bounded route 中实际替换 capital allocation，使用 destination-by-origin `S` 同时分配 private capital quantity 与 household `rah`，并已完成 equal-share `beta_distance=0` 与 pure-geographic `beta_distance=2` 两条 25-turn symmetric paths。1550 province-turn 中 capital conservation、home retention、quantity/rah same-`S`、C1 residual-public-assets 与 source-faithful labor gates 均闭合。geography 差异从 turn 2 开始经 network-produced `rah` 传播到 household、Y、wage 与后续 firm states。

Legacy allocator 仍作为 source-faithful/reference route 保留；K1 network 尚未被宣布为无条件 production/default steady-state route，因为 raw-payoff runtime safety、K1B、KFE 等后续科学门仍未完成。

## Payoff-return authority：raw `ra0` 已冻结
Payoff-return re-audit 已接受：source raw `ra0 = rk + after_tax_profit_over_K - delta`；历史 used `ra=clip(ra0,.02,.09)` 的 bounds 继续只属于 `EMPIRICAL_NUMERICAL_SAFEGUARD`。Owner 已冻结 raw `ra0` 为最终 K1 household illiquid payoff source object；不做 calendar annualization，不宣称外部 market-return mapping。

## Bootstrap/timing：Owner 已冻结方案2
Accepted initialization 的31个 province states 中 `ra0=0/31`，因此不能在首轮真实使用 prior-completed raw `ra0`。Owner 已明确冻结：

- Control 与 Raw 从同一 accepted initialization 开始；
- turn 1 为共同 bootstrap，二者都使用 entering clipped/source-used `ra`；
- turn 1 完成后，各自 firm state 产生并持久化 provenance-safe raw `ra0`；
- 从 turn 2 开始，Control 继续使用本路径 prior-completed clipped/source-used `ra`；
- 从 turn 2 开始，Raw 使用本路径 prior-completed raw `ra0`；
- quantity/payoff 继续使用同一 `S`；
- 不允许 same-turn feedback 或 cross-path return borrowing。

计数语义：每条最多5个 completed outer turns。turn 1 单独报告为 bootstrap；raw-payoff treatment horizon 为 turns 2-5，最多4个 treatment turns。

## 当前 active safety gate
当前 exact task 只比较 pure-geographic `beta_distance=2`, `beta_return=0` 下：

- Control C：turn1 bootstrap clipped `ra`；turns2-5 clipped `ra`；
- Raw R：turn1 bootstrap clipped `ra`；turns2-5 raw `ra0`。

除 payoff source 外 scientific inputs 必须一致。任务重点是 short-horizon HJB/KKT/control/drift/NaN/Inf/accounting/provenance safety，不是25-turn convergence或steady-state acceptance。

## K1B / K2 / KFE
K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；其 z-scored raw `ra0` 只用于 destination attractiveness，不是 payoff。K2不授权。

corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning 仍是独立 KFE blocker。当前任何 K1 结论均不构成 steady-state、KFE、annual/IRF/welfare 或 Results acceptance。
