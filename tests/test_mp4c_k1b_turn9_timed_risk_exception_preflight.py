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


def test_default_cli_is_inert_and_inactive_execute_denies_before_delegate(monkeypatch):
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
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__INACTIVE_CONTRACT"):
        wrapper.run_timed_action(ROOT, forged, fake)
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__INACTIVE_CONTRACT"):
        wrapper._instrumented_action(fake, ROOT, forged, {"monotonic_ns": 0}, {}, {})
    assert entered == []
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


def _fake_delegate(recorded, action):
    real = wrapper.load_delegate(ROOT, enforce_contract_hash=False)
    fake = SimpleNamespace(BudgetGuard=real.BudgetGuard, OUTPUT=real.OUTPUT,
                           FUTURE_TASK_RELATIVE=real.FUTURE_TASK_RELATIVE,
                           PER_PROVINCE=real.PER_PROVINCE,
                           write_output_json=lambda output, runtime, path, value: recorded.append(value))
    fake._execute_after_gate = lambda repo, execution_id, runtime: action(fake, runtime)
    return fake, real


def test_attempt_journal_alias_and_cumulative_guard_use_one_event(monkeypatch):
    journal = []
    def action(fake, runtime):
        guard = fake.BudgetGuard()
        runtime["guard"] = guard
        runtime["ledger"] = {}
        guard.enter("frozen_k1b_quantity_allocations")
        guard.enter("turn9_household_calls")
        return "VALID__C9_NINE_COMPONENT_LEVEL_NOT_MET"
    fake, real = _fake_delegate(journal, action)
    gate = {"ceilings": real.CEILINGS, "cumulative": real.TWO_TURN_CEILINGS,
            "per_province": real.PER_PROVINCE, "wall_seconds": 3600,
            "execution_id": "INERT", "contract_sha256": "INERT"}
    monkeypatch.setattr(wrapper, "future_gate", lambda repo, execution_id, c9: gate)
    runtime, record = {}, {}
    result = wrapper._instrumented_action(fake, ROOT, gate,
                                           {"monotonic_ns": wrapper.time.monotonic_ns()},
                                           record, runtime)
    assert result == "VALID__C9_NINE_COMPONENT_LEVEL_NOT_MET"
    attempted = record["attempted"]
    assert attempted["frozen_k1b_quantity_allocations"] == attempted["k1b_feedback_calls"] == 1
    assert attempted["turn9_household_calls"] == 1
    assert attempted["turn10_household_calls"] == 0
    assert sum(row.get("event") == "attempted_before_source_call" for row in journal) == 2
    assert any(row.get("detail", {}).get("alias") for row in journal if isinstance(row.get("detail"), dict))


def test_expired_resource_wall_denies_next_entry_without_call(monkeypatch):
    journal = []
    def action(fake, runtime):
        guard = fake.BudgetGuard()
        runtime["guard"] = guard
        guard.enter("turn9_household_calls")
    fake, real = _fake_delegate(journal, action)
    gate = {"ceilings": real.CEILINGS, "cumulative": real.TWO_TURN_CEILINGS,
            "per_province": real.PER_PROVINCE, "wall_seconds": 1,
            "execution_id": "INERT", "contract_sha256": "INERT"}
    monkeypatch.setattr(wrapper, "future_gate", lambda repo, execution_id, c9: gate)
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__MEASUREMENT_RESOURCE_CAP_REACHED"):
        wrapper._instrumented_action(fake, ROOT, gate, {"monotonic_ns": 0}, {}, {})
    assert any(row.get("event") == "cooperative_resource_cap_reached" for row in journal)
    assert not any(row.get("event") == "attempted_before_source_call" for row in journal)


def test_safe_pause_is_emitted_only_after_complete_seal(monkeypatch):
    events = []
    real = wrapper.load_delegate(ROOT, enforce_contract_hash=False)
    attempted = dict.fromkeys(real.CEILINGS, 0)
    attempted["turn9_household_calls"] = 1
    attempted["selector_evaluations"] = 17
    attempted["scalar_selector_root_invocations"] = 9
    guard = SimpleNamespace(attempted=attempted,
                            per_province={0: {"selector_evaluations": 17,
                                              "scalar_selector_root_invocations": 9}})
    def run_gate(repo, execution_id, action):
        return action({"guard": guard, "ledger": {"turn9_household_calls": 1},
                       "state": {"ledger_unresolved": False}})
    fake = SimpleNamespace(OUTPUT=wrapper.OUTPUT, run_after_valid_gate=run_gate,
                           path_components_safe=lambda path: True,
                           sha=lambda path: "HASH",
                           environment_snapshot=lambda: {},
                           write_output_json=lambda output, runtime, path, value:
                               events.append((path.name, value)))
    monkeypatch.setattr(wrapper, "seal_science_outputs",
                        lambda c9, output, runtime: (events.append(("seal", None)) or
                                                     {"manifest_sha256": "MANIFEST", "entry_count": 1}))
    def inert_action(c9, repo, gate, start, record, runtime):
        record["attempted"] = {"turn9_household_calls": 1, "turn10_household_calls": 0}
        record["source_ledger"] = {"turn9_household_calls": 1}
        return "VALID__C9_NINE_COMPONENT_LEVEL_NOT_MET"
    monkeypatch.setattr(wrapper, "_instrumented_action", inert_action)
    gate = {"execution_id": "INERT", "owner_adoption_sha256": "OWNER",
                                       "contract_sha256": "CONTRACT", "ceilings": real.CEILINGS,
                                       "cumulative": real.TWO_TURN_CEILINGS,
                                       "per_province": real.PER_PROVINCE,
                                       "wall_seconds": 3600}
    monkeypatch.setattr(wrapper, "future_gate", lambda repo, execution_id, c9: gate)
    result = wrapper.run_timed_action(ROOT, gate, fake)
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
    fake = SimpleNamespace(OUTPUT=wrapper.OUTPUT, run_after_valid_gate=run_gate,
                           path_components_safe=lambda path: True,
                           owns_output_root=lambda output, runtime: True,
                           write_output_json=lambda output, runtime, path, value:
                               events.append((path.name, value)))
    gate = {"execution_id": "INERT"}
    monkeypatch.setattr(wrapper, "future_gate", lambda repo, execution_id, c9: gate)
    monkeypatch.setattr(wrapper, "seal_partial_outputs",
                        lambda c9, output, runtime: (events.append(("partial_seal", None)) or
                                                     {"status": "PASS", "manifest_sha256": "HASH",
                                                      "readback_sha256": "READBACK", "entry_count": 2}))
    monkeypatch.setattr(wrapper, "_instrumented_action",
                        lambda *args: (_ for _ in ()).throw(FirstFailure()))
    with pytest.raises(wrapper.TimingBlocked, match="CALL_LEDGER_UNRESOLVED") as caught:
        wrapper.run_timed_action(ROOT, gate, fake)
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
    guard = SimpleNamespace(attempted={"turn9_household_calls": 1}, per_province={},
                            open_province={}, integration_start=None)
    def run_gate(repo, execution_id, action):
        action({"guard": guard, "ledger": {"turn9_household_calls": 1},
                "state": {"original_terminal": "FAIL__SOURCE", "ledger_unresolved": False},
                "output_identity": (1, 2)})
    fake = SimpleNamespace(OUTPUT=wrapper.OUTPUT, run_after_valid_gate=run_gate,
                           path_components_safe=lambda path: True,
                           owns_output_root=lambda output, runtime: True,
                           write_output_json=lambda output, runtime, path, value:
                               events.append((path.name, value)))
    gate = {"execution_id": "INERT"}
    monkeypatch.setattr(wrapper, "future_gate", lambda repo, execution_id, c9: gate)
    monkeypatch.setattr(wrapper, "seal_partial_outputs",
                        lambda c9, output, runtime: {"status": "FAIL", "bad_paths": ["x"]})
    monkeypatch.setattr(wrapper, "_instrumented_action",
                        lambda *args: (_ for _ in ()).throw(RuntimeError("later")))
    with pytest.raises(wrapper.TimingBlocked, match="CALL_LEDGER_UNRESOLVED"):
        wrapper.run_timed_action(ROOT, gate, fake)
    assert events[0][0] == "timing_failure.json"
    assert events[0][1]["original_terminal"] == "FAIL__SOURCE"
    assert events[0][1]["terminal"] == "CALL_LEDGER_UNRESOLVED"
    assert events[0][1]["retry_allowed"] is False
