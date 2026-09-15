# CH5 MP4C K1 — J640 HJB nonconvergence mechanism diagnostic acceptance

Date: 2026-09-15

Reviewer verdict:

`J640_HJB_MECHANISM_DIAGNOSTIC_ACCEPTED__POLICY_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION__FINER_J_ESCALATION_CLOSED`

Candidate accepted: `b1c4897c72e3c11c1774ec59145865ae3f5fa6ca`.
Baseline: `11d3839f6bc500709fe4fbf65edfc346bb7748f1`.

The candidate is a one-commit direct successor of the baseline. Changed paths are confined to the task report, compact evidence, focused test, and task-owned diagnostic validator package. Protected HJB/KFE source, oracle, MATLAB source, equations, FOCs, selectors, boundaries, derivative floors, solver, tolerance, maxit, mappings, guards, asset bounds, and economic parameters were not modified.

Accepted scientific finding:

- J640 failure is exactly reproducible at frozen inputs and frozen maxit=100.
- Final `max|dV|=0.0012277767122459426` matches the prior accepted J640 failure exactly.
- All operators remained legal and finite; no hard error or shape failure occurred.
- First selector switching: iteration 2.
- First convergence-statistic non-decrease: iteration 8.
- First derivative-floor hit: iteration 10.
- 61 adjacent decreases and 38 non-decreases; largest rebound about `0.07724984`.
- Selector changes remained active through most iterations; value hashes were all unique and no exact period-2/3 cycle was found.

Accepted mechanism class:

`POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`

Derivative-floor activity is accepted as later co-traveller/amplifier evidence, not the initiating event. Exact low-period cycling is not supported.

Route decision:

The finer-J escalation route is closed under the current accepted source-faithful HJB algorithm. Do not raise maxit, add damping/relaxation/line search, alter tolerance/floors/selectors, or continue to J1280/J2560 in order to manufacture convergence.

The project does not require continuum-grid convergence as a correctness criterion for the MATLAB-faithful household block. The original MATLAB authority used a much coarser grid. Current evidence instead supports a bounded practical-grid strategy:

- `J160` remains the provisional working illiquid-grid density for cross-state diagnostics.
- `J320` is retained as a valid one-point high-resolution sensitivity check at the representative state.
- This is not a claim that J160 is continuum-converged or production-final.

At the representative state, J160→J320 changes are comparatively small in aggregate/marginal terms (`Delta At≈-0.1280`, a-CDF distance≈0.00213), while J640 enters the accepted chatter mechanism. This supports using J160 as the next bounded cross-state diagnostic grid rather than pursuing finer J.

Results eligibility remains `FALSE`.
