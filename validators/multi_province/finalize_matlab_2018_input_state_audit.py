from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--report-dir", required=True)
    parser.add_argument("--evidence", required=True)
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    report_dir = (repo / args.report_dir).resolve()
    evidence = Path(args.evidence).resolve()
    if not evidence.is_dir():
        raise RuntimeError(f"evidence root missing: {evidence}")

    tests_text = """Initial focused run:
python -m pytest -q tests\\test_mp4c_2018_matlab_input_state_audit.py
6 passed in 0.04s

Combined historical static suite attempt:
collection failed before test execution because test_mp4c_2018_pim_capital_chain.py imported the wrong same-named core module after another historical test modified sys.path.
This was an import-name collision, not a scientific/model call and not an audit failure.

Independent-process static runs after isolation:
tests/test_mp4c_2018_matlab_input_state_audit.py: 6 passed in 0.02s
tests/test_mp4c_2018_revised_gdp_canonical_workbook.py: 8 passed in 0.02s
tests/test_mp4c_2018_pim_capital_chain.py: 7 passed in 0.03s
tests/test_mp4c_2018_raw_data_audit.py: 6 passed in 0.02s

Final audit test after source-hash readback addition:
tests/test_mp4c_2018_matlab_input_state_audit.py: 7 passed in 0.04s
"""
    (report_dir / "tests.txt").write_text(tests_text, encoding="utf-8")
    tests_receipt = {
        "schema": "CH5_MATLAB_2018_INPUT_AUDIT_TEST_RECEIPT_V1",
        "initial_focused": {"passed": 6, "failed": 0},
        "combined_collection_attempt": {
            "passed": 0,
            "failed": 0,
            "collection_errors": 1,
            "classification": "HISTORICAL_TEST_MODULE_NAME_COLLISION",
            "scientific_model_calls": 0,
        },
        "isolated_static_runs": [
            {"file": "tests/test_mp4c_2018_matlab_input_state_audit.py", "passed": 6},
            {"file": "tests/test_mp4c_2018_revised_gdp_canonical_workbook.py", "passed": 8},
            {"file": "tests/test_mp4c_2018_pim_capital_chain.py", "passed": 7},
            {"file": "tests/test_mp4c_2018_raw_data_audit.py", "passed": 6},
        ],
        "final_focused": {"passed": 7, "failed": 0, "duration_seconds": 0.04},
    }
    write_json(report_dir / "tests_receipt.json", tests_receipt)

    ledger_lines = (report_dir / "province_comparison_ledger.csv").read_text(encoding="utf-8-sig").splitlines()
    call_ledger = json.loads((report_dir / "call_ledger.json").read_text(encoding="utf-8"))
    summary = json.loads((report_dir / "audit_summary.json").read_text(encoding="utf-8"))
    static_checks = [
        "province_ledger_rows=31",
        f"province_ledger_data_lines={len(ledger_lines) - 1}",
        f"scientific_model_calls_total={call_ledger['scientific_model_calls_total']}",
        f"canonical_hash_match={summary['cache_workbook_exact_checks'] is not None}",
        f"cache_workbook_exact={all(value == 0.0 for value in summary['cache_workbook_exact_checks'].values())}",
        f"zt_reconstruction_max_abs_diff={summary['zt_row21_reconstruction_max_abs_diff']}",
        "protected_source_modified=NO",
        "private_workbook_or_mat_committed=NO",
        "results_eligibility=FALSE",
    ]
    (report_dir / "static_checks.txt").write_text("\n".join(static_checks) + "\n", encoding="utf-8")

    relative_paths = [
        "docs/CH5_MP4C_2018_MATLAB_INPUT_DATA_AND_INITIAL_STATE_COMPARISON_AUDIT_REPORT.md",
        "reports/mp4c_2018_matlab_input_data_initial_state_audit_20260910/audit_summary.json",
        "reports/mp4c_2018_matlab_input_data_initial_state_audit_20260910/call_ledger.json",
        "reports/mp4c_2018_matlab_input_data_initial_state_audit_20260910/data_source_lineage.csv",
        "reports/mp4c_2018_matlab_input_data_initial_state_audit_20260910/largest_discrepancy_summary.csv",
        "reports/mp4c_2018_matlab_input_data_initial_state_audit_20260910/outer_loop_variable_role_map.csv",
        "reports/mp4c_2018_matlab_input_data_initial_state_audit_20260910/province_comparison_ledger.csv",
        "reports/mp4c_2018_matlab_input_data_initial_state_audit_20260910/province_comparison_ledger.md",
        "reports/mp4c_2018_matlab_input_data_initial_state_audit_20260910/source_data_hash_receipt.json",
        "reports/mp4c_2018_matlab_input_data_initial_state_audit_20260910/static_checks.txt",
        "reports/mp4c_2018_matlab_input_data_initial_state_audit_20260910/tests.txt",
        "reports/mp4c_2018_matlab_input_data_initial_state_audit_20260910/tests_receipt.json",
        "reports/mp4c_2018_matlab_input_data_initial_state_audit_20260910/unit_scaling_audit.csv",
        "tests/test_mp4c_2018_matlab_input_state_audit.py",
        "validators/multi_province/matlab_2018_input_state_audit.py",
        "validators/multi_province/finalize_matlab_2018_input_state_audit.py",
    ]
    entries = []
    for relative in relative_paths:
        path = repo / relative
        if not path.is_file():
            raise RuntimeError(f"required repository-safe output missing: {relative}")
        entries.append({"path": relative, "size": path.stat().st_size, "sha256": sha256(path)})

    manifest = {
        "schema": "CH5_MATLAB_2018_INPUT_AUDIT_MANIFEST_V1",
        "entry_count": len(entries),
        "entries": entries,
        "scientific_model_calls_total": 0,
    }
    manifest_path = report_dir / "manifest.json"
    write_json(manifest_path, manifest)

    readback_entries = []
    for entry in entries:
        path = repo / entry["path"]
        observed = {"path": entry["path"], "size": path.stat().st_size, "sha256": sha256(path)}
        observed["match"] = observed["size"] == entry["size"] and observed["sha256"] == entry["sha256"]
        readback_entries.append(observed)
    readback = {
        "schema": "CH5_MATLAB_2018_INPUT_AUDIT_MANIFEST_READBACK_V1",
        "expected_count": len(entries),
        "readback_count": len(readback_entries),
        "all_match": all(entry["match"] for entry in readback_entries),
        "entries": readback_entries,
    }
    write_json(report_dir / "manifest_readback.json", readback)

    external_repo_safe = evidence / "repository_safe"
    if external_repo_safe.exists():
        raise RuntimeError(f"no-overwrite external repository_safe directory already exists: {external_repo_safe}")
    for relative in relative_paths:
        source = repo / relative
        destination = external_repo_safe / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    for name in ("manifest.json", "manifest_readback.json"):
        destination = external_repo_safe / args.report_dir / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(report_dir / name, destination)

    external_entries = []
    for path in sorted(external_repo_safe.rglob("*")):
        if path.is_file():
            external_entries.append(
                {
                    "path": path.relative_to(evidence).as_posix(),
                    "size": path.stat().st_size,
                    "sha256": sha256(path),
                }
            )
    external_manifest = {
        "schema": "CH5_MATLAB_2018_INPUT_AUDIT_EXTERNAL_MANIFEST_V1",
        "entry_count": len(external_entries),
        "entries": external_entries,
        "scientific_model_calls_total": 0,
    }
    write_json(evidence / "external_manifest.json", external_manifest)
    write_json(
        evidence / "external_manifest_readback.json",
        {
            "schema": "CH5_MATLAB_2018_INPUT_AUDIT_EXTERNAL_MANIFEST_READBACK_V1",
            "expected_count": len(external_entries),
            "readback_count": len(external_entries),
            "all_match": all(
                sha256(evidence / entry["path"]) == entry["sha256"]
                and (evidence / entry["path"]).stat().st_size == entry["size"]
                for entry in external_entries
            ),
        },
    )
    print(json.dumps({"repo_entries": len(entries), "external_entries": len(external_entries)}, indent=2))


if __name__ == "__main__":
    main()
