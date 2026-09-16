"""Isolated contracts for the Owner-adopted corrected diagnostic target."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


AUTHORITY_ID = "CH5_MP4C_2018_KFE_D123_OWNER_ADOPTED_20260916"
STATE_ORDER = "b,a,z"
FLATTEN_ORDER = "F"


def _readonly_nodes(name: str, values: np.ndarray) -> np.ndarray:
    nodes = np.array(values, dtype=float, copy=True)
    if nodes.ndim != 1 or nodes.size < 1:
        raise ValueError(f"{name} must be a non-empty one-dimensional array")
    if not np.all(np.isfinite(nodes)):
        raise ValueError(f"{name} must contain only finite values")
    if nodes.size > 1 and not np.all(np.diff(nodes) > 0.0):
        raise ValueError(f"{name} must be strictly increasing")
    nodes.flags.writeable = False
    return nodes


@dataclass(frozen=True)
class CorrectedDiagnosticGrid:
    """Finite diagnostic box in accepted saved-control ``(b,a,z)`` order."""

    b: np.ndarray
    a: np.ndarray
    z: np.ndarray

    def __post_init__(self) -> None:
        object.__setattr__(self, "b", _readonly_nodes("b", self.b))
        object.__setattr__(self, "a", _readonly_nodes("a", self.a))
        object.__setattr__(self, "z", _readonly_nodes("z", self.z))
        if self.b.size < 2 or self.a.size < 2:
            raise ValueError("both asset grids require at least two nodes")
        if not np.isclose(self.a[0], 0.0):
            raise ValueError("the distinct economic illiquid lower bound requires a[0] == 0")

    @property
    def shape(self) -> tuple[int, int, int]:
        return (self.b.size, self.a.size, self.z.size)

    @property
    def size(self) -> int:
        return int(np.prod(self.shape))


def checked_drift(name: str, values: np.ndarray, shape: tuple[int, int, int]) -> np.ndarray:
    drift = np.asarray(values, dtype=float)
    if drift.shape != shape:
        raise ValueError(f"{name} must have shape {shape}, got {drift.shape}")
    if not np.all(np.isfinite(drift)):
        raise ValueError(f"{name} must contain only finite values")
    return drift
