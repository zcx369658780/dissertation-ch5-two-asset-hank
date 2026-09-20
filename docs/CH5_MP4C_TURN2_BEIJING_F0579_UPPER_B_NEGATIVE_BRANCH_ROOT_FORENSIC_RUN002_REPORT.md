# Chapter 5 turn-2 Beijing F0579 upper-b negative-branch root forensic run002 report

Date: 2026-09-20

## Terminal verdict

`PASS__TURN2_BEIJING_F0579_UPPER_B_NEGATIVE_BRANCH_ROOT_FORENSIC_RUN002_COMPLETE__NO_SELECTOR_CHANGE`

Classification:

`TURN2_F0579_UPPER_B_NEGATIVE_PRE_ROOT_UNIQUENESS_FALSE_NEGATIVE_CONFIRMED` (A)

Fresh branch-specific root evaluation leaves exactly one distinct admissible
policy: the forward illiquid-derivative branch. The backward branch reaches a
valid liquid root but fails the frozen a-direction check. The current
pre-root branch-uniqueness rejection is therefore a false negative at this
persisted cell. This task does not modify the selector or authorize a turn-2
HJB rerun.

## Repository and exact authority binding

- fresh-fetched live-main baseline:
  `e3ee31db239787406827df305c9b6b695aa912e7`
- pre-science code-freeze commit:
  `630771c68e3fd578c50810febeeed3ebf148cc83`
- accepted turn-2 manifest:
  `50D2E87C94E762D3936C64E3AAD416F600118AEBB8DCE1588DB369938FA2351A`
- accepted forensic run001 manifest:
  `5EB92DEFF02D591A4E72FD2B19E1EF3DF6D4D2D45F13CE7B2A13311C6CD99247`
- exact cell Git blob:
  `799294deb8119e4581486d279bbf5704784588b2`
- exact cell SHA-256:
  `290630D26A63F2BEF3FFF1C9C6EE014E95ED5B3B470A7A5EC0FC8F3129178700`
- selector Git blob:
  `7e13fb53138788ec71541316a9e9815b5eb7c1f4`
- cost Git blob:
  `435705a50238aaeebe918430156bcc14df1ff794`

The exact cell is checkpoint 2, flat 579, index `[19,8,1]`, cell id
`v002_f0579_b019_a008_z001`, with persisted outcome
`NO_ADMISSIBLE_POLICY`. Its accepted scalars and derivatives all matched.
The persisted seven-candidate state reproduced without a full selector call.

## Finite-screen persistence repair

The forensic callback still computes and returns the raw residual. Evidence
capture applies the frozen `selector._finite_root_value` representation before
storing a screen value. Raw nonfinite observations are counted separately and
no infinity or NaN is serialized as a JSON number.

The synthetic `-inf` contract passed:

- evidence value equals frozen finite saturation;
- evidence value is finite and strict JSON serialization succeeds;
- raw callback return remains negative infinity;
- ordinary finite values are unchanged;
- selector/root callback behavior is unchanged.

The q-b domain, 513-point log grid, bracket rule, Brent configuration, branch
equations, and downstream admissibility laws were unchanged.

## Zero-science gate

Before any real F0579 root procedure:

- finite-screen repair contract: PASS
- accepted turn-2 and forensic-run001 manifest readback: PASS
- exact selector/cost identities: PASS
- exact failure-cell and seven-candidate reproduction: PASS
- focused tests: 7 passed
- `py_compile`: PASS
- `git diff --check`: PASS
- committed clean code freeze: PASS

One run002 launcher initially stopped inside this zero-science gate because
`sys` was not imported. The output root had not been created and F0579 root
consumption remained zero. The import was repaired within the allowed validator
path, a regression assertion was added, and the code was frozen again. The
subsequent successful execution was the only execution to enter branch-root
science; scientific retries remained zero.

## Backward branch

Input `p_a=-0.00014542975673859096`, with
`0 < q_b <= 0.005058006084641677`.

Root screen and solve:

- screen points: 513
- finite-screen SHA-256:
  `3CEE10B90DD80581EFCBB447A3E56CBF6B7361B97375828376BEB0A6DF40C0BE`
- raw nonfinite observations: 252
- finite residual min/max:
  `-1.7976931348623157e+308` / `0.7305767300601631`
- endpoint residuals:
  `[-1.7976931348623157e+308, 0.7305767300601631]`
- exact-grid count: 0
- sign-change bracket count: 1; left index 511
- bracket:
  `[0.0012810900847095138, 0.005058006084641675]`
- root status: `ROOT_CONVERGED`
- root: `0.004697887028753478`
- Brent solves: 1
- total function evaluations: 521

Post-root result:

- `q_b=0.004697887028753478`; `q_a=-0.00014542975673859096`
- `d=-1.9599082493888875`; cost `1.1082854071192596`
- `c=14.589779069921994`; `l=0.6317962081518563`
- raw `g_b=6.661338147750939e-16`; canonical `g_b=0`
- `g_a=1.7518552076793672`
- upper-b slack `-0.0`; multiplier `0.0003601190558881985`
- complementarity residual `-0.0`
- arithmetic tolerance `4.2742707282646107e-13`
- q-b domain, active equality, b-direction, transfer sign, transfer KKT,
  finite, face feasibility and D2-admissible drift checks: PASS
- transfer-KKT residual: `5.692061405548898e-19`
- a-direction consistency: FAIL
- utility: `-0.07914125526748655`
- raw/final Hamiltonian: `-0.07939602714418059`
- rejection: `A_DERIVATIVE_DIRECTION_INCONSISTENT`
- admissible: false

## Forward branch

Input `p_a=-0.0004814219651986697`, with the same q-b domain.

Root screen and solve:

- screen points: 513
- finite-screen SHA-256:
  `3D041B032BA984E51EB3F932D0A9F2849EB603723825450C0F92FD86746DDA6D`
- raw nonfinite observations: 253
- finite residual min/max:
  `-1.7976931348623157e+308` / `0.7219108688471196`
- endpoint residuals:
  `[-1.7976931348623157e+308, 0.7219108688471196]`
- exact-grid count: 0
- sign-change bracket count: 1; left index 511
- bracket:
  `[0.0012810900847095138, 0.005058006084641675]`
- root status: `ROOT_CONVERGED`
- root: `0.00470259773014529`
- Brent solves: 1
- total function evaluations: 521

Post-root result:

- `q_b=0.00470259773014529`; `q_a=-0.0004814219651986697`
- `d=-2.1102602580753396`; cost `1.2686606355504313`
- `c=14.582469778677709`; `l=0.6319228612726313`
- raw `g_b=1.5543122344752192e-15`; canonical `g_b=0`
- `g_a=1.6015031989929152`
- upper-b slack `-0.0`; multiplier `0.00035540835449638687`
- complementarity residual `-0.0`
- arithmetic tolerance `4.3070699391694177e-13`
- q-b domain, active equality, b/a direction, transfer sign, transfer KKT,
  finite, face feasibility and D2-admissible drift checks: PASS
- transfer-KKT residual: `6.505213034913027e-19`
- utility: `-0.07918836682454146`
- raw Hamiltonian: `-0.07995936564187257`
- final Hamiltonian: `-0.07995936564187259`
- rejection reasons: none
- admissible: true

## Switching prerequisite and classification

- `d_z=-3.7117634570682547`
- frozen negative-transfer ratio: `-0.8630876421074211`
- implied q-b endpoints:
  `[0.0005577903583733056, 0.00016849940799000638]`
- domain intersection is empty
- strict drift crossing: false
- prerequisite satisfied: false
- switching-root invocations: 0

The post-root admissible branch count and distinct-policy count are both 1.
The unique selected branch is `forward`; no Hamiltonian tie comparison is
needed. This satisfies classification A.

## Exact run002 scientific ledger

- run002 driver failure-cell load: 1
- zero-science focused-test failure-cell loads: 2
- backward/forward branch root procedures: 1 / 1
- total branch root procedures: 2
- Brent solves: 2
- interior-a switching roots: 0
- full selector calls / policy maps: 0 / 0
- D2/Q assemblies: 0
- HJB direct solves or reruns: 0
- KFE/SVD calls: 0
- aggregate/integration calls: 0
- turn-3 household calls: 0
- scientific retries: 0

Historical forensic run001 consumption remains separate:

- backward branch procedures: 1
- forward branch procedures: 0
- Brent solves: `UNRESOLVED_0_OR_1__NO_DURABLE_RETURN_RECEIPT`
- scientific retries: 0

## Evidence and closure

Evidence root:

`reports/ch5_mp4c_turn2_beijing_f0579_upper_b_negative_branch_forensic_20260920_run002/`

- sealed manifest SHA-256:
  `0DB648C10B42F5A8A187334FACEC123F9FD231999E09F650FE19C33114F420B4`
- entries: 16
- bytes: 19,348
- independent readback: PASS; bad paths 0
- pre/post source code freeze: exact match
- selector.py modified: false
- cost.py modified: false

No HJB, D2/Q, KFE, aggregate, integration, or turn-3 execution occurred.
CURRENT files were not modified, no successor was published, and main was not
merged.
