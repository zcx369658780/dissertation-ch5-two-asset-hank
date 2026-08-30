# CH5_TWO_ASSET_HANK_MP4B_MATLAB_FILENAME_CONCATENATION_REPAIR_PATH_SMOKE_AND_FRESH_PRESOLVER_REVALIDATION

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / MATLAB validation-helper repairer / non-scientific smoke executor

Owner: final scientific authority

## 1. Purpose

Repair the MATLAB validation-helper filename-concatenation defect that blocked the non-scientific logical/physical path smoke, complete that smoke, and then re-establish the full calendar-2009 presolver same-input identity.

This task is deliberately **non-scientific**. It does not authorize any MATLAB or Python stationary/model execution.

Prior terminal:

`MP4B_PATH_EQUIVALENCE_REPAIR_AND_CALENDAR2009_STATIONARY_PARITY_BLOCKED`

Prior first divergence:

`NONSCIENTIFIC_PATH_SMOKE_FILENAME_CONCATENATION`

Prior root cause:

`VALIDATION_HELPER_IMPLEMENTATION_ERROR__MATLAB_CHAR_PLUS_FILENAME_SUFFIX`

Prior report commit:

`60528127890a862d5c92ef4e7384a97e2ce1fe7f`

The prior task consumed zero scientific calls. Scientific budgets remain closed in this task even if all non-scientific gates pass.

## 2. Controlling authority

Read in full and obey:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `project_rules/PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md`
- `project_rules/PROJECT_RULE_MATLAB_MODEL_DIAGNOSTIC_GATES_CURRENT.md`
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`
- all Owner MP4 decision/adjudication documents;
- accepted MP4A2 report;
- all prior MP4B reports and task authorities, especially the path-equivalence report at commit `60528127890a862d5c92ef4e7384a97e2ce1fe7f`.

Preserve:

- corrected calendar-2009 identity and canonical SHA `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`;
- `SOURCE_BINDING_AUDIT_COMPLETE__N_PROV_IS_ONLY_MISSING_REQUIRED_BINDING`;
- source-faithful `global N_prov; N_prov=31;` binding;
- finite verified logical/physical protected-root guard design;
- protected MATLAB read-only status;
- accepted household/oracle, MP2, MP3, MP4A2 annual contracts.

## 3. Live continuity

Expected execution-start parent:

`60528127890a862d5c92ef4e7384a97e2ce1fe7f`

At start:

1. fresh-fetch `origin/main`;
2. confirm this exact task is live as a direct child of the prior blocker commit;
3. require clean worktree;
4. verify controlling rule blobs and protected-source hashes unchanged;
5. verify accepted household/oracle, MP2, MP3, annual binding, stationary runtime and current MATLAB validation helper identities;
6. verify no historical `chapter5_model` runtime dependency.

If continuity fails, stop BLOCKED.

## 4. Mandatory bounded defect audit before repair

The observed failing expression in `validators/multi_province/matlab/mp4b_path_equivalence_smoke.m` is:

```matlab
helpers{i}+'.m'
```

For a cell-contained char vector, `+` performs numeric array addition rather than filename concatenation.

Before editing, statically search **all MP4B validation MATLAB helpers** under `validators/multi_province/matlab/` for the same or equivalent char-plus filename-suffix pattern.

The current scientific wrapper is known to contain the same construction in its helper guard:

```matlab
required_helpers{helper_index}+'.m'
```

Therefore a PASS task must not repair only the smoke and leave the same latent defect in the scientific wrapper.

Required audit output:

- exact affected file/line list;
- confirmation whether any other `char + '.m'`, `char + suffix`, or equivalent unsafe concatenation exists in the active MP4B validation chain;
- classification `MP4B_FILENAME_CONCATENATION_DEFECT_SCOPE_COMPLETE` before execution.

Do not broaden into unrelated MATLAB refactoring.

## 5. Authorized repair

Repair only affected validation-helper string construction under `validators/multi_province/matlab/`.

Use an R2022b-safe explicit filename construction, for example one of:

```matlab
[helpers{i} '.m']
```

or

```matlab
string(helpers{i}) + ".m"
```

with downstream type handling kept explicit.

Requirements:

- identical helper names and exact logical/physical root semantics;
- preserve finite allowed-root guard;
- preserve `N_prov=31` binding;
- preserve all source hashes, calendar/index values, numerical/model formulas and no-overwrite behavior;
- do not modify protected MATLAB;
- do not modify accepted scientific Python arithmetic.

Add focused tests/static assertions proving the active smoke **and the scientific wrapper** no longer contain unsafe cell-char plus suffix expressions.

## 6. Static review before smoke

Before executing the smoke:

- MATLAB `checkcode`/syntax check every changed validation `.m` file;
- static scan for remaining unsafe filename concatenation in the active MP4B helper chain;
- verify repair diff changes only validation filename/path construction and necessary tests;
- verify protected source hashes unchanged;
- verify logical C junction -> physical D target evidence unchanged;
- verify exact finite allowed roots unchanged;
- verify `N_prov=31` unchanged;
- verify fresh no-overwrite smoke root and sufficient free space.

Required marker:

`MP4B_FILENAME_CONCATENATION_REPAIR_STATIC_REVIEW_PASS`

If absent, stop before smoke.

## 7. Non-scientific path-equivalence smoke

Run the repaired `mp4b_path_equivalence_smoke` exactly once on a fresh timestamped no-overwrite root.

This smoke remains infrastructure-only. It MUST NOT invoke:

- `mpHANK_equilibrium_2000`;
- `HANK_mp_1eq`;
- `HANK_mp_1turn`;
- `HANK_2ASSETS_HJB`;
- any HJB/KFE/model solver.

It must establish and persist:

`MP4B_LOGICAL_PHYSICAL_PATH_EQUIVALENCE_SMOKE_PASS`

including:

- logical protected root;
- physical protected root;
- verified junction relation;
- `N_prov=31`;
- exact required helper list;
- each `which` resolution;
- finite-root membership result;
- smoke manifest SHA-256;
- scientific model call count `0`.

If the smoke fails, stop BLOCKED. Do not repair and rerun within this task.

## 8. Fresh presolver revalidation after smoke PASS

Only after the smoke PASS, re-establish the complete prior presolver manifest equality contract and require:

`MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_PASS`

Frozen identity remains:

- `calendar_year=2009`;
- `analysis_index=1`;
- workbook numeric row `10` / physical Excel row `11`;
- `data_MAT_index=1`;
- output year `2009`;
- regression key `10`;
- fixed-2020 `IND_Zt` as numerical initialization anchor only;
- canonical SHA `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`.

Persist fresh MATLAB/Python presolver manifests and semantic comparison evidence on a new no-overwrite root.

If semantic mismatch exists, stop BLOCKED and report the first differing field.

## 9. Scientific/model call budget

Exactly zero scientific/model calls in this task:

- MATLAB stationary/model top-level: `0`;
- MATLAB HJB/KFE: `0`;
- Python stationary/model top-level: `0`;
- Python HA/HJB/KFE: `0`;
- wrong-year MATLAB: `0`;
- 2010-2023 batch: `0`;
- shocks/AR1: `0`;
- transition/dynamics/IRF: `0`;
- legacy R5: `0`;
- Results: `0`.

Allowed:

- MATLAB `checkcode`;
- non-scientific path smoke exactly once;
- presolver manifest generation/comparison only;
- Python focused tests/compile/static scans/hashes.

A PASS of this task does **not** itself authorize a stationary scientific run.

## 10. Allowed repository changes

Authorized writes are limited to:

- bounded repair of affected MP4B validation `.m` helper(s) under `validators/multi_province/matlab/`;
- focused MATLAB/Python static tests/validators for this defect;
- optional bounded CURRENT roadmap status update;
- one report:

`docs/CH5_TWO_ASSET_HANK_MP4B_MATLAB_FILENAME_CONCATENATION_REPAIR_PATH_SMOKE_AND_FRESH_PRESOLVER_REVALIDATION_REPORT.md`

Do not modify:

- protected MATLAB;
- accepted household/HJB/KFE/oracle;
- MP2/MP3 scientific arithmetic;
- canonical 2009 input;
- primary data/cache;
- historical R5;
- controlling rule files.

Do not commit raw/private data, MAT scientific outputs, figures, large logs, caches or secrets.

## 11. Required report

Include:

1. terminal verdict;
2. live continuity;
3. prior blocker and historical scientific ledger;
4. complete unsafe-concatenation audit;
5. exact repair diff and R2022b compatibility rationale;
6. static review marker;
7. checkcode/static/test results;
8. smoke root, marker, manifest and SHA;
9. resolved helpers and finite-root evidence;
10. fresh presolver root and equality result;
11. scientific/model call ledger proving all zero;
12. unresolved list;
13. forbidden-operation check;
14. Git closeout;
15. exactly one recommended next gate.

## 12. Terminals

PASS:

`MP4B_FILENAME_CONCATENATION_REPAIR_PATH_SMOKE_AND_PRESOLVER_REVALIDATION_PASS`

PASS requires all three:

- `MP4B_FILENAME_CONCATENATION_REPAIR_STATIC_REVIEW_PASS`;
- `MP4B_LOGICAL_PHYSICAL_PATH_EQUIVALENCE_SMOKE_PASS`;
- `MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_PASS`.

BLOCKED:

`MP4B_FILENAME_CONCATENATION_REPAIR_PATH_SMOKE_AND_PRESOLVER_REVALIDATION_BLOCKED`

No scientific parity PASS/MATERIAL terminal exists in this task because scientific execution is intentionally closed.

## 13. Next-stage boundary

On PASS recommend exactly one next gate: **fresh bounded corrected-calendar-2009 MATLAB/Python stationary parity execution**, using the now smoke-validated helper chain and separately reauthorized one-run-per-language budgets.

On BLOCKED recommend one bounded successor addressing only the first remaining infrastructure/presolver cause.

## 14. Closeout

Explicit-path staging only. One execution commit. One non-force push. GitHub read-back every changed path. Require `HEAD == origin/main`, ahead/behind `0/0`, and clean worktree.
