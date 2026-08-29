# CH5_TWO_ASSET_HANK_POST_P5_D2_COMPARATOR_CATEGORICAL_TERMINAL_SEMANTICS_AND_RESUMPTION

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Resolve the sole remaining comparator-preflight authority defect exposed by the accepted D2 comparator-field/heterogeneous-resumption report, then resume the already frozen post-P5 household-decision parity experiment.

Latest accepted report:

`docs/CH5_TWO_ASSET_HANK_POST_P5_D2_COMPARATOR_FIELD_AUTHORITY_AND_HETEROGENEOUS_RESUMPTION_REPORT.md`

Accepted terminal classification:

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

That report establishes:

- D1 remains accepted at `432/432 PASS`, including `216/216` low-`a` cases, with all compared scalar maximum absolute differences equal to `0` and all sign/direction mismatches equal to `0`;
- the D2 static 9+1 schema audit passed;
- the heterogeneous MATLAB serialization correction is plumbing-only and its no-model preflight passed;
- the authorized comparator already includes near-tie `gap` and `bound` under the frozen floating tolerance;
- deliberate `gap` and `bound` perturbations correctly produce terminal failure;
- a deliberate near-tie `canonical` perturbation increments categorical mismatch statistics but does not populate `failures`, so the comparator incorrectly exits PASS;
- no D2 or D3 scientific call was executed after that preflight failure.

This task freezes the categorical terminal semantics and authorizes one corrected comparator preflight. Only after that preflight passes may the already approved D2/D3 scientific sequence resume.

P5 remains Owner-accepted:

`MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`

The voluntary route hold remains:

`DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`

## 2. Comparator terminal-semantics authority decision

The frozen scientific meaning of a field comparison is equality within its already accepted comparison rule.

Therefore, for every categorical field already included in the frozen D2/D3 comparator field set, a categorical mismatch is hereby explicitly classified as a **terminal comparison failure**, not a non-terminal statistic.

Frozen authority marker:

`COMPARATOR_CATEGORICAL_MISMATCH_IS_TERMINAL_FAILURE`

This applies only to categorical fields that the comparator already compares. It does not authorize adding new fields.

At minimum the already frozen categorical fields include:

### Normal decision rows

- `a_direction`
- `b_direction`
- `boundary_feasible`

### Near-tie row

- `canonical`
- `raw`
- `alias_available`
- `boundary_feasible`

If static source inspection shows another categorical field is already in the existing frozen comparator field set, it receives the same terminal semantics. Do not add a categorical field that was not already compared.

Consequences:

1. every categorical mismatch already counted in categorical mismatch statistics must also make the comparator's overall PASS false;
2. the mismatch must be represented in the comparator `failures` output or an equivalent existing terminal-failure collection;
3. comparator nonzero/failure exit semantics must be triggered by either numerical failure or categorical failure;
4. matching categorical values remain PASS;
5. no tolerance, numerical threshold, expected value, field set, ordering, or scientific computation changes.

The previously authorized near-tie numerical field additions remain frozen:

- `gap`
- `bound`

using exactly:

`tau_fp(x,y) = 128*eps64*max(1,abs(x),abs(y))`

No widening or replacement tolerance is authorized.

## 3. Live authority and continuity

Task-authoring parent observed before publication:

`ded4046b06fd2e47d0c37993ef77f38bf02521d3`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main`;
3. record live start SHA;
4. verify all controlling predecessor tasks/reports remain present;
5. verify P5 marker and active dynamic hold;
6. verify accepted Python production `src/tests` continuity from baseline `7a2388a2ba89073e307f05a909570e8c40a4be13` using:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

It must be empty.

## 4. D1 remains reuse-only

D1 must not be rerun.

Re-verify the accepted artifacts:

- MATLAB `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`
- Python `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`
- comparison `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`

D1 MATLAB/Python/comparison call budget in this task is exactly `0/0/0`.

## 5. Reuse already-qualified D2 serialization evidence

Do not redo the already-passed MATLAB heterogeneous-result preflight unless a hash/source contradiction is found.

Verify and reuse:

- corrected heterogeneous D2 MATLAB harness SHA-256 `A7034181F3FC902E39EAB64CB8ED47C77BA52087B4E262325CAD33BAAECE3589`;
- frozen D2 Python SHA-256 `DD9DDCB675BE7A5C3A672CF1936AB7CBA1553AC8334989B2CDAA777FB2914344`;
- comparator-with-gap/bound SHA-256 `EBF1B72AC4ED53791646C5E06345D5D31FE06E16B6E81E618AD73229801EF0AF`;
- frozen D3 MATLAB SHA-256 `5D94EDF89259D543758E490EA25C9359C1B65588CF7BB0557EEEDFA6B7FF3F9A`;
- frozen D3 Python SHA-256 `6054A0C59E7C0CD0C83AD1919C3CFAF7B2987D0545EE4CEB26B3345FF2D01ABC`;
- frozen scientific manifest SHA-256 `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA`;
- accepted MATLAB heterogeneous preflight result SHA-256 `815C6703FECE0438B0584C3AD16A1A772D3A42D2AA57C7F2A4FBA0BF6F6808A4`.

Accepted D2 serialization contract remains:

`D2_HETEROGENEOUS_JSON_ARRAY_PRESERVE_NATIVE_CASE_SCHEMA`

with exactly 9 native 16-field normal rows and 1 native 10-field `lower_b_fz_near_tie` row.

Do not create a homogeneous union schema or fabricate missing fields.

## 6. Phase A — static comparator audit and minimal correction

Start from comparator SHA-256:

`EBF1B72AC4ED53791646C5E06345D5D31FE06E16B6E81E618AD73229801EF0AF`

Before changing it, statically identify:

- the exact categorical field list already compared;
- the categorical mismatch counter/statistics path;
- the numerical `failures` path and terminal PASS/FAIL/exit derivation;
- whether D2 and D3 use the same comparator terminal semantics.

Create a corrected external comparator with the smallest possible change so that every mismatch in the already-existing categorical comparison set becomes terminal.

Allowed changed-line classification only:

`COMPARATOR_CATEGORICAL_TERMINAL_SEMANTICS_ONLY`

Permitted implementation effects are limited to:

- appending an already-detected categorical mismatch to `failures` or an equivalent existing terminal-failure collection;
- making the existing final PASS/FAIL/exit decision depend on the union of already-detected numerical and categorical mismatches;
- recording field/case/left/right information for the categorical failure using existing comparator output conventions.

Forbidden changes:

- adding/removing comparison fields;
- changing `gap`/`bound` rules;
- changing numerical tolerances;
- changing expected values;
- changing ordering;
- changing scientific cases;
- changing any MATLAB or Python evaluator;
- changing production `src/tests`;
- weakening any mismatch into a warning.

Produce a complete comparator diff and classify every changed line.

If the correction cannot remain within this exact boundary, stop before preflight.

## 7. Phase B — one corrected comparator engineering preflight

Freeze/hash/read back before execution:

- corrected comparator;
- comparator diff;
- one engineering-only comparator preflight harness;
- unchanged corrected heterogeneous D2 MATLAB harness;
- unchanged D2 Python/D3 harnesses;
- unchanged scientific manifest;
- successor execution ledger.

Run exactly one engineering-only Python preflight invocation. It must not call any household evaluator.

The preflight must exercise synthetic paired JSON fixtures and prove all of the following:

### Matching control

- identical normal and near-tie fixtures: terminal PASS / exit `0`.

### Numerical negative controls

- near-tie `gap` perturbed beyond frozen `tau_fp`: terminal FAIL / nonzero failure exit;
- near-tie `bound` perturbed beyond frozen `tau_fp`: terminal FAIL / nonzero failure exit.

### Near-tie categorical negative controls

- perturbed `canonical`: terminal FAIL;
- perturbed `raw`: terminal FAIL;
- perturbed `alias_available`: terminal FAIL;
- perturbed `boundary_feasible`: terminal FAIL.

### Normal categorical negative controls

- perturbed `a_direction`: terminal FAIL;
- perturbed `b_direction`: terminal FAIL;
- perturbed `boundary_feasible`: terminal FAIL.

For every categorical negative control, require both:

- categorical mismatch count/statistic increments as before;
- terminal `failures`/PASS/exit also reflects the mismatch.

The preflight must additionally verify that a normal numerical perturbation still follows the unchanged frozen numerical tolerance and failure path.

No second preflight is authorized in this task. If it fails for any reason, do not repair or rerun it; stop fail-closed.

## 8. Phase C — resume D2 after preflight PASS

Only after Phase B PASS, authorize exactly one replacement D2 MATLAB scientific call using the already-qualified heterogeneous MATLAB harness.

Historical D2 MATLAB calls remain separately recorded:

1. input-container blocker: `1`;
2. zero-field output-container blocker: `1`;
3. later schema/comparator authority tasks: scientific calls `0`;
4. this task replacement D2 MATLAB: at most `1`.

Replacement D2 MATLAB requirements:

- exit zero;
- `d2_matlab.json` exists;
- exactly 10 rows in frozen order;
- 9 normal rows retain native 16-field schemas;
- `lower_b_fz_near_tie` retains native 10-field schema;
- no fabricated fields;
- independent read-back succeeds.

If the replacement D2 MATLAB call fails, do not repair or rerun it in this task.

After valid MATLAB persistence, run exactly once each:

- frozen D2 Python evaluator;
- corrected D2 comparator.

D2 comparison field set is frozen as already authorized.

### Nine normal cases

Compare the existing frozen normal fields, including numerical controls, directions, multipliers, KKT, boundary feasibility, and `boundary_violation` where already present in the comparator.

### Near-tie case

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

Any valid numerical or categorical mismatch is terminal and must stop before D3.

## 9. Phase D — unchanged D3 after D2 PASS

If D2 passes, execute the frozen D3 sequence exactly once each:

- MATLAB decision harness: `1`;
- Python decision harness: `1`;
- corrected comparator: `1`.

Use exactly the frozen 360 `gamma_c=2`, Python `phi=5`, MATLAB `frisch_l=.2` cases.

No D3 case, formula, parameter, ordering, tolerance, output field, or scientific rule may change.

The corrected comparator categorical-terminal semantics apply to any categorical fields that were already part of the frozen D3 comparison set; no D3 field may be added.

If D3 hits a source/environment blocker, stop without same-task repair. If a valid D3 scientific mismatch is observed, classify material contradiction.

## 10. Call budget

D1 scientific calls: exactly `0/0/0`.

Engineering-only calls:

- MATLAB heterogeneous-result preflight: `0` new calls; reuse accepted evidence;
- corrected comparator preflight: exactly `1` maximum.

Scientific calls after comparator preflight PASS:

- replacement D2 MATLAB: at most `1`;
- D2 Python: at most `1`;
- D2 comparison: at most `1`;
- D3 MATLAB/Python/comparison: at most `1/1/1`.

No full HJB, Python HJB/KFE/steady-state, P3/P4/R4, asset-tail, AR(1), transition, IRF, calibration extension, dynamics, or Results call is authorized.

## 11. Terminal classifications

Return exactly one.

### PASS

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_PASS__DYNAMIC_HOLD_MAY_ADVANCE_TO_ASSET_TAIL_GATE`

Use only if:

- comparator correction is categorical-terminal-semantics only;
- corrected comparator preflight passes all positive/negative controls;
- D1 is reused with zero calls;
- D2 MATLAB persists all 10 native-schema rows;
- D2 all 10 cases pass with categorical mismatches terminal;
- D3 all 360 cases pass;
- no forbidden mutation/rerun occurs.

### Material contradiction

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_MATERIAL_CONTRADICTION__DYNAMIC_HOLD_CONTINUES`

Use if a valid D2 or D3 scientific comparison has any numerical or categorical mismatch under the accepted equations and frozen comparator rules.

P5 is not automatically revoked.

### Blocked

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

Use if the comparator correction cannot remain within authority, corrected preflight fails, D2 persistence fails, or D3 encounters a source/environment blocker before valid comparison.

## 12. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_POST_P5_D2_COMPARATOR_CATEGORICAL_TERMINAL_SEMANTICS_AND_RESUMPTION_REPORT.md`

Report at minimum:

1. terminal classification;
2. live start/final `origin/main`;
3. Python production `src/tests` continuity;
4. predecessor/successor artifact roots;
5. D1 artifact re-verification and exact zero-call confirmation;
6. reused MATLAB heterogeneous serialization evidence and hashes;
7. exact pre-correction categorical field list and terminal logic;
8. complete comparator diff with per-line classification;
9. corrected comparator/preflight/ledger hashes;
10. corrected comparator preflight positive/negative-control results;
11. historical/current D2 call ledger;
12. D2 MATLAB/Python/comparison call counts;
13. D2 nine-normal-case per-field max differences and worst cases;
14. D2 near-tie full categorical/numerical comparison including `gap`/`bound`;
15. D2 categorical mismatch counts, numerical failure counts, KKT/boundary mismatch counts;
16. D3 360-case per-field max differences/worst cases and categorical mismatch counts if reached;
17. complete scientific mismatch list;
18. complete source/environment failure list;
19. forbidden-operation check;
20. git status;
21. acceptance level;
22. exact recommended next gate.

## 13. Explicit prohibitions

Do not:

- rerun D1;
- rerun the accepted MATLAB heterogeneous-result preflight;
- modify MATLAB/Python production source/tests/helpers/cache;
- modify frozen D2 Python scientific evaluator;
- add/remove comparator fields;
- alter `gap`/`bound` tolerance;
- alter any numerical tolerance;
- change D2/D3 cases, order, equations, parameters, roots, KKT conditions, multipliers, state/shadow/derivative inputs;
- fabricate missing heterogeneous fields;
- create a homogeneous union schema;
- add the MATLAB `raah/Rah` taper;
- use production bare-`a` FOC as corrected oracle;
- add `Tt`/`rb_gap` adapters;
- hard-code MATLAB/Python expected answers;
- repair and rerun a failed corrected preflight or scientific stage in this task;
- run full HJB/KFE/steady state;
- rerun P3/P4/R4;
- run upper-`a` asset-tail diagnostics;
- enter AR(1), transition, IRF, calibration extension, dynamics or Results;
- revoke or reissue P5 automatically.

## 14. Recommended next gate rule

If PASS, recommend only the already-identified post-P5 upper-`a` asset-tail robustness gate before actual dynamic execution.

If material contradiction, recommend the smallest Owner/reviewer diagnosis of the exact mismatched decision object.

If blocked, recommend only the smallest newly observed comparator/source/environment correction gate.