"""Forward/backward derivatives with explicit validity masks."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .contracts import GridSpec


@dataclass(frozen=True)
class DerivativeBundle:
    a_forward: np.ndarray
    a_backward: np.ndarray
    b_forward: np.ndarray
    b_backward: np.ndarray
    a_forward_valid: np.ndarray
    a_backward_valid: np.ndarray
    b_forward_valid: np.ndarray
    b_backward_valid: np.ndarray


def compute_derivatives(value: np.ndarray, grid: GridSpec) -> DerivativeBundle:
    array = np.asarray(value, dtype=float)
    if array.shape != grid.shape or not np.all(np.isfinite(array)):
        raise ValueError("value must be finite with canonical logical shape")
    shape = grid.shape
    nan = np.full(shape, np.nan)
    a_f, a_b, b_f, b_b = (nan.copy() for _ in range(4))
    a_f[:-1] = (array[1:] - array[:-1]) / np.diff(grid.a)[:, None, None]
    a_b[1:] = (array[1:] - array[:-1]) / np.diff(grid.a)[:, None, None]
    b_f[:, :-1] = (array[:, 1:] - array[:, :-1]) / np.diff(grid.b)[None, :, None]
    b_b[:, 1:] = (array[:, 1:] - array[:, :-1]) / np.diff(grid.b)[None, :, None]
    return DerivativeBundle(
        a_f,
        a_b,
        b_f,
        b_b,
        np.isfinite(a_f),
        np.isfinite(a_b),
        np.isfinite(b_f),
        np.isfinite(b_b),
    )

