# Chapter 5 MP4C temporal-contract minimal implementation — Reviewer acceptance

Date: 2026-09-09.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Accepted candidate: `6746565506eb953ea599536d3f745764d225ffef`.
Task: `tasks/CH5_MP4C_TEMPORAL_CONTRACT_MINIMAL_IMPLEMENTATION.md`.

## Verdict

Reviewer marker: `TEMPORAL_CONTRACT_IMPLEMENTATION_ACCEPTED__V2_ROLLING10Y_SAMEYEAR_ZT_STATIC_PASS__OFFICIAL_2018_DATA_STILL_BLOCKS_SCIENCE`.

Accept `TEMPORAL_CONTRACT_IMPLEMENTED_STATIC_VALIDATION_PASS` for the Python annual/pre-model input layer only.

The implementation correctly binds the Owner-approved temporal contract:
- `steady_year = 2008 + ii`;
- one-based level row = `ii + 9`;
- PLM estimator preserved with rolling 10-year window ending at steady year;
- same-year GDP/CAP/POP and same-year Zt source row;
- explicit V2 contract/schema/output identity and source-hash metadata;
- fail-closed rejection of missing, V1/legacy, internally inconsistent, or hash-mismatched corrected-input metadata.

This acceptance does NOT authorize or validate household/HJB/KFE/firm/GE/annual steady-state/IRF/Results execution.

## Accepted evidence

1. V2 contract identifier is `CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`; canonical schema is `CH5_CANONICAL_ANNUAL_PREMODEL_INPUT_V2`.
2. 2009 binds analysis/data_MAT 1/1, level row10/year2009, PLM vintage10, window2000–2009, Zt year2009.
3. 2018 binds analysis/data_MAT 10/10, level row19/year2018, PLM vintage19, window2009–2018, Zt year2018.
4. Calendar 2020 uses row21 only because it is the same-year row for 2020; there is no special fixed-2020 branch in the corrected Python pre-model contract.
5. Anhui remains Python index11 / MATLAB index12 / Excel column N. Corrected provisional 2018 inputs are GDP 34010910.0, POP 607600.0, CAP 1357314108201.3684, alpha 0.772866243094144, and same-year IND_Zt 0.0006934646534806338.
6. Current hash-bound PLM workbook remains primary for corrected input. The old ii15/industry4 cache alpha 0.967775174774325 cannot override current workbook value 1.0219847778591.
7. The protected MATLAB source was not modified; the candidate publishes a specification-only minimal MATLAB patch plan.
8. Scoped tests report 22 passed; py_compile and diff-check passed. Builder manifest reports 32 matched items with SHA256 `F529EF14096482734BC2FB98E90A739F2BBEF5D6AE23CE3D6B3AC8F1D8C10910`.
9. An attempted collection of the historical annual-driver test stopped before test execution due a protected standalone household-oracle identity mismatch. The failure was retained, not bypassed, not counted as PASS, and did not produce a model call.
10. Scientific-call ledger is zero for MATLAB, household/HJB/KFE, roots/solves, firm/one-turn/controller, stationary/GE/annual loop, IRF/dynamics/Results. Two static pre-model constructions are allowed input-preparation operations.

## Reviewer scope

Reviewer performed L3 repository/diff/code/report review and accepted the published test/manifest evidence. Reviewer did not independently execute the local Windows evidence generator, rehash all external evidence, or run scientific models.

## Remaining blocker and next route

The 2018 workbook values used by the corrected static input remain `PROVISIONAL_AUDITED_SOURCE__OFFICIAL_VERIFICATION_OPEN`. Anhui 2018 GDP, resident population, and fixed-investment/capital-stock chain therefore still require official-source identity closure before the first new 2018 scientific run.

The separate 2022–2023 negative-capital/complex-log observations remain unresolved and are not fixed by the temporal-contract implementation.

Until 2018 official-data identity is closed:
- do not start household/firm/GE or annual steady-state science;
- do not tune GovInv/alpha convergence speed;
- do not continue bmax expansion;
- do not silently promote provisional workbook values to official status.

Results eligibility = FALSE.
