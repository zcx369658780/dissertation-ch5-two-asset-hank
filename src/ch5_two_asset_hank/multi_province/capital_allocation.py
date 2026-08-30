"""At-only productive-capital allocation and literal household ``rah``.

Authority: ``HANK_mp_1turn.m:29-40``.  Liquid ``Bt`` is absent from this API by
construction and therefore cannot affect productive capital.
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


@dataclass(frozen=True)
class CapitalAllocationInputs:
    """Old-turn source objects; deliberately no liquid-asset ``Bt`` field."""

    illiquid_assets_at: np.ndarray
    population: np.ndarray
    inter_province_ratio: np.ndarray
    old_firm_return_ra: np.ndarray

    def __post_init__(self) -> None:
        assets = _readonly_vector("illiquid_assets_at", self.illiquid_assets_at)
        n = assets.size
        population = _readonly_vector("population", self.population, n)
        ratios = _readonly_vector("inter_province_ratio", self.inter_province_ratio, n)
        returns = _readonly_vector("old_firm_return_ra", self.old_firm_return_ra, n)
        if np.any(assets < 0.0) or np.any(population <= 0.0):
            raise ValueError("At must be non-negative and population strictly positive")
        if np.any((ratios < 0.0) | (ratios > 1.0)):
            raise ValueError("inter_province_ratio must lie in [0, 1]")
        object.__setattr__(self, "illiquid_assets_at", assets)
        object.__setattr__(self, "population", population)
        object.__setattr__(self, "inter_province_ratio", ratios)
        object.__setattr__(self, "old_firm_return_ra", returns)


@dataclass(frozen=True)
class CapitalAllocationResult:
    productive_contribution: np.ndarray
    kt_supply: np.ndarray
    household_illiquid_return_rah: np.ndarray

    def __post_init__(self) -> None:
        contribution = _readonly_vector("productive_contribution", self.productive_contribution)
        n = contribution.size
        supply = _readonly_vector("kt_supply", self.kt_supply, n)
        returns = _readonly_vector(
            "household_illiquid_return_rah", self.household_illiquid_return_rah, n
        )
        if np.any(contribution < 0.0) or np.any(supply < 0.0):
            raise ValueError("productive-capital contribution and supply must be non-negative")
        object.__setattr__(self, "productive_contribution", contribution)
        object.__setattr__(self, "kt_supply", supply)
        object.__setattr__(self, "household_illiquid_return_rah", returns)


def allocate_productive_capital(inputs: CapitalAllocationInputs) -> CapitalAllocationResult:
    """Apply the literal source exclusion/division and ``rah`` ratio placement."""

    n = inputs.illiquid_assets_at.size
    contributions = np.array(
        [
            inputs.inter_province_ratio[i]
            * inputs.illiquid_assets_at[i]
            * inputs.population[i]
            for i in range(n)
        ],
        dtype=float,
    )
    total_capital = sum(float(value) for value in contributions)
    total_return = sum(
        float(inputs.inter_province_ratio[i] * inputs.old_firm_return_ra[i])
        for i in range(n)
    )
    kt_supply = np.array(
        [(total_capital - contributions[i]) / (n - 1) for i in range(n)],
        dtype=float,
    )
    rah = np.array(
        [
            (1.0 - inputs.inter_province_ratio[i]) * inputs.old_firm_return_ra[i]
            + inputs.inter_province_ratio[i]
            * (
                total_return
                - inputs.inter_province_ratio[i] * inputs.old_firm_return_ra[i]
            )
            / (n - 1)
            for i in range(n)
        ],
        dtype=float,
    )
    return CapitalAllocationResult(
        productive_contribution=contributions,
        kt_supply=kt_supply,
        household_illiquid_return_rah=rah,
    )
