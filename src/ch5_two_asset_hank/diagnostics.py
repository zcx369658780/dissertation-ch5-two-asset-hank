"""Non-mutating HJB and generator diagnostics."""

from __future__ import annotations

import numpy as np

from .contracts import EconomicParams, GridSpec, OperatorBundle, PolicySnapshot
from .indexing import flatten


def normalized_change(left: np.ndarray, right: np.ndarray) -> float:
    left_array, right_array = np.asarray(left, dtype=float), np.asarray(right, dtype=float)
    if left_array.shape != right_array.shape or not np.isfinite(left_array).all() or not np.isfinite(right_array).all():
        raise ValueError("truncation comparison arrays must be finite and shape-identical")
    scale = max(1.0, float(np.max(np.abs(left_array))), float(np.max(np.abs(right_array))))
    return float(np.max(np.abs(left_array - right_array)) / scale)


def hjb_residual(
    value: np.ndarray,
    policy: PolicySnapshot,
    operator: OperatorBundle,
    grid: GridSpec,
    params: EconomicParams,
) -> np.ndarray:
    vector = flatten(value, grid.shape)
    utility = flatten(policy.utility, grid.shape)
    residual = params.rho * vector - utility - operator.g @ vector
    return np.asarray(residual)


def validate_operator(operator: OperatorBundle, tolerance: float) -> None:
    if operator.max_row_sum > tolerance:
        raise ValueError(f"generator row-sum residual {operator.max_row_sum} exceeds tolerance")
    if operator.min_off_diagonal < -tolerance:
        raise ValueError(f"generator has negative off-diagonal {operator.min_off_diagonal}")
