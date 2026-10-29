"""Isolated Owner-approved numerical bootstrap and tax-free HA input type.

19 is a numerical guess, never an empirical wage or tax-incidence proof.
Historical initialization algebra appended below is source-derived, not run.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping
import numpy as np
from scipy.optimize import brentq

from .temp31_ha_wage_debug import (
    CALCULATED_NET_AFTER_DESTINATION_TAU_AND_SIGMA, WageRoundRecord,
    prepare_proposed_consumers,
)

SOURCE_COMMIT = "5f55365d2aff6bd1517a567e2bcaf17452960a7e"
NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL = "NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL"


@dataclass(frozen=True)
class Temp31EffectiveWageRecord:
    semantics: str
    entering_iteration: int
    context_id: str
    province_order: tuple[str, ...]
    effective_wages_by_origin: tuple[float, ...]
    tax_by_destination: tuple[float, ...]
    sigma_destination_origin: tuple[tuple[float, ...], ...]
    w_initial: float | None = None
    tau_legacy_reference: float | None = None
    producer_record: WageRoundRecord | None = None
    source_commit: str = SOURCE_COMMIT

    def __post_init__(self) -> None:
        object.__setattr__(self, "province_order", tuple(self.province_order))
        object.__setattr__(self, "effective_wages_by_origin", tuple(float(x) for x in self.effective_wages_by_origin))
        object.__setattr__(self, "tax_by_destination", tuple(float(x) for x in self.tax_by_destination))
        object.__setattr__(self, "sigma_destination_origin", tuple(tuple(float(x) for x in row) for row in self.sigma_destination_origin))
        validate_effective_wage_record(self)


def validate_effective_wage_record(record: Temp31EffectiveWageRecord) -> tuple[float, ...]:
    if not isinstance(record, Temp31EffectiveWageRecord) or record.source_commit != SOURCE_COMMIT:
        raise ValueError("incorrect frozen effective-wage record identity")
    n = len(record.province_order)
    if (n < 2 or len(set(record.province_order)) != n
            or any(not isinstance(x, str) or not x for x in record.province_order)
            or not isinstance(record.context_id, str) or not record.context_id
            or type(record.entering_iteration) is not int or record.entering_iteration < 1):
        raise ValueError("invalid context/order/iteration")
    wages = tuple(float(x) for x in record.effective_wages_by_origin)
    taxes = tuple(float(x) for x in record.tax_by_destination)
    sigma = tuple(tuple(float(x) for x in row) for row in record.sigma_destination_origin)
    if len(wages) != n or len(taxes) != n or len(sigma) != n or any(len(row) != n for row in sigma):
        raise ValueError("wage/mechanism shape mismatch")
    if not np.isfinite((*wages, *taxes, *(x for row in sigma for x in row))).all() or any(w < 0 for w in wages):
        raise ValueError("wages and mechanism data must be finite")
    if record.semantics == NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL:
        if (record.entering_iteration != 1 or record.w_initial != 20.0 or record.tau_legacy_reference != 0.05
                or wages != (19.0,) * n or record.producer_record is not None):
            raise ValueError("bootstrap requires the exact Owner-approved 20*(1-.05)=19 first-round contract")
    elif record.semantics == CALCULATED_NET_AFTER_DESTINATION_TAU_AND_SIGMA:
        if record.w_initial is not None or record.tau_legacy_reference is not None or not isinstance(record.producer_record, WageRoundRecord):
            raise ValueError("later wages require the unchanged R5 producing witness")
        producer = record.producer_record
        proposal = prepare_proposed_consumers(producer)
        if (record.entering_iteration != producer.entering_iteration or record.context_id != producer.context_id
                or record.province_order != producer.province_order
                or wages != tuple(x.effective_wage for x in proposal.views.hjb)
                or taxes != proposal.views.tax_by_destination
                or sigma != proposal.views.migration_wedge_destination_origin):
            raise ValueError("later wage source/order/context/tax/wedge drift")
    else:
        raise ValueError("unapproved wage source semantics")
    return wages


def numerical_bootstrap19(*, context_id: str, province_order: tuple[str, ...],
    tax_by_destination, sigma_destination_origin, w_initial: float = 20.0,
    tau_legacy_reference: float = 0.05) -> Temp31EffectiveWageRecord:
    if w_initial != 20.0 or tau_legacy_reference != 0.05:
        raise ValueError("changed numerical initial values require new Owner authorization")
    order = tuple(province_order)
    guess = float(w_initial) * (1.0 - float(tau_legacy_reference))
    record = Temp31EffectiveWageRecord(NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL,
        1, context_id, order, (guess,) * len(order), tuple(float(x) for x in tax_by_destination),
        tuple(tuple(float(x) for x in row) for row in sigma_destination_origin),
        float(w_initial), float(tau_legacy_reference))
    validate_effective_wage_record(record)
    return record


def later_net_wage_record(producer: WageRoundRecord) -> Temp31EffectiveWageRecord:
    proposal = prepare_proposed_consumers(producer)
    record = Temp31EffectiveWageRecord(CALCULATED_NET_AFTER_DESTINATION_TAU_AND_SIGMA,
        producer.entering_iteration, producer.context_id, producer.province_order,
        tuple(x.effective_wage for x in proposal.views.hjb), proposal.views.tax_by_destination,
        proposal.views.migration_wedge_destination_origin, producer_record=producer)
    validate_effective_wage_record(record)
    return record


@dataclass(frozen=True)
class Temp31NetWageInputs:
    """New wage-only consumer type: no tau or migration_costs parameter."""
    r_a: float
    r_b: float
    wages: np.ndarray
    labor_weights: np.ndarray
    wage_record: Temp31EffectiveWageRecord
    origin_index: int
    expected_context_id: str
    expected_province_order: tuple[str, ...]

    def __post_init__(self) -> None:
        expected = validate_effective_wage_record(self.wage_record)
        if self.expected_context_id != self.wage_record.context_id or tuple(self.expected_province_order) != self.wage_record.province_order:
            raise ValueError("consumer context/province order does not match the wage record")
        if type(self.origin_index) is not int or not 0 <= self.origin_index < len(expected):
            raise ValueError("origin index invalid")
        wages = np.array(self.wages, dtype=float, copy=True)
        weights = np.array(self.labor_weights, dtype=float, copy=True)
        if (wages.shape != (1,) or weights.shape != (1,) or not np.isfinite(wages).all()
                or not np.isfinite(weights).all() or wages[0] <= 0 or weights[0] <= 0
                or wages[0] != expected[self.origin_index] or not np.isfinite([self.r_a, self.r_b]).all()):
            raise ValueError("net consumer inputs do not match the effective-wage record")
        wages.flags.writeable = False; weights.flags.writeable = False
        object.__setattr__(self, "wages", wages); object.__setattr__(self, "labor_weights", weights)
        object.__setattr__(self, "expected_province_order", tuple(self.expected_province_order))


def require_netwage_inputs(inputs: Temp31NetWageInputs) -> None:
    if not isinstance(inputs, Temp31NetWageInputs):
        raise TypeError("TEMP31 corrected consumer requires the new tax-free wage contract")
    expected = validate_effective_wage_record(inputs.wage_record)
    if inputs.expected_context_id != inputs.wage_record.context_id or inputs.expected_province_order != inputs.wage_record.province_order:
        raise ValueError("consumer context/province order changed")
    if inputs.wages.shape != (1,) or inputs.wages[0] != expected[inputs.origin_index]:
        raise ValueError("effective consumer wage was changed")


def netwage_inputs(record: Temp31EffectiveWageRecord, *, origin_index: int,
    r_a: float, r_b: float, expected_context_id: str,
    expected_province_order: tuple[str, ...]) -> Temp31NetWageInputs:
    wages = validate_effective_wage_record(record)
    if type(origin_index) is not int or not 0 <= origin_index < len(wages):
        raise ValueError("origin index invalid")
    return Temp31NetWageInputs(r_a, r_b, np.array([wages[origin_index]]), np.array([1.0]), record, origin_index,
        expected_context_id, expected_province_order)


# Source-derived initialization helpers; no initializer/root/HA calls in this task.
def _temp31_source_labor_root(
    *, wage: float, temp: float, alphac: float = 1.0, alphal: float = 1.0,
    frisch_l: float = 0.2, ga: float = 2.0, max_search: int = 128,
) -> tuple[float, tuple[float, float]]:
    """Solve the unchanged lab_solve2 residual only on its real-valued domain."""
    values = (wage, temp, alphac, alphal, frisch_l, ga)
    if not all(np.isfinite(value) for value in values):
        raise ValueError("source labor parameters must be finite")
    if wage <= 0 or alphac <= 0 or alphal <= 0 or frisch_l <= 0 or ga <= 0:
        raise ValueError("source labor parameters are outside the frozen positive regime")
    power = ga * frisch_l
    coefficient = (alphac / alphal * wage) ** frisch_l
    x0 = wage ** (frisch_l * (1.0 - ga) / (1.0 + ga * frisch_l))
    boundary = -temp / wage

    def residual(labor: float) -> float:
        base = labor * wage + temp
        if not np.isfinite(labor) or not base > 0:
            raise ValueError("labor residual evaluation outside the real-valued source domain")
        return labor - coefficient * base ** (-power)

    if not x0 > boundary:
        raise ValueError("source x0 is outside the real-valued labor domain")
    at_x0 = residual(x0)
    if at_x0 == 0:
        return x0, (x0, x0)
    if at_x0 < 0:
        lo, hi = x0, max(1.0, 2.0 * x0)
        for _ in range(max_search):
            if residual(hi) > 0:
                break
            hi *= 2.0
        else:
            raise RuntimeError("finite upward labor bracket search exhausted")
    else:
        hi = x0
        lo = 0.5 * (boundary + hi)
        for _ in range(max_search):
            if residual(lo) < 0:
                break
            lo = 0.5 * (boundary + lo)
        else:
            raise RuntimeError("finite interior labor bracket search exhausted")
    root = brentq(residual, lo, hi, xtol=1e-14, rtol=1e-14)
    return float(root), (float(lo), float(hi))


def temp31_netwage_initial_arrays(state: Mapping[str, object], grid: object, params, inputs: Temp31NetWageInputs):
    require_netwage_inputs(inputs)
    from ..temp31_netwage_economics import matlab_faithful_illiquid_return
    shape=(grid.b.size,grid.a.size,grid.z.size); labor=np.empty(shape); value=np.empty(shape)
    for k,z in enumerate(grid.z):
        for j,a in enumerate(grid.a):
            effective=float(matlab_faithful_illiquid_return(a,grid.a[-1],float(state["rah"])))
            for i,b in enumerate(grid.b):
                rb=float(state["rb"])+(float(state["rb_gap"]) if b<0 else 0.0)
                temp=effective*effective+rb*b+float(state["Tt"])
                wage=inputs.wages[0]*z
                l,_=_temp31_source_labor_root(wage=wage,temp=temp,frisch_l=1.0/params.phi,ga=params.gamma_c)
                c=wage*l+rb*b+float(state["Tt"])
                labor[i,j,k]=l
                value[i,j,k]=(c**(1-params.gamma_c)/(1-params.gamma_c)-l**6/6)/params.rho
    return value,labor
