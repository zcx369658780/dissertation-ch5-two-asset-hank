# CH5_TWO_ASSET_HANK_POST_P5_D2_PYTHON_UTF8_MANIFEST_DECODING_CORRECTION_AND_RESUMPTION

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Resume the post-P5 household-decision parity experiment after the corrected MATLAB D2 evaluator successfully persisted all ten frozen cases but the single D2 Python call failed before scientific case evaluation because the external Python harness used the platform default GBK decoder to read a UTF-8 manifest containing a Chinese MATLAB-source path.

Latest accepted report:

`docs/CH5_TWO_ASSET_HANK_POST_P5_D2_LOWER_A_ACTIVE_ROOT_CERTIFICATION_DIAGNOSIS_AND_RESUMPTION_REPORT.md`

Accepted terminal classification:

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The latest accepted report establishes:

- D1 remains accepted at `432/432 PASS`, including `216/216` low-`a` PASS, with all compared scalar maximum differences `0` and all sign/direction mismatch counts `0`;
- the D2 heterogeneous serialization contract and comparator are already qualified;
- the root diagnostic classified the prior MATLAB failure as `LOWER_A_ACTIVE_ROOT_CERTIFICATION_SOLVER_REPRESENTATION_DEFECT`;
- the bounded external `cert_root` refinement and corrected-root preflight passed without changing the root equation, bracket, or `1e-12` certification tolerance;
- the replacement D2 MATLAB call exited zero and persisted exactly ten frozen rows;
- the subsequent D2 Python call failed at manifest loading with `UnicodeDecodeError: 'gbk' codec can't decode ...` before case evaluation;
- no D2 comparison or D3 execution followed.

This task authorizes only the minimum external Python manifest text-decoding correction, one no-science encoding preflight, one replacement D2 Python call, and—conditional on valid D2 Python persistence—the existing corrected comparator and frozen D3 sequence.

P5 remains Owner-accepted:

`MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`

The voluntary route hold remains:

`DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`

## 2. Live authority and continuity

Task-authoring parent observed before publication:

`26ae01eea1a5588745c5cdad77eabb631b56e0d8`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task and all controlling predecessor tasks/reports exist on live `main`;
3. record live start SHA;
4. verify the P5 marker and active dynamic hold;
5. verify accepted Python production `src/tests` continuity from baseline `7a2388a2ba89073e307f05a909570e8c40a4be13` with:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

It must be empty.

## 3. Accepted evidence to reuse without rerun

### D1

Re-verify hashes only. Do not rerun D1.

- MATLAB `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`
- Python `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`
- comparison `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`

D1 call budget in this task: exactly `0/0/0`.

### D2 MATLAB and engineering evidence

Re-verify and reuse without rerun:

- frozen scientific manifest SHA-256 `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA`;
- original frozen D2 Python SHA-256 `DD9DDCB675BE7A5C3A672CF1936AB7CBA1553AC8334989B2CDAA777FB2914344`;
- accepted corrected comparator SHA-256 `FAF1A6ABB9F21E7DABD6CFB0857A72354CC3A5D0D532F4968F027E5CBBC0ECB5`;
- accepted comparator preflight result SHA-256 `52F55586BAFA456BC811E4CAD885F7C26DD30FF9F15165C405515C6CEAB1D0F9`;
- accepted heterogeneous MATLAB preflight result SHA-256 `815C6703FECE0438B0584C3AD16A1A772D3A42D2AA57C7F2A4FBA0BF6F6808A4`;
- accepted root diagnostic result SHA-256 `6C77624B69F1ECED1E54A216ABBA8D5BF28A031B83672AA74268774B8A26268C`;
- accepted corrected-root preflight result SHA-256 `2B01AD00F0CCF151D6BDC3EE46E476DA4BEC63FEE3A98B34CF299B0B5EEE8AB6`;
- accepted corrected D2 MATLAB harness SHA-256 `A0E3426F1FB58563821C429A119445B659933D7E321E0EFBD3A7EED4690D8E51`;
- persisted D2 MATLAB output SHA-256 `26F9E628021327D02897FE96A2FBAA52D1AF4434629676E03BD6614708D6E977`.

The persisted D2 MATLAB output is accepted input to this task and must not be regenerated. Verify read-back:

- exactly 10 ordered rows;
- 9 native 16-field normal rows;
- 1 native 10-field `lower_b_fz_near_tie` row;
- no fabricated union fields.

D2 MATLAB scientific call budget in this task: exactly `0`.

Do not rerun the accepted root diagnostic, corrected-root preflight, heterogeneous MATLAB preflight, or comparator preflight.

## 4. Mandatory static Python decoding audit

Before any new Python execution, inspect the frozen external D2 Python harness and the manifest read site that failed.

Report exactly:

- the manifest path supplied to the harness;
- the exact source line/expression that opens/loads the manifest;
- whether an explicit encoding is absent;
- the observed Windows default text encoding from the predecessor failure (`gbk`);
- whether the harness reads any other scientific input text files through the same default-decoder pattern;
- whether the failed call occurred before importing/evaluating any D2 scientific case outputs.

Verify the manifest bytes themselves are unchanged and match SHA-256:

`D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA`

Do not rewrite, normalize, re-encode, or regenerate the manifest.

If the failure is not fully explained by an absent explicit UTF-8 decoder at the manifest load, stop before correction and report the smallest exact contradiction.

## 5. Frozen text-decoding authority

If the static audit confirms the predecessor diagnosis, freeze:

`D2_PYTHON_MANIFEST_TEXT_ENCODING_UTF8_EXPLICIT`

Meaning:

- the manifest bytes remain exactly unchanged;
- the manifest semantic JSON content remains exactly unchanged;
- the external D2 Python harness must decode that manifest explicitly as UTF-8;
- no scientific input, case, parameter, equation, tolerance, ordering, output field, expected answer, or algorithm changes.

Preferred bounded correction:

Change only the manifest text open/load site from a platform-default text open to an explicit UTF-8 text open, e.g. `open(path, encoding="utf-8")` or an exactly equivalent explicit UTF-8 decoding construct.

Do not set or rely on a broad process-global locale/codepage/environment change when a single explicit manifest-open correction is sufficient.

Every changed line must be classified exactly:

`INPUT_TEXT_ENCODING_UTF8_ONLY`

If more than text-decoding plumbing would have to change, stop before preflight.

## 6. One no-science UTF-8 manifest preflight

Work in a fresh no-overwrite external artifact root.

Before execution, freeze/hash/read back:

- corrected D2 Python harness;
- original-to-corrected diff;
- one engineering-only UTF-8 manifest preflight;
- unchanged scientific manifest;
- unchanged persisted D2 MATLAB output;
- unchanged corrected comparator;
- unchanged frozen D3 harnesses;
- successor execution ledger.

Run exactly one engineering-only Python preflight invocation. It must not call the D2 household evaluator or any production model function.

The preflight must prove all of the following:

1. the frozen manifest SHA-256 is unchanged;
2. decoding the manifest bytes explicitly as UTF-8 succeeds;
3. JSON parsing succeeds;
4. the parsed D2 case count is exactly 10;
5. the ten D2 case IDs and order exactly match the frozen manifest authority;
6. the Chinese MATLAB-source path is decoded without replacement characters or content mutation;
7. a semantic round-trip check of the parsed object does not alter the in-memory case values used by the harness;
8. no scientific evaluator is imported/called for the preflight;
9. exit zero.

Do not rewrite the manifest as part of the preflight.

If the preflight fails, do not repair or rerun it in this task.

## 7. Exactly one replacement D2 Python call

The predecessor D2 Python call was consumed before scientific case evaluation by the default-GBK manifest decoder failure. After the static audit and UTF-8 preflight pass, this task explicitly authorizes exactly one replacement D2 Python scientific harness call using the corrected external harness.

The replacement call must use:

- the exact frozen manifest bytes;
- the exact frozen ten D2 cases/order;
- the exact accepted Python production source/tests;
- the exact frozen equations, roots, KKT logic, parameters, states/shadows/derivatives, outputs, and tolerances.

Acceptance before comparison:

- process exits zero;
- `d2_python.json` exists;
- exactly 10 rows are present in frozen order;
- 9 normal rows have the native 16-field schema;
- `lower_b_fz_near_tie` has the native 10-field schema;
- no fabricated fields;
- independent read-back succeeds.

If the replacement D2 Python call fails for any reason, do not repair or rerun it in this task. Stop fail-closed.

## 8. D2 comparison using accepted persisted MATLAB output

Only after valid D2 Python persistence, run exactly once the already accepted corrected comparator SHA-256:

`FAF1A6ABB9F21E7DABD6CFB0857A72354CC3A5D0D532F4968F027E5CBBC0ECB5`

Use the accepted persisted MATLAB output SHA-256:

`26F9E628021327D02897FE96A2FBAA52D1AF4434629676E03BD6614708D6E977`

Do not rerun MATLAB D2.

The D2 comparison contract remains frozen:

- all numerical mismatches use their already accepted frozen tolerance rules;
- all categorical mismatches are terminal under `COMPARATOR_CATEGORICAL_MISMATCH_IS_TERMINAL_FAILURE`;
- near-tie `gap` and `bound` are included under the frozen floating rule;
- no comparison field may be added or removed.

If any valid D2 scientific mismatch occurs, stop before D3 and return the material-contradiction terminal classification.

## 9. Frozen D3 after D2 PASS

If and only if D2 comparison passes, execute the frozen D3 sequence exactly once each:

- MATLAB decision harness: `1`;
- Python decision harness: `1`;
- accepted corrected comparator: `1`.

Use exactly the frozen 360 `gamma_c=2`, Python `phi=5`, MATLAB `frisch_l=.2` cases.

No D3 case, formula, parameter, ordering, tolerance, output field, or scientific rule may change.

If D3 hits a source/environment blocker, stop without same-task repair. If a valid D3 comparison mismatches, classify material contradiction.

## 10. Call budget

Historical calls remain recorded and are not erased:

- original D1 MATLAB blocked call: `1`;
- accepted D1 replacement MATLAB/Python/comparison: `1/1/1` historical, reused only;
- D2 MATLAB input-container blocker: `1`;
- D2 MATLAB zero-field-output blocker: `1`;
- D2 MATLAB root-certification blocker: `1`;
- accepted corrected replacement D2 MATLAB: `1` historical, reused output only;
- predecessor D2 Python default-GBK blocker: `1`.

Calls authorized in this task:

- D1 MATLAB/Python/comparison: exactly `0/0/0`;
- D2 MATLAB: exactly `0`;
- accepted engineering preflights/diagnostics: `0` new calls;
- UTF-8 engineering preflight: at most `1`;
- replacement D2 Python: at most `1`, only after preflight PASS;
- D2 comparator: at most `1`, only after valid D2 Python persistence;
- D3 MATLAB/Python/comparator: at most `1/1/1`, only after D2 PASS.

No full HJB, Python HJB/KFE/steady-state, P3/P4/R4, asset-tail, AR(1), transition, IRF, calibration extension, dynamics, or Results call is authorized.

## 11. Terminal classifications

Return exactly one.

### PASS

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_PASS__DYNAMIC_HOLD_MAY_ADVANCE_TO_ASSET_TAIL_GATE`

Use only if:

- the correction is strictly explicit UTF-8 manifest decoding only;
- the UTF-8 preflight passes;
- the persisted D2 MATLAB output is reused without rerun;
- replacement D2 Python persists all ten native-schema rows;
- D2 comparator passes all ten cases;
- D3 all 360 cases pass;
- no forbidden mutation/rerun occurs.

### Material contradiction

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_MATERIAL_CONTRADICTION__DYNAMIC_HOLD_CONTINUES`

Use if a valid D2 or D3 numerical/categorical comparison shows any material mismatch under the frozen accepted equations and comparator rules.

P5 is not automatically revoked.

### Blocked

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

Use if the UTF-8 diagnosis/correction cannot remain within authority, the UTF-8 preflight fails, replacement D2 Python fails before valid comparison, or D3 encounters a source/environment blocker before valid scientific comparison.

## 12. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_POST_P5_D2_PYTHON_UTF8_MANIFEST_DECODING_CORRECTION_AND_RESUMPTION_REPORT.md`

The report must include at minimum:

1. terminal classification;
2. live start/final `origin/main`;
3. Python production `src/tests` continuity;
4. predecessor/successor artifact roots;
5. D1 artifact re-verification and exact zero-call confirmation;
6. accepted D2 MATLAB output hash/read-back and exact zero D2 MATLAB calls;
7. exact manifest-open/default-decoder diagnosis;
8. complete D2 Python original-to-corrected diff with every changed line classified `INPUT_TEXT_ENCODING_UTF8_ONLY`;
9. corrected harness/preflight/diff/ledger hashes;
10. UTF-8 preflight result, including manifest hash, case IDs/order, and Chinese path integrity;
11. historical and current D2 Python call ledger;
12. D2 Python output hash/schema/read-back;
13. D2 comparator call count and ten-case comparison summary;
14. D2 nine-normal-case per-field maximum differences and worst cases;
15. D2 near-tie full categorical/numerical comparison including `gap`/`bound`;
16. D2 categorical/numerical/KKT/boundary mismatch counts;
17. D3 360-case per-field maximum differences/worst cases and categorical mismatch counts if reached;
18. complete scientific mismatch list;
19. complete source/environment failure list;
20. forbidden-operation check;
21. git status;
22. acceptance level;
23. exact recommended next gate.

## 13. Explicit prohibitions

Do not:

- rerun D1;
- rerun D2 MATLAB;
- rerun any accepted MATLAB/comparator/root engineering diagnostic or preflight;
- modify the frozen manifest bytes or semantic JSON content;
- modify MATLAB/Python production source/tests/helpers/cache;
- modify the accepted corrected comparator;
- modify frozen D2 scientific cases/order/equations/roots/KKT/multipliers/parameters/states/shadows/derivatives/outputs/tolerances;
- alter the corrected MATLAB root certification or D2 MATLAB output;
- set a broad locale/codepage/PYTHONUTF8 environment change when a local explicit UTF-8 manifest open suffices;
- add the MATLAB taper;
- use production bare-`a` FOC as corrected oracle;
- add `Tt/rb_gap` adapters;
- hard-code expected outputs;
- repair/rerun a failed replacement D2 Python or D3 stage in this same task;
- run full HJB/KFE/steady state;
- rerun P3/P4/R4;
- run asset-tail diagnostics;
- enter AR(1), transition, IRF, dynamics, calibration extension, or Results;
- revoke or reissue P5.

## 14. Recommended next gate rule

If PASS, recommend only the already-identified post-P5 upper-`a` asset-tail robustness gate before actual dynamic execution.

If a valid scientific contradiction appears, recommend only the smallest Owner/reviewer diagnosis of the exact mismatched D2/D3 household-decision object.

If blocked, recommend only the smallest newly exposed source/environment correction gate.