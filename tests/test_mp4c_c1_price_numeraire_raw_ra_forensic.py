from __future__ import annotations

import ast
from pathlib import Path

import pytest

from validators.multi_province.c1_price_numeraire_raw_ra_forensic import build


ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "validators/multi_province/c1_price_numeraire_raw_ra_forensic/build.py"


def _row(*, turn: int = 25, province: str = "甲", index: int = 0, mt: float = 1.0,
         y_over_k: float = 0.3, corptau: float = 0.25) -> tuple[dict[str, object], dict[str, float]]:
    alpha, capital, pit = 0.7380939146868483, 100.0, 0.02
    output = y_over_k * capital
    rk = mt * alpha * y_over_k
    profit_over_y = max(1.0 - mt - build.THETA / 2.0 * pit**2, 0.0)
    after_tax_profit_over_k = profit_over_y * y_over_k * (1.0 - corptau)
    ra0 = rk - build.DELTA + after_tax_profit_over_k
    used = min(max(ra0, build.RAMIN), build.RAMAX)
    row = {
        "turn": turn, "province_index": index, "province": province,
        "firm_K_total_MU": capital, "Y": output, "alpha": alpha,
        "firm_rk": rk, "firm_ra0": ra0, "firm_ra_used": used,
        "ramin": build.RAMIN, "ramax": build.RAMAX,
        "firm_wage_raw": 12.0, "firm_wage_used": 1.3,
        "household_composite_wage": 18.0, "firm_Lt_supply": 10.0,
        "Ltarget_proxy_NU": 8.0,
    }
    return row, {"corptau": corptau, "pit": pit}


def test_recover_components_matches_source_identity_with_profit_floor() -> None:
    row, state = _row(mt=1.0, y_over_k=0.3)
    result = build.recover_components(row, state)
    assert result["mt_recovered"] == pytest.approx(1.0)
    assert result["profit_floor_binding"] is True
    assert result["profit_over_K"] == 0.0
    assert result["ra0_reconstructed"] == pytest.approx(row["firm_ra0"])
    assert result["raw_ra_classification"] == "UPPER"


def test_recover_components_matches_positive_profit_case() -> None:
    row, state = _row(mt=0.9, y_over_k=0.2)
    result = build.recover_components(row, state)
    assert result["profit_floor_binding"] is False
    assert result["profit_over_Y"] == pytest.approx(0.08)
    assert result["after_tax_profit_over_K"] == pytest.approx(0.012)
    assert result["ra0_reconstruction_error"] == pytest.approx(0.0)


def test_clipped_return_mismatch_fails_closed() -> None:
    row, state = _row()
    row["firm_ra_used"] = 0.05
    with pytest.raises(RuntimeError, match="clipped ra mismatch"):
        build.recover_components(row, state)


def test_return_geometry_separates_three_equations() -> None:
    row, state = _row(mt=0.9, y_over_k=0.2)
    component = build.recover_components(row, state)
    geometry = build.geometry_rows([component])
    assert len(geometry) == 2
    upper = next(item for item in geometry if item["return_level_name"] == "ramax")
    assert upper["K_over_Y_for_pure_MPK_equal_return"] != upper["K_over_Y_for_rk_minus_delta_equal_return"]
    assert upper["K_over_Y_for_full_ra0_equal_return"] > upper["K_over_Y_for_rk_minus_delta_equal_return"]
    assert "NOT_TARGET" in upper["geometry_status"]


def test_turn25_has_three_independent_descending_ranks() -> None:
    rows = []
    for index in range(31):
        row, state = _row(province=f"省{index}", index=index, y_over_k=0.1 + index / 100.0,
                          mt=0.9 + (30 - index) / 1000.0)
        rows.append(build.recover_components(row, state))
    ranked = build.rank_turn25(rows)
    assert [item["ra0_desc_rank"] for item in ranked] == list(range(1, 32))
    assert {item["Y_over_K_desc_rank"] for item in ranked} == set(range(1, 32))
    assert {item["profit_over_K_desc_rank"] for item in ranked} == set(range(1, 32))


def test_accepted_c1_manifest_reopens_without_mismatch() -> None:
    receipt = build.verify_accepted_manifest()
    assert receipt["original_candidate_readback_all_match"] is True
    assert receipt["current_checkout_core_inputs_byte_exact"] is True
    assert receipt["current_checkout_all_content_equivalent"] is True
    assert receipt["entries_checked"] == 22


def test_builder_imports_no_model_runtime_functions() -> None:
    tree = ast.parse(BUILDER.read_text(encoding="utf-8"))
    imported = [node for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))]
    source = "\n".join(ast.unparse(node) for node in imported)
    for forbidden in ("firm", "wage", "household", "hjb", "kfe", "migration", "steady_state"):
        assert forbidden not in source.lower()


def test_zero_science_ledger_is_literal_and_complete() -> None:
    source = BUILDER.read_text(encoding="utf-8")
    for field in (
        "hjb_calls", "kfe_calls", "household_calls", "migration_calls", "firm_runtime_calls",
        "wage_runtime_calls", "controller_runtime_calls", "outer_turn_calls", "trajectory_calls",
        "steady_state_calls", "matlab_runtime_calls", "root_or_brent_calls", "results_calls",
    ):
        assert f'"{field}": 0' in source
    assert '"parameter_changes": 0' in source
