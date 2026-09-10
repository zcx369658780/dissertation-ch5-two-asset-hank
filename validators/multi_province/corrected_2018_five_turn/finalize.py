"""Finalize saved five-turn evidence without scientific calls."""
from __future__ import annotations

import csv
import json
import shutil
from collections import Counter
from hashlib import sha256
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[3]
EVIDENCE = Path(r"D:\ProjectTemp\ch5-corrected-2018-five-turn-20260909-001")
REPORT_DIR = REPO / "reports/mp4c_2018_corrected_five_turn_20260909"
REPORT = REPO / "docs/CH5_MP4C_2018_CORRECTED_INPUT_FIVE_TURN_PREFIX_REPORT.md"
EXECUTED = {
    "CORRECTED_2018_FIVE_TURN_PASS__BOUNDED_PREFIX_EXECUTABLE_AND_DIAGNOSTICALLY_STABLE",
    "CORRECTED_2018_FIVE_TURN_DIAGNOSTIC_BLOCKER__KFE_OR_DISTRIBUTION_VALIDITY",
    "CORRECTED_2018_FIVE_TURN_DIAGNOSTIC_BLOCKER__ASSET_TRANSITION_INSTABILITY",
}


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


def manifest_for(root: Path, excluded: set[str]) -> list[dict[str, Any]]:
    records = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = path.relative_to(root).as_posix()
        if rel not in excluded:
            records.append({"path": rel, "bytes": path.stat().st_size, "sha256": file_sha256(path)})
    return records


def asset_transition(rows: list[list[dict[str, Any]]]) -> dict[str, Any]:
    provinces, violent = [], []
    for index in range(31):
        points, previous = [], None
        for turn, turn_rows in enumerate(rows, 1):
            row = turn_rows[index]
            total = float(row["A_plus_B"])
            delta = None if previous is None else total - previous
            ratio = None if previous is None or previous == 0.0 else total / previous
            point = {"turn": turn, "A": row["A"], "B": row["B"], "A_plus_B": total,
                     "delta_A_plus_B": delta, "ratio_A_plus_B": ratio,
                     "rah_minus_rb": row["household_rah"] - row["household_rb"],
                     "kfe_diagnostic_status": row["kfe_diagnostic_status"]}
            if turn >= 4 and ratio is not None and (ratio < 0.2 or ratio > 5.0):
                violent.append({"province": row["province"], "turn": turn, "ratio": ratio})
            points.append(point)
            previous = total
        provinces.append({"province": rows[0][index]["province"], "province_index": index, "turns": points})
    return {"schema": "CH5_CORRECTED_2018_FIVE_TURN_ASSET_TRANSITION_V1",
            "classification_rule": "turn4_or_turn5 A_plus_B ratio below 0.2 or above 5.0 is a violent transition signal",
            "violent_transition_signals": violent, "provinces": provinces, "anhui": provinces[11]}


def finalize() -> None:
    if REPORT.exists() or REPORT_DIR.exists():
        raise FileExistsError("report output already exists")
    terminal = read(EVIDENCE / "terminal_result.json")
    ledger = read(EVIDENCE / "call_ledger.json")
    reproduction = read(EVIDENCE / "predecessor_reproduction.json")
    receipt = read(EVIDENCE / "runtime_input_receipt.json")
    if terminal["verdict"] not in EXECUTED or ledger["counts"]["turns_completed"] != 5:
        raise ValueError("five-turn trajectory did not complete under an executable verdict")
    if not reproduction["passed"] or len(reproduction["turns"]) != 3:
        raise ValueError("accepted turns 1-3 did not reproduce")
    rows = [read(EVIDENCE / f"turn_{turn:02d}/per_province_observables.json") for turn in range(1, 6)]
    summaries = [read(EVIDENCE / f"turn_{turn:02d}/national_summary.json") for turn in range(1, 6)]
    controllers = [read(EVIDENCE / f"turn_{turn:02d}/controller_observables.json") for turn in range(1, 6)]
    all_diagnostics = []
    for turn in range(1, 6):
        for index, province in enumerate(receipt["province_order"]):
            path = EVIDENCE / f"turn_{turn:02d}/household/p{index:02d}_{province}/kfe_distribution_diagnostic.json"
            all_diagnostics.append({"turn": turn, "province_index": index, "province": province, **read(path)})
    asset = asset_transition(rows)
    kfe_summary = {"schema": "CH5_CORRECTED_2018_FIVE_TURN_KFE_DISTRIBUTION_SUMMARY_V1",
        "classifications": dict(Counter(item["classification"] for item in all_diagnostics)),
        "material_blocker_established": any(item["classification"] == "DIAGNOSTIC_ONLY" for item in all_diagnostics),
        "diagnostics": all_diagnostics}
    observables = {f"turn_{turn}": rows[turn - 1] for turn in range(1, 6)}
    anhui = {"schema": "CH5_CORRECTED_2018_FIVE_TURN_ANHUI_FORENSIC_V1",
        "province_identity": {"province": "安徽", "python_index": 11, "matlab_index": 12, "excel_column": "N"},
        "turns": [turn_rows[11] for turn_rows in rows], "asset_transition": asset["anhui"]}
    outputs = {
        "turn_by_turn_observables.json": observables,
        "anhui_forensic.json": anhui,
        "national_transition_summary.json": {"turns": summaries},
        "asset_transition_summary.json": asset,
        "kfe_distribution_diagnostics.json": kfe_summary,
        "controller_adaptation_summary.json": {"turns": controllers},
    }
    for name, value in outputs.items():
        write_json(EVIDENCE / name, value)

    REPORT_DIR.mkdir(parents=True, exist_ok=False)
    copies = set(outputs) | {"runtime_input_receipt.json", "turn1_reproduction.json", "turn2_reproduction.json",
        "turn3_reproduction.json", "predecessor_reproduction.json", "call_ledger.json", "terminal_result.json",
        "pre_science_tests.log", "post_science_tests.log", "static_checks.log"}
    for name in sorted(copies):
        destination = name.removesuffix(".log") + ".txt" if name.endswith(".log") else name
        shutil.copyfile(EVIDENCE / name, REPORT_DIR / destination)
    with (REPORT_DIR / "turn_by_turn_observables.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0][0])); writer.writeheader()
        for turn_rows in rows:
            writer.writerows(turn_rows)

    a = [turn_rows[11] for turn_rows in rows]
    table = "\n".join(f"| {i} | {x['household_rah']:.17g} | {x['firm_ra0']:.17g} | {x['firm_ra_used']:.17g} | {x['firm_wage_raw']:.17g} | {x['firm_wage_used']:.17g} | {x['hjb_iterations']} | {x['C']:.17g} | {x['L']:.17g} | {x['A']:.17g} | {x['B']:.17g} | {x['A_plus_B']:.17g} | {x['nk_gap']:.17g} | {x['yt_gap']:.17g} |" for i, x in enumerate(a, 1))
    t5 = summaries[4]
    d4, d5 = all_diagnostics[93:124], all_diagnostics[124:155]
    report = f"""# Chapter 5 corrected-2018 five-turn bounded prefix

## Verdict

`{terminal['verdict']}`

One fresh trajectory completed exactly five turns. Accepted turns 1-3 reproduced exactly before turn 4 was entered. KFE return is not treated as distribution validity.

## Anhui turns 1-5

| turn | rah | raw ra0 | used ra | raw wage | used wage | HJB iter | C | L | A | B | A+B | nk_gap | yt_gap |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
{table}

## KFE and asset diagnostics

Turn 4 KFE classifications: `{dict(Counter(x['classification'] for x in d4))}`. Turn 5: `{dict(Counter(x['classification'] for x in d5))}`. Full diagnostics include normalized mass, signed density, contaminated-row and source-free residual numerators/scales/ratios, four boundary outward-leak faces, and upper-b face mass. No additional KFE solve was performed.

Anhui turn-3 asset collapse is retained without smoothing. Turn4/5 violent A+B ratio signals under the declared diagnostic rule: `{len(asset['violent_transition_signals'])}` nationally.

## National turn 5

- rate lower/interior/upper: {t5['firm_rate_regions']['lower']}/{t5['firm_rate_regions']['interior']}/{t5['firm_rate_regions']['upper']}
- wage lower/interior/upper: {t5['wage_regions']['lower']}/{t5['wage_regions']['interior']}/{t5['wage_regions']['upper']}
- rah min/median/max: {t5['household_rah']['min']:.17g}/{t5['household_rah']['median']:.17g}/{t5['household_rah']['max']:.17g}
- max nk_gap: {t5['nk_gap']['max']:.17g}
- adaptation gate open: {str(t5['controller']['adaptation_gate_open']).lower()}
- Zt adjustments: {t5['controller']['zt_adjusted_count']}; GovInv actions: {t5['controller']['govinv_action_counts']}

## Calls and boundary

Corrected raw-NBS ledger SHA-256: `{receipt['corrected_source_identities']['corrected_raw_nbs_ledger']['sha256']}`. Scientific process/trajectory: 1/1; completed turns/province updates: {ledger['counts']['turns_completed']}/{ledger['counts']['province_updates_completed']}; HJB/KFE direct solves: {ledger['counts']['hjb_direct_solves']}/{ledger['counts']['kfe_direct_solves']}; labor roots/Brent calls: {ledger['counts']['labor_roots_attempted']}/{ledger['counts']['brentq_calls_attempted']}; scientific retries: 0. MATLAB/GE/annual/IRF/Results/turn6+ calls: 0.

This bounded prefix does not prove steady-state convergence, global admissibility, GE or annual validity, or Results readiness. Turn 6+ authorized: **NO**. Steady state authorized: **NO**. Results eligibility: **FALSE**.
"""
    REPORT.write_text(report, encoding="utf-8", newline="\n")
    repo_records = manifest_for(REPORT_DIR, {"manifest.json", "manifest_readback.json"})
    write_json(REPORT_DIR / "manifest.json", {"files": repo_records})
    write_json(REPORT_DIR / "manifest_readback.json", {"checked_files": len(repo_records), "passed": all((REPORT_DIR / x["path"]).stat().st_size == x["bytes"] and file_sha256(REPORT_DIR / x["path"]) == x["sha256"] for x in repo_records)})
    external_records = manifest_for(EVIDENCE, {"manifest.json", "manifest_readback.json"})
    write_json(EVIDENCE / "manifest.json", {"files": external_records})
    write_json(EVIDENCE / "manifest_readback.json", {"checked_files": len(external_records), "passed": all((EVIDENCE / x["path"]).stat().st_size == x["bytes"] and file_sha256(EVIDENCE / x["path"]) == x["sha256"] for x in external_records)})


if __name__ == "__main__":
    finalize()
