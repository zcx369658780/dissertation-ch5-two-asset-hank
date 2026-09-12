# Chapter 5 当前规则入口
更新：2026-09-12；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
6. `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
7. `docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`
8. `docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_BOOTSTRAP_TIMING_FREEZE_CURRENT.md`
9. 当前 active exact task 及直接相关 acceptance/report。

当前状态：`K1_RAW_RA0_PAYOFF_SHORT_HORIZON_SAFETY_ACCEPTED__HJB_DRIFT_FORENSIC_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_RAW_RA0_PAYOFF_HJB_DRIFT_ZERO_SCIENCE_FORENSIC.md`。
最新 accepted raw-payoff safety candidate：`678860073d3d5b653b8863b71f494f569960ced7`。
Reviewer acceptance：`docs/CH5_MP4C_K1_RAW_RA0_PAYOFF_COMMON_TURN1_BOOTSTRAP_SAFETY_ACCEPTANCE.md`。
Results eligibility=`FALSE`。

K1 capital network 已在 corrected-2018 bounded runtime 中真实启用并通过 capital conservation、home retention、same-`S` quantity/payoff 与 C1 accounting gates；它不是仅离线测试。Owner 已冻结 raw `ra0` 为最终 K1 household illiquid payoff source object，并冻结 common turn-1 clipped bootstrap：Raw 从turn2开始使用本路径 prior-completed `ra0 @ S`。

最新5-turn Control/Raw safety evidence 已接受：两路径都完成5 turns，turn1科学状态一致，Raw turns2-5无NaN/Inf、same-turn feedback、same-S、K1或C1 hard failure。该结果只支持 narrow short-horizon executability。

同一 evidence 同时显示严重 numerical stress：treatment HJB convergence Control=`49/124`、Raw=`12/124`，Raw turn5=`0/31` converged；Raw entering `rah` 约为Control的5.3-5.6倍，且出现很大的有限drift/transfer放大。因此该路径可以作为cleanly isolated short-horizon mechanism evidence，但不能作为稳定quantitative solution，也不能进入K1B或更长runtime。

当前 exact task 为 zero-science HJB/drift forensic：只读accepted persisted evidence与source code，按province/turn/grid/boundary/policy label定位stress，区分Control已有大drift和Raw incremental amplification，追踪`rah/r_a`进入effective return、transfer、adjustment cost、drifts和boundary laws的source chain。新增trajectory/HJB/KFE/firm/household等科学调用预算全部为0。

K1B `beta_return=.5` 仍仅 preregistered，不授权 runtime；K2不授权。corrected-2018 finite-box upper-b leakage/MATLAB-style pinning 继续是独立 KFE blocker，相关KFE均为`DIAGNOSTIC_ONLY`。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复自动附Codex启动prompt。
