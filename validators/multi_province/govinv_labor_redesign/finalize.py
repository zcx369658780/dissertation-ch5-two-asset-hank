"""Build source receipts and a finite readback manifest without model imports."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[3]
ROOT = REPO / "reports/mp4c_govinv_labor_redesign_20260910"
PROTECTED = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK")
BASE = "9d1662bd85cdb3dd5be8660d2d08aa2bbe497aae"

PROTECTED_HASHES = {
    "HANK_mp_1eq.m": "ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF",
    "HANK_mp_1turn.m": "D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF",
    "HANK_2ASSETS_HJB.m": "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE",
    "Lt_seperate.m": "D30519AD81837E8EB5EBFE74BF25CC770E40B5C5AE5A254951AD97D436CACE26",
    "HANK_firm.m": "EE02C15414ADF9F99AADE04F1F22E64FA7094C8AB77753B6130BC4BFA6CE7BD5",
    "wage_caculate.m": "0FB84B51E2BE50CD3D065D33385882311A31E12596AEEB0CE2C808A8C36B6A63",
    "mpHANK_equilibrium_2000.m": "26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5",
    "load_GDPdata.m": "DECA8AF3F22097550B8957FE848989E6342619CB9929A1C00076E020549366C5",
}

REPO_INPUTS = [
    "AGENTS.md",
    "project_rules/PROJECT_RULE_INDEX_CURRENT.md",
    "docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md",
    "docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md",
    "docs/DISSERTATION_CH5_PYTHON_MULTI_PROVINCE_HANK_REBUILD_ROADMAP_CURRENT.md",
    "tasks/CH5_MP4C_GOVINV_INITIALIZATION_AND_LABOR_NORMALIZATION_REDESIGN_SPEC.md",
    "docs/CH5_MP4C_CORRECTED_2018_HJB_NONCONVERGENCE_PROPAGATION_AND_25TURN_KL_RERUN_REPORT.md",
    "docs/CH5_MP4C_CORRECTED_2018_HJB_NONCONVERGENCE_PROPAGATION_AND_25TURN_KL_RERUN_ACCEPTANCE.md",
    "docs/CH5_MP4C_PYTHON_RUNTIME_INPUT_BINDING_AND_UNIT_CONTRACT_REPAIR_REPORT.md",
    "docs/CH5_MP4C_PYTHON_RUNTIME_INPUT_BINDING_AND_UNIT_CONTRACT_REPAIR_ACCEPTANCE.md",
    "docs/CH5_MP4C_2018_RAW_NBS_DATA_REBUILD_CAPITAL_PRODUCTIVITY_REESTIMATION_REPORT.md",
    "docs/CH5_MP4C_UNIT_NORMALIZED_INITIALIZATION_ONLY_PROBE_REPORT.md",
    "docs/CH5_MP4C_FIRM_PRICE_NORMALIZATION_AND_HOUSEHOLD_MACRO_BRIDGE_FORENSIC_REPORT.md",
    "docs/CH5_TWO_ASSET_HANK_MATLAB_MULTI_PROVINCE_LOGIC_AND_LEGACY_R5_MIGRATION_AUDIT_REPORT.md",
    "reports/mp4c_corrected_2018_hjb_propagation_25turn_kl_20260910/province_turn_kl_ledger.csv",
]

PACKAGE_ENTRIES = [
    REPO / "docs/CH5_MP4C_GOVINV_INITIALIZATION_AND_LABOR_NORMALIZATION_REDESIGN_SPEC.md",
    ROOT / "govinv_candidate_matrix.csv",
    ROOT / "govinv_controller_compatibility.md",
    ROOT / "labor_object_dimensional_chain.csv",
    ROOT / "labor_reference_candidate_matrix.csv",
    ROOT / "joint_initialization_sequence.md",
    ROOT / "owner_decision_matrix.csv",
    ROOT / "zero_scientific_call_ledger.json",
    ROOT / "focused_static_test_receipt.json",
    ROOT / "source_hash_receipt.json",
    REPO / "tests/test_mp4c_govinv_labor_redesign_spec.py",
    REPO / "validators/multi_province/govinv_labor_redesign/finalize.py",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def write_new(path: Path, payload: object) -> None:
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(payload, stream, ensure_ascii=False, indent=2, sort_keys=True)
        stream.write("\n")


def main() -> int:
    protected_entries = []
    for name, expected in PROTECTED_HASHES.items():
        path = PROTECTED / name
        observed = digest(path)
        if observed != expected:
            raise RuntimeError(f"protected source drift: {name}")
        protected_entries.append({"path": str(path), "sha256": observed, "expected_sha256": expected, "match": True})

    repo_entries = []
    for relative in REPO_INPUTS:
        path = REPO / relative
        repo_entries.append({"path": relative, "bytes": path.stat().st_size, "sha256": digest(path)})

    write_new(ROOT / "source_hash_receipt.json", {
        "schema": "CH5_MP4C_GOVINV_LABOR_REDESIGN_SOURCE_HASH_RECEIPT_V1",
        "base_origin_main": BASE,
        "authority_resolution": "LIVE_INDEX_AND_EXACT_TASK_OVERRIDE_STALE_STATUS_HANDOFF_ROADMAP_SNAPSHOTS",
        "protected_sources_read_only": True,
        "protected_sources": protected_entries,
        "repository_inputs": repo_entries,
    })

    manifest_entries = []
    for path in PACKAGE_ENTRIES:
        manifest_entries.append({
            "path": path.relative_to(REPO).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": digest(path),
        })
    manifest_path = ROOT / "manifest.json"
    write_new(manifest_path, {
        "schema": "CH5_MP4C_GOVINV_LABOR_REDESIGN_MANIFEST_V1",
        "entries": manifest_entries,
    })

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    readback = []
    for entry in manifest["entries"]:
        path = REPO / entry["path"]
        readback.append({
            "path": entry["path"],
            "bytes_match": path.stat().st_size == entry["bytes"],
            "sha256_match": digest(path) == entry["sha256"],
        })
    if not all(row["bytes_match"] and row["sha256_match"] for row in readback):
        raise RuntimeError("manifest readback failed")
    write_new(ROOT / "manifest_readback.json", {
        "schema": "CH5_MP4C_GOVINV_LABOR_REDESIGN_MANIFEST_READBACK_V1",
        "manifest_sha256": digest(manifest_path),
        "passed": True,
        "entries": readback,
    })
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
