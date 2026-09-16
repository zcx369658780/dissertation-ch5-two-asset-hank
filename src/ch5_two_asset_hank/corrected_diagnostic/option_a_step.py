"""One-shot Option A corrected policy map and direct HJB step.

This module is isolated from the source-faithful and production household paths.
It binds the Owner-selected call-725 seed and stops at the first failed cell.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from decimal import Decimal
import hashlib
import inspect
import json
from pathlib import Path
import subprocess
import sys
from typing import Any, Iterator
import warnings

import numpy as np
from scipy import sparse
from scipy.io import loadmat
from scipy.sparse import linalg as sparse_linalg
from scipy.sparse.linalg import MatrixRankWarning

from .contracts import AUTHORITY_ID, CorrectedDiagnosticGrid
from .generator import CorrectedGenerator, assemble_consumed_drift_generator
from .selector import (
    CellDerivatives,
    CorrectedSelectorCell,
    CorrectedSelectorParameters,
    SelectorBudget,
    select_constrained_policy,
)


EVIDENCE_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_lower_a_zero_kink_option_a_reexecution_20260916"
)
BOUNDARY_ADAPTER_MARKER = "UNUSED_BOUNDARY_SLOT_DUPLICATES_INWARD_RAW_DERIVATIVE"
EXPECTED_BINDING_SHA256 = "A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6"
EXPECTED_SEED_SHA256 = "1718984CB588AE586F74AB8476C57AF849BB2C80CC95500329D29BC14207BB81"
EXPECTED_V0_FIELD_SHA256 = "564B95B818713477691389903C3CFF72B5A7F991B924D52FBEB23D5A3675D665"
EXPECTED_GRID_FIELD_SHA256 = {
    "b": "A3FF663C18A2088A75B0E76C8ADA982EAF6D33ACFECB8DAA17C6D7DDE0533A76",
    "a": "AE3A3A789FBC0DC9900B8153DEC717264C74AAB6FDA356C21C0EB22EEAC52567",
    "z": "A35F6FAB6E4564C6F4B1962A2ADE64E477F808432F747ABC7ACCF5E70B0B39B7",
}
FIXED_COORDINATE_ROW_TERMS = 4


@dataclass(frozen=True)
class RawDerivativeFields:
    p_b_backward: np.ndarray
    p_b_forward: np.ndarray
    p_a_backward: np.ndarray
    p_a_forward: np.ndarray


@dataclass(frozen=True)
class BoundOptionAInputs:
    seed_path: Path
    seed_sha256: str
    seed_bytes: int
    v0_field_sha256: str
    binding_path: Path
    binding_sha256: str
    binding_bytes: int
    grid: CorrectedDiagnosticGrid
    v0: np.ndarray
    parameters: CorrectedSelectorParameters
    scalars: dict[str, float]
    z_generator: np.ndarray


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def _field_sha256(values: np.ndarray) -> str:
    encoded = np.asarray(values, dtype="<f8").tobytes(order="F")
    return hashlib.sha256(encoded).hexdigest().upper()


def _write_json(path: Path, value: Any) -> None:
    text = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text + "\n", encoding="utf-8")
    temporary.replace(path)


def _git_head(repository: Path) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repository, text=True
    ).strip()


def iter_f_order_indices(shape: tuple[int, int, int]) -> Iterator[tuple[int, int, int]]:
    for flat_index in range(int(np.prod(shape))):
        yield tuple(map(int, np.unravel_index(flat_index, shape, order="F")))


def raw_derivative_fields(
    value: np.ndarray, grid: CorrectedDiagnosticGrid
) -> RawDerivativeFields:
    v = np.asarray(value, dtype=float)
    if v.shape != grid.shape or not np.all(np.isfinite(v)):
        raise ValueError("value must be a finite tensor matching the corrected grid")

    p_b_forward = np.empty_like(v)
    p_b_backward = np.empty_like(v)
    b_spacing = np.diff(grid.b)[:, None, None]
    b_slopes = (v[1:, :, :] - v[:-1, :, :]) / b_spacing
    p_b_forward[:-1, :, :] = b_slopes
    p_b_backward[1:, :, :] = b_slopes
    p_b_backward[0, :, :] = p_b_forward[0, :, :]
    p_b_forward[-1, :, :] = p_b_backward[-1, :, :]

    p_a_forward = np.empty_like(v)
    p_a_backward = np.empty_like(v)
    a_spacing = np.diff(grid.a)[None, :, None]
    a_slopes = (v[:, 1:, :] - v[:, :-1, :]) / a_spacing
    p_a_forward[:, :-1, :] = a_slopes
    p_a_backward[:, 1:, :] = a_slopes
    p_a_backward[:, 0, :] = p_a_forward[:, 0, :]
    p_a_forward[:, -1, :] = p_a_backward[:, -1, :]

    fields = RawDerivativeFields(
        p_b_backward=p_b_backward,
        p_b_forward=p_b_forward,
        p_a_backward=p_a_backward,
        p_a_forward=p_a_forward,
    )
    if not all(np.all(np.isfinite(array)) for array in asdict(fields).values()):
        raise ValueError("raw Option A derivatives are not finite")
    return fields


def boundary_cell_derivatives(
    fields: RawDerivativeFields,
    index: tuple[int, int, int],
    grid: CorrectedDiagnosticGrid,
) -> tuple[CellDerivatives, dict[str, str]]:
    i_b, i_a, _ = index
    markers: dict[str, str] = {}
    p_b_backward = float(fields.p_b_backward[index])
    p_b_forward = float(fields.p_b_forward[index])
    p_a_backward = float(fields.p_a_backward[index])
    p_a_forward = float(fields.p_a_forward[index])
    if i_b == 0:
        p_b_backward = p_b_forward
        markers["b"] = BOUNDARY_ADAPTER_MARKER
    elif i_b == grid.b.size - 1:
        p_b_forward = p_b_backward
        markers["b"] = BOUNDARY_ADAPTER_MARKER
    if i_a == 0:
        p_a_backward = p_a_forward
        markers["a"] = BOUNDARY_ADAPTER_MARKER
    elif i_a == grid.a.size - 1:
        p_a_forward = p_a_backward
        markers["a"] = BOUNDARY_ADAPTER_MARKER
    return (
        CellDerivatives(
            p_b_backward=p_b_backward,
            p_b_forward=p_b_forward,
            p_a_backward=p_a_backward,
            p_a_forward=p_a_forward,
        ),
        markers,
    )


def bind_option_a_inputs(seed_path: Path, binding_path: Path) -> BoundOptionAInputs:
    seed_path = seed_path.resolve(strict=True)
    binding_path = binding_path.resolve(strict=True)
    seed_hash = _sha256(seed_path)
    binding_hash = _sha256(binding_path)
    if seed_hash != EXPECTED_SEED_SHA256:
        raise ValueError("Option A seed container identity mismatch")
    if binding_hash != EXPECTED_BINDING_SHA256:
        raise ValueError("call-725 scalar binding identity mismatch")

    binding = json.loads(binding_path.read_text(encoding="utf-8"))
    if str(binding["mat_authority"]["path"]) != str(seed_path):
        raise ValueError("scalar binding does not point to the supplied Option A seed")
    if str(binding["mat_authority"]["sha256"]).upper() != seed_hash:
        raise ValueError("scalar binding seed hash disagrees with readback")
    document = loadmat(seed_path, squeeze_me=True, struct_as_record=False)
    required = tuple(binding["mat_authority"]["required_direct_load_fields"])
    if required != ("b", "ah", "z", "v0", "l0"):
        raise ValueError("Option A direct-load field contract changed")
    grid = CorrectedDiagnosticGrid(
        b=np.asarray(document["b"], dtype=float),
        a=np.asarray(document["ah"], dtype=float),
        z=np.asarray(document["z"], dtype=float),
    )
    if grid.shape != (20, 20, 2):
        raise ValueError("Option A grid shape changed")
    grid_hashes = {
        "b": _field_sha256(grid.b),
        "a": _field_sha256(grid.a),
        "z": _field_sha256(grid.z),
    }
    if grid_hashes != EXPECTED_GRID_FIELD_SHA256:
        raise ValueError("Option A grid identity mismatch")
    v0 = np.asarray(document["v0"], dtype=float)
    if v0.shape != grid.shape or not np.all(np.isfinite(v0)):
        raise ValueError("Option A v0 shape or finite contract failed")
    v0_hash = _field_sha256(v0)
    if v0_hash != EXPECTED_V0_FIELD_SHA256:
        raise ValueError("Option A v0 field identity mismatch")

    scalar = binding["scalar_binding"]
    p = scalar["parameters"]
    n = scalar["numerics"]
    expected_scalars = {
        "r_a": 0.09,
        "r_b": 0.02,
        "borrowing_rate_gap": 0.07,
        "tau": 0.05,
        "wage": 16.82014806560587,
        "transfer_income": 0.1,
        "rho": 0.05,
        "gamma_c": 2.0,
        "phi": 5.0,
        "chi_0": 0.1,
        "chi_1": 2.0,
        "a_bar": 1.0e-6,
        "labor_weight": 1.0,
        "delta": 1000.0,
    }
    scalars = {name: float(p[name]) for name in expected_scalars if name in p}
    scalars["delta"] = float(n["delta"])
    if scalars != expected_scalars:
        raise ValueError("call-725 frozen scalar values changed")
    z_generator = np.asarray(scalar["switch_matrix"], dtype=float)
    expected_z = np.array([[-1.0 / 3.0, 1.0 / 3.0], [1.0 / 3.0, -1.0 / 3.0]])
    if z_generator.shape != (2, 2) or not np.array_equal(z_generator, expected_z):
        raise ValueError("call-725 productivity generator changed")
    parameters = CorrectedSelectorParameters(
        gamma_c=scalars["gamma_c"],
        phi=scalars["phi"],
        labor_weight=scalars["labor_weight"],
        chi_0=scalars["chi_0"],
        chi_1=scalars["chi_1"],
        a_bar=scalars["a_bar"],
    )
    return BoundOptionAInputs(
        seed_path=seed_path,
        seed_sha256=seed_hash,
        seed_bytes=seed_path.stat().st_size,
        v0_field_sha256=v0_hash,
        binding_path=binding_path,
        binding_sha256=binding_hash,
        binding_bytes=binding_path.stat().st_size,
        grid=grid,
        v0=v0,
        parameters=parameters,
        scalars=scalars,
        z_generator=z_generator,
    )


def _spacing_representation_error(
    grid: CorrectedDiagnosticGrid, drift: np.ndarray, axis: int
) -> np.ndarray:
    result = np.zeros(grid.shape, dtype=float)
    nodes = grid.b if axis == 0 else grid.a
    for index in iter_f_order_indices(grid.shape):
        value = float(drift[index])
        if value == 0.0:
            continue
        coordinate = index[axis]
        neighbor = coordinate + 1 if value > 0.0 else coordinate - 1
        distance = float(abs(nodes[neighbor] - nodes[coordinate]))
        rate = float(abs(value) / distance)
        exact_reconstructed = Decimal.from_float(rate) * (
            Decimal.from_float(nodes[neighbor]) - Decimal.from_float(nodes[coordinate])
        )
        if value < 0.0:
            exact_reconstructed = -exact_reconstructed
        error = abs(exact_reconstructed - Decimal.from_float(value))
        result[index] = np.nextafter(float(error), np.inf) if error else 0.0
    return result


def coordinate_action_receipt(
    q: sparse.csr_matrix,
    grid: CorrectedDiagnosticGrid,
    mu_b: np.ndarray,
    mu_a: np.ndarray,
) -> dict[str, Any]:
    matrix = sparse.csr_matrix(q)
    eps = np.finfo(float).eps
    gamma = FIXED_COORDINATE_ROW_TERMS * eps / (
        1.0 - FIXED_COORDINATE_ROW_TERMS * eps
    )
    receipt: dict[str, Any] = {
        "fixed_pre_outcome_max_row_terms": FIXED_COORDINATE_ROW_TERMS,
        "gamma_n": float(gamma),
    }
    coordinates = {
        "b": np.broadcast_to(grid.b[:, None, None], grid.shape).ravel(order="F"),
        "a": np.broadcast_to(grid.a[None, :, None], grid.shape).ravel(order="F"),
    }
    drifts = {"b": np.asarray(mu_b, dtype=float), "a": np.asarray(mu_a, dtype=float)}
    for axis_number, axis in enumerate(("b", "a")):
        coordinate = coordinates[axis]
        target = drifts[axis].ravel(order="F")
        action = np.asarray(matrix @ coordinate).ravel()
        error = action - target
        product_sums = np.zeros(grid.size, dtype=float)
        for row in range(grid.size):
            start, end = matrix.indptr[row : row + 2]
            product_sum = float(
                np.sum(np.abs(matrix.data[start:end] * coordinate[matrix.indices[start:end]]))
            )
            product_sums[row] = (
                np.nextafter(product_sum, np.inf) if product_sum else 0.0
            )
        spacing = _spacing_representation_error(grid, drifts[axis], axis_number).ravel(
            order="F"
        )
        bound = gamma * product_sums + spacing
        bound = np.nextafter(bound, np.inf, where=bound > 0.0, out=bound)
        failures = np.flatnonzero(np.abs(error) > bound)
        receipt[axis] = {
            "max_abs_error": float(np.max(np.abs(error), initial=0.0)),
            "max_bound": float(np.max(bound, initial=0.0)),
            "violation_count": int(failures.size),
            "first_violation_flat_f": None if not failures.size else int(failures[0]),
            "passes": not failures.size,
            "error_field_sha256": _field_sha256(error),
            "bound_field_sha256": _field_sha256(bound),
        }
    return receipt


def _scientific_code_hashes(repository: Path) -> dict[str, str]:
    namespace = repository / "src/ch5_two_asset_hank/corrected_diagnostic"
    paths = list(namespace.glob("*.py")) + [
        repository / "tests/test_mp4c_2018_kfe_d123_option_a_single_step.py",
        repository
        / "tests/test_mp4c_2018_kfe_d123_lower_a_zero_kink_multiplier.py",
    ]
    return {
        path.relative_to(repository).as_posix(): _sha256(path)
        for path in sorted(paths)
    }


def _input_receipt(inputs: BoundOptionAInputs) -> dict[str, Any]:
    return {
        "seed": {
            "path": str(inputs.seed_path),
            "sha256": inputs.seed_sha256,
            "bytes": inputs.seed_bytes,
            "field": "v0",
            "field_sha256_f_order_little_endian_float64": inputs.v0_field_sha256,
            "shape_b_a_z": list(inputs.v0.shape),
            "range": [float(np.min(inputs.v0)), float(np.max(inputs.v0))],
        },
        "scalar_binding": {
            "path": str(inputs.binding_path),
            "sha256": inputs.binding_sha256,
            "bytes": inputs.binding_bytes,
        },
        "grid": {
            "shape": list(inputs.grid.shape),
            "order": "b,a,z",
            "flatten_order": "F",
            "b_field_sha256": _field_sha256(inputs.grid.b),
            "a_field_sha256": _field_sha256(inputs.grid.a),
            "z_field_sha256": _field_sha256(inputs.grid.z),
        },
        "scalars": inputs.scalars,
        "z_generator": inputs.z_generator.tolist(),
    }


def preflight_receipt(repository: Path, inputs: BoundOptionAInputs) -> dict[str, Any]:
    from . import selector

    inward_source = inspect.getsource(selector._inward_derivative)
    public_source = inspect.getsource(selector.select_constrained_policy)
    static_checks = {
        "lower_face_selects_forward_else_backward": (
            'branch = "forward" if face.startswith("lower") else "backward"'
            in inward_source
        ),
        "boundary_b_uses_only_inward_helper": (
            'b_options = [_inward_derivative(cell, "b", faces["b"])]'
            in public_source
        ),
        "boundary_a_uses_only_inward_helper": (
            'a_options = [_inward_derivative(cell, "a", faces["a"])]'
            in public_source
        ),
    }
    fields = raw_derivative_fields(inputs.v0, inputs.grid)
    boundary_marker_counts = {"b": 0, "a": 0}
    for index in iter_f_order_indices(inputs.grid.shape):
        _, markers = boundary_cell_derivatives(fields, index, inputs.grid)
        for axis in markers:
            boundary_marker_counts[axis] += 1
    expected_marker_counts = {
        "b": 2 * inputs.grid.a.size * inputs.grid.z.size,
        "a": 2 * inputs.grid.b.size * inputs.grid.z.size,
    }
    cell_zero_derivatives, _ = boundary_cell_derivatives(
        fields, (0, 0, 0), inputs.grid
    )
    cell_zero_shadow = selector.active_lower_a_zero_kink_shadow(
        p_a=cell_zero_derivatives.p_a_forward,
        q_b=cell_zero_derivatives.p_b_forward,
        chi_0=inputs.parameters.chi_0,
    )
    checks = {
        **static_checks,
        "exact_800_f_order_cells": len(list(iter_f_order_indices(inputs.grid.shape))) == 800,
        "boundary_marker_counts_exact": boundary_marker_counts == expected_marker_counts,
        "all_raw_derivatives_finite": all(
            np.all(np.isfinite(array)) for array in asdict(fields).values()
        ),
        "cell_zero_raw_p_a_exact_zero": cell_zero_derivatives.p_a_forward == 0.0,
        "cell_zero_shadow_interval_nonempty": cell_zero_shadow.intersection_nonempty,
        "cell_zero_shadow_marker_exact": (
            cell_zero_shadow.marker
            == "ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_CANONICAL_MIN"
        ),
        "git_head_resolves_before_execution": len(_git_head(repository)) == 40,
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "boundary_adapter_marker": BOUNDARY_ADAPTER_MARKER,
        "boundary_marker_counts": boundary_marker_counts,
        "expected_boundary_marker_counts": expected_marker_counts,
        "historical_option_a_cell_zero_algebraic_check": {
            "index_b_a_z_zero_based": [0, 0, 0],
            "p_b_forward": cell_zero_derivatives.p_b_forward,
            "p_a_forward": cell_zero_derivatives.p_a_forward,
            "shadow_receipt": asdict(cell_zero_shadow),
            "selector_evaluations": 0,
            "scalar_root_invocations": 0,
        },
        "input_identity": _input_receipt(inputs),
    }


def _ledger(
    budget: SelectorBudget,
    *,
    policy_maps: int,
    d2_assemblies: int,
    direct_solves: int,
    passed_cells: int,
    attempted_cells: int,
    terminal: str,
) -> dict[str, Any]:
    return {
        "terminal_classification": terminal,
        "corrected_policy_maps": policy_maps,
        "passed_cells": passed_cells,
        "attempted_cells": attempted_cells,
        "real_selector_evaluations": budget.selector_evaluations,
        "scalar_root_invocations": budget.root_invocations,
        "d2_generator_assemblies": d2_assemblies,
        "sparse_direct_hjb_solves": direct_solves,
        "selector_evaluations_on_v1": 0,
        "nonlinear_continuation_iterations": 0,
        "adverse_numerics_retries": 0,
        "forbidden_calls": {
            "KFE": 0,
            "MATLAB": 0,
            "outer": 0,
            "firm": 0,
            "wage_return_recalculation": 0,
            "GE": 0,
            "annual": 0,
            "shock": 0,
            "IRF": 0,
            "Results": 0,
        },
    }


def _seal_manifest(evidence: Path) -> dict[str, Any]:
    entries = []
    for path in sorted(evidence.iterdir()):
        if not path.is_file() or path.name == "manifest.json":
            continue
        entries.append(
            {
                "path": path.name,
                "sha256": _sha256(path),
                "bytes": path.stat().st_size,
            }
        )
    manifest = {
        "schema": "CH5_MP4C_2018_KFE_D123_LOWER_A_ZERO_KINK_OPTION_A_REEXECUTION_MANIFEST_V1",
        "entry_count": len(entries),
        "total_bytes": sum(int(row["bytes"]) for row in entries),
        "entries": entries,
    }
    _write_json(evidence / "manifest.json", manifest)
    return manifest


def _finalize(
    repository: Path,
    evidence: Path,
    pre_hashes: dict[str, str],
    budget: SelectorBudget,
    *,
    policy_maps: int,
    d2_assemblies: int,
    direct_solves: int,
    passed_cells: int,
    attempted_cells: int,
    terminal: str,
    terminal_detail: dict[str, Any],
) -> None:
    post_hashes = _scientific_code_hashes(repository)
    _write_json(
        evidence / "post_execution_freeze_check.json",
        {
            "scientific_code_sha256_after_execution": post_hashes,
            "matches_pre_execution_freeze": post_hashes == pre_hashes,
        },
    )
    _write_json(
        evidence / "execution_summary.json",
        {
            "verdict": terminal,
            "detail": terminal_detail,
            "scientific_code_freeze_preserved": post_hashes == pre_hashes,
        },
    )
    _write_json(
        evidence / "execution_ledger.json",
        _ledger(
            budget,
            policy_maps=policy_maps,
            d2_assemblies=d2_assemblies,
            direct_solves=direct_solves,
            passed_cells=passed_cells,
            attempted_cells=attempted_cells,
            terminal=terminal,
        ),
    )
    _seal_manifest(evidence)


def _cell_input_receipt(
    index: tuple[int, int, int],
    flat_index: int,
    cell: CorrectedSelectorCell,
    markers: dict[str, str],
) -> dict[str, Any]:
    return {
        "flat_index_f_zero_based": flat_index,
        "index_b_a_z_zero_based": list(index),
        "selector_cell": asdict(cell),
        "boundary_adapter_markers": markers,
    }


def execute(repository: Path, seed_path: Path, binding_path: Path) -> str:
    repository = repository.resolve(strict=True)
    evidence = repository / EVIDENCE_RELATIVE
    evidence.mkdir(parents=True, exist_ok=False)
    inputs = bind_option_a_inputs(seed_path, binding_path)
    preflight = preflight_receipt(repository, inputs)
    _write_json(evidence / "preflight.json", preflight)
    if preflight["status"] != "PASS":
        raise RuntimeError("preflight failed before first real selector call")

    pre_hashes = _scientific_code_hashes(repository)
    freeze = {
        "authority_id": AUTHORITY_ID,
        "git_head_before_first_real_selector_call": _git_head(repository),
        "scientific_code_sha256_before_first_real_selector_call": pre_hashes,
        "input_identity": _input_receipt(inputs),
        "budget": {
            "corrected_policy_maps": 1,
            "real_selector_evaluations": 800,
            "scalar_root_invocations": 264,
            "d2_assemblies": 1,
            "sparse_direct_hjb_solves": 1,
            "retries": 0,
            "v1_selector_evaluations": 0,
            "nonlinear_continuation": 0,
        },
    }
    _write_json(evidence / "pre_execution_freeze.json", freeze)
    code_freeze_identity = {
        "authority_id": freeze["authority_id"],
        "git_head_before_first_real_selector_call": freeze[
            "git_head_before_first_real_selector_call"
        ],
        "scientific_code_sha256_before_first_real_selector_call": pre_hashes,
        "seed_sha256": inputs.seed_sha256,
        "v0_field_sha256": inputs.v0_field_sha256,
        "scalar_binding_sha256": inputs.binding_sha256,
    }

    budget = SelectorBudget(max_selector_evaluations=800, max_root_invocations=264)
    policy_maps = 1
    d2_assemblies = 0
    direct_solves = 0
    passed_cells = 0
    attempted_cells = 0
    _write_json(
        evidence / "execution_ledger.json",
        _ledger(
            budget,
            policy_maps=policy_maps,
            d2_assemblies=d2_assemblies,
            direct_solves=direct_solves,
            passed_cells=0,
            attempted_cells=0,
            terminal="RUNNING",
        ),
    )
    fields = raw_derivative_fields(inputs.v0, inputs.grid)
    utility = np.empty(inputs.grid.shape, dtype=float)
    mu_b = np.empty(inputs.grid.shape, dtype=float)
    mu_a = np.empty(inputs.grid.shape, dtype=float)

    for flat_index, index in enumerate(iter_f_order_indices(inputs.grid.shape)):
        attempted_cells = flat_index + 1
        i_b, i_a, i_z = index
        b = float(inputs.grid.b[i_b])
        a = float(inputs.grid.a[i_a])
        z = float(inputs.grid.z[i_z])
        derivatives, markers = boundary_cell_derivatives(fields, index, inputs.grid)
        cell = CorrectedSelectorCell(
            cell_id=f"option_a_f{flat_index:04d}_b{i_b:03d}_a{i_a:03d}_z{i_z:03d}",
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
            effective_r_a=float(
                inputs.scalars["r_a"] * (1.0 - 0.1 * (a / 10.0) ** 9)
            ),
            derivatives=derivatives,
        )
        receipt_path = evidence / f"cell_{flat_index:04d}.json"
        input_receipt = _cell_input_receipt(index, flat_index, cell, markers)
        try:
            result = select_constrained_policy(cell, inputs.parameters, budget=budget)
        except Exception as exc:
            _write_json(
                receipt_path,
                {
                    **input_receipt,
                    "code_freeze_identity": code_freeze_identity,
                    "selector_exception": {
                        "type": type(exc).__name__,
                        "message": str(exc),
                    },
                    "cumulative_budget": asdict(budget),
                    "receipt_persistence_order": "SELECTOR_RETURN_OR_EXCEPTION_DURABLE_BEFORE_STOP",
                },
            )
            terminal = "FAIL__OPTION_A_POLICY_MAP_SELECTOR_EXCEPTION__STOPPED_WITHOUT_RETRY"
            _finalize(
                repository,
                evidence,
                pre_hashes,
                budget,
                policy_maps=policy_maps,
                d2_assemblies=d2_assemblies,
                direct_solves=direct_solves,
                passed_cells=passed_cells,
                attempted_cells=attempted_cells,
                terminal=terminal,
                terminal_detail={
                    "first_failing_flat_index_f_zero_based": flat_index,
                    "index_b_a_z_zero_based": list(index),
                    "receipt": receipt_path.name,
                },
            )
            return terminal

        receipt = {
            **input_receipt,
            "code_freeze_identity": code_freeze_identity,
            "selector_result": asdict(result),
            "cumulative_budget": asdict(budget),
            "receipt_persistence_order": "SELECTOR_RECEIPT_DURABLE_BEFORE_NEXT_CELL_OR_D2",
        }
        _write_json(receipt_path, receipt)
        current_hashes = _scientific_code_hashes(repository)
        if current_hashes != pre_hashes:
            terminal = "FAIL__SCIENTIFIC_CODE_MUTATED_AFTER_FREEZE__STOPPED_WITHOUT_RETRY"
            _finalize(
                repository,
                evidence,
                pre_hashes,
                budget,
                policy_maps=policy_maps,
                d2_assemblies=d2_assemblies,
                direct_solves=direct_solves,
                passed_cells=passed_cells,
                attempted_cells=attempted_cells,
                terminal=terminal,
                terminal_detail={"receipt": receipt_path.name},
            )
            return terminal
        if budget.selector_evaluations > 800 or budget.root_invocations > 264:
            terminal = "FAIL__SCIENTIFIC_CALL_BUDGET_EXCEEDED__STOPPED_WITHOUT_RETRY"
            _finalize(
                repository,
                evidence,
                pre_hashes,
                budget,
                policy_maps=policy_maps,
                d2_assemblies=d2_assemblies,
                direct_solves=direct_solves,
                passed_cells=passed_cells,
                attempted_cells=attempted_cells,
                terminal=terminal,
                terminal_detail={"receipt": receipt_path.name},
            )
            return terminal
        if result.outcome != "SELECTED_ADMISSIBLE" or result.selected is None:
            terminal = "FAIL__OPTION_A_REEXECUTION_FIRST_CELL_NOT_ADMISSIBLE__STOPPED_WITHOUT_RETRY"
            _finalize(
                repository,
                evidence,
                pre_hashes,
                budget,
                policy_maps=policy_maps,
                d2_assemblies=d2_assemblies,
                direct_solves=direct_solves,
                passed_cells=passed_cells,
                attempted_cells=attempted_cells,
                terminal=terminal,
                terminal_detail={
                    "first_failing_flat_index_f_zero_based": flat_index,
                    "index_b_a_z_zero_based": list(index),
                    "cell_id": cell.cell_id,
                    "selector_outcome": result.outcome,
                    "receipt": receipt_path.name,
                },
            )
            return terminal
        selected = result.selected
        if selected.utility is None or selected.g_b is None or selected.g_a is None:
            terminal = "FAIL__SELECTED_POLICY_MISSING_REQUIRED_OUTPUT__STOPPED_WITHOUT_RETRY"
            _finalize(
                repository,
                evidence,
                pre_hashes,
                budget,
                policy_maps=policy_maps,
                d2_assemblies=d2_assemblies,
                direct_solves=direct_solves,
                passed_cells=passed_cells,
                attempted_cells=attempted_cells,
                terminal=terminal,
                terminal_detail={"receipt": receipt_path.name},
            )
            return terminal
        utility[index] = float(selected.utility)
        mu_b[index] = float(selected.g_b)
        mu_a[index] = float(selected.g_a)
        passed_cells += 1

    if passed_cells != 800 or attempted_cells != 800:
        raise RuntimeError("internal full-map gate failed before D2")

    d2_assemblies = 1
    try:
        generator = assemble_consumed_drift_generator(
            inputs.grid,
            mu_b=mu_b,
            mu_a=mu_a,
            z_generator=inputs.z_generator,
        )
    except Exception as exc:
        terminal = "FAIL__OPTION_A_D2_ASSEMBLY_REJECTED__STOPPED_WITHOUT_RETRY"
        _write_json(
            evidence / "d2_receipt.json",
            {"status": "RAISED", "type": type(exc).__name__, "message": str(exc)},
        )
        _finalize(
            repository,
            evidence,
            pre_hashes,
            budget,
            policy_maps=policy_maps,
            d2_assemblies=d2_assemblies,
            direct_solves=direct_solves,
            passed_cells=passed_cells,
            attempted_cells=attempted_cells,
            terminal=terminal,
            terminal_detail={"d2_receipt": "d2_receipt.json"},
        )
        return terminal

    coordinate = coordinate_action_receipt(generator.q, inputs.grid, mu_b, mu_a)
    d2_checks = {
        "minimum_offdiagonal_nonnegative": generator.minimum_offdiagonal >= 0.0,
        "diagonal_construction_error_exact_zero": generator.diagonal_construction_error == 0.0,
        "q_one_within_prospective_bound": (
            generator.max_abs_q_one <= generator.arithmetic_tolerance
        ),
        "b_coordinate_within_prospective_bound": bool(coordinate["b"]["passes"]),
        "a_coordinate_within_prospective_bound": bool(coordinate["a"]["passes"]),
    }
    sparse.save_npz(evidence / "d2_generator.npz", generator.q)
    _write_json(
        evidence / "d2_receipt.json",
        {
            "status": "PASS" if all(d2_checks.values()) else "FAIL",
            "checks": d2_checks,
            "minimum_offdiagonal": generator.minimum_offdiagonal,
            "diagonal_construction_error": generator.diagonal_construction_error,
            "max_abs_q_one": generator.max_abs_q_one,
            "arithmetic_tolerance": generator.arithmetic_tolerance,
            "coordinate_action": coordinate,
            "q_artifact": {
                "path": "d2_generator.npz",
                "sha256": _sha256(evidence / "d2_generator.npz"),
                "bytes": (evidence / "d2_generator.npz").stat().st_size,
            },
        },
    )
    if not all(d2_checks.values()):
        terminal = "FAIL__OPTION_A_D2_INVARIANT_CHECK__STOPPED_WITHOUT_RETRY"
        _finalize(
            repository,
            evidence,
            pre_hashes,
            budget,
            policy_maps=policy_maps,
            d2_assemblies=d2_assemblies,
            direct_solves=direct_solves,
            passed_cells=passed_cells,
            attempted_cells=attempted_cells,
            terminal=terminal,
            terminal_detail={"d2_receipt": "d2_receipt.json"},
        )
        return terminal

    rho = inputs.scalars["rho"]
    delta = inputs.scalars["delta"]
    matrix = (rho + 1.0 / delta) * sparse.eye(inputs.grid.size, format="csr") - generator.q
    rhs = utility.ravel(order="F") + inputs.v0.ravel(order="F") / delta
    direct_solves = 1
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", MatrixRankWarning)
            v1_flat = np.asarray(sparse_linalg.spsolve(matrix, rhs), dtype=float)
    except Exception as exc:
        terminal = "FAIL__OPTION_A_DIRECT_HJB_SOLVE__STOPPED_WITHOUT_RETRY"
        _write_json(
            evidence / "direct_solve_receipt.json",
            {"status": "RAISED", "type": type(exc).__name__, "message": str(exc)},
        )
        _finalize(
            repository,
            evidence,
            pre_hashes,
            budget,
            policy_maps=policy_maps,
            d2_assemblies=d2_assemblies,
            direct_solves=direct_solves,
            passed_cells=passed_cells,
            attempted_cells=attempted_cells,
            terminal=terminal,
            terminal_detail={"direct_solve_receipt": "direct_solve_receipt.json"},
        )
        return terminal
    if v1_flat.shape != (inputs.grid.size,) or not np.all(np.isfinite(v1_flat)):
        terminal = "FAIL__OPTION_A_DIRECT_HJB_SOLVE_NONFINITE__STOPPED_WITHOUT_RETRY"
        _write_json(evidence / "direct_solve_receipt.json", {"status": "NONFINITE"})
        _finalize(
            repository,
            evidence,
            pre_hashes,
            budget,
            policy_maps=policy_maps,
            d2_assemblies=d2_assemblies,
            direct_solves=direct_solves,
            passed_cells=passed_cells,
            attempted_cells=attempted_cells,
            terminal=terminal,
            terminal_detail={"direct_solve_receipt": "direct_solve_receipt.json"},
        )
        return terminal

    v1 = v1_flat.reshape(inputs.grid.shape, order="F")
    residual = np.asarray(matrix @ v1_flat - rhs)
    residual_inf = float(np.linalg.norm(residual, ord=np.inf))
    matrix_inf = float(np.max(np.asarray(abs(matrix).sum(axis=1)).ravel(), initial=0.0))
    denominator = matrix_inf * float(np.linalg.norm(v1_flat, ord=np.inf)) + float(
        np.linalg.norm(rhs, ord=np.inf)
    )
    backward_error = residual_inf / denominator if denominator else 0.0
    if not np.isfinite(residual_inf) or not np.isfinite(backward_error):
        terminal = "FAIL__OPTION_A_DIRECT_HJB_RESIDUAL_NONFINITE__STOPPED_WITHOUT_RETRY"
        _write_json(
            evidence / "direct_solve_receipt.json",
            {"status": "NONFINITE_RESIDUAL", "residual_inf": residual_inf},
        )
        _finalize(
            repository,
            evidence,
            pre_hashes,
            budget,
            policy_maps=policy_maps,
            d2_assemblies=d2_assemblies,
            direct_solves=direct_solves,
            passed_cells=passed_cells,
            attempted_cells=attempted_cells,
            terminal=terminal,
            terminal_detail={"direct_solve_receipt": "direct_solve_receipt.json"},
        )
        return terminal

    np.savez_compressed(
        evidence / "direct_step_arrays.npz",
        v0=inputs.v0,
        utility=utility,
        mu_b=mu_b,
        mu_a=mu_a,
        rhs=rhs,
        v1=v1,
        residual=residual,
    )
    v1_fields = raw_derivative_fields(v1, inputs.grid)
    diagnostics = []
    for historical_cell, index in (
        (4, (19, 19, 0)),
        (8, (19, 19, 1)),
        (10, (19, 18, 0)),
    ):
        v0_derivatives, v0_markers = boundary_cell_derivatives(
            fields, index, inputs.grid
        )
        v1_derivatives, v1_markers = boundary_cell_derivatives(
            v1_fields, index, inputs.grid
        )
        diagnostics.append(
            {
                "historical_cell": historical_cell,
                "index_b_a_z_zero_based": list(index),
                "v0": float(inputs.v0[index]),
                "v1": float(v1[index]),
                "v1_minus_v0": float(v1[index] - inputs.v0[index]),
                "v0_derivatives": asdict(v0_derivatives),
                "v1_derivatives": asdict(v1_derivatives),
                "v0_boundary_adapter_markers": v0_markers,
                "v1_boundary_adapter_markers": v1_markers,
            }
        )
    _write_json(evidence / "failed_cell_diagnostics.json", {"cells": diagnostics})
    _write_json(
        evidence / "direct_solve_receipt.json",
        {
            "status": "PASS",
            "solver": "scipy.sparse.linalg.spsolve",
            "matrix_shape": list(matrix.shape),
            "matrix_nnz": int(matrix.nnz),
            "matrix_data_sha256": _field_sha256(matrix.data),
            "matrix_indices_sha256": hashlib.sha256(
                np.asarray(matrix.indices, dtype="<i8").tobytes()
            ).hexdigest().upper(),
            "matrix_indptr_sha256": hashlib.sha256(
                np.asarray(matrix.indptr, dtype="<i8").tobytes()
            ).hexdigest().upper(),
            "rhs_sha256": _field_sha256(rhs),
            "v1_sha256": _field_sha256(v1),
            "finite": True,
            "residual_inf": residual_inf,
            "matrix_inf": matrix_inf,
            "normwise_backward_error": backward_error,
            "arrays_artifact": {
                "path": "direct_step_arrays.npz",
                "sha256": _sha256(evidence / "direct_step_arrays.npz"),
                "bytes": (evidence / "direct_step_arrays.npz").stat().st_size,
            },
        },
    )
    terminal = "PASS__OPTION_A_COMPLETE_800_CELL_CORRECTED_POLICY_MAP__D2_PASS__ONE_DIRECT_HJB_STEP_COMPLETED"
    _finalize(
        repository,
        evidence,
        pre_hashes,
        budget,
        policy_maps=policy_maps,
        d2_assemblies=d2_assemblies,
        direct_solves=direct_solves,
        passed_cells=passed_cells,
        attempted_cells=attempted_cells,
        terminal=terminal,
        terminal_detail={
            "d2_receipt": "d2_receipt.json",
            "direct_solve_receipt": "direct_solve_receipt.json",
            "failed_cell_diagnostics": "failed_cell_diagnostics.json",
        },
    )
    return terminal


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--seed", type=Path, required=True)
    parser.add_argument("--binding", type=Path, required=True)
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args(argv)
    inputs = bind_option_a_inputs(args.seed, args.binding)
    if args.preflight_only:
        receipt = preflight_receipt(args.repository.resolve(strict=True), inputs)
        print(json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False))
        return 0 if receipt["status"] == "PASS" else 1
    verdict = execute(args.repository, args.seed, args.binding)
    print(verdict)
    return 0 if verdict.startswith("PASS__") else 2


if __name__ == "__main__":
    sys.exit(main())
