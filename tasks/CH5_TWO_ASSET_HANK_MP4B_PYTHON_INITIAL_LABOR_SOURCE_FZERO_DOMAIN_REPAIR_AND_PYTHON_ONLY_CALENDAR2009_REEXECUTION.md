# CH5_TWO_ASSET_HANK_MP4B_PYTHON_INITIAL_LABOR_SOURCE_FZERO_DOMAIN_REPAIR_AND_PYTHON_ONLY_CALENDAR2009_REEXECUTION

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / MATLAB-source-semantics diagnostician / Python validation-entry repairer / Python-only stationary executor

Owner: final scientific authority

## 1. Purpose

Diagnose and repair the Python validation-entry initial-labor construction that caused the sole authorized Python calendar-2009 stationary invocation to fail before completing the first household.

The prior terminal was:

`MP4B_PYTHON_ONLY_CALENDAR2009_STATIONARY_SCIENTIFIC_FAILURE`

Prior implementation/report commit:

`72e1e7a1dc60c528127880520ce760816a6e320e`

The observed failure occurred in `_source_initial_arrays` before `solve_household_steady_state` returned once. The current Python code brackets `brentq` with `lo=0.0`; for a negative-liquid-asset cell the labor-equation consumption base is negative at that endpoint, the fractional power is non-real/NaN, and SciPy aborts.

This task must determine the exact MATLAB source semantics first. It must not assume that “clamp consumption positive” or “start brentq above zero” is automatically source-faithful.

After source semantics are frozen and independently validated, the task may repair only the validation-entry initialization/root construction and then execute one fresh Python-only calendar-2009 stationary invocation maximum. The already completed MATLAB calendar-2009 stationary run is immutable comparison evidence and MUST NOT be rerun.

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
- all prior MP4B task authorities and reports;
- `docs/CH5_TWO_ASSET_HANK_MP4B_PYTHON_BOOTSTRAP_REPAIR_AND_PYTHON_ONLY_CALENDAR2009_STATIONARY_COMPARISON_REPORT.md`;
- `validators/multi_province/mp4b_comparison_contract.json`;
- current `validators/multi_province/mp4b_python_empirical.py`.

Preserve all accepted contracts and identities, including:

- `OWNER_SINGLE_ACTIVE_CODEBASE_TWO_ASSET_HANK_ONLY`;
- corrected calendar-2009 identity;
- canonical input SHA `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`;
- accepted standalone HA oracle SHA `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`;
- accepted MP2 and MP3 arithmetic/controller semantics;
- exact Python direct-script bootstrap contract already accepted;
- `OWNER_PARITY_MISMATCH_BOUNDED_ROOT_CAUSE_DIAGNOSIS_AUTHORIZED`.

Primary reconstruction authority remains:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

## 3. Live continuity

Expected execution-start parent / prior scientific-failure commit:

`72e1e7a1dc60c528127880520ce760816a6e320e`

At start:

1. fresh-fetch `origin/main`;
2. confirm this exact task is live on `main` as a direct child of the prior failure commit;
3. require clean worktree;
4. verify controlling rule blobs and protected-source hashes unchanged;
5. verify accepted oracle, MP2, MP3, MP4A2 annual binding, stationary runtime, comparison contract, bootstrap entry and canonical input identities;
6. rehash the preserved MATLAB run and require its accepted artifact identities;
7. verify no historical `chapter5_model` / R5 runtime dependency.

Any continuity failure => stop before diagnosis or scientific execution.

## 4. Protected MATLAB source-semantics audit — mandatory

Protected MATLAB root remains read-only:

`C:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Re-read and hash at minimum:

- `HANK_2ASSETS_HJB.m`, expected SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`;
- `lab_solve2.m`, expected SHA-256 `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`;
- source initialization fields in `multi_prov_HANK_12sts.m` / prepared-state evidence needed to identify `alphac`, `alphal`, `tau`, `frisch_l`, `ga`, `rb_gap`, grids and initial wages/returns.

Freeze the exact source formulas and line locations for:

```matlab
tempMat = Rah.*raah + Rb.*bbb + Tt;
params = [alphac,alphal,tau,w,zzz,frisch_l,tempMat,ga];
myfun = @(l) lab_solve2(l,params);
x0 = ((1-tau)*w*zzz)^(frisch_l*(1-ga)/(1+ga*frisch_l));
[l0j,fval,exitflag] = fzero(myfun,x0,options);
```

and the exact `lab_solve2` equation:

```matlab
eq = l - (alphac/alphal*(1-tau)*w*zzz)^frisch_l ...
    * (l*(1-tau)*w*zzz + tempMat)^(-ga*frisch_l);
```

Also freeze the source `c0` and `v02` initialization formulas immediately after the root loop, and compare every coefficient/exponent against the current Python `_source_initial_arrays` implementation. Do not assume omitted multiplicative constants are harmless unless the frozen prepared state proves they equal the values hard-coded by Python.

Required source-semantics marker:

`MP4B_INITIAL_LABOR_MATLAB_SOURCE_SEMANTICS_FROZEN`

If source identities/formulas cannot be established uniquely, stop `OWNER_PROVENANCE_REQUIRED` before any repair.

## 5. Exact failing-cell and admissible-domain diagnosis

Using the already persisted Python turn-1 household-input artifact from:

`D:\ProjectTemp\ch5-mp4b-python-only-calendar2009-20260830-001`

and the accepted calendar-2009 grid/prepared state, identify deterministically the first cell reached by the Python loop that generated the NaN.

Persist for that cell:

- province;
- `(b,a,z)` values and integer indices;
- `Rb`, effective illiquid return / `raah`, `tempMat`;
- `B = (1-tau)*w*z`;
- source `x0`;
- source exponent `p = ga*frisch_l`;
- consumption-base value at Python's old `l=0` endpoint;
- the exact old Python exception mechanism.

Then establish the real-valued admissible domain of the source labor equation without altering it. Under source-positive `alphac/alphal`, `B`, `frisch_l`, and `p`, prove or refute from the source-frozen parameters that on the real domain

`B*l + tempMat > 0`

the labor residual is continuous and strictly increasing, with at most one real root.

Do not silently impose a new economic labor constraint beyond what is needed to evaluate the source equation in the real domain. If the source scalar start `x0` itself is outside the real domain for any frozen cell needed by the first household, stop and report a source/runtime ambiguity instead of inventing a solver convention.

Required diagnosis marker on success:

`MP4B_PYTHON_INITIAL_LABOR_ZERO_ENDPOINT_IS_NONSOURCE_DOMAIN_ERROR_CONFIRMED`

## 6. Bounded source-equivalent root construction design

The repair must preserve the MATLAB source equation and source `x0` anchor. It may replace only the non-source Python bracketing logic.

A permissible design, if supported by the monotonicity/domain proof, is:

1. evaluate the source residual at the source `x0` only if `x0` is real/admissible;
2. if `f(x0) < 0`, expand only upward until a positive residual is found;
3. if `f(x0) > 0`, move monotonically from `x0` toward the open real-domain boundary using interior midpoints, never evaluating at or beyond the non-real boundary, until a negative residual is found;
4. solve the unique real root within that admissible sign-changing bracket using deterministic `brentq`;
5. fail closed after a pre-declared finite search limit rather than clipping the base, replacing NaN, changing the equation, or silently switching solvers.

Do not use `max(base,epsilon)` inside the source residual. Do not change `tempMat`, `Rb`, `raah`, `x0`, preferences, wages, taxes, grid, or HJB/KFE code.

If a different construction is more source-faithful, document and prove it before implementation.

## 7. Independent scalar MATLAB `fzero` diagnostic — allowed, not a stationary rerun

This task authorizes at most **one validation-only MATLAB scalar-diagnostic top-level invocation**. It is NOT a stationary/HJB/KFE/model invocation.

The diagnostic may evaluate at most **8 frozen labor-root cells** and may call only:

- protected read-only `lab_solve2.m`;
- MATLAB built-in `fzero` with source-equivalent `optimset('Display','off')` and the exact source scalar `x0`;
- no `HANK_2ASSETS_HJB`, no KFE, no `HANK_mp_1turn`, no `HANK_mp_1eq`, no multi-province model.

The frozen cell set must be declared before execution and include:

- the exact first failing negative-base-at-zero cell;
- at least one cell with nonnegative base at zero;
- both productivity states where feasible;
- at least one negative-liquid and one nonnegative-liquid grid location.

Persist for every cell:

- source parameters;
- `x0`;
- MATLAB `l0`, `fval`, `exitflag`;
- base `B*l0+tempMat`;
- Python repaired bracket and root;
- both residuals.

Pre-freeze the scalar root comparison rule before executing the diagnostic:

- categorical `exitflag > 0`: required for selected MATLAB cells;
- both roots finite and real;
- both source residual magnitudes `<= 1e-10`;
- absolute root difference `<= 1e-10 * max(1,abs(l_matlab),abs(l_python))`.

No post-hoc loosening. If this bounded parity fails, do not execute the Python stationary run.

Required marker:

`MP4B_INITIAL_LABOR_PYTHON_MATLAB_FROZEN_CELL_ROOT_PARITY_PASS`

## 8. Repair scope and static tests

Authorized repair path:

- `validators/multi_province/mp4b_python_empirical.py` only for initial-labor/source-initial-array logic and associated validation/bootstrap-safe helper code;
- focused tests/validators for this gate;
- optional validation-only MATLAB scalar diagnostic helper under `validators/multi_province/matlab/`;
- report and bounded roadmap status update.

Do not modify:

- `exports/matlab_faithful_two_asset_ha.py`;
- accepted modular household/HJB/KFE code;
- MP2 arithmetic;
- MP3 controller semantics;
- `stationary_runtime.py` unless an interface-only defect independent of initial-labor semantics is proven before science; default is no modification;
- protected MATLAB;
- canonical input/data/cache;
- historical R5.

Focused tests must cover at minimum:

- negative `tempMat` / invalid old zero endpoint;
- source `x0` admissibility;
- bracket never evaluates a non-real consumption base;
- monotonicity/unique-root diagnostic assumptions on the frozen source parameter regime;
- positive and negative liquid-asset cells;
- both z states;
- failure on impossible/non-source parameter domains;
- `c0`/`v02` formula identity to source constants;
- direct-script bootstrap smoke remains zero-science PASS;
- all seven MP3 online-controller scenarios remain exact.

Required pre-science marker:

`MP4B_INITIAL_LABOR_SOURCE_DOMAIN_REPAIR_STATIC_REVIEW_PASS`

## 9. Fresh presolver and preserved MATLAB evidence gate

Before the Python scientific invocation:

- re-establish `MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_PASS` with mismatch count zero;
- rehash and preserve the prior completed MATLAB root:
  `D:\ProjectTemp\ch5-mp4b-fresh-calendar2009-matlab-20260830-001`;
- require stationary output SHA-256:
  `6233AB8B7380BE4D4E136851BC59F747EEB78B285B3A7A5903FEFFE64BCF464B`;
- require preserved MATLAB status/turns/household calls:
  `COMPLETED / 184 / 5704`;
- require final household convergence flags `31/31` true;
- rerun the direct-script bootstrap smoke with zero model calls on a fresh no-overwrite path.

MATLAB stationary invocation remains exactly zero in this task.

## 10. Scientific execution budget

Only after Sections 4-9 PASS:

### Python

- corrected calendar-2009 stationary top-level invocation: maximum **1**;
- scientific rerun: **0**.

### MATLAB

- stationary / HJB / KFE / multi-province execution: **0**;
- validation-only scalar root diagnostic from Section 7: maximum **1** top-level invocation, <=8 cells, no model solver.

If Python fails after entering scientific execution, preserve the exact outcome and stop. Do not repair and rerun.

Forbidden remain zero:

- wrong-year MATLAB;
- 2010-2023 batch;
- shocks/AR1;
- transition/genuine dynamics/IRF;
- historical R5;
- Results/manuscript claims.

## 11. Python completion and comparison contract

If the Python stationary run completes or scientifically nonconverges after valid household calls, compare the maximum available result against the preserved MATLAB run under the already frozen:

`validators/multi_province/mp4b_comparison_contract.json`

Comparison hierarchy remains:

1. presolver identity;
2. first-turn household inputs;
3. first-turn household outputs where MATLAB evidence exists;
4. migration;
5. At-only capital / `Kt_supply` / `rah`;
6. firm;
7. wage/monetary/fiscal;
8. controller;
9. later turns;
10. final 31-province stationary state.

Do not rerun MATLAB to manufacture missing traces. If only final MATLAB state is available, compare final state/national aggregates/categorical boundary statuses and state exactly which upstream layers are unavailable.

Qualitative sign/ranking/boundary diagnostics remain secondary.

## 12. Terminals

If source semantics/domain cannot be frozen uniquely:

`MP4B_INITIAL_LABOR_SOURCE_SEMANTICS_OWNER_PROVENANCE_REQUIRED`

If bounded repair/static/scalar parity/presolver gates fail before Python science:

`MP4B_INITIAL_LABOR_SOURCE_DOMAIN_REPAIR_BLOCKED`

If the single Python scientific invocation fails after repair:

`MP4B_PYTHON_ONLY_CALENDAR2009_STATIONARY_SCIENTIFIC_FAILURE_AFTER_INITIAL_LABOR_REPAIR`

If Python produces a complete comparison package:

`MP4B_PYTHON_INITIAL_LABOR_REPAIR_AND_CALENDAR2009_COMPARISON_COMPLETE__L3_ACCEPTANCE_PENDING`

The executor MUST NOT self-upgrade the last terminal to final stationary parity PASS. L3 independent review is required.

## 13. Required report

Write:

`docs/CH5_TWO_ASSET_HANK_MP4B_PYTHON_INITIAL_LABOR_SOURCE_FZERO_DOMAIN_REPAIR_AND_PYTHON_ONLY_CALENDAR2009_REEXECUTION_REPORT.md`

Include at minimum:

1. terminal verdict;
2. live continuity;
3. protected source hashes and exact source-line semantics;
4. Python-vs-MATLAB initialization formula audit;
5. exact first failing cell and old endpoint diagnosis;
6. admissible-domain and uniqueness proof with assumptions;
7. root-construction design and finite-search limits;
8. exact repair diff;
9. scalar MATLAB frozen-cell diagnostic manifest/hash and table;
10. static-test evidence;
11. bootstrap smoke evidence;
12. fresh presolver mismatch count;
13. preserved MATLAB artifact rehash evidence;
14. full call ledger separating scalar diagnostic from stationary/model calls;
15. Python run root and artifact hashes;
16. household call count / outer turns / convergence status;
17. final MATLAB-Python comparison if Python produces a state;
18. unavailable MATLAB trace layers;
19. first supported divergence and root-cause classification;
20. material mismatch / unresolved residual / environment lists;
21. forbidden-operation check;
22. Git closeout;
23. exactly one recommended next gate.

## 14. Allowed repository writes

Only:

- bounded edit to `validators/multi_province/mp4b_python_empirical.py`;
- focused tests/validators for initial-labor source semantics/domain/root parity;
- optional bounded MATLAB scalar-root diagnostic helper under `validators/multi_province/matlab/`;
- this task report;
- bounded CURRENT roadmap status update.

No raw/private data, scientific MAT outputs, large logs, caches, or figures may be committed.

## 15. Closeout

Explicit-path staging only. One execution commit. One non-force push. GitHub read-back every changed path. Require `HEAD == origin/main`, ahead/behind `0/0`, clean worktree.

On `...L3_ACCEPTANCE_PENDING`, recommend exactly one next gate: L3 independent calendar-2009 stationary parity acceptance review using the preserved MATLAB result and new Python evidence.

On scientific failure, recommend exactly one bounded successor addressing only the newly localized first cause. Do not widen to MP5, multi-year, shocks, dynamics, or Results.
