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


_NORMALIZED_ORIENTATION = "rows=destination, columns=origin"
_NORMALIZED_SCHEMA = "origin-preserving-normalized-migration-labor/v1"
_NORMALIZED_TOLERANCE = 1.0e-12


@dataclass(frozen=True)
class OriginPreservingNormalizedMigrationLaborInputs:
    """Inputs for bilateral origin-mass-preserving labor allocation.

    Matrices have destination rows and origin columns.  Unlike
    :class:`MigrationLaborInputs`, ``household_labor_per_capita_by_origin`` is
    an explicit household output: it is multiplied by origin population once,
    after the source-faithful attractiveness kernel is normalized by column.
    """

    consumption_by_origin: np.ndarray
    household_labor_per_capita_by_origin: np.ndarray
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
        household_labor = _readonly_vector(
            "household_labor_per_capita_by_origin",
            self.household_labor_per_capita_by_origin,
            n,
        )
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
        if np.any(household_labor < 0.0):
            raise ValueError("household labor per capita must be non-negative")
        if np.any(wages < 0.0):
            raise ValueError("firm wages must be non-negative")
        if np.any(phi <= 0.0):
            raise ValueError("phi must be strictly positive")
        object.__setattr__(self, "consumption_by_origin", consumption)
        object.__setattr__(self, "household_labor_per_capita_by_origin", household_labor)
        object.__setattr__(self, "population_by_origin", population)
        object.__setattr__(self, "old_firm_wage_by_destination", wages)
        object.__setattr__(self, "tax_by_origin", taxes)
        object.__setattr__(self, "phi_destination_origin", phi)
        object.__setattr__(self, "migration_wedge_destination_origin", wedges)
        object.__setattr__(self, "gamma_c", gamma_c)
        object.__setattr__(self, "phi_l", phi_l)


@dataclass(frozen=True)
class OriginPreservingNormalizedMigrationLaborResult:
    """Auditable destination-by-origin normalized migration allocation."""

    raw_attractiveness_destination_origin: np.ndarray
    normalized_shares_destination_origin: np.ndarray
    origin_labor_mass_by_origin: np.ndarray
    bilateral_labor_flow_destination_origin: np.ndarray
    destination_firm_labor_by_destination: np.ndarray
    share_column_sums_by_origin: np.ndarray
    flow_column_sums_by_origin: np.ndarray
    net_labor_flow_by_province: np.ndarray
    national_conservation_residual: float
    orientation: str = _NORMALIZED_ORIENTATION
    schema: str = _NORMALIZED_SCHEMA

    def __post_init__(self) -> None:
        q = np.array(self.raw_attractiveness_destination_origin, dtype=float, copy=True)
        shares = np.array(self.normalized_shares_destination_origin, dtype=float, copy=True)
        origin_mass = np.array(self.origin_labor_mass_by_origin, dtype=float, copy=True)
        flows = np.array(self.bilateral_labor_flow_destination_origin, dtype=float, copy=True)
        destination = np.array(self.destination_firm_labor_by_destination, dtype=float, copy=True)
        share_sums = np.array(self.share_column_sums_by_origin, dtype=float, copy=True)
        flow_sums = np.array(self.flow_column_sums_by_origin, dtype=float, copy=True)
        net = np.array(self.net_labor_flow_by_province, dtype=float, copy=True)
        if q.ndim != 2 or q.shape[0] != q.shape[1]:
            raise ValueError("raw attractiveness must be a square destination-by-origin matrix")
        n = q.shape[0]
        arrays = (shares, flows)
        vectors = (origin_mass, destination, share_sums, flow_sums, net)
        if (
            any(array.shape != (n, n) for array in arrays)
            or any(vector.shape != (n,) for vector in vectors)
            or not all(np.all(np.isfinite(array)) for array in (q, *arrays, *vectors))
        ):
            raise ValueError("normalized migration result has an invalid shape or non-finite value")
        residual = float(self.national_conservation_residual)
        if not np.isfinite(residual):
            raise ValueError("national conservation residual must be finite")
        if np.any(q < 0.0) or np.any(shares < 0.0) or np.any(origin_mass < 0.0) or np.any(flows < 0.0):
            raise ValueError("normalized migration result cannot contain negative mass or shares")
        if self.orientation != _NORMALIZED_ORIENTATION or self.schema != _NORMALIZED_SCHEMA:
            raise ValueError("normalized migration result orientation or schema is invalid")
        if not np.allclose(share_sums, np.sum(shares, axis=0), rtol=_NORMALIZED_TOLERANCE, atol=_NORMALIZED_TOLERANCE):
            raise ValueError("share column sums must equal normalized-share columns")
        if not np.allclose(share_sums, 1.0, rtol=_NORMALIZED_TOLERANCE, atol=_NORMALIZED_TOLERANCE):
            raise ValueError("every normalized-share origin column must sum to one")
        if not np.allclose(flow_sums, np.sum(flows, axis=0), rtol=_NORMALIZED_TOLERANCE, atol=_NORMALIZED_TOLERANCE):
            raise ValueError("flow column sums must equal bilateral-flow columns")
        if not np.allclose(flow_sums, origin_mass, rtol=_NORMALIZED_TOLERANCE, atol=_NORMALIZED_TOLERANCE):
            raise ValueError("every bilateral-flow origin column must preserve origin labor mass")
        if not np.allclose(destination, np.sum(flows, axis=1), rtol=_NORMALIZED_TOLERANCE, atol=_NORMALIZED_TOLERANCE):
            raise ValueError("destination firm labor must equal bilateral-flow row sums")
        if not np.allclose(net, destination - origin_mass, rtol=_NORMALIZED_TOLERANCE, atol=_NORMALIZED_TOLERANCE):
            raise ValueError("net labor flow must be destination labor minus origin labor mass")
        expected_residual = float(np.sum(destination) - np.sum(origin_mass))
        if not np.isclose(residual, expected_residual, rtol=_NORMALIZED_TOLERANCE, atol=_NORMALIZED_TOLERANCE):
            raise ValueError("national conservation residual is inconsistent with labor masses")
        if not np.isclose(residual, 0.0, rtol=_NORMALIZED_TOLERANCE, atol=_NORMALIZED_TOLERANCE):
            raise ValueError("national labor conservation failed")
        for array in (q, shares, origin_mass, flows, destination, share_sums, flow_sums, net):
            array.flags.writeable = False
        object.__setattr__(self, "raw_attractiveness_destination_origin", q)
        object.__setattr__(self, "normalized_shares_destination_origin", shares)
        object.__setattr__(self, "origin_labor_mass_by_origin", origin_mass)
        object.__setattr__(self, "bilateral_labor_flow_destination_origin", flows)
        object.__setattr__(self, "destination_firm_labor_by_destination", destination)
        object.__setattr__(self, "share_column_sums_by_origin", share_sums)
        object.__setattr__(self, "flow_column_sums_by_origin", flow_sums)
        object.__setattr__(self, "net_labor_flow_by_province", net)
        object.__setattr__(self, "national_conservation_residual", residual)

    @property
    def q(self) -> np.ndarray:
        """Raw destination-attractiveness kernel, destination rows/origin columns."""
        return self.raw_attractiveness_destination_origin

    @property
    def s(self) -> np.ndarray:
        """Normalized bilateral shares, destination rows/origin columns."""
        return self.normalized_shares_destination_origin

    @property
    def origin_mass(self) -> np.ndarray:
        """Aggregate origin labor mass after its single population multiplication."""
        return self.origin_labor_mass_by_origin

    @property
    def M(self) -> np.ndarray:
        """Bilateral labor-flow matrix, destination rows/origin columns."""
        return self.bilateral_labor_flow_destination_origin

    @property
    def destination_labor(self) -> np.ndarray:
        """Destination firm-labor vector (the row sums of ``M``)."""
        return self.destination_firm_labor_by_destination

    @property
    def share_column_sums(self) -> np.ndarray:
        return self.share_column_sums_by_origin

    @property
    def flow_column_sums(self) -> np.ndarray:
        return self.flow_column_sums_by_origin

    @property
    def net_labor_flow(self) -> np.ndarray:
        return self.net_labor_flow_by_province

    @property
    def national_residual(self) -> float:
        return self.national_conservation_residual


def reconstruct_origin_preserving_normalized_migration_labor(
    inputs: OriginPreservingNormalizedMigrationLaborInputs,
) -> OriginPreservingNormalizedMigrationLaborResult:
    """Allocate each origin's household labor mass by normalized literal kernel.

    The legacy reconstruction remains untouched.  Here the literal kernel is
    first evaluated *without* population, then each origin column is normalized
    and receives ``household_labor_per_capita * population`` exactly once.
    """

    n = inputs.consumption_by_origin.size
    q = np.empty((n, n), dtype=float)
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
            value = consumption_scale * base ** (1.0 / inputs.phi_l)
            if not np.isfinite(value) or value < 0.0:
                raise ValueError("normalized migration kernel produced a non-finite or negative value")
            q[destination, origin] = value
    column_totals = np.sum(q, axis=0)
    if not np.all(np.isfinite(column_totals)) or np.any(column_totals <= 0.0):
        raise ValueError("every origin attractiveness column must have a finite positive total")
    shares = q / column_totals[np.newaxis, :]
    share_sums = np.sum(shares, axis=0)
    if np.any(shares < 0.0) or not np.allclose(
        share_sums, 1.0, rtol=_NORMALIZED_TOLERANCE, atol=_NORMALIZED_TOLERANCE
    ):
        raise ValueError("normalized migration shares must be non-negative and sum to one by origin")
    origin_mass = inputs.household_labor_per_capita_by_origin * inputs.population_by_origin
    if not np.all(np.isfinite(origin_mass)) or np.any(origin_mass < 0.0):
        raise ValueError("origin labor mass must be finite and non-negative")
    flows = shares * origin_mass[np.newaxis, :]
    destination = np.sum(flows, axis=1)
    flow_sums = np.sum(flows, axis=0)
    if not np.allclose(
        flow_sums, origin_mass, rtol=_NORMALIZED_TOLERANCE, atol=_NORMALIZED_TOLERANCE
    ):
        raise ValueError("bilateral labor flow failed origin-column conservation")
    residual = float(np.sum(destination) - np.sum(origin_mass))
    if not np.isclose(residual, 0.0, rtol=_NORMALIZED_TOLERANCE, atol=_NORMALIZED_TOLERANCE):
        raise ValueError("bilateral labor flow failed national conservation")
    return OriginPreservingNormalizedMigrationLaborResult(
        raw_attractiveness_destination_origin=q,
        normalized_shares_destination_origin=shares,
        origin_labor_mass_by_origin=origin_mass,
        bilateral_labor_flow_destination_origin=flows,
        destination_firm_labor_by_destination=destination,
        share_column_sums_by_origin=share_sums,
        flow_column_sums_by_origin=flow_sums,
        net_labor_flow_by_province=destination - origin_mass,
        national_conservation_residual=residual,
    )
