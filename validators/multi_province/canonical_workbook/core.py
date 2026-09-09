"""Pure static helpers for the Chapter 5 canonical data workbook."""

from __future__ import annotations

import math
from collections.abc import Iterable, Sequence


REQUIRED_SHEETS = (
    "README_METADATA",
    "PROVINCE_ORDER",
    "ANNUAL_BINDING_2009_2023",
    "GDP_2000_2023",
    "POP_2000_2023",
    "INVESTMENT_2000_2023",
    "PIM_CAPITAL_2000_2023",
    "PLM_ALPHA_2009_2023",
    "ZT_SAMEYEAR_2009_2023",
    "ANHUI_2018_FINAL_INPUT",
    "SOURCE_PROVENANCE",
    "DATA_QUALITY_FLAGS",
)


def matches_at_published_precision(
    provisional: float, official: float, decimal_places: int
) -> bool:
    """Compare a provisional value at the precision published by the authority."""

    if decimal_places < 0:
        raise ValueError("decimal_places must be nonnegative")
    values = (float(provisional), float(official))
    if not all(math.isfinite(value) for value in values):
        raise ValueError("comparison values must be finite")
    return round(values[0], decimal_places) == round(values[1], decimal_places)


def pim_path(
    investment: Iterable[float], depreciation: float = 0.096, divisor: float = 0.1
) -> list[float]:
    """Return K2000..K(last investment year + 1) under the frozen timing rule."""

    flows = [float(value) for value in investment]
    if not flows or not all(math.isfinite(value) for value in flows):
        raise ValueError("investment must be a nonempty finite sequence")
    if not 0.0 <= depreciation < 1.0 or divisor <= 0.0:
        raise ValueError("invalid frozen PIM parameters")
    result = [flows[0] / divisor]
    for flow in flows:
        result.append((1.0 - depreciation) * result[-1] + flow)
    return result


def same_year_zt(gdp: float, capital: float, population: float, alpha: float) -> float:
    """Apply the frozen same-year Zt formula to already transformed inputs."""

    values = tuple(float(value) for value in (gdp, capital, population, alpha))
    if not all(math.isfinite(value) for value in values):
        raise ValueError("Zt inputs must be finite")
    if min(values[:3]) <= 0.0:
        raise ValueError("GDP, capital, and population must be positive")
    return values[0] * values[1] ** (-values[3]) * values[2] ** (values[3] - 1.0)


def required_sheets_present(actual: Sequence[str]) -> bool:
    """Require the exact versioned canonical sheet order."""

    return tuple(actual) == REQUIRED_SHEETS
