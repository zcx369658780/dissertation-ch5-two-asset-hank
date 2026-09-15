"""Observation-only replay of the frozen accepted J640 HJB."""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict
from hashlib import sha256
import json
from pathlib import Path
import time
from typing import Any, Callable

import numpy as np
from scipy import sparse

from exports import matlab_faithful_two_asset_ha as oracle
from validators.multi_province.k1_household_illiquid_grid_finer_precision_escalation import (
    run as accepted_finer,
)
from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import run as coarse


REPO = Path(__file__).resolve().parents[3]
TASK_ID = "CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC"
ACTUAL_BASELINE = "11d3839f6bc500709fe4fbf65edfc346bb7748f1"
MATLAB_PATH = accepted_finer.accepted.MATLAB_PATH
MATLAB_SHA256 = accepted_finer.accepted.MATLAB_SHA256
ORACLE_PATH = REPO / "exports/matlab_faithful_two_asset_ha.py"
ORACLE_SHA256 = accepted_finer.accepted.ORACLE_SHA256
ACCEPTED_FINER_ROOT = REPO / "docs/evidence/ch5_mp4c_k1_household_illiquid_grid_finer_precision_escalation"
ACCEPTED_FINER_MANIFEST = ACCEPTED_FINER_ROOT / "sealed_manifest_sha256.json"
ACCEPTED_FINER_MANIFEST_CANONICAL_SHA256 = "4817728075A6E48C8B0A08766FF3FE540FFB7D94FAB9093FB49B72A295DF949B"
ACCEPTED_PARITY_ROOT = REPO / "docs/evidence/ch5_mp4c_k1_hjb_convergence_mechanism_turn1_turn2"
ACCEPTED_PARITY = ACCEPTED_PARITY_ROOT / "instrumentation_parity.json"
ACCEPTED_PARITY_MANIFEST = ACCEPTED_PARITY_ROOT / "sealed_manifest_sha256.json"
ACCEPTED_PARITY_MANIFEST_CANONICAL_SHA256 = "007E8051713C73CF860E6A7B4C98E1BE7A723549E5A0F9AC5C48513546A95D35"
HOMECRIT = coarse.HOMECRIT


def array_sha256(value: Any) -> str:
    array = np.asarray(value)
    header = f"{array.dtype.str}|{array.shape}|C|".encode("ascii")
    return sha256(header + np.ascontiguousarray(array).tobytes()).hexdigest().upper()


def file_sha256(path: Path) -> str:
    return sha256(Path(path).read_bytes()).hexdigest().upper()


def canonical_text_sha256(path: Path) -> str:
    return sha256(Path(path).read_text(encoding="utf-8").encode("utf-8")).hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    Path(path).write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def build_fixture() -> coarse.Fixture:
    return accepted_finer.build_fixture(accepted_finer.precision_spec(1))


def _sparse_sha256(value: Any) -> str:
    matrix = sparse.csr_matrix(value, dtype=float)
    payload = (
        f"{matrix.dtype.str}|{matrix.shape}|CSR|".encode("ascii")
        + np.ascontiguousarray(matrix.data).tobytes()
        + np.ascontiguousarray(matrix.indices).tobytes()
        + np.ascontiguousarray(matrix.indptr).tobytes()
    )
    return sha256(payload).hexdigest().upper()


def _operator_receipt(value: Any, iteration: int) -> dict[str, Any]:
    matrix = sparse.csr_matrix(value, dtype=float)
    row_sums = np.asarray(matrix.sum(axis=1)).ravel()
    coo = matrix.tocoo()
    off = coo.data[coo.row != coo.col]
    a2max = float(np.max(np.abs(row_sums)))
    return {
        "iteration": iteration,
        "a2max": a2max,
        "homecrit": HOMECRIT,
        "legal": bool(np.isfinite(a2max) and a2max <= HOMECRIT),
        "row_sum_nonfinite_count": int(np.count_nonzero(~np.isfinite(row_sums))),
        "minimum_stored_off_diagonal": float(np.min(off)) if off.size else 0.0,
        "matrix_shape": list(matrix.shape),
        "matrix_nnz": int(matrix.nnz),
        "operator_sha256": _sparse_sha256(matrix),
    }


def _change_receipt(current: np.ndarray, prior: np.ndarray | None) -> dict[str, Any]:
    if prior is None:
        return {"count": None, "max_abs": None}
    difference = np.asarray(current) - np.asarray(prior)
    return {
        "count": int(np.count_nonzero(difference != 0.0)),
        "max_abs": float(np.max(np.abs(difference))),
    }


def exact_cycle_evidence(rows: list[dict[str, Any]]) -> dict[str, Any]:
    value_seen: dict[str, int] = {}
    labels_seen: dict[tuple[str, str], int] = {}
    first_value = None
    first_labels = None
    for row in rows:
        iteration = int(row["iteration"])
        hashes = row["hashes"]
        value_hash = str(hashes["value"])
        labels_hash = (str(hashes["liquid_labels"]), str(hashes["transfer_labels"]))
        if first_value is None and value_hash in value_seen:
            prior = value_seen[value_hash]
            first_value = {"iteration": iteration, "prior_iteration": prior, "period": iteration - prior}
        if first_labels is None and labels_hash in labels_seen:
            prior = labels_seen[labels_hash]
            first_labels = {"iteration": iteration, "prior_iteration": prior, "period": iteration - prior}
        value_seen.setdefault(value_hash, iteration)
        labels_seen.setdefault(labels_hash, iteration)
    return {
        "first_exact_value_recurrence": first_value,
        "first_exact_joint_label_recurrence": first_labels,
        "exact_value_low_period_2_or_3": bool(first_value and first_value["period"] in {2, 3}),
        "exact_joint_label_low_period_2_or_3": bool(first_labels and first_labels["period"] in {2, 3}),
    }


def observe_accepted_hjb(
    grid: Any,
    params: Any,
    inputs: Any,
    initial_value: Any,
    baseline_labor: Any,
    transfer_income: Any,
    borrowing_rate_gap: Any,
    numerics: Any,
) -> tuple[Any, dict[str, Any]]:
    """Call the accepted solver once while transparently observing its primitives."""
    original_policy = oracle.select_matlab_faithful_local_policy
    original_assembler = oracle.assemble_source_operator
    original_spsolve = oracle.linalg.spsolve
    if grid is None:
        result = oracle.solve_matlab_faithful_hjb(
            grid, params, inputs, initial_value, baseline_labor,
            transfer_income, borrowing_rate_gap, numerics,
        )
        return result, {"schema": "CH5_MP4C_K1_J640_HJB_ITERATION_TRACE_V1", "iterations": []}

    shape = (grid.b.size, grid.a.size, grid.z.size)
    state_count = int(np.prod(shape))
    current_old = np.asarray(initial_value, dtype=float).copy()
    policy_rows: list[dict[str, Any]] = []
    pending: dict[str, Any] | None = None
    iterations: list[dict[str, Any]] = []
    value_history: list[np.ndarray] = []
    prior_liquid = None
    prior_transfer = None
    prior_consumption = None
    prior_labor = None
    prior_transfer_policy = None
    post_operator = None

    def observed_policy(*args: Any, **kwargs: Any) -> Any:
        result = original_policy(*args, **kwargs)
        policy_rows.append(
            {
                "v_b_forward": float(kwargs["v_b_forward"]),
                "v_b_backward": float(kwargs["v_b_backward"]),
                "v_a_forward": float(kwargs["v_a_forward"]),
                "v_a_backward": float(kwargs["v_a_backward"]),
                "liquid_label": result.liquid_label,
                "transfer_label": result.transfer_label,
                "consumption": float(result.consumption),
                "labor": float(result.labor),
                "transfer": float(result.transfer),
            }
        )
        return result

    def observed_assembler(*args: Any, **kwargs: Any) -> Any:
        nonlocal pending, post_operator, policy_rows
        result = original_assembler(*args, **kwargs)
        if len(policy_rows) == state_count:
            iteration = len(iterations) + 1
            fields: dict[str, np.ndarray] = {}
            for name in policy_rows[0]:
                dtype = "U1" if name.endswith("label") else float
                fields[name] = np.asarray([row[name] for row in policy_rows], dtype=dtype).reshape(shape, order="F")
            pending = {
                "iteration": iteration,
                "fields": fields,
                "operator": _operator_receipt(result.full, iteration),
                "drifts_finite": bool(all(np.isfinite(np.asarray(arg)).all() for arg in args[:4])),
            }
            policy_rows = []
        else:
            post_operator = _operator_receipt(result.full, len(iterations) + 1)
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
        coordinate = tuple(int(x) for x in np.unravel_index(flat_index, shape))
        fields = pending.pop("fields")
        liquid = fields["liquid_label"]
        transfer_labels = fields["transfer_label"]
        floor = oracle.MATLAB_DERIVATIVE_FLOOR
        floor_counts = {
            "vb_forward": int(np.count_nonzero(fields["v_b_forward"] < floor)),
            "vb_backward": int(np.count_nonzero(fields["v_b_backward"] < floor)),
        }
        row = {
            "iteration": pending["iteration"],
            "convergence_statistic": float(np.max(np.abs(update))),
            "signed_dV_at_argmax": float(update[coordinate]),
            "argmax": {
                "index_zero_based": {"b": coordinate[0], "a": coordinate[1], "z": coordinate[2]},
                "state": {
                    "b": float(grid.b[coordinate[0]]),
                    "a": float(grid.a[coordinate[1]]),
                    "z": float(grid.z[coordinate[2]]),
                },
            },
            "operator": pending["operator"],
            "finite_checks": {
                "old_value": bool(np.isfinite(current_old).all()),
                "new_value": bool(np.isfinite(value).all()),
                "rhs": bool(np.isfinite(np.asarray(rhs)).all()),
                "matrix_data": bool(np.isfinite(sparse.csr_matrix(matrix).data).all()),
                "policies": bool(all(np.isfinite(fields[name]).all() for name in ("consumption", "labor", "transfer"))),
                "drifts": pending["drifts_finite"],
            },
            "shape_checks": {
                "value": list(value.shape) == list(shape),
                "liquid_labels": list(liquid.shape) == list(shape),
                "transfer_labels": list(transfer_labels.shape) == list(shape),
            },
            "selector_changes": {
                "liquid": None if prior_liquid is None else int(np.count_nonzero(liquid != prior_liquid)),
                "transfer": None if prior_transfer is None else int(np.count_nonzero(transfer_labels != prior_transfer)),
            },
            "policy_changes": {
                "consumption": _change_receipt(fields["consumption"], prior_consumption),
                "labor": _change_receipt(fields["labor"], prior_labor),
                "transfer": _change_receipt(fields["transfer"], prior_transfer_policy),
            },
            "selector_counts": {
                "liquid": dict(Counter(map(str, liquid.ravel()))),
                "transfer": dict(Counter(map(str, transfer_labels.ravel()))),
            },
            "derivative_floor_hits": floor_counts,
            "hashes": {
                "value": array_sha256(value),
                "liquid_labels": array_sha256(liquid),
                "transfer_labels": array_sha256(transfer_labels),
                "consumption": array_sha256(fields["consumption"]),
                "labor": array_sha256(fields["labor"]),
                "transfer": array_sha256(fields["transfer"]),
            },
            "value_period_2_inf": (
                float(np.max(np.abs(value - value_history[-2]))) if len(value_history) >= 2 else None
            ),
            "value_period_3_inf": (
                float(np.max(np.abs(value - value_history[-3]))) if len(value_history) >= 3 else None
            ),
            "linear_solve_residual_inf": float(
                np.linalg.norm(sparse.csr_matrix(matrix) @ np.asarray(solved) - np.asarray(rhs), ord=np.inf)
            ),
        }
        iterations.append(row)
        value_history.append(value.copy())
        if len(value_history) > 3:
            value_history.pop(0)
        current_old = value.copy()
        prior_liquid = liquid.copy()
        prior_transfer = transfer_labels.copy()
        prior_consumption = fields["consumption"].copy()
        prior_labor = fields["labor"].copy()
        prior_transfer_policy = fields["transfer"].copy()
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

    cycle = exact_cycle_evidence(iterations)
    first_floor = next(
        (
            row["iteration"]
            for row in iterations
            if sum(row["derivative_floor_hits"].values()) > 0
        ),
        None,
    )
    return result, {
        "schema": "CH5_MP4C_K1_J640_HJB_ITERATION_TRACE_V1",
        "iterations": iterations,
        "first_derivative_floor_hit_iteration": first_floor,
        "cycle_evidence": cycle,
        "post_convergence_operator": post_operator,
        "instrumentation_design": "accepted solver called directly; wrapped primitives return original results unchanged",
    }


def _manifest_mapping(path: Path) -> dict[str, dict[str, Any]]:
    manifest = json.loads(Path(path).read_text(encoding="utf-8"))
    return {str(item["path"]): item for item in manifest["entries"]}


def _canonical_manifest_entry(root: Path, mapping: dict[str, dict[str, Any]], relative: str) -> dict[str, Any]:
    expected = mapping[relative]["sha256"]
    actual_bytes = file_sha256(root / relative)
    actual_canonical = canonical_text_sha256(root / relative)
    return {
        "path": str((root / relative).resolve()),
        "expected_sha256": expected,
        "actual_byte_sha256": actual_bytes,
        "actual_canonical_lf_sha256": actual_canonical,
        "matched_representation": (
            "BYTES" if actual_bytes == expected else "CANONICAL_LF" if actual_canonical == expected else None
        ),
        "pass": expected in {actual_bytes, actual_canonical},
    }


def _accepted_j640_point() -> dict[str, Any]:
    points = json.loads((ACCEPTED_FINER_ROOT / "point_receipts.json").read_text(encoding="utf-8"))
    selected = [point for point in points if point["specification"]["I"] == 20 and point["specification"]["J"] == 640]
    if len(selected) != 1:
        raise ValueError("accepted J640 point is not unique")
    return selected[0]


def preflight(output_root: Path) -> int:
    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=False)
    finer_manifest_hash = canonical_text_sha256(ACCEPTED_FINER_MANIFEST)
    parity_manifest_hash = canonical_text_sha256(ACCEPTED_PARITY_MANIFEST)
    finer_map = _manifest_mapping(ACCEPTED_FINER_MANIFEST)
    parity_map = _manifest_mapping(ACCEPTED_PARITY_MANIFEST)
    accepted_entries = [
        _canonical_manifest_entry(ACCEPTED_FINER_ROOT, finer_map, name)
        for name in ("point_receipts.json", "source_identity.json", "call_ledger.json")
    ]
    parity_entry = _canonical_manifest_entry(
        ACCEPTED_PARITY_ROOT, parity_map, "instrumentation_parity.json"
    )
    source = {
        "schema": "CH5_MP4C_K1_J640_HJB_MECHANISM_SOURCE_IDENTITY_V1",
        "actual_baseline": ACTUAL_BASELINE,
        "oracle_and_protected_hjb_kfe_source": {
            "path": str(ORACLE_PATH.resolve()),
            "expected_sha256": ORACLE_SHA256,
            "actual_sha256": file_sha256(ORACLE_PATH),
        },
        "matlab_source": {
            "path": str(MATLAB_PATH),
            "expected_sha256": MATLAB_SHA256,
            "actual_sha256": file_sha256(MATLAB_PATH),
        },
        "accepted_finer_manifest": {
            "path": str(ACCEPTED_FINER_MANIFEST.resolve()),
            "expected_canonical_sha256": ACCEPTED_FINER_MANIFEST_CANONICAL_SHA256,
            "actual_canonical_sha256": finer_manifest_hash,
        },
        "accepted_finer_entries": accepted_entries,
        "accepted_small_grid_instrumentation_parity_manifest": {
            "path": str(ACCEPTED_PARITY_MANIFEST.resolve()),
            "expected_canonical_sha256": ACCEPTED_PARITY_MANIFEST_CANONICAL_SHA256,
            "actual_canonical_sha256": parity_manifest_hash,
        },
        "accepted_small_grid_instrumentation_parity_entry": parity_entry,
        "matlab_runtime_calls": 0,
    }
    source["pass"] = bool(
        source["oracle_and_protected_hjb_kfe_source"]["actual_sha256"] == ORACLE_SHA256
        and source["matlab_source"]["actual_sha256"] == MATLAB_SHA256
        and finer_manifest_hash == ACCEPTED_FINER_MANIFEST_CANONICAL_SHA256
        and parity_manifest_hash == ACCEPTED_PARITY_MANIFEST_CANONICAL_SHA256
        and all(item["pass"] for item in [*accepted_entries, parity_entry])
    )
    write_json(root / "source_identity.json", source)

    fixture = build_fixture()
    accepted_point = _accepted_j640_point()
    accepted_spec = accepted_point["specification"]
    config = coarse.fixture_config(fixture)
    input_checks = {
        "I": fixture.grid.b.size == accepted_spec["I"] == 20,
        "J": fixture.grid.a.size == accepted_spec["J"] == 640,
        "Nz": fixture.grid.z.size == accepted_spec["Nz"] == 2,
        "a_bounds": [float(fixture.grid.a[0]), float(fixture.grid.a[-1])] == [0.0, 100.0],
        "b_bounds": [float(fixture.grid.b[0]), float(fixture.grid.b[-1])] == [-2.0, 20.0],
        "rb": fixture.inputs.r_b == accepted_spec["rb"] == 0.02,
        "ra": fixture.inputs.r_a == accepted_spec["ra"] == 0.0675,
        "wage": fixture.inputs.wages.tolist() == [accepted_spec["wage"]] == [15.5],
        "h": accepted_spec["h"] == 1.0,
        "delta": fixture.numerics.delta == 1000.0,
        "tolerance": fixture.numerics.convergence_tolerance == 1e-7,
        "maxit": fixture.numerics.max_iterations == 100,
        "drift_tolerance": fixture.numerics.drift_tolerance == 1e-12,
        "initial_value": array_sha256(fixture.initial_value) == accepted_point["fresh_initialization"]["initial_value_sha256"],
        "baseline_labor": array_sha256(fixture.baseline_labor) == accepted_point["fresh_initialization"]["baseline_labor_sha256"],
    }
    input_receipt = {
        "schema": "CH5_MP4C_K1_J640_HJB_MECHANISM_INPUT_INVARIANCE_V1",
        "configuration": config,
        "accepted_point_id": accepted_point["point_id"],
        "accepted_terminal": {
            "classification": accepted_point["hjb"]["classification"],
            "iterations": accepted_point["hjb"]["iterations_used"],
            "final_convergence_statistic": accepted_point["hjb"]["final_convergence_statistic"],
        },
        "checks": input_checks,
        "fresh_initialization": True,
        "no_warm_start": True,
        "pass": all(input_checks.values()),
    }
    write_json(root / "input_invariance_receipt.json", input_receipt)
    parity = json.loads(ACCEPTED_PARITY.read_text(encoding="utf-8"))
    instrumentation = {
        "schema": "CH5_MP4C_K1_J640_HJB_INSTRUMENTATION_INVARIANCE_V1",
        "new_hjb_calls": 0,
        "accepted_small_grid_reference_reused_without_runtime": True,
        "accepted_reference_path": str(ACCEPTED_PARITY.resolve()),
        "accepted_reference_status": parity["status"],
        "accepted_off_on_exact": parity["off_on_exact"],
        "accepted_off_accepted_exact": parity["off_accepted_exact"],
        "accepted_iterations_equal": parity["off_iterations"] == parity["on_iterations"],
        "current_design_calls_accepted_solver_directly": True,
        "wrapped_primitives_return_original_objects_or_values": True,
        "scientific_control_flow_reads_observations": False,
        "maxit_unchanged": fixture.numerics.max_iterations == 100,
        "tolerance_unchanged": fixture.numerics.convergence_tolerance == 1e-7,
        "initialization_unchanged": input_checks["initial_value"] and input_checks["baseline_labor"],
        "damping_clipping_renormalization_policy_freezing_added": False,
        "pass": bool(parity["status"] == "PASS" and parity["off_on_exact"] and parity["off_accepted_exact"]),
    }
    write_json(root / "instrumentation_invariance_receipt.json", instrumentation)
    ledger = {
        "schema": "CH5_MP4C_K1_J640_HJB_MECHANISM_CALL_LEDGER_V1",
        "hjb_budget": 1,
        "hjb_calls_started": 0,
        "hjb_calls_completed": 0,
        "kfe_calls": 0,
        "j1280_calls": 0,
        "scientific_retries": 0,
        "engineering_retries": 1,
        "global_outer_calls": 0,
        "firm_calls": 0,
        "matlab_calls": 0,
        "k1b_calls": 0,
        "k2_calls": 0,
        "ge_calls": 0,
        "downstream_calls": 0,
        "shock_calls": 0,
        "irf_calls": 0,
        "results_writes": 0,
    }
    write_json(root / "pre_science_call_ledger.json", ledger)
    status = source["pass"] and input_receipt["pass"] and instrumentation["pass"]
    write_json(root / "preflight_complete.json", {"status": "PASS" if status else "FAIL", "science_calls": 0})
    return 0 if status else 1


def classify_mechanism(trace: dict[str, Any], converged: bool) -> dict[str, Any]:
    rows = trace["iterations"]
    statistics = [float(row["convergence_statistic"]) for row in rows]
    first_switch = next(
        (
            row["iteration"]
            for row in rows
            if row["selector_changes"]["liquid"] is not None
            and row["selector_changes"]["liquid"] + row["selector_changes"]["transfer"] > 0
        ),
        None,
    )
    first_nondec = next(
        (index + 1 for index in range(1, len(statistics)) if statistics[index] >= statistics[index - 1]),
        None,
    )
    floor_first = trace["first_derivative_floor_hit_iteration"]
    cycle = trace["cycle_evidence"]
    nondecrease_count = sum(
        statistics[index] >= statistics[index - 1] for index in range(1, len(statistics))
    )
    if converged:
        classification = "J640_HJB_FAILURE_REPRODUCIBILITY_BLOCKER"
    elif cycle["exact_value_low_period_2_or_3"]:
        classification = "REPEATING_OR_LOW_PERIOD_CYCLE"
    elif (
        first_switch is not None
        and floor_first is not None
        and first_switch < floor_first
        and first_nondec is not None
        and floor_first <= first_nondec
    ):
        classification = "DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING"
    elif first_switch is not None and first_nondec is not None and first_switch <= first_nondec:
        classification = "POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION"
    elif nondecrease_count == 0:
        classification = "SLOW_MONOTONE_OR_NEAR_MONOTONE_VALUE_CONVERGENCE"
    else:
        classification = "MIXED_OR_UNRESOLVED_NUMERICAL_MECHANISM"
    return {
        "classification": classification,
        "first_policy_or_selector_switch_iteration": first_switch,
        "first_value_stat_non_decrease_iteration": first_nondec,
        "first_derivative_floor_hit_iteration": floor_first,
        "value_stat_non_decrease_count": nondecrease_count,
        "value_stat_decrease_count": max(len(statistics) - 1 - nondecrease_count, 0),
        "initial_convergence_statistic": statistics[0] if statistics else None,
        "final_convergence_statistic": statistics[-1] if statistics else None,
        "minimum_convergence_statistic": min(statistics) if statistics else None,
        "maximum_convergence_statistic": max(statistics) if statistics else None,
        "cycle_evidence": cycle,
        "classification_rule_preregistered_before_replay": True,
    }


def execute(output_root: Path) -> int:
    root = Path(output_root)
    preflight_receipt = json.loads((root / "preflight_complete.json").read_text(encoding="utf-8"))
    if preflight_receipt["status"] != "PASS":
        raise RuntimeError("preflight is not clean")
    if (root / "science_started.json").exists():
        raise FileExistsError("the exactly-once J640 HJB has already started")
    ledger = json.loads((root / "pre_science_call_ledger.json").read_text(encoding="utf-8"))
    fixture = build_fixture()
    write_json(root / "science_started.json", {"task_id": TASK_ID, "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "point": "I20_J640", "fresh_initialization": True})
    ledger["hjb_calls_started"] = 1
    write_json(root / "in_progress_call_ledger.json", ledger)
    result, trace = observe_accepted_hjb(*fixture.arguments())
    ledger["hjb_calls_completed"] = 1
    accepted_terminal = _accepted_j640_point()["hjb"]
    reproducible = bool(
        not result.converged
        and result.iterations == accepted_terminal["iterations_used"] == 100
        and np.isclose(
            result.convergence_statistic,
            accepted_terminal["final_convergence_statistic"],
            rtol=1e-10,
            atol=1e-12,
        )
    )
    mechanism = classify_mechanism(trace, bool(result.converged))
    mechanism.update(
        {
            "reproduced_accepted_nonconvergence": reproducible,
            "accepted_final_convergence_statistic": accepted_terminal["final_convergence_statistic"],
            "replay_iterations": int(result.iterations),
            "replay_converged": bool(result.converged),
            "broad_prior_trajectory_available": False,
            "broad_replay_trajectory_persisted": True,
            "prior_comparison_boundary": "accepted prior evidence persisted terminal statistic but not a per-iteration J640 trajectory",
            "prior_accepted_chattering_comparison": {
                "classification": "POLICY_CHATTERING_WITH_VALUE_UPDATE_OSCILLATION_AND_LATER_DERIVATIVE_FLOOR_AMPLIFICATION__NOT_PURE_TWO_CYCLE__NOT_MONOTONE_SLOW",
                "comparison_is_descriptive_only": True,
            },
            "results_eligibility": False,
            "exactly_one_next_reviewer_gate": "REVIEWER_J640_HJB_MECHANISM_ROUTE_DECISION",
        }
    )
    write_json(root / "iteration_trace.json", trace)
    write_json(root / "mechanism_summary.json", mechanism)
    write_json(root / "call_ledger.json", ledger)
    write_json(
        root / "execution_complete.json",
        {
            "terminal_classification": mechanism["classification"],
            "reproduced": reproducible,
            "hjb_calls": 1,
            "kfe_calls": 0,
            "j1280_calls": 0,
            "results_eligibility": False,
        },
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("preflight", "run"))
    parser.add_argument("output_root", type=Path)
    args = parser.parse_args()
    return preflight(args.output_root) if args.command == "preflight" else execute(args.output_root)


if __name__ == "__main__":
    raise SystemExit(main())
