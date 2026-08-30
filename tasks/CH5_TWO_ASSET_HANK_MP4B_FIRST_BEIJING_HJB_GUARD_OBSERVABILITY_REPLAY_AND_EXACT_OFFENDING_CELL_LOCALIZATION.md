# CH5_TWO_ASSET_HANK_MP4B_FIRST_BEIJING_HJB_GUARD_OBSERVABILITY_REPLAY_AND_EXACT_OFFENDING_CELL_LOCALIZATION

Date: 2026-08-31

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded diagnostician / HJB observability replay executor

Owner: final scientific authority

## 1. Purpose

Resolve the remaining observability blocker from the prior MP4B diagnosis by running exactly one bounded, instrumented **first-Beijing-household HJB-only replay** from the already validated calendar-2009 initial arrays until the first local-policy call at which the current accepted Python oracle would reject a non-positive raw liquid derivative.

Prior terminal:

`MP4B_HJB_LIQUID_DERIVATIVE_OBSERVABILITY_DIAGNOSIS_BLOCKED`

Prior report/implementation commit:

`71f363c550a56d7bdba605ac5e8c416f3707b582`

Already established and preserved:

- `MP4B_HJB_LIQUID_DERIVATIVE_MATLAB_SOURCE_ORDERING_FROZEN`
- static classification `PYTHON_IMPLEMENTATION_ERROR__NONSOURCE_PRE_FLOOR_LIQUID_DERIVATIVE_POSITIVITY_GUARD`
- Beijing initial iterate has `800/800` cells with both raw liquid derivatives positive
- the observed empirical guard failure must therefore occur after at least one HJB value update

This task exists only to identify the exact first offending HJB iteration/cell and persist the derivative/candidate evidence. It does **not** authorize any repair or any stationary/household/KFE/GE rerun.

## 2. Controlling authority

Read in full and obey:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `project_rules/PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md`
- `project_rules/PROJECT_RULE_MATLAB_MODEL_DIAGNOSTIC_GATES_CURRENT.md`
- `docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md`
- all Owner MP4 decisions/adjudications
- accepted MP4A2 report
- all prior MP4B tasks/reports
- `docs/CH5_TWO_ASSET_HANK_MP4B_HJB_LIQUID_DERIVATIVE_OBSERVABILITY_AND_MATLAB_SOURCE_SEMANTICS_DIAGNOSIS_REPORT.md`
- `validators/multi_province/mp4b_hjb_liquid_derivative_diagnostic.py`
- accepted standalone oracle `exports/matlab_faithful_two_asset_ha.py`

Preserve accepted evidence and identities:

- corrected calendar-2009 identity and canonical SHA `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`
- `MP4B_INITIAL_LABOR_PYTHON_MATLAB_FROZEN_CELL_ROOT_PARITY_PASS`
- `MP4B_PYTHON_FULL_FIRST_TURN_SOURCE_INITIALIZATION_PREFLIGHT_PASS`
- preserved MATLAB baseline `COMPLETED / 184 outer turns / 5704 household calls / 31-of-31`
- standalone oracle SHA `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`
- protected MATLAB HJB SHA `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- frozen MATLAB derivative ordering from the prior diagnosis

Primary authority remains:

`MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`

## 3. Live continuity

Expected execution-start parent:

`71f363c550a56d7bdba605ac5e8c416f3707b582`

At start:

1. fresh-fetch `origin/main`;
2. confirm this exact task is live on `main` as a direct child of the prior diagnosis commit;
3. require clean worktree;
4. verify controlling rule blobs, canonical input, accepted oracle, MP2, MP3, stationary runtime, comparison contract, and preserved MATLAB artifacts remain unchanged;
5. rehash protected MATLAB source identities;
6. verify no active historical R5 / `chapter5_model` dependency.

Any continuity failure => stop before replay.

## 4. Replay semantics — exact bounded HJB-only reconstruction

Create a validation-only replay, preferably:

`validators/multi_province/mp4b_first_beijing_hjb_guard_replay.py`

The replay MUST start from the exact first-Beijing household inputs and exact source-initialized `value` and `labor0` arrays already validated by the calendar-2009 Python entry.

Use the accepted oracle's exact:

- `20 x 20 x 2` grid and state ordering;
- `db`, `da`;
- raw forward/backward derivative construction;
- liquid boundary marginal-utility values;
- illiquid derivative/boundary construction;
- local traversal order `z -> a -> b`;
- accepted local-policy function for cells that occur strictly before the first offending cell;
- accepted `assemble_source_operator`;
- exact sparse HJB value-update equation, Fortran flatten/reshape order, pseudo-time step, discount rate and switching matrix.

Do not hand-redesign the HJB update. Reuse accepted oracle functions wherever possible and duplicate only the minimum loop/control needed to observe and stop before the guard.

Maximum replay horizon: the frozen household HJB maximum, **100 value iterations**. No second replay is authorized.

## 5. Mandatory stop-before-guard instrumentation

At each local cell, immediately before calling `select_matlab_faithful_local_policy`, inspect the exact raw boundary-treated:

- `v_b_forward`
- `v_b_backward`

If both are positive, proceed with the accepted local-policy call and continue the HJB iteration.

At the **first** cell in exact traversal order where either raw liquid derivative is `<= 0`:

1. DO NOT call `select_matlab_faithful_local_policy` for that cell;
2. persist the complete offending-cell evidence;
3. terminate the replay successfully as an observability stop;
4. do not assemble/solve the remainder of that HJB iteration;
5. do not continue to any later cell or iteration.

This produces the exact point at which the accepted Python oracle would have raised its pre-floor positivity exception, while avoiding the exception itself and avoiding any repair.

Required localization marker:

`MP4B_FIRST_BEIJING_HJB_OFFENDING_LIQUID_DERIVATIVE_EXACTLY_LOCALIZED`

If no offending cell is found within 100 completed HJB value iterations, stop BLOCKED and report that the preserved empirical failure was not reproduced by the bounded replay; do not change semantics or extend the horizon.

## 6. Replay identity checks before allowing iteration 2+

The replay's iteration-1 derivative reconstruction MUST reproduce the already accepted prior diagnostic exactly enough to establish identity before any value update is trusted.

Require at minimum:

- shape `[20,20,2]`;
- raw non-positive counts `0/0/0` exactly as previously reported;
- both-positive count `800`;
- no nonfinite raw derivatives;
- minimum raw derivative cell identity `(i,j,k)=(18,19,1)` zero-based;
- minimum raw `VbF = 0.001609918920837204` and `VbB = 0.001610998339912406` within the previously frozen direct-primitive floating contract;
- initial-value byte/hash identity if serialization is made identically, otherwise elementwise equality to the reconstructed accepted initial array.

Required marker:

`MP4B_FIRST_BEIJING_HJB_REPLAY_INITIAL_ITERATE_IDENTITY_PASS`

If this fails, stop before the first sparse value update.

## 7. Exact offending-cell evidence

Persist, at minimum:

- HJB iteration number at which the guard would first fail;
- number of fully completed previous HJB iterations;
- zero-based and MATLAB-style `(i,j,k)` indices;
- `(b,a,z)`;
- current `old` value and liquid forward/backward neighbor values used in the raw derivatives;
- raw `VbF`, raw `VbB`;
- MATLAB consumption/labor-processed `max(raw Vb,1e-6)` versions;
- derivative floor value;
- raw `VaF`, raw `VaB` and their boundary treatment;
- baseline labor;
- transfer income, `rb`, borrowing-rate gap and effective liquid rate;
- all four boundary booleans;
- raw `pa/pb` ratios for `BB/BF/FB/FF` under protected MATLAB `HANK3_FOC` semantics, using IEEE/MATLAB-like division behavior where needed and recording finite/Inf/NaN classification rather than introducing a Python guard;
- corresponding transfer candidates according to the protected source formula where mathematically defined;
- floored consumption/labor candidate values and liquid resources/drifts;
- source action at that exact stage: whether MATLAB proceeds to FOCs/transfer ratios rather than rejecting solely because the raw derivative is non-positive;
- current Python action: would reject before the floor.

If the offending derivative is exactly zero and MATLAB's raw transfer ratio creates Inf/NaN, record that faithfully; do not hide it. Distinguish the established **ordering mismatch** from any later MATLAB arithmetic consequence.

Also persist per-iteration summaries for every fully completed iteration before failure:

- HJB convergence statistic `max(abs(value_new-value_old))`;
- minimum/maximum raw `VbF` and `VbB`;
- counts of `VbF<=0`, `VbB<=0`, either non-positive, both positive and nonfinite;
- value-array min/max;
- optional SHA-256 of each value iterate serialized in a deterministic local-only format.

Do not commit large arrays to GitHub.

## 8. Source-semantics confirmation and classification

Re-read the protected source ordering already frozen in the prior task and confirm against the exact offending cell.

If the replay reproduces a raw non-positive derivative and protected MATLAB would not reject at that stage, establish:

`MP4B_HJB_FIRST_DIVERGENCE_SOURCE_SEMANTICS_DIAGNOSIS_COMPLETE`

and classify:

`PYTHON_IMPLEMENTATION_ERROR__NONSOURCE_PRE_FLOOR_LIQUID_DERIVATIVE_POSITIVITY_GUARD`

If the replay instead shows that the raw derivative construction itself diverges from the protected MATLAB formulas/boundaries, classify:

`PYTHON_IMPLEMENTATION_ERROR__LIQUID_DERIVATIVE_CONSTRUCTION_OR_BOUNDARY_MISMATCH`

If the exact source behavior at the offending cell cannot be determined because raw zero/negative transfer ratios create an unresolved source ambiguity, retain the exact localized cell but use:

`SCIENTIFIC_SPECIFICATION_OR_PROVENANCE_AMBIGUITY`

Do not repair anything in this task.

## 9. Call budget and prohibited execution

This task authorizes exactly **one Python first-Beijing HJB observability replay** as described above.

Authorized computational scope:

- one household only: Beijing;
- HJB value iterations only;
- maximum 100 iterations;
- stop immediately before the first non-positive-raw-Vb local-policy guard;
- accepted local-policy/operator/value-update arithmetic only for cells/iterations preceding the stop.

Explicitly prohibited:

- Python stationary top-level: 0;
- `solve_household_steady_state`: 0;
- KFE: 0;
- household aggregate computation: 0;
- any second province household: 0;
- MP2 empirical one-turn: 0;
- MP3/online stationary controller: 0;
- MATLAB HJB/KFE/stationary/multi-province model: 0;
- wrong-year / 2010-2023 batch / shocks / transition / dynamics / IRF / R5 / Results: 0;
- any repair or rerun after localization: 0.

The replay is diagnostic evidence, not an accepted HJB solution or household result.

## 10. Allowed repository changes

Allowed only:

- one observability replay validator under `validators/multi_province/`;
- focused tests for replay identity, stop semantics and zero downstream calls;
- bounded CURRENT roadmap status update;
- one report:
  `docs/CH5_TWO_ASSET_HANK_MP4B_FIRST_BEIJING_HJB_GUARD_OBSERVABILITY_REPLAY_AND_EXACT_OFFENDING_CELL_LOCALIZATION_REPORT.md`

Do not modify:

- `exports/matlab_faithful_two_asset_ha.py`;
- accepted modular household/HJB/KFE code;
- `validators/multi_province/mp4b_python_empirical.py` except read-only import/use;
- MP2;
- MP3;
- `stationary_runtime.py`;
- protected MATLAB;
- canonical input/data/cache;
- preserved MATLAB run;
- controlling rules;
- historical R5.

## 11. Tests and fail-closed requirements

Focused tests must prove at minimum:

- replay iteration-1 identity to the prior 800-positive diagnostic;
- exact traversal order;
- stop occurs before invoking local policy at a synthetic non-positive raw-Vb cell;
- no KFE/aggregate/MP2/MP3/stationary imports or calls are reachable from the replay execution path;
- no accepted oracle mutation;
- no-overwrite serialization;
- deterministic repeated reconstruction of the pre-stop iteration summaries from identical inputs.

Python compile and `git diff --check` must pass.

## 12. Required local artifact

Use a fresh no-overwrite root under `D:\ProjectTemp` and write one compact diagnostic JSON containing:

- source/oracle/canonical identities;
- replay configuration and call ledger;
- initial-iterate identity evidence;
- completed-iteration summaries;
- exact offending-cell payload or explicit `not_found_within_100_iterations`;
- final classification;
- downstream calls all zero.

Record its SHA-256 in the report. Large value arrays remain local-only and need not be persisted unless necessary for deterministic hashes.

## 13. Terminal verdicts

Successful exact localization:

`MP4B_FIRST_BEIJING_HJB_GUARD_OBSERVABILITY_REPLAY_LOCALIZATION_PASS`

Blocked because replay identity fails, no offender is found within 100 iterations, or required source evidence cannot be established:

`MP4B_FIRST_BEIJING_HJB_GUARD_OBSERVABILITY_REPLAY_BLOCKED`

Owner provenance required:

`MP4B_FIRST_BEIJING_HJB_GUARD_REPLAY_SOURCE_SEMANTICS_OWNER_PROVENANCE_REQUIRED`

A PASS is observability-only. It does not accept HJB parity, household parity or stationary parity.

## 14. Successor boundary

On PASS with confirmed non-source pre-floor guard, recommend exactly one successor:

**targeted accepted-oracle raw-Vb guard / transfer-candidate source-order repair plus affected local-policy/HJB/standalone-household parity revalidation, with empirical stationary calls held at zero.**

Only after that affected household authority is revalidated may a later, separately authorized Python-only calendar-2009 stationary run be considered.

On construction/boundary mismatch, recommend only that targeted repair/revalidation gate.

On ambiguity/BLOCKED, recommend the minimum evidence gate needed to resolve it.

## 15. Closeout

Explicit-path staging only. One execution commit. One non-force push. GitHub read-back every changed path. Require `HEAD == origin/main`, ahead/behind `0/0`, and clean worktree.
