# Chapter 5 两资产 HANK 当前状态
更新：2026-09-12。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1_RAW_RA0_HJB_DRIFT_FORENSIC_ACCEPTED__OWNER_PAYOFF_MAPPING_SCALE_DECISION_REQUIRED`。

最新 accepted raw-payoff short-horizon safety candidate：`678860073d3d5b653b8863b71f494f569960ced7`。
最新 accepted zero-science forensic candidate：`cd5abea31cfbfcdb4170970df7e0504b394571d5`。
Reviewer acceptance：`docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_HJB_DRIFT_ZERO_SCIENCE_FORENSIC_ACCEPTANCE.md`。
当前 active Builder task：NONE。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

资本网络总体科学设计冻结稿：`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
K1 scoring/data 冻结稿：`docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`。
Payoff-return 冻结稿：`docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`。
Bootstrap/timing 冻结稿：`docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOOTSTRAP_TIMING_FREEZE_CURRENT.md`。

## K1 capital network：bounded runtime 已接受
K1 bilateral capital network 已在 corrected-2018 bounded K1A route 中真实运行；equal-share `beta_distance=0` 与 pure-geographic `beta_distance=2` 均完成25 turns。quantity/payoff 使用同一 destination-by-origin `S`，capital conservation、home retention、C1 residual-public-assets 与 source-faithful labor gates 已有 accepted evidence。Legacy allocator 仅作为 source-faithful/reference route 保留。

## Raw payoff short-horizon safety：已接受但数值压力显著
Owner 已冻结 raw `ra0` 为最终 K1 household illiquid payoff source object，并冻结 common turn-1 clipped bootstrap；Raw 从 turn2 起使用本路径 prior-completed raw `ra0`。5-turn bounded safety 中 Control/Raw 均完成5 turns，provenance、same-S、K1/C1 accounting、source-faithful labor和NaN/Inf hard-stop gates均通过，但 Raw HJB convergence 显著恶化：treatment turns 2-5 Control `49/124`，Raw `12/124`，Raw turn5 `0/31` converged。该结果只支持 short-horizon executability，不支持稳定量化解、25-turn、steady-state或K1B。

## Zero-science HJB/drift forensic：已接受
Accepted classification：`RAW_PAYOFF_SCALE_EXPOSURE_PROPAGATES_THROUGH_ACCEPTED_VALUE_DERIVATIVE_TRANSFER_COST_LAW__UPPER_A_BOUNDARY_REGIME_EXPANDS__MIXED_BASELINE_EXTREMES__OWNER_DECISION_REQUIRED`。

Forensic 证明 stress 不是单一 boundary bug：top Raw drift/transfer/cost extreme cells 中绝大多数位于 interior；raw payoff 提高 `rah/r_a` 后，经 accepted HJB value derivatives 与 raw-`V_b` transfer FOC 放大为 large `d`，quadratic adjustment cost 再形成 huge negative `mu_b`。Raw 同时显著扩张 upper-a outward regime，但 upper-b large outward counts 是 Control 已存在的 legacy/source behavior，并非 Raw 独有。

Control 本身也包含巨大有限 transfer/cost/drift extremes；在相当数量 matched province-turn maxima 中 Raw 小于 Control，因此不能把所有 large values 归因于 Raw。另一方面，Raw treatment 明显增加 HJB nonconvergence、iteration-ceiling hits 和 upper-a outward events，说明当前 raw payoff scale 与既有 household transfer/cost law 的组合尚未获得 scientific/numerical acceptance。

Lower-b exact-sign outward counts均约为 `-8.88e-16`，低于 accepted `1e-12` drift tolerance，属于 sign-level floating-point noise，不构成 material KKT/boundary failure。Standalone KKT residual 仍 `UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。

## 当前 Owner scientific gate
下一步必须由 Owner 决定 payoff mapping / scale interpretation。Reviewer 当前不建议：
- 直接跑25-turn Raw；
- 直接进入K1B；
- 为求收敛调整solver/tolerance/grid；
- 将历史 `[.02,.09]` clipping 恢复为最终 structural payoff law；
- 把现有 evidence 误解为 boundary-law failure。

最需要决定的是：raw firm `ra0` 是否应以当前 level 直接作为 household HJB `r_a`，还是需要一个有经济来源的 period/scale mapping。任何 mapping、annualization、normalization、cap 或 transformed payoff 都是新的 scientific contract，必须先由 Owner 冻结并有来源/解释，不能由 Builder自行选择。

## K1B / K2 / KFE
K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；其 z-scored raw `ra0` 只用于 destination attractiveness，不是 household payoff。K2不授权。

corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning 仍是独立 KFE blocker。当前任何 K1 结论均不构成 steady-state、KFE、annual/IRF/welfare 或 Results acceptance。
