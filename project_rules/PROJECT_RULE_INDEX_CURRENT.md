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
12. current active task.

Current status:

`RUN002_BEIJING_HJB_CONVERGENCE_ACCEPTED__TERMINAL_KFE_TOPOLOGY_SERIALIZATION_EXCEPTION_ACCEPTED__SERIALIZATION_AND_LEDGER_REPAIR_RUN003_ACTIVE`.

Current active Builder task:

`tasks/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_TERMINAL_KFE_TOPOLOGY_SERIALIZATION_REPAIR_AND_RUN003_REEXECUTION_20260920.md`.

Results eligibility=`FALSE`.

Important current facts:

- run001 checkpoint-0 diagnostics defect is repaired and accepted;
- run002 Beijing exact initial-state corrected HJB converged at checkpoint 12 with B/D inside the frozen thresholds and all 12 direct solves below the backward-error bound;
- terminal KFE then executed one SCC decomposition but failed before topology receipt persistence because the raw topology dictionary contains a CSR adjacency and NumPy labels;
- no closed-class count, rank/nullity, stationary mass or aggregate is accepted from run002;
- run002 sealed global ledger SCC=0 is an exception-path undercount; accepted zero-science reconciliation establishes actual SCC=1;
- the active successor authorizes only topology-specific JSON persistence repair, exception-path call-ledger repair, zero-science regression tests, and one fresh run003 under unchanged science;
- turn 2, K1B, K2, GE and Results remain closed.
