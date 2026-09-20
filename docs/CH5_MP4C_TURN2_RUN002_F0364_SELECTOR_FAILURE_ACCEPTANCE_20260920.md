# Chapter 5 turn-2 run002 F0364 selector-failure acceptance

Date: 2026-09-20

Reviewer verdict:

`ACCEPTED_FAIL__AUTHORIZED_UPPER_B_NEGATIVE_REPAIR_PASS__TURN2_BEIJING_CHECKPOINT5_F0364_NO_ADMISSIBLE_POLICY__NEGATIVE_RATIO_INTERIOR_A_SWITCHING_FORENSIC_AUTHORIZED`

## Accepted candidate

- live-main baseline: `f0885e30832f30f3259f0549f6831fa9c17f6905`
- Builder candidate: `55dd5b81f1749e2af9e8d2a9a2507803b514131d`
- candidate tree: `1e96d697b3faac9ba530272c73aa122549e67461`
- ancestry independently verified: `2 ahead / 0 behind`, merge-base exactly baseline
- ordinary non-force push / remote readback / clean worktree reported PASS
- CURRENT governance files unchanged.

The candidate has been fast-forwarded into live `main`.

## Narrow upper-b negative repair acceptance

The authorized selector source change is accepted.

The exact code change exempts only:

`active upper_b + negative transfer`

from the pre-root single-a-branch count rejection.

It does not alter:

- the existing viability screen;
- q_b root domain;
- 513-point root screen;
- Brent configuration;
- transfer formulas;
- boundary/KKT/direction/complementarity checks;
- policy deduplication;
- Hamiltonian ordering/tie rule;
- upper-b zero-kink/positive behavior;
- lower-b negative behavior.

Accepted selector Git blob after repair:

`2c674b96fa7b665dab84f0ff3d98fbc5b8b16e22`.

Cost source remains:

`435705a50238aaeebe918430156bcc14df1ff794`.

F0579 formal runtime parity PASS:

- backward branch reaches its root and is rejected only by
  `A_DERIVATIVE_DIRECTION_INCONSISTENT`;
- forward branch is uniquely selected and exactly matches accepted forensic invariants.

## Preservation audit interpretation

The task-local predecessor audit found zero observable target tokens in the specified accepted predecessor roots.

However, the accepted turn-1 run004 evidence is compact and does not persist rejected candidate dictionaries. Therefore the zero-match result is an evidence-availability statement, not a proof that the repaired candidate class was mathematically absent at every historical accepted turn-1 cell.

This limitation does not invalidate the accepted historical turn-1 result, which remains tied to its original frozen code/evidence.

For fresh turn-2 run002, checkpoints 0 and 1 reproduce the prior turn-2 values exactly and checkpoint 2 now passes through the repaired F0579 cell as designed.

## Fresh turn-2 run002 progress

Only Beijing was reached.

Completed checkpoints 0 through 4 each passed:

- full policy map;
- D2/Q;
- direct HJB update;
- backward-error gate.

Reached values:

- checkpoint 0: B `0.35948978452765235`
- checkpoint 1: B `0.019968227378343403`, D `0.5603661628256393`
- checkpoint 2: B `0.0072664556369222005`, D `0.01838411533067008`
- checkpoint 3: B `0.10349094906054289`, D `0.015768036556986775`
- checkpoint 4: B `0.1804040891891172`, D `0.010078032277111681`.

No checkpoint met primary convergence. No rescue change was attempted.

## Exact new first failure

Terminal:

`FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`.

First failure:

- province: 北京
- province_index: `0`
- checkpoint: `5`
- F-order flat: `364`
- index: `(4,18,0)`
- physical state:
  - b = `-0.5263157894736843`
  - a = `9.473684210526315`
  - z = `0.8`
- selector outcome:
  `NO_ADMISSIBLE_POLICY`
- checkpoint-5 D2/Q: not assembled.

Exact durable cell:

`reports/ch5_mp4c_corrected_optionb_turn2_upper_b_negative_repair_20260920_run002/household/p00_北京/checkpoint_005/cell_0364.json`

Git blob:

`5e6528e07998cb6fe3b571cb21c778f3acf3775a`

SHA-256:

`F63B2D685F02D74ED3ED560F5DBD02FE5D7FF2B80ABF6D4F64414FFE1FCC7632`.

## F0364 structural diagnosis

F0364 is interior in both b and a.

There are no active geometric faces.

Persisted directional derivatives:

- p_b backward:
  `0.006091715618507631`
- p_b forward:
  `0.008179870108012337`
- p_a backward:
  `-0.0031029058502000167`
- p_a forward:
  `-0.004925792041697845`.

For negative transfer with the backward b derivative:

- the backward a derivative produces
  `g_a=1.1624821053092704 > 0`
  and is rejected by the a-direction rule;
- the forward a derivative produces
  `g_a=-0.25497146700720563 < 0`
  and is also rejected by the a-direction rule.

Thus these two ordinary candidates form the strict a-drift crossing that normally motivates an interior-a zero-drift switching candidate.

No interior-a switching candidate is emitted.

The current helper computes:

`d_z=-r_a*a=-7.8384208979658965`

and the frozen negative-transfer ratio:

`q_a/q_b = 1-chi_0 + chi_1*d_z/a = -0.7547777451261338`.

The current `_interior_a_switching_candidate` immediately returns no candidate when this ratio is <= 0.

At the same time:

- ordinary negative-transfer candidates already allow negative q_a;
- `check_transfer_kkt` requires q_b>0 but does not independently prohibit q_a<0.

Therefore the ratio-sign guard is now the next narrowly isolated scientific/numerical question.

## Scientific interpretation boundary

This acceptance does not remove or revise the ratio-sign guard.

It does not establish that negative-ratio interior-a switching is economically admissible.

It establishes only that:

- the current selector has a strict ordinary-branch a-drift crossing at F0364;
- the existing interior-a switching constructor stops before constructing a candidate because the D3 ratio is negative;
- all ordinary candidates are inadmissible.

A single-cell forensic is required before any selector decision.

## Scientific ledger

Fresh turn-2 run002 accepted consumption:

- source-native initializations: 1
- labor roots: 800/800
- policy maps started: 6
- complete maps: 5
- partial failed map: 1
- selector evaluations: 4,365
- scalar selector roots: 2,262
- interior-z roots: 642
- interior-a switching roots: 0
- joint switching roots: 0
- D2/Q assemblies: 5
- direct HJB updates: 5
- SCC/KFE/SVD: 0
- aggregates/integration: 0
- scientific retries: 0
- turn 3: 0.

## Evidence

Fresh run002 root:

`reports/ch5_mp4c_corrected_optionb_turn2_upper_b_negative_repair_20260920_run002/`

Sealed manifest:

`A2A882B8D79A6897D0518447FA84F7775609E31D34452A5EB2F7B7773E9FD0B0`

with 430 entries and 6,449,626 bytes. Independent readback PASS.

## Route consequence

No fresh HJB rerun is authorized yet.

The next task is a single-cell zero-HJB forensic of the F0364 negative-ratio interior-a switching geometry under the existing D3/KKT equations.

It must determine whether a sign-aware mapped q_b interval and zero-a-drift candidate would pass the existing downstream admissibility laws, or whether the negative ratio reflects a genuine selector-domain/economic restriction requiring Owner authority.

Results eligibility remains `FALSE`.
