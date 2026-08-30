# Chapter 5 Two-Asset HANK MP4A2 2009 Decoupled Annual Binding Report

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Live task authority: `10aa389858ba4987eb9ff64e9963bf5f99ecdc2a`

## 1. Terminal

`MP4A2_2009_DECOUPLED_ANNUAL_BINDING_CANONICAL_INPUT_AND_MATLAB_PARITY_WRAPPER_PREPARATION_PASS`

Freeze:

- `MP4A2_DECOUPLED_ANNUAL_INDEX_CONTRACT_ACCEPTED`
- `MP4A2_2009_PRIMARY_SOURCE_CANONICAL_INPUT_ACCEPTED`
- `MP4A2_2009_RUNTIME_REPRESENTATION_COMPATIBILITY_ACCEPTED`
- `MP4A2_MAT_CACHE_COMPATIBILITY_REPRESENTATION_ACCEPTED_FOR_2009_RUNTIME_ONLY`
- `MP4A2_MATLAB_2009_PARITY_WRAPPER_PREPARED_ACCEPTED`
- `MP4A2_PYTHON_2009_PARITY_ENTRY_PREPARED_ACCEPTED`
- `MP4A2_MP4B_SAME_INPUT_STATIONARY_PARITY_EXECUTION_CONTRACT_ACCEPTED`

This is input/preparation acceptance only. No MATLAB or Python scientific/model solver was run, and no stationary result is accepted here.

## 2. Live continuity and protected identities

- Fresh fetch found local `cf9516742afda1c4f9a57075253463a8810301a6` behind live `main` by two commits.
- Fast-forward-only synchronization reached `HEAD == origin/main == 10aa389858ba4987eb9ff64e9963bf5f99ecdc2a` at execution start.
- Accepted MP4A report commit `cf9516742afda1c4f9a57075253463a8810301a6` and Owner/L3 adjudication commit `8ea3f6d26ed1b29a460f8a03d554780be6236271` are in the live history.
- Worktree was clean at execution start.
- Accepted standalone HA oracle remains SHA-256 `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`.
- Accepted MP2 `one_turn.py` remains `D18C4385745E33E917B79994CAA069BE8825C9F22919A5A9EDE918845312D98D`.
- Accepted MP3 `steady_state.py` remains `7065D0FCBFDA6A88C8F773DEBDF277F6E300A8E0195B7CC635F7A0033D74D88C`.
- No import or runtime dependency on the historical one-asset R5 repository was introduced.

Owner/L3 markers preserved:

- `OWNER_ECONOMIC_CALENDAR_YEAR_IS_WORKBOOK_CALENDAR_YEAR`
- `OWNER_2009_ANCHOR_USES_EXPLICIT_WORKBOOK_2009_ROW`
- `MATLAB_LEGACY_ANNUAL_YEAR_INDEX_COUPLING_DEFECT_CONFIRMED`
- `OWNER_DERIVED_MAT_CALIBRATION_CACHE_NOT_PRIMARY_SCIENTIFIC_AUTHORITY`
- `MATLAB_FIXED_2020_IND_ZT_RETAINED_AS_SOURCE_NUMERICAL_INITIALIZATION_ANCHOR`
- `OWNER_PARITY_MISMATCH_BOUNDED_ROOT_CAUSE_DIAGNOSIS_AUTHORIZED`

## 3. Exact decoupled 2009 binding

| Identity | Frozen 2009 value | Role |
|---|---:|---|
| `calendar_year` | 2009 | economic calendar identity |
| workbook physical Excel row | 11 | row 1 is header |
| zero-based data index | 9 | 2000 is index 0 |
| `workbook_data_row_index` / MATLAB numeric row | 10 | economic GDP/CAP/POP/log row |
| `analysis_index` | 1 | first position in 2009--2023 analysis |
| `data_MAT_index` | 1 | calibration object cell |
| `output_filename_year` | 2009 | output label only |
| `regression_vintage_key` | 10 | source sheet suffix, not silently renamed calendar year |
| `fixed_zt_calendar_year` | 2020 | retained numerical initialization anchor, not annual identity |

`DecoupledAnnualIndex` enforces these identities independently. A reconstruction that reuses `analysis_index=1` as workbook row 1 fails closed.

## 4. Primary-source identities and dissertation cross-check

| Artifact | Role | SHA-256 |
|---|---|---|
| `2000年后各省数据_填充NA.xlsx` | active filled annual source | `C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929` |
| `2000年后各省数据.xlsx` | inactive raw fallback evidence | `09814A45D933B2685A35238A15C0C7BB501F00A63597796B3CADCE15C230ECB3` |
| `R语言估计结果_plm估计.xlsx` | primary regression-result input | `A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68` |
| `中国各省省会地理距离矩阵.xlsx` | primary distance/migration source | `26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566` |
| `数据估计结果_1000_100_0.mat` | derived, non-primary runtime representation | `923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A` |

No locally accessible dissertation PDF/TeX/Word source was found under the designated local research/source roots. The accepted Owner/L3 adjudication therefore controls the dissertation intent cross-check: Table 5-2's 2009 actual-GDP column means explicit workbook calendar 2009. The reconstruction independently verifies the workbook `GDP` year cell at physical row 11 before reading province columns C:AG. It does not use dissertation prose to alter any MATLAB formula.

The workbook province columns normalize only their literal `省`/`市` suffixes and exactly match the accepted 31-province order. The distance workbook `geom` row and column axes independently match the same order.

## 5. Field-by-field primary transformation

The production API has no local-path, year, analysis-index, cache, province-order, or scalar defaults. Callers must explicitly provide `PrimaryAnnualSourceFiles`, `DecoupledAnnualIndex`, and all `AnnualSourceScalars`.

| Canonical field | Primary source and formula | Shape/type |
|---|---|---|
| GDP | filled `GDP`, physical row 11, C:AG, times `1000` | `(31,)`, binary64 |
| CAP | filled `总资本存量`, physical row 11, C:AG, times `1000` | `(31,)`, binary64 |
| POP | filled `常住人口`, physical row 11, C:AG, times `100` | `(31,)`, binary64 |
| `log_pgdp` | `log(GDP/POP)` | `(31,)`, binary64 |
| `log_pcap` | `log(CAP/POP)` | `(31,)`, binary64 |
| `IND_alpha` | last numeric coefficient in `总面板回归系数_10_行业4`; value `0.539451671764441` | `(31,)`, repeated binary64 |
| `IND_Zt` | calendar-2020 GDP/CAP/POP with `GDP * CAP^(-alpha) * POP^(alpha-1)` | `(31,)`, binary64 |
| initialized Zt | `IND_Zt * Ztratio`, with explicit `Ztratio=1` | `(31,)` |
| GovInv | calendar-2009 CAP times explicit `GovInv_ratio=1` | `(31,)` |
| inter-province asset ratio | `0.3*(pcap-min)/(max-min)` | `(31,)` |
| distance | `geom` B2:AF32, order checked on both axes | `(31,31)` |
| `sigmau` | `distance/max(distance) * max_sigmau`, explicit `max_sigmau=0.5` | `(31,31)` |
| source initialization scalars | literal source initial values and multipliers supplied explicitly | typed immutable scalars |

The raw-workbook `makima`/capital reconstruction branch was not executed because the filled workbook is the active source and hash-matched.

## 6. Canonical primary-source 2009 input

- Local no-overwrite root: `D:\ProjectTemp\ch5-mp4a2-2009-input-binding-20260830-001`
- Sole artifact: `calendar_2009_primary_premodel_input.json`
- Size: `36263` bytes
- Schema: `CH5_MP4A2_CANONICAL_ANNUAL_INPUT_V1`
- SHA-256: `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`

The canonical JSON contains the six decoupled identities, 31-province order, three primary source hashes, regression sheet identity, industry/fixed-Zt roles, explicit scalar initialization, all annual/calibration vectors, raw distance matrix, and source-transformed migration-cost matrix. Serialization is UTF-8, sorted-key, compact JSON with a terminal newline and no NaN. The same semantic scalar inputs are normalized to binary64 before serialization, preventing integer-vs-float spelling from changing identity.

The artifact contains primary-source values and therefore remains outside Git. Only its schema, hash, path, and summary are committed. Exclusive file/directory creation and a negative no-overwrite test passed.

## 7. Complete consumed-field cache compatibility

Comparison object: cache `mydata2{1}`, industry 4, economic data row 10. Pre-frozen bound: `rtol=1e-12`, `atol=1e-12`; it was not loosened.

| Field consumed by 2009 initialization | Classification | Maximum absolute difference |
|---|---|---:|
| GDP | EXACT | 0 |
| CAP | EXACT | 0 |
| POP | EXACT | 0 |
| `log_pgdp` | SOURCE_EQUIVALENT_BINARY64 | `4.440892098500626e-16` |
| `log_pcap` | EXACT | 0 |
| `IND_alpha` | EXACT | 0 |
| `IND_Zt` | SOURCE_EQUIVALENT_BINARY64 | `6.938893903907228e-18` |
| `GDP_multiplier` | EXACT | 0 |
| `POP_multiplier` | EXACT | 0 |
| calibration `delta` | EXACT | 0 |
| `prvname` after literal suffix normalization | EXACT | 0 |

Material mismatch list: empty. Missing-field list: empty. The compatibility gate also has negative tests for missing fields and a perturbed GDP vector.

Accepted classification is limited to:

`MP4A2_MAT_CACHE_COMPATIBILITY_REPRESENTATION_ACCEPTED_FOR_2009_RUNTIME_ONLY`

The cache remains derived and non-primary. It cannot decide calendar mapping or override canonical workbook/regression values.

## 8. Python annual and parity-entry preparation

Production module: `src/ch5_two_asset_hank/multi_province/annual.py`.

Main public API:

- `DecoupledAnnualIndex.for_calendar_year`
- `PrimaryAnnualSourceFiles.verified_hashes`
- `AnnualSourceScalars`
- `load_primary_annual_input`
- `CanonicalAnnualInput.canonical_bytes/canonical_sha256`
- `write_canonical_artifact`
- `compare_runtime_representation`
- `build_python_parity_entry`

`PythonAnnualParityEntry` binds the canonical hash, exact annual identities, province order, and accepted household-adapter/MP2/MP3 layer names. It contains no callback and imports none of those solver layers. `scientific_solver_called` is statically false. MP4B must perform manifest equality before it separately invokes the accepted layers.

## 9. MATLAB parity-wrapper preparation

- Path: `validators/multi_province/matlab/mp4b_calendar2009_stationary_wrapper.m`
- SHA-256: `D0FCEE89536E9095AE76A4576A0CA9249A29813C37D89A6E192B9AF6F5CF04E9`

Static proof:

- function definition alone performs no action;
- explicit `calendar_year=2009`, `analysis_index=1`, `data_year=10`, `data_MAT_index=1`, and regression key 10;
- accepts explicit protected-source root, new run root, canonical SHA, and prepared param/grid/numerics/CHI/initial state;
- rejects any pre-existing run root and creates the manifest only inside that new root;
- calls `load_GDPdata` only through the reconciled runtime representation and selects `data_MAT{1}`;
- bypasses `multi_prov_HANK_12sts`, which would incorrectly reuse `ii=1` as data row 1;
- prepares the existing lower-level call `mpHANK_equilibrium_2000(..., selected, 4, data_year)` with `data_year=10`;
- writes the complete pre-solver field manifest before the lower-level call;
- declares the MP4B trace-field contract and prepares a no-overwrite final `st`/manifest output.

No MATLAB executable or parser was invoked. Static source/token checks were used; actual MATLAB syntax/checkcode and execution remain an MP4B preflight responsibility within its one-run gate.

## 10. Frozen MP4B contract

Exactly one corrected calendar-2009 stationary run per language:

| Route | Maximum scientific calls |
|---|---:|
| corrected MATLAB decoupled 2009 stationary route | 1 |
| corrected Python decoupled 2009 stationary route | 1 |

Before either solver starts, MP4B must persist both pre-solver manifests and abort unless the canonical SHA, six annual identities, province order, source hashes, all primary fields, and accepted cache representation agree.

MP4B must persist each province's Ct, household Lt, At, Bt, AtTax, convergence statistic/diagnostics; `Lt_mat`, `Lt_supply`; productive capital contribution, `Kt_supply`, `rah`; firm `Yt,Kt,Lt,mt,KNratio,wjt,rk,ra,Govinc` and intermediates; composite wage, Taylor `rb`, national `GovSurplus`; every controller gap/count/action/snapshot/`tKNratio`/iteration/termination; and final province/national stationary objects.

Parity hierarchy is source/input/order, source-local arithmetic, pre-frozen solver-propagated differences, then qualitative diagnostics. A first divergence may be classified only as one of the five Owner-approved mismatch classes. No automatic repair, tolerance loosening, or second run is authorized unless MP4B explicitly says so. The legacy literal `ii=1 -> data row 1` route is outside the scientific 2009 budget.

## 11. Tests and static checks

- MP4A2 plus complete accepted MP1--MP3 focused regression: `52 passed`.
- Python compilation of changed source, validator, and test: PASS.
- Deterministic canonical serialization/hash: PASS.
- Primary source hash, explicit year cell, province order, distance-axis, shape, finiteness, and formula invariants: PASS.
- Full consumed-field cache comparator: PASS with no material mismatch.
- Negative tests: recoupled row 1, out-of-range year, missing cache field, perturbed GDP, and artifact overwrite all fail closed.
- Static AST check: annual production imports no household/HJB/KFE/one-turn/fixed-point/legacy solver.
- MATLAB wrapper static token/entry/no-overwrite check: PASS.
- `git diff --check`: PASS before closeout.

## 12. Scientific/model call ledger

| Scientific/model operation | Calls |
|---|---:|
| MATLAB | 0 |
| modular/standalone HA/HJB/KFE | 0 |
| MP2 empirical one-turn | 0 |
| MP3 empirical fixed point | 0 |
| legacy R5 | 0 |
| annual 31-province solve | 0 |
| shocks/transition/dynamics/IRF | 0 |
| Results | 0 |

Only workbook/XML reads, primary transformations, deterministic serialization, HDF5 cache reads, compatibility arithmetic, static inspection, compilation, and focused non-model tests ran.

## 13. Files written

- `src/ch5_two_asset_hank/multi_province/annual.py`
- bounded updates to `src/ch5_two_asset_hank/multi_province/provenance.py`
- bounded exports in `src/ch5_two_asset_hank/multi_province/__init__.py`
- `validators/multi_province/mp4a2_cache_compatibility.py`
- `validators/multi_province/matlab/mp4b_calendar2009_stationary_wrapper.m`
- `tests/test_mp4a2_annual_binding.py`
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`
- this report
- one local, uncommitted canonical JSON artifact at the path recorded above

No raw workbook, MAT cache, or model output was copied into Git.

## 14. Unresolved items and forbidden-operation check

Remaining items are execution-stage facts, not MP4A2 provenance blockers:

1. MP4B must supply the explicit MATLAB prepared param/grid/numerics/CHI/initial-state object and verify its manifest before the single run.
2. MATLAB checkcode/runtime availability and actual trace persistence can only be proven when MP4B authorizes MATLAB execution.
3. No stationary numerical parity, convergence, shock response, or multi-year result exists yet.

Forbidden-operation check: PASS. Protected MATLAB, source workbooks, cache, accepted household/HJB/KFE/oracle, MP2 arithmetic, MP3 controller, and historical R5 were not modified. MATLAB, household, fixed point, annual solve, shocks, transition, dynamics, IRF, and Results were not run. No neural-network code was added.

## 15. Roadmap and recommended next gate

The CURRENT roadmap now records MP1--MP3 acceptance, MP4A's correct conflict terminal, the Owner/L3 decoupling resolution, the MP4A2 preparation route, and continued closure of shocks and the 2010--2023 batch.

Exactly one next gate is recommended: **MP4B controlled corrected-calendar-2009 same-input MATLAB-Python stationary parity**, with one run per language, pre-solver manifest equality, complete persisted intermediates, and bounded first-divergence diagnosis.
