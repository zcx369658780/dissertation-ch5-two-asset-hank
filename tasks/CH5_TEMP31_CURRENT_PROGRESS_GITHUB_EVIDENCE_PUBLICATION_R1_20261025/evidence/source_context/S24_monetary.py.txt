"""Literal one-turn Taylor assignment from ``HANK_mp_1turn.m:63-64``."""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class MonetaryResult:
    it: float
    rb: float


def taylor_assignment(
    *, istar: float, rho_pi: float, totalpit: float, epsilon_pi: float
) -> MonetaryResult:
    values = tuple(float(value) for value in (istar, rho_pi, totalpit, epsilon_pi))
    if not all(isfinite(value) for value in values):
        raise ValueError("Taylor inputs must be finite")
    interest = values[0] + values[1] * values[2] + values[3]
    rb = interest - values[2]
    if not isfinite(interest) or not isfinite(rb):
        raise ValueError("Taylor assignment produced a non-finite result")
    return MonetaryResult(it=interest, rb=rb)
