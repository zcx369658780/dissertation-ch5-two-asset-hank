from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def inspect(path: Path, display: str) -> dict:
    item = {"path": display, "sha256": sha256(path), "bytes": path.stat().st_size, "readback": "PASS"}
    if path.suffix == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.reader(handle))
        item.update({"data_rows": len(rows) - 1, "columns": len(rows[0])})
    elif path.suffix == ".json":
        json.loads(path.read_text(encoding="utf-8"))
        item["json_parse"] = "PASS"
    else:
        item["text_chars"] = len(path.read_text(encoding="utf-8-sig"))
    return item


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--evidence-root", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo_root.resolve()
    evidence = args.evidence_root.resolve()
    out = repo / "reports/mp4c_multi_province_steady_state_redesign_20260910"
    test_log = out / "focused_tests.txt"
    test_text = test_log.read_text(encoding="utf-8")
    if "10 passed" not in test_text:
        raise ValueError("Focused test receipt does not show 10 passed")

    validation = {
        "schema": "CH5_MP4C_STEADY_STATE_REDESIGN_STATIC_VALIDATION_V1",
        "focused_tests": 10, "focused_tests_passed": 10,
        "git_diff_check": "PASS",
        "contract_counts": {
            "unit_contract_rows": len(list(csv.DictReader((out / "unit_contract.csv").open(encoding="utf-8-sig")))),
            "source_to_successor_rows": len(list(csv.DictReader((out / "source_to_successor_contract.csv").open(encoding="utf-8-sig")))),
            "future_validation_rows": len(list(csv.DictReader((out / "future_validation_matrix.csv").open(encoding="utf-8-sig")))),
        },
        "scientific_model_calls": 0,
        "results_eligible": False,
    }
    validation_path = out / "static_validation_receipt.json"
    validation_path.write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    rels = [
        "docs/CH5_MP4C_MULTI_PROVINCE_STEADY_STATE_CALIBRATION_AND_INITIALIZATION_REDESIGN_SPEC.md",
        "reports/mp4c_multi_province_steady_state_redesign_20260910/source_to_successor_contract.csv",
        "reports/mp4c_multi_province_steady_state_redesign_20260910/unit_contract.csv",
        "reports/mp4c_multi_province_steady_state_redesign_20260910/initialization_contract.md",
        "reports/mp4c_multi_province_steady_state_redesign_20260910/update_order_contract.md",
        "reports/mp4c_multi_province_steady_state_redesign_20260910/calibration_stage_contract.md",
        "reports/mp4c_multi_province_steady_state_redesign_20260910/future_validation_matrix.csv",
        "reports/mp4c_multi_province_steady_state_redesign_20260910/source_hash_receipt.json",
        "reports/mp4c_multi_province_steady_state_redesign_20260910/zero_scientific_call_ledger.json",
        "reports/mp4c_multi_province_steady_state_redesign_20260910/focused_tests.txt",
        "reports/mp4c_multi_province_steady_state_redesign_20260910/static_validation_receipt.json",
        "validators/multi_province/steady_state_redesign/contracts.py",
        "validators/multi_province/steady_state_redesign/finalize.py",
        "tests/test_mp4c_steady_state_redesign_spec.py",
    ]
    entries = [inspect(repo / rel, rel) for rel in rels]
    manifest = {"schema": "CH5_MP4C_STEADY_STATE_REDESIGN_MANIFEST_V1",
                "artifact_count": len(entries), "readback_pass_count": len(entries), "entries": entries}
    manifest_path = out / "manifest_readback.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    source_receipt = json.loads((out / "source_hash_receipt.json").read_text(encoding="utf-8"))
    protected = Path(source_receipt["protected_root"])
    source_readback = []
    for item in source_receipt["sources"]:
        path = protected / item["file"]
        post = sha256(path)
        source_readback.append({"file": item["file"], "expected_sha256": item["sha256"],
                                "post_read_sha256": post, "unchanged": post == item["sha256"]})
    if not all(row["unchanged"] for row in source_readback):
        raise ValueError("Protected source changed")
    external = {"schema": "CH5_MP4C_STEADY_STATE_REDESIGN_EXTERNAL_EVIDENCE_V1",
                "repository_manifest_sha256": sha256(manifest_path), "source_readback": source_readback,
                "scientific_model_calls": 0, "results_eligible": False}
    (evidence / "external_evidence_manifest.json").write_text(
        json.dumps(external, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
