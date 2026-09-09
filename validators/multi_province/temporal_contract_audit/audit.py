"""Read-only temporal contract, PLM workbook, cache, and Zt audit."""
import csv
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

import h5py
import numpy as np

from contract import SUPPORTED_II, annual_mapping, classify_time_labels, expected_plm_sheets

REPO = Path(__file__).resolve().parents[3]
ROOT = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK")
LOAD = ROOT / "load_GDPdata.m"
ANNUAL = ROOT / "multi_prov_HANK_12sts.m"
EQUILIBRIUM = ROOT / "mpHANK_equilibrium_2000.m"
PLM = ROOT / "R语言估计结果_plm估计.xlsx"
MAT = ROOT / "数据估计结果_1000_100_0.mat"
FILLED = ROOT / "2000年后各省数据_填充NA.xlsx"
PRIOR_DIR = REPO / "reports/mp4c_2018_raw_data_audit_20260909"
PRIOR_FILES = [
    REPO / "docs/CH5_MP4C_2018_RAW_DATA_AND_INTERPOLATION_AUDIT_REPORT.md",
    REPO / "docs/CH5_MP4C_2018_RAW_DATA_AND_INTERPOLATION_AUDIT_ACCEPTANCE.md",
    PRIOR_DIR / "data_contract.json",
    PRIOR_DIR / "cache_audit.json",
    PRIOR_DIR / "anhui_2018_lineage.csv",
    PRIOR_DIR / "official_data_request.csv",
]
ZERO_CALLS = {
    "MATLAB_model": 0,
    "Python_HJB_KFE_household": 0,
    "firm_one_turn_controller": 0,
    "GE_annual_stationary_IRF_Results": 0,
    "root_direct_iterative_eigen_model_solve": 0,
}


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def write_json(path, value):
    Path(path).write_text(
        json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


class OOXMLWorkbook:
    MAIN = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    OFFICE_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

    def __init__(self, path):
        self.path = Path(path)
        with zipfile.ZipFile(self.path) as archive:
            strings_root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            self.strings = [
                "".join(node.text or "" for node in item.iter(f"{{{self.MAIN}}}t"))
                for item in strings_root.findall(f"{{{self.MAIN}}}si")
            ]
            book = ET.fromstring(archive.read("xl/workbook.xml"))
            relationships = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
            targets = {item.attrib["Id"]: item.attrib["Target"] for item in relationships}
            self.sheet_targets = {}
            for sheet in book.find(f"{{{self.MAIN}}}sheets"):
                target = targets[sheet.attrib[f"{{{self.OFFICE_REL}}}id"]].lstrip("/")
                self.sheet_targets[sheet.attrib["name"]] = target if target.startswith("xl/") else f"xl/{target}"

    @property
    def sheet_names(self):
        return tuple(self.sheet_targets)

    def cells(self, sheet_name):
        with zipfile.ZipFile(self.path) as archive:
            root = ET.fromstring(archive.read(self.sheet_targets[sheet_name]))
        rows = []
        for cell in root.iter(f"{{{self.MAIN}}}c"):
            value_node = cell.find(f"{{{self.MAIN}}}v")
            value = None if value_node is None else value_node.text
            if cell.attrib.get("t") == "s" and value is not None:
                value = self.strings[int(value)]
            rows.append({"cell": cell.attrib["r"], "value": value, "type": cell.attrib.get("t", "n")})
        return rows


def matlab_char(handle, reference):
    return "".join(chr(int(x)) for x in np.asarray(handle[reference][()]).reshape(-1))


def matlab_cell(handle, group, field, index):
    value = np.asarray(handle[group[field][()][index, 0]][()]).T
    if value.dtype.fields and set(value.dtype.fields) == {"real", "imag"}:
        value = value["real"] + 1j * value["imag"]
    return value


def source_contract():
    load_text = LOAD.read_text(encoding="utf-8")
    annual_text = ANNUAL.read_text(encoding="utf-8")
    equilibrium_text = EQUILIBRIUM.read_text(encoding="utf-8")
    assertions = {
        "supported_loop_1_to_15": bool(re.search(r"for\s+ii\s*=\s*1:15", load_text)),
        "plm_sheet_key_ii_plus_9": "num2str(ii+9)" in load_text,
        "fixed_zt_row21": "GDP{j}(21,col)" in load_text and "CAP{j}(21,col)" in load_text and "POP{j}(21,col)" in load_text,
        "active_zt_is_zt_new": "mydata.IND_Zt{j}(1,col) = Zt_new" in load_text,
        "active_reg_method_zero": "param.reg_method = 0" in annual_text,
        "filename_ii_plus_2008": bool(re.search(r"year\s*=\s*ii\+2008", annual_text)),
        "current_data_mat_and_level_index_ii": "data_MAT{ii}, 4, ii" in annual_text,
        "comment_declares_2000_2009_for_2009": "2000-2009年的数据可以估计出2009年的alpha" in annual_text,
        "equilibrium_consumes_data_year": all(
            token in equilibrium_text
            for token in ("CAP{st_ind}(data_year,i)", "POP{st_ind}(data_year,i)", "GDP{st_ind}(data_year,i)")
        ),
    }
    assert all(assertions.values()), assertions
    return {
        "assertions": assertions,
        "active_estimator": "reg_method=0; external R PLM alpha and level-implied Zt",
        "historical_alternatives": {
            "reg_method_1": "per-capita MATLAB regress branch with optional raw/movmean/movmedian inputs",
            "reg_method_2": "levels MATLAB regress branch with optional raw/movmean/movmedian inputs",
            "active_smoothing": "smooth_method=0",
        },
        "source_locations": {
            "annual_year_and_call": "multi_prov_HANK_12sts.m:118-133",
            "PLM_and_Zt": "load_GDPdata.m:106-140",
            "alternative_estimators": "load_GDPdata.m:140-237",
            "level_consumption": "mpHANK_equilibrium_2000.m:23-43",
        },
    }


def main(evidence_root, repo_output):
    evidence = Path(evidence_root).resolve()
    output = Path(repo_output).resolve()
    evidence.mkdir(parents=True, exist_ok=False)
    output.mkdir(parents=True, exist_ok=True)

    consumed = [LOAD, ANNUAL, EQUILIBRIUM, PLM, MAT, FILLED, *PRIOR_FILES]
    prior_inventory = json.loads((PRIOR_DIR / "source_inventory.json").read_text(encoding="utf-8"))
    accepted_hashes = {Path(item["path"]).name: item["sha256"] for item in prior_inventory}
    inventory = []
    for path in consumed:
        item = {"path": str(path.resolve()), "bytes": path.stat().st_size, "mtime_ns": path.stat().st_mtime_ns, "sha256": sha256(path)}
        accepted = accepted_hashes.get(path.name)
        if accepted:
            item["accepted_prior_sha256"] = accepted
            item["matches_accepted_prior"] = item["sha256"] == accepted
        inventory.append(item)
    assert all(item.get("matches_accepted_prior", True) for item in inventory)

    source = source_contract()
    workbook = OOXMLWorkbook(PLM)
    expected = {name for ii in SUPPORTED_II for name in expected_plm_sheets(ii)}
    missing_sheets = sorted(expected - set(workbook.sheet_names))
    assert not missing_sheets
    coefficient_audit = {}
    all_layouts = []
    for ii in SUPPORTED_II:
        for industry in range(1, 5):
            vintage = ii + 9
            name = f"总面板回归系数_{vintage}_行业{industry}"
            cells = workbook.cells(name)
            labels = [item["value"] for item in cells if item["cell"].startswith("A")]
            numerics = [(item["cell"], float(item["value"])) for item in cells if item["type"] == "n" and item["value"] is not None]
            layout = classify_time_labels(labels)
            all_layouts.append(layout)
            coefficient_audit[f"ii{ii}_industry{industry}"] = {
                "sheet": name,
                "vintage": vintage,
                "labels": labels,
                "layout_classification": layout,
                "alpha_cell": numerics[-1][0],
                "alpha": numerics[-1][1],
            }
    assert set(all_layouts) == {"FIXED_TEN_PERIOD_WINDOW_EVIDENCE"}

    mappings = []
    zt_checks = []
    alpha_checks = []
    with h5py.File(MAT, "r") as handle:
        top = np.asarray(handle["mydata2"][()])
        assert top.shape[0] == 15
        for ii in SUPPORTED_II:
            group = handle[top[ii - 1, 0]]
            names = [matlab_char(handle, ref) for ref in group["prvname"][()].reshape(-1)]
            gdp = np.real(matlab_cell(handle, group, "GDP", 3)).astype(float)
            capital = np.real(matlab_cell(handle, group, "CAP", 3)).astype(float)
            population = np.real(matlab_cell(handle, group, "POP", 3)).astype(float)
            alpha = np.real(matlab_cell(handle, group, "IND_alpha", 3)).astype(float).reshape(-1)
            saved_zt = np.real(matlab_cell(handle, group, "IND_Zt", 3)).astype(float).reshape(-1)
            sheet = coefficient_audit[f"ii{ii}_industry4"]
            alpha_diff = np.abs(alpha - sheet["alpha"])
            alpha_checks.append({
                "ii": ii,
                "sheet": sheet["sheet"],
                "sheet_alpha": sheet["alpha"],
                "cache_unique_alpha_count": int(np.unique(alpha).size),
                "cache_vs_sheet_exact_cells": int(np.sum(alpha == sheet["alpha"])),
                "cache_vs_sheet_max_abs": float(np.max(alpha_diff)),
            })
            fixed_row = 20
            fixed_formula = gdp[fixed_row] * capital[fixed_row] ** (-alpha) * population[fixed_row] ** (alpha - 1)
            fixed_diff = np.abs(saved_zt - fixed_formula)
            candidate_row = ii + 8
            valid = (gdp[candidate_row] > 0) & (capital[candidate_row] > 0) & (population[candidate_row] > 0)
            candidate = np.full(31, np.nan)
            candidate[valid] = (
                gdp[candidate_row, valid]
                * capital[candidate_row, valid] ** (-alpha[valid])
                * population[candidate_row, valid] ** (alpha[valid] - 1)
            )
            relative_change = np.abs(candidate[valid] / saved_zt[valid] - 1)
            mapping = annual_mapping(ii)
            mapping.update({
                "plm_sheet_industry4": sheet["sheet"],
                "plm_workbook_layout": sheet["layout_classification"],
                "workbook_implied_rolling_sample_end_year": mapping["steady_year"],
                "owner_expanding_sample_end_year": mapping["steady_year"],
                "plm_window_status": "ALIGNED_FIRST_2000_2009_WINDOW" if ii == 1 else "END_YEAR_ALIGNED__FIXED_TEN_PERIOD_LAYOUT_CONFLICTS_WITH_EXPANDING_FROM_2000",
                "level_status": "CONFIRMED_CURRENT_LEVEL_YEAR_MISMATCH",
                "zt_status": "YEAR_ALIGNED_ONLY_FOR_2020" if mapping["steady_year"] == 2020 else "FIXED_2020_ANCHOR_MISMATCH",
            })
            mappings.append(mapping)
            zt_checks.append({
                "ii": ii,
                "steady_year": mapping["steady_year"],
                "current_fixed_row_1based": 21,
                "current_fixed_year": 2020,
                "cache_vs_fixed_formula_exact_cells": int(np.sum(saved_zt == fixed_formula)),
                "cache_vs_fixed_formula_max_abs": float(np.max(fixed_diff)),
                "candidate_row_1based": ii + 9,
                "candidate_year": mapping["steady_year"],
                "candidate_valid_cells": int(np.sum(valid)),
                "candidate_invalid_nonpositive_level_cells": int(np.sum(~valid)),
                "candidate_invalid_provinces": [names[index] for index in np.where(~valid)[0]],
                "candidate_vs_saved_max_abs_relative_change_valid": float(np.max(relative_change)) if relative_change.size else None,
                "candidate_vs_saved_median_abs_relative_change_valid": float(np.median(relative_change)) if relative_change.size else None,
            })

    alpha_mismatches = [item for item in alpha_checks if item["cache_vs_sheet_exact_cells"] != 31]
    fixed_formula_exact = sum(item["cache_vs_fixed_formula_exact_cells"] for item in zt_checks)
    patch_plan = [
        {
            "class": "A_CONFIRMED_INDEX_DEFECT",
            "file": "multi_prov_HANK_12sts.m",
            "current": "mpHANK_equilibrium_2000(..., data_MAT{ii}, 4, ii)",
            "proposed": "level_row = ii + 9; mpHANK_equilibrium_2000(..., data_MAT{ii}, 4, level_row)",
            "meaning": "keep PLM-vintage cache entry ii; select GDP/CAP/POP levels for steady_year",
            "estimator_change": False,
        },
        {
            "class": "PLM_ARTIFACT_ALIGNMENT",
            "file": "R PLM generation source/workbook (future authorized task)",
            "current": "all coefficient vintages retain time1..time9, supporting fixed ten-period windows",
            "proposed": "retain PLM estimator; regenerate versioned coefficients on 2000:steady_year expanding samples",
            "meaning": "implement the Owner-approved expanding-window contract without switching estimators",
            "estimator_change": False,
        },
        {
            "class": "B_LIKELY_LEGACY_ZT_ANCHOR",
            "file": "load_GDPdata.m",
            "current": "Zt_new = GDP{j}(21,col)*CAP{j}(21,col)^(-alpha)*POP{j}(21,col)^(alpha-1)",
            "proposed": "level_row = ii + 9; use GDP/CAP/POP at level_row in the unchanged formula",
            "meaning": "align the level-implied technology index with the PLM vintage end year",
            "estimator_change": False,
            "requires_owner_acceptance": True,
        },
        {
            "class": "CACHE_IDENTITY",
            "file": "load_GDPdata.m",
            "current": "数据估计结果_{GDP multiplier}_{POP multiplier}_{reg_method}.mat",
            "proposed": "use a new explicit temporal-contract cache version and refuse old unversioned cache",
            "meaning": "prevent corrected source from silently loading stale row21 Zt",
            "estimator_change": False,
        },
        {
            "class": "OUTPUT_IDENTITY",
            "file": "multi_prov_HANK_12sts.m",
            "current": "Multi_Province_12sts_{steady_year}.mat",
            "proposed": "retain calendar filename but add temporal-contract metadata and reject stale files without it",
            "meaning": "filename is already calendar-consistent; metadata proves actual rows and vintages",
            "estimator_change": False,
        },
        {
            "class": "METADATA_CONTRACT",
            "file": "annual/cache serialization path",
            "current": "no authoritative row/vintage assertions; prior runtime metadata claimed row19 while bytes used row10",
            "proposed": "persist and assert steady_year, level_row/year, PLM vintage, sample start/end/window type, Zt row/year, contract version",
            "meaning": "make labels and consumed arrays mechanically auditable",
            "estimator_change": False,
        },
    ]
    unresolved = [
        {
            "required_future_evidence": "PLM expanding-window artifact provenance",
            "evidence": "source comment and all 60 coefficient sheets support a ten-period window; later sheets retain time1..time9",
            "required_action": "recover/freeze the R generation source and regenerate 2000:steady_year coefficients under the same PLM estimator in a later authorized task",
            "recommendation": "do not relabel the existing rolling-window coefficients as Owner-approved expanding estimates",
        },
        {
            "owner_decision": "fixed 2020 Zt anchor",
            "evidence": "only source comment says first method uses 2020; no normalization or base-year rationale was found",
            "choice_needed": "accept year-consistent ii+9 level rows before implementation",
            "recommendation": "accept the minimal year-consistent row substitution after PLM-window semantics are frozen",
        },
        {
            "owner_decision": "ii=15 / industry4 coefficient artifact identity",
            "evidence": "cache alpha=0.967775174774325, current vintage24 workbook B11=1.0219847778591; the workbook is newer than the cache",
            "choice_needed": "establish the authoritative saved PLM coefficient provenance before rebuilding the corrected cache",
            "recommendation": "treat the unversioned cache as stale/ambiguous; do not silently mix it with the current workbook",
        },
        {
            "official_data": "2018 Anhui GDP/population/investment-capital chain and alpha/Zt provenance",
            "status": "still pending in accepted official_data_request.csv",
        },
        {
            "official_data": "2022-2023 negative derived capital",
            "status": "independent data-quality issue; year-consistent Zt is undefined for affected province-years until corrected",
        },
    ]
    summary = {
        "temporal_contract_verdict": "CONFIRMED_LEVEL_INDEX_DEFECT__OWNER_EXPANDING_WINDOW_NOT_IMPLEMENTED_BY_SAVED_PLM_ARTIFACT",
        "plm_preservation_verdict": "PRESERVE_PLM_ESTIMATOR__VINTAGE_END_YEAR_ALIGNED__COEFFICIENT_ARTIFACT_REBUILD_REQUIRED",
        "zt_legacy_verdict": "LIKELY_LEGACY_FIXED_YEAR_ANCHOR",
        "supported_ii": list(SUPPORTED_II),
        "all_expected_plm_sheets_present": not missing_sheets,
        "expected_plm_sheet_count": len(expected),
        "all_60_coefficient_sheets_fixed_ten_period_layout": all(item == "FIXED_TEN_PERIOD_WINDOW_EVIDENCE" for item in all_layouts),
        "cache_alpha_matches_sheet_cells": sum(item["cache_vs_sheet_exact_cells"] for item in alpha_checks),
        "cache_alpha_total_cells": len(alpha_checks) * 31,
        "cache_alpha_mismatches": alpha_mismatches,
        "cache_older_than_plm_workbook": MAT.stat().st_mtime_ns < PLM.stat().st_mtime_ns,
        "cache_zt_matches_fixed_row21_formula_cells": fixed_formula_exact,
        "cache_zt_total_cells": len(zt_checks) * 31,
        "zero_scientific_call_ledger": ZERO_CALLS,
        "Results_eligibility": False,
    }

    for path, value in (
        ("source_inventory.json", inventory),
        ("source_contract.json", source),
        ("plm_workbook_audit.json", {"sheet_count": len(workbook.sheet_names), "expected_sheet_count": len(expected), "missing": missing_sheets, "coefficient_sheets": coefficient_audit, "alpha_cache_checks": alpha_checks}),
        ("temporal_mapping.json", mappings),
        ("zt_audit.json", zt_checks),
        ("patch_plan.json", patch_plan),
        ("unresolved_decisions.json", unresolved),
        ("call_ledger.json", ZERO_CALLS),
        ("summary.json", summary),
    ):
        write_json(evidence / path, value)
        write_json(output / path, value)
    with (output / "temporal_mapping.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=mappings[0].keys())
        writer.writeheader()
        writer.writerows(mappings)
    write_json(evidence / "terminal.json", {"completed": True, "summary": summary})
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main(*sys.argv[1:])
