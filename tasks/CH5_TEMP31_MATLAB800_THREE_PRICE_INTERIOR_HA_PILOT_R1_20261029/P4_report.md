# P4: KFE_NOT_CERTIFIED

Exactly one supervised command; exit0,elapsed6.078000s,timeoutFalse. The original point inputs and complete scalar result are below. Model calls are actual code-object observations, not inferred budgets. No warm start,clipping,source change or extra solve.

```json
{
  "event": "point_result",
  "point": "P4",
  "prices": {
    "id": "P4",
    "rah": 0.07,
    "rb": 0.03,
    "wt": 19.0
  },
  "classification": "KFE_NOT_CERTIFIED",
  "fatal_to_task": false,
  "wage_provenance": {
    "scope": "NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL",
    "chain": [
      "numerical_bootstrap19",
      "netwage_inputs"
    ],
    "entering_iteration": 1,
    "synthetic_firm_wage": null,
    "point": "P4",
    "requested_effective_wage": 19.0,
    "actual_source_effective_wage": 19.0,
    "wage_error": 0.0,
    "context_id": "TEMP31_MATLAB800_SYNTHETIC_PRICE_PILOT_20261029_P4",
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
    "value_min": -2.283445952434287,
    "value_max": -1.473352068476526,
    "labor_min": 0.6295434731579279,
    "labor_max": 0.6797104435951614,
    "finite": true,
    "value_F_float64_sha256": "c56b365ec7af7f43be8b4b5987d0757c9c971d57dea23f0cb295b5d64a276332",
    "labor_F_float64_sha256": "0a6c136b21408c8bd525b969ac56d8b110e76c326d261bc0fd11e0e5f5569981",
    "fresh_for_point": "P4",
    "warm_start": false
  },
  "HJB": {
    "converged": true,
    "iterations": 12,
    "convergence_statistic": 5.973323835561928e-08,
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
      "nnz": 3666,
      "finite": true,
      "row_sum_abs_max": 0.005235334255042967,
      "max_signed_row_sum": 5.717648576819556e-15,
      "min_offdiagonal_including_implicit_zeros": -4.085487501658151,
      "csr_sha256": "f384b5972014c937cc8f871a2504921600d08e60881f38bea06de72ab2612fdb"
    },
    "post_convergence_operator": {
      "shape": [
        800,
        800
      ],
      "nnz": 3127,
      "finite": true,
      "row_sum_abs_max": 4.089693449132323,
      "max_signed_row_sum": 4.718447854656915e-15,
      "min_offdiagonal_including_implicit_zeros": 0.0,
      "csr_sha256": "73f5c6e916ed62db1e0940123646e42392a5807394f147729d8df9f0ba652dda"
    },
    "max_observed_iteration_row_sum_abs": 0.005235334255043134,
    "MATLAB_homecrit": 0.01,
    "observed_homecrit_violation": false,
    "homecrit_guard_internal": "ABSENT_UNCHANGED_EXTERNAL_READONLY_OBSERVATION",
    "source_parity": "PARITY_UNCERTIFIED_RAW_MATLAB_NOT_LOCALLY_VERIFIED",
    "stale_last_policy_residual": 5.973330163833168e-11,
    "implicit_identity_error": 2.4422242006494343e-14,
    "full_nonlinear_Bellman_residual": "NOT_EVALUATED",
    "warnings": []
  },
  "KFE": {
    "status": "KFE_NOT_CERTIFIED",
    "At": 7.2688448772635486,
    "Bt": 4.70974313001291,
    "Lt": 0.6601808634080559,
    "Ct": 11.925467854930812,
    "a_mass20": [
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      2.1282374255790338e-06,
      3.56431802199123e-05,
      0.00026189389918271783,
      0.001393159773852164,
      0.006102564241698534,
      0.02345944310820311,
      0.07685503855978537,
      0.21220083368544895,
      0.49669756558577116,
      0.10293136305161149,
      0.06280401906670853,
      0.017256337302930767,
      1.0307161633425521e-08,
      0.0
    ],
    "b_mass20": [
      0.0,
      0.0,
      0.0,
      0.0,
      -2.5121662922401364e-18,
      -5.343780603246573e-18,
      -4.9950668033684495e-18,
      -5.2044928214386446e-18,
      -5.356905788476699e-18,
      -8.426486783810887e-18,
      -1.418673587540083e-17,
      -1.526849840254597e-17,
      -1.2167738595156964e-17,
      -3.028751866846113e-17,
      -3.4399180105701095e-17,
      0.08323695538715425,
      0.07838122356655354,
      0.07431821019991072,
      0.07111216303114319,
      0.6929514478152384
    ],
    "total_probability": 1.0,
    "negative_probability_mass": 1.6893356816383517e-16,
    "negative_density_cells": 115,
    "density_min": -9.502458705857893e-17,
    "density_max": 0.6851347398409715,
    "a_lower_mass": 0.0,
    "a_upper_mass": 0.0,
    "a_internal_mass": 1.0,
    "b_lower_mass": 0.0,
    "b_upper_mass": 0.6929514478152384,
    "b_internal_mass": 0.30704855218476157,
    "a_mode_indices0": [
      14
    ],
    "a_mode_asset_positions": [
      7.368421052631579
    ],
    "At_distance_from_lower": 7.2688448772635486,
    "At_distance_from_upper": 2.7311551227364514,
    "stationary_residual": 3.7634433046985296,
    "contaminated_raw_system_residual": 1.4619788669609224e-17,
    "source_raw_residual_inf": 1.4619788669609224e-17,
    "contaminated_row_index0": 295,
    "rhs_at_contaminated_row": 0.007,
    "normalization_factor": 0.018255522382932515,
    "cell_weight": 0.19390581717451522,
    "certification_tests": {
      "density_finite": true,
      "total_probability_abs_error_le_1e8": true,
      "negative_probability_mass_le_1e8": true,
      "post_stationary_residual_le_1e7": false,
      "contaminated_raw_system_residual_le_1e7": true
    },
    "interior_tests": {
      "At_strict_0_10": true,
      "a_internal_mass_ge_point10": true,
      "a_lower_mass_le_point50": true,
      "a_upper_mass_le_point50": true,
      "a_modal_indices_not_only_endpoints": true,
      "b_internal_mass_ge_point05": true
    },
    "warnings": [],
    "signed_density_unmodified": true,
    "source_post_operator_passed_directly_and_unchanged": true,
    "LOCAL_ONLY_archive": {
      "task_relative_path": "evidence\\LOCAL_ONLY_P4_true_KFE_density.npz",
      "bytes": 6501,
      "sha256": "b200d0f541e863235d3ad8f1423e1cf4815a860cbf2b6e11a07d3195e610e38b"
    }
  },
  "observed_counts": {
    "initializer_calls": 1,
    "root_cells": 800,
    "brentq_calls": 800,
    "hjb_calls": 1,
    "hjb_iterations": 12,
    "hjb_policy_cells": 9600,
    "operator_assemblies": 13,
    "hjb_linear_solves": 12,
    "kfe_calls": 1,
    "kfe_linear_solves": 1,
    "kfe_contaminated_row_index_calls": 1
  },
  "LOCAL_ONLY_hjb_archive": {
    "task_relative_path": "evidence\\LOCAL_ONLY_P4_true_arrays_and_rates.npz",
    "bytes": 106479,
    "sha256": "d66b8d8fe025067c5e41e35344b5c98180f4ba291f5b7763de7adbc7a1666180",
    "LOCAL_ONLY": true,
    "observed_new_point_not_historical_tinygrid": true
  },
  "MATLAB_RAW_LOCAL_VERIFICATION": "NOT_AVAILABLE",
  "firm_GE_IRF_outer_31province_data_calls": 0,
  "source_or_economic_parameter_changes": 0
}
```

Corresponding evidence/P4_claim.json binds the command and entry/supervisor/grid hashes. evidence/P4_iteration_trajectory.json records every completed iteration's scalar value changes and actual operator diagnostics. All raw/public stdout/stderr hashes,redaction and resource/call receipts are retained. KFE probability marginals,when actually computed,contain all20 signed bins,not a truncated display. A noncertified KFE moment is not a successful stationary estimate.
