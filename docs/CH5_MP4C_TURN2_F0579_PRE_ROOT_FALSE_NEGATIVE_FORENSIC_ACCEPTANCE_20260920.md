# Chapter 5 turn-2 F0579 pre-root false-negative forensic acceptance

Date: 2026-09-20

Reviewer verdict:

`ACCEPTED_PASS__TURN2_F0579_PRE_ROOT_BRANCH_UNIQUENESS_FALSE_NEGATIVE_CONFIRMED__NARROW_UPPER_B_NEGATIVE_ENUMERATION_REPAIR_AUTHORIZED`

## Accepted candidate

- live-main baseline: `e3ee31db239787406827df305c9b6b695aa912e7`
- Builder candidate: `5e1b898d959bea1fbbfdda84bf4d958f3b6dbbdc`
- candidate tree reported/read back by Builder:
  `39de3a2c49208c46853d0ac4700d50fe2d6262f1`
- ancestry independently verified: `2 ahead / 0 behind`, merge-base exactly baseline
- independently verified changed paths: 21
- selector.py and cost.py unchanged
- CURRENT governance files unchanged
- ordinary non-force push and remote SHA/tree readback passed.

The candidate has been fast-forwarded into live `main`.

## Accepted forensic terminal

`PASS__TURN2_BEIJING_F0579_UPPER_B_NEGATIVE_BRANCH_ROOT_FORENSIC_RUN002_COMPLETE__NO_SELECTOR_CHANGE`

Classification:

`TURN2_F0579_UPPER_B_NEGATIVE_PRE_ROOT_UNIQUENESS_FALSE_NEGATIVE_CONFIRMED`.

This is accepted.

## Exact branch result

At Beijing turn-2 checkpoint 2, flat 579, active upper-b / negative-transfer:

### Backward a-derivative branch

- root status: `ROOT_CONVERGED`
- q_b: `0.004697887028753478`
- q_a: `-0.00014542975673859096`
- d: `-1.9599082493888875`
- raw g_b: `6.661338147750939e-16`
- canonical g_b: `0`
- g_a: `1.7518552076793672`
- upper-b multiplier: `0.0003601190558881985`
- transfer-KKT residual: `5.692061405548898e-19`
- Hamiltonian: `-0.07939602714418059`
- rejection:
  `A_DERIVATIVE_DIRECTION_INCONSISTENT`
- admissible: false.

### Forward a-derivative branch

- root status: `ROOT_CONVERGED`
- q_b: `0.00470259773014529`
- q_a: `-0.0004814219651986697`
- d: `-2.1102602580753396`
- raw g_b: `1.5543122344752192e-15`
- canonical g_b: `0`
- g_a: `1.6015031989929152`
- upper-b multiplier: `0.00035540835449638687`
- transfer-KKT residual: `6.505213034913027e-19`
- Hamiltonian: `-0.07995936564187259`
- rejection reasons: none
- admissible: true.

Exactly one distinct post-root policy is admissible.

No Hamiltonian tie comparison is needed.

## Switching prerequisite

The existing interior-a switching prerequisite is false:

- d_z: `-3.7117634570682547`
- negative-transfer ratio: `-0.8630876421074211`
- implied q_b interval does not intersect the allowed upper-b multiplier domain
- strict drift crossing: false
- switching-root calls: 0.

Therefore the uniquely admissible forward branch is not superseded by an unresolved switching candidate.

## Scientific conclusion

The current selector's active-upper-b negative-transfer pre-root branch-uniqueness rejection is too early for this state.

The continuous constrained problem is not shown to be infeasible.

The false negative arises because the selector currently requires the surviving illiquid derivative branch to be unique **before** solving the branch-specific upper-b liquid equality.

At F0579:

- two illiquid derivative branches survive the pre-root screen;
- both have a unique liquid root;
- existing downstream direction/KKT/boundary checks eliminate the backward branch;
- the forward branch is uniquely admissible.

Thus the frozen downstream laws already contain the information needed to select a unique policy.

## Narrow selector authority revision

Under the Owner's standing authorization for bounded numerical/debugging corrections that do not introduce a new economic equation, calibration, boundary law, KKT law, solver, or tolerance, the Reviewer authorizes the following narrow selector enumeration repair:

For **active upper-b + negative-transfer only**:

- if multiple a-derivative branches survive the current pre-root viability screen, do not reject them solely with
  `DERIVATIVE_BRANCH_NOT_UNIQUE_BEFORE_ROOT`;
- evaluate each surviving a-derivative branch independently through the existing upper-b scalar-root procedure;
- apply all existing post-root admissibility checks unchanged;
- deduplicate policies using the existing `_same_policy` rule;
- apply the existing Hamiltonian ordering/tie rule unchanged.

No new branch is introduced.

No downstream acceptance law changes.

The current pre-root rule remains unchanged for active upper-b zero-kink and positive-transfer regimes.

The existing lower-b negative multi-branch treatment remains unchanged.

## Preservation requirement

Before a fresh turn-2 rerun, the Builder must zero-science audit the already accepted turn-1 run004 receipts and the completed turn-2 checkpoint-0/1 receipts for the exact target pattern:

`active upper_b + negative transfer + DERIVATIVE_BRANCH_NOT_UNIQUE_BEFORE_ROOT`.

If any such occurrence exists outside the known F0579 checkpoint-2 failure cell, the Builder must stop before fresh model science and report the impact set for Reviewer assessment.

If no prior accepted/reached cell uses that target rejection, the repair is proven route-local up to the failure point and a fresh turn-2 run002 is authorized.

## Evidence

Forensic run002 root:

`reports/ch5_mp4c_turn2_beijing_f0579_upper_b_negative_branch_forensic_20260920_run002/`

Sealed manifest:

`0DB648C10B42F5A8A187334FACEC123F9FD231999E09F650FE19C33114F420B4`

with 16 entries and 19,348 bytes. Independent readback PASS.

## Route consequence

The next Builder task implements only this selector enumeration repair, proves F0579 exact parity with the forensic, audits impact on accepted predecessor receipts, then performs one fresh turn-2 execution only if the zero-science preservation gate passes.

Turn 3, K1B, K2, GE and Results remain closed. Results eligibility remains `FALSE`.
