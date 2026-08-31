"""Validation-only one-shot calendar-2009 Python stationary entry."""
from __future__ import annotations

import json
import hashlib
import importlib.util
import sys
from dataclasses import fields, is_dataclass
from pathlib import Path
from typing import Mapping

import numpy as np
from scipy.optimize import brentq


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
ORACLE_PATH = REPO_ROOT / "exports" / "matlab_faithful_two_asset_ha.py"
ORACLE_SHA = "B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def _bootstrap_repository_imports() -> dict[str, object]:
    expected = (REPO_ROOT / ".git", SRC_ROOT / "ch5_two_asset_hank", ORACLE_PATH)
    if not all(path.exists() for path in expected):
        raise RuntimeError("current repository bootstrap identity is incomplete")
    oracle_sha = _sha256(ORACLE_PATH)
    if oracle_sha != ORACLE_SHA:
        raise RuntimeError("standalone household oracle identity mismatch")
    for root in (str(SRC_ROOT), str(REPO_ROOT)):
        if root not in sys.path:
            sys.path.insert(0, root)
    exports_spec = importlib.util.find_spec("exports.matlab_faithful_two_asset_ha")
    package_spec = importlib.util.find_spec("ch5_two_asset_hank")
    exports_origin = Path(exports_spec.origin).resolve() if exports_spec and exports_spec.origin else None
    package_origin = Path(package_spec.origin).resolve() if package_spec and package_spec.origin else None
    if exports_origin != ORACLE_PATH.resolve():
        raise RuntimeError("exports module resolved outside the current repository")
    if package_origin is None or SRC_ROOT.resolve() not in package_origin.parents:
        raise RuntimeError("ch5_two_asset_hank resolved outside the current repository src root")
    forbidden = ("chapter5_model", "dissertation-ch5-r5-python-model")
    resolved_text = "\n".join((str(exports_origin), str(package_origin))).lower()
    if any(name in resolved_text for name in forbidden):
        raise RuntimeError("forbidden historical runtime resolved during bootstrap")
    return {
        "schema": "CH5_MP4B_PYTHON_DIRECT_SCRIPT_BOOTSTRAP_V1",
        "repository_root": str(REPO_ROOT.resolve()),
        "src_root": str(SRC_ROOT.resolve()),
        "oracle_module_path": str(exports_origin),
        "package_module_path": str(package_origin),
        "oracle_sha256": oracle_sha,
        "scientific_model_calls": 0,
        "forbidden_runtime_imports": [],
    }


BOOTSTRAP_IDENTITY = _bootstrap_repository_imports()

from exports.matlab_faithful_two_asset_ha import (
    EconomicParams, HouseholdInputs, MatlabFaithfulHJBGrid,
    MatlabFaithfulHJBNumerics, matlab_faithful_illiquid_return,
)
from validators.multi_province.mp4b_matlab_source_postloop_household_adapter import (
    solve_matlab_source_postloop_household,
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


def _source_labor_root(
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


def _source_initial_arrays(state: Mapping[str, object], grid: MatlabFaithfulHJBGrid, params: EconomicParams):
    shape=(grid.b.size,grid.a.size,grid.z.size); labor=np.empty(shape); value=np.empty(shape)
    for k,z in enumerate(grid.z):
        for j,a in enumerate(grid.a):
            effective=float(matlab_faithful_illiquid_return(a,grid.a[-1],float(state["rah"])))
            for i,b in enumerate(grid.b):
                rb=float(state["rb"])+(float(state["rb_gap"]) if b<0 else 0.0)
                temp=effective*effective+rb*b+float(state["Tt"])
                wage=(1-float(state["tau"]))*float(state["w"])*z
                l,_=_source_labor_root(wage=wage,temp=temp,frisch_l=1.0/params.phi,ga=params.gamma_c)
                c=wage*l+rb*b+float(state["Tt"])
                labor[i,j,k]=l
                value[i,j,k]=(c**(1-params.gamma_c)/(1-params.gamma_c)-l**6/6)/params.rho
    return value,labor


def run_full_initialization_preflight(canonical_path: Path, output_path: Path) -> dict[str, object]:
    """Validate every first-turn source-initialization cell without model calls."""
    canonical,states=load_entry_state(canonical_path)
    b_grid=np.linspace(-2,5,20); a_grid=np.linspace(0,10,20); z_grid=np.array([0.8,1.3])
    checked=0; max_residual=0.0; min_c0=float("inf"); min_root_base=float("inf")
    min_v02=float("inf"); max_v02=float("-inf"); first_failure=None
    try:
        for province_index,state in enumerate(states):
            for k,z in enumerate(z_grid):
                for j,a in enumerate(a_grid):
                    effective=float(matlab_faithful_illiquid_return(a,a_grid[-1],float(state["rah"])))
                    for i,b in enumerate(b_grid):
                        rb=float(state["rb"])+(float(state["rb_gap"]) if b<0 else 0.0)
                        temp=effective*effective+rb*b+float(state["Tt"])
                        wage=(1-float(state["tau"]))*float(state["w"])*z
                        x0=wage**(0.2*(1-2)/(1+2*0.2)); boundary=-temp/wage
                        root,bracket=_source_labor_root(wage=wage,temp=temp)
                        residual=root-wage**0.2*(root*wage+temp)**(-0.4)
                        c0=wage*root+rb*b+float(state["Tt"])
                        v02=(c0**(1-2)/(1-2)-root**6/6)/0.05
                        checks=(
                            np.isfinite(x0) and x0>boundary,
                            all(np.isfinite(endpoint) and endpoint>boundary for endpoint in bracket),
                            np.isfinite(root) and root>boundary,
                            np.isfinite(residual) and abs(residual)<=1e-10,
                            np.isfinite(c0) and c0>0,
                            np.isfinite(v02) and np.isreal(v02),
                        )
                        if not all(checks):
                            raise ValueError(f"source initialization check failed: {checks}")
                        checked+=1; max_residual=max(max_residual,abs(float(residual)))
                        min_c0=min(min_c0,float(c0)); min_root_base=min(min_root_base,float(wage*root+temp))
                        min_v02=min(min_v02,float(v02)); max_v02=max(max_v02,float(v02))
    except Exception as exc:
        first_failure={"province_index":province_index,"province":state["name"],
            "indices":{"i":i,"j":j,"k":k},"b":float(b),"a":float(a),"z":float(z),
            "checked_before_failure":checked,"error_type":type(exc).__name__,"error":str(exc)}
    payload={"schema":"CH5_MP4B_PYTHON_FULL_FIRST_TURN_SOURCE_INITIALIZATION_PREFLIGHT_V1",
        "calendar_year":2009,"canonical_sha256":CANONICAL_SHA,
        "province_count":len(states),"grid_shape":[20,20,2],
        "loop_order":"province,k,j,i","checked_cell_count":checked,
        "expected_cell_count":len(states)*20*20*2,"max_abs_source_residual":max_residual,
        "minimum_c0":min_c0,"minimum_root_base":min_root_base,
        "minimum_v02":min_v02,"maximum_v02":max_v02,"first_failure":first_failure,
        "formula_guards":{"clipping":False,"epsilon_substitution":False,
            "nan_replacement":False,"formula_substitution":False,"alternate_solver":False},
        "scientific_calls":{"household":0,"hjb":0,"kfe":0,"mp2":0,"mp3":0,"stationary":0},
        "verdict":"MP4B_PYTHON_FULL_FIRST_TURN_SOURCE_INITIALIZATION_PREFLIGHT_PASS" if first_failure is None else "FAIL"}
    _write_json(Path(output_path),payload)
    if first_failure is not None:
        raise RuntimeError("full initialization preflight failed")
    return payload


def run_first_beijing_input_preflight(
    canonical_path: Path, accepted_contract_path: Path, output_path: Path,
) -> dict[str, object]:
    """Materialize the exact turn-1 Beijing household inputs without solving."""
    canonical, states = load_entry_state(canonical_path)
    state = states[0]
    grid = MatlabFaithfulHJBGrid(
        np.linspace(-2, 5, 20), np.linspace(0, 10, 20), np.array([0.8, 1.3]),
        np.array([[-1 / 3, 1 / 3], [1 / 3, -1 / 3]]),
    )
    params = EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    numerics = MatlabFaithfulHJBNumerics(1000.0, 1e-7, 100, 1e-12)
    initial_value, baseline_labor = _source_initial_arrays(state, grid, params)
    actual = {
        "EconomicParams": [params.rho, params.gamma_c, params.phi, params.chi_0,
                           params.chi_1, params.a_bar, params.mu_z, params.sigma_z],
        "HouseholdInputs": [float(state["rah"]), float(state["rb"]), float(state["tau"]),
                            [float(state["w"])], [0.0], [1.0]],
        "MatlabFaithfulHJBGrid": _jsonable(grid),
        "MatlabFaithfulHJBNumerics": [numerics.delta, numerics.convergence_tolerance,
                                      numerics.max_iterations, numerics.drift_tolerance],
        "initial_value": initial_value.tolist(),
        "baseline_labor": baseline_labor.tolist(),
        "transfer_income": float(state["Tt"]),
        "borrowing_rate_gap": float(state["rb_gap"]),
    }
    accepted = json.loads(Path(accepted_contract_path).read_text(encoding="utf-8"))
    expected = accepted["python_mapping"]
    mismatches: list[str] = []
    primitive_max_normalized_difference = 0.0

    def compare(left, right, path="$"):
        nonlocal primitive_max_normalized_difference
        if isinstance(right, dict):
            if not isinstance(left, dict) or set(left) != set(right):
                mismatches.append(path + ": key/type mismatch")
                return
            for key in right:
                compare(left[key], right[key], f"{path}.{key}")
        elif isinstance(right, list):
            if not isinstance(left, list) or len(left) != len(right):
                mismatches.append(path + ": shape mismatch")
                return
            for index, item in enumerate(right):
                compare(left[index], item, f"{path}[{index}]")
        elif isinstance(right, (int, float)) and not isinstance(right, bool):
            if not isinstance(left, (int, float)):
                mismatches.append(path)
            elif path.startswith("$.initial_value") or path.startswith("$.baseline_labor"):
                scale = max(1.0, abs(float(left)), abs(float(right)))
                normalized = abs(float(left) - float(right)) / scale
                primitive_max_normalized_difference = max(primitive_max_normalized_difference, normalized)
                if normalized > 128 * np.finfo(float).eps:
                    mismatches.append(path)
            elif float(left) != float(right):
                mismatches.append(path)
        elif left != right:
            mismatches.append(path)

    compare(actual, expected)
    payload = {
        "schema": "MP4B_STATIONARY_ENTRY_FIRST_BEIJING_INPUT_PREFLIGHT_V1",
        "marker": "MP4B_STATIONARY_ENTRY_FIRST_BEIJING_INPUT_CONFORMS_TO_ACCEPTED_HOUSEHOLD_AUTHORITY",
        "calendar_year": 2009,
        "province": canonical["province_order"][0],
        "canonical_sha256": CANONICAL_SHA,
        "accepted_contract_path": str(Path(accepted_contract_path).resolve()),
        "accepted_contract_sha256": _sha256(Path(accepted_contract_path)),
        "semantic_mismatch_count": len(mismatches),
        "semantic_mismatches": mismatches,
        "primitive_array_gate": "128*eps64*max(1,abs(x),abs(y))",
        "primitive_array_max_normalized_difference": primitive_max_normalized_difference,
        "asset_labels": {"liquid": "b", "illiquid": "a"},
        "scientific_calls": {"household": 0, "hjb": 0, "kfe": 0, "mp2": 0, "mp3": 0, "stationary": 0},
    }
    _write_json(Path(output_path), payload)
    if mismatches:
        raise RuntimeError("first-Beijing stationary-entry input mismatch")
    return payload


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
                result=solve_matlab_source_postloop_household(grid,params,HouseholdInputs(
                    float(state["rah"]),float(state["rb"]),float(state["tau"]),
                    np.array([state["w"]]),np.array([0.0]),np.array([1.0])),initial,labor,
                    float(state["Tt"]),float(state["rb_gap"]),numerics)
                call_count+=1; agg=result.aggregates; density=result.kfe.density
                effective=matlab_faithful_illiquid_return(grid.a,grid.a[-1],float(state["rah"]))
                at_tax=agg.a_ss*float(state["rah"])-float(np.sum(grid.a[None,:,None]*effective[None,:,None]*density)*result.kfe.cell_weight)
                outputs.append((agg.c_ss,agg.l_ss,agg.a_ss,agg.b_ss,at_tax,
                    result.hjb.converged,result.hjb.iterations,result.hjb.convergence_statistic))
        except Exception as exc:
            _write_json(root/f'turn_{iteration:03d}_household_failure.json', {
                "iteration":iteration,"completed_households":len(outputs),"household_call_count":call_count,
                "error_type":type(exc).__name__,"error":str(exc)})
            raise
        batch=PreFrozenHouseholdOutputBatch(
            ct=[x[0] for x in outputs],household_lt=[x[1] for x in outputs],at=[x[2] for x in outputs],
            bt=[x[3] for x in outputs],at_tax=[x[4] for x in outputs],converged=tuple(x[5] for x in outputs),
            diagnostics=tuple({"hjb_converged":x[5],"hjb_iterations":x[6],
                "hjb_statistic":x[7],"iteration":iteration} for x in outputs))
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
    if len(args) == 2 and args[0] == "--bootstrap-check":
        _write_json(Path(args[1]), BOOTSTRAP_IDENTITY)
        return 0
    if len(args) == 3 and args[0] == "--full-initialization-check":
        run_full_initialization_preflight(Path(args[1]),Path(args[2]))
        return 0
    if len(args) == 4 and args[0] == "--first-beijing-input-check":
        run_first_beijing_input_preflight(Path(args[1]), Path(args[2]), Path(args[3]))
        return 0
    if len(args) != 2:
        raise SystemExit(
            "usage: mp4b_python_empirical.py CANONICAL_JSON FRESH_RUN_ROOT | "
            "--bootstrap-check FRESH_MANIFEST_JSON | "
            "--full-initialization-check CANONICAL_JSON FRESH_MANIFEST_JSON | "
            "--first-beijing-input-check CANONICAL_JSON ACCEPTED_CONTRACT_JSON FRESH_MANIFEST_JSON"
        )
    run_python_once(Path(args[0]),Path(args[1]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
