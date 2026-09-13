# CH5 MP4C K1 — HJB convergence-mechanism turn1/turn2 diagnostic acceptance

Date: 2026-09-13.

Reviewer verdict:

`HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC_ACCEPTED__POLICY_CHATTERING_AND_NONMONOTONE_VALUE_UPDATE_PRECEDE_LATER_DERIVATIVE_FLOOR_AMPLIFICATION__NO_CAUSAL_INTERVENTION_YET`

Accepted candidate: `c6d89327933edef2b942f10f462b58cfa6b52954`.

## Acceptance basis

The candidate is accepted as an observation-only, exact-input HJB mechanism diagnostic under the frozen annual G2 control science with D1 OFF.

Independent review verified the candidate is a single commit directly ahead of baseline `79ced4f7a2f5e05722a77d23d75e37ee4eada058`, with changes confined to task-owned validator code/tests, compact evidence, report and CURRENT closeout docs. The instrumentation wrapper preserves the accepted HJB scientific operation order and places diagnostics after accepted scientific operations; the published parity receipt reports exact OFF/ON equality and exact accepted-output equality on the parity call.

Accepted execution facts:

- exact-input replay coverage `62/62`;
- instrumentation parity `PASS`;
- `64` total HJB calls = `2` parity + `62` exact replay;
- `4,689` HJB direct solves;
- scientific retries `0`;
- KFE, outer trajectory advancement, MATLAB, firm runtime, K1B/K2, GE, annual downstream, shock/IRF and Results calls all `0`;
- `62/62` replay scientific outputs and `62/62` final operators exact-equal to accepted artifacts;
- turn1 convergence `20/31`, turn2 convergence `2/31`, exactly reproducing accepted evidence.

## Accepted mechanism evidence

The supported descriptive classification is:

`POLICY_CHATTERING_WITH_VALUE_UPDATE_OSCILLATION_AND_LATER_DERIVATIVE_FLOOR_AMPLIFICATION__NOT_PURE_TWO_CYCLE__NOT_MONOTONE_SLOW`.

This remains explicitly `POST_HOC_DESCRIPTIVE_FROM_PREREGISTERED_CONTINUOUS_METRICS__NOT_A_GATE` and is not a causal claim.

Key accepted temporal facts:

- among all `40` failed calls, policy switching precedes the first derivative-floor hit in `40/40`;
- value-statistic non-decrease precedes the first derivative-floor hit in `38/40`;
- two-step label reversion precedes the first derivative-floor hit in `21/40`;
- all `20/20` provinces that converged in turn1 fail in turn2;
- in that transition set, policy switching first appears at iteration 2 for all 20, while first derivative-floor hits appear later at iterations 3/4/5;
- initial absolute linear-solve residuals across all 62 calls lie in approximately `4.39e-14` to `9.25e-14`, so the evidence does not support direct-solve failure as the initiating event;
- accepted signed off-diagonal / boundary row-sum operator features occur in both successful and failed calls and therefore do not isolate the convergence split;
- return/wage guard states do not separate successful from failed turn2 calls, and wage saturation already coexists with both success and failure in turn1.

The failed-call traces are not uniformly monotone-slow. Persistent switching/reversion and non-monotone value updates, including a turn2-failed median final/initial statistic ratio above one, do not support simply increasing the 100-iteration ceiling.

## Scientific interpretation boundary

The acceptance supports a fixed-point / policy-map instability diagnosis more strongly than the previously prioritized derivative-floor, return-interface or wage-interface explanations as the *initiating* mechanism. Derivative-floor activity remains an important later amplifier/co-traveller, not an exonerated mechanism.

No same-state intervention was run. Therefore this acceptance does not establish that policy switching causes nonconvergence, nor does it authorize any solver, pseudo-time, damping, policy-iteration, derivative-floor, price-guard, boundary/KKT, tolerance, grid or economic-parameter change.

## Remaining boundaries

KFE remains `DIAGNOSTIC_ONLY`; finite-box upper-b leakage and MATLAB-style pinning remain independent blockers. Standalone KKT residual remains `UNAVAILABLE_IN_ACCEPTED_EVIDENCE`.

Return/wage safeguards remain binding and `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS` remains a later scientific requirement.

Results eligibility remains `FALSE`.

## Exactly one next Owner gate

`OWNER_HJB_ITERATION_FIXED_POINT_MECHANISM_INTERVENTION_DESIGN_FREEZE`

The next gate should choose one isolated same-input intervention on the HJB fixed-point map, with all economic inputs, equations, grids, tolerances and price guards otherwise fixed, before any successor runtime task is published.
