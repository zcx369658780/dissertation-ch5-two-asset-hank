# Chapter 5 Two-Asset HANK Post-P5 D2 Result-Container Preallocation/Serialization Correction and Resumption Report

## Terminal classification

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

Execution stopped in Phase A, before creation or invocation of the mandatory no-model preflight. The frozen accepted-input-corrected D2 evaluator does not contain the task-presumed exact 17-field result row. Its normal scientific row has exactly 16 fields, while the frozen lower-`b` F/Z near-tie row has a distinct 10-field schema. Inventing a seventeenth field would change the frozen output definition; preallocating only the observed normal schema would still reject the near-tie row; and a union-schema normalization would no longer be the task-required exact 17-field schema. No authorized unambiguous correction could therefore be frozen.

This is a result-schema authority/source contradiction, not a scientific mismatch. P5 remains Owner-accepted and the voluntary dynamic hold continues.

## Live authority and continuity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Isolated worktree: `D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-repo-20260829`.
- Branch: `codex/ch5-adjustment-boundary-redesign`.
- Live start `origin/main` after one fresh fetch: `ae3b76b84995f13fc64adf665fdc6598b4aef7b8`.
- Live task: `tasks/CH5_TWO_ASSET_HANK_POST_P5_D2_RESULT_CONTAINER_PREALLOCATION_SERIALIZATION_CORRECTION_AND_RESUMPTION.md`.
- P5 marker verified: `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`.
- Hold verified: `DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`.
- Accepted Python baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`: empty.

## Artifact roots

- Original household-decision root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-artifacts-20260829-220000`.
- Accepted D1/resumption root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-resumption-artifacts-20260829-223000`.
- Accepted D2 input-container successor root: `D:\ProjectTemp\ch5-post-p5-d2-container-resumption-artifacts-20260830-001000`.
- Fresh no-overwrite current root: `D:\ProjectTemp\ch5-post-p5-d2-result-container-resumption-artifacts-20260830-054500`.

The current root contains only identity-preserving copies of the frozen manifest and unchanged D2 Python/comparison/D3 harnesses. No corrected MATLAB harness, preflight, ledger, diff, freeze, or output was created because the schema contradiction was terminal before freeze.

## Protected identities

| Object | SHA-256 | Result |
|---|---|---|
| frozen scientific `manifest.json` | `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA` | PASS |
| accepted input-corrected `d2_matlab_corrected.m` | `57FFAD7DA9DCBA043EC40B21C647AD8621E1D973C9670A7C73EF0E2E5F6F868E` | PASS |
| D2 Python | `DD9DDCB675BE7A5C3A672CF1936AB7CBA1553AC8334989B2CDAA777FB2914344` | PASS; not run |
| comparison harness | `5C6FDBEBDA8BA67D819E69808A43C076E8F7BCB3C85788DABD942CC35EB40BE7` | PASS; not run |
| corrected D1/D3 MATLAB evaluator | `5D94EDF89259D543758E490EA25C9359C1B65588CF7BB0557EEEDFA6B7FF3F9A` | PASS; not run |
| D3 Python evaluator | `6054A0C59E7C0CD0C83AD1919C3CFAF7B2987D0545EE4CEB26B3345FF2D01ABC` | PASS; not run |
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | PASS; not called |
| `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` | PASS; not called |
| production `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` | PASS; not called |
| `lab_solve2.m` | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` | PASS; not called |
| accepted O1 helper | `B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315` | PASS; not called |

No production source, helper, test, or cache was modified.

## D1 evidence reuse and zero-call confirmation

Accepted D1 artifacts were rehashed successfully:

- MATLAB: `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`;
- Python: `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`;
- comparison: `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`.

The accepted result remains `432/432 PASS`, including `216/216` low-`a` PASS, all scalar maximum absolute differences `0`, and transfer-sign/`a`-direction/`b`-direction mismatch counts `0/0/0`.

D1 calls in this successor: MATLAB/Python/comparison `0/0/0`.

## Accepted D2 input traversal reuse

The accepted `get_case` implementation and its `iscell(container)` / `container{k}` path were read and left byte-identical. The accepted facts remain: decoded `m.p2` is a `10x1 cell`; all ten IDs were previously traversed in frozen order; skipped/duplicated/reordered/merged counts were `0/0/0/0`. No input traversal was reopened or rerun.

## Exact observed D2 output schemas and blocker

The normal row assignment in the frozen evaluator has exactly these 16 field keys, in order:

`id, c, l, d, cost, mu_a, mu_b, utility, hamiltonian, a_direction, b_direction, lambda_a, lambda_b, kkt_max, boundary_feasible, boundary_violation`

The lower-`b` F/Z near-tie row has exactly these 10 field keys, in order:

`id, canonical, raw, alias_available, gap, bound, boundary_feasible, kkt_max, mu_a, mu_b`

The literal strings `FZ` and `FF` are values of `canonical` and `raw`, not field names.

Consequences:

1. the task-required exact 17-field schema is not present in the accepted evaluator;
2. a 16-field homogeneous preallocation permits normal-row assignment but cannot accept the distinct near-tie row;
3. a 21-field union schema would add absent fields/default values to each row and is not the task-required exact 17-field schema;
4. inventing a seventeenth key, deleting near-tie outputs, or changing expected Python/output definitions is forbidden;
5. therefore no complete accepted-input-corrected-to-result-corrected diff can be classified without first resolving the schema authority contradiction.

No changed harness line exists, so the allowed classification counts are all zero:

- `RESULT_CONTAINER_SCHEMA_ONLY`: `0`;
- `RESULT_PREALLOCATION_ONLY`: `0`;
- `RESULT_SERIALIZATION_ONLY`: `0`;
- `EXTERNAL_CALLABLE_ALIGNMENT_ONLY`: `0`.

## Freeze and no-model preflight disposition

- corrected D2 MATLAB harness: not created;
- result-container preflight: not created;
- successor execution ledger: not created;
- complete harness diff: not created;
- preflight invocation count: `0`;
- MATLAB process count at terminal diagnosis: `0`;
- Python process count at terminal diagnosis: `0`.

The mandatory preflight was prohibited once its required exact schema could not be derived without invention.

## Historical and successor call counts

- historical original D1 MATLAB blocked call: `1`;
- historical accepted D1 replacement MATLAB/Python/comparison: `1/1/1`, reused only;
- historical original D2 MATLAB input-container blocked call: `1`;
- historical replacement D2 MATLAB output-container blocked call: `1`;
- current newly authorized replacement D2 MATLAB: `0`;
- current D2 Python/comparison: `0/0`;
- current D3 MATLAB/Python/comparison: `0/0/0`;
- current engineering-only MATLAB preflight: `0`.

## D2/D3 numerical disposition

D2 and D3 were not reached. No valid new MATLAB output, Python output, or comparison exists.

- D2 ten-case per-field maximum absolute differences/worst cases: `NOT_REACHED_SCHEMA_AUTHORITY_BLOCKER`;
- D2 direction/multiplier/KKT/boundary mismatch counts: `NOT_REACHED`;
- D3 360-case gamma-2/phi-5 per-field differences/worst cases: `NOT_REACHED`;
- D3 labor/transfer maxima: `NOT_REACHED`.

Scientific mismatch list: empty. No scientific evaluation or valid comparison occurred.

Source/environment failure list contains exactly one entry:

| Stage | Failure | Interpretation |
|---|---|---|
| Phase A result-schema diagnosis | task requires an exact 17-field D2 row, but frozen evaluator defines one 16-field normal row schema and one distinct 10-field near-tie schema | schema authority/source contradiction; no unambiguous plumbing-only correction can be frozen |

## Forbidden-operation check

- D1 rerun: no (`0/0/0`);
- D2/D3 cases/order/equations/parameters/state/shadow/derivative inputs/tolerances changed: no;
- accepted `get_case` traversal changed: no;
- production MATLAB/Python source/tests/helpers/cache modified: no;
- taper, production bare-`a` oracle, `Tt`/`rb_gap` adapter, or Python-result hard-coding added: no;
- preflight or scientific MATLAB/Python/comparison calls: `0`;
- failed scientific stage repaired/rerun: no;
- full HJB/KFE/steady state or P3/P4/R4: `0`;
- asset-tail, AR(1), transition, IRF, dynamics, calibration extension, or Results: `0`;
- P5 revoked/reissued: no.

## Git status and acceptance level

At report freeze, the sole repository change is this required report. `src/tests` remain unchanged from the accepted baseline and no unrelated tracked or untracked repository paths are present. Final remote identity and clean status require post-publication verification.

Acceptance level: D1 remains fully accepted; accepted D2 input traversal remains qualified; D2 result-container correction, preflight, replacement call, D2 comparison, and D3 remain unentered. P5 remains accepted and the dynamic hold continues.

## Exact recommended next gate

Publish only the smallest D2 result-schema authority correction task. It must explicitly reconcile the frozen 16-field normal row and 10-field near-tie row and choose one permitted serialization contract—such as an exact union schema with specified default/null semantics or an explicitly authorized heterogeneous serialization representation—before authorizing a new preflight or replacement D2 MATLAB call. It must state the exact field list and count rather than preserving the unsupported 17-field premise. D1 must remain reuse-only with zero calls.
