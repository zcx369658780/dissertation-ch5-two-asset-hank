"""Validation-only composition matching MATLAB's nonconverged-HJB post-loop path."""

from __future__ import annotations

from typing import Callable

from exports.matlab_faithful_two_asset_ha import (
    HouseholdSteadyStateResult,
    aggregate_stationary_household,
    solve_matlab_faithful_hjb,
    solve_matlab_faithful_stationary_kfe,
)


def solve_matlab_source_postloop_household(
    grid,
    params,
    inputs,
    initial_value,
    baseline_labor,
    transfer_income,
    borrowing_rate_gap,
    numerics,
    *,
    hjb_solver: Callable = solve_matlab_faithful_hjb,
    kfe_solver: Callable = solve_matlab_faithful_stationary_kfe,
    aggregator: Callable = aggregate_stationary_household,
) -> HouseholdSteadyStateResult:
    """Compose accepted primitives without treating ``hjb.converged`` as an exception."""
    hjb = hjb_solver(
        grid, params, inputs, initial_value, baseline_labor,
        transfer_income, borrowing_rate_gap, numerics,
    )
    shape = (grid.b.size, grid.a.size, grid.z.size)
    db = float(grid.b[1] - grid.b[0])
    da = float(grid.a[1] - grid.a[0])
    kfe = kfe_solver(
        hjb.post_convergence_operator.full, shape=shape, db=db, da=da,
    )
    aggregates = aggregator(grid, hjb.consumption, hjb.labor, kfe.density)
    return HouseholdSteadyStateResult(hjb, kfe, aggregates)


__all__ = ["solve_matlab_source_postloop_household"]
