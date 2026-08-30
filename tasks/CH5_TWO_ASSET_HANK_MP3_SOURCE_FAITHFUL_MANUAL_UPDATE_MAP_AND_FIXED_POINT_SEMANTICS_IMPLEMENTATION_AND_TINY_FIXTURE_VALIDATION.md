# CH5_TWO_ASSET_HANK_MP3_SOURCE_FAITHFUL_MANUAL_UPDATE_MAP_AND_FIXED_POINT_SEMANTICS_IMPLEMENTATION_AND_TINY_FIXTURE_VALIDATION

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / source-faithful fixed-point controller implementer

Owner: final scientific authority

## 1. Purpose

Implement **MP3 only**: reproduce the MATLAB `HANK_mp_1eq.m` manual update-map / fixed-point **controller semantics** on bounded synthetic multi-turn fixtures, using the already accepted MP2 one-turn production layer as the only outer economic turn implementation.

MP3 must reproduce, from source and without redesign:

- full-turn old-state/new-state sequencing;
- fixed-point convergence diagnostics;
- household-convergence aggregation semantics without calling the household solver;
- `ra` boundary veto semantics;
- wage-bound diagnostics without silently promoting them into the convergence predicate;
- source-exact `Zt` adaptive reset rule;
- source-exact `GovInv` multiplicative adjustment rule and branch direction;
- source-exact `tKNratio` damping;
- prior-output bookkeeping such as `Yt_1` exactly where source requires it;
- maximum-iteration failure behavior;
- auditable iteration history and termination reason.

This task must **not** run the two-asset household solver, choose an empirical baseline year/cache, execute 31-province annual calibration, implement shocks/dynamics, or create Results.

## 2. Controlling authority

Read and obey:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MP1_SOURCE_FAITHFUL_MULTI_PROVINCE_CONTRACTS_ACCEPTED_HA_ADAPTER_AND_DETERMINISTIC_ONE_TURN_FIXTURE_FREEZE_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MP2_SOURCE_FAITHFUL_DETERMINISTIC_ONE_TURN_IMPLEMENTATION_AND_FROZEN_FIXTURE_PARITY_REPORT.md`

Owner route remains frozen:

- `OWNER_SINGLE_ACTIVE_CODEBASE_TWO_ASSET_HANK_ONLY`
- `LEGACY_ONE_ASSET_R5_SUPERSEDED_NO_ACTIVE_PROGRAM_AUTHORITY`
- `ACTIVE_MODEL_REPOSITORY_DISSERTATION_CH5_TWO_ASSET_HANK`

Primary source/numerical authority:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Accepted MP2 markers are prerequisites:

- `MP2_SOURCE_FAITHFUL_MIGRATION_LABOR_PARITY_ACCEPTED`
- `MP2_AT_ONLY_CAPITAL_AND_RAH_PARITY_ACCEPTED`
- `MP2_SOURCE_FAITHFUL_FIRM_BLOCK_PARITY_ACCEPTED`
- `MP2_SOURCE_FAITHFUL_COMPOSITE_WAGE_PARITY_ACCEPTED`
- `MP2_TAYLOR_AND_FISCAL_DIAGNOSTIC_PARITY_ACCEPTED`
- `MP2_SOURCE_FAITHFUL_ONE_TURN_COMPONENT_PARITY_ACCEPTED`
- `MP2_NO_HOUSEHOLD_SOLVER_OR_LEGACY_RUNTIME_DEPENDENCY_ACCEPTED`

## 3. Live continuity

Expected execution-start parent / accepted MP2 implementation commit:

`ebf26b1167baefaf5468a80c16ea3f443131597a`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main` as a direct child of the accepted MP2 commit;
3. require clean worktree;
4. verify MP1/MP2 reports and MP1 frozen fixture/evaluator identities;
5. verify accepted standalone household oracle remains byte-identical;
6. verify no legacy `chapter5_model` runtime import exists in active production source;
7. verify MP2 production one-turn source has not changed before MP3 implementation.

If continuity fails, stop `BLOCKED`.

## 4. Protected MATLAB read-only source authority

Read only from:

`D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Mandatory source:

- `HANK_mp_1eq.m` — expected SHA-256 `ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF`

Also re-read only as needed to resolve state fields passed to/from the controller:

- `HANK_mp_1turn.m` — `D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF`
- `mpHANK_equilibrium_2000.m` — `26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5`
- `multi_prov_HANK_12sts.m` — `3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97`

Do not modify or execute MATLAB.

Before coding, create a source-line contract in the MP3 report covering every controller branch. In particular, source-read and freeze rather than infer:

- exact loop bounds and iteration counter semantics;
- exact initialization of `tKNratio` and any previous-output fields;
- exact definitions/indexing of `NKrationgap` and `Ytgap`;
- exact test for all household convergence flags;
- exact `ra` upper/lower-bound counting and final veto predicate;
- exact role of `maxwjt/minwjt` or corresponding wage-bound counts;
- exact convergence predicate and comparison operators (`<` versus `<=`);
- exact order of convergence testing relative to adaptive updates;
- exact `Yt/Yt0` update threshold and exact `Zt` assignment;
- exact high-`ra` versus low-`ra` `GovInv` multiplier direction, thresholds, and whether equality is included;
- exact `tKNratio` damping formula and timing;
- exact update of `Yt_1`, snapshots, or other previous-turn fields;
- exact failure/exception behavior when iteration limit is exhausted.

If any controller-critical branch cannot be established from source, stop `BLOCKED` or `OWNER_PROVENANCE_REQUIRED` as appropriate. Do not guess from the dissertation prose.

## 5. MP3 architecture boundary

The controller must remain an **object-ordered source-faithful map**, not a newly invented simultaneous residual vector.

Do not introduce a GE unknown vector, residual vector, Brent/Newton/fsolve/least-squares solver, Jacobian, or arbitrary vector ordering. Therefore the unresolved Owner checkpoint about vectorized update-map ordering is **not triggered** by this task.

Allowed production target:

- `src/ch5_two_asset_hank/multi_province/steady_state.py`

A bounded update to:

- `src/ch5_two_asset_hank/multi_province/__init__.py`

is allowed only to expose accepted MP3 public objects.

Do not modify MP2 production component arithmetic unless MP3 reveals a genuine accepted-contract contradiction; if so, stop non-PASS and report it for a successor adjudication task.

## 6. Household boundary — no household solver in MP3

MP3 validates controller semantics without a household scientific run.

The production controller must consume an explicit **pre-frozen per-turn household-output provider/sequence** or another equivalently explicit deterministic test boundary. It may call the accepted MP2 `run_source_faithful_one_turn` / `compose_one_turn` using those supplied outputs.

Requirements:

- no callback may invoke HJB/KFE/standalone HA;
- no production import of accepted household solver entry points is needed for MP3;
- test fixtures must make household convergence flags and household outer outputs explicit;
- all household outputs for a turn are treated as a complete batch before any outer state update, preserving MATLAB old-state simultaneity;
- the controller must stop fail-closed if a required next-turn batch is unavailable before the source termination condition is reached.

This test boundary is **not** the future MP4 oracle-backed 31-province integration.

## 7. Required controller semantics

### 7.1 State snapshots and update order

Freeze typed/immutable old-turn and new-turn state containers sufficient to reproduce source controller semantics.

At minimum preserve a clear distinction among:

- state entering a turn;
- complete MP2 one-turn result;
- convergence diagnostics computed from that result and source history;
- adaptive parameter/state updates for the next turn;
- damped reference objects such as `tKNratio`;
- prior-output objects such as `Yt_1` if source uses them.

Do not allow province `i+1` in the same turn to observe post-firm/post-adaptation state from province `i` if MATLAB does not.

### 7.2 Convergence diagnostics

Implement source-exact diagnostics, including:

- `NKrationgap`;
- `Ytgap`;
- total household convergence count/condition;
- upper/lower `ra` bound counts and mandatory convergence veto;
- wage-bound counts as diagnostics only if source treats them that way.

Return raw vectors/counts and the final predicate in the iteration record.

Do not replace the source test with a generic norm.

### 7.3 Adaptive `Zt` update

Implement the exact source branch based on the output/data discrepancy. The MP0 audit indicates a 1% trigger and the assignment of `Zt` from `Yt0`, `Kt`, `Lt`, and `alpha`, but MP3 must bind the exact formula and branch comparisons to source lines before implementation.

Expose whether each province was adjusted and its pre/post value.

### 7.4 Adaptive `GovInv` update

Implement the exact source return-bound heuristic. Source-read the exact branch thresholds and multiplier direction before coding.

Do not infer direction from economic intuition.

Expose adjustment action and pre/post `GovInv` for every province.

### 7.5 `tKNratio` damping

Preserve the literal source formula and timing. MP0 identified:

`tKNratio <- 0.6 * KNratio + 0.4 * tKNratio`

but MP3 must re-bind exact lines and confirm whether the update occurs every nonterminal turn or under a narrower condition.

### 7.6 Termination and failure

The source default outer maximum is expected to be `500` through `num.max3iter`; bind exact source provenance.

Production controls may expose the source maximum as an explicit immutable parameter so tiny tests can use a smaller authorized fixture maximum, but:

- source default must remain 500;
- changing the test maximum must be labeled fixture-only numerical control, not a new economic rule;
- convergence must return immediately according to source semantics;
- nonconvergence must reproduce source-equivalent failure classification without silently returning a successful result.

Do not implement automatic solver switching, damping redesign, tolerance loosening, or retry.

## 8. Independent tiny multi-turn validation fixtures

Create bounded, non-calibration fixtures under:

`tests/fixtures/multi_province/`

and an independent evaluator/reference under:

`validators/multi_province/`

The independent MP3 validator must not import production `steady_state.py`. Production code must not import `validators/` or `tests/`.

At minimum freeze the following asymmetric synthetic/source-formula scenarios:

### Fixture A — delayed convergence

A deterministic sequence requiring more than one turn, then satisfying the exact source convergence predicate.

Must demonstrate:

- correct iteration count;
- correct gap calculations;
- all household convergence flags required;
- no `ra` bound veto at accepted turn;
- exact source state/snapshot timing;
- exact `tKNratio` history.

### Fixture B — adaptive updates

A nonconverged turn that triggers, as source dictates:

- at least one `Zt` reset;
- at least one `GovInv` high/low-return branch;
- at least one province with no adjustment;
- damping/update bookkeeping.

Expected actions and pre/post values must be frozen independently from source formulas.

### Fixture C — convergence veto / failure

Cover at minimum:

- household convergence flag false despite small numeric gaps;
- `ra` at a source-forbidden bound despite small numeric gaps;
- max-iteration exhaustion with source-equivalent failure terminal.

A separate source-formula test should prove wage-bound counts do **not** veto convergence if the MATLAB predicate excludes them.

All fixtures must be labeled:

`NON_CALIBRATION_SYNTHETIC_OR_SOURCE_FORMULA_FIXTURE`

and must not use annual empirical data or derived calibration caches.

## 9. Validation rules

For each fixture compare production controller output to the independent validator for:

- iteration count and indices;
- raw `NKrationgap` vector;
- raw `Ytgap` vector;
- household convergence count/condition;
- `ra` bound counts;
- wage-bound diagnostic counts;
- convergence predicate;
- `Zt` adjustment actions and values;
- `GovInv` adjustment actions and values;
- `tKNratio` pre/post values;
- previous-output bookkeeping;
- termination reason;
- final state for PASS scenarios;
- failure classification for exhaustion scenarios.

Use exact equality for categorical/integer/boolean objects. For deterministic Python binary64 source-equivalent arithmetic, require exact equality where arithmetic order is identical. Any non-exact float comparison must use a bound frozen **before** the comparison and no wider than `rtol=1e-12, atol=1e-12`; report it field by field. No post-hoc tolerance changes.

## 10. Required negative tests

Tests must prove at minimum:

- generic residual-norm convergence replacement fails;
- `<=` substitution fails when source uses strict `<`;
- omitting household convergence condition fails;
- omitting `ra` boundary veto fails;
- adding wage-bound veto fails if source does not include it;
- wrong high/low `GovInv` multiplier direction fails;
- wrong `Zt` threshold or formula fails;
- wrong `tKNratio` damping weights/order fails;
- within-turn partial-state update fails;
- missing household batch before termination fails closed;
- max-iteration exhaustion cannot be reported as convergence;
- production `steady_state.py` does not import legacy `chapter5_model`, `validators`, or `tests`;
- controller does not import/call HJB, KFE, standalone HA, transition, dynamics, or IRF code;
- no Brent/Newton/fsolve/residual-vector solver exists in the MP3 production path.

## 11. Scientific/model execution budget

Forbidden scientific/model calls:

- MATLAB execution: `0`;
- modular HJB/KFE: `0/0`;
- standalone HA/HJB/KFE/aggregate: `0`;
- legacy R5 model: `0`;
- empirical GE / 31-province annual solve: `0`;
- AR1/shock response: `0`;
- transition/dynamics/IRF: `0/0/0`;
- Results: `0`.

Allowed execution:

- source-faithful MP2 one-turn arithmetic on bounded synthetic MP3 fixtures;
- MP3 manual controller iterations on those fixtures only;
- independent fixture evaluator;
- focused tests/import/compile/static checks.

No annual workbook/cache data may be executed.

## 12. Allowed repository changes

On PASS, changed paths are limited to:

- `src/ch5_two_asset_hank/multi_province/steady_state.py`;
- bounded `src/ch5_two_asset_hank/multi_province/__init__.py` update;
- MP3 independent validator(s) under `validators/multi_province/`;
- MP3 tiny fixtures under `tests/fixtures/multi_province/`;
- MP3 focused tests under `tests/`;
- one MP3 report under `docs/`.

Do not modify:

- accepted MP1 fixture/evaluator/contracts;
- accepted MP2 component/one-turn arithmetic unless a contradiction forces non-PASS;
- accepted household/HJB/KFE/oracle source;
- protected MATLAB;
- historical R5 repository;
- CURRENT roadmap;
- raw `.mat`/`.xlsx`/calibration cache;
- shock/dynamic/Results paths.

## 13. Required report

Write:

`docs/CH5_TWO_ASSET_HANK_MP3_SOURCE_FAITHFUL_MANUAL_UPDATE_MAP_AND_FIXED_POINT_SEMANTICS_IMPLEMENTATION_AND_TINY_FIXTURE_VALIDATION_REPORT.md`

Include at minimum:

1. terminal classification;
2. live start/final pre-publication authority;
3. MP2 prerequisite identities;
4. source hashes and exact controller line map;
5. exact source pseudocode/update order;
6. files written;
7. public API and state types;
8. all fixture hashes/classifications;
9. independent-validator identities;
10. full fixture comparison tables;
11. exact-vs-bound classification;
12. convergence predicate proof;
13. `Zt` rule proof;
14. `GovInv` rule proof;
15. `tKNratio` damping proof;
16. state/snapshot timing proof;
17. failure semantics proof;
18. negative tests;
19. no-household/no-GE/no-legacy/no-dynamics proof;
20. scientific/model call ledger;
21. material mismatch list;
22. unresolved scientific residual list;
23. source/environment failure list;
24. forbidden-operation check;
25. tests/static checks;
26. git closeout;
27. recommended next gate.

## 14. Terminals and acceptance markers

PASS terminal:

`MP3_SOURCE_FAITHFUL_MANUAL_UPDATE_MAP_AND_FIXED_POINT_SEMANTICS_IMPLEMENTATION_AND_TINY_FIXTURE_VALIDATION_PASS`

On PASS freeze:

- `MP3_SOURCE_ORDERED_MANUAL_UPDATE_MAP_ACCEPTED`
- `MP3_SOURCE_CONVERGENCE_PREDICATE_ACCEPTED`
- `MP3_SOURCE_ZT_ADAPTIVE_UPDATE_ACCEPTED`
- `MP3_SOURCE_GOVINV_ADAPTIVE_UPDATE_ACCEPTED`
- `MP3_SOURCE_TKNRATIO_DAMPING_ACCEPTED`
- `MP3_SOURCE_MAX_ITERATION_FAILURE_SEMANTICS_ACCEPTED`
- `MP3_MANUAL_UPDATE_MAP_AND_CONVERGENCE_PARITY_ACCEPTED`
- `MP3_NO_HOUSEHOLD_SOLVER_GE_OR_LEGACY_RUNTIME_DEPENDENCY_ACCEPTED`

MATERIAL terminal:

`MP3_SOURCE_FAITHFUL_MANUAL_UPDATE_MAP_AND_FIXED_POINT_SEMANTICS_IMPLEMENTATION_AND_TINY_FIXTURE_VALIDATION_MATERIAL_MISMATCH`

BLOCKED terminal:

`MP3_SOURCE_FAITHFUL_MANUAL_UPDATE_MAP_AND_FIXED_POINT_SEMANTICS_IMPLEMENTATION_AND_TINY_FIXTURE_VALIDATION_BLOCKED`

OWNER provenance terminal, only if a source-critical ambiguity genuinely requires Owner adjudication:

`MP3_SOURCE_FAITHFUL_MANUAL_UPDATE_MAP_OWNER_PROVENANCE_REQUIRED`

Do not use Owner provenance merely because MP4 baseline/cache/year authority is unresolved; those remain later blockers.

## 15. Repository closeout

On PASS:

- explicit-path staging only;
- one commit;
- one non-force push;
- GitHub read-back every changed path;
- require `HEAD == origin/main`;
- require ahead/behind `0/0`;
- require clean worktree.

On non-PASS, publish only the task-authorized failure/adjudication report unless an already authorized immutable fixture artifact is necessary to document the contradiction; restore unaccepted production/test changes before closeout.

## 16. Stop boundary and successor

MP3 must stop after tiny-fixture manual update-map/fixed-point semantics acceptance.

Do **not**:

- invoke the two-asset household solver;
- choose a baseline year;
- approve a calibration cache;
- run the 31-province annual steady state;
- implement annual orchestration;
- implement shocks/AR1;
- run named MATLAB IRFs;
- implement genuine transition dynamics;
- write Results.

If and only if MP3 PASSes, recommend **MP4 provenance-resolution / annual-route preparation** as the next stage. Because MP4 is the first stage blocked by Owner decisions on baseline-vs-multi-year contract and calibration-cache authority, do not automatically execute a full annual solve without a separate Owner provenance decision and a new task.