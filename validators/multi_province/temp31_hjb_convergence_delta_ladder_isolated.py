"""Real fixed HJB; read-only profile/trace observations and stale-policy audit."""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import traceback
import warnings

TASK="CH5_TEMP31_HJB_TINYGRID_CONVERGENCE_NUMERICAL_DELTA_LADDER_R1_20261029"
SRC="ffdb7fcd41019bed7ce4652ee01c753bff6fcec8"
WORK=Path(__file__).resolve().parents[2]
REPORT=WORK/"tasks"/TASK
THREAD_KEYS=("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS","VECLIB_MAXIMUM_THREADS","BLIS_NUM_THREADS")

def emit(event,**values):
    print(json.dumps(dict(event=event,**values),allow_nan=False),flush=True)

def authenticated_helper(row,name):
    path=WORK/row["path"];raw=path.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==row["sha256"] and len(raw)==row["bytes"]
    assert hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()==row["git_blob"]
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
    return module

def run(args):
    counts={k:0 for k in ("initializer_batches","root_cells","brentq_calls","hjb_driver_calls","hjb_iteration_entries","hjb_policy_cells","operator_assemblies","linear_solves")}
    stage="HANDSHAKE";trajectory=[];last={};root_wages=[];active_hjb=0
    try:
        assert sys.stdin.readline().strip()=="GO","supervisor handshake required"
        assert all(os.environ.get(k)=="1" for k in THREAD_KEYS)
        stage="SOURCE_AUTHENTICATION"
        identity=json.loads((REPORT/"source_identity.json").read_text(encoding="utf-8"))
        tuning=json.loads((REPORT/"numerical_tuning_contract.json").read_text(encoding="utf-8"))
        assert identity["source"]["commit"]==SRC
        arm=tuning["arms"][args.arm];assert arm=={"delta":{"A":1000.0,"B":100.0,"C":10.0}[args.arm],"max_iterations":80}
        frozen=tuning["frozen_parameters"];source_root=args.source_root.absolute();expected={}
        for row in identity["scientific_source_files"]:
            relative=row["path"].removeprefix("src/");path=source_root/relative
            current=path
            while current!=source_root.parent:
                s=os.lstat(current);assert not(getattr(s,"st_file_attributes",0)&0x400) and not current.is_symlink()
                current=current.parent
            raw=path.read_bytes()
            assert len(raw)==row["bytes"] and hashlib.sha256(raw).hexdigest()==row["sha256"]
            assert hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()==row["git_blob"]
            expected[relative[:-3].replace("/",".")]=(path,row)
        loader=authenticated_helper(identity["authenticated_previous_helpers"][0],"temp31_previous_fixed_namespace_loader")
        loader.namespace("ch5_two_asset_hank",source_root/"ch5_two_asset_hank")
        loader.namespace("ch5_two_asset_hank.multi_province",source_root/"ch5_two_asset_hank/multi_province")
        stage="IMPORT_RUNTIME"
        modules={name:importlib.import_module(name) for name in expected}
        loaded={name for name in sys.modules if name.startswith("ch5_two_asset_hank.")}
        assert loaded==set(expected)|{"ch5_two_asset_hank.multi_province"}
        origins=[]
        for name,(path,row) in expected.items():
            module=modules[name]
            assert Path(module.__file__).absolute()==path and isinstance(module.__loader__,importlib.machinery.SourceFileLoader)
            origins.append({"module":name,"file":module.__file__,"git_blob":row["git_blob"],"bytes":row["bytes"],"sha256":row["sha256"]})
        import numpy as np
        import scipy
        from scipy.sparse.linalg import MatrixRankWarning
        short={name.rsplit(".",1)[-1]:module for name,module in modules.items()}
        bootstrap=short["temp31_ha_taxfree_bootstrap"];hjb=short["temp31_netwage_hjb"]
        policy=short["temp31_netwage_policy"];operator=short["matlab_faithful_operator"]
        contracts=short["contracts"]
        pools=[];native="UNAVAILABLE_ENVIRONMENT_LIMITS_ONLY"
        if importlib.util.find_spec("threadpoolctl") is not None:
            from threadpoolctl import threadpool_info
            pools=[{k:r.get(k) for k in ("user_api","internal_api","num_threads","prefix")} for r in threadpool_info()]
            assert all(r["num_threads"]==1 for r in pools if r["user_api"] in ("blas","openmp"))
            native="AVAILABLE"
        emit("imports",arm=args.arm,source_commit=SRC,modules=origins,python=sys.version.split()[0],numpy=np.__version__,scipy=scipy.__version__,
             skipped_package_initializers=identity["skipped_package_initializers"],BLAS_environment={k:os.environ[k] for k in THREAD_KEYS},native_thread_measurement=native,thread_pools=pools)
        limits={"initializer_batches":1,"root_cells":8,"brentq_calls":8,"hjb_driver_calls":1,"hjb_iteration_entries":80,"hjb_policy_cells":640,"operator_assemblies":81,"linear_solves":80}
        targets={bootstrap.temp31_netwage_initial_arrays.__code__:"initializer_batches",bootstrap._temp31_source_labor_root.__code__:"root_cells",
                 bootstrap.brentq.__code__:"brentq_calls",hjb.solve_temp31_netwage_hjb.__code__:"hjb_driver_calls",
                 policy.select_temp31_netwage_local_policy.__code__:"hjb_policy_cells",operator.assemble_source_operator.__code__:"operator_assemblies",hjb.linalg.spsolve.__code__:"linear_solves"}
        def bump(name):
            counts[name]+=1;assert counts[name]<=limits[name],"CALL_BUDGET_EXCEEDED "+name
        def profile(frame,event,arg):
            nonlocal active_hjb
            name=targets.get(frame.f_code)
            if name is None:return
            if event=="call":
                if name=="hjb_policy_cells":assert active_hjb==1,"extra policy outside HJB prohibited"
                bump(name)
                if name=="hjb_driver_calls":active_hjb+=1
                if name=="root_cells":root_wages.append(float(frame.f_locals["wage"]))
            elif event=="return" and name=="hjb_driver_calls":active_hjb-=1
        source_ast=ast.parse(Path(hjb.__file__).read_bytes().decode("utf-8"))
        function=next(n for n in source_ast.body if isinstance(n,ast.FunctionDef) and n.name=="solve_temp31_netwage_hjb")
        loop=next(n for n in function.body if isinstance(n,ast.For) and isinstance(n.target,ast.Name) and n.target.id=="iteration")
        entry_line=loop.body[0].lineno
        check_line=next(n.lineno for n in loop.body if isinstance(n,ast.If) and isinstance(n.test,ast.Compare) and isinstance(n.test.left,ast.Name) and n.test.left.id=="statistic")
        def norm(x):return float(np.max(np.abs(x))) if np.size(x) else 0.0
        def inspect_iteration(frame):
            loc=frame.f_locals;v=loc["value"];old=loc["old"];update=(v-old).ravel(order="F")
            statistic=float(loc["statistic"]);assert np.isfinite(statistic) and np.isfinite(v).all(),"NONFINITE_ITERATION"
            assert all(np.isfinite(loc["arrays"][name]).all() for name in ("consumption","labor","mu_a","mu_b","utility")),"NONFINITE_POLICY"
            assert np.isfinite(loc["operator"].full.data).all() and np.isfinite(loc["matrix"].data).all(),"NONFINITE_OPERATOR"
            assert statistic==norm(update),"source iteration statistic disagreement"
            prev=last.get("update");cosine=None
            if prev is not None and norm(prev)>0 and norm(update)>0:
                scaled=update/norm(update);previous=prev/norm(prev)
                cosine=float(np.dot(scaled,previous)/(np.linalg.norm(scaled)*np.linalg.norm(previous)))
            ratio=statistic/trajectory[-1]["value_change_sup"] if trajectory and trajectory[-1]["value_change_sup"]>0 else None
            row={"iteration":int(loc["iteration"]),"value_change_sup":statistic,"value_abs_max":norm(v),
                 "value_min":float(v.min()),"value_max":float(v.max()),"finite":True,"growth_ratio":ratio,"successive_update_cosine":cosine}
            trajectory.append(row)
            last.update(old=old.copy(),value=v.copy(),utility=loc["arrays"]["utility"].copy(),G=loc["operator"].full.copy(),
                        matrix=loc["matrix"].copy(),rhs=loc["rhs"].copy(),update=update.copy())
            emit("iteration",arm=args.arm,**row,observed_counts=dict(counts))
        def trace_hjb(frame,event,arg):
            if event=="line":
                if frame.f_lineno==entry_line:
                    bump("hjb_iteration_entries")
                    emit("iteration_entry",arm=args.arm,iteration=int(frame.f_locals["iteration"]),observed_counts=dict(counts))
                elif frame.f_lineno==check_line:inspect_iteration(frame)
            return trace_hjb
        def trace_calls(frame,event,arg):return trace_hjb if frame.f_code is hjb.solve_temp31_netwage_hjb.__code__ else None
        sys.setprofile(profile);sys.settrace(trace_calls)
        stage="FROZEN_INPUTS"
        params=contracts.EconomicParams(**frozen["EconomicParams"])
        record=bootstrap.numerical_bootstrap19(context_id=frozen["context_id"],province_order=tuple(frozen["province_order"]),
            tax_by_destination=frozen["tax_by_destination"],sigma_destination_origin=frozen["sigma_destination_origin"],w_initial=20.0,tau_legacy_reference=0.05)
        inputs=bootstrap.netwage_inputs(record,origin_index=0,r_a=.09,r_b=.02,expected_context_id=frozen["context_id"],expected_province_order=("A","B"))
        assert inputs.wages.tolist()==[19.0] and inputs.labor_weights.tolist()==[1.0] and record.tax_by_destination==(.05,.05)
        assert record.sigma_destination_origin==((0.0,0.0),(0.0,0.0)) and record.entering_iteration==1
        grid=hjb.Temp31NetWageHJBGrid(**{k:np.array(v,dtype=float) for k,v in frozen["grid"].items()})
        assert (grid.b.size,grid.a.size,grid.z.size)==(2,2,2)
        stage="INITIALIZER"
        value,labor=bootstrap.temp31_netwage_initial_arrays({"rah":.09,"rb":.02,"rb_gap":.07,"Tt":.1},grid,params,inputs)
        assert value.shape==labor.shape==(2,2,2) and np.isfinite(value).all() and np.isfinite(labor).all()
        assert counts["root_cells"]==8 and set(root_wages)=={19.0*.8,19.0*1.3}
        initial_hashes={"value_F_float64_sha256":hashlib.sha256(value.astype("<f8").tobytes(order="F")).hexdigest(),
                        "labor_F_float64_sha256":hashlib.sha256(labor.astype("<f8").tobytes(order="F")).hexdigest()}
        emit("initialization",arm=args.arm,shape=[2,2,2],effective_wage=19.0,original_initialization_hashes=initial_hashes,observed_counts=dict(counts))
        numerics=hjb.Temp31NetWageHJBNumerics(delta=arm["delta"],max_iterations=80,convergence_tolerance=1e-7,drift_tolerance=1e-12)
        stage="REAL_HJB_DRIVER"
        with warnings.catch_warnings(record=True) as warning_records:
            warnings.simplefilter("always")
            result=hjb.solve_temp31_netwage_hjb(grid,params,inputs,value,labor,.1,.07,numerics)
        sys.setprofile(None);sys.settrace(None)
        warning_summary=[{"type":type(w.message).__name__,"message":str(w.message)} for w in warning_records]
        assert not any(isinstance(w.message,MatrixRankWarning) for w in warning_records),"linear solve rank warning"
        stage="RETURN_AND_IMPLICIT_AUDIT"
        assert counts["hjb_driver_calls"]==1 and result.iterations==counts["hjb_iteration_entries"]==len(trajectory)
        assert 1<=result.iterations<=80 and counts["hjb_policy_cells"]==8*result.iterations and counts["linear_solves"]==result.iterations
        assert counts["operator_assemblies"]==result.iterations+1 and counts["initializer_batches"]==1
        assert np.array_equal(result.initial_value,value),"initial value mutated or warm-started"
        relevant=("value","initial_value","consumption","labor","transfer","adjustment_cost","effective_illiquid_return","mu_a","mu_b","utility")
        finite={name:bool(np.isfinite(getattr(result,name)).all()) for name in relevant}
        G=result.operator.full
        assert G.shape==(8,8) and np.isfinite(G.data).all() and np.isfinite(result.post_convergence_operator.full.data).all() and all(finite.values())
        assert norm((G-last["G"]).toarray())==0 and np.array_equal(result.utility,last["utility"])
        assert result.convergence_statistic==trajectory[-1]["value_change_sup"]
        v_new=result.value.ravel(order="F");v_old=last["old"].ravel(order="F");u=result.utility.ravel(order="F")
        Gv=G@v_new;residual=params.rho*v_new-u-Gv;implicit=(v_old-v_new)/arm["delta"]
        stale_norm=norm(residual);implicit_norm=norm(implicit)
        rounding_bound=1e-10*(1+max(norm(u),norm(params.rho*v_new),norm(Gv),implicit_norm))
        expected_matrix=(1/arm["delta"]+params.rho)*np.eye(8)-G.toarray()
        checks={"stale_policy_residual_sup":stale_norm,"last_step_change_over_delta":implicit_norm,
          "residual_vector_implicit_identity_error_sup":norm(residual-implicit),
          "stale_norm_step_norm_difference":abs(stale_norm-implicit_norm),
          "captured_linear_equation_residual_sup":norm(last["matrix"]@v_new-last["rhs"]),
          "captured_matrix_vs_expected_error_sup":norm(last["matrix"].toarray()-expected_matrix),
          "captured_rhs_vs_expected_error_sup":norm(last["rhs"]-(u+v_old/arm["delta"])),
          "frozen_rounding_bound":rounding_bound,"full_nonlinear_Bellman_optimality_residual":"NOT_EVALUATED_NO_POLICY_REOPTIMIZATION"}
        algebra_keys=("residual_vector_implicit_identity_error_sup","stale_norm_step_norm_difference","captured_linear_equation_residual_sup","captured_matrix_vs_expected_error_sup","captured_rhs_vs_expected_error_sup")
        consistent=all(np.isfinite(checks[k]) and checks[k]<=rounding_bound for k in algebra_keys)
        dense=G.toarray();offdiag=dense[~np.eye(8,dtype=bool)];rows=np.asarray(G.sum(axis=1)).ravel()
        operator_metrics={"shape":[8,8],"nnz":int(G.nnz),"density":float(G.nnz/64),
          "max_row_sum":float(rows.max()),"row_sum_abs_max":norm(rows),"min_offdiagonal_including_implicit_zeros":float(offdiag.min()),
          "finite":True,"returned_last_policy_operator_equals_captured_iteration_operator":True}
        risks=[]
        if norm(rows)>1e-12:risks.append("source operator row sums depart from zero; generator/scientific risk, no operator repair")
        if offdiag.min() < -1e-12:risks.append("source operator has negative offdiagonal; generator/scientific risk, no operator repair")
        if not consistent:
            outcome="INCONSISTENT_STOP"
        elif result.converged:
            outcome="PASS_BOUNDED_NUMERICAL_FIXED_POINT__STALE_POLICY_RESIDUAL_CHECKED" if result.convergence_statistic<1e-7 and stale_norm<=1e-7 else "INCONSISTENT_STOP"
        else:
            outcome="NOT_CONVERGED_FINITE" if result.iterations==80 else "INCONSISTENT_STOP"
        diagnostics={"arm":args.arm,"delta":arm["delta"],"max_iterations":80,"outcome":outcome,
          "result_converged":bool(result.converged),"actual_iterations":int(result.iterations),"last_value_change":float(result.convergence_statistic),
          "finite_return_arrays":finite,"operator":operator_metrics,"implicit_audit":checks,"implicit_consistent":consistent,
          "oscillation_growth":{"negative_successive_update_cosines":sum(r["successive_update_cosine"] is not None and r["successive_update_cosine"]<0 for r in trajectory),
            "growth_ratio_above_one_count":sum(r["growth_ratio"] is not None and r["growth_ratio"]>1 for r in trajectory),
            "max_growth_ratio":max((r["growth_ratio"] for r in trajectory if r["growth_ratio"] is not None),default=None),
            "interpretation":"observable update oscillation/growth indicators only; not a nonlinear optimality test"},
          "source_operator_scientific_risks":risks,"warnings":warning_summary,
          "original_initialization_hashes":initial_hashes,"observed_counts":counts,
          "source_commit":SRC,"Fortran_order":True,"KFE_GE_IRF":0,"outer_steady_state_turns":0,"empirical_data_reads":0}
        emit("arm_result",**diagnostics)
        return 0 if outcome in ("PASS_BOUNDED_NUMERICAL_FIXED_POINT__STALE_POLICY_RESIDUAL_CHECKED","NOT_CONVERGED_FINITE") else 1
    except BaseException as exc:
        sys.setprofile(None);sys.settrace(None);traceback.print_exc()
        emit("arm_result",arm=args.arm,outcome="STOP_EXCEPTION",failed_stage=stage,error_type=type(exc).__name__,error=str(exc),
             observed_counts=counts,completed_iteration_metrics=len(trajectory),KFE_GE_IRF=0,outer_steady_state_turns=0,empirical_data_reads=0)
        return 1

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arm",choices=("A","B","C"),required=True)
    parser.add_argument("--source-root",type=Path,default=WORK/"src")
    raise SystemExit(run(parser.parse_args()))
