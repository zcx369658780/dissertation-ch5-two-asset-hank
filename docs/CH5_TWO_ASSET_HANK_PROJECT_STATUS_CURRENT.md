# Chapter 5 两资产 HANK 当前状态

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`TURN2_F0579_FORENSIC_RUN001_SERIALIZATION_EXCEPTION_ACCEPTED__FINITE_SCREEN_PERSISTENCE_REPAIR_AND_RUN002_ACTIVE`

Results eligibility=`FALSE`。

## Accepted baseline scientific state

The corrected initial turn remains fully accepted and closed.

Turn 2 remains scientifically stopped at Beijing checkpoint 2, flat 579, where the current selector returned `NO_ADMISSIBLE_POLICY` before checkpoint-2 D2/Q assembly.

No selector law has changed.

## Accepted forensic run001 failure

Candidate:

`d104f7da14039eac36d76f81188c717df010848d`.

Acceptance:

`docs/CH5_MP4C_TURN2_F0579_FORENSIC_SERIALIZATION_EXCEPTION_ACCEPTANCE_20260920.md`.

Forensic run001:

- reproduced the persisted seven-candidate F0579 state;
- consumed one backward active-upper-b negative branch root procedure;
- evaluated 513 screen points;
- then failed while serializing the task-local root-screen receipt because the raw forensic capture contained `-Infinity`;
- did not durably persist the root result or Brent subcount;
- did not run the forward branch;
- did not evaluate switching or post-root Hamiltonian classification;
- made no selector decision.

The frozen selector helper itself uses finite saturation for root-screen residuals. The task-local forensic capture did not mirror that evidence representation.

## Active successor

`tasks/CH5_MP4C_TURN2_F0579_FORENSIC_FINITE_SCREEN_PERSISTENCE_REPAIR_AND_RUN002_20260920.md`.

The successor is limited to:

1. repair the forensic screen receipt to store the same finite-saturated values consumed by the frozen root screen;
2. prove JSON-safe persistence with zero science;
3. perform one fresh backward and one fresh forward branch root procedure;
4. apply the existing post-root KKT/direction/boundary/Hamiltonian checks;
5. return classification A/B/C/D;
6. make no selector source change and no HJB rerun.

Historical forensic run001 consumption remains immutable and separate.

Turn 3, K1B, K2, GE and Results remain closed.
