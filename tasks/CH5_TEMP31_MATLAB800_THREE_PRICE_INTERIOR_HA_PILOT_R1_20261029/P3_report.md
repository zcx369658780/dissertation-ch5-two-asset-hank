# P3: HJB_NOT_CONVERGED

Exactly one supervised command; exit0,elapsed47.812000s,timeoutFalse. The original point inputs and complete scalar result are below. Model calls are actual code-object observations, not inferred budgets. No warm start,clipping,source change or extra solve.

```json
{
  "event": "point_result",
  "point": "P3",
  "prices": {
    "id": "P3",
    "rah": 0.07,
    "rb": 0.01,
    "wt": 19.0
  },
  "classification": "HJB_NOT_CONVERGED",
  "fatal_to_task": false,
  "wage_provenance": {
    "scope": "NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL",
    "chain": [
      "numerical_bootstrap19",
      "netwage_inputs"
    ],
    "entering_iteration": 1,
    "synthetic_firm_wage": null,
    "point": "P3",
    "requested_effective_wage": 19.0,
    "actual_source_effective_wage": 19.0,
    "wage_error": 0.0,
    "context_id": "TEMP31_MATLAB800_SYNTHETIC_PRICE_PILOT_20261029_P3",
    "province_order": [
      "A",
      "B"
    ],
    "record_semantics": "NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL",
    "real_empirical_provenance": false,
    "tax_background_preserved": true
  },
  "initialization": {
    "shape": [
      20,
      20,
      2
    ],
    "states": 800,
    "value_min": -2.2758269495752206,
    "value_max": -1.4813990014860707,
    "labor_min": 0.6306894361297597,
    "labor_max": 0.6789545882557355,
    "finite": true,
    "value_F_float64_sha256": "8d9ebcb961738d449bde340aa7511857cd4b2b0ff8cd246eb96917808b0ed020",
    "labor_F_float64_sha256": "7ecace19f6d410aa617e125bec20f10112238cb9e6ab171945c97d9ad2834a60",
    "fresh_for_point": "P3",
    "warm_start": false
  },
  "HJB": {
    "converged": false,
    "iterations": 100,
    "convergence_statistic": 0.3137381136912758,
    "finite_return_fields": {
      "value": true,
      "initial_value": true,
      "consumption": true,
      "labor": true,
      "transfer": true,
      "adjustment_cost": true,
      "effective_illiquid_return": true,
      "mu_a": true,
      "mu_b": true,
      "utility": true
    },
    "iteration_operator": {
      "shape": [
        800,
        800
      ],
      "nnz": 3845,
      "finite": true,
      "row_sum_abs_max": 0.005268770152606017,
      "max_signed_row_sum": 8.502543669131057e-10,
      "min_offdiagonal_including_implicit_zeros": -2.7784911631324647,
      "csr_sha256": "62affc5e8fc79d6853c2400c92257a9961ea78e67313dcad527ed4397765ea44"
    },
    "post_convergence_operator": {
      "shape": [
        800,
        800
      ],
      "nnz": 3107,
      "finite": true,
      "row_sum_abs_max": 2.783717016145523,
      "max_signed_row_sum": 3.1044083970144243e-10,
      "min_offdiagonal_including_implicit_zeros": 0.0,
      "csr_sha256": "ce9e371ea30d8678aa7c5b54c63624aab6ef4917df5bf6f11989768b021cc694"
    },
    "max_observed_iteration_row_sum_abs": 0.005268770155790248,
    "MATLAB_homecrit": 0.01,
    "observed_homecrit_violation": false,
    "homecrit_guard_internal": "ABSENT_UNCHANGED_EXTERNAL_READONLY_OBSERVATION",
    "source_parity": "PARITY_UNCERTIFIED_RAW_MATLAB_NOT_LOCALLY_VERIFIED",
    "stale_last_policy_residual": 0.0003137381136897044,
    "implicit_identity_error": 7.675978818275574e-07,
    "full_nonlinear_Bellman_residual": "NOT_EVALUATED",
    "warnings": []
  },
  "KFE": {
    "status": "NOT_EXECUTED_HJB_NOT_CONVERGED",
    "At": null,
    "Bt": null,
    "Lt": null,
    "Ct": null,
    "a_mass20": null,
    "b_mass20": null
  },
  "observed_counts": {
    "initializer_calls": 1,
    "root_cells": 800,
    "brentq_calls": 800,
    "hjb_calls": 1,
    "hjb_iterations": 100,
    "hjb_policy_cells": 80000,
    "operator_assemblies": 101,
    "hjb_linear_solves": 100,
    "kfe_calls": 0,
    "kfe_linear_solves": 0,
    "kfe_contaminated_row_index_calls": 0
  },
  "LOCAL_ONLY_hjb_archive": {
    "task_relative_path": "evidence\\LOCAL_ONLY_P3_true_arrays_and_rates.npz",
    "bytes": 108773,
    "sha256": "e98d7b78e1aac09ba5f2e83ae5a7f2e2cc5e0f7e9d9266425e20b574a8ea1bb0",
    "LOCAL_ONLY": true,
    "observed_new_point_not_historical_tinygrid": true
  },
  "MATLAB_RAW_LOCAL_VERIFICATION": "NOT_AVAILABLE",
  "firm_GE_IRF_outer_31province_data_calls": 0,
  "source_or_economic_parameter_changes": 0
}
```

Corresponding evidence/P3_claim.json binds the command and entry/supervisor/grid hashes. evidence/P3_iteration_trajectory.json records every completed iteration's scalar value changes and actual operator diagnostics. All raw/public stdout/stderr hashes,redaction and resource/call receipts are retained. KFE probability marginals,when actually computed,contain all20 signed bins,not a truncated display. A noncertified KFE moment is not a successful stationary estimate.
