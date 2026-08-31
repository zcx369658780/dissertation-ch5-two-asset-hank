# CH5_TWO_ASSET_HANK_MP4B_NONCONVERGED_HJB_POSTLOOP_SOURCE_SEMANTICS_ADJUDICATION_AND_ZERO_SCIENCE_VALIDATION_ADAPTER_REPAIR

Date: 2026-08-31

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / source-semantics auditor / validation-adapter remediator

Owner: final scientific authority

## 1. Purpose

Resolve the first material mismatch observed in the corrected-calendar-2009 Python stationary route **without any stationary, household, HJB, KFE, MATLAB, MP2, or MP3 scientific rerun**.

Accepted predecessor terminal:

`MP4B_PYTHON_ONLY_CORRECTED_CALENDAR2009_STATIONARY_PARITY_AGAINST_PRESERVED_MATLAB_MATERIAL_MISMATCH`

Observed failure:

- Python completed outer turn 1;
- on outer turn 2, Beijing/Tianjin/Hebei households completed;
- Shanxi was the 35th attempted household;
- current validation route raised `RuntimeError: MATLAB-faithful HJB did not converge`;
- no qualified stationary comparator ran;
- MATLAB preserved baseline remained completed and was not rerun.

This task must adjudicate whether the **handling of a nonconverged inner HJB** differs from protected MATLAB source semantics and, only if confirmed, repair the Python **validation-only multi-province adapter/driver plumbing** so that a future separately authorized stationary execution can follow the MATLAB post-loop household semantics.

This task does not authorize the future stationary execution itself.

## 2. Primary authority

Retain:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

Retain accepted raw-`Vb` household authority:

- `economics.py` SHA-256 `F2B67D393D7495A83281C259F6D9CC5F8AFF18B3C4ABDEB7A07F354582DEF2D1`
- `matlab_faithful_policy.py` SHA-256 `ECF56FAA7E87A0F5156E5866F1873556D6603E98AA33C8E41C400FD016C75CDC`
- standalone export SHA-256 `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3`

Do not modify those files.

## 3. Controlling authority to read

Read in full before mutation:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `project_rules/PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md`
- `project_rules/PROJECT_RULE_MATLAB_MODEL_DIAGNOSTIC_GATES_CURRENT.md`
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_FULL_HJB_STRUCTURAL_DECOMPOSITION_AND_STATIONARY_OPERATOR_DIAGNOSTIC_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MP4B_BEIJING_FIRST_TURN_HOUSEHOLD_PARITY_REVALIDATION_AFTER_RAW_VB_REPAIR_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MP4B_PYTHON_ONLY_CORRECTED_CALENDAR2009_STATIONARY_EXECUTION_AGAINST_PRESERVED_MATLAB_BASELINE_REPORT.md`
- `validators/multi_province/mp4b_python_empirical.py`
- `exports/matlab_faithful_two_asset_ha.py`
- accepted MP2/MP3 multi-province reports and modules relevant to convergence-flag propagation.

## 4. Live continuity

Required execution-start predecessor:

`e31a2ac4ffb487be8e5883cc71f0947bf6b7cdbf`

At start:

1. fresh-fetch `origin/main`;
2. confirm this exact task is live on `main` as the direct child of `e31a2ac4ffb487be8e5883cc71f0947bf6b7cdbf`;
3. require clean worktree;
4. verify repository identity and controlling rules;
5. verify all accepted production/export hashes above;
6. verify the prior report and current validation entry identities;
7. verify no historical R5 / `chapter5_model` runtime dependency.

Any identity failure => stop before mutation.

## 5. Protected MATLAB source adjudication — read only

Read the following protected MATLAB files from the exact accepted logical/physical root pair under the local-file safety rule. Do not execute them and do not modify them.

Required accepted SHA-256 identities:

- `HANK_2ASSETS_HJB.m`: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK_mp_1turn.m`: `D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF`
- `HANK_mp_1eq.m`: `ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF`

Freeze a line-level source-semantics map covering at minimum:

### 5.1 `HANK_2ASSETS_HJB.m`

Determine exactly what happens when the HJB loop reaches `maxit` without satisfying `crit`.

The existing accepted forensic report indicates the source:

- initializes `convergent=0`;
- sets it to one only when the value-change criterion passes;
- does **not** return or throw solely because `convergent` remains false;
- rebuilds final policies/operator after the loop;
- executes stationary KFE/density logic after the loop;
- computes/publishes household aggregates and the convergence flag.

Reverify all of this against the protected source itself. Record exact line ranges / source statements and SHA identity.

### 5.2 `HANK_mp_1turn.m`

Determine whether a province-level `convergent=false` result is collected into the 31-province household batch or causes the entire turn to abort.

Freeze the exact source behavior.

### 5.3 `HANK_mp_1eq.m`

Determine where household convergence flags enter the outer fixed-point acceptance rule and whether the source continues outer iterations when one household flag is false.

Freeze the exact source behavior.

If the protected source does **not** support a single unambiguous post-loop/outer-loop contract, terminate BLOCKED and do not implement an adapter.

## 6. Python semantic adjudication

Read the accepted standalone and validation entry without executing model science.

Current accepted standalone composition contains:

- `solve_matlab_faithful_hjb(...)` returning an HJB result with `converged` and `convergence_statistic` even when false;
- `solve_household_steady_state(...)` raising `RuntimeError("MATLAB-faithful HJB did not converge")` before KFE and aggregation when `hjb.converged` is false.

Current `validators/multi_province/mp4b_python_empirical.py` calls `solve_household_steady_state(...)` inside each province loop, so a false HJB convergence flag aborts the whole multi-province turn before KFE/aggregates are produced for that province.

If Section 5 confirms that protected MATLAB instead completes post-loop policies/KFE/aggregates and returns a false convergence flag to the outer controller, establish:

`MP4B_PYTHON_STATIONARY_ABORT_ON_HJB_NONCONVERGENCE_SOURCE_SEMANTICS_MISMATCH_CONFIRMED`

The scientific classification is then:

`PYTHON_IMPLEMENTATION_ERROR__MULTI_PROVINCE_DRIVER_ABORTS_BEFORE_MATLAB_SOURCE_POSTLOOP_KFE_AND_AGGREGATES`

Do **not** claim that the raw HJB arithmetic itself is the first source mismatch unless separately supported. The turn-2 Shanxi HJB may still be numerically nonconverged under the same 100-iteration source rule; the adjudicated mismatch here is the handling of that flag in the multi-province route.

## 7. Zero-science validation adapter repair

Only if Sections 5-6 pass, implement the smallest validation-only adapter under `validators/multi_province/`.

Preferred file:

`validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py`

Its semantics must be composition-only and must use the already accepted public standalone primitives without changing them:

1. call `solve_matlab_faithful_hjb(...)`;
2. regardless of `hjb.converged`, use its `post_convergence_operator` to call `solve_matlab_faithful_stationary_kfe(...)`;
3. compute aggregates using `aggregate_stationary_household(...)`;
4. return the existing `HouseholdSteadyStateResult`-compatible object or an explicitly documented validation wrapper carrying the same HJB/KFE/aggregate objects;
5. preserve `hjb.converged`, `hjb.iterations`, and `hjb.convergence_statistic` exactly;
6. introduce no new tolerance, retry, extra HJB iteration, fallback, clipping, alternative KFE, alternate aggregation, or formula;
7. perform no work on import.

Then modify only the validation multi-province entry `validators/multi_province/mp4b_python_empirical.py` to use this adapter for its province household call.

The driver must continue to propagate the household convergence flags into `PreFrozenHouseholdOutputBatch` and the accepted MP3/outer convergence logic. It must not silently coerce a false flag to true.

Add diagnostic fields sufficient for a future run to persist each household's:

- HJB `converged`;
- HJB `iterations`;
- HJB `convergence_statistic`.

Do not add a new economic state or alter MP2/MP3 input semantics.

## 8. Zero-model tests only

This task has **zero scientific/model execution budget**.

Tests must use static analysis and/or mocks/stubs, not actual HJB/KFE/stationary solves.

Required focused tests:

1. protected-source semantic-map schema/identity test;
2. adapter nonconverged-HJB control-flow test using a stub HJB result with `converged=false` proving KFE and aggregation are still invoked exactly once;
3. adapter converged-HJB control-flow test proving the same composition path is used;
4. exact propagation of `converged`, `iterations`, and `convergence_statistic`;
5. no retry / no second HJB call;
6. validation driver uses the new source-postloop adapter rather than `solve_household_steady_state`;
7. no `chapter5_model` / historical R5 runtime import;
8. no production/export mutation;
9. no change to accepted MP2/MP3 arithmetic;
10. import of the adapter and validation entry performs zero model calls.

Also require:

- `py_compile` for touched Python validation/test files;
- focused pytest count reported exactly;
- `git diff --check` PASS.

## 9. Scientific/model call ledger — must remain zero

All counts must be exactly zero:

- Python stationary top-level;
- Python household scientific solve;
- Python HJB;
- Python KFE;
- Python household aggregation on real model inputs;
- MATLAB stationary;
- MATLAB household/HJB/KFE;
- MP2/MP3 scientific execution;
- second province scientific replay;
- turn-2 Shanxi HJB replay;
- comparator scientific execution;
- any other year / annual batch;
- shocks / AR1 / transition / dynamics / IRF;
- historical R5;
- Results.

Do not consume an observability HJB replay in this task. The accepted source audit is sufficient to adjudicate the abort semantic before any such replay.

## 10. Allowed repository changes

Allowed only:

- one protected-source semantic-map JSON/MD under `validators/multi_province/`;
- one validation-only post-loop household adapter under `validators/multi_province/`;
- bounded modification of `validators/multi_province/mp4b_python_empirical.py` to route household calls through that adapter and expose nonconvergence diagnostics;
- focused zero-model tests;
- bounded CURRENT roadmap status update;
- one report:
  `docs/CH5_TWO_ASSET_HANK_MP4B_NONCONVERGED_HJB_POSTLOOP_SOURCE_SEMANTICS_ADJUDICATION_AND_ZERO_SCIENCE_VALIDATION_ADAPTER_REPAIR_REPORT.md`.

Do not modify:

- `src/ch5_two_asset_hank/economics.py`;
- `src/ch5_two_asset_hank/matlab_faithful_policy.py`;
- `exports/matlab_faithful_two_asset_ha.py`;
- accepted HJB/operator/KFE production modules;
- MP2/MP3 scientific modules;
- protected MATLAB;
- canonical 2009 input/data/cache/workbooks;
- accepted Beijing source map/comparator contract;
- controlling project rules;
- historical R5.

## 11. Acceptance

PASS terminal:

`MP4B_NONCONVERGED_HJB_POSTLOOP_SOURCE_SEMANTICS_ADJUDICATION_AND_ZERO_SCIENCE_VALIDATION_ADAPTER_REPAIR_PASS`

On PASS establish all:

- `MP4B_MATLAB_HJB_NONCONVERGENCE_POSTLOOP_KFE_AGGREGATE_SEMANTICS_FROZEN`
- `MP4B_PYTHON_STATIONARY_ABORT_ON_HJB_NONCONVERGENCE_SOURCE_SEMANTICS_MISMATCH_CONFIRMED`
- `MP4B_PYTHON_MULTI_PROVINCE_SOURCE_POSTLOOP_HOUSEHOLD_ADAPTER_STATIC_PASS`

BLOCKED terminal:

`MP4B_NONCONVERGED_HJB_POSTLOOP_SOURCE_SEMANTICS_ADJUDICATION_AND_ZERO_SCIENCE_VALIDATION_ADAPTER_REPAIR_BLOCKED`

Use BLOCKED if protected source semantics are ambiguous, identities fail, or a faithful repair requires production/export/scientific-arithmetic mutation.

No stationary parity acceptance marker may be established in this task.

## 12. Required report

Include at minimum:

1. terminal verdict;
2. live continuity;
3. protected MATLAB file paths/SHA and exact source-semantic line map;
4. explicit answer: does MATLAB continue post-loop KFE/aggregates when HJB `convergent=false`?;
5. explicit answer: does `HANK_mp_1turn` abort on one false household flag?;
6. explicit answer: how does `HANK_mp_1eq` use household convergence flags?;
7. Python current-vs-source semantic comparison;
8. accepted scientific classification or unresolved status;
9. adapter path/SHA and exact composition contract;
10. proof no retries/tolerance/formula changes were added;
11. focused test count;
12. `py_compile` and `git diff --check`;
13. complete zero scientific/model call ledger;
14. production/export mutation count;
15. changed paths;
16. forbidden-operation audit;
17. Git commit/push/read-back closeout;
18. exactly one recommended next gate.

## 13. Next-stage boundary

On PASS, recommend exactly one next gate:

**one reauthorized Python-only corrected-calendar-2009 stationary invocation using the source-postloop household adapter, compared against the same immutable MATLAB baseline; MATLAB rerun remains zero.**

That successor must use a fresh no-overwrite Python run root and a separately frozen one-shot budget. It must not automatically proceed to another year, annual batch, shock/AR1, transition, dynamics, IRF, R5, or Results.

On BLOCKED, recommend only the smallest source/adapter ambiguity-resolution gate.

## 14. Closeout

Explicit-path staging only. One execution commit. One non-force push. GitHub read-back every changed path. Require final:

- `HEAD == origin/main`;
- ahead/behind `0/0`;
- clean worktree;
- forbidden-operation audit PASS.
