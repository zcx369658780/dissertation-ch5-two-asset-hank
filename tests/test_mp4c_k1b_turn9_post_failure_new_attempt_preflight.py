"""Inert checks for the post-failure C9 candidate; no model entrypoint is called."""

import ast
import importlib.util
import json
import stat
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
WRAPPER = ROOT / "validators/multi_province/k1b_turn9_post_failure_new_attempt_timed/run.py"
DELEGATE = ROOT / "validators/multi_province/k1b_turn9_post_failure_new_attempt_outer_r2/run.py"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def modules():
    before = {name for name in sys.modules if name.startswith("ch5_two_asset_hank")}
    wrapper = _load("new_c9_wrapper_inert", WRAPPER)
    delegate = _load("new_c9_delegate_inert", DELEGATE)
    after = {name for name in sys.modules if name.startswith("ch5_two_asset_hank")}
    assert after == before
    return wrapper, delegate


def test_candidate_import_and_static_preflight_stay_blocked(modules):
    wrapper, delegate = modules
    result = wrapper.static_preflight(ROOT)
    assert result["status"] == "BLOCKED__NEW_LIVE_AUTHORITY_ABSENT__PREPARATION_ONLY"
    assert all(result["checks"].values())
    assert result["new_execution_id"] == "C9_POST_FAILURE_NEW_ATTEMPT_001"
    assert result["old_actual_ledger"] == "CALL_LEDGER_UNRESOLVED"
    assert result["scientific_calls"] == result["c9_attempts"] == result["c10_attempts"] == 0
    budget = delegate.budget_binding(ROOT)
    assert budget["adopted"] is False  # Later Owner adoption is separately hashed.
    assert delegate.CEILINGS == budget["proposed_c9_per_category_attempt_ceiling"]
    assert delegate.PER_PROVINCE == budget["proposed_c9_per_province_attempt_ceiling"]
    assert delegate.TWO_TURN_CEILINGS == budget["proposed_c9_plus_future_c10_cumulative_ceiling"]
    assert delegate.PROJECT_LIFETIME_GOVERNANCE == budget[
        "full_old_turn_charge_project_lifetime_governance_ceiling_if_new_grant_adopted_not_calls"]
    assert not (ROOT / wrapper.OUTPUT).exists()


def test_old_id_and_absent_future_authority_fail_at_read_only_gate(modules):
    wrapper, delegate = modules
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__NEW_C9_EXECUTION_ID"):
        wrapper.future_gate(ROOT, "C9_TIMED_RISK_RUN001", delegate)
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__NEW_LIVE_CONTRACT_ABSENT"):
        wrapper.future_gate(ROOT, wrapper.NEW_EXECUTION_ID, delegate)
    with pytest.raises(delegate.RepeatBlocked, match="BLOCKED__NEW_C9_EXECUTION_ID"):
        delegate.future_gate(ROOT, "C9_TIMED_RISK_RUN001")
    with pytest.raises(delegate.RepeatBlocked, match="BLOCKED__NEW_LIVE_CONTRACT_ABSENT"):
        delegate.future_gate(ROOT, delegate.NEW_EXECUTION_ID)
    for path in (wrapper.CONTRACT, wrapper.OWNER_ADOPTION, wrapper.TASK_COPY,
                 wrapper.INDEPENDENT_REVIEW, wrapper.OUTPUT):
        assert not (ROOT / path).exists()


def test_attempt_guards_and_old_charge_are_separate(modules):
    _, delegate = modules
    guard = delegate.BudgetGuard()
    assert guard.old_governance == delegate.CEILINGS
    assert guard.lifetime_governance == delegate.PROJECT_LIFETIME_GOVERNANCE
    guard.enter("turn9_household_calls")
    assert guard.attempted["turn9_household_calls"] == 1
    assert guard.old_governance["turn9_household_calls"] + 1 <= guard.lifetime_governance[
        "turn9_household_calls"]
    with pytest.raises(delegate.RepeatBlocked, match="BLOCKED__ENTRY_BEFORE_CALL_BUDGET"):
        guard.enter("turn9_household_calls")
    guard.enter("terminal_kfe_attempts", 0)
    with pytest.raises(delegate.RepeatBlocked, match="BLOCKED__PROVINCE_BUDGET"):
        guard.enter("terminal_kfe_attempts", 0)
    with pytest.raises(delegate.RepeatBlocked, match="BLOCKED__ENTRY_BEFORE_CALL_BUDGET"):
        guard.enter("scientific_retries")
    assert guard.attempted["scientific_retries"] == 0


def test_cooperative_wall_is_checked_at_entry_only(modules):
    wrapper, _ = modules
    deadline = 36_000 * 1_000_000_000
    assert wrapper.cooperative_wall_expired(deadline - 1, deadline) is False
    assert wrapper.cooperative_wall_expired(deadline, deadline) is True
    assert wrapper.cooperative_wall_expired(deadline + 1, deadline) is True


def test_first_failure_retains_unresolved_old_ledger_and_zero_retry(modules):
    _, delegate = modules
    guard = delegate.BudgetGuard()
    guard.enter("turn9_household_calls")
    runtime = {"state": {"ledger_unresolved": True}, "guard": guard,
               "scientific_started": True, "ledger": dict.fromkeys(delegate.CEILINGS, 0)}
    detail = delegate.failure_detail(runtime, "TypeError", delegate.NEW_EXECUTION_ID)
    assert detail["terminal"] == "CALL_LEDGER_UNRESOLVED"
    assert detail["retry_allowed"] is False
    assert detail["old_actual_ledger"] == "CALL_LEDGER_UNRESOLVED"
    assert detail["old_governance_charge_not_calls"] == delegate.CEILINGS


def test_measured_guard_reconcile_signature_and_forwarding_are_inert():
    tree = ast.parse(WRAPPER.read_text(encoding="utf-8"))
    classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)
               and node.name == "MeasuredGuard"]
    assert len(classes) == 1
    methods = [node for node in classes[0].body if isinstance(node, ast.FunctionDef)
               and node.name == "reconcile"]
    assert len(methods) == 1
    method = methods[0]
    assert [arg.arg for arg in method.args.args] == ["self", "ledger", "province"]
    assert isinstance(method.args.defaults[-1], ast.Constant) and method.args.defaults[-1].value is None
    calls = [node for node in ast.walk(method) if isinstance(node, ast.Call)
             and isinstance(node.func, ast.Attribute) and node.func.attr == "reconcile"]
    assert len(calls) == 1
    assert [arg.id for arg in calls[0].args] == ["ledger", "province"]


def test_default_cli_is_inert_and_root_absent(modules, capsys):
    wrapper, _ = modules
    assert wrapper.main(["--repository", str(ROOT)]) == 0
    result = json.loads(capsys.readouterr().out)
    assert result["status"] == "BLOCKED__NEW_LIVE_AUTHORITY_ABSENT__PREPARATION_ONLY"
    assert not (ROOT / wrapper.OUTPUT).exists()


def test_all_five_protected_manifests_have_exact_read_only_identity(modules, monkeypatch):
    wrapper, delegate = modules
    assert wrapper.PROTECTED_MANIFESTS == delegate.PROTECTED_MANIFESTS
    assert len(wrapper.PROTECTED_MANIFESTS) == 5
    for module in modules:
        assert all(module.protected_manifest_checks(ROOT).values())
        target = next(iter(module.PROTECTED_MANIFESTS))
        original_sha = module.sha
        monkeypatch.setattr(module, "sha", lambda path, target=target, original=original_sha:
                            "0" * 64 if path == ROOT / target else original(path))
        assert module.protected_manifest_checks(ROOT)[target.as_posix()] is False
        monkeypatch.setattr(module, "sha", original_sha)


def test_reparse_component_and_missing_manifest_fail_closed(modules, monkeypatch):
    wrapper, delegate = modules
    target = ROOT / next(iter(wrapper.PROTECTED_MANIFESTS))
    component = target.parent
    original_lstat = Path.lstat
    def reparse_lstat(path):
        if path == component:
            original = original_lstat(path)
            class ReparseStat:
                st_mode = original.st_mode
                st_file_attributes = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
            return ReparseStat()
        return original_lstat(path)
    monkeypatch.setattr(Path, "lstat", reparse_lstat)
    for module in modules:
        assert not module.path_components_safe(target)
        assert module.protected_manifest_checks(ROOT)[target.relative_to(ROOT).as_posix()] is False
    monkeypatch.undo()
    monkeypatch.setattr(wrapper, "protected_manifest_checks", lambda repo: {"missing": False})
    with pytest.raises(wrapper.TimingBlocked, match="STATIC_IDENTITY"):
        wrapper.static_preflight(ROOT)
    with pytest.raises(wrapper.TimingBlocked, match="PROTECTED_MANIFEST"):
        wrapper.future_gate(ROOT, wrapper.NEW_EXECUTION_ID, delegate)
    monkeypatch.setattr(delegate, "protected_manifest_checks", lambda repo: {"missing": False})
    with pytest.raises(delegate.RepeatBlocked, match="PROTECTED_MANIFEST"):
        delegate.preflight(ROOT)
    with pytest.raises(delegate.RepeatBlocked, match="PROTECTED_MANIFEST"):
        delegate.future_gate(ROOT, delegate.NEW_EXECUTION_ID)
    assert not (ROOT / wrapper.OUTPUT).exists()


def test_future_execute_source_order_denies_missing_authority_before_loading():
    tree = ast.parse(WRAPPER.read_text(encoding="utf-8"))
    functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
    execute = functions["execute_once"]
    contract_check = next(node for node in ast.walk(execute) if isinstance(node, ast.Attribute)
                          and node.attr == "is_file")
    dispatch = next(node for node in ast.walk(execute) if isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Name) and node.func.id == "run_timed_action")
    assert contract_check.lineno < dispatch.lineno
    assert all(not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name)
               or node.func.id not in {"load_delegate", "claim_output_root"}
               for node in ast.walk(execute))
    assert (ROOT / "tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_CONTRACT.json").exists() is False


def _read_only_gates_block(module, delegate):
    if module is delegate:
        with pytest.raises(delegate.RepeatBlocked):
            delegate.preflight(ROOT)
        with pytest.raises(delegate.RepeatBlocked):
            delegate.future_gate(ROOT, delegate.NEW_EXECUTION_ID)
    else:
        with pytest.raises(module.TimingBlocked):
            module.static_preflight(ROOT)
        with pytest.raises(module.TimingBlocked):
            module.future_gate(ROOT, module.NEW_EXECUTION_ID, delegate)


def _mock_lstat_component(monkeypatch, component, missing=False):
    original = Path.lstat
    def substitute(path):
        if path == component:
            if missing:
                raise FileNotFoundError(str(path))
            identity = original(path)
            class ReparseStat:
                st_mode = identity.st_mode
                st_file_attributes = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
            return ReparseStat()
        return original(path)
    monkeypatch.setattr(Path, "lstat", substitute)


@pytest.mark.parametrize("index", range(5))
@pytest.mark.parametrize("fault", ["hash", "missing", "reparse"])
def test_every_protected_manifest_fault_blocks_both_runners(modules, monkeypatch, index, fault):
    wrapper, delegate = modules
    target = ROOT / list(wrapper.PROTECTED_MANIFESTS)[index]
    if fault == "hash":
        for module in modules:
            original = module.sha
            monkeypatch.setattr(module, "sha", lambda path, original=original:
                                "0" * 64 if path == target else original(path))
    else:
        _mock_lstat_component(monkeypatch, target if fault == "missing" else target.parent,
                              missing=fault == "missing")
    for module in modules:
        assert module.protected_manifest_checks(ROOT)[target.relative_to(ROOT).as_posix()] is False
        _read_only_gates_block(module, delegate)
    assert not (ROOT / wrapper.OUTPUT).exists()


@pytest.mark.parametrize("relative", [
    "reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn9_k1b_input_candidate.json",
    "reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn9_k1b_frozen_share_payoff_plan.npz",
    "reports/ch5_k1b_turn9_timed_risk_exception_run001/timing_failure.json",
])
@pytest.mark.parametrize("component_kind", ["leaf", "parent"])
def test_sealed_leaf_or_parent_reparse_denied_before_content_read(
        modules, monkeypatch, relative, component_kind):
    wrapper, delegate = modules
    target = ROOT / relative
    component = target if component_kind == "leaf" else target.parent
    _mock_lstat_component(monkeypatch, component)
    for module in modules:
        original = module.sha
        monkeypatch.setattr(module, "sha", lambda path, original=original:
                            (_ for _ in ()).throw(AssertionError("unsafe leaf was read"))
                            if path == target else original(path))
    for module in modules:
        assert module.sealed_evidence_checks(ROOT)[relative] is False
        _read_only_gates_block(module, delegate)
    assert not (ROOT / wrapper.OUTPUT).exists()


def test_new_output_parent_reparse_denied_without_root_creation(modules, monkeypatch):
    wrapper, delegate = modules
    _mock_lstat_component(monkeypatch, (ROOT / wrapper.OUTPUT).parent)
    for module in modules:
        assert not module.path_components_safe(ROOT / module.OUTPUT)
        _read_only_gates_block(module, delegate)
    assert not (ROOT / wrapper.OUTPUT).exists()
