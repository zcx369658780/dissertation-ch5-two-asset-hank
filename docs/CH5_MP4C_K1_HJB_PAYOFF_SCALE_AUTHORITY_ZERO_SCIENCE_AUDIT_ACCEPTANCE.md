# Chapter 5 MP4C K1 HJB payoff-scale authority zero-science audit acceptance

Date: 2026-09-12.

Reviewer verdict:

`K1_HJB_PAYOFF_SCALE_AUTHORITY_AUDIT_ACCEPTED__ANNUAL_FIRM_FLOW_AND_QUARTERLY_DEPRECIATION_CONFLICT_CONFIRMED__DIRECT_RA0_TO_HJB_RA_MAPPING_NOT_AUTHORIZED__ADDITIONAL_ZERO_SCIENCE_PROVENANCE_CLOSURE_REQUIRED`

Accepted candidate:

`367de55e60d144042b0a95ad1fd49fbc5267f85f`

## Scope accepted

This acceptance covers the zero-science time-unit, dimensional-consistency, legacy/dissertation authority and hard-bound audit only. The candidate is one commit ahead of baseline `060b6e4afe481740a2e80288bdbfa6e0d26768af` and changes only one audit report, compact static receipts, one zero-science builder and one focused test file. No `src/` scientific model code, calibration, bound, solver, grid, tolerance, K1B/K2 or Results artifact is changed.

## Accepted scientific findings

1. Corrected-2018 firm `Y` is an annual GDP flow while `K` is a capital stock. Therefore `rk=mt*alpha*Y/K` and profit/K inherit annual flow/stock rate units absent another explicit normalization.
2. Dissertation Chapter 4 explicitly identifies `delta=.025` as a quarterly depreciation rate. Active code also uses `.025`, while the current Chapter-5 parameter table prints `.0025`. The active `ra0=rk+after_tax_profit_over_K-delta` therefore combines source objects with conflicting calendar periods.
3. The stationary household HJB is continuous-time and requires `rho`, `rb`, `r_a`, `Q_z`, wage/transfer/adjustment-cost flows and asset drifts to share one HJB-time convention. Existing Chapter-5/legacy sources do not close that common calendar unit.
4. Historical direct wiring from firm return to `rah/r_a` proves implementation provenance only; it does not establish dimensional consistency.
5. Direct numerical identity `HouseholdInputs.r_a = firm ra0` is therefore not authorized for further runtime under current source authority.
6. No source-backed `/4`, compounding, logarithmic, normalization, shrinkage or other conversion was established. None is frozen by this acceptance.
7. Historical `ra [.02,.09]` and `wjt [.8,1.3]` remain safeguards/partially unresolved numerical devices rather than automatically valid structural calibration bounds.
8. Owner's diagnostic-bound policy remains valid for future exact debugging tasks, but no new bounds are activated by this acceptance.

## Boundary

Raw `ra0` remains the retained economic payoff source object. What is rejected is the unqualified numerical identity between the currently computed raw firm-return level and HJB `r_a`.

This acceptance does not authorize any runtime, annualization/deannualization, parameter rewrite, hard-bound change, K1B, K2, KFE upgrade, 25-turn raw trajectory, steady-state claim or Results claim.

KFE remains `DIAGNOSTIC_ONLY`; finite-box upper-b leakage and MATLAB-style pinning remain independent blockers. Results eligibility remains `FALSE`.

## Next gate

The next gate is a fresh zero-science source/calibration provenance closure for quarterly-HJB versus annual-firm-flow timing. It must resolve or explicitly classify the Chapter-4/Chapter-5/code depreciation conflict and assemble a coherent common time-scale authority for `rho`, `rb`, `r_a`, `Q_z`, annual `Y/K`, wage, transfer and adjustment-cost flows. If source evidence cannot uniquely determine that convention, the report must stop at a precise Owner calibration decision rather than invent a conversion.
