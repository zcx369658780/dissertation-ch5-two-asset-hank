"""Static/synthetic gates for the 25-turn K/L diagnostic harness."""

from __future__ import annotations

from pathlib import Path

import pytest

from validators.multi_province.corrected_2018_25turn_kl import finalize, run


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


def test_science_marker_is_after_serialized_payload_validation() -> None:
    source = Path(run.__file__).read_text(encoding="utf-8")
    validation = source.index("single.validate_serialized_payload(payload)")
    marker = source.index('write_json(root / "science_started.json"')
    assert validation < marker


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
    assert run.VERDICT_PASS.endswith("LATE_WINDOW_KL_GAPS_QUANTIFIED")
    assert run.VERDICT_PARTIAL.endswith("EARLY_HARD_FAILURE_BEFORE_LATE_WINDOW")
    assert run.VERDICT_BLOCKED.endswith("RUNTIME_CONTRACT_OR_LEDGER_INCOMPLETE")


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
