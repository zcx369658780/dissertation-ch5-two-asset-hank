# Turn6 same-frozen-input repeat runner: zero-science preparation

Task `CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_RUNNER_ZERO_SCIENCE_20260923`. Dispatch `b0bd3eb981a0c8848666d4ebae86d045875dddd1`, parent `1376297341548d569351b566e1507bdc37b6ef33`, frozen `src` tree `00682b2e1a7ba23665f6e16f6acf48ad35874883`. This candidate prepares a future one-shot replay. **Execution is not authorized here.** Household/HJB/KFE/integration/firm/K1B/model calls are all zero; turn7 household remains unrun; Results eligibility is `FALSE`.

## Exact replay object and static binding

The one future scientific object would be a new turn6 evaluation from the already sealed C5 entering-turn6 JSON and NPZ. The existing completed C6, represented by the sealed entering-turn7 JSON and NPZ, is the reference. A new isolated output root is planned at `reports/ch5_turn6_same_frozen_input_repeat_20260923_run001`; it does not exist at preparation time. No old two-turn `execute()` path is invoked.

| File | SHA-256 |
|---|---|
| `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/turn6_k1b_input_candidate.json` | `87BEB944AD35C16BAF62D35FE8DDAD3BDEBC9000DCB6CC9F7D6949A039F4B1BC` |
| `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/turn6_k1b_frozen_share_payoff_plan.npz` | `95880D37D5BBB10B95FF776E32B8B786447B20C1770117044C7735D91292ED34` |
| `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/turn7_k1b_input_candidate.json` | `D84E9D74C7E965A3B492F2F0F9A63D3320D436DD4A6D78E1E655F014C05FC059` |
| `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/turn7_k1b_frozen_share_payoff_plan.npz` | `37A1258F8EC87116F03084D8178C77424FDD5F3859A1BC73D9704940A3B9381E` |

Frozen distance: `docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv` SHA-256 `51A04FCAA1FA519B142BE2A155640F77E8746493AFDF4865ED243B96526E550D`. Old accepted runner SHA-256 `92018027502FFA5281F9BFAC91EE70D2BED17876B65100B3321819B2C0C59DB6`. Production `src` tree `00682b2e1a7ba23665f6e16f6acf48ad35874883`. Read-only helper hashes and exact bytes are recorded in the receipt. The new runner SHA-256 is `F0FF59BA8A088B8D74BEB396FBDE7D336D5DB28AC796A6E6BECEBC6FC048F405`; focused test SHA-256 is `C0DE8DF566E24930EBA6B6759FB77569ECDF4C54902E0C3FC15C9F0838ADFC85`. Static preflight checks 31 source-defined province labels/order, 31x31 destination-by-origin `S`, finite float64 arrays, nonnegative share columns, row/state/NPZ bit identities, raw `ra0_turn5`, entering `rah_turn6`, both sealed input/reference file hashes, distance, helper hashes, and absence of the planned output root.

Default CLI mode runs only this static preflight. An actual replay requires `--execute --execution-id`, a distinct future `TASK_CURRENT.md` with exact `Task ID: CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_EXECUTION_20260923`, active one-shot status and matching execution ID, plus a committed unchanged runner. The preparation task cannot satisfy that gate. Python, NumPy, SciPy, NumPy BLAS configuration, platform and thread environment are captured by preflight before any future model import/call. The future run would rehash all tracked production `src` files, helper runners, the current task, and sealed inputs after its one evaluation before drawing a reproducibility conclusion.

## Future entry guards and first failure

Every province is reserved against the full 800 labor roots, 51 maps, 40,800 selector evaluations, 20 million selector roots, 50 direct updates, 2,650 alpha arithmetic candidates and one terminal KFE envelope before entry. The frozen production selector `SelectorBudget` enforces its per-selector and root counts before each nested call; the source-native labor callback counts each attempted root before its scalar solve. A new guard counts map, direct-solve, KFE and relaxation entries before the call. The accepted KFE wrapper merges local counts in `finally`. The new map wrapper recovers selector budget counters and merges them into the global ledger on the first exceptional map exit, where the old helper would merge only after normal return. Direct HJB attempts are counted by the source before `spsolve`. Alpha attempts are recovered from the accepted relaxation receipt; if an exception lacks an exact attempt list, terminal `CALL_LEDGER_UNRESOLVED` preserves the original terminal as nested evidence.

Only after 31/31 household/KFE PASS may one integration start. The full integration envelope is reserved before entry; the accepted integration function counts labor, frozen share allocation, C1, firms, wage, monetary, fiscal, raw return and next K1B preparation. A new wrapper counts the same-S payoff call before entry, closing its old post-success-only increment gap. Failed attempted calls consume budget. No province borrows another province allowance; no retries, warm starts, fallback, second integration or solver substitution are prepared. The first identity, scientific, budget, seal or readback failure stops the entire one-shot path and preserves the consumed ledger. If exact attempted counts cannot be established, use `CALL_LEDGER_UNRESOLVED` rather than a false zero.

## Future single-repeat ceilings (not execution authority)

The one-turn ceilings halve the prior two-turn task where equivalent; the selector-root maximum is the frozen source `MAX_ROOTS_PER_PROVINCE=20,000,000` (`src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py:129`), thus at most 620,000,000 over 31 provinces. Root subtypes share that total. `k1b_feedback_calls=1` names the same frozen allocation event, not an extra feedback pass. All ceilings are future-task proposals; the present task budget is zero.

| Attempted category | One-repeat ceiling |
|---|---:|
| `source_native_initializations` | 31 |
| `scalar_labor_roots_attempted` | 24,800 |
| `scalar_labor_roots_returned` | 24,800 |
| `corrected_policy_maps` | 1,581 |
| `d2_q_assemblies` | 1,581 |
| `selector_evaluations` | 1,264,800 |
| `scalar_selector_root_invocations` | 620,000,000 |
| `direct_hjb_updates` | 1,550 |
| `hjb_checkpoint_evaluations_after_update` | 1,550 |
| `relaxation_helper_invocations` | 1,550 |
| `alpha_candidates` | 82,150 |
| `terminal_kfe_attempts` | 31 |
| `scc_decompositions` | 31 |
| `restricted_dense_scipy_linalg_svd_gesvd` | 31 |
| `normalized_stationary_candidates` | 31 |
| `q_transpose_times_p` | 31 |
| `corrected_aggregate_evaluations` | 31 |
| `firm_evaluations` | 31 |
| `household_batch_constructions` | 1 |
| `full_integrations` | 1 |
| `source_faithful_labor_reconstructions` | 1 |
| `frozen_k1b_quantity_allocations` | 1 |
| `k1b_feedback_calls` | 1 |
| `c1_residual_govinv_constructions` | 1 |
| `composite_wage_batches` | 1 |
| `monetary_assignments` | 1 |
| `fiscal_diagnostic_batches` | 1 |
| `completed_raw_ra0_vectors` | 1 |
| `deterministic_next_k1b_preparations` | 1 |
| `raw_next_payoff_same_s_constructions` | 1 |
| `turn7_household_calls` | 0 |
| `full_space_800_dense_scipy_linalg_svd_gesvd` | 0 |
| `scientific_retries` | 0 |
| `solver_substitutions` | 0 |
| `k2_calls` | 0 |
| `ge_annual_shock_irf_welfare_results_calls` | 0 |
| `matlab_scientific_calls` | 0 |

The direct HJB and post-update checkpoint limits are also **50 per province**. The output root must be new/disjoint. Before future calls, the future task must approve these ceilings and exact source/plan hashes independently; the old two-turn ceilings are provenance, not inherited permission.

## Post-execution comparison contract

After one legal turn6 and exactly one integration, the runner would seal the entering-turn7 bundle as C6-prime and compare it to sealed C6. For `Yt,Lt,wjt,w`, compute `max abs(new/old-1)`; for `Kt_prev`, `max abs(new-old)/Kt0` with exact positive frozen `Kt0`; for `rk,raw_ra0,rah,S`, compute maximum absolute difference (S over destination/origin). For every field record shape, finite status, float64 bitwise mismatch count, full-precision difference and argmax. Compare available household batch, KFE stationarity and integration numeric receipts as intermediates. Whole-file hashes bind identity but do **not** serve as numerical equivalence tests. Classification is `EXACT_BITWISE_MATCH`, `LEGAL_DIFFERENCE_OBSERVED`, or `UNAVAILABLE`. No `1e-6` repeatability PASS threshold is applied. Even exact agreement of one pair would not prove a general outer-map error bound, fixed point, MATLAB predicate, GE or Results.

## Preparation checks and limit

Static default preflight: PASS. Focused tests: **7 passed**, using `python -m pytest -q -p no:cacheprovider tests/test_mp4c_k1b_turn6_same_frozen_input_repeat_preflight.py` with bytecode writes disabled. Tests cover dry default, sealed-hash rejection, fresh authorization rejection, entry budget exhaustion, exact/changed sealed-data arithmetic, and failure-count reconciliation, including an early failed map entry whose source count remains zero. They import no model module and evaluate no model point. The future execution path, its exceptional call-accounting wrappers and numerical replay remain unexecuted; independent Work review and a distinct one-shot execution task are required.

## Scoped repair after independent REJECT (2026-09-24)

Work rejected candidate `c2a413c31115de9cd419b19f2e04cbe6460f86d1`; this zero-science repair starts from dispatch `0713726f5044fe375e49e9daca794a30205a0549` and retains `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`. The future gate now requires the specific future task file, byte-identical current task, and an explicit `Authorized output root` line naming the planned root. The source solver's `TASK_RELATIVE` is bound to that file before `_task_hashes()` and restored on exit. Both task files are in the before/after source snapshot. No future task or execution identifier was fabricated in this preparation.

The frozen old integration function is guarded at each source ledger entry line before the corresponding operation: source labor, frozen allocation and its feedback alias, C1, all 31 firms, wage, monetary, fiscal, completed raw return and next K1B preparation. Same-S payoff remains guarded before its call. A source-line marker mismatch blocks execution. Integration ledger reconciliation checks ceilings on success and exception, retains the larger of source and guarded attempted counts, and keeps an earlier terminal when reconciliation also fails. If a valid future task gate passes but a later pre-call identity check fails, the new, exclusive future output root receives `first_failure.json` with a literal zero-call ledger. An absent or invalid future gate writes nothing.

Comparison requires the accepted sealed manifest SHA-256 `51F636DF222DD1365B017091B6F77F78A71C606F84776CDFB62457105F2E9127` and verifies the hash and size of each of 70 reference intermediates before and after execution: eight shared receipts/arrays plus both KFE receipt and mass arrays for each of the canonical 31 provinces. JSON comparison labels cover numeric fields only; NPZ comparison covers named float64/int64 arrays with shape, finite, bitwise count, maximum absolute difference and location. Missing files or conflicting status, fields, shape or finiteness are explicit `UNAVAILABLE` and block a future success terminal. Sealed-old against sealed-old static arithmetic readback returned 70/70 exact comparisons; this is a comparator check, not replay evidence.

Repair checks: **13 static tests passed** with bytecode writes disabled using the focused command above; static preflight PASS, sealed reference readback 70/70, `git diff --check` PASS, four allowed changed paths only, and output root absent. The zero-science literal ledger remains household/HJB/KFE/integration/firm/K1B/GE/turn7/retries = 0. Execution remains unauthorized; Work must independently ACCEPT/REJECT this repair before any one-shot execution task.
