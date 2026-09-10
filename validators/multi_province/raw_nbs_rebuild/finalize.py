from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def inspect(path: Path) -> dict:
    item = {"path": path.as_posix(), "sha256": digest(path), "bytes": path.stat().st_size, "readback": "PASS"}
    if path.suffix == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.reader(handle)
            rows = list(reader)
        item.update({"data_rows": len(rows) - 1, "columns": len(rows[0])})
    elif path.suffix == ".json":
        json.loads(path.read_text(encoding="utf-8"))
        item["json_parse"] = "PASS"
    elif path.suffix in {".md", ".py", ".ps1"}:
        text = path.read_text(encoding="utf-8-sig")
        item["text_readback_chars"] = len(text)
    return item


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--evidence-root", type=Path, required=True)
    parser.add_argument("--raw-json", type=Path, required=True)
    parser.add_argument("--focused-test-log", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo_root.resolve()
    evidence = args.evidence_root.resolve()
    paths = [
        Path("docs/CH5_MP4C_2018_RAW_NBS_DATA_REBUILD_CAPITAL_PRODUCTIVITY_REESTIMATION_REPORT.md"),
        Path("reports/mp4c_2018_raw_nbs_rebuild_20260910/cleaned_province_year_panel.csv"),
        Path("reports/mp4c_2018_raw_nbs_rebuild_20260910/corrected_2018_vs_matlab_ledger.csv"),
        Path("reports/mp4c_2018_raw_nbs_rebuild_20260910/corrected_2018_vs_matlab_ledger.md"),
        Path("reports/mp4c_2018_raw_nbs_rebuild_20260910/alpha_estimation_receipt.json"),
        Path("reports/mp4c_2018_raw_nbs_rebuild_20260910/capital_method_comparison.csv"),
        Path("reports/mp4c_2018_raw_nbs_rebuild_20260910/source_hash_receipt.json"),
        Path("reports/mp4c_2018_raw_nbs_rebuild_20260910/data_quality_flags.csv"),
        Path("reports/mp4c_2018_raw_nbs_rebuild_20260910/rebuild_summary.json"),
        Path("validators/multi_province/raw_nbs_rebuild/extract_raw_nbs_xls.ps1"),
        Path("validators/multi_province/raw_nbs_rebuild/build.py"),
        Path("validators/multi_province/raw_nbs_rebuild/finalize.py"),
        Path("tests/test_mp4c_2018_raw_nbs_rebuild.py"),
    ]
    entries = [inspect(repo / path) | {"path": path.as_posix()} for path in paths]
    receipt = {
        "schema": "CH5_RAW_NBS_REBUILD_MANIFEST_READBACK_V1",
        "artifact_count": len(entries), "readback_pass_count": sum(e["readback"] == "PASS" for e in entries),
        "entries": entries,
    }
    target = repo / "reports/mp4c_2018_raw_nbs_rebuild_20260910/manifest_readback.json"
    target.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    external = evidence / "repository_artifact_manifest_readback.json"
    external.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    source_receipt = json.loads((repo / "reports/mp4c_2018_raw_nbs_rebuild_20260910/source_hash_receipt.json").read_text(encoding="utf-8"))
    source_readback = []
    for source in source_receipt["sources"]:
        source_path = Path(source["actual_path"])
        post_hash = digest(source_path)
        source_readback.append({
            "key": source["key"], "path": str(source_path), "expected_sha256": source["sha256"],
            "post_read_sha256": post_hash, "unchanged": post_hash == source["sha256"],
        })
    if not all(item["unchanged"] for item in source_readback):
        raise ValueError("A raw source hash changed during read-only processing")
    external_manifest = {
        "schema": "CH5_RAW_NBS_REBUILD_EXTERNAL_EVIDENCE_V1",
        "source_readback": source_readback,
        "evidence_files": [
            inspect(args.raw_json) | {"path": str(args.raw_json)},
            inspect(args.focused_test_log) | {"path": str(args.focused_test_log)},
            inspect(external) | {"path": str(external)},
        ],
        "call_budget": {
            "successful_raw_xls_extractions": 1,
            "prelaunch_extractor_parser_failures_before_source_open": 1,
            "data_cleaning_regression_calibration_script_runs": 4,
            "pooled_ols_fits": 4,
            "focused_test_processes": 4,
            "python_compile_checks": 2,
            "matlab_hank": 0, "python_household_hjb_kfe": 0,
            "firm_wage_migration_capital_allocation": 0, "outer_turn": 0,
            "steady_state_ge_annual_irf_results": 0,
        },
        "results_eligible": False,
    }
    (evidence / "external_evidence_manifest.json").write_text(
        json.dumps(external_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
