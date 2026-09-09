from __future__ import annotations

import csv
from hashlib import sha256
import json
from pathlib import Path
import sys

import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[3]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from ch5_two_asset_hank.multi_province.annual import (  # noqa: E402
    AnnualSourceScalars,
    DecoupledAnnualIndex,
    PrimaryAnnualSourceFiles,
    TEMPORAL_CONTRACT_VERSION,
    _xlsx_sheet_rows,
    load_primary_annual_input,
    validate_corrected_annual_payload,
    write_canonical_artifact,
)


SOURCE_HASHES = {
    "2000年后各省数据_填充NA.xlsx": "C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929",
    "R语言估计结果_plm估计.xlsx": "A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68",
    "中国各省省会地理距离矩阵.xlsx": "26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566",
}
OLD_CACHE_ALPHA_II15_INDUSTRY4 = 0.967775174774325
ACCEPTED_CURRENT_PLM_ALPHA_VINTAGE24_INDUSTRY4 = 1.0219847778591


def _json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def _scalars() -> AnnualSourceScalars:
    return AnnualSourceScalars(
        1000, 100, .096, 1, 1, .5, .07, .09, .09, .02, .02, .1,
        .6, 20, .1, .02, .05, 2, 1, .9, 4, .25,
    )


def _sources(source_root: Path) -> PrimaryAnnualSourceFiles:
    return PrimaryAnnualSourceFiles(
        source_root / "2000年后各省数据_填充NA.xlsx",
        source_root / "R语言估计结果_plm估计.xlsx",
        source_root / "中国各省省会地理距离矩阵.xlsx",
        SOURCE_HASHES["2000年后各省数据_填充NA.xlsx"],
        SOURCE_HASHES["R语言估计结果_plm估计.xlsx"],
        SOURCE_HASHES["中国各省省会地理距离矩阵.xlsx"],
    )


def _alpha(regression_workbook: Path, vintage: int) -> float:
    rows = _xlsx_sheet_rows(regression_workbook, f"总面板回归系数_{vintage}_行业4")
    numeric = [float(value) for row in rows.values() for value in row.values()
               if isinstance(value, float) and np.isfinite(value)]
    return float(numeric[-1])


def build(source_root: Path, evidence_root: Path, repo_report_root: Path) -> None:
    evidence_root.mkdir(parents=True, exist_ok=False)
    repo_report_root.mkdir(parents=True, exist_ok=False)
    premodel_root = evidence_root / "premodel"
    premodel_root.mkdir()
    sources = _sources(source_root)
    summaries: list[dict[str, object]] = []
    canonicals = {}
    for year in (2009, 2018):
        canonical = load_primary_annual_input(
            sources=sources,
            binding=DecoupledAnnualIndex.for_calendar_year(year),
            scalars=_scalars(),
        )
        year_root = premodel_root / str(year)
        artifact = write_canonical_artifact(canonical, year_root)
        validate_corrected_annual_payload(
            json.loads(artifact.read_text(encoding="utf-8")), expected_source_hashes=SOURCE_HASHES
        )
        canonicals[year] = canonical
        summaries.append({
            "year": year,
            "artifact": str(artifact),
            "canonical_sha256": canonical.canonical_sha256(),
            "binding": canonical.binding.temporal_metadata(),
            "regression_sheet": canonical.regression_sheet,
            "alpha": float(canonical.ind_alpha[0]),
            "zt_source_year": canonical.zt_source_calendar_year,
            "all_vectors_finite": all(np.isfinite(getattr(canonical, name)).all() for name in (
                "gdp", "cap", "pop", "log_pgdp", "log_pcap", "ind_alpha", "ind_zt",
                "initialized_zt", "gov_inv", "inter_province_asset_ratio",
            )),
            "province_count": len(canonical.province_axis.labels),
            "source_status": "PROVISIONAL_AUDITED_SOURCE__OFFICIAL_VERIFICATION_OPEN",
        })

    contract_rows = []
    for year in range(2009, 2024):
        item = DecoupledAnnualIndex.for_calendar_year(year)
        contract_rows.append(item.temporal_metadata())
    with (evidence_root / "temporal_contract_2009_2023.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(contract_rows[0]))
        writer.writeheader()
        writer.writerows(contract_rows)

    workbook = source_root / "2000年后各省数据_填充NA.xlsx"
    sheets = {key: _xlsx_sheet_rows(workbook, sheet) for key, sheet in {
        "gdp": "GDP", "cap": "总资本存量", "pop": "常住人口",
    }.items()}
    ah_index = 11
    excel_column = 14
    corrected = canonicals[2018]
    old_level = {}
    corrected_level = {}
    for key, multiplier in (("gdp", 1000.0), ("cap", 1000.0), ("pop", 100.0)):
        old_level[key] = float(sheets[key][11][excel_column]) * multiplier
        corrected_level[key] = float(sheets[key][20][excel_column]) * multiplier
    alpha2018 = float(corrected.ind_alpha[ah_index])
    old_zt_level = {
        key: float(sheets[key][22][excel_column]) * multiplier
        for key, multiplier in (("gdp", 1000.0), ("cap", 1000.0), ("pop", 100.0))
    }
    old_mixed_zt = old_zt_level["gdp"] * old_zt_level["cap"] ** (-alpha2018) * old_zt_level["pop"] ** (alpha2018 - 1)
    lineage = {
        "province": "安徽",
        "python_index_zero_based": ah_index,
        "matlab_index_one_based": 12,
        "excel_column": "N",
        "source_physical_row": 20,
        "level_data_row_one_based": 19,
        "calendar_year": 2018,
        "source_cells": {"GDP": "GDP!N20", "POP": "常住人口!N20", "CAP": "总资本存量!N20"},
        "raw_workbook_values": {
            "GDP_亿元": float(sheets["gdp"][20][excel_column]),
            "POP_万人": float(sheets["pop"][20][excel_column]),
            "CAP_derived_workbook_unit": float(sheets["cap"][20][excel_column]),
        },
        "corrected_transformed_values": corrected_level,
        "canonical_values": {
            "gdp": float(corrected.gdp[ah_index]),
            "pop": float(corrected.pop[ah_index]),
            "cap": float(corrected.cap[ah_index]),
            "alpha": alpha2018,
            "ind_zt": float(corrected.ind_zt[ah_index]),
        },
        "accepted_old_mixed_year_2018_description": {
            "level_calendar_year": 2009,
            "level_transformed_values": old_level,
            "zt_level_calendar_year": 2020,
            "ind_zt_reconstructed": float(old_mixed_zt),
            "difference_corrected_minus_old": {
                "gdp": corrected_level["gdp"] - old_level["gdp"],
                "cap": corrected_level["cap"] - old_level["cap"],
                "pop": corrected_level["pop"] - old_level["pop"],
                "ind_zt": float(corrected.ind_zt[ah_index]) - float(old_mixed_zt),
            },
            "interpretation": "DESCRIPTIVE_INPUT_DIFFERENCE_ONLY",
        },
        "official_data_status": "PROVISIONAL_AUDITED_SOURCE__OFFICIAL_VERIFICATION_OPEN",
    }
    assert corrected_level == {
        "gdp": 34010910.0,
        "cap": 1357314108201.3684,
        "pop": 607600.0,
    }

    current_alpha24 = _alpha(source_root / "R语言估计结果_plm估计.xlsx", 24)
    stale = {
        "classification": "STALE_UNVERSIONED_CACHE_REJECTED_AS_CORRECTED_INPUT",
        "data_mat_index": 15,
        "industry_index": 4,
        "old_cache_alpha": OLD_CACHE_ALPHA_II15_INDUSTRY4,
        "current_verified_plm_workbook_alpha": current_alpha24,
        "accepted_expected_current_alpha": ACCEPTED_CURRENT_PLM_ALPHA_VINTAGE24_INDUSTRY4,
        "difference": current_alpha24 - OLD_CACHE_ALPHA_II15_INDUSTRY4,
        "primary_authority": "R语言估计结果_plm估计.xlsx / vintage24 / industry4",
        "old_cache_can_override": False,
    }
    if current_alpha24 != ACCEPTED_CURRENT_PLM_ALPHA_VINTAGE24_INDUSTRY4:
        raise ValueError("current PLM workbook alpha does not match accepted identity")

    calls = {
        "MATLAB_process_or_model": 0,
        "household_HJB_KFE": 0,
        "labor_root_brentq": 0,
        "direct_iterative_eigen_solve": 0,
        "firm_one_turn_controller": 0,
        "stationary_GE_annual_loop": 0,
        "IRF_dynamics_Results": 0,
        "allowed_static_premodel_constructions": 2,
    }
    summary = {
        "verdict": "TEMPORAL_CONTRACT_IMPLEMENTED_STATIC_VALIDATION_PASS",
        "contract_version": TEMPORAL_CONTRACT_VERSION,
        "years": summaries,
        "anhui_2018": lineage,
        "stale_cache": stale,
        "scientific_call_ledger": calls,
        "Results_eligibility": False,
    }
    _json(evidence_root / "corrected_premodel_summary.json", summary)
    _json(evidence_root / "anhui_2018_lineage.json", lineage)
    _json(evidence_root / "stale_cache_provenance.json", stale)
    _json(evidence_root / "call_ledger.json", calls)
    _json(repo_report_root / "corrected_premodel_summary.json", summary)
    _json(repo_report_root / "stale_cache_provenance.json", stale)
    with (repo_report_root / "temporal_contract_2009_2023.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(contract_rows[0]))
        writer.writeheader()
        writer.writerows(contract_rows)


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit("usage: build_evidence.py SOURCE_ROOT FRESH_EVIDENCE_ROOT FRESH_REPO_REPORT_ROOT")
    build(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
