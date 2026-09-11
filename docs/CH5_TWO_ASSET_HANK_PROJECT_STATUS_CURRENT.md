# Chapter 5 两资产 HANK 当前状态
更新：2026-09-12。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_RAW_RA0_PAYOFF_SAFETY_BLOCKED_PRE_RUN_ACCEPTED__OWNER_BOOTSTRAP_DECISION_PENDING`。

最新 accepted payoff-return re-audit candidate：`e6297bb19e10a77593e1c2c7876eb94f02c71533`。
Owner payoff contract：raw `ra0` 已冻结为最终 K1 household illiquid payoff source object，解释为 `MODEL_TIME_RETURN_RATE__CALENDAR_PERIOD_UNRESOLVED` 与 `INTERNAL_MODEL_PRODUCTIVE_CAPITAL_RETURN_NUMERAIRE__EXTERNAL_MARKET_MAPPING_UNRESOLVED`。
最新 raw-payoff safety Builder candidate：`2c29a38b153ee56e58c833297b7dad2da639d6e7`。
Reviewer acceptance：`docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOUNDED_RUNTIME_SAFETY_DIAGNOSTIC_ACCEPTANCE.md`。
当前 active Builder task：NONE。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

资本网络总体科学设计冻结稿：`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
K1 scoring/data 冻结稿：`docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`。
Payoff-return 冻结稿：`docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`。

## K1 capital network：已真实进入 bounded runtime
K1 bilateral capital network 已不是离线测试对象。Accepted K1A adapter/runner 已在 corrected-2018 bounded route 中实际替换 capital allocation，使用 destination-by-origin `S` 同时分配 private capital quantity 与 household `rah`，并已完成 equal-share `beta_distance=0` 与 pure-geographic `beta_distance=2` 两条 25-turn symmetric paths。1550 province-turn 中 capital conservation、home retention、quantity/rah same-`S`、C1 residual-public-assets 与 source-faithful labor gates 均闭合。geography 差异从 turn 2 开始经 network-produced `rah` 传播到 household、Y、wage 与后续 firm states。

Legacy allocator 仍作为 source-faithful/reference route 保留；K1 network 尚未被宣布为无条件 production/default steady-state route，因为 payoff runtime safety、K1B、KFE 等后续科学门仍未完成。

## Payoff-return authority：raw `ra0` 已冻结，runtime switch 尚未通过
Payoff-return re-audit 已接受：source raw `ra0 = rk + after_tax_profit_over_K - delta`；历史 used `ra=clip(ra0,.02,.09)` 的 bounds 继续只属于 `EMPIRICAL_NUMERICAL_SAFEGUARD`。Owner 已冻结 raw `ra0` 为最终 K1 household illiquid payoff source object；不做 calendar annualization，不宣称外部 market-return mapping。

最新 bounded runtime-safety task 在 pre-run gate 正确停止：accepted initialization 的31个 province states 中 `ra0=0/31`，但 `ra/rah/rk=31/31`。completed firm turn 会把 `ra0` 持久化到下一 state，因此 provenance-safe raw payoff 只从完成 turn 1 后可用。Builder 没有自行发明 turn-1 bootstrap，也没有启动任何 trajectory/HJB/KFE；新增科学调用全部为0。

`RAW_RA0_PAYOFF_SHORT_HORIZON_RUNTIME_SAFETY_SUPPORTED` 当前不成立，因为 Raw path 未运行。

## 当前 Owner scientific gate
下一步必须冻结初始化/时序语义，二选一：

1. 提供含31省 provenance-bound prior-completed `ra0` 的 accepted initialization；或
2. 共同 turn-1 使用 accepted entering clipped/source-used `ra` 作为 bootstrap，Control 与 Raw 在 turn 1 完全相同；完成 turn 1 后，两者从同一 completed firm state 获得 raw `ra0`，Raw 从 turn 2 开始使用 `S'ra0`，Control 继续使用 `S'ra`。

Reviewer 推荐方案2：它不修改 accepted initialization，不虚构 prior raw return，且保持两条实验路径在 raw payoff 真正可得之前完全同源。该选择仍属于 Owner scientific freeze；确认前不发布 successor Builder task。

## K1B / K2 / KFE
K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；其 z-scored raw `ra0` 只用于 destination attractiveness，不是 payoff。K2不授权。

corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning 仍是独立 KFE blocker。当前任何 K1 结论均不构成 steady-state、KFE、annual/IRF/welfare 或 Results acceptance。
