"""Read-only MP4C MATLAB/Python model-unit lineage audit.

This utility deliberately opens only source text, the protected filled workbook,
and the protected MATLAB v7.3 runtime cache.  It does not import or invoke a
stationary worker, household/HJB/KFE routine, MATLAB, or R.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

import h5py
import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(REPO_ROOT / "src"), str(REPO_ROOT)]

from ch5_two_asset_hank.multi_province.annual import _normalize_province, _xlsx_sheet_rows
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER
from validators.multi_province import mp4c_matlab_runtime_cache as runtime_cache


MATLAB_ROOT = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK")
R_MAIN = Path(r"D:\Rprogramme\main.r")
FILLED_WORKBOOK = MATLAB_ROOT / "2000年后各省数据_填充NA.xlsx"
CACHE = MATLAB_ROOT / "数据估计结果_1000_100_0.mat"
EXPECTED_CACHE_SHA256 = "923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A"

MATLAB_FILES = (
    "load_GDPdata.m",
    "multi_prov_HANK_12sts.m",
    "mpHANK_equilibrium_2000.m",
    "HANK_mp_1eq.m",
    "HANK_mp_1turn.m",
    "HANK_firm.m",
    "main.m",
    "main2.m",
)
PYTHON_FILES = (
    "validators/multi_province/mp4c_python_annual_empirical.py",
    "validators/multi_province/mp4c_owner_a_2009_2022.py",
    "validators/multi_province/mp4c_matlab_runtime_cache.py",
    "validators/multi_province/mp4c_python_annual_production.py",
    "src/ch5_two_asset_hank/multi_province/annual.py",
)
SAMPLES = ((2000, 1), (2011, 3), (2022, 14))
SAMPLE_PROVINCES = ("北京", "河南", "广东", "西藏", "新疆")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def write_text(path: Path, text: str) -> None:
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def write_json(path: Path, payload: Any) -> None:
    write_text(path, json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def source_manifest(repo: Path) -> dict[str, Any]:
    matlab = []
    for relative in MATLAB_FILES:
        path = MATLAB_ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        matlab.append({"logical_role": relative, "path": str(path), "sha256": sha256(path)})
    python = []
    for relative in PYTHON_FILES:
        path = repo / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        python.append({"logical_role": relative, "path": str(path), "sha256": sha256(path)})
    for protected in (FILLED_WORKBOOK, CACHE, R_MAIN):
        if not protected.is_file():
            raise FileNotFoundError(protected)
    if sha256(CACHE) != EXPECTED_CACHE_SHA256:
        raise ValueError("protected cache hash does not match the frozen runtime-cache contract")
    return {
        "schema": "CH5_MP4C_MATLAB_UNIT_SCALING_SOURCE_IDENTITY_V1",
        "matlab_primary_root": str(MATLAB_ROOT),
        "matlab_sources": matlab,
        "python_sources": python,
        "protected_inputs": [
            {"role": "filled_workbook", "path": str(FILLED_WORKBOOK), "sha256": sha256(FILLED_WORKBOOK)},
            {"role": "runtime_cache", "path": str(CACHE), "sha256": sha256(CACHE)},
            {"role": "r_estimation_source", "path": str(R_MAIN), "sha256": sha256(R_MAIN)},
        ],
    }


def direct_multiplier_reads() -> dict[str, list[str]]:
    hits: dict[str, list[str]] = {"GDP_multiplier": [], "POP_multiplier": []}
    for relative in MATLAB_FILES:
        for number, line in enumerate((MATLAB_ROOT / relative).read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for token in hits:
                if token in line:
                    hits[token].append(f"{relative}:{number}: {line.strip()}")
    return hits


def literal_audit_text(reads: dict[str, list[str]]) -> str:
    direct = "\n".join(f"- `{item}`" for token in ("GDP_multiplier", "POP_multiplier") for item in reads[token])
    return f"""# MATLAB literal multiplier and downstream-use audit

Primary source root: `{MATLAB_ROOT}`.

## Direct reads of multiplier symbols

{direct}

The live global parameters are set in `multi_prov_HANK_12sts.m:81` to
`GDP_multiplier = 1000` and `POP_multiplier = 100`.  The same file passes both
values to `load_GDPdata(...)` at line 128.  No direct `param.GDP_multiplier` or
`param.POP_multiplier` read occurs in `mpHANK_equilibrium_2000.m`,
`HANK_mp_1eq.m`, `HANK_mp_1turn.m`, or `HANK_firm.m`.

## Literal source-to-runtime transforms (industry 4)

`load_GDPdata.m:74-104` actively reads workbook sheets `GDP`, `总资本存量`, and
`常住人口`; its commented `R语言计算资本存量` and `就业人数` alternatives are not
active runtime inputs.  The executable arithmetic is:

| field | exact expression | source-to-model factor |
| --- | --- | --- |
| GDP | `temp1(:,2:32) * GDP_multiplier` | x1000 |
| CAP | `temp2(:,2:32) * GDP_multiplier` | x1000 |
| POP | `temp3(:,2:32) * POP_multiplier` | x100 |

Thus the cached logarithms made at `load_GDPdata.m:126-127` equal
`log((raw_GDP/raw_POP) * 10)` and `log((raw_CAP/raw_POP) * 10)` for industry 4.
The cache records both scalars at lines 239-240.  The file name embeds the same
values (`数据估计结果_1000_100_0.mat`) at line 106.

## State inheritance, rather than another multiplier read

`mpHANK_equilibrium_2000.m:27-40` assigns cache CAP directly to `Kt0`/`Kt`,
cache POP directly to `N`/`Lt`, cache GDP directly to `Yt0`/`Yt`, derives
`pcap`/`pgdp` by exponentiating the cached logs, sets lagged K/L equal to the
initialized levels, and initializes `GovInv = Kt0 * GovInv_ratio`.  It applies
no second GDP/POP scaling.

`HANK_mp_1eq.m:27-66` and `HANK_mp_1turn.m:4-66` have no multiplier-symbol
read.  They consume those model-unit state levels: migration `phi_MAT` uses
`Yt/Lt`; interprovince capital aggregates `inter_prv_ratio * At * N`; the firm
block is called with `GovInv` and `Lt_supply`; and fiscal aggregation subtracts
`Bt * rb * N`.  `HANK_firm.m:9-98` uses `Kt_supply + GovInv`, computes
`Yt = Zt * Kt^alpha * Lt^(1-alpha)`, and makes income/tax terms proportional to
`Lt`, `Yt`, or `GovInv`.  Therefore a factor inversion/omission would propagate
as a model-scale change through migration, firm, and fiscal quantities, rather
than being canceled by a later direct multiplier operation.

## Output-side inverse display conversion

`main.m:164-181` writes `12年稳态值.xlsx`: Yt0/Yt/Kt0/Kt are divided by the
stored GDP multiplier, while N (shown as Lt0) and Lt are divided by the POP
multiplier.  `main2.m:164-181` duplicates this same writer.  These are
model-to-display conversions, inverse to loading, not a second model-input
transformation.
"""


def decode_numeric_proof() -> list[dict[str, Any]]:
    raw = {sheet: _xlsx_sheet_rows(FILLED_WORKBOOK, sheet) for sheet in ("GDP", "总资本存量", "常住人口")}
    headers = tuple(_normalize_province(raw["GDP"][1][column]) for column in range(3, 34))
    if headers != PROVINCE_ORDER:
        raise ValueError("filled workbook province axis violates the accepted contract")
    if any(tuple(_normalize_province(rows[1][column]) for column in range(3, 34)) != headers for rows in raw.values()):
        raise ValueError("workbook source sheets have inconsistent province axes")
    rows: list[dict[str, Any]] = []
    with h5py.File(CACHE, "r") as h5:
        entries = h5["mydata2"]
        for year, entry_index in SAMPLES:
            group = h5[entries[entry_index - 1, 0]]
            cache_names = tuple(_normalize_province(runtime_cache._text(h5, group["prvname"][i, 0])) for i in range(31))
            if cache_names != PROVINCE_ORDER:
                raise ValueError("cache province axis violates the accepted contract")
            arrays = {field: runtime_cache._cell_numeric(h5, group, field, 4) for field in ("GDP", "CAP", "POP", "log_pgdp", "log_pcap")}
            cache_row = year - 1999
            workbook_row = cache_row + 1
            scalar_gdp = float(np.asarray(group["GDP_multiplier"][()]).reshape(-1)[0])
            scalar_pop = float(np.asarray(group["POP_multiplier"][()]).reshape(-1)[0])
            for province in SAMPLE_PROVINCES:
                column = headers.index(province)
                raw_gdp = float(raw["GDP"][workbook_row][column + 3])
                raw_cap = float(raw["总资本存量"][workbook_row][column + 3])
                raw_pop = float(raw["常住人口"][workbook_row][column + 3])
                cached: dict[str, float] = {}
                for field, array in arrays.items():
                    value = array[cache_row - 1, column]
                    if np.iscomplexobj(value) and abs(value.imag) > 1e-14:
                        raise ValueError(f"unexpected non-real cache value for {field}")
                    cached[field] = float(np.real(value))
                expected = {"GDP": raw_gdp * scalar_gdp, "CAP": raw_cap * scalar_gdp, "POP": raw_pop * scalar_pop}
                row = {
                    "calendar_year": year,
                    "cache_entry_matlab_1based": entry_index,
                    "cache_data_row_matlab_1based": cache_row,
                    "workbook_row_1based": workbook_row,
                    "province": province,
                    "raw_GDP": raw_gdp,
                    "raw_CAP_total_capital_stock": raw_cap,
                    "raw_POP_resident_population": raw_pop,
                    "cache_GDP": cached["GDP"],
                    "cache_CAP": cached["CAP"],
                    "cache_POP": cached["POP"],
                    "GDP_factor_observed": cached["GDP"] / raw_gdp,
                    "CAP_factor_observed": cached["CAP"] / raw_cap,
                    "POP_factor_observed": cached["POP"] / raw_pop,
                    "cache_GDP_multiplier": scalar_gdp,
                    "cache_POP_multiplier": scalar_pop,
                    "cache_log_pgdp": cached["log_pgdp"],
                    "recomputed_log_pgdp": float(np.log(cached["GDP"] / cached["POP"])),
                    "cache_log_pcap": cached["log_pcap"],
                    "recomputed_log_pcap": float(np.log(cached["CAP"] / cached["POP"])),
                    "GDP_exact": bool(cached["GDP"] == expected["GDP"]),
                    "CAP_exact": bool(cached["CAP"] == expected["CAP"]),
                    "POP_exact": bool(cached["POP"] == expected["POP"]),
                    "log_pgdp_abs_error": abs(cached["log_pgdp"] - np.log(cached["GDP"] / cached["POP"])),
                    "log_pcap_abs_error": abs(cached["log_pcap"] - np.log(cached["CAP"] / cached["POP"])),
                }
                rows.append(row)
    if len(rows) != len(SAMPLES) * len(SAMPLE_PROVINCES):
        raise AssertionError("numeric audit sample count changed unexpectedly")
    if not all(row["GDP_exact"] and row["CAP_exact"] and row["POP_exact"] for row in rows):
        raise AssertionError("workbook-to-cache level transform is not exact")
    if not all(np.isclose(row["GDP_factor_observed"], 1000.0, rtol=1e-12, atol=0) and np.isclose(row["CAP_factor_observed"], 1000.0, rtol=1e-12, atol=0) and np.isclose(row["POP_factor_observed"], 100.0, rtol=1e-12, atol=0) for row in rows):
        raise AssertionError("observed factor is not the frozen MATLAB factor")
    if max(row["log_pgdp_abs_error"] for row in rows) > 1e-12 or max(row["log_pcap_abs_error"] for row in rows) > 1e-12:
        raise AssertionError("cached logs contradict model-unit levels")
    return rows


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def contracts_text() -> tuple[str, str]:
    r_contract = """# R estimation versus MATLAB runtime unit contracts

## R_ESTIMATION_UNIT_CONTRACT

`D:\\Rprogramme\\main.r` uses GDP x1000, CAP x1000, and POP x100.  Its active
empirical fields are `GDP`, `R语言计算资本存量`, and `就业人数`.

## MATLAB_RUNTIME_MODEL_UNIT_CONTRACT

`load_GDPdata.m` also uses GDP x1000, CAP x1000, and POP x100, but its active
fields are `GDP`, `总资本存量`, and `常住人口`.

The numeric factors agree.  The capital and population/employment provenance
does not.  This audit keeps those dimensions separate and does not treat the R
estimation data definition as proof of MATLAB runtime source identity.
"""
    python_contract = """# Current Python Owner-A unit contract

`accepted_source_scalars()` fixes `gdp_multiplier=1000.0` and
`pop_multiplier=100.0`.  `mp4c_owner_a_2009_2022.py::build_input` maps
`GDP` x1000, `R语言计算资本存量` x1000, and `就业人数` x100.  It recomputes
`log_pgdp=log(GDP/POP)` and `log_pcap=log(CAP/POP)` from those model levels.

`entry_states()` transfers those vectors without another level scaling:
GDP -> Yt0/Yt; CAP -> Kt0/Kt/Kt_prev and GovInv; POP -> N/Lt/Lt_prev.
The production worker consumes those entry states before its first household
call.  Its `legacy_workbook_rows` serialization divides Yt0/Yt/Kt0/Kt by 1000
and N/Lt by 100, mirroring MATLAB's display conversion.  `final_31x20` remains
in model units.
"""
    return r_contract, python_contract


def comparison_rows() -> list[dict[str, str]]:
    return [
        {"field": "GDP", "matlab_active_source": "GDP", "matlab_source_to_model_factor": "1000", "python_owner_a_source": "GDP", "python_source_to_model_factor": "1000", "classification": "PYTHON_UNIT_TRANSFORM_EXACTLY_MATCHES_MATLAB_RUNTIME", "basis": "literal and workbook-to-cache numeric proof"},
        {"field": "CAP", "matlab_active_source": "总资本存量", "matlab_source_to_model_factor": "1000", "python_owner_a_source": "R语言计算资本存量", "python_source_to_model_factor": "1000", "classification": "PYTHON_UNIT_TRANSFORM_FIELD_SOURCE_DIFFERS_BUT_UNIT_FACTOR_MATCHES", "basis": "same scale, Owner-A source-designated capital provenance differs"},
        {"field": "POP", "matlab_active_source": "常住人口", "matlab_source_to_model_factor": "100", "python_owner_a_source": "就业人数", "python_source_to_model_factor": "100", "classification": "PYTHON_UNIT_TRANSFORM_FIELD_SOURCE_DIFFERS_BUT_UNIT_FACTOR_MATCHES", "basis": "same scale, employment versus resident-population provenance differs"},
    ]


def run(repo: Path, out: Path) -> None:
    if out.exists():
        if any(out.iterdir()):
            raise FileExistsError(f"no-overwrite evidence root is not empty: {out}")
    else:
        out.mkdir(parents=True)
    manifest = source_manifest(repo)
    reads = direct_multiplier_reads()
    numeric = decode_numeric_proof()
    r_contract, python_contract = contracts_text()
    comparison = comparison_rows()
    write_json(out / "matlab_source_identity_manifest.json", manifest)
    write_text(out / "load_GDPdata_full_source_copy_or_hash_receipt.txt", "\n".join(f"{item['sha256']}  {item['path']}" for item in manifest["matlab_sources"]) + "\n")
    write_text(out / "matlab_unit_transform_literal_audit.md", literal_audit_text(reads))
    write_csv(out / "matlab_workbook_to_cache_numeric_scaling_audit.csv", numeric)
    write_text(out / "matlab_cache_to_entry_state_unit_lineage.md", """# Cache to MATLAB entry-state unit lineage

The protected HDF5 cache stores industry-4 arrays with shape 24 x 31.  Cache
metadata records GDP_multiplier=1000 and POP_multiplier=100 for all 15 entries.
`mpHANK_equilibrium_2000.m:27-40` transfers selected rows unchanged: CAP to
Kt0/Kt/Kt_1, POP to N/Lt/Lt_1, GDP to Yt0/Yt, and CAP to GovInv because
GovInv_ratio=1 in `multi_prov_HANK_12sts.m:83`.  Cached logs are exponentiated
only for pcap/pgdp and are not rescaled.  No subsequent multiplier read occurs
before the first HANK household call at `mpHANK_equilibrium_2000.m:72`.
""")
    write_text(out / "matlab_state_to_steady_workbook_output_unit_lineage.md", """# MATLAB state to steady-workbook output unit lineage

`main.m:167-172` writes Yt0/Yt/Kt0/Kt divided by GDP_multiplier (1000) and
N/Lt divided by POP_multiplier (100).  The N column is labeled Lt0 in the
workbook.  `main2.m:164-169` is the same inverse conversion.  Thus workbook
display values restore the loader's original GDP/CAP and POP source units; they
do not show a different runtime unit contract.
""")
    write_text(out / "r_estimation_vs_matlab_runtime_unit_contract.md", r_contract)
    write_text(out / "python_current_unit_contract.md", python_contract)
    write_csv(out / "matlab_python_unit_contract_comparison.csv", comparison)
    verdict = {
        "schema": "CH5_MP4C_MATLAB_UNIT_SCALING_VERDICT_V1",
        "terminal_classification": "MP4C_MATLAB_LOAD_GDPDATA_UNIT_SCALING_AUDIT_PASS__PYTHON_OWNER_A_RUNTIME_UNIT_CONTRACT_CONFIRMED__NO_PATCH__NO_SCIENTIFIC_RERUN",
        "fields": {row["field"]: row["classification"] for row in comparison},
        "numeric_proof": {"sample_count": len(numeric), "provinces": list(SAMPLE_PROVINCES), "calendar_years": [item[0] for item in SAMPLES], "all_level_transforms_exact": True, "max_log_pgdp_abs_error": max(row["log_pgdp_abs_error"] for row in numeric), "max_log_pcap_abs_error": max(row["log_pcap_abs_error"] for row in numeric)},
        "patch": {"required": False, "reason": "No deterministic MATLAB/Python unit-factor mismatch was proven."},
        "2018": "EXISTING_2018_KFE_BLOCKER_UNCHANGED__NO_RERUN_AUTHORIZED",
    }
    write_json(out / "unit_scaling_verdict.json", verdict)
    write_json(out / "zero_science_execution_ledger.json", {"schema": "CH5_MP4C_ZERO_SCIENCE_LEDGER_V1", "actions": ["read MATLAB source text", "parse protected XLSX XML", "read protected HDF5 cache", "write audit evidence"], "scientific_call_budget": {"python_stationary": 0, "household": 0, "HJB": 0, "KFE": 0, "MATLAB_model": 0, "R_PLM": 0, "retry_2018": 0, "shock_IRF_R5_Results": 0}, "observed_scientific_calls": 0})
    evidence_files = []
    for path in sorted(out.iterdir()):
        if path.name == "audit_manifest.json":
            continue
        evidence_files.append({"name": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)})
    write_json(out / "audit_manifest.json", {"schema": "CH5_MP4C_MATLAB_UNIT_SCALING_AUDIT_MANIFEST_V1", "evidence_root": str(out), "files": evidence_files, "verdict": verdict["terminal_classification"]})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    run(args.repo.resolve(), args.out.resolve())


if __name__ == "__main__":
    main()
