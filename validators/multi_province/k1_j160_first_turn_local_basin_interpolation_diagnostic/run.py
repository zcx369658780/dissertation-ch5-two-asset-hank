"""Run exactly twelve frozen J160 synthetic local-basin HJB probes."""
from __future__ import annotations

import argparse
import csv
from hashlib import sha256
import json
from pathlib import Path
import time
from typing import Any

import numpy as np

from validators.multi_province.k1_j160_coordinate_resolved_selector_floor_matched_control import run as coordinate
from validators.multi_province.k1_j160_first_turn_six_failure_hjb_mechanism_panel import run as mechanism
from validators.multi_province.k1_j160_provincial_first_turn_hjb_viability import run as viability
from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import run as accepted_hjb


REPO = Path(__file__).resolve().parents[3]
TASK_ID = "CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC"
ACTUAL_BASELINE = "3c64d28c8779baa72cd8208048a0a15751552b8b"
ACCEPTED_COORDINATE_CANDIDATE = "49ea4c12692c669701cdc7bcf8fd02267a068090"
PAIR_KEYS = (
    ((3, "山西"), (2, "河北")),
    ((21, "重庆"), (2, "河北")),
    ((13, "江西"), (11, "安徽")),
    ((23, "贵州"), (22, "四川")),
)
PROBE_T = (0.25, 0.50, 0.75)

ENVELOPE_ROOT = REPO / "docs/evidence/ch5_mp4c_k1_first_turn_provincial_input_outcome_envelope_audit"
ENVELOPE_TABLE = ENVELOPE_ROOT / "province_input_outcome_table.json"
COORDINATE_ROOT = REPO / "docs/evidence/ch5_mp4c_k1_j160_coordinate_resolved_selector_floor_matched_control"
COORDINATE_MANIFEST = COORDINATE_ROOT / "sealed_manifest_sha256.json"
COORDINATE_INVARIANCE = COORDINATE_ROOT / "instrumentation_invariance_receipt.json"
MATLAB_PATH = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m")

SOURCE_IDENTITIES = {
    "accepted_oracle_export": (REPO / "exports/matlab_faithful_two_asset_ha.py", "F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8"),
    "protected_python_hjb": (REPO / "src/ch5_two_asset_hank/matlab_faithful_hjb.py", "6CF6292C71488601CFB8D6A8BFB8C85868A3C3FE281794DCF6B5398F363FFA61"),
    "protected_python_kfe": (REPO / "src/ch5_two_asset_hank/matlab_faithful_kfe.py", "4A0C2734D5C5AF73448C0C3D18F34EB1786DECC7E32A20854FB862A401813ABD"),
    "protected_python_policy": (REPO / "src/ch5_two_asset_hank/matlab_faithful_policy.py", "09D1FD2007A1F5BBEBA023E239FC8442B37F99A72AED293AB9FFEC6FC9DA0E83"),
    "protected_python_operator": (REPO / "src/ch5_two_asset_hank/matlab_faithful_operator.py", "C1FBB8B0A979BE2D8F55806B458D9BB210174C82E1DA45D273DC8773D79375BD"),
    "source_initializer": (REPO / "validators/multi_province/corrected_2018_single_turn/run.py", "9EAF82373EE564E5F27BEA14D49D2177E0637A6969D946C86F519608FFBAE614"),
    "accepted_j640_observer": (REPO / "validators/multi_province/k1_j640_hjb_nonconvergence_mechanism_diagnostic/run.py", "F1E4D5A54293431C2C5EE428715C28AF4CCD9E5851D99DB544A0BA1BEEBAF867"),
    "accepted_six_failure_observer": (REPO / "validators/multi_province/k1_j160_first_turn_six_failure_hjb_mechanism_panel/run.py", "B83900B68B9927E2A5C9243B9137F3DCD3EA713DA96CF595C4A863A50B24C461"),
    "matlab_source": (MATLAB_PATH, "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE"),
    "accepted_coordinate_manifest": (COORDINATE_MANIFEST, "2B5D8D809C927085545358F7607DC91E73783818C3A211F9676C9BD959AE8127"),
    "accepted_envelope_table": (ENVELOPE_TABLE, "0366B0F5D8893DBF71C4A88DCC3A13A5FAA2E8197441A51658F8C38D8297B7DE"),
    "current_freeze": (REPO / "docs/CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC_FREEZE_CURRENT.md", "0D0DD4DC034FB09BA4FC340DB245584DD4500677B3252B3A4F1726EF1CCF0BEC"),
    "exact_task": (REPO / "tasks/CH5_MP4C_K1_J160_FIRST_TURN_LOCAL_BASIN_INTERPOLATION_DIAGNOSTIC.md", "59C8E19DC3F837164BCF278F5BC80C9B38261D47F65094869D0D280D7AC05BCC"),
}

FORBIDDEN_LEDGER_KEYS = (
    "kfe_calls", "endpoint_hjb_calls", "province_hjb_reruns", "outer_calls", "firm_calls",
    "wage_recalculation_calls", "return_recalculation_calls", "matlab_calls", "k1b_calls",
    "k2_calls", "ge_calls", "downstream_calls", "shock_calls", "irf_calls", "results_writes",
)


def file_sha256(path: Path) -> str:
    return sha256(Path(path).read_bytes()).hexdigest().upper()


def write_json(path: Path, value: Any, *, exclusive: bool = True) -> None:
    payload = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n"
    mode = "x" if exclusive else "w"
    with Path(path).open(mode, encoding="utf-8", newline="\n") as stream:
        stream.write(payload)


def source_identity_receipt() -> dict[str, Any]:
    inherited = coordinate.source_identity_receipt()
    files = {}
    for name, (path, expected) in SOURCE_IDENTITIES.items():
        exists = path.is_file()
        actual = file_sha256(path) if exists else None
        files[name] = {
            "path": str(path.resolve()), "exists": exists, "expected_sha256": expected,
            "actual_sha256": actual, "pass": exists and actual == expected,
        }
    receipt = {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_SOURCE_IDENTITY_V1",
        "task_id": TASK_ID, "actual_baseline": ACTUAL_BASELINE,
        "accepted_coordinate_candidate": ACCEPTED_COORDINATE_CANDIDATE,
        "accepted_coordinate_source_chain_pass": inherited["pass"],
        "files": files,
        "frozen_science": {
            "I": 20, "J": 160, "Nz": 2, "a_bounds": [0.0, 100.0],
            "b_bounds": [-2.0, 20.0], "diagnostic_bridge_h": 1.0,
            "Delta": 1000.0, "tolerance": 1e-7, "maxit": 100,
            "A2max_gate": 0.01, "fresh_source_initialization": True,
        },
        "science_calls_before_clean_preflight": 0,
    }
    receipt["pass"] = bool(inherited["pass"] and all(item["pass"] for item in files.values()))
    return receipt


def _non_interpolated_inputs(input_row: dict[str, Any], outcome_row: dict[str, Any]) -> dict[str, Any]:
    return {
        "r_b": input_row["r_b"], "borrowing_rate_gap": input_row["borrowing_rate_gap"],
        "tau": input_row["tau"], "transfer_income": input_row["transfer_income"],
        "params": input_row["params"], "accepted_numerics": input_row["accepted_numerics"],
        "return_guard_state": input_row["return_guard_state"],
        "input_receipt_wage_guard_state_metadata": input_row["wage_guard_state"],
        "transfer_control_state": input_row["transfer_control_state"],
        "corrected_upstream_wjt_guard_state": outcome_row["wage_guard_state"],
        "guarded_wjt": outcome_row["guarded_wjt"],
        "raw_provincial_wjt_status": outcome_row["raw_provincial_wjt_status"],
        "migration_costs": [0.0], "labor_weights": [1.0],
    }


def load_pair_authority() -> dict[str, Any]:
    input_authority = viability.load_first_turn_authority()
    inputs = {(row["province_index"], row["province"]): row for row in input_authority["provinces"]}
    envelope_payload = json.loads(ENVELOPE_TABLE.read_text(encoding="utf-8"))
    outcomes = {(row["province_index"], row["province"]): row for row in envelope_payload["rows"]}
    pairs = []
    for pair_index, (failure_key, success_key) in enumerate(PAIR_KEYS, start=1):
        if failure_key not in inputs or success_key not in inputs or failure_key not in outcomes or success_key not in outcomes:
            raise ValueError(f"LOCAL_BASIN_PAIR_INPUT_AUTHORITY_BLOCKER: missing pair authority {failure_key}->{success_key}")
        failure_input, success_input = inputs[failure_key], inputs[success_key]
        failure_outcome, success_outcome = outcomes[failure_key], outcomes[success_key]
        if (failure_outcome["accepted_hjb_classification"], failure_outcome["iterations"]) != ("HJB_NOT_CONVERGED", 100):
            raise ValueError(f"LOCAL_BASIN_PAIR_INPUT_AUTHORITY_BLOCKER: failure endpoint mismatch {failure_key}")
        if success_outcome["accepted_hjb_classification"] != "HJB_CONVERGED":
            raise ValueError(f"LOCAL_BASIN_PAIR_INPUT_AUTHORITY_BLOCKER: success endpoint mismatch {success_key}")
        failure_common = _non_interpolated_inputs(failure_input, failure_outcome)
        success_common = _non_interpolated_inputs(success_input, success_outcome)
        exact = failure_common == success_common
        pairs.append({
            "pair_index": pair_index,
            "pair_id": f"pair{pair_index:02d}_{failure_key[1]}_to_{success_key[1]}",
            "failure": {
                **failure_input, "accepted_hjb_classification": failure_outcome["accepted_hjb_classification"],
                "accepted_iterations": failure_outcome["iterations"],
                "accepted_final_convergence_statistic": failure_outcome["final_convergence_statistic"],
                "accepted_maximum_a2max": failure_outcome["maximum_a2max"],
            },
            "success": {
                **success_input, "accepted_hjb_classification": success_outcome["accepted_hjb_classification"],
                "accepted_iterations": success_outcome["iterations"],
                "accepted_final_convergence_statistic": success_outcome["final_convergence_statistic"],
                "accepted_maximum_a2max": success_outcome["maximum_a2max"],
            },
            "failure_non_interpolated_inputs": failure_common,
            "success_non_interpolated_inputs": success_common,
            "non_interpolated_inputs_exact": exact,
        })
    receipt = {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_PAIR_INPUT_AUTHORITY_V1",
        "accepted_first_turn_candidate": input_authority["accepted_candidate"],
        "accepted_envelope_table_sha256": file_sha256(ENVELOPE_TABLE),
        "pair_count": len(pairs), "pairs": pairs,
        "endpoint_hjb_reruns": 0,
    }
    receipt["pass"] = bool(len(pairs) == 4 and all(item["non_interpolated_inputs_exact"] for item in pairs))
    if not receipt["pass"]:
        raise ValueError("LOCAL_BASIN_PAIR_INPUT_AUTHORITY_BLOCKER: non-interpolated inputs differ")
    return receipt


def build_probe_fixtures(authority: dict[str, Any]) -> tuple[list[dict[str, Any]], list[Any]]:
    points: list[dict[str, Any]] = []
    fixtures: list[Any] = []
    for pair in authority["pairs"]:
        failure, success = pair["failure"], pair["success"]
        for t in PROBE_T:
            ra = (1.0 - t) * failure["consumed_r_a"] + t * success["consumed_r_a"]
            wage = (1.0 - t) * failure["household_composite_wage"] + t * success["household_composite_wage"]
            synthetic = {**failure, "consumed_r_a": ra, "raw_entering_r_a": ra, "household_composite_wage": wage}
            fixture = viability.build_fixture(synthetic)
            point = {
                "call": len(points) + 1, "pair_index": pair["pair_index"], "pair_id": pair["pair_id"],
                "failure_province": failure["province"], "success_province": success["province"],
                "t": t, "consumed_r_a": ra, "household_composite_wage": wage,
                "point_id": f"{pair['pair_id']}_t{int(t * 100):02d}",
                "formula": "(1-t)*failure+t*success",
                "common_non_interpolated_inputs_exact": pair["non_interpolated_inputs_exact"],
            }
            points.append(point); fixtures.append(fixture)
    return points, fixtures


def input_invariance_receipt(points: list[dict[str, Any]], fixtures: list[Any]) -> dict[str, Any]:
    if len(points) != 12 or len(fixtures) != 12:
        raise ValueError("local-basin input invariance requires exactly twelve fixtures")
    configurations = [accepted_hjb.fixture_config(fixture) for fixture in fixtures]
    varying = sorted(
        key for key in configurations[0]
        if any(configuration[key] != configurations[0][key] for configuration in configurations[1:])
    )
    entries = []
    for point, fixture, config in zip(points, fixtures, configurations):
        checks = {
            "I": fixture.grid.b.size == 20, "J": fixture.grid.a.size == 160, "Nz": fixture.grid.z.size == 2,
            "a_bounds": fixture.grid.a[[0, -1]].tolist() == [0.0, 100.0],
            "b_bounds": fixture.grid.b[[0, -1]].tolist() == [-2.0, 20.0],
            "synthetic_ra_exact": config["inputs.r_a"] == point["consumed_r_a"],
            "synthetic_w_exact": config["inputs.wages[0]"] == point["household_composite_wage"],
            "Delta": config["numerics.delta"] == 1000.0,
            "tolerance": config["numerics.convergence_tolerance"] == 1e-7,
            "maxit": config["numerics.max_iterations"] == 100,
            "initial_value_finite": bool(np.isfinite(fixture.initial_value).all()),
            "baseline_labor_finite": bool(np.isfinite(fixture.baseline_labor).all()),
            "pair_common_inputs": point["common_non_interpolated_inputs_exact"],
        }
        entries.append({
            "point_id": point["point_id"], "checks": checks, "fresh_source_initialization": True,
            "warm_start": False, "initial_value_sha256": accepted_hjb.array_sha256(fixture.initial_value),
            "baseline_labor_sha256": accepted_hjb.array_sha256(fixture.baseline_labor),
        })
    receipt = {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_INPUT_INVARIANCE_V1",
        "point_count": 12, "varying_fields": varying,
        "allowed_varying_fields": ["inputs.r_a", "inputs.wages[0]"],
        "fresh_initial_value_object_count": len({id(item.initial_value) for item in fixtures}),
        "fresh_baseline_labor_object_count": len({id(item.baseline_labor) for item in fixtures}),
        "entries": entries,
    }
    receipt["pass"] = bool(
        varying == ["inputs.r_a", "inputs.wages[0]"]
        and receipt["fresh_initial_value_object_count"] == 12
        and receipt["fresh_baseline_labor_object_count"] == 12
        and all(all(item["checks"].values()) for item in entries)
    )
    return receipt


def instrumentation_invariance_receipt() -> dict[str, Any]:
    accepted = json.loads(COORDINATE_INVARIANCE.read_text(encoding="utf-8"))
    receipt = {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_INSTRUMENTATION_INVARIANCE_V1",
        "accepted_coordinate_receipt_path": str(COORDINATE_INVARIANCE.resolve()),
        "accepted_coordinate_receipt_sha256": file_sha256(COORDINATE_INVARIANCE),
        "accepted_coordinate_invariance_pass": accepted.get("pass") is True,
        "observer_imported_without_modification": coordinate.observe_coordinate_hjb.__module__.endswith(
            "k1_j160_coordinate_resolved_selector_floor_matched_control.run"
        ),
        "scientific_control_flow_reads_observations": False,
        "retains_state_between_probes": False, "new_hjb_calls_for_invariance": 0,
    }
    receipt["pass"] = bool(receipt["accepted_coordinate_invariance_pass"] and receipt["observer_imported_without_modification"])
    return receipt


def empty_call_ledger() -> dict[str, Any]:
    ledger = {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_CALL_LEDGER_V1",
        "hjb_budget": 12, "hjb_calls_started": 0, "hjb_calls_completed": 0,
        "hjb_hard_errors": 0, "scientific_retries": 0,
        "engineering_retry_budget": 1, "engineering_retries_used": 0, "probe_calls": [],
    }
    ledger.update({key: 0 for key in FORBIDDEN_LEDGER_KEYS})
    return ledger


def _write_probe_points(path: Path, points: list[dict[str, Any]]) -> None:
    with Path(path).open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=(
            "call", "pair_index", "pair_id", "failure_province", "success_province", "t",
            "consumed_r_a", "household_composite_wage", "formula", "common_non_interpolated_inputs_exact",
        ))
        writer.writeheader()
        for point in points:
            writer.writerow({key: point[key] for key in writer.fieldnames})


def preflight(output_root: Path) -> int:
    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=False)
    source = source_identity_receipt()
    authority = load_pair_authority()
    points, fixtures = build_probe_fixtures(authority)
    invariance = input_invariance_receipt(points, fixtures)
    instrumentation = instrumentation_invariance_receipt()
    ledger = empty_call_ledger()
    write_json(root / "source_identity.json", source)
    write_json(root / "pair_input_authority.json", authority)
    write_json(root / "input_invariance_receipt.json", invariance)
    write_json(root / "instrumentation_invariance_receipt.json", instrumentation)
    _write_probe_points(root / "probe_points.csv", points)
    write_json(root / "pre_science_call_ledger.json", ledger)
    passed = bool(source["pass"] and authority["pass"] and invariance["pass"] and instrumentation["pass"])
    write_json(root / "preflight_complete.json", {"status": "PASS" if passed else "FAIL", "science_calls": 0})
    return 0 if passed else 1


def scientific_operator_gate(trace: dict[str, Any]) -> dict[str, Any]:
    """Evaluate only source-generator observations, never the later implicit system matrix."""
    rows = trace.get("iterations", [])
    operators = [row["operator"] for row in rows]
    illegal = [item for item in operators if not item["legal"]]
    return {
        "maximum_a2max": max((item["a2max"] for item in operators), default=None),
        "first_illegal_iteration": illegal[0]["iteration"] if illegal else None,
        "all_iteration_operators_legal": not illegal,
        "post_convergence_system_matrix_observation": trace.get("post_convergence_operator"),
        "post_convergence_system_matrix_excluded_from_generator_gate": True,
    }


def _trace_summary(trace: dict[str, Any], *, converged: bool) -> dict[str, Any]:
    rows = trace.get("iterations", [])
    descriptive = mechanism.classify_trace(trace, replay_converged=False) if rows else {}
    operator_gate = scientific_operator_gate(trace)
    return {
        "iteration_count_observed": len(rows),
        **operator_gate,
        "all_finite_checks_pass": all(all(row["finite_checks"].values()) for row in rows),
        "all_shape_checks_pass": all(all(row["shape_checks"].values()) for row in rows),
        "first_policy_or_selector_switch_iteration": descriptive.get("first_policy_or_selector_switch_iteration"),
        "first_value_stat_non_decrease_iteration": descriptive.get("first_value_stat_non_decrease_iteration"),
        "first_derivative_floor_hit_iteration": descriptive.get("first_derivative_floor_hit_iteration"),
        "mechanism_classification": None if converged else descriptive.get("classification"),
        "mechanism_event_ordering": [] if converged else descriptive.get("event_ordering", []),
        "cycle_evidence": trace.get("cycle_evidence"),
    }


def execute(output_root: Path) -> int:
    root = Path(output_root)
    status = json.loads((root / "preflight_complete.json").read_text(encoding="utf-8"))
    if status != {"science_calls": 0, "status": "PASS"}:
        raise RuntimeError("clean preflight PASS is required before science")
    if (root / "science_started.json").exists():
        raise FileExistsError("the exactly-once twelve-probe HJB panel has already started")
    authority = json.loads((root / "pair_input_authority.json").read_text(encoding="utf-8"))
    points, fixtures = build_probe_fixtures(authority)
    invariance = input_invariance_receipt(points, fixtures)
    if not invariance["pass"]:
        raise RuntimeError("fixture invariance no longer passes")
    ledger = json.loads((root / "pre_science_call_ledger.json").read_text(encoding="utf-8"))
    write_json(root / "science_started.json", {
        "task_id": TASK_ID, "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "probe_order": [point["point_id"] for point in points], "fresh_initialization": True,
    })
    receipts = []
    for point, fixture in zip(points, fixtures):
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
            result, trace = coordinate.observe_coordinate_hjb(*fixture.arguments())
            ledger["hjb_calls_completed"] += 1
            trace_summary = _trace_summary(trace, converged=bool(result.converged))
            numerically_valid = bool(
                trace_summary["all_iteration_operators_legal"]
                and trace_summary["all_finite_checks_pass"]
                and trace_summary["all_shape_checks_pass"]
                and trace_summary["maximum_a2max"] is not None
                and trace_summary["maximum_a2max"] <= 0.01
                and np.isfinite(result.convergence_statistic)
            )
            outcome = {
                **point, "hjb_classification": "HJB_CONVERGED" if result.converged else "HJB_NOT_CONVERGED",
                "converged": bool(result.converged), "iterations": int(result.iterations),
                "final_max_abs_delta_v": float(result.convergence_statistic),
                "numerically_valid": numerically_valid, "hard_error": None,
                "fresh_initialization_receipt": started, "trace_summary": trace_summary,
                "kfe_ran": False, "retried": False,
            }
        except Exception as exc:  # one started call remains one outcome; never retry
            ledger["hjb_hard_errors"] += 1
            outcome = {
                **point, "hjb_classification": "HJB_HARD_ERROR", "converged": False,
                "iterations": None, "final_max_abs_delta_v": None, "numerically_valid": False,
                "hard_error": {"type": type(exc).__name__, "message": str(exc)},
                "fresh_initialization_receipt": started, "trace_summary": None,
                "kfe_ran": False, "retried": False,
            }
        write_json(root / f"{point['point_id']}_outcome.json", outcome)
        receipts.append(outcome)
        ledger["probe_calls"].append({
            "call": point["call"], "point_id": point["point_id"],
            "completed": outcome["hard_error"] is None, "classification": outcome["hjb_classification"],
            "numerically_valid": outcome["numerically_valid"], "retried": False,
        })
    write_json(root / "probe_receipts.json", {
        "schema": "CH5_MP4C_K1_J160_LOCAL_BASIN_PROBE_RECEIPTS_V1", "probe_count": len(receipts),
        "probes": receipts,
    })
    write_json(root / "call_ledger.json", ledger)
    write_json(root / "execution_complete.json", {
        "status": "EXACT_TWELVE_LOCAL_BASIN_HJB_PROBES_COMPLETE",
        "hjb_calls_started": ledger["hjb_calls_started"], "hjb_calls_completed": ledger["hjb_calls_completed"],
        "hjb_hard_errors": ledger["hjb_hard_errors"], "kfe_calls": 0,
        "scientific_retries": 0, "results_eligibility": False,
    })
    return 0


def pair_classification(outcomes: list[dict[str, Any]]) -> str:
    if len(outcomes) != 3:
        raise ValueError("pair classification requires exactly three interior outcomes")
    if any(not item["numerically_valid"] for item in outcomes):
        return "PAIR_NUMERICAL_INVALIDITY_BLOCKER"
    interior = [bool(item["converged"]) for item in outcomes]
    if all(interior):
        return "ALL_INTERIOR_PROBES_CONVERGE"
    if not any(interior):
        return "ALL_INTERIOR_PROBES_FAIL"
    ordered = [False, *interior, True]
    if all((not ordered[index]) or ordered[index + 1] for index in range(len(ordered) - 1)):
        return "SINGLE_TRANSITION_FAILURE_TO_SUCCESS"
    return "NONMONOTONE_OR_INTERLEAVED_LOCAL_BASIN"


def panel_classification(classes: list[str]) -> str:
    if len(classes) != 4:
        raise ValueError("panel classification requires exactly four pairs")
    if "PAIR_NUMERICAL_INVALIDITY_BLOCKER" in classes:
        return "LOCAL_BASIN_EVIDENCE_NUMERICALLY_BLOCKED"
    if "NONMONOTONE_OR_INTERLEAVED_LOCAL_BASIN" in classes:
        return "LOCAL_BASIN_TOPOLOGY_HETEROGENEOUS_OR_INTERLEAVED"
    return "LOCAL_BASIN_BOUNDARIES_SIMPLE_AND_PAIR_SPECIFIC"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("preflight", "run"))
    parser.add_argument("output_root", type=Path)
    args = parser.parse_args()
    return preflight(args.output_root) if args.command == "preflight" else execute(args.output_root)


if __name__ == "__main__":
    raise SystemExit(main())
