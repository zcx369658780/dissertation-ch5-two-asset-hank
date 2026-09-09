"""Pure binary64 helpers for the frozen Chapter 5 PIM recurrence.

This module contains no spreadsheet writer, model, solver, interpolation, or
estimation entry point.
"""

from __future__ import annotations

import math
import struct
from collections.abc import Iterable, Sequence


DEPRECIATION = 0.096
INITIAL_DIVISOR = 0.1


def pim_path(
    investment_flows: Iterable[float],
    *,
    depreciation: float = DEPRECIATION,
    initial_divisor: float = INITIAL_DIVISOR,
) -> tuple[float, ...]:
    """Return K0 through K(T+1) from flows I0 through IT.

    The timing matches ``It_to_Kt.m``: K0=I0/0.1 and the next capital value
    uses the previous row's investment flow.
    """
    flows = tuple(float(value) for value in investment_flows)
    if not flows:
        raise ValueError("investment flow sequence is empty")
    if any(not math.isfinite(value) for value in flows):
        raise ValueError("investment flows must be finite")
    if not 0.0 <= depreciation < 1.0:
        raise ValueError("depreciation must be in [0, 1)")
    if not math.isfinite(initial_divisor) or initial_divisor <= 0.0:
        raise ValueError("initial divisor must be positive and finite")

    capital = [flows[0] / initial_divisor]
    retained_share = 1.0 - depreciation
    for flow in flows:
        capital.append(retained_share * capital[-1] + flow)
    return tuple(capital)


def binary64_hex(value: float) -> str:
    """Return the big-endian IEEE-754 binary64 representation."""
    return struct.pack(">d", float(value)).hex().upper()


def binary64_equal(left: float, right: float) -> bool:
    return binary64_hex(left) == binary64_hex(right)


def first_binary64_divergence(
    left: Sequence[float], right: Sequence[float], labels: Sequence[int]
) -> int | None:
    if len(left) != len(right) or len(left) != len(labels):
        raise ValueError("values and labels must have equal lengths")
    for lhs, rhs, label in zip(left, right, labels, strict=True):
        if not binary64_equal(lhs, rhs):
            return label
    return None


def direction(current: float, previous: float) -> str:
    if current > previous:
        return "UP"
    if current < previous:
        return "DOWN"
    return "FLAT"
