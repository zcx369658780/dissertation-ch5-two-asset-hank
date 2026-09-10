"""Static/synthetic gates for the 25-turn K/L diagnostic harness."""

from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest
from scipy import sparse

from validators.multi_province.corrected_2018_hjb_propagation_25turn_kl import finalize, run


def synthetic_hjb(*, converged: bool, nonfinite_field: str | None = None,
                  operator_shape: tuple[int, int] = (800, 800)) -> SimpleNamespace:
    arrays = {field: np.ones((20, 20, 2), dtype=float) for field in run.HJB_NUMERIC_ARRAY_FIELDS}
    if nonfinite_field is not None:
        arrays[nonfinite_field][0, 0, 0] = np.nan
    operator = SimpleNamespace(full=sparse.eye(*operator_shape, format="csr"))
    return SimpleNamespace(**arrays, operator=operator, post_convergence_operator=operator,
        iterations=100 if not converged else 3, converged=converged,
        convergence_statistic=0.2 if not converged else 1e-8)


def synthetic_household_output(converged: bool) -> dict[str, object]:
    return {"C": 1.0, "L": 1.0, "A": 1.0, "B": 1.0, "AtTax": 0.0,
        "hjb_converged": converged, "hjb_iterations": 100 if not converged else 3,
        "hjb_statistic": 0.2 if not converged else 1e-8,
        "hjb_acceptance_classification": (
            "HJB_CONVERGED" if converged else "HJB_NONCONVERGED_DIAGNOSTIC_ONLY"),
        "downstream_kfe_attempted": True, "downstream_kfe_returned": True,
        "continuation_status": "CONTINUED_TO_HOUSEHOLD_BATCH"}


def synthetic_kfe(*, density_shape: tuple[int, ...] = (20, 20, 2)) -> SimpleNamespace:
    matrix = sparse.eye(800, format="csr")
    return SimpleNamespace(density=np.ones(density_shape), density_vector=np.ones(800),
        rhs=np.ones(800), raw_solve_vector=np.ones(800), original_operator=matrix,
        transpose=matrix, contaminated_matrix=matrix, normalization_factor=1.0,
        db=1.0, da=1.0, cell_weight=1.0, raw_residual_inf=0.0)


def test_finite_nonconverged_hjb_is_diagnostic_and_does_not_abort() -> None:
    assert run.validate_hjb_return_for_continuation(synthetic_hjb(converged=False)) == (
        "HJB_NONCONVERGED_DIAGNOSTIC_ONLY")


def test_false_hjb_flag_is_preserved_and_blocks_final_source_predicate() -> None:
    outputs = [synthetic_household_output(True) for _ in range(31)]
    outputs[11] = synthetic_household_output(False)
    batch = run.build_household_batch(outputs)
    assert batch.converged[11] is False
    assert sum(batch.converged) == 30
    assert run.all_household_hjb_converged(batch) is False


def test_nonfinite_hjb_output_fails_closed() -> None:
    with pytest.raises(ValueError, match="nonfinite"):
        run.validate_hjb_return_for_continuation(
            synthetic_hjb(converged=False, nonfinite_field="consumption"))


def test_unusable_hjb_operator_and_malformed_kfe_fail_closed() -> None:
    with pytest.raises(ValueError, match="operator shape"):
        run.validate_hjb_return_for_continuation(
            synthetic_hjb(converged=False, operator_shape=(799, 799)))
    with pytest.raises(ValueError, match="density shape"):
        run.validate_kfe_return_for_continuation(synthetic_kfe(density_shape=(799,)))


def synthetic_rows() -> list[dict[str, object]]:
    rows = []
    for index in range(31):
        total_ratio = 1.0 + index / 100.0
        rows.append({
            "province": f"p{index}", "firm_ra0": 0.05, "ramin": 0.02, "ramax": 0.09,
            "firm_wage_raw": 1.0, "wjtmin": 0.8, "wjtmax": 1.3,
            "household_rah": 0.05, "nk_gap": 0.01, "yt_gap": 0.02,
            "GDP_level_gap": 0.03, "hjb_iterations": 3, "hjb_converged": True,
            "kfe_returned": True, "kfe_diagnostic_status": "DIAGNOSTIC_ONLY",
            "kfe_source_free_residual_inf": 1e-3,
            "kfe_source_free_normwise_ratio": 1e-4,
            "A": 2.0, "B": 1.0, "A_plus_B": 3.0,
            "Ktarget_2018_MU": 100.0, "Kt_supply_private_MU": total_ratio * 10.0,
            "GovInv_before_MU": total_ratio * 90.0, "GovInv_after_MU": total_ratio * 81.0,
            "firm_K_total_MU": total_ratio * 100.0,
            "firm_K_total_over_Ktarget": total_ratio,
            "private_K_over_Ktarget": total_ratio * 0.1,
            "GovInv_before_over_Ktarget": total_ratio * 0.9,
            "GovInv_after_over_Ktarget": total_ratio * 0.81,
            "Ltarget_proxy_NU": 100.0, "firm_Lt_supply": 90.0 + index,
            "firm_Lt_over_population_proxy": (90.0 + index) / 100.0,
        })
    return rows


def test_harness_has_exact_one_trajectory_and_25_turn_ceiling() -> None:
    source = Path(run.__file__).read_text(encoding="utf-8")
    assert "for turn_index in range(1, 26):" in source
    assert '"authorized_trajectory_count": 1' in source
    assert '"authorized_turns_maximum": 25' in source
    assert '"authorized_province_household_updates_maximum": 775' in source
    assert "compare_predecessor" not in source
    assert "accepted_three_turn" not in source
    assert 'raise RuntimeError("HJB did not converge")' not in source
    assert "validate_hjb_return_for_continuation(hjb)" in source


def test_science_marker_is_after_serialized_payload_validation() -> None:
    source = Path(run.__file__).read_text(encoding="utf-8")
    phase_gate = source.index("_require_phase_a_receipt(root)", source.index("def execute"))
    validation = source.index("single.validate_serialized_payload(payload)")
    marker = source.index('write_json(root / "science_started.json"')
    assert phase_gate < validation < marker


def test_national_summary_records_required_k_l_accounting() -> None:
    rows = synthetic_rows()
    controller = {
        "adaptation_allowed": True,
        "actions": [{"zt_adjusted": False, "govinv_action": "LOW_RA_DECREASE_0P9"}] * 31,
        "labor_row_sum_identity_max_abs_gap": 0.0,
        "labor_national_matrix_vs_destination_sum_abs_gap": 0.0,
    }
    result = run.national_summary(20, rows, controller)
    assert result["turn"] == 20
    assert result["firm_K_total_over_Ktarget"]["min"] == 1.0
    assert result["firm_K_ratio_counts"]["above_1p25"] == 5
    assert result["labor_ratio_outside_0p8_1p2_count"] == 0
    assert result["national_sums"]["firm_K_total_MU"] == pytest.approx(
        result["national_sums"]["Kt_supply_private_MU"]
        + result["national_sums"]["GovInv_before_MU"])


def test_allowed_verdicts_are_exact() -> None:
    assert run.VERDICT_PASS == "HJB_PROPAGATION_REPAIR_AND_25TURN_KL_PASS__LATE_WINDOW_RECONCILIATION_COMPLETE"
    assert run.VERDICT_PARTIAL == "HJB_PROPAGATION_REPAIR_PASS__25TURN_KL_PARTIAL_TRUE_HARD_FAILURE_BEFORE_LATE_WINDOW"
    assert run.VERDICT_BLOCKED == "HJB_PROPAGATION_REPAIR_BLOCKED__SOURCE_STYLE_CONTINUATION_NOT_IMPLEMENTABLE_WITH_CURRENT_RETURN_OBJECTS"


def test_late_window_classification_is_threshold_exact() -> None:
    assert finalize.classify("K", 1.1) == "K_NEAR_TARGET"
    assert finalize.classify("K", 1.1000001) == "K_MODERATELY_HIGH"
    assert finalize.classify("K", 1.5) == "K_MODERATELY_HIGH"
    assert finalize.classify("K", 1.5000001) == "K_SEVERELY_HIGH"
    assert finalize.classify("K", 0.9) == "K_NEAR_TARGET"
    assert finalize.classify("K", 0.5) == "K_MODERATELY_LOW"
    assert finalize.classify("K", 0.499999) == "K_SEVERELY_LOW"


def test_no_completed_turns_produce_no_late_window_claim() -> None:
    assert finalize.late_window([]) == []
