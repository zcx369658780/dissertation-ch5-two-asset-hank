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
11. current active task.

Current status:

`CORRECTED_INITIAL_TURN_RUN001_ENGINEERING_EXCEPTION_ACCEPTED__CHECKPOINT0_DIAGNOSTIC_REPAIR_AND_FRESH_REEXECUTION_ACTIVE`.

Current active Builder task:

`tasks/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_CHECKPOINT0_DIAGNOSTIC_REPAIR_AND_REEXECUTION_20260920.md`.

Results eligibility=`FALSE`.

Important current facts:

- run001 candidate `159786968d2bb47c12b0b7b88ed8aeaa6d0e8bdf` is accepted as failed evidence;
- Beijing checkpoint 0 completed native initialization, 800-cell policy map and D2/Q, then failed only in diagnostics composition before any direct HJB update;
- the failure does not establish Beijing HJB/KFE nonconvergence;
- the confirmed defect is the new driver passing nonexistent previous-checkpoint objects to comparative diagnostics;
- the successor is authorized to make a diagnostics-only repair, regression-test it before science, and perform one fresh bounded reexecution from the same accepted turn-1 initial states;
- turn 2, K1B, K2, GE and Results remain closed.
