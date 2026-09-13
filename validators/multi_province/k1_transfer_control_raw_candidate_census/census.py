"""Lossless per-HJB-call storage for raw transfer-candidate observations."""

from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np

from validators.multi_province.k1_g1_vs_g2_ha_hjb_instrumented.instrumented_hjb import array_hash


BRANCHES = ("d_bb", "d_bf", "d_fb", "d_ff")


def file_sha256(path: Path) -> str:
    digest = sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def boundary_bits(shape: tuple[int, int, int]) -> np.ndarray:
    result = np.zeros(shape, dtype=np.uint8)
    result[:, 0, :] |= 1
    result[:, -1, :] |= 2
    result[0, :, :] |= 4
    result[-1, :, :] |= 8
    return result


def selected_raw_masks(
    raw: np.ndarray, labels: np.ndarray, tolerance: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Return contributor and selector-direction masks without changing candidates.

    A B-labelled control is built from the bb/bf pair; an F-labelled control is
    built from fb/ff.  At the a boundaries the accepted source restricts the
    contributing member of each pair.  The second mask records the full pair
    participating in the selected selector direction even when one member does
    not contribute to the scalar selected transfer.
    """

    if raw.ndim != 5 or raw.shape[1] != len(BRANCHES):
        raise ValueError("raw census must have shape (iteration,branch,b,a,z)")
    if labels.shape != (raw.shape[0], *raw.shape[2:]):
        raise ValueError("transfer labels do not match raw-candidate shape")
    selected = np.zeros(raw.shape, dtype=bool)
    direction = np.zeros(raw.shape, dtype=bool)
    is_b, is_f = labels == "B", labels == "F"
    direction[:, 0] = is_b
    direction[:, 1] = is_b
    direction[:, 2] = is_f
    direction[:, 3] = is_f

    interior = np.ones(labels.shape, dtype=bool)
    interior[:, :, 0, :] = False
    interior[:, :, -1, :] = False
    lower_a = np.zeros(labels.shape, dtype=bool)
    upper_a = np.zeros(labels.shape, dtype=bool)
    lower_a[:, :, 0, :] = True
    upper_a[:, :, -1, :] = True

    selected[:, 0] = is_b & ((interior & (raw[:, 0] < 0.0)) | (upper_a & (raw[:, 0] < -tolerance)))
    selected[:, 1] = is_b & ((interior & (raw[:, 1] > 0.0)) | (lower_a & (raw[:, 1] > tolerance)))
    selected[:, 2] = is_f & ((interior & (raw[:, 2] < 0.0)) | (upper_a & (raw[:, 2] < -tolerance)))
    selected[:, 3] = is_f & ((interior & (raw[:, 3] > 0.0)) | (lower_a & (raw[:, 3] > tolerance)))
    return selected, direction


def _json_scalar(value: Mapping[str, Any]) -> np.ndarray:
    return np.asarray(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")))


def write_call_chunk(
    path: Path, observations: Sequence[tuple[int, Mapping[str, np.ndarray]]], *,
    grid: Any, numerics: Any, metadata: Mapping[str, Any], final_converged: bool,
    final_convergence_statistic: float,
) -> dict[str, Any]:
    if not observations:
        raise ValueError("at least one HJB iteration is required")
    destination = Path(path)
    if destination.exists():
        raise FileExistsError(destination)
    iteration_numbers = np.asarray([number for number, _ in observations], dtype=np.int32)
    if not np.array_equal(iteration_numbers, np.arange(1, len(observations) + 1, dtype=np.int32)):
        raise ValueError("HJB iteration numbers are not consecutive")
    raw = np.stack([
        np.stack([np.asarray(values[name]) for name in BRANCHES], axis=0)
        for _, values in observations
    ], axis=0)
    selected_transfer = np.stack([np.asarray(values["selected_transfer"]) for _, values in observations])
    selected_cost = np.stack([np.asarray(values["selected_adjustment_cost"]) for _, values in observations])
    labels = np.stack([np.asarray(values["transfer_label"]) for _, values in observations])
    contributor, direction = selected_raw_masks(raw, labels, float(numerics.drift_tolerance))
    reconstructed = np.sum(np.where(contributor, raw, 0.0), axis=1)
    reconstruction_equal = np.equal(reconstructed, selected_transfer)
    if not bool(np.all(reconstruction_equal)):
        raise RuntimeError("selected transfer cannot be reconstructed from raw contributors")

    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema": np.asarray("CH5_K1_TRANSFER_RAW_CANDIDATE_CENSUS_CALL_V1"),
        "branch_names": np.asarray(BRANCHES),
        "iteration": iteration_numbers,
        "raw_d": raw,
        "selected_transfer": selected_transfer,
        "selected_adjustment_cost": selected_cost,
        "selected_transfer_label": labels,
        "raw_branch_contributes_to_selected_transfer": contributor,
        "raw_branch_in_selected_direction": direction,
        "selected_transfer_reconstructed_from_raw": reconstructed,
        "selected_transfer_reconstruction_equal": reconstruction_equal,
        "boundary_bits": boundary_bits(tuple(int(x) for x in raw.shape[2:])),
        "grid_b": np.asarray(grid.b),
        "grid_a": np.asarray(grid.a),
        "grid_z": np.asarray(grid.z),
        "grid_switch_matrix": np.asarray(grid.switch_matrix),
        "final_converged": np.asarray(bool(final_converged)),
        "final_convergence_statistic": np.asarray(float(final_convergence_statistic)),
        "metadata_json": _json_scalar(metadata),
    }
    with destination.open("xb") as stream:
        np.savez_compressed(stream, **payload)

    with np.load(destination, allow_pickle=False) as check:
        if tuple(check.files) != tuple(payload):
            raise RuntimeError("census chunk field readback mismatch")
        for name, value in payload.items():
            equal_nan = np.issubdtype(np.asarray(value).dtype, np.inexact)
            if not np.array_equal(check[name], value, equal_nan=equal_nan):
                raise RuntimeError(f"census chunk array readback mismatch: {name}")
        readback_hashes = {name: array_hash(check[name]) for name in check.files}
    return {
        "schema": "CH5_K1_TRANSFER_RAW_CANDIDATE_CENSUS_CHUNK_RECEIPT_V1",
        "relative_path": destination.as_posix(),
        "sha256": file_sha256(destination),
        "iterations": int(raw.shape[0]),
        "branches": int(raw.shape[1]),
        "grid_cells_per_iteration": int(np.prod(raw.shape[2:])),
        "raw_candidate_count": int(raw.size),
        "raw_finite_count": int(np.count_nonzero(np.isfinite(raw))),
        "raw_nan_count": int(np.count_nonzero(np.isnan(raw))),
        "raw_positive_infinity_count": int(np.count_nonzero(np.isposinf(raw))),
        "raw_negative_infinity_count": int(np.count_nonzero(np.isneginf(raw))),
        "selected_transfer_reconstruction_equal_count": int(np.count_nonzero(reconstruction_equal)),
        "selected_transfer_cell_count": int(reconstruction_equal.size),
        "array_sha256": readback_hashes,
        "metadata": dict(metadata),
    }
