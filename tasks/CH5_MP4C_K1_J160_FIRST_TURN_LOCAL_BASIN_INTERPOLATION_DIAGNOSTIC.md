# Task — CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC

Status: ACTIVE

## Objective

Map local HJB convergence-basin topology between preregistered accepted first-turn failure/success pairs using exactly three synthetic interpolation probes per pair, while keeping all accepted household science frozen.

## Required authority reads

Before execution read and follow:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1_FIRST_TURN_PROVINCIAL_INPUT_OUTCOME_ENVELOPE_AUDIT_ACCEPTANCE.md`
6. `docs/CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC_FREEZE_CURRENT.md`
7. accepted first-turn provincial viability evidence
8. accepted six-failure mechanism evidence
9. accepted coordinate-resolved matched-control evidence
10. accepted MATLAB-faithful HJB authority

## Phase 0 — fresh governance and pair authority

Fresh-fetch `origin/main`; record actual baseline. Use a fresh isolated worktree and branch.

Verify exact accepted endpoint authority for the four pairs:

- 山西 failure ↔ 河北 success;
- 重庆 failure ↔ 河北 success;
- 江西 failure ↔ 安徽 success;
- 贵州 failure ↔ 四川 success.

For each pair prove every consumed household-call input other than consumed `ra/rah` and household composite `w` is exactly equal. This includes `rb`, borrowing gap, tax, transfer, model parameters, guard states and adapter inputs.

If any pair fails this equality/provenance gate, STOP before science as:

`LOCAL_BASIN_PAIR_INPUT_AUTHORITY_BLOCKER`

No endpoint HJB rerun is allowed.

## Frozen science

Use exactly:

- `I=20,J=160,Nz=2`;
- `a=[0,100]`, `b=[-2,20]`;
- `h=1`;
- fresh source-style initialization;
- tolerance `1e-7`;
- maxit `100`;
- `Delta=1000`;
- A2max legality gate `0.01`;
- accepted equations/FOCs/selectors/boundaries/floors/solver/convergence test unchanged.

KFE=0.

## Exact synthetic probes

For each pair define failure endpoint `F=(ra_F,w_F)` and success endpoint `S=(ra_S,w_S)` from accepted evidence.

Run only:

- `t=.25`: `(ra,w)=.75F+.25S`;
- `t=.50`: `(ra,w)=.50F+.50S`;
- `t=.75`: `(ra,w)=.25F+.75S`.

All other consumed inputs use the pair-common accepted value.

Exactly 4 pairs × 3 probes = 12 new HJB calls after clean preflight.

No extra `t`, no adaptive bisection, no synthetic point outside these 12.

These are numerical basin probes only. Do not call them feasible provincial equilibrium states or calibrated mapping outputs.

## Runtime and retries

- HJB exactly 12 after authority gate;
- KFE=0;
- scientific retries=0;
- engineering retry <=1 and only before first HJB, path/import/serialization/instrumentation plumbing only;
- endpoint HJB reruns=0;
- successful/failure province reruns=0;
- firm/wage/return mapping=0;
- outer/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results=0.

## Per-probe receipts

Record:

- pair id and `t`;
- exact synthetic `(ra,w)`;
- confirmation of common non-interpolated inputs;
- fresh-initialization receipt;
- HJB class;
- iterations;
- final max `|ΔV|`;
- max A2max and first illegal iteration if any;
- finite/shape checks;
- first selector switching;
- first value-stat non-decrease;
- first derivative-floor hit;
- for nonconverged probes, broad mechanism class using only the accepted taxonomy where evidence supports it.

Observation-only instrumentation must not affect scientific control flow.

## Pair outcome topology

For each pair report ordered sequence at:

`t=0` accepted failure endpoint,
`t=.25`, `.50`, `.75`,
`t=1` accepted success endpoint.

Choose exactly one pair class:

- `SINGLE_TRANSITION_FAILURE_TO_SUCCESS`
- `ALL_INTERIOR_PROBES_CONVERGE`
- `ALL_INTERIOR_PROBES_FAIL`
- `NONMONOTONE_OR_INTERLEAVED_LOCAL_BASIN`
- `PAIR_NUMERICAL_INVALIDITY_BLOCKER`

Do not infer a unique threshold beyond the tested points.

## Panel decision

Choose exactly one:

- `LOCAL_BASIN_BOUNDARIES_SIMPLE_AND_PAIR_SPECIFIC`
- `LOCAL_BASIN_TOPOLOGY_HETEROGENEOUS_OR_INTERLEAVED`
- `LOCAL_BASIN_EVIDENCE_NUMERICALLY_BLOCKED`

The first class requires all four pairs to show a simple ordered transition pattern without contradictory interleaving; it still does not authorize calibration.

## Interpretation boundary

This task may establish that tiny movements in consumed `(ra,w)` can cross numerical basins. It cannot establish causality, cannot identify the upstream mapping as wrong, and cannot authorize a safe-price clipping rule, recalibration, HJB modification or Results use.

## Required outputs

Report:

`docs/CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC_REPORT.md`

Evidence directory:

`docs/evidence/ch5_mp4c_k1_j160_first_turn_local_basin_interpolation_diagnostic/`

At least:

- `source_identity.json`
- `pair_input_authority.json`
- `input_invariance_receipt.json`
- `probe_points.csv`
- `probe_receipts.json`
- `pair_topology.json`
- `panel_decision.json`
- `call_ledger.json`
- `sealed_manifest_sha256.json`

## Git workflow

Fresh-fetch `origin/main`; record actual baseline. Fresh isolated worktree and branch. No reset/clean/stash/force push. No `git add .` or `git add -A`; explicit staging only. One coherent Builder commit, non-force push, exactly one remote readback. Do not merge main. Do not publish successor task.

## Final response

Start with the panel terminal class. Then report actual baseline, branch, worktree, candidate SHA, changed paths, authority gate, exact four endpoint pairs, 12 probe outcomes, per-pair ordered topology and pair class, any nonconverged-probe mechanism summaries, runtime ledger, KFE=0, scientific retries=0, interpretation limits, Results eligibility=FALSE, and exactly one next gate:

`REVIEWER_J160_LOCAL_BASIN_INTERPOLATION_ROUTE_DECISION`

Then STOP for independent ChatGPT Reviewer acceptance.
