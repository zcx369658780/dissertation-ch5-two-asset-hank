# CH5 MP4C 2018 raw-data and interpolation audit — Reviewer acceptance

Date: 2026-09-09. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Candidate: `f850937ccb7b11b835ce5e45b9819ee25412ad03`.
Task: `tasks/CH5_MP4C_2018_RAW_DATA_AND_INTERPOLATION_AUDIT.md`.

## Decision

Accept classifications `MATERIAL_DATA_QUALITY_OR_LINEAGE_ISSUE_FOUND` and `PARTIAL_EVIDENCE_NEEDS_OFFICIAL_DATA`.
Reviewer marker: `RAW_DATA_LINEAGE_AUDIT_ACCEPTED__YEAR_INDEX_MISALIGNMENT_AND_MIXED_VINTAGE_BLOCK_PRODUCTION`.

This is now a higher-priority blocker than the recent b-domain stress diagnostics. No change to production data, loader, alpha, GovInv, grid, equations or solver is authorized by this acceptance. Results eligibility remains FALSE.

## Accepted material findings

1. The annual label/year contract is inconsistent. `multi_prov_HANK_12sts(ii,pp)` names an annual file with `ii+2008`, but passes `mydata2{ii}` / `data_year=ii`; because workbook row 1 corresponds to calendar 2000, `ii=10` selects calendar 2009 while the file/runtime is labelled 2018.
2. For the saved 2018-labelled path, cache vectors and source lineage support that Anhui actually consumes the 2009 level row. Anhui is MATLAB province 12 / Python zero-based 11 / Excel column N. Accepted examples: GDP 10864.68亿元, resident population 6131万人, derived capital stock 228121755.48548827 before the final loader scaling.
3. The same labelled state mixes time concepts: regression vintage 19 supplies the common alpha, while Zt is constructed using fixed row 21 / calendar 2020 levels. Therefore the saved 2018-labelled state is not a coherent 2018 data vintage.
4. The filled workbook is an active persisted input. In the total-path variables, resident population has 3 endpoint-filled cells; total fixed-asset investment has 129 filled cells, of which 128 are endpoint/extrapolation-risk cells and one is an interior fill. Wider sectoral sheets contain additional long missing runs and endpoint fills.
5. The derived capital recurrence produces six negative 2022–2023 provincial capital cells, which make `log_pcap` complex. These later years do not directly explain the saved call725 2009-row input, but they independently prove that the current fill/recurrence pipeline can generate economically invalid derived states.
6. The 2024 source workbook comparison found 8,509 explicitly comparable numeric cells with zero differences; unmapped fields were correctly left `NOT_COMPARABLE` rather than force-merged.
7. Ten official-data/manual-verification requests are preserved. P0 priority is Anhui 2018 GDP, resident population, the 2000–2018 fixed-investment/capital-stock chain, and the alpha/Zt time-vintage contract. The six negative-capital province-years are P1 follow-up items.

## Budget and evidence level

All scientific/model calls were zero: MATLAB model, Python HJB/KFE/household, firm/controller/GE/annual/IRF/Results, and root/direct/iterative/eigen model solves.

Published synthetic tests: 6/6. Builder manifest/readback reports 32 files matched, manifest SHA-256 `A64F9B6B9CD244AA481F41BAD27C9A95BEF8A00C6CF3003781078552B8B5EDC3`. External cell ledger contains 10,416 records under `D:\ProjectTemp\ch5-2018-raw-data-audit-20260909-007`.

Reviewer performed repository/diff/report/contract and selected machine-readable evidence review. Reviewer did not independently reread every external workbook cell or recompute the entire 10,416-row ledger.

## Route consequence

Do not continue bmax expansion and do not tune alpha/GovInv convergence speed yet. First repair or explicitly redefine the annual data-year/vintage contract using Owner-approved semantics and, where needed, official data. Only after that contract is frozen should convergence adaptation be re-evaluated on a small controlled 2018 case.

No successor model-execution task is activated by this acceptance. Results eligibility=FALSE.
