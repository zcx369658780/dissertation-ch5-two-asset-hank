# Chapter 5 两资产 HANK 当前状态

更新：2026-09-20。唯一活动仓库：`zcx369658780/dissertation-ch5-two-asset-hank`。

状态：

`TURN2_UPPER_B_NEGATIVE_REPAIR_ACCEPTED__BEIJING_CHECKPOINT5_F0364_SELECTOR_FAIL__NEGATIVE_RATIO_INTERIOR_A_SWITCHING_FORENSIC_ACTIVE`

Results eligibility=`FALSE`。

## Accepted corrected initial turn

The first corrected multi-province turn remains fully accepted and closed.

## Accepted selector repair

The active-upper-b negative-transfer branch enumeration correction is accepted.

It changes only pre-root enumeration control flow and leaves all root/KKT/boundary/direction/Hamiltonian laws unchanged.

F0579 exact runtime parity passed.

## Fresh turn-2 run002

Candidate:

`55dd5b81f1749e2af9e8d2a9a2507803b514131d`.

Acceptance:

`docs/CH5_MP4C_TURN2_RUN002_F0364_SELECTOR_FAILURE_ACCEPTANCE_20260920.md`.

Only Beijing was reached.

Checkpoints 0 through 4 passed policy map, D2/Q and direct-solve gates.

The first new failure is checkpoint 5 / flat 364:

- index `(4,18,0)`
- b `-0.5263157894736843`
- a `9.473684210526315`
- z `0.8`
- outcome `NO_ADMISSIBLE_POLICY`
- checkpoint-5 D2/Q not assembled.

## F0364 scientific uncertainty

F0364 has no active geometric face.

For negative transfer under p_b backward:

- a-backward ordinary candidate has g_a > 0 and fails backward-a direction;
- a-forward ordinary candidate has g_a < 0 and fails forward-a direction.

This is a strict interior-a drift crossing.

The current switching constructor computes zero-a-drift transfer
`d_z=-r_a*a`
and a D3 shadow ratio
`q_a/q_b=-0.7547777451261338`,
then returns no switching candidate because the implementation requires the ratio to be positive.

No scientific decision has yet been made on whether that positivity guard is required authority or an implementation false negative.

## Active task

`tasks/CH5_MP4C_TURN2_BEIJING_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_FORENSIC_20260920.md`.

The task uses the persisted cell only, performs no roots and no HJB rerun, evaluates the sign-aware switching geometry under the existing D3/KKT equations, audits whether positive ratio/q_a is an explicit accepted scientific domain law, and returns A/B/C/D.

Turn 3, K1B, K2, GE and Results remain closed.
