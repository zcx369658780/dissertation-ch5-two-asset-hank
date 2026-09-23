"""Static-only checks; never invoke execute_once or any model module."""
import importlib.util
import inspect
import io
import json
import sys
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
    source = RUNNER.read_text(encoding="utf-8")
    assert "base.TASK_RELATIVE=FUTURE_TASK_RELATIVE" in source
    assert "base.TASK_RELATIVE=original_task" in source
    assert "FUTURE_TASK_RELATIVE" in inspect.getsource(runner.source_snapshot)
    with pytest.raises(runner.RepeatBlocked) as err:
        runner.future_gate(runner.REPOSITORY, "future-test")
    assert err.value.terminal == "BLOCKED__FRESH_EXECUTION_TASK_GATE"


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
