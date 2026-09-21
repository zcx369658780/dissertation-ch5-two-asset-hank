"""Validate the adopted relaxation implementation using persisted updates only."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Any
import xml.etree.ElementTree as ET

import numpy as np

REPOSITORY_IMPORT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPOSITORY_IMPORT_ROOT / "src"))

from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import (
    MONOTONICITY_RELAXATION_EXHAUSTED,
    MONOTONICITY_RELAXATION_MAX_HALVINGS,
    monotonicity_preserving_relaxation,
)


BASELINE = "94e174ef2c500b246106a848713c1af232c1cd80"
TASK_ID = "CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTATION_AND_PERSISTED_REPLAY_20260921"
TERMINAL = "PASS__MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTED__EXACT_PERSISTED_REPLAY_PASS__FRESH_HJB_NOT_RUN"
ROOT = Path("reports/ch5_mp4c_lower_a_interior_z_composition_repair_turn1_parity_turn2_run004_20260921")
PROVINCE = ROOT / "household/p07_黑龙江"
ACCEPTED_RUN004_MANIFEST = "1C501CEF7740748805CF538A05ECF9D80938149CDDF31A3158091F665C45AD80"
DESIGN_ROOT = Path("reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_scientific_design_gate_20260921_run001")
ACCEPTED_DESIGN_MANIFEST = "F54EDEAA8FC351981CD2CBD44F17FA58950155F12953B7983E174D5EAC0D2803"
OUT = Path("reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_implementation_persisted_replay_20260921_run001")
SHAPE = (20, 20, 2)
B_NODES = np.linspace(-2.0, 5.0, 20)

AUTHORITY = (
    Path("AGENTS.md"),
    Path("project_rules/PROJECT_RULE_INDEX_CURRENT.md"),
    Path("docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md"),
    Path("docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md"),
    Path("docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_OWNER_ADOPTION_20260921.md"),
    Path("docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_SCIENTIFIC_DESIGN_GATE_ACCEPTANCE_20260921.md"),
    Path("docs/CH5_MP4C_TURN2_HEILONGJIANG_F0063_NEGATIVE_DERIVATIVE_EMERGENCE_FORENSIC_ACCEPTANCE_20260921.md"),
    Path("tasks/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTATION_AND_PERSISTED_REPLAY_20260921.md"),
)
PRODUCTION = (
    Path("src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py"),
)
FROZEN_FILES = (
    Path("src/ch5_two_asset_hank/corrected_diagnostic/selector.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/cost.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/generator.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/option_a_step.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/q1_kfe_validation.py"),
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def field_sha256(value: np.ndarray) -> str:
    return hashlib.sha256(np.asarray(value, dtype="<f8").tobytes(order="F")).hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def identity(path: Path, repository: Path) -> dict[str, Any]:
    return {"path": path.relative_to(repository).as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)}


def git(repository: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repository, text=True).strip()


def git_bytes(repository: Path, revision: str, path: Path) -> bytes:
    return subprocess.check_output(["git", "show", f"{revision}:{path.as_posix()}"], cwd=repository)


def function_source(text: str, name: str) -> str:
    tree = ast.parse(text)
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
            lines = text.splitlines(keepends=True)
            return "".join(lines[node.lineno - 1 : node.end_lineno])
    raise RuntimeError(f"function not found: {name}")


def source_freeze(repository: Path) -> dict[str, Any]:
    frozen = []
    for relative in FROZEN_FILES:
        baseline_blob = git(repository, "rev-parse", f"{BASELINE}:{relative.as_posix()}")
        working_blob = git(repository, "hash-object", relative.as_posix())
        frozen.append({
            "path": relative.as_posix(),
            "baseline_blob": baseline_blob,
            "working_blob": working_blob,
            "exact_unchanged": baseline_blob == working_blob,
        })
    nonlinear = PRODUCTION[0]
    baseline_text = git_bytes(repository, BASELINE, nonlinear).decode("utf-8")
    working_text = (repository / nonlinear).read_text(encoding="utf-8")
    terminal_before = function_source(baseline_text, "_terminal_kfe")
    terminal_after = function_source(working_text, "_terminal_kfe")
    changed = git(repository, "diff", "--name-only", BASELINE, "--", "src/ch5_two_asset_hank").splitlines()
    allowed = {path.as_posix() for path in PRODUCTION}
    return {
        "authorized_production_paths": sorted(allowed),
        "changed_production_paths": changed,
        "changed_production_paths_exactly_authorized": bool(changed and set(changed).issubset(allowed)),
        "unchanged_file_blobs": frozen,
        "all_frozen_file_blobs_exact": all(row["exact_unchanged"] for row in frozen),
        "terminal_kfe_function": {
            "path": nonlinear.as_posix(),
            "baseline_sha256": text_sha256(terminal_before),
            "working_sha256": text_sha256(terminal_after),
            "exact_source_unchanged": terminal_before == terminal_after,
        },
        "authority_mapping": {
            "selector": "selector.py exact blob",
            "D3_cost_KKT": "cost.py exact blob",
            "D2_generator": "generator.py exact blob",
            "D1_and_derivative_law": "option_a_step.py exact blob",
            "terminal_KFE_support": "q1_kfe_validation.py exact blob plus _terminal_kfe exact function source",
        },
    }


def load_update(repository: Path, checkpoint: int) -> tuple[np.ndarray, np.ndarray]:
    directory = repository / PROVINCE / f"checkpoint_{checkpoint:03d}"
    with np.load(directory / "checkpoint_arrays.npz", allow_pickle=False) as saved:
        old = np.array(saved["value"], copy=True)
    with np.load(directory / "direct_update_arrays.npz", allow_pickle=False) as saved:
        full = np.array(saved["next_value"], copy=True)
    return old, full


def focused_test_receipt(junit: Path) -> dict[str, Any]:
    root = ET.parse(junit).getroot()
    cases = []
    for case in root.iter("testcase"):
        cases.append({
            "name": case.attrib["name"],
            "classname": case.attrib.get("classname"),
            "passed": case.find("failure") is None and case.find("error") is None,
        })
    required_fragments = (
        "alpha_one_returns_full_candidate_bitwise_unchanged",
        "one_halving_exact_persisted_replay",
        "nonfinite_input_rejects",
        "wrong_shape_rejects",
        "bitwise_stagnation_rejects",
        "signed_zero_difference_is_not_bitwise_stagnation",
        "no_positive_slope_candidate_exhausts_exact_terminal",
        "zero_slope_fails_strict_positivity",
        "no_positive_slope_magnitude_floor",
    )
    names = [case["name"] for case in cases]
    return {
        "status": "PASS" if cases and all(case["passed"] for case in cases) else "FAIL",
        "test_count": len(cases),
        "cases": cases,
        "required_negative_and_parity_coverage": {
            fragment: any(fragment in name for name in names) for fragment in required_fragments
        },
    }


def build_manifest(output: Path) -> None:
    excluded = {"sealed_manifest.json", "independent_readback_receipt.json"}
    rows = []
    for path in sorted(p for p in output.rglob("*") if p.is_file() and p.name not in excluded):
        rows.append({"path": path.relative_to(output).as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)})
    write_json(output / "sealed_manifest.json", {
        "schema": "CH5_MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTATION_REPLAY_MANIFEST_V1",
        "entry_count": len(rows), "total_bytes": sum(row["bytes"] for row in rows), "entries": rows,
    })
    payload = json.loads((output / "sealed_manifest.json").read_text(encoding="utf-8"))
    bad = []
    for row in payload["entries"]:
        path = output / row["path"]
        if not path.is_file() or path.stat().st_size != row["bytes"] or sha256(path) != row["sha256"]:
            bad.append(row["path"])
    write_json(output / "independent_readback_receipt.json", {
        "status": "PASS" if not bad else "FAIL", "manifest_sha256": sha256(output / "sealed_manifest.json"),
        "entry_count": payload["entry_count"], "total_bytes": payload["total_bytes"], "bad_paths": bad,
        "fresh_scientific_runtime_calls": 0,
    })


def execute(repository: Path, junit: Path) -> str:
    repository = repository.resolve(strict=True)
    output = repository / OUT
    if output.exists():
        raise RuntimeError("fresh evidence root already exists")
    head = git(repository, "rev-parse", "HEAD")
    origin = git(repository, "rev-parse", "origin/main")
    if head != BASELINE or origin != BASELINE:
        raise RuntimeError("live-main baseline binding failed")
    output.mkdir(parents=True)
    write_json(output / "authority_source_binding.json", {
        "status": "PASS", "task_id": TASK_ID, "head": head, "origin_main": origin,
        "authority": [identity(repository / path, repository) for path in AUTHORITY],
        "production_sources": [identity(repository / path, repository) for path in PRODUCTION],
    })
    freeze = source_freeze(repository)
    if not freeze["changed_production_paths_exactly_authorized"] or not freeze["all_frozen_file_blobs_exact"] or not freeze["terminal_kfe_function"]["exact_source_unchanged"]:
        raise RuntimeError("production scope or source-freeze gate failed")
    write_json(output / "production_diff_source_freeze_receipt.json", freeze)

    run004_manifest = repository / ROOT / "sealed_manifest.json"
    design_manifest = repository / DESIGN_ROOT / "sealed_manifest.json"
    design_replay = json.loads((repository / DESIGN_ROOT / "persisted_update_arithmetic_replay.json").read_text(encoding="utf-8"))
    if sha256(run004_manifest) != ACCEPTED_RUN004_MANIFEST or sha256(design_manifest) != ACCEPTED_DESIGN_MANIFEST:
        raise RuntimeError("accepted input manifest mismatch")
    write_json(output / "accepted_input_binding.json", {
        "run004_manifest_sha256": sha256(run004_manifest),
        "accepted_run004_manifest_sha256": ACCEPTED_RUN004_MANIFEST,
        "design_manifest_sha256": sha256(design_manifest),
        "accepted_design_manifest_sha256": ACCEPTED_DESIGN_MANIFEST,
    })

    replay_rows = []
    expected = ((1.0, 0), (1.0, 0), (0.5, 1))
    for checkpoint in range(3):
        old, full = load_update(repository, checkpoint)
        accepted, receipt = monotonicity_preserving_relaxation(old, full, B_NODES)
        design_row = next(
            row for row in design_replay["rows"]
            if row["design"] == "design1_deterministic_halving" and row["update"] == f"{checkpoint}->{checkpoint+1}"
        )
        row = {
            "update": f"{checkpoint}->{checkpoint+1}",
            "receipt": receipt,
            "accepted_state_sha256": field_sha256(accepted),
            "accepted_bitwise_equals_full_candidate": bool(np.array_equal(accepted, full)),
            "design_gate_expected": design_row,
            "alpha_and_halvings_exact": (receipt["accepted_alpha"], receipt["accepted_halvings"]) == expected[checkpoint],
            "design_gate_identity_exact": field_sha256(accepted) == design_row["candidate_sha256"],
        }
        replay_rows.append(row)
    final = replay_rows[2]
    final_attempt = final["receipt"]["attempts"][-1]
    replay_pass = (
        all(row["alpha_and_halvings_exact"] and row["design_gate_identity_exact"] for row in replay_rows)
        and replay_rows[0]["accepted_bitwise_equals_full_candidate"]
        and replay_rows[1]["accepted_bitwise_equals_full_candidate"]
        and final["accepted_state_sha256"] == "987A20DE9252104ECFAB59436433F0C73EEB8C513589B8B0FA98DB64018B66BF"
        and final_attempt["minimum_raw_b_slope"] == 0.005032838660371801
        and final_attempt["positive_edges"] == 760
        and final_attempt["negative_edges"] == 0
        and final_attempt["zero_edges"] == 0
        and final["receipt"]["accepted_value_change_inf"] == 0.017682618173863407
    )
    if not replay_pass:
        raise RuntimeError("exact persisted replay mismatch")
    write_json(output / "three_update_exact_persisted_replay_receipts.json", {"status": "PASS", "rows": replay_rows})
    write_json(output / "checkpoint2_to_3_exact_identity_receipt.json", {
        "status": "PASS", "accepted_alpha": final["receipt"]["accepted_alpha"],
        "accepted_halvings": final["receipt"]["accepted_halvings"],
        "accepted_state_sha256": final["accepted_state_sha256"],
        "minimum_raw_b_slope": final_attempt["minimum_raw_b_slope"],
        "positive_edges": final_attempt["positive_edges"], "negative_edges": final_attempt["negative_edges"],
        "zero_edges": final_attempt["zero_edges"],
        "value_change_inf": final["receipt"]["accepted_value_change_inf"],
    })
    write_json(output / "exact_helper_contract.json", {
        "maximum_halvings": MONOTONICITY_RELAXATION_MAX_HALVINGS,
        "alpha_schedule": "alpha=1 then alpha=2^-k for k=1..52",
        "candidate_formula": "(1-alpha)*V_old+alpha*Vhat",
        "edge_count": 760, "strict_comparison": ">0", "positive_magnitude_floor": None,
        "bitwise_stagnation_rejected": True, "exhaustion_terminal": MONOTONICITY_RELAXATION_EXHAUSTED,
        "full_solve_count_per_update": 1, "additional_solve_from_relaxation": 0,
    })

    tests = focused_test_receipt(junit)
    if tests["status"] != "PASS" or not all(tests["required_negative_and_parity_coverage"].values()):
        raise RuntimeError("focused negative-test gate failed")
    shutil.copyfile(junit, output / "focused_tests.xml")
    tests["junit_sha256"] = sha256(output / "focused_tests.xml")
    write_json(output / "negative_and_focused_test_receipt.json", tests)

    ledger = {
        "persisted_npz_loads": 6, "persisted_json_loads": 1,
        "production_relaxation_helper_persisted_replay_calls": 3,
        "new_direct_linear_solves": 0, "hjb_update_executions": 0, "selector_maps": 0,
        "production_root_helper_calls": 0, "d2_q_rebuilds": 0, "kfe_svd": 0,
        "aggregates_integration": 0, "turn2_replay_rerun": 0, "turn3": 0,
        "matlab": 0, "ge_results": 0, "scientific_retry_tuning": 0,
        "fresh_scientific_runtime_calls": 0,
    }
    write_json(output / "scientific_call_ledger.json", ledger)
    write_json(output / "terminal_receipt.json", {
        "terminal": TERMINAL, "implementation_parity": "PASS", "scientific_call_ledger": ledger,
        "current_modified": False, "successor_published": False, "results_eligibility": False,
    })
    build_manifest(output)
    return TERMINAL


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--focused-test-junit", type=Path, required=True)
    args = parser.parse_args(argv)
    print(execute(args.repository, args.focused_test_junit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
