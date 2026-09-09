# Chapter 5 MP4C temporal-contract minimal implementation report

Date: 2026-09-09
Verdict: `TEMPORAL_CONTRACT_IMPLEMENTED_STATIC_VALIDATION_PASS`
Results eligibility: `FALSE`

## Implemented behavior

The Python annual/pre-model input layer now uses `CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`. For every supported year 2009–2023 it mechanically binds:

- `analysis_index=steady_year-2008`, `data_mat_index=analysis_index`;
- one-based workbook data row and PLM vintage `steady_year-1999`;
- `ROLLING_10_YEAR`, start `steady_year-9`, end `steady_year`, length 10;
- GDP/CAP/POP, their log ratios, and the unchanged `Zt` formula to the same steady-year level row.

The canonical schema is `CH5_CANONICAL_ANNUAL_PREMODEL_INPUT_V2`, with output identity `CH5_CORRECTED_ANNUAL_PREMODEL_INPUT`, version 2. Serialized input validation rejects a missing or V1 schema, missing/inconsistent temporal metadata, incompatible output identity, a mismatched PLM vintage, and primary/PLM source hash mismatch. The writer now derives the artifact year from its binding instead of hard-coding 2009.

## Static corrected inputs

Two pre-model inputs were constructed directly from hash-verified, read-only workbooks. No economic model was called.

| Year | analysis / data_MAT | level row / year | PLM vintage | rolling window | Zt row / year | alpha |
|---|---:|---|---:|---|---|---:|
| 2009 | 1 / 1 | 10 / 2009 | 10 | 2000–2009 | 10 / 2009 | 0.539451671764441 |
| 2018 | 10 / 10 | 19 / 2018 | 19 | 2009–2018 | 19 / 2018 | 0.772866243094144 |

All required 31-province vectors are finite for both artifacts. The current workbooks remain `PROVISIONAL_AUDITED_SOURCE__OFFICIAL_VERIFICATION_OPEN`; this work does not upgrade them to official national-statistics validation.

## Anhui 2018 lineage

Anhui remains Python zero-based index 11, MATLAB one-based index 12, Excel column N. The corrected 2018 source cells are `GDP!N20`, `常住人口!N20`, and `总资本存量!N20`, corresponding to one-based data row 19/calendar 2018.

| Field | workbook value | multiplier | corrected model input |
|---|---:|---:|---:|
| GDP | 34010.91 亿元 | 1000 | 34010910.0 |
| POP | 6076 万人 | 100 | 607600.0 |
| CAP | 1357314108.2013683, derived workbook unit | 1000 | 1357314108201.3684 |

With vintage19 alpha, corrected same-year `IND_Zt=0.0006934646534806338`. The accepted old mixed-year representation used 2009 level values and a 2020 Zt level anchor; the saved evidence reports corrected-minus-old differences only as descriptive input differences, without causal or model interpretation.

## Stale cache handling

The accepted `ii=15`, industry-4 old-cache alpha is `0.967775174774325`; direct read from the current hash-verified PLM workbook vintage24 gives `1.0219847778591`, a difference of `0.05420960308477507`. The V2 constructor reads the workbook directly. The fail-closed validator does not accept an unversioned legacy cache as corrected input and does not allow that cache to override the workbook.

## Validation and evidence

The dedicated test module covers all 15 year/index/row/vintage mappings, rolling windows, same-year Zt including natural row21 only for 2020, 2018 construction and Anhui location, V2 payload round-trip, rejection cases, dynamic no-overwrite output naming, stale-alpha provenance, absence of solver calls in the annual input module, and protected MATLAB hashes. Final scoped execution with the existing provenance-contract tests: `22 passed in 0.69s`.

An additional attempt to collect the historical `test_mp4c_annual_driver_generalization.py` stopped before test execution because its protected standalone household-oracle bootstrap identity did not match. That validator imports the scientific annual driver and lies outside this task's allowed write paths. The original failure log is retained as `pytest_with_legacy_driver_collection_failure.log`; it did not trigger a model call and was not bypassed or used as PASS evidence.

External evidence root: `D:\ProjectTemp\ch5-temporal-contract-implementation-20260909-001`.

The call ledger records two allowed static pre-model constructions and zero MATLAB, household, HJB, KFE, root, direct/iterative/eigen solve, firm, one-turn, controller, stationary/GE/annual loop, IRF, dynamics, or Results calls. The manifest and final test log are generated after repository files are finalized.

## Limits and open evidence

The 2018 official-data requests for GDP, population, and the investment/capital-stock chain remain open. The 2022–2023 negative-capital observations are a separate data-quality issue. This PASS covers only static annual-input temporal identity; it does not establish household, KFE, firm, GE, annual steady-state, or Results validity.

The protected MATLAB implementation was not changed. Its future minimal patch is specified in `docs/CH5_MP4C_TEMPORAL_CONTRACT_MATLAB_PATCH_SPEC.md`; no scientific run is authorized by this report.
