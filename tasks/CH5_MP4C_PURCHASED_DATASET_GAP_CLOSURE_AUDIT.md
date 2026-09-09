# CH5 MP4C purchased-dataset gap-closure audit

Date: 2026-09-09. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.

## 1. Objective

Audit the Owner's purchased/high-quality manually curated local datasets under `D:\BaiduNetdiskDownload` as a secondary evidence source for closing the remaining 2018 data-identity gaps and for evaluating whether a higher-quality production/produc­tivity data source exists for future model reconstruction.

This is a **read-only data audit and candidate-source qualification task**. It does not authorize any scientific model run or any production-data overwrite.

The immediate questions are:

1. Can the purchased datasets provide a defensible replacement/cross-check for Anhui 2018 GDP and resident population?
2. Can they provide a complete, internally consistent and better documented Anhui fixed-asset-investment chain for the years needed by `K2018`, namely 2000–2017?
3. Do they contain a productivity/TFP series that is economically and geographically compatible with the current province-level HANK technology input, or at least useful as an independent validation benchmark?
4. What source granularity, statistical concept, units, coverage, missingness, revisions and provenance accompany each candidate file?

A successful task may qualify purchased data as a high-quality **secondary candidate source**, but must not describe it as official National Bureau of Statistics authority unless the dataset itself includes verifiable official provenance.

## 2. Frozen scientific contract

Do not reopen or modify:

- temporal contract `CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`;
- 2018 `steady_year=2018`, `analysis_index=data_mat_index=10`, level row 19;
- PLM estimator and rolling window 2009–2018;
- PLM vintage19 industry4 alpha currently hash-bound to the accepted workbook;
- same-year Zt formula;
- capital recurrence `K0=I0/.1`, `Kt=(1-.096)K(t-1)+I(t-1)`;
- therefore `K2018` uses `I2000..I2017`; `I2018` is not required for the 2018 stock;
- province order and Anhui position;
- model equations, grid, `a_bar`, rates, GovInv rule, solver and tolerances.

Current provisional 2018 Anhui values remain comparison targets only:

- GDP `34010.91` 亿元;
- resident population `6076` 万人;
- workbook-derived CAP `1357314108.2013683`;
- current accepted preliminary official bulletin observations: GDP `30006.82` 亿元 and resident population `6323.6` 万人, both not closed as final revised identities.

## 3. Local source root and protection

Primary local source root:

`D:\BaiduNetdiskDownload`

The Owner states that these datasets were purchased and manually curated and are believed to be of relatively high quality. They are nevertheless private/purchased sources and must be treated as **read-only, no-overwrite, no-upload** under `PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md`.

Do not commit raw purchased files, complete purchased tables, screenshots, proprietary documentation, passwords, license files or material from which the purchased datasets could be reconstructed.

Repository outputs may contain only:

- file names/relative paths;
- hashes;
- schema descriptions;
- narrow extracted observations needed for this scientific audit;
- provenance notes;
- aggregate quality summaries;
- candidate-source classifications.

## 4. Initial high-priority directories

Audit these paths first if present:

1. `D:\BaiduNetdiskDownload\中国各地级市全要素生产率数据（1978-2022年）`
2. `D:\BaiduNetdiskDownload\sj479-地级市-固定资产投资额数据（2000-2024年）`
3. `D:\BaiduNetdiskDownload\NJ73-中国人口与就业统计年鉴1949-2023年`

Also inventory other immediately relevant directories under the root, without recursively ingesting irrelevant large collections. The screenshot provided by Owner also showed examples such as:

- `sj363-298个地级市人口密度1998-2024年无缺失`
- `sj10-分省份按三次产业分从业人员数（就业人员数）1985-2024年数据`
- other city-level panel datasets.

If a better-matching province-level GDP, population, investment or productivity dataset is found elsewhere under `D:\BaiduNetdiskDownload`, include it and explain why it is relevant.

## 5. Phase A — inventory before reading values

Create a file inventory for the relevant candidate directories before using any data values.

For each file record at minimum:

- relative path;
- extension/type;
- size;
- mtime;
- SHA-256;
- sheet/table names when applicable;
- row/column dimensions;
- detected geographic level (`PROVINCE`, `PREFECTURE_CITY`, `COUNTY`, `MIXED`, `UNKNOWN`);
- year coverage;
- candidate variables;
- whether a data dictionary/readme/source note exists;
- whether the source claims manual checking, official provenance, interpolation, deflation, revision, or derived/calculated status.

Do not infer provenance from the commercial folder name alone.

## 6. Phase B — schema/provenance qualification

For every candidate dataset that could close a current gap, determine:

- geographic unit and code/name system;
- year variable and calendar convention;
- monetary unit;
- current/constant price status;
- nominal/real definition;
- whether data are levels, growth rates, indices or ratios;
- whether missing values were filled and by what method if documented;
- whether source notes cite NBS, provincial yearbooks, CEIC, CSMAR, EPS, CNRDS, CNKI, manual collection, interpolation or another origin;
- revision/vintage information;
- whether the dataset supplies original source citations by cell/year/variable or only a generic source note.

Classify source quality separately from official authority:

- `PURCHASED_CURATED_WITH_TRACEABLE_OFFICIAL_PROVENANCE`
- `PURCHASED_CURATED_PROVENANCE_PARTIAL`
- `PURCHASED_CURATED_PROVENANCE_UNDOCUMENTED`
- `DERIVED_RESEARCH_DATASET`
- `NOT_RELEVANT_TO_CURRENT_GAP`

## 7. GDP and population search

Search the relevant purchased files for Anhui 2018 GDP and resident population.

For each candidate observation record:

- source file/sheet/cell or row key;
- raw value;
- unit;
- concept;
- geographic identity;
- year;
- documented original source/provenance;
- comparison with provisional workbook;
- comparison with preliminary official bulletin;
- whether the value appears to be an official revised vintage, an older vintage, an interpolated/derived value, or unresolved.

Do not declare identity closure solely because a purchased value matches either the provisional workbook or the preliminary bulletin.

Use statuses such as:

- `SECONDARY_MATCHES_PROVISIONAL`
- `SECONDARY_MATCHES_PRELIMINARY_OFFICIAL`
- `SECONDARY_SUPPORTS_REVISED_OFFICIAL_VINTAGE`
- `SECONDARY_VALUE_DIFFERS`
- `SECONDARY_PROVENANCE_INSUFFICIENT`
- `NO_RELEVANT_SECONDARY_VALUE`

If the purchased dataset includes a precise official table/yearbook citation sufficient to resolve the previous manual official request, preserve that citation and classify it as a **navigation/traceable provenance lead** for Reviewer/Owner verification.

## 8. Fixed-asset-investment chain

The highest-priority investment candidate is the city-level dataset:

`D:\BaiduNetdiskDownload\sj479-地级市-固定资产投资额数据（2000-2024年）`

Audit its schema carefully before aggregating anything.

Determine:

- whether the investment concept matches the current workbook's `固定资产投资额`;
- whether values are absolute levels or growth rates;
- units and price basis;
- prefecture coverage by year;
- whether province-administered county/city units are included;
- handling of municipalities/direct-administered units;
- missingness and imputation;
- whether Anhui prefecture-city coverage is complete and stable over 2000–2017;
- whether a province total is already supplied by the dataset.

### Aggregation prohibition unless proven

Do **not** automatically sum prefecture values into an Anhui provincial value merely because city observations exist.

City-to-province summation may be calculated only as a **descriptive candidate aggregation** if all of the following are established:

1. the dataset explicitly represents additive absolute investment levels;
2. all relevant Anhui prefecture units for the year are covered exactly once;
3. geographic boundary/coding changes are reconciled;
4. no province-level residual/direct-administered component is omitted;
5. units and statistical scope are consistent;
6. the dataset documentation supports aggregation.

Even then, label results `PURCHASED_CITY_SUM_CANDIDATE`, not official provincial investment.

If any condition fails, report why and do not aggregate.

Produce a 2000–2017 Anhui candidate investment ledger comparing where possible:

- original current workbook value;
- purchased dataset province-level value if directly available;
- purchased city-sum candidate if defensibly computable;
- preliminary/official evidence from the previous audit;
- unit/concept/provenance status;
- 2011 definition-break relevance;
- missingness/completeness.

Do not run the capital recurrence unless a complete candidate chain is defensibly available. If it is available, a static recurrence may be calculated and labeled:

`MODEL_DERIVED_FROM_PURCHASED_CURATED_INVESTMENT_CANDIDATE`

Never label it official capital stock.

## 9. Productivity / TFP dataset audit

Audit:

`D:\BaiduNetdiskDownload\中国各地级市全要素生产率数据（1978-2022年）`

Determine, from documentation and schema:

- estimation method(s) used (e.g. DEA/Malmquist, Solow residual, LP/OP, GMM, index construction, etc.);
- whether TFP is a level, index, growth rate or log;
- base year/normalization;
- nominal/real inputs and deflators;
- geographic coverage and city-code mapping;
- whether multiple TFP variants are included;
- source/provenance for inputs;
- missingness/imputation;
- whether 2009–2018 Anhui cities are sufficiently complete.

Do not replace the current PLM technology estimator in this task.

The purpose is only to decide whether the purchased TFP data are suitable as:

- `INDEPENDENT_PRODUCTIVITY_VALIDATION_BENCHMARK`;
- `POTENTIAL_FUTURE_ALTERNATIVE_PRODUCTIVITY_INPUT_REQUIRES_OWNER_METHOD_DECISION`;
- `NOT_COMPARABLE_WITH_CURRENT_PROVINCE_ZT`.

If province aggregation would be required, do not choose weighting/aggregation methodology without Owner scientific authority. You may list feasible aggregation options and their data requirements, but do not adopt one.

## 10. Population/yearbook candidate audit

Audit `NJ73-中国人口与就业统计年鉴1949-2023年` for a possible traceable 2018 Anhui resident-population series and revision history.

Prefer structured tables and source notes. Do not OCR scanned proprietary pages unless unavoidable; if values are not machine-readable, produce a precise manual-extraction request naming file/table/page.

If the purchased yearbook package contains official yearbook tables or scans, treat the underlying publication as the source authority and the purchased package as a local copy. Preserve publication/table/page metadata and hash of the local file, but do not commit the copyrighted publication.

## 11. Cross-source comparison

For each relevant variable, construct a source matrix comparing:

- current CNKI-derived/provisional workbook;
- accepted preliminary official evidence;
- purchased curated dataset(s);
- directly traceable official source if the purchased dataset identifies one.

Explicitly separate:

- `VALUE_AGREEMENT`;
- `SOURCE_AUTHORITY`;
- `STATISTICAL_CONCEPT_COMPARABILITY`;
- `YEAR/VINTAGE_MATCH`;
- `SUITABILITY_FOR_MODEL_INPUT`.

Agreement between two secondary datasets does not by itself establish official correctness.

## 12. Candidate package rules

No production source may be changed in this task.

If a purchased dataset substantially closes a gap, create a **versioned, no-overwrite candidate evidence package** under the task evidence root containing only the minimal extracted candidate values and provenance needed for later Reviewer adjudication.

Possible candidate package states:

- `SECONDARY_DATA_CLOSES_GAP_WITH_TRACEABLE_OFFICIAL_PROVENANCE`
- `SECONDARY_DATA_PROVIDES_HIGH_QUALITY_CANDIDATE_REQUIRES_OWNER_ACCEPTANCE`
- `SECONDARY_DATA_USEFUL_FOR_CROSSCHECK_ONLY`
- `SECONDARY_DATA_INSUFFICIENT_OR_INCOMPATIBLE`

A later separate task is required before any candidate package becomes production input.

## 13. Scientific-call budget

All scientific/model calls are ZERO:

- MATLAB model = 0;
- household/HJB/KFE = 0;
- root/brentq/direct/iterative/eigen solve = 0;
- firm/one-turn/controller = 0;
- stationary/GE/annual model = 0;
- IRF/dynamics/Results = 0.

Allowed: filesystem inventory, Excel/CSV/Stata/R data reads, metadata extraction, hashes, descriptive statistics, unit conversions, geographic crosswalk checks, static candidate aggregation where specifically allowed above, frozen recurrence arithmetic only if its candidate chain qualifies, static Zt/TFP descriptive comparison, serialization and synthetic tests.

## 14. Required outputs

Create a concise repository report and machine-readable summaries, for example:

- `docs/CH5_MP4C_PURCHASED_DATASET_GAP_CLOSURE_AUDIT_REPORT.md`
- `reports/mp4c_purchased_dataset_gap_closure_20260909/source_inventory.csv`
- `.../candidate_variable_map.csv`
- `.../anhui_2018_gdp_population_secondary_comparison.csv`
- `.../anhui_investment_2000_2017_secondary_comparison.csv`
- `.../productivity_dataset_qualification.json`
- `.../candidate_package_status.json`
- `.../manual_followup_request.csv` when needed
- call ledger, tests, manifest/readback.

Do not commit full purchased datasets or reconstructable large excerpts.

External evidence root:

`D:\ProjectTemp\ch5-purchased-dataset-gap-closure-20260909-001`

Use a fresh suffix if occupied. Never overwrite prior evidence.

## 15. Verdicts

Use one primary verdict:

- `PURCHASED_DATASET_GAP_CLOSURE_PASS__CANDIDATE_SOURCE_IDENTIFIED`
- `PURCHASED_DATASET_PARTIAL_GAP_CLOSURE__OWNER_DECISION_REQUIRED`
- `PURCHASED_DATASET_CROSSCHECK_ONLY__OFFICIAL_GAPS_REMAIN`
- `PURCHASED_DATASET_INCOMPATIBLE_OR_INSUFFICIENT`

Separately report:

- GDP candidate status;
- population candidate status;
- investment-chain candidate status;
- capital candidate status;
- productivity-data qualification;
- source-provenance quality;
- remaining official/manual gaps;
- scientific calls = 0;
- Results eligibility = FALSE.

No successor scientific model run may be started by Builder. Commit and non-force push a dedicated branch; do not merge main.
