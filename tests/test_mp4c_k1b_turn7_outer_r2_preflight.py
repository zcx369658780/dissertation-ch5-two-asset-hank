"""Static and inert-stub checks for the future turn7 R2 runner; no model import/call."""
import importlib.util
import inspect
import io
import json
import os
import stat
import sys
from contextlib import redirect_stdout
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

sys.dont_write_bytecode=True
RUNNER=Path(__file__).resolve().parents[1]/"validators/multi_province/k1b_turn7_outer_r2/run.py"
spec=importlib.util.spec_from_file_location("turn7_r2_static",RUNNER)
runner=importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(runner)


def turn8_clone(c6):
    rows=[]
    for row in c6["rows"]:
        new={**row,"state":dict(row["state"])}
        new["raw_ra0_turn7"]=row["raw_ra0_turn6"]
        rows.append(new)
    return {**c6,"rows":rows,"S":np.array(c6["S"],copy=True)}


def test_default_cli_is_static_and_binds_only_sealed_c6(monkeypatch):
    monkeypatch.setattr(runner,"execute_once",lambda *_: (_ for _ in ()).throw(AssertionError("science")))
    with redirect_stdout(io.StringIO()) as stream:
        assert runner.main([])==0
    result=json.loads(stream.getvalue())
    assert result["status"]=="PASS__STATIC_PREFLIGHT_ONLY"
    assert result["scientific_calls"]==0
    assert result["C6_entering"]["json"]==runner.SEALED["turn7_k1b_input_candidate.json"]
    assert "C5_entering" not in result
    assert all(result["checks"].values())
    assert not (runner.REPOSITORY/runner.OUTPUT).exists()


def test_future_task_gate_rejects_current_task_without_writing(monkeypatch):
    output=runner.REPOSITORY/runner.OUTPUT
    monkeypatch.setattr(runner,"_execute_after_gate",lambda *_: (_ for _ in ()).throw(AssertionError("science")))
    with pytest.raises(runner.RepeatBlocked) as err:
        runner.execute_once(runner.REPOSITORY,"inert-stub-id")
    assert err.value.terminal=="BLOCKED__FRESH_EXECUTION_TASK_GATE"
    assert not output.exists()
    assert "ch5_two_asset_hank.corrected_diagnostic.optionb_turn2_household_integration" not in sys.modules


def test_sealed_c6_identity_rejected_before_science(monkeypatch):
    monkeypatch.setitem(runner.SEALED,"turn7_k1b_input_candidate.json","0"*64)
    with pytest.raises(runner.RepeatBlocked) as err:runner.preflight()
    assert err.value.terminal=="BLOCKED__SEALED_BUNDLE_HASH_MISMATCH"
    assert not (runner.REPOSITORY/runner.OUTPUT).exists()


def test_owner_per_turn_ceilings_and_turn7_only_are_exact():
    expected={
        "source_native_initializations":31,"scalar_labor_roots_attempted":24800,
        "scalar_labor_roots_returned":24800,"corrected_policy_maps":1581,
        "d2_q_assemblies":1581,"selector_evaluations":1264800,
        "scalar_selector_root_invocations":620000000,"direct_hjb_updates":1550,
        "hjb_checkpoint_evaluations_after_update":1550,"relaxation_helper_invocations":1550,
        "alpha_candidates":82150,"terminal_kfe_attempts":31,"scc_decompositions":31,
        "restricted_dense_scipy_linalg_svd_gesvd":31,"normalized_stationary_candidates":31,
        "q_transpose_times_p":31,"corrected_aggregate_evaluations":31,
        "firm_evaluations":31,"household_batch_constructions":1,"full_integrations":1,
        "source_faithful_labor_reconstructions":1,"frozen_k1b_quantity_allocations":1,
        "k1b_feedback_calls":1,"c1_residual_govinv_constructions":1,
        "composite_wage_batches":1,"monetary_assignments":1,"fiscal_diagnostic_batches":1,
        "completed_raw_ra0_vectors":1,"deterministic_next_k1b_preparations":1,
        "raw_next_payoff_same_s_constructions":1,"turn7_household_calls":1,
        "turn8_household_calls":0,"full_space_800_dense_scipy_linalg_svd_gesvd":0,
        "scientific_retries":0,"solver_substitutions":0,"k2_calls":0,
        "ge_annual_shock_irf_welfare_results_calls":0,"matlab_scientific_calls":0,
    }
    assert runner.CEILINGS==expected
    assert runner.PER_PROVINCE=={
        "corrected_policy_maps":51,"selector_evaluations":40800,
        "scalar_selector_root_invocations":20000000,"direct_hjb_updates":50,
        "terminal_kfe_attempts":1}


def test_failed_attempt_and_province_budget_do_not_reset():
    guard=runner.BudgetGuard()
    guard.enter("turn7_household_calls")
    with pytest.raises(runner.RepeatBlocked):guard.enter("turn7_household_calls")
    assert guard.attempted["turn7_household_calls"]==1
    with pytest.raises(runner.RepeatBlocked):guard.enter("turn8_household_calls")
    assert guard.attempted["turn8_household_calls"]==0
    guard.enter("terminal_kfe_attempts",0)
    with pytest.raises(runner.RepeatBlocked):guard.enter("terminal_kfe_attempts",0)
    guard.enter("terminal_kfe_attempts",1)
    assert guard.per_province[0]["terminal_kfe_attempts"]==1
    assert guard.attempted["terminal_kfe_attempts"]==2
    guard.reserve({"scalar_selector_root_invocations":20000000},2)
    with pytest.raises(runner.RepeatBlocked):guard.reserve({"scalar_selector_root_invocations":20000001},2)


def test_source_reconciliation_preserves_guarded_failed_entry():
    guard=runner.BudgetGuard({"firm_evaluations":1})
    guard.enter("firm_evaluations")
    guard.reconcile_all({"firm_evaluations":0})
    assert guard.attempted["firm_evaluations"]==1
    with pytest.raises(runner.RepeatBlocked):guard.reconcile_all({"firm_evaluations":2})
    assert guard.attempted["firm_evaluations"]==1


def test_stubbed_integration_entry_trace_denies_second_firm():
    def inert(ledger):
        ledger["firm_evaluations"]+=1
    source,first=inspect.getsourcelines(inert)
    line=next(first+i for i,row in enumerate(source) if 'ledger["firm_evaluations"]+=' in row)
    guard=runner.BudgetGuard({"firm_evaluations":1})
    previous=sys.gettrace()
    sys.settrace(runner.make_entry_trace(inert.__code__,{line:("firm_evaluations",)},guard))
    ledger={"firm_evaluations":0}
    try:
        inert(ledger)
        with pytest.raises(runner.RepeatBlocked):inert(ledger)
    finally:sys.settrace(previous)
    assert ledger["firm_evaluations"]==guard.attempted["firm_evaluations"]==1


def test_c6_to_c7_same_stage_exact_pair_is_first_pass_only():
    c6=runner.load_bundle(runner.REPOSITORY,7)
    c7=turn8_clone(c6)
    result=runner.compare_carrier(c6,c7)
    assert len(result["components"])==9
    assert result["classification"]=="EXACT_BITWISE_MATCH"
    assert result["all_nine_strictly_below_level"] is True
    assert result["r2_confirmed"] is False
    assert runner.turn7_terminal(result)=="VALID__FIRST_OF_TWO_NINE_COMPONENT_PASSES__TURN8_NOT_RUN"
    assert runner.clipped_ra_upper_summary(c7)["new_criterion_disqualifier"] is False


def test_owner_formula_families_and_strict_boundary(monkeypatch):
    c6=runner.load_bundle(runner.REPOSITORY,7)
    c7=turn8_clone(c6)
    for bundle in (c6,c7):
        bundle["rows"][0]["state"]["Yt"]=2.0
        bundle["rows"][0]["state"]["Kt_prev"]=20.0
        bundle["rows"][0]["state"]["Kt0"]=10.0
        bundle["rows"][0]["state"]["rk"]=0.03
    c7["rows"][0]["state"].update(Yt=3.0,Kt_prev=25.0,rk=0.53)
    monkeypatch.setattr(runner,"STRICT_LEVEL",0.5)
    result=runner.compare_carrier(c6,c7)
    assert result["components"]["Yt"]["diagnostic_difference"]==0.5
    assert result["components"]["Kt_prev"]["diagnostic_difference"]==0.5
    assert result["components"]["rk"]["diagnostic_difference"]==0.5
    assert result["all_nine_strictly_below_level"] is False
    assert runner.turn7_terminal(result)=="VALID__NINE_COMPONENT_LEVEL_NOT_MET"


def test_adopted_one_e_minus_six_boundary_is_strict():
    c6=runner.load_bundle(runner.REPOSITORY,7)
    c7=turn8_clone(c6)
    for bundle in (c6,c7):bundle["rows"][0]["state"]["rk"]=0.0
    c7["rows"][0]["state"]["rk"]=1e-6
    result=runner.compare_carrier(c6,c7)
    assert result["components"]["rk"]["diagnostic_difference"]==1e-6
    assert result["components"]["rk"]["strictly_below_1e6"] is False
    assert result["all_nine_strictly_below_level"] is False


def test_invalid_comparison_fails_instead_of_zero():
    c6=runner.load_bundle(runner.REPOSITORY,7)
    c7=turn8_clone(c6)
    c6["rows"][0]["state"]["Yt"]=0.0
    result=runner.compare_carrier(c6,c7)
    assert result["components"]["Yt"]["reason"]=="zero_denominator"
    with pytest.raises(runner.RepeatBlocked) as err:runner.turn7_terminal(result)
    assert err.value.terminal=="FAIL__OUTER_COMPARISON_UNAVAILABLE"
    c7["S"]=np.ones((30,31))
    assert runner.compare_carrier(c6,c7)["components"]["S"]["reason"]=="shape"


def test_clipped_ra_is_report_only_and_matlab_predicate_distinct():
    c6=runner.load_bundle(runner.REPOSITORY,7)
    summary=runner.clipped_ra_upper_summary(c6)
    assert summary["upper_hit_count"]==31
    assert summary["new_criterion_disqualifier"] is False
    assert summary["original_matlab_predicate_passed"] is False


def test_reused_integration_entry_markers_cover_each_budgeted_stage():
    path=runner.REPOSITORY/"validators/multi_province/k1b_turn5_turn6_bounded_continuation/run.py"
    source=path.read_text(encoding="utf-8")
    categories=("source_faithful_labor_reconstructions","frozen_k1b_quantity_allocations",
        "k1b_feedback_calls","c1_residual_govinv_constructions","firm_evaluations",
        "composite_wage_batches","monetary_assignments","fiscal_diagnostic_batches",
        "completed_raw_ra0_vectors","deterministic_next_k1b_preparations")
    markers=inspect.getsource(runner.integration_entry_lines)
    for category in categories:
        assert source.count(f'ledger["{category}"] += 1')==1
        assert category in markers
    assert source.index('raw = np.asarray([firm.ra0 for firm in firms], dtype=np.float64)') < source.index('ledger["completed_raw_ra0_vectors"] += 1')
    assert 'raw = np.asarray([firm.ra0 for firm in firms], dtype=np.float64)' in markers
    assert 'ledger[f"turn{next_turn}_household_calls"] == 0' in source


@pytest.mark.parametrize("mutation",("mkdir","unlink"))
def test_lost_root_blocks_reused_path_mutation(tmp_path,mutation):
    output=tmp_path/"future_output"
    runtime={"output_identity":None}
    runner.claim_output_root(output,runtime)
    child=output/"turn7"/"household"
    if mutation=="unlink":
        child.mkdir(parents=True)
        (child/"cell_000.json").write_text("preserve",encoding="utf-8")
    output.rename(tmp_path/"moved_original")
    original_mkdir,original_unlink=runner.install_output_mutation_guards(output,runtime)
    try:
        with pytest.raises(runner.RepeatBlocked) as err:
            if mutation=="mkdir":child.mkdir(parents=True)
            else:(child/"cell_000.json").unlink()
        assert err.value.terminal=="BLOCKED__FUTURE_EVIDENCE_ROOT_NOT_OWNED"
    finally:Path.mkdir,Path.unlink=original_mkdir,original_unlink
    assert not output.exists()
    if mutation=="unlink":assert (tmp_path/"moved_original"/"turn7"/"household"/"cell_000.json").exists()


def test_same_inode_reparse_root_is_rejected(tmp_path,monkeypatch):
    if os.name!="nt":pytest.skip("Windows reparse attributes unavailable")
    output=tmp_path/"future_output"
    runtime={"output_identity":None}
    runner.claim_output_root(output,runtime)
    original_lstat=Path.lstat
    def marked(path,*args,**kwargs):
        identity=original_lstat(path,*args,**kwargs)
        if path==output:return SimpleNamespace(st_mode=stat.S_IFDIR,st_dev=identity.st_dev,
            st_ino=identity.st_ino,st_file_attributes=identity.st_file_attributes|stat.FILE_ATTRIBUTE_REPARSE_POINT)
        return identity
    monkeypatch.setattr(Path,"lstat",marked)
    assert not runner.owns_output_root(output,runtime)


def test_symlink_back_to_claimed_inode_is_rejected_if_supported(tmp_path):
    output=tmp_path/"future_output"
    runtime={"output_identity":None}
    runner.claim_output_root(output,runtime)
    moved=tmp_path/"moved_original"
    output.rename(moved)
    try:output.symlink_to(moved,target_is_directory=True)
    except (OSError,NotImplementedError) as exc:pytest.skip(f"directory symlink unavailable: {exc}")
    assert not runner.owns_output_root(output,runtime)
    with pytest.raises(runner.RepeatBlocked):runner.guard_output_mutation(output,runtime,output/"turn7")


def test_lost_root_failure_detail_preserves_first_terminal_and_ledgers(tmp_path):
    output=tmp_path/runner.OUTPUT
    def inert(runtime):
        runner.claim_output_root(output,runtime)
        guard=runner.BudgetGuard()
        guard.enter("turn7_household_calls")
        runtime.update(guard=guard,ledger={"turn7_household_calls":1},scientific_started=True,
            state={"original_terminal":"FAIL__EARLIEST","ledger_unresolved":True})
        output.rename(tmp_path/"moved_original")
        raise runner.RepeatBlocked("BLOCKED__LATER")
    with pytest.raises(runner.RepeatBlocked) as err:
        runner.run_after_valid_gate(tmp_path,"stub",inert)
    assert err.value.terminal=="BLOCKED__FUTURE_EVIDENCE_ROOT_NOT_OWNED"
    detail=err.value.detail
    assert detail["original_terminal"]=="FAIL__EARLIEST"
    assert detail["terminal"]=="CALL_LEDGER_UNRESOLVED"
    assert detail["literal_scientific_call_ledger"]["turn7_household_calls"]==1
    assert detail["source_ledger"]["turn7_household_calls"]==1
    assert detail["call_ledger_resolved"] is False
    assert not output.exists()


def test_owned_json_npz_writes_are_exclusive(tmp_path):
    output=tmp_path/"future_output"
    runtime={"output_identity":None}
    runner.claim_output_root(output,runtime)
    runner.write_output_json(output,runtime,output/"turn7"/"receipt.json",{"status":"PASS"})
    with pytest.raises(runner.RepeatBlocked):
        runner.write_output_json(output,runtime,output/"turn7"/"receipt.json",{"status":"SECOND"})
    assert json.loads((output/"turn7"/"receipt.json").read_text(encoding="utf-8"))["status"]=="PASS"
    path=output/"turn7"/"arrays.npz"
    runner.write_output_npz(output,runtime,path,np.savez_compressed,a=np.array([1.0]))
    with pytest.raises(runner.RepeatBlocked):
        runner.write_output_npz(output,runtime,path,np.savez_compressed,a=np.array([2.0]))
    with np.load(path,allow_pickle=False) as z:assert z["a"].tolist()==[1.0]
