"""Deterministic helpers for the 2018 official-data identity closure.

This module contains no model, solver, interpolation, or estimation entry point.
"""

from __future__ import annotations

import hashlib
import math
from pathlib import Path


REQUIRED_INVESTMENT_YEARS = tuple(range(2000, 2018))
NOT_REQUIRED_INVESTMENT_YEAR = 2018


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def investment_years_for_stock(stock_year: int, initial_year: int = 2000) -> tuple[int, ...]:
    """Return investment years used by K0=I0/.1; Kt=(1-d)K(t-1)+I(t-1)."""
    if stock_year < initial_year:
        raise ValueError("stock year precedes initial year")
    return tuple(range(initial_year, stock_year)) if stock_year > initial_year else (initial_year,)


def frozen_capital_recurrence(investment: list[float], depreciation: float = 0.096) -> list[float]:
    if not investment:
        raise ValueError("investment vector is empty")
    if any(not math.isfinite(float(value)) for value in investment):
        raise ValueError("investment vector must be finite")
    capital = [float(investment[0]) / 0.1]
    for value in investment[:-1]:
        capital.append((1.0 - depreciation) * capital[-1] + float(value))
    return capital


def relative_difference(left: float, right: float) -> float | None:
    if right == 0:
        return None
    return (left - right) / right


def transformed_value(variable: str, raw_value: float) -> float:
    multiplier = {"GDP": 1000.0, "POP": 100.0, "CAP": 1000.0}[variable]
    return float(raw_value) * multiplier
