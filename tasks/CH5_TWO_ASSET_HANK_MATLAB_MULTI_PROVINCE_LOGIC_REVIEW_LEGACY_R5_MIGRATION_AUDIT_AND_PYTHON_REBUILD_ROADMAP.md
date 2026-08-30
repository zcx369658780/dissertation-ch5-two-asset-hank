# CH5_TWO_ASSET_HANK_MATLAB_MULTI_PROVINCE_LOGIC_REVIEW_LEGACY_R5_MIGRATION_AUDIT_AND_PYTHON_REBUILD_ROADMAP

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / source auditor / migration planner

Owner: final scientific authority

## 1. Purpose

Reconstruct, from source, the complete MATLAB **multi-province Chapter 5 model logic** around the already accepted two-asset household block; audit the historical Python R5 repository as a read-only migration source; classify every reusable legacy component; and produce an upload-ready **CURRENT Python multi-province HANK rebuild roadmap** plus a precise future task chain.

This task is planning/source-audit only. It must not implement, modify, or run any model solver.

The accepted MATLAB-faithful two-asset HA household route is already closed and must be treated as a frozen numerical oracle, not re-derived here.

The task must answer two practical questions:

1. What exactly does the designated MATLAB program do at the multi-province level, including steady-state iteration, regional migration/spatial allocation, firm/price/fiscal blocks, annual data/cache routing, and any dynamic/shock/IRF path that actually exists in the protected source tree?
2. Given the historical one-asset/synthetic Python R5 codebase, which pieces should be `KEEP`, `ADAPT`, `REPLACE`, or `DEFER`, and what is the shortest scientifically controlled path to a faithful Python multi-province two-asset HANK implementation?

## 2. Controlling accepted authority

Read and obey first:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_SOURCE_AUDIT_AND_CONTRACT_FREEZE_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_END_TO_END_AGGREGATE_COMPARATOR_NUMPY_BOOL_SERIALIZATION_CORRECTION_AND_CLOSEOUT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_FAITHFUL_STANDALONE_LABEL_ENCODING_CANONICALIZATION_AND_EXPORT_CLOSEOUT_REPORT.md`

Primary numerical authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Accepted household authorities remain frozen:

- `MATLAB_FAITHFUL_HJB_PROPAGATION_AWARE_PARITY_CONTRACT_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HJB_OPERATOR_PARITY_ACCEPTED`
- `MATLAB_FAITHFUL_STATIONARY_KFE_CONTAMINATED_ROW_AND_SAME_OPERATOR_DENSITY_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_KFE_DENSITY_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_END_TO_END_STATIONARY_DISTRIBUTION_PARITY_ACCEPTED`
- `MATLAB_PYTHON_TWO_ASSET_HA_FAITHFUL_HOUSEHOLD_AGGREGATE_PARITY_ACCEPTED`
- `MATLAB_FAITHFUL_TWO_ASSET_HA_STANDALONE_SINGLE_FILE_EXPORT_ACCEPTED`

The accepted standalone oracle is:

`exports/matlab_faithful_two_asset_ha.py`

Required SHA-256:

`276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`

The current GE provenance state remains:

`MATLAB_FAITHFUL_GE_STEADY_STATE_CLOSURE_OWNER_PROVENANCE_REQUIRED`

This is a known future production-baseline blocker. It does **not** prevent this source/migration audit or roadmap from passing if the roadmap explicitly carries the blocker forward without guessing.

## 3. Live continuity

Task-authoring parent observed before publication:

`14d474590df3575bd463ae69da8e481b4b2f27ea`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main` as a direct child of the accepted standalone-oracle commit;
3. verify clean worktree;
4. verify the standalone oracle SHA above;
5. verify the three controlling reports exist;
6. record the live start SHA.

Do not begin from uncommitted scientific changes.

## 4. External read-only evidence explicitly authorized for this task

### 4.1 Protected MATLAB source tree

Read-only root:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Designated household source:

`HANK_2ASSETS_HJB.m`

SHA-256:

`049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`

The previous GE audit identified at minimum:

- `main.m`
- `multi_prov_HANK_12sts.m`
- `mpHANK_equilibrium_2000.m`
- `HANK_mp_1eq.m`
- `HANK_mp_1turn.m`
- `HANK_2ASSETS_HJB.m`
- `HANK_firm.m`
- `Lt_seperate.m`
- `wage_caculate.m`
- `load_distdata.m`
- `load_GDPdata.m`

Do not assume this list is exhaustive for multi-province **dynamics**. Recursively inventory the protected MATLAB tree for additional relevant `.m`, `.mat` references, scripts, wrappers, transition/shock/IRF code, cached steady states, linearization/iteration code, plotting/output callers, and helper functions.

Do not modify or run protected MATLAB source.

### 4.2 Historical Python R5 repository

Read-only migration evidence:

`zcx369658780/dissertation-ch5-r5-python-model`

Expected live `main` at task publication time:

`9e73f7189865958fbe38a3cad4547b06b3d17aa3`

Fresh-fetch it read-only at execution time and report the observed SHA. If it has advanced, inspect the new live main but distinguish publication-time identity from execution-time identity.

This repository is **not** scientific authority for the two-asset household equations. It is read-only engineering/migration evidence.

At minimum audit:

- `AGENTS.md`
- `README.md`
- `configs/*`
- `docs/ARCHITECTURE.md`
- `docs/IMPLEMENTATION_STATUS.md`
- `docs/STEADY_STATE_EQUATION_CONTRACT.md`
- `docs/STEADY_STATE_DIAGNOSTIC_CONTRACT.md`
- `docs/AR1_ENGINE_CONTRACT.md`
- `docs/TRANSITION_SOLVER_CONTRACT.md`
- `docs/CONFIGURATION_CONTRACT.md`
- `docs/IO_AND_PROVENANCE_CONTRACT.md`
- `docs/R5_1_MIGRATION_TRACEABILITY.csv`
- `src/chapter5_model/parameters.py`
- `src/chapter5_model/grids.py`
- `src/chapter5_model/household_hjb.py`
- `src/chapter5_model/distribution_kfe.py`
- `src/chapter5_model/regional_structure.py`
- `src/chapter5_model/spatial_links.py`
- `src/chapter5_model/aggregate_block.py`
- `src/chapter5_model/steady_state.py`
- `src/chapter5_model/shocks.py`
- `src/chapter5_model/transition.py`
- `src/chapter5_model/diagnostics.py`
- `src/chapter5_model/io_contracts.py`
- relevant tests and experiment runners.

Do not modify or execute the historical repository.

## 5. Zero scientific-call budget

This task is source audit and planning only.

Required call ledger:

- MATLAB model calls: `0`
- current modular Python HA solver calls: `0`
- standalone HA oracle scientific calls: `0`
- legacy Python steady-state calls: `0`
- legacy Python transition calls: `0`
- AR(1) path-generation/model-response calls: `0`
- GE/manual fixed-point calls: `0`
- IRF/dynamics calls: `0`

Allowed operations are static file reads, hashes, recursive inventory, grep/search, AST/source inspection, dependency/call-graph analysis, metadata inspection, and documentation generation.

## 6. Mandatory MATLAB multi-province logic reconstruction

Do not merely restate the previous GE report. Extend it into a complete **multi-province architecture specification**.

### 6.1 Full source inventory and call graph

For every relevant MATLAB file report:

- relative path;
- SHA-256;
- script/function signature;
- callers;
- callees;
- relevant line ranges;
- model role;
- steady-state / dynamic / data / calibration / diagnostics classification.

Construct separate source-backed call graphs for:

1. annual data/cache preparation;
2. 31-province steady-state/manual fixed-point;
3. household–migration–capital–firm–wage–monetary feedback;
4. any genuine dynamic/transition/shock/IRF route found in the source tree;
5. output/persistence flow.

If no source-backed dynamic route exists, state that explicitly. Do not invent one.

### 6.2 Multi-province state and flow contracts

Freeze exact source roles for at minimum:

- province population `N`;
- household `Ct`, household effective `Lt`, `At`, `Bt`, `AtTax`;
- migration flows and `Lt_mat` / `Lt_supply`;
- `At*N` cross-province productive-capital allocation;
- `Kt_supply`, `GovInv`, `Kt`;
- issuer/province `ra`, household `rah`, liquid `rb`, borrowing spread `rb_gap`;
- firm `wjt`, household wage `w`;
- `Zt`, `Yt`, `KNratio`, `tKNratio`;
- inflation/price variables used in steady state;
- fiscal variables and diagnostics;
- any source-level distance, migration-cost, cross-province exposure, or weighting objects.

For every mapping, state orientation/index convention. Example: origin/destination province ordering must be explicit rather than inferred.

### 6.3 Manual steady-state iteration

Extract exact source semantics for:

- initialization;
- order of the 31 household calls;
- whether provinces are evaluated from old or partially updated state within one turn;
- `Lt_seperate` update timing;
- capital allocation update timing;
- `rah` update timing;
- firm update timing;
- wage update timing;
- Taylor `rb` update timing;
- `Zt` heuristic update;
- `GovInv` heuristic update;
- `tKNratio` damping;
- clipping/veto rules;
- all convergence tests;
- maximum iterations;
- failure behavior;
- annual cache read/write behavior.

The roadmap must treat this as an **update-map/fixed-point algorithm**, not silently redesign it into `fsolve`/Brent/Newton.

### 6.4 Data/calibration/cache provenance

Map every external input referenced by the designated multi-province route:

- annual `data_MAT{ii}` contents and construction;
- `load_GDPdata` inputs/outputs;
- `load_distdata` inputs/outputs;
- annual `Multi_Province_12sts_<year>.mat` caches;
- any workbook/R/MAT dependency;
- calibration parameters embedded in source;
- source-defined years and province ordering.

For each external input classify provenance as:

- `SOURCE_IDENTIFIED_AND_HASHABLE`
- `SOURCE_IDENTIFIED_EXTERNAL_DATA_PENDING_CAPTURE`
- `CACHE_DERIVED_NOT_PRIMARY_AUTHORITY`
- `OWNER_PROVENANCE_REQUIRED`

Do not read sensitive or irrelevant content beyond model provenance needs.

### 6.5 Dynamics/shock/IRF source audit

Search recursively for MATLAB code implementing or calling:

- AR(1) shocks;
- one-time innovations;
- province-specific productivity/public-capital/policy shocks;
- transition paths;
- backward time-dependent HJB;
- forward time-dependent KFE;
- time-indexed `a,b,z` distributions;
- price/wage/return paths;
- NK Phillips/Taylor dynamics;
- IRF construction;
- response normalization;
- transition convergence;
- terminal conditions.

If multiple routes exist, classify which are Chapter 5 two-asset, which are older/other models, and which are ambiguous.

Do not equate old Python R5 dynamics with MATLAB dynamics unless source establishes equivalence.

## 7. Mandatory historical Python R5 migration audit

The old Python repo is a **synthetic two-region one-asset architecture**. Its own README/status says full 31-province execution and empirical calibration were outside scope. Treat this limitation explicitly.

### 7.1 File-level migration matrix

For every relevant old Python source/config/doc/test, assign exactly one primary disposition:

- `KEEP` — reusable essentially unchanged as engineering/scientific component after bounded verification;
- `ADAPT` — useful architecture or logic, but must change for the faithful two-asset/multi-province model;
- `REPLACE` — scientific core is incompatible and must be replaced by current accepted authority or new source-faithful implementation;
- `DEFER` — not needed until a later stage or blocked by provenance.

For each row include:

- file/module;
- old role;
- disposition;
- exact reason;
- source authority for the new behavior;
- proposed target module/path;
- required validation gate;
- risk level.

At minimum explicitly adjudicate:

- old one-asset `household_hjb.py`;
- old one-asset `distribution_kfe.py`;
- old one-asset `grids.py`;
- old two-region/symmetric `steady_state.py` and its Brent closure;
- old synthetic `regional_structure.py`;
- old generic `spatial_links.py` and `W` orientation;
- old balanced-budget `aggregate_block.py` versus MATLAB fiscal diagnostics;
- old `parameters.py` and fixture validations;
- old `shocks.py` AR(1) engine;
- old `transition.py`;
- transition timing/accounting bridge;
- diagnostics/provenance/no-overwrite code;
- experiment runners/tests/configs.

### 7.2 Non-negotiable migration constraints

The roadmap must freeze:

- old one-asset HJB/KFE are not scientific authority and cannot be adapted by simply adding a second dimension;
- accepted standalone two-asset HA oracle is the household reference baseline;
- productive capital clearing must use the MATLAB source-defined illiquid `At`, not `At+Bt`;
- liquid `Bt` must not be silently repurposed as productive capital;
- firm labor must follow the MATLAB migration-derived `Lt_supply` contract, not household `Lt` unless source says otherwise;
- old balanced fiscal closure, goods-resource residual, NFI/current-account identities, `W` portfolio interpretation, and Brent root are retained only if MATLAB source independently supports them; otherwise they are diagnostic/history only;
- old AR(1) engine may be `KEEP` only for its generic recursion/provenance machinery if MATLAB shock-law audit supports the needed law/role; otherwise `ADAPT`;
- old transition timing bridges may be retained only as reference until two-asset MATLAB/source accounting validates each identity.

## 8. Repository strategy decision

The roadmap must explicitly recommend where the future multi-province Python implementation should live.

Evaluate at least:

1. extend `zcx369658780/dissertation-ch5-r5-python-model` using its engineering shell but replacing scientific cores;
2. extend the current `dissertation-ch5-two-asset-hank` beyond its present household boundary;
3. create a new dedicated multi-province successor repository and consume the accepted standalone oracle as vendored/frozen evidence.

For each option report:

- governance fit;
- migration cost;
- risk of mixing obsolete one-asset authority with accepted two-asset authority;
- traceability;
- ease of reusing diagnostics/AR1/transition scaffolding;
- recommended disposition.

Do not create a repository in this task. If a repository choice requires Owner approval, mark the roadmap decision point explicitly.

## 9. Upload-ready CURRENT roadmap requirements

Create:

`docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`

This document is intended for upload into the GPT Project Sources. It must be self-contained and written as the new **CURRENT** route.

It must explicitly state that it supersedes, for future multi-province development, the older 2026-08-22 R5 Python/AR1 roadmap and stale status documents that predate accepted two-asset household parity. Do not delete historical files in this task.

The roadmap must contain at minimum:

### 9.1 Current accepted baseline

- accepted two-asset HA oracle identity/hash;
- accepted HJB/KFE/distribution/aggregate markers;
- accepted stationary aggregate values as regression anchors;
- current GE provenance blocker;
- old R5 repo live identity and evidence-only status.

### 9.2 Scientific target architecture

A proposed Python module architecture for:

- provenance/data contracts;
- province/calibration objects;
- two-asset household adapter/oracle interface;
- migration/labor allocation;
- cross-province illiquid-capital allocation;
- firm block;
- wage aggregator;
- monetary/Taylor block;
- fiscal diagnostics;
- one-turn update map;
- manual steady-state fixed-point orchestrator;
- annual cache/orchestration;
- shocks;
- dynamic two-asset HJB/KFE;
- transition/spatial accounting;
- diagnostics/I/O;
- Results boundary.

Distinguish production modules from validators/adapters and from historical/reference code.

### 9.3 Phased task dependency graph

Define a complete staged route with clear gates. Codex may revise labels/splits based on source evidence, but it must cover the following logical sequence:

- `MP0` — this source/migration audit and roadmap;
- `MP1` — source-faithful province/data/calibration contracts + frozen two-asset household adapter interface;
- `MP2` — source-faithful single `HANK_mp_1turn` equivalent on deterministic frozen fixture, with component-by-component parity/localization;
- `MP3` — `HANK_mp_1eq` manual update-map/fixed-point semantics and convergence parity;
- `MP4` — annual/cache orchestration + 31-province stationary acceptance after Owner baseline/cache provenance is frozen;
- `MP5` — shock/AR(1) source-law reconciliation and reuse/adaptation of old engine;
- `MP6` — MATLAB dynamic/transition source specification freeze;
- `MP7` — two-asset time-dependent household HJB/KFE implementation and validation;
- `MP8` — multi-province transition/spatial/fiscal/accounting integration;
- `MP9` — conditional transition/IRF numerical validation and robustness;
- `MP10` — formal Results eligibility gate.

If the MATLAB source shows a better stage ordering, change it and explain why.

For every stage include:

- objective;
- primary authority;
- inputs;
- target files/modules;
- scientific execution budget concept;
- mandatory diagnostics;
- acceptance marker(s);
- blockers / Owner decisions;
- successor gate.

### 9.4 Structure-first validation policy

Freeze the rule:

**Do not jump from the accepted single-household fixture directly to a full 31-province annual run.**

The roadmap must define source-extracted deterministic fixtures for structural parity before production data/calibration, including where possible:

- a tiny province-count fixture for migration/capital/wage orientation;
- a one-turn fixture with pre-frozen household outputs to isolate outer logic;
- a same-input annual-data snapshot before any full fixed-point solve;
- own-language end-to-end bridge only after same-input component parity.

### 9.5 Owner provenance checkpoints

Carry forward explicit unresolved decisions without guessing:

- Chapter 5 baseline year vs multi-year acceptance contract;
- calibration cache authority;
- dissertation Chapter 5 source/evidence path;
- manual update-map state ordering if a vector representation is needed;
- any ambiguous MATLAB dynamic route;
- repository strategy if not source-determined.

For each checkpoint state the earliest stage at which it becomes blocking.

### 9.6 Legacy reuse estimate

Provide a source-backed work estimate table separating:

- reusable without scientific redesign;
- reusable after adaptation;
- scientifically replaced by the new two-asset oracle/source;
- future/new work not previously completed.

Do not present fake precision. Use ranges and explain the dependency basis.

### 9.7 Results boundary

Freeze that no paper IRF/Results claim is allowed until:

- multi-province steady-state route is accepted;
- dynamic two-asset household route is accepted;
- transition/spatial/accounting route is accepted;
- shock provenance and response definition are accepted;
- formal run provenance/robustness gates pass.

## 10. Required source-audit report

Also create:

`docs/CH5_TWO_ASSET_HANK_MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_REPORT.md`

The report must include:

1. terminal classification;
2. live current-repo and old-R5-repo identities;
3. zero-scientific-call ledger;
4. full MATLAB multi-province source inventory and hashes;
5. steady-state call graph;
6. multi-province flow/orientation table;
7. manual update-map timing/convergence specification;
8. data/calibration/cache provenance table;
9. dynamic/shock/IRF source inventory and conclusions;
10. old Python R5 file-level `KEEP/ADAPT/REPLACE/DEFER` matrix;
11. repository strategy comparison and recommendation;
12. contradictions between old Python assumptions and designated MATLAB behavior;
13. complete Owner-provenance list with blocking stage;
14. revised proposed task chain;
15. source-backed reuse/redo estimate;
16. exact roadmap path/hash;
17. changed-path list and git closeout evidence.

## 11. Immediate next-task design

At the end of the roadmap, propose exactly **one** smallest next task based on evidence.

Expected class, unless audit shows a prerequisite first:

**source-faithful multi-province contracts + two-asset household adapter + deterministic one-turn fixture freeze**.

Design the task name, purpose, inputs, allowed paths, scientific-call budget, acceptance outputs, and stop boundary, but **do not create or execute the successor task**.

If repository strategy requires Owner approval before implementation, make the next task a bounded repository/migration authority freeze instead.

## 12. Explicit prohibitions

Do not:

- run MATLAB;
- run current or legacy Python model solvers;
- modify protected MATLAB files;
- modify the historical R5 repository;
- modify accepted household source/oracle;
- copy/import old one-asset household code as authority;
- implement multi-province Python code;
- choose a baseline year for the Owner;
- bless a calibration cache without provenance;
- redesign the manual MATLAB fixed point into a root solver;
- assume `W` matches MATLAB cross-province allocation without source proof;
- run full 31-province experiments;
- run transition/IRF/dynamics;
- generate Results claims;
- delete/supersede historical files physically.

## 13. Repository closeout

Authorized mutation in the current repository is documentation only:

- `docs/CH5_TWO_ASSET_HANK_MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_REPORT.md`
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`

Stage only those two paths, commit once, non-force push once, read back both from GitHub, require `HEAD == origin/main`, and require clean worktree.

## 14. Terminal classifications

Return exactly one:

- `MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_ROADMAP_PASS`
- `MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_OWNER_PROVENANCE_REQUIRED`
- `MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_BLOCKED`

Use `...PASS` if the architecture/migration audit and roadmap are complete while clearly carrying known future Owner-provenance blockers forward.

Use `...OWNER_PROVENANCE_REQUIRED` only if missing Owner information prevents completion of the audit/roadmap itself, not merely because a later production stage will need an Owner decision.
