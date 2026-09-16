"""One-shot accepted-V1 policy remap and exact-positive Q1 topology audit.

This task-local module reuses the accepted corrected selector, derivative
adapter, and D2 assembler without changing their scientific laws.  It does not
construct a value iterate, stationary mass, nullspace, eigenvector, or KFE
solution.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from typing import Any

import numpy as np
from scipy import sparse
from scipy.sparse import csgraph

from .contracts import AUTHORITY_ID
from .generator import assemble_consumed_drift_generator
from .option_a_step import (
    BoundOptionAInputs,
    _field_sha256,
    _input_receipt,
    bind_option_a_inputs,
    boundary_cell_derivatives,
    coordinate_action_receipt,
    iter_f_order_indices,
    raw_derivative_fields,
)
from .selector import (
    CorrectedSelectorCell,
    SelectorBudget,
    select_constrained_policy,
)


N = 800
SHAPE = (20, 20, 2)
ACCEPTED_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_interior_z_switching_option_a_reexecution_20260916"
)
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_v1_policy_remap_q1_topology_20260916"
)
ARRAYS_NAME = "direct_step_arrays.npz"
ARRAYS_SHA256 = "28A27473A4C08CCD20550B9EDF1509BABB4D7D882A9429F7F54F55DE72083173"
ARRAYS_BYTES = 29380
V1_SHA256 = "5C410EBC329F08B37F941A783E7F2C84BFCDCB67C6E24118114BE8C55697F2E2"
ACCEPTED_OPTION_A_COMMIT = "9a4eb0e5ec3627743596daa9b991436d2124efa9"
PRIOR_Q0_CLASSES = ((5, 405), (6, 406))
PRIOR_Q0_POLICY_BRANCH = "INTERIOR_Z_ZERO_LIQUID_SWITCH"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    encoded = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(encoded + "\n", encoding="utf-8")
    temporary.replace(path)


def git_head(repository: Path) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repository, text=True
    ).strip()


def git_blob(repository: Path, revision: str, relative: str) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", f"{revision}:{relative}"], cwd=repository, text=True
    ).strip()


def state_index(flat: int, shape: tuple[int, int, int] = SHAPE) -> list[int]:
    return [int(value) for value in np.unravel_index(flat, shape, order="F")]


def policy_branch(selected: dict[str, Any]) -> str:
    if selected.get("interior_z_receipt") is not None:
        return "INTERIOR_Z_ZERO_LIQUID_SWITCH"
    return "ENUMERATED_DIRECTIONAL_DERIVATIVE_POLICY"


def analyze_exact_positive_topology(q: sparse.spmatrix) -> dict[str, Any]:
    """Perform one exact-positive graph audit, SCC, and condensation analysis."""

    matrix = sparse.csr_matrix(q)
    if matrix.shape[0] != matrix.shape[1] or not np.all(np.isfinite(matrix.data)):
        raise ValueError("Q1 must be a finite square sparse matrix")
    offdiagonal = matrix.copy()
    offdiagonal.setdiag(0.0)
    offdiagonal.eliminate_zeros()
    if offdiagonal.nnz and np.any(offdiagonal.data < 0.0):
        raise ValueError("Q1 contains a negative offdiagonal")
    adjacency = offdiagonal.copy()
    adjacency.data = np.ones(adjacency.nnz, dtype=np.int8)
    adjacency = sparse.csr_matrix(adjacency)

    component_count, labels = csgraph.connected_components(
        adjacency, directed=True, connection="strong", return_labels=True
    )
    component_count = int(component_count)
    members = [
        [int(value) for value in np.flatnonzero(labels == component)]
        for component in range(component_count)
    ]
    successors: list[set[int]] = [set() for _ in range(component_count)]
    edges: set[tuple[int, int]] = set()
    for origin in range(matrix.shape[0]):
        source = int(labels[origin])
        for destination in adjacency.indices[
            adjacency.indptr[origin] : adjacency.indptr[origin + 1]
        ]:
            target = int(labels[int(destination)])
            if source != target:
                successors[source].add(target)
                edges.add((source, target))
    closed_labels = sorted(
        (component for component in range(component_count) if not successors[component]),
        key=lambda component: members[component][0],
    )
    closed_ordinal = {label: ordinal for ordinal, label in enumerate(closed_labels)}

    nodes = []
    for source in range(component_count):
        stack = [source]
        seen: set[int] = set()
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            stack.extend(successors[node])
        reached = sorted(
            closed_ordinal[label] for label in closed_labels if label in seen
        )
        nodes.append(
            {
                "label": source,
                "members": members[source],
                "successors": sorted(successors[source]),
                "reachable_closed_ordinals": reached,
            }
        )
    closed_members = [members[label] for label in closed_labels]
    closed_state_count = sum(len(item) for item in closed_members)
    return {
        "adjacency": adjacency,
        "labels": labels,
        "exact_positive_edge_count": int(adjacency.nnz),
        "component_count": component_count,
        "component_sizes": [len(item) for item in members],
        "closed_labels": closed_labels,
        "closed_members": closed_members,
        "closed_class_count": len(closed_labels),
        "transient_state_count": int(matrix.shape[0] - closed_state_count),
        "condensation": {
            "edge_count": len(edges),
            "edges": [[left, right] for left, right in sorted(edges)],
            "nodes": nodes,
        },
    }


def _selected_summary(receipt: dict[str, Any]) -> dict[str, Any]:
    selected = receipt["selector_result"]["selected"]
    interior_z = selected.get("interior_z_receipt")
    lower_zero = selected.get("lower_a_zero_kink_multiplier_receipt")
    return {
        "policy_branch": policy_branch(selected),
        "active_constraints": selected["active_constraints"],
        "transfer_branch": selected["transfer_branch"],
        "derivative_branches": selected["derivative_branches"],
        "z_marker": None if interior_z is None else interior_z.get("marker"),
        "lower_a_zero_kink_marker": None if lower_zero is None else lower_zero.get("marker"),
        "q_b": selected["q_b"],
        "q_a": selected["q_a"],
        "c": selected["c"],
        "l": selected["l"],
        "d": selected["d"],
        "cost": selected["cost"],
        "g_b": selected["g_b"],
        "g_a": selected["g_a"],
        "utility": selected["utility"],
        "hamiltonian": selected["hamiltonian"],
        "multipliers": selected.get("multipliers", {}),
        "slacks": selected.get("slacks", {}),
        "active_equality_receipts": selected.get("active_equality_receipts", {}),
        "interior_z_receipt": interior_z,
        "lower_a_zero_kink_multiplier_receipt": lower_zero,
        "cell_derivatives": receipt["selector_cell"]["derivatives"],
        "boundary_adapter_markers": receipt.get("boundary_adapter_markers", {}),
    }


def _physical(receipts: list[dict[str, Any]], flat: int) -> dict[str, float]:
    cell = receipts[flat]["selector_cell"]
    return {name: float(cell[name]) for name in ("b", "a", "z")}


def _outgoing(q: sparse.csr_matrix, receipts: list[dict[str, Any]], flat: int) -> dict[str, Any]:
    origin = state_index(flat)
    rows = []
    for position in range(q.indptr[flat], q.indptr[flat + 1]):
        destination = int(q.indices[position])
        rate = float(q.data[position])
        if destination == flat or rate <= 0.0:
            continue
        destination_index = state_index(destination)
        changed = [
            name
            for name, left, right in zip(("b", "a", "z"), origin, destination_index)
            if left != right
        ]
        rows.append(
            {
                "destination_flat_f_zero_based": destination,
                "destination_index_b_a_z_zero_based": destination_index,
                "destination_physical_b_a_z": _physical(receipts, destination),
                "rate": rate,
                "transition_dimension": changed[0] if len(changed) == 1 else changed,
            }
        )
    return {
        "diagonal": float(q[flat, flat]),
        "positive_outgoing_rate_sum": float(sum(row["rate"] for row in rows)),
        "positive_outgoing": rows,
    }


def _reachability_receipt(
    topology: dict[str, Any], receipts: list[dict[str, Any]]
) -> dict[str, Any]:
    labels = np.asarray(topology["labels"])
    closed_members = topology["closed_members"]
    exact_q0_pair_survival = closed_members == [list(item) for item in PRIOR_Q0_CLASSES]
    if exact_q0_pair_survival:
        closed_names = ["A", "B"]
    else:
        closed_names = [f"C{ordinal}" for ordinal in range(len(closed_members))]
    nodes = topology["condensation"]["nodes"]
    node_categories = {
        int(node["label"]): (
            "NONE_REACHABLE"
            if not node["reachable_closed_ordinals"]
            else "+".join(closed_names[value] for value in node["reachable_closed_ordinals"])
        )
        for node in nodes
    }
    category_counts: dict[str, dict[str, int]] = {}
    for label, category in node_categories.items():
        row = category_counts.setdefault(category, {"scc_count": 0, "state_count": 0})
        row["scc_count"] += 1
        row["state_count"] += int(np.count_nonzero(labels == label))

    asset_categories = np.empty((SHAPE[0], SHAPE[1]), dtype=object)
    for i_b in range(SHAPE[0]):
        for i_a in range(SHAPE[1]):
            flat0 = int(np.ravel_multi_index((i_b, i_a, 0), SHAPE, order="F"))
            flat1 = int(np.ravel_multi_index((i_b, i_a, 1), SHAPE, order="F"))
            if labels[flat0] != labels[flat1]:
                raise RuntimeError("two-way productivity pair does not share one Q1 SCC")
            asset_categories[i_b, i_a] = node_categories[int(labels[flat0])]
    separatrix = []
    for i_b in range(SHAPE[0]):
        for i_a in range(SHAPE[1]):
            for j_b, j_a, dimension in ((i_b + 1, i_a, "b"), (i_b, i_a + 1, "a")):
                if j_b >= SHAPE[0] or j_a >= SHAPE[1]:
                    continue
                left = str(asset_categories[i_b, i_a])
                right = str(asset_categories[j_b, j_a])
                if left != right:
                    separatrix.append(
                        {
                            "dimension": dimension,
                            "left_index_b_a": [i_b, i_a],
                            "left_category": left,
                            "right_index_b_a": [j_b, j_a],
                            "right_category": right,
                        }
                    )
    return {
        "closed_class_names": closed_names,
        "q0_A_B_style_labels_applicable": exact_q0_pair_survival,
        "category_counts": category_counts,
        "asset_grid": {
            "b_values": [_physical(receipts, i_b)["b"] for i_b in range(SHAPE[0])],
            "a_values": [
                _physical(receipts, int(np.ravel_multi_index((0, i_a, 0), SHAPE, order="F")))["a"]
                for i_a in range(SHAPE[1])
            ],
            "row_order": "a increasing; each row lists b increasing",
            "categories": [
                [str(asset_categories[i_b, i_a]) for i_b in range(SHAPE[0])]
                for i_a in range(SHAPE[1])
            ],
        },
        "separatrix_neighbor_pair_count": len(separatrix),
        "separatrix_neighbor_pairs": separatrix,
    }


def _outward_face_receipt(mu_b: np.ndarray, mu_a: np.ndarray) -> dict[str, Any]:
    rows = []
    for axis, drift, dimension in (("b", mu_b, 0), ("a", mu_a, 1)):
        for side in ("lower", "upper"):
            selector: list[object] = [slice(None)] * 3
            selector[dimension] = 0 if side == "lower" else drift.shape[dimension] - 1
            values = np.asarray(drift[tuple(selector)], dtype=float)
            outward_drift = np.maximum(-values, 0.0) if side == "lower" else np.maximum(values, 0.0)
            # D2 divides retained drift by a positive adjacent spacing.  Exact
            # zero outward drift therefore implies exact zero outward rate and
            # flux without clipping or an edge tolerance.
            rows.append(
                {
                    "axis": axis,
                    "side": side,
                    "maximum_outward_drift": float(np.max(outward_drift, initial=0.0)),
                    "maximum_outward_rate": 0.0 if not np.any(outward_drift) else None,
                    "maximum_outward_flux": 0.0 if not np.any(outward_drift) else None,
                    "exact_zero": bool(np.all(outward_drift == 0.0)),
                }
            )
    return {"faces": rows, "all_exact_zero": all(row["exact_zero"] for row in rows)}


def _scientific_code_hashes(repository: Path) -> dict[str, str]:
    paths = list((repository / "src/ch5_two_asset_hank/corrected_diagnostic").glob("*.py"))
    paths.extend(
        [
            repository / "tests/test_mp4c_2018_kfe_d123_option_a_single_step.py",
            repository / "tests/test_mp4c_2018_kfe_d123_lower_a_zero_kink_multiplier.py",
            repository / "tests/test_mp4c_2018_kfe_d123_interior_z_switching.py",
            repository / "tests/test_mp4c_2018_kfe_d123_v1_q1_topology.py",
        ]
    )
    return {
        path.relative_to(repository).as_posix(): sha256_file(path) for path in sorted(paths)
    }


def _preflight(repository: Path, inputs: BoundOptionAInputs) -> dict[str, Any]:
    accepted = repository / ACCEPTED_RELATIVE
    artifact = accepted / ARRAYS_NAME
    direct = json.loads((accepted / "direct_solve_receipt.json").read_text(encoding="utf-8"))
    manifest = json.loads((accepted / "manifest.json").read_text(encoding="utf-8"))
    entries = {str(row["path"]): row for row in manifest["entries"]}
    artifact_entry = entries.get(ARRAYS_NAME)
    frozen_core_paths = (
        "src/ch5_two_asset_hank/corrected_diagnostic/selector.py",
        "src/ch5_two_asset_hank/corrected_diagnostic/generator.py",
        "src/ch5_two_asset_hank/corrected_diagnostic/option_a_step.py",
    )
    # Git blob identity is invariant to checkout line-ending representation;
    # the accepted run's byte hashes are retained in its sealed freeze receipt.
    frozen_core_matches = {
        relative: git_blob(repository, "HEAD", relative)
        == git_blob(repository, ACCEPTED_OPTION_A_COMMIT, relative)
        for relative in frozen_core_paths
    }
    checks = {
        "artifact_exists": artifact.is_file(),
        "artifact_bytes_exact": artifact.stat().st_size == ARRAYS_BYTES,
        "artifact_sha256_exact": sha256_file(artifact) == ARRAYS_SHA256,
        "manifest_binds_artifact": artifact_entry is not None
        and int(artifact_entry["bytes"]) == ARRAYS_BYTES
        and str(artifact_entry["sha256"]) == ARRAYS_SHA256,
        "direct_receipt_binds_artifact": direct["arrays_artifact"] == {
            "bytes": ARRAYS_BYTES,
            "path": ARRAYS_NAME,
            "sha256": ARRAYS_SHA256,
        },
        "direct_receipt_binds_v1": direct["v1_sha256"] == V1_SHA256,
        "grid_shape_exact": inputs.grid.shape == SHAPE,
        "f_order_size_exact": len(list(iter_f_order_indices(inputs.grid.shape))) == N,
        "git_head_resolves": len(git_head(repository)) == 40,
        "accepted_selector_generator_adapter_unchanged": all(frozen_core_matches.values()),
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "accepted_artifact": {
            "path": str(artifact),
            "bytes": artifact.stat().st_size,
            "sha256": sha256_file(artifact),
            "v1_field_sha256_expected": V1_SHA256,
        },
        "input_identity": _input_receipt(inputs),
        "accepted_core_hash_matches": frozen_core_matches,
    }


def _ledger(budget: SelectorBudget) -> dict[str, Any]:
    return {
        "v1_artifact_loads": 0,
        "corrected_policy_maps": 0,
        "real_selector_evaluations": budget.selector_evaluations,
        "scalar_root_invocations": budget.root_invocations,
        "interior_z_root_invocations": budget.interior_z_root_invocations,
        "q1_d2_assemblies": 0,
        "graph_audits": 0,
        "scc_decompositions": 0,
        "condensation_reachability_analyses": 0,
        "retries": 0,
        "forbidden_calls": {
            "HJB_direct_solve_or_nonlinear_continuation": 0,
            "V2": 0,
            "KFE_nullspace_SVD_eigen_stationary_mass": 0,
            "Q1_transpose_times_p": 0,
            "row_replacement_pin_or_source_RHS": 0,
            "MATLAB_outer_firm_wage_return_GE_annual_shock_IRF_Results": 0,
        },
    }


def _seal(output: Path) -> None:
    entries = []
    for path in sorted(output.iterdir()):
        if path.is_file() and path.name != "sealed_manifest.json":
            entries.append(
                {"path": path.name, "bytes": path.stat().st_size, "sha256": sha256_file(path)}
            )
    write_json(
        output / "sealed_manifest.json",
        {
            "schema": "CH5_D123_V1_POLICY_REMAP_Q1_TOPOLOGY_V1",
            "entry_count": len(entries),
            "total_bytes": sum(int(row["bytes"]) for row in entries),
            "entries": entries,
        },
    )


def _finalize(
    repository: Path,
    output: Path,
    pre_hashes: dict[str, str],
    ledger: dict[str, Any],
    terminal: str,
    detail: dict[str, Any],
    started: float,
) -> str:
    post_hashes = _scientific_code_hashes(repository)
    ledger["terminal_classification"] = terminal
    ledger["wall_seconds"] = float(time.perf_counter() - started)
    write_json(output / "execution_ledger.json", ledger)
    write_json(
        output / "execution_summary.json",
        {
            "verdict": terminal,
            "detail": detail,
            "scientific_code_freeze_preserved": post_hashes == pre_hashes,
        },
    )
    write_json(
        output / "post_execution_freeze_check.json",
        {
            "scientific_code_sha256_after_execution": post_hashes,
            "matches_pre_execution_freeze": post_hashes == pre_hashes,
        },
    )
    _seal(output)
    return terminal


def execute(repository: Path, seed_path: Path, binding_path: Path) -> str:
    repository = repository.resolve(strict=True)
    output = repository / OUTPUT_RELATIVE
    output.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    inputs = bind_option_a_inputs(seed_path, binding_path)
    preflight = _preflight(repository, inputs)
    write_json(output / "preflight.json", preflight)
    if preflight["status"] != "PASS":
        raise RuntimeError("preflight failed before scientific-code freeze")

    pre_hashes = _scientific_code_hashes(repository)
    freeze = {
        "authority_id": AUTHORITY_ID,
        "git_head_before_v1_artifact_load": git_head(repository),
        "scientific_code_sha256_before_v1_artifact_load": pre_hashes,
        "accepted_v1_artifact": preflight["accepted_artifact"],
        "input_identity": _input_receipt(inputs),
        "budget": {
            "v1_artifact_loads": 1,
            "corrected_policy_maps": 1,
            "real_selector_evaluations": 800,
            "scalar_root_invocations": 3144,
            "interior_z_root_invocations": 2880,
            "q1_d2_assemblies": 1,
            "graph_audits": 1,
            "scc_decompositions": 1,
            "condensation_reachability_analyses": 1,
            "retries": 0,
        },
    }
    write_json(output / "pre_execution_freeze.json", freeze)
    code_freeze_identity = {
        "authority_id": AUTHORITY_ID,
        "git_head": freeze["git_head_before_v1_artifact_load"],
        "scientific_code_sha256": pre_hashes,
        "artifact_sha256": ARRAYS_SHA256,
        "v1_field_sha256": V1_SHA256,
    }

    budget = SelectorBudget(
        max_selector_evaluations=800,
        max_root_invocations=3144,
        max_interior_z_root_invocations=2880,
    )
    ledger = _ledger(budget)
    write_json(output / "execution_ledger.json", ledger)

    ledger["v1_artifact_loads"] = 1
    artifact = repository / ACCEPTED_RELATIVE / ARRAYS_NAME
    try:
        with np.load(artifact, allow_pickle=False) as loaded:
            if "v1" not in loaded.files:
                raise ValueError("accepted arrays artifact lacks v1")
            v1 = np.array(loaded["v1"], dtype=float, copy=True, order="F")
    except Exception as exc:
        return _finalize(
            repository,
            output,
            pre_hashes,
            ledger,
            "BLOCKED__INPUT_OR_FREEZE_BINDING_MISMATCH",
            {"stage": "v1_artifact_load", "type": type(exc).__name__, "message": str(exc)},
            started,
        )
    if v1.shape != SHAPE or not np.all(np.isfinite(v1)) or _field_sha256(v1) != V1_SHA256:
        return _finalize(
            repository,
            output,
            pre_hashes,
            ledger,
            "BLOCKED__INPUT_OR_FREEZE_BINDING_MISMATCH",
            {"stage": "v1_field_identity", "shape": list(v1.shape), "sha256": _field_sha256(v1)},
            started,
        )

    fields = raw_derivative_fields(v1, inputs.grid)
    mu_b = np.empty(SHAPE, dtype=float)
    mu_a = np.empty(SHAPE, dtype=float)
    receipts: list[dict[str, Any]] = []
    ledger["corrected_policy_maps"] = 1
    for flat, index in enumerate(iter_f_order_indices(SHAPE)):
        i_b, i_a, i_z = index
        b = float(inputs.grid.b[i_b])
        a = float(inputs.grid.a[i_a])
        z = float(inputs.grid.z[i_z])
        derivatives, markers = boundary_cell_derivatives(fields, index, inputs.grid)
        cell = CorrectedSelectorCell(
            cell_id=f"v1_q1_f{flat:04d}_b{i_b:03d}_a{i_a:03d}_z{i_z:03d}",
            b=b,
            a=a,
            z=z,
            b_lower=float(inputs.grid.b[0]),
            b_upper=float(inputs.grid.b[-1]),
            a_lower=float(inputs.grid.a[0]),
            a_upper=float(inputs.grid.a[-1]),
            net_wage=float((1.0 - inputs.scalars["tau"]) * inputs.scalars["wage"] * z),
            effective_r_b=float(
                inputs.scalars["r_b"]
                + (inputs.scalars["borrowing_rate_gap"] if b < 0.0 else 0.0)
            ),
            transfer_income=inputs.scalars["transfer_income"],
            effective_r_a=float(inputs.scalars["r_a"] * (1.0 - 0.1 * (a / 10.0) ** 9)),
            derivatives=derivatives,
        )
        path = output / f"cell_{flat:04d}.json"
        base = {
            "flat_index_f_zero_based": flat,
            "index_b_a_z_zero_based": list(index),
            "selector_cell": asdict(cell),
            "boundary_adapter_markers": markers,
            "code_freeze_identity": code_freeze_identity,
        }
        try:
            result = select_constrained_policy(cell, inputs.parameters, budget=budget)
            receipt = {
                **base,
                "selector_result": asdict(result),
                "cumulative_budget": asdict(budget),
                "receipt_persistence_order": "SELECTOR_RECEIPT_DURABLE_BEFORE_NEXT_CELL_OR_Q1",
            }
        except Exception as exc:
            receipt = {
                **base,
                "selector_exception": {"type": type(exc).__name__, "message": str(exc)},
                "cumulative_budget": asdict(budget),
                "receipt_persistence_order": "SELECTOR_EXCEPTION_DURABLE_BEFORE_STOP",
            }
            write_json(path, receipt)
            ledger.update(
                real_selector_evaluations=budget.selector_evaluations,
                scalar_root_invocations=budget.root_invocations,
                interior_z_root_invocations=budget.interior_z_root_invocations,
            )
            return _finalize(
                repository,
                output,
                pre_hashes,
                ledger,
                "FAIL__V1_POLICY_MAP_FIRST_CELL_NOT_ADMISSIBLE__STOPPED_WITHOUT_RETRY",
                {"flat": flat, "index": list(index), "receipt": path.name, "exception": receipt["selector_exception"]},
                started,
            )
        write_json(path, receipt)
        receipts.append(receipt)
        ledger.update(
            real_selector_evaluations=budget.selector_evaluations,
            scalar_root_invocations=budget.root_invocations,
            interior_z_root_invocations=budget.interior_z_root_invocations,
        )
        if _scientific_code_hashes(repository) != pre_hashes:
            return _finalize(
                repository,
                output,
                pre_hashes,
                ledger,
                "BLOCKED__INPUT_OR_FREEZE_BINDING_MISMATCH",
                {"stage": "post_selector_code_freeze", "flat": flat, "receipt": path.name},
                started,
            )
        if result.outcome != "SELECTED_ADMISSIBLE" or result.selected is None:
            return _finalize(
                repository,
                output,
                pre_hashes,
                ledger,
                "FAIL__V1_POLICY_MAP_FIRST_CELL_NOT_ADMISSIBLE__STOPPED_WITHOUT_RETRY",
                {"flat": flat, "index": list(index), "outcome": result.outcome, "receipt": path.name},
                started,
            )
        if result.selected.g_b is None or result.selected.g_a is None:
            return _finalize(
                repository,
                output,
                pre_hashes,
                ledger,
                "FAIL__V1_POLICY_MAP_FIRST_CELL_NOT_ADMISSIBLE__STOPPED_WITHOUT_RETRY",
                {"flat": flat, "index": list(index), "reason": "selected drift missing", "receipt": path.name},
                started,
            )
        mu_b[index] = float(result.selected.g_b)
        mu_a[index] = float(result.selected.g_a)

    if len(receipts) != N or budget.selector_evaluations != N:
        raise RuntimeError("full-map gate failed before Q1 D2")

    ledger["q1_d2_assemblies"] = 1
    try:
        generator = assemble_consumed_drift_generator(
            inputs.grid, mu_b=mu_b, mu_a=mu_a, z_generator=inputs.z_generator
        )
    except Exception as exc:
        write_json(output / "q1_d2_receipt.json", {"status": "RAISED", "type": type(exc).__name__, "message": str(exc)})
        return _finalize(
            repository,
            output,
            pre_hashes,
            ledger,
            "FAIL__Q1_D2_INVARIANT__STOPPED_BEFORE_TOPOLOGY",
            {"q1_d2_receipt": "q1_d2_receipt.json"},
            started,
        )
    coordinate = coordinate_action_receipt(generator.q, inputs.grid, mu_b, mu_a)
    face_rows = [asdict(face) for face in generator.boundary.faces]
    outward = _outward_face_receipt(mu_b, mu_a)
    checks = {
        "minimum_offdiagonal_nonnegative": generator.minimum_offdiagonal >= 0.0,
        "diagonal_construction_error_exact_zero": generator.diagonal_construction_error == 0.0,
        "q_one_within_prospective_bound": generator.max_abs_q_one <= generator.arithmetic_tolerance,
        "b_coordinate_within_prospective_bound": bool(coordinate["b"]["passes"]),
        "a_coordinate_within_prospective_bound": bool(coordinate["a"]["passes"]),
        "zero_tolerance_closed_faces_feasible": generator.boundary.feasible,
        "zero_outward_face_count": all(row["outward_count"] == 0 for row in face_rows),
        "zero_outward_face_amount": all(row["max_outward"] == 0.0 for row in face_rows),
        "exact_zero_outward_drift_rate_flux": bool(outward["all_exact_zero"]),
    }
    sparse.save_npz(output / "q1_generator.npz", generator.q)
    write_json(
        output / "q1_d2_receipt.json",
        {
            "status": "PASS" if all(checks.values()) else "FAIL",
            "checks": checks,
            "minimum_offdiagonal": generator.minimum_offdiagonal,
            "diagonal_construction_error": generator.diagonal_construction_error,
            "max_abs_q_one": generator.max_abs_q_one,
            "arithmetic_tolerance": generator.arithmetic_tolerance,
            "coordinate_action": coordinate,
            "closed_face_summaries": face_rows,
            "outward_face_drift_rate_flux": outward,
            "q1_artifact": {
                "path": "q1_generator.npz",
                "bytes": (output / "q1_generator.npz").stat().st_size,
                "sha256": sha256_file(output / "q1_generator.npz"),
            },
        },
    )
    if not all(checks.values()):
        return _finalize(
            repository,
            output,
            pre_hashes,
            ledger,
            "FAIL__Q1_D2_INVARIANT__STOPPED_BEFORE_TOPOLOGY",
            {"q1_d2_receipt": "q1_d2_receipt.json"},
            started,
        )

    ledger["graph_audits"] = 1
    ledger["scc_decompositions"] = 1
    ledger["condensation_reachability_analyses"] = 1
    try:
        topology = analyze_exact_positive_topology(generator.q)
        reachability = _reachability_receipt(topology, receipts)
    except Exception as exc:
        return _finalize(
            repository,
            output,
            pre_hashes,
            ledger,
            "FAIL__Q1_TOPOLOGY_AUDIT__STOPPED_WITHOUT_RETRY",
            {"type": type(exc).__name__, "message": str(exc)},
            started,
        )

    closed_classes = []
    for ordinal, members in enumerate(topology["closed_members"]):
        closed_classes.append(
            {
                "ordinal": ordinal,
                "members": [
                    {
                        "flat_f_zero_based": flat,
                        "index_b_a_z_zero_based": state_index(flat),
                        "physical_b_a_z": _physical(receipts, flat),
                        "selected_policy": _selected_summary(receipts[flat]),
                        "outgoing_q1_rates": _outgoing(generator.q, receipts, flat),
                    }
                    for flat in members
                ],
            }
        )
    closed_sets = [set(item) for item in topology["closed_members"]]
    prior_comparison = []
    for flat in (5, 405, 6, 406):
        selected = _selected_summary(receipts[flat])
        recurrent = any(flat in members for members in closed_sets)
        both_zero = selected["g_b"] == 0.0 and selected["g_a"] == 0.0
        prior_comparison.append(
            {
                "flat_f_zero_based": flat,
                "index_b_a_z_zero_based": state_index(flat),
                "physical_b_a_z": _physical(receipts, flat),
                "q0": {
                    "recurrent": True,
                    "policy_branch": PRIOR_Q0_POLICY_BRANCH,
                    "g_b": 0.0,
                    "g_a": 0.0,
                },
                "q1": {
                    "recurrent": recurrent,
                    "transient": not recurrent,
                    "policy_branch": selected["policy_branch"],
                    "policy_branch_changed": selected["policy_branch"] != PRIOR_Q0_POLICY_BRANCH,
                    "g_b": selected["g_b"],
                    "g_a": selected["g_a"],
                    "both_g_exact_zero": both_zero,
                    "no_longer_both_g_zero": not both_zero,
                    "selected_policy": selected,
                },
            }
        )

    if topology["closed_class_count"] == 1:
        terminal = "PASS__V1_COMPLETE_POLICY_MAP__Q1_SINGLE_CLOSED_CLASS__Q0_TWO_SINKS_DO_NOT_PERSIST"
    elif topology["closed_members"] == [list(item) for item in PRIOR_Q0_CLASSES]:
        terminal = "PASS__V1_COMPLETE_POLICY_MAP__Q1_TWO_RECURRENT_CLASSES_PERSIST"
    else:
        terminal = "PASS__V1_COMPLETE_POLICY_MAP__Q1_RECURRENT_TOPOLOGY_CHANGED_OTHERWISE"
    topology_receipt = {
        "terminal_classification": terminal,
        "q0_comparison": {
            "closed_class_count": 2,
            "closed_members": [list(item) for item in PRIOR_Q0_CLASSES],
        },
        "q1": {
            "exact_positive_edge_count": topology["exact_positive_edge_count"],
            "scc_count": topology["component_count"],
            "scc_sizes": topology["component_sizes"],
            "closed_class_count": topology["closed_class_count"],
            "closed_members": topology["closed_members"],
            "transient_state_count": topology["transient_state_count"],
            "condensation_edge_count": topology["condensation"]["edge_count"],
        },
        "closed_classes": closed_classes,
        "prior_q0_coordinate_comparison": prior_comparison,
        "condensation": topology["condensation"],
        "reachability": reachability,
    }
    write_json(output / "q1_topology.json", topology_receipt)
    return _finalize(
        repository,
        output,
        pre_hashes,
        ledger,
        terminal,
        {"q1_d2_receipt": "q1_d2_receipt.json", "q1_topology": "q1_topology.json"},
        started,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--seed", type=Path, required=True)
    parser.add_argument("--binding", type=Path, required=True)
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args(argv)
    if args.preflight_only:
        repository = args.repository.resolve(strict=True)
        inputs = bind_option_a_inputs(args.seed, args.binding)
        receipt = _preflight(repository, inputs)
        print(json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False))
        return 0 if receipt["status"] == "PASS" else 1
    terminal = execute(args.repository, args.seed, args.binding)
    print(terminal)
    return 0 if terminal.startswith("PASS__") else 2


if __name__ == "__main__":
    sys.exit(main())
