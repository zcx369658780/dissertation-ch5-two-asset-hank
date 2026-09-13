# CH5 MP4C K1 — HJB fixed-point value-update relaxation omega=0.5 same-input diagnostic

Date: 2026-09-13
Task ID: `CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_SAME_INPUT_DIAGNOSTIC`
Type: bounded scientific same-input HJB intervention diagnostic.

## Goal

Test one isolated HJB fixed-point intervention on the exact accepted turn1/turn2 G2-control inputs: value-update relaxation with `omega=0.5`.

The task asks whether policy chattering and non-monotone value-update behavior are reduced, whether raw fixed-point convergence improves, and whether outputs remain finite and numerically coherent when all economic inputs, equations, grids, tolerances, guards and direct-solve semantics are held fixed.

This is a diagnostic intervention, not a production solver change.

## Mandatory authority

Read live `AGENTS.md`, rule index, CURRENT status/handoff, accepted HJB mechanism diagnostic acceptance/report, `docs/CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_FREEZE_CURRENT.md`, accepted annual-HJB / price-guard / bilateral-capital / same-S / C1 authority docs, the accepted HJB implementation, and the accepted exact-input mechanism diagnostic validator/evidence producer.

## Frozen science

Keep unchanged except for the explicitly authorized value-state relaxation after each direct solve:

- `MODEL_TIME_BASE=ANNUAL_CONTINUOUS_TIME`;
- `rho=.05/year`, `rb=.02/year`, borrowing gap `.07/year`;
- firm/HJB `delta=.10/year`, `Q_z` off-diagonal `1/3/year`;
- `chi0=.1`, `chi1=2 years`;
- transfer FOC, candidate generation, selector scoring/labels and boundary/KKT law;
- derivative floor/safeguard and derivative formulas;
- HJB economic equation;
- accepted pseudo-time/direct-solve matrix and RHS construction;
- accepted sparse/direct linear solver;
- tolerance `1e-7`;
- 100-iteration ceiling;
- grids;
- G2 return guard `r_a in [-.10,.35]`;
- wage safeguard `wjt in [.8,1.3]`;
- fixed theta, `beta_distance=2`, `beta_return=0`;
- accepted destination-by-origin `S`, same-S quantity/payoff, source-faithful labor and C1 accounting;
- D1 OFF;
- K1B/K2 OFF.

Do not change return/wage guards, derivative floors, transfer-control law, FOC, selector, boundary/KKT, grid, tolerance, economic parameters, direct-solve expression or outer-loop state.

## Exact intervention

At HJB iteration `n`, preserve the accepted map through direct solve:

`V_solve = AcceptedDirectSolve(V_old, policies, operator, rhs)`.

Treatment next state:

`V_next = 0.5 * V_old + 0.5 * V_solve`.

The accepted baseline is `omega=1`, i.e. `V_next=V_solve`.

No other `omega`, damping ladder, adaptive damping, line search or state-dependent relaxation is allowed.

## Convergence rule

Do not use the mechanically halved relaxed update as the convergence statistic.

For treatment, convergence is:

`raw_fixed_point_gap = ||V_solve - V_old||_inf < 1e-7`.

Record separately:

`relaxed_state_update = ||V_next - V_old||_inf`.

The 100-iteration ceiling is unchanged. Tests/receipts must prove the convergence check uses the raw fixed-point gap.

## Phase 0 — exact-input reuse, zero science

Reuse the 62 already proven-exact accepted G2-control, D1-OFF inputs from the accepted mechanism diagnostic: 31 provinces turn1 plus 31 provinces turn2.

Revalidate identity receipts against accepted evidence as needed. Do not synthesize or approximate any state. If any previously proven input can no longer be validated, mark it unproven and skip that treatment call. Do not rerun the full `omega=1` baseline cross-section.

## Phase 1 — implementation / zero-science checks

Implement a task-owned generalized relaxation HJB wrapper or validator implementation preserving the accepted operation order through `V_solve` and altering only the stored next-iteration value state after the solve.

Focused tests must prove at least:

1. `omega=1` selects `V_solve` unchanged;
2. `omega=0.5` computes the exact convex combination;
3. convergence uses raw `||V_solve-V_old||_inf`, not relaxed update;
4. no KFE, outer trajectory, firm, K1B/K2, GE/IRF/Results calls are reachable from the task runner;
5. frozen numerics/parameters/grids remain unchanged.

## Phase 2 — omega=1 equivalence gate

Use two preregistered proven-exact inputs: one accepted converged call and one accepted ceiling-failure call.

Run the generalized wrapper with `omega=1` exactly once on each. Require exact equality with the accepted HJB map for scientific outputs, final values, policy labels, iteration count, convergence flag/statistic, final operator and deterministic scientific receipts, excluding new diagnostic metadata.

If either equivalence call fails exact parity, hard stop before `omega=0.5` treatment.

## Phase 3 — omega=0.5 same-input treatment

For every proven-exact input, run exactly one isolated HJB replay with `omega=0.5`. Target coverage is 62 treatment calls. No KFE and no outer-state advancement. Baseline comparator is the already accepted `omega=1` evidence; do not rerun baseline solely for comparison.

## Scientific budget

- `omega=1` equivalence HJB calls: exactly 2 if preflight passes;
- `omega=0.5` treatment HJB calls: at most 62, one per proven-exact input;
- total HJB calls: at most 64;
- HJB direct solves/internal iterations: naturally generated under the frozen 100-iteration ceiling, count truthfully;
- scientific retries after an HJB call begins: `0`;
- KFE, outer trajectory/turn advancement, MATLAB, firm runtime, standalone KFE, K1B/K2, GE, annual downstream, shock/IRF/Results: all `0`.

One engineering retry is allowed only before any HJB invocation for path/import/serialization/output-shape defects with unchanged scientific inputs.

## Required treatment diagnostics

Per iteration record at least:

- raw fixed-point gap `||V_solve-V_old||_inf`;
- relaxed update `||V_next-V_old||_inf`;
- policy/selector label counts, switch counts and two-step reversion counts;
- raw/used derivatives and derivative-floor hit counts/shares;
- consumption, labor, transfer, adjustment cost, `mu_a`, `mu_b`, liquid/illiquid drift summaries;
- accepted mechanism operator metrics;
- post-direct-solve residual;
- consumed return/wage and guard states;
- finite/nonfinite checks.

Retain enough external trace detail to audit event ordering and group comparisons.

## Pre-registered comparisons

Compare accepted baseline `omega=1` versus treatment `omega=0.5` on exact same inputs, for all calls and separately for baseline turn1 converged, turn1 failed, turn2 converged, turn2 failed, and the 20 provinces that were turn1-converged -> turn2-failed under baseline.

Primary outcomes:

- convergence under the same raw tolerance;
- iterations to raw fixed-point convergence;
- raw fixed-point-gap trajectory;
- policy-switch and two-step reversion trajectories;
- derivative-floor timing/share;
- finite output status.

Secondary outcomes:

- final value/policy/control differences where both baseline and treatment converge;
- treatment final raw fixed-point gap for baseline-failed/treatment-converged calls;
- whether chattering reduction temporally precedes convergence improvement.

Do not invent a post-result `omega` threshold or tune `omega`.

## Output-normality / fixed-point checks

For every treatment-converged call require/report:

- raw fixed-point gap below `1e-7`;
- all returned scientific arrays finite;
- no unauthorized clipping/manufactured candidate;
- expected shapes and accepted label domain;
- finite post-convergence operator/direct-solve receipts;
- no scientific exception.

For calls converged under both baseline and treatment, report max/median absolute differences in final value and principal controls/policies. Similarity is evidence about reaching the same numerical fixed point; it is not assumed in advance.

For baseline-failed/treatment-converged calls, report full fixed-point residual and output diagnostics but do not call the isolated HJB object a steady state.

## Questions to answer

1. Does `omega=0.5` increase, decrease or leave unchanged raw-fixed-point-converged HJB calls relative to accepted baseline?
2. Does it reduce persistent policy switching and two-step reversions on the same inputs?
3. Does value-update non-monotonicity decrease before derivative-floor activity changes?
4. Are new converged calls finite and numerically coherent under frozen equations/guards?
5. For calls converged under both maps, do final value/policy/control objects approach the same fixed point within reported numerical differences?
6. Is the accepted chattering/oscillation diagnosis supported causally by this isolated intervention, contradicted, or only partially supported?
7. Does evidence justify a future Owner discussion of a production HJB solution-method contract, or should the route redirect?

## Hard stops

Stop scientific execution on any `omega=1` equivalence parity failure; any evidence the relaxation changes policy/operator/RHS/direct solve before `V_solve`; convergence criterion using relaxed update instead of raw fixed-point gap; unauthorized parameter/equation/guard/grid/tolerance/ceiling/solver change; new scientific NaN/Inf exception outside accepted semantics; or source/provenance corruption in exact inputs.

Subset input identity failure: skip only that call and continue with independently proven inputs; do not synthesize replacements.

## Allowed changes

Only task-owned generalized value-relaxation HJB validator/wrapper, exact-input treatment runner and offline analyzer, focused tests, report `docs/CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_SAME_INPUT_DIAGNOSTIC_REPORT.md`, compact evidence under `docs/evidence/ch5_mp4c_k1_hjb_value_update_relaxation_omega_0p5/`, and truthful CURRENT closeout docs if needed.

Do not modify protected MATLAB or unrelated scientific source.

## Git / publication

Fresh-fetch live main and record actual baseline. Use a fresh isolated worktree/branch. Preserve unrelated dirty work. No reset/clean/stash/force push. Explicit stage paths only; no `git add .` or `git add -A`.

One coherent Builder commit, non-force push, one remote readback. Do not merge main and do not publish a successor task. External run artifacts use a fresh no-overwrite evidence root.

## Required final response

Return outcome first and include classification; actual baseline/branch/worktree/candidate SHA; changed paths; exact-input coverage; two-call `omega=1` equivalence result; complete call/direct-solve ledger; baseline versus `omega=0.5` convergence table for turn1/turn2/all 62; policy-switch/reversion comparison; raw-gap versus relaxed-update evidence; derivative-floor timing comparison; output-normality/finite checks; both-converged fixed-point comparison; baseline-failed/treatment-converged analysis; causal interpretation boundary; exactly one recommended next Owner gate; KFE/KKT caveats; and `Results eligibility=FALSE`.

Stop after publication for independent ChatGPT Reviewer acceptance.
