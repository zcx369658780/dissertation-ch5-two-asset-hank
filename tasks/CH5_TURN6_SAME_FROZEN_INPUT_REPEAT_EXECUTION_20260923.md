# Current Builder Task

Task ID: `CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_EXECUTION_20260923`
Status: `ACTIVE__ONE_SHOT_SAME_FROZEN_INPUT_REPEAT`
Execution authorization ID: `K1B_C5_C6P_20260925_ONCE`
Authorized output root: `reports/ch5_turn6_same_frozen_input_repeat_20260923_run001`

## Authority and purpose

The Owner agreed to pursue one separately budgeted repeat from sealed C5, and on 2026-09-25 directed GPT Work to continue the established route after independent review. GPT Work independently ACCEPTED the zero-science runner repair5 candidate `81866d8f23cbb36e16281c41add27539c6ce7c6f` in `docs/CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_RUNNER_REPAIR5_INDEPENDENT_REVIEW_20260925.md`. This is a **new, one-shot execution authorization** for exactly one turn6 evaluation from the same frozen C5 input, yielding C6-prime for comparison with the sealed C6. It does not authorize turn7 household, a second repeat, tuning, convergence, GE, or Results.

Only work in `D:\ProjectTemp\c5k1bturn56`. Never access `deep-learning-hank`. Local committed state and evidence are authority; GitHub is not an execution gate. Read `CURRENT.md`, `SCIENTIFIC_DECISIONS.md`, this task, `REVIEW_GATE.md`, the repair5 independent review, and the directly relevant preparation report/receipt before execution.

## Mandatory pre-entry gate

Before any scientific call, verify: clean local HEAD and unchanged committed runner; `HEAD:src=00682b2e1a7ba23665f6e16f6acf48ad35874883`; this `TASK_CURRENT.md` byte-identical to `tasks/CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_EXECUTION_20260923.md`; no existing authorized output root; default static preflight PASS; accepted runner SHA-256 `E362B921D4984669C3257A671684F55809702531522D253C26D80886786880B2`; sealed manifest SHA-256 `51F636DF222DD1365B017091B6F77F78A71C606F84776CDFB62457105F2E9127`; distance mapping SHA-256 `51A04FCAA1FA519B142BE2A155640F77E8746493AFDF4865ED243B96526E550D`; frozen input and reference identities listed below. Preserve the runner's future-task gate and source/reference snapshots. If any pre-entry check fails, stop with zero scientific calls and report the first blocker; do not repair or replace inputs.

Sealed C5 entering-turn6 input: `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/turn6_k1b_input_candidate.json` SHA-256 `87BEB944AD35C16BAF62D35FE8DDAD3BDEBC9000DCB6CC9F7D6949A039F4B1BC`; paired `turn6_k1b_frozen_share_payoff_plan.npz` SHA-256 `95880D37D5BBB10B95FF776E32B8B786447B20C1770117044C7735D91292ED34`. Sealed C6 reference: `turn7_k1b_input_candidate.json` SHA-256 `D84E9D74C7E965A3B492F2F0F9A63D3320D436DD4A6D78E1E655F014C05FC059`; paired `turn7_k1b_frozen_share_payoff_plan.npz` SHA-256 `37A1258F8EC87116F03084D8178C77424FDD5F3859A1BC73D9704940A3B9381E`, both under the same sealed report root.

## One-shot call budget

Exactly **one runner `--execute` invocation**, no retry. At most 31 province household HJB/KFE evaluations, one completed turn6 integration after 31/31 household PASS, and zero turn7 household evaluations. Failed entries count. The following category ceilings are adopted for this one repeat, not for a successor; the runner's `CEILINGS` and per-province guard must agree exactly. The 620,000,000 selector-root invocations are an aggregate ceiling from 20,000,000 per province; root subtypes share that ceiling. `k1b_feedback_calls=1` is the same frozen allocation event, not an extra pass.

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

Direct HJB updates and post-update checkpoint evaluations are also bounded at 50 each per province. No province borrows another's allowance. No warm starts, alternate initialization, retry, second integration, solver substitution, damping/tolerance/grid change, or model-law change. Do not enlarge this budget if a call fails. If exact attempted counts cannot be resolved, use `CALL_LEDGER_UNRESOLVED` and preserve the earliest terminal and all available counts.

## Exact execution and writes

After the pre-entry gate, run the accepted future runner once with `--execute --execution-id K1B_C5_C6P_20260925_ONCE`; do not invoke the old two-turn `execute()`. The runner alone creates and writes the fresh authorized output root. The Builder may write only that root, a concise `docs/CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_EXECUTION_REPORT_20260925.md`, and the already committed current task/archive only as read-only authority. Do not edit `src/`, runner, tests, sealed evidence, governance files, scientific law, or old report roots. Preserve any partial output after first failure; do not delete, reset, overwrite, or rerun it. Do not push.

On terminal success or first failure, perform read-only hashes and a bounded manifest/readback over generated artifacts, recording relative path, bytes and SHA-256 under the authorized output root if it can be safely written. Include input/source/runner/task identities, environment, exact attempted and source call ledgers, first terminal, output status, and comparison status in the report. Stage only explicit allowed paths and make one local evidence commit when safe; if the output is too large for a single bounded commit, preserve it in place and report the exact uncommitted inventory and manifest rather than broad staging or cleanup.

## Interpretation and terminal gate

For the nine components compare C6-prime to sealed C6 using the formulas and complete float64/shape/finite/bitwise diagnostics already specified in the preparation report. Classify observed evidence as `EXACT_BITWISE_MATCH`, `LEGAL_DIFFERENCE_OBSERVED`, or `UNAVAILABLE`; do not turn `1e-6` into a repeatability pass threshold. One exact pair is not a general error bound, contraction, fixed point, steady state, or GE. `Results eligibility = FALSE`.

Stop on the first identity, budget, scientific, output ownership, seal, or readback failure. No repair, retry or successor execution under this task. Return the local commit if one was made, artifact manifest/location, exact call ledger including failed attempts, first terminal, and C6-prime comparison if available. **GPT Work independently reviews this one-shot execution before any successor task.** Turn7 household and every later scientific route remain closed.
