# Chapter 5 两资产 HANK 当前状态
更新：2026-09-11。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1A_SYMMETRIC_BOUNDED_RERUN_ACCEPTED__PAYOFF_RETURN_REAUDIT_ACTIVE`。

最新 accepted K1A symmetric rerun candidate：`ca66dd5d7364f80ed2686d4d2e77a1a6adab2ecb`。
Reviewer acceptance：`docs/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_SYMMETRIC_RERUN_ACCEPTANCE.md`。
当前 active Builder task：`tasks/CH5_MP4C_K1A_PAYOFF_RETURN_REAUDIT.md`。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

资本网络总体科学设计冻结稿：`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
K1 scoring/data 冻结稿：`docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`。

## K1A symmetric bounded rerun：已接受
两条 preregistered 路径均完成25/25 turns：equal-share `beta_distance=0` 与 pure-geographic `beta_distance=2`，两者均 `beta_return=0`。两条路径保持 fixed `theta_i=inter_prv_ratio_i`、source-faithful labor、smoothing OFF、C1 `GovInv=max(Ktarget-Kprivate,0)` 与 transitional source-used/clipped-`ra` payoff bridge。

接受证据：1550 province-turn 中 capital share/origin/national conservation、home retention、quantity/rah same-`S` 与 C1 逐省逐轮闭合；destination-theta double weighting=0；`Kprivate>=Ktarget`=0/0，private-only overshoot=0/0；total K/target 两路径均约为1。geography差异从turn2开始经network-produced `rah`进入household并传播到Y、wage及后续firm states。

两路径turn25均未满足冻结final predicate：A/B `max_nk_gap`约为`1.94e-9 / 1.86e-9`，均高于`1e-9`。不得因此修改阈值。KFE仍全部`DIAGNOSTIC_ONLY`。

## 当前主要 scientific blocker：payoff-return authority
K1A当前 payoff 仍为 `K1A_SOURCE_FAITHFUL_PAYOFF_BRIDGE__NOT_FINAL_ECONOMIC_RETURN_AUTHORITY`。对称rerun显示持续严重 upper clipping pressure：Path A raw `ra0>.09`=`754/775`；Path B=`755/775`；两路径 lower clips=0。因此历史 `[.02,.09]` 不能升级为最终经济authority，也不能未经审计直接切换为 raw `ra0` payoff。

当前 exact task `CH5_MP4C_K1A_PAYOFF_RETURN_REAUDIT` 只允许读取 accepted source 与已持久化K1A evidence，厘清 `ra0`、used/clipped `ra`、`rah` 的 source semantics、单位/周期、decomposition 与 clipping distortion，并评估候选 payoff contract。新 HJB/KFE/firm/trajectory 等科学调用预算全部为0。

## K1B / K2 / KFE
K1B `beta_return=0.5` 仍仅为 preregistered，不授权 runtime。K1B attractiveness 仍冻结为 completed-iteration raw unclipped `ra0` cross-sectional z-score，只能进入下一 outer iteration。K2不授权。

corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning 仍是独立 KFE blocker。当前任何 K1A 结论均不构成 steady-state、KFE、annual/IRF/welfare 或 Results acceptance。
