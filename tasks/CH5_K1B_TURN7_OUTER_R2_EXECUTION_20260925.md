# Current Builder Task

Task ID: `CH5_K1B_TURN7_OUTER_R2_EXECUTION_20260925`

Status: `ACTIVE__ONE_SHOT_TURN7_OUTER_R2`

Execution authorization ID: `turn7-r2-run001`

Authorized output root: `reports/ch5_k1b_turn7_outer_r2_20260925_run001`

## Authority and exact boundary

GPT Work independently **ACCEPTED** zero-science runner candidate `740f06648a3be7f3d571d5bb2f8ff6668a193b90` in `docs/CH5_K1B_TURN7_OUTER_R2_RUNNER_INDEPENDENT_REVIEW_20260925.md`. Owner adopted the future frozen bounded nine-component strict `<1e-6`, two consecutive complete legal adjacent comparisons (R2), clipped-`ra` report-only for the new criterion, two-turn maximum ceilings, and first-failure zero-retry contract in `docs/CH5_FULL_OUTER_STATE_STOP_FAILURE_BUDGET_OWNER_ADOPTION_20260925.md`. This task authorizes exactly **one** C6→C7 turn7 attempt, not turn8. Its first scientific/model entry consumes this one-shot authorization whether success or failure. No repair, rescue, rerun, second integration, or budget reset is authorized.

Work only in `D:\ProjectTemp\c5k1bturn56`; never enter, read, search, cite or modify `deep-learning-hank`. Use only the designated Codex session “整理第五章 K1B 收敛设计证据” (`01a0cce5-241d-7ab3-b87c-e0a41628572e`). Local Git and evidence are authority; GitHub is not a daily gate. Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, this task, `REVIEW_GATE.md`, Owner adoption, the accepted proposal, the independent runner review, and directly bound source/evidence.

## Before the sole invocation

Verify the committed `TASK_CURRENT.md` and this archived file are byte identical, the execution ID and root above match the runner, HEAD descends from runner candidate and Owner adoption, `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`, and production `src`/runner/task files are clean. Confirm the only pre-existing untracked path is preserved `reports/ch5_turn6_same_frozen_input_repeat_20260923_run001/`; preserve its full manifest SHA-256 `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61` and contents. The new output root must be absent. Bind the sealed completed C6 entering-turn7 JSON SHA-256 `D84E9D74C7E965A3B492F2F0F9A63D3320D436DD4A6D78E1E655F014C05FC059`, NPZ SHA-256 `37A1258F8EC87116F03084D8178C77424FDD5F3859A1BC73D9704940A3B9381E`, and sealed manifest SHA-256 `51F636DF222DD1365B017091B6F77F78A71C606F84776CDFB62457105F2E9127`. C6-prime repeat output is **not** an input. Run the runner's default static preflight. If any pre-call check fails, stop before science and report the first blocker.

## Exact scientific ceiling, attempted calls including failed entries

The following table reproduces every adopted proposal category plus Owner's three resolved categories, turn7-only batch boundary, and the one integration ceiling. A per-turn cap is the maximum for this task; the two-turn cap is a cumulative upper bound across turn7 and any separately authorized future turn8. No unused turn7 allowance may be borrowed within a province or used to retry. These are maxima, not required target counts.

| Ledger category | turn7 maximum | turn7+turn8 maximum |
|---|---:|---:|
| `source_native_initializations` | 31 | 62 |
| `scalar_labor_roots_attempted` | 24800 | 49600 |
| `scalar_labor_roots_returned` | 24800 | 49600 |
| `corrected_policy_maps` | 1581 | 3162 |
| `d2_q_assemblies` | 1581 | 3162 |
| `selector_evaluations` | 1264800 | 2529600 |
| `scalar_selector_root_invocations` | 620000000 | 1240000000 |
| `direct_hjb_updates` | 1550 | 3100 |
| `hjb_checkpoint_evaluations_after_update` | 1550 | 3100 |
| `relaxation_helper_invocations` | 1550 | 3100 |
| `alpha_candidates` | 82150 | 164300 |
| `terminal_kfe_attempts` | 31 | 62 |
| `scc_decompositions` | 31 | 62 |
| `restricted_dense_scipy_linalg_svd_gesvd` | 31 | 62 |
| `normalized_stationary_candidates` | 31 | 62 |
| `q_transpose_times_p` | 31 | 62 |
| `corrected_aggregate_evaluations` | 31 | 62 |
| `household_batch_constructions` | 1 | 2 |
| `full_integrations` | 1 | 2 |
| `source_faithful_labor_reconstructions` | 1 | 2 |
| `frozen_k1b_quantity_allocations` | 1 | 2 |
| `k1b_feedback_calls` | 1 | 2 |
| `c1_residual_govinv_constructions` | 1 | 2 |
| `firm_evaluations` | 31 | 62 |
| `composite_wage_batches` | 1 | 2 |
| `monetary_assignments` | 1 | 2 |
| `fiscal_diagnostic_batches` | 1 | 2 |
| `completed_raw_ra0_vectors` | 1 | 2 |
| `deterministic_next_k1b_preparations` | 1 | 2 |
| `raw_next_payoff_same_s_constructions` | 1 | 2 |
| `turn7_household_calls` | 1 | 1 |
| `turn8_household_calls` | 0 | 1 only under a new task |
| `full_space_800_dense_scipy_linalg_svd_gesvd` | 0 | 0 |
| `scientific_retries`, `solver_substitutions` | 0 | 0 |
| `k2_calls`, `ge_annual_shock_irf_welfare_results_calls`, `matlab_scientific_calls` | 0 | 0 |

Per province, turn7 maxima are 51 policy maps, 40800 selector evaluations, 20000000 selector-root invocations, 50 direct HJB updates, and 1 terminal KFE attempt. Source-native initialization is one/province. 31/31 household HJB/KFE PASS is required before the single integration. Source entry guards and source ledger must reconcile; if exact attempted counts cannot be resolved, report `CALL_LEDGER_UNRESOLVED` and the available partial ledgers. The earliest underlying failure remains visible. Do not relabel a valid threshold miss as scientific failure.

## Execution and evidence

After the above checks, make exactly one invocation of `python -B validators/multi_province/k1b_turn7_outer_r2/run.py --execute --execution-id turn7-r2-run001` from the sole worktree. Do not invoke any old runner's `execute()`, invoke this runner again, or run turn8. The runner must exclusively claim the new root; preserve every written artifact, including a failed/partial root. No cleanup, overwrite, output-root relocation, or repair after the first terminal.

On a legal complete C7 only, seal/read back the entering-turn8 candidate and plan; compare C6→C7 using all nine adopted same-stage formulas, strict `<1e-6` for each component. Report clipped `ra` hits separately from the original MATLAB zero-hit predicate. A first pass is **not** R2; a legal miss is `VALID__NINE_COMPONENT_LEVEL_NOT_MET`. Results eligibility stays `FALSE` regardless of the outcome.

Allowed writes are the new output root and, after the invocation, a concise execution report at `docs/CH5_K1B_TURN7_OUTER_R2_EXECUTION_REPORT_20260925.md` and machine receipt at `EVIDENCE/ch5_k1b_turn7_outer_r2_execution_20260925/execution_receipt.json`. Do not edit `src/`, any runner/test, governance/authority files, sealed evidence, or the repeat output. Record exact invocation count, first terminal, guard/source ledgers including failed attempts, hashes and full output manifest when safely available, C6/C7 comparison or its absence, `git diff --check`, and any unverifiable fact as `UNRESOLVED`. Stage only the report and receipt for one local candidate commit; leave scientific output untracked and intact. Do not claim the worktree clean while outputs are untracked.

Stop immediately on the first identity, legality, budget, ownership, seal/readback, ledger or model failure. If the process fails without an exact ledger, do not infer zero or retry. Report to GPT Work for independent ACCEPT/REJECT. No self-acceptance, automatic turn8, K2, GE, annual dynamics, shocks, IRFs, welfare or Results. The latest independent Work review controls the next gate.
