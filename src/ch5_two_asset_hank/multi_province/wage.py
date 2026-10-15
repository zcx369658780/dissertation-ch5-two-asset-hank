"""Household composite wage from ``wage_caculate.m:4-16``."""

from __future__ import annotations

from math import isfinite
from typing import Mapping, Sequence

import numpy as np


def composite_household_wages(
    provinces: Sequence[Mapping[str, float]],
    firm_wages: Sequence[float],
    phi_mat: Sequence[Sequence[float]],
    sigmau_mat: Sequence[Sequence[float]],
    *,
    phi_l: float,
    alphal: float,
) -> tuple[float, ...]:
    """Return one composite wage per origin household province.

    Rows are destinations and columns are origins.  The MATLAB wage formula
    intentionally indexes ``tau`` by destination, unlike ``Lt_seperate``.
    """

    count = len(provinces)
    if count < 1 or len(firm_wages) != count:
        raise ValueError("provinces and firm_wages must have the same nonzero length")
    phi = np.asarray(phi_mat, dtype=float)
    sigma = np.asarray(sigmau_mat, dtype=float)
    wages = np.asarray(firm_wages, dtype=float)
    if phi.shape != (count, count) or sigma.shape != (count, count):
        raise ValueError("phi_mat and sigmau_mat must have shape (destination, origin)")
    if not np.isfinite(phi).all() or not np.isfinite(sigma).all() or not np.isfinite(wages).all():
        raise ValueError("wage inputs must be finite")
    if np.any(phi <= 0.0):
        raise ValueError("phi_mat labor-disutility entries must be positive")
    phi_l = float(phi_l)
    alphal = float(alphal)
    if not isfinite(phi_l) or phi_l <= 0.0 or not isfinite(alphal) or alphal <= 0.0:
        raise ValueError("phi_l and alphal must be finite and positive")
    taxes = []
    for province in provinces:
        try:
            tax = float(province["tau"])
        except KeyError as exc:
            raise ValueError("every province requires destination tau") from exc
        if not isfinite(tax):
            raise ValueError("destination tau must be finite")
        taxes.append(tax)

    exponent = 1.0 + 1.0 / phi_l
    outer_exponent = phi_l / (1.0 + phi_l)
    output: list[float] = []
    for origin in range(count):
        total = 0.0
        for destination in range(count):
            divisor = phi[destination, origin]
            base = (
                wages[destination]
                * (1.0 - taxes[destination] - sigma[destination, origin])
                / divisor
            )
            if base < 0.0:
                raise ValueError("wage_caculate source power base would be negative/non-real")
            term = divisor * base**exponent
            if not isfinite(term):
                raise ValueError("wage_caculate term must be finite")
            total += term
        if total < 0.0:
            raise ValueError("wage_caculate outer power base would be negative/non-real")
        value = alphal ** (-outer_exponent) * total**outer_exponent
        if not isfinite(value) or value < 0.0:
            raise ValueError("wage_caculate produced an invalid composite wage")
        output.append(value)
    return tuple(output)


def mainline_phi(pgdp_reference):
    """Frozen reference, destination rows/origin columns, richer destination preferred."""
    p = np.asarray(pgdp_reference, dtype=float)
    if p.ndim != 1 or not np.isfinite(p).all() or np.any(p <= 0):
        raise ValueError('pgdp reference must be a positive finite vector')
    return 1.0 + 0.3 * (p[None, :] - p[:, None]) / (p[None, :] + p[:, None])


def mainline_effective_wages(gross_wages, destination_taxes, phi, sigma, *, phi_l, alphal):
    """Net composite wage; feed to HA with tau_HA=0 (no second deduction)."""
    wages, taxes = np.asarray(gross_wages, dtype=float), np.asarray(destination_taxes, dtype=float)
    provinces = tuple({'tau': float(t)} for t in taxes)
    return np.asarray(composite_household_wages(provinces, wages, phi, sigma,
                                               phi_l=phi_l, alphal=alphal))
