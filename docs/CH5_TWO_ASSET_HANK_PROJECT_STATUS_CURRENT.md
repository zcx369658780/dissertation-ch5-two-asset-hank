# Chapter 5 两资产 HANK 当前状态
更新：2026-09-12。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1A_PAYOFF_RETURN_REAUDIT_ACCEPTED__OWNER_PAYOFF_CONTRACT_FREEZE_PENDING`。

最新 accepted payoff-return re-audit candidate：`e6297bb19e10a77593e1c2c7876eb94f02c71533`。
Reviewer acceptance：`docs/CH5_MP4C_K1A_PAYOFF_RETURN_REAUDIT_ACCEPTANCE.md`。
当前 active Builder task：NONE。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

资本网络总体科学设计冻结稿：`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
K1 scoring/data 冻结稿：`docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`。

## K1A symmetric bounded rerun：已接受
两条 preregistered 路径均完成25/25 turns：equal-share `beta_distance=0` 与 pure-geographic `beta_distance=2`，两者均 `beta_return=0`。两条路径保持 fixed `theta_i=inter_prv_ratio_i`、source-faithful labor、smoothing OFF、C1 `GovInv=max(Ktarget-Kprivate,0)` 与 transitional source-used/clipped-`ra` payoff bridge。

接受证据：1550 province-turn 中 capital share/origin/national conservation、home retention、quantity/rah same-`S` 与 C1 逐省逐轮闭合；destination-theta double weighting=0；`Kprivate>=Ktarget`=0/0，private-only overshoot=0/0；total K/target 两路径均约为1。geography差异从turn2开始经network-produced `rah`进入household并传播到Y、wage及后续firm states。

两路径turn25均未满足冻结final predicate：A/B `max_nk_gap`约为`1.94e-9 / 1.86e-9`，均高于`1e-9`。不得因此修改阈值。KFE仍全部`DIAGNOSTIC_ONLY`。

## Payoff-return re-audit：已接受
Accepted classification：`CLIPPED_RA_REMAINS_ONLY_TRANSITIONAL_BRIDGE__RAW_RA0_IS_SOURCE_CONSISTENT_CANDIDATE_REQUIRING_OWNER_PERIOD_NUMERAIRE_FREEZE`。

Source audit确认 active `ra0 = rk + after_tax_profit_over_K - delta`，source-used `ra` 是将 `ra0` 截到 `[.02,.09]` 后的 runtime object；K1A 使用同一 destination-by-origin `S` 同时分配资本数量和聚合 household illiquid payoff `rah`。lagged payoff timing 与 persisted same-`S` provenance 在授权范围内闭合。

对称rerun的 upper clips：Path A `754/775`，Path B `755/775`；lower clips均为0；30省在25 turns中全部 upper-clipped。used return 每轮仅1–2个 unique values，说明 clipping 基本消除了横截面 payoff ordering。`[.02,.09]`继续只属于`EMPIRICAL_NUMERICAL_SAFEGUARD`，不得升级为 economic calibration authority。

raw `ra0` 重建最大残差为`5.551115123125783e-17`，压力主要来自`rk`。holding persisted `S` fixed 的 zero-feedback arithmetic 给出 `S'ra0-S'ra_used` median约`.172`、max约`.95`；这只证明 clipped bridge 与 raw source object 在 payoff level 上差异巨大，不证明 raw-payoff trajectory 会收敛。

raw `ra0` 现可列为 source-consistent payoff candidate，但 model-period/calendar periodicity、最终 economic numeraire/payoff interpretation 与 runtime safety 尚未冻结。因此 current clipped/used `ra` 仍只能作为 transitional bridge，且目前不得切换 runtime payoff。

## 当前 Owner scientific gate
下一步不是 Builder task，而是 Owner/Reviewer 冻结 payoff-return contract。必须明确：
- 是否将 raw `ra0` 作为最终 household illiquid payoff source object；
- 模型 period / calendar interpretation；
- payoff/numeraire convention；
- 是否接受 raw level 进入 HJB 的经济含义。

只有 Owner freeze 完成后，Reviewer 才能发布一个新的 bounded runtime-safety diagnostic exact task；在该 gate 通过前不得进入 K1B runtime。

## K1B / K2 / KFE
K1B `beta_return=0.5` 仍仅为 preregistered，不授权 runtime。K1B attractiveness 仍冻结为 completed-iteration raw unclipped `ra0` cross-sectional z-score，只能用于 destination attractiveness，不能替代 household payoff。K2不授权。

corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning 仍是独立 KFE blocker。当前任何 K1A 结论均不构成 steady-state、KFE、annual/IRF/welfare 或 Results acceptance。
