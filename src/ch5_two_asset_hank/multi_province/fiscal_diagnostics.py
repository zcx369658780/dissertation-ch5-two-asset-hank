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


def mainline_fiscal_accounts(states, firms, household, rb):
    """Population bridge only on household means; clip compensation stays visible."""
    rows = []
    for i, (state, firm) in enumerate(zip(states, firms)):
        n = float(state['N'])
        wage_tax = state['tau'] * firm.wt0 * firm.Lt
        asset_tax = n * float(household.at_tax[i])
        transfers = n * state['Tt']
        income = firm.Corptax + wage_tax + asset_tax + state['GovInv']*firm.ra - transfers
        if abs(income-firm.Govinc) > 1e-12*max(1.0,abs(income)):
            raise ValueError('firm and fiscal total accounts disagree')
        rows.append({'wage_tax':wage_tax,'asset_return_gap_total':asset_tax,
                     'transfers_total':transfers,'corporate_tax_with_clip_compensation':firm.Corptax,
                     'government_capital_income':state['GovInv']*firm.ra,'GovInc':income,
                     'household_labor_population_bridge':n*float(household.household_lt[i]),
                     'firm_labor':firm.Lt,
                     'labor_bridge_residual':firm.Lt-n*float(household.household_lt[i])})
    diagnostic = national_fiscal_diagnostics([r['GovInc'] for r in rows], household.bt, rb,
                                            [s['N'] for s in states])
    return {'provinces':rows,'GovSurplus':diagnostic.GovSurplus,'budget_zero_imposed':False}
