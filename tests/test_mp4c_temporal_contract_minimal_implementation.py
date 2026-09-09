from __future__ import annotations

import copy
import inspect
import json
from pathlib import Path

import numpy as np
import pytest

from ch5_two_asset_hank.multi_province import annual
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER


SOURCE_HASHES = {
    "2000年后各省数据_填充NA.xlsx": "C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929",
    "R语言估计结果_plm估计.xlsx": "A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68",
    "中国各省省会地理距离矩阵.xlsx": "26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566",
}
MATLAB_HASHES = {
    "multi_prov_HANK_12sts.m": "3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97",
    "load_GDPdata.m": "DECA8AF3F22097550B8957FE848989E6342619CB9929A1C00076E020549366C5",
    "mpHANK_equilibrium_2000.m": "26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5",
}


def _scalars() -> annual.AnnualSourceScalars:
    return annual.AnnualSourceScalars(
        1000, 100, .096, 1, 1, .5, .07, .09, .09, .02, .02, .1,
        .6, 20, .1, .02, .05, 2, 1, .9, 4, .25,
    )


def _synthetic_loader(path: Path, sheet: str) -> dict[int, dict[int, object]]:
    if sheet == "geom":
        rows = {1: {column + 2: label for column, label in enumerate(PROVINCE_ORDER)}}
        for row, label in enumerate(PROVINCE_ORDER, start=2):
            rows[row] = {1: label}
            for column in range(2, 33):
                rows[row][column] = float(abs((row - 2) - (column - 2)))
        return rows
    if sheet in {"GDP", "总资本存量", "常住人口"}:
        base = {"GDP": 1000.0, "总资本存量": 5000.0, "常住人口": 100.0}[sheet]
        rows = {1: {column + 3: label for column, label in enumerate(PROVINCE_ORDER)}}
        for physical_row, year in enumerate(range(2000, 2024), start=2):
            rows[physical_row] = {1: f"{year}年"}
            for column in range(3, 34):
                rows[physical_row][column] = base + 10 * (year - 2000) + column
        return rows
    if sheet.startswith("总面板回归系数_"):
        vintage = int(sheet.split("_")[1])
        return {1: {1: 0.0}, 2: {1: .5 + vintage / 100}}
    raise KeyError(sheet)


def _canonical(monkeypatch: pytest.MonkeyPatch, tmp_path: Path, year: int):
    paths = [tmp_path / name for name in SOURCE_HASHES]
    for path in paths:
        path.write_bytes(b"synthetic")
    monkeypatch.setattr(annual, "_xlsx_sheet_rows", _synthetic_loader)
    monkeypatch.setattr(annual, "_sha256", lambda path: SOURCE_HASHES[Path(path).name])
    sources = annual.PrimaryAnnualSourceFiles(
        paths[0], paths[1], paths[2], *SOURCE_HASHES.values()
    )
    return annual.load_primary_annual_input(
        sources=sources,
        binding=annual.DecoupledAnnualIndex.for_calendar_year(year),
        scalars=_scalars(),
    )


def test_all_fifteen_years_obey_index_row_vintage_and_rolling_window_contract() -> None:
    bindings = [annual.DecoupledAnnualIndex.for_calendar_year(year) for year in range(2009, 2024)]
    assert [item.analysis_index for item in bindings] == list(range(1, 16))
    assert [item.workbook_data_row_index for item in bindings] == list(range(10, 25))
    assert [item.data_mat_index for item in bindings] == list(range(1, 16))
    assert [item.regression_vintage_key for item in bindings] == list(range(10, 25))
    assert [(item.plm_sample_start_year, item.plm_sample_end_year) for item in bindings] == [
        (year - 9, year) for year in range(2009, 2024)
    ]
    assert all(item.plm_sample_length == 10 and item.plm_window_type == "ROLLING_10_YEAR"
               for item in bindings)


@pytest.mark.parametrize("year,row,vintage,start", [(2009, 10, 10, 2000), (2018, 19, 19, 2009), (2023, 24, 24, 2014)])
def test_key_year_contracts_use_same_year_zt(year: int, row: int, vintage: int, start: int) -> None:
    binding = annual.DecoupledAnnualIndex.for_calendar_year(year)
    metadata = binding.temporal_metadata()
    assert metadata["steady_year"] == metadata["level_calendar_year"] == year
    assert metadata["zt_source_calendar_year"] == year
    assert metadata["zt_source_data_row_index"] == row
    assert metadata["plm_vintage_key"] == vintage
    assert metadata["plm_sample_start_year"] == start


def test_2020_row21_is_natural_same_year_case() -> None:
    metadata = annual.DecoupledAnnualIndex.for_calendar_year(2020).temporal_metadata()
    assert metadata["workbook_data_row_index"] == 21
    assert metadata["zt_source_calendar_year"] == 2020
    assert "fixed" not in json.dumps(metadata).lower()


def test_synthetic_2018_loader_uses_row19_vintage19_and_same_year_zt(monkeypatch, tmp_path) -> None:
    canonical = _canonical(monkeypatch, tmp_path, 2018)
    assert canonical.regression_sheet == "总面板回归系数_19_行业4"
    assert canonical.zt_source_data_row_index == 19
    assert canonical.zt_source_calendar_year == 2018
    assert np.array_equal(
        canonical.ind_zt,
        canonical.gdp * canonical.cap ** (-canonical.ind_alpha) * canonical.pop ** (canonical.ind_alpha - 1),
    )
    assert PROVINCE_ORDER[11] == "安徽"


def test_payload_contains_complete_v2_metadata_and_roundtrips(monkeypatch, tmp_path) -> None:
    canonical = _canonical(monkeypatch, tmp_path, 2018)
    payload = canonical.canonical_payload()
    assert payload["temporal_contract"] == canonical.binding.temporal_metadata()
    assert payload["plm_workbook_sha256"] == SOURCE_HASHES["R语言估计结果_plm估计.xlsx"]
    assert payload["output_identity"] == {
        "name": annual.ANNUAL_PREMODEL_OUTPUT_IDENTITY,
        "version": annual.ANNUAL_PREMODEL_OUTPUT_VERSION,
    }
    assert annual.validate_corrected_annual_payload(
        json.loads(canonical.canonical_bytes()), expected_source_hashes=SOURCE_HASHES
    ) == canonical.binding


@pytest.mark.parametrize("mutation,match", [
    (lambda p: p.pop("temporal_contract"), "temporal contract"),
    (lambda p: p.update(schema="CH5_MP4A2_CANONICAL_ANNUAL_INPUT_V1"), "legacy"),
    (lambda p: p["temporal_contract"].update(level_calendar_year=2009), "temporal contract"),
    (lambda p: p["source_hashes"].update({"R语言估计结果_plm估计.xlsx": "0" * 64}), "source hash"),
])
def test_missing_legacy_inconsistent_or_wrong_hash_metadata_is_rejected(monkeypatch, tmp_path, mutation, match) -> None:
    payload = _canonical(monkeypatch, tmp_path, 2018).canonical_payload()
    mutation(payload)
    with pytest.raises(ValueError, match=match):
        annual.validate_corrected_annual_payload(payload, expected_source_hashes=SOURCE_HASHES)


def test_dynamic_artifact_name_and_no_overwrite(monkeypatch, tmp_path) -> None:
    canonical = _canonical(monkeypatch, tmp_path, 2018)
    path = annual.write_canonical_artifact(canonical, tmp_path / "fresh")
    assert path.name == "calendar_2018_primary_premodel_input.json"
    with pytest.raises(FileExistsError):
        annual.write_canonical_artifact(canonical, tmp_path / "fresh")


def test_stale_cache_alpha_is_evidence_only() -> None:
    old_cache_alpha = 0.967775174774325
    current_workbook_alpha = 1.0219847778591
    assert old_cache_alpha != current_workbook_alpha
    source = inspect.getsource(annual.load_primary_annual_input)
    assert "regression_rows" in source and "numeric[-1]" in source
    assert "cache" not in source.lower()


def test_annual_input_module_has_no_scientific_solver_import_or_call() -> None:
    source = inspect.getsource(annual)
    forbidden = ("solve_household", "run_online_stationary", "brentq", "spsolve", "eig")
    assert all(token not in source for token in forbidden)


def test_protected_matlab_source_identities_are_unchanged() -> None:
    root = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK")
    if not root.is_dir():
        pytest.skip("protected MATLAB source is unavailable")
    assert {name: annual._sha256(root / name) for name in MATLAB_HASHES} == MATLAB_HASHES
