# Chapter 5 corrected-2018 three-turn propagation — Reviewer acceptance of controlled failure

Date: 2026-09-09.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Accepted candidate: `8b80b491421603b94a281211d683d94e2a78fdaf`.

## Verdict

Reviewer marker: `CORRECTED_2018_THREE_TURN_CONTROLLED_FAIL_ACCEPTED__PERSISTENCE_COLLISION_ONLY__REEXECUTION_REQUIRED`.

Accept the candidate terminal verdict `CORRECTED_2018_THREE_TURN_FAIL__UPSTREAM_STATE_OR_FIRM_BLOCKER` only as a controlled execution failure with terminal classification `EVIDENCE_PERSISTENCE_COLLISION_AFTER_TURN2__TURN3_NOT_ENTERED`.

This is not evidence of a household, HJB, KFE, firm, controller, or economic-state failure.

## Accepted findings

1. Fresh corrected-2018 turn 1 and turn 2 reproduced the previously accepted two-turn evidence with `mismatch_count=0`.
2. Exactly one scientific process was started. It completed 2 turns / 62 province updates. All 62 household, HJB, KFE, aggregate, and firm calls returned. Scientific retries were 0.
3. Before turn 3 entry, the runner attempted a second exclusive persistence write to `predecessor_reproduction.json`, raising `FileExistsError`. Therefore turn 3 was not entered and all turn-3 scientific observables remain `NOT_CHECKED`.
4. No formula-derived or prepared-state value is promoted to a turn-3 scientific observation.
5. The executed runner identity was preserved. A one-line persistence-sequencing repair was then implemented and static-tested, but the repaired runner was not scientifically executed. The failed task therefore remains FAIL.
6. The repair is accepted as an engineering evidence-persistence fix only. It does not alter model equations, canonical inputs, state-transition semantics, capital allocation, firm behavior, household behavior, controller logic, numerical methods, grids, bounds, solvers, or tolerances.
7. Turn 4, steady state, GE, annual model, IRF and Results remained unexecuted and unauthorized.

## Next authority

A new exact task is required for one fresh three-turn scientific reexecution on the repaired runner. The previous failed process does not authorize an implicit retry.

Results eligibility = FALSE.
