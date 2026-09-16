# CH5 MP4C 2018 KFE D1-D3 interior zero-liquid Z switching law — Owner adoption acceptance

Date: 2026-09-16
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

## Owner decision

Owner explicitly adopts inheritance of the historical/accepted-HJB interior zero-liquid `Z` switching law into the separately governed corrected D1-D3 selector.

Adopted decision text:

`同意继承 interior zero-liquid Z switching law`

## Scientific meaning

The corrected selector may include an interior liquid `Z` candidate only when the same frozen non-liquid branch/regime yields a genuine forward/backward direction crossing and a unique finite positive liquid shadow solving the zero-liquid-drift equation.

This adoption does not authorize averaging, interpolation, derivative floors, clipping, drift repair, fitted tolerances, new calibration, seed switching or any change to D1/D2/D3 economics. It inherits the repository's zero-liquid upwind/Hamiltonian switching concept while keeping the corrected D1-D3 boundary/KKT/generator laws unchanged.

## Exact corrected-target Z contract

For an interior liquid node only:

1. Evaluate the already-authorized backward and forward liquid derivative candidates under the same a-side active set / derivative branch / transfer regime.
2. A `Z` root is eligible only if both raw one-sided liquid shadows are finite and positive and the corresponding liquid drifts form a strict direction-crossing bracket: backward candidate drift is positive while forward candidate drift is negative, with neither endpoint already direction-consistent through zero under the prospective arithmetic bound.
3. Solve the frozen liquid-drift equation for `q_b` on the closed interval between the two positive one-sided shadows. Require exactly one finite positive root. The root must lie within that interval; otherwise the `Z` candidate is invalid.
4. Recompute all controls and a-side KKT objects from that `q_b` using the same frozen D3 branch law. No averaging or interpolation of controls or derivatives is allowed.
5. Persist the raw root residual, prospective arithmetic bound, bracket endpoints, endpoint drifts, root identity and marker `INTERIOR_LIQUID_Z_ZERO_DRIFT_SWITCH`.
6. If the raw zero-drift residual is within the prospective arithmetic bound, represent consumed `g_b` as exact `0.0`; otherwise reject the candidate. This canonicalization is specific to the mathematically defined `Z` zero-drift equation and does not relax D2's strict outward-face rule.
7. The `Z` candidate must pass all existing domain, a-side feasibility, multiplier, complementarity, transfer-KKT and finite-value checks and must enter the same admissible Hamiltonian comparison/deduplication as backward/forward candidates.
8. If no strict crossing exists, no interior `Z` root may be invoked. If the root is absent, nonunique, nonfinite or outside the derivative interval, reject fail-closed; do not retry or widen the bracket.

The adopted law is generic for corrected-target interior liquid switching cases; it is not a Cell-5-specific patch.

## Root budget consequence

The previous corrected-HJB design ceiling of 264 roots assumed interior liquid cells were root-free and is superseded for tasks that implement this adopted `Z` law.

For the `(20,20,2)` call-725 grid, there are 720 interior-`b` cells. Under the current frozen selector enumeration, each such cell has at most four a-side/transfer combinations that can reach an interior liquid `Z` root. Therefore a conservative exact additional ceiling is `720*4=2880` interior-Z root invocations. Retaining the previously accepted 264 boundary-liquid root ceiling gives a total root ceiling of `3144` for one fresh complete Option-A map.

This is an operation ceiling, not permission to invoke roots when the strict crossing trigger is absent. No outcome-dependent budget enlargement is allowed.

## Interpretation boundary

This Owner adoption changes only the corrected selector's interior liquid switching law. It does not establish HJB convergence, KFE validity, production readiness, GE/annual/shock/IRF validity or Results eligibility. Results eligibility remains `FALSE`.