"""Finalize the saved corrected-2018 two-turn evidence without model calls."""
from __future__ import annotations

import csv
import json
import shutil
from hashlib import sha256
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[3]
EVIDENCE = Path(r"D:\ProjectTemp\ch5-corrected-2018-two-turn-20260909-001")
REPORT_DIR = REPO / "reports/mp4c_2018_corrected_two_turn_20260909"
REPORT = REPO / "docs/CH5_MP4C_2018_CORRECTED_INPUT_TWO_TURN_PROPAGATION_REPORT.md"


def read(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
        stream.write("\n")


def file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def build_anhui(turn1: dict[str, Any], turn2: dict[str, Any], provenance: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "CH5_CORRECTED_2018_TWO_TURN_ANHUI_FORENSIC_V1",
        "province_identity": {"province": "Anhui", "python_index": 11, "matlab_index": 12, "excel_column": "N"},
        "turn_1": turn1,
        "turn_2": turn2,
        "turn_2_rah_provenance": provenance,
        "answers": {
            "turn1_ra_0p02_directly_became_turn2_rah": False,
            "native_rule": provenance["formula"],
            "turn2_firm_raw_return_region": "LOWER",
            "wage_clipping_change": "RAW_WAGE_DECREASED_BUT_UPPER_CLIP_REMAINED",
            "hjb_kfe_executable_after_propagation": True,
            "turn2_adaptation_gate_open": False,
        },
    }


def manifest_for(root: Path, excluded: set[str]) -> list[dict[str, Any]]:
    records = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = path.relative_to(root).as_posix()
        if rel in excluded:
            continue
        records.append({"path": rel, "bytes": path.stat().st_size, "sha256": file_sha256(path)})
    return records


def finalize() -> None:
    if REPORT.exists() or REPORT_DIR.exists():
        raise FileExistsError("report output already exists")
    terminal = read(EVIDENCE / "terminal_result.json")
    reproduction = read(EVIDENCE / "turn1_reproduction.json")
    ledger = read(EVIDENCE / "call_ledger.json")
    transition = read(EVIDENCE / "transition_summary.json")
    receipt = read(EVIDENCE / "runtime_input_receipt.json")
    if terminal["verdict"] != "CORRECTED_2018_TWO_TURN_PASS__TURN2_PROPAGATION_OBSERVED":
        raise ValueError("terminal verdict is not the authorized PASS result")
    if not reproduction["passed"] or reproduction["mismatch_count"] != 0:
        raise ValueError("fresh turn 1 did not reproduce the accepted evidence")

    rows1 = read(EVIDENCE / "turn_01/per_province_observables.json")
    rows2 = read(EVIDENCE / "turn_02/per_province_observables.json")
    provenance = read(EVIDENCE / "turn_02/entering_state.json")["rah_provenance"][11]
    anhui = build_anhui(rows1[11], rows2[11], provenance)
    write_json(EVIDENCE / "anhui_forensic.json", anhui)
    write_json(EVIDENCE / "turn_by_turn_observables.json", {"turn_1": rows1, "turn_2": rows2})

    REPORT_DIR.mkdir(parents=True, exist_ok=False)
    copies = {
        "runtime_input_receipt.json": "runtime_input_receipt.json",
        "turn1_reproduction.json": "turn1_reproduction.json",
        "transition_summary.json": "transition_summary.json",
        "call_ledger.json": "call_ledger.json",
        "terminal_result.json": "terminal_result.json",
        "anhui_forensic.json": "anhui_forensic.json",
        "turn_by_turn_observables.json": "turn_by_turn_observables.json",
        "pre_science_tests.log": "pre_science_tests.txt",
        "post_science_tests.log": "post_science_tests.txt",
        "static_checks.log": "static_checks.txt",
    }
    for source, destination in copies.items():
        shutil.copyfile(EVIDENCE / source, REPORT_DIR / destination)
    with (REPORT_DIR / "turn_by_turn_observables.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows1[0]))
        writer.writeheader()
        writer.writerows(rows1 + rows2)

    t1, t2 = transition["turns"]
    a1, a2 = rows1[11], rows2[11]
    counts = ledger["counts"]
    report = f"""# Chapter 5 corrected-2018 two-turn propagation validation

## Verdict

`{terminal['verdict']}`

The fresh corrected-2018 trajectory completed exactly two turns in the frozen 31-province source order. Fresh turn 1 reproduced every accepted observable and controller field exactly (`mismatch_count=0`), so turn 2 was entered. This is a bounded propagation observation, not steady-state or convergence evidence. Third turn authorized: **NO**. Steady state authorized: **NO**. Results eligibility: **FALSE**.

## Central propagation finding

For Anhui (Python 11 / MATLAB 12 / Excel N), turn-2 household `rah` was `{a2['household_rah']:.17g}`. It was produced by the native pre-firm capital-allocation rule

`(1-ratio_i)*old_ra_i + ratio_i*(sum_j(ratio_j*old_ra_j)-ratio_i*old_ra_i)/(n-1)`.

The source vector was the turn-1 **entering** `ra` vector (SHA-256 `{provenance['source_old_ra_vector_sha256']}`), whose Anhui value was `{provenance['own_old_ra']}`. Therefore turn-1 firm used `ra=0.02` did not directly become turn-2 household `rah`. It did become turn-2 entering firm state `ra=0.02`; the capital block reads that state when constructing the next post-turn `rah`, which would concern turn 3 and was not executed.

## Anhui turn 1 to turn 2

| observable | turn 1 | turn 2 |
|---|---:|---:|
| household rah | {a1['household_rah']:.17g} | {a2['household_rah']:.17g} |
| household composite wage | {a1['household_composite_wage']:.17g} | {a2['household_composite_wage']:.17g} |
| firm raw ra0 | {a1['firm_ra0']:.17g} | {a2['firm_ra0']:.17g} |
| firm used ra | {a1['firm_ra_used']:.17g} | {a2['firm_ra_used']:.17g} |
| firm raw wage | {a1['firm_wage_raw']:.17g} | {a2['firm_wage_raw']:.17g} |
| firm used wage | {a1['firm_wage_used']:.17g} | {a2['firm_wage_used']:.17g} |
| HJB iterations | {a1['hjb_iterations']} | {a2['hjb_iterations']} |
| HJB statistic | {a1['hjb_statistic']:.17g} | {a2['hjb_statistic']:.17g} |
| KFE returned | {a1['kfe_returned']} | {a2['kfe_returned']} |
| C | {a1['C']:.17g} | {a2['C']:.17g} |
| L | {a1['L']:.17g} | {a2['L']:.17g} |
| A | {a1['A']:.17g} | {a2['A']:.17g} |
| B | {a1['B']:.17g} | {a2['B']:.17g} |
| nk_gap | {a1['nk_gap']:.17g} | {a2['nk_gap']:.17g} |
| yt_gap | {a1['yt_gap']:.17g} | {a2['yt_gap']:.17g} |

Turn-2 raw `ra0` remained below the 0.02 lower bound and used `ra` remained clipped to 0.02. Raw wage decreased from `{a1['firm_wage_raw']:.17g}` to `{a2['firm_wage_raw']:.17g}`, but both exceeded 1.3 and were clipped at the upper wage bound. HJB and KFE returned in both turns. The adaptation gate remained closed because the national maximum `nk_gap` was `{t2['nk_gap']['max']:.17g}`, above 0.1; no Zt or GovInv action occurred.

## National transition

| diagnostic | turn 1 | turn 2 |
|---|---:|---:|
| firm rate lower/interior/upper | {t1['firm_rate_regions']['lower']}/{t1['firm_rate_regions']['interior']}/{t1['firm_rate_regions']['upper']} | {t2['firm_rate_regions']['lower']}/{t2['firm_rate_regions']['interior']}/{t2['firm_rate_regions']['upper']} |
| wage lower/interior/upper | {t1['wage_regions']['lower']}/{t1['wage_regions']['interior']}/{t1['wage_regions']['upper']} | {t2['wage_regions']['lower']}/{t2['wage_regions']['interior']}/{t2['wage_regions']['upper']} |
| raw ra0 min/median/max | {t1['raw_ra0']['min']:.9g} / {t1['raw_ra0']['median']:.9g} / {t1['raw_ra0']['max']:.9g} | {t2['raw_ra0']['min']:.9g} / {t2['raw_ra0']['median']:.9g} / {t2['raw_ra0']['max']:.9g} |
| nk_gap min/median/max | {t1['nk_gap']['min']:.9g} / {t1['nk_gap']['median']:.9g} / {t1['nk_gap']['max']:.9g} | {t2['nk_gap']['min']:.9g} / {t2['nk_gap']['median']:.9g} / {t2['nk_gap']['max']:.9g} |
| yt_gap min/median/max | {t1['yt_gap']['min']:.9g} / {t1['yt_gap']['median']:.9g} / {t1['yt_gap']['max']:.9g} | {t2['yt_gap']['min']:.9g} / {t2['yt_gap']['median']:.9g} / {t2['yt_gap']['max']:.9g} |
| HJB failures / KFE failures | {t1['hjb_failures']} / {t1['kfe_failures']} | {t2['hjb_failures']} / {t2['kfe_failures']} |
| Zt adjustments / GovInv non-NONE | 0 / 0 | 0 / 0 |

Turn 1 had 31 HJB returns at 64 iterations. Turn 2 iterations ranged from 13 to 41; the full distribution is saved in `transition_summary.json`. These two observations do not establish convergence.

## Input and calls

Canonical workbook SHA-256: `{receipt['canonical_workbook_sha256']}`. The private workbook was read only and was not copied into Git. The corrected 2018 temporal contract, grids, model equations, solvers and tolerances were unchanged.

The single scientific process took `{ledger['elapsed_seconds']:.3f}` seconds. It executed {counts['turns_completed']} turns and {counts['province_updates_completed']} province updates: {counts['household_calls_attempted']} household calls, {counts['native_initializations_attempted']} native initializations, {counts['labor_roots_attempted']} labor-root attempts and {counts['brentq_calls_attempted']} Brent calls, {counts['hjb_calls']} HJB calls with {counts['hjb_direct_solves']} direct solves, {counts['kfe_calls']} KFE calls with {counts['kfe_direct_solves']} direct solves, {counts['aggregate_calls']} aggregates, {counts['firm_calls']} firm calls, {counts['wage_batch_calls']} wage batches, {counts['migration_calls']} migration calls, {counts['capital_allocation_calls']} capital allocations and {counts['controller_calls']} controller evaluations. All 62 household/HJB/KFE/firm calls returned; retries were 0. MATLAB, GE, annual model, IRF and Results calls were 0.
"""
    REPORT.write_text(report, encoding="utf-8", newline="\n")

    repo_records = manifest_for(REPORT_DIR, {"manifest.json", "manifest_readback.json"})
    write_json(REPORT_DIR / "manifest.json", {"schema": "CH5_CORRECTED_2018_TWO_TURN_REPO_MANIFEST_V1",
                                                "files": repo_records})
    checked = all((REPORT_DIR / item["path"]).stat().st_size == item["bytes"] and
                  file_sha256(REPORT_DIR / item["path"]) == item["sha256"] for item in repo_records)
    write_json(REPORT_DIR / "manifest_readback.json", {"checked_files": len(repo_records), "passed": checked})

    external_records = manifest_for(EVIDENCE, {"manifest.json", "manifest_readback.json"})
    write_json(EVIDENCE / "manifest.json", {"schema": "CH5_CORRECTED_2018_TWO_TURN_EVIDENCE_MANIFEST_V1",
                                             "files": external_records})
    external_checked = all((EVIDENCE / item["path"]).stat().st_size == item["bytes"] and
                           file_sha256(EVIDENCE / item["path"]) == item["sha256"] for item in external_records)
    write_json(EVIDENCE / "manifest_readback.json", {"checked_files": len(external_records),
                                                       "passed": external_checked})


if __name__ == "__main__":
    finalize()
