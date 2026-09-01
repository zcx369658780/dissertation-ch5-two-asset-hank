from __future__ import annotations

import json
from pathlib import Path

import pytest

from validators.multi_province import mp4c_python_annual_empirical as driver


def _minimal_canonical(year: int) -> dict[str, object]:
    binding = driver.DecoupledAnnualIndex.for_calendar_year(year)
    scalars = {field: 1.0 for field in (
        "rb_gap", "rah", "ra", "nominal_rate", "rb", "rk", "wjt", "composite_wage",
        "transfer_income", "inflation", "wage_tax", "initial_at", "initial_bt", "initial_mt",
        "initial_ct", "corporate_tax",
    )}
    vectors = {name: [1.0] * 31 for name in (
        "pop", "ind_alpha", "initialized_zt", "cap", "gdp", "gov_inv",
        "inter_province_asset_ratio",
    )}
    return {
        "binding": {key: getattr(binding, key) for key in (
            "analysis_index", "calendar_year", "data_mat_index", "output_filename_year",
            "regression_vintage_key", "workbook_data_row_index",
        )},
        "regression_sheet": f"总面板回归系数_{binding.regression_vintage_key}_行业4",
        "source_hashes": driver.SOURCE_HASHES,
        "province_order": [f"p{index}" for index in range(31)],
        "scalars": scalars,
        "vectors": vectors,
    }


@pytest.mark.parametrize("year,analysis,row,vintage", [(2010, 2, 11, 11), (2011, 3, 12, 12)])
def test_load_entry_state_preserves_decoupled_annual_binding(
    tmp_path: Path, year: int, analysis: int, row: int, vintage: int,
) -> None:
    payload = _minimal_canonical(year)
    path = tmp_path / f"calendar_{year}.json"
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    canonical, states = driver.load_entry_state(path)
    assert canonical["binding"]["analysis_index"] == analysis
    assert canonical["binding"]["workbook_data_row_index"] == row
    assert canonical["binding"]["data_mat_index"] == analysis
    assert canonical["binding"]["regression_vintage_key"] == vintage
    assert len(states) == 31


def test_load_entry_state_rejects_recoupled_binding(tmp_path: Path) -> None:
    payload = _minimal_canonical(2010)
    payload["binding"]["workbook_data_row_index"] = 2
    path = tmp_path / "bad.json"
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    with pytest.raises(ValueError, match="binding mismatch"):
        driver.load_entry_state(path)


def test_scientific_authority_and_ceiling_are_finite_and_narrow() -> None:
    assert driver.AUTHORIZED_SCIENTIFIC_YEARS == (2010, 2011)
    assert driver.MAX_OUTER_TURNS == 250
    assert driver.MAX_HOUSEHOLD_CALLS == 31 * driver.MAX_OUTER_TURNS
    assert driver.WALL_CLOCK_LIMIT_SECONDS == 14400
    assert driver.anchor.CANONICAL_SHA == driver.ACCEPTED_2009_CANONICAL_SHA


def test_accepted_driver_is_reused_without_mutation() -> None:
    assert driver.anchor._sha256(driver.anchor.ORACLE_PATH) == driver.anchor.ORACLE_SHA
    assert driver.anchor.BOOTSTRAP_IDENTITY["scientific_model_calls"] == 0
