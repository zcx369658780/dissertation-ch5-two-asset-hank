"""Canonical (a,b,z), a-fast index operations."""

from __future__ import annotations

import numpy as np


def canonical_index(i_a: int, i_b: int, i_z: int, shape: tuple[int, int, int]) -> int:
    n_a, n_b, n_z = shape
    if not (0 <= i_a < n_a and 0 <= i_b < n_b and 0 <= i_z < n_z):
        raise IndexError("state index outside canonical shape")
    return i_a + n_a * (i_b + n_b * i_z)


def inverse_index(k: int, shape: tuple[int, int, int]) -> tuple[int, int, int]:
    n_a, n_b, n_z = shape
    if not 0 <= k < n_a * n_b * n_z:
        raise IndexError("flat index outside canonical shape")
    i_a = k % n_a
    quotient = k // n_a
    i_b = quotient % n_b
    i_z = quotient // n_b
    return i_a, i_b, i_z


def flatten(values: np.ndarray, shape: tuple[int, int, int]) -> np.ndarray:
    array = np.asarray(values, dtype=float)
    if array.shape != shape:
        raise ValueError(f"expected logical shape {shape}, got {array.shape}")
    return np.reshape(array, -1, order="F")


def unflatten(values: np.ndarray, shape: tuple[int, int, int]) -> np.ndarray:
    array = np.asarray(values, dtype=float)
    if array.ndim != 1 or array.size != int(np.prod(shape)):
        raise ValueError("flat vector size does not match canonical shape")
    return np.reshape(array, shape, order="F")


def matlab_to_canonical(values_baz: np.ndarray) -> np.ndarray:
    array = np.asarray(values_baz)
    if array.ndim != 3:
        raise ValueError("MATLAB provenance array must have logical axes [b,a,z]")
    return np.transpose(array, (1, 0, 2))

