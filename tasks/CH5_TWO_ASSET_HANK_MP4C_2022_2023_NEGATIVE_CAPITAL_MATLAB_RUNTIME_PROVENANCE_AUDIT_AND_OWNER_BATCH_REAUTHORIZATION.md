# CH5_TWO_ASSET_HANK_MP4C_2022_2023_NEGATIVE_CAPITAL_MATLAB_RUNTIME_PROVENANCE_AUDIT_AND_OWNER_BATCH_REAUTHORIZATION

Date: 2026-09-02

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Builder: Codex bounded Builder / MATLAB-runtime provenance auditor

Owner: final scientific authority and manual batch executor

## 1. Trigger and current blocker

The previous Owner-run full-batch workflow was authorized by:

`fa662a97feadd371556bb7f482c7d314c781df97`

The Owner launched the generated PowerShell workflow, but execution stopped **before any scientific annual worker started** during canonical preflight.

Observed primary-workbook blocker reported by Codex:

- calendar 2022: Shanghai `CAP = -1124219643.8727567`;
- calendar 2023: Jilin, Shanghai, Jiangxi, Hunan and Xinjiang have `CAP < 0`;
- current `annual.py` computes `log(cap / pop)` and therefore fails closed on non-finite `log_pcap`;
- only 2009–2021 canonical artifacts were materialized in the failed output root;
- scientific annual worker starts: `0`;
- Python stationary / household / HJB / KFE scientific calls: `0`;
- MATLAB scientific calls: `0`.

Accepted blocker marker:

`MP4C_FULL_2009_2023_OWNER_BATCH_BLOCKED_PRE_SCIENCE__PRIMARY_SOURCE_2022_2023_NEGATIVE_CAPITAL__SCIENTIFIC_CALLS_0`

The Owner explicitly requests: **inspect the actual MATLAB source/runtime records first, then reauthorize a corrected retry if the MATLAB evidence identifies one unique source-faithful treatment.**

This task supersedes the previous Phase-A READY receipt for launch purposes. Do not rerun the old command until this task reaches a new READY marker.

## 2. Scientific principle

Do NOT repair the data by convenience.

Forbidden without source evidence:

- `abs(CAP)`;
- clipping negative CAP to zero or epsilon;
- interpolation / extrapolation / manual replacement;
- silently switching to the unfilled workbook;
- dropping 2022 or 2023;
- changing `log_pcap` formula merely to make it finite;
- changing calendar binding;
- changing model equations, calibration, grid, HJB/KFE numerics, controller semantics or convergence criteria.

The purpose is to determine what the **protected MATLAB implementation actually read and successfully used** for 2022–2023.

The protected MATLAB source/runtime route is evidence authority for reconstruction. A derived cache may be admitted only as an explicitly labeled **MATLAB runtime representation** if protected source plus local records prove that MATLAB actually selects/consumes it. This does not automatically promote that cache to primary scientific/raw-data authority.

## 3. Required live continuity and preservation of local Phase-A work

At start:

1. fresh-fetch `origin/main`;
2. require this exact task live on `main` as direct child of `fa662a97feadd371556bb7f482c7d314c781df97`;
3. require `HEAD == origin/main`, ahead/behind `0/0`;
4. inspect tracked and untracked worktree state before touching anything;
5. the previous Phase-A implementation was intentionally left uncommitted, so **do not require an empty worktree**;
6. locate the previous `batch_runner_build_receipt.json` and verify every existing uncommitted implementation file against that receipt before modification;
7. preserve the failed pre-science batch output root read-only; do not delete, overwrite or reuse it;
8. record its available canonical artifacts and the fact that annual workers/scientific calls were zero.

If there are unexplained local edits not covered by the prior build receipt, stop before remediation.

## 4. Mandatory sources to read

Read completely before deciding any remediation:

Repository governance/evidence:

- `AGENTS.md`;
- all CURRENT project rules named by `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
- formal corrected-2009 stationary parity acceptance report;
- MP4C multiyear annual scope-freeze report;
- MP4C MATLAB active-data-source/local-copy staging report;
- Chunk 01 report;
- the superseded Chunk 02 task;
- the full-batch owner-run task at `fa662a97...`;
- current annual input API and current local uncommitted production/batch scripts.

Protected MATLAB source under the accepted C/D Junction identity:

- `main.m`;
- `main2.m`;
- `multi_prov_HANK_12sts.m`;
- `load_GDPdata.m`;
- `mpHANK_equilibrium_2000.m`;
- `HANK_mp_1eq.m`;
- `HANK_mp_1turn.m`;
- `HANK_2ASSETS_HJB.m`;
- any helper called by `load_GDPdata.m` for fill/cache/regression logic;
- persistence writers/readers for `数据估计结果_1000_100_0.mat`, annual `Multi_Province_12sts_<year>.mat`, `12年稳态值.xlsx`, `12年稳态Ltmat.xlsx` or their actual current equivalents.

## 5. Read-only MATLAB data/runtime provenance audit

No MATLAB process is authorized in this task.

Inspect read-only the protected/local artifacts actually present, including where available:

1. active filled workbook `2000年后各省数据_填充NA.xlsx`;
2. fallback/unfilled workbook `2000年后各省数据.xlsx`;
3. regression workbook `R语言估计结果_plm估计.xlsx`;
4. fixed MAT cache `数据估计结果_1000_100_0.mat`, expected SHA-256 `923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A`;
5. any existing annual steady-state MAT files for 2009–2023 anywhere under the protected project tree or prior accepted diagnostic/run roots;
6. any existing steady-state summary workbooks;
7. existing logs/manifests that can prove which input representation MATLAB consumed in a successful annual run.

Do not modify any of these artifacts.

### 5.1 Exact source route questions

Answer from source lines, not inference:

- Under what exact condition does `load_GDPdata.m` load `数据估计结果_1000_100_0.mat` instead of rebuilding `mydata2` from workbooks?
- If that MAT cache exists, is it the normal current protected MATLAB runtime path?
- Does `multi_prov_HANK_12sts.m` reuse existing `Multi_Province_12sts_<year>.mat` before calling `load_GDPdata`?
- Which `mydata2/data_MAT` fields are consumed by `mpHANK_equilibrium_2000` for `CAP`, `GDP`, `POP`, `IND_alpha`, `IND_Zt`, `GovInv`, etc.?
- Is any transform such as abs/clipping/fill applied to negative CAP after workbook read and before `data_MAT`/`Kt0` use?
- Is `log(CAP/POP)` actually evaluated on the protected MATLAB path for the problematic years, and at what stage?

### 5.2 Exact 2022–2023 value census

For all 31 provinces and both years, extract and compare read-only:

- active filled-workbook CAP;
- fallback/unfilled-workbook CAP, if available;
- MAT-cache `data_MAT/mydata2` CAP corresponding to the accepted decoupled calendar mapping, if structurally identifiable;
- existing annual steady-state `Kt0/Kt/GovInv` or equivalent initial/final capital evidence if available.

Persist a table with province, year, value, source artifact, source field/index and sign/finiteness.

Also compare 2009–2021 at least sufficiently to determine whether cache vs canonical differences are isolated to known representation differences or are materially broader.

### 5.3 Cache lineage and calendar identity

The fixed MAT cache is derived and its authority was previously unresolved. This task must explicitly audit:

- `mydata2` structure/schema;
- number of annual entries;
- internal year/index convention;
- province order;
- whether exact fields can be mapped to 2009–2023 without using the legacy `ii+2008` naming error as proof;
- whether the cache bytes can be causally tied to the protected `load_GDPdata.m` route;
- whether existing annual steady-state outputs/logs independently corroborate the cache values for 2022/2023.

Do not assume that `data_MAT{14}` means 2022 until the accepted decoupled mapping is explicitly established from source/data evidence.

## 6. Pre-frozen classifications

After the read-only audit, choose the strongest supported classification only:

### A — protected MATLAB runtime cache resolves the blocker

Use only if all are proven:

- protected MATLAB source normally selects the fixed MAT cache when present;
- 2022/2023 cache annual identity is unambiguous under the accepted decoupled calendar contract;
- cache CAP used by MATLAB is finite and economically admissible for all 31 provinces;
- existing MATLAB outputs/logs or source-route evidence corroborate this representation;
- no arbitrary imputation is introduced.

Classification:

`MP4C_2022_2023_NEGATIVE_WORKBOOK_CAPITAL_RESOLVED_BY_PROTECTED_MATLAB_RUNTIME_CACHE_PROVENANCE`

### B — MATLAB applies a specific source transform before use

Use only if protected source literally proves a deterministic transform/fill step that Python omitted and that transform uniquely resolves the negative values.

Classification:

`MP4C_2022_2023_NEGATIVE_CAPITAL_RESOLVED_BY_MISSING_SOURCE_TRANSFORM_IN_PYTHON_BINDING`

### C — protected MATLAB annual outputs establish a different exact admissible input representation

Use only if a saved annual `st/data_MAT` or equivalent successful MATLAB output has exact provenance and unambiguous calendar identity, but cache/source route needs a narrower runtime overlay.

Classification:

`MP4C_2022_2023_NEGATIVE_CAPITAL_RESOLVED_BY_PROVEN_MATLAB_ANNUAL_RUNTIME_REPRESENTATION`

### D — raw/fill data itself is invalid for the claimed years and no unique MATLAB treatment is proven

Classification:

`MP4C_2022_2023_NEGATIVE_CAPITAL_PROVENANCE_UNRESOLVED__OWNER_DATA_DECISION_REQUIRED`

In D, do not patch and do not reauthorize the batch.

### E — MATLAB itself would fail on the same current artifacts

Use if protected source plus identical current artifacts imply MATLAB would encounter the same non-finite/negative-capital blocker and there is no saved successful runtime representation proving otherwise.

Classification:

`MP4C_2022_2023_CURRENT_PRIMARY_ARTIFACTS_INCOMPATIBLE_WITH_PROTECTED_MATLAB_STEADY_STATE_ROUTE`

In E, stop for Owner data/provenance decision.

## 7. Conditional remediation authority — only for A/B/C

If and only if classification A, B or C is proven, Codex may repair the local uncommitted Phase-A runner with the **smallest explicit source-faithful binding change**.

### 7.1 Preferred representation contract

Do not overwrite `PRIMARY_SOURCE_CANONICAL` semantics.

Introduce a clearly named runtime representation layer only if needed, e.g.:

`MATLAB_PROTECTED_RUNTIME_ANNUAL_INPUT`

or a narrower field overlay such as:

`MATLAB_RUNTIME_CACHE_CAPITAL_OVERLAY`

The implementation must:

- keep raw workbook values visible in provenance;
- state exactly which fields are replaced and why;
- preserve all non-replaced canonical fields bitwise where applicable;
- bind replacement values to artifact SHA, year, province and field;
- prohibit fallback or fuzzy matching;
- fail closed if cache/output identity changes;
- never silently convert negative values.

If the protected MATLAB route proves that the whole `data_MAT/mydata2` object, rather than only CAP, is the actual runtime representation, do not invent a CAP-only overlay merely for convenience. Reproduce the smallest semantically correct protected runtime object.

### 7.2 15-year canonical/runtime preflight must be fixed

The previous READY had a test gap. The repaired build must, with **zero scientific calls**, materialize/validate all 15 annual input representations 2009–2023 before issuing READY.

For each year require:

- exact decoupled calendar identity;
- exact province order;
- exact source/runtime artifact hashes;
- all scientific entry arrays required by the annual solver finite;
- positive/admissible CAP/Kt0 where required by the model;
- finite log-derived objects where source route requires them;
- no annual worker launch.

No future READY may be based only on reconstructing 2009.

### 7.3 Regression protection

For 2009, verify the repaired input path preserves the previously accepted compatibility baseline or document the exact runtime-representation distinction.

For 2010/2011, compare the repaired premodel input representation against the previously executed canonical route and identify every changed field before allowing the full owner rerun.

No scientific rerun is authorized for Codex.

## 8. Phase-A remediation tests — ZERO SCIENCE

Run only static/serialization/data-binding tests.

At minimum test:

- source-route parser/contract for cache selection;
- full 2009–2023 input materialization under the new runtime contract;
- exact 15-year calendar/index mapping;
- exact 31-province order;
- 2022/2023 problematic province capital values are source-backed and admissible under the selected runtime representation;
- all 15 years have finite required scientific entry arrays;
- raw workbook negative values remain recorded, not hidden;
- replacement/overlay field set is exact and bounded;
- wrong cache SHA fails closed;
- wrong province/year mapping fails closed;
- missing cache/output fails closed when that representation is required;
- terminal-only logging remains no-per-turn;
- restart checkpoint schema unchanged unless source persistence audit requires a documented addition;
- scheduler still covers exactly 2009–2023;
- worker default/cap and BLAS single-thread environment unchanged;
- resume semantics unchanged;
- PowerShell static syntax passes;
- scientific model calls remain `0`.

## 9. New build receipt and Owner retry authority

For classification A/B/C only, create a fresh no-overwrite remediation root, preferred:

`D:\ProjectTemp\ch5-mp4c-negative-capital-matlab-provenance-remediation-20260902-001`

Persist at minimum:

- `negative_capital_source_census.csv`;
- `matlab_runtime_data_route.json`;
- `cache_calendar_province_field_map.json` if applicable;
- `matlab_runtime_vs_workbook_2009_2023_diff.json`;
- `all_year_input_preflight.json`;
- `zero_science_test_receipt.json`;
- `batch_runner_build_receipt_v2.json`;
- `owner_retry_instructions.txt`;
- `remediation_manifest.json`.

`batch_runner_build_receipt_v2.json` must hash every local uncommitted implementation file the Owner will use.

Do NOT commit or push the implementation yet.

Do NOT run any annual worker.

If A/B/C passes, final Phase-A marker:

`MP4C_FULL_2009_2023_OWNER_BATCH_REAUTHORIZED_AFTER_MATLAB_RUNTIME_PROVENANCE_AUDIT__READY_FOR_OWNER_RETRY__SCIENTIFIC_CALLS_0`

Then print the exact new PowerShell command and output-root policy for the Owner.

The new retry MUST use a fresh output root. Do not reuse the failed pre-science root.

## 10. Retry scientific budget belongs to Owner manual execution only

After the new READY marker, the Owner may manually run one full 2009–2023 production batch using the new receipt-bound scripts.

The Owner retry is a new coherent batch and may freshly execute all 15 years including 2009–2011.

Codex automatic scientific execution remains forbidden.

Per year frozen ceilings remain:

- outer turns max `250`;
- household calls max `7750`;
- automatic reruns `0`;
- year-level parallelism only;
- default workers `4` unless Owner explicitly chooses otherwise;
- BLAS/OpenMP threads `1` per worker;
- no default wall-clock kill.

## 11. Post-run Phase B

After the Owner later reports that the fresh retry has completed and identifies its output root, Codex may resume the previous Phase-B closeout under this task plus the prior full-batch task:

- verify implementation hashes against `batch_runner_build_receipt_v2.json`;
- audit all 15 years read-only;
- no stationary rerun;
- optional separately bounded 2009 comparator-only check if all eligibility conditions remain satisfied;
- generate final report;
- commit/push scripts, tests, provenance contract and report only;
- never commit generated MAT/NPZ/XLSX/CSV batch outputs or local primary/cache data.

## 12. Required repository report

Before final GitHub closeout after Owner retry, create:

`docs/CH5_TWO_ASSET_HANK_MP4C_2022_2023_NEGATIVE_CAPITAL_MATLAB_RUNTIME_PROVENANCE_AUDIT_AND_OWNER_BATCH_REAUTHORIZATION_REPORT.md`

The report must distinguish:

- raw primary workbook evidence;
- fallback workbook evidence;
- derived MAT-cache evidence;
- saved MATLAB runtime/output evidence;
- protected source-route evidence;
- accepted runtime representation;
- Python binding remediation;
- scientific execution evidence.

Do not call derived cache “primary scientific data” unless a later Owner decision explicitly promotes it.

## 13. Hard prohibitions

Throughout this task:

- no MATLAB execution;
- no Codex Python stationary/HJB/KFE/household execution;
- no arbitrary data repair;
- no source workbook modification;
- no cache modification;
- no protected MATLAB modification;
- no threshold/calibration/grid/controller changes;
- no shock/AR1/transition/IRF execution;
- no Results claims.

If the audit ends in D or E, stop and report the exact evidence. Do not fabricate a READY marker.
