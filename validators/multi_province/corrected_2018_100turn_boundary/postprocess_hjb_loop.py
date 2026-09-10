"""Correct HJB-loop validity labels from saved arrays; performs no solve."""
from __future__ import annotations

import csv
import json
from hashlib import sha256
from pathlib import Path
from typing import Any

import numpy as np

from validators.multi_province.corrected_2018_100turn_boundary import finalize

EVIDENCE = finalize.EVIDENCE
REPORT_DIR = finalize.REPORT_DIR
REPORT = finalize.REPORT


def operator_stats(path: Path, key: str) -> dict[str, Any]:
    with np.load(path, allow_pickle=True) as archive:
        matrix = archive[key].item().tocsr()
    matrix.setdiag(0.0)
    matrix.eliminate_zeros()
    negative = matrix.data[matrix.data < -1e-12]
    return {
        "classification": "VALID" if negative.size == 0 else "DIAGNOSTIC_ONLY",
        "negative_offdiagonal_count": int(negative.size),
        "minimum_offdiagonal": float(negative.min()) if negative.size else 0.0,
    }


def write_json_x(path: Path, value: Any) -> None:
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
        stream.write("\n")


def rewrite_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def manifest_for(root: Path, excluded: set[str]) -> list[dict[str, Any]]:
    return [{"path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size,
             "sha256": file_sha256(path)}
            for path in sorted(p for p in root.rglob("*") if p.is_file())
            if path.relative_to(root).as_posix() not in excluded]


def run_postprocess() -> None:
    external_output = EVIDENCE / "hjb_loop_operator_postprocess.json"
    external_receipt = EVIDENCE / "hjb_loop_operator_correction_receipt.json"
    for path in (external_output, external_receipt, EVIDENCE / "manifest_v2.json",
                 EVIDENCE / "manifest_v2_readback.json", REPORT_DIR / "manifest_v2.json",
                 REPORT_DIR / "manifest_v2_readback.json"):
        if path.exists():
            raise FileExistsError(path)

    diagnostics = []
    by_turn: dict[int, list[dict[str, Any]]] = {}
    for turn in range(1, 101):
        rows = json.loads((EVIDENCE / f"turn_{turn:02d}/per_province_observables.json").read_text(
            encoding="utf-8"))
        current = []
        for row in rows:
            path = (EVIDENCE / f"turn_{turn:02d}/household" /
                    f"p{int(row['province_index']):02d}_{row['province']}" / "hjb_return.npz")
            loop = operator_stats(path, "operator")
            post = operator_stats(path, "post_convergence_operator")
            item = {"turn": turn, "province_index": row["province_index"],
                    "province": row["province"], "hjb_loop": loop,
                    "post_convergence_operator": post, "additional_solves": 0}
            diagnostics.append(item)
            current.append(item)
        by_turn[turn] = current
    payload = {
        "schema": "CH5_CORRECTED_2018_100TURN_HJB_LOOP_OPERATOR_POSTPROCESS_V1",
        "source": "saved hjb_return.npz operator and post_convergence_operator arrays",
        "scientific_calls": 0, "additional_solves": 0, "diagnostics": diagnostics,
    }

    validity = read_csv(REPORT_DIR / "scientific_validity_ledger.csv")
    turn_ledger = read_csv(REPORT_DIR / "turn_ledger.csv")
    anhui = read_csv(REPORT_DIR / "anhui_trace.csv")
    for turn, items in by_turn.items():
        loop_negative = sum(x["hjb_loop"]["negative_offdiagonal_count"] for x in items)
        loop_min = min(x["hjb_loop"]["minimum_offdiagonal"] for x in items)
        loop_valid = sum(x["hjb_loop"]["classification"] == "VALID" for x in items)
        post_negative = sum(x["post_convergence_operator"]["negative_offdiagonal_count"] for x in items)
        v = validity[turn - 1]
        v["hjb_operator_valid_count"] = str(loop_valid)
        v["hjb_operator_diagnostic_only_count"] = str(31 - loop_valid)
        v["hjb_negative_offdiagonal_count"] = str(loop_negative)
        v["minimum_hjb_offdiagonal"] = repr(loop_min)
        v["post_convergence_negative_offdiagonal_count"] = str(post_negative)
        turn_ledger[turn - 1]["hjb_negative_offdiagonals"] = str(loop_negative)
        a = items[11]["hjb_loop"]
        anhui[turn - 1]["hjb_operator_status"] = a["classification"]
    rewrite_csv(REPORT_DIR / "scientific_validity_ledger.csv", validity)
    rewrite_csv(REPORT_DIR / "turn_ledger.csv", turn_ledger)
    rewrite_csv(REPORT_DIR / "anhui_trace.csv", anhui)

    report = REPORT.read_text(encoding="utf-8")
    changed = report.count("| DIAGNOSTIC_ONLY | VALID |")
    if changed != 9:
        raise ValueError(f"expected 9 selected Anhui validity labels, found {changed}")
    report = report.replace("| DIAGNOSTIC_ONLY | VALID |", "| DIAGNOSTIC_ONLY | DIAGNOSTIC_ONLY |")
    turn1 = by_turn[1]
    turn100 = by_turn[100]
    correction = (
        "\n## HJB-loop operator correction\n\n"
        "The first derived ledger had inspected the KFE-input post-convergence operator. "
        "A zero-solve readback of the separately saved HJB-loop `operator` corrected that label. "
        f"Turn 1/100 national negative offdiagonals are "
        f"{sum(x['hjb_loop']['negative_offdiagonal_count'] for x in turn1)}/"
        f"{sum(x['hjb_loop']['negative_offdiagonal_count'] for x in turn100)}; "
        f"diagnostic-only provinces are "
        f"{sum(x['hjb_loop']['classification'] == 'DIAGNOSTIC_ONLY' for x in turn1)}/"
        f"{sum(x['hjb_loop']['classification'] == 'DIAGNOSTIC_ONLY' for x in turn100)}. "
        "The post-convergence operator has zero negative offdiagonals in both turns. "
        "This correction changes no scientific state, solve, boundary verdict, or call count.\n"
    )
    marker = "\n## Calls and protected boundary\n"
    if marker not in report:
        raise ValueError("report insertion marker missing")
    REPORT.write_text(report.replace(marker, correction + marker), encoding="utf-8", newline="\n")

    write_json_x(external_output, payload)
    receipt = {
        "schema": "CH5_CORRECTED_2018_100TURN_HJB_LOOP_CORRECTION_RECEIPT_V1",
        "reason": "initial derived ledger inspected post-convergence operator instead of saved HJB-loop operator",
        "scientific_calls": 0, "additional_solves": 0, "trajectory_rerun": False,
        "external_postprocess_sha256": file_sha256(external_output),
        "corrected_repo_files": [
            "turn_ledger.csv", "anhui_trace.csv", "scientific_validity_ledger.csv",
            "docs/CH5_MP4C_CORRECTED_2018_100_TURN_BOUNDARY_TRAJECTORY_DIAGNOSTIC_REPORT.md",
        ],
    }
    write_json_x(external_receipt, receipt)
    write_json_x(REPORT_DIR / "hjb_loop_operator_correction_receipt.json", receipt)

    repo_excluded = {"manifest.json", "manifest_readback.json", "manifest_v2.json",
                     "manifest_v2_readback.json"}
    repo_records = manifest_for(REPORT_DIR, repo_excluded)
    write_json_x(REPORT_DIR / "manifest_v2.json", {"files": repo_records})
    write_json_x(REPORT_DIR / "manifest_v2_readback.json", {
        "checked_files": len(repo_records),
        "passed": all((REPORT_DIR / row["path"]).stat().st_size == row["bytes"]
                      and file_sha256(REPORT_DIR / row["path"]) == row["sha256"]
                      for row in repo_records),
    })
    external_excluded = {"manifest.json", "manifest_readback.json", "manifest_v2.json",
                         "manifest_v2_readback.json"}
    external_records = manifest_for(EVIDENCE, external_excluded)
    write_json_x(EVIDENCE / "manifest_v2.json", {"files": external_records})
    write_json_x(EVIDENCE / "manifest_v2_readback.json", {
        "checked_files": len(external_records),
        "passed": all((EVIDENCE / row["path"]).stat().st_size == row["bytes"]
                      and file_sha256(EVIDENCE / row["path"]) == row["sha256"]
                      for row in external_records),
    })


def write_v3_manifests() -> None:
    """Bind the final human-reviewed report wording without changing evidence."""
    for root in (REPORT_DIR, EVIDENCE):
        for name in ("manifest_v3.json", "manifest_v3_readback.json"):
            if (root / name).exists():
                raise FileExistsError(root / name)
    repo_excluded = {"manifest.json", "manifest_readback.json", "manifest_v2.json",
                     "manifest_v2_readback.json", "manifest_v3.json", "manifest_v3_readback.json"}
    repo_records = manifest_for(REPORT_DIR, repo_excluded)
    doc_record = {"path": str(REPORT.relative_to(finalize.REPO)).replace("\\", "/"),
                  "bytes": REPORT.stat().st_size, "sha256": file_sha256(REPORT)}
    write_json_x(REPORT_DIR / "manifest_v3.json", {
        "files": repo_records,
        "docs_report": doc_record,
    })
    write_json_x(REPORT_DIR / "manifest_v3_readback.json", {
        "checked_files": len(repo_records) + 1,
        "passed": all((REPORT_DIR / row["path"]).stat().st_size == row["bytes"]
                      and file_sha256(REPORT_DIR / row["path"]) == row["sha256"]
                      for row in repo_records),
        "docs_report_passed": (REPORT.is_file() and REPORT.stat().st_size == doc_record["bytes"]
                               and file_sha256(REPORT) == doc_record["sha256"]),
    })
    external_excluded = {"manifest.json", "manifest_readback.json", "manifest_v2.json",
                         "manifest_v2_readback.json", "manifest_v3.json", "manifest_v3_readback.json"}
    external_records = manifest_for(EVIDENCE, external_excluded)
    write_json_x(EVIDENCE / "manifest_v3.json", {"files": external_records})
    write_json_x(EVIDENCE / "manifest_v3_readback.json", {
        "checked_files": len(external_records),
        "passed": all((EVIDENCE / row["path"]).stat().st_size == row["bytes"]
                      and file_sha256(EVIDENCE / row["path"]) == row["sha256"]
                      for row in external_records),
    })


def write_publication_manifest() -> None:
    """Bind final repo-safe outputs and the docs report after human interpretation."""
    output = REPORT_DIR / "publication_manifest.json"
    readback = REPORT_DIR / "publication_manifest_readback.json"
    if output.exists() or readback.exists():
        raise FileExistsError("publication manifest already exists")
    records = [{"path": path.relative_to(REPORT_DIR).as_posix(), "bytes": path.stat().st_size,
                "sha256": file_sha256(path)}
               for path in sorted(p for p in REPORT_DIR.rglob("*") if p.is_file())
               if "manifest" not in path.name]
    doc = {"path": str(REPORT.relative_to(finalize.REPO)).replace("\\", "/"),
           "bytes": REPORT.stat().st_size, "sha256": file_sha256(REPORT)}
    write_json_x(output, {"files": records, "docs_report": doc})
    write_json_x(readback, {
        "checked_files": len(records) + 1,
        "passed": (all((REPORT_DIR / row["path"]).stat().st_size == row["bytes"]
                       and file_sha256(REPORT_DIR / row["path"]) == row["sha256"]
                       for row in records)
                   and REPORT.stat().st_size == doc["bytes"]
                   and file_sha256(REPORT) == doc["sha256"]),
    })


if __name__ == "__main__":
    run_postprocess()
