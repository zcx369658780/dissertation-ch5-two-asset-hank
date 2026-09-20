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
10. `docs/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_RUN001_ENGINEERING_EXCEPTION_ACCEPTANCE_20260920.md`
11. `docs/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_RUN002_TERMINAL_KFE_TOPOLOGY_SERIALIZATION_EXCEPTION_ACCEPTANCE_20260920.md`
12. `docs/CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_NONNEGATIVITY_FAILURE_ACCEPTANCE_20260920.md`
13. current active task.

Current status:

`RUN003_BEIJING_HJB_TOPOLOGY_RANK_PASS__STATIONARY_MASS_ENTRYWISE_NONNEGATIVITY_FAIL__ZERO_SCIENCE_SUPPORT_FORENSIC_ACTIVE`.

Current active Builder task:

`tasks/CH5_MP4C_CORRECTED_OPTIONB_RUN003_STATIONARY_MASS_NEGATIVITY_SUPPORT_FORENSIC_20260920.md`.

Results eligibility=`FALSE`.

Important current facts:

- run001/run002 engineering defects are closed;
- run003 Beijing corrected HJB converges at checkpoint 12;
- exact-positive topology has exactly one 400-state closed communicating class and 400 transient states;
- full dense GESVD passes rank/nullity `799/1`, agreeing with the one closed class;
- the normalized stationary candidate passes stationarity, normalization, source-free accounting and total-negative-mass bounds;
- it fails the frozen per-entry nonnegativity floor: min p `-2.217909641958515e-12` versus allowed `-1.9184653865526386e-13`;
- this is accepted as a real KFE scientific failure under the current contract;
- no clipping, projection, renormalization, tolerance relaxation or alternate solver is authorized;
- the active task is zero-science only and localizes the negative mass relative to closed versus transient support;
- turn 2, K1B, K2, GE and Results remain closed.
