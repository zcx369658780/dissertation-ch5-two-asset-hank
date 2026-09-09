"""Reexecute the accepted persistence-repaired three-turn runner once."""
from __future__ import annotations

import argparse
import json
from hashlib import sha256
from pathlib import Path
from typing import Any

from validators.multi_province.corrected_2018_three_turn import run


REPO = Path(__file__).resolve().parents[3]
REPAIR_RECEIPT = REPO / "reports/mp4c_2018_corrected_three_turn_20260909/post_failure_repair_identity.json"
EXPECTED_RUNNER_SHA256 = "1D53DADBC5D6AD75A695DCD84829C46F657795F368EA25248A5EE13B8C129813"
VERDICT_PASS = "CORRECTED_2018_THREE_TURN_REEXEC_PASS__DIRECT_CORRECTED_RATE_TRANSMISSION_OBSERVED"
VERDICT_TURN1 = "CORRECTED_2018_THREE_TURN_REEXEC_FAIL__TURN1_REPRODUCTION_MISMATCH"
VERDICT_TURN2 = "CORRECTED_2018_THREE_TURN_REEXEC_FAIL__TURN2_REPRODUCTION_MISMATCH"
VERDICT_HOUSEHOLD = "CORRECTED_2018_THREE_TURN_REEXEC_FAIL__HOUSEHOLD_OR_NUMERICAL_BLOCKER"
VERDICT_UPSTREAM = "CORRECTED_2018_THREE_TURN_REEXEC_FAIL__UPSTREAM_STATE_OR_FIRM_BLOCKER"
MISMATCH_SENTINEL = "REEXEC_PREDECESSOR_REPRODUCTION_MISMATCH"


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest().upper()


def verify_repaired_runner() -> dict[str, Any]:
    receipt = json.loads(REPAIR_RECEIPT.read_text(encoding="utf-8"))
    actual = file_sha256(Path(run.__file__))
    source = Path(run.__file__).read_text(encoding="utf-8")
    write_sites = source.count('write_json(root / "predecessor_reproduction.json"')
    sequencing = 'if not reproduction["passed"] or turn_index == 2:' in source
    exact_turns = "for turn_index in (1, 2, 3):" in source
    passed = (
        receipt["repaired_run_source_sha256"] == EXPECTED_RUNNER_SHA256 == actual
        and write_sites == 1 and sequencing and exact_turns
    )
    return {
        "schema": "CH5_CORRECTED_2018_THREE_TURN_REEXEC_REPAIRED_RUNNER_IDENTITY_V1",
        "accepted_repair_receipt": str(REPAIR_RECEIPT.relative_to(REPO)).replace("\\", "/"),
        "accepted_repaired_runner_sha256": receipt["repaired_run_source_sha256"],
        "actual_repaired_runner_sha256": actual,
        "combined_predecessor_write_sites": write_sites,
        "noncolliding_sequencing_guard": sequencing,
        "exact_three_turn_guard": exact_turns,
        "passed": passed,
        "scientific_calls": 0,
    }


def prepare(canonical_workbook: Path, distance_workbook: Path, evidence_root: Path) -> None:
    identity = verify_repaired_runner()
    if not identity["passed"]:
        raise RuntimeError("BLOCKED_REPAIRED_RUNNER_IDENTITY")
    run.prepare(canonical_workbook, distance_workbook, evidence_root)
    run.write_json(Path(evidence_root) / "repaired_runner_identity.json", identity)


def _translate_terminal(root: Path, value: dict[str, Any]) -> dict[str, Any]:
    translated = dict(value)
    if translated.get("verdict") == MISMATCH_SENTINEL:
        turn2 = root / "turn2_reproduction.json"
        translated["verdict"] = VERDICT_TURN2 if turn2.is_file() else VERDICT_TURN1
    translated["schema"] = "CH5_CORRECTED_2018_THREE_TURN_REEXEC_TERMINAL_V1"
    return translated


def execute(evidence_root: Path) -> int:
    root = Path(evidence_root)
    identity = verify_repaired_runner()
    saved = json.loads((root / "repaired_runner_identity.json").read_text(encoding="utf-8"))
    if not identity["passed"] or saved != identity:
        raise RuntimeError("BLOCKED_REPAIRED_RUNNER_IDENTITY")

    original_write_json = run.write_json
    run.VERDICT_PASS = VERDICT_PASS
    run.VERDICT_MISMATCH = MISMATCH_SENTINEL
    run.VERDICT_HOUSEHOLD = VERDICT_HOUSEHOLD
    run.VERDICT_UPSTREAM = VERDICT_UPSTREAM

    def classified_write(path: Path, value: Any) -> None:
        if Path(path).name == "terminal_result.json":
            value = _translate_terminal(root, value)
        original_write_json(path, value)

    run.write_json = classified_write
    try:
        return run.execute(root)
    finally:
        run.write_json = original_write_json


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("canonical_workbook", type=Path)
    prep.add_argument("distance_workbook", type=Path)
    prep.add_argument("evidence_root", type=Path)
    launch = sub.add_parser("run")
    launch.add_argument("evidence_root", type=Path)
    args = parser.parse_args(argv)
    if args.command == "prepare":
        prepare(args.canonical_workbook, args.distance_workbook, args.evidence_root)
        return 0
    return execute(args.evidence_root)


if __name__ == "__main__":
    raise SystemExit(main())
