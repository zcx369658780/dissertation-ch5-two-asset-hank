"""Inert C9 delegate checks; no household or output is entered."""
import importlib.util
import json
from pathlib import Path

import numpy as np
import pytest


ROOT = Path(__file__).resolve().parents[1]
DELEGATE = ROOT / "validators/multi_province/k1b_turn9_outer_r2/run.py"
spec = importlib.util.spec_from_file_location("c9_delegate_under_test", DELEGATE)
c9 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c9)


def test_inactive_delegate_has_no_direct_science_entry():
    with pytest.raises(c9.RepeatBlocked, match="BLOCKED__C9_WRAPPER_REQUIRED"):
        c9.execute_once(ROOT, "INERT")
    with pytest.raises(c9.RepeatBlocked, match="BLOCKED__INACTIVE_CONTRACT"):
        c9._execute_after_gate(ROOT, "INERT", {})
    with pytest.raises(c9.RepeatBlocked, match="BLOCKED__INACTIVE_CONTRACT"):
        c9.run_after_valid_gate(ROOT, "INERT", lambda runtime: pytest.fail("action entered"))
    assert not (ROOT / c9.OUTPUT).exists()


def test_active_looking_direct_delegate_runtime_denied_before_output(monkeypatch):
    monkeypatch.setattr(c9, "assert_active_authority",
                        lambda repo, execution_id: {"contract_sha256": "INERT_ACTIVE"})
    monkeypatch.setattr(c9, "claim_output_root",
                        lambda *args: pytest.fail("output root claimed"))
    runtime_values = {"c9_wrapper_contract_sha256": "INERT_ACTIVE",
                      "c9_wrapper_execution_id": "INERT"}
    with pytest.raises(c9.RepeatBlocked, match="BLOCKED__C9_TIMED_WRAPPER_RUNTIME_REQUIRED"):
        c9._execute_after_gate(ROOT, "INERT", dict(runtime_values))
    with pytest.raises(c9.RepeatBlocked, match="BLOCKED__C9_TIMED_WRAPPER_ACTION_REQUIRED"):
        c9.run_after_valid_gate(ROOT, "INERT",
                                lambda runtime: c9._execute_after_gate(
                                    ROOT, "INERT", {**runtime, **runtime_values}))
    assert not (ROOT / c9.OUTPUT).exists()


def test_sealed_c8_identity_and_39_category_budget():
    report = c9.preflight(ROOT)
    assert report["status"] == "PASS__STATIC_PREFLIGHT_ONLY"
    assert all(report["checks"].values())
    assert all(report["prior_output_checks"].values())
    assert len(c9.CEILINGS) == 39
    assert len(c9.PER_PROVINCE) == 5
    assert c9.CEILINGS["turn8_household_calls"] == 0
    assert c9.CEILINGS["turn9_household_calls"] == 1
    assert c9.CEILINGS["turn10_household_calls"] == 0
    assert c9.TWO_TURN_CEILINGS["turn10_household_calls"] == 1
    contract = json.loads((ROOT / "tasks/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_INACTIVE_CONTRACT.json").read_text())
    assert contract["per_category_attempt_ceiling"] == c9.CEILINGS
    assert contract["per_province_attempt_ceiling"] == c9.PER_PROVINCE
    assert contract["c9_c10_cumulative_ceiling"] == c9.TWO_TURN_CEILINGS
    assert report["scientific_calls"] == 0


def test_per_turn_province_and_cumulative_denial():
    guard = c9.BudgetGuard()
    guard.enter("turn9_household_calls")
    with pytest.raises(c9.RepeatBlocked, match="BLOCKED__ENTRY_BEFORE_CALL_BUDGET"):
        guard.enter("turn9_household_calls")
    province = c9.BudgetGuard()
    for _ in range(51):
        province.enter("corrected_policy_maps", 0)
    with pytest.raises(c9.RepeatBlocked, match="BLOCKED__PROVINCE_BUDGET"):
        province.enter("corrected_policy_maps", 0)
    prior = {"full_integrations": 2}
    cumulative = c9.BudgetGuard(prior=prior)
    with pytest.raises(c9.RepeatBlocked, match="BLOCKED__ENTRY_BEFORE_CALL_BUDGET"):
        cumulative.enter("full_integrations")
    for key, ceiling in c9.CEILINGS.items():
        if ceiling == 0:
            with pytest.raises(c9.RepeatBlocked):
                c9.BudgetGuard().enter(key)


@pytest.mark.parametrize("category,limit", [
    ("selector_evaluations", 40800),
    ("scalar_selector_root_invocations", 20000000),
])
def test_actual_province_counts_reconcile_without_double_count(category, limit):
    ledger = dict.fromkeys(c9.CEILINGS, 0)
    guard = c9.BudgetGuard()
    guard.begin_province(0, ledger, {category: limit})
    ledger[category] = limit
    guard.reconcile(ledger, 0)
    guard.reconcile(ledger, 0)  # Repeated map readout is cumulative, not a second attempt.
    assert guard.per_province[0][category] == limit
    assert guard.attempted[category] == limit
    assert guard.prior[category] + guard.attempted[category] <= guard.combined[category]
    with pytest.raises(c9.RepeatBlocked, match="BLOCKED__PROVINCE_BUDGET"):
        guard.reserve({category: 1}, 0)
    ledger[category] = limit + 1  # One province fails while global total stays below its cap.
    assert ledger[category] < c9.CEILINGS[category]
    with pytest.raises(c9.RepeatBlocked, match="BLOCKED__PROVINCE_BUDGET"):
        guard.reconcile(ledger, 0)


def test_interrupted_province_preserves_first_failure_and_reserved_exposure():
    ledger = dict.fromkeys(c9.CEILINGS, 0)
    guard = c9.BudgetGuard()
    envelope = {"source_native_initializations": 1, "scalar_labor_roots_attempted": 800}
    guard.begin_province(0, ledger, envelope)
    guard.reserve(envelope, 0)
    ledger["source_native_initializations"] = 1
    ledger["scalar_labor_roots_attempted"] = 17
    runtime = {"state": {"original_terminal": "FAIL__FIRST", "ledger_unresolved": False},
               "guard": guard, "ledger": ledger, "inflight_province": 0,
               "inflight_reserved_envelope": envelope, "scientific_started": True}
    c9.mark_interrupted_province(runtime, RuntimeError("later interrupt"))
    detail = c9.failure_detail(runtime, "FAIL__FIRST", "INERT")
    assert detail["terminal"] == "CALL_LEDGER_UNRESOLVED"
    assert detail["original_terminal"] == "FAIL__FIRST"
    assert detail["confirmed_attempted_at_interruption"]["scalar_labor_roots_attempted"] == 17
    assert detail["reserved_exposure_at_interruption"]["scalar_labor_roots_attempted"] == 800
    assert detail["retry_allowed"] is False


def _bundle(turn, delta=0.0):
    rows = []
    for index in range(31):
        state = {key: 1.0 for key in c9.FIELDS if key not in ("raw_ra0", "S")}
        state["Kt0"] = 1.0
        rows.append({"state": state, f"raw_ra0_turn{turn-1}": delta if index == 0 else 0.0})
    return {"rows": rows, "S": np.eye(31, dtype=np.float64)}


def test_nine_component_strict_boundary_and_pause_only_after_valid_comparison():
    first = _bundle(9)
    below = c9.compare_carrier(first, _bundle(10, 0.5e-6))
    assert len(below["components"]) == 9
    assert below["all_nine_strictly_below_level"] is True
    assert below["consecutive_new_passes"] == 1
    at_boundary = c9.compare_carrier(first, _bundle(10, 1e-6))
    assert at_boundary["all_nine_strictly_below_level"] is False
    assert at_boundary["consecutive_new_passes"] == 0
    assert c9.turn9_terminal(at_boundary) == "VALID__C9_NINE_COMPONENT_LEVEL_NOT_MET"
    assert c9.turn9_terminal(below) == "VALID__C9_NINE_COMPONENT_LEVEL_MET"
    with pytest.raises(c9.RepeatBlocked, match="FAIL__OUTER_COMPARISON_UNAVAILABLE"):
        c9.turn9_terminal({"classification": "UNAVAILABLE"})


def test_uncertain_first_failure_preserves_original_and_no_retry():
    guard = c9.BudgetGuard()
    guard.enter("turn9_household_calls")
    runtime = {"state": {"ledger_unresolved": True}, "guard": guard,
               "scientific_started": True, "ledger": {"turn9_household_calls": 1}}
    detail = c9.failure_detail(runtime, "FAIL__FIRST_SCIENCE", "INERT")
    assert detail["terminal"] == "CALL_LEDGER_UNRESOLVED"
    assert detail["original_terminal"] == "FAIL__FIRST_SCIENCE"
    assert detail["literal_scientific_call_ledger"]["turn9_household_calls"] == 1
    assert detail["call_ledger_resolved"] is False
