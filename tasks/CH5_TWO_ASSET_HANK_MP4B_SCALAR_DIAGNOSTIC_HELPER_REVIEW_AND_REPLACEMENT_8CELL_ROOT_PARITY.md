# CH5_TWO_ASSET_HANK_MP4B_SCALAR_DIAGNOSTIC_HELPER_REVIEW_AND_REPLACEMENT_8CELL_ROOT_PARITY

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / validation-helper reviewer / scalar-root parity executor

Owner: final scientific authority

## 1. Purpose

Close only the unresolved eight-cell initial-labor root-parity gate left by the prior blocked task.

The prior terminal was:

`MP4B_INITIAL_LABOR_SOURCE_DOMAIN_REPAIR_BLOCKED`

Prior report / implementation commit:

`9fa649c80420ae0f95aaddb30234e85314c980c5`

The prior task already established:

- `MP4B_INITIAL_LABOR_MATLAB_SOURCE_SEMANTICS_FROZEN`;
- `MP4B_PYTHON_INITIAL_LABOR_ZERO_ENDPOINT_IS_NONSOURCE_DOMAIN_ERROR_CONFIRMED`;
- `MP4B_INITIAL_LABOR_SOURCE_DOMAIN_REPAIR_STATIC_REVIEW_PASS`;
- a source-`x0`-anchored Python admissible-domain bracket repair;
- eight predeclared frozen cells and their Python roots.

The only unresolved gate is MATLAB-vs-Python scalar root parity because the single prior validation-only MATLAB scalar diagnostic failed before persisting its first `fzero` result.

This task MUST remain non-stationary and non-model. It does not authorize Python stationary execution, MATLAB stationary execution, HJB, KFE, multi-province execution, shocks, transition, dynamics, IRF, or Results.

## 2. Controlling authority

Read in full and obey:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `project_rules/PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md`
- `project_rules/PROJECT_RULE_MATLAB_MODEL_DIAGNOSTIC_GATES_CURRENT.md`
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`
- all Owner MP4 decision/adjudication documents;
- all prior MP4B reports/tasks;
- `docs/CH5_TWO_ASSET_HANK_MP4B_PYTHON_INITIAL_LABOR_SOURCE_FZERO_DOMAIN_REPAIR_AND_PYTHON_ONLY_CALENDAR2009_REEXECUTION_REPORT.md`;
- current `validators/multi_province/mp4b_python_empirical.py`;
- current `validators/multi_province/matlab/mp4b_initial_labor_scalar_diagnostic.m`.

Preserve:

- corrected calendar-2009 identity and canonical SHA `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`;
- protected `HANK_2ASSETS_HJB.m` SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`;
- protected `lab_solve2.m` SHA-256 `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`;
- frozen MATLAB source labor equation, `x0`, `c0`, and `v02` semantics;
- Python source-domain repair from commit `9fa649c8...` unchanged;
- preserved completed MATLAB stationary run unchanged and not rerun.

Primary reconstruction authority remains:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

## 3. Live continuity

Expected execution-start parent:

`9fa649c80420ae0f95aaddb30234e85314c980c5`

At start:

1. fresh-fetch `origin/main`;
2. confirm this exact task is live on `main` as a direct child of the prior blocker commit;
3. require clean worktree;
4. verify controlling rule blobs and protected source hashes unchanged;
5. verify current Python repair and scalar diagnostic helper identities;
6. verify accepted standalone oracle / MP2 / MP3 / stationary-runtime identities unchanged;
7. verify no historical `chapter5_model` / R5 runtime dependency.

If continuity fails, stop before any MATLAB diagnostic invocation.

## 4. Static review of the corrected scalar diagnostic helper

The prior invocation failed on dissimilar-structure assignment. The current helper now contains an explicit typed row template and `repmat(template,1,8)` before assignments.

Independently review the complete helper before consuming the replacement invocation.

Mandatory checks:

1. exactly eight rows are preallocated with an identical field set and field order;
2. each populated row has exactly the same fields as the template;
3. the eight frozen cells remain exactly the Cartesian product:
   - `b={-2, 4/19}`;
   - `a={0,10}`;
   - `z={0.8,1.3}`;
4. source parameters remain exactly `alphac=1`, `alphal=1`, `tau=.05`, `w=20`, `frisch_l=.2`, `ga=2`, `Tt=.1`, `rb=.02`, `rb_gap=.07`, `rah=.09`, `a_max=10` as frozen by the prior source audit;
5. source `x0`, `tempMat`, `lab_solve2`, `fzero`, `optimset('Display','off')`, and `root_base` formulas remain unchanged;
6. no model/HJB/KFE/multi-province function is called;
7. protected `lab_solve2.m` hash is verified before `fzero`;
8. output is no-overwrite and R2022b-compatible.

### 4.1 Known persistence-compatibility audit

The current helper uses `fopen(output_json,'x')`. Earlier MP4B infrastructure evidence already observed that exclusive-open mode as incompatible in the local MATLAB R2022b environment.

Therefore, before the sole replacement invocation, explicitly audit and, if still present, repair the output-creation path so the helper cannot reach all eight roots and then fail on a known R2022b-incompatible persistence primitive.

The repair MUST remain no-overwrite. Preferred bounded design:

- caller supplies a fresh, already-created timestamped diagnostic directory;
- output JSON path must not exist;
- atomically reserve/create that exact new file with an R2022b-compatible mechanism (for example Java `java.io.File(...).createNewFile()`), failing closed if it already exists;
- then open only that newly reserved file for writing;
- never truncate or overwrite a pre-existing file.

Do not weaken no-overwrite merely to avoid `fopen('x')`.

No other helper behavior may change unless a second validation-only infrastructure defect is proven statically before invocation.

Required marker:

`MP4B_INITIAL_LABOR_SCALAR_DIAGNOSTIC_HELPER_STATIC_REVIEW_PASS`

If this marker is not established, consume zero MATLAB scalar diagnostic calls.

## 5. Frozen Python scalar roots

Before MATLAB execution, recompute the eight Python roots using the already repaired `_source_labor_root` logic only. This is scalar validation arithmetic, not household/HJB/KFE/model execution.

The prior accepted evidence recorded:

| b | a | z | Python root |
|---:|---:|---:|---:|
| -2 | 0 | .8 | .6792542039265690 |
| 4/19 | 0 | .8 | .6757964176493583 |
| -2 | 10 | .8 | .6792832786668417 |
| 4/19 | 10 | .8 | .6758251235775711 |
| -2 | 0 | 1.3 | .6333079596259149 |
| 4/19 | 0 | 1.3 | .6311790863732587 |
| -2 | 10 | 1.3 | .6333258210921237 |
| 4/19 | 10 | 1.3 | .6311967980580924 |

Require recomputation to reproduce these prior values within the already frozen scalar root contract; if the current repaired Python code does not reproduce them, stop BLOCKED before MATLAB invocation.

Persist a small text/JSON Python scalar-side manifest with cell identities, source parameters, root, bracket, residual, current Python repair file hash, and scientific model calls `0`.

## 6. Exactly one replacement MATLAB scalar diagnostic invocation

Only after Section 4 static review and Section 5 Python scalar revalidation PASS, authorize exactly one replacement validation-only MATLAB scalar diagnostic top-level invocation.

Allowed calls:

- current validation helper `mp4b_initial_labor_scalar_diagnostic.m`;
- protected read-only `lab_solve2.m`;
- MATLAB built-in `fzero`;
- at most the exact eight frozen cells.

Forbidden within this invocation:

- `HANK_2ASSETS_HJB`;
- any KFE;
- `HANK_mp_1turn`;
- `HANK_mp_1eq`;
- `mpHANK_equilibrium_2000`;
- `multi_prov_HANK_12sts`;
- any multi-province stationary/model route.

Use a new timestamped no-overwrite root distinct from the failed prior root.

Persist one complete JSON manifest containing all eight MATLAB roots and source diagnostics. Hash the manifest after completion.

No second scalar diagnostic invocation is authorized.

## 7. Frozen root-parity contract

Apply the already frozen rule, with no post-hoc loosening:

For all eight cells:

- MATLAB `exitflag > 0`;
- MATLAB and Python roots finite and real;
- MATLAB source residual magnitude `<= 1e-10`;
- Python source residual magnitude `<= 1e-10`;
- MATLAB `root_base = B*l0 + tempMat > 0`;
- Python repaired bracket and root remain strictly inside the real domain;
- absolute root difference
  `<= 1e-10 * max(1,abs(l_matlab),abs(l_python))`.

Also compare `b,a,z,Rb,raah,tempMat,B,x0` exactly/source-locally for each cell.

On complete PASS establish:

`MP4B_INITIAL_LABOR_PYTHON_MATLAB_FROZEN_CELL_ROOT_PARITY_PASS`

If any cell fails, stop without Python stationary execution and report the first failing cell/object.

## 8. Call budget

This task is validation-only.

- MATLAB scalar diagnostic: maximum `1` top-level invocation, <=8 cells.
- MATLAB stationary / HJB / KFE / multi-province: `0`.
- Python stationary: `0`.
- Python household / HJB / KFE: `0`.
- MP2/MP3 empirical execution: `0`.
- wrong-year MATLAB: `0`.
- 2010-2023 batch: `0`.
- shocks / transition / dynamics / IRF: `0`.
- legacy R5: `0`.
- Results: `0`.

Do not continue to fresh presolver or Python stationary in this task even if eight-cell root parity passes.

## 9. Allowed repository changes

Allowed only:

- bounded validation-infrastructure correction to `validators/multi_province/matlab/mp4b_initial_labor_scalar_diagnostic.m` if required by the static review, including the known R2022b-safe no-overwrite persistence repair;
- focused validation-only test(s) for template compatibility / no-overwrite / forbidden call scanning;
- one task report;
- bounded CURRENT-roadmap status update.

Do not modify:

- `validators/multi_province/mp4b_python_empirical.py` scientific/root logic;
- accepted standalone/modular household code;
- MP2;
- MP3;
- `stationary_runtime.py`;
- protected MATLAB;
- canonical input/data/cache;
- historical R5;
- controlling rules.

## 10. Required report

Write:

`docs/CH5_TWO_ASSET_HANK_MP4B_SCALAR_DIAGNOSTIC_HELPER_REVIEW_AND_REPLACEMENT_8CELL_ROOT_PARITY_REPORT.md`

Include:

1. terminal verdict;
2. live continuity;
3. prior failed diagnostic identity and call ledger;
4. complete static helper review;
5. exact structure-template proof;
6. R2022b persistence compatibility audit and exact repair if needed;
7. helper hash before/after;
8. Python scalar-side manifest path/hash and eight roots;
9. replacement MATLAB diagnostic root and manifest SHA;
10. eight-cell MATLAB/Python table with `x0`, roots, residuals, root-base and exitflags;
11. exact/within-contract parity result per cell;
12. `MP4B_INITIAL_LABOR_PYTHON_MATLAB_FROZEN_CELL_ROOT_PARITY_PASS` status;
13. full zero-model call ledger;
14. tests/checks;
15. forbidden-operation check;
16. Git closeout;
17. exactly one recommended next gate.

## 11. Terminals

PASS:

`MP4B_INITIAL_LABOR_REPLACEMENT_8CELL_SCALAR_ROOT_PARITY_PASS`

PASS requires the frozen eight-cell root parity marker.

BLOCKED / validation-infrastructure failure:

`MP4B_INITIAL_LABOR_REPLACEMENT_8CELL_SCALAR_ROOT_PARITY_BLOCKED`

Scientific/source scalar mismatch:

`MP4B_INITIAL_LABOR_REPLACEMENT_8CELL_SCALAR_ROOT_PARITY_MATERIAL_MISMATCH`

No terminal authorizes stationary execution.

## 12. Next-stage boundary

On PASS recommend exactly one next gate:

**fresh Python direct-script/bootstrap smoke + fresh calendar-2009 presolver equality + one Python-only stationary invocation against the preserved completed MATLAB run; MATLAB stationary remains zero.**

On BLOCKED/MATERIAL recommend exactly one bounded successor addressing only the first localized scalar diagnostic/root-parity cause.

Do not publish or execute MP5, shocks, or 2010-2023 batch from this task.

## 13. Closeout

Explicit-path staging only. One execution commit. One non-force push. GitHub read-back every changed path. Require `HEAD == origin/main`, ahead/behind `0/0`, and clean worktree.
