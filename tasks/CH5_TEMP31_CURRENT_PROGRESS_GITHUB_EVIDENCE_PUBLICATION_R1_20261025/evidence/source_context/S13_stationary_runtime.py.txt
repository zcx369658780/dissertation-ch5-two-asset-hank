"""Online MP4B bridge joining the frozen HA, MP2, and MP3 semantics."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Callable, Mapping, Sequence

import numpy as np

from .one_turn import OneTurnInputs, PreFrozenHouseholdOutputBatch, run_source_faithful_one_turn
from .steady_state import (
    AdaptiveAction, IterationRecord, ManualSteadyStateResult,
    SteadyStateConvergenceError, TERMINATION_CONVERGED, TERMINATION_MAX_ITERATIONS,
    _adapt, _diagnostics, _freeze_state, _post_turn_states,
)


HouseholdBatchSolver = Callable[[tuple[Mapping[str, object], ...], int], PreFrozenHouseholdOutputBatch]


@dataclass(frozen=True)
class OnlineStationaryInputs:
    province_order: tuple[str, ...]
    initial_provinces: tuple[Mapping[str, object], ...]
    params: Mapping[str, float]
    phi_destination_origin: np.ndarray
    migration_wedge_destination_origin: np.ndarray
    household_solver: HouseholdBatchSolver
    reg_threshold: float = 1e-9
    max_iterations: int = 500
    steady_state: bool = True


def run_online_stationary(inputs: OnlineStationaryInputs) -> ManualSteadyStateResult:
    """Mirror MP3 exactly while obtaining one simultaneous HA batch per turn."""
    order = tuple(inputs.province_order)
    states = _freeze_state(inputs.initial_provinces)
    n = len(order)
    if n < 2 or len(states) != n or any(str(s.get("name", "")) != order[i] for i, s in enumerate(states)):
        raise ValueError("province state and order mismatch")
    phi = np.asarray(inputs.phi_destination_origin, dtype=float)
    wedges = np.asarray(inputs.migration_wedge_destination_origin, dtype=float)
    if phi.shape != (n, n) or wedges.shape != (n, n):
        raise ValueError("cross-province matrices have the wrong shape")
    if inputs.reg_threshold <= 0 or inputs.max_iterations < 1:
        raise ValueError("invalid controller bounds")
    tkn_ratio = np.full(n, 3.0, dtype=float)
    history: list[IterationRecord] = []
    for iteration in range(1, inputs.max_iterations + 1):
        entering = states
        batch = inputs.household_solver(entering, iteration)
        turn = run_source_faithful_one_turn(OneTurnInputs(
            order, entering, MappingProxyType(dict(inputs.params)), phi, wedges, batch
        ))
        before = _post_turn_states(entering, batch, turn)
        diagnostic = _diagnostics(before, batch, tkn_ratio, inputs.reg_threshold)
        snapshot = _freeze_state(before)
        nk_gap, yt_gap, household_count, ra_upper, ra_lower, wage_upper, wage_lower, converged = diagnostic
        tkn_before = np.array(tkn_ratio, copy=True)
        if converged:
            next_states = before
            tkn_after = np.array(tkn_ratio, copy=True)
            actions = tuple(AdaptiveAction(
                province=str(s["name"]), zt_adjusted=False,
                zt_before=float(s["Zt"]), zt_after=float(s["Zt"]), govinv_action="NONE",
                govinv_before=float(s["GovInv"]), govinv_after=float(s["GovInv"]),
            ) for s in next_states)
        else:
            next_states, actions = _adapt(before, float(np.max(nk_gap)), inputs.steady_state)
            tkn_after = np.array([0.6*float(s["KNratio"])+0.4*tkn_ratio[i] for i, s in enumerate(next_states)])
        record = IterationRecord(
            iteration=iteration, state_entering_turn=entering, one_turn=turn,
            state_before_adaptation=snapshot, state_for_next_turn=_freeze_state(next_states),
            nk_ratio_gap=nk_gap, yt_gap=yt_gap, household_converged_count=household_count,
            household_all_converged=household_count == n, ra_upper_count=ra_upper,
            ra_lower_count=ra_lower, wage_upper_count=wage_upper, wage_lower_count=wage_lower,
            converged=converged, tkn_ratio_before=tkn_before, tkn_ratio_after=tkn_after,
            adaptive_actions=actions,
        )
        history.append(record); states = _freeze_state(next_states)
        if converged:
            return ManualSteadyStateResult(True, TERMINATION_CONVERGED, iteration, states, tuple(history))
        tkn_ratio = tkn_after
    result = ManualSteadyStateResult(False, TERMINATION_MAX_ITERATIONS, inputs.max_iterations, states, tuple(history))
    raise SteadyStateConvergenceError(result)
