# CH5 MP4C 2018 KFE D1-D3 lower-a zero-kink multiplier repair + Option A reexecution

Date: 2026-09-16
Status: ACTIVE
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Role: bounded Builder repair + one-shot scientific reexecution

## Objective

Repair exactly one accepted selector omission: the active lower-`a` zero-transfer-kink branch must allow the existing D1/D3 lower-face multiplier law `q_a=p_a+lambda_a`, `lambda_a>=0`, instead of forcing `q_a=p_a`. After focused preflight and code freeze, rerun the Owner-approved Option A corrected policy-map gate from Cell 0 under a fresh one-shot budget. Only if all 800 cells select admissible policies may D2 be assembled once and at most one direct HJB solve be executed.

No other selector law, seed, grid, calibration, tolerance, generator or production path may change.

## Required startup authority

Fresh-fetch `origin/main`; record actual baseline. Read in order:
1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_OPTION_A_FIRST_CELL_SELECTOR_OMISSION_ACCEPTANCE_20260916.md`
6. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_OPTION_A_SINGLE_POLICY_MAP_DIRECT_STEP_REPORT.md`
7. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_OPTION_A_SEED_OWNER_ADOPTION_ACCEPTANCE_20260916.md`
8. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_HJB_ONE_STEP_DESIGN_AND_INPUT_BINDING_REPORT.md`
9. accepted corrected-diagnostic selector/cost/generator code and exact Option-A provenance.

If live authority materially differs, stop before scientific execution.

## Frozen seed and common contract

Keep the Owner-selected Option A exactly:
- `hjb100_initialization.mat:v0`
- file SHA-256 `1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81`
- field SHA-256 `564B95B818713477691389903C3CFF72B5A7F991B924D52FBEB23D5A3675D665`
- shape `(20,20,2)`, F-order.

Keep the already frozen call-725 grid, scalars, raw one-sided derivative construction, boundary carrier marker, D1 state constraints, D2 strict zero-tolerance conservative assembly, D3 regularized cost/KKT, one-step HJB equation and downstream prohibitions unchanged.

## Exact authorized selector repair

The only scientific-code behavior change authorized is for `a_active` with `regime == "zero_kink"` at a lower-`a` face where the active equality implies `d=0`.

Frozen laws:
- lower-`a` multiplier: `q_a = p_a + lambda_a`, `lambda_a >= 0`;
- zero-kink transfer KKT: `q_a in [q_b*(1-chi_0), q_b*(1+chi_0)]`;
- lower-`a` active equality at `a=0`: `g_a=d=0`.

Define the feasible shadow interval as the intersection

`[p_a,+inf) ∩ [q_b*(1-chi_0), q_b*(1+chi_0)]`.

If nonempty, use the deterministic minimum feasible representative

`q_a = max(p_a, q_b*(1-chi_0))`,

and `lambda_a=q_a-p_a`.

The upper endpoint test must use the task's prospectively defined arithmetic bound, not an outcome-fitted tolerance. Persist the raw interval, chosen `q_a`, multiplier and a marker such as `ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_CANONICAL_MIN`.

If the intersection is empty, reject the candidate fail-closed.

This canonical representative is permitted only because `d=g_a=0` on this active branch, so all feasible shadows in the interval imply the same consumed controls/drifts and Hamiltonian. Do not generalize this rule to slack faces, upper-`a`, nonzero-transfer branches, liquid multipliers, or other KKT objects.

## Explicitly forbidden repairs

Do not:
- change Option A seed or fall back to another seed;
- add derivative floors, transfer caps, damping, generic optimizer, tolerance tuning, grid/domain changes or recalibration;
- alter D2 zero-tolerance closed-face rejection;
- alter active-equality canonical-zero logic already accepted;
- project/clip a slack-face drift or shadow;
- alter nonzero-transfer active-`a` logic;
- modify source-faithful/production paths;
- use the first failed outcome to introduce new economic semantics.

## Preflight before any real Option-A selector call

Complete all implementation and focused tests first. Required tests include:

1. synthetic lower-`a`, `a=0`, active zero-kink case with `p_a=0`, `q_b>0`: verify nonempty kink/multiplier intersection, positive `lambda_a`, `d=g_a=0`, transfer KKT satisfied and no change to consumed policy relative to the same `q_b,d=0` controls;
2. synthetic case with `p_a` already inside the kink interval: canonical representative may equal `p_a` with `lambda_a=0`;
3. synthetic empty-intersection case: fail closed;
4. prove slack lower-`a` zero-kink still keeps `lambda_a=0` and is not repaired;
5. prove upper-`a` and nonzero-transfer active branches are unchanged;
6. reproduce the historical Option-A Cell-0 algebraic inputs without executing the real-cell panel and show that the formerly omitted active-lower-a zero-kink shadow interval is nonempty. This may be a pure arithmetic/source-binding check, not a counted selector evaluation.

Run focused unit tests, `py_compile`, `git diff --check`, exact Option-A hash/grid/scalar readback and F-order enumeration. Freeze all scientific-code hashes before the first real selector call.

## Fresh scientific reexecution

After preflight and freeze, execute the Option-A policy map once from flat F-order Cell 0.

- Exactly one shared fresh `SelectorBudget`.
- Persist a complete durable receipt for each attempted cell before moving on.
- Stop at the first cell that is not `SELECTED_ADMISSIBLE`, any exception, budget breach, missing receipt or code/hash drift.
- No scientific-code patch after the first real selector call.
- No retry of any attempted cell.

The prior run's Cell-0 call and roots are historical evidence only; they do not count against this fresh task budget.

## Runtime ceilings

- corrected policy maps: <=1
- real selector evaluations: <=800
- scalar root invocations: <=264
- D2 generator assemblies: <=1, only after all 800 cells pass
- sparse direct HJB solves: <=1, only after D2 passes
- selector evaluations on `V1`: 0
- nonlinear HJB continuation/iterations after direct step: 0
- adverse-outcome/adverse-numerics retries: 0
- KFE: 0
- MATLAB: 0
- outer/firm/wage-return recalculation: 0
- GE/annual/shock/IRF/Results: 0

## Full-map / D2 / direct-step gates

Keep the accepted design unchanged:
- all 800 cells must produce exactly one selected admissible consumed policy before D2;
- D2 consumes only total `g_b,g_a`, retains nonnegative rates, strict closed-face zero tolerance and conservative diagonal;
- D2 invariant/coordinate-action checks must pass under prospectively defined bounds;
- only then solve once `M=(rho+1/Delta)I-Q0`, `rhs=vec_F(u0)+vec_F(V0)/Delta`;
- persist solve residual/backward error and `V1` identity;
- do not run a selector on `V1`.

## Required evidence/report

Use a fresh evidence root distinct from the previous failed run. Persist:
- exact baseline, seed/grid/scalar identities;
- repair implementation identity and focused preflight results;
- pre-execution code-freeze hashes;
- per-cell durable receipts for every attempted real cell;
- explicit lower-`a` zero-kink shadow/multiplier receipt where encountered;
- complete call/root counters and first-failure identity if applicable;
- D2 and direct-solve evidence only if their gates are reached;
- post-execution code-freeze check;
- sealed manifest with byte/hash readback.

Create one report:
`docs/CH5_MP4C_2018_KFE_D123_LOWER_A_ZERO_KINK_MULTIPLIER_REPAIR_AND_OPTION_A_REEXECUTION_REPORT.md`.

A PASS requires the full 800-cell map, D2 PASS and one finite direct step. A fail-closed first-cell or later-cell result remains valid evidence but is not HJB convergence evidence.

## Git

Use isolated worktree if useful. No reset/clean/stash/force-push. Stage only allowed corrected-diagnostic implementation/tests/new evidence/report. Commit and non-force push task branch, verify remote readback and clean worktree. Do not merge main and do not publish a successor task.
