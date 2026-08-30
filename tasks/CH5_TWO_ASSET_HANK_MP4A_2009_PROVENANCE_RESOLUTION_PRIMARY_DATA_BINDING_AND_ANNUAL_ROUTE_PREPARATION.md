# CH5_TWO_ASSET_HANK_MP4A_2009_PROVENANCE_RESOLUTION_PRIMARY_DATA_BINDING_AND_ANNUAL_ROUTE_PREPARATION

Date: 2026-08-30
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer
Executor: Codex bounded Builder / provenance resolver / annual-route preparer
Owner: final scientific authority

## 1. Purpose

Execute **MP4A only**. Resolve the Owner-approved 2009 annual input identity from primary source evidence, bind the source-defined annual/calibration route, and prepare the first controlled MATLAB-Python 2009 stationary parity gate without running either model.

This task must answer, from source/workbook evidence rather than assumption:

1. Which exact workbook calendar-year row is 2009?
2. Which exact source `ii` / dataset index corresponds to that row?
3. Which filename/calendar-year label would MATLAB generate for the same object?
4. Which 31-province columns/order are consumed?
5. Which primary workbooks/regression inputs and transformations construct the annual calibration object?
6. Which parts of `数据估计结果_1000_100_0.mat` are merely derived cache representations?
7. Can Python reconstruct the complete 2009 pre-model calibration/input object from primary sources with a deterministic canonical identity?
8. What exact controlled run contract is required for MP4B same-input MATLAB-Python 2009 stationary parity?

No HJB, KFE, household, fixed point, GE, annual model, shock, transition, dynamics, IRF, or Results run is authorized here.

## 2. Controlling authority

Read and obey:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MP3_SOURCE_FAITHFUL_MANUAL_UPDATE_MAP_AND_FIXED_POINT_SEMANTICS_IMPLEMENTATION_AND_TINY_FIXTURE_VALIDATION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_OWNER_MP4_MULTI_YEAR_BASELINE_CACHE_AND_FIRST_YEAR_PARITY_DECISION.md`

Owner decisions frozen:

- `OWNER_MP4_FINAL_CONTRACT_MULTI_YEAR_2009_2023`
- `OWNER_MP4_INITIAL_CONTROLLED_ANCHOR_YEAR_2009`
- `OWNER_MP4_SINGLE_YEAR_PARITY_PRECEDES_MULTI_YEAR_BATCH`
- `OWNER_DERIVED_MAT_CALIBRATION_CACHE_NOT_PRIMARY_SCIENTIFIC_AUTHORITY`
- `OWNER_PRIMARY_CALIBRATION_AUTHORITY_SOURCE_WORKBOOKS_REGRESSION_INPUTS_AND_LOAD_GDPDATA_TRANSFORMATION`
- `OWNER_FIRST_YEAR_STATIONARY_PARITY_BEFORE_SHOCK_RESPONSE_PARITY`
- `OWNER_PARITY_MISMATCH_BOUNDED_ROOT_CAUSE_DIAGNOSIS_AUTHORIZED`

The active model repository remains the two-asset repository only. Historical one-asset R5 remains read-only evidence and must not be imported or modified.

## 3. Live continuity

Expected execution-start parent / accepted MP3 implementation commit:

`dbd80110a6d4d055c0326a309cdce214abfd50ce`

Expected Owner-decision commit directly after MP3:

`0af28e227a3438a72e3f69f5985a3d707b0e5432`

At start:

1. fresh-fetch `origin/main`;
2. confirm this task is on live `main` after the Owner-decision file;
3. verify clean worktree;
4. verify accepted MP1-MP3 production sources have not changed;
5. verify household oracle SHA remains accepted;
6. record live start SHA and source hashes.

If continuity fails, stop BLOCKED.

## 4. Protected/source data boundary

Protected MATLAB root is read-only:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Treat direct D: access as the physical target of the documented MatlabProgram boundary, not as a separate mutable copy.

At minimum re-read and hash:

- `main.m`
- `multi_prov_HANK_12sts.m`
- `mpHANK_equilibrium_2000.m`
- `load_GDPdata.m`
- `load_distdata.m`
- any helper directly required by `load_GDPdata.m`

Primary external data candidates identified by MP0, read-only:

- `中国各省省会地理距离矩阵.xlsx`
- `2000年后各省数据_填充NA.xlsx`
- `2000年后各省数据.xlsx`
- `R语言估计结果_plm估计.xlsx`

Derived cache candidate, read-only and non-authoritative:

- `数据估计结果_1000_100_0.mat`

Search for any existing `Multi_Province_12sts_<year>.mat` or other 2009 steady-state artifact only as provenance evidence. Do not treat discovered derived output as primary authority.

Do not modify any source workbook, MAT file, or MATLAB source.

## 5. Mandatory 2009 calendar/index adjudication

Build a fail-closed mapping table covering every relevant year/index representation:

- workbook explicit calendar-year label/value;
- workbook physical row number and zero/one-based data-row index;
- source `ii` used by `main.m` / `multi_prov_HANK_12sts`;
- `data_MAT{ii}` meaning;
- `data_year` passed downstream;
- `ii+2008` cache/output filename convention;
- any source offset/subset that makes `ii=1` or another index correspond to a specific calendar year.

Do not infer 2009 from the filename formula alone.

Read workbook year cells/headers directly and reconcile them with source loops. If the source and workbook semantics conflict, classify and stop before any annual model preparation that would guess the year.

Required terminal sub-classification:

- `YEAR_MAPPING_2009_SOURCE_AND_WORKBOOK_IDENTIFIED`
- or `YEAR_MAPPING_OWNER_PROVENANCE_REQUIRED`
- or `YEAR_MAPPING_SOURCE_CONFLICT_BLOCKED`

The final MP4A PASS requires the first classification.

## 6. Primary calibration transformation audit

Reconstruct the exact call/data graph for `load_GDPdata` with source lines and objects.

For each output field required by `mpHANK_equilibrium_2000`, record:

- output field name;
- economic meaning;
- source workbook/sheet/range or regression input;
- fill/interpolation rule;
- multiplier/scaling;
- panel/regression transform;
- year axis;
- province axis;
- dtype/shape;
- any MATLAB-specific operation affecting numeric identity;
- whether the field is primitive, transformed, estimated, or cached.

Explicitly identify all runtime dependencies such as R/regression calls, helper scripts, or cached regression results. Do not silently substitute a different estimator.

If `load_GDPdata` has multiple branches, establish which branch the designated Chapter 5 annual route actually uses for the 2009 path.

## 7. Derived MAT cache audit

Inspect the derived cache read-only only to establish compatibility/provenance:

- file hash/size/type;
- top-level variables;
- shape/schema identities if safely readable;
- creation/loading source lines;
- whether its content corresponds to primary source-derived `mydata2/data_MAT`;
- any evidence that the cache predates or differs from current source workbooks.

Do not use the MAT cache to overwrite or define primary 2009 inputs.

If cache and source-reconstructed inputs differ, record the difference and classify it. Do not repair by choosing whichever looks convenient.

## 8. Python annual-input reconstruction boundary

If and only if the primary source transformations are unambiguous and implementable without running the model, create a source-faithful annual-input preparation layer under the current repository.

Authorized production paths:

- `src/ch5_two_asset_hank/multi_province/annual.py`
- optional bounded additions to `provenance.py` / `province_contracts.py` only if required for annual-input contracts and not contradictory to accepted MP1 contracts
- bounded `multi_province/__init__.py` exports

The annual preparation layer may read the primary workbooks/regression input at a caller-supplied local path and construct typed immutable annual calibration/input objects. It must not contain HJB/KFE/household/fixed-point/shock execution.

No hidden defaults for local paths, year, cache use, province order, fill route, or estimator branch.

The derived MAT cache must be disabled by default and may only be requested in an explicit `compatibility_check`/read-only comparison mode.

If exact reconstruction requires an external estimator or unprovided source that cannot be reproduced in MP4A, do not invent a replacement. Stop with `OWNER_PROVENANCE_REQUIRED` or BLOCKED and report the missing authority.

## 9. Canonical 2009 input artifact

On a resolved route, construct exactly one deterministic 2009 **pre-model input artifact** from primary sources only.

This is input preparation, not a model solve.

Use a new no-overwrite local artifact root such as:

`D:\ProjectTemp\ch5-mp4a-2009-input-binding-<timestamp-or-task-id>`

Persist a canonical machine-readable representation sufficient for MP4B, plus a text manifest containing:

- source file hashes;
- source sheet/range identities;
- calendar/index mapping;
- province order;
- all transformed-field names/shapes;
- exact canonical artifact SHA-256;
- Python/NumPy/pandas/openpyxl/scipy versions actually used, if applicable;
- whether cache compatibility was checked;
- no-overwrite evidence.

Do not commit raw workbook contents or a full private/purchased dataset to GitHub. If the canonical object itself contains restricted/raw values, keep it local and commit only its hash/schema/summary evidence.

## 10. Pre-freeze MP4B stationary parity contract

Design but do not execute the next gate.

MP4B must compare **the same source-backed 2009 economic input identity** in MATLAB and Python.

Before either model runs, MP4B must persist and compare pre-solver input manifests for both languages.

Minimum stationary comparison layers to freeze:

1. annual/province/calibration input identity;
2. initialization of `Zt`, `GovInv`, household prices/returns, and controller state;
3. household outputs per province: at least `Ct`, household `Lt`, `At`, `Bt`, `AtTax`, convergence/statistic and any available diagnostics;
4. migration `Lt_mat`, `Lt_supply`;
5. productive capital contributions / `Kt_supply` and `rah`;
6. firm outputs including `Yt`, `Kt`, `Lt`, `wjt`, `rk`, `ra`, `Govinc` and source-relevant intermediates;
7. composite `w`, Taylor `rb`, national `GovSurplus`;
8. each manual fixed-point iteration: gaps, boundary counts, adaptive actions, `tKNratio`, iteration count and termination;
9. final 31-province stationary objects and national aggregates.

Acceptance must distinguish:

- exact/source-local parity;
- accepted binary64/solver-propagated diagnostic differences under a pre-frozen rule;
- material structural/numerical mismatch;
- qualitative sign/trend diagnostics.

Qualitative agreement never substitutes for unexplained source/formula mismatch.

## 11. Bounded mismatch diagnosis design for MP4B

The Owner authorizes bounded root-cause diagnosis after a parity mismatch. MP4A must therefore design MP4B to persist enough intermediate objects to localize the **first divergent stage**.

Allowed diagnostic classifications:

- `PYTHON_IMPLEMENTATION_ERROR`
- `MATLAB_SOURCE_OR_LEGACY_NUMERICAL_BEHAVIOR`
- `DATA_OR_CALIBRATION_PROVENANCE_MISMATCH`
- `SHARED_SOURCE_NUMERICAL_PROPAGATION_DIFFERENCE`
- `SCIENTIFIC_SPECIFICATION_OR_PROVENANCE_AMBIGUITY`

MP4B may diagnose after its single controlled comparison without automatic formula repair or tolerance loosening. Repair/re-execution requires explicit pre-authorized retry logic or a successor task.

## 12. Shock route planning boundary

Do not run shocks in MP4A.

Record for the future MP5A task that after accepted 2009 stationary parity, the project will compare the MATLAB **source-named response route** and Python faithful reproduction on the same 2009 baseline.

Future response diagnostics must compare numerical paths plus:

- sign/direction;
- peak sign and magnitude;
- peak period / turning points;
- decay/persistence;
- province-level spillover direction;
- cross-province ranking used by Chapter 5.

The MATLAB source-named response must remain classified as period-by-period stationary/comparative-static if that is what the source implements; do not relabel it genuine dynamic HANK transition.

## 13. Execution budget

Scientific/model solver calls in MP4A must be exactly zero:

- MATLAB model/solver: `0`
- modular HJB/KFE: `0/0`
- standalone HA/HJB/KFE/aggregate: `0`
- MP2 one-turn scientific execution: `0` except pure non-model schema/import tests; do not feed empirical annual data through it
- MP3 fixed-point: `0`
- legacy R5: `0`
- 31-province annual model: `0`
- shocks/AR1/transition/dynamics/IRF: `0`
- Results: `0`

Allowed:

- static source/workbook/cache reads;
- Python annual-input transformations only;
- canonical input serialization/hash;
- schema/contract/unit tests;
- compatibility comparison of source-derived input vs derived cache without model execution.

## 14. Allowed repository changes

On PASS, allowed changes are limited to:

- `src/ch5_two_asset_hank/multi_province/annual.py` if implemented;
- bounded annual-contract updates to existing MP1 provenance/contracts and `__init__.py` only when necessary and source-consistent;
- MP4A validators/tests for annual-input preparation;
- one MP4A report;
- update `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md` to record MP1-MP3 accepted status and the resolved Owner MP4 decisions / MP4A->MP4B->MP5A route.

Do not add raw workbook/cache data or model outputs to GitHub.

Do not modify accepted HJB/KFE/household/oracle, MP2 arithmetic, MP3 controller semantics, protected MATLAB, or legacy R5.

## 15. Required report

Write:

`docs/CH5_TWO_ASSET_HANK_MP4A_2009_PROVENANCE_RESOLUTION_PRIMARY_DATA_BINDING_AND_ANNUAL_ROUTE_PREPARATION_REPORT.md`

Include:

1. terminal classification;
2. live authority/continuity;
3. Owner decision markers;
4. exact 2009 calendar/index adjudication table;
5. province-order confirmation;
6. primary source/data hashes and workbook sheet/range map;
7. `load_GDPdata` field-by-field transformation map;
8. regression/R/cache dependency audit;
9. derived MAT cache classification and compatibility result if checked;
10. annual-input implementation API if created;
11. canonical 2009 input artifact path/hash/schema summary;
12. source-derived vs cache comparison table if available;
13. zero model-call ledger;
14. tests/static checks;
15. unresolved provenance list;
16. forbidden-operation check;
17. roadmap update summary;
18. exact MP4B proposed call budget and persisted intermediates;
19. exact mismatch-diagnosis boundary;
20. recommended next gate.

## 16. Terminals

PASS:

`MP4A_2009_PROVENANCE_RESOLUTION_PRIMARY_DATA_BINDING_AND_ANNUAL_ROUTE_PREPARATION_PASS`

Freeze on PASS:

- `MP4A_2009_CALENDAR_DATASET_INDEX_MAPPING_ACCEPTED`
- `MP4A_PRIMARY_CALIBRATION_SOURCE_CHAIN_ACCEPTED`
- `MP4A_DERIVED_MAT_CACHE_NONPRIMARY_ROLE_ACCEPTED`
- `MP4A_2009_CANONICAL_PREMODEL_INPUT_IDENTITY_ACCEPTED`
- `MP4A_MP4B_STATIONARY_PARITY_CONTRACT_ACCEPTED`

OWNER provenance terminal:

`MP4A_2009_PROVENANCE_RESOLUTION_OWNER_PROVENANCE_REQUIRED`

BLOCKED:

`MP4A_2009_PROVENANCE_RESOLUTION_PRIMARY_DATA_BINDING_AND_ANNUAL_ROUTE_PREPARATION_BLOCKED`

No scientific/model run is authorized by any MP4A terminal.

## 17. Repository closeout

Explicit-path stage only. One commit. One non-force push. GitHub read-back every changed path. Require `HEAD == origin/main`, ahead/behind `0/0`, clean worktree.

If PASS, recommend exactly one next gate: **MP4B controlled 2009 same-input MATLAB-Python stationary parity with persisted intermediate localization and bounded mismatch diagnosis**. Do not authorize 2010-2023 batch or shocks yet.
