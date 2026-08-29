# Chapter 5 Two-Asset HANK Post-P5 Shared-Input Household Decision-Map Parity Report

## Terminal classification

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The first and only authorized scientific call, D1 MATLAB, failed after start in the external result-container assignment at `decision_matlab.m:9`. No valid D1 output was persisted. The task's fail-closed/no-rerun rule stopped execution before D1 Python, D1 comparison, D2, or D3.

This is an external harness blocker, not a household-decision mismatch. P5 remains Owner-accepted and is neither revoked nor reissued. The voluntary dynamic hold remains active.

## Live authority and continuity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Live start `origin/main` after fresh fetch: `f8b79e9da5f6edaad70a15799502209d13dba572`
- Live `origin/main` at report freeze, before report-only publication: `f8b79e9da5f6edaad70a15799502209d13dba572`
- Owner P5 marker verified: `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`.
- Active voluntary hold verified: `DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`.
- Accepted Python baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`: empty before execution and at report freeze.

## Frozen scientific authority and protected identities

- Illiquid law: `mu_a = r_a*a + d`.
- Adjustment scale: `m(a)=max(a,a_bar)`.
- No MATLAB `raah/Rah` taper was used.
- D1/D3 MATLAB path was frozen to the accepted O1 helper, not production bare-`a` `HANK3_FOC`.

| Protected object | SHA-256 | Result |
|---|---|---|
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | PASS; not called |
| `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | PASS |
| production `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | PASS; not used as corrected oracle |
| `lab_solve2.m` | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` | PASS; not called |
| accepted O1 `HANK3_FOC.m` | `B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315` | PASS; selected by D1 harness |
| accepted predecessor P1 manifest | `3D2A35A7118CFEE479C05C1339AB247D78F5A71BBA044779AAB678D59E72D449` | PASS |

No protected source/helper/test/cache file was modified.

## External artifact root and freeze

Fresh no-overwrite artifact root:

`D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-artifacts-20260829-220000`

All 432 D1 cases, ten D2 cases, 360 D3 cases, parameters, tolerances, run order and budgets were frozen before the first scientific call. Python files passed static compilation; manifest/source JSON read-back passed. A static scan of `d2_matlab.m` found no Python-output import or embedded expected-result values.

| Frozen artifact | SHA-256 |
|---|---|
| `manifest.json` | `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA` |
| `source_identity.json` | `BB566ADE93412B06E4E172812E597B1449A3D787F7ED117F08494921EB25F558` |
| `decision_matlab.m` | `C758F97CB4AF7F372595D4425064E6DDF1B8BE230C42CB1264CFF34066E94202` |
| `decision_python.py` | `6054A0C59E7C0CD0C83AD1919C3CFAF7B2987D0545EE4CEB26B3345FF2D01ABC` |
| `d2_matlab.m` | `8067196C2C680926490B6231EE2FF3125DD43B26AB812A1566719043E270C7C9` |
| `d2_python.py` | `DD9DDCB675BE7A5C3A672CF1936AB7CBA1553AC8334989B2CDAA777FB2914344` |
| `compare.py` | `5C6FDBEBDA8BA67D819E69808A43C076E8F7BCB3C85788DABD942CC35EB40BE7` |
| `execution_ledger.json` | `88DAC099829318A85691040588AEB17150ED2356AE95C968835D7B954E13D703` |

Harnesses and cases were not modified after scientific execution began.

## Exact execution ledger

| Ordered step | Calls | Entered/completed cases | Status |
|---|---:|---:|---|
| D1 MATLAB | `1` | entered loop / valid persisted rows `0` | FAILED_POST_START at external struct aggregation |
| D1 Python | `0` | `0/432` | NOT_REACHED |
| D1 comparison | `0` | `0/432` | NOT_REACHED |
| D2 MATLAB | `0` | `0/10` | NOT_REACHED |
| D2 Python | `0` | `0/10` | NOT_REACHED |
| D2 comparison | `0` | `0/10` | NOT_REACHED |
| D3 MATLAB | `0` | `0/360` | NOT_REACHED |
| D3 Python | `0` | `0/360` | NOT_REACHED |
| D3 comparison | `0` | `0/360` | NOT_REACHED |

- MATLAB scientific harness calls: `1`.
- Python scientific harness calls: `0`.
- comparison calls: `0`.
- reruns: `0`.
- full HJB/KFE/steady-state calls: `0`.

## Blocker and complete failure list

Complete failure list contains one entry:

| Stage | Location | Failure | Scientific interpretation |
|---|---|---|---|
| D1 MATLAB | external `decision_matlab.m:9`, `rows(k)=row(...)` | MATLAB reported subscripted assignment between dissimilar structures; process exited nonzero; `d1_matlab.json` was not created | harness result-container blocker only; no cross-language comparison and no material mismatch observed |

The external harness failed before a complete output could be durably persisted. Under the explicit no-rerun rule, the harness was not repaired and D1 was not repeated.

## Required D1/D2/D3 diagnostics disposition

Because no valid D1 pair exists, maximum absolute differences, worst cases and categorical mismatches for all requested scalar fields are `NOT_AVAILABLE_BLOCKED_BEFORE_COMPARISON`.

- D1 completed cases: `0/432`; low-`a` subset statistics: `NOT_AVAILABLE_BLOCKED_BEFORE_COMPARISON`.
- D2 completed cases: `0/10`; KKT maxima and boundary-feasibility mismatch count: `NOT_AVAILABLE_NOT_REACHED`.
- D3 completed cases: `0/360`; gamma-2/phi-5 labor and transfer maxima: `NOT_AVAILABLE_NOT_REACHED`.
- Scientific failure/mismatch list: empty; the sole failure is the external harness entry above.

No PASS or FAIL is inferred for D1, D2, or D3 from absent evidence.

## Forbidden-operation and repository check

- production MATLAB/Python source/tests modified: no
- MATLAB taper added to Python: no
- production bare-`a` FOC used as corrected oracle: no
- `Tt`/`rb_gap` adapter added: no
- tolerance widened or cases tuned: no
- failed stage rerun: no
- full `HANK_2ASSETS_HJB`: `0`
- Python HJB/KFE/steady state: `0`
- P3/P4/R4 rerun: `0`
- upper-`a` tail, AR(1), transition, IRF, dynamics, calibration extension or Results entered: no
- P5 revoked/reissued: no

Git status at report freeze: the sole repository change was this authorized report; no unrelated tracked or untracked repository paths were present. Final clean status and remote identity require post-publication verification.

## Acceptance level and exact recommended next gate

Acceptance level: post-P5 household-decision parity experiment is incomplete due solely to an external D1 MATLAB result-container blocker. P5 remains accepted, but `DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY` continues.

Exact recommended next gate: publish the smallest external-harness correction-and-resumption task authorizing only:

1. correction of `decision_matlab.m` result-struct preallocation/assignment;
2. a no-model synthetic struct serialization preflight;
3. freeze/hash of the corrected harness while preserving the already frozen 432/10/360 scientific cases, equations and tolerances;
4. exactly one replacement D1 MATLAB call, followed—only after valid persistence—by the remaining original D1→D2→D3 sequence and budgets.

That successor must explicitly authorize the replacement D1 MATLAB call consumed here. It must not authorize scientific-case changes, tuning, P5 revocation, asset-tail testing, or dynamics.
