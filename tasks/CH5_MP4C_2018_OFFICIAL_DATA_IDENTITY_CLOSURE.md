# CH5 MP4C 2018 official-data identity closure

Date: 2026-09-09. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Close the remaining data-identity blocker for the corrected 2018 annual input before any new scientific model execution.

Audit and, where possible, verify from authoritative public sources the 2018 Anhui values/series used by the V2 temporal contract:

1. Anhui 2018 GDP;
2. Anhui 2018 resident population;
3. Anhui fixed-asset-investment observations needed for the 2000–2018 capital-stock recurrence;
4. the resulting 2018 derived total capital stock under the already frozen recurrence and units.

This task is data/evidence work only. It must distinguish **official observed statistics** from **model-derived capital stock**. A capital stock produced by the recurrence must never be described as an official published capital-stock observation unless an authoritative source explicitly publishes that same object.

## 2. Frozen scientific contract

Do not reopen or modify:

- temporal contract version `CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`;
- `steady_year=2008+ii`;
- 2018 `analysis_index=data_mat_index=10`;
- 2018 same-year level row = 19;
- PLM estimator and rolling 10-year window 2009–2018;
- PLM vintage19 / industry4 alpha from the currently hash-bound PLM workbook;
- same-year Zt formula;
- capital recurrence `K0=I0/0.1`, `Kt=(1-.096)K(t-1)+I(t-1)`;
- GDP multiplier 1000 and population multiplier 100;
- province order and Anhui position (MATLAB 12 / Python 11 / Excel N);
- production asset grids, model equations, `a_bar`, rates, GovInv rule, solver/tolerances.

The current provisional 2018 workbook values are evidence to verify, not facts to force-match:

- GDP raw `34010.91` 亿元;
- resident population raw `6076` 万人;
- derived workbook capital stock `1357314108.2013683` in the workbook-derived unit;
- transformed pre-model values GDP `34010910.0`, POP `607600.0`, CAP `1357314108201.3684`.

## 3. Source authority hierarchy

Prefer and document sources in this order when available:

1. National Bureau of Statistics of China (国家统计局) official database/publication;
2. Anhui Provincial Bureau of Statistics / official Anhui Statistical Yearbook;
3. other official government statistical publications with explicit table title, year, unit and revision status.

Non-official mirrors, encyclopedia pages, search snippets, blogs, commercial databases, papers, and secondary citations may be used only as navigation clues, not final authority.

If automated access to an official source is blocked, do not substitute a lower-authority value silently. Produce an exact manual-download request for Owner containing source, table, variable, years, unit and expected comparison target.

## 4. Evidence requirements

For every accepted official observation, preserve at minimum:

- source institution;
- publication/database name;
- table title / indicator name;
- province;
- calendar year;
- raw published value;
- published unit;
- any price basis/current-vs-constant-price wording;
- retrieval date;
- stable URL or publication identifier where available;
- downloaded file name and SHA-256 if a file is obtained;
- source page/table number for PDFs/yearbooks where available;
- notes on revisions or conflicting official vintages.

Do not use OCR unless no structured/text source exists. If a scanned yearbook requires manual extraction, stop with a manual request rather than inventing a value.

## 5. GDP and population closure

Verify Anhui 2018 GDP and resident population against authoritative sources.

Classify each as one of:

- `OFFICIAL_IDENTITY_MATCH`;
- `OFFICIAL_IDENTITY_MATCH_AFTER_DOCUMENTED_UNIT_CONVERSION`;
- `OFFICIAL_REVISION_DIFFERENCE`;
- `OFFICIAL_CONFLICT_NEEDS_OWNER_DECISION`;
- `OFFICIAL_SOURCE_NOT_OBTAINED`.

If multiple official vintages disagree, preserve all values and explain the revision chronology; do not choose whichever matches the workbook.

## 6. Fixed-asset-investment and capital-stock chain

The task must first trace exactly which investment series/sheet the frozen recurrence consumes for Anhui and which observations from 2000 through the 2018 stock are mathematically required. Respect the recurrence timing: document whether 2018 capital depends through 2017 or 2018 investment according to the implemented formula; do not assume from the label alone.

For every required Anhui annual investment observation:

- identify whether current workbook value is original observed, interior-filled, endpoint/extrapolated, or otherwise derived;
- seek an official observation with the same statistical concept and unit;
- document known statistical breaks, especially fixed-asset-investment scope/coverage changes;
- never splice conceptually incompatible official series merely to make a complete vector.

Produce a year-by-year chain table with columns at least:

`year, workbook_value, workbook_status, official_value, official_unit, source_id, comparability_status, conversion, accepted_for_candidate_chain, caveat`.

Allowed comparability statuses include:

- `DIRECTLY_COMPARABLE`;
- `COMPARABLE_AFTER_UNIT_CONVERSION`;
- `STATISTICAL_DEFINITION_BREAK`;
- `OFFICIAL_VALUE_MISSING`;
- `SOURCE_NOT_OBTAINED`;
- `NOT_REQUIRED_BY_RECURRENCE`.

Only if a complete comparable official chain is available may the task compute an **official-source-based candidate model capital stock** using the frozen recurrence. That result must be labeled `MODEL_DERIVED_FROM_OFFICIAL_INVESTMENT`, not official capital stock.

If the chain is incomplete or definition breaks prevent defensible splicing, do not interpolate new values in this task. Return `CAPITAL_CHAIN_OFFICIAL_CLOSURE_INCOMPLETE` and an exact Owner manual-data request.

## 7. Comparison to current provisional V2 input

Create a machine-readable comparison of:

- current provisional workbook raw values;
- official raw values where closed;
- documented unit conversion;
- current transformed V2 input;
- candidate verified transformed value;
- absolute/relative difference;
- identity status;
- whether a corrected-data candidate package is warranted.

Do not change alpha, Zt formula, GovInv, or any downstream model state. If GDP/POP/CAP candidate values differ, Zt may be recomputed only as **static pre-model arithmetic** using the already frozen vintage19 alpha, and must be labeled candidate input arithmetic, not a model result.

## 8. Candidate data package; no production overwrite

If authoritative evidence supports changes, create a new no-overwrite candidate package under the task evidence root containing only the minimal corrected 2018/required-chain data and provenance metadata. Do not modify:

- original Excel workbooks;
- filled workbook;
- PLM workbook;
- old MAT caches;
- protected MATLAB files;
- production annual input source values in place.

The candidate package must have an explicit schema/version and source hashes and must be sufficient for a later bounded pre-model reconstruction after Reviewer acceptance.

If no changes are required, create an identity-closure receipt proving the existing provisional values match the official sources.

## 9. Scientific call budget

All scientific/model calls are ZERO:

- MATLAB = 0;
- household/HJB/KFE = 0;
- root/brentq/direct/iterative/eigen = 0;
- firm/one-turn/controller = 0;
- stationary/GE/annual model = 0;
- IRF/dynamics/Results = 0.

Allowed: web/download access to official public sources, spreadsheet/PDF/table reads, hashes, source comparison, unit conversion, frozen capital recurrence arithmetic, static same-year Zt arithmetic, serialization, and synthetic tests.

## 10. Required outputs

Repository outputs may include:

- `docs/CH5_MP4C_2018_OFFICIAL_DATA_IDENTITY_CLOSURE_REPORT.md`;
- `reports/mp4c_2018_official_data_identity_closure_20260909/official_source_inventory.csv`;
- `.../anhui_2018_gdp_population_identity.csv`;
- `.../anhui_investment_chain_2000_2018.csv`;
- `.../candidate_2018_input_comparison.json`;
- `.../manual_official_data_request.csv` when needed;
- tests/validator code limited to this task;
- manifest/readback/call ledger.

Do not commit copyrighted full yearbooks, raw proprietary files, or large official downloads. Commit citations, hashes, extracted minimal observations and reproducible provenance only.

External evidence root: `D:\ProjectTemp\ch5-2018-official-data-identity-closure-20260909-001`; if occupied, use a fresh suffix. Never overwrite prior evidence.

## 11. Decision logic

Use one primary verdict:

- `OFFICIAL_2018_DATA_IDENTITY_CLOSED__CURRENT_VALUES_CONFIRMED`;
- `OFFICIAL_2018_DATA_IDENTITY_CLOSED__CANDIDATE_CORRECTION_REQUIRED`;
- `PARTIAL_OFFICIAL_IDENTITY__MANUAL_DATA_REQUIRED`;
- `OFFICIAL_SOURCE_CONFLICT__OWNER_DECISION_REQUIRED`.

Separately report:

- `GDP_identity_status`;
- `population_identity_status`;
- `investment_chain_status`;
- `capital_stock_status`;
- `candidate_V2_input_status`;
- `official_source_completeness`;
- `scientific_calls=0`;
- `Results_eligible=FALSE`.

A PASS here establishes data identity only. It does not authorize or imply household, HJB, KFE, firm, GE or steady-state validity.

## 12. Stop conditions

Stop and report rather than improvising if:

- official GDP/population vintages conflict materially without a clear revision hierarchy;
- investment concepts/units cannot be made comparable across the required recurrence window;
- an official source cannot be accessed and the missing value is material to closure;
- completing the task would require changing an economic equation, interpolation method, PLM estimator, temporal contract or model solver.

No successor scientific run is to be started by Builder. Commit and non-force push a dedicated branch; do not merge main.
