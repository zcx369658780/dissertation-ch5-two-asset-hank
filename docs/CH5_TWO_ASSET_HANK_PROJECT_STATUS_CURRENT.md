# Chapter 5 两资产 HANK 当前状态

更新：2026-09-21。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`F0364_NEGATIVE_RATIO_SWITCHING_FALSE_NEGATIVE_CONFIRMED__INTERIOR_B_REPAIR_TURN1_POLICY_PARITY_AND_TURN2_RUN003_ACTIVE__BUILDER_EXECUTING`

Results eligibility=`FALSE`。

## Accepted corrected initial turn

The first corrected multi-province turn remains accepted under its original frozen code/evidence.

Before turn 2 continues under the new interior-b negative-ratio selector correction, its selected-policy path must be replayed exactly to prove compatibility.

## Accepted selector corrections

Already accepted:

1. active-upper-b negative-transfer branch enumeration repair;
2. Owner-adopted unique-closed-class terminal KFE.

Newly accepted forensic finding:

`docs/CH5_MP4C_TURN2_F0364_NEGATIVE_RATIO_SWITCHING_FALSE_NEGATIVE_ACCEPTANCE_20260921.md`.

F0364 proves that the implementation-only `ratio<=0` guard incorrectly suppresses an otherwise legal interior-a switching candidate at an interior liquid node.

## Narrow new implementation authority

For interior b only:

- finite negative nonzero D3 ratio may be used;
- mapped q_b endpoints are obtained by dividing both a-derivative interval endpoints by the ratio and sorting;
- the current persisted liquid derivative shadow is used as q_b;
- q_a=R*q_b must remain inside the original a-derivative interval;
- all existing direction/KKT/finite/Hamiltonian checks remain unchanged.

Not changed:

- active liquid-face negative-ratio behavior;
- ratio-zero behavior;
- D3 equations;
- boundary/KKT laws;
- root semantics;
- HJB/KFE rules.

## Mandatory historical compatibility gate

Current active task:

`tasks/CH5_MP4C_INTERIOR_B_NEGATIVE_RATIO_SWITCHING_REPAIR_TURN1_PARITY_AND_TURN2_RUN003_20260921.md`.

It must replay all 408 accepted turn-1 household policy maps using persisted V and the corrected selector, with zero HJB updates and zero D2/KFE work.

Every replayed selected-policy identity must exactly equal the accepted persisted identity.

Any mismatch blocks turn 2 and requires a separately authorized turn-1 reexecution.

Only exact parity authorizes fresh turn-2 run003.

Turn 3, K1B, K2, GE and Results remain closed.


## Session checkpoint while task executes

The active Builder task is currently executing. No new scientific result, candidate SHA, turn-1 parity verdict or turn-2 run003 verdict has been accepted yet.

Authoritative handoff checkpoint:

`docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_20260921_INTERIOR_B_NEGATIVE_RATIO_REPAIR_TURN1_PARITY_TURN2_RUN003_EXECUTING.md`

The next Reviewer must verify the mandatory 408-map turn-1 selected-policy identity parity gate before accepting any evidence that fresh turn-2 run003 legitimately proceeded.
