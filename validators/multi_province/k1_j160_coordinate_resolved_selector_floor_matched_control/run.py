"""Exactly-seven observation-only HJB replays with coordinate-resolved traces."""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import gzip
from hashlib import sha256
import json
from pathlib import Path
import time
from typing import Any

import numpy as np
from scipy import sparse

from validators.multi_province.k1_j160_provincial_first_turn_hjb_viability import run as viability
from validators.multi_province.k1_j640_hjb_nonconvergence_mechanism_diagnostic import run as accepted_observer
from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import run as accepted_hjb


REPO = Path(__file__).resolve().parents[3]
TASK_ID = "CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC"
ACTUAL_BASELINE = "543e7fc434ea75d1e18453922809bba05a0cec18"
BRANCH = "codex/ch5-mp4c-k1-j160-coordinate-resolved-selector-floor-matched-control-20260915"
WORKTREE = r"D:\ProjectTemp\ch5-mp4c-k1-j160-coordinate-resolved-selector-floor-matched-control-20260915-001"

PANEL = (
    (1, "天津", "failure", "POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION"),
    (13, "江西", "failure", "DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING"),
    (23, "贵州", "failure", "REPEATING_OR_LOW_PERIOD_CYCLE"),
    (27, "甘肃", "failure", "POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION"),
    (17, "湖南", "control", "HJB_CONVERGED"),
    (8, "上海", "control", "HJB_CONVERGED"),
    (12, "福建", "control", "HJB_CONVERGED"),
)
MATCHES = (("天津", "湖南"), ("江西", "上海"), ("贵州", "福建"), ("甘肃", "福建"))

VIABILITY_ROOT = REPO / "docs/evidence/ch5_mp4c_k1_j160_provincial_first_turn_hjb_viability"
VIABILITY_MANIFEST = VIABILITY_ROOT / "sealed_manifest_sha256.json"
VIABILITY_MANIFEST_CANONICAL_SHA256 = "78E39ACA7E051980D842BA861367E3424EE95578AD806802E8216E6AA14D3DFE"
SIX_ROOT = REPO / "docs/evidence/ch5_mp4c_k1_j160_first_turn_six_failure_hjb_mechanism_panel"
SIX_MANIFEST = SIX_ROOT / "sealed_manifest_sha256.json"
SIX_MANIFEST_CANONICAL_SHA256 = "B51E63EF493E31E979165052C5C98EA5AC32D945F9479DB5AB9D4A3F1EFF8855"
SPATIAL_ROOT = REPO / "docs/evidence/ch5_mp4c_k1_j160_six_failure_trace_spatial_localization_audit"
SPATIAL_MANIFEST = SPATIAL_ROOT / "sealed_manifest_sha256.json"
SPATIAL_MANIFEST_CANONICAL_SHA256 = "C61C6D06BF7773BB12C7BAD6F2D74EAD606D7BB294685FFF226ABFF0227AB535"

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
    "spatial_audit_acceptance": (REPO / "docs/CH5_MP4C_K1_J160_SIX_FAILURE_TRACE_SPATIAL_LOCALIZATION_AUDIT_ACCEPTANCE.md", "F43C906736F703A597653894528D5E3186E614DD34CE3DFEF9A8CE7BB8EC10AF"),
    "current_freeze": (REPO / "docs/CH5_MP4C_K1_J160_COORDINATE_RESOLVED_SELECTOR_FLOOR_MATCHED_CONTROL_DIAGNOSTIC_FREEZE_CURRENT.md", "1623450BD3B35D9C9B6681EDC27A06CD865BC4D2729585E1F1819596663993D7"),
}

oracle = accepted_observer.oracle


@dataclass(frozen=True)
class SimpleGrid:
    b: np.ndarray
    a: np.ndarray
    z: np.ndarray


def file_sha256(path: Path) -> str:
    return sha256(Path(path).read_bytes()).hexdigest().upper()


def canonical_text_sha256(path: Path) -> str:
    return sha256(Path(path).read_text(encoding="utf-8").encode("utf-8")).hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    Path(path).write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def write_gzip_json(path: Path, value: Any) -> None:
    payload = (json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")
    with Path(path).open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as compressed:
            compressed.write(payload)


def _coordinate(index: tuple[int, int, int], grid: Any) -> dict[str, Any]:
    i, j, k = (int(value) for value in index)
    return {
        "index_zero_based": {"b": i, "a": j, "z": k},
        "state": {"b": float(grid.b[i]), "a": float(grid.a[j]), "z": float(grid.z[k])},
    }


def changed_cell_records(current: np.ndarray, previous: np.ndarray | None, grid: Any) -> list[dict[str, Any]]:
    current_array = np.asarray(current)
    if previous is None:
        return []
    previous_array = np.asarray(previous)
    if current_array.shape != previous_array.shape:
        raise ValueError("selector arrays must have identical shapes")
    records = []
    for raw_index in np.argwhere(current_array != previous_array):
        index = tuple(int(value) for value in raw_index)
        records.append({
            **_coordinate(index, grid),
            "old_label": str(previous_array[index]), "new_label": str(current_array[index]),
        })
    return records


def floor_hit_records(values: np.ndarray, grid: Any, *, floor_type: str, floor: float) -> list[dict[str, Any]]:
    array = np.asarray(values, dtype=float)
    records = []
    for raw_index in np.argwhere(array < floor):
        index = tuple(int(value) for value in raw_index)
        records.append({
            **_coordinate(index, grid), "floor_type": floor_type,
            "raw_derivative": float(array[index]),
        })
    return records


def _manifest_receipt(root: Path, manifest_path: Path, expected_canonical_hash: str) -> dict[str, Any]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = []
    for expected in manifest["entries"]:
        target = root / expected["path"]
        exists = target.is_file()
        byte_hash = file_sha256(target) if exists else None
        canonical_hash = canonical_text_sha256(target) if exists and target.suffix.lower() in {".json", ".md", ".csv", ".py", ".txt"} else None
        entries.append({
            "path": expected["path"], "exists": exists,
            "expected_sha256": expected["sha256"], "actual_byte_sha256": byte_hash,
            "actual_canonical_lf_sha256": canonical_hash,
            "expected_bytes": expected["bytes"], "actual_bytes": target.stat().st_size if exists else None,
            "pass": exists and expected["sha256"] in {byte_hash, canonical_hash},
        })
    receipt = {
        "path": str(manifest_path.resolve()), "entry_count": len(entries), "entries": entries,
        "expected_canonical_sha256": expected_canonical_hash,
        "actual_canonical_sha256": canonical_text_sha256(manifest_path),
        "declared_entry_count": manifest["entry_count"],
        "declared_bytes_excluding_manifest": manifest["bytes_excluding_manifest"],
    }
    receipt["pass"] = bool(
        receipt["actual_canonical_sha256"] == expected_canonical_hash
        and receipt["declared_entry_count"] == len(entries)
        and receipt["declared_bytes_excluding_manifest"] == sum(item["expected_bytes"] for item in entries)
        and all(item["pass"] for item in entries)
    )
    return receipt


def source_identity_receipt() -> dict[str, Any]:
    manifests = {
        "accepted_first_turn": _manifest_receipt(VIABILITY_ROOT, VIABILITY_MANIFEST, VIABILITY_MANIFEST_CANONICAL_SHA256),
        "accepted_six_failure": _manifest_receipt(SIX_ROOT, SIX_MANIFEST, SIX_MANIFEST_CANONICAL_SHA256),
        "accepted_spatial_audit": _manifest_receipt(SPATIAL_ROOT, SPATIAL_MANIFEST, SPATIAL_MANIFEST_CANONICAL_SHA256),
    }
    files = {}
    for name, (path, expected) in SOURCE_IDENTITIES.items():
        exists = path.is_file()
        actual = file_sha256(path) if exists else None
        files[name] = {
            "path": str(path.resolve()), "exists": exists,
            "expected_sha256": expected, "actual_sha256": actual,
            "pass": exists and actual == expected,
        }
    receipt = {
        "schema": "CH5_MP4C_K1_J160_COORDINATE_RESOLVED_MATCHED_PANEL_SOURCE_IDENTITY_V1",
        "task_id": TASK_ID, "actual_baseline": ACTUAL_BASELINE,
        "manifests": manifests, "files": files,
        "frozen_science": {
            "I": 20, "J": 160, "Nz": 2, "a_bounds": [0.0, 100.0], "b_bounds": [-2.0, 20.0],
            "diagnostic_bridge_h": 1.0, "Delta": 1000.0, "tolerance": 1e-7,
            "maxit": 100, "A2max_gate": 0.01, "derivative_floor": float(oracle.MATLAB_DERIVATIVE_FLOOR),
            "sparse_direct_solve": True,
        },
        "science_calls_before_clean_preflight": 0,
    }
    receipt["pass"] = bool(all(item["pass"] for item in manifests.values()) and all(item["pass"] for item in files.values()))
    return receipt


def load_panel_authority() -> dict[str, Any]:
    input_authority = viability.load_first_turn_authority()
    inputs_by_key = {(row["province_index"], row["province"]): row for row in input_authority["provinces"]}
    accepted_outcomes = json.loads((VIABILITY_ROOT / "province_receipts.json").read_text(encoding="utf-8"))
    outcomes_by_key = {(row["province_index"], row["province"]): row for row in accepted_outcomes}
    rows = []
    for index, province, role, accepted_mechanism in PANEL:
        key = (index, province)
        if key not in inputs_by_key or key not in outcomes_by_key:
            raise ValueError(f"COORDINATE_RESOLVED_MATCHED_PANEL_AUTHORITY_BLOCKER: missing {key}")
        input_row = inputs_by_key[key]
        accepted = outcomes_by_key[key]
        expected_class = "HJB_NOT_CONVERGED" if role == "failure" else "HJB_CONVERGED"
        if accepted["hjb"]["classification"] != expected_class:
            raise ValueError(f"COORDINATE_RESOLVED_MATCHED_PANEL_AUTHORITY_BLOCKER: accepted class mismatch {key}")
        rows.append({
            **input_row, "panel_role": role, "accepted_mechanism": accepted_mechanism,
            "accepted_hjb": accepted["hjb"], "accepted_fresh_initialization": accepted["fresh_initialization"],
        })
    return {
        "schema": "CH5_MP4C_K1_J160_COORDINATE_RESOLVED_MATCHED_PANEL_INPUT_AUTHORITY_V1",
        "accepted_first_turn_candidate": input_authority["accepted_candidate"],
        "province_count": len(rows), "panel_order": [row["province"] for row in rows],
        "provinces": rows, "pass": len(rows) == 7,
    }


def build_fixture(row: dict[str, Any]) -> Any:
    return viability.build_fixture(row)


def input_authority_receipt(authority: dict[str, Any]) -> dict[str, Any]:
    entries = []
    fixtures = [build_fixture(row) for row in authority["provinces"]]
    initial_ids = {id(fixture.initial_value) for fixture in fixtures}
    labor_ids = {id(fixture.baseline_labor) for fixture in fixtures}
    for row, fixture in zip(authority["provinces"], fixtures):
        initial_ids.add(id(fixture.initial_value)); labor_ids.add(id(fixture.baseline_labor))
        checks = {
            "I": fixture.grid.b.size == 20, "J": fixture.grid.a.size == 160, "Nz": fixture.grid.z.size == 2,
            "a_bounds": fixture.grid.a[[0, -1]].tolist() == [0.0, 100.0],
            "b_bounds": fixture.grid.b[[0, -1]].tolist() == [-2.0, 20.0],
            "r_a": fixture.inputs.r_a == row["consumed_r_a"], "r_b": fixture.inputs.r_b == row["r_b"],
            "wage": fixture.inputs.wages.tolist() == [row["household_composite_wage"]],
            "tau": fixture.inputs.tau == row["tau"], "transfer": fixture.transfer_income == row["transfer_income"],
            "borrowing_gap": fixture.borrowing_rate_gap == row["borrowing_rate_gap"],
            "Delta": fixture.numerics.delta == 1000.0, "tolerance": fixture.numerics.convergence_tolerance == 1e-7,
            "maxit": fixture.numerics.max_iterations == 100, "drift_tolerance": fixture.numerics.drift_tolerance == 1e-12,
            "initial_value": accepted_hjb.array_sha256(fixture.initial_value) == row["accepted_fresh_initialization"]["initial_value_sha256"],
            "baseline_labor": accepted_hjb.array_sha256(fixture.baseline_labor) == row["accepted_fresh_initialization"]["baseline_labor_sha256"],
        }
        entries.append({
            "province_index": row["province_index"], "province": row["province"], "panel_role": row["panel_role"],
            "exact_household_inputs": {
                "r_b": row["r_b"], "consumed_r_a": row["consumed_r_a"],
                "household_composite_wage": row["household_composite_wage"], "tau": row["tau"],
                "transfer_income": row["transfer_income"], "borrowing_rate_gap": row["borrowing_rate_gap"],
                "return_guard_state": row["return_guard_state"], "wage_guard_state": row["wage_guard_state"],
            },
            "checks": checks, "fresh_initialization": True, "warm_start": False,
        })
    receipt = {
        "schema": "CH5_MP4C_K1_J160_COORDINATE_RESOLVED_MATCHED_PANEL_INPUT_RECEIPT_V1",
        "province_count": len(entries), "panel_order": [item["province"] for item in entries],
        "fresh_initial_value_object_count": len(initial_ids), "fresh_baseline_labor_object_count": len(labor_ids),
        "entries": entries,
    }
    receipt["pass"] = bool(
        len(entries) == 7 and len(initial_ids) == 7 and len(labor_ids) == 7
        and all(all(item["checks"].values()) for item in entries)
    )
    return receipt


def instrumentation_invariance_receipt() -> dict[str, Any]:
    accepted_j640 = json.loads((REPO / "docs/evidence/ch5_mp4c_k1_j640_hjb_nonconvergence_mechanism_diagnostic/instrumentation_invariance_receipt.json").read_text(encoding="utf-8"))
    accepted_six = json.loads((SIX_ROOT / "instrumentation_invariance_receipt.json").read_text(encoding="utf-8"))
    grid = SimpleGrid(np.array([-2.0, 0.0, 20.0]), np.array([0.0, 50.0, 100.0]), np.array([0.8, 1.3]))
    labels = np.full((3, 3, 2), "0"); prior = labels.copy(); labels[2, 1, 0] = "B"
    derivatives = np.full((3, 3, 2), 2.0e-6); derivatives[0, 2, 1] = 0.5e-6
    before = {"labels": accepted_hjb.array_sha256(labels), "prior": accepted_hjb.array_sha256(prior), "derivatives": accepted_hjb.array_sha256(derivatives)}
    changed = changed_cell_records(labels, prior, grid)
    floors = floor_hit_records(derivatives, grid, floor_type="vb_forward", floor=1.0e-6)
    after = {"labels": accepted_hjb.array_sha256(labels), "prior": accepted_hjb.array_sha256(prior), "derivatives": accepted_hjb.array_sha256(derivatives)}
    receipt = {
        "schema": "CH5_MP4C_K1_J160_COORDINATE_RESOLVED_INSTRUMENTATION_INVARIANCE_V1",
        "accepted_j640_parity_pass": accepted_j640.get("pass") is True,
        "accepted_j640_off_on_exact": accepted_j640.get("accepted_off_on_exact") is True,
        "accepted_six_failure_invariance_pass": accepted_six.get("pass") is True,
        "coordinate_extraction_input_hashes_unchanged": before == after,
        "synthetic_changed_cell_count": len(changed), "synthetic_floor_hit_count": len(floors),
        "wrapped_primitives_return_original_objects_or_values": True,
        "scientific_control_flow_reads_observations": False,
        "retains_state_between_provinces": False,
        "new_hjb_calls_for_parity": 0,
        "methodology": "accepted J640 primitive wrappers extended only by copies of coordinates and old/new labels",
    }
    receipt["pass"] = bool(
        receipt["accepted_j640_parity_pass"] and receipt["accepted_j640_off_on_exact"]
        and receipt["accepted_six_failure_invariance_pass"]
        and receipt["coordinate_extraction_input_hashes_unchanged"]
        and len(changed) == 1 and len(floors) == 1
    )
    return receipt


def observe_coordinate_hjb(
    grid: Any, params: Any, inputs: Any, initial_value: Any, baseline_labor: Any,
    transfer_income: Any, borrowing_rate_gap: Any, numerics: Any,
) -> tuple[Any, dict[str, Any]]:
    """Call the accepted solver once; every observation is a copy outside control flow."""
    original_policy = oracle.select_matlab_faithful_local_policy
    original_assembler = oracle.assemble_source_operator
    original_spsolve = oracle.linalg.spsolve
    if grid is None:
        result = oracle.solve_matlab_faithful_hjb(
            grid, params, inputs, initial_value, baseline_labor,
            transfer_income, borrowing_rate_gap, numerics,
        )
        return result, {"schema": "CH5_MP4C_K1_J160_COORDINATE_RESOLVED_TRACE_V1", "iterations": []}

    shape = (grid.b.size, grid.a.size, grid.z.size)
    state_count = int(np.prod(shape))
    current_old = np.asarray(initial_value, dtype=float).copy()
    policy_rows: list[dict[str, Any]] = []
    pending: dict[str, Any] | None = None
    iterations: list[dict[str, Any]] = []
    value_history: list[np.ndarray] = []
    prior_liquid = None; prior_transfer = None
    prior_consumption = None; prior_labor = None; prior_transfer_policy = None
    post_operator = None

    def observed_policy(*args: Any, **kwargs: Any) -> Any:
        result = original_policy(*args, **kwargs)
        policy_rows.append({
            "v_b_forward": float(kwargs["v_b_forward"]), "v_b_backward": float(kwargs["v_b_backward"]),
            "v_a_forward": float(kwargs["v_a_forward"]), "v_a_backward": float(kwargs["v_a_backward"]),
            "liquid_label": result.liquid_label, "transfer_label": result.transfer_label,
            "consumption": float(result.consumption), "labor": float(result.labor), "transfer": float(result.transfer),
        })
        return result

    def observed_assembler(*args: Any, **kwargs: Any) -> Any:
        nonlocal pending, post_operator, policy_rows
        result = original_assembler(*args, **kwargs)
        if len(policy_rows) == state_count:
            iteration = len(iterations) + 1
            fields = {}
            for name in policy_rows[0]:
                dtype = "U1" if name.endswith("label") else float
                fields[name] = np.asarray([row[name] for row in policy_rows], dtype=dtype).reshape(shape, order="F")
            pending = {
                "iteration": iteration, "fields": fields,
                "operator": accepted_observer._operator_receipt(result.full, iteration),
                "drifts_finite": bool(all(np.isfinite(np.asarray(arg)).all() for arg in args[:4])),
            }
            policy_rows = []
        else:
            post_operator = accepted_observer._operator_receipt(result.full, len(iterations) + 1)
        return result

    def observed_spsolve(matrix: Any, rhs: Any, *args: Any, **kwargs: Any) -> Any:
        nonlocal current_old, pending, prior_liquid, prior_transfer
        nonlocal prior_consumption, prior_labor, prior_transfer_policy
        solved = original_spsolve(matrix, rhs, *args, **kwargs)
        if pending is None:
            return solved
        value = np.asarray(solved, dtype=float).reshape(shape, order="F")
        update = value - current_old
        flat_index = int(np.argmax(np.abs(update)))
        coordinate = tuple(int(item) for item in np.unravel_index(flat_index, shape))
        fields = pending.pop("fields")
        liquid = fields["liquid_label"]; transfer_labels = fields["transfer_label"]
        floor = float(oracle.MATLAB_DERIVATIVE_FLOOR)
        liquid_changes = changed_cell_records(liquid, prior_liquid, grid)
        transfer_changes = changed_cell_records(transfer_labels, prior_transfer, grid)
        forward_hits = floor_hit_records(fields["v_b_forward"], grid, floor_type="vb_forward", floor=floor)
        backward_hits = floor_hit_records(fields["v_b_backward"], grid, floor_type="vb_backward", floor=floor)
        row = {
            "iteration": pending["iteration"], "convergence_statistic": float(np.max(np.abs(update))),
            "signed_dV_at_argmax": float(update[coordinate]), "argmax": _coordinate(coordinate, grid),
            "operator": pending["operator"],
            "finite_checks": {
                "old_value": bool(np.isfinite(current_old).all()), "new_value": bool(np.isfinite(value).all()),
                "rhs": bool(np.isfinite(np.asarray(rhs)).all()),
                "matrix_data": bool(np.isfinite(sparse.csr_matrix(matrix).data).all()),
                "policies": bool(all(np.isfinite(fields[name]).all() for name in ("consumption", "labor", "transfer"))),
                "drifts": pending["drifts_finite"],
            },
            "shape_checks": {
                "value": list(value.shape) == list(shape), "liquid_labels": list(liquid.shape) == list(shape),
                "transfer_labels": list(transfer_labels.shape) == list(shape),
            },
            "selector_changes": {"liquid": None if prior_liquid is None else len(liquid_changes), "transfer": None if prior_transfer is None else len(transfer_changes)},
            "selector_changed_cells": {"liquid": liquid_changes, "transfer": transfer_changes},
            "policy_changes": {
                "consumption": accepted_observer._change_receipt(fields["consumption"], prior_consumption),
                "labor": accepted_observer._change_receipt(fields["labor"], prior_labor),
                "transfer": accepted_observer._change_receipt(fields["transfer"], prior_transfer_policy),
            },
            "selector_counts": {"liquid": dict(Counter(map(str, liquid.ravel()))), "transfer": dict(Counter(map(str, transfer_labels.ravel())))},
            "derivative_floor_hits": {"vb_forward": len(forward_hits), "vb_backward": len(backward_hits)},
            "derivative_floor_hit_cells": {"vb_forward": forward_hits, "vb_backward": backward_hits},
            "hashes": {
                "value": accepted_observer.array_sha256(value), "liquid_labels": accepted_observer.array_sha256(liquid),
                "transfer_labels": accepted_observer.array_sha256(transfer_labels),
                "consumption": accepted_observer.array_sha256(fields["consumption"]),
                "labor": accepted_observer.array_sha256(fields["labor"]),
                "transfer": accepted_observer.array_sha256(fields["transfer"]),
            },
            "value_period_2_inf": float(np.max(np.abs(value - value_history[-2]))) if len(value_history) >= 2 else None,
            "value_period_3_inf": float(np.max(np.abs(value - value_history[-3]))) if len(value_history) >= 3 else None,
            "linear_solve_residual_inf": float(np.linalg.norm(sparse.csr_matrix(matrix) @ np.asarray(solved) - np.asarray(rhs), ord=np.inf)),
        }
        iterations.append(row); value_history.append(value.copy())
        if len(value_history) > 3:
            value_history.pop(0)
        current_old = value.copy(); prior_liquid = liquid.copy(); prior_transfer = transfer_labels.copy()
        prior_consumption = fields["consumption"].copy(); prior_labor = fields["labor"].copy(); prior_transfer_policy = fields["transfer"].copy()
        pending = None
        return solved

    oracle.select_matlab_faithful_local_policy = observed_policy
    oracle.assemble_source_operator = observed_assembler
    oracle.linalg.spsolve = observed_spsolve
    try:
        result = oracle.solve_matlab_faithful_hjb(
            grid, params, inputs, initial_value, baseline_labor,
            transfer_income, borrowing_rate_gap, numerics,
        )
    finally:
        oracle.select_matlab_faithful_local_policy = original_policy
        oracle.assemble_source_operator = original_assembler
        oracle.linalg.spsolve = original_spsolve
    cycle = accepted_observer.exact_cycle_evidence(iterations)
    return result, {
        "schema": "CH5_MP4C_K1_J160_COORDINATE_RESOLVED_TRACE_V1",
        "iterations": iterations, "cycle_evidence": cycle, "post_convergence_operator": post_operator,
        "first_derivative_floor_hit_iteration": next((row["iteration"] for row in iterations if sum(row["derivative_floor_hits"].values()) > 0), None),
        "instrumentation_design": "accepted solver called directly; coordinate copies never feed scientific control flow",
    }


FORBIDDEN_LEDGER_KEYS = (
    "kfe_calls", "outer_calls", "firm_calls", "wage_recalculation_calls", "return_recalculation_calls",
    "matlab_calls", "k1b_calls", "k2_calls", "ge_calls", "downstream_calls", "shock_calls",
    "irf_calls", "results_writes",
)


def empty_call_ledger() -> dict[str, Any]:
    ledger = {
        "schema": "CH5_MP4C_K1_J160_COORDINATE_RESOLVED_MATCHED_PANEL_CALL_LEDGER_V1",
        "hjb_budget": 7, "hjb_calls_started": 0, "hjb_calls_completed": 0,
        "failed_province_hjb_budget": 4, "failed_province_hjb_calls": 0,
        "successful_control_hjb_budget": 3, "successful_control_hjb_calls": 0,
        "scientific_retries": 0, "engineering_retry_budget": 1, "engineering_retries_used": 0,
        "province_calls": [],
    }
    ledger.update({key: 0 for key in FORBIDDEN_LEDGER_KEYS})
    return ledger


def _result_array_hashes(result: Any) -> dict[str, str]:
    return {
        name: accepted_hjb.array_sha256(getattr(result, name))
        for name in result.__dataclass_fields__ if isinstance(getattr(result, name), np.ndarray)
    }


def engineering_retry_eligible(prior: dict[str, Any]) -> bool:
    return bool(
        prior.get("status") == {"science_calls": 0, "status": "FAIL"}
        and prior.get("source_pass") is True
        and prior.get("instrumentation_pass") is True
        and prior.get("hjb_calls_started") == 0
        and prior.get("engineering_retries_used") == 0
        and prior.get("failed_check_names") == {"initial_value", "baseline_labor"}
    )


def _archive_failed_preflight(root: Path) -> int:
    status = json.loads((root / "preflight_complete.json").read_text(encoding="utf-8"))
    source = json.loads((root / "source_identity.json").read_text(encoding="utf-8"))
    inputs = json.loads((root / "input_authority_receipt.json").read_text(encoding="utf-8"))
    instrumentation = json.loads((root / "instrumentation_invariance_receipt.json").read_text(encoding="utf-8"))
    ledger = json.loads((root / "call_ledger.json").read_text(encoding="utf-8"))
    failed = {
        key for item in inputs["entries"] for key, value in item["checks"].items() if not value
    }
    prior = {
        "status": status, "source_pass": source.get("pass"),
        "instrumentation_pass": instrumentation.get("pass"),
        "hjb_calls_started": ledger.get("hjb_calls_started"),
        "engineering_retries_used": ledger.get("engineering_retries_used"),
        "failed_check_names": failed,
    }
    if not engineering_retry_eligible(prior) or (root / "science_started.json").exists():
        raise RuntimeError("engineering retry is not authorized for this preflight state")
    archive = root / "engineering_retry_01_failed_preflight"
    archive.mkdir(exist_ok=False)
    for name in (
        "source_identity.json", "input_authority_receipt.json",
        "instrumentation_invariance_receipt.json", "call_ledger.json", "preflight_complete.json",
    ):
        (root / name).replace(archive / name)
    return 1


def preflight(output_root: Path) -> int:
    root = Path(output_root)
    if root.exists():
        retry_count = _archive_failed_preflight(root)
    else:
        root.mkdir(parents=True, exist_ok=False)
        retry_count = 0
    source = source_identity_receipt()
    authority = load_panel_authority()
    inputs = input_authority_receipt(authority)
    instrumentation = instrumentation_invariance_receipt()
    ledger = empty_call_ledger()
    ledger["engineering_retries_used"] = retry_count
    write_json(root / "source_identity.json", source)
    write_json(root / "input_authority_receipt.json", inputs)
    write_json(root / "instrumentation_invariance_receipt.json", instrumentation)
    write_json(root / "call_ledger.json", ledger)
    if retry_count:
        write_json(root / "engineering_retry_receipt.json", {
            "schema": "CH5_MP4C_K1_J160_COORDINATE_RESOLVED_ENGINEERING_RETRY_V1",
            "retry": 1, "before_first_hjb": True, "science_calls_before_retry": 0,
            "failure": "input receipt compared against an earlier authority-layer initialization hash and did not retain fixtures while counting object identities",
            "repair": "compare against sealed province replay fresh_initialization hashes and retain all seven fixtures during the identity check",
            "scientific_source_changed": False, "scientific_inputs_changed": False,
        })
    passed = source["pass"] and authority["pass"] and inputs["pass"] and instrumentation["pass"]
    write_json(root / "preflight_complete.json", {"status": "PASS" if passed else "FAIL", "science_calls": 0})
    return 0 if passed else 1


def execute(output_root: Path) -> int:
    root = Path(output_root)
    preflight_status = json.loads((root / "preflight_complete.json").read_text(encoding="utf-8"))
    if preflight_status != {"science_calls": 0, "status": "PASS"}:
        raise RuntimeError("COORDINATE_RESOLVED_MATCHED_PANEL_AUTHORITY_BLOCKER")
    if (root / "science_started.json").exists():
        raise FileExistsError("exactly-once seven-province science has already started")
    authority = load_panel_authority()
    ledger = json.loads((root / "call_ledger.json").read_text(encoding="utf-8"))
    write_json(root / "science_started.json", {
        "task_id": TASK_ID, "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "panel_order": [row["province"] for row in authority["provinces"]],
        "fresh_initialization": True, "warm_start": False,
    })
    traces_root = root / "coordinate_traces"; traces_root.mkdir()
    outcomes = []
    for call, row in enumerate(authority["provinces"], start=1):
        fixture = build_fixture(row)
        point_id = f"p{row['province_index']:02d}_{row['province']}"
        write_json(root / f"{point_id}_started.json", {
            "call": call, "province_index": row["province_index"], "province": row["province"],
            "panel_role": row["panel_role"], "fresh_initialization": True, "warm_start": False,
            "initial_value_sha256": accepted_hjb.array_sha256(fixture.initial_value),
            "baseline_labor_sha256": accepted_hjb.array_sha256(fixture.baseline_labor),
        })
        ledger["hjb_calls_started"] += 1
        ledger[f"{'failed_province' if row['panel_role'] == 'failure' else 'successful_control'}_hjb_calls"] += 1
        write_json(root / f"ledger_before_{point_id}.json", ledger)
        try:
            result, trace = observe_coordinate_hjb(*fixture.arguments())
        except Exception as exc:
            ledger["province_calls"].append({
                "call": call, "province": row["province"], "province_index": row["province_index"],
                "panel_role": row["panel_role"], "completed": False, "retried": False,
                "error_type": type(exc).__name__, "error": str(exc),
            })
            write_json(root / "call_ledger.json", ledger)
            write_json(root / f"{point_id}_failure.json", ledger["province_calls"][-1])
            raise
        ledger["hjb_calls_completed"] += 1
        replay_hashes = _result_array_hashes(result)
        accepted_arrays = row["accepted_hjb"]["scientific_arrays"]["arrays"]
        comparable = {name: value for name, value in replay_hashes.items() if name in accepted_arrays}
        hashes_exact = bool(comparable) and all(value == accepted_arrays[name]["sha256"] for name, value in comparable.items())
        expected_converged = row["panel_role"] == "control"
        legal = all(item["operator"]["legal"] for item in trace["iterations"])
        reproducibility = bool(
            result.converged == expected_converged
            and result.iterations == row["accepted_hjb"]["iterations_used"]
            and result.convergence_statistic == row["accepted_hjb"]["final_convergence_statistic"]
            and hashes_exact and legal
        )
        trace.update({"province_index": row["province_index"], "province": row["province"], "panel_role": row["panel_role"]})
        trace_path = traces_root / f"{point_id}.json.gz"
        write_gzip_json(trace_path, trace)
        outcome = {
            "call": call, "point_id": point_id, "province_index": row["province_index"], "province": row["province"],
            "panel_role": row["panel_role"], "accepted_mechanism": row["accepted_mechanism"],
            "accepted_classification": row["accepted_hjb"]["classification"],
            "replay_classification": "HJB_CONVERGED" if result.converged else "HJB_NOT_CONVERGED",
            "accepted_iterations": row["accepted_hjb"]["iterations_used"], "replay_iterations": int(result.iterations),
            "accepted_final_convergence_statistic": row["accepted_hjb"]["final_convergence_statistic"],
            "replay_final_convergence_statistic": float(result.convergence_statistic),
            "accepted_result_array_hashes_exact": hashes_exact,
            "all_iteration_operators_legal": legal,
            "all_finite_shape_checks_pass": all(all(item["finite_checks"].values()) and all(item["shape_checks"].values()) for item in trace["iterations"]),
            "reproducibility_pass": reproducibility, "trace_path": str(trace_path.relative_to(root).as_posix()),
            "trace_sha256": file_sha256(trace_path), "trace_bytes": trace_path.stat().st_size,
            "exact_joint_selector_recurrence": trace["cycle_evidence"]["first_exact_joint_label_recurrence"],
            "exact_value_recurrence": trace["cycle_evidence"]["first_exact_value_recurrence"],
        }
        outcomes.append(outcome)
        write_json(root / f"{point_id}_outcome.json", outcome)
        ledger["province_calls"].append({
            "call": call, "province": row["province"], "province_index": row["province_index"],
            "panel_role": row["panel_role"], "completed": True, "retried": False,
            "reproducibility_pass": reproducibility,
        })
        write_json(root / "call_ledger.json", ledger)
    write_json(root / "province_outcomes.json", {
        "schema": "CH5_MP4C_K1_J160_COORDINATE_RESOLVED_MATCHED_PANEL_OUTCOMES_V1",
        "province_count": len(outcomes), "all_reproducibility_pass": all(item["reproducibility_pass"] for item in outcomes),
        "provinces": outcomes,
    })
    write_json(root / "execution_complete.json", {
        "status": "EXACT_SEVEN_PROVINCE_COORDINATE_REPLAY_COMPLETE",
        "hjb_calls": ledger["hjb_calls_started"], "kfe_calls": 0, "scientific_retries": 0,
        "results_eligibility": False,
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
