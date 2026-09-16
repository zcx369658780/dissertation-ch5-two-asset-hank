"""One-shot structural attribution of the two accepted Q0 closed classes.

This task-local forensic script performs no numerical stationary-mass solve and
imports no selector, root, generator-assembly, or HJB implementation.
"""

from __future__ import annotations

import argparse
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


N = 800
SHAPE = (20, 20, 2)
Q0_SHA256 = "093E1AF1ADFEEE5C50D3DD91EDDD678EBAC5BBA6C42E64DE73A63B82102AF1D5"
Q0_BYTES = 22474
ACCEPTED_MANIFEST_SHA256 = (
    "D628E24AD421EA5A38EF80230862FE7B3BBD9BFA368CA7BEB08820528ADB643E"
)
ACCEPTED_MANIFEST_BYTES = 125779
EXPECTED_LABELS_SHA256 = (
    "63717388651FFCCB336F6D0D324D6E3B063276E4F4D3ADE726FD639A63494A76"
)
ACCEPTED_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_interior_z_switching_option_a_reexecution_20260916"
)
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_q0_two_closed_classes_structural_attribution_20260916"
)
SCRIPT_RELATIVE = Path("scripts/ch5_q0_two_closed_classes_structural_attribution.py")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def array_sha256(values: np.ndarray, dtype: str) -> str:
    return sha256_bytes(np.asarray(values, dtype=dtype).tobytes())


def write_json(path: Path, value: Any) -> None:
    encoded = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(encoded + "\n", encoding="utf-8")
    temporary.replace(path)


def git_head(repository: Path) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repository, text=True
    ).strip()


def state_index(flat: int) -> list[int]:
    return [int(value) for value in np.unravel_index(flat, SHAPE, order="F")]


def physical_state(receipts: list[dict[str, Any]], flat: int) -> dict[str, float]:
    cell = receipts[flat]["selector_cell"]
    return {name: float(cell[name]) for name in ("b", "a", "z")}


def selected_policy_receipt(
    receipt: dict[str, Any], manifest_entry: dict[str, Any]
) -> dict[str, Any]:
    selected = receipt["selector_result"]["selected"]
    interior_z = selected.get("interior_z_receipt")
    lower_zero = selected.get("lower_a_zero_kink_multiplier_receipt")
    if interior_z is not None:
        policy_branch = "INTERIOR_Z_ZERO_LIQUID_SWITCH"
    else:
        policy_branch = "ENUMERATED_DIRECTIONAL_DERIVATIVE_POLICY"
    return {
        "receipt": {
            "path": manifest_entry["path"],
            "bytes": int(manifest_entry["bytes"]),
            "sha256": str(manifest_entry["sha256"]),
        },
        "policy_branch": policy_branch,
        "active_constraints": selected["active_constraints"],
        "transfer_branch": selected["transfer_branch"],
        "derivative_branches": selected["derivative_branches"],
        "z_marker": None if interior_z is None else interior_z.get("marker"),
        "lower_a_zero_kink_marker": None if lower_zero is None else lower_zero.get("marker"),
        "boundary_adapter_markers": receipt.get("boundary_adapter_markers", {}),
        "q_b": selected["q_b"],
        "q_a": selected["q_a"],
        "c": selected["c"],
        "l": selected["l"],
        "d": selected["d"],
        "cost": selected["cost"],
        "g_b": selected["g_b"],
        "g_a": selected["g_a"],
        "multipliers": selected.get("multipliers", {}),
        "slacks": selected.get("slacks", {}),
        "active_equality_receipts": selected.get("active_equality_receipts", {}),
        "interior_z_receipt": interior_z,
        "lower_a_zero_kink_multiplier_receipt": lower_zero,
        "cell_derivatives": receipt["selector_cell"]["derivatives"],
    }


def outgoing_rates(
    q: sparse.csr_matrix, receipts: list[dict[str, Any]], flat: int
) -> dict[str, Any]:
    row_start, row_end = q.indptr[flat : flat + 2]
    origin_index = state_index(flat)
    outgoing = []
    for position in range(int(row_start), int(row_end)):
        destination = int(q.indices[position])
        rate = float(q.data[position])
        if destination == flat or rate <= 0.0:
            continue
        destination_index = state_index(destination)
        changed = [
            name
            for name, left, right in zip(
                ("b", "a", "z"), origin_index, destination_index
            )
            if left != right
        ]
        outgoing.append(
            {
                "destination_flat_f_zero_based": destination,
                "destination_index_b_a_z_zero_based": destination_index,
                "destination_physical_b_a_z": physical_state(receipts, destination),
                "rate": rate,
                "transition_dimension": changed[0] if len(changed) == 1 else changed,
            }
        )
    return {
        "diagonal": float(q[flat, flat]),
        "positive_outgoing_rate_sum": float(sum(item["rate"] for item in outgoing)),
        "positive_outgoing": outgoing,
        "asset_outgoing": [
            item for item in outgoing if item["transition_dimension"] in ("b", "a")
        ],
        "productivity_outgoing": [
            item for item in outgoing if item["transition_dimension"] == "z"
        ],
    }


def condensation_analysis(
    adjacency: sparse.csr_matrix,
    labels: np.ndarray,
    component_count: int,
    closed_labels: list[int],
    receipts: list[dict[str, Any]],
) -> dict[str, Any]:
    edges: set[tuple[int, int]] = set()
    for origin in range(N):
        source_component = int(labels[origin])
        for destination in adjacency.indices[
            adjacency.indptr[origin] : adjacency.indptr[origin + 1]
        ]:
            target_component = int(labels[int(destination)])
            if target_component != source_component:
                edges.add((source_component, target_component))
    successors: list[set[int]] = [set() for _ in range(component_count)]
    for source, target in edges:
        successors[source].add(target)

    class_a, class_b = closed_labels
    reachable: list[set[int]] = []
    distances: list[dict[int, int]] = []
    for source in range(component_count):
        stack = [(source, 0)]
        seen: dict[int, int] = {}
        while stack:
            node, distance = stack.pop()
            old = seen.get(node)
            if old is not None and old <= distance:
                continue
            seen[node] = distance
            stack.extend((target, distance + 1) for target in successors[node])
        reached = {label for label in closed_labels if label in seen}
        reachable.append(reached)
        distances.append({label: seen[label] for label in reached})

    def category(reached: set[int]) -> str:
        if reached == {class_a}:
            return "A_ONLY"
        if reached == {class_b}:
            return "B_ONLY"
        if reached == {class_a, class_b}:
            return "BOTH_REACHABLE"
        return "NEITHER"

    categories = [category(item) for item in reachable]
    component_sizes = np.bincount(labels, minlength=component_count)
    category_counts: dict[str, dict[str, int]] = {}
    for name in ("A_ONLY", "B_ONLY", "BOTH_REACHABLE", "NEITHER"):
        members = [index for index, value in enumerate(categories) if value == name]
        category_counts[name] = {
            "scc_count": len(members),
            "state_count": int(sum(component_sizes[index] for index in members)),
        }

    component_members = [
        [int(value) for value in np.flatnonzero(labels == component)]
        for component in range(component_count)
    ]
    dag_nodes = []
    for component in range(component_count):
        representative = component_members[component][0]
        dag_nodes.append(
            {
                "scc_label": component,
                "members_flat_f_zero_based": component_members[component],
                "representative_index_b_a_z_zero_based": state_index(representative),
                "representative_physical_b_a_z": physical_state(receipts, representative),
                "successors": sorted(successors[component]),
                "reachable_closed_labels": sorted(reachable[component]),
                "distance_to_reachable_closed_labels": {
                    str(key): value for key, value in sorted(distances[component].items())
                },
                "reachability_category": categories[component],
            }
        )

    asset_scc = np.empty((SHAPE[0], SHAPE[1]), dtype=int)
    asset_category = np.empty((SHAPE[0], SHAPE[1]), dtype=object)
    for i_b in range(SHAPE[0]):
        for i_a in range(SHAPE[1]):
            flat_zero = int(np.ravel_multi_index((i_b, i_a, 0), SHAPE, order="F"))
            flat_one = int(np.ravel_multi_index((i_b, i_a, 1), SHAPE, order="F"))
            if labels[flat_zero] != labels[flat_one]:
                raise RuntimeError("productivity pair does not share one SCC")
            label = int(labels[flat_zero])
            asset_scc[i_b, i_a] = label
            asset_category[i_b, i_a] = categories[label]

    separatrix = []
    for i_b in range(SHAPE[0]):
        for i_a in range(SHAPE[1]):
            for j_b, j_a, dimension in (
                (i_b + 1, i_a, "b"),
                (i_b, i_a + 1, "a"),
            ):
                if j_b >= SHAPE[0] or j_a >= SHAPE[1]:
                    continue
                left_category = str(asset_category[i_b, i_a])
                right_category = str(asset_category[j_b, j_a])
                if left_category == right_category:
                    continue
                left_flat = int(np.ravel_multi_index((i_b, i_a, 0), SHAPE, order="F"))
                right_flat = int(np.ravel_multi_index((j_b, j_a, 0), SHAPE, order="F"))
                separatrix.append(
                    {
                        "neighbor_dimension": dimension,
                        "left_index_b_a": [i_b, i_a],
                        "left_physical_b_a": {
                            key: physical_state(receipts, left_flat)[key] for key in ("b", "a")
                        },
                        "left_scc": int(asset_scc[i_b, i_a]),
                        "left_category": left_category,
                        "right_index_b_a": [j_b, j_a],
                        "right_physical_b_a": {
                            key: physical_state(receipts, right_flat)[key] for key in ("b", "a")
                        },
                        "right_scc": int(asset_scc[j_b, j_a]),
                        "right_category": right_category,
                    }
                )

    directed_forks = []
    for component in range(component_count):
        successor_categories = sorted({categories[item] for item in successors[component]})
        if categories[component] == "BOTH_REACHABLE" and len(successor_categories) > 1:
            directed_forks.append(
                {
                    "scc_label": component,
                    "members_flat_f_zero_based": component_members[component],
                    "representative_index_b_a_z_zero_based": state_index(
                        component_members[component][0]
                    ),
                    "representative_physical_b_a_z": physical_state(
                        receipts, component_members[component][0]
                    ),
                    "successors": sorted(successors[component]),
                    "successor_categories": successor_categories,
                    "distance_to_A": distances[component].get(class_a),
                    "distance_to_B": distances[component].get(class_b),
                }
            )

    b_values = [physical_state(receipts, i_b)["b"] for i_b in range(SHAPE[0])]
    a_values = [
        physical_state(
            receipts,
            int(np.ravel_multi_index((0, i_a, 0), SHAPE, order="F")),
        )["a"]
        for i_a in range(SHAPE[1])
    ]
    category_grid_by_a_then_b = [
        [str(asset_category[i_b, i_a]) for i_b in range(SHAPE[0])]
        for i_a in range(SHAPE[1])
    ]
    return {
        "dag_edge_count": len(edges),
        "dag_edges": [[source, target] for source, target in sorted(edges)],
        "dag_nodes": dag_nodes,
        "basin_counts": category_counts,
        "asset_grid": {
            "b_values": b_values,
            "a_values": a_values,
            "row_order": "a increasing; each row lists b increasing",
            "reachability_categories": category_grid_by_a_then_b,
        },
        "separatrix_neighbor_pair_count": len(separatrix),
        "separatrix_neighbor_pairs": separatrix,
        "directed_fork_count": len(directed_forks),
        "directed_forks": directed_forks,
    }


def seal_manifest(output: Path) -> None:
    entries = []
    for path in sorted(item for item in output.iterdir() if item.name != "sealed_manifest.json"):
        if path.is_file():
            entries.append(
                {"path": path.name, "bytes": path.stat().st_size, "sha256": sha256_file(path)}
            )
    write_json(
        output / "sealed_manifest.json",
        {
            "schema": "CH5_Q0_TWO_CLOSED_CLASSES_STRUCTURAL_ATTRIBUTION_V1",
            "entry_count": len(entries),
            "total_bytes": sum(int(item["bytes"]) for item in entries),
            "entries": entries,
        },
    )


def execute(repository: Path) -> str:
    repository = repository.resolve(strict=True)
    accepted = repository / ACCEPTED_RELATIVE
    output = repository / OUTPUT_RELATIVE
    output.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    script_path = repository / SCRIPT_RELATIVE
    pre_hash = sha256_file(script_path)
    ledger = {
        "q0_loads": 0,
        "structural_graph_audits": 0,
        "scc_decompositions": 0,
        "condensation_reachability_analyses": 0,
        "accepted_cell_receipt_reads": 0,
        "forbidden_calls": {
            "SVD_or_GESVD": 0,
            "eigendecomposition_or_nullspace": 0,
            "stationary_mass": 0,
            "Q0_transpose_times_p": 0,
            "row_replacement_pin_or_source": 0,
            "selector": 0,
            "root": 0,
            "policy_map": 0,
            "D2_reassembly": 0,
            "HJB": 0,
            "V1_remap": 0,
            "MATLAB_or_downstream": 0,
            "retry": 0,
            "edge_tolerance_graph_repair_or_diffusion": 0,
        },
    }

    manifest_path = accepted / "manifest.json"
    manifest_bytes = manifest_path.read_bytes()
    if len(manifest_bytes) != ACCEPTED_MANIFEST_BYTES or sha256_bytes(manifest_bytes) != ACCEPTED_MANIFEST_SHA256:
        raise RuntimeError("accepted manifest identity mismatch")
    manifest = json.loads(manifest_bytes)
    entries = {str(item["path"]): item for item in manifest["entries"]}
    q0_path = accepted / "d2_generator.npz"
    if q0_path.stat().st_size != Q0_BYTES or sha256_file(q0_path) != Q0_SHA256:
        raise RuntimeError("accepted Q0 identity mismatch")

    receipts: list[dict[str, Any]] = []
    for flat in range(N):
        name = f"cell_{flat:04d}.json"
        entry = entries.get(name)
        if entry is None:
            raise RuntimeError(f"manifest lacks {name}")
        raw = (accepted / name).read_bytes()
        ledger["accepted_cell_receipt_reads"] += 1
        if len(raw) != int(entry["bytes"]) or sha256_bytes(raw) != str(entry["sha256"]):
            raise RuntimeError(f"accepted receipt identity mismatch: {name}")
        receipt = json.loads(raw)
        if (
            receipt["flat_index_f_zero_based"] != flat
            or receipt["index_b_a_z_zero_based"] != state_index(flat)
            or receipt["selector_result"]["outcome"] != "SELECTED_ADMISSIBLE"
            or receipt["selector_result"]["selected"] is None
        ):
            raise RuntimeError(f"accepted receipt content mismatch: {name}")
        receipts.append(receipt)

    ledger["q0_loads"] += 1
    q_loaded = sparse.load_npz(q0_path)
    if getattr(q_loaded, "format", None) != "csr":
        raise RuntimeError("accepted Q0 is not CSR")
    q = sparse.csr_matrix(q_loaded, copy=False)

    ledger["structural_graph_audits"] += 1
    if q.shape != (N, N) or not np.all(np.isfinite(q.data)):
        raise RuntimeError("accepted Q0 shape or finite audit failed")
    offdiagonal = q.copy()
    offdiagonal.setdiag(0.0)
    offdiagonal.eliminate_zeros()
    if np.any(offdiagonal.data < 0.0):
        raise RuntimeError("accepted Q0 has a negative offdiagonal")
    positive = offdiagonal.copy()
    positive.data = np.ones(positive.nnz, dtype=np.int8)
    adjacency = sparse.csr_matrix(positive)
    if adjacency.nnz != 2318:
        raise RuntimeError("exact-positive edge count did not reproduce")

    ledger["scc_decompositions"] += 1
    component_count, labels = csgraph.connected_components(
        adjacency, directed=True, connection="strong", return_labels=True
    )
    sizes = np.bincount(labels, minlength=component_count)
    closed = np.ones(component_count, dtype=bool)
    for origin in range(N):
        origin_component = int(labels[origin])
        for destination in adjacency.indices[
            adjacency.indptr[origin] : adjacency.indptr[origin + 1]
        ]:
            if int(labels[int(destination)]) != origin_component:
                closed[origin_component] = False
    closed_labels = [int(value) for value in np.flatnonzero(closed)]
    labels_hash = array_sha256(labels, "<i8")
    if (
        int(component_count) != 400
        or not np.all(sizes == 2)
        or len(closed_labels) != 2
        or int(N - np.sum(sizes[closed])) != 796
        or labels_hash != EXPECTED_LABELS_SHA256
    ):
        raise RuntimeError("previous two-class SCC result did not reproduce exactly")

    closed_classes = []
    for class_name, label in zip(("A", "B"), closed_labels):
        members = [int(value) for value in np.flatnonzero(labels == label)]
        member_receipts = []
        for flat in members:
            receipt = receipts[flat]
            policy = selected_policy_receipt(receipt, entries[f"cell_{flat:04d}.json"])
            rates = outgoing_rates(q, receipts, flat)
            member_receipts.append(
                {
                    "flat_f_zero_based": flat,
                    "index_b_a_z_zero_based": state_index(flat),
                    "physical_b_a_z": physical_state(receipts, flat),
                    "selected_policy": policy,
                    "outgoing_q0_rates": rates,
                    "asset_grid_boundary_flags": {
                        "lower_b": state_index(flat)[0] == 0,
                        "upper_b": state_index(flat)[0] == SHAPE[0] - 1,
                        "lower_a": state_index(flat)[1] == 0,
                        "upper_a": state_index(flat)[1] == SHAPE[1] - 1,
                    },
                }
            )
        closed_classes.append(
            {
                "class": class_name,
                "scc_label": label,
                "members": member_receipts,
            }
        )

    ledger["condensation_reachability_analyses"] += 1
    condensation = condensation_analysis(
        adjacency, labels, int(component_count), closed_labels, receipts
    )

    diagnostics_path = accepted / "failed_cell_diagnostics.json"
    diagnostics = json.loads(diagnostics_path.read_text(encoding="utf-8"))
    diagnostic_by_index = {
        tuple(item["index_b_a_z_zero_based"]): item for item in diagnostics["cells"]
    }
    comparisons = []
    for closed_class in closed_classes:
        for member in closed_class["members"]:
            index = tuple(member["index_b_a_z_zero_based"])
            comparison = diagnostic_by_index.get(index)
            comparisons.append(
                {
                    "class": closed_class["class"],
                    "flat_f_zero_based": member["flat_f_zero_based"],
                    "index_b_a_z_zero_based": list(index),
                    "exact_existing_v0_v1_diagnostic": comparison,
                    "comparison_available": comparison is not None,
                }
            )

    all_members = [
        member for closed_class in closed_classes for member in closed_class["members"]
    ]
    zero_asset_drift = all(
        member["selected_policy"]["g_b"] == 0.0
        and member["selected_policy"]["g_a"] == 0.0
        and not member["outgoing_q0_rates"]["asset_outgoing"]
        for member in all_members
    )
    z_markers = sorted(
        {
            member["selected_policy"]["z_marker"]
            for member in all_members
            if member["selected_policy"]["z_marker"] is not None
        }
    )
    zero_kink_markers = sorted(
        {
            member["selected_policy"]["lower_a_zero_kink_marker"]
            for member in all_members
            if member["selected_policy"]["lower_a_zero_kink_marker"] is not None
        }
    )
    any_boundary = any(
        any(member["asset_grid_boundary_flags"].values()) for member in all_members
    )
    if zero_asset_drift:
        terminal = "ATTRIBUTED__TWO_RECURRENT_CLASSES_FROM_EXACT_ZERO_ASSET_DRIFT_SINKS"
    else:
        terminal = "ATTRIBUTED__TWO_RECURRENT_CLASSES_FROM_EXACT_POLICY_FLOW_TOPOLOGY"
    attribution = {
        "terminal": terminal,
        "baseline": git_head(repository),
        "q0": {"bytes": Q0_BYTES, "sha256": Q0_SHA256},
        "graph": {
            "exact_positive_edge_count": int(adjacency.nnz),
            "component_count": int(component_count),
            "component_sizes": [int(value) for value in sizes],
            "closed_labels": closed_labels,
            "closed_class_count": len(closed_labels),
            "transient_state_count": int(N - np.sum(sizes[closed])),
            "labels_sha256": labels_hash,
        },
        "closed_classes": closed_classes,
        "condensation": condensation,
        "v0_v1_exact_coordinate_comparisons": comparisons,
        "mechanism": {
            "all_recurrent_states_have_exact_zero_g_b_and_g_a": zero_asset_drift,
            "all_recurrent_states_have_only_productivity_positive_outgoing_rates": all(
                not member["outgoing_q0_rates"]["asset_outgoing"]
                and len(member["outgoing_q0_rates"]["productivity_outgoing"]) == 1
                for member in all_members
            ),
            "z_markers": z_markers,
            "lower_a_zero_kink_markers": zero_kink_markers,
            "any_recurrent_state_on_asset_grid_boundary": any_boundary,
            "classification": terminal,
        },
    }
    write_json(output / "structural_attribution.json", attribution)
    ledger["terminal_classification"] = terminal
    ledger["wall_seconds"] = float(time.perf_counter() - started)
    write_json(output / "execution_ledger.json", ledger)
    post_hash = sha256_file(script_path)
    write_json(
        output / "code_freeze_readback.json",
        {
            "script": str(SCRIPT_RELATIVE),
            "sha256_before_q0_load": pre_hash,
            "sha256_after_execution": post_hash,
            "matches": post_hash == pre_hash,
        },
    )
    seal_manifest(output)
    print(terminal)
    return terminal


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    args = parser.parse_args(argv)
    execute(args.repository)
    return 0


if __name__ == "__main__":
    sys.exit(main())
