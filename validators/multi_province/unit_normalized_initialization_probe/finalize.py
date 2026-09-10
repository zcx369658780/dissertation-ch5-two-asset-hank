from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
from pathlib import Path

from .build import SOURCE_HASHES


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def inspect(path: Path, display: str | None = None) -> dict:
    item = {"path": display or str(path), "sha256": sha256(path), "bytes": path.stat().st_size, "readback": "PASS"}
    if path.suffix == ".json":
        json.loads(path.read_text(encoding="utf-8")); item["json_parse"] = "PASS"
    elif path.suffix == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.reader(handle))
        item.update({"data_rows": len(rows) - 1, "columns": len(rows[0])})
    else:
        item["text_readback_chars"] = len(path.read_text(encoding="utf-8-sig"))
    return item


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--protected-root", type=Path, required=True)
    parser.add_argument("--evidence-root", type=Path, required=True)
    parser.add_argument("--test-receipt", type=Path, required=True)
    args = parser.parse_args()
    repo, protected, evidence = args.repo_root.resolve(), args.protected_root.resolve(), args.evidence_root.resolve()
    relative = [
        "docs/CH5_MP4C_UNIT_NORMALIZED_INITIALIZATION_ONLY_PROBE_REPORT.md",
        "reports/mp4c_unit_normalized_initialization_probe_20260910/province_initialization_receipt.csv",
        "reports/mp4c_unit_normalized_initialization_probe_20260910/province_initialization_receipt.md",
        "reports/mp4c_unit_normalized_initialization_probe_20260910/national_initialization_summary.json",
        "reports/mp4c_unit_normalized_initialization_probe_20260910/asset_bridge_scale_diagnostic.csv",
        "reports/mp4c_unit_normalized_initialization_probe_20260910/source_equation_receipt.json",
        "reports/mp4c_unit_normalized_initialization_probe_20260910/call_ledger.json",
        "validators/multi_province/unit_normalized_initialization_probe/__init__.py",
        "validators/multi_province/unit_normalized_initialization_probe/build.py",
        "validators/multi_province/unit_normalized_initialization_probe/finalize.py",
        "tests/test_mp4c_unit_normalized_initialization_probe.py",
    ]
    entries = [inspect(repo / name, name) for name in relative]
    manifest = {"schema": "CH5_UNIT_NORMALIZED_INITIALIZATION_MANIFEST_V1", "scope": "finite repository package; excludes manifest itself and readback", "artifact_count": len(entries), "entries": entries}
    out = repo / "reports/mp4c_unit_normalized_initialization_probe_20260910"
    write_json(out / "manifest.json", manifest)
    reread = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
    for entry in reread["entries"]:
        if sha256(repo / entry["path"]) != entry["sha256"]:
            raise ValueError(f"repository manifest readback mismatch: {entry['path']}")
    readback = {"manifest_sha256": sha256(out / "manifest.json"), "entries_verified": len(entries), "all_hashes_match": True}
    write_json(out / "manifest_readback.json", readback)

    source_post = []
    for name, expected in SOURCE_HASHES.items():
        path = protected / name
        actual = sha256(path)
        source_post.append({"file": name, "path": str(path), "expected_sha256": expected, "post_read_sha256": actual, "unchanged": actual == expected})
    if not all(row["unchanged"] for row in source_post):
        raise ValueError("protected source changed during probe")
    shutil.copy2(out / "manifest.json", evidence / "repository_manifest.json")
    shutil.copy2(out / "manifest_readback.json", evidence / "repository_manifest_readback.json")
    external_files = [path for path in sorted(evidence.iterdir()) if path.is_file() and path.name not in {"external_evidence_manifest.json", "external_evidence_manifest_readback.json"}]
    external = {
        "schema": "CH5_UNIT_NORMALIZED_INITIALIZATION_EXTERNAL_EVIDENCE_V1",
        "protected_source_post_read": source_post,
        "files": [inspect(path) for path in external_files],
        "test_receipt": inspect(args.test_receipt.resolve()),
        "results_eligible": False,
    }
    write_json(evidence / "external_evidence_manifest.json", external)
    check = json.loads((evidence / "external_evidence_manifest.json").read_text(encoding="utf-8"))
    for entry in check["files"]:
        if sha256(Path(entry["path"])) != entry["sha256"]:
            raise ValueError(f"external manifest readback mismatch: {entry['path']}")
    external_readback = {"manifest_sha256": sha256(evidence / "external_evidence_manifest.json"), "files_verified": len(check["files"]), "all_hashes_match": True, "protected_sources_unchanged": True}
    write_json(evidence / "external_evidence_manifest_readback.json", external_readback)
    print(json.dumps({"repository": readback, "external": external_readback}, ensure_ascii=False))


if __name__ == "__main__":
    main()
