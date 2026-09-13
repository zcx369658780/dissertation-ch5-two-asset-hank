"""Lossless per-HJB-call receipts for the D1 transfer-control diagnostic."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np

from validators.multi_province.k1_transfer_control_raw_candidate_census.census import (
    BRANCHES,
    boundary_bits,
    file_sha256,
    selected_raw_masks,
)


D1_LIMIT = 1.0e5


def _json_scalar(value: Mapping[str, Any]) -> np.ndarray:
    return np.asarray(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")))


def write_d1_call_chunk(
    path: Path,
    observations: Sequence[tuple[int, Mapping[str, np.ndarray]]],
    *,
    grid: Any,
    numerics: Any,
    metadata: Mapping[str, Any],
    d1_active: bool,
    final_converged: bool,
    final_convergence_statistic: float,
) -> dict[str, Any]:
    if not observations:
        raise ValueError("at least one HJB iteration is required")
    destination = Path(path)
    if destination.exists():
        raise FileExistsError(destination)
    iteration = np.asarray([number for number, _ in observations], dtype=np.int32)
    if not np.array_equal(iteration, np.arange(1, len(observations) + 1, dtype=np.int32)):
        raise ValueError("HJB iteration numbers are not consecutive")

    def stack(name: str) -> np.ndarray:
        return np.stack([np.asarray(values[name]) for _, values in observations])

    raw = np.stack([np.stack([np.asarray(values[name]) for name in BRANCHES])
                    for _, values in observations])
    selected = stack("selected_transfer")
    selected_label = stack("selected_transfer_label")
    control = stack("control_transfer")
    control_label = stack("control_transfer_label")
    admissible = np.abs(raw) <= D1_LIMIT if d1_active else np.ones(raw.shape, dtype=bool)
    contributor, direction = selected_raw_masks(
        raw,
        control_label,
        float(numerics.drift_tolerance),
    )
    winner_changed = (selected_label != control_label) | (selected != control)
    control_direction_rejected = np.any(direction & ~admissible, axis=1)
    control_contributor_rejected = np.any(contributor & ~admissible, axis=1)
    fallback_to_zero = winner_changed & (selected == 0.0)
    switch_to_other_nonzero = winner_changed & (selected != 0.0)

    payload = {
        "schema": np.asarray("CH5_K1_TRANSFER_CONTROL_D1_CALL_V1"),
        "branch_names": np.asarray(BRANCHES),
        "iteration": iteration,
        "raw_d": raw,
        "d1_admissible": admissible,
        "raw_branch_existing_contributor_to_control": contributor,
        "raw_branch_in_control_winning_direction": direction,
        "control_winning_direction_branch_rejected": control_direction_rejected,
        "control_selected_contributor_rejected": control_contributor_rejected,
        "selected_transfer": selected,
        "selected_transfer_label": selected_label,
        "control_transfer": control,
        "control_transfer_label": control_label,
        "winner_changed": winner_changed,
        "fallback_to_existing_zero": fallback_to_zero,
        "switch_to_other_admissible_nonzero": switch_to_other_nonzero,
        "selected_adjustment_cost": stack("selected_adjustment_cost"),
        "control_adjustment_cost": stack("control_adjustment_cost"),
        "selected_mu_a": stack("selected_mu_a"),
        "control_mu_a": stack("control_mu_a"),
        "selected_mu_b": stack("selected_mu_b"),
        "control_mu_b": stack("control_mu_b"),
        "selected_consumption": stack("selected_consumption"),
        "control_consumption": stack("control_consumption"),
        "selected_labor": stack("selected_labor"),
        "control_labor": stack("control_labor"),
        "selected_liquid_label": stack("selected_liquid_label"),
        "control_liquid_label": stack("control_liquid_label"),
        "value_new": stack("value_new"),
        "convergence_statistic": stack("convergence_statistic"),
        "operator_sha256": stack("operator_sha256"),
        "boundary_bits": boundary_bits(tuple(int(x) for x in raw.shape[2:])),
        "grid_b": np.asarray(grid.b),
        "grid_a": np.asarray(grid.a),
        "grid_z": np.asarray(grid.z),
        "grid_switch_matrix": np.asarray(grid.switch_matrix),
        "d1_active": np.asarray(d1_active),
        "d1_limit": np.asarray(D1_LIMIT),
        "final_converged": np.asarray(final_converged),
        "final_convergence_statistic": np.asarray(final_convergence_statistic),
        "metadata_json": _json_scalar(metadata),
    }
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("xb") as stream:
        np.savez_compressed(stream, **payload)
    with np.load(destination, allow_pickle=False) as check:
        if tuple(check.files) != tuple(payload):
            raise RuntimeError("D1 chunk field readback mismatch")
        for name, expected in payload.items():
            equal_nan = np.issubdtype(np.asarray(expected).dtype, np.inexact)
            if not np.array_equal(check[name], expected, equal_nan=equal_nan):
                raise RuntimeError(f"D1 chunk array readback mismatch: {name}")

    hit = ~admissible
    return {
        "schema": "CH5_K1_TRANSFER_CONTROL_D1_CHUNK_RECEIPT_V1",
        "relative_path": destination.as_posix(),
        "sha256": file_sha256(destination),
        "iterations": int(raw.shape[0]),
        "raw_candidate_count": int(raw.size),
        "d1_inadmissible_count": int(np.count_nonzero(hit)),
        "d1_positive_inadmissible_count": int(np.count_nonzero(hit & (raw > 0.0))),
        "d1_negative_inadmissible_count": int(np.count_nonzero(hit & (raw < 0.0))),
        "rejected_never_in_control_winning_direction_count": int(np.count_nonzero(hit & ~direction)),
        "rejected_in_control_winning_direction_count": int(np.count_nonzero(hit & direction)),
        "rejected_control_contributor_count": int(np.count_nonzero(hit & contributor)),
        "winner_changed_count": int(np.count_nonzero(winner_changed)),
        "fallback_to_existing_zero_count": int(np.count_nonzero(fallback_to_zero)),
        "switch_to_other_admissible_nonzero_count": int(np.count_nonzero(switch_to_other_nonzero)),
        "selected_cell_count": int(selected.size),
        "metadata": dict(metadata),
    }
