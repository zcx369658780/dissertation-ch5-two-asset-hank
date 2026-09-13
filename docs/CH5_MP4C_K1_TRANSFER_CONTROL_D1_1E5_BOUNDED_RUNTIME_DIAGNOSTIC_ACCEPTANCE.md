# CH5 MP4C K1 transfer-control D1=1e5 bounded runtime diagnostic acceptance

Date: 2026-09-13.

Reviewer verdict:

`D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC_ACCEPTED__FAR_TAIL_STRESS_REDUCED__HJB_CONVERGENCE_NOT_IMPROVED__NO_LONGER_D1_OR_WIDER_D_STAGE_AUTHORIZED__OWNER_HA_NUMERICAL_CONTRACT_REASSESSMENT_REQUIRED`

Accepted candidate:

`c7d29f5bc0751751f1547072eac79eff916a8240`

## Accepted scope

This acceptance covers the bounded fresh-G2-control versus G2+D1 five-turn diagnostic under the Owner-frozen D1 contract. D1 is symmetric `[-1e5,+1e5]`, inclusive, post-FOC and pre-selector. Raw FOC candidates are preserved; inadmissible branches are excluded from selector competition; the existing zero-transfer option and other admissible branches remain available; clipping and manufactured endpoint candidates are prohibited.

The optional D1 implementation defaults OFF and passed OFF-oracle parity, raw-before-eligibility identity, no-hit ON/OFF parity, inclusive endpoint, zero-option, other-admissible-branch and no-clipping gates.

## Accepted findings

1. Turn 1 is exact-equal and turn 2 enters from the same completed scientific state, with identical return/wage inputs, grids, numerics, same-S provenance and pre-eligibility raw transfer candidates.
2. D1 rejected `15,330/39,440,000` active raw branches in turns 2–5 (`0.0388692%`). There were `3,459` iteration-cell winner changes: `2,156` to the already existing zero option and `1,303` to another admissible nonzero branch. No changed cell appeared without a rejected control contributor.
3. D1 sharply reduced far-tail selected-transfer and associated cost/drift extrema: selected `|d|` max fell from about `4.27e7` to below `1e5`; adjustment-cost max from about `1.92e14` to `3.79e9`; corresponding `mu_a` and `mu_b` extrema fell by similar orders of magnitude.
4. This tail reduction did not improve HJB convergence. Treatment turns 2–5 were control `6/124` versus D1 `5/124`; all-turn convergence was `26/155` versus `25/155`. D1 used 87 more HJB iterations. Turn-2 same-state convergence remained `2/31` versus `2/31`.
5. D1 therefore identifies explosive transfer candidates as a major far-tail numerical-stress amplifier, but not as the dominant blocker to HJB convergence under the current annual price-interface and HA numerical contracts.
6. Return and wage safeguards remain heavily binding. `ZERO_DIAGNOSTIC_PRICE_GUARD_HITS` is not met.
7. same-S, capital conservation, C1 accounting, source-faithful labor, no same-turn feedback and raw-`ra0` provenance remain within accepted tolerances. No scientific NaN/Inf hard stop or scientific exception occurred.
8. KFE remains `DIAGNOSTIC_ONLY`; finite-box upper-b leakage and MATLAB-style pinning remain independent blockers. Standalone KKT residual remains `UNAVAILABLE_IN_ACCEPTED_EVIDENCE`.

## Reviewer decision

The evidence does **not** authorize:

- longer D1 continuation;
- D2/D3/OFF transfer-control stages;
- G3/G4 return-guard widening;
- wage-guard relaxation;
- tuning `chi0`/`chi1`;
- derivative-floor, grid, tolerance, solver, boundary/KKT or equation changes;
- K1B/K2, steady-state acceptance, GE, IRF or Results.

The narrow D1 implementation remains accepted as temporary numerical-diagnostic infrastructure with OFF exact-parity, but it is not promoted to a provisional steady-state solution route.

## Next gate

`OWNER_HA_NUMERICAL_CONTRACT_REASSESSMENT_REQUIRED`

The next discussion should treat D1 as evidence that far-tail transfer explosion is not sufficient to explain the convergence failure. Before another scientific runtime, Owner/Reviewer should decide which remaining HA/HJB numerical contract deserves the next isolated gate. Candidate families include price-interface calibration/safeguards, wage-interface calibration, derivative/value-function numerical safeguards, and HJB iteration/solution method diagnostics. No successor Builder task is published by this acceptance.

Results eligibility remains `FALSE`.
