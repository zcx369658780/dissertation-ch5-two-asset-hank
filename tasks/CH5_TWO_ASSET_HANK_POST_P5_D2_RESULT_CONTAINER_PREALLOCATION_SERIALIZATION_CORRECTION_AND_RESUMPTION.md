# CH5_TWO_ASSET_HANK_POST_P5_D2_RESULT_CONTAINER_PREALLOCATION_SERIALIZATION_CORRECTION_AND_RESUMPTION

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Resume the accepted post-P5 household-decision parity experiment after D1 achieved exact parity and D2 input-container traversal was successfully corrected, but the replacement D2 MATLAB call was then blocked solely by an external D2 result-container preallocation/whole-struct assignment defect.

Controlling predecessor specifications/evidence:

- `tasks/CH5_TWO_ASSET_HANK_POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_MAP_PARITY.md`
- `tasks/CH5_TWO_ASSET_HANK_POST_P5_HOUSEHOLD_DECISION_MAP_PARITY_MATLAB_STRUCT_HARNESS_CORRECTION_AND_RESUMPTION.md`
- `tasks/CH5_TWO_ASSET_HANK_POST_P5_D2_HETEROGENEOUS_CASE_CONTAINER_CORRECTION_AND_RESUMPTION.md`
- `docs/CH5_TWO_ASSET_HANK_POST_P5_HOUSEHOLD_DECISION_MAP_PARITY_MATLAB_STRUCT_HARNESS_CORRECTION_AND_RESUMPTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_POST_P5_D2_HETEROGENEOUS_CASE_CONTAINER_CORRECTION_AND_RESUMPTION_REPORT.md`

Latest accepted terminal classification:

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The only current blocker is the D2 MATLAB output container at `d2_matlab_corrected.m:13`: the evaluator still declares `rows=struct([])` and attempts whole-struct assignment of a normal 17-field D2 result row, producing MATLAB's dissimilar-structure assignment error before `d2_matlab.json` is persisted.

This successor authorizes only the minimum D2 result-row schema/preallocation/serialization correction, one no-model result-container preflight, one replacement D2 MATLAB scientific call, and—conditional on valid D2 persistence—the remaining frozen D2 Python/comparison and unchanged D3 sequence.

P5 remains Owner-accepted:

`MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`

The voluntary hold remains:

`DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`

## 2. Accepted D1 evidence is frozen and reuse-only

D1 must not be rerun.

Accepted D1 result:

- `432/432 PASS`;
- `216/216` low-`a` cases PASS;
- maximum absolute difference `0` for every compared scalar field;
- transfer-sign mismatch `0`;
- `a`-direction mismatch `0`;
- `b`-direction mismatch `0`.

Accepted D1 artifacts:

- MATLAB: `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`
- Python: `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`
- comparison: `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`

D1 MATLAB/Python/comparison call budget in this successor is exactly `0/0/0`.

## 3. Live authority and continuity

Task-authoring parent observed before publication:

`e6f1b41d73425539ed8435859bf0abab97e3178e`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main`;
3. confirm all controlling predecessor tasks/reports exist;
4. record live start SHA;
5. verify P5 marker and active dynamic hold;
6. verify accepted Python `src/tests` continuity from baseline `7a2388a2ba89073e307f05a909570e8c40a4be13` using:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

It must be empty.

## 4. Required reads

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- all three controlling household-decision task files above;
- both latest accepted household-decision reports above;
- `docs/CH5_TWO_ASSET_HANK_P5_OWNER_FINAL_ACCEPTANCE_DECISION.md`;
- every source/evidence file required by the original household-decision task that is necessary to execute D2/D3 unchanged.

The original household-decision task continues to control all scientific equations, cases, order, parameters, tolerances, outputs, and fail-closed logic except where this task explicitly authorizes the D2 result-container fix and consumed-call replacement.

## 5. Frozen predecessor identities to preserve

Original household-decision artifact root:

`D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-artifacts-20260829-220000`

Accepted D1/resumption artifact root:

`D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-resumption-artifacts-20260829-223000`

Latest D2 input-container successor root:

`D:\ProjectTemp\ch5-post-p5-d2-container-resumption-artifacts-20260830-001000`

Frozen scientific manifest:

- `manifest.json` SHA-256 `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA`

Frozen D2/D3 identities:

- original blocked D2 MATLAB harness `8067196C2C680926490B6231EE2FF3125DD43B26AB812A1566719043E270C7C9`
- accepted input-container-corrected `d2_matlab_corrected.m` `57FFAD7DA9DCBA043EC40B21C647AD8621E1D973C9670A7C73EF0E2E5F6F868E`
- D2 Python `DD9DDCB675BE7A5C3A672CF1936AB7CBA1553AC8334989B2CDAA777FB2914344`
- comparison harness `5C6FDBEBDA8BA67D819E69808A43C076E8F7BCB3C85788DABD942CC35EB40BE7`
- corrected D1/D3 MATLAB decision evaluator `5D94EDF89259D543758E490EA25C9359C1B65588CF7BB0557EEEDFA6B7FF3F9A`
- D3 Python decision evaluator `6054A0C59E7C0CD0C83AD1919C3CFAF7B2987D0545EE4CEB26B3345FF2D01ABC`

Accepted D2 heterogeneous-container preflight facts:

- MATLAB decoded `m.p2` type: `10x1 cell`;
- correct frozen-case traversal: `m.p2{k}` via the accepted `get_case` accessor;
- preflight `10/10 PASS`;
- IDs/order/required-field access all PASS;
- skipped/duplicated/reordered/merged counts all zero.

Preserve this accepted input traversal exactly. Do not reopen or alter it unless a direct contradiction is observed.

## 6. Scientific content is immutable

Do not change any frozen D2/D3 scientific content.

The following remain byte/value/semantic identical:

- all 10 D2 cases and ordering;
- all 360 D3 cases and ordering;
- all D2/D3 parameters;
- all state/shadow/derivative inputs;
- `mu_a = r_a*a + d`;
- `m(a)=max(a,a_bar)`;
- accepted O1 behavior;
- labor-curvature mapping;
- common-budget scope;
- D2 root/KKT/multiplier equations;
- D3 `gamma_c=2`, Python `phi=5`, MATLAB `frisch_l=.2` regime;
- all comparison fields;
- all tolerances;
- all stop/fail-closed rules except the explicitly authorized replacement D2 MATLAB call.

Reuse the frozen manifest after identity verification. Do not regenerate a scientifically different manifest.

## 7. Phase A — correct only D2 result schema/preallocation/serialization

Work in a fresh no-overwrite external artifact root. Do not modify predecessor artifact roots.

Start from accepted `d2_matlab_corrected.m` SHA-256:

`57FFAD7DA9DCBA043EC40B21C647AD8621E1D973C9670A7C73EF0E2E5F6F868E`

The accepted input traversal (`get_case`, `iscell`, `{k}` extraction) must remain scientifically and functionally unchanged.

Diagnose the exact D2 output row schema generated by the existing scientific evaluator. Create `d2_matlab_result_corrected.m` with only result-container/serialization changes.

Allowed edits are limited to:

- declaring the exact D2 result-row field schema;
- homogeneous struct-array preallocation using that exact schema;
- field-order/schema normalization solely to permit MATLAB whole-struct assignment;
- assigning already-computed D2 result rows into the output container;
- JSON serialization/file-writing plumbing for the same homogeneous result container;
- external callable/file-name alignment required by the corrected harness.

Forbidden edits include any change to:

- accepted `get_case` input traversal and frozen case values;
- scientific formulas;
- roots;
- state constraints;
- KKT equations;
- multiplier recovery;
- O1 transfer scaling;
- constant-`r_a` drift;
- parameters, states, derivatives, shadow inputs;
- tolerances;
- result values produced by the existing evaluator;
- expected Python outputs or comparison thresholds.

Produce a complete original-versus-corrected diff from the accepted input-corrected D2 harness. Every changed line must be classified as exactly one of:

- `RESULT_CONTAINER_SCHEMA_ONLY`
- `RESULT_PREALLOCATION_ONLY`
- `RESULT_SERIALIZATION_ONLY`
- `EXTERNAL_CALLABLE_ALIGNMENT_ONLY`

If any scientific line would require modification, stop before preflight and report blocked.

## 8. Phase B — mandatory no-model D2 result-container preflight

Before the replacement D2 MATLAB scientific call, create and freeze one no-model MATLAB preflight.

It must not call:

- `HANK_2ASSETS_HJB`;
- production `HANK3_FOC`;
- accepted O1 FOC;
- `HANK3_cost`;
- `lab_solve2`;
- any D2 scientific root/KKT/equation evaluator;
- Python.

The preflight must:

1. construct at least two synthetic D2 result rows with the exact 17-field schema and representative field types expected from the existing D2 evaluator;
2. exercise the corrected homogeneous preallocation and whole-struct assignment path;
3. serialize using the exact JSON/file path intended by the corrected D2 harness;
4. independently read back and verify row count, field names/order/schema and representative values;
5. additionally load/extract all 10 frozen case IDs through the already accepted `get_case` input traversal without evaluating science, so both accepted input traversal and corrected output plumbing are exercised together;
6. exit zero.

Freeze/hash/read back before preflight:

- corrected D2 MATLAB harness;
- result-container preflight;
- unchanged scientific manifest;
- unchanged D2 Python/comparison/D3 harnesses;
- a new successor execution ledger;
- complete harness diff.

If preflight fails, no replacement D2 scientific call is allowed.

## 9. Phase C — exactly one replacement D2 MATLAB scientific call

The latest replacement D2 MATLAB call was consumed by the output-container defect before valid persistence. This task explicitly authorizes exactly **one new replacement D2 MATLAB scientific call** after a successful no-model preflight.

It must use the exact frozen 10 D2 cases, exact order, accepted input traversal, accepted equations, root/KKT logic, parameters, and tolerances.

Acceptance before advancing:

- process exits zero;
- `d2_matlab.json` exists;
- exactly 10 rows are present in frozen order;
- every required identity and output field exists;
- all required values are finite where the original contract requires finiteness;
- JSON parses/read-backs independently;
- no scientific case, equation or output definition changed.

If this replacement D2 MATLAB call fails for any reason, do not repair or rerun it in this task. Stop fail-closed.

## 10. Phase D — finish D2 then unchanged D3

Only after valid D2 MATLAB persistence:

### D2 remainder

Run exactly once each:

- D2 Python production evaluator;
- D2 comparison.

Apply the original frozen D2 comparison contract unchanged.

For all ten cases compare:

- `c`;
- `l`;
- `d`;
- adjustment cost;
- `mu_a`;
- `mu_b`;
- utility;
- Hamiltonian;
- `a` direction;
- `b` direction;
- `lambda_a`;
- `lambda_b`;
- maximum KKT residual;
- boundary-feasibility result.

If any valid D2 scientific mismatch occurs, stop before D3 and classify material contradiction.

### D3

If D2 passes, execute the exact unchanged frozen D3 sequence:

- MATLAB decision harness: 1 scientific call using the already accepted corrected decision result-container implementation;
- Python decision harness: 1 scientific call;
- comparison: 1 call.

Use exactly the frozen 360 `gamma_c=2` / Python `phi=5` / MATLAB `frisch_l=.2` cases. No D3 scientific formula, case, parameter, ordering, or tolerance may change.

If D3 encounters a source/environment blocker, stop without same-task repair. If a valid D3 comparison mismatches, classify material contradiction.

## 11. Exact call budget

Engineering-only result-container preflight: at most 1 MATLAB invocation.

Historical scientific calls must be reported separately and not erased:

- original D1 MATLAB blocked call: `1`;
- accepted D1 replacement MATLAB/Python/comparison: `1/1/1`;
- original D2 MATLAB input-container blocked call: `1`;
- replacement D2 MATLAB output-container blocked call: `1`.

Scientific calls authorized in this successor:

- D1 MATLAB/Python/comparison: exactly `0/0/0`;
- new replacement D2 MATLAB: exactly `1` if preflight passes;
- D2 Python: at most `1`, only after valid D2 MATLAB persistence;
- D2 comparison: at most `1`;
- D3 MATLAB/Python/comparison: at most `1/1/1`, only after D2 PASS.

No full HJB, Python HJB/KFE/steady-state, P3/P4/R4, asset-tail, AR(1), transition, IRF, calibration-extension, dynamics or Results call is authorized.

## 12. Terminal classifications

Return exactly one.

### D2 and D3 pass

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_PASS__DYNAMIC_HOLD_MAY_ADVANCE_TO_ASSET_TAIL_GATE`

Use only if:

- accepted D1 PASS is reused with zero D1 calls;
- D2 result-container diff is strictly within allowed plumbing classes;
- no-model preflight passes;
- replacement D2 MATLAB persists all 10 rows;
- D2 all 10 cases pass;
- D3 all 360 cases pass;
- no forbidden mutation or rerun occurs.

### Scientific contradiction

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_MATERIAL_CONTRADICTION__DYNAMIC_HOLD_CONTINUES`

Use if a valid D2 or D3 comparison shows any material mismatch under the frozen accepted common equations.

P5 is not automatically revoked. Report the exact contradiction for Owner/reviewer diagnosis.

### Source/environment/harness blocked

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

Use if:

- the D2 result-container correction cannot remain within allowed plumbing-only classes;
- preflight fails;
- replacement D2 persistence fails;
- or D3 hits a new source/environment blocker before valid scientific comparison.

Do not infer scientific PASS/FAIL from missing comparison evidence.

## 13. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_POST_P5_D2_RESULT_CONTAINER_PREALLOCATION_SERIALIZATION_CORRECTION_AND_RESUMPTION_REPORT.md`

The report must include:

1. terminal classification;
2. live start/final `origin/main`;
3. Python `src/tests` continuity;
4. predecessor and successor artifact roots;
5. protected identities;
6. D1 accepted artifact re-verification and explicit zero-call confirmation;
7. D2 accepted input-container correction/preflight reuse;
8. exact D2 output blocker diagnosis and 17-field schema;
9. complete accepted-input-corrected-to-result-corrected D2 harness diff with per-line classifications;
10. corrected harness/preflight/ledger/diff hashes;
11. no-model result-container preflight result;
12. all historical D2 consumed-call counts and the new replacement D2 count separately;
13. exact successor D2/D3 call counts;
14. D2 ten-case per-field maximum absolute differences and worst cases if reached;
15. D2 direction/multiplier/KKT/boundary mismatch counts if reached;
16. D3 360-case gamma-2/phi-5 per-field maximum absolute differences and worst cases if reached;
17. complete scientific mismatch list;
18. complete source/environment failure list;
19. forbidden-operation check;
20. git status;
21. acceptance level;
22. exact recommended next gate.

## 14. Explicit prohibitions

Do not:

- rerun D1;
- alter the accepted D2 input traversal beyond mechanical reuse;
- modify MATLAB production source/helpers/cache;
- modify Python production source/tests;
- alter any frozen D2/D3 case or ordering;
- alter equations, parameters, grids, state/shadow/derivative inputs or tolerances;
- add the legacy `raah/Rah` taper;
- use production bare-`a` FOC as corrected oracle;
- add `Tt` or `rb_gap` adapters;
- import or hard-code Python result values into MATLAB;
- change D2 scientific root/KKT evaluator logic;
- repair and rerun a failed replacement D2 or D3 stage in this same task;
- run full `HANK_2ASSETS_HJB`;
- run Python HJB/KFE/steady state;
- rerun P3/P4/R4;
- run upper-`a` asset-tail diagnostics;
- enter AR(1), transition, IRF, calibration extension, dynamics or Results;
- revoke or reissue P5 automatically.

## 15. Recommended next gate rule

If PASS, recommend only the already-identified upper-`a` asset-tail robustness gate before actual dynamics execution.

If material contradiction, recommend the smallest Owner/reviewer diagnosis of the exact D2/D3 mismatch.

If blocked, recommend only the smallest newly observed source/environment correction gate.
