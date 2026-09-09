# CH5 MP4C 2018 raw-data and interpolation audit

Date: 2026-09-09. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer. Owner has redirected the route away from further `bmax` expansion: historically, converged steady states had `Bt` near zero, and the production asset-grid design should retain `amax > bmax`. The accepted `bmax=12` experiment remains a stress diagnostic only.

Execution preference: `gpt-5.6-sol / medium`. Do not alter provider/global settings and do not claim the host label was verified unless exposed.

## 1. Objective

Perform a read-only, zero-model-call audit of the original provincial data, missing-value/interpolation chain, year/province mapping, units/scaling, and the exact lineage of the data consumed by the 2018 Anhui model state.

Primary question: could incomplete, imputed, misaligned, mis-scaled, or otherwise abnormal source data be materially contributing to the 2018 Anhui/high-return/household-failure path?

This task succeeds by producing an auditable lineage and anomaly classification. It does NOT need to find a data defect.

## 2. Hard boundaries

Scientific/model calls are all ZERO:
- MATLAB model calls = 0;
- Python HJB/KFE/household/firm/one-turn/controller = 0;
- GE/stationary/annual/IRF/Results = 0;
- root/direct/iterative/eigen solves = 0.

Allowed work: filesystem/source reads, hashes, workbook/MAT decoding, tables, descriptive statistics, formula/value inspection, comparisons, and synthetic-only tests.

Do NOT modify any original workbook, MAT cache, protected MATLAB source, production Python loader, model parameter, `bmax`, `amax`, `a_bar`, `ramax`, convergence rule, `alpha`, `GovInv`, equation, boundary law, or solver.

Do NOT run multiple provinces as a model. Panel-wide DATA checks are allowed because they are static reads, not scientific model execution.

## 3. Required source files and path protection

Resolve and hash these read-only candidates under the protected MATLAB project root:

1. `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\2000年后各省数据.xlsx`
2. `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\2024年数据原始版.xlsx`
3. `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\2000年后各省数据_填充NA.xlsx` if present.
4. `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\数据估计结果_1000_100_0.mat` if present.
5. Relevant protected source readers, especially `load_GDPdata.m`, `mpHANK_equilibrium_2000.m`, `multi_prov_HANK_12sts.m`, and any helper they actually call for these inputs.

The original files are READ ONLY. Verify the resolved physical path and record file size, mtime, SHA-256, workbook sheet names/dimensions, and MAT top-level variables where readable.

Repository work directory: `D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001`.
New no-overwrite evidence root: `D:\ProjectTemp\ch5-2018-raw-data-audit-20260909-001`; if occupied use a fresh suffix.

## 4. Establish the true data contract before auditing values

Statically trace the MATLAB source to enumerate every workbook sheet/range/column and every transformation used to construct the current model data objects. Do not infer the contract from variable names alone.

At minimum establish:
- exact province order and the Anhui position/header;
- exact calendar-year mapping, model index `ii/data_year`, and cache filename convention;
- workbook row/column mapping for each consumed raw variable;
- transformations, multipliers, deflators, logs/ratios, interpolation/fill rules, smoothing, regression-derived fields, and unit changes;
- path from workbook -> loader intermediate -> `mydata2/data_MAT` -> annual/cached state -> 2018 Anhui inputs.

A prior static audit found a possible year-semantics hazard: cache filenames use `ii+2008`, while other indexing begins from an earlier dataset origin. This task must resolve the mapping from actual workbook contents and source, not assume that filename year equals data row year.

## 5. Original-versus-filled data audit

For each model-consumed raw series, compare the original workbook with the filled/interpolated workbook where schemas overlap.

Produce a machine-readable cell-level ledger containing, when available:
- logical variable;
- source workbook/sheet/cell;
- province;
- calendar year;
- original raw value;
- filled value;
- exact equality / changed flag;
- missing-original flag;
- fill/interpolation classification if derivable;
- final transformed/model-consumed value;
- transformation/unit description;
- source confidence and caveat.

Do not silently classify a changed cell as interpolation unless source/formula/evidence supports that mechanism. Use categories such as `OBSERVED_UNCHANGED`, `MISSING_FILLED_INTERIOR`, `ENDPOINT_OR_EXTRAPOLATION_SUSPECT`, `CHANGED_MECHANISM_UNRESOLVED`, `SCHEMA_NOT_COMPARABLE`.

## 6. Focused 2018 Anhui lineage

Create a compact but complete 2018 Anhui lineage table for every field actually used by the annual equilibrium initializer / data structure.

For each field report:
- original value and exact cell;
- filled/interpolated value and exact cell;
- any transformation/scaling;
- cache/intermediate value if readable;
- final value consumed by the 2018 Anhui state;
- observed vs imputed status;
- year/province alignment status;
- anomaly flag and reason.

Important: enumerate actual fields from source. Likely GDP/CAP/POP/industry/productivity/calibration objects are relevant, but do not treat this non-exhaustive list as authority.

## 7. Panel-wide static quality checks

Without running the model, compute descriptive audits over all available province-years for each consumed raw field:
- missingness before/after filling;
- lengths and locations of consecutive missing runs;
- endpoint fills/extrapolations versus interior fills;
- zero/nonpositive values where economically impossible or suspicious;
- duplicate or missing province headers;
- row/year misalignment and schema changes;
- abrupt year-to-year jumps and extreme province cross-sections;
- unit/order-of-magnitude discontinuities;
- ratios that directly enter calibration where source defines them.

Flag anomalies; do not auto-correct or winsorize them. Use robust descriptive thresholds only as discovery aids and label them as such, not as model acceptance thresholds.

## 8. Compare the 2024 raw workbook carefully

Inspect `2024年数据原始版.xlsx` and map its schema to `2000年后各省数据.xlsx` only where a source-backed or header-backed correspondence exists.

Where years/variables overlap, report value differences and units. Where they do not, mark `NOT_COMPARABLE` rather than forcing a merge.

The 2024 workbook is a cross-check/source clue, not automatically the authority for historical 2018 observations.

## 9. Cache / derived-object audit

If `数据估计结果_1000_100_0.mat` is readable without MATLAB execution, inspect it read-only. Trace whether 2018-related values correspond to the original or filled workbook route and whether cache contents agree with source transformations.

If v7.3/HDF5 or another format is not safely readable in Python, record that gap. Do not launch MATLAB merely to open it in this task.

Distinguish primary raw evidence from derived cache. A cache being internally consistent does not prove the raw source is correct.

## 10. Official-data escalation list

Do not replace data automatically and do not write production workbooks.

If the audit finds missing, imputed, conflicting, suspicious, or unresolvable values that could materially affect the 2018 state or model calibration, generate:
- `official_data_request.csv` and/or `.md`;
- exact variable, province, year, unit, current raw/filled value, why verification is needed;
- suggested authoritative publication/table/source, prioritizing National Bureau of Statistics or official provincial statistical yearbooks.

Internet lookup is optional and must be limited to authoritative metadata/verification. Do not use random aggregators as final authority. If official data cannot be retrieved automatically, provide a precise manual-download list for Owner.

## 11. Classification

Do not preordain a PASS. Report one or more evidence-based labels:
- `MATERIAL_DATA_QUALITY_OR_LINEAGE_ISSUE_FOUND`;
- `PARTIAL_EVIDENCE_NEEDS_OFFICIAL_DATA`;
- `NO_MATERIAL_DATA_ISSUE_FOUND_WITHIN_AUDITED_SCOPE`.

Define “material” by a clear path to a consumed 2018/calibration quantity, not merely by a cosmetic workbook difference.

If a material issue is found, STOP before changing data or running the model. The next step requires Owner selection of corrected official values and a separate task.

If no material issue is found, STOP and report that the next scientific route should audit/modify the OUTER convergence/adaptation algorithm (including the speed of regional `GovInv` adjustment when the relevant return/capital condition is too high), not continue expanding `bmax`.

## 12. Outputs and allowed repo paths

Allowed repository additions/changes for Builder:
- `validators/multi_province/data_audit/**`;
- `tests/test_mp4c_2018_raw_data_audit.py` or closely named related synthetic test(s);
- `reports/mp4c_2018_raw_data_audit_20260909/**` containing text/CSV/JSON summaries only, no private raw workbook copies;
- `docs/CH5_MP4C_2018_RAW_DATA_AND_INTERPOLATION_AUDIT_REPORT.md`.

Do not commit raw/private Excel/MAT files or large extracts sufficient to reconstruct them. Commit only hashes, targeted lineage values required for scientific audit, summaries, and source-cell references.

Synthetic tests should cover year/province mapping helpers, missing/fill classification, unit/lineage bookkeeping, and import-time zero-science behavior. Do not use scientific model calls inside tests.

Final report must include source hashes, exact 2018 Anhui lineage, anomaly table, original-vs-filled summary, cache status, official-data request list if needed, zero-model call ledger, tests, manifest/readback, and a bounded next recommendation.

Task time budget: 90 minutes. No scientific retry budget exists because scientific calls are prohibited.

Publish on a dedicated non-force branch, verify remote SHA and clean worktree, and do not merge main. Do not start any convergence-algorithm experiment in this task.

Results eligibility remains FALSE.
