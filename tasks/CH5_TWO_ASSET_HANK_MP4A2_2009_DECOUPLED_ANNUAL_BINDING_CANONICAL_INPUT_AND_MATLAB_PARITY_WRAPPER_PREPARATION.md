# CH5_TWO_ASSET_HANK_MP4A2_2009_DECOUPLED_ANNUAL_BINDING_CANONICAL_INPUT_AND_MATLAB_PARITY_WRAPPER_PREPARATION

Date: 2026-08-30
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer
Executor: Codex bounded Builder / provenance resolver / annual-input implementer
Owner: final scientific authority

## 1. Purpose

Resolve the MP4A year-routing blocker under the accepted Owner/L3 adjudication and prepare, but do not execute, the first controlled calendar-2009 MATLAB-Python stationary parity run.

MP4A2 must:

1. implement the decoupled annual index contract;
2. reconstruct a canonical calendar-2009 pre-model input from primary workbooks/regression inputs;
3. fully compare the consumed 2009 calibration/input fields against the derived MAT cache as a compatibility representation only;
4. prepare a non-destructive MATLAB parity wrapper that uses analysis/calibration index 1 but economic workbook/data row 10 and labels the run 2009;
5. prepare Python annual binding to the same canonical 2009 economic identity;
6. freeze the exact MP4B run and comparison contract.

No model solver may run in MP4A2.

## 2. Controlling authority

Read and obey:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MP4A_2009_PROVENANCE_RESOLUTION_PRIMARY_DATA_BINDING_AND_ANNUAL_ROUTE_PREPARATION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_OWNER_MP4_MULTI_YEAR_BASELINE_CACHE_AND_FIRST_YEAR_PARITY_DECISION.md`
- `docs/CH5_TWO_ASSET_HANK_OWNER_MP4_ANNUAL_YEAR_AXIS_DECOUPLING_AND_2009_BINDING_ADJUDICATION.md`
- accepted MP1-MP3 reports

Freeze and preserve:

- `OWNER_ECONOMIC_CALENDAR_YEAR_IS_WORKBOOK_CALENDAR_YEAR`
- `OWNER_2009_ANCHOR_USES_EXPLICIT_WORKBOOK_2009_ROW`
- `MATLAB_LEGACY_ANNUAL_YEAR_INDEX_COUPLING_DEFECT_CONFIRMED`
- `OWNER_DERIVED_MAT_CALIBRATION_CACHE_NOT_PRIMARY_SCIENTIFIC_AUTHORITY`
- `MATLAB_FIXED_2020_IND_ZT_RETAINED_AS_SOURCE_NUMERICAL_INITIALIZATION_ANCHOR`
- `OWNER_PARITY_MISMATCH_BOUNDED_ROOT_CAUSE_DIAGNOSIS_AUTHORIZED`

## 3. Live continuity

Expected accepted MP4A BLOCKED report commit:

`cf9516742afda1c4f9a57075253463a8810301a6`

Expected Owner/L3 adjudication commit directly after it:

`8ea3f6d26ed1b29a460f8a03d554780be6236271`

At start:

- fresh-fetch `origin/main`;
- confirm this exact task is live after the adjudication commit;
- require clean worktree;
- verify MP1-MP3 production hashes unchanged;
- verify accepted standalone HA oracle unchanged;
- verify no legacy one-asset runtime import.

## 4. Frozen decoupled calendar contract

For calendar year `y` in 2009-2023:

- `calendar_year = y`
- `analysis_index = y - 2008`
- `workbook_data_row_index = y - 1999` (MATLAB one-based numeric row)
- `data_MAT_index = analysis_index`
- `output_filename_year = y`
- `regression_vintage_key = analysis_index + 9`

For 2009 exactly:

- calendar year `2009`
- analysis/calibration cell index `1`
- workbook/data row index `10`
- output label `2009`
- regression vintage key/suffix `10`

Do not re-couple these identities into one scalar.

## 5. Primary-data 2009 reconstruction

Read-only protected/data boundary remains the documented MatlabProgram physical target.

Primary inputs:

- `2000年后各省数据_填充NA.xlsx`
- `R语言估计结果_plm估计.xlsx`
- `中国各省省会地理距离矩阵.xlsx`

Raw fallback workbook may be audited but is not the active filled-workbook route.

Derived/non-primary compatibility cache:

- `数据估计结果_1000_100_0.mat`

Implement source-faithful Python annual input preparation under:

- `src/ch5_two_asset_hank/multi_province/annual.py`

Bounded source-consistent changes to `provenance.py`, `province_contracts.py`, and package `__init__.py` are allowed only if necessary.

No hidden defaults for local paths, calendar year, analysis index, data row, cache, province order, or estimator/regression branch.

The canonical 2009 object must explicitly contain or bind all pre-model objects consumed by `mpHANK_equilibrium_2000` and the later household/outer route, including at minimum:

- calendar/index identities;
- province order;
- GDP/CAP/POP and logs at calendar 2009;
- `IND_alpha` from `data_MAT{1}` / regression vintage key 10;
- source-defined fixed-2020 `IND_Zt` initialization object for the same calibration vintage;
- all source scalars/multipliers needed to initialize `Zt`, `GovInv`, population, targets, and provincial state;
- distance/migration source identity and schema;
- any other source-required annual field discovered during implementation.

Persist exactly one canonical pre-model artifact in a timestamped no-overwrite local root. Commit only schema/hash/summary evidence, not restricted/raw contents.

## 6. Dissertation cross-check

Use the designated dissertation evidence if locally accessible; otherwise use the accepted Owner/L3 adjudication as authority.

At minimum cross-check that Table 5-2's 2009 actual-GDP column corresponds to the explicit workbook 2009 row for sampled/all provinces where deterministic extraction is practical. This is an intent/provenance check, not model-output validation.

Do not use dissertation text to silently alter MATLAB formulas beyond the accepted year-axis adjudication.

## 7. Derived MAT cache compatibility gate

The MAT cache remains non-primary.

Compare **all fields consumed by the 2009 stationary initialization**, not only the earlier MP4A sample, between:

- primary-source reconstruction; and
- cache `mydata2{1}` representation.

Required classifications:

- exact;
- source-equivalent binary64 representation within a pre-frozen machine bound;
- material mismatch.

If every consumed field is compatible, freeze only:

`MP4A2_MAT_CACHE_COMPATIBILITY_REPRESENTATION_ACCEPTED_FOR_2009_RUNTIME_ONLY`

This permits MP4B MATLAB to use the existing cache as a runtime representation **only because its pre-solver values have been independently reconciled to primary sources**. It does not upgrade the cache to scientific authority.

If a consumed field is materially different, MP4A2 cannot authorize the cache-backed MATLAB runtime. Prepare a cache-bypass parity wrapper/input route instead or stop BLOCKED if that cannot be done without guessing.

## 8. MATLAB parity wrapper preparation

Prepare a validation-only MATLAB wrapper under repository validator paths, for example:

`validators/multi_province/matlab/mp4b_calendar2009_stationary_wrapper.m`

The wrapper must be small, explicit, source-line documented, and must not modify protected MATLAB files.

Required semantics:

- explicit `calendar_year = 2009`;
- explicit `analysis_index = 1`;
- explicit `data_year = 10`;
- explicit `data_MAT_index = 1`;
- load/reconstruct the source calibration representation through the reconciled route;
- call the existing lower-level MATLAB stationary route using `data_MAT{1}` together with `data_year=10`;
- never invoke the conflicting `multi_prov_HANK_12sts(ii,pp)` annual coupling as the scientific 2009 entry;
- output only to an MP4B-supplied timestamped no-overwrite run root;
- expose/persist pre-solver input manifest and all parity intermediates required by MP4B;
- default behavior must not run merely by import/path addition.

MP4A2 performs static/checkcode-style inspection only. Do not execute MATLAB.

## 9. Python parity entry preparation

Prepare the Python annual entry/binding needed by MP4B without running the scientific model.

It must consume the same canonical 2009 identity and wire it to the already accepted two-asset HA adapter / MP2 / MP3 layers without changing their accepted arithmetic.

Do not execute HJB/KFE/HA/MP3 on empirical 2009 inputs in MP4A2.

## 10. MP4B exact run plan

Freeze, but do not execute, exactly one corrected calendar-2009 run per language:

- MATLAB corrected/decoupled 2009 route: max 1 scientific stationary run;
- Python corrected/decoupled 2009 route: max 1 scientific stationary run.

The legacy literal `ii=1 -> workbook 2000` route is **not** part of the scientific 2009 run budget. It may remain forensic evidence and requires separate authority if later executed.

Before either solver starts in MP4B:

- persist both pre-solver input manifests;
- require calendar/index identities to match the adjudication;
- compare canonical primary-source values and cache/runtime representation identity;
- abort before solver execution if same-input identity is not established.

Persist per iteration and final state enough to compare:

- each province household `Ct`, household `Lt`, `At`, `Bt`, `AtTax`, convergence/statistic and available diagnostics;
- `Lt_mat`, `Lt_supply`;
- capital contribution, `Kt_supply`, `rah`;
- firm `Yt,Kt,Lt,mt,KNratio,wjt,rk,ra,Govinc` and relevant intermediates;
- composite `w`, Taylor `rb`, `GovSurplus`;
- controller raw gaps, household count, ra/wage bound counts, Zt/GovInv actions, `tKNratio`, snapshots, iteration and termination;
- final province and national stationary aggregates.

## 11. MP4B comparison and bounded diagnosis

Parity hierarchy:

1. source/input/ordering parity;
2. source-local arithmetic parity;
3. accepted solver-propagated numerical differences under pre-frozen bounds;
4. qualitative diagnostics only after the above.

On mismatch, the same MP4B task may perform bounded read-only diagnosis to locate the first divergent object and classify it as:

- `PYTHON_IMPLEMENTATION_ERROR`
- `MATLAB_SOURCE_OR_LEGACY_NUMERICAL_BEHAVIOR`
- `DATA_OR_CALIBRATION_PROVENANCE_MISMATCH`
- `SHARED_SOURCE_NUMERICAL_PROPAGATION_DIFFERENCE`
- `SCIENTIFIC_SPECIFICATION_OR_PROVENANCE_AMBIGUITY`

No automatic repair/retry unless MP4B explicitly pre-authorizes a bounded retry branch.

## 12. Model-call budget

Exactly zero scientific/model solver calls in MP4A2:

- MATLAB: 0
- modular/standalone HA/HJB/KFE: 0
- MP2 empirical one-turn: 0
- MP3 empirical fixed point: 0
- legacy R5: 0
- annual 31-province solve: 0
- shocks/transition/dynamics/IRF: 0
- Results: 0

Allowed:

- workbook/regression/cache reads;
- primary-data transformations;
- canonical artifact serialization;
- static MATLAB wrapper inspection;
- schema/hash/unit/compatibility tests.

## 13. Allowed repository changes

On PASS:

- `src/ch5_two_asset_hank/multi_province/annual.py`
- bounded annual-contract changes to existing `provenance.py`, `province_contracts.py`, `__init__.py`
- validation-only MATLAB wrapper/helper(s) under `validators/multi_province/matlab/`
- MP4A2 validators/tests
- one MP4A2 report
- CURRENT roadmap update recording MP1-MP3 accepted, MP4A blocked/resolved, and MP4A2 -> MP4B route

Do not modify accepted household/HJB/KFE/oracle, MP2 arithmetic, MP3 controller, protected MATLAB, historical R5, or raw/cache files.

## 14. Required report

Write:

`docs/CH5_TWO_ASSET_HANK_MP4A2_2009_DECOUPLED_ANNUAL_BINDING_CANONICAL_INPUT_AND_MATLAB_PARITY_WRAPPER_PREPARATION_REPORT.md`

Include:

- terminal;
- live continuity;
- Owner/L3 adjudication markers;
- exact decoupled year table;
- dissertation/workbook 2009 cross-check;
- source-data/regression hashes;
- field-by-field primary transformation map;
- canonical 2009 artifact path/hash/schema;
- full consumed-field cache compatibility table;
- annual.py API;
- MATLAB wrapper path/hash/static proof;
- Python parity-entry preparation;
- MP4B exact call budget and manifests/intermediates;
- zero model-call ledger;
- tests/static checks;
- unresolved list;
- forbidden-operation check;
- roadmap update;
- recommended next gate.

## 15. Terminals

PASS:

`MP4A2_2009_DECOUPLED_ANNUAL_BINDING_CANONICAL_INPUT_AND_MATLAB_PARITY_WRAPPER_PREPARATION_PASS`

Freeze on PASS:

- `MP4A2_DECOUPLED_ANNUAL_INDEX_CONTRACT_ACCEPTED`
- `MP4A2_2009_PRIMARY_SOURCE_CANONICAL_INPUT_ACCEPTED`
- `MP4A2_2009_RUNTIME_REPRESENTATION_COMPATIBILITY_ACCEPTED`
- `MP4A2_MATLAB_2009_PARITY_WRAPPER_PREPARED_ACCEPTED`
- `MP4A2_PYTHON_2009_PARITY_ENTRY_PREPARED_ACCEPTED`
- `MP4A2_MP4B_SAME_INPUT_STATIONARY_PARITY_EXECUTION_CONTRACT_ACCEPTED`

BLOCKED:

`MP4A2_2009_DECOUPLED_ANNUAL_BINDING_CANONICAL_INPUT_AND_MATLAB_PARITY_WRAPPER_PREPARATION_BLOCKED`

OWNER provenance required:

`MP4A2_2009_DECOUPLED_ANNUAL_BINDING_OWNER_PROVENANCE_REQUIRED`

## 16. Closeout

Explicit paths only. One commit. One non-force push. GitHub read-back. `HEAD == origin/main`. ahead/behind `0/0`. clean worktree.

If PASS, recommend exactly one next gate: **MP4B controlled corrected-calendar-2009 same-input MATLAB-Python stationary parity**. Do not authorize shocks or 2010-2023 batch yet.
