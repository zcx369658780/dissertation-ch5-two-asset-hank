# CH5_TWO_ASSET_HANK_MP4B_PYTHON_HJB_LIQUID_DERIVATIVE_OBSERVABILITY_AND_MATLAB_SOURCE_SEMANTICS_DIAGNOSIS

Date: 2026-08-31

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded diagnostician / observability-only validator

Owner: final scientific authority

## 1. Purpose

Diagnose, without any stationary/HJB/KFE scientific rerun, the first Beijing household HJB failure from the accepted MP4B Python-only calendar-2009 attempt:

`ValueError: designated transfer FOCs require positive liquid derivatives`

Prior terminal:

`MP4B_PYTHON_ONLY_CALENDAR2009_STATIONARY_SCIENTIFIC_FAILURE_AFTER_FULL_INIT_PREFLIGHT`

Prior implementation/report commit:

`1aeca1cfb2f083e151e881d92db8a81d53b6c918`

This gate must expose the exact first offending liquid derivative, grid cell, surrounding value-function data, local-policy candidate inputs, and the exact ordering of MATLAB source derivative processing versus the current Python guard.

This task is **observability and source-semantics diagnosis only**. It does not authorize repair of the accepted standalone oracle, Python stationary reexecution, MATLAB stationary reexecution, HJB/KFE solving, MP2/MP3 empirical execution, shocks, batch runs, or Results.

## 2. Controlling authority

Read in full and obey:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `project_rules/PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md`
- `project_rules/PROJECT_RULE_MATLAB_MODEL_DIAGNOSTIC_GATES_CURRENT.md`
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`
- all Owner MP4 decision/adjudication documents
- accepted MP4A2 report
- all prior MP4B tasks/reports
- `docs/CH5_TWO_ASSET_HANK_MP4B_PYTHON_FULL_INITIALIZATION_PREFLIGHT_AND_PYTHON_ONLY_CALENDAR2009_STATIONARY_COMPARISON_REPORT.md`
- `validators/multi_province/mp4b_comparison_contract.json`
- current `validators/multi_province/mp4b_python_empirical.py`
- accepted standalone oracle `exports/matlab_faithful_two_asset_ha.py`

Preserve accepted evidence:

- corrected calendar-2009 identity and canonical SHA `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`
- `MP4B_INITIAL_LABOR_PYTHON_MATLAB_FROZEN_CELL_ROOT_PARITY_PASS`
- `MP4B_PYTHON_FULL_FIRST_TURN_SOURCE_INITIALIZATION_PREFLIGHT_PASS`
- preserved MATLAB completed baseline `COMPLETED / 184 / 5704 / 31-of-31`
- standalone oracle SHA `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`
- primary authority marker `MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

## 3. Live continuity

Expected execution-start parent:

`1aeca1cfb2f083e151e881d92db8a81d53b6c918`

At start:

1. fresh-fetch `origin/main`;
2. confirm this exact task is live on `main` as a direct child of the prior failure commit;
3. require clean worktree;
4. verify controlling rule blobs, accepted oracle, MP2, MP3, stationary runtime, canonical input, comparison contract, and preserved MATLAB artifact hashes;
5. verify protected MATLAB source remains unchanged;
6. verify no historical R5 / `chapter5_model` runtime dependency.

Any continuity failure => stop before diagnosis.

## 4. Protected MATLAB source-semantics audit — mandatory

Protected MATLAB root remains read-only:

`C:\MatlabProgram\2023年12月2日 多省份神经网络HANK`

Re-read and hash `HANK_2ASSETS_HJB.m` and all directly relevant helper code. Expected HJB SHA-256:

`049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`

Freeze exact source lines and operation order for:

- forward/backward liquid derivative construction;
- liquid-grid lower/upper boundary derivative treatment;
- any derivative floor such as `max(...,1e-6)` or equivalent;
- which derivative version is passed into consumption/labor FOCs;
- which derivative version is used in the transfer FOC ratio involving `pa/pb`;
- whether MATLAB ever rejects a cell solely because a **raw pre-floor** liquid derivative is non-positive;
- local liquid upwind selection and transfer-policy selection around the relevant source lines.

Do not infer from the Python implementation. Quote only short source fragments as needed and otherwise report exact formulas/line ranges.

Required marker:

`MP4B_HJB_LIQUID_DERIVATIVE_MATLAB_SOURCE_ORDERING_FROZEN`

If the source operation order cannot be established uniquely, stop `OWNER_PROVENANCE_REQUIRED`.

## 5. Audit the current accepted Python oracle ordering

Read the current accepted standalone oracle and identify the exact guard/order surrounding:

- raw `v_b_forward` / `v_b_backward`;
- `MATLAB_DERIVATIVE_FLOOR`;
- `vb_f=max(...)`, `vb_b=max(...)` or equivalent;
- `transfer_candidate(...)` calls;
- local liquid/transfer branch selection.

In particular, determine whether the current Python condition equivalent to:

`min(v_b_forward, v_b_backward) <= 0`

is source-backed, source-equivalent, or an additional Python-only admissibility restriction applied before a MATLAB source floor.

Do not modify the accepted oracle in this task.

## 6. Exact first-Beijing HJB observability reconstruction

Use only already accepted/persisted calendar-2009 inputs and the validated source-initialized value/labor construction. Do not call `solve_household_steady_state`, the HJB solver, KFE, MP2, MP3, or the online stationary controller.

Create a validation-only diagnostic, preferably under:

`validators/multi_province/mp4b_hjb_liquid_derivative_diagnostic.py`

that deterministically reconstructs the **initial HJB iterate** for the first Beijing household and computes the same local finite-difference inputs that the accepted HJB route would hand to `select_matlab_faithful_local_policy`.

Required evidence:

- exact Beijing state and household prices/wage/tax/returns;
- exact grid arrays and `db`, `da`, z ordering;
- initial value array identity/summary;
- raw `V_b^F`, `V_b^B` arrays before any floor;
- source-processed/floored liquid derivative arrays, if source applies a floor;
- raw and processed illiquid derivatives needed by the same local policy call;
- boundary flags;
- exact HJB/local-cell traversal order used to define “first offending cell”.

Find and persist the first cell for which the current Python guard fails. Record at minimum:

- province;
- zero-based and MATLAB-style indices;
- `(b,a,z)`;
- neighboring value-function values used in both liquid derivatives;
- raw `v_b_forward`, raw `v_b_backward`;
- source-processed/floored versions;
- derivative floor value;
- raw and source-processed `v_a_forward/backward`;
- baseline labor, transfer income, borrowing-rate gap;
- all boundary flags;
- the four transfer-candidate FOC inputs/ratios that would be formed if source semantics permit evaluation;
- the liquid candidate resources/drifts sufficient to identify the local liquid branch;
- whether the MATLAB source would proceed, floor, switch branch, or reject at the corresponding stage.

Also report scope counts over the complete first Beijing initial iterate:

- number of cells with raw `v_b_forward <= 0`;
- raw `v_b_backward <= 0`;
- either raw liquid derivative non-positive;
- both raw liquid derivatives positive;
- any nonfinite raw derivative;
- counts after source derivative processing/flooring.

Persist one no-overwrite diagnostic JSON artifact under a fresh `D:\ProjectTemp\...` root and record its SHA-256. Do not commit empirical arrays/raw outputs to GitHub; commit text-first summaries/hashes only.

Required marker:

`MP4B_FIRST_BEIJING_HJB_OFFENDING_LIQUID_DERIVATIVE_EXACTLY_LOCALIZED`

## 7. Source-vs-Python classification gate

After Sections 4-6, classify the earliest mismatch exactly.

If MATLAB source floors/processes the liquid derivative before every FOC that requires positivity, and does not reject the raw non-positive derivative, while Python rejects the raw derivative first, use:

`PYTHON_IMPLEMENTATION_ERROR__NONSOURCE_PRE_FLOOR_LIQUID_DERIVATIVE_POSITIVITY_GUARD`

If instead the Python raw derivative itself differs because derivative construction/boundary/order is wrong, use:

`PYTHON_IMPLEMENTATION_ERROR__LIQUID_DERIVATIVE_CONSTRUCTION_OR_BOUNDARY_MISMATCH`

If MATLAB source itself is ambiguous or would also be non-real/invalid at the same cell, use:

`SCIENTIFIC_SPECIFICATION_OR_PROVENANCE_AMBIGUITY`

Do not collapse these into a generic Python error.

Required diagnostic marker on successful localization:

`MP4B_HJB_FIRST_DIVERGENCE_SOURCE_SEMANTICS_DIAGNOSIS_COMPLETE`

## 8. Minimal successor repair specification — design only

If a Python implementation error is confirmed, write a minimal repair specification but do not implement it.

The repair spec must state:

- exact function/path to change;
- whether the raw positivity guard must be removed, moved after source floor, or replaced by a different source-backed condition;
- exact derivative variables to use in consumption/labor FOCs and transfer FOCs;
- required boundary behavior;
- required regression tests;
- whether accepted standalone household parity authorities need targeted revalidation because the accepted oracle itself changes.

Any proposed change to `exports/matlab_faithful_two_asset_ha.py` MUST be treated as a successor gate that revalidates the affected accepted household/HJB contracts before another empirical stationary run.

## 9. Call budget

Scientific/model calls in this task are all zero:

- MATLAB stationary: 0
- MATLAB HJB/KFE/multi-province: 0
- Python stationary: 0
- Python `solve_household_steady_state`: 0
- Python HJB solver iterations: 0
- Python KFE: 0
- MP2 empirical one-turn: 0
- MP3 empirical controller: 0
- wrong-year / annual batch / shocks / transition / dynamics / IRF / R5 / Results: 0

Allowed only:

- protected source reads/hashes;
- deterministic initial-array and finite-difference reconstruction;
- direct local arithmetic needed to expose candidate inputs without invoking the solver;
- tests/static checks;
- no-overwrite diagnostic serialization.

## 10. Allowed repository changes

Allowed:

- one observability-only Python diagnostic/validator under `validators/multi_province/`;
- focused tests for the diagnostic;
- CURRENT roadmap bounded status update;
- one report:
  `docs/CH5_TWO_ASSET_HANK_MP4B_HJB_LIQUID_DERIVATIVE_OBSERVABILITY_AND_MATLAB_SOURCE_SEMANTICS_DIAGNOSIS_REPORT.md`

Do not modify:

- `exports/matlab_faithful_two_asset_ha.py`;
- accepted modular household/HJB/KFE code;
- MP2;
- MP3;
- `stationary_runtime.py`;
- protected MATLAB;
- canonical input/data/cache;
- preserved MATLAB run;
- controlling rules;
- historical R5.

## 11. Required report

Include at minimum:

1. terminal verdict;
2. live continuity;
3. source hashes;
4. exact MATLAB liquid-derivative source ordering;
5. exact Python oracle ordering;
6. first Beijing initial-HJB reconstruction method;
7. diagnostic artifact path/hash;
8. exact first offending cell and all derivative/candidate inputs;
9. complete first-Beijing derivative sign/floor count table;
10. source-vs-Python earliest-divergence classification;
11. whether source would proceed at that cell;
12. minimal successor repair specification, if justified;
13. accepted household authority impact assessment;
14. zero scientific-call ledger;
15. tests/checks;
16. forbidden-operation check;
17. Git closeout;
18. exactly one recommended next gate.

## 12. Terminals

Successful diagnosis:

`MP4B_HJB_LIQUID_DERIVATIVE_OBSERVABILITY_AND_SOURCE_SEMANTICS_DIAGNOSIS_PASS`

Blocked before localization:

`MP4B_HJB_LIQUID_DERIVATIVE_OBSERVABILITY_DIAGNOSIS_BLOCKED`

Owner provenance required:

`MP4B_HJB_LIQUID_DERIVATIVE_SOURCE_SEMANTICS_OWNER_PROVENANCE_REQUIRED`

A PASS here is diagnostic only. It does not accept stationary parity and does not authorize any scientific rerun.

## 13. Next-stage boundary

On PASS with a confirmed Python implementation error, recommend exactly one bounded successor:

**targeted accepted-oracle HJB derivative-order repair + affected household/HJB parity revalidation + zero empirical stationary calls**.

Only after that repair/revalidation passes may a later gate separately authorize one new Python-only calendar-2009 stationary invocation against the preserved MATLAB baseline.

On ambiguity/BLOCKED, recommend only the bounded evidence/provenance gate needed to resolve it.

## 14. Closeout

Explicit-path staging only. One execution commit. One non-force push. GitHub read-back every changed path. Require `HEAD == origin/main`, ahead/behind `0/0`, and clean worktree.
