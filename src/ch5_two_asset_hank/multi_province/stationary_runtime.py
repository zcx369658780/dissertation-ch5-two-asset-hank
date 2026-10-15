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


def mainline_initial_states(fixture):
    """Only the frozen synthetic fixture; no cache or annual-data reader."""
    from .wage import mainline_phi, mainline_effective_wages
    p=fixture['parameters']
    wages=mainline_effective_wages(fixture['firm_gross_wage_initial'],fixture['destination_tax_tau'],
        mainline_phi(fixture['pgdp_reference']),fixture['migration_wedge_destination_origin'],
        phi_l=p['phi_l'],alphal=p['alphal'])
    states=[]
    mapping={'N':'population_N','tau':'destination_tax_tau','corptau':'corporate_tax_rate',
        'GovInv':'initial_GovInv','At':'initial_private_assets_At_per_person',
        'Bt':'initial_liquid_assets_Bt_per_person','Ct':'initial_consumption_Ct_per_person',
        'Lt_HA':'initial_household_Lt_per_person','Kt_prev':'initial_firm_Kt_previous',
        'Lt_prev':'initial_firm_Lt_previous','Yt':'initial_Yt_previous','Yt0':'synthetic_target_Yt0',
        'alpha':'alpha','Zt':'Zt','Zt_1':'Zt_previous','pit':'pit','pit_1':'pit_previous',
        'rk':'initial_rk','Tt':'transfer_Tt_per_person','rb_gap':'borrowing_rate_gap',
        'rah':'initial_household_rah','ra':'initial_ra_used','wjt_gross':'firm_gross_wage_initial',
        'ra0_raw_previous':'initial_lagged_raw_ra0_by_destination'}
    for i,name in enumerate(fixture['province_order']):
        state={key:float(fixture[field][i]) for key,field in mapping.items()}
        state.update(name=name,rb=float(fixture['initial_rb']),w_eff=float(wages[i]),
            Lt=float(fixture['initial_firm_Lt_previous'][i]),Kt=float(fixture['initial_firm_Kt_previous'][i]),
            Lt_firm_ss=float(fixture['initial_firm_Lt_previous'][i]),
            ramin=0.02,ramax=0.09,wjtmin=0.8,wjtmax=1.3)
        states.append(state)
    return tuple(states)


def run_mainline_stationary(fixture, solve_batch, *, max_iterations=5):
    from .one_turn import run_mainline_one_turn, prepare_mainline_household_states
    from .steady_state import mainline_outer_diagnostics
    if not isinstance(max_iterations,int) or not 1 <= max_iterations <= 5:
        raise ValueError('V010 outer ceiling is five two-province turns')
    states=mainline_initial_states(fixture); tkn=np.full(len(states),3.0); history=[]
    for iteration in range(1,max_iterations+1):
        states=prepare_mainline_household_states(states,fixture)
        batch=solve_batch(states,'outer')
        turn=run_mainline_one_turn(states,batch,fixture)
        states=tuple(dict(s) for s in turn['states'])
        diagnostic=mainline_outer_diagnostics(states,tkn)
        snapshot=tuple(dict(s) for s in states)
        if diagnostic['OUTER_ITERATION_CONVERGED']:
            history.append({'iteration':iteration,'diagnostics':diagnostic,'turn':turn,'adapt':()})
            return {'status':'OUTER_ITERATION_CONVERGED','states':states,'history':history}
        adjusted,actions=_adapt([dict(s) for s in states],max(diagnostic['nk_gap']),True)
        tkn=np.array([0.6*s['KNratio']+0.4*tkn[i] for i,s in enumerate(adjusted)])
        history.append({'iteration':iteration,'diagnostics':diagnostic,'turn':turn,
                        'before_adapt':snapshot,'adapt':actions})
        states=tuple(adjusted)
    return {'status':'OUTER_BUDGET_NONCONVERGED','states':states,'history':history}


def verify_mainline_frozen(fixture, calibrated, solve_batch):
    from .one_turn import run_mainline_one_turn, prepare_mainline_household_states
    from .steady_state import mainline_outer_diagnostics
    if calibrated['status'] != 'OUTER_ITERATION_CONVERGED':
        raise ValueError('freeze verification requires outer convergence')
    states=prepare_mainline_household_states(calibrated['states'],fixture)
    batch=solve_batch(states,'verify')
    turn=run_mainline_one_turn(states,batch,fixture)
    diagnostic=mainline_outer_diagnostics(turn['states'],np.array([s['KNratio'] for s in states]))
    passed=diagnostic['OUTER_ITERATION_CONVERGED'] and max(diagnostic['target_gap']) <= 0.01
    if any(s['Zt'] != t['Zt'] or s['GovInv'] != t['GovInv'] for s,t in zip(states,turn['states'])):
        raise ValueError('frozen calibration mutated')
    return {'status':'TARGET_CALIBRATION_VERIFIED' if passed else 'FROZEN_VERIFICATION_FAILED',
            'states':turn['states'],'diagnostics':dict(diagnostic,TARGET_CALIBRATION_VERIFIED=passed)}
