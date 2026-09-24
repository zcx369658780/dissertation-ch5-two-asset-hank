"""Static-only checks; never invoke execute_once or any model module."""
import importlib.util
import inspect
import io
import json
import sys
from types import SimpleNamespace
from contextlib import redirect_stdout
from pathlib import Path

import pytest
import numpy as np

sys.dont_write_bytecode = True
RUNNER = Path(__file__).resolve().parents[1] / "validators/multi_province/k1b_turn6_same_frozen_input_repeat/run.py"
spec = importlib.util.spec_from_file_location("turn6_repeat_static", RUNNER)
runner = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(runner)


def test_default_is_static_preflight(monkeypatch):
    monkeypatch.setattr(runner, "execute_once", lambda *_: (_ for _ in ()).throw(AssertionError("science called")))
    with redirect_stdout(io.StringIO()) as stream:
        assert runner.main([]) == 0
    assert "PASS__STATIC_PREFLIGHT_ONLY" in stream.getvalue()
    assert not (runner.REPOSITORY / runner.OUTPUT).exists()


def test_sealed_hash_rejection_before_science(monkeypatch):
    monkeypatch.setitem(runner.SEALED, "turn6_k1b_input_candidate.json", "0" * 64)
    with pytest.raises(runner.RepeatBlocked) as err:
        runner.preflight()
    assert err.value.terminal == "BLOCKED__SEALED_BUNDLE_HASH_MISMATCH"


def test_future_execution_gate_requires_fresh_task():
    with pytest.raises(runner.RepeatBlocked) as missing:
        runner.future_gate(runner.REPOSITORY, None)
    assert missing.value.terminal == "EXECUTION_AUTHORIZATION_REQUIRED"
    with pytest.raises(runner.RepeatBlocked) as stale:
        runner.future_gate(runner.REPOSITORY, "not-authorized")
    assert stale.value.terminal == "BLOCKED__FRESH_EXECUTION_TASK_GATE"


def test_budget_entry_counts_failure_and_denies_excess():
    guard = runner.BudgetGuard({"direct_hjb_updates": 1})
    guard.enter("direct_hjb_updates", 0)
    assert guard.attempted["direct_hjb_updates"] == 1
    with pytest.raises(runner.RepeatBlocked) as err:
        guard.enter("direct_hjb_updates", 0)
    assert err.value.terminal == "BLOCKED__ENTRY_BEFORE_CALL_BUDGET"
    assert guard.attempted["direct_hjb_updates"] == 1
    assert len(guard.denied) == 1


def test_comparison_arithmetic_on_sealed_values_only():
    sealed = runner.load_bundle(runner.REPOSITORY, 7)
    same = runner.compare_carrier(sealed, sealed)
    assert same["classification"] == "EXACT_BITWISE_MATCH"
    assert all(row["bitwise_mismatch_count"] == 0 for row in same["components"].values())
    changed = {**sealed, "rows": [dict(row) for row in sealed["rows"]]}
    changed["rows"][0]["state"] = dict(changed["rows"][0]["state"])
    changed["rows"][0]["state"]["rk"] += 1e-7
    observed = runner.compare_carrier(sealed, changed)
    assert observed["classification"] == "LEGAL_DIFFERENCE_OBSERVED"
    assert observed["components"]["rk"]["bitwise_mismatch_count"] == 1
    assert observed["components"]["rk"]["max_location"] == {"province_index": 0}
    assert observed["repeatability_threshold"] is None


def test_failed_attempt_ledger_reconciliation_is_not_zeroed():
    guard = runner.BudgetGuard()
    keys = ("source_native_initializations", "scalar_labor_roots_attempted",
            "scalar_labor_roots_returned", "corrected_policy_maps", "selector_evaluations",
            "scalar_selector_root_invocations", "d2_q_assemblies", "direct_hjb_updates",
            "hjb_checkpoint_evaluations_after_update", "scc_decompositions",
            "restricted_dense_scipy_linalg_svd_gesvd", "normalized_stationary_candidates",
            "q_transpose_times_p", "corrected_aggregate_evaluations")
    failed_local = {k: 0 for k in keys}
    failed_local.update(corrected_policy_maps=1, selector_evaluations=17,
                        scalar_selector_root_invocations=8)
    guard.reconcile(failed_local)
    assert guard.attempted["corrected_policy_maps"] == 1
    assert guard.attempted["selector_evaluations"] == 17
    assert guard.attempted["scalar_selector_root_invocations"] == 8


def test_early_failed_map_entry_survives_source_reconciliation():
    guard = runner.BudgetGuard()
    guard.enter("corrected_policy_maps", 0)
    keys = ("source_native_initializations", "scalar_labor_roots_attempted",
            "scalar_labor_roots_returned", "corrected_policy_maps", "selector_evaluations",
            "scalar_selector_root_invocations", "d2_q_assemblies", "direct_hjb_updates",
            "hjb_checkpoint_evaluations_after_update", "scc_decompositions",
            "restricted_dense_scipy_linalg_svd_gesvd", "normalized_stationary_candidates",
            "q_transpose_times_p", "corrected_aggregate_evaluations")
    guard.reconcile({k: 0 for k in keys})
    assert guard.attempted["corrected_policy_maps"] == 1


def test_future_task_binding_is_explicit_and_future_gate_stays_closed():
    source = inspect.getsource(runner._execute_after_gate)
    assert "bind_future_task(base)" in source
    assert "restore_task_binding(base,original_task)" in source
    assert "FUTURE_TASK_RELATIVE" in inspect.getsource(runner.source_snapshot)
    for failed in (False,True):
        base=SimpleNamespace(TASK_RELATIVE=Path("old-task.md"))
        previous=runner.bind_future_task(base)
        try:
            assert base.TASK_RELATIVE==runner.FUTURE_TASK_RELATIVE
            if failed:raise ValueError("stub failure")
        except ValueError:
            assert failed
        finally:
            runner.restore_task_binding(base,previous)
        assert base.TASK_RELATIVE==Path("old-task.md")
    output=runner.REPOSITORY/runner.OUTPUT
    assert not output.exists()
    with pytest.raises(runner.RepeatBlocked) as err:
        runner.future_gate(runner.REPOSITORY, "future-test")
    assert err.value.terminal == "BLOCKED__FRESH_EXECUTION_TASK_GATE"
    assert not output.exists()


def test_integration_entry_trace_blocks_second_stubbed_firm_before_call():
    def stub(ledger):
        ledger["firm_evaluations"] += 1
    lines,first=inspect.getsourcelines(stub)
    marker=next(first+i for i,line in enumerate(lines) if 'ledger["firm_evaluations"] += 1' in line)
    guard=runner.BudgetGuard({"firm_evaluations":1})
    trace=runner.make_entry_trace(stub.__code__,{marker:("firm_evaluations",)},guard)
    ledger={"firm_evaluations":0}
    previous=sys.gettrace()
    sys.settrace(trace)
    try:
        stub(ledger)
        with pytest.raises(runner.RepeatBlocked) as err:
            stub(ledger)
    finally:
        sys.settrace(previous)
    assert err.value.terminal == "BLOCKED__ENTRY_BEFORE_CALL_BUDGET"
    assert ledger["firm_evaluations"] == guard.attempted["firm_evaluations"] == 1


def test_all_31_kfe_paths_and_sealed_reference_binding(monkeypatch):
    names=runner.reference_intermediate_paths(runner.REPOSITORY)
    assert len([n for n in names if n.endswith("stationary_mass_arrays.npz")]) == 31
    assert len([n for n in names if n.endswith("stationarity_normalization_nonnegativity_receipt.json")]) == 31
    assert len(runner.reference_intermediate_hashes(runner.REPOSITORY)) == 70
    monkeypatch.setattr(runner,"MANIFEST_SHA","0"*64)
    with pytest.raises(runner.RepeatBlocked) as err:
        runner.reference_intermediate_hashes(runner.REPOSITORY)
    assert err.value.terminal == "BLOCKED__SEALED_MANIFEST_HASH"


def test_array_comparison_reports_shape_nonfinite_and_integer_membership():
    x=np.array([1.0,2.0],dtype=np.float64)
    assert runner.compare_array(x,x.copy())["status"] == "EXACT_BITWISE_MATCH"
    assert runner.compare_array(x,np.array([1.0]))["reason"] == "shape_or_dtype"
    assert runner.compare_array(x,np.array([1.0,np.nan]))["reason"] == "nonfinite"
    a=np.array([1,2],dtype=np.int64)
    b=np.array([1,3],dtype=np.int64)
    assert runner.compare_array(a,b)["bitwise_mismatches"] == 1
    boundary=np.array([2**53],dtype=np.int64)
    changed=np.array([2**53+1],dtype=np.int64)
    assert runner.compare_array(boundary,changed)["max_absolute_difference"]==1
    assert runner.compare_array(boundary,boundary.copy())["max_absolute_difference"]==0
    json.dumps(runner.compare_array(boundary,changed),allow_nan=False)


def test_post_gate_pre_call_failure_receipt_is_exclusive_and_zero(tmp_path):
    output=tmp_path/"new_repeat_root"
    runner.record_pre_call_failure(output,runner.RepeatBlocked("BLOCKED__TEST_IDENTITY"),"stub-id")
    record=json.loads((output/"first_failure.json").read_text(encoding="utf-8"))
    assert record["terminal"]=="BLOCKED__TEST_IDENTITY"
    assert all(value==0 for value in record["literal_scientific_call_ledger"].values())
    with pytest.raises(FileExistsError):
        runner.record_pre_call_failure(output,runner.RepeatBlocked("SECOND"),"stub-id")
    assert json.loads((output/"first_failure.json").read_text(encoding="utf-8"))==record


def test_carrier_finite_inputs_with_overflowed_ratio_are_unavailable():
    sealed=runner.load_bundle(runner.REPOSITORY,7)
    old={**sealed,"rows":[dict(row) for row in sealed["rows"]]}
    new={**sealed,"rows":[dict(row) for row in sealed["rows"]]}
    old["rows"][0]["state"]={**old["rows"][0]["state"],"w":1e-300}
    new["rows"][0]["state"]={**new["rows"][0]["state"],"w":1e300}
    with np.errstate(over="ignore"):
        result=runner.compare_carrier(old,new)
    assert result["components"]["w"]["reason"]=="nonfinite_difference"


def test_all_integration_entry_categories_and_raw_guard_order():
    old=(runner.REPOSITORY/"validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py").read_text(encoding="utf-8")
    categories=("source_faithful_labor_reconstructions","frozen_k1b_quantity_allocations",
                "k1b_feedback_calls","c1_residual_govinv_constructions","firm_evaluations",
                "composite_wage_batches","monetary_assignments","fiscal_diagnostic_batches",
                "completed_raw_ra0_vectors","deterministic_next_k1b_preparations")
    for category in categories:
        assert old.count(f'ledger["{category}"] += 1')==1
    assert old.index('raw = np.asarray([firm.ra0 for firm in firms], dtype=np.float64)') < old.index('ledger["completed_raw_ra0_vectors"] += 1')
    markers=inspect.getsource(runner.integration_entry_lines)
    for category in categories:
        assert category in markers
    assert 'raw = np.asarray([firm.ra0 for firm in firms], dtype=np.float64)' in markers


def test_stubbed_trace_counts_each_integration_entry_and_all_firms():
    def inert_integration(ledger):
        ledger["source_faithful_labor_reconstructions"]+=1
        ledger["frozen_k1b_quantity_allocations"]+=1
        ledger["k1b_feedback_calls"]+=1
        ledger["c1_residual_govinv_constructions"]+=1
        for _ in range(31):
            ledger["firm_evaluations"]+=1
        ledger["composite_wage_batches"]+=1
        ledger["monetary_assignments"]+=1
        ledger["fiscal_diagnostic_batches"]+=1
        ledger["completed_raw_ra0_vectors"]+=1
        ledger["deterministic_next_k1b_preparations"]+=1
    categories={"source_faithful_labor_reconstructions","frozen_k1b_quantity_allocations",
                "k1b_feedback_calls","c1_residual_govinv_constructions","firm_evaluations",
                "composite_wage_batches","monetary_assignments","fiscal_diagnostic_batches",
                "completed_raw_ra0_vectors","deterministic_next_k1b_preparations"}
    source,first=inspect.getsourcelines(inert_integration)
    entry={}
    for i,line in enumerate(source):
        for category in categories:
            if f'ledger["{category}"]+=' in line:
                entry[first+i]=(category,)
    assert len(entry)==len(categories)
    guard=runner.BudgetGuard({k:(31 if k=="firm_evaluations" else 1) for k in categories})
    ledger={k:0 for k in categories}
    previous=sys.gettrace()
    sys.settrace(runner.make_entry_trace(inert_integration.__code__,entry,guard))
    try:
        inert_integration(ledger)
    finally:
        sys.settrace(previous)
    assert guard.attempted==ledger
    guard.reconcile_all(ledger)
    assert guard.attempted["firm_evaluations"]==31


def test_reconcile_all_preserves_failed_entry_and_rejects_over_budget():
    guard=runner.BudgetGuard({"firm_evaluations":1,"completed_raw_ra0_vectors":1})
    guard.enter("firm_evaluations")
    guard.reconcile_all({"firm_evaluations":0,"completed_raw_ra0_vectors":0})
    assert guard.attempted["firm_evaluations"]==1
    with pytest.raises(runner.RepeatBlocked) as err:
        guard.reconcile_all({"firm_evaluations":2})
    assert err.value.terminal=="BLOCKED__CONSUMED_CALL_BUDGET"
    assert guard.attempted["firm_evaluations"]==1


def test_json_structure_orientation_and_province_identity_are_required(tmp_path):
    old=runner.REPOSITORY/runner.OLD_ROOT/"turn6/source_faithful_labor_receipt.json"
    doc=json.loads(old.read_text(encoding="utf-8"))
    new=tmp_path/old.name
    doc["orientation"]="origin_by_destination"
    new.write_text(json.dumps(doc),encoding="utf-8")
    result=runner.compare_receipt(old,new)
    assert result["status"]=="UNAVAILABLE" and result["field"]=="orientation"
    doc=json.loads(old.read_text(encoding="utf-8"))
    doc["lt_matrix_sha256"]="0"*64 if doc["lt_matrix_sha256"]!="0"*64 else "1"*64
    new.write_text(json.dumps(doc),encoding="utf-8")
    result=runner.compare_receipt(old,new)
    assert result["status"]!="EXACT_BITWISE_MATCH"
    assert result["field"]=="lt_matrix_sha256"
    old=runner.REPOSITORY/runner.OLD_ROOT/"turn6/household_batch_receipt.json"
    doc=json.loads(old.read_text(encoding="utf-8"))
    new=tmp_path/old.name
    doc["rows"][0]["province"]="wrong"
    new.write_text(json.dumps(doc),encoding="utf-8")
    assert runner.compare_receipt(old,new)["reason"]=="province_order"


def test_full_sealed_comparison_strictly_serializes_and_overflow_is_unavailable():
    hashes=runner.reference_intermediate_hashes(runner.REPOSITORY)
    compared=runner.compare_intermediates(runner.REPOSITORY,runner.REPOSITORY/runner.OLD_ROOT,hashes)
    assert len(compared)==70 and all(v["status"]=="EXACT_BITWISE_MATCH" for v in compared.values())
    json.dumps(compared,allow_nan=False)
    with np.errstate(over="ignore"):
        result=runner.compare_array(np.array([1e308]),np.array([-1e308]))
    assert result["reason"]=="nonfinite_difference"
    json.dumps(result,allow_nan=False)


def test_stubbed_post_gate_failure_captures_zero_and_restores_state(tmp_path):
    before_path=list(sys.path)
    before_trace=sys.gettrace()
    def inert_failure(runtime):
        sys.path.insert(0,"stub-path")
        runner.claim_output_root(tmp_path/runner.OUTPUT,runtime)
        (tmp_path/runner.OUTPUT/"preflight.json").write_text("partial",encoding="utf-8")
        raise runner.RepeatBlocked("BLOCKED__STUB_PREFLIGHT_WRITE")
    with pytest.raises(runner.RepeatBlocked):
        runner.run_after_valid_gate(tmp_path,"stub-id",inert_failure)
    receipt=json.loads((tmp_path/runner.OUTPUT/"first_failure.json").read_text(encoding="utf-8"))
    assert receipt["terminal"]=="BLOCKED__STUB_PREFLIGHT_WRITE"
    assert all(v==0 for v in receipt["literal_scientific_call_ledger"].values())
    assert sys.path==before_path and sys.gettrace() is before_trace
    with pytest.raises(runner.RepeatBlocked) as err:
        runner.run_after_valid_gate(tmp_path,"stub-id",lambda runtime:"unexpected")
    assert err.value.terminal=="BLOCKED__FUTURE_EVIDENCE_PATH_EXISTS"


def test_pre_call_identity_failure_claims_new_root_exclusively(tmp_path):
    with pytest.raises(runner.RepeatBlocked):
        runner.run_after_valid_gate(tmp_path,"stub-id",
            lambda runtime: (_ for _ in ()).throw(runner.RepeatBlocked("BLOCKED__STUB_HASH")))
    receipt=json.loads((tmp_path/runner.OUTPUT/"first_failure.json").read_text(encoding="utf-8"))
    assert receipt["terminal"]=="BLOCKED__STUB_HASH"
    assert all(v==0 for v in receipt["literal_scientific_call_ledger"].values())


def test_foreign_root_race_does_not_write_failure_receipt(tmp_path):
    output=tmp_path/runner.OUTPUT
    def foreign_wins(runtime):
        output.mkdir(parents=True,exist_ok=False)
        (output/"foreign.txt").write_text("keep",encoding="utf-8")
        raise FileExistsError("stubbed competing creator")
    with pytest.raises(runner.RepeatBlocked) as err:
        runner.run_after_valid_gate(tmp_path,"stub-id",foreign_wins)
    assert err.value.terminal=="BLOCKED__FUTURE_EVIDENCE_ROOT_NOT_OWNED"
    assert (output/"foreign.txt").read_text(encoding="utf-8")=="keep"
    assert not (output/"first_failure.json").exists()


def test_owned_root_failure_retains_stubbed_attempted_call(tmp_path):
    def inert_attempt(runtime):
        runner.claim_output_root(tmp_path/runner.OUTPUT,runtime)
        guard=runner.BudgetGuard()
        guard.enter("firm_evaluations")
        runtime["guard"]=guard
        runtime["ledger"]={"firm_evaluations":0}
        runtime["scientific_started"]=True
        raise runner.RepeatBlocked("FAIL__STUB_AFTER_ENTRY")
    with pytest.raises(runner.RepeatBlocked):
        runner.run_after_valid_gate(tmp_path,"stub-id",inert_attempt)
    receipt=json.loads((tmp_path/runner.OUTPUT/"first_failure.json").read_text(encoding="utf-8"))
    assert receipt["original_terminal"]=="FAIL__STUB_AFTER_ENTRY"
    assert receipt["literal_scientific_call_ledger"]["firm_evaluations"]==1
    assert receipt["source_ledger"]["firm_evaluations"]==0
