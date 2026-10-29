# P6: HJB_NOT_CONVERGED

Exactly one supervised command; exit0,elapsed79.188000s,timeoutFalse. The original point inputs and complete scalar result are below. Model calls are actual code-object observations, not inferred budgets. No warm start,clipping,source change or extra solve.

```json
{
  "event": "point_result",
  "point": "P6",
  "prices": {
    "id": "P6",
    "rah": 0.07,
    "rb": 0.02,
    "wt": 22.0
  },
  "classification": "HJB_NOT_CONVERGED",
  "fatal_to_task": false,
  "wage_provenance": {
    "scope": "COUNTERFACTUAL_SYNTHETIC_WAGE_WITNESS_NO_REAL_FIRM_EMPIRICAL_PROVENANCE",
    "chain": [
      "SyntheticNetWageCalculation",
      "calculated_round_record",
      "later_net_wage_record",
      "netwage_inputs"
    ],
    "generated_after_iteration": 1,
    "entering_iteration": 2,
    "synthetic_firm_wage": 12.99692898042432,
    "phi_destination_origin": [
      [
        1,
        1
      ],
      [
        1,
        1
      ]
    ],
    "phi_l": 5,
    "alphal": 1,
    "metadata_only_no_actual_firm_or_iteration_run": true,
    "point": "P6",
    "requested_effective_wage": 22.0,
    "actual_source_effective_wage": 22.0,
    "wage_error": 0.0,
    "context_id": "TEMP31_MATLAB800_SYNTHETIC_PRICE_PILOT_20261029_P6",
    "province_order": [
      "A",
      "B"
    ],
    "record_semantics": "CALCULATED_NET_AFTER_DESTINATION_TAU_AND_SIGMA",
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
    "value_min": -2.008853973581662,
    "value_max": -1.3045887236833664,
    "labor_min": 0.6173279721837283,
    "labor_max": 0.6650866225592402,
    "finite": true,
    "value_F_float64_sha256": "602de2266a90d1448697b5f9ce0e8166a4bce2e9cbe488a5f502445a9e49fed3",
    "labor_F_float64_sha256": "250eeb2345850ba279944d6a73b086192cf164cc812a472ccfac30d4a778ee0e",
    "fresh_for_point": "P6",
    "warm_start": false
  },
  "HJB": {
    "converged": false,
    "iterations": 100,
    "convergence_statistic": 0.30284201302767055,
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
      "nnz": 3638,
      "finite": true,
      "row_sum_abs_max": 0.005259977773237445,
      "max_signed_row_sum": 3.092281986027956e-10,
      "min_offdiagonal_including_implicit_zeros": -4.159921138081178,
      "csr_sha256": "d0df9b8a0adf563180b0613a41ee51961e889364653924532c96c8523ebcd555"
    },
    "post_convergence_operator": {
      "shape": [
        800,
        800
      ],
      "nnz": 3106,
      "finite": true,
      "row_sum_abs_max": 4.164157033891794,
      "max_signed_row_sum": 3.092281986027956e-10,
      "min_offdiagonal_including_implicit_zeros": 0.0,
      "csr_sha256": "ec4ef023dd130520c1f677dd7ce63e70eb53b0b02a5bd446378bb02a8a923c8b"
    },
    "max_observed_iteration_row_sum_abs": 0.005259977773237556,
    "MATLAB_homecrit": 0.01,
    "observed_homecrit_violation": false,
    "homecrit_guard_internal": "ABSENT_UNCHANGED_EXTERNAL_READONLY_OBSERVATION",
    "source_parity": "PARITY_UNCERTIFIED_RAW_MATLAB_NOT_LOCALLY_VERIFIED",
    "stale_last_policy_residual": 0.0003028442138285764,
    "implicit_identity_error": 2.200800905828148e-09,
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
    "task_relative_path": "evidence\\LOCAL_ONLY_P6_true_arrays_and_rates.npz",
    "bytes": 104972,
    "sha256": "162a232a678cbc0f06163a4c098647978bf33d34035d73f8f5dcb4134cb824fe",
    "LOCAL_ONLY": true,
    "observed_new_point_not_historical_tinygrid": true
  },
  "MATLAB_RAW_LOCAL_VERIFICATION": "NOT_AVAILABLE",
  "firm_GE_IRF_outer_31province_data_calls": 0,
  "source_or_economic_parameter_changes": 0
}
```

Corresponding evidence/P6_claim.json binds the command and entry/supervisor/grid hashes. evidence/P6_iteration_trajectory.json records every completed iteration's scalar value changes and actual operator diagnostics. All raw/public stdout/stderr hashes,redaction and resource/call receipts are retained. KFE probability marginals,when actually computed,contain all20 signed bins,not a truncated display. A noncertified KFE moment is not a successful stationary estimate.
