"""Run exactly one original call725 household with rah=float('0.07')."""
import copy
import io
import contextlib
import json
import os
from pathlib import Path
import platform
import sys
import time
import traceback
import warnings

RUNTIME = Path(os.environ["CH5_RAH07_RUNTIME"])
BASELINE = Path(os.environ["CH5_RAH07_BASELINE"])
sys.path[:0] = [str(RUNTIME), str(RUNTIME / "src"), str(Path(__file__).resolve().parent)]

import numpy as np
import scipy
from evidence import Store, decode_saved
from validators.multi_province import mp4b_python_empirical as anchor
from validators.multi_province import mp4b_matlab_source_postloop_household_adapter as adapter
import exports.matlab_faithful_two_asset_ha as faithful


def run(root):
    root = Path(root)
    store = Store(root / "science")
    entry = decode_saved(BASELINE / "capture/call_0725/entry.json")
    hjb_entry = decode_saved(BASELINE / "capture/call_0725/hjb_entry.json")
    state09 = entry["state"]
    state07 = copy.deepcopy(state09)
    state07["rah"] = float("0.07")
    grid = faithful.MatlabFaithfulHJBGrid(entry["grid"]["b"], entry["grid"]["a"], entry["grid"]["z"], entry["grid"]["switch_matrix"])
    params = faithful.EconomicParams(**entry["params"])
    old_inputs = hjb_entry["inputs"]
    inputs = faithful.HouseholdInputs(float(state07["rah"]), float(state07["rb"]), float(state07["tau"]), old_inputs["wages"], old_inputs["migration_costs"], old_inputs["labor_weights"])
    numerics = faithful.MatlabFaithfulHJBNumerics(**hjb_entry["numerics"])
    counts = {name: 0 for name in ("native_initialization", "labor_root", "brentq", "root_residual", "root_bracketing_residual", "root_brentq_residual", "adapter", "HJB", "HJB_return", "HJB_direct_solve", "KFE", "KFE_direct_solve", "KFE_return", "aggregate", "aggregate_return")}
    per_call = {"labor_root": 0, "brentq": 0, "HJB_direct_solve": 0, "KFE_direct_solve": 0}
    restores = []
    phase = "BOUND"
    in_brentq = False
    deadline = time.monotonic() + 900

    def patch(module, name, replacement):
        original = getattr(module, name)
        restores.append((module, name, original))
        setattr(module, name, replacement)
        return original

    def check_time():
        if time.monotonic() >= deadline:
            raise TimeoutError("15-minute scientific wall ceiling")

    labor_original = anchor._source_labor_root
    residual_codes = {code for code in labor_original.__code__.co_consts if hasattr(code, "co_name") and code.co_name == "residual"}

    def profile(frame, event, arg):
        if event == "call" and frame.f_code in residual_codes:
            counts["root_residual"] += 1
            counts["root_brentq_residual" if in_brentq else "root_bracketing_residual"] += 1

    def labor(*args, **kwargs):
        check_time()
        counts["labor_root"] += 1
        per_call["labor_root"] += 1
        if counts["labor_root"] > 800:
            raise RuntimeError("labor-root budget exceeded")
        previous = sys.getprofile()
        sys.setprofile(profile)
        try:
            return labor_original(*args, **kwargs)
        finally:
            sys.setprofile(previous)

    brent_original = anchor.brentq

    def brent(*args, **kwargs):
        nonlocal in_brentq
        counts["brentq"] += 1
        per_call["brentq"] += 1
        if counts["brentq"] > 800:
            raise RuntimeError("brentq budget exceeded")
        in_brentq = True
        try:
            return brent_original(*args, **kwargs)
        finally:
            in_brentq = False

    direct_original = faithful.linalg.spsolve

    def direct(matrix, rhs, *args, **kwargs):
        key = "KFE_direct_solve" if phase == "KFE" else "HJB_direct_solve" if phase == "HJB" else None
        if key is None:
            raise RuntimeError("unexpected direct solve phase")
        counts[key] += 1
        per_call[key] += 1
        if counts["HJB_direct_solve"] > 100 or counts["KFE_direct_solve"] > 1:
            raise RuntimeError("direct-solve budget exceeded")
        if phase == "KFE":
            store.save("kfe_direct_input", {"matrix": matrix, "rhs": rhs})
        result = direct_original(matrix, rhs, *args, **kwargs)
        if phase == "KFE":
            store.save("kfe_direct_return", {"raw": result})
        return result

    hjb_original = faithful.solve_matlab_faithful_hjb

    def hjb(*args, **kwargs):
        nonlocal phase
        check_time()
        counts["HJB"] += 1
        if counts["HJB"] > 1:
            raise RuntimeError("HJB budget exceeded")
        phase = "HJB"
        store.save("hjb_entry", {"grid": args[0], "params": args[1], "inputs": args[2], "initial_value": args[3], "baseline_labor": args[4], "transfer_income": args[5], "borrowing_rate_gap": args[6], "numerics": args[7]})
        result = hjb_original(*args, **kwargs)
        counts["HJB_return"] += 1
        store.save("hjb_return_before_kfe", result)
        phase = "HJB_RETURN_SAVED"
        return result

    kfe_original = faithful.solve_matlab_faithful_stationary_kfe

    def kfe(*args, **kwargs):
        nonlocal phase
        check_time()
        counts["KFE"] += 1
        if counts["KFE"] > 1:
            raise RuntimeError("KFE budget exceeded")
        phase = "KFE"
        store.save("kfe_entry", {"operator": args[0], "kwargs": kwargs})
        result = kfe_original(*args, **kwargs)
        counts["KFE_return"] += 1
        store.save("kfe_return", result)
        return result

    aggregate_original = faithful.aggregate_stationary_household

    def aggregate(*args, **kwargs):
        nonlocal phase
        counts["aggregate"] += 1
        if counts["aggregate"] > 1:
            raise RuntimeError("aggregate budget exceeded")
        phase = "AGGREGATE"
        result = aggregate_original(*args, **kwargs)
        counts["aggregate_return"] += 1
        store.save("aggregate_return", result)
        return result

    config = io.StringIO()
    with contextlib.redirect_stdout(config):
        np.show_config()
    store.save("environment", {"pid": os.getpid(), "python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__, "platform": platform.platform(), "blas": config.getvalue(), "threads": {name: os.environ.get(name) for name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS")}, "module_paths": {"anchor": anchor.__file__, "adapter": adapter.__file__, "faithful": faithful.__file__}})
    store.save("binding", {"baseline_context": entry["context"], "state_09": state09, "state_07": state07, "state_diff": {"rah": {"old": state09["rah"], "new": state07["rah"], "repr": repr(state07["rah"]), "hex": state07["rah"].hex()}}, "mapped_input_diff": {"r_a": {"old": old_inputs["r_a"], "new": inputs.r_a, "repr": repr(inputs.r_a), "hex": inputs.r_a.hex()}}, "grid": grid, "params": params, "inputs_09": old_inputs, "inputs_07": inputs, "numerics": numerics})
    terminal = "PRE_SCIENCE"
    error = None
    started = time.monotonic()
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            patch(anchor, "_source_labor_root", labor)
            patch(anchor, "brentq", brent)
            patch(faithful.linalg, "spsolve", direct)
            counts["native_initialization"] += 1
            phase = "NATIVE_INITIALIZATION"
            initial, baseline_labor = anchor._source_initial_arrays(state07, grid, params)
            store.save("native_initialization_return", {"initial_value": initial, "baseline_labor": baseline_labor})
            counts["adapter"] += 1
            phase = "ADAPTER"
            result = adapter.solve_matlab_source_postloop_household(grid, params, inputs, initial, baseline_labor, float(state07["Tt"]), float(state07["rb_gap"]), numerics, hjb_solver=hjb, kfe_solver=kfe, aggregator=aggregate)
            store.save("household_return", result)
            terminal = "NORMAL_RETURN"
        except BaseException as exception:
            terminal = "ORIGINAL_EXCEPTION"
            error = {"type": type(exception).__name__, "message": str(exception), "traceback": traceback.format_exc()}
        finally:
            warning_rows = [{"category": item.category.__name__, "message": str(item.message), "filename": item.filename, "lineno": item.lineno} for item in caught]
            store.save("terminal", {"terminal": terminal, "error": error, "phase": phase, "last_durable_stage": store.last, "counts": counts, "per_call": per_call, "warnings": warning_rows, "scientific_seconds": time.monotonic() - started, "scientific_processes": 1, "scientific_restarts": 0, "Results_eligible": False})
            for module, name, original in reversed(restores):
                setattr(module, name, original)
            store.close()
    print(json.dumps({"terminal": terminal, "counts": counts, "error": error and error["message"]}), flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    run(Path(sys.argv[1]))
