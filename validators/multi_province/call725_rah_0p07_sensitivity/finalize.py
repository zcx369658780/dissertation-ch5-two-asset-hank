"""Build finite manifests after science and report completion."""
import hashlib
import json
from pathlib import Path
import shutil
import sys

from evidence import sha256

REPO = Path(__file__).resolve().parents[3]


def write_revision(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main(root, output):
    root = Path(root).resolve()
    output = Path(output).resolve()
    terminal = json.loads((root / "science/terminal.json").read_text(encoding="utf-8"))
    process = json.loads((root / "process_receipt.json").read_text(encoding="utf-8"))
    assert terminal["terminal"] == "NORMAL_RETURN" and process["terminal_saved"] and not process["external_timeout"]
    expected = {"native_initialization": 1, "labor_root": 800, "brentq": 800, "adapter": 1, "HJB": 1, "HJB_return": 1, "HJB_direct_solve": 26, "KFE": 1, "KFE_direct_solve": 1, "KFE_return": 1, "aggregate": 1, "aggregate_return": 1}
    assert all(terminal["counts"][name] == value for name, value in expected.items())
    assert terminal["counts"]["root_residual"] == terminal["counts"]["root_bracketing_residual"] + terminal["counts"]["root_brentq_residual"]
    launch = json.loads((root / "launch_receipt.json").read_text(encoding="utf-8"))
    launched_sources = {}
    for name in ("control.py", "evidence.py", "run.py"):
        path = Path(__file__).with_name(name)
        launched_sources[name] = {"launch_sha256": launch["observer_sources"][name], "current_sha256": sha256(path)}
        assert launched_sources[name]["launch_sha256"] == launched_sources[name]["current_sha256"]
    index_rows = [json.loads(line) for line in (root / "science/index.jsonl").read_text(encoding="utf-8").splitlines()]
    phases = [row["phase"] for row in index_rows]
    expected_phases = ["environment", "binding", "native_initialization_return", "hjb_entry", "hjb_return_before_kfe", "kfe_entry", "kfe_direct_input", "kfe_direct_return", "kfe_return", "aggregate_return", "household_return", "terminal"]
    assert phases == expected_phases
    binding = json.loads((output / "intervention_binding.json").read_text(encoding="utf-8"))
    ledger = json.loads((output / "call_ledger.json").read_text(encoding="utf-8"))
    assert binding["state_changed_fields"] == ["rah"] and binding["mapped_input_changed_fields"] == ["r_a"]
    assert ledger["scientific_processes"] == 1 and ledger["scientific_restarts"] == 0 and ledger["baseline_09_new_scientific_calls"] == 0
    delivery_checks = {
        "passed": True,
        "launch_observer_sources_unchanged": launched_sources,
        "science_phase_order": phases,
        "hjb_saved_before_kfe": phases.index("hjb_return_before_kfe") < phases.index("kfe_entry"),
        "input_binding": {"state_changed_fields": binding["state_changed_fields"], "mapped_input_changed_fields": binding["mapped_input_changed_fields"]},
        "budget": {"within_limits": True, "counts": terminal["counts"]},
        "processes": {"science": 1, "workers": 1, "science_restarts": 0, "external_launch_retries": 0},
        "baseline_09_new_scientific_calls": 0,
    }
    write_revision(output / "delivery_checks.json", delivery_checks)
    receipts = output / "receipts"
    receipts.mkdir(exist_ok=True)
    for pattern in ("preflight.json", "launch_marker.json", "launch_receipt.json", "process_receipt.json", "stdout.txt", "stderr.txt", "tests_*.json", "tests_*.txt"):
        for path in root.glob(pattern):
            shutil.copyfile(path, receipts / path.name)
    for name in ("environment.json", "binding.json", "terminal.json"):
        shutil.copyfile(root / "science" / name, receipts / name)
    shutil.copyfile(root / "science/index.jsonl", output / "science_capture_index.jsonl")
    preflight = json.loads((root / "preflight.json").read_text(encoding="utf-8"))
    inputs = preflight["consumed_baseline"] + preflight["sources"] + [{"path": r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m", "sha256": preflight["protected_HJB_sha256"], "role": "protected_readonly_identity"}]
    captures = []
    for line in (root / "science/index.jsonl").read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        for key in ("json", "npz"):
            if key in row:
                captures.append({"path": row[key], "sha256": row[f"{key}_sha256"], "bytes": Path(row[key]).stat().st_size, "role": "immutable_new_science"})
    output_files = []
    report = REPO / "docs/CH5_MP4C_CALL725_RAH_0P07_NATIVE_INIT_SENSITIVITY_REPORT.md"
    paths = [report, REPO / "tests/test_mp4c_call725_rah_0p07_sensitivity.py", *sorted((REPO / "validators/multi_province/call725_rah_0p07_sensitivity").glob("*.py")), *sorted(output.rglob("*"))]
    for path in paths:
        if path.is_file() and path.name not in ("manifest.json", "manifest_readback.json"):
            raw = path.read_bytes()
            output_files.append({"path": str(path), "sha256": hashlib.sha256(raw).hexdigest().upper(), "LF_sha256": hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest().upper(), "bytes": len(raw)})
    manifest = {"scope": "Consumed baseline set, loaded source bytes, immutable new science captures, and allowed delivery files; excludes itself and readback.", "inputs": inputs, "captures": captures, "outputs": output_files}
    manifest_path = root / "manifest.json"
    write_revision(manifest_path, manifest)
    shutil.copyfile(manifest_path, output / "manifest.json")
    reopened = json.loads(manifest_path.read_text(encoding="utf-8"))
    count = 0
    for section in ("inputs", "captures", "outputs"):
        for item in reopened[section]:
            assert sha256(item["path"]) == item.get("sha256", item.get("raw_sha256")), item["path"]
            count += 1
    tests = json.loads(sorted(root.glob("tests_*.receipt.json"))[-1].read_text(encoding="utf-8"))
    receipt = {"manifest_sha256": sha256(manifest_path), "independent_files_verified": count, "all_matched": True, "science_capture_files": len(captures), "science_capture_index_entries": len((root / "science/index.jsonl").read_text(encoding="utf-8").splitlines()), "actual_test_receipt": tests}
    write_revision(root / "manifest_readback.json", receipt)
    shutil.copyfile(root / "manifest_readback.json", output / "manifest_readback.json")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
