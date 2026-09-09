"""Publish the terminal three-turn prefix failure without any model call."""
from __future__ import annotations

import csv
import json
import shutil
from hashlib import sha256
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[3]
EVIDENCE = Path(r"D:\ProjectTemp\ch5-corrected-2018-three-turn-20260909-001")
REPORT_DIR = REPO / "reports/mp4c_2018_corrected_three_turn_20260909"
REPORT = REPO / "docs/CH5_MP4C_2018_CORRECTED_INPUT_THREE_TURN_PROPAGATION_REPORT.md"
FAIL = "CORRECTED_2018_THREE_TURN_FAIL__UPSTREAM_STATE_OR_FIRM_BLOCKER"


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


def finalize_failure() -> None:
    if REPORT.exists() or REPORT_DIR.exists():
        raise FileExistsError("report output already exists")
    terminal = read(EVIDENCE / "terminal_result.json")
    failure = read(EVIDENCE / "scientific_failure.json")
    ledger = read(EVIDENCE / "call_ledger.json")
    transition = read(EVIDENCE / "transition_summary.json")
    receipt = read(EVIDENCE / "runtime_input_receipt.json")
    repair = read(EVIDENCE / "post_failure_repair_identity.json")
    turn1_reproduction = read(EVIDENCE / "turn1_reproduction.json")
    turn2_reproduction = read(EVIDENCE / "turn2_reproduction.json")
    if terminal["verdict"] != FAIL:
        raise ValueError("unexpected terminal verdict")
    if failure["type"] != "FileExistsError" or failure["turn"] != 2:
        raise ValueError("unexpected terminal failure")
    if not turn1_reproduction["passed"] or not turn2_reproduction["passed"]:
        raise ValueError("predecessor reproduction did not pass")

    rows1 = read(EVIDENCE / "turn_01/per_province_observables.json")
    rows2 = read(EVIDENCE / "turn_02/per_province_observables.json")
    controllers = [read(EVIDENCE / f"turn_{turn:02d}/controller_observables.json") for turn in (1, 2)]
    predecessor = {
        "schema": "CH5_CORRECTED_2018_PREDECESSOR_REPRODUCTION_POST_FAILURE_CLOSURE_V1",
        "turns": [turn1_reproduction, turn2_reproduction],
        "passed": True,
        "closure_only": True,
    }
    write_json(EVIDENCE / "predecessor_reproduction_post_failure_closure.json", predecessor)
    write_json(EVIDENCE / "turn_by_turn_observables.json", {
        "turn_1": rows1, "turn_2": rows2,
        "turn_3": {"status": "NOT_REACHED", "reason": "EVIDENCE_PERSISTENCE_COLLISION_AFTER_TURN2"},
    })
    write_json(EVIDENCE / "anhui_forensic.json", {
        "schema": "CH5_CORRECTED_2018_THREE_TURN_ANHUI_FORENSIC_PREFIX_FAILURE_V1",
        "province_identity": {"province": "Anhui", "python_index": 11,
                              "matlab_index": 12, "excel_column": "N"},
        "turn_1": rows1[11], "turn_2": rows2[11], "turn_3": None,
        "status": "TURN3_NOT_REACHED",
    })
    write_json(EVIDENCE / "turn3_rah_provenance.json", {
        "schema": "CH5_CORRECTED_2018_TURN3_RAH_PROVENANCE_NOT_REACHED_V1",
        "status": "NOT_REACHED", "value": None, "source_old_ra_vector_sha256": None,
        "manual_override": False, "reason": "EVIDENCE_PERSISTENCE_COLLISION_AFTER_TURN2",
    })
    write_json(EVIDENCE / "controller_observables.json", {
        "schema": "CH5_CORRECTED_2018_THREE_TURN_CONTROLLERS_PREFIX_V1",
        "turns": controllers, "turn_3": "NOT_REACHED",
    })

    REPORT_DIR.mkdir(parents=True, exist_ok=False)
    copies = {
        "runtime_input_receipt.json": "runtime_input_receipt.json",
        "turn1_reproduction.json": "turn1_reproduction.json",
        "turn2_reproduction.json": "turn2_reproduction.json",
        "predecessor_reproduction_post_failure_closure.json": "predecessor_reproduction.json",
        "turn_by_turn_observables.json": "turn_by_turn_observables.json",
        "anhui_forensic.json": "anhui_forensic.json",
        "turn3_rah_provenance.json": "turn3_rah_provenance.json",
        "transition_summary.json": "transition_summary.json",
        "controller_observables.json": "controller_observables.json",
        "call_ledger.json": "call_ledger.json",
        "terminal_result.json": "terminal_result.json",
        "scientific_failure.json": "scientific_failure.json",
        "pre_science_tests.log": "pre_science_tests.txt",
        "post_science_tests.log": "post_science_tests.txt",
        "static_checks.log": "static_checks.txt",
        "post_failure_static_checks.log": "post_failure_static_checks.txt",
        "source_code_identity.json": "source_code_identity.json",
        "post_failure_repair_identity.json": "post_failure_repair_identity.json",
    }
    for source, destination in copies.items():
        shutil.copyfile(EVIDENCE / source, REPORT_DIR / destination)
    with (REPORT_DIR / "turn_by_turn_observables.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows1[0]))
        writer.writeheader()
        writer.writerows(rows1 + rows2)

    counts = ledger["counts"]
    report = f"""# Chapter 5 corrected-2018 three-turn propagation validation

## Verdict

`{terminal['verdict']}`

Terminal classification: `EVIDENCE_PERSISTENCE_COLLISION_AFTER_TURN2__TURN3_NOT_ENTERED`.

The only scientific process completed fresh turns 1 and 2, and both reproduced the accepted two-turn package exactly (`mismatch_count=0`). Before turn 3 entry, the runner attempted a second exclusive write of `predecessor_reproduction.json` and stopped with `FileExistsError`. No model, HJB, KFE, firm, controller, or province update for turn 3 was attempted. Scientific retry was prohibited and was not performed.

## Observed prefix

Anhui turn 1 and turn 2 remain exactly the accepted values, including household `rah` `{rows1[11]['household_rah']:.17g} -> {rows2[11]['household_rah']:.17g}`, raw firm `ra0` `{rows1[11]['firm_ra0']:.17g} -> {rows2[11]['firm_ra0']:.17g}`, used `ra=0.02`, raw wage `{rows1[11]['firm_wage_raw']:.17g} -> {rows2[11]['firm_wage_raw']:.17g}`, and HJB iterations `{rows1[11]['hjb_iterations']} -> {rows2[11]['hjb_iterations']}`.

Turn-3 Anhui `rah`, provenance, firm state, national distributions, gap and adaptation behavior are **NOT CHECKED** because turn 3 was not entered. No inference from the prepared state is substituted for a scientific observation.

## Calls

- scientific processes: {counts['scientific_processes']}
- trajectory attempts/returns: {counts['trajectory_attempts']}/{counts['trajectory_returns']}
- turns entered/completed: {counts['turns_entered']}/{counts['turns_completed']}
- province updates attempted/completed: {counts['province_updates_attempted']}/{counts['province_updates_completed']}
- household/HJB/KFE/firm returns: {counts['household_calls_returned']}/{counts['hjb_returns']}/{counts['kfe_returns']}/{counts['firm_returns']}
- HJB/KFE direct solves: {counts['hjb_direct_solves']}/{counts['kfe_direct_solves']}
- labor roots/Brent: {counts['labor_roots_attempted']}/{counts['brentq_calls_attempted']}
- scientific retries: {counts['scientific_retries']}
- MATLAB/GE/annual/IRF/Results/turn4+: 0/0/0/0/0/0

## Post-failure repair boundary

The executed runner was preserved at SHA-256 `{repair['executed_run_source_sha256']}`. The one-line persistence sequencing defect was repaired and static-tested at SHA-256 `{repair['repaired_run_source_sha256']}`, but the repaired runner was **not scientifically executed**. This repair does not convert the failed task into a PASS or authorize a retry.

Canonical workbook SHA-256: `{receipt['canonical_workbook_sha256']}`. Turn 4 authorized: **NO**. Steady state authorized: **NO**. Results eligibility: **FALSE**.
"""
    REPORT.write_text(report, encoding="utf-8", newline="\n")

    repo_records = manifest_for(REPORT_DIR, {"manifest.json", "manifest_readback.json"})
    write_json(REPORT_DIR / "manifest.json", {
        "schema": "CH5_CORRECTED_2018_THREE_TURN_FAILURE_REPO_MANIFEST_V1", "files": repo_records})
    checked = all((REPORT_DIR / item["path"]).stat().st_size == item["bytes"] and
                  file_sha256(REPORT_DIR / item["path"]) == item["sha256"] for item in repo_records)
    write_json(REPORT_DIR / "manifest_readback.json", {"checked_files": len(repo_records), "passed": checked})

    external_records = manifest_for(EVIDENCE, {"manifest.json", "manifest_readback.json"})
    write_json(EVIDENCE / "manifest.json", {
        "schema": "CH5_CORRECTED_2018_THREE_TURN_FAILURE_EVIDENCE_MANIFEST_V1", "files": external_records})
    external_checked = all((EVIDENCE / item["path"]).stat().st_size == item["bytes"] and
                           file_sha256(EVIDENCE / item["path"]) == item["sha256"] for item in external_records)
    write_json(EVIDENCE / "manifest_readback.json", {
        "checked_files": len(external_records), "passed": external_checked})


if __name__ == "__main__":
    finalize_failure()
