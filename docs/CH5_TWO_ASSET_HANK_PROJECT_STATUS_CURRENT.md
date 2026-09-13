# Chapter 5 两资产 HANK 当前状态

更新：2026-09-13。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：`WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT_CANDIDATE_PUBLISHED__INDEPENDENT_REVIEW_REQUIRED`。

最新 accepted narrow-frontier candidate：`d1401fc5154a6fb77989b0de343da20329bf724a`。
Reviewer acceptance：`docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_SCAN_ACCEPTANCE.md`。
Owner/Reviewer freeze：`docs/CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_FREEZE_CURRENT.md`。
当前 active Builder task：`NONE`；未发布 successor task。
Results eligibility=`FALSE`。

Accepted terminal classification：`ALL_HJB_LEGAL_CONVERGED__NO_WAGE_ROBUST_INTERIOR_RA__TWO_DIMENSIONAL_HEALTH_REGION_REQUIRED`。

Accepted standalone evidence shows no universal scalar `ra` health band across tested wages. The next task therefore stops one-dimensional `ra` refinement and performs an evidence-only two-dimensional `(ra,w)` health-region / provincial mapping audit.

The task first constructs the observed standalone health map from accepted points, then audits wage semantics and scaling end-to-end (`wjt` -> any source-defined transformation -> exact wage object consumed by the household HJB). Provincial projection is allowed only if this wage comparability/mapping gate is proven. If standalone `w` and the actual multi-province HJB wage input are not directly comparable and no source-defined deterministic transformation is proven, projection must stop with a mapping/scaling blocker.

No new HJB or KFE calls are allowed. No global outer turns, MATLAB, firm, K1B/K2, GE, downstream, shock, IRF or Results runtime. Existing accepted turn-1/turn-2 provincial HJB-input evidence may be parsed and compared only after the wage-semantic gate passes.

Important boundary remains: `(.06,.8)` standalone contaminated-row KFE has severe signed pathology and is not an admissible healthy point. No interpolation may create new healthy labels for unobserved `(ra,w)` coordinates.

Standalone contaminated-row KFE remains separate from the unresolved corrected-2018 multi-province finite-box upper-b leakage and MATLAB-style pinning blocker.

Builder audit candidate 已完成：wage semantic gate=`WAGE_VARIABLE_IDENTITY_PROVEN_DIRECTLY_COMPARABLE`。Standalone `w` 与省级 HJB consumed `results.w` / `HouseholdInputs.wages[0]` 是同一对象；guarded `wjt` 是上游 firm wage，必须经 source-defined aggregation 生成 composite wage，不能直接作为 standalone coordinate。

Observed map 汇总 accepted 27 点；canonical counts 为 interior=4、ambiguous=7、lower=7、upper=8、KFE pathological=1。Accepted provincial projection 共 62 行，但两轮各 31/31 都是 `UNOBSERVED_OR_INTERPOLATION_NOT_AUTHORIZED`：省级 composite wage 范围约 `12.84–18.52`，完全超出 standalone `.8–1.3` coverage。

报告：`docs/CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT_REPORT.md`。Compact evidence：`docs/evidence/ch5_mp4c_k1_ra_w_health_region_provincial_mapping/`。Scientific runtime 全部为 0。

唯一当前 gate：ChatGPT Reviewer 独立 ACCEPT/REJECT。唯一建议但未授权的 Owner gate：`OWNER_REVIEW_TWO_DIMENSIONAL_HEALTH_REGION_UNRESOLVED`。不要 merge main。
