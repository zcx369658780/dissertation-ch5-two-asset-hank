# CH5 MP4C 2018 KFE D1-D3 nonlinear HJB-KFE fixed-point design/binding acceptance

Date: 2026-09-17

Reviewer verdict:

`PASS__NONLINEAR_FIXED_POINT_DESIGN_BINDING_ACCEPTED__OWNER_CONVERGENCE_LAW_DECISION_REQUIRED__NO_RUNTIME_AUTHORIZED`

## Accepted candidate

- Candidate: `ee83051d40c1389618288cef61d7d97711c1a861`
- Baseline: `77d7a60763d7670838c9f6cc2cbf7ffd2370aac6`
- Builder classification: `BLOCKED__OWNER_DECISION_REQUIRED_FOR_ITERATION_OR_CONVERGENCE_LAW`
- Changed scientific/runtime paths: none; report-only zero-science gate.

The Builder classification is accepted. The repository authority is sufficient to freeze the nonlinear state, iteration ordering, fixed `Delta=1000`, terminal-only KFE timing, finite resource ceilings, same-value checkpoint consistency, and fail-closed prohibition on damping/adaptive-Delta/continuation/clipping/artificial diffusion. It is not sufficient to select the corrected-target convergence law.

## Accepted design

The nonlinear state is only `V_n`. For each checkpoint, `(P_n,u_n,Q_n)` must be freshly and completely derived from that same `V_n` before any stationary Bellman residual or stability metric is interpreted. The accepted ordering is:

1. derivative construction from `V_n`;
2. one complete 800-cell corrected policy map;
3. one D2 `Q_n` assembly after full-map PASS;
4. same-value Bellman residual and stability diagnostics;
5. if convergence law has not passed, one implicit HJB update with fixed `Delta=1000`.

KFE is not part of every HJB round. It is run only once after an HJB convergence candidate exists, and only on the final same-value `Q*`. The terminal KFE retains the accepted pin-free/source-free contract.

The accepted `V1/P1/u1/Q1` may be used directly as checkpoint 1. `p1` remains operator evidence only and is not an HJB state or later-KFE warm start.

The call-725 trajectory ceiling remains at most 100 HJB updates total. The already accepted `V0 -> V1` update consumed update 1; no more than 99 future updates through `V100` are available. Unused calls from a failed round cannot be recycled into a retry.

## Unresolved Owner authority

Before any continuation runtime, Owner must freeze all of the following prospectively:

- stationary Bellman-residual threshold and comparison rule;
- value-change threshold and its conjunction with Bellman residual;
- whether policy stability and operator stability are mandatory termination guards or diagnostic-only evidence, including any required consecutive-checkpoint window;
- prospective direct-linear-solve backward-error rejection bound;
- non-exact cycling/oscillation criterion and window.

Historical `max|V_new-V_old| < 1e-7` is provenance only and is not corrected-target authority.

No Builder may infer these thresholds from the already observed V0/V1/Q0/Q1 trajectory or tune them after execution begins.

## Prohibited without new authority

Damping, relaxation, adaptive `Delta`, line search, parameter continuation, averaging, clipping, artificial diffusion, derivative floors/caps, topology repair, solver substitution and scientific retry remain unauthorized.

## Current gate

No scientific runtime successor is authorized. There is no active Builder scientific task until the Owner adopts a convergence law.

Results eligibility remains `FALSE`. Production replacement, GE, annualization, shocks, IRFs and paper Results remain outside this gate.
