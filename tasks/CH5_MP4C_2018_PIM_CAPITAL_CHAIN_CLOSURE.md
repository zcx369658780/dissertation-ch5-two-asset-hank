# CH5 MP4C 2018 PIM capital-chain closure

Date: 2026-09-09. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner scientific authority.

## 1. Owner decision now frozen

Owner has explicitly decided that the Chapter 5 province capital stock remains a **model-constructed perpetual-inventory-method (PIM) object**, not an official published capital-stock series.

Do not continue treating the absence of an official Chinese capital-stock series as a blocker. Do not search for or invent an official capital-stock table.

The existing Chapter 5 PIM specification remains frozen for this task:

- `K0 = I0 / 0.1`;
- `Kt = (1 - 0.096) * K(t-1) + I(t-1)`;
- depreciation rate remains `0.096`;
- no change to the initialization rule;
- no change to units/multipliers unless the existing source contract itself requires an already-documented conversion;
- for `K2018`, the required flow sequence is `I2000..I2017`; `I2018` is not used in the recurrence.

This task does **not** authorize choosing another PIM formula, another depreciation rate, another initial-capital estimator, or a different investment concept merely to improve convergence.

## 2. Objective

Close the 2018 capital-stock data-method blocker by converting the existing province-level investment/PIM path from a provisional lineage into a versioned, auditable model-calibration contract.

The task must answer:

1. Does the accepted current Anhui province-level investment sequence `I2000..I2017` reproduce the existing 2018 workbook-derived capital stock exactly under the frozen recurrence?
2. What source/provenance status should be attached to that sequence, given that it originates from the existing CNKI-curated province panel and contains no fill for Anhui 2000–2018?
3. How should the documented 2011 fixed-asset-investment statistical coverage break be represented as a limitation without silently pretending full official comparability?
4. Can the purchased `sj479` city investment series contribute a descriptive cross-check of direction/growth without being aggregated into a province total or replacing the province series?
5. Can a versioned 2018 capital-input receipt be produced that is adequate for later V2 pre-model reconstruction while preserving all caveats?

## 3. Source hierarchy for this task

The purpose here is no longer to prove an official capital-stock identity. Keep the source roles distinct:

### A. Current province-level investment chain

Existing source workbook under the protected original data root, already audited in prior tasks. For Anhui, 2000–2018 investment cells were previously classified `ORIGINAL_OBSERVED_UNCHANGED` between raw and filled workbooks.

Treat these values as:

`MODEL_CALIBRATION_SOURCE__CNKI_CURATED_PROVINCE_PANEL`

unless source evidence supports a more precise provenance label.

Do **not** upgrade them to official statistics solely because they are used in the model.

### B. Official publications

Use accepted prior evidence only to document known statistical-definition breaks or revisions. This task does not need to re-search all official investment values.

### C. Purchased `sj479` city investment data

May be used only as a secondary descriptive cross-check. Because the six-condition city-to-province aggregation gate failed in the accepted purchased-data audit, this task must not compute or use a province city-sum candidate unless the task discovers genuinely new evidence that independently closes every gate. In the ordinary path, do not aggregate.

## 4. Required recurrence closure

Read the accepted Anhui province-level investment sequence for 2000–2017 from the protected source workbook / audited lineage.

Mechanically reconstruct:

- `K2000 = I2000 / 0.1`;
- `K2001 = (1-.096)K2000 + I2000`;
- continue exactly under the source implementation's timing convention through `K2018`.

Do not assume index labels; reproduce the exact source timing and verify against the existing `It_to_Kt.m`/accepted audit contract.

Compare the reconstructed `K2018` with the existing workbook-derived 2018 capital stock:

`1357314108.2013683`

Report:

- exact/binary64 equality if applicable;
- absolute difference;
- relative difference;
- first year of any divergence;
- full recurrence ledger sufficient to diagnose a mismatch without running MATLAB.

If the frozen source recurrence does not reproduce the existing workbook-derived value, stop with `PIM_SOURCE_REPRODUCTION_MISMATCH` rather than changing parameters.

## 5. 2011 statistical-definition break

The accepted official evidence records a 2011 fixed-asset-investment coverage change.

Owner has decided to retain the existing PIM/model calibration route despite this limitation. Therefore:

- do not treat the 2011 break as an automatic blocker to using the existing Chapter 5 calibrated province series;
- do not claim the entire 2000–2017 series is an official same-definition panel;
- explicitly classify the series as a model calibration dataset crossing a documented statistical-definition break;
- preserve the break in metadata and future paper/model limitations;
- do not create a synthetic backcast, bridge factor, splice, interpolation, or rescaling in this task.

Required metadata should include something equivalent to:

`statistical_comparability = MODEL_CALIBRATION_SERIES_WITH_DOCUMENTED_2011_DEFINITION_BREAK`

## 6. Purchased city-data cross-check

Using accepted purchased-data evidence, optionally perform only descriptive comparisons that do not require province aggregation, for example:

- whether city-level investment is predominantly increasing/decreasing around selected years;
- distribution of city growth rates for Anhui;
- whether the province-level series direction is grossly inconsistent with the city panel;
- source coverage notes for 2000–2016 versus derived 2017 levels.

Do not compute a city sum merely for convenience.

Do not use city data to overwrite any province investment observation.

Any such evidence must be labeled `SECONDARY_DIRECTIONAL_CROSSCHECK_ONLY`.

## 7. Versioned PIM capital-input receipt

If recurrence reproduction passes, generate a versioned, no-overwrite machine-readable receipt for the 2018 capital input.

Suggested schema identifier:

`CH5_2018_PIM_CAPITAL_INPUT_V1`

It must record at least:

- target year `2018`;
- source investment years `2000..2017`;
- source workbook identity/hash;
- province = Anhui;
- province index identities;
- source classification;
- raw investment unit;
- recurrence formula;
- initialization formula;
- depreciation rate `0.096`;
- timing convention;
- derived `K2018`;
- transformed V2 CAP input if applicable;
- statistical comparability caveat for the 2011 break;
- source lineage status (all Anhui required source cells observed/unfilled if confirmed);
- purchased-city cross-check status;
- explicit statement `capital_stock_is_model_derived = true`;
- explicit statement `official_published_capital_stock = false`.

The receipt is data/method evidence, not production authority until Reviewer acceptance.

## 8. Relationship to the V2 annual contract

Do not modify the already accepted temporal contract:

`CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`

Do not change:

- 2018 level row 19;
- analysis/data_MAT index 10;
- PLM vintage19;
- rolling 2009–2018 PLM window;
- same-year Zt formula;
- 2018 resident population `6076` identity now supported by the revised official 2023 population yearbook;
- current GDP status (still unresolved revised identity).

This task closes only the capital/PIM branch.

## 9. Scientific call budget

All scientific/model calls are ZERO:

- MATLAB process/model = 0;
- household/HJB/KFE = 0;
- roots/direct/iterative/eigen = 0;
- firm/one-turn/controller = 0;
- stationary/GE/annual model = 0;
- IRF/dynamics/Results = 0.

Allowed: protected-source reads, spreadsheet/CSV reads, hashes, static PIM arithmetic, descriptive purchased-data cross-checks, serialization, tests, manifest/readback.

## 10. Protected files and no-overwrite

Do not modify:

- original/raw/filled Excel workbooks;
- purchased datasets under `D:\BaiduNetdiskDownload`;
- PLM workbook;
- MAT caches;
- protected MATLAB source;
- production model code;
- GovInv/alpha/rates/grid/boundary law/solver/tolerances.

Purchased/private data remain read-only and must not be committed in reconstructable form.

## 11. Required outputs

At minimum:

- `docs/CH5_MP4C_2018_PIM_CAPITAL_CHAIN_CLOSURE_REPORT.md`;
- recurrence ledger (machine-readable, narrow Anhui-only values permitted);
- PIM capital-input receipt JSON;
- source/provenance summary;
- optional directional cross-check summary for `sj479`;
- tests;
- call ledger;
- manifest/readback.

External evidence root:

`D:\ProjectTemp\ch5-2018-pim-capital-chain-closure-20260909-001`

Use a fresh suffix if occupied; never overwrite prior evidence.

## 12. Decision logic

Use one primary verdict:

- `PIM_CAPITAL_CHAIN_CLOSED__EXISTING_2018_CAP_REPRODUCED`;
- `PIM_SOURCE_REPRODUCTION_MISMATCH`;
- `PIM_CAPITAL_CHAIN_PARTIAL__SOURCE_IDENTITY_GAP`.

Separately report:

- recurrence reproduction status;
- source lineage status;
- 2011 comparability caveat status;
- purchased-data cross-check status;
- derived 2018 capital value;
- V2 transformed CAP value if applicable;
- scientific calls = 0;
- Results eligibility = FALSE.

A PASS closes the capital/PIM data-method blocker only. It does not close the still-open revised 2018 GDP identity and does not authorize a 2018 model run by Builder.

Commit and non-force push a dedicated branch. Do not merge main. Do not start a successor scientific experiment.