# CH5 MP4C temporal contract and Zt legacy audit

Date: 2026-09-09. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer.

Owner scientific clarification:
- The intended annual design starts around 2009 because provincial productivity/technology estimation requires a historical window.
- The intended logic is: use 2000–2009 observations to estimate the technology object used for the 2009 steady state; later annual steady states should analogously use information available through that year.
- PLM was tested against alternative methods in `load_GDPdata.m`/related legacy code and was retained because it performed best. This task MUST NOT replace PLM unless a later Owner decision explicitly authorizes that scientific change.
- Owner suspects the fixed use of the 2020 level row in `Zt` construction is legacy code rather than an intentional economic anchor.

Execution preference: `gpt-5.6-sol / medium`. Do not modify provider/global settings; do not claim host model identity unless exposed.

## 1. Objective

Perform a zero-model-call source/design audit that converts the Owner clarification and accepted raw-data audit into an explicit annual temporal contract and a minimal repair specification.

Primary questions:
1. What is the intended mapping among `ii`, steady-state calendar year, workbook level-data row, PLM estimation window/vintage, and cache/output filename?
2. Does the existing PLM workbook naming/indexing already implement the intended expanding-window estimation logic?
3. Is the current fixed `Zt` use of workbook row21/calendar2020 a legacy indexing defect, and what year-consistent row/formula would preserve the original PLM method?
4. What is the smallest source-level repair needed to make 2009, 2018, and the supported annual sequence internally time-consistent without changing the estimation method?

This task is a DESIGN/AUDIT task only. It does not change production source or data and does not run the model.

## 2. Hard zero-science boundary

All scientific/model calls are ZERO:
- MATLAB model calls 0;
- Python HJB/KFE/household/firm/one-turn/controller 0;
- GE/annual/steady-state/IRF/Results 0;
- root/direct/iterative/eigen/model solves 0.

Allowed: static source reads, workbook header/value inspection, cache metadata/value inspection, hashes, symbolic/index arithmetic, tables, source diff proposals, and synthetic-only tests.

Do NOT modify original Excel/MAT/MATLAB files, production Python loaders, cache, parameters, `bmax`, `amax`, `a_bar`, `ramax`, `alpha`, `GovInv`, equations, solver, or convergence rules.

## 3. Required evidence

Read the accepted audit and its report artifacts, especially:
- `docs/CH5_MP4C_2018_RAW_DATA_AND_INTERPOLATION_AUDIT_REPORT.md`
- `reports/mp4c_2018_raw_data_audit_20260909/data_contract.json`
- `reports/mp4c_2018_raw_data_audit_20260909/anhui_2018_lineage.csv`
- `reports/mp4c_2018_raw_data_audit_20260909/cache_audit.json`
- `reports/mp4c_2018_raw_data_audit_20260909/official_data_request.csv`

Read protected source files directly, read-only, including as relevant:
- `load_GDPdata.m`
- `multi_prov_HANK_12sts.m`
- `mpHANK_equilibrium_2000.m`
- any helper that selects `IND_alpha`, `IND_Zt`, `mydata2/data_MAT`, or regression-vintage sheets
- the PLM-result workbook and only those other estimation-method source branches needed to document alternatives.

Do not re-run PLM estimation or any alternative estimator.

## 4. Freeze the intended temporal contract

Test the Owner-consistent hypothesis:

`steady_year = 2008 + ii`

For a workbook whose province-year rows start at calendar 2000, the same-year level-data row index should therefore be:

`level_row_1based_within_data_matrix = steady_year - 1999 = ii + 9`

and the expanding estimation sample for the first steady state should be 2000:2009, with later vintages extending through the corresponding steady year.

Do NOT assume this formula is correct merely because Owner described the design. Verify it against:
- actual regression sheet names/contents;
- code that computes `ii+9` or equivalent vintage keys;
- file naming `ii+2008`;
- workbook row headers/years;
- any available historical comments or alternative estimation branches.

Produce a table for every supported `ii` showing at minimum:
`ii`, output/steady year, intended level year, intended workbook row, PLM vintage/sheet, PLM sample end year if derivable, current actual level row, current Zt anchor row/year, and consistency status.

At minimum explicitly resolve `ii=1` (2009) and `ii=10` (2018).

## 5. PLM method preservation

Document the estimation alternatives present in legacy source, but classify them only as historical alternatives unless currently active.

Required conclusion fields:
- `current_preferred_estimator = PLM` unless source contradicts the Owner statement;
- whether PLM vintage indexing is internally consistent with the intended annual sequence;
- whether any source change to the PLM estimation method is required for temporal repair.

Do not recommend switching estimators merely to solve a convergence problem.

## 6. Zt legacy audit

Trace the exact current formula for `IND_Zt{4}` and determine whether its fixed row21/calendar2020 level anchor is caused by:
- an explicit documented normalization/base-year design;
- a hard-coded row left from later calibration work;
- another source transformation.

Search comments/branches/alternative methods for evidence of intended time-varying Zt construction.

If no documented economic reason supports the fixed 2020 anchor, classify it as `LIKELY_LEGACY_FIXED_YEAR_ANCHOR` rather than silently declaring a proven bug.

Construct, but DO NOT execute, the minimally changed year-consistent formula that would use the steady-year level row while retaining the same PLM alpha and functional form. Show the exact 2009 and 2018 row/index substitutions.

## 7. Minimal repair specification

Produce a source-level patch plan, not a production patch.

The plan must distinguish:
A. confirmed indexing defects;
B. likely legacy Zt anchor requiring Owner acceptance;
C. data values still requiring official validation;
D. unrelated later-year negative-capital data-quality issues.

For each proposed source edit give:
- file/function;
- current expression;
- proposed expression;
- economic meaning preserved;
- expected affected years/objects;
- whether it changes estimator, calibration, or merely year alignment.

Prefer the smallest repair. Do not redesign the annual architecture if an index correction is sufficient.

## 8. No official-data replacement in this task

The accepted audit's official-data requests remain pending. This task may say whether official values are needed before execution, but must not download/replace production values or create a new filled workbook.

For 2018, distinguish:
- year-alignment defect (already evidenced), from
- whether the workbook's 2018 GDP/population/investment values are officially correct (still to be validated by Owner where requested).

## 9. Deliverables

Allowed repository writes only:
- `validators/multi_province/temporal_contract_audit/`
- `tests/test_mp4c_temporal_contract_audit.py`
- `reports/mp4c_temporal_contract_audit_20260909/`
- `docs/CH5_MP4C_TEMPORAL_CONTRACT_AND_ZT_LEGACY_AUDIT_REPORT.md`

External evidence root:
`D:\ProjectTemp\ch5-temporal-contract-audit-20260909-001` or fresh suffix.

Required report outputs:
- explicit accepted/blocked temporal-contract table;
- PLM preservation verdict;
- Zt legacy classification;
- minimal repair specification;
- exact list of unresolved Owner/official-data decisions;
- zero scientific-call ledger;
- relevant synthetic tests and manifest/readback.

Suggested branch:
`codex/ch5-temporal-contract-zt-legacy-audit-20260909`

Do not merge main and do not execute the proposed repair. Do not launch annual/single-household science afterward.

Results eligibility remains FALSE.
