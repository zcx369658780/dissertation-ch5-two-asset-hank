"""Inert C9 wrapper checks; all journals stay in memory."""
import importlib.util
import hashlib
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path, PurePosixPath
from types import SimpleNamespace

import pytest


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "validators/multi_province/k1b_turn9_timed_risk_exception/run.py"
spec = importlib.util.spec_from_file_location("c9_timed_wrapper_under_test", PATH)
wrapper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wrapper)
CONTRACT = ROOT / wrapper.CONTRACT


def _allow_uncommitted_candidate_in_inert_test(monkeypatch):
    original = wrapper.committed_file
    monkeypatch.setattr(wrapper, "committed_file",
                        lambda repo, relative: wrapper.sha(repo / relative)
                        if relative == wrapper.DELEGATE else original(repo, relative))


def test_default_cli_is_inert_and_inactive_execute_denies_before_delegate(monkeypatch):
    _allow_uncommitted_candidate_in_inert_test(monkeypatch)
    result = wrapper.static_preflight(ROOT)
    assert result["status"] == "BLOCKED__INACTIVE_CONTRACT__DELEGATE_REBIND_REQUIRED"
    assert result["checks"]["delegate_hash"] is False  # Frozen inactive contract is read-only in Repair1.
    assert all(value for key, value in result["checks"].items() if key != "delegate_hash")
    assert all(result["delegated_checks"].values())
    assert result["scientific_calls"] == result["c9_attempts"] == result["c10_attempts"] == 0
    monkeypatch.setattr(wrapper, "load_delegate", lambda _: pytest.fail("delegate entered"))
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__INACTIVE_CONTRACT"):
        wrapper.execute_once(ROOT, "INERT")
    assert not (ROOT / wrapper.OUTPUT).exists()


def test_contract_and_sealed_identity_mismatch_fail_closed(monkeypatch):
    original = Path.read_text
    def bad_contract(path, *args, **kwargs):
        text = original(path, *args, **kwargs)
        if path == CONTRACT:
            doc = json.loads(text)
            doc["resource_wall_seconds"] = 1
            return json.dumps(doc)
        return text
    monkeypatch.setattr(Path, "read_text", bad_contract)
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__C9_STATIC_IDENTITY"):
        wrapper.static_preflight(ROOT)
    monkeypatch.setattr(Path, "read_text", original)
    real_sha = wrapper.sha
    monkeypatch.setattr(wrapper, "sha", lambda p: "BAD" if p.name == "turn9_entering_bundle_manifest.json" else real_sha(p))
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__C9_STATIC_IDENTITY"):
        wrapper.static_preflight(ROOT)
    monkeypatch.setattr(wrapper, "sha", real_sha)
    real_lexists = wrapper.os.path.lexists
    monkeypatch.setattr(wrapper.os.path, "lexists",
                        lambda path: True if Path(path) == ROOT / wrapper.OUTPUT else real_lexists(path))
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__C9_STATIC_IDENTITY"):
        wrapper.static_preflight(ROOT)


def test_caller_constructed_active_looking_gate_cannot_enter(monkeypatch):
    entered = []
    fake = SimpleNamespace(path_components_safe=lambda path: True, OUTPUT=wrapper.OUTPUT,
                           run_after_valid_gate=lambda *args: entered.append("science"))
    forged = {"execution_id": "FORGED", "wall_seconds": 3600,
              "contract_sha256": "FORGED", "ceilings": {}, "cumulative": {}}
    monkeypatch.setattr(wrapper, "future_gate", lambda *args: forged)
    with pytest.raises(TypeError):
        wrapper.run_timed_action(ROOT, forged, fake)
    assert not hasattr(wrapper, "_instrumented_action")
    assert entered == []
    assert not (ROOT / wrapper.OUTPUT).exists()


def test_production_entries_load_delegate_before_any_action(monkeypatch):
    forged = {"execution_id": "INERT", "wall_seconds": 3600}
    entered = []
    def deny_identity(repo):
        entered.append("load_fixed_delegate")
        raise wrapper.TimingBlocked("BLOCKED__C9_DELEGATE_IDENTITY")
    monkeypatch.setattr(wrapper, "load_delegate", deny_identity)
    monkeypatch.setattr(wrapper, "future_gate", lambda *args: forged)
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__C9_DELEGATE_IDENTITY"):
        wrapper.run_timed_action(ROOT, forged)
    assert entered == ["load_fixed_delegate"]
    bound = object()
    monkeypatch.setattr(wrapper, "load_delegate", lambda repo: bound)
    def check_bound(repo, execution_id, c9):
        assert c9 is bound
        raise wrapper.TimingBlocked("BLOCKED__INERT_AFTER_BOUND_IDENTITY")
    monkeypatch.setattr(wrapper, "future_gate", check_bound)
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__INERT_AFTER_BOUND_IDENTITY"):
        wrapper.run_timed_action(ROOT, forged)
    assert not (ROOT / wrapper.OUTPUT).exists()


def test_dirty_contract_or_delegate_denied_before_module_import(monkeypatch):
    import_calls = []
    monkeypatch.setattr(wrapper.importlib.util, "spec_from_file_location",
                        lambda *args: import_calls.append(args) or pytest.fail("delegate imported"))
    original = wrapper.committed_file
    for target in (wrapper.CONTRACT, wrapper.DELEGATE):
        def reject(repo, relative, target=target):
            if relative == target:
                raise wrapper.TimingBlocked("BLOCKED__MEASUREMENT_AUTHORITY_DIRTY_OR_MISSING")
            return original(repo, relative)
        monkeypatch.setattr(wrapper, "committed_file", reject)
        with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__MEASUREMENT_AUTHORITY_DIRTY_OR_MISSING"):
            wrapper.load_delegate(ROOT)
    assert import_calls == []


def test_real_delegate_accepts_only_wrapper_measured_context_before_science(monkeypatch):
    _allow_uncommitted_candidate_in_inert_test(monkeypatch)
    c9 = wrapper.load_delegate(ROOT, enforce_contract_hash=False)
    gate = {"execution_id": "INERT", "contract_sha256": "INERT_CONTRACT",
            "ceilings": c9.CEILINGS, "cumulative": c9.TWO_TURN_CEILINGS,
            "per_province": c9.PER_PROVINCE, "wall_seconds": 3600}
    entered = []
    monkeypatch.setattr(wrapper, "load_delegate", lambda repo: c9)
    monkeypatch.setattr(wrapper, "future_gate", lambda repo, execution_id, module: gate)
    monkeypatch.setattr(c9, "assert_active_authority",
                        lambda repo, execution_id: {"contract_sha256": "INERT_CONTRACT"})
    def stop_before_science(repo):
        entered.append("preflight_after_measured_guard")
        raise RuntimeError("INERT_PRE_SCIENCE_STOP")
    monkeypatch.setattr(c9, "preflight", stop_before_science)
    with pytest.raises(wrapper.TimingBlocked, match="CALL_LEDGER_UNRESOLVED"):
        wrapper.run_timed_action(ROOT, gate)
    assert entered == ["preflight_after_measured_guard"]
    assert not (ROOT / wrapper.OUTPUT).exists()


def test_clock_resource_semantics_and_budget_schema(monkeypatch):
    start = {"monotonic_ns": 100, "utc": datetime(2026, 9, 26, tzinfo=timezone.utc).isoformat()}
    end = {"monotonic_ns": 1_000_000_100,
           "utc": (datetime(2026, 9, 26, tzinfo=timezone.utc) + timedelta(seconds=1)).isoformat()}
    assert wrapper.elapsed_clock(start, end) == 1_000_000_000
    end["utc"] = (datetime(2026, 9, 26, tzinfo=timezone.utc) + timedelta(seconds=5)).isoformat()
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__CLOCK_MAPPING_INVALID"):
        wrapper.elapsed_clock(start, end)
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__MEASUREMENT_BUDGET_CATEGORY_SET"):
        wrapper._contract_numbers({"wrong": 1}, {"right": 1})
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__MEASUREMENT_BUDGET_VALUE"):
        wrapper._contract_numbers({"right": True}, {"right": 1})


def _fake_delegate(monkeypatch, recorded, action):
    _allow_uncommitted_candidate_in_inert_test(monkeypatch)
    real = wrapper.load_delegate(ROOT, enforce_contract_hash=False)
    fake = SimpleNamespace(BudgetGuard=real.BudgetGuard, OUTPUT=real.OUTPUT,
                           FUTURE_TASK_RELATIVE=real.FUTURE_TASK_RELATIVE,
                           PER_PROVINCE=real.PER_PROVINCE,
                           path_components_safe=lambda path: True,
                           owns_output_root=lambda output, runtime: False,
                           run_after_valid_gate=lambda repo, execution_id, callback:
                               callback({"guard": None, "ledger": None, "state": None,
                                         "output_identity": None}),
                           write_output_json=lambda output, runtime, path, value: recorded.append(value))
    fake._execute_after_gate = lambda repo, execution_id, runtime: action(fake, runtime)
    return fake, real


def test_attempt_journal_alias_and_cumulative_guard_use_one_event(monkeypatch):
    journal = []
    holder = {}
    def action(fake, runtime):
        guard = runtime["c9_timed_guard"]
        holder["guard"] = guard
        runtime["guard"] = guard
        runtime["ledger"] = {}
        guard.enter("frozen_k1b_quantity_allocations")
        guard.enter("turn9_household_calls")
        return "VALID__C9_NINE_COMPONENT_LEVEL_NOT_MET"
    fake, real = _fake_delegate(monkeypatch, journal, action)
    gate = {"ceilings": real.CEILINGS, "cumulative": real.TWO_TURN_CEILINGS,
            "per_province": real.PER_PROVINCE, "wall_seconds": 3600,
            "execution_id": "INERT", "contract_sha256": "INERT"}
    monkeypatch.setattr(wrapper, "load_delegate", lambda repo: fake)
    monkeypatch.setattr(wrapper, "future_gate", lambda repo, execution_id, c9: gate)
    monkeypatch.setattr(wrapper, "seal_science_outputs",
                        lambda *args: (_ for _ in ()).throw(RuntimeError("INERT_AFTER_ACTION")))
    with pytest.raises(wrapper.TimingBlocked, match="RuntimeError"):
        wrapper.run_timed_action(ROOT, gate)
    attempted = holder["guard"].attempted
    assert attempted["frozen_k1b_quantity_allocations"] == attempted["k1b_feedback_calls"] == 1
    assert attempted["turn9_household_calls"] == 1
    assert attempted["turn10_household_calls"] == 0
    assert sum(row.get("event") == "attempted_before_source_call" for row in journal) == 2
    assert any(row.get("detail", {}).get("alias") for row in journal if isinstance(row.get("detail"), dict))


def test_expired_resource_wall_denies_next_entry_without_call(monkeypatch):
    journal = []
    def action(fake, runtime):
        guard = runtime["c9_timed_guard"]
        runtime["guard"] = guard
        guard.enter("turn9_household_calls")
    fake, real = _fake_delegate(monkeypatch, journal, action)
    gate = {"ceilings": real.CEILINGS, "cumulative": real.TWO_TURN_CEILINGS,
            "per_province": real.PER_PROVINCE, "wall_seconds": 0,
            "execution_id": "INERT", "contract_sha256": "INERT"}
    monkeypatch.setattr(wrapper, "load_delegate", lambda repo: fake)
    monkeypatch.setattr(wrapper, "future_gate", lambda repo, execution_id, c9: gate)
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__MEASUREMENT_RESOURCE_CAP_REACHED"):
        wrapper.run_timed_action(ROOT, gate)
    assert any(row.get("event") == "cooperative_resource_cap_reached" for row in journal)
    assert not any(row.get("event") == "attempted_before_source_call" for row in journal)


def test_safe_pause_is_emitted_only_after_complete_seal(monkeypatch):
    events = []
    identities = []
    _allow_uncommitted_candidate_in_inert_test(monkeypatch)
    real = wrapper.load_delegate(ROOT, enforce_contract_hash=False)
    attempted = dict.fromkeys(real.CEILINGS, 0)
    attempted["turn9_household_calls"] = 1
    attempted["selector_evaluations"] = 17
    attempted["scalar_selector_root_invocations"] = 9
    def run_gate(repo, execution_id, action):
        identities.append(fake)
        return action({"guard": None, "ledger": None,
                       "state": {"ledger_unresolved": False}})
    def science(repo, execution_id, runtime):
        identities.append(fake)
        guard = runtime["c9_timed_guard"]
        assert isinstance(guard, real.BudgetGuard)
        guard.attempted.update(attempted)
        guard.per_province[0] = {"selector_evaluations": 17,
                                 "scalar_selector_root_invocations": 9}
        runtime["guard"] = guard
        runtime["ledger"] = {"turn9_household_calls": 1}
        return "VALID__C9_NINE_COMPONENT_LEVEL_NOT_MET"
    fake = SimpleNamespace(BudgetGuard=real.BudgetGuard, OUTPUT=wrapper.OUTPUT,
                           FUTURE_TASK_RELATIVE=real.FUTURE_TASK_RELATIVE,
                           PER_PROVINCE=real.PER_PROVINCE,
                           run_after_valid_gate=run_gate, _execute_after_gate=science,
                           path_components_safe=lambda path: True,
                           sha=lambda path: "HASH",
                           environment_snapshot=lambda: {},
                           write_output_json=lambda output, runtime, path, value:
                               events.append((path.name, value)))
    monkeypatch.setattr(wrapper, "seal_science_outputs",
                        lambda c9, output, runtime: (identities.append(c9) or events.append(("seal", None)) or
                                                     {"manifest_sha256": "MANIFEST", "entry_count": 1}))
    gate = {"execution_id": "INERT", "owner_adoption_sha256": "OWNER",
                                       "contract_sha256": "CONTRACT", "ceilings": real.CEILINGS,
                                       "cumulative": real.TWO_TURN_CEILINGS,
                                       "per_province": real.PER_PROVINCE,
                                       "wall_seconds": 3600}
    monkeypatch.setattr(wrapper, "load_delegate", lambda repo: fake)
    monkeypatch.setattr(wrapper, "future_gate",
                        lambda repo, execution_id, c9: (identities.append(c9) or gate))
    result = wrapper.run_timed_action(ROOT, gate)
    assert identities == [fake, fake, fake, fake, fake]
    assert [name for name, _ in events] == ["seal", "timing_receipt.json", "pause_receipt.json"]
    assert result["terminal"] == "SAFE_PAUSE_AFTER_SEALED_C9"
    assert events[1][1]["safe_pause_pending"] is True
    assert events[2][1]["C10_started"] is False
    assert events[2][1]["C10_authorized"] is False
    assert events[2][1]["attempted_per_province_C9"][0]["selector_evaluations"] == 17
    assert events[2][1]["remaining_per_province_C9"]["0"]["selector_evaluations"] == 40783
    assert events[2][1]["remaining_per_province_C9"]["0"]["scalar_selector_root_invocations"] == 19999991
    assert not (ROOT / wrapper.OUTPUT).exists()


def test_partial_manifest_and_readback_use_only_in_memory_files(monkeypatch):
    class FakeOutput:
        def __init__(self):
            self.files = {"attempt_journal_0000001.json": b"attempt",
                          "terminal_receipt.json": b"terminal"}
        def __truediv__(self, name):
            return FakePath(self, name)
        def rglob(self, pattern):
            return [FakePath(self, name) for name in tuple(self.files)]
    class FakePath:
        def __init__(self, root, name):
            self.root, self.name = root, name
        def __lt__(self, other):
            return self.name < other.name
        def is_file(self):
            return self.name in self.root.files
        def stat(self):
            return SimpleNamespace(st_size=len(self.root.files[self.name]))
        def relative_to(self, root):
            assert root is self.root
            return PurePosixPath(self.name)
    output = FakeOutput()
    fake = SimpleNamespace(owns_output_root=lambda output, runtime: True,
                           path_components_safe=lambda path: True,
                           write_output_json=lambda output, runtime, path, value:
                               output.files.__setitem__(path.name, json.dumps(value).encode()))
    monkeypatch.setattr(wrapper, "sha",
                        lambda path: hashlib.sha256(output.files[path.name]).hexdigest().upper())
    sealed = wrapper.seal_partial_outputs(fake, output, {})
    manifest = json.loads(output.files["partial_artifact_manifest.json"])
    readback = json.loads(output.files["partial_artifact_readback.json"])
    assert sealed["status"] == readback["status"] == "PASS"
    assert {row["path"] for row in manifest["entries"]} == {
        "attempt_journal_0000001.json", "terminal_receipt.json"}
    assert manifest["complete_outer_turn"] is False and readback["safe_pause"] is False


def test_failure_after_entry_seals_partial_root_without_safe_pause(monkeypatch):
    events = []
    _allow_uncommitted_candidate_in_inert_test(monkeypatch)
    real = wrapper.load_delegate(ROOT, enforce_contract_hash=False)
    guard = SimpleNamespace(attempted={"turn9_household_calls": 1},
                            per_province={0: {"selector_evaluations": 17}},
                            open_province={0: {}}, integration_start=None)
    class FirstFailure(RuntimeError):
        terminal = "FAIL__LATER"
    def run_gate(repo, execution_id, action):
        runtime = {"guard": guard, "ledger": {"selector_evaluations": 17},
                   "state": {"original_terminal": "FAIL__FIRST", "ledger_unresolved": True},
                   "output_identity": (1, 2), "inflight_province": 0,
                   "reserved_exposure_at_interruption": {"selector_evaluations": 40800}}
        action(runtime)
    fake = SimpleNamespace(BudgetGuard=real.BudgetGuard, OUTPUT=wrapper.OUTPUT,
                           FUTURE_TASK_RELATIVE=real.FUTURE_TASK_RELATIVE,
                           PER_PROVINCE=real.PER_PROVINCE,
                           _execute_after_gate=lambda *args: (_ for _ in ()).throw(FirstFailure()),
                           run_after_valid_gate=run_gate,
                           path_components_safe=lambda path: True,
                           owns_output_root=lambda output, runtime: True,
                           write_output_json=lambda output, runtime, path, value:
                               events.append((path.name, value)))
    gate = {"execution_id": "INERT"}
    monkeypatch.setattr(wrapper, "load_delegate", lambda repo: fake)
    monkeypatch.setattr(wrapper, "future_gate", lambda repo, execution_id, c9: gate)
    monkeypatch.setattr(wrapper, "seal_partial_outputs",
                        lambda c9, output, runtime: (events.append(("partial_seal", None)) or
                                                     {"status": "PASS", "manifest_sha256": "HASH",
                                                      "readback_sha256": "READBACK", "entry_count": 2}))
    with pytest.raises(wrapper.TimingBlocked, match="CALL_LEDGER_UNRESOLVED") as caught:
        wrapper.run_timed_action(ROOT, gate)
    assert [name for name, _ in events] == ["partial_seal", "timing_failure.json"]
    failure = events[1][1]
    assert failure["original_terminal"] == "FAIL__FIRST"
    assert failure["partial_artifacts"]["status"] == "PASS"
    assert failure["reserved_exposure"]["selector_evaluations"] == 40800
    assert failure["per_province_attempted"][0]["selector_evaluations"] == 17
    assert failure["retry_allowed"] is False and failure["safe_pause"] is False
    assert caught.value.detail["original_terminal"] == "FAIL__FIRST"
    assert not (ROOT / wrapper.OUTPUT).exists()


def test_failed_partial_readback_forces_unresolved_terminal(monkeypatch):
    events = []
    _allow_uncommitted_candidate_in_inert_test(monkeypatch)
    real = wrapper.load_delegate(ROOT, enforce_contract_hash=False)
    guard = SimpleNamespace(attempted={"turn9_household_calls": 1}, per_province={},
                            open_province={}, integration_start=None)
    def run_gate(repo, execution_id, action):
        action({"guard": guard, "ledger": {"turn9_household_calls": 1},
                "state": {"original_terminal": "FAIL__SOURCE", "ledger_unresolved": False},
                "output_identity": (1, 2)})
    fake = SimpleNamespace(BudgetGuard=real.BudgetGuard, OUTPUT=wrapper.OUTPUT,
                           FUTURE_TASK_RELATIVE=real.FUTURE_TASK_RELATIVE,
                           PER_PROVINCE=real.PER_PROVINCE,
                           _execute_after_gate=lambda *args: (_ for _ in ()).throw(RuntimeError("later")),
                           run_after_valid_gate=run_gate,
                           path_components_safe=lambda path: True,
                           owns_output_root=lambda output, runtime: True,
                           write_output_json=lambda output, runtime, path, value:
                               events.append((path.name, value)))
    gate = {"execution_id": "INERT"}
    monkeypatch.setattr(wrapper, "load_delegate", lambda repo: fake)
    monkeypatch.setattr(wrapper, "future_gate", lambda repo, execution_id, c9: gate)
    monkeypatch.setattr(wrapper, "seal_partial_outputs",
                        lambda c9, output, runtime: {"status": "FAIL", "bad_paths": ["x"]})
    with pytest.raises(wrapper.TimingBlocked, match="CALL_LEDGER_UNRESOLVED"):
        wrapper.run_timed_action(ROOT, gate)
    assert events[0][0] == "timing_failure.json"
    assert events[0][1]["original_terminal"] == "FAIL__SOURCE"
    assert events[0][1]["terminal"] == "CALL_LEDGER_UNRESOLVED"
    assert events[0][1]["retry_allowed"] is False
