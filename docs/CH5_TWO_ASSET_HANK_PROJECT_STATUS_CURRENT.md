# Chapter 5 两资产 HANK 当前状态
更新：2026-09-11。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

## 当前状态
状态：`K1A_SYMMETRIC_BOUNDED_RERUN_ACCEPTED__PAYOFF_RETURN_REAUDIT_REQUIRED_BEFORE_K1B`。

最新 accepted K1A symmetric rerun candidate：`ca66dd5d7364f80ed2686d4d2e77a1a6adab2ecb`。
Reviewer acceptance：`docs/CH5_MP4C_K1A_EQUAL_SHARE_VS_GEOGRAPHIC_BETA2_SYMMETRIC_RERUN_ACCEPTANCE.md`。
当前 active Builder task：无，待发布 payoff-return re-audit exact task。
Builder默认`gpt-5.6-sol / medium`。Results eligibility=`FALSE`。

资本网络总体科学设计冻结稿：
`docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`。
K1 scoring/data 冻结稿：
`docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`。

## K1A symmetric bounded rerun：已接受
两条 preregistered 路径均从 byte-identical accepted initialization 完成25/25 turns：

1. equal-share：`beta_distance=0`, `beta_return=0`；
2. pure-geographic：`beta_distance=2`, `beta_return=0`。

两条路径均保持 fixed `theta_i=inter_prv_ratio_i`、source-faithful labor、smoothing OFF、C1 `GovInv=max(Ktarget-Kprivate,0)` 和 transitional source-used/clipped-`ra` payoff bridge。

接受证据：
- 1550 province-turn 中 capital share/origin/national conservation、home retention、quantity/rah same-`S` 全部闭合；
- destination-theta double weighting=0；
- C1逐省逐轮闭合；`Kprivate>=Ktarget`=0/0，private-only overshoot=0/0；
- total K/target 两路径均约为1；
- geography差异从turn2开始经network-produced `rah`进入household并传播到Y、wage及后续firm states；
- Path A/B turn25均未满足冻结final predicate，`max_nk_gap`分别约`1.94e-9`和`1.86e-9`，均高于`1e-9`；
- HJB nonconverged-but-continued=88/92；
- KFE仍全部`DIAGNOSTIC_ONLY`。

## 当前主要 scientific blocker：payoff-return authority
K1A当前仍使用：

`K1A_SOURCE_FAITHFUL_PAYOFF_BRIDGE__NOT_FINAL_ECONOMIC_RETURN_AUTHORITY`

即 household payoff 暂时使用 source-used/clipped `ra`，目的仅是保持资本网络变化的 attribution，不代表历史 `[.02,.09]` return bounds 已获得经济识别。

对称rerun显示持续严重 upper clipping pressure：
- Path A raw `ra0>.09`：`754/775`；
- Path B raw `ra0>.09`：`755/775`；
- 两路径 lower clips 均为0。

因此在进入K1B之前必须先做 payoff-return re-audit，厘清 raw `ra0`、used/clipped `ra`、`rah` 的 source semantics、单位/周期、firm decomposition 和 clipping distortion。不得直接把 raw `ra0` 改成household payoff，也不得把 clipped `ra`升级为最终经济authority。

## K1B / K2 状态
K1B future benchmark `beta_return=0.5` 仍仅为 preregistered，不授权 runtime。K1B attractiveness 仍冻结为 completed-iteration raw unclipped `ra0` cross-sectional z-score，只能进入下一 outer iteration。

K2 endogenous-theta functional form继续不授权。

## KFE边界
clean/source-free generator-KFE方法学与 corrected-2018 empirical finite-box upper-b leakage/MATLAB-style pinning 必须继续分开。当前 empirical KFE blocker 未解决；K1A bounded rerun不能被写成 KFE、steady state 或 Results PASS。

## 下一步
优先发布 zero-science payoff-return re-audit exact task。该任务只使用 accepted source与已持久化K1A evidence，禁止新增HJB/KFE/firm/trajectory科学调用，也不改变现行payoff law。
