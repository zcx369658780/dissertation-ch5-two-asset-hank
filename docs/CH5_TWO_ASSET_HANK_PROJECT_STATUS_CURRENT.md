# Chapter 5 两资产 HANK 当前状态

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`TURN2_F0579_PRE_ROOT_FALSE_NEGATIVE_CONFIRMED__NARROW_UPPER_B_NEGATIVE_ENUMERATION_REPAIR_AND_TURN2_RUN002_ACTIVE`

Results eligibility=`FALSE`。

## Accepted corrected initial turn

The first corrected multi-province turn remains fully accepted and closed.

## Accepted turn-2 blocker

Turn-2 run001 stopped at Beijing checkpoint 2 / flat 579 because the current selector rejected active upper-b negative transfer at a pre-root branch-uniqueness gate.

No checkpoint-2 D2/Q or later science occurred.

## Accepted F0579 forensic result

Candidate:

`5e1b898d959bea1fbbfdda84bf4d958f3b6dbbdc`.

Acceptance:

`docs/CH5_MP4C_TURN2_F0579_PRE_ROOT_FALSE_NEGATIVE_FORENSIC_ACCEPTANCE_20260920.md`.

Classification:

`TURN2_F0579_UPPER_B_NEGATIVE_PRE_ROOT_UNIQUENESS_FALSE_NEGATIVE_CONFIRMED`.

Branch result:

- backward branch root converges but fails `A_DERIVATIVE_DIRECTION_INCONSISTENT`;
- forward branch root converges and passes all existing downstream checks;
- admissible policies = 1;
- unique selected branch = forward;
- switching prerequisite = false.

Therefore the underlying constrained state is not a true no-policy point under the existing downstream laws.

## Authorized narrow repair

For active upper-b negative transfer only:

- preserve the current pre-root viability screen;
- do not reject merely because multiple a branches survive it;
- root each surviving branch independently using the existing upper-b domain and root method;
- apply unchanged post-root direction/KKT/boundary checks;
- apply unchanged policy deduplication and Hamiltonian uniqueness logic.

No equation, tolerance, calibration, KKT law, boundary law or solver changes.

## Active task

`tasks/CH5_MP4C_ACTIVE_UPPER_B_NEGATIVE_BRANCH_ENUMERATION_REPAIR_AND_TURN2_RUN002_20260920.md`.

Before fresh turn-2 science the task must scan accepted turn-1 run004 and completed turn-2 checkpoint-0/1 receipts for the exact repaired rejection pattern. Any occurrence outside F0579 blocks execution for impact review.

If preservation audit is empty, perform one fresh turn-2 run002 and stop before turn 3.

K1B, K2, GE and Results remain closed.
