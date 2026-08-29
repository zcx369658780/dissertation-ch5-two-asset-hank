"""Validated immutable contracts for the bounded HJB layer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np
from scipy import sparse


def _readonly_1d(name: str, values: np.ndarray) -> np.ndarray:
    array = np.array(values, dtype=float, copy=True)
    if array.ndim != 1 or array.size < 2:
        raise ValueError(f"{name} must be a one-dimensional array with at least two nodes")
    if not np.all(np.isfinite(array)) or not np.all(np.diff(array) > 0.0):
        raise ValueError(f"{name} must be finite and strictly increasing")
    array.flags.writeable = False
    return array


@dataclass(frozen=True)
class GridSpec:
    a: np.ndarray
    b: np.ndarray
    z: np.ndarray
    b_bar: float

    def __post_init__(self) -> None:
        object.__setattr__(self, "a", _readonly_1d("a", self.a))
        object.__setattr__(self, "b", _readonly_1d("b", self.b))
        object.__setattr__(self, "z", _readonly_1d("z", self.z))
        if not np.isclose(self.a[0], 0.0):
            raise ValueError("the frozen illiquid lower bound requires a[0] == 0")
        if not np.isfinite(self.b_bar) or not np.isclose(self.b[0], self.b_bar):
            raise ValueError("b[0] must equal the declared borrowing limit b_bar")
        if self.z[0] <= 0.0:
            raise ValueError("the frozen productivity support requires z_L > 0")
        for name, values in (("a", self.a), ("b", self.b), ("z", self.z)):
            steps = np.diff(values)
            if not np.allclose(steps, steps[0], rtol=1e-12, atol=1e-14):
                raise ValueError(f"initial HJB slice supports uniform {name} grids only")

    @property
    def shape(self) -> tuple[int, int, int]:
        return (self.a.size, self.b.size, self.z.size)

    @property
    def size(self) -> int:
        return int(np.prod(self.shape))


@dataclass(frozen=True)
class EconomicParams:
    rho: float
    gamma_c: float
    phi: float
    chi_0: float
    chi_1: float
    a_bar: float
    mu_z: float
    sigma_z: float

    def __post_init__(self) -> None:
        values = np.array(
            [self.rho, self.gamma_c, self.phi, self.chi_0, self.chi_1, self.a_bar, self.mu_z, self.sigma_z]
        )
        if not np.all(np.isfinite(values)):
            raise ValueError("economic parameters must be finite")
        if self.rho <= 0 or self.gamma_c <= 0 or self.phi <= 0:
            raise ValueError("rho, gamma_c, and phi must be positive")
        if self.chi_0 < 0 or self.chi_1 <= 0 or self.a_bar <= 0:
            raise ValueError("adjustment parameters violate the frozen domain")
        if self.mu_z < 0 or self.sigma_z < 0:
            raise ValueError("diffusion parameters must be non-negative")


@dataclass(frozen=True)
class HouseholdInputs:
    r_a: float
    r_b: float
    tau: float
    wages: np.ndarray
    migration_costs: np.ndarray
    labor_weights: np.ndarray

    def __post_init__(self) -> None:
        for name in ("wages", "migration_costs", "labor_weights"):
            array = np.array(getattr(self, name), dtype=float, copy=True)
            if array.ndim != 1 or array.size == 0 or not np.all(np.isfinite(array)):
                raise ValueError(f"{name} must be a non-empty finite vector")
            array.flags.writeable = False
            object.__setattr__(self, name, array)
        if not (self.wages.shape == self.migration_costs.shape == self.labor_weights.shape):
            raise ValueError("province input vectors must share one shape")
        if not np.all(self.wages >= 0) or not np.all(self.labor_weights > 0):
            raise ValueError("wages must be non-negative and labor weights positive")
        if not np.isfinite([self.r_a, self.r_b, self.tau]).all():
            raise ValueError("rates and tax must be finite")
        if np.any(1.0 - self.tau - self.migration_costs < 0.0):
            raise ValueError("after-tax migration wedges must be non-negative")
        effective_wages = self.wages * (1.0 - self.tau - self.migration_costs)
        if not np.any(effective_wages > 0.0):
            raise ValueError("at least one province must have a strictly positive effective wage")


@dataclass(frozen=True)
class PolicySnapshot:
    consumption: np.ndarray
    labor: np.ndarray
    transfer: np.ndarray
    adjustment_cost: np.ndarray
    mu_a: np.ndarray
    mu_b: np.ndarray
    utility: np.ndarray
    candidate_id: np.ndarray
    lambda_a: np.ndarray
    lambda_b: np.ndarray
    kkt_state_residual: np.ndarray
    kkt_component_maxima: dict[str, float]
    boundary_violation: float
    kkt_residual: float
    raw_candidate_id: Optional[np.ndarray] = None
    qualifying_lower_b_alias_available: Optional[np.ndarray] = None
    effective_shadow_b: Optional[np.ndarray] = None
    alias_hamiltonian_gap: Optional[np.ndarray] = None
    alias_hamiltonian_bound: Optional[np.ndarray] = None


@dataclass(frozen=True)
class OperatorBundle:
    g_a: sparse.csr_matrix
    g_b: sparse.csr_matrix
    g_z: sparse.csr_matrix
    g: sparse.csr_matrix
    max_row_sum: float
    min_off_diagonal: float


@dataclass(frozen=True)
class HJBResult:
    value: np.ndarray
    policy: PolicySnapshot
    operator: OperatorBundle
    iterations: int
    converged: bool
    iteration_change: float
    residual_sup: float
