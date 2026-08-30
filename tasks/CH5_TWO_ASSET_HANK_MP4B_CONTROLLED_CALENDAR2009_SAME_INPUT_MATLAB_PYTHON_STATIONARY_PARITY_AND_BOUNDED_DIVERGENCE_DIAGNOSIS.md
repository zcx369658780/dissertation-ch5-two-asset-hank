# CH5_TWO_ASSET_HANK_MP4B_CONTROLLED_CALENDAR2009_SAME_INPUT_MATLAB_PYTHON_STATIONARY_PARITY_AND_BOUNDED_DIVERGENCE_DIAGNOSIS

Date: 2026-08-30
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Issuer: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer
Executor: Codex bounded Builder / parity-run executor / first-divergence diagnostician
Owner: final scientific authority

## 1. Purpose

Execute the first controlled **calendar-2009** stationary comparison between the corrected/decoupled MATLAB route and the Python two-asset HANK reconstruction.

This task is the first authorized empirical 31-province stationary run after MP1-MP3 and MP4A2.

The task must:

1. prove same-input identity before any solver call;
2. prepare the exact MATLAB and Python stationary runtime states from the accepted MP4A2 calendar-2009 canonical input and source constants;
3. execute at most one corrected calendar-2009 MATLAB stationary route;
4. execute at most one corrected calendar-2009 Python stationary route;
5. persist enough per-turn and final objects to compare household, spatial, firm, monetary, fiscal, and controller layers;
6. compare the two routes layer-by-layer;
7. if a mismatch occurs, perform bounded first-divergence diagnosis sufficient to classify the earliest differing stage/object;
8. stop without automatic scientific repair or uncontrolled reruns.

This task does **not** authorize shocks, 2010-2023 batch execution, genuine dynamics, transition, Results prose, or manuscript claims.

## 2. Controlling authority

Read and obey first:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `project_rules/PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md`
- `project_rules/PROJECT_RULE_MATLAB_MODEL_DIAGNOSTIC_GATES_CURRENT.md`
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_OWNER_MP4_MULTI_YEAR_BASELINE_CACHE_AND_FIRST_YEAR_PARITY_DECISION.md`
- `docs/CH5_TWO_ASSET_HANK_OWNER_MP4_ANNUAL_YEAR_AXIS_DECOUPLING_AND_2009_BINDING_ADJUDICATION.md`
- `docs/CH5_TWO_ASSET_HANK_MP4A2_2009_DECOUPLED_ANNUAL_BINDING_CANONICAL_INPUT_AND_MATLAB_PARITY_WRAPPER_PREPARATION_REPORT.md`
- accepted MP1, MP2, and MP3 reports.

Preserve these Owner/L3 decisions:

- `OWNER_SINGLE_ACTIVE_CODEBASE_TWO_ASSET_HANK_ONLY`
- `OWNER_MP4_FINAL_CONTRACT_MULTI_YEAR_2009_2023`
- `OWNER_MP4_INITIAL_CONTROLLED_ANCHOR_YEAR_2009`
- `OWNER_MP4_SINGLE_YEAR_PARITY_PRECEDES_MULTI_YEAR_BATCH`
- `OWNER_ECONOMIC_CALENDAR_YEAR_IS_WORKBOOK_CALENDAR_YEAR`
- `OWNER_2009_ANCHOR_USES_EXPLICIT_WORKBOOK_2009_ROW`
- `MATLAB_LEGACY_ANNUAL_YEAR_INDEX_COUPLING_DEFECT_CONFIRMED`
- `OWNER_DERIVED_MAT_CALIBRATION_CACHE_NOT_PRIMARY_SCIENTIFIC_AUTHORITY`
- `MATLAB_FIXED_2020_IND_ZT_RETAINED_AS_SOURCE_NUMERICAL_INITIALIZATION_ANCHOR`
- `OWNER_FIRST_YEAR_STATIONARY_PARITY_BEFORE_SHOCK_RESPONSE_PARITY`
- `OWNER_PARITY_MISMATCH_BOUNDED_ROOT_CAUSE_DIAGNOSIS_AUTHORIZED`

Primary reconstruction authority remains:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

## 3. Live continuity

Expected accepted MP4A2 implementation/preparation commit:

`85772bc6920db58cd6ec38bf8e1d7a5d593e12fc`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task is on live `main` as a direct child of the accepted MP4A2 commit;
3. require clean worktree;
4. verify accepted MP1-MP3 source hashes are unchanged;
5. verify `annual.py` and the MP4A2 MATLAB wrapper identities from the MP4A2 report;
6. verify the accepted standalone household oracle SHA remains `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`;
7. verify the local canonical 2009 artifact exists at the reported no-overwrite root and has SHA-256 exactly `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`;
8. verify primary workbook/regression/distance/cache hashes match MP4A2;
9. verify no legacy `chapter5_model` runtime import exists.

If any identity fails, stop `MP4B_2009_STATIONARY_PARITY_BLOCKED` before scientific execution.

## 4. Frozen calendar-2009 identity

The scientific 2009 run must use the accepted decoupled binding:

- `calendar_year = 2009`
- `analysis_index = 1`
- `workbook_data_row_index = 10` (MATLAB one-based numeric row)
- physical Excel row = 11
- `data_MAT_index = 1`
- `output_filename_year = 2009`
- `regression_vintage_key = 10`
- fixed-2020 `IND_Zt` retained only as the source numerical initialization anchor.

The literal legacy route `ii=1 -> data_year=1 -> workbook calendar 2000` is forbidden from the scientific 2009 run budget.

## 5. Required pre-run source and storage preflight

Before either scientific route is invoked:

### 5.1 MATLAB storage/source safety

Record:

- logical `C:\MatlabProgram` compatibility entry if present;
- resolved physical target `D:\MatlabProgram` when safely checkable;
- protected source root identity;
- physical target drive free space;
- output drive free space;
- all required MATLAB source hashes.

Protected MATLAB remains read-only. Do not edit the original `.m` files.

### 5.2 Source-prepared state contract

MP4A2 left MATLAB `prepared.param/grids/num/CHI/inits` explicit. MP4B must source-bind them before the run.

Read the exact designated MATLAB initialization source, at minimum:

- `multi_prov_HANK_12sts.m`
- `mpHANK_equilibrium_2000.m`
- `HANK_mp_1eq.m`
- `HANK_mp_1turn.m`
- `HANK_2ASSETS_HJB.m`

Construct a **prepared-state manifest** from literal/source-defined values only. Do not infer missing constants from old R5, generic HANK literature, or convenience defaults.

The prepared-state manifest must include every field in `param`, `grids`, `num`, `CHI`, and `inits` that can affect the stationary run, including array shapes/order and `la_mat`/switching-generator identity.

Prepare the equivalent Python runtime manifest from the same source-defined values and the accepted HA mapping.

### 5.3 Manifest equality gate

Before any solver call, compare MATLAB and Python pre-solver manifests for:

- canonical 2009 SHA;
- all six decoupled annual identities;
- primary source hashes;
- province order;
- GDP/CAP/POP/log vectors;
- `IND_alpha`, fixed-2020 `IND_Zt`;
- distance/migration inputs;
- `Zt`, `GovInv`, `inter_prv_ratio` initialization;
- all source scalars;
- household grids and state ordering;
- switching matrix/generator identity;
- HJB/KFE numerics and tolerances;
- outer-controller `reg_threshold`, max iterations, clipping bounds, and initialization;
- any other prepared field that affects either route.

Required pre-solver terminal:

`MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_PASS`

If not established, abort before both model runs and report the first differing input field.

The derived MAT cache may be used on the MATLAB route only as the already accepted 2009 runtime compatibility representation. It must not override the canonical primary-source manifest.

## 6. MATLAB validation runtime and trace requirement

Use the accepted validation-only wrapper:

`validators/multi_province/matlab/mp4b_calendar2009_stationary_wrapper.m`

Expected SHA-256:

`D0FCEE89536E9095AE76A4576A0CA9249A29813C37D89A6E192B9AF6F5CF04E9`

### 6.1 Prepared-state builder

A small validation-only MATLAB prepared-state helper may be added under:

`validators/multi_province/matlab/`

only to construct `prepared.param/grids/num/CHI/inits` byte-/value-faithfully from the designated source literals.

It must perform no model run by itself.

### 6.2 Trace instrumentation

The protected MATLAB source does not necessarily expose every per-iteration object needed for first-divergence localization.

MP4B may create a **timestamped local diagnostic copy** or repository validation-only trace helper that reproduces the relevant `mpHANK_equilibrium_2000` / `HANK_mp_1eq` orchestration with observability hooks only.

Hard requirements:

- protected source remains untouched;
- no economic formula, branch, tolerance, update order, clipping rule, HJB/KFE call, or convergence condition may change;
- instrumentation may only persist already-computed objects;
- before the scientific run, perform a static source-to-trace audit showing that all computational expressions are source-identical except observability/output statements;
- if trace equivalence cannot be established without changing computation, use the uninstrumented accepted wrapper and persist all objects available without modification; do not invent a second scientific algorithm.

The MATLAB route must use calendar 2009 with `data_MAT{1}` and `data_year=10`; it must never call the conflicting annual wrapper as the scientific entry.

### 6.3 MATLAB output root

Create one new timestamped no-overwrite root, for example:

`D:\ProjectTemp\ch5-mp4b-matlab-2009-<timestamp>`

Persist:

- pre-solver manifest;
- command/environment/source manifest;
- trace manifest/data;
- terminal status;
- final stationary object;
- warnings/errors;
- output hashes.

Do not overwrite legacy `.mat`, Excel, figures, or prior runs.

## 7. Python empirical stationary runtime bridge

The accepted MP3 controller intentionally consumes pre-frozen household batches and must remain unchanged.

MP4B may add a new production/runtime integration module, preferably:

`src/ch5_two_asset_hank/multi_province/stationary_runtime.py`

or another clearly named equivalent.

Its role is only to connect the accepted layers online:

`current old-state snapshot -> 31 accepted two-asset HA solves from the same copied old state -> complete household-output batch -> accepted MP2 one-turn arithmetic -> accepted MP3 controller semantics -> next turn`.

Hard requirements:

- do not modify accepted household/HJB/KFE/oracle arithmetic;
- do not modify accepted MP2 component arithmetic;
- do not modify accepted MP3 controller semantics;
- all 31 province household solves in a turn must observe the same copied old-turn state, preserving MATLAB simultaneity;
- no province may observe another province's newly updated state within the same turn;
- use the accepted static household adapter mapping and standalone MATLAB-faithful HA implementation;
- productive capital remains `At` only;
- firm labor remains `Lt_supply`;
- no generic GE root solver may be introduced.

Because MP3's accepted implementation is offline-batch oriented, an online runtime controller may mirror its already frozen source semantics, but before empirical execution it must prove exact equivalence against the accepted MP3 controller on **all seven MP3 tiny scenarios**. This regression must compare iteration count, gaps, flags/counts, adaptive actions, damping history, snapshots, termination, and final states. Any mismatch blocks the 2009 Python run.

The new runtime layer must not create a new economic closure; it is integration only.

## 8. Scientific execution budget

This task authorizes exactly the following scientific top-level runs:

### 8.1 MATLAB

- corrected/decoupled calendar-2009 stationary route: **maximum 1 top-level invocation**.

Internal calls made by that one invocation, including household HJB/KFE calls across provinces and outer iterations, are part of the single authorized stationary run.

No retry.

### 8.2 Python

- corrected/decoupled calendar-2009 stationary route: **maximum 1 top-level invocation**.

Internal accepted HA solves are bounded by source controller semantics: at most 31 province household solves per outer iteration and at most the source `max3iter=500` outer turns.

No retry.

### 8.3 Ordering on failures

- If pre-solver identity fails: run neither language.
- Run MATLAB first.
- If MATLAB fails because of environment/path/storage/wrapper/syntax infrastructure before producing a scientific stationary attempt, do not consume the Python scientific run; stop BLOCKED.
- If MATLAB scientifically executes but terminates with source nonconvergence or a model-domain failure, preserve that scientific outcome and proceed with the single Python run so the two routes can be compared.
- After the Python run, no automatic scientific rerun is permitted.

Forbidden scientific calls:

- literal legacy wrong-year MATLAB route: 0;
- 2010-2023 annual batch: 0;
- shocks/AR1 response: 0;
- transition/genuine dynamics/IRF Results: 0;
- legacy one-asset R5: 0.

## 9. Required persisted comparison objects

For both languages persist, where source/runtime makes the object available:

### 9.1 Input/initialization

- annual/calibration manifest;
- `param/grids/num/CHI/inits` or Python equivalents;
- initial province `Zt`, `GovInv`, `w`, `wjt`, `rb`, `rah`, `ra`, `Yt`, `Kt`, `Lt`, `pit`, targets, bounds;
- migration matrices and province order.

### 9.2 Every outer iteration

For each province:

- household inputs sufficient to establish same-input identity;
- `Ct`;
- household `Lt`;
- `At`;
- `Bt`;
- `AtTax`;
- household convergence flag/statistic and available diagnostics;
- `Lt_mat` and `Lt_supply`;
- productive capital contribution and `Kt_supply`;
- `rah`;
- firm `Kt`, `Lt`, `Yt`, `mt`, `KNratio`, `wt0`, `wjt`, `rk`, `Thetat`, `It`, `PIt`, `Corptax`, `ra0`, `ra`, `Govinc`;
- composite household `w`;
- Taylor `it` and `rb`;
- national `GovSurplus`;
- `NKrationgap`, `Ytgap`;
- household convergence count;
- `ra`/wage bound counts;
- `Zt` and `GovInv` adaptive actions;
- `tKNratio` before/after;
- old/pre-adaptation/next-state snapshots;
- iteration index and termination status.

### 9.3 Final

- final 31-province state;
- province stationary aggregates;
- national totals/diagnostics available under the source route;
- convergence/failure status and iteration count;
- output hashes/manifests.

Do not add large raw scientific outputs to GitHub; keep them in no-overwrite local run roots and commit text-first summaries/hashes only.

## 10. Comparison hierarchy

Compare in this order and stop the structural search at the **first divergent stage**:

1. pre-solver annual/prepared input identity;
2. first-turn household inputs;
3. first-turn household outputs;
4. first-turn migration labor;
5. first-turn capital contribution / `Kt_supply` / `rah`;
6. first-turn firm block;
7. first-turn composite wage / monetary / fiscal objects;
8. first-turn controller diagnostics/adaptation;
9. subsequent iterations in order;
10. final stationary state.

For fields governed by previously accepted same-input parity contracts, apply those contracts first.

Do not declare a downstream difference independently material if it is fully propagated from an already-localized upstream difference.

## 11. Numerical comparison rules

### 11.1 Exact/source-local objects

Require exact equality for categorical, integer, boolean, province order, branch labels, and source-identical deterministic arithmetic where binary64 operation order is matched.

### 11.2 Floating scientific objects

Before inspecting results, freeze a comparison table by object class.

Use prior accepted household parity contracts where applicable. Do not invent a broad universal tolerance after seeing results.

For newly compared outer/final objects, distinguish:

- source-identical local arithmetic;
- solver-propagated numeric difference;
- material structural/numerical mismatch.

No post-hoc tolerance loosening.

### 11.3 Qualitative diagnostics

After structural/numerical localization, also report:

- sign agreement;
- relative direction across provinces;
- ranking/correlation where economically meaningful;
- whether any difference would reverse a Chapter 5 interpretation.

Qualitative agreement is diagnostic only and does not erase an unexplained source-formula mismatch.

## 12. Bounded mismatch diagnosis

If the two scientific routes differ, use the persisted objects and read-only source inspection to classify the **first differing object/stage** as exactly one primary class:

- `PYTHON_IMPLEMENTATION_ERROR`
- `MATLAB_SOURCE_OR_LEGACY_NUMERICAL_BEHAVIOR`
- `DATA_OR_CALIBRATION_PROVENANCE_MISMATCH`
- `SHARED_SOURCE_NUMERICAL_PROPAGATION_DIFFERENCE`
- `SCIENTIFIC_SPECIFICATION_OR_PROVENANCE_AMBIGUITY`

Diagnosis may include:

- source-line comparison;
- runtime input comparison;
- formula/order comparison;
- persisted intermediate comparison;
- static inspection of Python and MATLAB code;
- non-scientific arithmetic reproduction on already persisted values.

Diagnosis may **not** include:

- a second MATLAB scientific run;
- a second Python scientific run;
- automatic repair and rerun;
- tolerance loosening;
- changing economic formulas;
- altering primary data.

If the root cause is clearly a Python implementation error, report the exact repair target and stop for a successor repair task. If the root cause is MATLAB legacy behavior, preserve the source behavior and propose a separate adjudication/repair gate; do not silently make Python copy a scientifically rejected legacy defect.

## 13. Tests and preflight gates before scientific execution

At minimum require:

- MP1-MP4A2 focused regression PASS;
- Python compile/static import PASS;
- MATLAB wrapper/prepared-state helper static or checkcode preflight PASS if MATLAB checkcode is available without executing the model;
- trace instrumentation source-equivalence audit PASS if instrumentation is used;
- prepared-state manifest equality PASS;
- canonical artifact SHA PASS;
- all primary/cache hashes PASS;
- online Python controller exact regression against all MP3 tiny fixtures PASS;
- no legacy runtime import;
- no production import from tests/validators unless explicitly validation-only runner design requires it outside production;
- no overwrite/output-root collision;
- disk-space preflight PASS.

If any preflight fails, do not consume scientific run budget.

## 14. Allowed repository changes

Authorized, if needed:

- `src/ch5_two_asset_hank/multi_province/stationary_runtime.py` or equivalent integration module;
- bounded `__init__.py` export update;
- MP4B parity comparator/runner/serializer under `validators/multi_province/`;
- validation-only MATLAB prepared-state/trace helpers under `validators/multi_province/matlab/`;
- MP4B focused tests;
- one text-first MP4B report under `docs/`;
- bounded CURRENT roadmap status update after terminal classification.

Do not modify:

- accepted standalone household/oracle source;
- accepted MP1 contracts except for a separately reported contradiction;
- accepted MP2 arithmetic;
- accepted MP3 controller semantics;
- MP4A2 canonical artifact bytes;
- protected MATLAB originals;
- primary workbooks/regression/distance files;
- derived MAT cache;
- historical one-asset R5 repository.

## 15. Required report

Write:

`docs/CH5_TWO_ASSET_HANK_MP4B_CONTROLLED_CALENDAR2009_SAME_INPUT_MATLAB_PYTHON_STATIONARY_PARITY_AND_BOUNDED_DIVERGENCE_DIAGNOSIS_REPORT.md`

Include at minimum:

1. terminal classification;
2. live authority/commit continuity;
3. all source/artifact hashes;
4. exact prepared-state source map;
5. MATLAB/Python pre-solver manifest equality table;
6. scientific call ledger with top-level counts;
7. run roots and output manifests/hashes;
8. MATLAB and Python convergence/failure status;
9. outer iteration counts;
10. complete first-divergence search table;
11. layer-by-layer stationary comparison summary;
12. household aggregate comparison;
13. migration/capital/rah comparison;
14. firm/wage/monetary/fiscal comparison;
15. controller history comparison;
16. final 31-province stationary comparison;
17. exact/source-local vs solver-propagated vs material classification;
18. qualitative sign/ranking interpretation diagnostic;
19. bounded root-cause classification if any mismatch;
20. material mismatch list;
21. unresolved scientific residual list;
22. source/environment failure list;
23. forbidden-operation check;
24. tests/static checks;
25. git closeout;
26. exactly one recommended next gate.

## 16. Terminals and acceptance

### Full stationary parity PASS

`MP4B_CONTROLLED_CALENDAR2009_SAME_INPUT_MATLAB_PYTHON_STATIONARY_PARITY_PASS`

Freeze only if justified:

- `MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_ACCEPTED`
- `MP4B_2009_HOUSEHOLD_ROUTE_PARITY_ACCEPTED`
- `MP4B_2009_MULTI_PROVINCE_OUTER_ROUTE_PARITY_ACCEPTED`
- `MP4B_2009_MANUAL_CONTROLLER_PARITY_ACCEPTED`
- `MP4B_2009_FINAL_STATIONARY_PARITY_ACCEPTED`
- `MP4B_2009_STATIONARY_ROUTE_ACCEPTED`

### Material mismatch / diagnosis complete

`MP4B_CONTROLLED_CALENDAR2009_STATIONARY_PARITY_MATERIAL_MISMATCH_DIAGNOSED`

Use when both controlled scientific runs completed and the first material divergence was localized/classified but parity cannot be accepted.

### Scientific nonconvergence comparison

`MP4B_CONTROLLED_CALENDAR2009_STATIONARY_NONCONVERGENCE_COMPARISON_COMPLETE`

Use when one or both scientific routes execute but source-level stationary convergence is not achieved, and the outcome has been compared/diagnosed without rerun.

### Infrastructure/source block

`MP4B_CONTROLLED_CALENDAR2009_STATIONARY_PARITY_BLOCKED`

Use when a required preflight or environment/source condition prevents the controlled comparison.

No terminal in this task authorizes shocks or 2010-2023 batch execution automatically.

## 17. Recommended next gate policy

Exactly one successor recommendation:

- if full PASS: recommend **MP5A source-named 2009 shock-law/response contract freeze and controlled response-parity preparation**, not multi-year batch yet;
- if Python implementation error: recommend a bounded Python repair task followed by one separately authorized parity rerun;
- if MATLAB legacy behavior: recommend an Owner/L3 MATLAB-legacy adjudication task;
- if provenance ambiguity: recommend provenance adjudication;
- if scientific nonconvergence: recommend a nonconvergence diagnosis/remediation gate without Results.

## 18. Git closeout

Explicit path staging only. No `git add .` / `git add -A`. One commit. One non-force push. GitHub read-back all changed paths. Require `HEAD == origin/main`, ahead/behind `0/0`, clean worktree.
