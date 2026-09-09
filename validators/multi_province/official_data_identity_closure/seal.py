"""Seal the repository and external evidence after report and tests exist."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from core import sha256


def entries(root: Path, excluded: set[str]) -> list[dict]:
    return [
        {"path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)}
        for path in sorted(root.rglob("*"))
        if path.is_file() and path.name not in excluded
    ]


def write(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main(evidence_root: str, repo_report_dir: str, report_path: str) -> None:
    evidence = Path(evidence_root)
    repo = Path(repo_report_dir)
    report = Path(report_path)
    if not report.is_file() or not (repo / "tests.txt").is_file():
        raise RuntimeError("report and actual test log are required before sealing")
    repo_manifest = {"schema": "CH5_MP4C_2018_OFFICIAL_IDENTITY_MANIFEST_V1", "files": entries(repo, {"manifest.json", "manifest_readback.json"}), "report": {"path": str(report), "bytes": report.stat().st_size, "sha256": sha256(report)}}
    write(repo / "manifest.json", repo_manifest)
    readback = json.loads((repo / "manifest.json").read_text(encoding="utf-8"))
    checks = all((repo / row["path"]).is_file() and sha256(repo / row["path"]) == row["sha256"] for row in readback["files"])
    checks = checks and sha256(report) == readback["report"]["sha256"]
    write(repo / "manifest_readback.json", {"manifest_sha256": sha256(repo / "manifest.json"), "entries_verified": len(readback["files"]) + 1, "all_hashes_match": checks})
    external_manifest = {"schema": "CH5_MP4C_2018_OFFICIAL_IDENTITY_EXTERNAL_MANIFEST_V1", "files": entries(evidence, {"manifest.json", "manifest_readback.json"})}
    write(evidence / "manifest.json", external_manifest)
    external_readback = json.loads((evidence / "manifest.json").read_text(encoding="utf-8"))
    external_checks = all((evidence / row["path"]).is_file() and sha256(evidence / row["path"]) == row["sha256"] for row in external_readback["files"])
    write(evidence / "manifest_readback.json", {"manifest_sha256": sha256(evidence / "manifest.json"), "entries_verified": len(external_readback["files"]), "all_hashes_match": external_checks})
    if not checks or not external_checks:
        raise RuntimeError("manifest readback failed")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
