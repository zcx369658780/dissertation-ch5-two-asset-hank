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
11. `docs/CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_FREEZE_CURRENT.md`
12. active exact task：`tasks/CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT.md`

当前状态：`WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT_TASK_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT.md`。
最新 accepted narrow-frontier candidate：`d1401fc5154a6fb77989b0de343da20329bf724a`。
Results eligibility=`FALSE`。

Accepted narrow-frontier evidence：9/9 HJB legal/converged；不存在对 `w={.8,1.05,1.3}` 全部 interior 的 tested scalar `ra`。停止自动一维 `ra` refinement，健康域视为二维 `(ra,w)` 问题。

当前 audit 只做 accepted evidence integration 和 source-trace。第一 gate 是 wage semantics/scaling：必须证明 standalone scan 的 `w` 与 multi-province household HJB 实际消费的 wage object 是否相同/可由 source-defined deterministic mapping 转换。没有证明时不得把 `wjt` 或 composite wage 强行投影到 standalone health map。

若 wage gate 通过，才允许复用 accepted turn-1/turn-2 provincial HJB input evidence 做 conservative projection；非 exact observed coordinates 默认 `UNOBSERVED_OR_INTERPOLATION_NOT_AUTHORIZED`，不得靠插值制造 healthy label。

Scientific runtime 全部为零：HJB=0、KFE=0、outer turns=0、MATLAB=0、firm=0、K1B/K2=0、GE/downstream/shock/IRF/Results=0。HJB/KFE算法继续冻结。

Important caveat：`(.06,.8)` standalone KFE 有 severe signed pathology，不是 admissible steady state。Standalone contaminated-row KFE 与 unresolved corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker 继续分离。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
