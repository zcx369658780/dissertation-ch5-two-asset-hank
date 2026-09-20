# Chapter 5 当前规则入口

更新：2026-09-20；治理修订仍为 `CH5_ASTRA_WORKFLOW_2026_09_07`。

唯一活动仓库：

`zcx369658780/dissertation-ch5-two-asset-hank`

开始任何工作先读取：

1. `AGENTS.md`
2. 本索引
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_UNIQUE_CLOSED_CLASS_SUPPORT_KFE_OWNER_ADOPTION_20260920.md`
6. `docs/CH5_MP4C_RUN004_31PROVINCE_HOUSEHOLD_KFE_PASS_RAW_NEXT_PAYOFF_REDUCTION_ORDER_GUARD_ACCEPTANCE_20260920.md`
7. current active task.

Current status:

`RUN004_31_PROVINCE_HOUSEHOLD_AND_ADOPTED_KFE_ACCEPTED__RAW_NEXT_PAYOFF_REDUCTION_ORDER_GUARD_FAIL__INTEGRATION_ONLY_REPLAY_ACTIVE`.

Current active Builder task:

`tasks/CH5_MP4C_RUN004_CANONICAL_SAME_S_RAW_NEXT_PAYOFF_REPAIR_AND_INTEGRATION_ONLY_REPLAY_20260920.md`.

Results eligibility=`FALSE`.

Important current facts:

- Owner-adopted unique-closed-class terminal KFE implementation is accepted;
- fresh run004 passes 31/31 household HJB and 31/31 terminal KFE;
- 31 corrected stationary aggregates and the exact household batch are accepted;
- accepted household-batch identity is `8B7875F3BD603038E4D415D9F9FF759D4FDDC93E2E677C13BF0B649571B2EB05`;
- run004 integration consumed one labor/K1A/C1/31-firm/wage/monetary/fiscal sequence but stopped before closure at a bitwise comparison of two mathematically identical same-S reduction orders;
- the failure is accepted as an engineering/numerical identity-guard defect, not an economic payoff-law failure;
- the active successor does not rerun household HJB/KFE/aggregates;
- canonical raw-next-payoff evaluation is the adopted mathematical sum evaluated deterministically by per-origin `math.fsum` in ascending destination order;
- BLAS `raw_ra0 @ S` may be diagnostic only and is not a bitwise acceptance gate;
- turn 2, K1B, K2, GE and Results remain closed.
