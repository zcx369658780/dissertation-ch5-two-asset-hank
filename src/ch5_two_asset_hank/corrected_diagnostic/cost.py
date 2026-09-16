"""D3 regularized adjustment cost and transfer KKT arithmetic."""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class CostSubgradient:
    point: float | None
    interval: tuple[float, float]
    scale: float


@dataclass(frozen=True)
class TransferKKTCheck:
    satisfied: bool
    residual: float
    target_interval: tuple[float, float]
    scale: float
    branch: str


def _parameters(*, a: float, chi_0: float, chi_1: float, a_bar: float) -> None:
    if not all(math.isfinite(x) for x in (a, chi_0, chi_1, a_bar)):
        raise ValueError("cost inputs must be finite")
    if a < 0.0:
        raise ValueError("illiquid assets must respect the economic lower bound a >= 0")
    if chi_0 < 0.0 or chi_1 <= 0.0 or a_bar <= 0.0:
        raise ValueError("regularized adjustment-cost parameters are invalid")


def regularized_scale(a: float, *, a_bar: float) -> float:
    if not math.isfinite(a) or not math.isfinite(a_bar) or a < 0.0 or a_bar <= 0.0:
        raise ValueError("regularized scale requires finite a >= 0 and a_bar > 0")
    return max(float(a), float(a_bar))


def regularized_adjustment_cost(
    d: float,
    a: float,
    *,
    chi_0: float,
    chi_1: float,
    a_bar: float,
) -> float:
    _parameters(a=a, chi_0=chi_0, chi_1=chi_1, a_bar=a_bar)
    if not math.isfinite(d):
        raise ValueError("transfer must be finite")
    scale = regularized_scale(a, a_bar=a_bar)
    return float(chi_0 * abs(d) + chi_1 * d * d / (2.0 * scale))


def regularized_adjustment_cost_subgradient(
    d: float,
    a: float,
    *,
    chi_0: float,
    chi_1: float,
    a_bar: float,
) -> CostSubgradient:
    _parameters(a=a, chi_0=chi_0, chi_1=chi_1, a_bar=a_bar)
    if not math.isfinite(d):
        raise ValueError("transfer must be finite")
    scale = regularized_scale(a, a_bar=a_bar)
    if d > 0.0:
        point = chi_0 + chi_1 * d / scale
        return CostSubgradient(float(point), (float(point), float(point)), scale)
    if d < 0.0:
        point = -chi_0 + chi_1 * d / scale
        return CostSubgradient(float(point), (float(point), float(point)), scale)
    return CostSubgradient(None, (-float(chi_0), float(chi_0)), scale)


def check_transfer_kkt(
    *,
    d: float,
    a: float,
    q_a: float,
    q_b: float,
    chi_0: float,
    chi_1: float,
    a_bar: float,
    tolerance: float = 0.0,
) -> TransferKKTCheck:
    """Check ``0 in q_a-q_b*(1+partial_d C)`` without floors or caps."""

    if not all(math.isfinite(x) for x in (q_a, q_b, tolerance)):
        raise ValueError("KKT shadows and tolerance must be finite")
    if q_b <= 0.0:
        raise ValueError("transfer KKT requires q_b > 0; no derivative floor is allowed")
    if tolerance < 0.0:
        raise ValueError("tolerance must be non-negative")
    subgradient = regularized_adjustment_cost_subgradient(
        d, a, chi_0=chi_0, chi_1=chi_1, a_bar=a_bar
    )
    lower = q_b * (1.0 + subgradient.interval[0])
    upper = q_b * (1.0 + subgradient.interval[1])
    if q_a < lower:
        residual = lower - q_a
    elif q_a > upper:
        residual = q_a - upper
    else:
        residual = 0.0
    branch = "positive" if d > 0.0 else "negative" if d < 0.0 else "zero_kink"
    return TransferKKTCheck(
        satisfied=residual <= tolerance,
        residual=float(residual),
        target_interval=(float(lower), float(upper)),
        scale=subgradient.scale,
        branch=branch,
    )
