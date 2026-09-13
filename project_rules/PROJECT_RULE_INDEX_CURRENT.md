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
9. `docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_3X3_SCAN_ACCEPTANCE.md`
10. `docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_REFINEMENT_FREEZE_CURRENT.md`
11. active exact task：`tasks/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_SCAN.md`

当前状态：`STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_SCAN.md`。
最新 accepted refinement candidate：`cdaba87bae181280e182f639d4cf8fa5a5bae773`。
Results eligibility=`FALSE`。

Accepted prior refinement：9/9 HJB legal/converged；只有 `ra=.065,w={1.05,1.3}` 为 interior candidates；`.065,.8` transitional；`.0725,.8` upper-bound；`.0725` higher wages ambiguous；`.08` all wages upper-bound。不存在 wage-robust connected interior `ra` band。

Active narrow refinement：`rb=.02`；`ra={.06,.0675,.07}`；`w={.8,1.05,1.3}`。只允许9个Cartesian points，fresh initialization，除 `ra`/wage 外其他 standalone MATLAB-faithful household science/numerics 全冻结。不得改 HJB/KFE、不得 damping、不得新增自适应点、不得运行 global model。

本轮是对“是否存在 universal scalar `ra` health band”的最后一次窄区高信息量检查之一。若没有任何 tested `ra` 对三种 wage 均为 interior，后续不得自动继续一维盲扫，Owner gate 转向二维 wage-conditional `(ra,w)` health-region / provincial return-mapping review。

KFE caveat：standalone contaminated-row KFE 与 unresolved corrected-2018 multi-province finite-box upper-b leakage/MATLAB-style pinning blocker 分离。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
