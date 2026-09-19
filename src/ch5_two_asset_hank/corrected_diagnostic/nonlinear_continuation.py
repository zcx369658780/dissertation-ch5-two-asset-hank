"""Bounded corrected-target nonlinear HJB continuation and terminal KFE gate."""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import time
from typing import Any
import warnings

import numpy as np
from scipy import linalg, sparse
from scipy.sparse import linalg as sparse_linalg

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
from .q1_kfe_validation import gamma, normalize_null_vector, rank_receipt
from .selector import (
    CorrectedSelectorCell,
    SelectorBudget,
    select_constrained_policy,
)
from .v1_q1_topology import analyze_exact_positive_topology


SHAPE = (20, 20, 2)
N = 800
DELTA = 1000.0
BELLMAN_TOLERANCE = 1.0e-8
VALUE_TOLERANCE = 1.0e-7
BACKWARD_ERROR_TOLERANCE = 1.0e-12
CYCLE_TOLERANCE = 1.0e-8
MAX_TOTAL_UPDATES = 100
MAX_NEW_UPDATES = 99
MAX_NEW_POLICY_MAPS = 99
MAX_SELECTOR_EVALUATIONS = 79_200
MAX_ROOT_INVOCATIONS = 311_256
MAX_INTERIOR_Z_ROOT_INVOCATIONS = 285_120
OMEGA = 70.0 / 361.0

OPTION_A_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_interior_z_switching_option_a_reexecution_20260916"
)
V1_Q1_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_v1_policy_remap_q1_topology_20260916"
)
Q1_KFE_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_q1_source_free_kfe_operator_validation_20260916"
)
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_bounded_nonlinear_hjb_kfe_continuation_20260917"
)

V1_ARTIFACT_SHA256 = "28A27473A4C08CCD20550B9EDF1509BABB4D7D882A9429F7F54F55DE72083173"
V1_FIELD_SHA256 = "5C410EBC329F08B37F941A783E7F2C84BFCDCB67C6E24118114BE8C55697F2E2"
V0_FIELD_SHA256 = "564B95B818713477691389903C3CFF72B5A7F991B924D52FBEB23D5A3675D665"
Q1_SHA256 = "5F96C2CFAAFB3EA7EF32943A892A9191FEDCC5DBC7AB28D066F5893D3F560D1E"
Q1_MANIFEST_SHA256 = "573FCF61220E5982EB4A6E78FAFC5D82310BAC7F7638D2D83B576B1420DDCF37"
P1_G1_ARTIFACT_SHA256 = "14E6EC29650A7F9F5D95B023E5B6E54AC1391DC836E2513AC9CACAFEEB7B4254"
ACCEPTED_OPTION_A_COMMIT = "9a4eb0e5ec3627743596daa9b991436d2124efa9"

CORE_AUTHORITY_PATHS = (
    "src/ch5_two_asset_hank/corrected_diagnostic/selector.py",
    "src/ch5_two_asset_hank/corrected_diagnostic/generator.py",
    "src/ch5_two_asset_hank/corrected_diagnostic/option_a_step.py",
)


class FailClosed(RuntimeError):
    def __init__(self, terminal: str, detail: dict[str, Any] | None = None) -> None:
        super().__init__(terminal)
        self.terminal = terminal
        self.detail = detail or {}


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def _canonical_sha256(value: Any) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest().upper()


def _integer_sha256(values: np.ndarray) -> str:
    return hashlib.sha256(np.asarray(values, dtype="<i8").tobytes()).hexdigest().upper()


def _write_json(path: Path, value: Any) -> None:
    text = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text + "\n", encoding="utf-8")
    temporary.replace(path)


def _git_head(repository: Path) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repository, text=True
    ).strip()


def _git_blob(repository: Path, revision: str, relative: str) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", f"{revision}:{relative}"], cwd=repository, text=True
    ).strip()


def _scientific_code_hashes(repository: Path) -> dict[str, str]:
    paths = list((repository / "src/ch5_two_asset_hank/corrected_diagnostic").glob("*.py"))
    paths.extend(
        [
            repository / "tests/test_mp4c_2018_kfe_d123_option_a_single_step.py",
            repository / "tests/test_mp4c_2018_kfe_d123_lower_a_zero_kink_multiplier.py",
            repository / "tests/test_mp4c_2018_kfe_d123_interior_z_switching.py",
            repository
            / "tests/test_mp4c_2018_kfe_d123_interior_a_zero_drift_switching.py",
            repository
            / "tests/test_mp4c_2018_kfe_d123_joint_two_axis_zero_drift_switching.py",
            repository / "tests/test_mp4c_2018_kfe_d123_v1_q1_topology.py",
            repository
            / "tests/test_mp4c_2018_kfe_d123_bounded_nonlinear_continuation.py",
        ]
    )
    return {
        path.relative_to(repository).as_posix(): _sha256(path)
        for path in sorted(paths)
    }


def _sparse_identity(q: sparse.csr_matrix) -> dict[str, str]:
    matrix = sparse.csr_matrix(q)
    return {
        "data": _field_sha256(matrix.data),
        "indices": _integer_sha256(matrix.indices),
        "indptr": _integer_sha256(matrix.indptr),
    }


def checkpoint_identity(
    value_sha256: str, policy_sha256: str, q_identity: dict[str, str]
) -> str:
    return _canonical_sha256(
        {"value": value_sha256, "policy": policy_sha256, "q": q_identity}
    )


def primary_converged(bellman_residual: float, value_change: float) -> bool:
    return bool(
        np.isfinite(bellman_residual)
        and np.isfinite(value_change)
        and bellman_residual <= BELLMAN_TOLERANCE
        and value_change <= VALUE_TOLERANCE
    )


def detect_exact_cycle(identities: list[str]) -> int | None:
    if len(identities) < 3:
        return None
    current = identities[-1]
    for previous in range(len(identities) - 3, -1, -1):
        if identities[previous] == current:
            return len(identities) - 1 - previous
    return None


def detect_approximate_cycle(
    values: list[np.ndarray], *, tolerance: float = CYCLE_TOLERANCE
) -> dict[str, Any] | None:
    for period in (2, 3):
        if len(values) < 2 * period:
            continue
        start = len(values) - period
        comparisons = [
            float(
                np.linalg.norm(
                    (values[index] - values[index - period]).ravel(order="F"),
                    ord=np.inf,
                )
            )
            for index in range(start, len(values))
        ]
        if all(np.isfinite(value) and value <= tolerance for value in comparisons):
            return {
                "period": period,
                "tolerance": tolerance,
                "comparison_indices_zero_based": [
                    [index - period, index] for index in range(start, len(values))
                ],
                "comparisons": comparisons,
            }
    return None


def normwise_backward_error(
    matrix: sparse.spmatrix, solution: np.ndarray, rhs: np.ndarray
) -> dict[str, Any]:
    csr = sparse.csr_matrix(matrix)
    x = np.asarray(solution, dtype=float)
    b = np.asarray(rhs, dtype=float)
    residual = np.asarray(csr @ x - b)
    residual_inf = float(np.linalg.norm(residual, ord=np.inf))
    matrix_inf = float(np.max(np.asarray(abs(csr).sum(axis=1)).ravel(), initial=0.0))
    solution_inf = float(np.linalg.norm(x, ord=np.inf))
    rhs_inf = float(np.linalg.norm(b, ord=np.inf))
    denominator = matrix_inf * solution_inf + rhs_inf
    backward_error = residual_inf / denominator if denominator else (0.0 if residual_inf == 0 else math.inf)
    return {
        "residual": residual,
        "residual_inf": residual_inf,
        "matrix_inf": matrix_inf,
        "solution_inf": solution_inf,
        "rhs_inf": rhs_inf,
        "denominator": denominator,
        "normwise_backward_error": backward_error,
    }


def _selected_identity(selected: dict[str, Any]) -> dict[str, Any]:
    interior = selected.get("interior_z_receipt")
    lower_a = selected.get("lower_a_zero_kink_multiplier_receipt")
    return {
        "derivative_branches": selected.get("derivative_branches"),
        "active_constraints": selected.get("active_constraints"),
        "transfer_branch": selected.get("transfer_branch"),
        "interior_z_marker": None if interior is None else interior.get("marker"),
        "lower_a_zero_kink_marker": None if lower_a is None else lower_a.get("marker"),
    }


def _policy_arrays(selected_rows: list[dict[str, Any]]) -> dict[str, np.ndarray]:
    names = ("utility", "c", "l", "d", "g_b", "g_a", "q_b", "q_a")
    result = {name: np.empty(SHAPE, dtype=float, order="F") for name in names}
    for flat, selected in enumerate(selected_rows):
        index = tuple(map(int, np.unravel_index(flat, SHAPE, order="F")))
        for name in names:
            value = selected.get(name)
            if value is None or not np.isfinite(float(value)):
                raise FailClosed(
                    "FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE",
                    {"stage": "selected_policy_field", "flat": flat, "field": name},
                )
            result[name][index] = float(value)
    return result


def _policy_diagnostics(
    current_rows: list[dict[str, Any]],
    previous_rows: list[dict[str, Any]],
    current_arrays: dict[str, np.ndarray],
    previous_arrays: dict[str, np.ndarray],
) -> dict[str, Any]:
    current_identities = [_selected_identity(row) for row in current_rows]
    previous_identities = [_selected_identity(row) for row in previous_rows]
    changed = [
        index
        for index, (left, right) in enumerate(zip(current_identities, previous_identities))
        if left != right
    ]
    summary: dict[str, Any] = {
        "identity_sha256": _canonical_sha256(current_identities),
        "identity_change_count": len(changed),
        "identity_change_flat_f_zero_based": changed,
        "transfer_branch_counts": dict(
            sorted(Counter(str(row["transfer_branch"]) for row in current_rows).items())
        ),
        "active_constraint_counts": dict(
            sorted(
                Counter(
                    "+".join(map(str, row.get("active_constraints", []))) or "none"
                    for row in current_rows
                ).items()
            )
        ),
        "interior_z_marker_counts": dict(
            sorted(
                Counter(
                    str(identity["interior_z_marker"] or "none")
                    for identity in current_identities
                ).items()
            )
        ),
        "continuous_field_max_abs_change": {},
    }
    for name in ("c", "l", "d", "g_b", "g_a", "q_b", "q_a", "utility"):
        difference = current_arrays[name] - previous_arrays[name]
        summary["continuous_field_max_abs_change"][name] = float(
            np.linalg.norm(difference.ravel(order="F"), ord=np.inf)
        )
    return summary


def _operator_diagnostics(
    current: sparse.csr_matrix, previous: sparse.csr_matrix
) -> dict[str, Any]:
    current_csr = sparse.csr_matrix(current)
    previous_csr = sparse.csr_matrix(previous)
    difference = (current_csr - previous_csr).tocsr()
    pattern_same = bool(
        np.array_equal(current_csr.indices, previous_csr.indices)
        and np.array_equal(current_csr.indptr, previous_csr.indptr)
    )
    return {
        "identity": _sparse_identity(current_csr),
        "nnz": int(current_csr.nnz),
        "sparsity_pattern_same_as_previous": pattern_same,
        "sparsity_pattern_changed": not pattern_same,
        "difference_nnz": int(difference.nnz),
        "difference_max_abs_entry": float(
            np.max(np.abs(difference.data), initial=0.0)
        ),
        "difference_inf_norm": float(
            np.max(np.asarray(abs(difference).sum(axis=1)).ravel(), initial=0.0)
        ),
    }


def _manifest_entries(document: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(row["path"]): row for row in document["entries"]}


def _verify_manifest_files(root: Path, document: dict[str, Any]) -> None:
    entries = _manifest_entries(document)
    for relative, expected in entries.items():
        path = root / relative
        if (
            not path.is_file()
            or path.stat().st_size != int(expected["bytes"])
            or _sha256(path) != str(expected["sha256"]).upper()
        ):
            raise FailClosed(
                "BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT",
                {"stage": "accepted_manifest_readback", "path": str(path)},
            )


def _load_accepted_checkpoint(
    repository: Path, inputs: BoundOptionAInputs
) -> dict[str, Any]:
    option_a = repository / OPTION_A_RELATIVE
    v1_q1 = repository / V1_Q1_RELATIVE
    q1_kfe = repository / Q1_KFE_RELATIVE
    arrays_path = option_a / "direct_step_arrays.npz"
    q1_path = v1_q1 / "q1_generator.npz"
    manifest_path = v1_q1 / "sealed_manifest.json"
    p1_path = q1_kfe / "stationary_mass_arrays.npz"
    if _sha256(arrays_path) != V1_ARTIFACT_SHA256:
        raise FailClosed("BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT", {"path": str(arrays_path)})
    if _sha256(q1_path) != Q1_SHA256:
        raise FailClosed("BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT", {"path": str(q1_path)})
    if _sha256(manifest_path) != Q1_MANIFEST_SHA256:
        raise FailClosed("BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT", {"path": str(manifest_path)})
    if _sha256(p1_path) != P1_G1_ARTIFACT_SHA256:
        raise FailClosed("BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT", {"path": str(p1_path)})
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if int(manifest["entry_count"]) != 808:
        raise FailClosed(
            "BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT",
            {"stage": "accepted_q1_manifest_entry_count"},
        )
    _verify_manifest_files(v1_q1, manifest)
    with np.load(arrays_path, allow_pickle=False) as loaded:
        v0 = np.array(loaded["v0"], dtype=float, copy=True, order="F")
        v1 = np.array(loaded["v1"], dtype=float, copy=True, order="F")
    if (
        v0.shape != SHAPE
        or v1.shape != SHAPE
        or not np.all(np.isfinite(v0))
        or not np.all(np.isfinite(v1))
        or _field_sha256(v0) != V0_FIELD_SHA256
        or _field_sha256(v1) != V1_FIELD_SHA256
    ):
        raise FailClosed(
            "BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT", {"stage": "accepted_v0_v1_identity"}
        )
    selected_rows: list[dict[str, Any]] = []
    for flat in range(N):
        receipt = json.loads((v1_q1 / f"cell_{flat:04d}.json").read_text(encoding="utf-8"))
        result = receipt.get("selector_result", {})
        if (
            int(receipt["flat_index_f_zero_based"]) != flat
            or result.get("outcome") != "SELECTED_ADMISSIBLE"
            or not isinstance(result.get("selected"), dict)
        ):
            raise FailClosed(
                "BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT",
                {"stage": "accepted_p1_receipt", "flat": flat},
            )
        selected_rows.append(result["selected"])
    policy_arrays = _policy_arrays(selected_rows)
    q1 = sparse.load_npz(q1_path)
    if getattr(q1, "format", None) != "csr" or q1.shape != (N, N):
        raise FailClosed(
            "BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT", {"stage": "accepted_q1_shape_format"}
        )
    core_blobs = {
        path: {
            "head": _git_blob(repository, "HEAD", path),
            "accepted": _git_blob(repository, ACCEPTED_OPTION_A_COMMIT, path),
        }
        for path in CORE_AUTHORITY_PATHS
    }
    if not all(row["head"] == row["accepted"] for row in core_blobs.values()):
        raise FailClosed(
            "BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT", {"stage": "core_authority_blob", "blobs": core_blobs}
        )
    if inputs.grid.shape != SHAPE or inputs.scalars["delta"] != DELTA:
        raise FailClosed(
            "BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT", {"stage": "grid_or_delta"}
        )
    return {
        "v0": v0,
        "v1": v1,
        "selected_rows": selected_rows,
        "policy_arrays": policy_arrays,
        "q1": sparse.csr_matrix(q1),
        "core_blobs": core_blobs,
        "paths": {
            "v1_artifact": str(arrays_path.relative_to(repository)),
            "q1": str(q1_path.relative_to(repository)),
            "q1_manifest": str(manifest_path.relative_to(repository)),
            "p1_g1": str(p1_path.relative_to(repository)),
        },
    }


def _verify_accepted_q1_kfe_reuse(repository: Path) -> dict[str, Any]:
    root = repository / Q1_KFE_RELATIVE
    manifest_path = root / "sealed_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    _verify_manifest_files(root, manifest)
    terminal = json.loads((root / "terminal_receipt.json").read_text(encoding="utf-8"))
    ledger = json.loads((root / "execution_ledger.json").read_text(encoding="utf-8"))
    mass = json.loads(
        (root / "stationarity_normalization_nonnegativity_receipt.json").read_text(
            encoding="utf-8"
        )
    )
    freeze = json.loads(
        (root / "post_execution_freeze_check.json").read_text(encoding="utf-8")
    )
    preflight = json.loads(
        (root / "preflight_binding_receipt.json").read_text(encoding="utf-8")
    )
    checks = {
        "terminal_pass": terminal.get("terminal")
        == "PASS__ACCEPTED_Q1_UNIQUE_SOURCE_FREE_NORMALIZED_NONNEGATIVE_INVARIANT_MASS",
        "mass_receipt_pass": mass.get("status") == "PASS",
        "mass_artifact_exact": mass.get("arrays_artifact", {}).get("sha256")
        == P1_G1_ARTIFACT_SHA256,
        "q1_exact": preflight.get("q1", {}).get("sha256") == Q1_SHA256,
        "one_dense_gesvd": ledger.get("dense_scipy_linalg_svd_gesvd") == 1,
        "one_normalized_candidate": ledger.get("normalized_stationary_candidates") == 1,
        "one_q_transpose_times_p": ledger.get("q1_transpose_times_p") == 1,
        "zero_retries": ledger.get("retries") == 0,
        "scientific_code_freeze_preserved": freeze.get(
            "matches_pre_execution_freeze"
        )
        is True,
    }
    if not all(checks.values()):
        raise FailClosed(
            "FAIL__HJB_CONVERGED__TERMINAL_TOPOLOGY_OR_KFE_GATE",
            {"checkpoint": 1, "stage": "accepted_q1_kfe_reuse", "checks": checks},
        )
    return {
        "status": "PASS",
        "accepted_manifest_sha256": _sha256(manifest_path),
        "accepted_manifest_entry_count": int(manifest["entry_count"]),
        "accepted_p1_g1_artifact_sha256": P1_G1_ARTIFACT_SHA256,
        "checks": checks,
        "new_kfe_calls": 0,
        "new_svd_calls": 0,
        "new_q_transpose_times_p_calls": 0,
    }


def _new_ledger() -> dict[str, Any]:
    return {
        "accepted_v1_artifact_loads": 0,
        "accepted_q1_loads": 0,
        "new_corrected_policy_maps": 0,
        "selector_evaluations": 0,
        "scalar_root_invocations": 0,
        "interior_z_root_invocations": 0,
        "d2_assemblies": 0,
        "direct_hjb_solves": 0,
        "ordinary_graph_scc_summaries": 0,
        "terminal_topology_gates": 0,
        "terminal_dense_gesvd": 0,
        "terminal_normalized_stationary_candidates": 0,
        "terminal_q_transpose_times_p": 0,
        "scientific_retries": 0,
        "solver_substitutions": 0,
        "damping_relaxation_adaptive_delta_continuation_calls": 0,
        "matlab_production_ge_irf_results_calls": 0,
    }


def _check_ledger(ledger: dict[str, Any]) -> None:
    ceilings = {
        "new_corrected_policy_maps": MAX_NEW_POLICY_MAPS,
        "selector_evaluations": MAX_SELECTOR_EVALUATIONS,
        "scalar_root_invocations": MAX_ROOT_INVOCATIONS,
        "interior_z_root_invocations": MAX_INTERIOR_Z_ROOT_INVOCATIONS,
        "d2_assemblies": MAX_NEW_POLICY_MAPS,
        "direct_hjb_solves": MAX_NEW_UPDATES,
        "terminal_dense_gesvd": 1,
        "terminal_normalized_stationary_candidates": 1,
        "terminal_q_transpose_times_p": 1,
    }
    breaches = {
        name: {"actual": int(ledger[name]), "ceiling": ceiling}
        for name, ceiling in ceilings.items()
        if int(ledger[name]) > ceiling
    }
    if breaches:
        raise FailClosed(
            "FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE",
            {"stage": "scientific_ledger_ceiling", "breaches": breaches},
        )


def _cell(
    inputs: BoundOptionAInputs,
    index: tuple[int, int, int],
    derivatives: Any,
    checkpoint: int,
    flat: int,
) -> CorrectedSelectorCell:
    i_b, i_a, i_z = index
    b = float(inputs.grid.b[i_b])
    a = float(inputs.grid.a[i_a])
    z = float(inputs.grid.z[i_z])
    return CorrectedSelectorCell(
        cell_id=f"v{checkpoint:03d}_f{flat:04d}_b{i_b:03d}_a{i_a:03d}_z{i_z:03d}",
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


def _map_checkpoint(
    repository: Path,
    output: Path,
    checkpoint: int,
    value: np.ndarray,
    inputs: BoundOptionAInputs,
    budget: SelectorBudget,
    ledger: dict[str, Any],
    pre_hashes: dict[str, str],
) -> tuple[list[dict[str, Any]], dict[str, np.ndarray], sparse.csr_matrix, dict[str, Any]]:
    directory = output / f"checkpoint_{checkpoint:03d}"
    directory.mkdir(parents=False, exist_ok=False)
    fields = raw_derivative_fields(value, inputs.grid)
    derivative_hashes = {
        name: _field_sha256(array)
        for name, array in asdict(fields).items()
    }
    _write_json(
        directory / "derivative_receipt.json",
        {
            "checkpoint": checkpoint,
            "value_sha256": _field_sha256(value),
            "shape": list(value.shape),
            "flatten_order": "F",
            "boundary_carrier_marker": "UNUSED_BOUNDARY_SLOT_DUPLICATES_INWARD_RAW_DERIVATIVE",
            "derivative_sha256": derivative_hashes,
        },
    )
    selected_rows: list[dict[str, Any]] = []
    ledger["new_corrected_policy_maps"] += 1
    for flat, index in enumerate(iter_f_order_indices(SHAPE)):
        derivatives, markers = boundary_cell_derivatives(fields, index, inputs.grid)
        cell = _cell(inputs, index, derivatives, checkpoint, flat)
        path = directory / f"cell_{flat:04d}.json"
        try:
            result = select_constrained_policy(cell, inputs.parameters, budget=budget)
            receipt = {
                "checkpoint": checkpoint,
                "flat_index_f_zero_based": flat,
                "index_b_a_z_zero_based": list(index),
                "selector_cell": asdict(cell),
                "boundary_adapter_markers": markers,
                "selector_result": asdict(result),
                "cumulative_budget": asdict(budget),
                "receipt_persistence_order": "DURABLE_BEFORE_NEXT_CELL_OR_D2",
            }
        except Exception as exc:
            _write_json(
                path,
                {
                    "checkpoint": checkpoint,
                    "flat_index_f_zero_based": flat,
                    "index_b_a_z_zero_based": list(index),
                    "selector_exception": {"type": type(exc).__name__, "message": str(exc)},
                    "cumulative_budget": asdict(budget),
                },
            )
            ledger.update(
                selector_evaluations=budget.selector_evaluations,
                scalar_root_invocations=budget.root_invocations,
                interior_z_root_invocations=budget.interior_z_root_invocations,
            )
            if "interior_a_switching_root_invocations" in ledger:
                ledger["interior_a_switching_root_invocations"] = (
                    budget.interior_a_switching_root_invocations
                )
            if "joint_switching_root_invocations" in ledger:
                ledger["joint_switching_root_invocations"] = (
                    budget.joint_switching_root_invocations
                )
            raise FailClosed(
                "FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE",
                {"checkpoint": checkpoint, "flat": flat, "stage": "selector_exception"},
            ) from exc
        _write_json(path, receipt)
        ledger.update(
            selector_evaluations=budget.selector_evaluations,
            scalar_root_invocations=budget.root_invocations,
            interior_z_root_invocations=budget.interior_z_root_invocations,
        )
        if "interior_a_switching_root_invocations" in ledger:
            ledger["interior_a_switching_root_invocations"] = (
                budget.interior_a_switching_root_invocations
            )
        if "joint_switching_root_invocations" in ledger:
            ledger["joint_switching_root_invocations"] = (
                budget.joint_switching_root_invocations
            )
        _check_ledger(ledger)
        if result.outcome != "SELECTED_ADMISSIBLE" or result.selected is None:
            raise FailClosed(
                "FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE",
                {
                    "checkpoint": checkpoint,
                    "flat": flat,
                    "stage": "selector_outcome",
                    "outcome": result.outcome,
                },
            )
        selected_rows.append(asdict(result.selected))
    if len(selected_rows) != N:
        raise FailClosed(
            "FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE",
            {"checkpoint": checkpoint, "stage": "incomplete_policy_map"},
        )
    policy_arrays = _policy_arrays(selected_rows)
    ledger["d2_assemblies"] += 1
    try:
        generator = assemble_consumed_drift_generator(
            inputs.grid,
            mu_b=policy_arrays["g_b"],
            mu_a=policy_arrays["g_a"],
            z_generator=inputs.z_generator,
        )
    except Exception as exc:
        _write_json(
            directory / "d2_receipt.json",
            {"status": "RAISED", "type": type(exc).__name__, "message": str(exc)},
        )
        raise FailClosed(
            "FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE",
            {"checkpoint": checkpoint, "stage": "d2_exception"},
        ) from exc
    coordinate = coordinate_action_receipt(
        generator.q, inputs.grid, policy_arrays["g_b"], policy_arrays["g_a"]
    )
    faces = [asdict(face) for face in generator.boundary.faces]
    checks = {
        "minimum_offdiagonal_nonnegative": generator.minimum_offdiagonal >= 0.0,
        "diagonal_construction_error_exact_zero": generator.diagonal_construction_error == 0.0,
        "q_one_within_prospective_bound": generator.max_abs_q_one <= generator.arithmetic_tolerance,
        "b_coordinate_within_prospective_bound": bool(coordinate["b"]["passes"]),
        "a_coordinate_within_prospective_bound": bool(coordinate["a"]["passes"]),
        "zero_tolerance_closed_faces_feasible": bool(generator.boundary.feasible),
        "zero_outward_face_count": all(row["outward_count"] == 0 for row in faces),
        "zero_outward_face_amount": all(row["max_outward"] == 0.0 for row in faces),
    }
    sparse.save_npz(directory / "q_generator.npz", generator.q)
    d2_receipt = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "minimum_offdiagonal": generator.minimum_offdiagonal,
        "diagonal_construction_error": generator.diagonal_construction_error,
        "max_abs_q_one": generator.max_abs_q_one,
        "arithmetic_tolerance": generator.arithmetic_tolerance,
        "coordinate_action": coordinate,
        "closed_face_summaries": faces,
        "q_identity": _sparse_identity(generator.q),
        "q_artifact": {
            "path": "q_generator.npz",
            "bytes": (directory / "q_generator.npz").stat().st_size,
            "sha256": _sha256(directory / "q_generator.npz"),
        },
    }
    _write_json(directory / "d2_receipt.json", d2_receipt)
    if not all(checks.values()):
        raise FailClosed(
            "FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE",
            {"checkpoint": checkpoint, "stage": "d2_legality"},
        )
    _check_ledger(ledger)
    if _scientific_code_hashes(repository) != pre_hashes:
        raise FailClosed(
            "BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT",
            {"checkpoint": checkpoint, "stage": "post_round_code_hash"},
        )
    return selected_rows, policy_arrays, generator.q, d2_receipt


def _seal_directory(directory: Path, schema: str) -> dict[str, Any]:
    entries = []
    for path in sorted(item for item in directory.iterdir() if item.name != "sealed_manifest.json"):
        if path.is_file():
            entries.append(
                {"path": path.name, "bytes": path.stat().st_size, "sha256": _sha256(path)}
            )
    document = {
        "schema": schema,
        "entry_count": len(entries),
        "total_bytes": sum(int(row["bytes"]) for row in entries),
        "entries": entries,
    }
    _write_json(directory / "sealed_manifest.json", document)
    return document


def _terminal_kfe(
    checkpoint: int,
    q: sparse.csr_matrix,
    q_one_bound: float,
    output: Path,
    ledger: dict[str, Any],
) -> dict[str, Any]:
    terminal = output / "terminal_kfe"
    terminal.mkdir(parents=False, exist_ok=False)
    ledger["terminal_topology_gates"] += 1
    topology = analyze_exact_positive_topology(q)
    _write_json(terminal / "topology_receipt.json", topology)
    if len(topology["closed_members"]) != 1:
        raise FailClosed(
            "FAIL__HJB_CONVERGED__TERMINAL_TOPOLOGY_OR_KFE_GATE",
            {
                "checkpoint": checkpoint,
                "stage": "closed_communicating_classes",
                "closed_members": topology["closed_members"],
            },
        )
    q_one = np.asarray(q @ np.ones(N, dtype=float)).ravel()
    if not np.all(np.isfinite(q.data)) or float(np.max(np.abs(q_one), initial=0.0)) > q_one_bound:
        raise FailClosed(
            "FAIL__HJB_CONVERGED__TERMINAL_TOPOLOGY_OR_KFE_GATE",
            {"checkpoint": checkpoint, "stage": "terminal_q_structure"},
        )
    a = q.transpose().tocsr()
    ledger["terminal_dense_gesvd"] += 1
    try:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            _u, singular_values, vh = linalg.svd(
                a.toarray(), full_matrices=True, lapack_driver="gesvd", check_finite=True
            )
    except Exception as exc:
        raise FailClosed(
            "FAIL__HJB_CONVERGED__TERMINAL_TOPOLOGY_OR_KFE_GATE",
            {"checkpoint": checkpoint, "stage": "svd_exception", "type": type(exc).__name__, "message": str(exc)},
        ) from exc
    warning_rows = [
        {"category": row.category.__name__, "message": str(row.message)} for row in caught
    ]
    rank = rank_receipt(singular_values)
    rank.update(
        {
            "solver": "scipy.linalg.svd",
            "lapack_driver": "gesvd",
            "warnings": warning_rows,
            "status": "PASS",
        }
    )
    if (
        warning_rows
        or rank["numerical_rank"] != 799
        or rank["numerical_nullity"] != 1
        or not rank["second_smallest_strictly_above_tau_rank"]
    ):
        rank["status"] = "FAIL"
        _write_json(terminal / "svd_rank_nullity_receipt.json", rank)
        raise FailClosed(
            "FAIL__HJB_CONVERGED__TERMINAL_TOPOLOGY_OR_KFE_GATE",
            {"checkpoint": checkpoint, "stage": "svd_rank_nullity"},
        )
    _write_json(terminal / "svd_rank_nullity_receipt.json", rank)
    ledger["terminal_normalized_stationary_candidates"] += 1
    p, orientation = normalize_null_vector(vh[-1, :])
    g = p / OMEGA
    ledger["terminal_q_transpose_times_p"] += 1
    residual = np.asarray(a @ p).ravel()
    a_inf = float(np.max(np.asarray(abs(a).sum(axis=1)).ravel(), initial=0.0))
    p_inf = float(np.linalg.norm(p, ord=np.inf))
    p_l1 = math.fsum(abs(float(value)) for value in p)
    residual_inf = float(np.linalg.norm(residual, ord=np.inf))
    scale = max(1.0, a_inf * p_inf)
    backward_ratio = residual_inf / scale
    tau_stationarity = gamma(N + 64) * scale
    residual_sum = math.fsum(float(value) for value in residual)
    q_one_dot_p = float(np.dot(q_one, p))
    source_discrepancy = abs(residual_sum - q_one_dot_p)
    source_bound = gamma(N + 64) * max(1.0, N * a_inf * p_inf)
    p_sum = math.fsum(float(value) for value in p)
    p_normalization_bound = gamma(N) * max(1.0, p_l1)
    weighted_density_sum = OMEGA * math.fsum(float(value) for value in g)
    grouped_density_bound = gamma(N + 2) * max(
        1.0, OMEGA * math.fsum(abs(float(value)) for value in g)
    )
    tau_nonnegative = gamma(N + 64) * max(1.0, p_inf)
    negative = [max(-float(value), 0.0) for value in p]
    checks = {
        "arrays_finite": bool(np.all(np.isfinite(p)) and np.all(np.isfinite(g)) and np.all(np.isfinite(residual))),
        "stationarity_inf_within_bound": residual_inf <= tau_stationarity,
        "normwise_backward_ratio_within_gamma_864": backward_ratio <= gamma(N + 64),
        "residual_sum_within_global_source_bound": abs(residual_sum) <= source_bound,
        "q_one_dot_p_within_global_source_bound": abs(q_one_dot_p) <= source_bound,
        "source_identity_discrepancy_within_bound": source_discrepancy <= source_bound,
        "probability_mass_normalized": abs(p_sum - 1.0) <= p_normalization_bound,
        "density_volume_normalized": abs(weighted_density_sum - 1.0) <= grouped_density_bound,
        "minimum_mass_within_allowance": float(np.min(p)) >= -tau_nonnegative,
        "total_negative_mass_within_allowance": math.fsum(negative) <= N * tau_nonnegative,
        "no_clipping": True,
        "no_retry": True,
    }
    receipt = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checkpoint": checkpoint,
        "checks": checks,
        "orientation_and_normalization": orientation,
        "stationarity": {
            "residual_inf": residual_inf,
            "tau_stationarity": tau_stationarity,
            "normwise_backward_ratio": backward_ratio,
            "gamma_864": gamma(N + 64),
            "math_fsum_residual": residual_sum,
            "dot_q_one_p": q_one_dot_p,
            "source_identity_discrepancy": source_discrepancy,
            "source_bound": source_bound,
        },
        "normalization": {
            "math_fsum_p": p_sum,
            "omega_times_math_fsum_g": weighted_density_sum,
            "probability_mass_bound": p_normalization_bound,
            "grouped_density_bound": grouped_density_bound,
        },
        "nonnegativity": {
            "minimum_p": float(np.min(p)),
            "negative_entry_count": int(sum(value > 0 for value in negative)),
            "total_negative_mass": math.fsum(negative),
            "tau_nonnegative": tau_nonnegative,
            "total_negative_mass_bound": N * tau_nonnegative,
        },
    }
    np.savez_compressed(
        terminal / "stationary_mass_arrays.npz",
        p=p,
        g=g,
        residual=residual,
        q_times_one=q_one,
        singular_values=singular_values,
    )
    receipt["arrays_artifact"] = {
        "path": "stationary_mass_arrays.npz",
        "bytes": (terminal / "stationary_mass_arrays.npz").stat().st_size,
        "sha256": _sha256(terminal / "stationary_mass_arrays.npz"),
        "p_sha256": _field_sha256(p),
        "g_sha256": _field_sha256(g),
        "residual_sha256": _field_sha256(residual),
    }
    _write_json(terminal / "stationarity_normalization_nonnegativity_receipt.json", receipt)
    if not all(checks.values()):
        raise FailClosed(
            "FAIL__HJB_CONVERGED__TERMINAL_TOPOLOGY_OR_KFE_GATE",
            {"checkpoint": checkpoint, "stage": "stationary_mass"},
        )
    _seal_directory(terminal, "CH5_D123_BOUNDED_CONTINUATION_TERMINAL_KFE_V1")
    return receipt


def _write_root_manifest(output: Path) -> None:
    entries = []
    for path in sorted(output.rglob("*")):
        if path.is_file() and path != output / "sealed_manifest.json":
            entries.append(
                {
                    "path": path.relative_to(output).as_posix(),
                    "bytes": path.stat().st_size,
                    "sha256": _sha256(path),
                }
            )
    _write_json(
        output / "sealed_manifest.json",
        {
            "schema": "CH5_D123_BOUNDED_NONLINEAR_HJB_KFE_CONTINUATION_V1",
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
    if post_hashes != pre_hashes and terminal.startswith("PASS__"):
        terminal = "BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT"
        detail = {"stage": "post_execution_scientific_code_hash", "prior_detail": detail}
    ledger["terminal_verdict"] = terminal
    ledger["wall_seconds"] = float(time.perf_counter() - started)
    _write_json(output / "scientific_ledger.json", ledger)
    _write_json(
        output / "post_execution_code_freeze.json",
        {
            "scientific_code_sha256_after": post_hashes,
            "matches_pre_execution_freeze": post_hashes == pre_hashes,
        },
    )
    _write_json(
        output / "terminal_receipt.json",
        {"terminal_verdict": terminal, "detail": detail},
    )
    _write_root_manifest(output)
    return terminal


def execute(repository: Path, seed_path: Path, binding_path: Path) -> str:
    repository = repository.resolve(strict=True)
    output = repository / OUTPUT_RELATIVE
    output.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    ledger = _new_ledger()
    pre_hashes = _scientific_code_hashes(repository)
    baseline = _git_head(repository)
    _write_json(
        output / "startup_manifest.json",
        {
            "task_id": "CH5_MP4C_2018_KFE_D123_BOUNDED_NONLINEAR_HJB_KFE_CONTINUATION_20260917",
            "baseline_sha": baseline,
            "authority_id": AUTHORITY_ID,
            "convergence_law": {
                "bellman_residual_inclusive": BELLMAN_TOLERANCE,
                "value_change_inclusive": VALUE_TOLERANCE,
                "both_required_same_checkpoint": True,
                "policy_operator_stability": "DIAGNOSTIC_ONLY",
                "direct_solve_backward_error_inclusive": BACKWARD_ERROR_TOLERANCE,
                "approximate_cycle_periods": [2, 3],
                "approximate_cycle_inclusive": CYCLE_TOLERANCE,
                "delta": DELTA,
                "total_update_ceiling": MAX_TOTAL_UPDATES,
                "already_consumed_updates": 1,
            },
            "scientific_code_sha256_before": pre_hashes,
            "input_receipt_planned": {
                "seed_path": str(seed_path),
                "binding_path": str(binding_path),
            },
        },
    )
    try:
        inputs = bind_option_a_inputs(seed_path, binding_path)
        accepted = _load_accepted_checkpoint(repository, inputs)
        ledger["accepted_v1_artifact_loads"] = 1
        ledger["accepted_q1_loads"] = 1
        _write_json(
            output / "accepted_checkpoint_1_binding.json",
            {
                "status": "PASS",
                "input_identity": _input_receipt(inputs),
                "accepted_paths": accepted["paths"],
                "accepted_hashes": {
                    "v0_field": _field_sha256(accepted["v0"]),
                    "v1_field": _field_sha256(accepted["v1"]),
                    "v1_artifact": V1_ARTIFACT_SHA256,
                    "q1": Q1_SHA256,
                    "q1_manifest": Q1_MANIFEST_SHA256,
                    "p1_g1": P1_G1_ARTIFACT_SHA256,
                },
                "accepted_policy_receipts": 800,
                "core_authority_blobs": accepted["core_blobs"],
                "v1_policy_map_rerun": False,
            },
        )
        values = [accepted["v0"], accepted["v1"]]
        previous_rows = accepted["selected_rows"]
        previous_arrays = accepted["policy_arrays"]
        previous_q = accepted["q1"]
        identities: list[str] = []
        final_checkpoint = 1
        final_metrics: dict[str, Any] = {}
        checkpoint = 1
        current_value = accepted["v1"]
        current_rows = previous_rows
        current_arrays = previous_arrays
        current_q = previous_q
        current_d2_bound = float(
            json.loads(
                (repository / V1_Q1_RELATIVE / "q1_d2_receipt.json").read_text(encoding="utf-8")
            )["arithmetic_tolerance"]
        )
        budget = SelectorBudget(
            max_selector_evaluations=MAX_SELECTOR_EVALUATIONS,
            max_root_invocations=MAX_ROOT_INVOCATIONS,
            max_interior_z_root_invocations=MAX_INTERIOR_Z_ROOT_INVOCATIONS,
        )
        while True:
            directory = output / f"checkpoint_{checkpoint:03d}"
            if checkpoint == 1:
                directory.mkdir(parents=False, exist_ok=False)
                policy_identity_sha = _canonical_sha256(
                    [_selected_identity(row) for row in current_rows]
                )
                policy_diagnostics = {
                    "identity_sha256": policy_identity_sha,
                    "identity_change_count": None,
                    "identity_change_flat_f_zero_based": [],
                    "source": "ACCEPTED_P1_RECEIPTS_REUSED_WITHOUT_POLICY_MAP_RERUN",
                }
                operator_diagnostics = {
                    "identity": _sparse_identity(current_q),
                    "nnz": int(current_q.nnz),
                    "sparsity_pattern_same_as_previous": None,
                    "source": "ACCEPTED_Q1_REUSED",
                }
                _write_json(directory / "accepted_source_receipt.json", {
                    "p1_u1_q1_reused": True,
                    "v1_policy_map_rerun": False,
                    "accepted_q1_sha256": Q1_SHA256,
                    "accepted_q1_manifest_sha256": Q1_MANIFEST_SHA256,
                })
            else:
                current_rows, current_arrays, current_q, d2_receipt = _map_checkpoint(
                    repository,
                    output,
                    checkpoint,
                    current_value,
                    inputs,
                    budget,
                    ledger,
                    pre_hashes,
                )
                current_d2_bound = float(d2_receipt["arithmetic_tolerance"])
                policy_diagnostics = _policy_diagnostics(
                    current_rows, previous_rows, current_arrays, previous_arrays
                )
                policy_identity_sha = str(policy_diagnostics["identity_sha256"])
                operator_diagnostics = _operator_diagnostics(current_q, previous_q)
            bellman = (
                inputs.scalars["rho"] * current_value.ravel(order="F")
                - current_arrays["utility"].ravel(order="F")
                - np.asarray(current_q @ current_value.ravel(order="F")).ravel()
            )
            if not np.all(np.isfinite(bellman)):
                raise FailClosed(
                    "FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE",
                    {"checkpoint": checkpoint, "stage": "bellman_nonfinite"},
                )
            value_change_field = current_value - values[-2]
            bellman_inf = float(np.linalg.norm(bellman, ord=np.inf))
            value_change_inf = float(
                np.linalg.norm(value_change_field.ravel(order="F"), ord=np.inf)
            )
            q_identity = _sparse_identity(current_q)
            identity = checkpoint_identity(
                _field_sha256(current_value), policy_identity_sha, q_identity
            )
            identities.append(identity)
            converged = primary_converged(bellman_inf, value_change_inf)
            metrics = {
                "checkpoint": checkpoint,
                "value_sha256": _field_sha256(current_value),
                "policy_identity_sha256": policy_identity_sha,
                "q_identity": q_identity,
                "checkpoint_identity_sha256": identity,
                "bellman_residual_inf": bellman_inf,
                "bellman_threshold_inclusive": BELLMAN_TOLERANCE,
                "value_change_inf": value_change_inf,
                "value_change_threshold_inclusive": VALUE_TOLERANCE,
                "primary_convergence_pass": converged,
                "policy_diagnostics": policy_diagnostics,
                "operator_diagnostics": operator_diagnostics,
                "cumulative_scientific_ledger": dict(ledger),
            }
            np.savez_compressed(
                directory / "checkpoint_arrays.npz",
                value=current_value,
                utility=current_arrays["utility"],
                mu_b=current_arrays["g_b"],
                mu_a=current_arrays["g_a"],
                bellman_residual=bellman,
                value_change=value_change_field,
            )
            metrics["checkpoint_arrays"] = {
                "path": "checkpoint_arrays.npz",
                "bytes": (directory / "checkpoint_arrays.npz").stat().st_size,
                "sha256": _sha256(directory / "checkpoint_arrays.npz"),
                "bellman_residual_sha256": _field_sha256(bellman),
                "value_change_sha256": _field_sha256(value_change_field),
            }
            final_checkpoint = checkpoint
            final_metrics = metrics
            if converged:
                metrics["disposition"] = "HJB_CONVERGED__NO_FURTHER_UPDATE"
                _write_json(directory / "checkpoint_manifest.json", metrics)
                _seal_directory(directory, "CH5_D123_BOUNDED_CONTINUATION_CHECKPOINT_V1")
                if checkpoint == 1:
                    reuse = _verify_accepted_q1_kfe_reuse(repository)
                    reuse["same_q_identity_proven"] = (
                        _sha256(repository / V1_Q1_RELATIVE / "q1_generator.npz")
                        == Q1_SHA256
                    )
                    _write_json(
                        output / "terminal_kfe_reuse_receipt.json",
                        {"checkpoint": 1, **reuse},
                    )
                else:
                    terminal_receipt = _terminal_kfe(
                        checkpoint, current_q, current_d2_bound, output, ledger
                    )
                    final_metrics["terminal_kfe"] = terminal_receipt
                terminal = (
                    "PASS__CORRECTED_HJB_CONVERGED__TERMINAL_SOURCE_FREE_KFE_PASS__"
                    "CONDITIONAL_HOUSEHOLD_FIXED_POINT_ESTABLISHED"
                )
                return _finalize(
                    repository,
                    output,
                    pre_hashes,
                    ledger,
                    terminal,
                    {"final_checkpoint": final_checkpoint, "terminal_metrics": final_metrics},
                    started,
                )
            exact_period = detect_exact_cycle(identities)
            approximate = detect_approximate_cycle(values, tolerance=CYCLE_TOLERANCE)
            cycle_receipt = {
                "checkpoint": checkpoint,
                "primary_convergence_failed_first": True,
                "exact_compared_checkpoint_indices": list(range(1, checkpoint)),
                "exact_period": exact_period,
                "approximate_period_2_or_3": approximate,
            }
            _write_json(directory / "cycle_detection_receipt.json", cycle_receipt)
            if exact_period is not None:
                metrics["disposition"] = "EXACT_CYCLE"
                _write_json(directory / "checkpoint_manifest.json", metrics)
                _seal_directory(directory, "CH5_D123_BOUNDED_CONTINUATION_CHECKPOINT_V1")
                raise FailClosed(
                    "FAIL__CORRECTED_HJB_EXACT_CYCLE",
                    {"final_checkpoint": checkpoint, "period": exact_period, "terminal_metrics": metrics},
                )
            if approximate is not None:
                period = int(approximate["period"])
                metrics["disposition"] = f"APPROXIMATE_PERIOD_{period}_CYCLE"
                _write_json(directory / "checkpoint_manifest.json", metrics)
                _seal_directory(directory, "CH5_D123_BOUNDED_CONTINUATION_CHECKPOINT_V1")
                raise FailClosed(
                    f"FAIL__CORRECTED_HJB_APPROXIMATE_PERIOD_{period}_CYCLE",
                    {"final_checkpoint": checkpoint, "cycle": approximate, "terminal_metrics": metrics},
                )
            if checkpoint >= MAX_TOTAL_UPDATES:
                metrics["disposition"] = "UPDATE_CEILING_REACHED_WITHOUT_CONVERGENCE"
                _write_json(directory / "checkpoint_manifest.json", metrics)
                _seal_directory(directory, "CH5_D123_BOUNDED_CONTINUATION_CHECKPOINT_V1")
                raise FailClosed(
                    "FAIL__CORRECTED_HJB_UPDATE_CEILING_REACHED_WITHOUT_CONVERGENCE",
                    {"final_checkpoint": checkpoint, "terminal_metrics": metrics},
                )
            matrix = (
                (inputs.scalars["rho"] + 1.0 / DELTA)
                * sparse.eye(N, format="csr")
                - current_q
            )
            rhs = current_arrays["utility"].ravel(order="F") + current_value.ravel(order="F") / DELTA
            ledger["direct_hjb_solves"] += 1
            _check_ledger(ledger)
            try:
                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    next_flat = np.asarray(sparse_linalg.spsolve(matrix, rhs), dtype=float)
            except Exception as exc:
                _write_json(
                    directory / "direct_solve_receipt.json",
                    {
                        "status": "RAISED",
                        "type": type(exc).__name__,
                        "message": str(exc),
                    },
                )
                raise FailClosed(
                    "FAIL__CORRECTED_HJB_LINEAR_SOLVE_ACCURACY_GATE",
                    {"checkpoint": checkpoint, "stage": "direct_solve_exception"},
                ) from exc
            warning_rows = [
                {"category": row.category.__name__, "message": str(row.message)} for row in caught
            ]
            if warning_rows or next_flat.shape != (N,) or not np.all(np.isfinite(next_flat)):
                _write_json(
                    directory / "direct_solve_receipt.json",
                    {
                        "status": "FAIL",
                        "warnings": warning_rows,
                        "shape": list(next_flat.shape),
                        "finite": bool(np.all(np.isfinite(next_flat))),
                    },
                )
                raise FailClosed(
                    "FAIL__CORRECTED_HJB_LINEAR_SOLVE_ACCURACY_GATE",
                    {"checkpoint": checkpoint, "stage": "solve_warning_shape_or_finite"},
                )
            backward = normwise_backward_error(matrix, next_flat, rhs)
            residual = backward.pop("residual")
            next_value = next_flat.reshape(SHAPE, order="F")
            solve_pass = bool(
                np.isfinite(backward["normwise_backward_error"])
                and backward["normwise_backward_error"] <= BACKWARD_ERROR_TOLERANCE
            )
            np.savez_compressed(
                directory / "direct_update_arrays.npz",
                matrix_data=matrix.data,
                matrix_indices=matrix.indices,
                matrix_indptr=matrix.indptr,
                rhs=rhs,
                next_value=next_value,
                residual=residual,
            )
            solve_receipt = {
                "status": "PASS" if solve_pass else "FAIL",
                "solver": "scipy.sparse.linalg.spsolve",
                "checkpoint_from": checkpoint,
                "checkpoint_to": checkpoint + 1,
                "delta": DELTA,
                "warnings": warning_rows,
                **backward,
                "backward_error_threshold_inclusive": BACKWARD_ERROR_TOLERANCE,
                "matrix_identity": _sparse_identity(matrix),
                "rhs_sha256": _field_sha256(rhs),
                "next_value_sha256": _field_sha256(next_value),
                "residual_sha256": _field_sha256(residual),
                "arrays_artifact": {
                    "path": "direct_update_arrays.npz",
                    "bytes": (directory / "direct_update_arrays.npz").stat().st_size,
                    "sha256": _sha256(directory / "direct_update_arrays.npz"),
                },
            }
            _write_json(directory / "direct_solve_receipt.json", solve_receipt)
            if not solve_pass:
                metrics["disposition"] = "LINEAR_SOLVE_ACCURACY_GATE_FAIL"
                _write_json(directory / "checkpoint_manifest.json", metrics)
                _seal_directory(directory, "CH5_D123_BOUNDED_CONTINUATION_CHECKPOINT_V1")
                raise FailClosed(
                    "FAIL__CORRECTED_HJB_LINEAR_SOLVE_ACCURACY_GATE",
                    {"final_checkpoint": checkpoint, "direct_solve": solve_receipt, "terminal_metrics": metrics},
                )
            metrics["disposition"] = "CONTINUE_TO_NEXT_CHECKPOINT"
            metrics["direct_solve"] = solve_receipt
            _write_json(directory / "checkpoint_manifest.json", metrics)
            _seal_directory(directory, "CH5_D123_BOUNDED_CONTINUATION_CHECKPOINT_V1")
            if _scientific_code_hashes(repository) != pre_hashes:
                raise FailClosed(
                    "BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT",
                    {"checkpoint": checkpoint, "stage": "post_update_code_hash"},
                )
            previous_rows = current_rows
            previous_arrays = current_arrays
            previous_q = current_q
            current_value = next_value
            values.append(current_value)
            checkpoint += 1
    except FailClosed as failure:
        return _finalize(
            repository,
            output,
            pre_hashes,
            ledger,
            failure.terminal,
            failure.detail,
            started,
        )
    except Exception as exc:
        return _finalize(
            repository,
            output,
            pre_hashes,
            ledger,
            "BLOCKED__PROVENANCE_OR_AUTHORITY_DRIFT",
            {"stage": "unhandled_exception", "type": type(exc).__name__, "message": str(exc)},
            started,
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--seed", type=Path, required=True)
    parser.add_argument("--binding", type=Path, required=True)
    args = parser.parse_args(argv)
    terminal = execute(args.repository, args.seed, args.binding)
    print(terminal)
    return 0 if terminal.startswith("PASS__") else 2


if __name__ == "__main__":
    sys.exit(main())
