"""TEMP31 candidate algebra and wage data only; deliberately not production wired.

Rows are destinations j, columns origins i. Historical migration/HA functions
are neither imported nor changed. These contracts do not certify labor units,
empirical wage provenance, fiscal adoption, or a real household solution.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isclose, isfinite

Vector = tuple[float, ...]
Matrix = tuple[Vector, ...]
NET_COMPOSITE = "NET_COMPOSITE_AFTER_DESTINATION_TAU_AND_MIGRATION_WEDGE"


def _vector(name: str, values: object, n: int | None = None) -> Vector:
    try:
        result = tuple(float(x) for x in values)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} requires a finite one-dimensional vector") from exc
    if len(result) < 2 or (n is not None and len(result) != n) or not all(map(isfinite, result)):
        raise ValueError(f"{name} has invalid length or non-finite entries")
    return result


def _matrix(name: str, values: object, n: int) -> Matrix:
    try:
        result = tuple(_vector(name, row, n) for row in values)
    except TypeError as exc:
        raise ValueError(f"{name} requires destination rows and origin columns") from exc
    if len(result) != n:
        raise ValueError(f"{name} requires shape ({n}, {n})")
    return result


def _nonnegative(value: float, name: str) -> float:
    if not isfinite(value) or value < 0:
        raise ValueError(f"{name} must be finite and non-negative")
    return value


@dataclass(frozen=True)
class Temp31LaborInputs:
    consumption_by_origin: Vector
    population_by_origin: Vector
    old_firm_wage_by_destination: Vector
    tax_by_destination: Vector
    phi_destination_origin: Matrix
    migration_wedge_destination_origin: Matrix
    gamma_c: float
    phi_l: float

    def __post_init__(self) -> None:
        consumption = _vector("consumption_by_origin", self.consumption_by_origin)
        n = len(consumption)
        population = _vector("population_by_origin", self.population_by_origin, n)
        wages = _vector("old_firm_wage_by_destination", self.old_firm_wage_by_destination, n)
        taxes = _vector("tax_by_destination", self.tax_by_destination, n)
        phi = _matrix("phi_destination_origin", self.phi_destination_origin, n)
        sigma = _matrix("migration_wedge_destination_origin", self.migration_wedge_destination_origin, n)
        gamma, elasticity = float(self.gamma_c), float(self.phi_l)
        if any(x <= 0 for x in (*consumption, *population)):
            raise ValueError("consumption and population must be positive")
        if any(x < 0 for x in wages) or any(x <= 0 for row in phi for x in row):
            raise ValueError("wages must be non-negative and phi positive")
        if not all(map(isfinite, (gamma, elasticity))) or gamma <= 0 or elasticity <= 0:
            raise ValueError("gamma_c and phi_l must be finite and positive")
        for name, value in (("consumption_by_origin", consumption), ("population_by_origin", population),
                            ("old_firm_wage_by_destination", wages), ("tax_by_destination", taxes),
                            ("phi_destination_origin", phi), ("migration_wedge_destination_origin", sigma),
                            ("gamma_c", gamma), ("phi_l", elasticity)):
            object.__setattr__(self, name, value)


@dataclass(frozen=True)
class Temp31LaborResult:
    lt_mat: Matrix
    lt_supply: Vector
    raw_attractiveness: Matrix
    shares: Matrix | None = None
    origin_mass: Vector | None = None
    national_conservation_residual: float | None = None
    orientation: str = "rows=destination, columns=origin"


def _temp31_attractiveness(inputs: Temp31LaborInputs) -> Matrix:
    """Same consumption/wage powers as history, with destination tax indexing."""
    n = len(inputs.consumption_by_origin)
    q = [[0.0] * n for _ in range(n)]
    try:
        for origin in range(n):
            scale = inputs.consumption_by_origin[origin] ** (-inputs.gamma_c / inputs.phi_l)
            for destination in range(n):
                base = (inputs.old_firm_wage_by_destination[destination]
                        * (1 - inputs.tax_by_destination[destination]
                           - inputs.migration_wedge_destination_origin[destination][origin])
                        / inputs.phi_destination_origin[destination][origin])
                _nonnegative(base, "TEMP31 power base")
                q[destination][origin] = _nonnegative(scale * base ** (1 / inputs.phi_l), "TEMP31 kernel")
    except OverflowError as exc:
        raise ValueError("TEMP31 kernel overflow") from exc
    return tuple(tuple(row) for row in q)


def reconstruct_temp31_worksite_labor(inputs: Temp31LaborInputs) -> Temp31LaborResult:
    """Source-like quantity reconstruction; no origin-mass normalization."""
    q = _temp31_attractiveness(inputs)
    matrix = tuple(tuple(_nonnegative(value * inputs.population_by_origin[i], "bilateral labor")
                         for i, value in enumerate(row)) for row in q)
    supply = tuple(_nonnegative(sum(row), "destination row sum") for row in matrix)
    return Temp31LaborResult(matrix, supply, q)


def reconstruct_temp31_normalized_worksite_labor(
    inputs: Temp31LaborInputs, household_labor_per_capita_by_origin: Vector,
) -> Temp31LaborResult:
    """Normalize each origin column; multiply household labor and N once only."""
    n = len(inputs.consumption_by_origin)
    labor = _vector("household_labor_per_capita_by_origin", household_labor_per_capita_by_origin, n)
    if any(x < 0 for x in labor):
        raise ValueError("household labor must be non-negative")
    q = _temp31_attractiveness(inputs)
    totals = tuple(sum(row[i] for row in q) for i in range(n))
    if any(not isfinite(x) or x <= 0 for x in totals):
        raise ValueError("each origin kernel column needs a positive finite total")
    shares = tuple(tuple(row[i] / totals[i] for i in range(n)) for row in q)
    mass = tuple(_nonnegative(labor[i] * inputs.population_by_origin[i], "origin mass") for i in range(n))
    flows = tuple(tuple(_nonnegative(row[i] * mass[i], "bilateral flow") for i in range(n)) for row in shares)
    supply = tuple(_nonnegative(sum(row), "destination row sum") for row in flows)
    for i in range(n):
        if not isclose(sum(row[i] for row in shares), 1.0, rel_tol=1e-12, abs_tol=1e-12):
            raise ValueError("origin shares do not sum to one")
        if not isclose(sum(row[i] for row in flows), mass[i], rel_tol=1e-12, abs_tol=1e-12):
            raise ValueError("origin labor mass is not conserved")
    residual = sum(supply) - sum(mass)
    if not isfinite(residual) or not isclose(residual, 0.0, rel_tol=1e-12, abs_tol=1e-12):
        raise ValueError("national labor conservation failed")
    return Temp31LaborResult(flows, supply, q, shares, mass, residual)


@dataclass(frozen=True)
class Temp31SingleClassWage:
    """Pure proposed HA wage semantics, not a shared HouseholdInputs instance."""
    w_for_HA: float
    tau_for_HA: float = 0.0
    sigma_for_HA: float = 0.0
    labor_weight_for_HA: float = 1.0

    def __post_init__(self) -> None:
        _nonnegative(float(self.w_for_HA), "net composite wage")
        if (self.tau_for_HA, self.sigma_for_HA, self.labor_weight_for_HA) != (0.0, 0.0, 1.0):
            raise ValueError("already-net single-class wage requires zero additional tax/wedge and unit weight")
        object.__setattr__(self, "w_for_HA", float(self.w_for_HA))

    @property
    def effective_wage(self) -> float:
        return self.w_for_HA * (1 - self.tau_for_HA - self.sigma_for_HA)


@dataclass(frozen=True)
class Temp31NetWageViews:
    initialization: tuple[Temp31SingleClassWage, ...]
    hjb: tuple[Temp31SingleClassWage, ...]
    tax_by_destination: Vector
    migration_wedge_destination_origin: Matrix
    semantic: str = NET_COMPOSITE


def adapt_temp31_net_composite_wage(
    net_wage_by_origin: Vector, *, semantic: str,
    tax_by_destination: Vector, migration_wedge_destination_origin: Matrix,
) -> Temp31NetWageViews:
    """Supply one immutable net-wage contract to both future consumer phases.

    The caller must establish actual net-wage provenance. A semantic label
    alone cannot certify a production default wage; production stays unwired.
    Original destination taxes and migration wedges remain separate data.
    """
    if semantic != NET_COMPOSITE:
        raise ValueError("requires proven NET_COMPOSITE wage semantics")
    wages = _vector("net_wage_by_origin", net_wage_by_origin)
    n = len(wages)
    taxes = _vector("tax_by_destination", tax_by_destination, n)
    sigma = _matrix("migration_wedge_destination_origin", migration_wedge_destination_origin, n)
    single_class = tuple(Temp31SingleClassWage(value) for value in wages)
    return Temp31NetWageViews(single_class, single_class, taxes, sigma)


@dataclass(frozen=True)
class Temp31ConditionalTaxDiagnostic:
    legacy_lt_times_tau: Vector
    conditional_wage_tax: Vector
    conditional_national_tax: float
    scientific_status: str = "SCIENTIFIC_PENDING"
    assumption: str = "L assumed already effective and population-aggregated; units and incidence unresolved"


def diagnose_temp31_conditional_wage_tax(
    tax_by_destination: Vector, gross_wage_by_destination: Vector,
    assumed_effective_labor_by_destination: Vector,
) -> Temp31ConditionalTaxDiagnostic:
    """Compare tau*L and conditional tau*w*L; never replace formal Govinc.

    Neither N nor z nor sigma is multiplied here. Their economic/measurement
    contracts and any wage clipping remain scientific gaps.
    """
    taxes = _vector("tax_by_destination", tax_by_destination)
    wages = _vector("gross_wage_by_destination", gross_wage_by_destination, len(taxes))
    labor = _vector("assumed_effective_labor_by_destination", assumed_effective_labor_by_destination, len(taxes))
    if any(x < 0 for x in (*wages, *labor)):
        raise ValueError("conditional wages and labor must be non-negative")
    legacy = tuple(t * l for t, l in zip(taxes, labor))
    conditional = tuple(t * w * l for t, w, l in zip(taxes, wages, labor))
    total = sum(conditional)
    if not all(map(isfinite, (*legacy, *conditional, total))):
        raise ValueError("conditional tax diagnostic overflow")
    return Temp31ConditionalTaxDiagnostic(legacy, conditional, total)
