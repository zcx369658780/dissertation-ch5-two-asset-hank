# Chapter 5 Two-Asset HANK Post-P5 D2 Heterogeneous Result-Schema Authority and Resumption Report

## Terminal classification

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The mandatory static schema audit confirmed the frozen 9-normal/1-near-tie heterogeneous row schemas, but exposed a comparator-authority contradiction before any corrected harness, artifact root, or preflight was created. The frozen comparator can already consume heterogeneous JSON rows, yet it does not compare the near-tie numerical fields `gap` and `bound` required by the live task. The task permits comparator changes only when necessary to consume heterogeneous JSON and simultaneously forbids changing the comparison field set. Adding the missing comparisons is therefore not authorized. Execution stopped fail-closed before Phase A.

This is a source/comparator contract blocker, not a scientific mismatch. P5 remains Owner-accepted and the voluntary dynamic hold continues.

## Live authority and source continuity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Isolated worktree: `D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-repo-20260829`.
- Branch: `codex/ch5-adjustment-boundary-redesign`.
- Live start `origin/main` after one fresh fetch: `a0ebd17f1af56b65379eff8e12dfe8dc03f1ead6`.
- Live task: `tasks/CH5_TWO_ASSET_HANK_POST_P5_D2_HETEROGENEOUS_RESULT_SCHEMA_AUTHORITY_AND_RESUMPTION.md`.
- P5 marker verified: `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`.
- Hold verified: `DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`.
- Accepted Python baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`: empty.

All controlling predecessor tasks/reports required by the live task were present and read after fast-forwarding to live main.

## Artifact roots and protected identities

- Original household-decision root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-artifacts-20260829-220000`.
- Accepted D1/resumption root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-resumption-artifacts-20260829-223000`.
- Accepted D2 input-container successor root: `D:\ProjectTemp\ch5-post-p5-d2-container-resumption-artifacts-20260830-001000`.
- Prior schema-authority blocked root: `D:\ProjectTemp\ch5-post-p5-d2-result-container-resumption-artifacts-20260830-054500`.
- Current successor artifact root: not created because the mandatory static audit was terminal before Phase A.

| Object | SHA-256 | Status |
|---|---|---|
| frozen scientific `manifest.json` | `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA` | PASS |
| accepted input-corrected D2 MATLAB harness | `57FFAD7DA9DCBA043EC40B21C647AD8621E1D973C9670A7C73EF0E2E5F6F868E` | PASS; not run |
| frozen D2 Python harness | `DD9DDCB675BE7A5C3A672CF1936AB7CBA1553AC8334989B2CDAA777FB2914344` | PASS; not run |
| frozen comparator | `5C6FDBEBDA8BA67D819E69808A43C076E8F7BCB3C85788DABD942CC35EB40BE7` | PASS; not run |
| corrected D1/D3 MATLAB evaluator | `5D94EDF89259D543758E490EA25C9359C1B65588CF7BB0557EEEDFA6B7FF3F9A` | PASS; not run |
| D3 Python evaluator | `6054A0C59E7C0CD0C83AD1919C3CFAF7B2987D0545EE4CEB26B3345FF2D01ABC` | PASS; not run |

No MATLAB/Python production source, helper, test, or cache was modified.

## D1 reuse and zero-call confirmation

The accepted D1 artifacts were rehashed successfully:

- MATLAB: `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`;
- Python: `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`;
- comparison: `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`.

Accepted D1 remains `432/432 PASS`, including `216/216` low-`a` PASS, all scalar maximum absolute differences `0`, and all sign/direction mismatch counts `0`.

D1 MATLAB/Python/comparison calls in this task: `0/0/0`.

## Complete static D2 schema audit

### Manifest cases

The frozen manifest contains exactly ten D2 cases in this order:

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

Counts: normal rows `9`; near-tie rows `1`. IDs are unique and the exact near-tie ID is `lower_b_fz_near_tie`.

### MATLAB schemas

The accepted input-corrected MATLAB evaluator creates the following normal-row schema with exactly 16 fields:

`id, c, l, d, cost, mu_a, mu_b, utility, hamiltonian, a_direction, b_direction, lambda_a, lambda_b, kkt_max, boundary_feasible, boundary_violation`

Its `lower_b_fz_near_tie` branch creates exactly the following 10 fields:

`id, canonical, raw, alias_available, gap, bound, boundary_feasible, kkt_max, mu_a, mu_b`

The accepted `get_case` input traversal remains `iscell(container)` with `container{k}` and was not modified.

### Python schemas

The frozen Python `record(...)` path returns exactly the same 16-field normal schema. It is used by the first nine frozen cases. The final `else` canonicalization path appends exactly the same 10-field near-tie schema for `lower_b_fz_near_tie`.

Python therefore confirms `9 x 16-field` plus `1 x 10-field`, with no seventeenth field, union schema, or fabricated placeholder.

### Comparator behavior

The frozen comparator successfully loads `stage+'_matlab.json'` and `stage+'_python.json'`, asserts equal row counts, and iterates the two ordered `rows` arrays with `zip`.

For D2 it:

- compares normal numerical fields `c,l,d,cost,mu_a,mu_b,utility,hamiltonian,lambda_a,lambda_b,kkt_max,boundary_violation` only when the field exists on both rows;
- compares `a_direction,b_direction,boundary_feasible` only when present on both rows;
- separately compares near-tie `canonical,raw,alias_available` when present on both rows;
- consequently already consumes heterogeneous top-level row objects without a schema-dispatch or JSON parsing change;
- also compares near-tie `mu_a`, `mu_b`, `kkt_max`, and `boundary_feasible` through the shared presence-gated loops;
- does not compare near-tie `gap` or `bound` at all.

Thus the frozen comparator implements partial field-presence dispatch, not the complete near-tie comparison required by the new authority.

## Frozen serialization authority and exact blocker

The static source confirms that `D2_HETEROGENEOUS_JSON_ARRAY_PRESERVE_NATIVE_CASE_SCHEMA` is the correct serialization model. A MATLAB cell array of nine existing 16-field scalar structs plus one existing 10-field scalar struct could preserve the native schemas without changing science.

However, the live task requires `gap` and `bound` to be compared for the near-tie case and says to stop if frozen Python/comparator source contradicts that interpretation. It permits comparator correction only if the existing comparator cannot consume heterogeneous JSON. That condition is false: the comparator already consumes it. Adding `gap` and `bound` would also alter the comparison field set, which the same task explicitly forbids.

Therefore no authorized comparator diff exists, and advancing to a MATLAB plumbing correction/preflight would create scientific output without an authorized complete comparison gate.

## Harness, preflight, and call disposition

- corrected heterogeneous MATLAB harness: not created;
- MATLAB harness diff/classifications: none;
- execution ledger: not created;
- heterogeneous-result MATLAB preflight: `0` calls, not created;
- comparator schema-dispatch preflight: `0` calls, not authorized or needed for parsing;
- replacement D2 MATLAB: `0`;
- D2 Python/comparison: `0/0`;
- D3 MATLAB/Python/comparison: `0/0/0`.

Historical D2 scientific calls remain separately recorded:

1. input-container blocked MATLAB call: `1`;
2. zero-field output-container blocked replacement MATLAB call: `1`;
3. prior result-schema-authority task MATLAB scientific calls: `0`;
4. current replacement MATLAB scientific calls: `0`.

## Numerical and mismatch disposition

- D2 normal-case maximum differences/worst cases: `NOT_REACHED_STATIC_COMPARATOR_AUTHORITY_BLOCKER`;
- D2 near-tie comparison: `NOT_REACHED`;
- D2 KKT/boundary mismatch counts: `NOT_REACHED`;
- D3 360-case maximum differences/worst cases: `NOT_REACHED`.

Scientific mismatch list: empty. No new scientific evaluator or comparison ran.

Source/environment failure list contains exactly one entry:

| Stage | Failure | Interpretation |
|---|---|---|
| mandatory static schema audit | frozen comparator can consume heterogeneous rows but omits required near-tie `gap` and `bound`; current task does not authorize adding comparison fields when parsing already works | comparator authority contradiction before Phase A |

## Forbidden-operation check

- D1 rerun: no (`0/0/0`);
- D2/D3 cases/order/equations/parameters/state/shadow/derivative inputs/tolerances changed: no;
- native 16/10-field schemas changed or normalized: no;
- seventeenth field or 21-field union created: no;
- missing fields fabricated: no;
- comparator changed: no;
- production MATLAB/Python source/tests/helpers/cache modified: no;
- taper, production bare-`a` oracle, `Tt`/`rb_gap` adapter, hard-coded Python answers, or widened tolerance added: no;
- preflight/scientific MATLAB/Python/comparison calls: `0`;
- full HJB/KFE/steady state, P3/P4/R4, asset-tail, AR(1), transition, IRF, dynamics, calibration extension, or Results: `0`;
- P5 revoked/reissued: no.

## Git status, acceptance level, and next gate

At report freeze, the sole repository change is this required report. `src/tests` remain unchanged from the accepted baseline and no unrelated tracked or untracked repository paths are present. Final remote identity and clean status require post-publication verification.

Acceptance level: the 9+1 heterogeneous schema authority is statically confirmed, but no serialization harness, preflight, D2 replacement, D2 comparison, or D3 execution was entered. D1 remains accepted; P5 remains accepted; the dynamic hold continues.

Exact recommended next gate: publish only a comparator-field-authority correction task that explicitly authorizes adding near-tie `gap` and `bound` to the frozen D2 comparison set, while preserving the existing tolerance, expected values, order, PASS/FAIL rule, and all other comparison fields. It may then reauthorize the same cell-array serialization plumbing, one no-model heterogeneous-result preflight, and one replacement D2 MATLAB call. D1 must remain reuse-only with zero calls.
