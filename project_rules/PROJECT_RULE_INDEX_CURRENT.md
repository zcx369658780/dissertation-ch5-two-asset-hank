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
11. `docs/CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT_ACCEPTANCE.md`

当前状态：`WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT_ACCEPTED__OWNER_REVIEW_TWO_DIMENSIONAL_HEALTH_REGION_UNRESOLVED`。
当前 active Builder task：NONE。
最新 accepted audit candidate：`3975d42fae57cc25f179225857b5defce1d7731f`。
Results eligibility=`FALSE`。

Accepted wage semantic gate：standalone `w` 与 provincial household-HJB consumed `results.w` / `HouseholdInputs.wages[0]` 语义/API identity 对齐；`guarded_wjt` 是上游 firm wage，必须通过 source-defined wage aggregation 后才能成为 household composite wage。不得把 `wjt` 直接用于 standalone health-map projection，也不得 outcome-fitted rescaling。

关键 coverage finding：accepted standalone map 仅观察 wage `.8/1.05/1.3`，而 accepted provincial composite wage turn1 约 `13.84–18.52`、turn2 约 `12.84–17.48`。62/62 provincial states 都在 standalone wage coverage 外，全部只能是 `UNOBSERVED_OR_INTERPOLATION_NOT_AUTHORIZED`。因此当前 map 不能给 provincial states 分配健康/不健康标签。

20/20 turn1-converged→turn2-failed 省份的 consumed `ra` 全部上升、composite wage 全部下降，但仅为描述性共变，不能证明跨越 health frontier 或构成因果。Return/wage guard 也不能唯一分离成功失败。

科学路线：不得继续自动一维 `ra` refinement，也不得直接进行 return-mapping redesign。唯一下一 Owner gate：`OWNER_REVIEW_TWO_DIMENSIONAL_HEALTH_REGION_UNRESOLVED`。应先扩展 standalone `(ra,w)` health-map coverage 到真实 provincial household composite-wage domain，再决定是否需要 provincial return mapping 调整。

Important caveat：`(.06,.8)` standalone KFE severe signed pathology 继续视为 non-admissible，不得 clipping。Standalone contaminated-row KFE 与 unresolved corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning blocker 分离。

GitHub live main 是唯一 repository authority；聊天不能替代 exact task。
