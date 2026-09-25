# C5-to-C6-prime same-frozen-input one-shot execution

Task: `CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_EXECUTION_20260923`; execution ID: `K1B_C5_C6P_20260925_ONCE`.

## Terminal and scope

Exactly one accepted runner `--execute` invocation returned exit code 0 and `PASS__TURN6_SAME_FROZEN_INPUT_REPEAT__ONE_PAIR_ONLY`. First failure: none. `call_ledger_resolved=true`, `guard_denied=[]`. Thirty-one province terminal receipts exist and one turn6 integration completed. The future turn7 household, K2, GE, Results and retries remain zero. No second invocation, tuning or replacement input was used.

This is one observed pair only. It does not establish a general repeatability error bound, convergence, fixed point, steady state or GE. `1e-6` is diagnostic precision only; Results eligibility is `FALSE`. GPT Work independent review is required before any successor.

## Authority and identity readback

Pre-entry local HEAD: `dca015404855fbf25fb4b496fb60ad91a1696043`. Frozen `HEAD:src`: `00682b2e1a7ba23665f6e16f6acf48ad35874883`. The worktree was clean and the planned output root absent before entry. `TASK_CURRENT.md` and the archived execution task were byte-identical. The 37 runner ceilings and per-province guard matched the task; default static preflight returned `PASS__STATIC_PREFLIGHT_ONLY`.

| Identity | Relative path | SHA-256 after execution |
|---|---|---|
| runner | `validators/multi_province/k1b_turn6_same_frozen_input_repeat/run.py` | `E362B921D4984669C3257A671684F55809702531522D253C26D80886786880B2` |
| current task | `TASK_CURRENT.md` | `576F35B2D94B135AB3538AB5E6D4EE0D192A4B9183CC3A73BADB7FCD3DCA8F59` |
| archived execution task | `tasks/CH5_TURN6_SAME_FROZEN_INPUT_REPEAT_EXECUTION_20260923.md` | `576F35B2D94B135AB3538AB5E6D4EE0D192A4B9183CC3A73BADB7FCD3DCA8F59` |
| sealed manifest | `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/sealed_manifest.json` | `51F636DF222DD1365B017091B6F77F78A71C606F84776CDFB62457105F2E9127` |
| distance mapping | `docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv` | `51A04FCAA1FA519B142BE2A155640F77E8746493AFDF4865ED243B96526E550D` |
| C5 JSON | `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/turn6_k1b_input_candidate.json` | `87BEB944AD35C16BAF62D35FE8DDAD3BDEBC9000DCB6CC9F7D6949A039F4B1BC` |
| C5 NPZ | `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/turn6_k1b_frozen_share_payoff_plan.npz` | `95880D37D5BBB10B95FF776E32B8B786447B20C1770117044C7735D91292ED34` |
| sealed C6 JSON | `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/turn7_k1b_input_candidate.json` | `D84E9D74C7E965A3B492F2F0F9A63D3320D436DD4A6D78E1E655F014C05FC059` |
| sealed C6 NPZ | `reports/ch5_mp4c_k1b_turn5_turn6_bounded_continuation_20260921_run001/turn7_k1b_frozen_share_payoff_plan.npz` | `37A1258F8EC87116F03084D8178C77424FDD5F3859A1BC73D9704940A3B9381E` |

The runner's own post-execution source and sealed-reference checks passed. The generated preflight receipt is `reports/ch5_turn6_same_frozen_input_repeat_20260923_run001/preflight.json` (SHA-256 `85DFE5F6210DA8373880AFE51213C20C24967008FB028E31B490785E5022A55E`). Its captured environment was Python `3.11.9`, NumPy `2.4.6`, SciPy `1.17.1`, `Windows-10-10.0.26200-SP0`; complete BLAS and thread settings are preserved verbatim in that receipt.

## Exact call ledgers

The full source and guard-attempted ledgers below are copied from `terminal_receipt.json` (SHA-256 `8F008B2CEF18A305EB3A1F4C11DF484CAB249513ACB7475728CF1B1248E6B03F`). All 37 guarded categories agree with their source counts. Every attempted call, including failed entries if any, consumes its budget.

Source ledger:

```json
{
  "source_native_initializations": 31,
  "scalar_labor_roots_attempted": 24800,
  "scalar_labor_roots_returned": 24800,
  "corrected_policy_maps": 409,
  "selector_evaluations": 327200,
  "scalar_selector_root_invocations": 141123,
  "interior_z_root_invocations": 30086,
  "interior_a_switching_root_invocations": 0,
  "joint_switching_root_invocations": 0,
  "d2_q_assemblies": 409,
  "direct_hjb_updates": 378,
  "hjb_checkpoint_evaluations_after_update": 378,
  "scc_decompositions": 31,
  "restricted_dense_scipy_linalg_svd_gesvd": 31,
  "full_space_800_dense_scipy_linalg_svd_gesvd": 0,
  "normalized_stationary_candidates": 31,
  "q_transpose_times_p": 31,
  "corrected_aggregate_evaluations": 31,
  "household_batch_constructions": 1,
  "source_faithful_labor_reconstructions": 1,
  "k1a_capital_network_allocations": 0,
  "c1_residual_govinv_constructions": 1,
  "firm_evaluations": 31,
  "composite_wage_batches": 1,
  "monetary_assignments": 1,
  "fiscal_diagnostic_batches": 1,
  "raw_next_payoff_same_s_constructions": 1,
  "turn3_household_calls": 0,
  "third_outer_turns": 0,
  "k1b_feedback_calls": 1,
  "k2_calls": 0,
  "adaptive_controller_calls": 0,
  "matlab_scientific_calls": 0,
  "ge_annual_shock_irf_welfare_results_calls": 0,
  "scientific_retries": 0,
  "solver_substitutions": 0,
  "damping_relaxation_adaptive_delta_clipping_artificial_diffusion_continuation_calls": 0,
  "payoff_clipping_annualization_rescaling_smoothing_risk_adjustment_zscore_calls": 0,
  "turn": 6,
  "authorized_k1b_household_batches": 0,
  "frozen_k1b_quantity_allocations": 1,
  "completed_raw_ra0_vectors": 1,
  "deterministic_next_k1b_preparations": 1,
  "turn5_household_calls": 0,
  "turn6_household_calls": 0,
  "turn7_household_calls": 0,
  "terminal_kfe_attempts": 31,
  "full_integrations": 1,
  "relaxation_helper_invocations": 378,
  "alpha_candidates": 382
}
```

Guard-attempted ledger:

```json
{
  "source_native_initializations": 31,
  "scalar_labor_roots_attempted": 24800,
  "scalar_labor_roots_returned": 24800,
  "corrected_policy_maps": 409,
  "d2_q_assemblies": 409,
  "selector_evaluations": 327200,
  "scalar_selector_root_invocations": 141123,
  "direct_hjb_updates": 378,
  "hjb_checkpoint_evaluations_after_update": 378,
  "relaxation_helper_invocations": 378,
  "alpha_candidates": 382,
  "terminal_kfe_attempts": 31,
  "scc_decompositions": 31,
  "restricted_dense_scipy_linalg_svd_gesvd": 31,
  "normalized_stationary_candidates": 31,
  "q_transpose_times_p": 31,
  "corrected_aggregate_evaluations": 31,
  "firm_evaluations": 31,
  "household_batch_constructions": 1,
  "full_integrations": 1,
  "source_faithful_labor_reconstructions": 1,
  "frozen_k1b_quantity_allocations": 1,
  "k1b_feedback_calls": 1,
  "c1_residual_govinv_constructions": 1,
  "composite_wage_batches": 1,
  "monetary_assignments": 1,
  "fiscal_diagnostic_batches": 1,
  "completed_raw_ra0_vectors": 1,
  "deterministic_next_k1b_preparations": 1,
  "raw_next_payoff_same_s_constructions": 1,
  "turn7_household_calls": 0,
  "full_space_800_dense_scipy_linalg_svd_gesvd": 0,
  "scientific_retries": 0,
  "solver_substitutions": 0,
  "k2_calls": 0,
  "ge_annual_shock_irf_welfare_results_calls": 0,
  "matlab_scientific_calls": 0
}
```

## C6-prime comparison

The generated C6-prime carrier compared with sealed C6 as `EXACT_BITWISE_MATCH` for all nine components. The 70 sealed-reference intermediate comparisons also all report `EXACT_BITWISE_MATCH`; none is `UNAVAILABLE`. Each row retains shape, finite status, bitwise mismatch count, full-precision difference and location in `comparison_receipt.json` (SHA-256 `4E41A251E050A0D25F73246E36800B872B29F526D519189C1D69B425A8D89C9B`). The generated entering-turn7 bundle readback is `PASS` with no bad paths and zero turn7 household calls (SHA-256 `0A0C71F53B58A216B627CBCC5AA9E6FAF0E5633CB6DF3AC2FD85C586E63CDFF1`). The generated turn7 bundle is output evidence only, not authorization to run its household stage.

| Component | Bitwise mismatches | Diagnostic difference | Classification |
|---|---:|---:|---|
| `Yt` | 0 | 0 | `EXACT_BITWISE_MATCH` |
| `Lt` | 0 | 0 | `EXACT_BITWISE_MATCH` |
| `wjt` | 0 | 0 | `EXACT_BITWISE_MATCH` |
| `rk` | 0 | 0 | `EXACT_BITWISE_MATCH` |
| `Kt_prev` | 0 | 0 | `EXACT_BITWISE_MATCH` |
| `w` | 0 | 0 | `EXACT_BITWISE_MATCH` |
| `raw_ra0` | 0 | 0 | `EXACT_BITWISE_MATCH` |
| `rah` | 0 | 0 | `EXACT_BITWISE_MATCH` |
| `S` | 0 | 0 | `EXACT_BITWISE_MATCH` |

## Output inventory and preservation

Authorized output root: `reports/ch5_turn6_same_frozen_input_repeat_20260923_run001`. An exclusive, root-contained `execution_artifact_manifest.json` lists each pre-manifest artifact with relative path, byte count and SHA-256. Its full readback passed: **5141 artifacts, 63888760 bytes**. Manifest SHA-256: `7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61`; manifest size: `1069046` bytes. Including the manifest, the preserved root contains **5142 files, 64957806 bytes**. No `first_failure.json` exists. The entire root remains untracked and in place because 5,142 files/64.96 MB exceed this task's bounded single-commit evidence set; its exact inventory is the manifest. The local evidence commit stages this report only. No output was deleted or overwritten.
