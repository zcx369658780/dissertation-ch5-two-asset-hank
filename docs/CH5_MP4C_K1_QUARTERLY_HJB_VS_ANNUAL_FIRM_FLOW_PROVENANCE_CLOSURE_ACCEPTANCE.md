# Chapter 5 MP4C K1 quarterly-HJB vs annual-firm-flow provenance closure acceptance

Date: 2026-09-12.

Reviewer verdict:

`K1_TIME_BASE_PROVENANCE_CLOSURE_ACCEPTED__COMMON_CALENDAR_BASE_NOT_SOURCE_IDENTIFIABLE__GENUINE_DEPRECIATION_CALIBRATION_CONFLICT__OWNER_COMPLETE_RECALIBRATION_CONTRACT_REQUIRED`

Accepted candidate:

`c94352740f4390bbf2fbaecae93c486395afe83f`

## Scope accepted

This acceptance covers the zero-science source/calibration provenance closure only. The candidate is one commit ahead of baseline `331d46a3044fcff7ed089d1f88705683eb86722a` and changes only one report, compact static evidence, one zero-science audit builder and one focused test file. No `src/` scientific implementation, parameter, bound, solver, grid, tolerance, K1B/K2 runtime or Results artifact is changed.

## Accepted findings

1. Existing sources do not uniquely identify one common Chapter-5 calendar base for the continuous-time HJB and firm block. Quarterly-HJB and annual-HJB conventions both remain incomplete; abstract model time is the only source-honest current convention.
2. Corrected-2018 `Y/K` and profit/K inherit annual firm flow/stock scale, while Chapter 4 explicitly describes `delta=.025` as quarterly depreciation. Chapter 5 prints `.0025`, active Python/protected MATLAB use `.025`, annualized prose is approximately `.10`, and PIM `.096` belongs to capital-stock construction. This is a genuine calibration/provenance conflict, not a Builder-resolvable typo.
3. No complete source-backed annual-firm-flow to HJB-flow bridge was found. `/4`, `*4`, compounding and `log(1+r)` are therefore not authorized by source provenance.
4. A valid recalibration must jointly close `rho`, `rb`, `r_a`, `Q_z`, `delta`, annual `Y/K`, wage/asset numeraire, transfer, consumption, adjustment-cost flow and `chi1`; repairing only `ra0` would remain dimensionally incomplete.
5. Raw firm objects must be preserved before any future conversion. Temporary diagnostic guards, if later authorized, belong after the Owner-frozen conversion at the HJB interface, with raw/converted/guarded receipts and saturation counts preserved separately.
6. Historical `[.02,.09]` return and `[.8,1.3]` wage guards remain numerical safeguards/unresolved legacy devices; they are not structural calibration authority and must not be silently reused before conversion.
7. No `STATIC_NO_FEEDBACK` transformed table is accepted because no legitimate conversion law has yet been frozen.

## Boundary

This acceptance does not select annual versus quarterly HJB time, does not choose `.025`, `.0025`, `.10` or `.096` as the final depreciation calibration, and does not authorize any runtime, payoff mapping, parameter rewrite, hard-bound change, K1B, K2, KFE upgrade, steady-state claim or Results claim.

KFE remains `DIAGNOSTIC_ONLY`; finite-box upper-b leakage and MATLAB-style pinning remain independent blockers. Results eligibility remains `FALSE`.

## Next gate

The next gate is an Owner scientific freeze of a complete common time-base and recalibration contract. The contract must explicitly choose the model-time base and jointly specify the treatment of `delta/rho/rb/Q_z`, annual firm-flow conversion, wage/asset numeraire, transfer/consumption/adjustment-cost flows, `chi1`, and the permitted conversion law. Only after that freeze may Reviewer issue a bounded runtime diagnostic task with preregistered temporary guards if desired.
