"""Terminal-only MP4C annual production worker; importing it performs no science."""
from __future__ import annotations

import argparse
import csv
import json
import os
import platform
import sys
import time
from dataclasses import asdict
from hashlib import sha256
from pathlib import Path
from typing import Any, Mapping

import numpy as np
from scipy.io import loadmat, savemat

REPO_ROOT = Path(__file__).resolve().parents[2]
for root in (REPO_ROOT / "src", REPO_ROOT):
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

from validators.multi_province import mp4b_python_empirical as anchor
from validators.multi_province import mp4c_python_annual_empirical as empirical
from validators.multi_province import mp4c_matlab_runtime_cache as runtime_cache
from ch5_two_asset_hank.multi_province.one_turn import PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.stationary_runtime import OnlineStationaryInputs, run_online_stationary
from ch5_two_asset_hank.multi_province.steady_state import SteadyStateConvergenceError

SUPPORTED_YEARS = tuple(range(2009, 2024))
FINAL_FIELDS = ("Ct", "At", "Bt", "Lt", "Lt_supply", "Kt_supply", "rah", "Kt", "Yt", "mt", "KNratio", "w", "wjt", "rk", "ra", "GovInv", "rb", "it", "Zt", "Govinc")
CHECKPOINT_SCHEMA = "CH5_MP4C_FINAL_HOUSEHOLD_CHECKPOINT_V1"
THREAD_ENV = {name: "1" for name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS")}


def _sha(path: Path) -> str:
    h = sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def _jsonable(value: Any) -> Any:
    if isinstance(value, np.ndarray): return value.tolist()
    if isinstance(value, np.generic): return value.item()
    if isinstance(value, Path): return str(value.resolve())
    if hasattr(value, "__dataclass_fields__"): return {k: _jsonable(v) for k, v in asdict(value).items()}
    if isinstance(value, Mapping): return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)): return [_jsonable(v) for v in value]
    return value


def write_json_no_overwrite(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(_jsonable(payload), stream, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        stream.write("\n")


def scientific_identities() -> dict[str, str]:
    paths = [
        Path(__file__), Path(runtime_cache.__file__), Path(empirical.__file__), REPO_ROOT / "src/ch5_two_asset_hank/multi_province/annual.py",
        REPO_ROOT / "src/ch5_two_asset_hank/multi_province/one_turn.py",
        REPO_ROOT / "src/ch5_two_asset_hank/multi_province/firm.py",
        REPO_ROOT / "src/ch5_two_asset_hank/multi_province/stationary_runtime.py",
        REPO_ROOT / "validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py",
        REPO_ROOT / "src/ch5_two_asset_hank/matlab_faithful_hjb.py",
        REPO_ROOT / "src/ch5_two_asset_hank/matlab_faithful_kfe.py",
    ]
    return {str(p.relative_to(REPO_ROOT)).replace("\\", "/"): _sha(p) for p in paths}


def serialize_final_state(states: tuple[Mapping[str, object], ...]) -> list[dict[str, object]]:
    if len(states) != 31 or len({str(s["name"]) for s in states}) != 31:
        raise ValueError("final state must contain 31 unique ordered provinces")
    rows = []
    for state in states:
        row = {"name": str(state["name"])}
        for field in FINAL_FIELDS:
            value = float(state[field])
            if not np.isfinite(value): raise ValueError(f"non-finite final field: {field}")
            row[field] = value
        rows.append(row)
    return rows


def validate_lt_mat(matrix: np.ndarray, province_order: list[str]) -> np.ndarray:
    value = np.asarray(matrix, dtype=float)
    if value.shape != (31, 31) or len(province_order) != 31 or not np.isfinite(value).all():
        raise ValueError("Lt_mat must be finite 31x31 with 31 province axes")
    return value


def extract_household_checkpoint(result: Any, grid: Any, province: str) -> dict[str, Any]:
    hjb, kfe = result.hjb, result.kfe
    return {
        "province": province, "grid_b": grid.b, "grid_a": grid.a, "grid_z": grid.z,
        "switch_matrix": grid.switch_matrix, "value": hjb.value, "initial_value": hjb.initial_value,
        "consumption": hjb.consumption, "labor": hjb.labor, "transfer": hjb.transfer,
        "adjustment_cost": hjb.adjustment_cost, "effective_illiquid_return": hjb.effective_illiquid_return,
        "mu_a": hjb.mu_a, "mu_b": hjb.mu_b, "utility": hjb.utility,
        "liquid_label": hjb.liquid_label.astype("U1"), "transfer_label": hjb.transfer_label.astype("U1"),
        "kfe_density": kfe.density, "hjb_iterations": np.int64(hjb.iterations),
        "hjb_converged": np.int8(hjb.converged), "hjb_statistic": np.float64(hjb.convergence_statistic),
    }


def persist_checkpoint(root: Path, year: int, canonical_sha: str, source_hashes: Mapping[str, str],
                       province_order: list[str], checkpoints: list[dict[str, Any]], terminal_sha: str) -> dict[str, Any]:
    if len(checkpoints) != 31: raise ValueError("checkpoint requires 31 final household objects")
    arrays: dict[str, np.ndarray] = {}
    for index, item in enumerate(checkpoints):
        for key, value in item.items(): arrays[f"p{index:02d}_{key}"] = np.asarray(value)
    npz = root / "final_household_restart.npz"
    if npz.exists(): raise FileExistsError(npz)
    np.savez_compressed(npz, **arrays)
    mat = root / f"Python_Multi_Province_12sts_{year}.mat"
    if mat.exists(): raise FileExistsError(mat)
    savemat(mat, {"checkpoint_schema": CHECKPOINT_SCHEMA, "calendar_year": year,
                  "province_order": np.asarray(province_order, dtype=object), **arrays}, do_compression=True)
    manifest = {
        "schema": CHECKPOINT_SCHEMA, "calendar_year": year, "canonical_sha256": canonical_sha,
        "source_hashes": dict(source_hashes), "scientific_code_identities": scientific_identities(),
        "province_order": province_order, "terminal_sha256": terminal_sha,
        "npz": {"path": npz.name, "sha256": _sha(npz), "bytes": npz.stat().st_size},
        "mat": {"path": mat.name, "sha256": _sha(mat), "bytes": mat.stat().st_size},
        "compatibility": "PYTHON_SOURCE_BACKED_CHECKPOINT_NOT_LEGACY_MATLAB_ST_DROP_IN",
        "matlab_contract_coverage": {
            "results": "final_steady_state.json plus final household arrays",
            "grids": "grid_b/grid_a/grid_z/switch_matrix in NPZ and MAT",
            "param_num": "bound by scientific code identities and run_manifest.json",
            "data_MAT": "represented by canonical annual input JSON and SHA, not copied as a legacy MATLAB struct",
            "CHI": "Python policy/cost implementation is bound by code identity; no standalone MATLAB CHI struct is fabricated",
            "sigmau_MAT": "canonical matrices.sigmau; live shock source reloads it rather than consuming st.sigmau_MAT",
            "N_prov": 31
        },
    }
    write_json_no_overwrite(root / "checkpoint_manifest.json", manifest)
    return manifest


def run_year(runtime_input_path: Path, cache_path: Path, run_root: Path) -> int:
    root = Path(run_root); root.mkdir(parents=True, exist_ok=False)
    supplied=json.loads(Path(runtime_input_path).read_text(encoding="utf-8"));year=int(supplied["binding"]["calendar_year"])
    rebuilt=runtime_cache.add_runtime_support(runtime_cache.load_runtime_year(cache_path,year),distance_workbook=empirical.primary_sources(REPO_ROOT/"data_local/matlab_primary_source_snapshot").distance_workbook,distance_sha256=empirical.SOURCE_HASHES["中国各省省会地理距离矩阵.xlsx"],max_sigmau=empirical.accepted_source_scalars().max_sigmau)
    if runtime_cache.canonical_bytes(rebuilt)!=Path(runtime_input_path).read_bytes():raise ValueError("runtime input bytes do not match exact cache materialization")
    canonical=supplied; scalars=asdict(empirical.accepted_source_scalars());states=runtime_cache.entry_states(canonical,scalars)
    if year not in SUPPORTED_YEARS: raise ValueError(f"unsupported calendar year: {year}")
    canonical_copy = root / f"calendar_{year}_matlab_runtime_cache_input.json"
    canonical_copy.write_bytes(Path(runtime_input_path).read_bytes())
    canonical_sha = _sha(canonical_copy); started = time.time(); started_mono = time.monotonic()
    grid = anchor.MatlabFaithfulHJBGrid(np.linspace(-2,5,20), np.linspace(0,10,20), np.array([0.8,1.3]), np.array([[-1/3,1/3],[1/3,-1/3]]))
    params = anchor.EconomicParams(0.05,2.0,5.0,0.1,2.0,1e-6,0.0,0.0)
    numerics = anchor.MatlabFaithfulHJBNumerics(1000.0,1e-7,100,1e-12)
    calls = 0; phi = np.ones((31,31)); final_checkpoints: list[dict[str, Any]] = []

    def solve_batch(snapshot, iteration):
        nonlocal calls, final_checkpoints
        if calls + 31 > empirical.MAX_HOUSEHOLD_CALLS: raise RuntimeError("household-call ceiling would be exceeded")
        prod=np.array([float(s["Yt"])/float(s["Lt"]) for s in snapshot]); phi[:]=1+0.3*(prod[:,None]-prod[None,:])/(prod[:,None]+prod[None,:])
        outputs=[]; current=[]
        for state in snapshot:
            initial,labor=anchor._source_initial_arrays(state,grid,params)
            result=anchor.solve_matlab_source_postloop_household(grid,params,anchor.HouseholdInputs(float(state["rah"]),float(state["rb"]),float(state["tau"]),np.array([state["w"]]),np.array([0.0]),np.array([1.0])),initial,labor,float(state["Tt"]),float(state["rb_gap"]),numerics)
            calls += 1; aggregate=result.aggregates; density=result.kfe.density
            effective=anchor.matlab_faithful_illiquid_return(grid.a,grid.a[-1],float(state["rah"]))
            at_tax=aggregate.a_ss*float(state["rah"])-float(np.sum(grid.a[None,:,None]*effective[None,:,None]*density)*result.kfe.cell_weight)
            outputs.append((aggregate.c_ss,aggregate.l_ss,aggregate.a_ss,aggregate.b_ss,at_tax,result.hjb.converged,result.hjb.iterations,result.hjb.convergence_statistic))
            current.append(extract_household_checkpoint(result,grid,str(state["name"])))
        final_checkpoints=current
        return PreFrozenHouseholdOutputBatch(ct=[x[0] for x in outputs],household_lt=[x[1] for x in outputs],at=[x[2] for x in outputs],bt=[x[3] for x in outputs],at_tax=[x[4] for x in outputs],converged=tuple(x[5] for x in outputs),diagnostics=tuple({"hjb_converged":x[5],"hjb_iterations":x[6],"hjb_statistic":x[7],"iteration":iteration} for x in outputs))

    manifest={"schema":"CH5_MP4C_ANNUAL_PRODUCTION_RUN_V2","representation":runtime_cache.REPRESENTATION,"logging_mode":"terminal-only","calendar_year":year,"runtime_input_sha256":canonical_sha,"runtime_cache_sha256":canonical["cache_sha256"],"scientific_code_identities":scientific_identities(),"max_outer_turns":empirical.MAX_OUTER_TURNS,"max_household_calls":empirical.MAX_HOUSEHOLD_CALLS,"automatic_reruns":0,"wall_clock_timeout_seconds":None,"thread_environment":{k:os.environ.get(k) for k in THREAD_ENV}}
    write_json_no_overwrite(root/"run_manifest.json",manifest)
    model_params={"ga":2.0,"phi_l":5.0,"alphal":1.0,"epsilon":10.0,"theta":100.0,"delta":0.025,"istar":0.015,"rho_pi":1.25,"totalpit":0.02,"epsilon_pi":0.0}
    try:
        result=run_online_stationary(OnlineStationaryInputs(tuple(canonical["province_order"]),states,model_params,phi,np.array(canonical["runtime_support"]["sigmau_destination_origin"]),solve_batch,1e-9,empirical.MAX_OUTER_TURNS,True))
    except SteadyStateConvergenceError as exc: result=exc.result
    rows=serialize_final_state(result.final_state); last=result.history[-1]
    lt=validate_lt_mat(np.asarray(last.one_turn.migration.lt_mat),list(canonical["province_order"]))
    np.save(root/"Lt_mat_destination_row_origin_column.npy",lt)
    terminal={"schema":"CH5_MP4C_ANNUAL_TERMINAL_V1","calendar_year":year,"status":result.termination_reason,"converged":bool(result.converged),"iteration_count":result.iteration_count,"household_call_count":calls,"household_converged_count":last.household_converged_count,"ra_upper_count":last.ra_upper_count,"ra_lower_count":last.ra_lower_count,"wage_upper_count":last.wage_upper_count,"wage_lower_count":last.wage_lower_count,"province_order":canonical["province_order"],"final_31x20":rows,"legacy_workbook_rows":[{"name":str(s["name"]),"Yt0":float(s["Yt0"])/float(canonical["scalars"]["gdp_multiplier"]),"Yt":float(s["Yt"])/float(canonical["scalars"]["gdp_multiplier"]),"Kt0":float(s["Kt0"])/float(canonical["scalars"]["gdp_multiplier"]),"Kt":float(s["Kt"])/float(canonical["scalars"]["gdp_multiplier"]),"Lt0":float(s["N"])/float(canonical["scalars"]["pop_multiplier"]),"Lt":float(s["Lt"])/float(canonical["scalars"]["pop_multiplier"])} for s in result.final_state],"national":{f:sum(float(r[f]) for r in rows) for f in ("Ct","At","Bt","Yt")},"Lt_mat":{"orientation":"destination_row_x_origin_column","row_axis":canonical["province_order"],"column_axis":canonical["province_order"],"path":"Lt_mat_destination_row_origin_column.npy"},"wall_clock_seconds":time.monotonic()-started_mono}
    write_json_no_overwrite(root/"final_steady_state.json",terminal); terminal_sha=_sha(root/"final_steady_state.json")
    with (root/"final_31x20.csv").open("x",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["name",*FINAL_FIELDS]); w.writeheader(); w.writerows(rows)
    persist_checkpoint(root,year,canonical_sha,{"数据估计结果_1000_100_0.mat":canonical["cache_sha256"],"中国各省省会地理距离矩阵.xlsx":canonical["runtime_support"]["distance_sha256"]},list(canonical["province_order"]),final_checkpoints,terminal_sha)
    timing={"calendar_year":year,"start_epoch":started,"end_epoch":time.time(),"wall_clock_seconds":time.monotonic()-started_mono,"process_status":result.termination_reason}
    write_json_no_overwrite(root/"year_timing.json",timing)
    required=[canonical_copy,root/"run_manifest.json",root/"final_steady_state.json",root/"final_31x20.csv",root/"Lt_mat_destination_row_origin_column.npy",root/"final_household_restart.npz",root/f"Python_Multi_Province_12sts_{year}.mat",root/"checkpoint_manifest.json",root/"year_timing.json"]
    marker={"schema":"CH5_MP4C_YEAR_SUCCESS_V2","representation":runtime_cache.REPRESENTATION,"year":year,"status":result.termination_reason,"runtime_input_sha256":canonical_sha,"runtime_cache_sha256":canonical["cache_sha256"],"scientific_code_identities":scientific_identities(),"checkpoint_schema":CHECKPOINT_SCHEMA,"outputs":{p.name:{"sha256":_sha(p),"bytes":p.stat().st_size} for p in required}}
    name="SUCCESS.json" if result.converged else "FAILURE.json"; write_json_no_overwrite(root/name,marker)
    return 0 if result.converged else 2


def main(argv=None) -> int:
    parser=argparse.ArgumentParser(); parser.add_argument("runtime_input"); parser.add_argument("runtime_cache"); parser.add_argument("output_root")
    args=parser.parse_args(argv); return run_year(Path(args.runtime_input),Path(args.runtime_cache),Path(args.output_root))

if __name__ == "__main__": raise SystemExit(main())
