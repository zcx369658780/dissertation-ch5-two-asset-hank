# Chapter 5 Two-Asset HANK Post-P5 D2 Heterogeneous-Case Container Correction and Resumption Report

## Terminal classification

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The authorized heterogeneous-input correction and ten-case no-model preflight passed. The single replacement D2 MATLAB call then reached the unchanged result aggregation and failed at `d2_matlab_corrected.m:13`: its zero-field `rows=struct([])` container could not accept a whole 17-field result struct. No valid `d2_matlab.json` was persisted. The task prohibited broadening the input-only correction, repair, or rerun, so D2 Python/comparison and all D3 calls were not entered.

This is a newly exposed D2 output-container blocker, not a scientific mismatch. P5 remains Owner-accepted and the voluntary dynamic hold continues.

## Live authority and source continuity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Live start `origin/main` after fresh fetch: `675475c5b5f0ecc87a153895fbf554ccbe509418`
- Live `origin/main` at report freeze, before report-only publication: `675475c5b5f0ecc87a153895fbf554ccbe509418`
- P5 marker verified: `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`.
- Hold verified: `DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`.
- Accepted Python baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`: empty before preflight, before the replacement call, and at report freeze.

## Artifact roots and protected identities

- Original household-decision root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-artifacts-20260829-220000`.
- Accepted D1/resumption root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-resumption-artifacts-20260829-223000`.
- Fresh D2 successor root: `D:\ProjectTemp\ch5-post-p5-d2-container-resumption-artifacts-20260830-001000`.

| Object | SHA-256 | Status |
|---|---|---|
| frozen scientific `manifest.json` | `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA` | unchanged |
| original blocked `d2_matlab.m` | `8067196C2C680926490B6231EE2FF3125DD43B26AB812A1566719043E270C7C9` | verified |
| `d2_python.py` | `DD9DDCB675BE7A5C3A672CF1936AB7CBA1553AC8334989B2CDAA777FB2914344` | unchanged; not run |
| `compare.py` | `5C6FDBEBDA8BA67D819E69808A43C076E8F7BCB3C85788DABD942CC35EB40BE7` | unchanged; not run |
| corrected D1/D3 MATLAB evaluator | `5D94EDF89259D543758E490EA25C9359C1B65588CF7BB0557EEEDFA6B7FF3F9A` | unchanged; D3 not run |
| D3 Python evaluator | `6054A0C59E7C0CD0C83AD1919C3CFAF7B2987D0545EE4CEB26B3345FF2D01ABC` | unchanged; not run |
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | protected; not called |
| `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | protected |
| production `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | protected; not used as corrected oracle |
| `lab_solve2.m` | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` | protected; not called |
| accepted O1 helper | `B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315` | protected |

No production source, helper, test, or cache was modified.

## D1 evidence reuse and zero-call confirmation

Accepted D1 evidence was rehashed and reused:

- MATLAB: `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`;
- Python: `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`;
- comparison: `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`.

Accepted result remains `432/432 PASS`, `216/216` low-`a` PASS, every scalar maximum absolute difference `0`, and all sign/direction mismatch counts `0`.

D1 calls in this successor: MATLAB `0`, Python `0`, comparison `0`.

## Exact decoded container type and blocker diagnosis

The no-model MATLAB preflight established that `jsondecode` represents the heterogeneous frozen `p2` array as a `10×1 cell` array. Each cell contains one scalar struct with the case-specific fields. Consequently:

- invalid predecessor access: `c=m.p2(k)` returns a cell, so `c.id` is invalid;
- correct input traversal: `c=m.p2{k}` returns the frozen scalar case struct;
- the order and values are unchanged.

The corrected accessor supports the observed cell contract while retaining homogeneous-struct access as a non-scientific parsing fallback.

## Complete original-to-corrected D2 diff

```diff
-function d2_matlab
+function d2_matlab_corrected
```

Classification: `JSON_ACCESS_PLUMBING_ONLY` — external filename/callable alignment only.

```diff
-for k=1:numel(m.p2); c=m.p2(k); id=c.id;
+for k=1:numel(m.p2); c=get_case(m.p2,k); id=c.id;
```

Classification: `INPUT_CONTAINER_TRAVERSAL_ONLY` — obtains the same frozen k-th case under its decoded container contract.

```diff
+function c=get_case(container,k)
+if iscell(container); c=container{k}; else; c=container(k); end
+end
```

Classification for all added lines: `INPUT_CONTAINER_TRAVERSAL_ONLY` — only cell/struct element extraction is normalized.

No formula, root, KKT, multiplier, parameter, tolerance, case, ordering, result-container, or expected-output line changed.

## Frozen successor artifacts and preflight

| Artifact | SHA-256 |
|---|---|
| corrected `d2_matlab_corrected.m` | `57FFAD7DA9DCBA043EC40B21C647AD8621E1D973C9670A7C73EF0E2E5F6F868E` |
| `heterogeneous_container_preflight.m` | `E85D11AE208CD37CE9E09A61EC327289872DEB82DDBA6D5EADBBFCB635CA75F8` |
| frozen successor ledger | `044E63121C4DE636B8D58A8D2902FBFD9045D7FBBD40D32168816976531EE743` |
| `harness_diff.md` | `CE614EA907942E7EE550D5FD77CE279859E0D9D92285FD5700651E00A8649191` |
| `successor_freeze.json` | `B3F6F1BCC42EDC90A17E30C081B1304EB2D56A6C7103594F4811A2A7349F6D7D` |
| final `execution_results.json` | `730A7A297096E5DA55C9B3826C372F82CDD0C216DD5A0E3B9173CDF607647377` |

Single no-model MATLAB preflight result:

- invocation count: `1`;
- decoded container: `cell`, size `10×1`;
- cases accessed: `10/10`;
- exact order: PASS;
- distinct IDs: `10/10`;
- required fields addressable for every case: PASS;
- skipped/duplicated/reordered/merged cases: `0/0/0/0`;
- exit status: `0`;
- read-back: PASS;
- `heterogeneous_preflight.json` SHA-256: `DCC7A02E8AD4A695AA1F725AA4CB1A606FEFFB85DEDDE3E26CC1A915E50B9FA5`.

## Historical and successor call counts

- historical predecessor D1 blocked MATLAB: `1`;
- accepted D1 replacement MATLAB/Python/comparison: `1/1/1` historical, reused only;
- historical predecessor D2 MATLAB blocked at input traversal: `1`;
- successor replacement D2 MATLAB: `1`;
- successor D2 Python/comparison: `0/0`;
- successor D3 MATLAB/Python/comparison: `0/0/0`;
- successor D1 MATLAB/Python/comparison: `0/0/0`;
- scientific reruns within this task: `0`.

## Replacement D2 outcome and requested comparisons

The replacement D2 MATLAB process crossed the corrected input traversal and then failed at `d2_matlab_corrected.m:13` on:

`rows(k)=struct(...)`

The frozen evaluator still declares `rows=struct([])`, a zero-field struct array. Whole-struct assignment of the normal 17-field D2 result therefore raised MATLAB's dissimilar-structure assignment error. This result-container line was deliberately not changed because the live task authorized input-container/JSON-access plumbing only and explicitly required stopping rather than silently broadening scope.

- valid persisted D2 rows: `0/10`;
- `d2_matlab.json`: absent;
- per-field maximum differences and worst cases: `NOT_AVAILABLE_BLOCKED_BEFORE_VALID_D2_OUTPUT` for `c`, `l`, `d`, cost, `mu_a`, `mu_b`, utility, Hamiltonian, `lambda_a`, `lambda_b`, and KKT residual;
- direction mismatch counts: `NOT_AVAILABLE`;
- multiplier mismatch counts: `NOT_AVAILABLE`;
- boundary-feasibility mismatch count: `NOT_AVAILABLE`.

No D2 scientific PASS or FAIL is inferred.

## D3 disposition

D3 was not reached. All 360 gamma-2/phi-5 cases remain frozen and unexecuted in this successor. Per-field differences, worst cases, labor/transfer maxima, and categorical mismatches are `NOT_REACHED`.

## Complete mismatch and failure lists

Scientific mismatch list: empty. No valid D2 or D3 comparison occurred.

Source/environment failure list contains exactly one entry:

| Stage | Location | Failure | Interpretation |
|---|---|---|---|
| replacement D2 MATLAB | `d2_matlab_corrected.m:13` | zero-field output struct container cannot accept the 17-field result row; nonzero exit; no JSON persisted | newly exposed external result-container blocker, outside this input-only correction authority |

Preflight failures: none. Input-container traversal failures after correction: none.

## Forbidden-operation and Git check

- D1 rerun: no (`0/0/0`)
- frozen D2/D3 cases/order/equations/parameters/state/shadow inputs/tolerances changed: no
- production MATLAB/Python source/tests/helpers/cache modified: no
- taper added, production bare-`a` FOC used as oracle, or `Tt`/`rb_gap` adapter added: no
- Python results imported/hard-coded into MATLAB: no
- D2 scientific evaluation changed: no
- failed replacement D2 repaired/rerun: no
- full HJB/KFE/steady state or P3/P4/R4: `0`
- asset-tail, AR(1), transition, IRF, dynamics, calibration extension, or Results: `0`
- P5 revoked/reissued: no

Git status at report freeze: the sole repository change was this authorized report; no unrelated tracked or untracked repository paths were present. Final remote identity and clean status require post-publication verification.

## Acceptance level and exact next gate

Acceptance level: D1 remains fully accepted; D2 input-container traversal is now conclusively corrected and preflight-qualified; the supplementary D2→D3 parity gate remains incomplete solely because the next external D2 output-container defect prevented persistence. P5 remains accepted and the dynamic hold continues.

Exact recommended next gate: a smallest D2 result-container preallocation/serialization correction and resumption task that:

1. reuses the corrected input traversal and all existing frozen scientific content;
2. changes only D2 result-row schema/preallocation/serialization plumbing;
3. runs one no-model heterogeneous-result-schema assignment/JSON preflight;
4. explicitly authorizes exactly one replacement D2 MATLAB call because the call here was consumed by that output-container defect;
5. conditionally completes D2 Python/comparison and unchanged D3.

D1 must remain reuse-only with zero calls. No asset-tail or dynamic work should begin until D2 and D3 complete.
