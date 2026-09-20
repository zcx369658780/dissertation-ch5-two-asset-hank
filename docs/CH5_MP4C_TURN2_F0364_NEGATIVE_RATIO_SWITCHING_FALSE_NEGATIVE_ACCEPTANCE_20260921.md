# Chapter 5 turn-2 F0364 negative-ratio switching false-negative acceptance

Date: 2026-09-21

Reviewer verdict:

`ACCEPTED_PASS__F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_GUARD_FALSE_NEGATIVE__NARROW_INTERIOR_B_SIGN_AWARE_REPAIR_AUTHORIZED`

## Accepted candidate

- live-main baseline: `fddaef785bca01373492576047d574f07761d084`
- Builder candidate: `5a6f3870ceccb7730d5417e87d801ac0bc8e210a`
- candidate tree: `514ed00b9ba1bec369b677203dc2c395384452fb`
- ancestry independently verified: `2 ahead / 0 behind`, merge-base exactly baseline
- independently verified changed paths: 16
- selector.py and cost.py unchanged
- CURRENT governance files unchanged
- ordinary non-force push and remote SHA/tree readback passed.

The candidate has been fast-forwarded into live `main`.

## Accepted forensic terminal

`PASS__TURN2_BEIJING_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_FORENSIC_COMPLETE__NO_SELECTOR_CHANGE`

Classification:

`TURN2_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_GUARD_FALSE_NEGATIVE_CONFIRMED`.

This classification is accepted.

## Exact local finding

At Beijing turn-2 checkpoint 5 / flat 364:

- state is interior in both b and a;
- negative-transfer ordinary candidates under `p_b_backward` have a strict arithmetic-separated a-drift crossing;
- current selector emits no interior-a switching candidate because the implementation returns when the D3 ratio is non-positive.

The zero-a-drift equality gives:

`d_z=-r_a*a=-7.8384208979658965`.

Under unchanged D3:

`R=q_a/q_b=1-chi_0+chi_1*d_z/max(a,a_bar)=-0.7547777451261338`.

The sorted one-sided illiquid derivative interval is:

`[-0.004925792041697845,-0.0031029058502000167]`.

Mapping both endpoints through the negative ratio and sorting gives the positive liquid-shadow interval:

`[0.004111019263931103,0.006526149020033277]`.

The persisted backward liquid derivative:

`q_b=0.006091715618507631`

lies inside that interval.

The corresponding diagnostic switching shadow is:

`q_a=-0.0045978913784868415`.

It lies inside the original illiquid derivative interval.

## Unique admissible switching candidate

For the backward liquid branch:

- q_b: `0.006091715618507631`
- q_a: `-0.0045978913784868415`
- d: `-7.8384208979658965`
- g_a: `0`
- g_b: `-4.227123020026542`
- b-direction: PASS
- transfer sign: PASS
- transfer KKT: PASS with residual `0`
- finite checks: PASS
- Hamiltonian: `-0.11188508398929994`
- rejection reasons: none.

For the forward liquid branch:

- q_b lies outside the sign-aware mapped interval;
- q_a lies outside the original illiquid derivative interval;
- b-direction is inconsistent;
- candidate is inadmissible.

Exactly one sign-aware switching candidate is admissible.

## Scientific-authority audit

The accepted Owner interior-a switching authority explicitly requires:

- `q_b>0`;
- unchanged D3 KKT:
  `0 in q_a-q_b(1+partial_d C)`;
- `q_a` inside the closed sorted interval between the one-sided illiquid derivatives.

It does not independently impose:

- `q_a>0`;
- `R>0`;
- positive interior-a switching ratio.

The current `ratio<=0` rejection is therefore an implementation guard, not an adopted scientific-domain law.

The forensic conclusion is supported by the positively stated Owner contract, not merely by absence of a contrary rule.

## Narrow repair authority

Under the existing Owner-adopted interior-a zero-drift switching law and the standing authorization for bounded numerical/debugging corrections, Reviewer authorizes a narrow implementation correction for **interior liquid nodes only**:

When:

- a is interior;
- b is interior;
- ordinary one-sided a candidates form the already-adopted strict crossing;
- d_z is nonzero;
- the D3 ratio R is finite and negative;

do not reject solely because `R<=0`.

Instead:

1. compute the closed sorted a-derivative interval;
2. map both interval endpoints through division by R;
3. sort the two q_b endpoint images;
4. use the persisted liquid derivative shadow for the current b branch;
5. construct the switching candidate only through the unchanged existing switching-candidate path;
6. require q_a=R*q_b to lie in the original a-derivative interval;
7. apply all existing direction, KKT, finite, D2-admissibility, deduplication and Hamiltonian rules unchanged.

This authorization does **not** revise active liquid-face negative-ratio switching.

For active lower-b or upper-b faces, the current fail-closed ratio-sign behavior remains unchanged pending separate evidence.

Ratio zero also remains fail closed.

No new equation, tolerance, solver, KKT law, boundary law or calibration is introduced.

## Historical compatibility gate

Because the Owner interior-a switching law predates the accepted turn-1 run004, the next implementation task must prove that this correction does not alter any accepted turn-1 selected policy.

A zero-HJB policy-map replay of every accepted run004 household checkpoint is required using:

- each persisted checkpoint V;
- the exact accepted turn-1 province state/scalars;
- the corrected selector;
- no HJB update;
- no D2/KFE/aggregate/integration work.

Every replayed selected-policy identity must exactly match the accepted run004 checkpoint identity.

If any mismatch occurs, the accepted turn-1 path requires separate reexecution before turn 2 may continue.

## Evidence

Forensic root:

`reports/ch5_mp4c_turn2_beijing_f0364_negative_ratio_switching_forensic_20260920_run001/`

Sealed manifest:

`6FF469F423A7D5D321A59E1DC4031B04E967E3EE4A03E58865824D8B5D8CE1D0`

with 11 entries and 21,408 bytes. Independent readback PASS.

## Route consequence

The next task implements only the interior-b negative-ratio switching correction, proves exact F0364 parity, performs the mandatory full accepted-turn1 policy-identity compatibility replay, and only if that parity is exact executes one fresh turn-2 run003.

Turn 3, K1B, K2, GE and Results remain closed. Results eligibility remains `FALSE`.
