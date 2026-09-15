# Exact task — CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY

## Objective

Test whether the accepted practical household grid `I=20,J=160,a=[0,100],b=[-2,20]` can solve the accepted real first-turn province household HJB inputs across the multi-province state vector, without invoking KFE or any outer-model update.

## Authority

Read first:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1_J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY_ACCEPTANCE.md`
6. `docs/CH5_MP4C_K1_J160_BOUNDED_CROSS_STATE_CONFIRMATION_ACCEPTANCE.md`
7. `docs/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_FREEZE_CURRENT.md`
8. accepted prior first-turn provincial mechanism/trajectory evidence and MATLAB-faithful HJB authority.

## Phase 0 — exact input authority gate

Recover the exact accepted first-turn province-level household-call input vector from repository evidence. Expected province count is 31.

For every province seal at least:

- province index/id;
- `rb`;
- consumed `ra/rah` household return input;
- household composite wage `w`;
- transfer/tax inputs used by the accepted household adapter;
- any additional household-call input needed by the live accepted adapter.

Do not reconstruct these values from memory, interpolate them, recompute them from a new firm/wage call, or substitute raw `wjt` for household composite `w`.

If the exact accepted first-turn vector is unavailable or ambiguous, STOP before science with:

`FIRST_TURN_PROVINCIAL_INPUT_AUTHORITY_BLOCKER`

## Frozen grid and science

Use for every province:

- `I=20`
- `J=160`
- `Nz=2`
- `amin=0`
- `amax=100`
- `bmin=-2`
- `bmax=20`
- diagnostic bridge `h=1`

Keep accepted MATLAB-faithful HJB behavior unchanged:

- equations;
- FOCs;
- selectors;
- boundary laws;
- derivative floors;
- `Delta=1000` numerical pseudo-time parameter;
- sparse direct solve;
- tolerance `1e-7`;
- maxit `100`;
- legality gate `A2max<=0.01`;
- fresh source-style initialization.

No warm start between provinces.

## Exact runtime

If Phase 0 passes, run exactly one fresh HJB per authorized first-turn province input.

Expected:

- HJB exactly 31;
- KFE 0;
- scientific retries 0.

No province may be retried or tuned.

## Required per-province receipts

Record:

- province id/index;
- exact frozen household inputs;
- HJB classification;
- iterations;
- final `max(abs(Vnew-Vold))`;
- max `A2max`;
- first illegal iteration if any;
- finite/shape checks;
- fresh-initialization receipt;
- consumed wage/return guard status inherited from the accepted first-turn evidence where available.

## Aggregate diagnostic summary

Report:

- converged count / total;
- illegal-operator count;
- nonconverged-but-legal count;
- iteration distribution;
- convergence-stat distribution;
- max A2max distribution;
- failure provinces and their exact `(ra,w)` locations;
- whether failures cluster near accepted standalone cross-state boundaries or occur inside the previously supported region.

This last comparison is descriptive only and must not be used to recalibrate within this task.

## Decision

If all authorized provinces are legal/converged:

`J160_FIRST_TURN_PROVINCIAL_HJB_VIABILITY_PASS`

If one or more provinces fail:

`J160_FIRST_TURN_PROVINCIAL_HJB_VIABILITY_BLOCKED`

Do not change `wjt`, `ra`, grid, maxit, solver, tolerance, or household science in response.

Exactly one next Reviewer gate:

`REVIEWER_J160_FIRST_TURN_PROVINCIAL_ROUTE_DECISION`

## Prohibited

Do not run:

- KFE;
- global outer turn;
- firm model;
- wage recalculation;
- MATLAB;
- K1B/K2;
- GE;
- downstream annual dynamics;
- shocks/IRFs;
- Results.

Do not modify:

- asset domain;
- I/J;
- economic parameters;
- HJB/KFE scientific source;
- `wjt` guard;
- return mapping;
- wage mapping;
- solver/tolerance/maxit;
- derivative floor.

## Outputs

Report:

`docs/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_REPORT.md`

Evidence directory:

`docs/evidence/ch5_mp4c_k1_j160_provincial_first_turn_hjb_viability/`

At minimum:

- `source_identity.json`
- `first_turn_input_authority.json`
- `input_invariance_receipt.json`
- `province_receipts.json`
- `points.csv`
- `summary.json`
- `call_ledger.json`
- `sealed_manifest_sha256.json`

## Git workflow

Fresh-fetch `origin/main`; use a fresh isolated worktree and branch; no reset/clean/stash/force-push; explicit staging only; one coherent Builder commit; non-force push; exactly one remote readback; do not merge main and do not publish a successor task.

Results eligibility remains `FALSE`.