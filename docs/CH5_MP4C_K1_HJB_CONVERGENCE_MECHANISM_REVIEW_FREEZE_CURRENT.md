# CH5 MP4C K1 — HJB convergence-mechanism diagnostic route freeze

Date: 2026-09-13.
Status: `OWNER_APPROVED_HJB_CONVERGENCE_MECHANISM_REVIEW_FIRST__DIAGNOSTIC_ONLY__NO_SCIENCE_PARAMETER_CHANGE`.

## 1. Owner decision

After accepted D1 evidence showed that aggressive transfer far-tail reduction did not improve HJB convergence, Owner and Reviewer freeze the next route as a diagnostic-first HJB convergence-mechanism review.

Priority order is:

`D HJB iteration / fixed-point mechanism -> C derivative/value safeguard evidence -> A return interface -> B wage interface -> E boundary/selector only if evidence redirects there`.

This freeze does not authorize any economic, solver, tolerance, grid, derivative-floor, boundary/KKT, price-guard or transfer-control change.

## 2. Scientific question

Explain why the accepted annual G2 control path collapses from 20/31 converged HJB calls at turn 1 to 2/31 at turn 2, even though D1 sharply removes transfer/cost/drift far-tail amplification without improving convergence.

The first objective is mechanism classification, not repair. The diagnostic must determine whether failed HJB calls are best characterized by one or more of:

- monotone but too-slow convergence;
- stagnation / plateau;
- oscillation or short-cycle behavior;
- policy-label chattering;
- derivative-safeguard domination or derivative pathology;
- operator/value-update amplification;
- price-input-associated regime change;
- another source-backed mechanism identified by the evidence.

A final failure variable is not enough. The review should identify the earliest observable event/order that distinguishes converged and failed calls where the evidence permits.

## 3. Frozen comparison basis

Use the accepted fresh G2 control route with D1 OFF as the primary scientific object. D1 is accepted diagnostic infrastructure but is not the treatment of this review.

Preferred evidence window is turn 1 versus turn 2 because:

- turn 1 has 20/31 converged and 11/31 failed calls;
- turn 2 has 2/31 converged and 29/31 failed calls;
- accepted D1 evidence established a common entering turn-2 state and no convergence improvement from transfer-tail rejection.

The review may reuse persisted accepted runtime inputs/receipts. Where exact per-call replay is needed, it must use byte-identical persisted call inputs and must not advance the outer multi-province state.

## 4. Mandatory observation layers

Without changing solver semantics, record enough per-HJB-iteration evidence to inspect:

1. convergence statistic trajectory and ceiling behavior;
2. `V_new - V_old` norm/extrema and signed value at the max-absolute-update cell where practical;
3. policy/selector label switching counts and repeated switching/cycle indicators;
4. raw and safeguarded liquid/illiquid value derivatives, derivative-floor hit counts/masks, sign/pathology summaries and raw-to-used deviations;
5. selected consumption, labor, transfer, adjustment cost, `mu_a`, `mu_b` and drift extrema/quantiles needed to establish event ordering;
6. HJB sparse operator invariants relevant to the accepted implementation, including row-sum/off-diagonal checks where defined;
7. direct/linear solve residual or equivalent numerical solve receipt available from the accepted solver path;
8. consumed return/wage values and guard-hit state, for correlation/ordering only, not guard relaxation.

The diagnostic must preserve raw versus safeguarded quantities separately. It must not infer causality merely from end-of-call correlation.

## 5. Comparison design

The first review should compare all provinces for accepted control turn 1 and turn 2 when persisted exact inputs can be reconstructed, yielding four evidence groups:

- turn-1 converged;
- turn-1 ceiling/failure;
- turn-2 converged;
- turn-2 ceiling/failure.

If full 62-call exact replay is available within the task budget, prefer the complete cross-section over hand-picked provinces. If an input identity needed for a replay cannot be proven, do not substitute an approximate state; preserve the limitation and use existing persisted evidence instead.

The review should report both province-level traces and cross-group summaries. Any mechanistic classifier must be preregistered in the task/report before looking at replay outcomes, or otherwise be clearly labeled post-hoc descriptive rather than a gate.

## 6. Frozen science

Continue to hold fixed:

- `MODEL_TIME_BASE=ANNUAL_CONTINUOUS_TIME`;
- `rho=.05/year`;
- `rb=.02/year`;
- borrowing gap `.07/year`;
- firm/HJB `delta=.10/year`;
- `Q_z` off-diagonal `1/3/year`;
- `chi0=.1`;
- `chi1=2 years`;
- accepted transfer FOC and selector/boundary laws;
- derivative floor/safeguard;
- HJB equation, pseudo-time/update law, tolerance, iteration ceiling and linear solver semantics;
- G2 return guard `[-.10,.35]`;
- wage safeguard `[.8,1.3]`;
- fixed theta, `beta_distance=2`, `beta_return=0`;
- same-S quantity/payoff, source-faithful labor and C1 accounting;
- K1B/K2 OFF.

D1 stays OFF for the primary replay object. No D2/D3/OFF continuation experiment is authorized.

## 7. Interpretation boundary

This route may establish that a mechanism is strongly associated with, temporally precedes, or is absent/present in failed calls. It does not automatically authorize changing that mechanism.

If evidence points to derivative safeguards, return interface, wage interface, or boundary/selector authority, the next scientific intervention still requires a new Owner/Reviewer freeze and exact task.

No longer HJB ceiling, altered pseudo-time step, alternative policy iteration, false-transient setting, Newton method, tolerance change, grid change, price-guard change or economic-parameter tuning is authorized by this freeze.

## 8. KFE / Results boundary

KFE remains `DIAGNOSTIC_ONLY`; finite-box upper-b leakage and MATLAB-style pinning remain independent blockers. Standalone KKT residual remains unavailable in accepted evidence.

This route is HA/HJB diagnostic work only. It cannot accept a steady state, GE, annual results, IRF or dissertation Results.

Results eligibility=`FALSE`.
