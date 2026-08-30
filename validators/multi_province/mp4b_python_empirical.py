"""Validation-only one-shot calendar-2009 Python stationary entry."""
from __future__ import annotations

import json
import sys
from dataclasses import fields, is_dataclass
from pathlib import Path
from typing import Mapping

import numpy as np
from scipy.optimize import brentq

from exports.matlab_faithful_two_asset_ha import (
    EconomicParams, HouseholdInputs, MatlabFaithfulHJBGrid,
    MatlabFaithfulHJBNumerics, matlab_faithful_illiquid_return,
    solve_household_steady_state,
)
from ch5_two_asset_hank.multi_province.one_turn import PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.stationary_runtime import OnlineStationaryInputs, run_online_stationary
from ch5_two_asset_hank.multi_province.steady_state import SteadyStateConvergenceError


CANONICAL_SHA = "507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48"


def _jsonable(value):
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, (np.integer, np.floating, np.bool_)):
        return value.item()
    if isinstance(value, Mapping):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jsonable(item) for item in value]
    if is_dataclass(value):
        return {field.name: _jsonable(getattr(value, field.name)) for field in fields(value)}
    return value


def _write_json(path: Path, payload) -> None:
    if path.exists():
        raise FileExistsError(f"refusing to overwrite {path}")
    path.write_text(json.dumps(_jsonable(payload), ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")


def load_entry_state(canonical_path: Path) -> tuple[dict, tuple[dict[str, object], ...]]:
    canonical = json.loads(Path(canonical_path).read_text(encoding="utf-8"))
    if canonical["binding"] != {"analysis_index":1,"calendar_year":2009,"data_mat_index":1,
            "output_filename_year":2009,"regression_vintage_key":10,"workbook_data_row_index":10}:
        raise ValueError("canonical annual binding mismatch")
    v=canonical["vectors"]; s=canonical["scalars"]
    states=[]
    for i,name in enumerate(canonical["province_order"]):
        state={"name":name,"N":v["pop"][i],"alpha":v["ind_alpha"][i],"Zt":v["initialized_zt"][i],
            "Kt0":v["cap"][i],"Kt":v["cap"][i],"Kt_prev":v["cap"][i],"Lt":v["pop"][i],
            "Lt_prev":v["pop"][i],"Yt0":v["gdp"][i],"Yt":v["gdp"][i],"Zt_1":v["initialized_zt"][i],
            "GovInv":v["gov_inv"][i],"inter_prv_ratio":v["inter_province_asset_ratio"][i],
            "rb_gap":s["rb_gap"],"rah":s["rah"],"ra":s["ra"],"it":s["nominal_rate"],
            "rb":s["rb"],"rk":s["rk"],"wjt":s["wjt"],"w":s["composite_wage"],
            "Tt":s["transfer_income"],"pit":s["inflation"],"pit_1":s["inflation"],
            "totalpit":s["inflation"],"epsilon_pi":0.0,"tau":s["wage_tax"],"At":s["initial_at"],
            "Bt":s["initial_bt"],"mt":s["initial_mt"],"Ct":s["initial_ct"],"AtTax":0.0,
            "GovSurplus":0.0,"corptau":s["corporate_tax"],"ramin":0.02,"ramax":0.09,
            "wjtmin":0.8,"wjtmax":1.3}
        states.append(state)
    return canonical, tuple(states)


def _source_initial_arrays(state: Mapping[str, object], grid: MatlabFaithfulHJBGrid, params: EconomicParams):
    shape=(grid.b.size,grid.a.size,grid.z.size); labor=np.empty(shape); value=np.empty(shape)
    for k,z in enumerate(grid.z):
        for j,a in enumerate(grid.a):
            effective=float(matlab_faithful_illiquid_return(a,grid.a[-1],float(state["rah"])))
            for i,b in enumerate(grid.b):
                rb=float(state["rb"])+(float(state["rb_gap"]) if b<0 else 0.0)
                temp=effective*effective+rb*b+float(state["Tt"])
                wage=(1-float(state["tau"]))*float(state["w"])*z
                def equation(l): return l-(wage**0.2)*(l*wage+temp)**(-0.4)
                lo=0.0; hi=max(1.0,(wage**0.2)*max(temp,1e-12)**(-0.4))
                while equation(hi)<0: hi*=2
                l=brentq(equation,lo,hi,xtol=1e-14,rtol=1e-14)
                c=wage*l+rb*b+float(state["Tt"])
                labor[i,j,k]=l
                value[i,j,k]=(c**(1-params.gamma_c)/(1-params.gamma_c)-l**6/6)/params.rho
    return value,labor


def run_python_once(canonical_path: Path, run_root: Path):
    root=Path(run_root); root.mkdir(parents=True,exist_ok=False)
    canonical,states=load_entry_state(canonical_path)
    _write_json(root/'python_run_manifest.json', {
        "schema":"CH5_MP4B_PYTHON_SCIENTIFIC_RUN_V1", "calendar_year":2009,
        "canonical_sha256":CANONICAL_SHA, "province_order":canonical["province_order"],
        "reg_threshold":1e-9, "max_iterations":500,
        "interface_only_unused_fields":{"mu_z":0.0,"sigma_z":0.0},
    })
    grid=MatlabFaithfulHJBGrid(np.linspace(-2,5,20),np.linspace(0,10,20),np.array([0.8,1.3]),
                              np.array([[-1/3,1/3],[1/3,-1/3]]))
    params=EconomicParams(0.05,2.0,5.0,0.1,2.0,1e-6,0.0,0.0)
    numerics=MatlabFaithfulHJBNumerics(1000.0,1e-7,100,1e-12)
    call_count=0
    phi_matrix=np.ones((31,31),dtype=float)
    def solve_batch(snapshot,iteration):
        nonlocal call_count
        productivity=np.array([float(s["Yt"])/float(s["Lt"]) for s in snapshot])
        phi_matrix[:]=1.0+0.3*(productivity[:,None]-productivity[None,:])/(productivity[:,None]+productivity[None,:])
        outputs=[]
        _write_json(root/f'turn_{iteration:03d}_household_inputs.json', {
            "iteration":iteration,"state_entering_turn":snapshot,"phi_destination_origin":phi_matrix})
        try:
            for province_index,state in enumerate(snapshot):
                initial,labor=_source_initial_arrays(state,grid,params)
                result=solve_household_steady_state(grid,params,HouseholdInputs(
                    float(state["rah"]),float(state["rb"]),float(state["tau"]),
                    np.array([state["w"]]),np.array([0.0]),np.array([1.0])),initial,labor,
                    float(state["Tt"]),float(state["rb_gap"]),numerics)
                call_count+=1; agg=result.aggregates; density=result.kfe.density
                effective=matlab_faithful_illiquid_return(grid.a,grid.a[-1],float(state["rah"]))
                at_tax=agg.a_ss*float(state["rah"])-float(np.sum(grid.a[None,:,None]*effective[None,:,None]*density)*result.kfe.cell_weight)
                outputs.append((agg.c_ss,agg.l_ss,agg.a_ss,agg.b_ss,at_tax,result.hjb.converged,result.hjb.convergence_statistic))
        except Exception as exc:
            _write_json(root/f'turn_{iteration:03d}_household_failure.json', {
                "iteration":iteration,"completed_households":len(outputs),"household_call_count":call_count,
                "error_type":type(exc).__name__,"error":str(exc)})
            raise
        batch=PreFrozenHouseholdOutputBatch(
            ct=[x[0] for x in outputs],household_lt=[x[1] for x in outputs],at=[x[2] for x in outputs],
            bt=[x[3] for x in outputs],at_tax=[x[4] for x in outputs],converged=tuple(x[5] for x in outputs),
            diagnostics=tuple({"hjb_statistic":x[6],"iteration":iteration} for x in outputs))
        _write_json(root/f'turn_{iteration:03d}_household_outputs.json', batch)
        return batch
    p={"ga":2.0,"phi_l":5.0,"alphal":1.0,"epsilon":10.0,"theta":100.0,"delta":0.025,
       "istar":0.015,"rho_pi":1.25,"totalpit":0.02,"epsilon_pi":0.0}
    try:
        result=run_online_stationary(OnlineStationaryInputs(tuple(canonical["province_order"]),states,p,
            phi_matrix,np.array(canonical["matrices"]["sigmau"]),solve_batch,1e-9,500,True))
    except SteadyStateConvergenceError as exc:
        result=exc.result
        _write_json(root/'python_terminal_summary.json', {
            "status":result.termination_reason,"converged":False,"iteration_count":result.iteration_count,
            "household_call_count":call_count,"history":result.history,"final_state":result.final_state})
        raise
    except Exception as exc:
        _write_json(root/'python_terminal_summary.json', {
            "status":"ERROR","converged":False,"household_call_count":call_count,
            "error_type":type(exc).__name__,"error":str(exc)})
        raise
    summary={"status":result.termination_reason,"iteration_count":result.iteration_count,
             "household_call_count":call_count,"history":result.history,"final_state":result.final_state}
    _write_json(root/'python_terminal_summary.json', summary)
    return result


def main(argv=None) -> int:
    args=list(sys.argv[1:] if argv is None else argv)
    if len(args) != 2:
        raise SystemExit("usage: mp4b_python_empirical.py CANONICAL_JSON FRESH_RUN_ROOT")
    run_python_once(Path(args[0]),Path(args[1]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
