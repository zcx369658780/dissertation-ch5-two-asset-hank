# Chapter 5 turn-2 Hebei F0005 lower-a / interior-liquid switching forensic — Reviewer acceptance

Date: 2026-09-21

Verdict:

`ACCEPTED_PASS__TURN2_HEBEI_F0005_ACTIVE_LOWER_A_INTERIOR_Z_COMPOSITION_FALSE_NEGATIVE_CONFIRMED__IMPLEMENTATION_REPAIR_AUTHORIZED`

Accepted terminal:

`PASS__TURN2_HEBEI_F0005_FORENSIC__ACTIVE_LOWER_A_INTERIOR_Z_COMPOSITION_FALSE_NEGATIVE_CONFIRMED__NO_CODE_CHANGE`

Accepted classification:

`IMPLEMENTATION_COMPOSITION_FALSE_NEGATIVE_UNDER_ALREADY_ADOPTED_AUTHORITY`

Results eligibility remains `FALSE`.

## Independent Git review

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

- live-main baseline: `3473ada0d9d6d8767383969dc5fe268763cebf54`
- Builder candidate: `26853c49a06ba0cc3da88df2df250f2f0fd22ff8`
- candidate tree: `3dfde221b62ff723723e7489a35afbecad85f5f5`
- ancestry: 1 ahead / 0 behind
- merge-base: exact baseline
- remote candidate branch: exact candidate SHA/tree
- changed paths: 17
- production `src/ch5_two_asset_hank/**` changes: 0
- CURRENT changes: 0

All changed paths are the forensic report, evidence root, validator and focused test authorized by the task.

## Accepted authority composition

The forensic correctly binds the two already adopted authorities.

### Active lower-a zero-kink authority

At active lower-`a`, the equality implies `d=0` at this cell. The inward a derivative is the existing forward branch. The lower-face shadow is determined by:

`q_a in [p_a,+infinity) intersect [q_b(1-chi_0), q_b(1+chi_0)]`

with the already adopted deterministic minimum:

`q_a=max(p_a,q_b(1-chi_0))`

and

`lambda_a=q_a-p_a>=0`.

### Owner-adopted interior-liquid Z authority

At interior liquid `b`, under the same a-side branch / active set / transfer regime, finite positive backward and forward liquid shadows with a strict direction crossing authorize exactly one zero-liquid root search over the closed derivative interval. At the switching shadow all a-side KKT objects are recomputed; endpoint full admissibility is not itself the final switching test.

The composition does not create an interior-a switching shadow. Therefore the separate two-interior-axis restriction is not implicated.

No new equation, KKT law, boundary law, root law, tolerance or calibration is required.

## Exact persisted object

Accepted failing cell:

`reports/ch5_mp4c_interior_b_negative_ratio_repair_turn1_parity_turn2_run003_20260921/household/p02_河北/checkpoint_001/cell_0005.json`

Binding:

- province: 河北
- checkpoint: 1
- flat F-order index: 5
- index: `(5,0,0)`
- cell: `v001_f0005_b005_a000_z000`
- `b=-0.1578947368421053`
- `a=0`
- `z=0.8`
- `p_a^B=p_a^F=0.010591720688767481`
- `p_b^B=0.016103423470140932`
- `p_b^F=0.008913524380688508`
- persisted selector outcome: `NO_ADMISSIBLE_POLICY`

The cell identity matches the accepted predecessor manifest.

## Strict liquid-direction crossing

Within the same legal family:

- active constraints: lower-a
- a derivative branch: forward
- transfer regime: zero-kink
- d: 0

the raw liquid endpoint drifts are:

- backward endpoint:
  `q_b=0.016103423470140932`,
  `g_b=+1.7486866578989382`
- forward endpoint:
  `q_b=0.008913524380688508`,
  `g_b=-2.027652723229073`

This is a strict interior-liquid crossing.

The forward endpoint's lower-a kink intersection is empty at that endpoint. Under the adopted Z authority that does not terminate the switching family because the lower-a KKT objects must be recomputed at the switching shadow.

## Independent zero-liquid reconstruction

The forensic did not call the production selector or production root helper.

It independently reconstructed:

`g_b(q)=w_net*(q*w_net)^(1/5)+r_b*b+T-q^(-1/2)`.

The unique positive root is:

`q_b*=0.0120851325790094875041402945557588462734692022962404697375483941...`

with:

- Decimal residual: `-3E-89`
- root strictly inside the closed derivative interval
- monotonicity: `dg_b/dq>0` for every `q>0`
- limits: `g_b(q)->-infinity` as `q->0+`, and `g_b(q)->+infinity` as `q->infinity`

Therefore the positive root is unique.

## Combined candidate under existing laws

Using current binary64 operation order at the switching shadow:

- active constraints: lower-a
- derivative branches: `a=forward, b=zero`
- transfer: zero-kink
- `q_b=0.012085132579009488`
- lower-a kink interval:
  `[0.01087661932110854,0.013293645836910438]`
- `q_a=0.01087661932110854`
- `lambda_a=0.00028489863234105843`
- `d=0`
- `g_a=0`
- `g_b=0`
- transfer-KKT residual: 0
- lower-a complementarity residual: 0
- Hamiltonian: `-0.1280816705218543`
- admissible: true

All finite/domain, lower-a equality/multiplier, complementarity, transfer-KKT and zero-liquid residual checks pass under the existing clauses.

All 15 persisted candidates are inadmissible, so this combined candidate is the unique admissible policy for the unchanged Hamiltonian comparison.

## Current selector omission

Independent source review confirms:

1. ordinary active lower-a / zero-kink endpoint construction computes the lower-a kink intersection before controls;
2. the forward endpoint returns early on `ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERSECTION_EMPTY`;
3. that rejected endpoint therefore carries `g_b=None` and no arithmetic tolerance;
4. `_interior_z_candidate` requires both endpoint `g_b` values and bounds, so it exits before the adopted zero-liquid root reconstruction;
5. if the root is reached, the existing `_candidate(...,q_b_override=root,...)` path already recomputes the lower-a kink interval at the switching shadow before unchanged KKT/feasibility/Hamiltonian checks.

This is an implementation composition omission, not a new scientific-law question.

## Zero-science boundary and evidence integrity

Accepted ledger:

- production selector calls: 0
- production root-helper calls: 0
- HJB/direct update: 0
- D2/Q: 0
- SCC/KFE/SVD: 0
- aggregate/integration: 0
- turn2 replay: 0
- turn3: 0
- MATLAB / GE / Results: 0
- retry/tuning: 0
- persisted cell loads: 6
- independent Decimal reconstructions: 4
- binary64 scalar spot checks: 1

Focused tests: 4/4 PASS.

Evidence root:

`reports/ch5_mp4c_turn2_hebei_f0005_lower_a_liquid_switch_forensic_20260921_run001/`

- manifest SHA-256:
  `039E74760D6FFAC8DD3177723B6F7EE9FFC9CFE2BD6C192EF4EB34160DAD026A`
- entries: 11
- bytes: 23,993
- independent readback: PASS
- bad paths: none

## Reviewer decision

The forensic candidate is accepted.

The current persisted `NO_ADMISSIBLE_POLICY` at 河北 F0005 is not a valid terminal under the already adopted lower-a zero-kink plus interior-liquid Z authorities.

A narrow implementation repair is authorized. The repair must make the existing interior-Z screening able to use the raw endpoint liquid drift information for the active lower-a / zero-kink family even when an endpoint's full lower-a kink intersection is empty, then use the existing interior-Z root law and existing final `_candidate` path to recompute lower-a KKT at the switching shadow.

The next task must prove exact F0005 normal-selector parity, preserve all unrelated selector laws, replay all 408 accepted turn-1 policy maps as a hard compatibility gate, and only then run one fresh turn-2 execution from the exact accepted entering state.

No turn-1 authority may be silently rewritten. Turn 3 and Results remain closed.
