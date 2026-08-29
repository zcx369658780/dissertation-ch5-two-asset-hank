# CH5_TWO_ASSET_HANK_POST_P5_D2_COMPARATOR_FIELD_AUTHORITY_AND_HETEROGENEOUS_RESUMPTION

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Resolve the sole comparator-authority contradiction exposed by the accepted D2 heterogeneous-result-schema audit, then resume the already frozen post-P5 household-decision parity experiment.

Controlling predecessor evidence includes:

- `tasks/CH5_TWO_ASSET_HANK_POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_MAP_PARITY.md`
- `tasks/CH5_TWO_ASSET_HANK_POST_P5_HOUSEHOLD_DECISION_MAP_PARITY_MATLAB_STRUCT_HARNESS_CORRECTION_AND_RESUMPTION.md`
- `tasks/CH5_TWO_ASSET_HANK_POST_P5_D2_HETEROGENEOUS_CASE_CONTAINER_CORRECTION_AND_RESUMPTION.md`
- `tasks/CH5_TWO_ASSET_HANK_POST_P5_D2_RESULT_CONTAINER_PREALLOCATION_SERIALIZATION_CORRECTION_AND_RESUMPTION.md`
- `tasks/CH5_TWO_ASSET_HANK_POST_P5_D2_HETEROGENEOUS_RESULT_SCHEMA_AUTHORITY_AND_RESUMPTION.md`
- `docs/CH5_TWO_ASSET_HANK_POST_P5_HOUSEHOLD_DECISION_MAP_PARITY_MATLAB_STRUCT_HARNESS_CORRECTION_AND_RESUMPTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_POST_P5_D2_HETEROGENEOUS_CASE_CONTAINER_CORRECTION_AND_RESUMPTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_POST_P5_D2_RESULT_CONTAINER_PREALLOCATION_SERIALIZATION_CORRECTION_AND_RESUMPTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_POST_P5_D2_HETEROGENEOUS_RESULT_SCHEMA_AUTHORITY_AND_RESUMPTION_REPORT.md`

Latest accepted terminal classification:

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The latest accepted report establishes all of the following statically:

- D2 has exactly 9 normal rows with the native 16-field schema;
- D2 has exactly 1 near-tie row, `lower_b_fz_near_tie`, with the native 10-field schema;
- MATLAB and Python emit the same two native schemas;
- the frozen comparator already consumes heterogeneous JSON objects correctly;
- the comparator already checks near-tie `canonical`, `raw`, `alias_available`, `mu_a`, `mu_b`, `kkt_max`, and `boundary_feasible`;
- the comparator omits only the required near-tie numerical fields `gap` and `bound`;
- the prior task did not authorize expanding the comparison field set, so execution correctly stopped before any new preflight or scientific call.

This task explicitly resolves that authority gap and authorizes only the minimum comparator-field correction plus the already approved heterogeneous serialization/resumption route.

P5 remains Owner-accepted:

`MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`

The voluntary route hold remains:

`DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`

## 2. D1 remains frozen accepted evidence

D1 must not be rerun.

Accepted D1 result:

- `432/432 PASS`;
- `216/216` low-`a` cases PASS;
- maximum absolute difference `0` for every compared scalar field;
- transfer-sign mismatch `0`;
- `a`-direction mismatch `0`;
- `b`-direction mismatch `0`.

Accepted D1 artifacts:

- MATLAB `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`
- Python `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`
- comparison `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`

D1 MATLAB/Python/comparison call budget in this task is exactly `0/0/0`.

## 3. Live authority and continuity

Task-authoring parent observed before publication:

`1cbdfd5af2c1e462258c7784297a2cbede1dd90d`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main`;
3. confirm all controlling predecessor tasks/reports exist;
4. record live start SHA;
5. verify P5 marker and active dynamic hold;
6. verify accepted Python `src/tests` continuity from baseline `7a2388a2ba89073e307f05a909570e8c40a4be13` using:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

It must be empty.

## 4. Frozen scientific and serialization authority

All household science remains unchanged.

Use exactly:

- `mu_a = r_a*a + d`;
- `m(a)=max(a,a_bar)`;
- accepted O1 low-`a` MATLAB behavior;
- accepted labor-curvature mapping;
- all frozen D2/D3 cases, ordering, parameters, state/shadow/derivative inputs, roots, KKT equations, multiplier recovery, tolerances, and PASS/FAIL rules.

The accepted D2 serialization contract remains:

`D2_HETEROGENEOUS_JSON_ARRAY_PRESERVE_NATIVE_CASE_SCHEMA`

Normal D2 row, exactly 16 fields:

`id, c, l, d, cost, mu_a, mu_b, utility, hamiltonian, a_direction, b_direction, lambda_a, lambda_b, kkt_max, boundary_feasible, boundary_violation`

Near-tie D2 row, exactly 10 fields:

`id, canonical, raw, alias_available, gap, bound, boundary_feasible, kkt_max, mu_a, mu_b`

Do not invent a 17th field, do not create a union schema, and do not fabricate absent fields.

MATLAB may use a heterogeneous cell array of scalar structs solely as serialization plumbing.

## 5. Comparator field authority correction

This task explicitly authorizes changing the frozen external comparator only to add the two omitted near-tie fields:

- `gap`
- `bound`

The corrected D2 comparator field contract is hereby frozen as follows.

### Normal cases

Retain the existing comparison behavior and field set unchanged.

### Near-tie case `lower_b_fz_near_tie`

Compare exactly:

- `canonical`
- `raw`
- `alias_available`
- `gap`
- `bound`
- `boundary_feasible`
- `kkt_max`
- `mu_a`
- `mu_b`

`gap` and `bound` must use the same existing frozen floating-point comparison rule already used for ordinary numerical D2 fields:

`tau_fp(x,y) = 128*eps64*max(1,abs(x),abs(y))`

No new tolerance may be introduced and no existing tolerance may be widened.

No other comparator field, ordering, expected value, threshold, PASS/FAIL rule, aggregation logic, or scientific calculation may change.

Every comparator changed line must be classified exactly:

`COMPARATOR_NEAR_TIE_GAP_BOUND_ONLY`

If any additional comparator change would be required, stop before execution and report blocked.

## 6. Required static read-back before execution

Before creating any corrected artifact, statically re-verify:

- D2 MATLAB native 9+1 schemas;
- D2 Python native 9+1 schemas;
- frozen comparator behavior;
- exact near-tie case ID;
- frozen manifest and case ordering.

Confirm that the only comparator scientific-field omission remains `gap` and `bound`.

If another omitted or conflicting field is discovered, stop before modification and report the exact contradiction. Do not guess or broaden scope.

## 7. Phase A — create corrected external comparator and MATLAB heterogeneous serialization harness

Work in a fresh no-overwrite external artifact root. Do not modify predecessor roots.

### Comparator

Start from frozen comparator SHA-256:

`5C6FDBEBDA8BA67D819E69808A43C076E8F7BCB3C85788DABD942CC35EB40BE7`

Create a corrected comparator that differs only by adding near-tie `gap` and `bound` to the numerical comparison set under the existing `tau_fp` rule.

Produce a complete original-to-corrected diff and classify every changed line as:

`COMPARATOR_NEAR_TIE_GAP_BOUND_ONLY`

### MATLAB D2 serialization

Start from accepted input-corrected D2 MATLAB harness SHA-256:

`57FFAD7DA9DCBA043EC40B21C647AD8621E1D973C9670A7C73EF0E2E5F6F868E`

Preserve `get_case` and all scientific calculations unchanged.

Correct only the output container/serialization so the 9 native 16-field rows and 1 native 10-field near-tie row are preserved as an ordered heterogeneous JSON array.

Allowed MATLAB changed-line classifications are only:

- `HETEROGENEOUS_RESULT_CONTAINER_ONLY`
- `RESULT_SERIALIZATION_ONLY`
- `EXTERNAL_CALLABLE_ALIGNMENT_ONLY`

No scientific line may change.

## 8. Mandatory engineering-only preflights

Freeze/hash/read back before any scientific call:

- corrected MATLAB D2 harness;
- corrected comparator;
- unchanged scientific manifest;
- unchanged D2 Python harness;
- unchanged D3 MATLAB/Python harnesses;
- MATLAB heterogeneous-result preflight;
- comparator near-tie preflight;
- complete diffs;
- successor execution ledger.

### MATLAB heterogeneous-result preflight

At most 1 MATLAB invocation.

It must not call any household scientific function.

It must:

1. construct one synthetic 16-field normal row and one synthetic 10-field near-tie row;
2. store them using the exact corrected heterogeneous container;
3. serialize to a two-object JSON array;
4. read back and verify exact 16-key/10-key preservation with no fabricated fields;
5. traverse all 10 frozen D2 case IDs using accepted `get_case` input traversal without evaluating household science;
6. verify exact order and uniqueness;
7. exit zero.

### Comparator near-tie preflight

At most 1 Python engineering-only invocation.

It must not call any household evaluator.

It must create/read two synthetic matching heterogeneous D2 outputs where the near-tie row contains `gap` and `bound`, then verify:

- matching `gap` and `bound` pass;
- an intentionally perturbed `gap` beyond the frozen `tau_fp` fails;
- an intentionally perturbed `bound` beyond the frozen `tau_fp` fails;
- all existing near-tie categorical fields retain their previous comparison behavior;
- no normal-case comparison field or threshold changed.

This is comparator plumbing/contract validation only, not a scientific model call.

If either preflight fails, no replacement D2 scientific call is authorized.

## 9. Exactly one replacement D2 MATLAB scientific call

Historical consumed D2 MATLAB calls remain separately recorded:

1. input-container blocker: `1`;
2. zero-field output-container blocker: `1`;
3. subsequent schema/comparator authority tasks: scientific calls `0`.

This task explicitly authorizes exactly one new replacement D2 MATLAB scientific call after both preflights pass.

Requirements before advancing:

- exit zero;
- `d2_matlab.json` exists;
- exactly 10 ordered objects;
- first 9 rows preserve the native 16-field schema;
- `lower_b_fz_near_tie` preserves the native 10-field schema;
- no fabricated fields;
- independent JSON read-back succeeds;
- all required finite values are finite.

If this replacement D2 MATLAB call fails, do not repair or rerun it in this task.

## 10. Complete D2 and D3 conditionally

Only after valid D2 MATLAB persistence:

### D2 Python

Run the frozen D2 Python harness exactly once. Do not modify it.

### D2 comparison

Run the corrected comparator exactly once.

For the nine normal cases, retain the prior frozen comparisons unchanged.

For `lower_b_fz_near_tie`, compare exactly the nine fields in Section 5, including newly authorized `gap` and `bound` under existing `tau_fp`.

If any valid scientific mismatch occurs, stop before D3 and return material contradiction.

### D3

If D2 passes, execute unchanged frozen D3 exactly once each:

- MATLAB: `1`
- Python: `1`
- comparison: `1`

Use exactly the frozen 360 `gamma_c=2`, Python `phi=5`, MATLAB `frisch_l=.2` cases and all original D3 tolerances/fields.

No D3 scientific formula or case may change.

## 11. Call budget

D1 in this task: exactly `0/0/0`.

Engineering-only calls:

- MATLAB heterogeneous-result preflight: at most `1`;
- Python comparator near-tie preflight: at most `1`.

Scientific calls:

- replacement D2 MATLAB: exactly `1` if both preflights pass;
- D2 Python: at most `1` after valid MATLAB persistence;
- D2 comparison: at most `1`;
- D3 MATLAB/Python/comparison: at most `1/1/1` after D2 PASS.

No full HJB, Python HJB/KFE/steady-state, P3/P4/R4, asset-tail, AR(1), transition, IRF, calibration-extension, dynamics, or Results call is authorized.

## 12. Terminal classifications

Return exactly one.

### PASS

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_PASS__DYNAMIC_HOLD_MAY_ADVANCE_TO_ASSET_TAIL_GATE`

Use only if:

- static audit confirms only `gap`/`bound` were missing from comparator coverage;
- D1 evidence is reused with zero calls;
- comparator diff contains only the authorized two-field addition;
- MATLAB serialization diff remains plumbing-only;
- both engineering preflights pass;
- replacement D2 MATLAB persists all 10 native-schema rows;
- D2 all 10 cases pass, including near-tie `gap` and `bound`;
- D3 all 360 cases pass;
- no forbidden mutation/rerun occurs.

### Material contradiction

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_MATERIAL_CONTRADICTION__DYNAMIC_HOLD_CONTINUES`

Use if a valid D2 or D3 comparison shows a scientific mismatch under the frozen accepted equations.

P5 is not automatically revoked.

### Blocked

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

Use if static audit finds another contract contradiction, either preflight fails, replacement D2 persistence fails, comparator correction requires broader changes, or D3 encounters a source/environment blocker before valid comparison.

## 13. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_POST_P5_D2_COMPARATOR_FIELD_AUTHORITY_AND_HETEROGENEOUS_RESUMPTION_REPORT.md`

Report at minimum:

1. terminal classification;
2. live start/final `origin/main`;
3. Python `src/tests` continuity;
4. predecessor/successor artifact roots;
5. protected identities;
6. D1 artifact re-verification and zero-call confirmation;
7. static schema/comparator re-audit;
8. exact normal/near-tie schemas and counts;
9. comparator `gap`/`bound` authority applied;
10. complete comparator diff with line classifications;
11. complete MATLAB serialization diff with line classifications;
12. both preflight hashes/results;
13. full historical/current D2 call ledger;
14. D2 MATLAB/Python/comparison call counts;
15. nine normal-case max differences/worst cases;
16. near-tie `canonical/raw/alias_available/gap/bound/boundary_feasible/kkt_max/mu_a/mu_b` comparison;
17. D2 KKT/boundary mismatch counts;
18. D3 360-case max differences/worst cases if reached;
19. scientific mismatch list;
20. source/environment failure list;
21. forbidden-operation check;
22. git status;
23. acceptance level;
24. exact recommended next gate.

## 14. Explicit prohibitions

Do not:

- rerun D1;
- modify MATLAB production source/helpers/cache;
- modify Python production source/tests;
- modify frozen D2 Python scientific harness;
- alter any D2/D3 case, ordering, equation, parameter, state/shadow/derivative input, root, KKT condition, multiplier recovery, or tolerance;
- add any comparator field other than near-tie `gap` and `bound`;
- change any comparator tolerance, expected value, ordering, or PASS/FAIL rule;
- invent a 17-field or union D2 row schema;
- fabricate missing row fields;
- add the MATLAB `raah/Rah` taper;
- use production bare-`a` FOC as the corrected oracle;
- add `Tt`/`rb_gap` adapters;
- hard-code Python outputs into MATLAB;
- repair/rerun a failed scientific stage in this task;
- run full HJB/KFE/steady-state;
- rerun P3/P4/R4;
- run asset-tail diagnostics;
- enter AR(1), transition, IRF, dynamics, calibration extension, or Results;
- revoke or reissue P5.

## 15. Recommended next gate rule

If PASS, recommend only the already-identified upper-`a` asset-tail robustness gate before actual dynamic execution.

If material contradiction, recommend the smallest Owner/reviewer scientific diagnosis of the exact mismatched D2/D3 object.

If blocked, recommend only the smallest correction for the newly observed source/environment blocker.