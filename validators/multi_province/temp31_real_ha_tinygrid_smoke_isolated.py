"""Frozen real TEMP31 smoke child. Run only through the 30-second supervisor."""
from __future__ import annotations

import argparse
import ast
import hashlib
import importlib
import importlib.machinery
import importlib.util
import json
import os
from pathlib import Path
import sys
import traceback
import types

TASK = "CH5_TEMP31_REAL_HA_RUNTIME_TINYGRID_SMOKE_R1_20261029"
SOURCE = "b4f5471aeca304f60da4bd2340e4238561c5a92d"
WORK = Path(__file__).resolve().parents[2]
THREAD_KEYS = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
               "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "BLIS_NUM_THREADS")


def emit(event: str, **values) -> None:
    print(json.dumps(dict(event=event, **values), allow_nan=False), flush=True)


def namespace(name: str, path: Path) -> None:
    assert name not in sys.modules, "unexpected preloaded scientific package"
    module = types.ModuleType(name)
    module.__path__ = [str(path)]
    module.__package__ = name
    module.__spec__ = importlib.machinery.ModuleSpec(name, loader=None, is_package=True)
    module.__spec__.submodule_search_locations = module.__path__
    sys.modules[name] = module


def run(args) -> int:
    counts = {k: 0 for k in ("initializer_batches", "root_cells", "brentq_calls",
                            "direct_policy_cells", "hjb_policy_cells", "hjb_driver_calls",
                            "hjb_iteration_entries", "operator_assemblies", "linear_solves")}
    root_wages = []
    stage = "SUPERVISOR_HANDSHAKE"
    import_pass = False
    init_policy_pass = False
    hjb_executed = False
    active_hjb = 0
    try:
        assert sys.stdin.readline().strip() == "GO", "supervisor handshake required"
        assert all(os.environ.get(k) == "1" for k in THREAD_KEYS), "BLAS thread gate"
        assert sys.version_info >= (3, 11)
        stage = "SOURCE_IDENTITY"
        report = WORK / "tasks" / TASK
        identity = json.loads((report / "source_identity.json").read_text(encoding="utf-8"))
        frozen = json.loads((report / "grid_and_parameters.json").read_text(encoding="utf-8"))
        assert identity["source"]["commit"] == SOURCE and len(identity["source_files"]) == 8
        source_root = args.source_root.absolute()
        expected_paths = {}
        for row in identity["source_files"]:
            relative = row["path"].removeprefix("src/")
            path = source_root / relative
            # Never follow source symlinks or Windows reparse points.
            current = path
            while current != source_root.parent:
                attrs = os.lstat(current)
                assert not (getattr(attrs, "st_file_attributes", 0) & 0x400)
                assert not path.is_symlink()
                current = current.parent
            raw = path.read_bytes()
            assert len(raw) == row["bytes"] and hashlib.sha256(raw).hexdigest() == row["sha256"]
            assert hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest() == row["git_blob"]
            expected_paths[relative[:-3].replace("/", ".")] = (path, row)
        stage = "IMPORT_RUNTIME"
        namespace("ch5_two_asset_hank", source_root / "ch5_two_asset_hank")
        namespace("ch5_two_asset_hank.multi_province", source_root / "ch5_two_asset_hank/multi_province")
        modules = {name: importlib.import_module(name) for name in expected_paths}
        loaded_names = {name for name in sys.modules if name.startswith("ch5_two_asset_hank.")}
        assert loaded_names == set(expected_paths) | {"ch5_two_asset_hank.multi_province"}
        origins = []
        for name, (path, row) in expected_paths.items():
            module = modules[name]
            assert Path(module.__file__).absolute() == path
            assert isinstance(module.__loader__, importlib.machinery.SourceFileLoader)
            origins.append({"module": name, "file": module.__file__, "git_blob": row["git_blob"],
                            "sha256": row["sha256"], "bytes": row["bytes"]})
        import numpy as np
        import scipy
        thread_pools = []
        thread_count_scope = "ENVIRONMENT_LIMITS_1; native thread counts unavailable"
        if importlib.util.find_spec("threadpoolctl") is not None:
            from threadpoolctl import threadpool_info
            thread_pools = [{k: item.get(k) for k in ("user_api", "internal_api", "num_threads", "prefix")}
                            for item in threadpool_info()]
            assert all(item["num_threads"] == 1 for item in thread_pools
                       if item["user_api"] in ("blas", "openmp")), "native thread limit drift"
            thread_count_scope = "native threadpoolctl observation plus frozen environment"
        imports = {name.rsplit(".", 1)[-1]: module for name, module in modules.items()}
        bootstrap = imports["temp31_ha_taxfree_bootstrap"]
        hjb = imports["temp31_netwage_hjb"]
        policy = imports["temp31_netwage_policy"]
        operator = imports["matlab_faithful_operator"]
        contracts = imports["contracts"]
        import_pass = True
        emit("import_runtime", status="IMPORT_RUNTIME_PASS", source_commit=SOURCE,
             python=sys.version.split()[0], numpy=np.__version__, scipy=scipy.__version__,
             modules=origins, skipped_package_initializers=identity["skipped_package_initializers"],
             blas_environment={k: os.environ[k] for k in THREAD_KEYS},
             thread_pools=thread_pools, thread_count_scope=thread_count_scope)

        targets = {bootstrap.temp31_netwage_initial_arrays.__code__: "initializer_batches",
                   bootstrap._temp31_source_labor_root.__code__: "root_cells",
                   bootstrap.brentq.__code__: "brentq_calls",
                   policy.select_temp31_netwage_local_policy.__code__: "policy",
                   hjb.solve_temp31_netwage_hjb.__code__: "hjb_driver_calls",
                   operator.assemble_source_operator.__code__: "operator_assemblies",
                   hjb.linalg.spsolve.__code__: "linear_solves"}
        limits = {"initializer_batches": 1, "root_cells": 8, "brentq_calls": 8,
                  "direct_policy_cells": 1 if args.phase == "import-initial-policy" else 0,
                  "hjb_policy_cells": 0 if args.phase == "import-initial-policy" else 8,
                  "hjb_driver_calls": 0 if args.phase == "import-initial-policy" else 1,
                  "operator_assemblies": 0 if args.phase == "import-initial-policy" else 2,
                  "linear_solves": 0 if args.phase == "import-initial-policy" else 1,
                  "hjb_iteration_entries": 0 if args.phase == "import-initial-policy" else 1}

        def increment(name):
            counts[name] += 1
            assert counts[name] <= limits[name], "CALL_BUDGET_EXCEEDED: " + name

        def profile(frame, event, arg):
            nonlocal active_hjb
            name = targets.get(frame.f_code)
            if name is None:
                return
            if event == "call":
                if name == "policy":
                    increment("hjb_policy_cells" if active_hjb else "direct_policy_cells")
                else:
                    increment(name)
                if name == "hjb_driver_calls":
                    active_hjb += 1
                if name == "root_cells":
                    root_wages.append(float(frame.f_locals["wage"]))
            elif event == "return" and name == "hjb_driver_calls":
                active_hjb -= 1

        tree = ast.parse(Path(hjb.__file__).read_bytes().decode("utf-8"))
        definition = next(n for n in tree.body if isinstance(n, ast.FunctionDef)
                          and n.name == "solve_temp31_netwage_hjb")
        iteration_loop = next(n for n in definition.body if isinstance(n, ast.For)
                              and isinstance(n.target, ast.Name) and n.target.id == "iteration")
        loop_entry_line = iteration_loop.body[0].lineno

        def trace_hjb(frame, event, arg):
            if event == "line" and frame.f_lineno == loop_entry_line:
                increment("hjb_iteration_entries")
            return trace_hjb

        def trace_calls(frame, event, arg):
            return trace_hjb if frame.f_code is hjb.solve_temp31_netwage_hjb.__code__ else None

        sys.setprofile(profile)
        sys.settrace(trace_calls)
        stage = "INPUT_CONTRACT"
        params = contracts.EconomicParams(**frozen["EconomicParams"])
        record = bootstrap.numerical_bootstrap19(context_id=frozen["context_id"],
            province_order=tuple(frozen["province_order"]), tax_by_destination=frozen["tax_by_destination"],
            sigma_destination_origin=frozen["sigma_destination_origin"], w_initial=20.0,
            tau_legacy_reference=0.05)
        assert type(record) is bootstrap.Temp31EffectiveWageRecord
        assert record.entering_iteration == 1 and record.effective_wages_by_origin == (19.0, 19.0)
        assert record.semantics == bootstrap.NUMERICAL_NET_WAGE_INITIAL_GUESS_NOT_EMPIRICAL
        inputs = bootstrap.netwage_inputs(record, origin_index=0, r_a=0.09, r_b=0.02,
            expected_context_id=frozen["context_id"], expected_province_order=("A", "B"))
        assert inputs.wages.tolist() == [19.0] and inputs.labor_weights.tolist() == [1.0]
        assert not hasattr(inputs, "tau") and not hasattr(inputs, "migration_costs")
        assert record.tax_by_destination == (0.05, 0.05) and record.sigma_destination_origin == ((0.0, 0.0), (0.0, 0.0))
        grid = hjb.Temp31NetWageHJBGrid(**{k: np.array(v, dtype=float) for k, v in frozen["grid"].items()})
        shape = (grid.b.size, grid.a.size, grid.z.size)
        assert shape == (2, 2, 2) and int(np.prod(shape)) == 8
        state = {"rah": 0.09, "rb": 0.02, "rb_gap": 0.07, "Tt": 0.1}
        stage = "INITIALIZER"
        value, labor = bootstrap.temp31_netwage_initial_arrays(state, grid, params, inputs)
        assert value.shape == labor.shape == shape and np.isfinite(value).all() and np.isfinite(labor).all()
        assert counts["initializer_batches"] == 1 and counts["root_cells"] == 8
        assert set(root_wages) == {19.0 * 0.8, 19.0 * 1.3}, "initializer effective wage drift"
        emit("initializer", shape=list(shape), finite=True,
             value_min=float(value.min()), value_max=float(value.max()),
             labor_min=float(labor.min()), labor_max=float(labor.max()),
             wage_record_semantics=record.semantics, effective_wage=19.0,
             observed_root_wage_coefficients=sorted(set(root_wages)),
             context_id=record.context_id, province_order=list(record.province_order), counts=dict(counts))

        if args.phase == "import-initial-policy":
            stage = "DIRECT_POLICY_CELL"
            result = policy.select_temp31_netwage_local_policy(
                a=0.0, b=-2.0, z=0.8,
                v_a_forward=1.0, v_a_backward=1.0, v_b_forward=1.0, v_b_backward=1.0,
                baseline_labor=float(labor[0, 0, 0]), transfer_income=0.1, borrowing_rate_gap=0.07,
                a_max=10.0, da=10.0, db=7.0, at_lower_a=True, at_upper_a=False,
                at_lower_b=True, at_upper_b=False, inputs=inputs, params=params, tolerance=1e-12)
            summary = {name: float(getattr(result, name)) for name in
                       ("consumption", "labor", "transfer", "adjustment_cost",
                        "effective_illiquid_return", "mu_a", "mu_b", "utility")}
            assert np.isfinite(list(summary.values())).all()
            assert counts["direct_policy_cells"] == 1 and counts["hjb_driver_calls"] == 0
            init_policy_pass = True
            emit("direct_policy", finite=True, result_type=type(result).__name__,
                 summary=summary, liquid_label=result.liquid_label, transfer_label=result.transfer_label)
        else:
            stage = "TINY_HJB_DRIVER"
            numerics = hjb.Temp31NetWageHJBNumerics(**frozen["numerics"])
            result = hjb.solve_temp31_netwage_hjb(grid, params, inputs, value, labor, 0.1, 0.07, numerics)
            hjb_executed = True
            arrays = ("value", "initial_value", "consumption", "labor", "transfer", "adjustment_cost",
                      "effective_illiquid_return", "mu_a", "mu_b", "utility")
            finite = all(np.isfinite(getattr(result, name)).all() for name in arrays)
            finite = finite and np.isfinite(result.operator.full.data).all() and np.isfinite(result.post_convergence_operator.full.data).all()
            assert finite and np.isfinite(result.convergence_statistic)
            assert result.iterations == counts["hjb_iteration_entries"] == 1
            assert counts["hjb_policy_cells"] == 8 and counts["linear_solves"] == 1 and counts["operator_assemblies"] == 2
            emit("tiny_hjb", status="TINY_HJB_ONE_ITERATION_EXECUTED", finite=bool(finite),
                 iterations=int(result.iterations), converged=bool(result.converged),
                 convergence_statistic=float(result.convergence_statistic),
                 value_min=float(result.value.min()), value_max=float(result.value.max()),
                 operator_shape=list(result.operator.full.shape), operator_nnz=int(result.operator.full.nnz),
                 source_post_iteration_operator_assembly_count=counts["operator_assemblies"],
                 science_scope="one synthetic iteration, not steady-state convergence")
        sys.setprofile(None)
        sys.settrace(None)
        emit("phase_result", phase=args.phase, outcome="PASS_BOUNDED_RUNTIME_SMOKE",
             import_status="IMPORT_RUNTIME_PASS",
             initializer_policy_status="INITIALIZER_POLICY_CELL_PASS" if init_policy_pass else "phase2 reinitialization finite; no extra direct policy call",
             hjb_status="TINY_HJB_ONE_ITERATION_EXECUTED" if hjb_executed else "NOT_EXECUTED",
             counts=counts, KFE_GE_IRF=0, outer_steady_state_turns=0, empirical_data_reads=0)
        return 0
    except BaseException as exc:
        sys.setprofile(None)
        sys.settrace(None)
        traceback.print_exc()
        emit("phase_result", phase=args.phase, outcome="CHANGES_REQUIRED" if import_pass else "BLOCKED",
             failed_stage=stage, error_type=type(exc).__name__, error=str(exc),
             import_status="IMPORT_RUNTIME_PASS" if import_pass else "NOT_PASSED",
             initializer_policy_status="INITIALIZER_POLICY_CELL_PASS" if init_policy_pass else "NOT_PASSED",
             hjb_status="RETURNED_BUT_CHECK_FAILED" if hjb_executed else "NOT_COMPLETED_OR_NOT_EXECUTED",
             counts=counts, KFE_GE_IRF=0, outer_steady_state_turns=0, empirical_data_reads=0)
        return 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", choices=("import-initial-policy", "tiny-hjb-one-iteration"), required=True)
    parser.add_argument("--source-root", type=Path, default=WORK / "src")
    raise SystemExit(run(parser.parse_args()))
