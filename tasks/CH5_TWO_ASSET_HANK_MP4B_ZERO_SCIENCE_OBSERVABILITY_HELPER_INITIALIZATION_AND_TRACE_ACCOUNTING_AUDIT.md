# CH5_TWO_ASSET_HANK_MP4B_ZERO_SCIENCE_OBSERVABILITY_HELPER_INITIALIZATION_AND_TRACE_ACCOUNTING_AUDIT

Date: 2026-08-31

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / zero-science observability-contract auditor

Owner: final scientific authority

## 1. Purpose

The immediately preceding Owner-reauthorized instrumented MATLAB corrected-calendar-2009 one-shot consumed its single permitted MATLAB launcher and stationary top-level entry, then failed on outer turn 1 inside the copied observability helper before the first `HANK_2ASSETS_HJB` call.

Accepted predecessor terminal:

`MP4B_OWNER_REAUTHORIZED_INSTRUMENTED_MATLAB_CORRECTED2009_ONE_SHOT_BLOCKED_NO_RERUN`

Accepted predecessor execution commit:

`0dd1ab05ad5d7e6e923ab4d1f7ae8f998b66abcd`

Accepted predecessor task authority:

`535044b4030df6c25cf83092538f54496b8bd680`

Exact failure:

- MATLAB identifier: `MATLAB:invalidConversion`;
- message: `无法从 struct 转换为 double。`;
- location: copied `MP4B_OBS.m` line 19 while assigning `household_inputs(i)`;
- route reached: `mpHANK_equilibrium_2000 -> HANK_mp_1eq -> HANK_mp_1turn`;
- failure occurred before the first `HANK_2ASSETS_HJB` call.

The predecessor report also establishes an observability-accounting issue that must be audited independently: `instrumented_trace_summary.json` reported `household_call_count=31` from a formula based on turn count even though controlling stack evidence proves completed HJB/household calls were `0`.

This task is a **zero-science, read-only observability-helper initialization and trace-accounting audit**. It must determine the complete helper/schema defect surface before any future Owner decision about another MATLAB one-shot.

This task MUST NOT repair, mutate, execute, or reauthorize the instrumented stationary route.

## 2. Hard execution budget

For this task:

- MATLAB processes: `0`;
- MATLAB stationary/HJB/KFE/household/firm/controller calls: `0`;
- MATLAB `checkcode`: `0`;
- Python stationary/HJB/KFE/household/MP2/MP3 scientific calls: `0`;
- comparator / `compare_terminal`: `0`;
- Zhejiang/Shanxi replay: `0`;
- other years/batch: `0`;
- shocks/AR1/transition/dynamics/IRF: `0`;
- historical R5/Results: `0`.

Static text parsing, hashing, PowerShell/Python standard-library-only inspection, MAT/HDF5 metadata inspection without importing or invoking scientific modules, and bounded external audit artifacts are allowed.

No MATLAB executable may be started for any reason.

## 3. Required live continuity

At execution start:

1. fresh-fetch `origin/main`;
2. require this exact task live on `main` as the direct child of `0dd1ab05ad5d7e6e923ab4d1f7ae8f998b66abcd`;
3. require clean worktree, `HEAD == origin/main`, ahead/behind `0/0`;
4. read completely:
   - `AGENTS.md`;
   - `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
   - `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`;
   - `project_rules/PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md`;
   - `project_rules/PROJECT_RULE_MATLAB_MODEL_DIAGNOSTIC_GATES_CURRENT.md`;
   - predecessor task `tasks/CH5_TWO_ASSET_HANK_MP4B_OWNER_REAUTHORIZED_INSTRUMENTED_MATLAB_CORRECTED2009_ONE_SHOT_AND_CHRONOLOGICAL_ADJUDICATION.md`;
   - predecessor report `docs/CH5_TWO_ASSET_HANK_MP4B_OWNER_REAUTHORIZED_INSTRUMENTED_MATLAB_CORRECTED2009_ONE_SHOT_AND_CHRONOLOGICAL_ADJUDICATION_REPORT.md`;
   - zero-science copy-binding remediation task/report;
   - the earlier blocked instrumented-run task/report whose observability patch was reused.

Any authority/identity failure => stop with zero science.

## 4. Immutable predecessor evidence

Read-only predecessor run root:

`D:\ProjectTemp\ch5-mp4b-instrumented-matlab-calendar2009-owner-reauthorized-20260831-001`

Require at minimum these identities from the accepted report:

- source-copy manifest:
  `757D83D13B32BC92411F687069797A0F3DA4ADFC06FFEBD872B0674DBEDE9961`
- instrumentation manifest:
  `511F59C6F6482DC5BBA7EBBFAD5B234C7D31B840AB2DE2CDDC836F4B74A52B2B`
- copied-source instrumentation diff:
  `0B4B4D78EF45E33052E0888CC0E4AD8703167DC71DD8FA0D79BD01B5A053BB9F`
- pre-science gate:
  `CFA0EE14410F44C9E56D8977D4F1363590CB8AC70E392F62E8CD47404EEF753D`
- exact launcher command:
  `9F6E9A73CE4DECE261B390567DBD3EEC1BA287502D29D0C9FFB260DD31AB90D0`
- invocation-binding manifest:
  `50614001EF125A035EB78EB9C796BF3BFEEC6E0017A4206FCBA01402FF63A3F2`
- partial outer trace MAT:
  `E3EC398D6B2A5284A07941D74C4DA6FB5C460BC61D373A860C7D024CD86C7EAF`
- terminal status:
  `B36EA498862231AF914B9922B1A9581E405EFAE05893BEF8CE4D459B8F1BA5D9`
- trace summary:
  `F15DBA7B9FF42C7F2169CD7850543FB1DEDDDFE85640BCCFE7D49A2AD7CEE90C`
- launcher stdout/stderr:
  `40C4EFDC4091569931CA49827AC60AB131BCD424AF69AB54A9772C7B8F7C55E6`
- run manifest:
  `AE078A56AF7FA22F87049A037E9151C9D8BEC76153659946AA937C26F82D215E`.

Also reverify the frozen path-normalized candidate wrapper and scientific invocation body identities from the accepted remediation report:

- candidate wrapper:
  `DA998FB04C35EE852F53A504D5F4EB17EC089A8EC616A082F38E2B5CB2CD5A93`
- scientific invocation body:
  `80BAEDE65829F6A1215638F556544C92CAAB203A149FA6D1D88196BE22045F45`.

The predecessor run root, remediation package, protected MATLAB tree, canonical data, and preserved baseline are strictly read-only.

## 5. Primary audit object: complete `MP4B_OBS` state/schema contract

Read the exact copied `MP4B_OBS.m` used in the failed run and every copied source call site that invokes it, especially:

- copied `HANK_mp_1eq.m`;
- copied `HANK_mp_1turn.m`;
- copied `HANK_firm.m`;
- any wrapper terminal/exception serialization call.

Build a complete event-by-event observability contract table. For every observer operation/event, record:

- event/action name;
- exact call site file and source-order location;
- exact arguments passed;
- intended turn index;
- intended province index;
- destination trace field/path;
- destination container created by initialization;
- initialized MATLAB type/class implied by source (`double`, `logical`, `struct`, cell, string/char, etc.);
- initialized shape;
- assigned runtime value type implied by the call-site expression;
- assigned shape;
- scalar/vector/struct nesting requirements;
- whether direct `()` indexing is type-compatible;
- whether `{}` or struct-field assignment would be required in a future repair;
- whether the event can occur multiple times per turn/province;
- whether missing events are semantically distinguishable from zero-valued events;
- failure risk classification.

Do not stop after `household_inputs`.

Audit **every trace field and every observer action** so that another one-shot is not wasted on the next latent struct/cell/type mismatch.

## 6. Exact failed assignment adjudication

For the observed `household_inputs(i)` failure, determine statically and exactly:

1. how `household_inputs` was initialized;
2. its resulting MATLAB class/shape;
3. the exact value passed by the `HANK_mp_1turn` observer call;
4. the value's intended class/shape;
5. why MATLAB attempts a struct-to-double conversion;
6. whether the defect is:
   - container initialization only;
   - indexing mode only;
   - both;
   - or a deeper event-schema mismatch.

Use one exact classification:

- `MP4B_OBS_HOUSEHOLD_INPUT_CONTAINER_INITIALIZATION_TYPE_MISMATCH_CONFIRMED`
- `MP4B_OBS_HOUSEHOLD_INPUT_INDEXING_MODE_MISMATCH_CONFIRMED`
- `MP4B_OBS_HOUSEHOLD_INPUT_CONTAINER_AND_INDEXING_SCHEMA_MISMATCH_CONFIRMED`
- `MP4B_OBS_HOUSEHOLD_INPUT_FAILURE_ROOT_UNRESOLVED`.

Do not edit the helper.

## 7. Full latent-defect sweep

Perform a bounded static sweep for analogous defects in all observer data structures.

At minimum inspect:

- turn container initialization;
- per-province preallocation;
- household input/output slots;
- migration slots;
- capital/`rah` slots;
- firm input/pre-clip/output slots;
- composite wage/Taylor/fiscal/controller slots;
- action/event labels;
- booleans/logicals;
- vectors versus scalars;
- raw/source province names;
- terminal/exception persistence;
- summary counters.

Flag any field where the initializer type/shape is incompatible with at least one statically visible assignment.

For each flagged latent defect give:

- exact field/action;
- exact initializer;
- exact assignment expression;
- exact type/shape conflict;
- whether it would necessarily fail, conditionally fail, silently coerce, overwrite prior evidence, or miscount evidence.

Use the strongest supported global classification:

- `MP4B_OBS_SINGLE_CONTAINER_DEFECT_LOCALIZED_NO_OTHER_STATIC_SCHEMA_BLOCKERS`
- `MP4B_OBS_MULTIPLE_STATIC_SCHEMA_DEFECTS_LOCALIZED`
- `MP4B_OBS_INITIALIZATION_SCHEMA_AUDIT_INCOMPLETE_OR_AMBIGUOUS`.

## 8. Trace-accounting semantics audit

Independently audit all summary and call-count fields produced by `MP4B_OBS` / wrapper persistence.

The predecessor establishes a concrete discrepancy:

- `instrumented_trace_summary.json` reports `household_call_count=31`;
- controlling stack evidence proves completed HJB/household calls = `0`;
- report states the summary used a formula equivalent to `numel(turns)*31`.

Determine exactly:

- where each summary counter is computed;
- whether it counts attempted slots, scheduled calls, entered calls, completed calls, or inferred calls;
- whether a failed partial turn can inflate counts;
- whether any other counters can similarly overstate executed science;
- whether controller/firm/Zt/GovInv counts are based on actual observer events or inferred from allocated structures.

Freeze a future accounting contract, **specification only**, in which each counter has an explicit semantic label such as:

- `scheduled_household_slots`;
- `household_call_entries`;
- `household_call_completions`;
- `firm_call_entries/completions`;
- `controller_evaluations`;
- `low_action_events`;
- `high_action_events`;
- `zt_reset_events`.

The audit must require event-derived execution counts rather than allocation-derived counts for future scientific ledgers.

If supported, establish:

`MP4B_OBS_ALLOCATION_DERIVED_HOUSEHOLD_CALL_COUNT_SEMANTIC_DEFECT_CONFIRMED`

This is an observability/accounting defect, not a scientific-model defect.

## 9. Partial trace evidence boundary

Inspect `instrumented_outer_trace.mat` and related JSON only to determine what evidence was actually written before failure.

Do not use the partial trace for MATLAB/Python chronology adjudication.

Report separately:

- outer turn entry evidence that is valid;
- province entries initialized but not scientifically executed;
- observer fields filled before failure;
- fields merely preallocated/defaulted;
- fields never reached;
- any summary claims that must not be interpreted as executed model calls.

Establish a clear distinction between:

`OBSERVED_EVENT`

and

`PREALLOCATED_OR_INFERRED_SLOT`.

No causal or parity inference is permitted from preallocated/default values.

## 10. No repair in this task

This task MUST NOT:

- edit predecessor `MP4B_OBS.m`;
- edit copied instrumentation files;
- create an executable repaired observer/helper;
- create or modify a MATLAB wrapper;
- invoke MATLAB;
- mutate the predecessor run root;
- mutate the remediation package;
- publish a future MATLAB execution task;
- declare a new MATLAB one-shot authorized.

It MAY provide a **minimal remediation specification** in prose/pseudocode/diff-outline form only, sufficient for Owner/L3 review.

That specification must enumerate every required future observability-only change, with no scientific-state changes.

## 11. Reauthorization-readiness decision

This zero-science audit must end with exactly one readiness classification:

### A. Ready after bounded helper remediation

`MP4B_ZERO_SCIENCE_OBSERVABILITY_HELPER_INITIALIZATION_AUDIT_READY_FOR_OWNER_REAUTHORIZATION_REVIEW`

Allowed only if:

- the failed assignment is exactly explained;
- the full observer schema has been audited;
- all statically visible latent type/shape/accounting defects are enumerated;
- a bounded observability-only remediation specification is complete;
- no unresolved ambiguity could plausibly consume a future one-shot before scientific execution.

Recommendation may then be:

`OWNER_REVIEW_OF_BOUNDED_OBSERVABILITY_HELPER_REMEDIATION_WARRANTED`

This is **not** authorization to repair or rerun MATLAB.

### B. Not ready

`MP4B_ZERO_SCIENCE_OBSERVABILITY_HELPER_INITIALIZATION_AUDIT_NOT_READY_FOR_REAUTHORIZATION`

Use if any schema/call-site/accounting ambiguity remains that requires another zero-science diagnostic before a safe repair can be specified.

### C. Blocked

`MP4B_ZERO_SCIENCE_OBSERVABILITY_HELPER_INITIALIZATION_AUDIT_BLOCKED`

Use on identity/readability/provenance failure.

## 12. Scientific interpretation limits

This task cannot establish or change any of the following accepted scientific facts:

- `MP4B_FINAL_GOVINV_CONTROLLER_BRANCH_COUNT_DIFFERENCE_LOCALIZED`;
- `MP4B_MATLAB_PROFILE_LOW_GOVINV_BRANCH_EXECUTION_COUNT_EXCEEDS_PYTHON_BY_ONE`;
- `MP4B_FINAL_WAGE_BOUNDARY_CATEGORY_MISMATCH_CONFIRMED_ORDER_INVARIANT`.

It cannot establish:

- MATLAB/Python stationary parity;
- chronological first divergence;
- extra low-return turn/province;
- extra Zt-reset turn/province;
- MATLAB legacy defect;
- Python implementation defect;
- IRF validity.

The current blocker is instrumentation infrastructure only.

## 13. Required external audit artifacts

Use one fresh no-overwrite audit root under `D:\ProjectTemp`, recommended:

`D:\ProjectTemp\ch5-mp4b-observability-helper-initialization-audit-20260831-001`

If it exists, choose the next deterministic fresh suffix; do not delete or overwrite.

Persist at minimum:

- `observer_event_schema.json`;
- `observer_initializer_assignment_matrix.json`;
- `trace_accounting_semantics.json`;
- `partial_trace_evidence_boundary.json`;
- `minimal_remediation_specification.md`;
- `audit_manifest.json` with SHA-256 and source identities.

No copied/repaired MATLAB code is required or authorized.

## 14. Repository change boundary

Required report:

`docs/CH5_TWO_ASSET_HANK_MP4B_ZERO_SCIENCE_OBSERVABILITY_HELPER_INITIALIZATION_AND_TRACE_ACCOUNTING_AUDIT_REPORT.md`

Allowed repository changes:

- exactly the required report;
- at most one strictly necessary CURRENT roadmap/status line if truly needed.

Do not change scientific code, MATLAB files, validators, comparators, contracts, tests, canonical data, project rules, prior reports, or tasks.

## 15. Closeout

At completion report:

- terminal verdict;
- readiness classification;
- live continuity;
- immutable identities;
- zero-science ledger;
- exact failed-assignment root classification;
- complete observer event/schema table;
- complete initializer/assignment compatibility matrix;
- latent-defect classification;
- trace-accounting audit;
- whether `MP4B_OBS_ALLOCATION_DERIVED_HOUSEHOLD_CALL_COUNT_SEMANTIC_DEFECT_CONFIRMED` is established;
- partial trace evidence boundary;
- minimal remediation specification;
- unresolved ambiguities, if any;
- explicit statement that no repair/reauthorization occurred;
- external artifact paths/sizes/SHA-256;
- `git diff --check`;
- changed paths;
- forbidden-operation audit;
- exactly one execution commit;
- non-force push;
- fresh GitHub read-back;
- `HEAD == origin/main`;
- ahead/behind `0/0`;
- clean worktree;
- exactly one recommended next gate.

Do not auto-publish or execute a later helper repair or MATLAB rerun task.
