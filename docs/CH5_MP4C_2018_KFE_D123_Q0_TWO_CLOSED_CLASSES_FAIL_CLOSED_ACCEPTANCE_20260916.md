# CH5 MP4C 2018 KFE D1-D3 Q0 two-closed-class fail-closed acceptance

Date: 2026-09-16

## Verdict

`PASS__Q0_TWO_CLOSED_CLASSES_FAIL_CLOSED_EVIDENCE_ACCEPTED__UNIQUENESS_FAILS_STRUCTURALLY_FOR_Q0__CLASS_MEMBERSHIP_AND_BASIN_ATTRIBUTION_REQUIRED_NEXT`

Reviewer accepts Builder candidate `132b2657c61e0707a5fff96b936b5a62a78dbb2e` as valid bounded fail-closed evidence.

Accepted facts:

- exact accepted Q0 identity is preserved;
- accepted D2 construction identity remains exact `0.0`;
- secondary CSR reaggregation discrepancy `3.552713678800501e-15` is inside the previously frozen prospective bound `5.222144858126786e-14`;
- `max(abs(Q0 @ 1))=3.552713678800501e-15` passes the same accepted conservation bound;
- negative off-diagonal count is zero and all four asset-face outward drift/rate/flux ledgers are exact zero;
- the exact-positive off-diagonal graph has 2318 directed edges, 400 SCCs of size 2, exactly two closed communicating classes, each size 2, and 796 transient states;
- the task correctly stopped before GESVD, mass normalization or `Q0.T @ p`.

## Scientific meaning

For a finite conservative continuous-time Markov generator, more than one closed communicating class is structural evidence that the invariant stationary space is not unique. Therefore the previously frozen `one closed communicating class` uniqueness requirement is not met by accepted Q0. This is not a numerical-SVD ambiguity and must not be repaired by pinning, edge tolerances, artificial diffusion, source terms, clipping or selecting one class by convenience.

The current evidence does not yet identify which asset coordinates/policies form the two closed classes, whether they are created by exact zero-drift Z policies, boundary/state-constraint behavior, or another accepted policy combination, nor how the 796 transient states partition into attraction basins. Those facts are required before deciding whether the two recurrent classes are an expected property of the one-step V0 policy operator, an artifact of the diagnostic seed/grid, or a blocker for any later fixed-point route.

No claim is made about nonlinear HJB convergence, Q1, corrected fixed-point existence, economic multiple equilibria, stationary economic equilibrium, production readiness or Results. Results eligibility remains `FALSE`.

## Next gate

Authorize only a bounded structural attribution of the two closed communicating classes and their basins. Do not run GESVD, stationary-mass solving, selector, HJB, KFE solve, MATLAB or downstream blocks. The next task must map each closed class to exact F-order states and accepted cell receipts, report their selected policies and consumed drifts, identify incoming basin membership for all transient SCCs, and determine whether class closure follows from exact zero asset drift or from directed asset-flow topology.
