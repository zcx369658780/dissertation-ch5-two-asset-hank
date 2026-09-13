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
10. `docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_SCAN_ACCEPTANCE.md`

当前状态：`STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_ACCEPTED__OWNER_REVIEW_TWO_DIMENSIONAL_HEALTH_REGION_REQUIRED`。
当前 active Builder task：NONE。
最新 accepted narrow-frontier candidate：`d1401fc5154a6fb77989b0de343da20329bf724a`。
Results eligibility=`FALSE`。

Accepted narrow-frontier evidence：`rb=.02`；`ra={.06,.0675,.07}`；`w={.8,1.05,1.3}`。9/9 HJB legal/converged；lower `2`、interior `2`、ambiguous `4`、upper `1`。Interior candidates only at `(.06,1.3)` and `(.0675,1.3)`。不存在对三种 wage 均 interior 的 tested scalar `ra`，也不存在 connected wage-robust scalar `ra` health band。

重要 caveat：`(.06,.8)` contaminated-row KFE 存在显著 signed pathology（`At<0`、endpoint/interior signed masses invalid as probability shares）；该点不得作为 admissible steady state。不得通过 clipping 或算法修改掩盖此现象。

科学路线：停止自动一维 `ra` refinement。下一唯一 Owner gate 为 `OWNER_REVIEW_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING`。下一步应把 accepted standalone evidence 组织为二维 `(ra,w)` household-health map，并审查现有 provincial return/wage mapping 如何把各省映射到该区域；尚未发布 successor runtime task。

HJB/KFE 算法继续冻结；不得 damping、solver/tolerance/grid/derivative-floor/FOC/selector/boundary/KFE 重设计。Standalone contaminated-row KFE 与 unresolved corrected-2018 multi-province finite-box upper-b leakage/MATLAB-style pinning blocker 分离。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
