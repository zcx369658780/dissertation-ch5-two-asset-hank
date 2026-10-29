# P2: KFE_NOT_CERTIFIED

Exactly one supervised command; exit0,elapsed11.281000s,timeoutFalse. The original point inputs and complete scalar result are below. Model calls are actual code-object observations, not inferred budgets. No warm start,clipping,source change or extra solve.

```json
{
  "event": "point_result",
  "point": "P2",
  "prices": {
    "id": "P2",
    "rah": 0.05,
    "rb": 0.02,
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
    "point": "P2",
    "requested_effective_wage": 19.0,
    "actual_source_effective_wage": 19.0,
    "wage_error": 0.0,
    "context_id": "TEMP31_MATLAB800_SYNTHETIC_PRICE_PILOT_20261029_P2",
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
    "value_min": -2.2796310570573266,
    "value_max": -1.4773663703160558,
    "labor_min": 0.6301433055220917,
    "labor_max": 0.6793689907027272,
    "finite": true,
    "value_F_float64_sha256": "445c6cb5a20dfe19b4353856ed42ce5c63b6827002b078ca6b91574bc0e3c83f",
    "labor_F_float64_sha256": "27afc18ba634c0188b9eb9eb7eb85b103a875b8c0186585b936137e7d87db339",
    "fresh_for_point": "P2",
    "warm_start": false
  },
  "HJB": {
    "converged": true,
    "iterations": 22,
    "convergence_statistic": 6.868061674936143e-11,
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
      "nnz": 4032,
      "finite": true,
      "row_sum_abs_max": 0.0026797228997116895,
      "max_signed_row_sum": 3.3861802251067274e-15,
      "min_offdiagonal_including_implicit_zeros": -2.8177223635567863,
      "csr_sha256": "dc3aa38739229d9bb85583bc21e361045e18f938754fe9381e299be96d7ac923"
    },
    "post_convergence_operator": {
      "shape": [
        800,
        800
      ],
      "nnz": 3139,
      "finite": true,
      "row_sum_abs_max": 2.81989295896252,
      "max_signed_row_sum": 1.1657341758564144e-15,
      "min_offdiagonal_including_implicit_zeros": 0.0,
      "csr_sha256": "9c08c6375db03b4da4e395f2f2055852f045946d73457d7d44fc9247a508442e"
    },
    "max_observed_iteration_row_sum_abs": 0.0026797228997118006,
    "MATLAB_homecrit": 0.01,
    "observed_homecrit_violation": false,
    "homecrit_guard_internal": "ABSENT_UNCHANGED_EXTERNAL_READONLY_OBSERVATION",
    "source_parity": "PARITY_UNCERTIFIED_RAW_MATLAB_NOT_LOCALLY_VERIFIED",
    "stale_last_policy_residual": 7.939482404850651e-14,
    "implicit_identity_error": 1.8469004103849327e-14,
    "full_nonlinear_Bellman_residual": "NOT_EVALUATED",
    "warnings": []
  },
  "KFE": {
    "status": "KFE_NOT_CERTIFIED",
    "At": 5.0722995536457365,
    "Bt": 1.8147088284647883,
    "Lt": 0.654140959372768,
    "Ct": 12.662694105957085,
    "a_mass20": [
      0.05389567218397699,
      0.005911239260122004,
      0.010787907929031976,
      0.01770573853697303,
      0.026455567821289418,
      0.03680417211731372,
      0.048171926242478035,
      0.05999498732400711,
      0.07160929893823889,
      0.08297364494863003,
      0.09112446296420555,
      0.0947839180060336,
      0.09830295862800563,
      0.11644390641124343,
      0.18450491035784702,
      0.0005296883306036243,
      0.0,
      0.0,
      0.0,
      0.0
    ],
    "b_mass20": [
      0.0496207419991515,
      0.09286958611662856,
      0.04651592449663138,
      0.04493553072097982,
      0.04503360578397046,
      0.04441196423565691,
      0.040892680368989964,
      0.03784977605640843,
      0.03627854174085846,
      0.03538144850008494,
      0.03484766009001982,
      0.034529876343658616,
      0.03434944916237907,
      0.034260669717764904,
      0.034235646455307925,
      0.03425629177210006,
      0.02385658219495632,
      0.023459801807371568,
      0.023081415426769204,
      0.2493328070103121
    ],
    "total_probability": 1.0000000000000002,
    "negative_probability_mass": 0.0,
    "negative_density_cells": 0,
    "density_min": 0.0,
    "density_max": 0.1578029953767361,
    "a_lower_mass": 0.05389567218397699,
    "a_upper_mass": 0.0,
    "a_internal_mass": 0.9461043278160232,
    "b_lower_mass": 0.0496207419991515,
    "b_upper_mass": 0.2493328070103121,
    "b_internal_mass": 0.7010464509905365,
    "a_mode_indices0": [
      14
    ],
    "a_mode_asset_positions": [
      7.368421052631579
    ],
    "At_distance_from_lower": 5.0722995536457365,
    "At_distance_from_upper": 4.9277004463542635,
    "stationary_residual": 0.3255716333674026,
    "contaminated_raw_system_residual": 1.3064636178450328e-17,
    "source_raw_residual_inf": 1.3064636178450328e-17,
    "contaminated_row_index0": 295,
    "rhs_at_contaminated_row": 0.007,
    "normalization_factor": 0.11570771109142623,
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
      "task_relative_path": "evidence\\LOCAL_ONLY_P2_true_KFE_density.npz",
      "bytes": 10882,
      "sha256": "a6fadbdddf0d6e72575e33055ba5effef49abe150beadcc8235676fdf9fe500b"
    }
  },
  "observed_counts": {
    "initializer_calls": 1,
    "root_cells": 800,
    "brentq_calls": 800,
    "hjb_calls": 1,
    "hjb_iterations": 22,
    "hjb_policy_cells": 17600,
    "operator_assemblies": 23,
    "hjb_linear_solves": 22,
    "kfe_calls": 1,
    "kfe_linear_solves": 1,
    "kfe_contaminated_row_index_calls": 1
  },
  "LOCAL_ONLY_hjb_archive": {
    "task_relative_path": "evidence\\LOCAL_ONLY_P2_true_arrays_and_rates.npz",
    "bytes": 108106,
    "sha256": "6120c236ce2bb9cf051446e75bc7d5f246832cd4a12dddb14f9275540d8df4ca",
    "LOCAL_ONLY": true,
    "observed_new_point_not_historical_tinygrid": true
  },
  "MATLAB_RAW_LOCAL_VERIFICATION": "NOT_AVAILABLE",
  "firm_GE_IRF_outer_31province_data_calls": 0,
  "source_or_economic_parameter_changes": 0
}
```

Corresponding evidence/P2_claim.json binds the command and entry/supervisor/grid hashes. evidence/P2_iteration_trajectory.json records every completed iteration's scalar value changes and actual operator diagnostics. All raw/public stdout/stderr hashes,redaction and resource/call receipts are retained. KFE probability marginals,when actually computed,contain all20 signed bins,not a truncated display. A noncertified KFE moment is not a successful stationary estimate.
