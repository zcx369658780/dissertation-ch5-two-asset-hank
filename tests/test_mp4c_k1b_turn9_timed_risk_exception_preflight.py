"""Inert C9 wrapper checks; all journals stay in memory."""
import importlib.util
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
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
    assert result["status"] == "BLOCKED__INACTIVE_CONTRACT"
    assert all(result["checks"].values())
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
    real = wrapper.load_delegate(ROOT)
    fake = SimpleNamespace(BudgetGuard=real.BudgetGuard, OUTPUT=real.OUTPUT,
                           FUTURE_TASK_RELATIVE=real.FUTURE_TASK_RELATIVE,
                           PER_PROVINCE=real.PER_PROVINCE,
                           write_output_json=lambda output, runtime, path, value: recorded.append(value))
    fake._execute_after_gate = lambda repo, execution_id, runtime: action(fake, runtime)
    return fake, real


def test_attempt_journal_alias_and_cumulative_guard_use_one_event():
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


def test_expired_resource_wall_denies_next_entry_without_call():
    journal = []
    def action(fake, runtime):
        guard = fake.BudgetGuard()
        runtime["guard"] = guard
        guard.enter("turn9_household_calls")
    fake, real = _fake_delegate(journal, action)
    gate = {"ceilings": real.CEILINGS, "cumulative": real.TWO_TURN_CEILINGS,
            "per_province": real.PER_PROVINCE, "wall_seconds": 1,
            "execution_id": "INERT", "contract_sha256": "INERT"}
    with pytest.raises(wrapper.TimingBlocked, match="BLOCKED__MEASUREMENT_RESOURCE_CAP_REACHED"):
        wrapper._instrumented_action(fake, ROOT, gate, {"monotonic_ns": 0}, {}, {})
    assert any(row.get("event") == "cooperative_resource_cap_reached" for row in journal)
    assert not any(row.get("event") == "attempted_before_source_call" for row in journal)


def test_safe_pause_is_emitted_only_after_complete_seal(monkeypatch):
    events = []
    real = wrapper.load_delegate(ROOT)
    attempted = dict.fromkeys(real.CEILINGS, 0)
    attempted["turn9_household_calls"] = 1
    guard = SimpleNamespace(attempted=attempted, per_province={})
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
    result = wrapper.run_timed_action(ROOT,
                                      {"execution_id": "INERT", "owner_adoption_sha256": "OWNER",
                                       "contract_sha256": "CONTRACT", "ceilings": real.CEILINGS,
                                       "cumulative": real.TWO_TURN_CEILINGS,
                                       "per_province": real.PER_PROVINCE,
                                       "wall_seconds": 3600}, fake, action=inert_action)
    assert [name for name, _ in events] == ["seal", "pause_receipt.json", "timing_receipt.json"]
    assert result["terminal"] == "SAFE_PAUSE_AFTER_SEALED_C9"
    assert events[1][1]["C10_started"] is False
    assert events[1][1]["C10_authorized"] is False
    assert not (ROOT / wrapper.OUTPUT).exists()
