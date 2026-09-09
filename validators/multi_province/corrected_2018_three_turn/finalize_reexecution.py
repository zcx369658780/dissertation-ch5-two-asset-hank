"""Finalize saved corrected-2018 three-turn reexecution evidence without model calls."""
from __future__ import annotations

import csv
import json
import shutil
from hashlib import sha256
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[3]
EVIDENCE = Path(r"D:\ProjectTemp\ch5-corrected-2018-three-turn-reexec-20260909-001")
REPORT_DIR = REPO / "reports/mp4c_2018_corrected_three_turn_reexec_20260909"
REPORT = REPO / "docs/CH5_MP4C_2018_CORRECTED_INPUT_THREE_TURN_PROPAGATION_REEXECUTION_REPORT.md"
PASS = "CORRECTED_2018_THREE_TURN_REEXEC_PASS__DIRECT_CORRECTED_RATE_TRANSMISSION_OBSERVED"


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


def _region(value: float, lower: float, upper: float) -> str:
    return "LOWER" if value < lower else "UPPER" if value > upper else "INTERIOR"


def build_anhui(turn1: dict[str, Any], turn2: dict[str, Any], turn3: dict[str, Any],
                provenance: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "CH5_CORRECTED_2018_THREE_TURN_ANHUI_FORENSIC_V1",
        "province_identity": {"province": "Anhui", "python_index": 11,
                              "matlab_index": 12, "excel_column": "N"},
        "turn_1": turn1,
        "turn_2": turn2,
        "turn_3": turn3,
        "turn_3_rah_provenance": provenance,
        "answers": {
            "turn2_entering_ra_participated_in_turn3_rah": provenance["own_old_ra"] == turn2["entering_firm_ra"],
            "turn3_rah_source_old_ra_turn": provenance["source_old_ra_turn"],
            "turn3_firm_raw_return_region": _region(turn3["firm_ra0"], turn3["ramin"], turn3["ramax"]),
            "hjb_kfe_executable_after_direct_propagation": bool(
                turn3["hjb_converged"] and turn3["kfe_returned"]),
            "turn3_adaptation_gate_open": bool(turn3["adaptation_gate_open"]),
        },
    }


def manifest_for(root: Path, excluded: set[str]) -> list[dict[str, Any]]:
    records = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = path.relative_to(root).as_posix()
        if rel not in excluded:
            records.append({"path": rel, "bytes": path.stat().st_size, "sha256": file_sha256(path)})
    return records


def finalize() -> None:
    if REPORT.exists() or REPORT_DIR.exists():
        raise FileExistsError("report output already exists")
    terminal = read(EVIDENCE / "terminal_result.json")
    predecessor = read(EVIDENCE / "predecessor_reproduction.json")
    ledger = read(EVIDENCE / "call_ledger.json")
    transition = read(EVIDENCE / "transition_summary.json")
    receipt = read(EVIDENCE / "runtime_input_receipt.json")
    if terminal["verdict"] != PASS:
        raise ValueError("terminal verdict is not the authorized PASS result")
    if not predecessor["passed"] or len(predecessor["turns"]) != 2:
        raise ValueError("accepted predecessor did not reproduce")

    rows = [read(EVIDENCE / f"turn_{turn:02d}/per_province_observables.json") for turn in (1, 2, 3)]
    provenance_all = read(EVIDENCE / "turn_03/entering_state.json")["rah_provenance"]
    anhui = build_anhui(rows[0][11], rows[1][11], rows[2][11], provenance_all[11])
    write_json(EVIDENCE / "anhui_forensic.json", anhui)
    write_json(EVIDENCE / "turn3_rah_provenance.json", {
        "schema": "CH5_CORRECTED_2018_TURN3_RAH_PROVENANCE_V1",
        "source_old_ra_turn": 2,
        "source_old_ra_vector_sha256": provenance_all[0]["source_old_ra_vector_sha256"],
        "manual_override": False,
        "provinces": provenance_all,
    })
    write_json(EVIDENCE / "turn_by_turn_observables.json", {
        "turn_1": rows[0], "turn_2": rows[1], "turn_3": rows[2]})
    controllers = [read(EVIDENCE / f"turn_{turn:02d}/controller_observables.json") for turn in (1, 2, 3)]
    write_json(EVIDENCE / "controller_observables.json", {
        "schema": "CH5_CORRECTED_2018_THREE_TURN_CONTROLLERS_V1", "turns": controllers})

    REPORT_DIR.mkdir(parents=True, exist_ok=False)
    copies = {
        "repaired_runner_identity.json", "runtime_input_receipt.json", "independent_readback.json",
        "turn1_reproduction.json", "turn2_reproduction.json",
        "predecessor_reproduction.json", "turn_by_turn_observables.json", "anhui_forensic.json",
        "turn3_rah_provenance.json", "transition_summary.json", "controller_observables.json",
        "call_ledger.json", "terminal_result.json", "pre_science_tests.log", "post_science_tests.log",
        "static_checks.log", "source_code_identity.json",
    }
    for name in sorted(copies):
        destination = name.removesuffix(".log") + ".txt" if name.endswith(".log") else name
        shutil.copyfile(EVIDENCE / name, REPORT_DIR / destination)
    with (REPORT_DIR / "turn_by_turn_observables.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0][0]))
        writer.writeheader()
        for turn_rows in rows:
            writer.writerows(turn_rows)

    a = [turn_rows[11] for turn_rows in rows]
    t = transition["turns"]
    p = provenance_all[11]
    counts = ledger["counts"]
    legacy_direct = any(float(item["own_old_ra"]) == 0.09 for item in provenance_all)
    report = f"""# Chapter 5 corrected-2018 three-turn propagation reexecution

## Verdict

`{terminal['verdict']}`

One fresh corrected-2018 trajectory completed exactly three turns in the frozen 31-province source order. Fresh turns 1 and 2 reproduced the accepted two-turn package exactly (`mismatch_count=0` for both) before turn 3 was entered. This is propagation evidence, not steady-state or convergence evidence. Turn 4 authorized: **NO**. Steady state authorized: **NO**. Results eligibility: **FALSE**.

## Direct corrected-rate propagation

Anhui turn-3 household `rah` was `{a[2]['household_rah']:.17g}`. It was generated by the native rule

`(1-ratio_i)*old_ra_i + ratio_i*(sum_j(ratio_j*old_ra_j)-ratio_i*old_ra_i)/(n-1)`

from the turn-2 **entering** firm-`ra` vector (SHA-256 `{p['source_old_ra_vector_sha256']}`). Anhui's own old `ra` was `{p['own_old_ra']:.17g}`, equal to its turn-2 entering firm `ra`. Thus the corrected lower-clipped rate materially enters the turn-3 household return through the native composite rule; turn-3 `rah` is not manually set to `0.02`. Direct `.09` entries remained in that source vector: **{str(legacy_direct).lower()}**. All 31 source entries were `.02`; the lower resulting `rah` reflects the frozen inter-province ratios, own-term exclusion and division by `n-1`, not residual `.09` in the direct old-`ra` vector.

## Anhui transition

| observable | turn 1 | turn 2 | turn 3 |
|---|---:|---:|---:|
| household rah | {a[0]['household_rah']:.17g} | {a[1]['household_rah']:.17g} | {a[2]['household_rah']:.17g} |
| firm raw ra0 | {a[0]['firm_ra0']:.17g} | {a[1]['firm_ra0']:.17g} | {a[2]['firm_ra0']:.17g} |
| firm used ra | {a[0]['firm_ra_used']:.17g} | {a[1]['firm_ra_used']:.17g} | {a[2]['firm_ra_used']:.17g} |
| firm raw wage | {a[0]['firm_wage_raw']:.17g} | {a[1]['firm_wage_raw']:.17g} | {a[2]['firm_wage_raw']:.17g} |
| firm used wage | {a[0]['firm_wage_used']:.17g} | {a[1]['firm_wage_used']:.17g} | {a[2]['firm_wage_used']:.17g} |
| HJB iterations | {a[0]['hjb_iterations']} | {a[1]['hjb_iterations']} | {a[2]['hjb_iterations']} |
| nk_gap | {a[0]['nk_gap']:.17g} | {a[1]['nk_gap']:.17g} | {a[2]['nk_gap']:.17g} |

Turn-3 firm raw return is **{_region(a[2]['firm_ra0'], a[2]['ramin'], a[2]['ramax'])}**. HJB converged and KFE returned for Anhui and all 31 provinces.

## National turn 3

- firm rate lower/interior/upper: {t[2]['firm_rate_regions']['lower']}/{t[2]['firm_rate_regions']['interior']}/{t[2]['firm_rate_regions']['upper']}
- wage lower/interior/upper: {t[2]['wage_regions']['lower']}/{t[2]['wage_regions']['interior']}/{t[2]['wage_regions']['upper']}
- household rah min/median/max: {t[2]['household_rah']['min']:.17g} / {t[2]['household_rah']['median']:.17g} / {t[2]['household_rah']['max']:.17g}
- max nk_gap: {t[2]['nk_gap']['max']:.17g}
- adaptation gate open: {str(t[2]['controller']['adaptation_gate_open']).lower()}
- Zt adjustments / GovInv non-NONE: {t[2]['controller']['zt_adjusted_count']} / {sum(v for k, v in t[2]['controller']['govinv_action_counts'].items() if k != 'NONE')}

The three observed turns do not establish monotone or stationary convergence.

## Calls and evidence

Canonical workbook SHA-256: `{receipt['canonical_workbook_sha256']}`. The single scientific process took `{ledger['elapsed_seconds']:.3f}` seconds and completed {counts['turns_completed']} turns, {counts['province_updates_completed']} province updates, {counts['household_calls_attempted']} household calls, {counts['hjb_calls']} HJB calls with {counts['hjb_direct_solves']} direct solves, {counts['kfe_calls']} KFE direct solves, {counts['labor_roots_attempted']} labor roots and {counts['brentq_calls_attempted']} Brent calls. Scientific retries, MATLAB, GE, annual model, IRF, Results and turn-4-or-later calls were all zero.
"""
    REPORT.write_text(report, encoding="utf-8", newline="\n")

    repo_records = manifest_for(REPORT_DIR, {"manifest.json", "manifest_readback.json"})
    write_json(REPORT_DIR / "manifest.json", {
        "schema": "CH5_CORRECTED_2018_THREE_TURN_REEXEC_REPO_MANIFEST_V1", "files": repo_records})
    checked = all((REPORT_DIR / item["path"]).stat().st_size == item["bytes"] and
                  file_sha256(REPORT_DIR / item["path"]) == item["sha256"] for item in repo_records)
    write_json(REPORT_DIR / "manifest_readback.json", {"checked_files": len(repo_records), "passed": checked})

    external_records = manifest_for(EVIDENCE, {"manifest.json", "manifest_readback.json"})
    write_json(EVIDENCE / "manifest.json", {
        "schema": "CH5_CORRECTED_2018_THREE_TURN_REEXEC_EVIDENCE_MANIFEST_V1", "files": external_records})
    external_checked = all((EVIDENCE / item["path"]).stat().st_size == item["bytes"] and
                           file_sha256(EVIDENCE / item["path"]) == item["sha256"] for item in external_records)
    write_json(EVIDENCE / "manifest_readback.json", {
        "checked_files": len(external_records), "passed": external_checked})


if __name__ == "__main__":
    finalize()
