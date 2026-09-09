# Chapter 5 MP4C purchased-dataset gap-closure audit — Reviewer acceptance

Date: 2026-09-09.
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Accepted candidate: `4db5c0691535e92d34a86c67ee96c2b8978c1de2`.

## Verdict

Reviewer marker: `PURCHASED_DATASET_AUDIT_ACCEPTED__2018_POPULATION_IDENTITY_CLOSED__GDP_AND_INVESTMENT_REMAIN_OPEN`.

Accept the candidate verdict `PURCHASED_DATASET_PARTIAL_GAP_CLOSURE__OWNER_DECISION_REQUIRED` and its bounded evidence, with one Reviewer adjudication: the 2018 Anhui resident-population identity is now considered closed at `6076` 万人 because the purchased package contains a local copy of the official `中国人口和就业统计年鉴2023`, table 1-1, and the table explicitly states that 2011–2019 values were revised using the 2020 Population Census. Authority belongs to the official publication, not to the purchased package itself.

## Accepted findings

1. Population: Anhui 2018 resident population `6076` 万人 is supported by the 2023 official population/employment yearbook revision vintage and explains the difference from the preliminary 2018 bulletin value `6323.6` 万人 and the rounded 2019-yearbook value `6324` 万人. For current Chapter 5 data identity, population status is `OFFICIAL_REVISED_IDENTITY_CLOSED__6076_WAN`.
2. GDP: no purchased candidate closes the gap between provisional workbook `34010.91` 亿元 and preliminary official `30006.82` 亿元. Revised post-fourth-economic-census 2018 current-price GDP remains open.
3. Investment: `sj479` has complete Anhui 16-city coverage for 2000–2017 with no duplicate/missing city-year keys, but this does not prove province-total additivity. Province residual/direct-admin coverage, administrative-boundary reconciliation, statistical-scope consistency, and aggregation authority remain unproven; 2017 values are growth-derived. No city sum or capital recurrence was correctly performed.
4. Capital: no purchased-data candidate capital stock is accepted. Current CAP remains workbook-derived provisional input.
5. TFP: the purchased city TFP package is a well-covered derived research dataset for Anhui 2009–2018 (16 cities × 10 years × 11 methods, no missing), but its normalization, exact deflators and province-aggregation contract are insufficient to replace current province-level PLM/Zt. Accept `NOT_COMPARABLE_WITH_CURRENT_PROVINCE_ZT` for production use; it may be used later as an independent validation benchmark only under a separate task.
6. Scientific/model calls were all zero. No production data, PLM estimator, temporal contract, model equation, grid, solver, MATLAB source or cache was modified.

## Remaining decisions / blockers

The remaining 2018 data blocker is now narrowed to:
- revised official Anhui 2018 current-price GDP;
- a defensible province-level 2000–2017 fixed-asset-investment chain, or an Owner-approved alternative capital-stock reconstruction methodology if no comparable official chain exists.

No new 2018 household/HJB/KFE/firm/GE/annual run is authorized yet.

Results eligibility = FALSE.
