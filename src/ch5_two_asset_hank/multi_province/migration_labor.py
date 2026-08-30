"""Source-faithful migration-labor reconstruction for one outer turn.

Authority: ``Lt_seperate.m:6-14`` and ``HANK_mp_1turn.m:23-25``.
No household or fixed-point solver is imported or called here.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


def _readonly_vector(name: str, value: object, n: int | None = None) -> np.ndarray:
    array = np.array(value, dtype=float, copy=True)
    if array.ndim != 1 or array.size < 2 or (n is not None and array.shape != (n,)):
        expected = "a vector with at least two provinces" if n is None else f"shape ({n},)"
        raise ValueError(f"{name} must have {expected}")
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values")
    array.flags.writeable = False
    return array


def _readonly_matrix(name: str, value: object, n: int) -> np.ndarray:
    array = np.array(value, dtype=float, copy=True)
    if array.shape != (n, n):
        raise ValueError(f"{name} must have destination-by-origin shape ({n}, {n})")
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values")
    array.flags.writeable = False
    return array


@dataclass(frozen=True)
class MigrationLaborInputs:
    """Complete literal inputs; matrices use rows=destination, columns=origin."""

    consumption_by_origin: np.ndarray
    population_by_origin: np.ndarray
    old_firm_wage_by_destination: np.ndarray
    tax_by_origin: np.ndarray
    phi_destination_origin: np.ndarray
    migration_wedge_destination_origin: np.ndarray
    gamma_c: float
    phi_l: float

    def __post_init__(self) -> None:
        consumption = _readonly_vector("consumption_by_origin", self.consumption_by_origin)
        n = consumption.size
        population = _readonly_vector("population_by_origin", self.population_by_origin, n)
        wages = _readonly_vector("old_firm_wage_by_destination", self.old_firm_wage_by_destination, n)
        taxes = _readonly_vector("tax_by_origin", self.tax_by_origin, n)
        phi = _readonly_matrix("phi_destination_origin", self.phi_destination_origin, n)
        wedges = _readonly_matrix(
            "migration_wedge_destination_origin", self.migration_wedge_destination_origin, n
        )
        gamma_c = float(self.gamma_c)
        phi_l = float(self.phi_l)
        if not np.isfinite([gamma_c, phi_l]).all() or gamma_c <= 0.0 or phi_l <= 0.0:
            raise ValueError("gamma_c and phi_l must be finite and positive")
        if np.any(consumption <= 0.0) or np.any(population <= 0.0):
            raise ValueError("consumption and population must be strictly positive")
        if np.any(wages < 0.0) or np.any(phi <= 0.0):
            raise ValueError("firm wages must be non-negative and phi must be positive")
        object.__setattr__(self, "consumption_by_origin", consumption)
        object.__setattr__(self, "population_by_origin", population)
        object.__setattr__(self, "old_firm_wage_by_destination", wages)
        object.__setattr__(self, "tax_by_origin", taxes)
        object.__setattr__(self, "phi_destination_origin", phi)
        object.__setattr__(self, "migration_wedge_destination_origin", wedges)
        object.__setattr__(self, "gamma_c", gamma_c)
        object.__setattr__(self, "phi_l", phi_l)


@dataclass(frozen=True)
class MigrationLaborResult:
    """``lt_mat[destination, origin]`` and its destination row sums."""

    lt_mat: np.ndarray
    lt_supply: np.ndarray

    def __post_init__(self) -> None:
        matrix = np.array(self.lt_mat, dtype=float, copy=True)
        supply = np.array(self.lt_supply, dtype=float, copy=True)
        if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
            raise ValueError("lt_mat must be a square destination-by-origin matrix")
        if supply.shape != (matrix.shape[0],) or not np.all(np.isfinite(matrix)) or not np.all(np.isfinite(supply)):
            raise ValueError("migration-labor result has an invalid shape or non-finite value")
        if not np.array_equal(supply, np.sum(matrix, axis=1)):
            raise ValueError("lt_supply must equal destination row sums of lt_mat")
        matrix.flags.writeable = False
        supply.flags.writeable = False
        object.__setattr__(self, "lt_mat", matrix)
        object.__setattr__(self, "lt_supply", supply)


def reconstruct_migration_labor(inputs: MigrationLaborInputs) -> MigrationLaborResult:
    """Evaluate ``Lt_seperate`` literally, preserving its index placement."""

    n = inputs.consumption_by_origin.size
    matrix = np.empty((n, n), dtype=float)
    for origin in range(n):
        consumption_scale = inputs.consumption_by_origin[origin] ** (
            -inputs.gamma_c / inputs.phi_l
        )
        for destination in range(n):
            base = (
                inputs.old_firm_wage_by_destination[destination]
                * (
                    1.0
                    - inputs.tax_by_origin[origin]
                    - inputs.migration_wedge_destination_origin[destination, origin]
                )
                / inputs.phi_destination_origin[destination, origin]
            )
            if not np.isfinite(base) or base < 0.0:
                raise ValueError(
                    "Lt_seperate power base must be finite and non-negative "
                    f"at destination={destination}, origin={origin}"
                )
            value = (
                consumption_scale
                * base ** (1.0 / inputs.phi_l)
                * inputs.population_by_origin[origin]
            )
            if not np.isfinite(value) or value < 0.0:
                raise ValueError("migration labor produced a non-finite or negative value")
            matrix[destination, origin] = value
    supply = np.sum(matrix, axis=1)
    return MigrationLaborResult(lt_mat=matrix, lt_supply=supply)
