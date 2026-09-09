# CH5 MP4C temporal-contract minimal implementation

Date: 2026-09-09. Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
Issuer: ChatGPT Reviewer under Owner standing authorization.
Publication baseline: `492dc4cdbd1e8617775382fb93e6ad6da55dd5ae`.

Builder default: `gpt-5.6-sol / medium`. Do not alter provider/global settings; do not claim the runtime model label is verified unless the host exposes it.

## 1. Scientific authority frozen before implementation

Owner has made the substantive scientific decisions required for this task.

The annual temporal contract is now:

- `steady_year = 2008 + ii`, `ii=1..15` for 2009..2023;
- workbook level data are calendar 2000..2023 and the MATLAB-style one-based level row is `level_row = ii + 9`;
- the PLM estimator is preserved;
- PLM uses a rolling 10-year window ending at the steady-state year: `steady_year-9 : steady_year`;
- therefore 2009 uses 2000–2009, 2018 uses 2009–2018, 2023 uses 2014–2023;
- existing PLM workbook fixed-ten-period/vintage structure is consistent with this contract and MUST NOT be rebuilt into an expanding-from-2000 estimator;
- fixed use of calendar-2020 levels in `Zt` has no identified economic/base-year/normalization authority and is accepted only as `LIKELY_LEGACY_FIXED_YEAR_ANCHOR`;
- corrected `Zt` candidate uses the unchanged formula and the same steady-year level row as GDP/CAP/POP;
- old unversioned caches are derived evidence, not primary authority, and may not be silently reused after the contract changes.

Do not reopen these choices in this task.

## 2. Objective

Implement the corrected temporal contract in the repository's Python annual-input/pre-model layer, with explicit provenance/version metadata and rejection of stale/incompatible annual cache metadata.

Produce corrected **pre-model input artifacts only** for calendar 2009 and 2018 using the currently audited source workbooks and source hashes. These artifacts are for input identity verification; they are NOT authorization to run the economic model and are NOT Results.

Also produce a read-only MATLAB patch specification showing the minimal source changes that would implement the same contract in the protected original MATLAB route. Do NOT edit the protected MATLAB source itself.

## 3. No scientific model execution

All scientific/model calls are ZERO:

- MATLAB process/model = 0;
- household/HJB/KFE = 0;
- labor/root/brentq/direct/iterative/eigen solve = 0;
- firm/one-turn/controller = 0;
- stationary/GE/annual steady-state loop = 0;
- IRF/dynamics/Results = 0.

Allowed: source/workbook reads, hashes, deterministic input construction, static arithmetic for `Zt`, serialization, validation, synthetic tests, and generation of pre-model JSON/CSV evidence.

The existing annual input loader in `multi_province/annual.py` is an input-preparation layer and may be executed only insofar as it does not import/call household, HJB, KFE, firm, one-turn, fixed-point, or annual solvers.

## 4. Required implementation behavior

### 4.1 Annual index contract

Use one authoritative calendar binding. For every supported year 2009..2023, require:

- `analysis_index = calendar_year - 2008`;
- `output_filename_year = calendar_year`;
- `workbook_data_row_index = calendar_year - 1999` in one-based data-row semantics (2000->1, 2009->10, 2018->19, 2023->24);
- `data_mat_index = analysis_index` for the PLM-vintage/cache slot;
- `regression_vintage_key = calendar_year - 1999`;
- rolling-window start year = `calendar_year - 9`;
- rolling-window end year = `calendar_year`;
- rolling-window length = 10;
- window type = an explicit stable identifier such as `ROLLING_10_YEAR`.

The code must mechanically assert these relations rather than relying on file naming conventions.

### 4.2 Level data

GDP/CAP/POP and derived `log_pgdp/log_pcap` must come from the explicit calendar-year row corresponding to the binding, not from `analysis_index` alone.

For 2018 the corrected source row must resolve to calendar 2018 / one-based data row 19. For 2009 it must resolve to row10/calendar2009.

Do not alter multipliers, capital recurrence, province order, industry index, or other economic transformations.

### 4.3 PLM

Preserve the current PLM estimator and current primary PLM workbook.

For industry 4, the regression sheet must remain tied to `regression_vintage_key`, so 2018 uses vintage19 and 2009 uses vintage10.

Add/assert metadata describing the rolling sample window. This task does NOT re-estimate PLM and does NOT create a new expanding-window coefficient workbook.

Do not silently use an old cached alpha when it conflicts with the current primary PLM workbook. For corrected pre-model construction, the current verified PLM workbook is the direct source authority; old MAT cache values are comparison evidence only.

Record the known ii15/industry4 old-cache/current-workbook alpha mismatch as a stale-cache identity example; do not attempt to resolve it by changing coefficients.

### 4.4 Zt

Remove the Python annual-input contract's assumption that all years use fixed calendar 2020 levels.

For each annual binding, compute `ind_zt` using the unchanged source formula and the same calendar-year GDP/CAP/POP row as the steady-state year, together with that year's PLM alpha.

Required examples:

- 2009: PLM vintage10 + 2009 GDP/CAP/POP;
- 2018: PLM vintage19 + 2018 GDP/CAP/POP;
- 2020: PLM vintage21 + 2020 GDP/CAP/POP, which naturally coincides with the old row21 anchor only for this year.

Do not change the `Zt` formula, `Ztratio`, alpha values, or any model equation.

### 4.5 Versioned temporal metadata / stale-cache rejection

Introduce an explicit temporal-contract version, e.g. `CH5_ANNUAL_TEMPORAL_CONTRACT_V2_ROLLING10Y_SAMEYEAR_ZT`.

Canonical/pre-model payload metadata must contain at least:

- contract version;
- steady/calendar year;
- analysis index;
- workbook data row index and calendar year;
- PLM vintage key;
- PLM window type;
- PLM sample start/end year and length;
- Zt source row/calendar year;
- primary workbook SHA-256 values;
- PLM workbook SHA-256;
- output identity/version.

Any repository path that accepts a serialized/cached annual binding for corrected execution must reject missing, old, internally inconsistent, or source-hash-incompatible temporal metadata. Do not delete or overwrite old cache files.

If the current code has no reusable cache-reader surface for this, implement a narrow validator/contract function rather than inventing a new cache subsystem.

### 4.6 Corrected pre-model evidence for 2009 and 2018

Using the audited current primary sources read-only, construct corrected annual pre-model inputs for 2009 and 2018 only.

Persist compact JSON/CSV summaries proving:

- exact calendar binding;
- source hashes;
- GDP/CAP/POP row/year;
- regression sheet/vintage;
- rolling 10-year sample metadata;
- alpha;
- same-year `Zt` row/year;
- 31-province vectors are finite for 2009 and 2018;
- Anhui position remains MATLAB12 / Python11 / Excel N;
- Anhui 2018 GDP/POP/CAP values correspond to the audited 2018 row, not old 2009 values;
- difference versus the accepted old mixed-year 2018 input is reported descriptively, with no causal/model interpretation.

Do not label these values as officially validated national-statistics values. The prior official-data request remains open.

## 5. Protected MATLAB source

The original project root remains read-only:
`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Do not edit:
- `multi_prov_HANK_12sts.m`;
- `load_GDPdata.m`;
- `mpHANK_equilibrium_2000.m`;
- original Excel/MAT/PLM workbooks.

Instead write a patch-spec document that identifies exact source expressions/lines to change later:

1. annual level row passed into the initializer must be `ii+9` while PLM/cache slot remains `data_MAT{ii}`;
2. `Zt` formula should use `ii+9` calendar-year levels instead of fixed row21;
3. cache/output metadata should include and assert the temporal contract/version/source hashes;
4. old unversioned caches should not be accepted as corrected annual inputs.

This task does not authorize applying that MATLAB patch.

## 6. Scope and allowed repository writes

Production code allowed:
- `src/ch5_two_asset_hank/multi_province/annual.py`
- `src/ch5_two_asset_hank/multi_province/provenance.py`
- `src/ch5_two_asset_hank/multi_province/__init__.py` only if needed to export the new contract/validator; otherwise leave unchanged.

Tests/validation/report allowed:
- `validators/multi_province/temporal_contract_impl/`
- `tests/test_mp4c_temporal_contract_minimal_implementation.py`
- `reports/mp4c_temporal_contract_implementation_20260909/`
- `docs/CH5_MP4C_TEMPORAL_CONTRACT_MINIMAL_IMPLEMENTATION_REPORT.md`
- `docs/CH5_MP4C_TEMPORAL_CONTRACT_MATLAB_PATCH_SPEC.md`

No other production/model/equation files may change.

The exact task file itself is already published on main and must not be edited by Builder.

## 7. Required tests

At minimum test:

1. all 15 years map exactly to 2009..2023;
2. one-based level rows map exactly 10..24;
3. rolling windows map exactly 2000–2009 through 2014–2023, always length10;
4. regression vintage keys map exactly 10..24;
5. 2009/2018/2023 same-year Zt source year equals steady year;
6. 2020 naturally remains row21 without any special-case fixed anchor;
7. 2018 input uses workbook row19/calendar2018 and vintage19;
8. 2018 Anhui position/value lineage matches the accepted audit source cells;
9. canonical payload includes all required temporal/source metadata;
10. missing/old/inconsistent temporal metadata is rejected;
11. wrong source hash is rejected;
12. stale old-cache alpha mismatch is surfaced as provenance evidence and never silently substituted for the workbook value;
13. import-time and test execution call no household/HJB/KFE/firm/one-turn/annual solver/root/eigen path;
14. protected MATLAB/original data identities are unchanged.

Tests must use deterministic source reads or synthetic objects only. No scientific model execution.

## 8. Evidence and manifest

New external evidence root:
`D:\ProjectTemp\ch5-temporal-contract-implementation-20260909-001`
Use a fresh suffix if occupied; no overwrite.

Manifest must hash the task, modified repo code, relevant tests, report, patch spec, primary workbook identities, accepted temporal audit/acceptance, and generated 2009/2018 pre-model summaries. Do not copy original private workbooks into Git.

Record an explicit call ledger proving zero scientific/model calls.

## 9. Acceptance outcomes

Use one of:

- `TEMPORAL_CONTRACT_IMPLEMENTED_STATIC_VALIDATION_PASS`
- `PARTIAL_IMPLEMENTATION_EVIDENCE`
- `BLOCKED_SOURCE_IDENTITY_OR_CONTRACT_MISMATCH`

A PASS means only that the annual **input temporal contract** is implemented and statically validated. It does NOT mean 2018 steady state, household, KFE, GE, corrected annual coverage, or Results pass.

Results eligibility remains `FALSE`.

## 10. Stop condition and successor

Do not start any model run after implementation.

At the end, report:
- changed paths;
- exact contract/version;
- 2009/2018 corrected pre-model binding summary;
- 2018 Anhui corrected input lineage;
- stale-cache rejection behavior;
- MATLAB patch-spec summary;
- tests/manifest/call ledger;
- commit/branch/remote SHA/clean worktree;
- unresolved official-data items.

Commit and non-force push a dedicated branch, suggested:
`codex/ch5-temporal-contract-minimal-implementation-20260909`.

Do not merge main and do not launch the first corrected 2018 scientific experiment. Reviewer will inspect this implementation before authorizing any model execution.
