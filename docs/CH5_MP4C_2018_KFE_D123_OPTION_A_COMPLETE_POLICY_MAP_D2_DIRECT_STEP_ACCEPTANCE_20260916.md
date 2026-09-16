# CH5 MP4C 2018 KFE D1-D3 Option A complete corrected map / D2 / direct-step — Reviewer acceptance

Date: 2026-09-16

Reviewer verdict:

`PASS__OPTION_A_COMPLETE_CORRECTED_POLICY_MAP_ACCEPTED__D2_CONSERVATIVE_GENERATOR_AND_SINGLE_DIRECT_HJB_STEP_ACCEPTED__ONE_STEP_DIAGNOSTIC_ONLY__KFE_NOT_YET_AUTHORIZED`

Accepted Builder candidate: `9a4eb0e5ec3627743596daa9b991436d2124efa9`.

The candidate is one commit ahead of baseline `c2e3c257a1e508acf9f567a3d672ca4c751dc770`. The Owner-adopted interior liquid `Z` switching law is implemented only for strict interior liquid direction crossings, with positive one-sided shadow endpoints, a root confined to that interval, no widening/retry/interpolation/floor/cap/clipping, and full recomputation of controls, a-side KKT and Hamiltonian before ordinary candidate comparison.

Fresh Option A execution produced 800/800 durable `SELECTED_ADMISSIBLE` receipts. Real selector evaluations were 800, total scalar roots 442, interior-Z roots 206, selected Z policies 42, retries 0. Cell 5 selected the expected active-lower-a / zero-kink / Z policy with consumed `g_b=0.0` and `INTERIOR_LIQUID_Z_ZERO_DRIFT_SWITCH` marker. No liquid-face Z candidate was generated.

D2 was assembled once only after the complete map and passed: minimum offdiagonal `0.2642984748447064`, exact diagonal-construction error `0.0`, `max_abs(Q*1)=3.552713678800501e-15` within the prospective bound, and both asset-coordinate action checks had zero violations. No outward-face drift was tolerance-repaired.

One sparse direct HJB solve was then executed. It returned finite `V1`, residual infinity norm `2.5875135367670055e-14`, normwise backward error `1.9727855630325988e-16`, and V1 SHA-256 `5C410EBC329F08B37F941A783E7F2C84BFCDCB67C6E24118114BE8C55697F2E2`.

Post-execution scientific/test hashes match the pre-execution freeze. The sealed evidence manifest contains 810 entries. KFE, MATLAB, outer/firm/wage-return, GE, annual, shock, IRF and Results calls were all zero. There was no V1 selector map or nonlinear continuation.

Interpretation boundary: this acceptance establishes one complete corrected Option-A policy map, one passing D2 conservative generator, and one numerically valid direct linear HJB step. It does not establish nonlinear HJB convergence, a corrected fixed point, stationary-density validity, steady-state equilibrium, production replacement or Results eligibility. Results eligibility remains `FALSE`.

Before any KFE runtime, Reviewer requires a separate zero-science design/binding gate to determine the exact operator object to validate, whether the accepted pre-step `Q0` may be used as an operator-level KFE diagnostic without a V1 policy remap, and the pin-free conservation/nullspace/rank/nonnegativity/normalization/uniqueness contract. No KFE call is authorized by this acceptance.
