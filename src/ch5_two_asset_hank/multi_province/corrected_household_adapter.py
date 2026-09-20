"""Opt-in aggregate adapter for an already accepted corrected household object.

This module performs deterministic reductions only.  It has no solver entry
point and requires every policy, state, return, and mass input explicitly.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np

from .household_adapter import FrozenHouseholdOutputs


FLATTEN_ORDER = "F"
AXIS_ORDER = ("b", "a", "z")


def _readonly_array(name: str, value: np.ndarray, shape: tuple[int, ...]) -> np.ndarray:
    array = np.array(value, dtype=np.float64, copy=True, order="F")
    if array.shape != shape:
        raise ValueError(f"{name} must have shape {shape!r} in (b,a,z) axis order")
    if not np.isfinite(array).all():
        raise ValueError(f"{name} must be finite")
    array.flags.writeable = False
    return array


def _gamma(count: int) -> float:
    epsilon = np.finfo(np.float64).eps
    numerator = count * epsilon
    return numerator / (1.0 - numerator)


@dataclass(frozen=True)
class CorrectedHouseholdAggregateInputs:
    consumption: np.ndarray
    labor: np.ndarray
    b_grid: np.ndarray
    a_grid: np.ndarray
    z_grid: np.ndarray
    effective_r_a: np.ndarray
    probability_mass: np.ndarray
    density: np.ndarray
    omega: float
    source_r_a: float

    def __post_init__(self) -> None:
        b = np.asarray(self.b_grid, dtype=np.float64)
        a = np.asarray(self.a_grid, dtype=np.float64)
        z = np.asarray(self.z_grid, dtype=np.float64)
        for name, axis in (("b_grid", b), ("a_grid", a), ("z_grid", z)):
            if (
                axis.ndim != 1
                or axis.size < 1
                or not np.isfinite(axis).all()
                or (axis.size > 1 and not np.all(np.diff(axis) > 0.0))
            ):
                raise ValueError(f"{name} must be a finite strictly increasing axis")
        shape = (b.size, a.size, z.size)
        for name in (
            "consumption",
            "labor",
            "effective_r_a",
            "probability_mass",
            "density",
        ):
            object.__setattr__(self, name, _readonly_array(name, getattr(self, name), shape))
        for name, axis in (("b_grid", b), ("a_grid", a), ("z_grid", z)):
            frozen = np.array(axis, dtype=np.float64, copy=True)
            frozen.flags.writeable = False
            object.__setattr__(self, name, frozen)
        omega = float(self.omega)
        source_r_a = float(self.source_r_a)
        if not math.isfinite(omega) or omega <= 0.0:
            raise ValueError("omega must be finite and positive")
        if not math.isfinite(source_r_a):
            raise ValueError("source_r_a must be finite")
        object.__setattr__(self, "omega", omega)
        object.__setattr__(self, "source_r_a", source_r_a)

        p = self.probability_mass.ravel(order=FLATTEN_ORDER)
        g = self.density.ravel(order=FLATTEN_ORDER)
        discrepancy = np.abs(p - omega * g)
        bound = _gamma(p.size + 2) * np.maximum.reduce(
            (np.ones_like(p), np.abs(p), np.abs(omega * g))
        )
        if np.any(discrepancy > bound):
            raise ValueError("probability_mass and density*omega are inconsistent")


@dataclass(frozen=True)
class AggregateComparison:
    mass_form: float
    density_form: float
    absolute_difference: float
    prospective_bound: float
    equivalent: bool


@dataclass(frozen=True)
class CorrectedHouseholdAggregates:
    Ct: AggregateComparison
    Lt: AggregateComparison
    At: AggregateComparison
    Bt: AggregateComparison
    total_assets: AggregateComparison
    AtTax: AggregateComparison
    flatten_order: str = FLATTEN_ORDER
    axis_order: tuple[str, str, str] = AXIS_ORDER

    def frozen_output(
        self, *, converged: bool, convergence_statistic: float
    ) -> FrozenHouseholdOutputs:
        """Expose the existing output contract only through this opt-in object."""

        return FrozenHouseholdOutputs(
            Ct=self.Ct.mass_form,
            Lt=self.Lt.mass_form,
            At=self.At.mass_form,
            Bt=self.Bt.mass_form,
            AtTax=self.AtTax.mass_form,
            converged=converged,
            convergence_statistic=convergence_statistic,
        )


def _comparison(
    mass_terms: np.ndarray,
    density_terms: np.ndarray,
    omega: float,
) -> AggregateComparison:
    mass = float(math.fsum(float(item) for item in mass_terms))
    density = float(omega * math.fsum(float(item) for item in density_terms))
    difference = abs(mass - density)
    scale = max(
        1.0,
        math.fsum(abs(float(item)) for item in mass_terms),
        abs(omega) * math.fsum(abs(float(item)) for item in density_terms),
    )
    bound = float(_gamma(mass_terms.size + 3) * scale)
    return AggregateComparison(
        mass_form=mass,
        density_form=density,
        absolute_difference=difference,
        prospective_bound=bound,
        equivalent=bool(difference <= bound),
    )


def evaluate_corrected_household_aggregates(
    inputs: CorrectedHouseholdAggregateInputs,
) -> CorrectedHouseholdAggregates:
    """Evaluate source aggregates once, using F-order with ``b`` fastest.

    ``AtTax`` follows the protected MATLAB source exactly:
    ``At * source_r_a - sum(a * effective_r_a * mass)``.
    It is the aggregate illiquid-return flow gap between the uniform source
    return and the state-dependent tapered return used by the household.
    """

    shape = inputs.consumption.shape
    b = np.broadcast_to(inputs.b_grid[:, None, None], shape).ravel(order=FLATTEN_ORDER)
    a = np.broadcast_to(inputs.a_grid[None, :, None], shape).ravel(order=FLATTEN_ORDER)
    z = np.broadcast_to(inputs.z_grid[None, None, :], shape).ravel(order=FLATTEN_ORDER)
    c = inputs.consumption.ravel(order=FLATTEN_ORDER)
    labor = inputs.labor.ravel(order=FLATTEN_ORDER)
    effective_r_a = inputs.effective_r_a.ravel(order=FLATTEN_ORDER)
    p = inputs.probability_mass.ravel(order=FLATTEN_ORDER)
    g = inputs.density.ravel(order=FLATTEN_ORDER)

    ct = _comparison(c * p, c * g, inputs.omega)
    lt = _comparison(z * labor * p, z * labor * g, inputs.omega)
    at = _comparison(a * p, a * g, inputs.omega)
    bt = _comparison(b * p, b * g, inputs.omega)
    total_assets = AggregateComparison(
        mass_form=at.mass_form + bt.mass_form,
        density_form=at.density_form + bt.density_form,
        absolute_difference=abs(
            (at.mass_form + bt.mass_form) - (at.density_form + bt.density_form)
        ),
        prospective_bound=at.prospective_bound + bt.prospective_bound,
        equivalent=bool(
            abs((at.mass_form + bt.mass_form) - (at.density_form + bt.density_form))
            <= at.prospective_bound + bt.prospective_bound
        ),
    )
    tapered_mass_terms = a * effective_r_a * p
    tapered_density_terms = a * effective_r_a * g
    at_tax_mass_terms = np.concatenate(
        (np.array([at.mass_form * inputs.source_r_a]), -tapered_mass_terms)
    )
    at_tax_density_terms = np.concatenate(
        (np.array([at.density_form * inputs.source_r_a / inputs.omega]), -tapered_density_terms)
    )
    at_tax = _comparison(at_tax_mass_terms, at_tax_density_terms, inputs.omega)
    result = CorrectedHouseholdAggregates(
        Ct=ct,
        Lt=lt,
        At=at,
        Bt=bt,
        total_assets=total_assets,
        AtTax=at_tax,
    )
    if not all(
        getattr(result, name).equivalent
        for name in ("Ct", "Lt", "At", "Bt", "total_assets", "AtTax")
    ):
        raise ValueError("mass-form and density-form aggregate reductions disagree")
    return result
