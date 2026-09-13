# Chapter 5 当前规则入口
更新：2026-09-13；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. accepted bilateral-capital / scoring-data / payoff / annual-HJB / price-guard authority docs
6. `docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC_ACCEPTANCE.md`
7. `docs/CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_SAME_INPUT_DIAGNOSTIC_ACCEPTANCE.md`
8. `docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_COARSE_3X3_SCAN_ACCEPTANCE.md`
9. `docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_FREEZE_CURRENT.md`
10. active exact task：`tasks/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_3X3_SCAN.md`

当前状态：`STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_3X3_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_3X3_SCAN.md`。
Results eligibility=`FALSE`。

Accepted coarse scan：9/9 HJB converged；0 invalid transition matrix；`ra=.02/.055`均为lower-a-bound ambiguous，`ra=.09`均为upper-a-boundary pile-up；wage方向在粗网格中未形成HJB failure。下一步只沿`ra`在`.055`与`.09`之间做预注册 refinement，不改HJB/KFE算法，不跑全局模型。

Refinement grid：`rb=.02`；`ra={.065,.0725,.08}`；`w={.8,1.05,1.3}`。只允许九个Cartesian points。目标是寻找从`amin`集中向`amax`集中之间是否存在interior illiquid-asset distribution。不得新增自适应点、不得调solver/tolerance/grid/derivative floor/FOC/selector/boundary/KFE。

KFE caveat：accepted standalone MATLAB-faithful contaminated-row KFE仅用于独立household domain mapping；corrected-2018 multi-province finite-box upper-b leakage/MATLAB-style pinning blocker仍独立未解决。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
