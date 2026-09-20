# Chapter 5 corrected Option-B checkpoint-0 repair and run002 report

Date: 2026-09-20

## Terminal verdict

`FAIL__UNEXPECTED_TASK_EXCEPTION__NO_SCIENTIFIC_RETRY`

The authorized checkpoint-0 diagnostics repair passed its zero-science gate. The one authorized fresh run002 then reached Beijing (`province_index=0`), converged its HJB at checkpoint 12, and stopped at the first terminal-KFE engineering exception. No second scientific run was attempted.

The exact exception was `TypeError: Object of type csr_matrix is not JSON serializable`. The accepted topology helper completed one exact-positive SCC decomposition and returned a dictionary containing sparse `adjacency` and NumPy `labels`. The unchanged terminal-KFE caller then attempted to serialize that raw dictionary as JSON. The write failed before any topology receipt, GESVD, stationary mass, aggregate, or integration object was persisted.

## Authority, branch, and code freeze

- Fresh live-main baseline: `67584b84d02823b56089a7eaa10e47ccaf811e5a`.
- Execution-freeze commit: `57819c23342ec1e7c488ab924234f02759091e3f`.
- Task branch: `codex/ch5-mp4c-optionb-checkpoint0-repair-run002-20260920`.
- The pre-execution and post-execution scientific-code hash maps match exactly.
- The only execution-freeze changes were the authorized driver and focused regression test.
- `nonlinear_continuation.py`, the selector, D1/D2/D3, KKT, boundary, solver, Delta, tolerances, calibration, and scientific equations were not modified.
- The accepted run001 evidence remained read-only. Its sealed manifest stayed `F447D5DF30D302963D81EB09E68BEC72C1B89F8C1DE227936533045F9A16F315`.

## Zero-science checkpoint-0 repair gate

Checkpoint 0 now emits current-only policy and operator diagnostics. It records current canonical policy identity, selected-field hashes, active constraints, transfer branches, switching summaries, selector/root counts, current Q CSR identity, Q nonzeros, D2 receipt, and same-value B. Every comparison-only field to a nonexistent predecessor is explicitly `null`.

Checkpoint 1 and later still route through the unchanged comparative policy/operator helpers. A partial predecessor tuple fails closed.

Pre-science verification passed:

- Focused regression suite: `43 passed`, failures `0`, errors `0`.
- `py_compile`: PASS.
- `git diff --check`: PASS.
- Authority blobs, baseline ancestry, 31-row order, predecessor lineage, exact changed paths, and code freeze: PASS.
- Scientific calls during this gate: `0`.

The run002 checkpoint-0 receipt confirms:

- diagnostic mode: `CURRENT_ONLY__NO_PREVIOUS_CHECKPOINT`;
- policy identity: `E09671771A95DFAF5EF8D7AFC9F980DB72125AEBF9D2B1297FC3FA2BBBD1B7FA`;
- Q nonzeros: `3118`;
- D2: PASS;
- `B0=0.3384513972950506`;
- previous-policy and previous-Q comparisons: unavailable (`null`).

## Run002 reached result

Only Beijing was reached. The other 30 provinces were not started because the first terminal exception stops the full task.

### Beijing initialization and HJB

- Source-native initialization: `1`.
- Labor roots: `800/800` attempted/returned.
- Initial value SHA-256: `92C09D3DB6976DE2093795AB2BEF1DF7164AB7F1F71136E30FF23B88275BDD56`.
- Policy maps and D2/Q assemblies: `13/13`; every reached D2 receipt passed.
- Direct HJB updates: `12`.
- Direct solver: `scipy.sparse.linalg.spsolve` only.
- Maximum normwise backward error across 12 solves: `3.0832786979441453e-16`, below `1e-12`.
- Final checkpoint: `12`.
- `B12=1.292732587643286e-11`.
- `D12=1.2743897048750341e-08`, using `||vec_F(V12-V11)||_inf`.
- Primary convergence: PASS.
- Final value SHA-256: `48396D52F13045B4F3370CA892C9989813BBEA8F0D45A577DD8C6D6EDE5ADA93`.
- Final Q artifact SHA-256: `E1F55D0B755CB83D4F6A3CB4FEFD6DBC8CD4F05C6D23FC5DE00302E16B74BF20`.

At checkpoint 12, the policy identity did not change from checkpoint 11. Transfer branches were negative `320`, positive `291`, and zero-kink `189`. Active constraints were lower-b `20`, none `752`, upper-a `8`, upper-a plus upper-b `1`, and upper-b `19`. The Q had `3116` nonzeros, retained the preceding sparsity pattern, and had operator difference infinity norm `9.270040234800325e-05`. Selected switching policies were liquid-Z `0`, interior-a `35`, and joint `0`.

### Exact first KFE failure

The terminal directory was created. The caller incremented its local topology gate and called `analyze_exact_positive_topology(Q12)`. That helper built the exact-positive graph and called `scipy.sparse.csgraph.connected_components(..., connection="strong")` exactly once before returning. Serialization of the returned raw topology object then failed because its `adjacency` field is a CSR matrix.

Consequently:

- actual SCC decompositions: `1`;
- persisted global-ledger SCC count: `0`, an exception-path undercount because the province-local ledger is accumulated only after `_terminal_kfe` returns;
- persisted topology classification, closed-class count, and SCC sizes: unavailable;
- dense GESVD: `0`;
- normalized stationary candidates: `0`;
- `Q.T@p`: `0`;
- corrected household aggregates: `0`;
- household PASS count: `0/31` because Beijing did not complete KFE.

No second SCC was run to reconstruct the unavailable topology result. The original `scientific_ledger.json` and `terminal_receipt.json` remain unchanged; `post_terminal_zero_science_diagnostic_receipt.json` records the accounting reconciliation.

## Integration status

The 31-household prerequisite was not met. `PreFrozenHouseholdOutputBatch`, source-faithful labor reconstruction, K1A, C1, firm evaluation, and `raw_ra0_turn1 @ S_destination_origin` were not reached. Their values and identities are unavailable.

## Exact run002 scientific accounting

| Object | Actual count |
|---|---:|
| Source-native initializations | 1 |
| Labor roots attempted / returned | 800 / 800 |
| Corrected policy maps / D2 assemblies | 13 / 13 |
| Selector evaluations | 10,400 |
| Scalar selector roots | 4,148 |
| Interior-Z / interior-a / joint roots | 760 / 17 / 1 |
| Direct HJB updates / checkpoint evaluations | 12 / 12 |
| SCC decompositions | 1 |
| Dense GESVD / normalized mass / `Q.T@p` | 0 / 0 / 0 |
| Aggregate evaluations / household batches | 0 / 0 |
| Labor / K1A / C1 / firm evaluations | 0 / 0 / 0 / 0 |
| Wage / monetary / fiscal / raw-next-payoff | 0 / 0 / 0 / 0 |
| Scientific retries / solver substitutions | 0 / 0 |
| Turn-2 household / second outer turn | 0 / 0 |
| K1B / K2 / adaptive controller | 0 / 0 / 0 |
| MATLAB / GE-annual-shock-IRF-welfare-Results | 0 / 0 |
| Payoff transformations or repair | 0 |

The sealed original global ledger reports SCC `0`; that persisted count is retained for provenance and reconciled to actual SCC `1` by the post-terminal zero-science diagnostic receipt.

## Predecessor run001 historical consumption

Run001 remains separate historical consumption: one initialization, `800/800` labor roots, one policy map, `800` selector evaluations, `483` scalar selector roots including `206` interior-Z roots, one D2/Q assembly, zero HJB updates, and zero SCC/GESVD/aggregate/integration calls. Its scientific retries were `0`.

## Evidence and boundaries

- Evidence root: `reports/ch5_mp4c_corrected_optionb_initial_turn_31_province_household_kfe_k1a_c1_one_turn_integration_20260920_run002`.
- Final sealed-manifest SHA-256: `D01A8A0CDF6808824735FEACABD7572249970DE97606A63BEA86209B5B6F531A`.
- Manifest entries / bytes: `139` / `1,949,298`.
- Independent readback: PASS; bad paths `0`.
- Turn 2 was not run.
- CURRENT files were not modified.
- No successor was published.
- Main was not merged.
