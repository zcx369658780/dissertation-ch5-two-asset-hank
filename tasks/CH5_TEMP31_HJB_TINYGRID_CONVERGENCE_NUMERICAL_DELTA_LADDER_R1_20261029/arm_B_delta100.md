# Arm B: delta=100.0

STATUS=NOT_CONVERGED_FINITE; NOT_EXECUTED=FALSE
Transition authority: previous arm reached80 finite iterations without convergence or solver errors. Real exit0, elapsed1.390000s, timeoutFalse. One real initializer,8 roots/brentq, one corrected HJB driver,80 actual loop entries,640 internal policy calls,81 source operator assemblies,80 real spsolve calls. Parameters and initial-array hashes match the frozen common baseline. No previous arm terminal value was supplied.

Final source flagFalse; deltaV=0.01607907986119894; stale residual=0.00016079079861245488. Every audited return field is finite. Full diagnostic record:
```json
{
  "event": "arm_result",
  "arm": "B",
  "delta": 100.0,
  "max_iterations": 80,
  "outcome": "NOT_CONVERGED_FINITE",
  "result_converged": false,
  "actual_iterations": 80,
  "last_value_change": 0.01607907986119894,
  "finite_return_arrays": {
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
  "operator": {
    "shape": [
      8,
      8
    ],
    "nnz": 24,
    "density": 0.375,
    "max_row_sum": 5.551115123125783e-17,
    "row_sum_abs_max": 0.00045691399330394233,
    "min_offdiagonal_including_implicit_zeros": -0.081,
    "finite": true,
    "returned_last_policy_operator_equals_captured_iteration_operator": true
  },
  "implicit_audit": {
    "stale_policy_residual_sup": 0.00016079079861245488,
    "last_step_change_over_delta": 0.00016079079861198943,
    "residual_vector_implicit_identity_error_sup": 5.084840426321235e-16,
    "stale_norm_step_norm_difference": 4.654479926480271e-16,
    "captured_linear_equation_residual_sup": 4.85722573273506e-16,
    "captured_matrix_vs_expected_error_sup": 0.0,
    "captured_rhs_vs_expected_error_sup": 0.0,
    "frozen_rounding_bound": 1.1139815686914166e-10,
    "full_nonlinear_Bellman_optimality_residual": "NOT_EVALUATED_NO_POLICY_REOPTIMIZATION"
  },
  "implicit_consistent": true,
  "oscillation_growth": {
    "negative_successive_update_cosines": 38,
    "growth_ratio_above_one_count": 35,
    "max_growth_ratio": 23.15105041414698,
    "interpretation": "observable update oscillation/growth indicators only; not a nonlinear optimality test"
  },
  "source_operator_scientific_risks": [
    "source operator row sums depart from zero; generator/scientific risk, no operator repair",
    "source operator has negative offdiagonal; generator/scientific risk, no operator repair"
  ],
  "warnings": [],
  "original_initialization_hashes": {
    "value_F_float64_sha256": "c649277b2fee82d18a05772a74a0e1ed1daf096fca202b099913b58814b15289",
    "labor_F_float64_sha256": "5e949ee3990545189c8c690a6c247edee3dfa82f20e5e8d180bc41707c99bd5e"
  },
  "observed_counts": {
    "initializer_batches": 1,
    "root_cells": 8,
    "brentq_calls": 8,
    "hjb_driver_calls": 1,
    "hjb_iteration_entries": 80,
    "hjb_policy_cells": 640,
    "operator_assemblies": 81,
    "linear_solves": 80
  },
  "source_commit": "ffdb7fcd41019bed7ce4652ee01c753bff6fcec8",
  "Fortran_order": true,
  "KFE_GE_IRF": 0,
  "outer_steady_state_turns": 0,
  "empirical_data_reads": 0
}
```

The80-row original scalar trajectory is evidence/arm_B_trajectory.json and the raw/public stdout contains actual traced iteration observations. DeltaV range in this arm: min0.005318458710180662, max0.5111367036231265. Negative successive-update cosines/growth ratios are descriptive oscillation indicators, not proof of eventual impossibility. No hidden rerun or new policy residual evaluation occurred.
