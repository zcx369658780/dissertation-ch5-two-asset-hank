"""Owner-A corrected 2009--2022 annual empirical input representation.

This module is deliberately input-only: importing or preparing inputs never
invokes a stationary, household, HJB, or KFE computation.
"""
from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path
from typing import Any, Mapping

import h5py
import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[2]
for _root in (REPO_ROOT / "src", REPO_ROOT):
    if str(_root) not in sys.path:
        sys.path.insert(0, str(_root))

from ch5_two_asset_hank.multi_province.annual import _normalize_province, _xlsx_sheet_rows
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER
from validators.multi_province import mp4c_matlab_runtime_cache as cache
from validators.multi_province import mp4c_python_annual_empirical as empirical


REPRESENTATION = "OWNER_A_2009_2022_VERIFIED_CHNCAPITALSTOCK_ROLLING_PLM_END_YEAR_CALENDAR_INPUT"
YEARS = tuple(range(2009, 2023))
FILLED_WORKBOOK = "2000年后各省数据_填充NA.xlsx"
REGRESSION_WORKBOOK = "R语言估计结果_plm估计.xlsx"
DISTANCE_WORKBOOK = "中国各省省会地理距离矩阵.xlsx"
CAPITAL_SHEET = "R语言计算资本存量"
GDP_SHEET = "GDP"
POP_SHEET = "就业人数"


def _sha(path: Path) -> str:
    return cache.file_sha256(path)


def _binding(year: int) -> dict[str, int]:
    if year not in YEARS:
        raise ValueError("Owner-A input year must be in 2009..2022")
    return {
        "steady_state_calendar_year": year,
        "rolling_window_entry_index": year - 2008,
        "regression_vintage_index": year - 1999,
        "calendar_level_row_index": year - 1999,
        "rolling_window_start_year": year - 9,
        "rolling_window_end_year": year,
    }


def _year(value: object) -> int:
    if isinstance(value, (int, float)) and float(value).is_integer():
        return int(value)
    text = str(value)
    digits = "".join(character for character in text if character.isdigit())
    if len(digits) != 4:
        raise ValueError(f"workbook year is not explicit: {value!r}")
    return int(digits)


def _axis(rows: Mapping[int, Mapping[int, object]], start: int, end: int) -> tuple[str, ...]:
    labels = tuple(_normalize_province(rows[1][column]) for column in range(start, end + 1))
    if labels != PROVINCE_ORDER:
        raise ValueError("workbook province order differs from the accepted 31-province axis")
    return labels


def _level(rows: Mapping[int, Mapping[int, object]], physical_row: int, start: int, end: int, year: int) -> np.ndarray:
    if _year(rows[physical_row][1]) != year:
        raise ValueError("calendar level row does not match the Owner-A year")
    value = np.asarray([rows[physical_row][column] for column in range(start, end + 1)], dtype=np.float64)
    if value.shape != (31,) or not np.isfinite(value).all() or not np.all(value > 0):
        raise ValueError("Owner-A level input must be finite and strictly positive")
    return value


def _technology(cache_path: Path, year: int) -> tuple[np.ndarray, np.ndarray, list[str]]:
    binding = _binding(year)
    if _sha(cache_path) != cache.EXPECTED_CACHE_SHA256:
        raise ValueError("runtime cache SHA mismatch")
    with h5py.File(cache_path, "r") as h5:
        entries = h5["mydata2"]
        group = h5[entries[binding["rolling_window_entry_index"] - 1, 0]]
        names = tuple(_normalize_province(cache._text(h5, group["prvname"][index, 0])) for index in range(31))
        if names != PROVINCE_ORDER:
            raise ValueError("runtime technology province order differs from Owner-A axis")
        alpha = cache._cell_numeric(h5, group, "IND_alpha", cache.INDUSTRY_MATLAB_INDEX).reshape(-1)
        zt = cache._cell_numeric(h5, group, "IND_Zt", cache.INDUSTRY_MATLAB_INDEX).reshape(-1)
    if alpha.shape != (31,) or zt.shape != (31,) or not np.isfinite(alpha).all() or not np.isfinite(zt).all():
        raise ValueError("runtime technology artifact is non-finite or malformed")
    if not np.all((alpha > 0) & (alpha < 1)) or not np.all(zt > 0):
        raise ValueError("runtime technology artifact is inadmissible")
    return alpha, zt, list(names)


def _numeric_cells(rows: Mapping[int, Mapping[int, object]]) -> list[float]:
    return [float(value) for row in rows.values() for value in row.values() if isinstance(value, float) and np.isfinite(value)]


def static_plm_audit(data_root: Path, cache_path: Path) -> dict[str, Any]:
    """Verify frozen stored vintages 10--23 without invoking R."""
    regression = Path(data_root) / REGRESSION_WORKBOOK
    results: list[dict[str, Any]] = []
    for year in YEARS:
        binding = _binding(year)
        vintage = binding["regression_vintage_index"]
        coefficient_sheet = f"总面板回归系数_{vintage}_行业4"
        intercept_sheet = f"总面板回归截距_{vintage}_行业4"
        coefficient = _xlsx_sheet_rows(regression, coefficient_sheet)
        intercept = _xlsx_sheet_rows(regression, intercept_sheet)
        coefficient_values = _numeric_cells(coefficient)
        intercept_values = _numeric_cells(intercept)
        if len(coefficient_values) < 2 or len(intercept_values) < 31:
            raise ValueError(f"stored PLM vintage {vintage} lacks required finite values")
        alpha, zt, names = _technology(cache_path, year)
        results.append({
            "steady_state_calendar_year": year,
            "rolling_window_entry_index": binding["rolling_window_entry_index"],
            "regression_vintage_index": vintage,
            "coefficient_sheet": coefficient_sheet,
            "intercept_sheet": intercept_sheet,
            "coefficient_finite_count": len(coefficient_values),
            "intercept_finite_count": len(intercept_values),
            "runtime_technology_entry": binding["rolling_window_entry_index"],
            "runtime_ind_alpha_min": float(alpha.min()),
            "runtime_ind_alpha_max": float(alpha.max()),
            "runtime_ind_zt_min": float(zt.min()),
            "runtime_ind_zt_max": float(zt.max()),
            "province_order": names,
            "vintage_24_consumed": False,
        })
    return {"schema": "CH5_MP4C_OWNER_A_STORED_PLM_VINTAGES_10_23_STATIC_AUDIT_V1", "representation": REPRESENTATION, "years": results}


def build_input(data_root: Path, cache_path: Path, year: int) -> dict[str, Any]:
    """Materialize one corrected Owner-A input with no HANK science."""
    binding = _binding(year)
    root = Path(data_root)
    filled = root / FILLED_WORKBOOK
    sources = empirical.primary_sources(root)
    source_hashes = dict(sources.verified_hashes())
    if _sha(filled) != source_hashes[FILLED_WORKBOOK]:
        raise ValueError("filled workbook identity mismatch")
    gdp_rows = _xlsx_sheet_rows(filled, GDP_SHEET)
    pop_rows = _xlsx_sheet_rows(filled, POP_SHEET)
    cap_rows = _xlsx_sheet_rows(filled, CAPITAL_SHEET)
    _axis(gdp_rows, 3, 33)
    _axis(pop_rows, 3, 33)
    _axis(cap_rows, 2, 32)
    physical_row = binding["calendar_level_row_index"] + 1
    scalars = empirical.accepted_source_scalars()
    gdp = _level(gdp_rows, physical_row, 3, 33, year) * scalars.gdp_multiplier
    pop = _level(pop_rows, physical_row, 3, 33, year) * scalars.pop_multiplier
    cap = _level(cap_rows, physical_row, 2, 32, year) * scalars.gdp_multiplier
    log_pgdp = np.log(gdp / pop)
    log_pcap = np.log(cap / pop)
    alpha, zt, names = _technology(cache_path, year)
    distance = cache.add_runtime_support(
        {"placeholder": True}, distance_workbook=sources.distance_workbook,
        distance_sha256=source_hashes[DISTANCE_WORKBOOK], max_sigmau=scalars.max_sigmau,
    )["runtime_support"]
    pcap = cap / pop
    ratio = 0.3 * (pcap - pcap.min()) / (pcap.max() - pcap.min())
    return {
        "schema": "CH5_MP4C_OWNER_A_CORRECTED_RUNTIME_INPUT_V1",
        "representation": REPRESENTATION,
        "binding": binding,
        "source_hashes": source_hashes,
        "runtime_cache_sha256": _sha(cache_path),
        "cache_sha256": _sha(cache_path),
        "capital_authority": "OWNER_A_CHNCAPITALSTOCK_2000_2022_VERIFIED_SEGMENT__AUTHORIZED_FOR_2009_2022_STEADY_STATE_INPUT",
        "plm_authority": "OWNER_ACCEPTS_STORED_R_PLM_VINTAGES_10_23_AS_FROZEN_EMPIRICAL_CALIBRATION_ARTIFACTS__ESTIMATOR_REPRODUCIBILITY_DEFERRED",
        "province_order": names,
        "scalars": asdict(scalars),
        "vectors": {"GDP": gdp.tolist(), "CAP": cap.tolist(), "POP": pop.tolist(), "log_pgdp": log_pgdp.tolist(), "log_pcap": log_pcap.tolist(), "IND_alpha": alpha.tolist(), "IND_Zt": zt.tolist()},
        "derived": {"gov_inv": cap.tolist(), "inter_province_asset_ratio": ratio.tolist()},
        "runtime_support": distance,
        "source_fields": {"GDP": GDP_SHEET, "POP": POP_SHEET, "CAP": CAPITAL_SHEET},
        "no_2023_scientific_input": True,
    }


def canonical_bytes(payload: Mapping[str, Any]) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def validate(payload: Mapping[str, Any]) -> None:
    if payload.get("representation") != REPRESENTATION or payload.get("schema") != "CH5_MP4C_OWNER_A_CORRECTED_RUNTIME_INPUT_V1":
        raise ValueError("wrong Owner-A runtime input representation")
    binding = payload.get("binding", {})
    year = binding.get("steady_state_calendar_year")
    if year not in YEARS or binding != _binding(int(year)):
        raise ValueError("Owner-A semantic indices are not exact")
    if tuple(payload.get("province_order", ())) != PROVINCE_ORDER:
        raise ValueError("Owner-A province order is not exact")
    vectors = payload.get("vectors", {})
    for field in ("GDP", "CAP", "POP", "log_pgdp", "log_pcap", "IND_alpha", "IND_Zt"):
        value = np.asarray(vectors.get(field), dtype=np.float64)
        if value.shape != (31,) or not np.isfinite(value).all():
            raise ValueError(f"Owner-A vector malformed: {field}")
    if not all(np.all(np.asarray(vectors[field]) > 0) for field in ("GDP", "CAP", "POP", "IND_Zt")):
        raise ValueError("Owner-A positive-level contract failed")
    if not np.all((np.asarray(vectors["IND_alpha"]) > 0) & (np.asarray(vectors["IND_alpha"]) < 1)):
        raise ValueError("Owner-A alpha contract failed")
    if not np.allclose(np.asarray(vectors["log_pgdp"]), np.log(np.asarray(vectors["GDP"]) / np.asarray(vectors["POP"])), rtol=0, atol=1e-12):
        raise ValueError("Owner-A log_pgdp contract failed")
    if not np.allclose(np.asarray(vectors["log_pcap"]), np.log(np.asarray(vectors["CAP"]) / np.asarray(vectors["POP"])), rtol=0, atol=1e-12):
        raise ValueError("Owner-A log_pcap contract failed")


def entry_states(payload: Mapping[str, Any], accepted_scalars: Mapping[str, float]) -> tuple[dict[str, Any], ...]:
    validate(payload)
    vectors, derived, names = payload["vectors"], payload["derived"], payload["province_order"]
    states = []
    for index, name in enumerate(names):
        states.append({"name": name, "N": vectors["POP"][index], "alpha": vectors["IND_alpha"][index], "Zt": vectors["IND_Zt"][index], "Kt0": vectors["CAP"][index], "Kt": vectors["CAP"][index], "Kt_prev": vectors["CAP"][index], "Lt": vectors["POP"][index], "Lt_prev": vectors["POP"][index], "Yt0": vectors["GDP"][index], "Yt": vectors["GDP"][index], "Zt_1": vectors["IND_Zt"][index], "GovInv": derived["gov_inv"][index], "inter_prv_ratio": derived["inter_province_asset_ratio"][index], "rb_gap": accepted_scalars["rb_gap"], "rah": accepted_scalars["rah"], "ra": accepted_scalars["ra"], "it": accepted_scalars["nominal_rate"], "rb": accepted_scalars["rb"], "rk": accepted_scalars["rk"], "wjt": accepted_scalars["wjt"], "w": accepted_scalars["composite_wage"], "Tt": accepted_scalars["transfer_income"], "pit": accepted_scalars["inflation"], "pit_1": accepted_scalars["inflation"], "totalpit": accepted_scalars["inflation"], "epsilon_pi": 0.0, "tau": accepted_scalars["wage_tax"], "At": accepted_scalars["initial_at"], "Bt": accepted_scalars["initial_bt"], "mt": accepted_scalars["initial_mt"], "Ct": accepted_scalars["initial_ct"], "AtTax": 0.0, "GovSurplus": 0.0, "corptau": accepted_scalars["corporate_tax"], "ramin": 0.02, "ramax": 0.09, "wjtmin": 0.8, "wjtmax": 1.3})
    return tuple(states)
