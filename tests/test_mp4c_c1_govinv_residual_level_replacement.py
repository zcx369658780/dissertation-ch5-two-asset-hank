"""Zero-science gates for C1 residual public-asset level replacement."""

from __future__ import annotations

import csv
import hashlib
import inspect
import json
from pathlib import Path

import numpy as np
import pytest

from ch5_two_asset_hank.multi_province.government_assets import (
    CAPITAL_UNIT,
    RESIDUAL_PUBLIC_ASSET_POSITIVE,
    RESIDUAL_PUBLIC_ASSET_ZERO_PRIVATE_AT_OR_ABOVE_TARGET,
    residual_government_asset_level,
    residual_government_asset_levels,
)
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER


REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / "reports/mp4c_c1_govinv_residual_level_replacement_20260911"
REPORT = REPO / "docs/CH5_MP4C_C1_GOVINV_RESIDUAL_LEVEL_REPLACEMENT_IMPLEMENTATION_REPORT.md"
HELPER = REPO / "src/ch5_two_asset_hank/multi_province/government_assets.py"
LEGACY_C0 = REPO / "src/ch5_two_asset_hank/multi_province/steady_state.py"
LEGACY_C0_SHA256 = "B8897FDEF9CC59A2811561A18CB0FADF059A158AD8E5F3661BD10A5734D264AA"


def csv_rows(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert rows and all(None not in row for row in rows)
    return rows


def test_zero_private_makes_public_asset_equal_target() -> None:
    result = residual_government_asset_level(Ktarget_MU=100.0, Kprivate_current_MU=0.0)
    assert result.GovInv_residual_MU == 100.0
    assert result.firm_K_accounting_MU == 100.0
    assert result.firm_K_over_target == 1.0
    assert result.status == RESIDUAL_PUBLIC_ASSET_POSITIVE


def test_interior_private_capital_closes_exactly() -> None:
    result = residual_government_asset_level(Ktarget_MU=100.0, Kprivate_current_MU=37.0)
    assert result.GovInv_residual_MU == 63.0
    assert result.firm_K_accounting_MU == result.Ktarget_MU
    assert result.capital_gap_before_MU == 63.0
    assert result.capital_gap_after_MU == 0.0
    assert not result.residual_floor_binding


def test_private_equal_target_binds_zero_floor() -> None:
    result = residual_government_asset_level(Ktarget_MU=100.0, Kprivate_current_MU=100.0)
    assert result.GovInv_residual_MU == 0.0
    assert result.firm_K_accounting_MU == 100.0
    assert result.private_at_or_above_target
    assert result.residual_floor_binding
    assert result.status == RESIDUAL_PUBLIC_ASSET_ZERO_PRIVATE_AT_OR_ABOVE_TARGET


def test_private_overshoot_is_preserved() -> None:
    result = residual_government_asset_level(Ktarget_MU=100.0, Kprivate_current_MU=140.0)
    assert result.GovInv_residual_MU == 0.0
    assert result.firm_K_accounting_MU == 140.0
    assert result.firm_K_over_target == 1.4
    assert result.capital_gap_after_MU == -40.0
    assert result.private_at_or_above_target


def test_vectorized_31_province_contract_preserves_axis_shape_and_units() -> None:
    target = np.linspace(100.0, 400.0, 31)
    private = target * np.linspace(0.0, 1.5, 31)
    result = residual_government_asset_levels(
        Ktarget_MU=target,
        Kprivate_current_MU=private,
        province_order=PROVINCE_ORDER,
    )
    assert result.province_order == PROVINCE_ORDER
    assert result.capital_unit == CAPITAL_UNIT
    for value in (
        result.Ktarget_MU,
        result.Kprivate_current_MU,
        result.GovInv_residual_MU,
        result.firm_K_accounting_MU,
        result.firm_K_over_target,
        result.private_at_or_above_target,
        result.residual_floor_binding,
        result.capital_gap_before_MU,
        result.capital_gap_after_MU,
    ):
        assert value.shape == (31,)
        assert not value.flags.writeable
    np.testing.assert_array_equal(result.firm_K_accounting_MU, np.maximum(target, private))


@pytest.mark.parametrize(
    ("target", "private"),
    [(0.0, 0.0), (-1.0, 0.0), (np.nan, 0.0), (np.inf, 0.0), (1.0, -1.0), (1.0, np.nan), (1.0, np.inf)],
)
def test_invalid_scalar_inputs_fail_closed(target: float, private: float) -> None:
    with pytest.raises(ValueError):
        residual_government_asset_level(Ktarget_MU=target, Kprivate_current_MU=private)


def test_vector_shape_and_province_order_mismatch_fail_closed() -> None:
    valid = np.ones(31)
    with pytest.raises(ValueError, match="shape"):
        residual_government_asset_levels(
            Ktarget_MU=valid,
            Kprivate_current_MU=np.ones(30),
            province_order=PROVINCE_ORDER,
        )
    wrong_order = tuple(reversed(PROVINCE_ORDER))
    with pytest.raises(ValueError, match="province_order"):
        residual_government_asset_levels(
            Ktarget_MU=valid,
            Kprivate_current_MU=valid,
            province_order=wrong_order,
        )


def test_helper_has_no_tuning_or_return_target_interface() -> None:
    text = HELPER.read_text(encoding="utf-8")
    for forbidden in ("lambda_K", "ra_target", "damping", "hysteresis"):
        assert forbidden not in text
    signature = inspect.signature(residual_government_asset_level)
    assert tuple(signature.parameters) == ("Ktarget_MU", "Kprivate_current_MU")


def test_historical_c0_source_is_byte_identical_to_accepted_baseline() -> None:
    assert hashlib.sha256(LEGACY_C0.read_bytes()).hexdigest().upper() == LEGACY_C0_SHA256


def test_static_replay_covers_all_rows_and_uses_residual_labels() -> None:
    rows = csv_rows("static_g1_replay.csv")
    assert len(rows) == 775
    assert {row["c1_status"] for row in rows} <= {
        RESIDUAL_PUBLIC_ASSET_POSITIVE,
        RESIDUAL_PUBLIC_ASSET_ZERO_PRIVATE_AT_OR_ABOVE_TARGET,
    }
    assert all(row["c1_firm_K_accounting_over_target"] == "1.0" for row in rows)


def test_summary_reports_requested_windows_and_late_counterfactual() -> None:
    payload = json.loads((ROOT / "static_replay_summary.json").read_text(encoding="utf-8"))
    expected = {
        "ALL_TURNS_01_25", "TURNS_01_05", "TURNS_06_10", "TURNS_11_15",
        "TURNS_16_20", "TURNS_21_25", "LATE_TURNS_20_25",
    }
    assert {row["window"] for row in payload["windows"]} == expected
    all_rows = next(row for row in payload["windows"] if row["window"] == "ALL_TURNS_01_25")
    late = next(row for row in payload["windows"] if row["window"] == "LATE_TURNS_20_25")
    assert all_rows["observations"] == 775
    assert all_rows["c1_exact_target_rows"] == 775
    assert all_rows["private_at_or_above_target_rows"] == 0
    assert late["observations"] == 186
    assert late["c1_total_K_over_target"]["median"] == 1.0
    assert late["remaining_private_only_overshoot_MU"]["sum"] == 0.0


def test_zero_scientific_call_ledger_is_strictly_zero() -> None:
    payload = json.loads((ROOT / "zero_scientific_call_ledger.json").read_text(encoding="utf-8"))
    counters = {key: value for key, value in payload.items() if key.endswith("_calls") or key == "scientific_model_state_advances"}
    assert counters and all(value == 0 for value in counters.values())
    assert payload["results_eligibility"] is False


def test_report_has_pass_verdict_and_stops_before_runtime_integration() -> None:
    text = REPORT.read_text(encoding="utf-8")
    assert "C1_GOVINV_RESIDUAL_LEVEL_REPLACEMENT_PASS__PURE_PUBLIC_ASSET_RESIDUAL_IMPLEMENTED_AND_STATICALLY_VALIDATED" in text
    for number in range(1, 6):
        assert f"{number}. **" in text
    assert "not connected to the active steady-state runtime" in text
    assert "Results eligibility=FALSE" in text
