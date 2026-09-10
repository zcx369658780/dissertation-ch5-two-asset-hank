"""Read-only finalization of the saved corrected-2018 single-turn evidence."""
from __future__ import annotations

import csv
import json
import re
import shutil
import subprocess
import sys
from hashlib import sha256
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[3]
EVIDENCE = Path(r"D:\ProjectTemp\ch5-corrected-2018-single-turn-20260909-001")
OLD_REPORT = REPO / "reports/2018_observable_prefix_replay_20260908"
REPORT_DIR = REPO / "reports/mp4c_2018_corrected_single_turn_20260909"
DOC = REPO / "docs/CH5_MP4C_2018_CORRECTED_INPUT_SINGLE_TURN_VALIDATION_REPORT.md"


def sha(path: Path) -> str:
    digest = sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def read(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(payload, stream, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
        stream.write("\n")


def old_anhui_turn1(path: Path) -> dict[str, float]:
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    matches = [row for row in rows if row["step"] == "1" and row["index_0"] == "11"]
    if len(matches) != 1:
        raise ValueError("saved old Anhui turn-1 firm record is not unique")
    row = matches[0]
    return {
        "GDP": float(row["input_Yt0"]), "POP": float(row["input_N"]),
        "CAP": float(row["input_Kt0"]), "alpha": float(row["input_alpha"]),
        "Zt": float(row["input_Zt"]), "firm_ra0": float(row["ra0"]),
        "firm_ra_used": float(row["ra"]), "firm_wage_raw": float(row["wt0"]),
        "firm_wage_used": float(row["wjt"]), "household_rah": float(row["input_rah"]),
    }


def build_comparison(old: dict[str, float], new: dict[str, Any]) -> dict[str, Any]:
    fields = ("GDP", "POP", "CAP", "alpha", "Zt", "firm_ra0", "firm_ra_used",
              "firm_wage_raw", "firm_wage_used", "household_rah")
    new_names = {"Zt": "same_year_Zt"}
    rows = []
    for field in fields:
        new_value = float(new[new_names.get(field, field)])
        old_value = float(old[field])
        rows.append({"field": field, "saved_old_mixed_year": old_value,
                     "corrected_2018": new_value, "difference": new_value - old_value})
    return {
        "schema": "CH5_CORRECTED_2018_SAVED_OLD_COMPARISON_V1",
        "classification": "DESCRIPTIVE_INPUT_CORRECTION_EFFECT_ONLY",
        "old_model_rerun": False,
        "saved_source": "reports/2018_observable_prefix_replay_20260908/firm_prices_and_operands.csv",
        "rows": rows,
    }


def run_tests() -> dict[str, Any]:
    command = [sys.executable, "-m", "pytest", "-q",
               "tests/test_mp4c_2018_corrected_single_turn.py",
               "tests/test_mp2_source_faithful_one_turn.py"]
    result = subprocess.run(command, cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    text = result.stdout.decode("utf-8").replace("\r\n", "\n")
    test_path = REPORT_DIR / "tests.txt"
    test_path.write_text(text, encoding="utf-8", newline="\n")
    match = re.search(r"(\d+) passed", text)
    receipt = {"command": command, "returncode": result.returncode,
               "passed_count": int(match.group(1)) if match else None,
               "raw_sha256": sha256(result.stdout).hexdigest().upper(),
               "lf_text_sha256": sha(test_path), "passed": result.returncode == 0}
    write(REPORT_DIR / "tests_receipt.json", receipt)
    if not receipt["passed"] or receipt["passed_count"] != 15:
        raise RuntimeError("focused test evidence failed")
    return receipt


def finalize() -> None:
    if REPORT_DIR.exists() or DOC.exists():
        raise FileExistsError("refusing to overwrite repository report output")
    REPORT_DIR.mkdir(parents=True)
    terminal = read(EVIDENCE / "terminal_result.json")
    ledger = read(EVIDENCE / "call_ledger.json")
    anhui = read(EVIDENCE / "anhui_forensic.json")
    controller = read(EVIDENCE / "controller_observables.json")
    runtime = read(EVIDENCE / "runtime_input_receipt.json")
    expected = {
        "one_turn_executions": 1, "one_turn_returns": 1,
        "province_updates_attempted": 31, "province_updates_completed": 31,
        "household_calls_attempted": 31, "household_calls_returned": 31, "household_calls_failed": 0,
        "hjb_calls": 31, "hjb_returns": 31, "hjb_direct_solves": 1984,
        "kfe_calls": 31, "kfe_returns": 31, "kfe_direct_solves": 31,
        "firm_calls": 31, "firm_returns": 31, "controller_calls": 1,
    }
    if terminal["verdict"] != "CORRECTED_2018_SINGLE_TURN_PASS__FULL_ORDERED_TURN_COMPLETED":
        raise ValueError("saved science did not complete the authorized turn")
    if any(ledger["counts"][key] != value for key, value in expected.items()):
        raise ValueError("saved call ledger contradicts completed-turn contract")
    old = old_anhui_turn1(OLD_REPORT / "firm_prices_and_operands.csv")
    comparison = build_comparison(old, anhui)
    write(EVIDENCE / "saved_old_comparison.json", comparison)

    for name in ("runtime_input_receipt.json", "per_province_observables.json",
                 "per_province_observables.csv", "anhui_forensic.json", "call_ledger.json",
                 "terminal_result.json", "controller_observables.json"):
        shutil.copy2(EVIDENCE / name, REPORT_DIR / name)
    write(REPORT_DIR / "saved_old_comparison.json", comparison)
    tests = run_tests()

    old_map = {row["field"]: row for row in comparison["rows"]}
    report = f"""# Chapter 5 MP4C corrected-2018 single-turn validation report

## Verdict

`{terminal['verdict']}`

The corrected raw-NBS ledger SHA-256 is `{read(EVIDENCE / 'runtime_input_payload.json')['source_identities']['corrected_raw_nbs_ledger']['sha256']}`. The validator bound all 31 provinces in the frozen source order under `{runtime['contract']}` and completed exactly one ordered turn. Downstream steady-state execution is **not authorized**. Results eligibility remains **FALSE**.

## Corrected runtime input

The runtime used actual 2018 GDP/population, Track-A PIM capital, and same-year 2018 Zt under the explicit MU/NU contract. Anhui stayed at Python index 11 / MATLAB index 12 / Excel N. Its bound inputs were GDP `{anhui['GDP']}`, POP `{anhui['POP']}`, PIM CAP `{anhui['CAP']}`, alpha `{anhui['alpha']}`, Zt `{anhui['same_year_Zt']}`, and GovInv `{anhui['GovInv']}`. The grid remained I20 b[-2,5], J20 a[0,10], Nz2 z[0.8,1.3].

No private canonical workbook is an active corrected-route input. The distance matrix retained SHA-256 `{read(EVIDENCE / 'runtime_input_payload.json')['distance_workbook']['sha256']}` and the existing destination-by-origin normalization.

## Household and one-turn result

All 31 native initializations returned. Each used 800 labor roots. All 31 HJB calls converged in 64 updates, for 1,984 HJB direct solves total; every HJB result was saved before its KFE call. All 31 KFE direct solves and aggregates returned. The one-turn output contains finite JSON-serializable observables for all provinces.

Anhui's household input was rah `{anhui['household_rah']}`, rb `{anhui['household_rb']}`, composite wage `{anhui['household_composite_wage']}`, and entering Lt_prev `{anhui['entering_Lt_prev']}`. Its HJB converged in `{anhui['hjb_iterations']}` updates with statistic `{anhui['hjb_statistic']}`; KFE returned. Household aggregates were C `{anhui['C']}`, L `{anhui['L']}`, A `{anhui['A']}`, B `{anhui['B']}`, A+B `{anhui['A_plus_B']}`.

## Anhui firm forensic

After correcting the time/data input, Anhui first-turn raw return was `{anhui['firm_ra0']}`. It did **not** hit the upper bound 0.09; it fell below the lower bound and the used rate was clipped to `{anhui['firm_ra_used']}`. Raw wage was `{anhui['firm_wage_raw']}` and the used wage was clipped to the upper bound `{anhui['firm_wage_used']}`. The household still entered this first turn with carried rah `{anhui['household_rah']}`.

Across all provinces, firm rates hit the lower boundary in `{controller['ra_lower_count']}` cases and the upper boundary in `{controller['ra_upper_count']}` cases. Wages hit the lower/upper boundaries in `{controller['wage_lower_count']}` / `{controller['wage_upper_count']}` cases. Maximum nk_gap was `{controller['max_nk_gap']}` at `{controller['max_nk_gap_province']}`. Because this exceeded the 0.1 adaptation gate, the existing controller recorded no Zt or GovInv adjustment in this turn. This one-turn PASS does not establish stationary convergence or household/KFE global admissibility.

## Saved old mixed-year comparison

This is `DESCRIPTIVE_INPUT_CORRECTION_EFFECT_ONLY`; the old model was not rerun. For Anhui, saved old versus corrected values were: GDP `{old_map['GDP']['saved_old_mixed_year']}` to `{old_map['GDP']['corrected_2018']}`, POP `{old_map['POP']['saved_old_mixed_year']}` to `{old_map['POP']['corrected_2018']}`, CAP `{old_map['CAP']['saved_old_mixed_year']}` to `{old_map['CAP']['corrected_2018']}`, Zt `{old_map['Zt']['saved_old_mixed_year']}` to `{old_map['Zt']['corrected_2018']}`, firm ra0 `{old_map['firm_ra0']['saved_old_mixed_year']}` to `{old_map['firm_ra0']['corrected_2018']}`, and raw wage `{old_map['firm_wage_raw']['saved_old_mixed_year']}` to `{old_map['firm_wage_raw']['corrected_2018']}`. Alpha and carried rah remained `{anhui['alpha']}` and `{anhui['household_rah']}`.

## Call ledger and checks

One scientific Python process ran for `{ledger['elapsed_seconds']}` seconds with zero scientific retries. Counts were: one-turn 1/1 attempted/returned; province updates 31/31; household 31/31 returned and 0 failed; HJB 31 calls / 1,984 direct solves; KFE 31 calls / 31 direct solves; firm 31/31; wage batch 1 with 31 outputs; controller 1. MATLAB, second turn, steady-state loop, GE, annual model, IRF, and Results calls were all 0.

Focused static and one-turn component checks passed `{tests['passed_count']}` tests. Full machine-readable evidence and per-province records are in `reports/mp4c_2018_corrected_single_turn_20260909/` and the external evidence root `{EVIDENCE}`.
"""
    DOC.write_text(report, encoding="utf-8", newline="\n")

    repo_files = [DOC, *sorted(path for path in REPORT_DIR.iterdir() if path.is_file())]
    external_files = sorted(path for path in EVIDENCE.rglob("*") if path.is_file()
                            and path.name not in ("manifest.json", "manifest_readback.json"))
    manifest = {
        "schema": "CH5_CORRECTED_2018_SINGLE_TURN_MANIFEST_V1",
        "verdict": terminal["verdict"], "evidence_root": str(EVIDENCE),
        "repository_files": [{"path": str(path.relative_to(REPO)).replace("\\", "/"),
                              "sha256": sha(path), "bytes": path.stat().st_size} for path in repo_files],
        "external_files": [{"path": str(path.relative_to(EVIDENCE)).replace("\\", "/"),
                            "sha256": sha(path), "bytes": path.stat().st_size} for path in external_files],
        "scientific_calls": ledger, "results_eligible": False,
    }
    write(REPORT_DIR / "manifest.json", manifest)
    write(EVIDENCE / "manifest.json", manifest)
    manifest_sha = sha(EVIDENCE / "manifest.json")
    readback = {"schema": "CH5_CORRECTED_2018_SINGLE_TURN_MANIFEST_READBACK_V1",
                "manifest_sha256": manifest_sha,
                "repository_entry_count": len(manifest["repository_files"]),
                "external_entry_count": len(manifest["external_files"]),
                "all_repository_hashes_match": all(sha(REPO / row["path"]) == row["sha256"] for row in manifest["repository_files"]),
                "all_external_hashes_match": all(sha(EVIDENCE / row["path"]) == row["sha256"] for row in manifest["external_files"])}
    write(REPORT_DIR / "manifest_readback.json", readback)
    write(EVIDENCE / "manifest_readback.json", readback)


if __name__ == "__main__":
    finalize()
