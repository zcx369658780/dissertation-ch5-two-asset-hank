"""Conditional simultaneous static-path diagnostics. NOT_REAL_IRF."""
from copy import deepcopy
from pathlib import Path
import json
import os
from .reconciled_stationary import reserve, solve_blocks

def require_baseline(baseline):
    if not baseline["success"] or baseline["qualification"]!="SYNTHETIC_CONDITIONAL_STATIONARY":
        raise ValueError("Gate B qualified baseline required")

def shock_path(case, baseline, horizon, amplitude, *, rho=.5):
    require_baseline(baseline)
    attempt=reserve("path",case["n"])
    if not 1<=horizon<=40 or not 0<=rho<1 or abs(amplitude)>1e-3:
        raise ValueError("frozen synthetic horizon / local shock bound")
    cases=[]; shocks=[]; state=[0.0,0.0,0.0]
    # Explicit artificial independent AR(1) processes, innovations at t=0/10/20.
    for t in range(horizon):
        state=[rho*s for s in state]
        for k,start in enumerate((0,10,20)):
            if t==start: state[k]+=amplitude
        c=deepcopy(case)
        c["A"]=[x*(1+state[0]) for x in case["A"]]
        c["tax"]=case["tax"]+state[1]
        c["Kg"]=[x*(1+state[2]) for x in case["Kg"]]
        cases.append(c); shocks.append(state[:])
    initial=[baseline["solution_vector"][0][:] for _ in cases]
    solution=solve_blocks(cases,initial,label="gate_c_joint_static_blocks")
    result=dict(qualification="CONDITIONAL_SHOCK_PATH_DIAGNOSTIC",NOT_REAL_IRF=True,
        path_attempt=attempt,horizon=horizon,amplitude=amplitude,rho=rho,
        innovations={"TFP":0,"national_tax":10,"public_capital":20},
        exogenous_states=shocks,solution=solution)
    with (Path(os.environ["V008_LEDGER_DIR"])/f"path_{attempt:03d}.json").open("x",encoding="utf-8") as f:
        json.dump(result,f,indent=2,allow_nan=False)
    return result

def compare_paths(zero,full,half,prefix,baseline):
    paths=(zero,full,half,prefix)
    if not all(p["solution"]["success"] for p in paths):
        return dict(success=False,reason="PERIOD_EQUILIBRIUM_FAILED")
    base=baseline["results"][0]
    def values(r): return r["Y"]+r["L"]+r["w"]+[r["C"],r["transfer"]]
    b=values(base)
    zero_error=max(abs(x-y) for r in zero["solution"]["results"] for x,y in zip(values(r),b))
    prefix_error=max(abs(x-y) for r,s in zip(full["solution"]["results"],prefix["solution"]["results"])
                     for x,y in zip(values(r),values(s)))
    deviations=[[x-y for x,y in zip(values(r),b)] for r in full["solution"]["results"]]
    halves=[[x-y for x,y in zip(values(r),b)] for r in half["solution"]["results"]]
    scale=max(abs(v) for row in deviations for v in row)
    linear_error=max(abs(h-.5*d) for hh,dd in zip(halves,deviations) for h,d in zip(hh,dd))/max(scale,1e-12)
    tail=max(abs(v) for v in deviations[-1])/max(scale,1e-12)
    bounded=all(abs(x)<1e6 for p in paths for r in p["solution"]["results"] for x in values(r))
    return dict(success=zero_error<1e-10 and prefix_error<1e-9 and linear_error<.02 and tail<1e-4 and bounded,
                zero_error=zero_error,prefix_horizon_error=prefix_error,
                half_amplitude_relative_error=linear_error,tail_relative_response=tail,
                finite_bounded=bounded,period_max_residual=max(p["solution"]["max_scaled_residual"] for p in paths),
                NOT_REAL_IRF=True,all_province_response_sign_not_imposed=True)

def public_capital_endowment_bridge(case, path):
    """Explicit SYNTHETIC_SCENARIO: in-kind external public-capital endowments.

    Capital shocks are NOT an unfunded investment policy or endogenous state law.
    At each model-period boundary an artificial external donor supplies/removes
    delta Kg. The identical in-kind grant finances that net public investment;
    gross public investment additionally contains maintenance delta*Kg.
    This is separate from cash taxes and cannot be residual fiscal income.
    """
    previous=list(case["Kg"]); rows=[]
    for t,(c,r) in enumerate(zip(path["solution"]["scenario"],path["solution"]["results"])):
        change=[k-old for k,old in zip(c["Kg"],previous)]
        grant=sum(change)
        rows.append(dict(t=t,scenario="SYNTHETIC_EXTERNAL_CAPITAL_ENDOWMENT",
            public_stock=list(c["Kg"]),net_public_investment=change,
            in_kind_grant=grant,external_donor_asset_change=-grant,
            government_asset_change=grant,
            gross_public_investment=grant+c["delta"]*sum(c["Kg"]),
            cash_grant=0.0,stock_counterparty_residual=grant-grant,
            resource_with_grant_residual=(sum(r["Y"])+grant-r["C"]-r["G"]
                -c["delta"]*sum(r["K"])-grant)/max(1,sum(r["Y"]))))
        previous=list(c["Kg"])
    return rows
