"""Repair A2max observation receipts and run the same twelve sealed HJB probes once."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import time
from typing import Any

import numpy as np

from validators.multi_province.k1_j160_coordinate_resolved_selector_floor_matched_control import run as observer
from validators.multi_province.k1_j160_first_turn_local_basin_interpolation_diagnostic import run as blocked
from validators.multi_province.k1_j160_first_turn_six_failure_hjb_mechanism_panel import run as mechanism
from validators.multi_province.k1_j160_provincial_first_turn_hjb_viability import run as viability
from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import run as accepted_hjb


REPO = Path(__file__).resolve().parents[3]
TASK_ID = "CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION"
ACTUAL_BASELINE = "a3978f7827aa00e880822c47a2c24157ef092e76"
ACCEPTED_BLOCKED_CANDIDATE = "06b427f4f0c705a17c0d064a5f508c7e3e72ccce"
A2MAX_GATE = 0.01

BLOCKED_ROOT = REPO / "docs/evidence/ch5_mp4c_k1_j160_first_turn_local_basin_interpolation_diagnostic"
BLOCKED_MANIFEST = BLOCKED_ROOT / "sealed_manifest_sha256.json"
BLOCKED_PROBES = BLOCKED_ROOT / "probe_receipts.json"
BLOCKED_PAIR_AUTHORITY = BLOCKED_ROOT / "pair_input_authority.json"
MATLAB_PATH = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m")

EXPECTED_POINT_IDS = (
    "pair01_山西_to_河北_t25", "pair01_山西_to_河北_t50", "pair01_山西_to_河北_t75",
    "pair02_重庆_to_河北_t25", "pair02_重庆_to_河北_t50", "pair02_重庆_to_河北_t75",
    "pair03_江西_to_安徽_t25", "pair03_江西_to_安徽_t50", "pair03_江西_to_安徽_t75",
    "pair04_贵州_to_四川_t25", "pair04_贵州_to_四川_t50", "pair04_贵州_to_四川_t75",
)
EXPECTED_PATTERN = (
    ("HJB_CONVERGED", 34), ("HJB_CONVERGED", 39), ("HJB_CONVERGED", 37),
    ("HJB_CONVERGED", 46), ("HJB_CONVERGED", 57), ("HJB_CONVERGED", 30),
    ("HJB_NOT_CONVERGED", 100), ("HJB_CONVERGED", 77), ("HJB_CONVERGED", 71),
    ("HJB_CONVERGED", 80), ("HJB_NOT_CONVERGED", 100), ("HJB_CONVERGED", 56),
)

SOURCE_IDENTITIES = {
    "accepted_oracle_export": (REPO / "exports/matlab_faithful_two_asset_ha.py", "F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8"),
    "protected_python_hjb": (REPO / "src/ch5_two_asset_hank/matlab_faithful_hjb.py", "6CF6292C71488601CFB8D6A8BFB8C85868A3C3FE281794DCF6B5398F363FFA61"),
    "protected_python_kfe": (REPO / "src/ch5_two_asset_hank/matlab_faithful_kfe.py", "4A0C2734D5C5AF73448C0C3D18F34EB1786DECC7E32A20854FB862A401813ABD"),
    "protected_python_policy": (REPO / "src/ch5_two_asset_hank/matlab_faithful_policy.py", "09D1FD2007A1F5BBEBA023E239FC8442B37F99A72AED293AB9FFEC6FC9DA0E83"),
    "protected_python_operator": (REPO / "src/ch5_two_asset_hank/matlab_faithful_operator.py", "C1FBB8B0A979BE2D8F55806B458D9BB210174C82E1DA45D273DC8773D79375BD"),
    "source_initializer": (REPO / "validators/multi_province/corrected_2018_single_turn/run.py", "9EAF82373EE564E5F27BEA14D49D2177E0637A6969D946C86F519608FFBAE614"),
    "accepted_coordinate_observer": (REPO / "validators/multi_province/k1_j160_coordinate_resolved_selector_floor_matched_control/run.py", "193FE9834B55BED338164DABE5737C7EC6DCB3C2F6B6DDBD4C9C0BF8153857A5"),
    "accepted_blocked_aggregator": (REPO / "validators/multi_province/k1_j160_first_turn_local_basin_interpolation_diagnostic/run.py", "73E1EB63AEA006E0FC0BF893B3BF90C25B8399C6418FEB16A7467BF64BF26F0F"),
    "accepted_blocked_review": (REPO / "docs/CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC_ACCEPTANCE.md", "D5C9A5DCDAB8655B1FF3E466FC8A7CEACA938563C6A9C70F8574D19CC9CE6B53"),
    "current_freeze": (REPO / "docs/CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION_FREEZE_CURRENT.md", "5B54B41B0C17DF05779A2462291539347804C358C526061FD9773DD56D28B61D"),
    "exact_task": (REPO / "tasks/CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_AND_REEXECUTION.md", "495163BA38AD9DA6A135C2714F6A5A696737E6C1993B3543FB0979E530D3DCC6"),
    "matlab_source": (MATLAB_PATH, "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE"),
}

FORBIDDEN_LEDGER_KEYS = (
    "kfe_calls", "endpoint_hjb_calls", "outer_calls", "firm_calls", "wage_recalculation_calls",
    "return_recalculation_calls", "matlab_calls", "k1b_calls", "k2_calls", "ge_calls",
    "downstream_calls", "shock_calls", "irf_calls", "results_writes",
)


def file_sha256(path: Path) -> str:
    return sha256(Path(path).read_bytes()).hexdigest().upper()


def canonical_lf_bytes(path: Path) -> bytes:
    return Path(path).read_bytes().replace(b"\r\n", b"\n")


def canonical_lf_sha256(path: Path) -> str:
    return sha256(canonical_lf_bytes(path)).hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    with Path(path).open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        stream.write("\n")


def verify_blocked_manifest() -> dict[str, Any]:
    manifest = json.loads(BLOCKED_MANIFEST.read_text(encoding="utf-8"))
    entries = []
    for expected in manifest["entries"]:
        path = BLOCKED_ROOT / expected["path"]
        exists = path.is_file()
        byte_hash = file_sha256(path) if exists else None
        canonical_hash = canonical_lf_sha256(path) if exists else None
        canonical_bytes = len(canonical_lf_bytes(path)) if exists else None
        raw_bytes = path.stat().st_size if exists else None
        raw_exact = bool(exists and expected["sha256"] == byte_hash and expected["bytes"] == raw_bytes)
        canonical_exact = bool(exists and expected["sha256"] == canonical_hash and expected["bytes"] == canonical_bytes)
        entries.append({
            "path": expected["path"], "exists": exists, "expected_sha256": expected["sha256"],
            "actual_byte_sha256": byte_hash, "actual_canonical_lf_sha256": canonical_hash,
            "expected_bytes": expected["bytes"], "actual_bytes": raw_bytes,
            "actual_canonical_lf_bytes": canonical_bytes, "raw_exact": raw_exact,
            "canonical_lf_exact": canonical_exact, "pass": raw_exact or canonical_exact,
        })
    receipt = {
        "accepted_candidate": ACCEPTED_BLOCKED_CANDIDATE,
        "manifest_path": str(BLOCKED_MANIFEST.resolve()),
        "expected_manifest_canonical_lf_sha256": "4340B85F960E403592F59317367E2892BCD6D092057138F86B47061ABECF2333",
        "actual_manifest_canonical_lf_sha256": canonical_lf_sha256(BLOCKED_MANIFEST),
        "declared_entry_count": manifest["entry_count"], "entries": entries,
    }
    receipt["pass"] = bool(
        receipt["actual_manifest_canonical_lf_sha256"] == receipt["expected_manifest_canonical_lf_sha256"]
        and receipt["declared_entry_count"] == len(entries) == 50
        and all(item["pass"] for item in entries)
    )
    return receipt


def source_identity_receipt() -> dict[str, Any]:
    manifest = verify_blocked_manifest()
    files = {}
    for name, (path, expected) in SOURCE_IDENTITIES.items():
        exists = path.is_file()
        actual = file_sha256(path) if exists else None
        files[name] = {
            "path": str(path.resolve()), "exists": exists, "expected_sha256": expected,
            "actual_sha256": actual, "pass": bool(exists and actual == expected),
        }
    receipt = {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_REEXECUTION_SOURCE_IDENTITY_V1",
        "task_id": TASK_ID, "actual_baseline": ACTUAL_BASELINE,
        "accepted_blocked_candidate": ACCEPTED_BLOCKED_CANDIDATE,
        "accepted_blocked_manifest": manifest, "files": files,
        "frozen_science": {
            "I": 20, "J": 160, "Nz": 2, "a_bounds": [0.0, 100.0], "b_bounds": [-2.0, 20.0],
            "diagnostic_bridge_h": 1.0, "Delta": 1000.0, "tolerance": 1e-7,
            "maxit": 100, "A2max_gate": A2MAX_GATE, "fresh_source_initialization": True,
        },
        "science_calls_before_clean_preflight": 0,
    }
    receipt["pass"] = bool(manifest["pass"] and all(item["pass"] for item in files.values()))
    return receipt


def load_blocked_authority() -> dict[str, Any]:
    manifest = verify_blocked_manifest()
    pair_authority = json.loads(BLOCKED_PAIR_AUTHORITY.read_text(encoding="utf-8"))
    payload = json.loads(BLOCKED_PROBES.read_text(encoding="utf-8"))
    raw_points = payload["probes"]
    if [item["point_id"] for item in raw_points] != list(EXPECTED_POINT_IDS):
        raise ValueError("LOCAL_BASIN_REEXECUTION_AUTHORITY_BLOCKER: sealed point order mismatch")
    points = []
    for call, (item, expected) in enumerate(zip(raw_points, EXPECTED_PATTERN), start=1):
        if (item["hjb_classification"], item["iterations"]) != expected:
            raise ValueError(f"LOCAL_BASIN_REEXECUTION_AUTHORITY_BLOCKER: blocked outcome mismatch call {call}")
        points.append({
            "call": call, "point_id": item["point_id"], "pair_id": item["pair_id"],
            "pair_index": item["pair_index"], "failure_province": item["failure_province"],
            "success_province": item["success_province"], "t": item["t"],
            "consumed_r_a": item["consumed_r_a"],
            "household_composite_wage": item["household_composite_wage"],
            "hjb_classification": item["hjb_classification"], "iterations": item["iterations"],
            "final_max_abs_delta_v": item["final_max_abs_delta_v"],
            "blocked_mechanism_classification": (item.get("trace_summary") or {}).get("mechanism_classification"),
        })
    pairs_ok = bool(
        pair_authority.get("pass") is True and pair_authority.get("pair_count") == 4
        and all(item.get("non_interpolated_inputs_exact") is True for item in pair_authority["pairs"])
    )
    receipt = {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_REEXECUTION_PAIR_INPUT_AUTHORITY_V1",
        "accepted_blocked_candidate": ACCEPTED_BLOCKED_CANDIDATE,
        "accepted_blocked_manifest_pass": manifest["pass"], "accepted_pair_authority_pass": pairs_ok,
        "accepted_pair_authority": pair_authority, "point_count": len(points), "points": points,
        "synthetic_input_source": str(BLOCKED_PROBES.resolve()),
        "synthetic_input_source_sha256": canonical_lf_sha256(BLOCKED_PROBES),
        "synthetic_inputs_recomputed": False, "endpoint_hjb_reruns": 0,
    }
    receipt["pass"] = bool(manifest["pass"] and pairs_ok and len(points) == 12)
    return receipt


def build_exact_fixtures(authority: dict[str, Any]) -> list[Any]:
    pairs = {item["pair_id"]: item for item in authority["accepted_pair_authority"]["pairs"]}
    fixtures = []
    for point in authority["points"]:
        failure = pairs[point["pair_id"]]["failure"]
        row = {
            **failure, "consumed_r_a": point["consumed_r_a"],
            "raw_entering_r_a": point["consumed_r_a"],
            "household_composite_wage": point["household_composite_wage"],
        }
        fixtures.append(viability.build_fixture(row))
    return fixtures


def input_invariance_receipt(points: list[dict[str, Any]], fixtures: list[Any]) -> dict[str, Any]:
    configurations = [accepted_hjb.fixture_config(item) for item in fixtures]
    varying = sorted(
        key for key in configurations[0]
        if any(config[key] != configurations[0][key] for config in configurations[1:])
    )
    entries = []
    for point, fixture, config in zip(points, fixtures, configurations):
        checks = {
            "exact_sealed_r_a": config["inputs.r_a"] == point["consumed_r_a"],
            "exact_sealed_wage": config["inputs.wages[0]"] == point["household_composite_wage"],
            "I": fixture.grid.b.size == 20, "J": fixture.grid.a.size == 160, "Nz": fixture.grid.z.size == 2,
            "a_bounds": fixture.grid.a[[0, -1]].tolist() == [0.0, 100.0],
            "b_bounds": fixture.grid.b[[0, -1]].tolist() == [-2.0, 20.0],
            "Delta": fixture.numerics.delta == 1000.0,
            "tolerance": fixture.numerics.convergence_tolerance == 1e-7,
            "maxit": fixture.numerics.max_iterations == 100,
            "initial_value_finite": bool(np.isfinite(fixture.initial_value).all()),
            "baseline_labor_finite": bool(np.isfinite(fixture.baseline_labor).all()),
        }
        entries.append({
            "point_id": point["point_id"], "checks": checks, "fresh_source_initialization": True,
            "warm_start": False, "initial_value_sha256": accepted_hjb.array_sha256(fixture.initial_value),
            "baseline_labor_sha256": accepted_hjb.array_sha256(fixture.baseline_labor),
        })
    receipt = {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_REEXECUTION_INPUT_INVARIANCE_V1",
        "point_count": len(points), "varying_fields": varying,
        "allowed_varying_fields": ["inputs.r_a", "inputs.wages[0]"],
        "fresh_initial_value_object_count": len({id(item.initial_value) for item in fixtures}),
        "fresh_baseline_labor_object_count": len({id(item.baseline_labor) for item in fixtures}),
        "all_exact_sealed_ra_w_consumed": all(
            config["inputs.r_a"] == point["consumed_r_a"]
            and config["inputs.wages[0]"] == point["household_composite_wage"]
            for point, config in zip(points, configurations)
        ),
        "entries": entries,
    }
    receipt["pass"] = bool(
        len(points) == len(fixtures) == 12 and varying == ["inputs.r_a", "inputs.wages[0]"]
        and receipt["fresh_initial_value_object_count"] == 12
        and receipt["fresh_baseline_labor_object_count"] == 12
        and receipt["all_exact_sealed_ra_w_consumed"]
        and all(all(item["checks"].values()) for item in entries)
    )
    return receipt


def scientific_a2max_receipt(trace: dict[str, Any], *, scientific_iteration_count: int) -> dict[str, Any]:
    rows = trace.get("iterations", [])
    sequence = [float(row["operator"]["a2max"]) for row in rows]
    finite = [bool(np.isfinite(value)) for value in sequence]
    legal = [bool(is_finite and value <= A2MAX_GATE) for value, is_finite in zip(sequence, finite)]
    max_index = int(np.argmax(sequence)) if sequence and all(finite) else None
    post = trace.get("post_convergence_operator")
    length_matches = len(sequence) == scientific_iteration_count
    receipt_complete = bool(length_matches and len(sequence) > 0 and all(finite))
    return {
        "schema": "CH5_MP4C_K1_J160_SCIENTIFIC_A2MAX_RECEIPT_V1",
        "definition": "source-generator max(abs(sum(A,2))) for actual HJB scientific iterations only",
        "scientific_iteration_count": int(scientific_iteration_count),
        "scientific_A2max_sequence": sequence, "sequence_length": len(sequence),
        "sequence_length_matches_scientific_iteration_count": length_matches,
        "all_scientific_A2max_finite": all(finite),
        "max_scientific_A2max": sequence[max_index] if max_index is not None else None,
        "max_scientific_A2max_iteration": max_index + 1 if max_index is not None else None,
        "first_scientific_illegal_iteration": next((index + 1 for index, ok in enumerate(legal) if not ok), None),
        "scientific_operator_legal": bool(receipt_complete and all(legal)),
        "receipt_complete": receipt_complete,
        "post_convergence_system_matrix_metric": None if post is None else {
            "iteration_label": post.get("iteration"), "observed_row_sum_metric": post.get("a2max"),
            "classification": "NOT_SCIENTIFIC_A2MAX", "legality_treatment": "EXCLUDED_FROM_LEGALITY",
        },
    }


def receipt_repair_invariance() -> dict[str, Any]:
    accepted = json.loads(
        (REPO / "docs/evidence/ch5_mp4c_k1_j160_coordinate_resolved_selector_floor_matched_control/instrumentation_invariance_receipt.json").read_text(encoding="utf-8")
    )
    synthetic = {
        "iterations": [
            {"iteration": 1, "operator": {"iteration": 1, "a2max": 0.002, "legal": True}},
            {"iteration": 2, "operator": {"iteration": 2, "a2max": 0.003, "legal": True}},
        ],
        "post_convergence_operator": {"iteration": 3, "a2max": 1.5, "legal": False},
    }
    repaired = scientific_a2max_receipt(synthetic, scientific_iteration_count=2)
    receipt = {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_RECEIPT_REPAIR_INVARIANCE_V1",
        "accepted_coordinate_observer_invariance_pass": accepted.get("pass") is True,
        "accepted_observer_imported_unchanged": observer.observe_coordinate_hjb.__module__.endswith(
            "k1_j160_coordinate_resolved_selector_floor_matched_control.run"
        ),
        "repair_runs_after_observer_returns": True,
        "repair_reads_copied_iteration_operator_receipts_only": True,
        "repair_changes_hjb_arrays": False, "repair_changes_selectors": False,
        "repair_changes_derivative_floors": False, "repair_changes_sparse_solve": False,
        "repair_changes_iteration_order": False, "repair_changes_convergence_statistic": False,
        "repair_changes_iteration_count": False, "repair_changes_terminal_outcome": False,
        "repair_changes_initialization": False, "parity_hjb_calls": 0,
        "deterministic_fixture_sequence_exact": repaired["scientific_A2max_sequence"] == [0.002, 0.003],
        "deterministic_fixture_post_matrix_excluded": repaired["max_scientific_A2max"] == 0.003,
    }
    receipt["pass"] = bool(
        receipt["accepted_coordinate_observer_invariance_pass"]
        and receipt["accepted_observer_imported_unchanged"]
        and receipt["deterministic_fixture_sequence_exact"]
        and receipt["deterministic_fixture_post_matrix_excluded"]
    )
    return receipt


def empty_call_ledger() -> dict[str, Any]:
    ledger = {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_REEXECUTION_CALL_LEDGER_V1",
        "hjb_budget": 12, "hjb_calls_started": 0, "hjb_calls_completed": 0, "hjb_hard_errors": 0,
        "scientific_retries": 0, "engineering_retry_budget": 1, "engineering_retries_used": 1,
        "probe_calls": [],
    }
    ledger.update({key: 0 for key in FORBIDDEN_LEDGER_KEYS})
    return ledger


def preflight(output_root: Path) -> int:
    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=False)
    source = source_identity_receipt()
    authority = load_blocked_authority()
    fixtures = build_exact_fixtures(authority)
    inputs = input_invariance_receipt(authority["points"], fixtures)
    invariance = receipt_repair_invariance()
    ledger = empty_call_ledger()
    write_json(root / "source_identity.json", source)
    write_json(root / "pair_input_authority.json", authority)
    write_json(root / "input_invariance_receipt.json", inputs)
    write_json(root / "receipt_repair_invariance.json", invariance)
    write_json(root / "pre_science_call_ledger.json", ledger)
    passed = bool(source["pass"] and authority["pass"] and inputs["pass"] and invariance["pass"])
    write_json(root / "preflight_complete.json", {"status": "PASS" if passed else "FAIL", "science_calls": 0})
    return 0 if passed else 1


def _trace_events(trace: dict[str, Any], *, converged: bool) -> dict[str, Any]:
    rows = trace.get("iterations", [])
    classified = mechanism.classify_trace(trace, replay_converged=False) if rows else {}
    return {
        "all_finite_checks_pass": all(all(row["finite_checks"].values()) for row in rows),
        "all_shape_checks_pass": all(all(row["shape_checks"].values()) for row in rows),
        "first_policy_or_selector_switch_iteration": classified.get("first_policy_or_selector_switch_iteration"),
        "first_value_stat_non_decrease_iteration": classified.get("first_value_stat_non_decrease_iteration"),
        "first_derivative_floor_hit_iteration": classified.get("first_derivative_floor_hit_iteration"),
        "mechanism_classification": None if converged else classified.get("classification"),
        "mechanism_event_ordering": [] if converged else classified.get("event_ordering", []),
    }


def execute(output_root: Path) -> int:
    root = Path(output_root)
    if json.loads((root / "preflight_complete.json").read_text(encoding="utf-8")) != {"science_calls": 0, "status": "PASS"}:
        raise RuntimeError("clean preflight PASS required")
    if (root / "science_started.json").exists():
        raise FileExistsError("the exactly-once controlled reexecution has already started")
    authority = json.loads((root / "pair_input_authority.json").read_text(encoding="utf-8"))
    fixtures = build_exact_fixtures(authority)
    if not input_invariance_receipt(authority["points"], fixtures)["pass"]:
        raise RuntimeError("sealed input invariance no longer passes")
    ledger = json.loads((root / "pre_science_call_ledger.json").read_text(encoding="utf-8"))
    write_json(root / "science_started.json", {
        "task_id": TASK_ID, "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "point_order": [item["point_id"] for item in authority["points"]],
        "fresh_source_initialization": True,
    })
    outcomes = []
    for point, fixture in zip(authority["points"], fixtures):
        started = {
            "call": point["call"], "point_id": point["point_id"], "pair_id": point["pair_id"], "t": point["t"],
            "consumed_r_a": point["consumed_r_a"], "household_composite_wage": point["household_composite_wage"],
            "fresh_source_initialization": True, "warm_start": False,
            "initial_value_sha256": accepted_hjb.array_sha256(fixture.initial_value),
            "baseline_labor_sha256": accepted_hjb.array_sha256(fixture.baseline_labor),
        }
        write_json(root / f"{point['point_id']}_started.json", started)
        ledger["hjb_calls_started"] += 1
        write_json(root / f"ledger_before_{point['point_id']}.json", ledger)
        try:
            result, trace = observer.observe_coordinate_hjb(*fixture.arguments())
            ledger["hjb_calls_completed"] += 1
            a2max = scientific_a2max_receipt(trace, scientific_iteration_count=int(result.iterations))
            events = _trace_events(trace, converged=bool(result.converged))
            classification = "HJB_CONVERGED" if result.converged else "HJB_NOT_CONVERGED"
            valid = bool(
                a2max["receipt_complete"] and a2max["scientific_operator_legal"]
                and events["all_finite_checks_pass"] and events["all_shape_checks_pass"]
                and np.isfinite(result.convergence_statistic)
            )
            outcome = {
                **point, "hjb_classification": classification, "converged": bool(result.converged),
                "iterations": int(result.iterations), "final_max_abs_delta_v": float(result.convergence_statistic),
                "scientific_a2max_receipt": a2max, "trace_events": events,
                "numerically_valid": valid, "hard_error": None, "fresh_initialization_receipt": started,
                "kfe_ran": False, "retried": False,
            }
        except Exception as exc:  # a started HJB is never retried
            ledger["hjb_hard_errors"] += 1
            outcome = {
                **point, "hjb_classification": "HJB_HARD_ERROR", "converged": False,
                "iterations": None, "final_max_abs_delta_v": None, "scientific_a2max_receipt": None,
                "trace_events": None, "numerically_valid": False,
                "hard_error": {"type": type(exc).__name__, "message": str(exc)},
                "fresh_initialization_receipt": started, "kfe_ran": False, "retried": False,
            }
        write_json(root / f"{point['point_id']}_outcome.json", outcome)
        outcomes.append(outcome)
        ledger["probe_calls"].append({
            "call": point["call"], "point_id": point["point_id"],
            "classification": outcome["hjb_classification"], "numerically_valid": outcome["numerically_valid"],
            "completed": outcome["hard_error"] is None, "retried": False,
        })
    write_json(root / "probe_receipts.json", {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_A2MAX_REEXECUTION_PROBE_RECEIPTS_V1",
        "probe_count": len(outcomes), "probes": outcomes,
    })
    write_json(root / "call_ledger.json", ledger)
    write_json(root / "execution_complete.json", {
        "status": "EXACT_TWELVE_A2MAX_RECEIPT_REEXECUTION_COMPLETE",
        "hjb_calls_started": ledger["hjb_calls_started"], "hjb_calls_completed": ledger["hjb_calls_completed"],
        "hjb_hard_errors": ledger["hjb_hard_errors"], "kfe_calls": 0,
        "scientific_retries": 0, "results_eligibility": False,
    })
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("preflight", "run"))
    parser.add_argument("output_root", type=Path)
    args = parser.parse_args()
    return preflight(args.output_root) if args.command == "preflight" else execute(args.output_root)


if __name__ == "__main__":
    raise SystemExit(main())
