# CH5_TWO_ASSET_HANK_POST_P5_D2_PYTHON_CHECK_BOUNDARY_ARITY_CORRECTION_AND_RESUMPTION

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Purpose

Resume the post-P5 household-decision parity experiment after the explicit UTF-8 D2 Python manifest correction passed, but the single replacement D2 Python call was consumed by an external harness/API call-shape defect before valid persistence.

Latest accepted report:

`docs/CH5_TWO_ASSET_HANK_POST_P5_D2_PYTHON_UTF8_MANIFEST_DECODING_CORRECTION_AND_RESUMPTION_REPORT.md`

Accepted terminal classification:

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The latest accepted report establishes:

- D1 remains accepted at `432/432 PASS`, including `216/216` low-`a` PASS, with every compared scalar maximum difference `0` and all sign/direction mismatch counts `0`;
- the corrected D2 MATLAB output is already valid and persisted as exactly ten frozen cases;
- the explicit UTF-8 manifest decoding correction and one-shot preflight passed without changing manifest bytes or semantics;
- the replacement D2 Python call passed manifest decoding and entered the first frozen case;
- it then failed because the external harness called `check_boundary(*idx,3,3,ma,mb,tol)`, where `idx` is a three-element `(i_a,i_b,i_z)` tuple, producing eight positional arguments;
- the accepted production interface is seven positional arguments: `check_boundary(i_a,i_b,n_a,n_b,mu_a,mu_b,tolerance)`;
- no D2 Python output, D2 comparison, or D3 scientific execution followed.

This task authorizes only a static interface audit, the minimum external D2 Python call-shape correction, one no-model interface preflight, one replacement D2 Python call, and—conditional on valid D2 Python persistence—the already accepted comparator and frozen D3 sequence.

P5 remains Owner-accepted:

`MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`

The voluntary hold remains:

`DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`

## 2. Live authority and continuity

Task-authoring parent observed before publication:

`e2d2daca2c63b6182746fb1ff12503239a3eae1d`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task and all controlling predecessor tasks/reports exist on live `main`;
3. record live start SHA;
4. verify the P5 marker and active dynamic hold;
5. verify accepted Python production `src/tests` continuity from baseline `7a2388a2ba89073e307f05a909570e8c40a4be13` using:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

It must be empty.

## 3. Accepted evidence to reuse without rerun

### D1

Re-verify hashes only. D1 call budget is exactly `0/0/0`.

- MATLAB `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`
- Python `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`
- comparison `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`

### D2 MATLAB / comparator / root / encoding evidence

Re-verify and reuse without rerun:

- frozen scientific manifest `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA`;
- accepted persisted D2 MATLAB output `26F9E628021327D02897FE96A2FBAA52D1AF4434629676E03BD6614708D6E977`;
- accepted corrected comparator `FAF1A6ABB9F21E7DABD6CFB0857A72354CC3A5D0D532F4968F027E5CBBC0ECB5`;
- accepted comparator preflight `52F55586BAFA456BC811E4CAD885F7C26DD30FF9F15165C405515C6CEAB1D0F9`;
- accepted heterogeneous MATLAB preflight `815C6703FECE0438B0584C3AD16A1A772D3A42D2AA57C7F2A4FBA0BF6F6808A4`;
- accepted root diagnostic `6C77624B69F1ECED1E54A216ABBA8D5BF28A031B83672AA74268774B8A26268C`;
- accepted corrected-root preflight `2B01AD00F0CCF151D6BDC3EE46E476DA4BEC63FEE3A98B34CF299B0B5EEE8AB6`;
- accepted UTF-8-corrected external D2 Python harness `C60CF89CCCC01E359D1F8BBB9D8918132E0569B463AD524101D66F51DE1483F7`;
- accepted UTF-8 preflight result `5E3C17CC617EF03AE8D80D55736F2A79B7124A6E6DE16C630F54A69386025EF0`;
- frozen D3 MATLAB `5D94EDF89259D543758E490EA25C9359C1B65588CF7BB0557EEEDFA6B7FF3F9A`;
- frozen D3 Python `6054A0C59E7C0CD0C83AD1919C3CFAF7B2987D0545EE4CEB26B3345FF2D01ABC`.

D2 MATLAB call budget in this task is exactly `0`.

Do not rerun any accepted diagnostic or engineering preflight above.

## 4. Existing accepted API-arity authority

Read and treat as directly relevant accepted precedent:

`docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P2_PYTHON_HARNESS_API_ARITY_CORRECTION_AND_COMPLETION_REPORT.md`

That accepted predecessor established all of the following:

- production signature:

  `check_boundary(i_a,i_b,n_a,n_b,mu_a,mu_b,tolerance)`

- the three-element policy/state index tuple includes productivity index `idx[2]`, but `check_boundary` is defined only on the two asset-grid indices;
- the accepted external-harness correction was exactly:

```diff
-bc=check_boundary(*idx,3,3,ma,mb,tol)
+bc=check_boundary(idx[0],idx[1],3,3,ma,mb,tol)
```

- `idx[2]` is intentionally omitted from this boundary API call;
- no scientific state, case, formula, classification, output, orientation, or tolerance changed;
- the corrected predecessor P2 Python harness subsequently completed all ten frozen P2 cases and passed comparison.

Do not assume the current D2 harness is byte-identical to that historical P2 harness. First verify the current call site and surrounding semantics statically.

## 5. Mandatory static call-shape audit

Before writing a corrected harness or running any new Python process, inspect read-only:

1. current production `src/ch5_two_asset_hank/boundaries.py` and record the exact live `check_boundary` signature;
2. accepted UTF-8-corrected external D2 Python harness SHA-256 `C60CF89CCCC01E359D1F8BBB9D8918132E0569B463AD524101D66F51DE1483F7`;
3. every `check_boundary` call site in that external D2 harness;
4. the construction and meaning of every `idx` value passed to those calls;
5. whether `idx` is always exactly `(i_a,i_b,i_z)` for the frozen D2 cases;
6. whether any other API call in the D2 harness expands `idx` or has an analogous arity mismatch;
7. the accepted predecessor arity-correction report cited above.

Report exactly:

- production parameter names/order/count;
- external call expression(s);
- expanded positional count for each call shape;
- semantic meaning of `idx[0]`, `idx[1]`, `idx[2]`;
- whether omission of `idx[2]` is exactly consistent with production boundary semantics;
- whether the historical accepted correction can be reused verbatim in the current D2 harness except for the already-accepted UTF-8 change.

If any scientific ambiguity exists—for example, if `idx[2]` is used by the current boundary API or if current `idx` semantics differ from the accepted predecessor—stop before correction and report the smallest contradiction. Do not guess.

## 6. Frozen call-shape authority

If the static audit confirms the accepted diagnosis, freeze:

`D2_PYTHON_CHECK_BOUNDARY_ASSET_INDEX_ARITY_CORRECTION`

The corrected external D2 Python harness must preserve the accepted UTF-8 decoding line and change only the boundary API call shape from:

```python
check_boundary(*idx, 3, 3, ma, mb, tol)
```

to:

```python
check_boundary(idx[0], idx[1], 3, 3, ma, mb, tol)
```

or the exact syntactic equivalent required by the current harness.

Scientific meaning:

- `idx[0]` = illiquid-asset grid index `i_a`;
- `idx[1]` = liquid-asset grid index `i_b`;
- `idx[2]` = productivity-state index `i_z`, intentionally not part of the asset-boundary feasibility API;
- `n_a=3`, `n_b=3`, `mu_a=ma`, `mu_b=mb`, `tolerance=tol` remain unchanged.

Every changed line for this new correction must be classified exactly:

`BOUNDARY_API_ARITY_PLUMBING_ONLY`

The previously accepted UTF-8 change remains unchanged and is not a new scientific modification.

Forbidden changes include:

- changing `idx` values or case definitions;
- changing `n_a`, `n_b`;
- changing `mu_a`, `mu_b`;
- changing boundary tolerance;
- changing `check_boundary` production source;
- changing any root, KKT, multiplier, policy, equation, parameter, output field, ordering, or expected result;
- changing any other external D2 call unless a separately authorized contradiction is discovered.

## 7. One no-model interface preflight

Work in a fresh no-overwrite external artifact root.

Before execution freeze/hash/read back:

- corrected D2 Python harness;
- complete original-to-corrected diff relative to the accepted UTF-8-corrected harness;
- one engineering-only interface preflight;
- unchanged manifest;
- unchanged persisted D2 MATLAB output;
- unchanged comparator;
- unchanged D3 harnesses;
- successor execution ledger.

Run exactly one engineering-only Python preflight invocation. It must not execute the D2 household case loop or any HJB/KFE/steady-state code.

The preflight must prove:

1. live production `check_boundary` exposes exactly seven positional parameters in the accepted order;
2. the corrected D2 call site supplies exactly seven positional arguments;
3. the original frozen call shape would supply eight when `idx=(i_a,i_b,i_z)`;
4. the corrected call omits only `idx[2]` and preserves `idx[0]`, `idx[1]`, `n_a`, `n_b`, `mu_a`, `mu_b`, and `tol` exactly;
5. at least four synthetic boundary-interface calls execute successfully without model evaluation, covering lower/lower, upper/upper, interior/interior, and one mixed asset-boundary index combination;
6. the returned object exposes the expected `feasible`, `violation`, `active_a`, and `active_b` fields;
7. a source/diff assertion verifies that no D2 scientific formula, case, parameter, tolerance, output, or UTF-8 decoding line changed;
8. exit zero.

If this one preflight fails, do not repair or rerun it in this task.

## 8. Exactly one replacement D2 Python call

The predecessor D2 Python calls already consumed are:

1. default-GBK manifest-decoder blocker: `1`;
2. UTF-8-corrected boundary-arity blocker: `1`.

After static audit and interface preflight PASS, this task explicitly authorizes exactly one new replacement D2 Python scientific harness call.

It must use:

- the exact frozen manifest bytes;
- the exact accepted UTF-8 decoding;
- the exact frozen ten D2 cases/order;
- accepted Python production source/tests;
- the exact accepted equations, roots, KKT, multipliers, parameters, states/shadows/derivatives, outputs, and tolerances;
- only the accepted seven-argument boundary call shape above.

Acceptance before comparison:

- process exits zero;
- `d2_python.json` exists;
- exactly ten rows in frozen order;
- 9 normal rows retain native 16-field schema;
- `lower_b_fz_near_tie` retains native 10-field schema;
- no fabricated fields;
- independent read-back succeeds.

If the replacement D2 Python call fails for any reason, do not repair or rerun it in this task. Stop fail-closed.

## 9. D2 comparison against accepted MATLAB output

Only after valid D2 Python persistence, execute exactly once the accepted corrected comparator:

`FAF1A6ABB9F21E7DABD6CFB0857A72354CC3A5D0D532F4968F027E5CBBC0ECB5`

Use the accepted persisted D2 MATLAB output:

`26F9E628021327D02897FE96A2FBAA52D1AF4434629676E03BD6614708D6E977`

Do not rerun D2 MATLAB.

The frozen comparison contract remains unchanged:

- every existing numerical tolerance remains unchanged;
- every categorical mismatch is terminal under `COMPARATOR_CATEGORICAL_MISMATCH_IS_TERMINAL_FAILURE`;
- near-tie `gap` and `bound` remain included;
- no comparison field may be added or removed.

If any valid D2 mismatch occurs, stop before D3 and return the material-contradiction terminal classification.

## 10. Frozen D3 after D2 PASS

If and only if D2 comparison passes, execute the frozen D3 sequence exactly once each:

- MATLAB decision harness: `1`;
- Python decision harness: `1`;
- accepted corrected comparator: `1`.

Use exactly the frozen 360 `gamma_c=2`, Python `phi=5`, MATLAB `frisch_l=.2` cases.

No D3 case, formula, parameter, ordering, tolerance, output field, or scientific rule may change.

If D3 hits a source/environment blocker, stop without same-task repair. If a valid D3 comparison mismatches, classify material contradiction.

## 11. Call budget

Historical calls remain recorded and are not erased:

- accepted D1 historical execution exists, but D1 calls in this task are exactly `0/0/0`;
- D2 MATLAB historical blockers and accepted corrected execution remain historical; D2 MATLAB calls in this task are exactly `0`;
- predecessor D2 Python default-GBK blocker: `1`;
- predecessor D2 Python UTF-8/arity blocker: `1`.

Calls authorized in this task:

- engineering interface preflight: at most `1`;
- replacement D2 Python: at most `1`, only after preflight PASS;
- D2 comparator: at most `1`, only after valid D2 Python persistence;
- D3 MATLAB/Python/comparator: at most `1/1/1`, only after D2 PASS.

No accepted diagnostic/preflight may be rerun. No full HJB, Python HJB/KFE/steady-state, P3/P4/R4, asset-tail, AR(1), transition, IRF, calibration extension, dynamics, or Results call is authorized.

## 12. Terminal classifications

Return exactly one.

### PASS

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_PASS__DYNAMIC_HOLD_MAY_ADVANCE_TO_ASSET_TAIL_GATE`

Use only if:

- the current D2 arity defect is statically identical in scientific meaning to the already accepted predecessor P2 arity defect;
- correction is strictly `BOUNDARY_API_ARITY_PLUMBING_ONLY`;
- the interface preflight passes;
- persisted D2 MATLAB output is reused without rerun;
- replacement D2 Python persists all ten native-schema rows;
- D2 comparator passes all ten cases;
- D3 all 360 cases pass;
- no forbidden mutation/rerun occurs.

### Material contradiction

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_MATERIAL_CONTRADICTION__DYNAMIC_HOLD_CONTINUES`

Use if a valid D2 or D3 numerical/categorical comparison shows a mismatch under the frozen accepted equations and comparison rules.

P5 is not automatically revoked.

### Blocked

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

Use if the arity diagnosis/correction cannot remain within authority, the interface preflight fails, replacement D2 Python fails before valid persistence/comparison, or D3 encounters a source/environment blocker before valid scientific comparison.

## 13. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_POST_P5_D2_PYTHON_CHECK_BOUNDARY_ARITY_CORRECTION_AND_RESUMPTION_REPORT.md`

The report must include at minimum:

1. terminal classification;
2. live start/final `origin/main`;
3. Python production `src/tests` continuity;
4. predecessor/successor artifact roots;
5. D1 artifact re-verification and exact zero-call confirmation;
6. accepted D2 MATLAB output hash/read-back and exact zero D2 MATLAB calls;
7. accepted UTF-8 correction/preflight evidence reused and no rerun;
8. production `check_boundary` signature and current D2 call-shape audit;
9. explicit comparison to the accepted historical P2 arity correction;
10. complete accepted-UTF8-harness to arity-corrected-harness diff with every new changed line classified `BOUNDARY_API_ARITY_PLUMBING_ONLY`;
11. corrected harness/interface-preflight/diff/ledger hashes;
12. interface preflight results;
13. historical/current D2 Python call ledger;
14. D2 Python output hash/schema/read-back;
15. D2 comparator call count and ten-case comparison summary;
16. D2 nine-normal-case per-field maximum differences and worst cases;
17. D2 near-tie full comparison including `gap`/`bound`;
18. D2 categorical/numerical/KKT/boundary mismatch counts;
19. D3 360-case per-field maximum differences/worst cases and categorical mismatch counts if reached;
20. complete scientific mismatch list;
21. complete source/environment failure list;
22. forbidden-operation check;
23. git status;
24. acceptance level;
25. exact recommended next gate.

## 14. Explicit prohibitions

Do not:

- rerun D1;
- rerun D2 MATLAB;
- rerun accepted UTF-8/root/heterogeneous/comparator diagnostics or preflights;
- modify production MATLAB/Python source/tests/helpers/cache;
- modify production `check_boundary`;
- modify the manifest bytes or semantic content;
- modify persisted D2 MATLAB output;
- modify the accepted comparator;
- change D2/D3 cases, order, equations, roots, KKT, multipliers, parameters, state/shadow/derivative inputs, outputs, or tolerances;
- alter `n_a`/`n_b`, `mu_a`/`mu_b`, or boundary tolerance in the corrected call;
- add the MATLAB `raah/Rah` taper;
- use production bare-`a` FOC as corrected oracle;
- add `Tt/rb_gap` adapters;
- hard-code expected MATLAB/Python answers;
- repair or rerun a failed interface preflight, replacement D2 Python, or D3 stage in this task;
- run full HJB/KFE/steady state;
- rerun P3/P4/R4;
- run asset-tail diagnostics;
- enter AR(1), transition, IRF, calibration extension, dynamics, or Results;
- revoke or reissue P5.

## 15. Recommended next gate rule

If D2 and D3 pass, recommend only the already-identified upper-`a` asset-tail robustness gate before actual dynamic execution.

If a valid D2/D3 mismatch is observed, recommend the smallest Owner/reviewer diagnosis of the exact mismatch.

If blocked, recommend only the smallest new source/environment/interface correction gate for the newly observed blocker.
