"""Source fiscal diagnostics; no balanced-budget closure is imposed."""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Sequence


@dataclass(frozen=True)
class FiscalDiagnostics:
    Govinc: tuple[float, ...]
    GovSurplus: float


def national_fiscal_diagnostics(
    govinc: Sequence[float],
    bt: Sequence[float],
    rb: float | Sequence[float],
    population: Sequence[float],
) -> FiscalDiagnostics:
    """Compute ``sum(Govinc_i - Bt_i * rb_i * N_i)`` (one-turn lines 61-65)."""

    count = len(govinc)
    if count < 1 or len(bt) != count or len(population) != count:
        raise ValueError("fiscal province vectors must have the same nonzero length")
    if isinstance(rb, (int, float)):
        returns = (float(rb),) * count
    else:
        if len(rb) != count:
            raise ValueError("rb vector must match the province count")
        returns = tuple(float(value) for value in rb)
    incomes = tuple(float(value) for value in govinc)
    liquid_assets = tuple(float(value) for value in bt)
    populations = tuple(float(value) for value in population)
    values = incomes + liquid_assets + returns + populations
    if not all(isfinite(value) for value in values):
        raise ValueError("fiscal diagnostic inputs must be finite")
    if any(value < 0.0 for value in populations):
        raise ValueError("province populations must be non-negative")
    surplus = sum(
        incomes[i] - liquid_assets[i] * returns[i] * populations[i]
        for i in range(count)
    )
    if not isfinite(surplus):
        raise ValueError("GovSurplus must be finite")
    return FiscalDiagnostics(Govinc=incomes, GovSurplus=surplus)
