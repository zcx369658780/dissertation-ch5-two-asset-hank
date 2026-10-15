"""Original one-turn recursive response, never an outer recalibration or dynamic IRF."""
from __future__ import annotations
import math
from .one_turn import run_mainline_one_turn, prepare_mainline_household_states


def run_mainline_response(fixture, verified, solve_batch, *, zero=False, turn_function=None):
    if verified['status'] != 'TARGET_CALIBRATION_VERIFIED':
        raise ValueError('response requires independently verified frozen calibration')
    if fixture['response']['periods'] != 3:
        raise ValueError('V010 response ceiling is exactly three dates')
    actual_mainline = turn_function is None
    turn_function = run_mainline_one_turn if actual_mainline else turn_function
    baseline=tuple(dict(s) for s in verified['states'])
    states=baseline; history=[]
    for t in range(1,4):
        entering=[]
        for i,(base,old) in enumerate(zip(baseline,states)):
            state=dict(old)
            for key in ('Zt','GovInv','tau','corptau'):
                state[key]=base[key]
            shock=0.0 if zero or i != 0 else 0.01*math.exp(-0.5*(t-1))
            state['Zt']=base['Zt']*(1+shock)
            entering.append(state)
        if actual_mainline:
            entering=prepare_mainline_household_states(tuple(entering),fixture)
        batch=solve_batch(tuple(entering),'response_zero' if zero else 'response_tfp')
        turn=turn_function(tuple(entering),batch,fixture)
        states=turn['states']
        response=[{key:float(s[key]/b[key]-1) if b[key] != 0 else None
                   for key in ('Yt','Ct','Kt','Lt')} for s,b in zip(states,baseline)]
        history.append({'period':t,'entering':tuple(entering),'turn':turn,'relative_response':response})
    return {'status':'CONDITIONAL_RECURSION_DIAGNOSTIC','states':states,'history':history,
            'lagged_NKPC':True,'outer_recalibration':False,'formal_dynamic_IRF':False}
