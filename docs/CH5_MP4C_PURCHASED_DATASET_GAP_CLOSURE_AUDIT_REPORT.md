# Chapter 5 MP4C purchased-dataset gap-closure audit

Date: 2026-09-09

Repository baseline: `30c09ced38e2467a3c5533b3d197498a5e2918c1`

Task: `tasks/CH5_MP4C_PURCHASED_DATASET_GAP_CLOSURE_AUDIT.md`

External evidence: `D:\ProjectTemp\ch5-purchased-dataset-gap-closure-20260909-001`

## Verdict

`PURCHASED_DATASET_PARTIAL_GAP_CLOSURE__OWNER_DECISION_REQUIRED`

The purchased package supplies a traceable later official-yearbook observation for 2018 Anhui resident population. `中国人口和就业统计年鉴2023`, table `1-1`, `Sheet1!AE22`, reports `6076` 万人 and states that 2011–2019 values were revised using the 2020 Census. This matches the current provisional workbook and explains why the 2018 bulletin's preliminary `6323.6` 万人 and the 2019 yearbook's rounded `6324` 万人 differ. The underlying official publication is the authority; the purchased package is only a local copy. A versioned candidate receipt was created for Reviewer adjudication and was not applied to production data.

No purchased source in the narrow authorized inventory closes revised 2018 GDP or the comparable 2000–2017 provincial investment chain. No city investment sum, capital recurrence, province TFP aggregation, or model computation was performed.

Results eligibility remains `FALSE`.

## Source scope and handling

The audit read the three priority directories plus the two directly named root-level candidates for employment and city population density. Purchased files remained read-only. Repository artifacts contain hashes, schema, aggregate coverage, source notes, and the few observations required for this audit; they do not contain purchased tables, screenshots, archives, or reconstructable extracts.

The 2019 yearbook archive was listed with 7-Zip. Only table `1-1` was temporarily extracted outside the repository for a read-only Excel-COM inspection. Its SHA-256 was recorded and the temporary copy was removed. The original archive and all source files were unchanged.

## GDP and population

| Variable | Current provisional | Preliminary official | Purchased/official-yearbook finding | Status |
| --- | ---: | ---: | --- | --- |
| 2018 Anhui GDP | `34010.91` 亿元 | `30006.82` 亿元 | No relevant GDP candidate was found in the narrow purchased-root inventory | `NO_RELEVANT_SECONDARY_VALUE` |
| 2018 Anhui resident population | `6076` 万人 | `6323.6` 万人 | 2019 yearbook: `6324` 万人 at `AE21`; 2023 yearbook: revised `6076` 万人 at `AE22` | `SECONDARY_SUPPORTS_REVISED_OFFICIAL_VINTAGE` |

The 2023 table uses the same resident-population concept and explicitly documents the census-based revision. It therefore provides more than value agreement. Production promotion still belongs to Reviewer/Owner governance and is outside this task.

The revised 2018 current-price GDP remains unresolved. Agreement between the provisional workbook and any future secondary dataset will not close it without an official revised table and revision note.

## Fixed-asset investment

The `sj479` workbook contains 7,400 valid city-year rows: 296 cities over 2000–2024, with no duplicate city-year keys and no missing investment values. It has no Anhui province-total row. For every year 2000–2017, Anhui has 16 distinct city rows, no duplicate city key, and no missing investment value.

Its documentation says 2000–2016 data come from the *China City Statistical Yearbook*. After 2016, missing levels are estimated from investment growth drawn from provincial/city yearbooks and bulletins. All 16 Anhui 2017 rows contain the growth field, so 2017 cannot be treated as an independently observed provincial chain endpoint.

Only the additive-level condition is established. The package does not establish all of the remaining task gates:

- exact inclusion of every province-administered or residual component;
- reconciliation of geographic boundary and coding changes;
- absence of province-level residuals;
- consistent statistical scope, including the known 2011 definition break;
- documentation authorizing city-to-province aggregation.

The six-condition gate therefore fails closed. No `PURCHASED_CITY_SUM_CANDIDATE` was calculated. The frozen capital recurrence was not run, and capital status is `NOT_COMPUTED__CITY_SUM_GATE_FAILED`.

## Productivity / TFP

The city TFP workbook contains 18,945 valid rows, 416 city labels, 31 provinces, years 1978–2022, and zero duplicate province-city-year keys. It includes eleven variants: OLS, FE, RE, DGMM, SGMM, SFA1, SFA2, SFA3, SFA3D, TFE, and a DEA-Malmquist nonparametric measure.

For Anhui 2009–2018, all ten years contain the same 16 cities. The 160 city-year rows have no missing value in any of the eleven variants.

The method note identifies real GDP as output, perpetual-inventory capital and total employment as inputs, a 9.6% depreciation rate, deflation, and an initial-year base setting. It does not identify the exact deflator series, base year, normalization, per-cell source, or a province aggregation contract. The data are therefore classified `DERIVED_RESEARCH_DATASET` and `NOT_COMPARABLE_WITH_CURRENT_PROVINCE_ZT`. They may support a later city-level validation design, but selecting an employment, GDP, capital, or equal-weight province aggregation requires Owner authority. The frozen PLM estimator was not changed.

## Other narrow candidates

The `sj10` dataset measures employment by industry, not resident population. The `sj363` panel includes city resident population and an explicit interpolated-population field, but has no province total and only generic yearbook/bulletin provenance. Both are `NOT_RELEVANT_TO_CURRENT_GAP` for the present province-level identities. No city population aggregation was performed.

## Candidate and remaining gaps

Candidate package state: `SECONDARY_DATA_CLOSES_GAP_WITH_TRACEABLE_OFFICIAL_PROVENANCE`, limited to the 2018 Anhui resident-population observation and its revision note.

Remaining manual/official work:

1. Obtain the post-fourth-economic-census revised Anhui 2018 current-price GDP table and revision note.
2. Obtain a same-definition official Anhui 2000–2017 annual fixed-asset-investment chain, or an authoritative linkage/backcast across the 2011 definition break.
3. If `sj479` is reconsidered, obtain explicit evidence for province residual/direct-admin coverage, boundary reconciliation, statistical-scope consistency, and aggregation authority.

No production input was modified. No candidate became production authority.

## Verification and call ledger

- Synthetic tests: `7/7` passed; the actual unittest log was retained and parsed.
- Machine-readable outputs include the source inventory, candidate map, GDP/population comparison, investment ledger, cross-source matrix, TFP qualification, candidate status, manual follow-up, call ledger, and manifest/readback.
- MATLAB/model, household/HJB/KFE, root/direct/iterative/eigen, firm/controller, GE/annual/stationary, IRF/dynamics/Results calls: all `0`.
- `scientific_calls = 0`.
- `Results_eligible = FALSE`.
