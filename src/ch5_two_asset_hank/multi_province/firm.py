"""Literal feasible steady-state firm branch from ``HANK_firm.m:5-98``."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import isfinite
from typing import Mapping


def _finite(mapping: Mapping[str, float], name: str) -> float:
    try:
        value = float(mapping[name])
    except KeyError as exc:
        raise ValueError(f"missing required firm source field: {name}") from exc
    if not isfinite(value):
        raise ValueError(f"firm source field {name} must be finite")
    return value


@dataclass(frozen=True)
class FirmResult:
    """Auditable source-named outputs of one province's firm block."""

    Kt: float
    Lt: float
    Yt: float
    mt: float
    KNratio: float
    wt0: float
    wjt: float
    rk: float
    Thetat: float
    It: float
    PIt: float
    Corptax: float
    ra0: float
    ra: float
    Govinc: float

    def as_source_dict(self) -> dict[str, float]:
        return asdict(self)


def evaluate_firm(
    province: Mapping[str, float],
    kt_supply: float,
    lt_supply: float,
    params: Mapping[str, float],
) -> FirmResult:
    """Evaluate the MATLAB steady-state branch without solving any model.

    ``lt_supply`` is destination firm labor.  Household aggregate ``Lt`` is
    intentionally not read from ``province``.
    """

    kt_supply = float(kt_supply)
    lt = float(lt_supply)
    if not isfinite(kt_supply) or not isfinite(lt):
        raise ValueError("Kt_supply and Lt_supply must be finite")
    gov_inv = _finite(province, "GovInv")
    kt = kt_supply + gov_inv  # HANK_firm.m:14
    if kt <= 0.0 or lt <= 0.0:
        raise ValueError("firm Kt and destination Lt_supply must be positive")

    alpha = _finite(province, "alpha")
    zt = _finite(province, "Zt")
    if not 0.0 < alpha < 1.0 or zt <= 0.0:
        raise ValueError("firm alpha must be in (0,1) and Zt must be positive")
    epsilon = _finite(params, "epsilon")
    theta = _finite(params, "theta")
    delta = _finite(params, "delta")
    if epsilon == 0.0:
        raise ValueError("epsilon must be nonzero")

    pit = _finite(province, "pit")
    kt_previous = _finite(province, "Kt_prev")
    lt_previous = _finite(province, "Lt_prev")
    zt_previous = _finite(province, "Zt_1")
    pit_previous = _finite(province, "pit_1")
    prior_rk = _finite(province, "rk")
    corptau = _finite(province, "corptau")
    at_tax = _finite(province, "AtTax")
    tau = _finite(province, "tau")
    transfer = _finite(province, "Tt")

    yt = zt * kt**alpha * lt ** (1.0 - alpha)  # line 30
    mstar = 1.0 - 1.0 / epsilon
    mt = (
        (
            prior_rk
            - (zt_previous - zt) / zt
            - alpha * (kt_previous - kt) / kt
            - (1.0 - alpha) * (lt_previous - lt) / lt
        )
        * pit
        * theta
        / epsilon
        + mstar
        - (pit - pit_previous) * theta / epsilon
    )  # line 35, steady-state branch
    knratio = kt / lt
    wt0 = mt * (1.0 - alpha) * zt * knratio**alpha
    rk = mt * alpha / (kt / yt)
    thetat = theta / 2.0 * pit**2 * yt
    investment = kt - kt_previous + delta * kt
    profit = (1.0 - mt) * yt - thetat
    if profit < 0.0:  # lines 48-51
        profit = 0.0
    corporate_tax = profit * corptau
    ra0 = rk - delta + profit * (1.0 - corptau) / kt

    ramin = _finite(province, "ramin")
    ramax = _finite(province, "ramax")
    wjtmin = _finite(province, "wjtmin")
    wjtmax = _finite(province, "wjtmax")
    if ramin > ramax or wjtmin > wjtmax:
        raise ValueError("firm clipping minima must not exceed maxima")
    if ra0 > ramax:  # preserve lines 57-65 ordering
        corporate_tax += (ra0 - ramax) * kt
        ra = ramax
    elif ra0 < ramin:
        corporate_tax -= (ramin - ra0) * kt
        ra = ramin
    else:
        ra = ra0
    if wt0 < wjtmin:  # preserve lines 66-74 ordering
        corporate_tax -= (wjtmin - wt0) * lt
        wjt = wjtmin
    elif wt0 > wjtmax:
        corporate_tax += (wt0 - wjtmax) * lt
        wjt = wjtmax
    else:
        wjt = wt0

    govinc = corporate_tax + lt * tau + at_tax + gov_inv * ra - transfer
    result = FirmResult(
        Kt=kt, Lt=lt, Yt=yt, mt=mt, KNratio=knratio, wt0=wt0, wjt=wjt,
        rk=rk, Thetat=thetat, It=investment, PIt=profit, Corptax=corporate_tax,
        ra0=ra0, ra=ra, Govinc=govinc,
    )
    if not all(isfinite(value) for value in asdict(result).values()):
        raise ValueError("firm arithmetic produced a non-finite output")
    return result
