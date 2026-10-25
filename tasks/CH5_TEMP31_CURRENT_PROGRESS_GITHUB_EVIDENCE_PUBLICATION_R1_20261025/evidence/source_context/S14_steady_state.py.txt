"""Manual source-ordered controller from ``HANK_mp_1eq.m:3-66``.

The controller consumes complete pre-frozen household-output batches and calls
only the accepted deterministic MP2 one-turn arithmetic.  It is not a generic
root solver and contains no household, HJB, KFE, GE, or dynamic invocation.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from types import MappingProxyType
from typing import Mapping, Sequence

import numpy as np

from .one_turn import (
    OneTurnInputs,
    OneTurnResult,
    PreFrozenHouseholdOutputBatch,
    run_source_faithful_one_turn,
)


SOURCE_MAX_ITERATIONS = 500
TERMINATION_CONVERGED = "SOURCE_CONVERGED"
TERMINATION_MAX_ITERATIONS = "SOURCE_MAX_ITERATION_EXHAUSTED"


def _readonly_vector(name: str, values: object, n: int) -> np.ndarray:
    array = np.array(values, dtype=float, copy=True)
    if array.shape != (n,) or not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must be a finite vector of shape ({n},)")
    array.flags.writeable = False
    return array


def _freeze_state(states: Sequence[Mapping[str, object]]) -> tuple[Mapping[str, object], ...]:
    return tuple(MappingProxyType(dict(state)) for state in states)


@dataclass(frozen=True)
class AdaptiveAction:
    province: str
    zt_adjusted: bool
    zt_before: float
    zt_after: float
    govinv_action: str
    govinv_before: float
    govinv_after: float


@dataclass(frozen=True)
class IterationRecord:
    iteration: int
    state_entering_turn: tuple[Mapping[str, object], ...]
    one_turn: OneTurnResult
    state_before_adaptation: tuple[Mapping[str, object], ...]
    state_for_next_turn: tuple[Mapping[str, object], ...]
    nk_ratio_gap: np.ndarray
    yt_gap: np.ndarray
    household_converged_count: int
    household_all_converged: bool
    ra_upper_count: int
    ra_lower_count: int
    wage_upper_count: int
    wage_lower_count: int
    converged: bool
    tkn_ratio_before: np.ndarray
    tkn_ratio_after: np.ndarray
    adaptive_actions: tuple[AdaptiveAction, ...]

    def __post_init__(self) -> None:
        n = len(self.state_entering_turn)
        for name in ("nk_ratio_gap", "yt_gap", "tkn_ratio_before", "tkn_ratio_after"):
            object.__setattr__(self, name, _readonly_vector(name, getattr(self, name), n))
        if self.iteration < 1:
            raise ValueError("iteration is one-based")
        if len(self.adaptive_actions) != n:
            raise ValueError("adaptive action count must match provinces")


@dataclass(frozen=True)
class ManualSteadyStateInputs:
    province_order: tuple[str, ...]
    initial_provinces: tuple[Mapping[str, object], ...]
    params: Mapping[str, float]
    phi_destination_origin: np.ndarray
    migration_wedge_destination_origin: np.ndarray
    household_batches: tuple[PreFrozenHouseholdOutputBatch, ...]
    reg_threshold: float
    max_iterations: int = SOURCE_MAX_ITERATIONS
    steady_state: bool = True

    def __post_init__(self) -> None:
        order = tuple(self.province_order)
        n = len(order)
        if n < 2 or len(set(order)) != n or len(self.initial_provinces) != n:
            raise ValueError("province_order and initial_provinces must define at least two unique provinces")
        states = _freeze_state(self.initial_provinces)
        if any(str(state.get("name", "")) != order[i] for i, state in enumerate(states)):
            raise ValueError("initial province records must exactly match province_order")
        params = MappingProxyType(dict(self.params))
        phi = np.array(self.phi_destination_origin, dtype=float, copy=True)
        wedges = np.array(self.migration_wedge_destination_origin, dtype=float, copy=True)
        if phi.shape != (n, n) or wedges.shape != (n, n):
            raise ValueError("cross-province matrices must have destination-by-origin shape")
        if not np.all(np.isfinite(phi)) or not np.all(np.isfinite(wedges)):
            raise ValueError("cross-province matrices must be finite")
        threshold = float(self.reg_threshold)
        if not isfinite(threshold) or threshold <= 0.0:
            raise ValueError("reg_threshold must be finite and positive")
        if not isinstance(self.max_iterations, int) or self.max_iterations < 1:
            raise ValueError("max_iterations must be a positive integer")
        batches = tuple(self.household_batches)
        for batch in batches:
            if batch.ct.shape != (n,):
                raise ValueError("every household batch must match the province count")
        phi.flags.writeable = False
        wedges.flags.writeable = False
        object.__setattr__(self, "province_order", order)
        object.__setattr__(self, "initial_provinces", states)
        object.__setattr__(self, "params", params)
        object.__setattr__(self, "phi_destination_origin", phi)
        object.__setattr__(self, "migration_wedge_destination_origin", wedges)
        object.__setattr__(self, "household_batches", batches)
        object.__setattr__(self, "reg_threshold", threshold)


@dataclass(frozen=True)
class ManualSteadyStateResult:
    converged: bool
    termination_reason: str
    iteration_count: int
    final_state: tuple[Mapping[str, object], ...]
    history: tuple[IterationRecord, ...]


class SteadyStateConvergenceError(RuntimeError):
    """Source-equivalent max-iteration failure with auditable partial result."""

    def __init__(self, result: ManualSteadyStateResult) -> None:
        super().__init__("source manual steady state did not converge before max_iterations")
        self.result = result


def _post_turn_states(
    states: tuple[Mapping[str, object], ...],
    batch: PreFrozenHouseholdOutputBatch,
    turn: OneTurnResult,
) -> list[dict[str, object]]:
    updated: list[dict[str, object]] = []
    for i, old in enumerate(states):
        firm = turn.firms[i]
        state = dict(old)
        state.update({
            "Ct": float(batch.ct[i]), "At": float(batch.at[i]), "Bt": float(batch.bt[i]),
            "AtTax": float(batch.at_tax[i]), "convergent": bool(batch.converged[i]),
            "Lt_supply": float(turn.migration.lt_supply[i]),
            "Kt_supply": float(turn.capital.kt_supply[i]),
            "rah": float(turn.capital.household_illiquid_return_rah[i]),
            "w": float(turn.household_composite_wage[i]), "it": turn.monetary.it,
            "rb": turn.monetary.rb, "Yt_1": float(old["Yt"]),
            "Kt_prev": firm.Kt, "Lt_prev": firm.Lt, "Zt_1": float(old["Zt"]),
            "pit_1": float(old["pit"]),
        })
        state.update(firm.as_source_dict())
        updated.append(state)
    return updated


def _diagnostics(
    states: Sequence[Mapping[str, object]],
    batch: PreFrozenHouseholdOutputBatch,
    tkn_ratio: np.ndarray,
    threshold: float,
) -> tuple[np.ndarray, np.ndarray, int, int, int, int, int, bool]:
    nk_gap = np.array([abs(float(s["KNratio"]) / tkn_ratio[i] - 1.0) for i, s in enumerate(states)])
    yt_gap = np.array([abs(float(s["Yt"]) / float(s["Yt_1"]) - 1.0) for s in states])
    if not np.all(np.isfinite(nk_gap)) or not np.all(np.isfinite(yt_gap)):
        raise ValueError("source convergence gaps must be real and finite")
    household_count = sum(bool(value) for value in batch.converged)
    ra_upper = sum(float(s["ra"]) == float(s["ramax"]) for s in states)
    ra_lower = sum(float(s["ra"]) == float(s["ramin"]) for s in states)
    wage_upper = sum(float(s["wjt"]) == float(s["wjtmax"]) for s in states)
    wage_lower = sum(float(s["wjt"]) == float(s["wjtmin"]) for s in states)
    converged = (
        float(np.max(nk_gap)) < threshold
        and float(np.max(yt_gap)) < threshold
        and household_count == len(states)
        and ra_upper == 0
        and ra_lower == 0
    )
    return nk_gap, yt_gap, household_count, ra_upper, ra_lower, wage_upper, wage_lower, converged


def _adapt(
    states: list[dict[str, object]], max_nk_gap: float, steady_state: bool
) -> tuple[list[dict[str, object]], tuple[AdaptiveAction, ...]]:
    actions: list[AdaptiveAction] = []
    allow = max_nk_gap < 0.1 and steady_state
    for state in states:
        zt_before = float(state["Zt"])
        gov_before = float(state["GovInv"])
        zt_after = zt_before
        gov_after = gov_before
        gov_action = "NONE"
        zt_adjusted = False
        if allow:
            discrepancy = float(state["Yt"]) / float(state["Yt0"]) - 1.0
            if discrepancy > 0.01 or discrepancy < -0.01:
                zt_after = (
                    float(state["Yt0"])
                    * float(state["Kt"]) ** (-float(state["alpha"]))
                    * float(state["Lt"]) ** (float(state["alpha"]) - 1.0)
                )
                state["Zt"] = zt_after
                zt_adjusted = True
            if float(state["ra"]) < float(state["ramin"]) + 0.02:
                gov_after = gov_before * 0.9
                gov_action = "LOW_RA_DECREASE_0P9"
                state["GovInv"] = gov_after
            elif float(state["ra"]) > float(state["ramax"]) - 0.02:
                gov_after = gov_before * 1.1
                gov_action = "HIGH_RA_INCREASE_1P1"
                state["GovInv"] = gov_after
        actions.append(AdaptiveAction(
            province=str(state["name"]), zt_adjusted=zt_adjusted,
            zt_before=zt_before, zt_after=zt_after, govinv_action=gov_action,
            govinv_before=gov_before, govinv_after=gov_after,
        ))
    return states, tuple(actions)


def run_manual_steady_state(inputs: ManualSteadyStateInputs) -> ManualSteadyStateResult:
    """Run the literal one-based manual loop, raising on source exhaustion."""

    n = len(inputs.province_order)
    states = inputs.initial_provinces
    tkn_ratio = np.full(n, 3.0, dtype=float)  # HANK_mp_1eq.m:3
    history: list[IterationRecord] = []
    for iteration in range(1, inputs.max_iterations + 1):
        if iteration > len(inputs.household_batches):
            raise ValueError("required pre-frozen household batch is unavailable before termination")
        batch = inputs.household_batches[iteration - 1]
        entering = states
        turn = run_source_faithful_one_turn(OneTurnInputs(
            province_order=inputs.province_order,
            old_provinces=states,
            params=inputs.params,
            phi_destination_origin=inputs.phi_destination_origin,
            migration_wedge_destination_origin=inputs.migration_wedge_destination_origin,
            household_outputs=batch,
        ))
        before_adaptation = _post_turn_states(states, batch, turn)
        diagnostic = _diagnostics(before_adaptation, batch, tkn_ratio, inputs.reg_threshold)
        before_adaptation_snapshot = _freeze_state(before_adaptation)
        nk_gap, yt_gap, household_count, ra_upper, ra_lower, wage_upper, wage_lower, converged = diagnostic
        tkn_before = np.array(tkn_ratio, copy=True)
        if converged:
            next_states = before_adaptation
            tkn_after = np.array(tkn_ratio, copy=True)
            actions = tuple(AdaptiveAction(
                province=str(state["name"]), zt_adjusted=False,
                zt_before=float(state["Zt"]), zt_after=float(state["Zt"]),
                govinv_action="NONE", govinv_before=float(state["GovInv"]),
                govinv_after=float(state["GovInv"]),
            ) for state in next_states)
        else:
            next_states, actions = _adapt(before_adaptation, float(np.max(nk_gap)), inputs.steady_state)
            tkn_after = np.array([
                0.6 * float(state["KNratio"]) + 0.4 * tkn_ratio[i]
                for i, state in enumerate(next_states)
            ])
        record = IterationRecord(
            iteration=iteration, state_entering_turn=entering, one_turn=turn,
            state_before_adaptation=before_adaptation_snapshot,
            state_for_next_turn=_freeze_state(next_states), nk_ratio_gap=nk_gap,
            yt_gap=yt_gap, household_converged_count=household_count,
            household_all_converged=household_count == n, ra_upper_count=ra_upper,
            ra_lower_count=ra_lower, wage_upper_count=wage_upper,
            wage_lower_count=wage_lower, converged=converged,
            tkn_ratio_before=tkn_before, tkn_ratio_after=tkn_after,
            adaptive_actions=actions,
        )
        history.append(record)
        states = _freeze_state(next_states)
        if converged:
            return ManualSteadyStateResult(
                converged=True, termination_reason=TERMINATION_CONVERGED,
                iteration_count=iteration, final_state=states, history=tuple(history),
            )
        tkn_ratio = tkn_after
        if iteration == inputs.max_iterations:
            result = ManualSteadyStateResult(
                converged=False, termination_reason=TERMINATION_MAX_ITERATIONS,
                iteration_count=iteration, final_state=states, history=tuple(history),
            )
            raise SteadyStateConvergenceError(result)
    raise AssertionError("unreachable manual steady-state controller path")
