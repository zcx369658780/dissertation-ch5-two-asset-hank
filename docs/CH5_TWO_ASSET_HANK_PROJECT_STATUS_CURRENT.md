# Chapter 5 两资产 HANK 当前状态

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`CORRECTED_INITIAL_TURN_RUN001_ENGINEERING_EXCEPTION_ACCEPTED__CHECKPOINT0_DIAGNOSTIC_REPAIR_AND_FRESH_REEXECUTION_ACTIVE`

Results eligibility=`FALSE`。

## Accepted scientific foundation

Still accepted:

- corrected D1/D2/D3 household law;
- checkpoint-11 HJB convergence authority;
- same-Q11 unique source-free KFE;
- stationary Ct/Lt/At/Bt/AtTax mapping;
- opt-in corrected aggregate adapter;
- Owner Option-B raw-ra0 payoff law;
- three-point and exact 31-payoff fixed-price one-step safety progression.

## Accepted run001 failure

Accepted candidate:

`159786968d2bb47c12b0b7b88ed8aeaa6d0e8bdf`.

Acceptance:

`docs/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_RUN001_ENGINEERING_EXCEPTION_ACCEPTANCE_20260920.md`.

Run001 reached only Beijing checkpoint 0:

- source-native initialization: PASS;
- labor roots: 800/800;
- corrected policy map: 800/800 admissible;
- D2/Q: PASS;
- direct HJB updates: 0;
- KFE: 0;
- aggregates/integration: 0.

The terminal `TypeError: 'NoneType' object is not iterable` is an engineering diagnostic-composition failure caused by calling comparative policy/operator diagnostics without a previous checkpoint. No Beijing HJB/KFE scientific failure is inferred.

Run001 evidence manifest:
`F447D5DF30D302963D81EB09E68BEC72C1B89F8C1DE227936533045F9A16F315`.
Independent readback passed and pre/post code freeze matched.

## Active successor

`tasks/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_CHECKPOINT0_DIAGNOSTIC_REPAIR_AND_REEXECUTION_20260920.md`.

The successor may only repair checkpoint-0 current-only diagnostic representation in the opt-in driver, prove the repair before science, then perform one fresh bounded reexecution of the same initial-turn scientific objective using a new run002 evidence root.

Scientific laws, parameters, solver, tolerances, KFE, K1A/C1, payoff timing and integration semantics remain unchanged.

Turn 2, K1B, K2, GE and Results remain closed.
