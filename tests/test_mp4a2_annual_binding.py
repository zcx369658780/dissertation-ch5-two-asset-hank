from __future__ import annotations

import ast
from pathlib import Path

import numpy as np
import pytest

from ch5_two_asset_hank.multi_province.annual import (
    AnnualSourceScalars,
    DecoupledAnnualIndex,
    PrimaryAnnualSourceFiles,
    build_python_parity_entry,
    compare_runtime_representation,
    load_primary_annual_input,
    write_canonical_artifact,
)
from validators.multi_province.mp4a2_cache_compatibility import load_cache_fields


SOURCE_ROOT = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK")


def _sources() -> PrimaryAnnualSourceFiles:
    return PrimaryAnnualSourceFiles(
        SOURCE_ROOT / "2000年后各省数据_填充NA.xlsx",
        SOURCE_ROOT / "R语言估计结果_plm估计.xlsx",
        SOURCE_ROOT / "中国各省省会地理距离矩阵.xlsx",
        "C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929",
        "A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68",
        "26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566",
    )


def _scalars() -> AnnualSourceScalars:
    return AnnualSourceScalars(
        1000, 100, 0.096, 1, 1, 0.5, 0.07, 0.09, 0.09, 0.02, 0.02,
        0.1, 0.6, 20, 0.1, 0.02, 0.05, 2, 1, 0.9, 4, 0.25,
    )


def test_decoupled_index_contract_and_negative_recoupling() -> None:
    binding = DecoupledAnnualIndex.for_calendar_year(2009)
    assert (
        binding.calendar_year,
        binding.analysis_index,
        binding.workbook_data_row_index,
        binding.data_mat_index,
        binding.output_filename_year,
        binding.regression_vintage_key,
    ) == (2009, 1, 10, 1, 2009, 10)
    with pytest.raises(ValueError, match="decoupled"):
        DecoupledAnnualIndex(2009, 1, 1, 1, 2009, 10)
    with pytest.raises(ValueError, match="decoupled"):
        DecoupledAnnualIndex.for_calendar_year(2008)


@pytest.mark.skipif(not SOURCE_ROOT.is_dir(), reason="protected primary sources unavailable")
def test_primary_2009_canonical_identity_full_cache_compatibility_and_no_overwrite(tmp_path: Path) -> None:
    binding = DecoupledAnnualIndex.for_calendar_year(2009)
    canonical = load_primary_annual_input(sources=_sources(), binding=binding, scalars=_scalars())
    assert canonical.canonical_sha256() == "507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48"
    assert canonical.gdp.shape == canonical.cap.shape == canonical.pop.shape == (31,)
    assert canonical.distance.shape == canonical.sigmau.shape == (31, 31)
    assert canonical.regression_sheet == "总面板回归系数_10_行业4"
    assert canonical.fixed_zt_calendar_year == 2020
    assert not canonical.gdp.flags.writeable
    assert float(np.max(canonical.sigmau)) == 0.5

    artifact = write_canonical_artifact(canonical, tmp_path / "new")
    assert artifact.read_bytes() == canonical.canonical_bytes()
    with pytest.raises(FileExistsError):
        write_canonical_artifact(canonical, tmp_path / "new")

    cache = load_cache_fields(
        SOURCE_ROOT / "数据估计结果_1000_100_0.mat",
        data_mat_index=1,
        data_row_index=10,
    )
    results = compare_runtime_representation(canonical, cache, rtol=1e-12, atol=1e-12)
    by_field = {result.field: result for result in results}
    assert set(by_field) == {
        "GDP", "CAP", "POP", "log_pgdp", "log_pcap", "IND_alpha", "IND_Zt",
        "GDP_multiplier", "POP_multiplier", "delta", "prvname",
    }
    assert all(result.classification != "MATERIAL_MISMATCH" for result in results)
    assert by_field["log_pgdp"].classification == "SOURCE_EQUIVALENT_BINARY64"
    assert by_field["IND_Zt"].max_abs_difference == 6.938893903907228e-18

    parity_entry = build_python_parity_entry(canonical)
    assert parity_entry.scientific_solver_called is False
    assert parity_entry.binding == binding
    assert parity_entry.canonical_input_sha256 == canonical.canonical_sha256()


def test_cache_comparator_fails_closed_on_missing_and_material_fields() -> None:
    if not SOURCE_ROOT.is_dir():
        pytest.skip("protected primary sources unavailable")
    canonical = load_primary_annual_input(
        sources=_sources(), binding=DecoupledAnnualIndex.for_calendar_year(2009), scalars=_scalars()
    )
    with pytest.raises(ValueError, match="missing consumed fields"):
        compare_runtime_representation(canonical, {}, rtol=1e-12, atol=1e-12)
    cache = load_cache_fields(SOURCE_ROOT / "数据估计结果_1000_100_0.mat", data_mat_index=1, data_row_index=10)
    cache["GDP"] = np.asarray(cache["GDP"]) + 1.0
    result = {item.field: item for item in compare_runtime_representation(
        canonical, cache, rtol=1e-12, atol=1e-12
    )}
    assert result["GDP"].classification == "MATERIAL_MISMATCH"


def test_annual_module_and_matlab_wrapper_are_static_preparation_only() -> None:
    annual_path = Path("src/ch5_two_asset_hank/multi_province/annual.py")
    tree = ast.parse(annual_path.read_text(encoding="utf-8"))
    imports = {
        alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names
    } | {
        node.module or "" for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)
    }
    forbidden = ("household", "hjb", "kfe", "one_turn", "steady_state", "chapter5_model")
    assert not any(marker in name.casefold() for name in imports for marker in forbidden)

    wrapper = Path(
        "validators/multi_province/matlab/mp4b_calendar2009_stationary_wrapper.m"
    ).read_text(encoding="utf-8")
    assert "calendar_year = 2009;" in wrapper
    assert "analysis_index = 1;" in wrapper
    assert "data_year = 10;" in wrapper
    assert "data_MAT_index = 1;" in wrapper
    assert "multi_prov_HANK_12sts" not in wrapper
    assert "mpHANK_equilibrium_2000" in wrapper
    assert "isfolder(run_root) || isfile(run_root)" in wrapper
