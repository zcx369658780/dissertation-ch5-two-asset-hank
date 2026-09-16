# CH5 MP4C 2018 KFE D1-D3 interior Z switching repair + Option A reexecution

Date: 2026-09-16
Status: ACTIVE
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Role: bounded Builder implementation + one-shot scientific execution

## Objective

Implement the Owner-adopted corrected-target interior zero-liquid `Z` switching candidate under the frozen D1+D2+D3 contract, then perform one fresh Option-A policy-map execution from Cell 0. Only if all 800 cells are admissible with durable receipts may D2 be assembled once and at most one direct linear HJB solve be performed.

This task is not a Cell-5 patch. It implements the generic inherited interior liquid zero-drift switching law now adopted by Owner.

## Required startup authority

Fresh-fetch `origin/main`; record the actual baseline. Read in order:
1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_INTERIOR_ZERO_LIQUID_Z_OWNER_ADOPTION_ACCEPTANCE_20260916.md`
6. `docs/CH5_MP4C_2018_KFE_D123_CELL5_LIQUID_DIRECTION_SWITCH_ATTRIBUTION_ACCEPTANCE_20260916.md`
7. `docs/CH5_MP4C_2018_KFE_D123_CELL5_LIQUID_DIRECTION_SWITCH_ALGEBRAIC_ATTRIBUTION_REPORT.md`
8. `docs/CH5_MP4C_2018_KFE_D123_LOWER_A_ZERO_KINK_REPAIR_OPTION_A_REEXECUTION_FAIL_CLOSED_ACCEPTANCE_20260916.md`
9. `docs/CH5_MP4C_2018_KFE_D123_LOWER_A_ZERO_KINK_MULTIPLIER_REPAIR_AND_OPTION_A_REEXECUTION_REPORT.md`
10. accepted corrected selector / Option-A driver / D2 generator / exact seed-grid-scalar provenance.

If live authority or accepted identities materially differ, stop before scientific execution.

## Frozen objects that must not change

- Option A seed remains `hjb100_initialization.mat:v0` with accepted file/field identities.
- Grid remains exact call-725 `(b,a,z)=(20,20,2)`, 800 cells, F-order.
- Prices/calibration, D1 state-constraint law, D2 strict zero-tolerance outward-face contract, D3 regularized adjustment cost/KKT, lower-a zero-kink multiplier repair, active-equality representation and Hamiltonian-selection semantics remain unchanged.
- No production/source-faithful path edits.

## Exact authorized interior Z implementation

At an interior liquid node, for each already-authorized a-side active set / derivative branch / transfer regime:

1. Form the existing backward and forward liquid candidates using their raw one-sided liquid shadows.
2. The Z branch is eligible only when both liquid shadows are finite and positive and the endpoint candidates exhibit strict crossing:
   - backward candidate has positive `g_b` (points forward), and
   - forward candidate has negative `g_b` (points backward).
   If either endpoint is already direction-consistent or zero within its prospective arithmetic bound, do not invoke a Z root for that combination.
3. Invoke at most one scalar root for that combination on the closed interval between the two raw positive one-sided shadows, using the frozen liquid-drift equation with the same a-side branch/regime logic recomputed as `q_b` changes.
4. Require exactly one finite positive root inside the derivative interval. No bracket widening, root retry, optimizer, average, interpolation, floor, cap or outcome-dependent tolerance is allowed.
5. Persist endpoint shadows/drifts, root bracket, root method/status, raw root residual, prospective arithmetic bound and marker `INTERIOR_LIQUID_Z_ZERO_DRIFT_SWITCH`.
6. If the raw residual is inside the prospective arithmetic bound, set consumed `g_b=0.0` exactly for this Z candidate; otherwise reject it. This is a mathematical equality representation, not D2 relaxation.
7. Recompute `c,l,d,cost,g_a,utility`, a-side shadow/multiplier/KKT objects and Hamiltonian from the root using the same frozen laws. The Z candidate must pass all existing domain, a-side feasibility, complementarity, transfer-KKT and finite checks.
8. Include the Z candidate in the same admissible comparison/deduplication/Hamiltonian selection as backward/forward candidates. `g_b=0` makes the liquid-Hamiltonian derivative term zero; no synthetic averaging derivative is introduced.
9. If no crossing exists, Z is not a candidate and no Z root may be counted.

For accepted Cell 5, focused preflight must reproduce the forensic identity `q_b*=0.01250021388291760706054915182349077777...` to appropriate binary64/root-contract accuracy and confirm it lies strictly between `p_b^F` and `p_b^B`. Do not use that expected value to tune the solver.

## Focused preflight before first real selector call

Complete implementation and tests before scientific execution. At minimum test:

- Cell-5-style strict crossing creates one Z candidate and one root invocation;
- no crossing => no Z root;
- endpoint already zero/direction-consistent => no unnecessary Z root;
- nonpositive derivative endpoint => Z unavailable/fail-closed;
- absent/nonunique/out-of-interval root => fail-closed without retry;
- Z controls are recomputed from root, not interpolated;
- repaired lower-a zero-kink law remains unchanged and compatible with Z;
- upper/lower liquid faces never use interior Z;
- slack/upper-a/nonzero-transfer behavior remains unchanged except for availability of a generic interior-liquid Z candidate when its own strict trigger is met;
- D2 strict outward-face contract unchanged;
- Option A hash/grid/scalar/F-order identities unchanged;
- `py_compile` and `git diff --check` pass.

Synthetic tests do not count as real scientific calls but must be reported separately.

## Scientific-code freeze

Before real selector call 1, persist hashes for the corrected-diagnostic scientific namespace and changed focused tests. After real execution begins, no scientific-code or test modification is allowed under this task. A discovered defect after call 1 ends this task without patch/retry.

## Fresh Option-A execution

Start again from F-order Cell 0 with one shared fresh budget. Persist a durable complete receipt after each attempted cell before advancing. Stop at the first `NO_ADMISSIBLE_POLICY`, nonunique selection, exception, evidence failure or budget breach. Do not resume from Cell 5 and do not reuse prior Cell 0–4 outcomes as substitutes for the fresh run.

Only after all 800 cells are `SELECTED_ADMISSIBLE` may D2 be assembled exactly once from the selected consumed drifts. Only after D2 passes all accepted invariants may one sparse direct HJB solve be executed using the already accepted one-step equation.

## Exact finite scientific-call ceiling

| Operation | Ceiling |
|---|---:|
| corrected policy maps | 1 |
| real selector evaluations | 800 |
| scalar roots total | 3144 |
| of which interior-Z roots | <=2880 |
| D2 generator assemblies | 1 |
| sparse direct HJB solves | 1 |
| selector evaluations on `V1` | 0 |
| nonlinear continuation after direct step | 0 |
| adverse scientific/numerical retries | 0 |
| KFE / MATLAB / outer / firm / wage-return / GE / annual / shock / IRF / Results | 0 |

Root ceiling derivation: retain the previously accepted 264 boundary-liquid-root ceiling; add at most four Z-root-eligible a-side/transfer combinations for each of 720 interior-`b` cells, `720*4=2880`; total `3144`. This ceiling does not authorize a root when the strict Z crossing trigger is absent.

## D2 and direct-step gates

D2 remains exactly the accepted consumed-total-drift conservative generator with strict zero-tolerance artificial/economic face checks. No outward drift may be repaired by tolerance. The direct HJB equation, `rho`, `Delta`, F-order mapping, solver-evidence requirements and no-second-map rule remain exactly as frozen in the accepted design report.

## Evidence requirements

Persist:
- preflight and input/hash identities;
- pre-execution freeze;
- per-cell receipts including all B/F/Z candidate evidence and root counts;
- cumulative selector/root budgets;
- first-failure receipt if any;
- if full map passes: one D2 receipt and invariants;
- if direct solve occurs: `V1`, matrix/RHS identities, residual/backward-error diagnostics and raw `V1` derivatives at historical coordinates 4/8/10 without a second selector map;
- execution ledger, post-freeze hash check and sealed manifest;
- final report `docs/CH5_MP4C_2018_KFE_D123_INTERIOR_Z_SWITCHING_REPAIR_AND_OPTION_A_REEXECUTION_REPORT.md`.

## Interpretation boundaries

A failed cell remains local fail-closed evidence and does not establish HJB/KFE/equilibrium nonexistence. A complete map plus one finite direct solve remains one-step diagnostic evidence only, not nonlinear HJB convergence, fixed-point existence, KFE validity, production readiness or Results authority.

Results eligibility remains `FALSE`.

## Git

Use an isolated worktree if useful. No reset/clean/stash/force-push. Stage only allowed implementation/tests/evidence/report paths. Commit and non-force push the task branch, verify remote readback and clean worktree. Do not merge main and do not publish a successor task.