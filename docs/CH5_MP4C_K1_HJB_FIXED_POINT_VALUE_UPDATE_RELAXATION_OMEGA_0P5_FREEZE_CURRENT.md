# CH5 MP4C K1 — HJB fixed-point value-update relaxation intervention freeze

Date: 2026-09-13.
Status: `OWNER_APPROVED_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_DIAGNOSTIC__OMEGA_0P5__SAME_INPUT__OTHER_SCIENCE_FROZEN`.

## 1. Owner decision

Owner and Reviewer approve the first isolated same-input intervention on the accepted HJB fixed-point map.

The intervention is a single preregistered value-update relaxation:

`omega = 0.5`.

For each HJB iteration, preserve the accepted scientific sequence through policy selection, operator construction, RHS construction and direct solve. Let the accepted direct-solve output be `V_solve`. Instead of passing `V_solve` directly as the next-iteration value state, the treatment passes:

`V_next = (1-omega) * V_old + omega * V_solve`

with `omega=0.5`.

The accepted baseline corresponds to `omega=1`.

This is a temporary numerical fixed-point diagnostic intervention. It is not an economic parameter, not a value-function rescaling, and not a new HJB equation.

## 2. Why this intervention is first

The accepted turn1/turn2 mechanism diagnostic found persistent policy-label chattering and non-monotone value updates preceding later derivative-floor amplification. It did not support pure two-cycle behavior, monotone-slow convergence, direct-solve failure as the initiating event, or return/wage guard state as a separator of success and failure.

The first causal question is therefore narrow:

> holding exact inputs, equations, controls, prices, grids, tolerances and direct-solve semantics fixed, does moderating only the value state passed to the next iteration reduce policy chattering and restore fixed-point convergence?

No other mechanism is changed in this stage.

## 3. Fixed-point convergence criterion

The treatment must not declare convergence merely because damping mechanically shrinks the stored update.

At each iteration record separately:

- raw fixed-point gap: `||V_solve - V_old||_inf`;
- relaxed state update: `||V_next - V_old||_inf`.

Treatment convergence is defined by the unchanged tolerance applied to the **raw fixed-point gap**:

`||V_solve - V_old||_inf < 1e-7`.

The 100-iteration ceiling remains unchanged.

This preserves the accepted fixed-point target and avoids false convergence caused solely by multiplying the update by `omega`.

## 4. Frozen science

Keep unchanged:

- `MODEL_TIME_BASE=ANNUAL_CONTINUOUS_TIME`;
- `rho=.05/year`, `rb=.02/year`, borrowing gap `.07/year`;
- firm/HJB `delta=.10/year`, `Q_z` off-diagonal `1/3/year`;
- `chi0=.1`, `chi1=2 years`;
- accepted transfer FOC, candidate generation, selector scoring/labels and boundary/KKT law;
- derivative floor/safeguard and derivative formulas;
- HJB economic equation;
- accepted pseudo-time/direct-solve matrix/RHS construction and linear solver;
- tolerance `1e-7`, 100-iteration ceiling and grids;
- G2 return guard `[-.10,.35]`;
- wage safeguard `[.8,1.3]`;
- fixed theta, `beta_distance=2`, `beta_return=0`;
- accepted destination-by-origin `S`, same-S quantity/payoff, source-faithful labor and C1 accounting;
- D1 OFF for the primary comparison;
- K1B/K2 OFF.

No change to prices, guards, derivative floors, transfer control, FOC, policy selector, boundaries, grid, tolerance, economic parameters or outer-loop state is authorized.

## 5. Comparison basis

Use the same 62 proven-exact accepted G2-control, D1-OFF HJB inputs from turn1 and turn2 used in the accepted mechanism diagnostic.

Baseline facts are the already accepted `omega=1` traces and outputs; do not rerun the full baseline cross-section merely to recreate evidence.

The treatment is `omega=0.5`, one replay per proven-exact input.

Before treatment replay, prove a generalized relaxation wrapper with `omega=1` is exact-equal to the accepted map on two preregistered exact inputs: one accepted converged call and one accepted ceiling-failure call. This is an engineering/scientific equivalence gate, not a second treatment.

## 6. Required observations

For each treatment call, preserve the previous mechanism diagnostics and add:

- raw `V_solve - V_old` fixed-point gap trajectory;
- relaxed `V_next - V_old` trajectory;
- policy switch count and two-step reversion count;
- raw/used derivative summaries and derivative-floor hits;
- selected controls, cost and drifts;
- operator diagnostics and direct-solve residual;
- consumed return/wage and guard states;
- final finite/nonfinite checks.

For calls that converge under both baseline and treatment, compare final value functions and final policies/controls quantitatively. Do not require exact equality because the iteration path differs; report residual differences and whether both satisfy the same fixed-point tolerance.

For baseline-failed but treatment-converged calls, report the treatment raw fixed-point gap, policy stability, finite outputs and final control/value summaries. Do not promote these isolated HJB outputs to steady-state or Results authority.

## 7. Interpretation

Because the inputs are exact-equal and the only intended scientific difference is the value-update relaxation, changes in HJB convergence/chattering may be attributed to this numerical fixed-point intervention within the isolated HJB calls.

This does not establish that `omega=0.5` is the final production solver setting. It is a first causal diagnostic. A positive result may justify a later Owner decision about the HJB solution-method contract; a negative or mixed result may redirect the next gate.

Do not tune `omega` after observing results. No ladder, adaptive damping or alternative `omega` is authorized in this stage.

## 8. Boundaries

KFE remains `DIAGNOSTIC_ONLY`; finite-box upper-b leakage and MATLAB-style pinning remain independent blockers. Standalone KKT residual remains `UNAVAILABLE_IN_ACCEPTED_EVIDENCE`.

Return/wage safeguards remain binding and `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS` remains a later requirement.

Results eligibility=`FALSE`.
