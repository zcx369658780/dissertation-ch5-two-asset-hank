# CH5 MP4C 2018 revised-GDP closure and canonical data workbook

Date: 2026-09-09. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Close the last remaining 2018 data-identity blocker: the post-fourth-economic-census revised current-price GDP of Anhui for calendar 2018. Then build one versioned `.xlsx` workbook that consolidates the accepted/qualified Chapter 5 annual-data inputs and provenance needed for future work.

This task is data/research/artifact work only. No household, HJB, KFE, firm, GE, annual steady-state, IRF or Results run is authorized.

## 2. Frozen accepted facts

Do not reopen or change:

- temporal contract `CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`;
- 2018: `analysis_index=data_mat_index=10`, level row 19, PLM vintage19, rolling window 2009–2018, same-year Zt;
- 2018 Anhui resident population = `6076` 万人, supported by official *中国人口和就业统计年鉴2023* table 1-1 with 2011–2019 revised using the 2020 Census;
- PIM capital method and source identity: `K0=I0/.1`, `Kt=(1-.096)K(t-1)+I(t-1)`, `K2018=1357314108.2013683`, V2 CAP=`1357314108201.3684`;
- PIM source classification `MODEL_CALIBRATION_SOURCE__CNKI_CURATED_PROVINCE_PANEL` and the documented 2011 investment-definition break;
- PLM estimator/workbook and 2018 industry4 alpha `0.772866243094144`;
- production grids, model equations, rates, GovInv rule, solver/tolerances.

The remaining unresolved GDP comparison is:

- provisional workbook 2018 Anhui GDP = `34010.91` 亿元;
- preliminary 2018 official bulletin GDP = `30006.82` 亿元;
- the exact revised 2018 current-price GDP after the Fourth National Economic Census has not yet been accepted.

## 3. Revised GDP research authority

Owner authorizes public-data research and downloads necessary to close revised 2018 Anhui GDP.

Authority order:

1. National Bureau of Statistics of China official database/yearbook/publication;
2. Anhui Provincial Bureau of Statistics / Anhui Statistical Yearbook / Anhui government official publication;
3. another government statistical publication that explicitly provides the revised historical GDP series and revision vintage.

Search engines, Baidu snippets, CNKI secondary tables, blogs, commercial datasets, papers, Wikipedia/encyclopedia and mirrors may help locate a source but cannot serve as final authority.

Prefer structured official tables, downloadable Excel/CSV, HTML tables, or official yearbook spreadsheets. Avoid OCR unless no structured official source exists. If only a scanned official table can be located, preserve the exact locator and ask Owner for manual extraction rather than inventing a value.

## 4. GDP closure requirements

The accepted revised GDP observation must record at minimum:

- institution;
- publication/database/yearbook name;
- exact table/indicator;
- province = Anhui;
- year = 2018;
- current-price wording;
- revised value;
- unit;
- revision basis/vintage, preferably explicitly linked to the Fourth National Economic Census or later revised historical GDP series;
- publication/retrieval date;
- stable URL/publication identifier;
- downloaded file name and SHA-256 when applicable;
- table/page/cell locator where applicable.

Explicitly compare revised GDP against both `34010.91` and `30006.82` and classify:

- `REVISED_GDP_MATCHES_CURRENT_PROVISIONAL`;
- `REVISED_GDP_REQUIRES_CORRECTION`;
- `REVISED_GDP_OFFICIAL_CONFLICT_NEEDS_OWNER_DECISION`;
- `REVISED_GDP_NOT_OBTAINED`.

Do not choose a value merely because it matches the existing workbook.

## 5. Final 2018 static input arithmetic

Only if revised GDP identity is closed, construct a final 2018 static input receipt using:

- accepted revised GDP;
- population `6076` 万人;
- PIM CAP `1357314108.2013683`;
- frozen multipliers GDP ×1000, POP ×100, CAP ×1000;
- alpha `0.772866243094144`;
- unchanged same-year Zt formula.

Recompute final 2018 `IND_Zt` only as static pre-model arithmetic. Do not run any model.

If revised GDP differs from the provisional workbook, do NOT overwrite the protected original/filled workbooks in this task. Store the accepted revised value in the canonical workbook and a versioned candidate receipt.

## 6. Canonical `.xlsx` workbook required

Create exactly one main future-use workbook outside the protected source directories:

`D:\ProjectTemp\ch5-canonical-data-workbook-20260909-001\CH5_MULTI_PROVINCE_CANONICAL_DATA_V1.xlsx`

If the evidence root is occupied, use a fresh suffix. Do not overwrite an existing workbook.

The workbook is a curated canonical research artifact, not a replacement of the protected raw source files until Reviewer acceptance.

Minimum sheets:

### `README_METADATA`
Document:
- workbook schema/version `CH5_MULTI_PROVINCE_CANONICAL_DATA_V1`;
- creation date;
- repository commit baseline;
- temporal contract version;
- province order contract;
- data-authority/status vocabulary;
- PIM formula and 2011 caveat;
- PLM rolling-window contract;
- source file hashes/identities;
- notes that purchased/raw proprietary source files are not embedded.

### `PROVINCE_ORDER`
31 accepted province labels with MATLAB one-based index, Python zero-based index and source-column mapping where known.

### `ANNUAL_BINDING_2009_2023`
For every supported year include:
`steady_year, analysis_index, data_mat_index, level_row, level_year, plm_vintage, plm_window_start, plm_window_end, zt_year, contract_version`.

### `GDP_2000_2023`
31-province annual GDP matrix from the current protected source, preserving values and source status. For Anhui 2018, include separate columns/fields or notes for:
- original/provisional workbook value;
- preliminary official value;
- accepted revised value when closed;
- final-use status.
Do not silently rewrite history without provenance.

### `POP_2000_2023`
31-province annual population matrix from the current source plus source/status metadata. Anhui 2018 must explicitly record the accepted revised official-history value `6076` and its 2023 yearbook provenance.

### `INVESTMENT_2000_2023`
Current 31-province investment source matrix, clearly classified as model-calibration/CNKI-curated source, with raw/filled status where recoverable and a visible note on the 2011 statistical-definition break. Do not insert purchased city sums.

### `PIM_CAPITAL_2000_2023`
PIM-derived capital matrix generated from the frozen recurrence using the accepted calibration investment matrix. It must distinguish model-derived values from observed statistics. For Anhui, `K2000..K2018` must reproduce the accepted binary64 chain exactly.

If 2022–2023 source problems generate nonpositive/invalid capital for some provinces, do not repair them silently. Preserve the original/source-derived value and add explicit status fields/notes identifying the known negative-capital blocker.

### `PLM_ALPHA_2009_2023`
At minimum industry4 annual alpha/vintage mapping from the current hash-bound PLM workbook, with workbook/sheet identity and source hash. Preserve the known ii15 old-cache mismatch as provenance note; current workbook remains authority.

### `ZT_SAMEYEAR_2009_2023`
Static same-year Zt data derived under the V2 temporal contract where inputs are valid. Include status. For years/provinces where CAP is nonpositive or otherwise invalid, leave derived Zt blank/error-status rather than produce complex/log-invalid values.

### `ANHUI_2018_FINAL_INPUT`
One compact auditable sheet containing:
- GDP raw/current-price revised value and transformed value;
- population raw `6076` and transformed value;
- PIM CAP raw/model-derived value and transformed value;
- alpha;
- final same-year Zt;
- all source statuses and citations;
- calendar/index/row/vintage/window metadata.

If GDP remains unresolved, this sheet must say `GDP_OPEN` and must not label the input final.

### `SOURCE_PROVENANCE`
One row per source/artifact used, with:
`source_id, file/publication, institution, path_or_url, SHA256, source_type, authority_level, variables, year_coverage, geography, revision_vintage, caveat`.

### `DATA_QUALITY_FLAGS`
Machine-readable table of known issues, including at least:
- 2011 investment definition break;
- source CNKI/manual-curation limitation;
- 2022–2023 six negative-capital/complex-log observations;
- stale ii15 cache alpha mismatch;
- old mixed-year 2018 representation deprecated;
- purchased TFP not comparable to current province Zt.

## 7. Workbook quality requirements

The workbook must be readable and durable:

- freeze headers where useful;
- use clear table headers, units and source-status columns;
- sensible column widths, number formats and filters;
- formulas only where they improve auditability; do not hide material derivations;
- do not embed copyrighted yearbook scans or purchased raw tables;
- include plain-text official URLs in provenance cells;
- no external links/formulas that require the source files to remain open;
- avoid macros.

Validate the workbook after creation: reopen/read key sheets, verify 2018 Anhui values, verify PIM recurrence identities, check required sheet names, scan for formula/reference errors if formulas are used, record the `.xlsx` SHA-256 and a compact workbook manifest.

## 8. Repository outputs

Commit only narrow reproducible metadata/report artifacts, not the full private canonical workbook unless its contents are judged safe to publish. By default the `.xlsx` stays in the external evidence root because it contains proprietary/CNKI-derived panel data.

Repository outputs should include:

- `docs/CH5_MP4C_2018_REVISED_GDP_AND_CANONICAL_DATA_WORKBOOK_REPORT.md`;
- `reports/mp4c_2018_revised_gdp_canonical_workbook_20260909/revised_gdp_receipt.json`;
- `.../canonical_workbook_manifest.json`;
- `.../anhui_2018_final_input_receipt.json` if GDP closes;
- `.../source_provenance_summary.csv`;
- `.../data_quality_flags.csv`;
- tests/call ledger/manifest/readback.

## 9. Scientific call budget

All scientific/model calls = 0:

- MATLAB model = 0;
- household/HJB/KFE = 0;
- root/direct/eigen = 0;
- firm/one-turn/controller = 0;
- stationary/GE/annual model = 0;
- IRF/dynamics/Results = 0.

Allowed: official web research/download, spreadsheet/table reads, hash/provenance checks, static PIM and Zt arithmetic, workbook creation/validation, serialization, synthetic tests.

## 10. Verdicts

Primary verdict must be one of:

- `REVISED_2018_GDP_CLOSED__CANONICAL_WORKBOOK_BUILT`;
- `REVISED_2018_GDP_CORRECTION_REQUIRED__CANONICAL_WORKBOOK_BUILT`;
- `REVISED_2018_GDP_CONFLICT__OWNER_DECISION_REQUIRED`;
- `REVISED_2018_GDP_NOT_OBTAINED__CANONICAL_WORKBOOK_PROVISIONAL_ONLY`.

Separately report:
- GDP identity status;
- canonical workbook path and SHA-256;
- workbook validation status;
- final/provisional 2018 input status;
- population/PIM carry-forward status;
- scientific calls = 0;
- Results eligibility = FALSE.

Do not merge main and do not start the 2018 scientific steady-state run. Push a dedicated non-force branch and return the exact commit/SHA and workbook path.