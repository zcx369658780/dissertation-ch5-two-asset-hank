# Chapter 5 Two-Asset HANK Post-P5 Household Decision-Map Parity MATLAB Struct-Harness Correction and Resumption Report

## Terminal classification

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The authorized MATLAB result-container correction and synthetic preflight passed. Replacement D1 then completed and all 432 corrected common-equation cases passed exactly, including all 216 low-`a` cases. The next frozen step, unmodified predecessor D2 MATLAB, failed after start at `d2_matlab.m:3` before producing a valid output. Per the task, it was not repaired or rerun, and D2 Python/comparison plus D3 were not entered.

This is a new D2 external harness/input-container blocker, not a scientific mismatch. P5 remains Owner-accepted and is neither revoked nor reissued. The voluntary dynamic hold continues.

## Live authority and source continuity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Live start `origin/main` after fresh fetch: `56039fc01d499eaa9dea34e2988e1438c5196623`
- Live `origin/main` at report freeze, before report-only publication: `56039fc01d499eaa9dea34e2988e1438c5196623`
- Owner P5 marker: `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`.
- Route hold: `DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`.
- Accepted Python baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`: empty before preflight, before scientific execution, and at report freeze.

## Artifact roots and protected identities

- Predecessor artifact root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-artifacts-20260829-220000`.
- Fresh successor artifact root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-resumption-artifacts-20260829-223000`.
- Unchanged predecessor scientific manifest: SHA-256 `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA`.

| Protected object | SHA-256 | Status |
|---|---|---|
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | PASS; not called |
| `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | PASS |
| production bare-`a` `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | PASS; not used as corrected oracle |
| `lab_solve2.m` | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` | PASS; not called |
| accepted O1 `HANK3_FOC.m` | `B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315` | PASS; used by D1 |
| predecessor `decision_python.py` | `6054A0C59E7C0CD0C83AD1919C3CFAF7B2987D0545EE4CEB26B3345FF2D01ABC` | unchanged |
| predecessor `d2_matlab.m` | `8067196C2C680926490B6231EE2FF3125DD43B26AB812A1566719043E270C7C9` | unchanged, as required |
| predecessor `d2_python.py` | `DD9DDCB675BE7A5C3A672CF1936AB7CBA1553AC8334989B2CDAA777FB2914344` | unchanged |
| predecessor `compare.py` | `5C6FDBEBDA8BA67D819E69808A43C076E8F7BCB3C85788DABD942CC35EB40BE7` | unchanged |

No production source/helper/test/cache was modified.

## Exact predecessor blocker diagnosis

The blocked predecessor declared `rows=struct([])`, which is a zero-field struct array. It then attempted whole-struct assignment of the 18-field result produced by `row(...)`. MATLAB whole-struct assignment requires identical field schema/order, so `rows(k)=row(...)` failed with dissimilar-structure assignment before a valid D1 JSON could be produced.

The correction preallocates `s.case_count` homogeneous rows from an exact 18-field schema. Scientific calculations and the row-producing function are unchanged.

## Complete original-to-corrected harness diff

Every changed line is classified `RESULT_CONTAINER_OR_SERIALIZATION_ONLY`.

```diff
-function decision_matlab(stage)
+function decision_matlab_corrected(stage)
```

Classification: `RESULT_CONTAINER_OR_SERIALIZATION_ONLY`; external callable/file-name alignment only.

```diff
-... dummy=struct(); rows=struct([]); k=0;
+... dummy=struct(); rows=repmat(row_schema(),1,s.case_count); k=0;
```

Classification: `RESULT_CONTAINER_OR_SERIALIZATION_ONLY`; zero-field container replaced by exact-schema preallocation. Every scientific expression surrounding the container clause remains byte-identical.

```diff
+function r=row_schema()
+r=struct('case_id',0,'a',0,'b',0,'z',0,'v_b',0,'q',0,'c',0,'l',0,'labor_income',0,'d',0,'cost',0,'mu_a',0,'mu_b',0,'utility',0,'hamiltonian',0,'transfer_sign',0,'a_direction','Z','b_direction','Z');
+end
```

Classification for all three added lines: `RESULT_CONTAINER_OR_SERIALIZATION_ONLY`; they declare only the existing row field names/order and storage types and perform no scientific evaluation.

No other original line changed. The complete frozen diff is also recorded in external `harness_diff.md`.

## Frozen successor identities and synthetic preflight

| Artifact | SHA-256 |
|---|---|
| corrected `decision_matlab_corrected.m` | `5D94EDF89259D543758E490EA25C9359C1B65588CF7BB0557EEEDFA6B7FF3F9A` |
| `synthetic_struct_preflight.m` | `7B02E81C7C19C6F26A2CA26144BA4503800BFBDC6AFDD0DE79FBE08E472D78F0` |
| frozen successor ledger | `BA3A5FF1AA0A476C85AB0DF760EC844D4319F9269F6E53AB6E8339AA3FD339CC` |
| `harness_diff.md` | `E8B15BCD96EC788FF364F82AD5C0BF20E1D699D44E0D9A89EBF3BC498A630D4E` |
| `successor_freeze.json` | `2F4C8F86700FFB49A3044FF93025BE0A24618D6709E2AFBF2E3EE0B38109E32F` |
| final `execution_results.json` | `C6B038F72C331DAB661E164CCE4A0A61D35F6AC10C302CA511B2D734011459A9` |

The single engineering-only MATLAB preflight:

- invocation count: `1`;
- scientific/helper calls: `0`;
- exit status: `0`;
- rows serialized/read back: `2/2`;
- field schema: exact 18-field D1 row schema on both rows;
- JSON serialization/read-back: PASS;
- `synthetic_preflight.json` SHA-256: `30E02BA56E7C0103A6558C5AB9C69FCBCFBB5E26B86E7A50AC55B3C727DFAF69`.

## Exact call counts

Historical and successor counts are separated:

- historical consumed predecessor D1 MATLAB: `1`;
- successor replacement D1 MATLAB: `1`;
- successor D1 Python: `1`;
- successor D1 comparison: `1`;
- successor D2 MATLAB: `1`;
- successor D2 Python/comparison: `0/0`;
- successor D3 MATLAB/Python/comparison: `0/0/0`;
- scientific reruns: `0`.

No full HJB, generator, KFE, steady-state, P3/P4/R4, asset-tail or dynamic call occurred.

## D1 corrected 432-case result

Replacement D1 MATLAB exited zero. `d1_matlab.json` existed, independently parsed, contained exactly 432 rows in frozen order, and every row contained all required fields.

Artifact identities:

- `d1_matlab.json`: `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`;
- `d1_python.json`: `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`;
- `d1_compare.json`: `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`.

| Compared scalar | Maximum absolute difference | Worst-case index/state/input |
|---|---:|---|
| `c` | `0` | case 1: `a=0,b=0,z=.5,v_b=.75,q=-.2` |
| `l` | `0` | case 1: same |
| labor income | `0` | case 1: same |
| `d` | `0` | case 1: same |
| adjustment cost | `0` | case 1: same |
| `mu_a` | `0` | case 1: same |
| `mu_b` | `0` | case 1: same |
| utility | `0` | case 1: same |
| Hamiltonian | `0` | case 1: same |

Categorical mismatches: transfer sign `0`; `a` direction `0`; `b` direction `0`.

Low-`a` subset (`a<a_bar`): `216` cases; maximum absolute difference is `0` for every scalar field; failure count `0`. The predecessor O1 low-`a` gap is therefore closed under the accepted corrected evaluator for the entire frozen D1 map.

D1 terminal result: PASS, `432/432`, complete scientific mismatch list empty.

## D2 and D3 disposition

The unmodified frozen D2 MATLAB evaluator was invoked exactly once and failed at `d2_matlab.m:3` while evaluating `c=m.p2(k); id=c.id`. The heterogeneous ten-case JSON array does not decode into a homogeneous MATLAB struct array supporting the assumed `c.id` dot-indexing path. No `d2_matlab.json` was produced and no D2 scientific comparison exists.

- D2 valid completed rows: `0/10`.
- D2 controls/directions/multipliers/KKT/boundary differences: `NOT_AVAILABLE_BLOCKED_BEFORE_VALID_D2_OUTPUT`.
- D3 completed rows: `0/360`; gamma-2/phi-5 comparisons: `NOT_REACHED`.

Per explicit authority, `d2_matlab.m` was not proactively edited, not repaired after failure, and not rerun.

## Complete mismatch and failure lists

Scientific mismatch list: empty. D1 has no failures; D2/D3 have no valid comparisons from which to infer a scientific PASS or FAIL.

Source/environment/harness failure list contains exactly one entry:

| Stage | Location | Failure | Interpretation |
|---|---|---|---|
| D2 MATLAB | frozen `d2_matlab.m:3` | heterogeneous decoded P2 case container does not support assumed `c.id` dot indexing; nonzero MATLAB exit; no output persisted | external input-container traversal blocker; no scientific mismatch |

Synthetic preflight failures: none. Replacement D1 persistence failures: none.

## Forbidden-operation and Git check

- predecessor cases/order/parameters/equations/state/shadow inputs/O1 behavior/comparison fields/tolerances changed: no
- MATLAB/Python production source/tests/helpers/cache modified: no
- taper added or production bare-`a` FOC used as oracle: no
- `Tt`/`rb_gap` adapter added: no
- D2 edited: no
- failed successor scientific stage repaired/rerun: no
- full HJB/KFE/steady state or P3/P4/R4: `0`
- asset-tail, AR(1), transition, IRF, dynamics, calibration extension or Results: `0`
- P5 revoked/reissued: no

Git status at report freeze: the sole repository change was this authorized report; no unrelated tracked or untracked repository paths were present. Final remote identity and clean status require post-publication verification.

## Acceptance level and exact recommended next gate

Acceptance level: corrected D1 household-decision parity is fully established for all 432 cases, including the low-`a` subset. Overall D1→D3 supplementary gate remains incomplete because D2 MATLAB did not produce a valid container. P5 remains accepted; the dynamic hold continues.

Exact recommended next gate: the smallest D2 external heterogeneous-case-container correction and resumption task. It should authorize only:

1. correcting D2 MATLAB iteration/access for the already frozen heterogeneous ten-case manifest, without changing any D2 calculation;
2. one no-model synthetic heterogeneous-JSON/container preflight;
3. one explicitly authorized replacement D2 MATLAB call, because the D2 call here was consumed before valid persistence;
4. conditional D2 Python/comparison and then the unchanged D3 sequence.

The accepted D1 outputs and PASS must be reused without rerunning D1. No asset-tail or dynamic execution should begin until D2/D3 complete.
