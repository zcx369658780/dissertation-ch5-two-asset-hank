# CH5_TWO_ASSET_HANK_POST_P5_D2_HETEROGENEOUS_RESULT_SCHEMA_AUTHORITY_AND_RESUMPTION

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Resolve the D2 result-schema authority contradiction exposed by the latest fail-closed report, then resume the already accepted post-P5 household-decision parity experiment without changing any household science.

Controlling predecessor evidence includes:

- `tasks/CH5_TWO_ASSET_HANK_POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_MAP_PARITY.md`
- `tasks/CH5_TWO_ASSET_HANK_POST_P5_HOUSEHOLD_DECISION_MAP_PARITY_MATLAB_STRUCT_HARNESS_CORRECTION_AND_RESUMPTION.md`
- `tasks/CH5_TWO_ASSET_HANK_POST_P5_D2_HETEROGENEOUS_CASE_CONTAINER_CORRECTION_AND_RESUMPTION.md`
- `tasks/CH5_TWO_ASSET_HANK_POST_P5_D2_RESULT_CONTAINER_PREALLOCATION_SERIALIZATION_CORRECTION_AND_RESUMPTION.md`
- `docs/CH5_TWO_ASSET_HANK_POST_P5_HOUSEHOLD_DECISION_MAP_PARITY_MATLAB_STRUCT_HARNESS_CORRECTION_AND_RESUMPTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_POST_P5_D2_HETEROGENEOUS_CASE_CONTAINER_CORRECTION_AND_RESUMPTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_POST_P5_D2_RESULT_CONTAINER_PREALLOCATION_SERIALIZATION_CORRECTION_AND_RESUMPTION_REPORT.md`

Latest accepted terminal classification:

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The latest report establishes that the prior task's presumed homogeneous 17-field D2 row does not exist. The accepted D2 evaluator instead contains:

Normal decision row schema, 16 fields:

`id, c, l, d, cost, mu_a, mu_b, utility, hamiltonian, a_direction, b_direction, lambda_a, lambda_b, kkt_max, boundary_feasible, boundary_violation`

Near-tie row schema, 10 fields:

`id, canonical, raw, alias_available, gap, bound, boundary_feasible, kkt_max, mu_a, mu_b`

The near-tie row is the frozen case `lower_b_fz_near_tie` unless static source inspection proves otherwise.

P5 remains Owner-accepted:

`MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`

The voluntary hold remains:

`DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`

## 2. D1 remains frozen accepted evidence

D1 must not be rerun.

Accepted result:

- `432/432 PASS`;
- `216/216` low-`a` PASS;
- every compared scalar maximum absolute difference `0`;
- transfer-sign mismatch `0`;
- `a`-direction mismatch `0`;
- `b`-direction mismatch `0`.

Accepted D1 artifacts:

- MATLAB `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`
- Python `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`
- comparison `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`

D1 call budget in this task is exactly `0/0/0`.

## 3. Live authority and continuity

Task-authoring parent observed before publication:

`a7b13f44d3b1df754ff8e5c09dd121ce0aef26d1`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main`;
3. confirm all controlling predecessor tasks/reports exist;
4. record live start SHA;
5. verify P5 marker and active dynamic hold;
6. verify accepted Python `src/tests` continuity from baseline `7a2388a2ba89073e307f05a909570e8c40a4be13` using:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

It must be empty.

## 4. Required static schema audit before any execution

Before writing a corrected harness or running any preflight, inspect read-only:

- accepted input-corrected D2 MATLAB harness SHA-256 `57FFAD7DA9DCBA043EC40B21C647AD8621E1D973C9670A7C73EF0E2E5F6F868E`;
- frozen D2 Python harness SHA-256 `DD9DDCB675BE7A5C3A672CF1936AB7CBA1553AC8334989B2CDAA777FB2914344`;
- frozen comparison harness SHA-256 `5C6FDBEBDA8BA67D819E69808A43C076E8F7BCB3C85788DABD942CC35EB40BE7`;
- frozen ten D2 case definitions from manifest SHA-256 `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA`.

Confirm and report:

1. exact case ID corresponding to the 10-field near-tie schema;
2. exact number of normal 16-field rows versus near-tie 10-field rows;
3. exact Python output schema for every D2 case type;
4. whether the frozen comparator already branches by case ID/schema;
5. whether top-level heterogeneous JSON objects can be consumed by the frozen Python/comparison side without changing any scientific comparison rule.

If the observed source contradicts the two schemas stated above, stop before execution and report the smallest exact contradiction. Do not guess.

## 5. Frozen D2 serialization authority

If the static audit confirms the stated schemas, the accepted serialization contract for D2 is hereby frozen as:

`D2_HETEROGENEOUS_JSON_ARRAY_PRESERVE_NATIVE_CASE_SCHEMA`

Meaning:

1. The top-level D2 output is one ordered JSON array containing exactly 10 row objects.
2. Every non-near-tie case retains the exact existing 16-field normal row schema, with no added placeholder fields.
3. The frozen near-tie case retains its exact existing 10-field near-tie schema, with no added placeholder fields.
4. No 17-field row is invented.
5. No 21-field union row is created.
6. Missing fields are represented by field absence, not fabricated zeros, NaNs, nulls, or defaults.
7. Row order remains exactly the frozen D2 case order.
8. MATLAB may use a heterogeneous cell array of scalar structs solely as external serialization plumbing, e.g. each cell stores one already-computed row struct before `jsonencode`.
9. This serialization decision changes no household equation, root, KKT condition, multiplier, policy value, tolerance, case definition, or expected scientific result.

The reason for choosing heterogeneous serialization is preservation: it preserves both existing scientific output schemas exactly rather than inventing a common schema.

## 6. D2 comparison authority under heterogeneous schemas

If static audit confirms the predecessor intent, freeze comparison by case type:

### Normal D2 cases

For every normal 16-field case compare the existing scientific outputs:

- `c`
- `l`
- `d`
- `cost`
- `mu_a`
- `mu_b`
- `utility`
- `hamiltonian`
- `a_direction`
- `b_direction`
- `lambda_a`
- `lambda_b`
- `kkt_max`
- `boundary_feasible`
- `boundary_violation` where the frozen comparator/source defines it.

### Near-tie D2 case

For the 10-field `lower_b_fz_near_tie` case compare exactly the existing near-tie outputs:

- `canonical`
- `raw`
- `alias_available`
- `gap`
- `bound`
- `boundary_feasible`
- `kkt_max`
- `mu_a`
- `mu_b`

Do not invent unavailable `c/l/d/cost/utility/H/lambda` fields for this special canonicalization case.

The near-tie case remains a policy-selection/canonicalization test rather than a full normal-row control report. D1 already provides full primitive decision coverage over the corrected common equations.

If the frozen Python/comparator source contradicts this case-specific interpretation, stop and report the contradiction before execution.

## 7. Phase A — correct only D2 output serialization plumbing

Work in a fresh no-overwrite external artifact root. Do not modify predecessor roots.

Start from accepted input-corrected D2 MATLAB harness SHA-256:

`57FFAD7DA9DCBA043EC40B21C647AD8621E1D973C9670A7C73EF0E2E5F6F868E`

Preserve the accepted input traversal exactly:

- decoded `m.p2` is `10x1 cell`;
- `get_case` / `container{k}` extraction remains unchanged.

Create a corrected D2 MATLAB harness that changes only result-container/serialization plumbing so it can hold the existing heterogeneous row structs and emit the frozen 10-object JSON array.

Allowed changes only:

- external callable/file-name alignment;
- heterogeneous result container declaration, such as a cell array;
- insertion of already-computed row structs into that container;
- `jsonencode` / file-write plumbing for that container;
- schema-preserving read-back checks.

Every changed line must be classified as exactly one of:

- `HETEROGENEOUS_RESULT_CONTAINER_ONLY`
- `RESULT_SERIALIZATION_ONLY`
- `EXTERNAL_CALLABLE_ALIGNMENT_ONLY`

Forbidden changes include any scientific formula, case field, root, KKT equation, multiplier recovery, policy decision, O1 behavior, constant-`r_a` drift, parameter, state/shadow input, tolerance, or expected answer.

## 8. Mandatory no-model heterogeneous-result preflight

Before any replacement D2 scientific call, freeze/hash/read back the corrected harness, preflight, unchanged manifest, unchanged Python/comparison/D3 harnesses, complete diff, and execution ledger.

Run exactly one engineering-only MATLAB preflight that does not call any household scientific function.

It must:

1. construct at least one synthetic 16-field normal row and one synthetic 10-field near-tie row using the exact schemas above;
2. store them in the exact heterogeneous result container intended by D2;
3. serialize to a two-object JSON array;
4. read back and prove object 1 retains exactly 16 keys and object 2 exactly 10 keys, with no fabricated union fields;
5. verify representative values and types survive;
6. additionally traverse all 10 frozen D2 input case IDs using the already accepted `get_case` path without evaluating science;
7. verify frozen order and unique IDs;
8. exit zero.

The preflight must not call:

- `HANK_2ASSETS_HJB`;
- production `HANK3_FOC`;
- accepted O1 FOC;
- `HANK3_cost`;
- `lab_solve2`;
- any D2 root/KKT/scientific evaluator;
- Python.

If preflight fails, no replacement D2 scientific call is allowed.

## 9. Exactly one replacement D2 MATLAB call

Historical consumed D2 MATLAB calls remain recorded separately:

1. input-container blocker: `1`;
2. output zero-field struct blocker: `1`.

The latest schema-authority task consumed `0` scientific calls.

This task explicitly authorizes exactly one new replacement D2 MATLAB scientific call after successful static audit and preflight.

Requirements before advancing:

- exit zero;
- `d2_matlab.json` exists;
- top-level array length exactly 10;
- frozen order preserved;
- normal rows retain exact 16-field schemas;
- near-tie row retains exact 10-field schema;
- no fabricated fields;
- all required values finite where required;
- independent read-back succeeds.

If the replacement D2 MATLAB call fails, do not repair or rerun it in this task.

## 10. Complete D2 and D3 conditionally

Only after valid D2 MATLAB persistence:

### D2 Python and comparison

Run each exactly once.

Do not modify Python production source/tests.

If the frozen external comparator needs a purely serialization/schema-dispatch correction to consume the now-authorized heterogeneous JSON array, such a change is allowed only if:

- static audit first proves the existing comparator cannot consume it;
- the change does not alter any field comparison, tolerance, case ordering, expected value, PASS/FAIL rule, or scientific computation;
- every changed line is classified `COMPARATOR_SCHEMA_DISPATCH_ONLY`;
- a no-science JSON comparator preflight is run before the scientific comparison.

If any broader comparator change would be required, stop and report blocked rather than broadening scope.

For D2, compare normal cases by the normal schema and the near-tie case by the near-tie schema exactly as frozen in Section 6.

If any valid scientific mismatch occurs, stop before D3 and classify material contradiction.

### D3

If D2 passes, execute the unchanged frozen D3 sequence:

- MATLAB decision harness: `1`;
- Python decision harness: `1`;
- comparison: `1`.

Use exactly the frozen 360 `gamma_c=2`, Python `phi=5`, MATLAB `frisch_l=.2` cases. No D3 science may change.

## 11. Call budget

D1 in this task: exactly `0/0/0`.

Engineering-only calls:

- heterogeneous-result MATLAB preflight: at most `1`;
- comparator schema-dispatch preflight: at most `1` only if a comparator plumbing correction is statically proven necessary.

Scientific calls:

- replacement D2 MATLAB: exactly `1` if preflight passes;
- D2 Python: at most `1` after valid MATLAB persistence;
- D2 comparison: at most `1`;
- D3 MATLAB/Python/comparison: at most `1/1/1` after D2 PASS.

No full HJB, Python HJB/KFE/steady-state, P3/P4/R4, asset-tail, AR(1), transition, IRF, calibration-extension, dynamics, or Results call is authorized.

## 12. Terminal classifications

Return exactly one.

### PASS

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_PASS__DYNAMIC_HOLD_MAY_ADVANCE_TO_ASSET_TAIL_GATE`

Use only if:

- static schema audit confirms the frozen heterogeneous contract;
- D1 accepted evidence is reused with zero calls;
- heterogeneous-result plumbing diff remains within authority;
- preflight passes;
- replacement D2 MATLAB persists all 10 rows with native schemas;
- D2 all normal cases and the near-tie case pass their case-specific frozen comparisons;
- D3 all 360 cases pass;
- no forbidden mutation/rerun occurs.

### Material contradiction

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_MATERIAL_CONTRADICTION__DYNAMIC_HOLD_CONTINUES`

Use if a valid D2 or D3 comparison shows a scientific mismatch under the accepted equations.

P5 is not automatically revoked.

### Blocked

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

Use if source schema contradicts this authority, plumbing cannot remain non-scientific, preflight fails, replacement persistence fails, comparator requires broader changes, or D3 hits a new source/environment blocker.

## 13. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_POST_P5_D2_HETEROGENEOUS_RESULT_SCHEMA_AUTHORITY_AND_RESUMPTION_REPORT.md`

Report at minimum:

1. terminal classification;
2. live start/final `origin/main`;
3. Python `src/tests` continuity;
4. predecessor/successor artifact roots;
5. protected identities;
6. D1 artifact re-verification and exact zero-call confirmation;
7. complete static audit of MATLAB/Python/comparator D2 schemas;
8. exact normal and near-tie case IDs/counts/schemas;
9. frozen serialization authority applied;
10. complete corrected MATLAB diff with line classifications;
11. preflight hashes/results;
12. historical D2 call ledger plus new replacement count;
13. D2 MATLAB/Python/comparison call counts;
14. D2 normal-case per-field max differences/worst cases;
15. D2 near-tie categorical/numerical comparison;
16. D2 KKT/boundary mismatch counts;
17. D3 360-case per-field max differences/worst cases if reached;
18. scientific mismatch list;
19. source/environment failure list;
20. forbidden-operation check;
21. git status;
22. acceptance level;
23. exact recommended next gate.

## 14. Explicit prohibitions

Do not:

- rerun D1;
- invent a seventeenth D2 field;
- create a 21-field union schema;
- fabricate zeros/NaNs/nulls/defaults for fields absent from a native case schema;
- delete the near-tie case;
- convert the near-tie case into a normal case;
- change any D2/D3 scientific case/order/equation/parameter/state/shadow/derivative/tolerance;
- modify MATLAB/Python production source/tests/helpers/cache;
- add the MATLAB taper;
- use production bare-`a` FOC as corrected oracle;
- add `Tt`/`rb_gap` adapters;
- import or hard-code Python expected values into MATLAB;
- widen comparison tolerances;
- repair/rerun a failed scientific stage in this same task;
- run full HJB/KFE/steady state or P3/P4/R4;
- enter asset-tail testing, AR(1), transition, IRF, dynamics, calibration extension, or Results;
- revoke or reissue P5 automatically.

## 15. Recommended next gate rule

If PASS, recommend only the already identified upper-`a` asset-tail robustness gate before actual dynamic execution.

If scientific contradiction, recommend only the smallest Owner/reviewer diagnosis of the exact mismatched decision object.

If blocked, recommend only the smallest new source/environment correction required by the newly observed blocker.
