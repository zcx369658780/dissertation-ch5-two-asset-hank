# Chapter 5 当前规则入口

更新：2026-09-20；治理修订仍为 `CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：

`zcx369658780/dissertation-ch5-two-asset-hank`

开始任何工作先读取：

1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_20260920_1112_REVIEWER_CHECKPOINT.md`
6. `docs/CH5_MP4C_K1A_RAW_RA0_PAYOFF_OWNER_ADOPTION_20260920.md`
7. `docs/CH5_MP4C_K1A_RAW_RA0_PATH_B_TURN1_31_PROVINCE_FIXED_PRICE_ONE_STEP_CROSS_SECTION_ACCEPTANCE_20260920.md`
8. `docs/CH5_MP4C_2018_KFE_D123_CHECKPOINT11_TERMINAL_SOURCE_FREE_KFE_VALIDATION_ACCEPTANCE_20260920.md`
9. `docs/CH5_MP4C_2018_CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATE_AND_ADAPTER_BINDING_ACCEPTANCE_20260920.md`
10. `docs/CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_NONNEGATIVITY_FAILURE_ACCEPTANCE_20260920.md`
11. `docs/CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_SUPPORT_FORENSIC_ACCEPTANCE_20260920.md`
12. current active task.

Current status:

`RUN003_TRANSIENT_ONLY_NEGATIVITY_FORENSIC_ACCEPTED__UNIQUE_CLOSED_CLASS_KFE_METHOD_CANDIDATE_DIAGNOSTIC_ACTIVE`.

Current active Builder task:

`tasks/CH5_MP4C_CORRECTED_OPTIONB_BEIJING_UNIQUE_CLOSED_CLASS_KFE_METHOD_CANDIDATE_DIAGNOSTIC_20260920.md`.

Results eligibility=`FALSE`.

Important current facts:

- Beijing corrected HJB checkpoint 12 is accepted;
- exact-positive topology has one unique 400-state closed communicating class and 400 transient states;
- full-space GESVD rank/nullity is 799/1;
- the current full-space stationary candidate fails the frozen per-entry nonnegativity floor;
- accepted forensic classification A proves all 14 floor breaches are transient-only;
- all 400 closed-class entries are strictly positive and have zero floor breaches;
- current KFE status remains FAIL and no KFE method has changed;
- the active task is a bounded method-candidate diagnostic: solve only the accepted closed-class Q block once, embed exact zero transient mass by support construction, and test the candidate against the original full Q;
- this diagnostic cannot adopt the method or rerun the 31-province model;
- turn 2, K1B, K2, GE and Results remain closed.
