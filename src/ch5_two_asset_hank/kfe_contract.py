"""Validated input boundary between the accepted HJB operator and KFE."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import sparse

from .contracts import OperatorBundle


@dataclass(frozen=True)
class KFEInput:
    generator: sparse.csr_matrix
    canonical_shape: tuple[int, int, int]
    cell_weights: np.ndarray


def make_kfe_input(generator: sparse.csr_matrix, shape: tuple[int, int, int], cell_weights: np.ndarray) -> KFEInput:
    if len(shape) != 3 or any(size < 1 for size in shape):
        raise ValueError("KFE canonical shape must contain three positive dimensions")
    expected_size = int(np.prod(shape))
    if generator.shape != (expected_size, expected_size):
        raise ValueError("KFE generator shape does not match canonical state size")
    if not np.all(np.isfinite(generator.data)):
        raise ValueError("KFE generator entries must be finite")
    weights = np.array(cell_weights, dtype=float, copy=True)
    if weights.shape != shape or np.any(weights <= 0) or not np.all(np.isfinite(weights)):
        raise ValueError("KFE cell weights must be finite, positive, and canonical-shaped")
    weights.flags.writeable = False
    return KFEInput(generator.tocsr(copy=False), shape, weights)


def make_kfe_input_from_operator(
    operator: OperatorBundle,
    shape: tuple[int, int, int],
    cell_weights: np.ndarray,
) -> KFEInput:
    """Consume the accepted shared operator without reconstructing its drifts."""
    return make_kfe_input(operator.g, shape, cell_weights)
