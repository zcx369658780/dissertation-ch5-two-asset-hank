"""Inert checks for the post-failure C9 candidate; no model entrypoint is called."""

import ast
import importlib
import importlib.util
import json
import stat
import sys
from pathlib import Path
from types import SimpleNamespace

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
    authority_checks = [node for node in ast.walk(execute) if isinstance(node, ast.Call)
                        and isinstance(node.func, ast.Name)
                        and node.func.id == "authority_file_present"]
    dispatch = next(node for node in ast.walk(execute) if isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Name) and node.func.id == "run_timed_action")
    assert authority_checks and max(node.lineno for node in authority_checks) < dispatch.lineno
    assert all(not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name)
               or node.func.id not in {"load_delegate", "claim_output_root"}
               for node in ast.walk(execute))
    assert (ROOT / "tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_CONTRACT.json").exists() is False


def _call_name(node):
    if isinstance(node.func, ast.Name):
        return node.func.id
    if isinstance(node.func, ast.Attribute):
        return node.func.attr
    return None


def _assert_final_entry_guards_precede(function, downstream):
    checks = [node for node in function.body if isinstance(node, ast.If)]
    assert len(checks) >= 2
    sealed, output = checks[:2]
    sealed_calls = {_call_name(node) for node in ast.walk(sealed.test)
                    if isinstance(node, ast.Call)}
    output_calls = {_call_name(node) for node in ast.walk(output.test)
                    if isinstance(node, ast.Call)}
    assert {"sealed_evidence_checks", "protected_manifest_checks"} <= sealed_calls
    assert {"lexists", "path_components_safe"} <= output_calls
    calls = [node for node in ast.walk(function) if isinstance(node, ast.Call)]
    for name in downstream:
        lines = [node.lineno for node in calls if _call_name(node) == name]
        assert lines, f"{function.name}: missing {name}"
        assert output.lineno < min(lines), f"{function.name}: {name} precedes output gate"
    assert sealed.lineno < output.lineno
    for name in ("claim_output_root", "mkdir", "makedirs"):
        assert all(output.lineno < node.lineno for node in calls if _call_name(node) == name)


def test_final_committed_load_delegate_guards_precede_contract_and_exec():
    tree = ast.parse(WRAPPER.read_bytes(), filename=str(WRAPPER))
    function = next(node for node in tree.body if isinstance(node, ast.FunctionDef)
                    and node.name == "load_delegate")
    _assert_final_entry_guards_precede(
        function, {"committed_file", "spec_from_file_location", "exec"})


def test_final_committed_run_timed_action_guards_precede_dispatch_and_clock():
    tree = ast.parse(WRAPPER.read_bytes(), filename=str(WRAPPER))
    function = next(node for node in tree.body if isinstance(node, ast.FunctionDef)
                    and node.name == "run_timed_action")
    _assert_final_entry_guards_precede(
        function, {"load_delegate", "future_gate", "clock_sample"})


def _source_function(path, name):
    tree = ast.parse(path.read_bytes(), filename=str(path))
    return next(node for node in tree.body if isinstance(node, ast.FunctionDef)
                and node.name == name)


def _named_calls(function, name):
    return [node for node in ast.walk(function) if isinstance(node, ast.Call)
            and _call_name(node) == name]


def test_repair3_preflight_has_distinct_fail_closed_inactive_and_active_branches():
    function = _source_function(WRAPPER, "static_preflight")
    branch = next(node for node in ast.walk(function) if isinstance(node, ast.If)
                  and isinstance(node.test, ast.Name) and node.test.id == "require_inactive")
    inactive_source = "\n".join(ast.unparse(node) for node in branch.body)
    active_source = "\n".join(ast.unparse(node) for node in branch.orelse)
    for name in ("CONTRACT", "OWNER_ADOPTION", "TASK_COPY", "INDEPENDENT_REVIEW"):
        assert name in inactive_source
    assert inactive_source.count("authority_file_absent") == 4
    assert "preimport_authority_gate" in active_source
    assert "NEW_EXECUTION_ID" in active_source
    assert "preimport_authority_gate" not in inactive_source
    assert any(_call_name(node) == "preimport_authority_gate"
               for statement in branch.orelse for node in ast.walk(statement)
               if isinstance(node, ast.Call))
    assert "ACTIVE_AUTHORITY_STATIC_PREFLIGHT_ONLY__NO_SCIENCE" in ast.unparse(function)


def test_repair3_wrapper_checks_all_authorities_before_delegate_exec():
    loader = _source_function(WRAPPER, "load_delegate")
    _assert_final_entry_guards_precede(loader, {"preimport_authority_gate", "exec"})
    assert max(node.lineno for node in _named_calls(loader, "preimport_authority_gate")) < min(
        node.lineno for node in _named_calls(loader, "exec"))
    gate = _source_function(WRAPPER, "preimport_authority_gate")
    source = ast.unparse(gate)
    for name in ("CONTRACT", "TASK_COPY", "INDEPENDENT_REVIEW", "OWNER_ADOPTION",
                 "TIMED_RUNNER", "DELEGATE", "TASK_CURRENT.md"):
        assert name in source
    assert len(_named_calls(gate, "committed_file")) >= 7
    first_authority = min(node.lineno for node in _named_calls(gate, "committed_file"))
    for name in ("sealed_evidence_checks", "protected_manifest_checks",
                 "lexists", "path_components_safe"):
        assert min(node.lineno for node in _named_calls(gate, name)) < first_authority
    assert "NEW_C9_CONTRACT_IDENTITY" in source
    assert "NEW_C9_TASK_IDENTITY" in source
    assert "NEW_C9_INDEPENDENT_REVIEW_IDENTITY" in source
    assert "NEW_C9_OWNER_EXECUTION_ADOPTION" in source
    assert "exec(" not in source and "exec_module" not in source


def test_repair3_delegate_checks_all_authorities_before_wrapper_exec():
    direct = _source_function(DELEGATE, "assert_active_authority")
    preflight = _named_calls(direct, "preimport_wrapper_authority_gate")
    imports = _named_calls(direct, "exec_module")
    assert len(preflight) == len(imports) == 1
    assert preflight[0].lineno < imports[0].lineno
    gate = _source_function(DELEGATE, "preimport_wrapper_authority_gate")
    source = ast.unparse(gate)
    for name in ("TIMED_CONTRACT", "FUTURE_TASK_RELATIVE", "RUNNER_REVIEW",
                 "EXECUTION_ADOPTION", "TIMED_WRAPPER_RELATIVE", "DELEGATE_RELATIVE",
                 "TASK_CURRENT.md"):
        assert name in source
    assert len(_named_calls(gate, "_committed_authority_sha")) >= 7
    first_authority = min(node.lineno for node in _named_calls(gate, "_committed_authority_sha"))
    for name in ("sealed_evidence_checks", "protected_manifest_checks",
                 "lexists", "path_components_safe"):
        assert min(node.lineno for node in _named_calls(gate, name)) < first_authority
    committed = ast.unparse(_source_function(DELEGATE, "_committed_authority_sha"))
    assert "status" in committed and "rev-parse" in committed and "hash-object" in committed
    assert "NEW_C9_CONTRACT_IDENTITY" in source
    assert "NEW_C9_TASK_IDENTITY" in source
    assert "NEW_C9_INDEPENDENT_REVIEW_IDENTITY" in source
    assert "NEW_C9_OWNER_EXECUTION_ADOPTION" in source
    assert "exec_module" not in source and "spec_from_file_location" not in source


@pytest.fixture
def repair4_wrapper_only():
    before = {name for name in sys.modules if name.startswith("ch5_two_asset_hank")}
    wrapper = importlib.import_module(
        "validators.multi_province.k1b_turn9_post_failure_new_attempt_timed.run")
    after = {name for name in sys.modules if name.startswith("ch5_two_asset_hank")}
    assert after == before
    return wrapper


def test_repair4_committed_authority_file_fails_closed(repair4_wrapper_only, tmp_path, monkeypatch):
    wrapper = repair4_wrapper_only
    relative = Path("authority/contract.json")
    target = tmp_path / relative
    with pytest.raises(wrapper.TimingBlocked, match="DIRTY_OR_MISSING"):
        wrapper.committed_file(tmp_path, relative)
    target.parent.mkdir()
    target.write_text("inert authority fixture", encoding="utf-8")

    def git_reply(repo, *args):
        if args[0] == "status":
            return " M authority/contract.json"
        raise AssertionError("dirty authority must stop before Git blob lookup")

    monkeypatch.setattr(wrapper, "git", git_reply)
    with pytest.raises(wrapper.TimingBlocked, match="DIRTY_OR_MISSING"):
        wrapper.committed_file(tmp_path, relative)

    def mismatched_git(repo, *args):
        return "" if args[0] == "status" else ("a" * 40 if args[0] == "rev-parse" else "b" * 40)

    monkeypatch.setattr(wrapper, "git", mismatched_git)
    with pytest.raises(wrapper.TimingBlocked, match="NOT_COMMITTED"):
        wrapper.committed_file(tmp_path, relative)

    original_lstat = Path.lstat
    for unsafe in (target, target.parent):
        def reparse_lstat(path, unsafe=unsafe):
            original = original_lstat(path)
            if path == unsafe:
                return SimpleNamespace(st_mode=original.st_mode,
                                       st_file_attributes=getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400))
            return original

        with monkeypatch.context() as context:
            context.setattr(Path, "lstat", reparse_lstat)
            context.setattr(wrapper, "git", lambda *args: (_ for _ in ()).throw(
                AssertionError("unsafe authority must stop before Git lookup")))
            with pytest.raises(wrapper.TimingBlocked, match="DIRTY_OR_MISSING"):
                wrapper.committed_file(tmp_path, relative)


def test_repair4_active_preflight_rejects_missing_and_mocked_identity_failures(
        repair4_wrapper_only, monkeypatch):
    wrapper = repair4_wrapper_only
    with pytest.raises(wrapper.TimingBlocked, match="NEW_LIVE_CONTRACT_ABSENT"):
        wrapper.static_preflight(ROOT, require_inactive=False)
    for terminal in ("DIRTY_OR_MISSING", "NOT_COMMITTED", "NEW_C9_CONTRACT_IDENTITY",
                     "NEW_C9_INDEPENDENT_REVIEW_IDENTITY"):
        with monkeypatch.context() as context:
            def reject(repo, execution_id, terminal=terminal):
                raise wrapper.TimingBlocked(terminal)
            context.setattr(wrapper, "preimport_authority_gate", reject)
            with pytest.raises(wrapper.TimingBlocked, match=terminal):
                wrapper.static_preflight(ROOT, require_inactive=False)


def test_repair4_inactive_stays_blocked_and_active_accepts_only_mocked_valid_chain(
        repair4_wrapper_only, monkeypatch):
    wrapper = repair4_wrapper_only
    inactive = wrapper.static_preflight(ROOT, require_inactive=True)
    assert inactive["status"] == "BLOCKED__NEW_LIVE_AUTHORITY_ABSENT__PREPARATION_ONLY"
    assert inactive["scientific_calls"] == inactive["c9_attempts"] == 0
    future = {ROOT / path for path in (wrapper.CONTRACT, wrapper.TASK_COPY,
                                      wrapper.OWNER_ADOPTION, wrapper.INDEPENDENT_REVIEW)}
    original_lexists = wrapper.os.path.lexists

    def simulated_lexists(path):
        return True if Path(path) in future else original_lexists(path)

    with monkeypatch.context() as context:
        context.setattr(wrapper.os.path, "lexists", simulated_lexists)
        with pytest.raises(wrapper.TimingBlocked, match="NEW_C9_STATIC_IDENTITY"):
            wrapper.static_preflight(ROOT, require_inactive=True)
        context.setattr(wrapper, "preimport_authority_gate", lambda repo, execution_id: {
            "execution_id": execution_id})
        active = wrapper.static_preflight(ROOT, require_inactive=False)
    assert active["status"] == "ACTIVE_AUTHORITY_STATIC_PREFLIGHT_ONLY__NO_SCIENCE"
    assert active["checks"]["active_authority_committed_and_bound"] is True
    assert active["scientific_calls"] == active["c9_attempts"] == 0


@pytest.fixture
def repair5_modules():
    before = {name for name in sys.modules if name.startswith("ch5_two_asset_hank")}
    wrapper = importlib.import_module(
        "validators.multi_province.k1b_turn9_post_failure_new_attempt_timed.run")
    delegate = importlib.import_module(
        "validators.multi_province.k1b_turn9_post_failure_new_attempt_outer_r2.run")
    after = {name for name in sys.modules if name.startswith("ch5_two_asset_hank")}
    assert after == before
    return wrapper, delegate


@pytest.mark.parametrize("kind,component", [
    ("symlink", "leaf"), ("symlink", "parent"),
    ("reparse", "leaf"), ("reparse", "parent"),
])
def test_repair5_unsafe_authority_stops_before_follows_link_metadata(
        repair5_modules, tmp_path, monkeypatch, kind, component):
    relative = Path("authority/contract.json")
    target = tmp_path / relative
    target.parent.mkdir()
    target.write_text("inert authority fixture", encoding="utf-8")
    unsafe = target if component == "leaf" else target.parent
    original_lstat = Path.lstat
    original_is_file = Path.is_file

    def unsafe_lstat(path):
        if path != unsafe:
            return original_lstat(path)
        original = original_lstat(path)
        if kind == "symlink":
            return SimpleNamespace(st_mode=stat.S_IFLNK | 0o777, st_file_attributes=0)
        return SimpleNamespace(st_mode=original.st_mode,
                               st_file_attributes=getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400))

    def forbidden_is_file(path):
        if path == target:
            raise AssertionError("follows-link is_file reached unsafe authority")
        return original_is_file(path)

    monkeypatch.setattr(Path, "lstat", unsafe_lstat)
    monkeypatch.setattr(Path, "is_file", forbidden_is_file)
    for module in repair5_modules:
        monkeypatch.setattr(module, "git", lambda *args: (_ for _ in ()).throw(
            AssertionError("Git reached unsafe authority")))
        assert module.authority_file_present(tmp_path, relative) is False
        committed = (module.committed_file if module is repair5_modules[0]
                     else module._committed_authority_sha)
        with pytest.raises(module.TimingBlocked if module is repair5_modules[0]
                           else module.RepeatBlocked):
            committed(tmp_path, relative)


def test_repair5_missing_dirty_and_blob_mismatch_fail_in_both_helpers(
        repair5_modules, tmp_path, monkeypatch):
    relative = Path("authority/contract.json")
    target = tmp_path / relative
    for module in repair5_modules:
        committed = (module.committed_file if module is repair5_modules[0]
                     else module._committed_authority_sha)
        blocked = module.TimingBlocked if module is repair5_modules[0] else module.RepeatBlocked
        with pytest.raises(blocked):
            committed(tmp_path, relative)
    target.parent.mkdir()
    target.write_text("inert authority fixture", encoding="utf-8")
    for module in repair5_modules:
        committed = (module.committed_file if module is repair5_modules[0]
                     else module._committed_authority_sha)
        blocked = module.TimingBlocked if module is repair5_modules[0] else module.RepeatBlocked
        with monkeypatch.context() as context:
            context.setattr(module, "git", lambda repo, *args: " M authority/contract.json"
                            if args[0] == "status" else "a" * 40)
            with pytest.raises(blocked):
                committed(tmp_path, relative)
        with monkeypatch.context() as context:
            context.setattr(module, "git", lambda repo, *args: "" if args[0] == "status"
                            else ("a" * 40 if args[0] == "rev-parse" else "b" * 40))
            with pytest.raises(blocked):
                committed(tmp_path, relative)


def test_repair5_active_and_preimport_paths_reject_unsafe_contract_before_metadata(
        repair5_modules, monkeypatch):
    wrapper, delegate = repair5_modules
    contract = ROOT / wrapper.CONTRACT
    original_lstat = Path.lstat
    original_is_file = Path.is_file

    def symlink_contract_lstat(path):
        if path == contract:
            return SimpleNamespace(st_mode=stat.S_IFLNK | 0o777, st_file_attributes=0)
        return original_lstat(path)

    def forbidden_is_file(path):
        if path == contract:
            raise AssertionError("follows-link is_file reached unsafe live contract")
        return original_is_file(path)

    monkeypatch.setattr(Path, "lstat", symlink_contract_lstat)
    monkeypatch.setattr(Path, "is_file", forbidden_is_file)
    with pytest.raises(wrapper.TimingBlocked):
        wrapper.static_preflight(ROOT, require_inactive=False)
    with pytest.raises(wrapper.TimingBlocked):
        wrapper.preimport_authority_gate(ROOT, wrapper.NEW_EXECUTION_ID)
    with pytest.raises(delegate.RepeatBlocked):
        delegate.preimport_wrapper_authority_gate(ROOT, delegate.NEW_EXECUTION_ID)
    with pytest.raises(wrapper.TimingBlocked):
        wrapper.static_preflight(ROOT, require_inactive=True)


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
