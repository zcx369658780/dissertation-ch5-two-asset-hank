# CH5_TWO_ASSET_HANK_POST_P5_D2_COMPARATOR_INPUT_CONTAINER_NORMALIZATION_AND_RESUMPTION

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Resume the post-P5 household-decision parity experiment after both frozen D2 language outputs were successfully persisted, but the single accepted comparator invocation was consumed before comparison because the accepted MATLAB heterogeneous output is a native top-level JSON array while the comparator assumed a mapping with a `rows` key.

Latest accepted report:

`docs/CH5_TWO_ASSET_HANK_POST_P5_D2_PYTHON_CHECK_BOUNDARY_ARITY_CORRECTION_AND_RESUMPTION_REPORT.md`

Accepted terminal classification:

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The accepted evidence now establishes:

- D1 is accepted `432/432 PASS`, including `216/216` low-`a` PASS, with all compared scalar maximum differences equal to `0` and all sign/direction mismatches equal to `0`;
- D2 MATLAB is already persisted and accepted as exactly ten frozen rows under the native heterogeneous `9 x 16-field + 1 x 10-field` schema;
- D2 Python is already persisted and accepted as exactly the same ten frozen rows/order/schema after bounded UTF-8 and `check_boundary` arity plumbing corrections;
- the accepted corrected comparator already has near-tie `gap/bound` comparison authority and categorical-terminal semantics;
- the single comparator call failed before row-by-row comparison solely because the MATLAB JSON loaded as a Python `list`, while the comparator executed `M['rows']`;
- no D2 scientific mismatch was observed and D3 was not entered.

This task authorizes only the smallest comparator **input-container semantic-view normalization**, one no-science container preflight, one replacement D2 comparison, and—only after D2 PASS—the existing frozen D3 sequence.

P5 remains Owner-accepted:

`MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`

The voluntary route hold remains:

`DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`

## 2. Live authority and continuity

Task-authoring parent observed before publication:

`0dc80c7ca62e6fa2c7c417c8f8c21730c2ff2097`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task and all controlling predecessor tasks/reports exist on live `main`;
3. record live start SHA;
4. verify the P5 marker and active dynamic hold;
5. verify accepted Python production `src/tests` continuity from baseline `7a2388a2ba89073e307f05a909570e8c40a4be13` using:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

It must be empty.

## 3. Accepted evidence to reuse without rerun

Re-verify hashes/read-back only. Do not rerun any accepted scientific stage or engineering preflight.

### D1

- MATLAB `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`
- Python `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`
- comparison `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`

D1 call budget in this task: exactly `0/0/0`.

### D2 persisted scientific outputs

Accepted MATLAB output:

`26F9E628021327D02897FE96A2FBAA52D1AF4434629676E03BD6614708D6E977`

Accepted Python output:

`C8FF69CDD8DDF6F742CB0A98D562D4020DB65E69A3D04BC7A90C34B95199227B`

Verify both contain exactly ten frozen case IDs in identical order:

1. `interior_ff`
2. `interior_bb`
3. `liquid_zero`
4. `lower_a_active`
5. `lower_b_active`
6. `interior_mu_a_zero`
7. `upper_a_lower_b`
8. `upper_a_interior_b`
9. `dual_upper`
10. `lower_b_fz_near_tie`

Verify native field counts remain:

`16,16,16,16,16,16,16,16,16,10`

and no fabricated union fields exist.

D2 MATLAB call budget in this task: exactly `0`.

D2 Python scientific call budget in this task: exactly `0`.

### Accepted comparator and supporting evidence

- accepted corrected comparator `FAF1A6ABB9F21E7DABD6CFB0857A72354CC3A5D0D532F4968F027E5CBBC0ECB5`;
- accepted comparator preflight `52F55586BAFA456BC811E4CAD885F7C26DD30FF9F15165C405515C6CEAB1D0F9`;
- accepted heterogeneous MATLAB preflight `815C6703FECE0438B0584C3AD16A1A772D3A42D2AA57C7F2A4FBA0BF6F6808A4`;
- accepted UTF-8 preflight `5E3C17CC617EF03AE8D80D55736F2A79B7124A6E6DE16C630F54A69386025EF0`;
- accepted boundary-arity interface preflight `BEAE0726E679F3DD24EBEB2978A2E35D47B99CD8FD732EBB4506D307820E052E`;
- accepted root diagnostic `6C77624B69F1ECED1E54A216ABBA8D5BF28A031B83672AA74268774B8A26268C`;
- accepted corrected-root preflight `2B01AD00F0CCF151D6BDC3EE46E476DA4BEC63FEE3A98B34CF299B0B5EEE8AB6`.

Do not rerun any of them.

### Frozen D3 harnesses

- MATLAB `5D94EDF89259D543758E490EA25C9359C1B65588CF7BB0557EEEDFA6B7FF3F9A`;
- Python `6054A0C59E7C0CD0C83AD1919C3CFAF7B2987D0545EE4CEB26B3345FF2D01ABC`.

## 4. Mandatory static comparator/container audit

Before writing a corrected comparator or running any process, inspect read-only:

1. accepted D2 MATLAB JSON object at SHA `26F9E6...E977` and record the exact top-level Python type after `json.load`;
2. accepted D2 Python JSON object at SHA `C8FF69...227B` and record the exact top-level Python type after `json.load`;
3. accepted comparator SHA `FAF1A6...ECB5` and identify every place where it assumes a top-level mapping/`rows` key;
4. identify whether metadata such as `stage` or `case_count` is used for PASS/FAIL or only the ordered row semantic view is used;
5. inspect frozen D3 MATLAB/Python external harness serialization paths statically and determine whether the same top-level container asymmetry can arise in D3;
6. verify the comparator's actual row-wise comparison logic, field sets, tolerances, categorical terminal semantics, and `gap/bound` rules are independent of the top-level wrapper representation.

Report exactly:

- MATLAB D2 top-level type and nested element shape;
- Python D2 top-level type and mapping keys;
- current comparator extraction expressions;
- exact row semantic view expected by the comparison loops;
- whether a pure container adapter can produce the same ordered list of ten row dicts from each accepted payload without changing any row dict;
- whether the same bounded normalization should apply to D3 only as container plumbing, if D3's frozen serializers use the corresponding shapes.

If normalization would require changing any row field/value/order, expected result, tolerance, comparison field set, or scientific rule, stop before correction and report the smallest contradiction.

## 5. Frozen input-container normalization authority

If the static audit confirms the latest report, freeze:

`COMPARATOR_TOP_LEVEL_CONTAINER_NORMALIZATION_ONLY`

The corrected external comparator may introduce exactly one bounded row-view extractor whose semantics are:

- if a loaded payload is a `list`, that list itself is the ordered row semantic view;
- if a loaded payload is a mapping containing `rows`, `payload['rows']` is the ordered row semantic view;
- any other payload shape is a terminal source/environment error;
- the extractor must return the existing row objects **without copying, merging, filling, renaming, reordering, coercing, or mutating any row field/value**.

Equivalent minimal syntax is allowed, for example:

```python
def rows_view(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and 'rows' in payload:
        return payload['rows']
    raise TypeError(...)
```

Then replace only top-level `M['rows']` / `P['rows']` assumptions with the normalized ordered row views.

Every changed line must be classified exactly:

`COMPARATOR_INPUT_CONTAINER_NORMALIZATION_ONLY`

No other comparator change is authorized.

The already accepted comparison semantics remain frozen:

- numerical tolerances unchanged;
- categorical mismatches terminal under `COMPARATOR_CATEGORICAL_MISMATCH_IS_TERMINAL_FAILURE`;
- near-tie `gap` and `bound` included under the accepted floating rule;
- no comparison field added/removed;
- no PASS/FAIL threshold changed.

## 6. One no-science container preflight

Work in a fresh no-overwrite external artifact root.

Before execution, freeze/hash/read back:

- input-container-normalized comparator;
- complete comparator diff relative to accepted comparator `FAF1A6...ECB5`;
- one engineering-only container preflight;
- accepted D2 MATLAB and Python JSON outputs;
- unchanged D3 harnesses;
- successor execution ledger.

Run exactly one engineering-only Python preflight invocation. It must not call any D2/D3 household evaluator.

The preflight must prove all of the following:

1. a synthetic top-level list of heterogeneous row dicts normalizes to itself in exact order;
2. a synthetic mapping `{'rows': same_rows}` normalizes to the exact same row semantic view;
3. row count, object identity/equality, field names, field values, heterogeneous schemas, and order are unchanged;
4. unsupported top-level payload shape is rejected terminally;
5. accepted D2 MATLAB output normalizes to exactly ten rows with field counts `9 x 16 + 1 x 10`;
6. accepted D2 Python output normalizes to exactly the same ten IDs/order/schema;
7. after normalization, the two accepted payloads expose identical case IDs and compatible native schemas for comparison;
8. existing comparator positive/negative numerical and categorical logic is not modified by the diff;
9. if static D3 audit shows the same list-vs-mapping wrapper asymmetry, synthetic representatives of both D3 wrapper shapes normalize without row mutation;
10. exit zero.

If this one preflight fails, do not repair or rerun it in this task.

## 7. Exactly one replacement D2 comparison

The predecessor accepted-comparator invocation was consumed by the top-level container blocker before comparison. After static audit and container preflight PASS, this task explicitly authorizes exactly **one replacement D2 comparator invocation** using:

- accepted D2 MATLAB output SHA `26F9E628021327D02897FE96A2FBAA52D1AF4434629676E03BD6614708D6E977`;
- accepted D2 Python output SHA `C8FF69CDD8DDF6F742CB0A98D562D4020DB65E69A3D04BC7A90C34B95199227B`;
- corrected input-container-normalized comparator.

Do not rerun either D2 scientific harness.

The D2 comparison must retain every frozen rule.

### Nine normal rows

Compare the existing accepted normal-field set, including controls, drifts, directions, multipliers, KKT, boundary feasibility, and `boundary_violation` where already present.

### Near-tie row

Compare exactly the already authorized fields:

- `canonical`
- `raw`
- `alias_available`
- `gap`
- `bound`
- `boundary_feasible`
- `kkt_max`
- `mu_a`
- `mu_b`

Every numerical or categorical mismatch is terminal.

If D2 comparator reports any valid mismatch, stop before D3 and return:

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_MATERIAL_CONTRADICTION__DYNAMIC_HOLD_CONTINUES`

Do not tune or reinterpret a mismatch.

## 8. Frozen D3 after D2 PASS

If and only if D2 comparison passes, execute the frozen D3 sequence exactly once each:

- MATLAB decision harness: `1`;
- Python decision harness: `1`;
- corrected input-container-normalized comparator: `1`.

Use exactly the frozen 360 `gamma_c=2`, Python `phi=5`, MATLAB `frisch_l=.2` cases.

The comparator may use the same already-preflighted top-level container normalization if the static D3 audit confirmed that the frozen D3 serializers emit the supported list/mapping-with-rows forms. No D3-specific comparator field or tolerance change is authorized.

If D3 hits a new source/environment blocker, stop without repair/rerun. If a valid D3 numerical/categorical mismatch occurs, classify material contradiction.

## 9. Exact call budget

Historical scientific and engineering calls remain recorded; none may be erased.

Calls authorized in this task:

- D1 MATLAB/Python/comparison: exactly `0/0/0`;
- D2 MATLAB: exactly `0`;
- D2 Python: exactly `0`;
- previously accepted diagnostics/preflights: `0` new calls;
- comparator container preflight: at most `1`;
- replacement D2 comparison: at most `1`, only after preflight PASS;
- D3 MATLAB/Python/comparator: at most `1/1/1`, only after D2 PASS.

No full HJB, Python HJB/KFE/steady-state, P3/P4/R4, asset-tail, AR(1), transition, IRF, calibration extension, dynamics, or Results call is authorized.

## 10. Terminal classifications

Return exactly one.

### PASS

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_PASS__DYNAMIC_HOLD_MAY_ADVANCE_TO_ASSET_TAIL_GATE`

Use only if:

- comparator change is strictly top-level container normalization;
- container preflight passes;
- D2 persisted MATLAB/Python outputs are reused without rerun;
- replacement D2 comparison passes all ten cases under frozen rules;
- D3 all 360 cases pass;
- no forbidden mutation/rerun occurs.

### Material contradiction

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_MATERIAL_CONTRADICTION__DYNAMIC_HOLD_CONTINUES`

Use if a valid D2 or D3 comparison reports any numerical or categorical mismatch under frozen accepted equations/comparator rules.

P5 is not automatically revoked.

### Blocked

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

Use if static normalization cannot remain plumbing-only, preflight fails, replacement D2 comparison is blocked before valid comparison, or D3 hits a source/environment blocker before valid scientific comparison.

## 11. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_POST_P5_D2_COMPARATOR_INPUT_CONTAINER_NORMALIZATION_AND_RESUMPTION_REPORT.md`

The report must include at minimum:

1. terminal classification;
2. live start/final `origin/main`;
3. Python production `src/tests` continuity;
4. predecessor/successor artifact roots;
5. D1 hash re-verification and exact zero-call confirmation;
6. accepted D2 MATLAB/Python output hashes, schemas, IDs/order, and exact zero scientific calls;
7. complete top-level container audit for D2 and static D3 serializer audit;
8. complete accepted-comparator-to-corrected-comparator diff with every changed line classified `COMPARATOR_INPUT_CONTAINER_NORMALIZATION_ONLY`;
9. corrected comparator/preflight/diff/ledger hashes;
10. one-shot container preflight result;
11. historical/current comparator invocation ledger;
12. replacement D2 comparison output hash and terminal result;
13. D2 nine-normal-case per-field maximum differences and worst cases;
14. D2 near-tie categorical/numerical comparison including `gap`/`bound`;
15. D2 numerical/categorical/KKT/boundary mismatch counts;
16. D3 360-case per-field maximum differences/worst cases and categorical mismatch counts if reached;
17. complete scientific mismatch list;
18. complete source/environment failure list;
19. forbidden-operation check;
20. git status;
21. acceptance level;
22. exact recommended next gate.

## 12. Explicit prohibitions

Do not:

- rerun D1;
- rerun D2 MATLAB;
- rerun D2 Python;
- rerun any accepted diagnostic or engineering preflight;
- modify any D2 persisted output;
- modify MATLAB/Python production source/tests/helpers/cache;
- modify frozen scientific manifest;
- alter any row field/value/order/schema;
- fabricate/unionize heterogeneous fields;
- add/remove comparator fields;
- change numerical tolerances;
- weaken categorical terminal semantics;
- change D2/D3 cases, equations, roots, KKT, multipliers, parameters, states/shadows/derivatives, outputs, expected values, or ordering;
- add the MATLAB `raah/Rah` taper;
- use production bare-`a` FOC as corrected oracle;
- add `Tt/rb_gap` adapters;
- hard-code expected Python/MATLAB outputs;
- repair/rerun a failed preflight/comparison/scientific stage in the same task;
- run full HJB/KFE/steady state;
- rerun P3/P4/R4;
- run upper-`a` asset-tail diagnostics;
- enter AR(1), transition, IRF, calibration extension, dynamics, or Results;
- revoke or reissue P5.

## 13. Recommended next-gate rule

If PASS, recommend only the already-identified upper-`a` asset-tail robustness gate before actual dynamic execution.

If material contradiction, recommend the smallest Owner/reviewer diagnosis of the exact D2/D3 mismatched scientific object.

If blocked, recommend only the smallest new source/environment correction gate for the newly observed blocker.
