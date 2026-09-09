"""Finalize the finite zero-science attribution manifest and readback."""

import json
from pathlib import Path
import shutil
import sys

from evidence import lf_sha256, sha256, write_json


REPO = Path(__file__).resolve().parents[3]
VALIDATORS = REPO / "validators/multi_province/call725_kfe_mass_balance"
TEST = REPO / "tests/test_mp4c_call725_kfe_mass_balance.py"
REPORT = REPO / "docs/CH5_MP4C_CALL725_RAH_0P07_KFE_MASS_BALANCE_ATTRIBUTION_REPORT.md"


def output_item(path, role):
    path = Path(path).resolve()
    return {"path": str(path), "raw_sha256": sha256(path), "LF_sha256": lf_sha256(path), "bytes": path.stat().st_size, "role": role}


def main(evidence_root, report_output):
    evidence_root = Path(evidence_root).resolve()
    report_output = Path(report_output).resolve()
    summary = json.loads((evidence_root / "summary.json").read_text(encoding="utf-8"))
    preflight = json.loads((evidence_root / "preflight.json").read_text(encoding="utf-8"))
    calls = json.loads((evidence_root / "zero_call_ledger.json").read_text(encoding="utf-8"))
    tests_path = sorted(evidence_root.glob("tests_*.receipt.json"))[-1]
    tests = json.loads(tests_path.read_text(encoding="utf-8"))
    assert summary["diagnostic_completion"] == "COMPLETE"
    assert summary["source_escape_interpretation"] == "SUPPORTED"
    assert summary["Results_eligible"] is False
    assert tests["passed"] and tests["ran"] == tests["individual_ok"] == 10
    assert sum(1 for _ in (evidence_root / "cell_ledger.csv").open(encoding="utf-8")) == 801
    scientific_keys = (
        "new_initializer", "new_root", "new_HJB", "new_KFE",
        "new_direct_iterative_eigen_optimization_condition_solves", "new_policy_evaluator",
        "firm_one_turn_controller_GE_annual_dynamics_IRF_Results", "MATLAB_startups",
        "scientific_retries", "assembler_or_selector_calls",
    )
    assert all(calls[key] == 0 for key in scientific_keys)
    assert summary["identity_checks"]["consumed_object_count"] == 13
    assert summary["signed_mass_balance"]["mass_identity_frozen_rule_pass"]
    assert summary["signed_mass_balance"]["source_balance_frozen_rule_pass"]

    copied_pairs = []
    for external in evidence_root.iterdir():
        repository = report_output / external.name
        if external.is_file() and external.name not in ("manifest.json", "manifest_readback.json"):
            assert repository.exists() and sha256(external) == sha256(repository)
            copied_pairs.append({"external": str(external), "repository": str(repository), "sha256": sha256(external)})
    delivery = {
        "passed": True,
        "identity_checks_passed": True,
        "pin_residual_localized": summary["pin_residual_localization"]["pin_abs_share_of_residual_L1"],
        "mass_identity_frozen_rule_pass": True,
        "source_balance_frozen_rule_pass": True,
        "cell_ledger_rows": 800,
        "actual_test_receipt": tests,
        "zero_new_scientific_calls": True,
        "copied_external_repository_pairs": len(copied_pairs),
        "model_label_exposed_by_repository_receipts": False,
    }
    write_json(evidence_root / "delivery_checks.json", delivery, exclusive=True)
    shutil.copyfile(evidence_root / "delivery_checks.json", report_output / "delivery_checks.json")
    copied_pairs.append({"external": str(evidence_root / "delivery_checks.json"), "repository": str(report_output / "delivery_checks.json"), "sha256": sha256(evidence_root / "delivery_checks.json")})

    inputs = [
        {**item, "role": "consumed_predecessor_science"} for item in preflight["consumed"]
    ]
    for path, role in (
        (preflight["resolved_predecessor_manifest"], "predecessor_manifest_resolved_by_receipt"),
        (preflight["index_identity"]["external_path"], "external_science_index"),
        (preflight["index_identity"]["repository_path"], "repository_science_index_copy"),
        (REPO / "exports/matlab_faithful_two_asset_ha.py", "frozen_source_attribution"),
        (Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m"), "protected_readonly_identity"),
    ):
        inputs.append(output_item(path, role))
    outputs = []
    external_files = [path for path in evidence_root.iterdir() if path.is_file() and path.name not in ("manifest.json", "manifest_readback.json")]
    repository_files = [REPORT, TEST, *sorted(VALIDATORS.glob("*.py")), *sorted(path for path in report_output.rglob("*") if path.is_file() and path.name not in ("manifest.json", "manifest_readback.json"))]
    outputs.extend(output_item(path, "external_attribution_evidence") for path in external_files)
    outputs.extend(output_item(path, "repository_delivery") for path in repository_files)
    manifest = {
        "scope": "13 consumed predecessor science files, their manifest/index/source identities, external derived evidence, and allowed repository delivery; excludes manifest and final readback from self-hashing.",
        "inputs": inputs,
        "outputs": outputs,
        "external_repository_copy_pairs": copied_pairs,
    }
    manifest_path = evidence_root / "manifest.json"
    write_json(manifest_path, manifest, exclusive=True)
    shutil.copyfile(manifest_path, report_output / "manifest.json")
    verified = 0
    for section in ("inputs", "outputs"):
        for item in manifest[section]:
            expected = item["sha256"] if "sha256" in item else item["raw_sha256"]
            assert sha256(item["path"]) == expected
            verified += 1
    readback = {
        "manifest_sha256": sha256(manifest_path),
        "repository_manifest_copy_sha256": sha256(report_output / "manifest.json"),
        "independent_files_verified": verified,
        "all_matched": True,
        "consumed_science_files": 13,
        "cell_ledger_rows": 800,
        "actual_test_receipt": tests,
        "zero_new_scientific_calls": True,
    }
    write_json(evidence_root / "manifest_readback.json", readback, exclusive=True)
    shutil.copyfile(evidence_root / "manifest_readback.json", report_output / "manifest_readback.json")
    print(json.dumps(readback))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
