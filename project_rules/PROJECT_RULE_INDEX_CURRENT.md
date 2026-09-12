# Chapter 5 当前规则入口
更新：2026-09-13；治理修订仍为`CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

开始任何工作先读取：
1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
6. `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
7. `docs/CH5_MP4C_K1_PAYOFF_RETURN_CONTRACT_FREEZE_CURRENT.md`
8. `docs/CH5_MP4C_K1_PAYOFF_SCALE_MAPPING_AND_DIAGNOSTIC_BOUND_POLICY_FREEZE_CURRENT.md`
9. `docs/CH5_MP4C_K1_ANNUAL_HJB_COMPLETE_RECALIBRATION_CONTRACT_FREEZE_CURRENT.md`
10. `docs/CH5_MP4C_K1_PRICE_GUARD_CONTINUATION_AND_BOUNDARY_HIT_MONITORING_FREEZE_CURRENT.md`
11. `docs/CH5_MP4C_K1_G1_VS_G2_HA_HJB_INSTRUMENTED_BOUNDED_DIAGNOSTIC_ACCEPTANCE.md`
12. `docs/CH5_MP4C_K1_TRANSFER_CONTROL_TEMPORARY_ADMISSIBILITY_SAFEGUARD_FREEZE_CURRENT.md`
13. `docs/CH5_MP4C_K1_TRANSFER_CONTROL_ADMISSIBILITY_SAFEGUARD_ZERO_SCIENCE_DESIGN_ACCEPTANCE.md`
14. 当前 active exact task 及直接相关 report/evidence。

当前状态：`K1_TRANSFER_CONTROL_ZERO_SCIENCE_DESIGN_ACCEPTED__EXPLOSIVE_RAW_TAIL_CONFIRMED__EXACT_NUMERIC_LADDER_UNRESOLVED__RAW_CANDIDATE_CENSUS_DIAGNOSTIC_ACTIVE`。
当前 active Builder task：`tasks/CH5_MP4C_K1_TRANSFER_CONTROL_RAW_CANDIDATE_CENSUS_INSTRUMENTED_BOUNDED_DIAGNOSTIC.md`。
最新 accepted transfer-control design candidate：`bdc2ecd48ca3408cf10138ee58d02383185ffd50`。
Results eligibility=`FALSE`。

Accepted zero-science design确认：raw transfer candidates存在many-orders-of-magnitude finite explosive tail，但accepted traces只保存per-array summaries/hashes/extrema witnesses，没有完整cell-level raw branch arrays；因此不能冻结exact numeric ladder，也不能把static `1e3/1e4/1e5/1e6` sensitivity thresholds升级为continuation stages。

当前preferred safeguard semantics为`C_FALLBACK_TO_EXISTING_ZERO_WITH_RAW_BRANCH_REJECTION`，理由是保留raw FOC receipt、拒绝inadmissible raw branch、继续使用already-existing zero-transfer option，并避免candidate clipping制造non-FOC endpoint surrogate。该语义尚未构成numeric implementation authority。

下一 gate 不是更多纯zero-science统计，因为缺失raw arrays无法从hash或summary反推。当前exact task重复accepted annual G1/G2 5-turn science并增加observation-only exact raw-candidate census instrumentation；每个HJB iteration × transfer branch × grid cell必须持久化raw candidate，完整census进入sealed external evidence，Git仅保存compact summaries/manifests。

本任务不得实现任何d safeguard。`chi0/chi1`、annual calibration、transfer FOC、derivative floor、return/wage guards、selector/boundary/KKT、grid/tolerance/solver、K1/C1/labor science全部冻结。不得 longer G2、G3/G4、wage relaxation、K1B/K2。

Price-bound hit monitoring继续强制；长期目标仍为`ZERO_DIAGNOSTIC_PRICE_GUARD_HITS`。KFE finite-box upper-b leakage/MATLAB-style pinning仍为独立blocker，KFE=`DIAGNOSTIC_ONLY`；standalone KKT residual=`UNAVAILABLE_IN_ACCEPTED_EVIDENCE`。

GitHub live main是repository-state authority；聊天不能替代exact task。正式发布task时同一回复必须附Codex启动prompt。
