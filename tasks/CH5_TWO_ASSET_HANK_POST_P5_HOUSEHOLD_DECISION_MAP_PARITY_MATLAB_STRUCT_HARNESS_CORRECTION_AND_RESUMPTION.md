# CH5_TWO_ASSET_HANK_POST_P5_HOUSEHOLD_DECISION_MAP_PARITY_MATLAB_STRUCT_HARNESS_CORRECTION_AND_RESUMPTION

Date: 2026-08-29

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Resume the accepted post-P5 household-decision parity experiment after a single external MATLAB harness-container failure.

The predecessor task remains the controlling scientific specification:

`tasks/CH5_TWO_ASSET_HANK_POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_MAP_PARITY.md`

The predecessor report is accepted as a source/environment blocker only:

`docs/CH5_TWO_ASSET_HANK_POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_MAP_PARITY_REPORT.md`

Accepted predecessor terminal classification:

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The only reached failure was external `decision_matlab.m:9`, where `rows(k)=row(...)` attempted assignment between dissimilar MATLAB structures. No `d1_matlab.json` was produced, no D1 cross-language comparison occurred, and there is no scientific mismatch evidence.

This successor authorizes only the minimum external harness correction needed to make result aggregation/serialization valid, followed by one replacement D1 MATLAB call and, conditional on success, the remainder of the already frozen D1 -> D2 -> D3 sequence.

P5 remains Owner-accepted under:

`MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`

The voluntary route hold remains:

`DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`

## 2. Live authority and continuity

Task-authoring parent observed before publication:

`cc5a6586737e27ebe15422892fd27aecb28d1ddf`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task and the predecessor task/report exist on live `main`;
3. record live start SHA;
4. verify Owner P5 acceptance remains present;
5. verify accepted Python `src/tests` continuity from baseline `7a2388a2ba89073e307f05a909570e8c40a4be13` using:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

It must be empty.

## 3. Required reads

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `tasks/CH5_TWO_ASSET_HANK_POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_MAP_PARITY.md`
- `docs/CH5_TWO_ASSET_HANK_POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_MAP_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_P5_OWNER_FINAL_ACCEPTANCE_DECISION.md`
- every source/evidence file required by the predecessor task that is needed to execute D1/D2/D3 unchanged.

The predecessor task controls every scientific equation, case, parameter, tolerance, comparison field and D2/D3 rule except where this task explicitly authorizes the consumed D1 replacement call and the external struct-container correction.

## 4. Frozen predecessor identities to preserve

Predecessor external artifact root:

`D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-artifacts-20260829-220000`

Frozen predecessor identities:

- `manifest.json` SHA-256 `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA`
- original blocked `decision_matlab.m` SHA-256 `C758F97CB4AF7F372595D4425064E6DDF1B8BE230C42CB1264CFF34066E94202`
- `decision_python.py` SHA-256 `6054A0C59E7C0CD0C83AD1919C3CFAF7B2987D0545EE4CEB26B3345FF2D01ABC`
- `d2_matlab.m` SHA-256 `8067196C2C680926490B6231EE2FF3125DD43B26AB812A1566719043E270C7C9`
- `d2_python.py` SHA-256 `DD9DDCB675BE7A5C3A672CF1936AB7CBA1553AC8334989B2CDAA777FB2914344`
- `compare.py` SHA-256 `5C6FDBEBDA8BA67D819E69808A43C076E8F7BCB3C85788DABD942CC35EB40BE7`
- predecessor execution ledger SHA-256 `88DAC099829318A85691040588AEB17150ED2356AE95C968835D7B954E13D703`

Protected MATLAB/Python scientific identities remain exactly those required by the predecessor task. No production source/helper/test/cache mutation is authorized.

## 5. Scientific content is immutable

Do not change any predecessor scientific content.

The following remain byte/value/semantic identical to the predecessor freeze:

- all 432 D1 cases and ordering;
- all 10 D2 cases and ordering;
- all 360 D3 cases and ordering;
- all economic parameters;
- all state/shadow inputs;
- `mu_a = r_a*a + d`;
- `m(a)=max(a,a_bar)`;
- accepted O1 MATLAB low-`a` FOC behavior;
- labor-curvature mapping;
- common-budget scope;
- all comparison fields;
- all tolerances;
- all stop/fail-closed rules except the explicitly authorized replacement D1 MATLAB call.

Do not regenerate a scientifically different manifest. Reuse the predecessor manifest after identity verification.

## 6. Phase A — diagnose and correct only the MATLAB result-container plumbing

Work in a fresh no-overwrite external artifact root. Do not modify the predecessor artifact root.

Read the blocked `decision_matlab.m` and identify the exact reason why `rows(k)=row(...)` produces dissimilar-structure assignment.

Create a corrected replacement `decision_matlab_corrected.m` subject to all constraints below.

Allowed edits are only external result-container plumbing, such as:

- struct preallocation/schema construction;
- field-order/schema normalization where required solely for MATLAB struct-array assignment;
- assignment into the result array/cell container;
- final conversion to a JSON-serializable homogeneous structure;
- output-file serialization plumbing if required by the same container defect.

Forbidden edits include any change to:

- scientific case loading;
- formulas;
- O1 helper selection;
- parameter values;
- shadow inputs;
- decision calculation;
- drift calculation;
- utility/Hamiltonian calculation;
- sign/direction classification;
- tolerances;
- row contents/field values produced by the scientific evaluator.

Produce a complete original-versus-corrected diff and classify every changed line. Every changed line must be `RESULT_CONTAINER_OR_SERIALIZATION_ONLY`.

If the failure cannot be corrected within this boundary, stop before any replacement scientific call.

## 7. Phase B — mandatory no-model synthetic struct preflight

Before the replacement D1 MATLAB call, create a separate synthetic MATLAB preflight that does not call `HANK_2ASSETS_HJB`, `HANK3_FOC`, O1 FOC, `HANK3_cost`, `lab_solve2`, Python, or any scientific evaluator.

The preflight must:

1. construct at least two synthetic row structs with the exact field schema and representative scalar/string/logical/array types expected from the corrected D1 result rows;
2. exercise the corrected preallocation/container assignment path for multiple rows;
3. serialize the resulting container using the same JSON path intended by D1;
4. read the JSON back or otherwise verify row count and field schema;
5. exit zero.

This preflight is engineering-only and does not consume a scientific call.

Freeze/hash/read back before running it:

- corrected MATLAB harness;
- synthetic preflight;
- unchanged predecessor manifest and unchanged Python/D2/comparison harnesses;
- a new successor execution ledger.

If preflight fails, no D1 replacement call is allowed.

## 8. Phase C — exactly one replacement D1 MATLAB call

The predecessor D1 MATLAB call was consumed by an external container defect before valid persistence. This task explicitly authorizes exactly **one replacement D1 MATLAB scientific call** using the corrected harness.

The replacement call must use the exact predecessor 432 D1 cases, parameters, equations, O1 helper, ordering and tolerances.

Acceptance before advancing:

- process exits zero;
- `d1_matlab.json` exists;
- it contains exactly 432 rows in the frozen order;
- every required field exists on every row;
- all required values are finite where the predecessor contract requires finiteness;
- output can be parsed/read back independently.

If the replacement D1 MATLAB call fails for any reason, do not repair or rerun it in this task. Stop fail-closed.

## 9. Phase D — resume the original D1 -> D2 -> D3 sequence conditionally

Only after Phase C valid persistence:

### D1 remainder

Run exactly once each:

- D1 Python scientific harness;
- D1 comparison.

Apply the predecessor D1 acceptance contract unchanged. If any scientific mismatch occurs, stop before D2.

### D2

If D1 passes, execute the predecessor D2 stage exactly as originally authorized:

- MATLAB accepted-equation evaluator: 1 call;
- Python production evaluator: 1 call;
- comparison: 1 call.

Do not proactively edit `d2_matlab.m`. If D2 encounters a new source/environment/harness blocker, stop and report it; no same-task repair is authorized.

If any D2 scientific mismatch occurs, stop before D3.

### D3

If D2 passes, execute the predecessor D3 stage exactly as originally authorized:

- MATLAB decision harness: 1 call using the corrected result-container plumbing and the exact frozen D3 cases;
- Python decision harness: 1 call;
- comparison: 1 call.

If the corrected D1 harness and D3 share one common decision evaluator, the scientific formula portion must remain identical to the predecessor; only the already-audited result-container fix may be reused.

No rerun is allowed.

## 10. Exact call budget

Engineering-only synthetic struct preflight: at most 1 MATLAB invocation.

Scientific calls in this successor:

- replacement D1 MATLAB: exactly 1 if preflight passes;
- D1 Python: at most 1, only after valid D1 MATLAB persistence;
- D1 comparison: at most 1;
- D2 MATLAB/Python/comparison: at most `1/1/1` conditional on D1 PASS;
- D3 MATLAB/Python/comparison: at most `1/1/1` conditional on D2 PASS.

The consumed predecessor D1 MATLAB call must be reported separately as historical count `1`, not silently erased.

No full HJB, KFE, steady-state, P3/P4/R4, asset-tail or dynamics call is authorized.

## 11. Terminal classifications

Return exactly one.

### All D1/D2/D3 pass

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_PASS__DYNAMIC_HOLD_MAY_ADVANCE_TO_ASSET_TAIL_GATE`

Use only if:

- corrected harness diff is container/serialization-only;
- synthetic preflight passes;
- replacement D1 MATLAB persists all 432 rows;
- D1 all 432 cases pass;
- D2 all 10 cases pass;
- D3 all 360 cases pass;
- no forbidden mutation/rerun occurred.

### Scientific contradiction

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_MATERIAL_CONTRADICTION__DYNAMIC_HOLD_CONTINUES`

Use if a valid D1/D2/D3 comparison shows any material mismatch under the frozen accepted common equations.

P5 is not automatically revoked; report the exact contradiction for Owner/reviewer decision.

### Source/environment/harness blocked

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

Use if the corrected harness cannot be bounded to container-only changes, synthetic preflight fails, replacement D1 persistence fails, or a later D2/D3 harness/environment blocker occurs before a valid scientific comparison.

Do not convert missing comparison evidence into a PASS or FAIL.

## 12. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_POST_P5_HOUSEHOLD_DECISION_MAP_PARITY_MATLAB_STRUCT_HARNESS_CORRECTION_AND_RESUMPTION_REPORT.md`

The report must include:

1. terminal classification;
2. live start/final `origin/main`;
3. Python `src/tests` continuity;
4. predecessor and successor artifact roots;
5. all protected identities;
6. exact blocker diagnosis;
7. original-to-corrected MATLAB harness diff with per-line classification;
8. corrected harness/preflight/ledger hashes;
9. synthetic preflight result;
10. historical consumed D1 count and successor replacement call count separately;
11. exact D1/D2/D3 execution counts;
12. D1 432-case comparison summary, including low-`a` subset and per-field max difference/worst case if reached;
13. D2 10-case controls/directions/multipliers/KKT/boundary comparison if reached;
14. D3 360-case gamma-2/phi-5 comparison summary and per-field max difference/worst case if reached;
15. complete scientific mismatch list;
16. complete source/environment failure list;
17. forbidden-operation check;
18. git status;
19. acceptance level;
20. exact recommended next gate.

## 13. Explicit prohibitions

Do not:

- modify MATLAB production source/helpers/cache;
- modify Python production source/tests;
- alter any frozen scientific case or ordering;
- alter equations, calibration, grids, state/shadow values or tolerances;
- add the legacy `raah/Rah` taper;
- use production bare-`a` FOC as corrected oracle;
- add `Tt` or `rb_gap` adapters;
- change D2 scientific evaluator unless a later separately authorized task permits it;
- repair and rerun any replacement scientific stage in this same task;
- run full `HANK_2ASSETS_HJB`;
- run Python HJB/KFE/steady state;
- rerun P3/P4/R4;
- run upper-`a` asset-tail diagnostics;
- enter AR(1), transition, IRF, calibration extension, dynamics or Results;
- revoke or reissue P5 automatically.

## 14. Recommended next gate rule

If PASS, recommend only the already-identified post-P5 upper-`a` asset-tail robustness gate before actual dynamic execution.

If material contradiction, recommend the smallest Owner/reviewer scientific diagnosis of the exact mismatched decision object.

If blocked, recommend only the smallest new source/environment correction gate for the newly observed blocker.
