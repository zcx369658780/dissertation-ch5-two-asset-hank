from __future__ import annotations

from pathlib import Path

import numpy as np

from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER
from validators.multi_province.k1b_turn5_turn6_bounded_continuation import run as gate


REPOSITORY = Path(__file__).resolve().parents[1]


def test_exact_turn5_entering_authority_is_bound() -> None:
    states, shares, raw, receipt = gate.load_turn5(REPOSITORY)
    assert receipt["status"] == "PASS"
    assert len(states) == 31
    assert shares.shape == (31, 31)
    assert raw.shape == (31,)
    assert gate.base._field_sha256(shares) == gate.TURN5_SHARE_SHA
    assert gate.base._field_sha256(np.asarray([row["rah"] for row in states])) == gate.TURN5_RAH_SHA


def test_production_source_is_exact_and_unmodified() -> None:
    receipt = gate.accepted_source_binding(REPOSITORY)
    assert receipt["status"] == "PASS"
    assert receipt["worktree_diff"] == []


def test_transition_panel_is_descriptive_and_complete() -> None:
    old_states = tuple({name: float(i + j) for j, name in enumerate(gate.STATE_FIELDS + ("rah",))}
                       for i in range(31))
    new_states = tuple({name: float(i + j) + 0.5 for j, name in enumerate(gate.STATE_FIELDS + ("rah",))}
                       for i in range(31))
    household_old = [{"checkpoint": 10} for _ in PROVINCE_ORDER]
    household_new = [{"checkpoint": 11} for _ in PROVINCE_ORDER]
    panel = gate.transition_panel("test", np.arange(31.0), np.arange(31.0) + 1.0,
        old_states, new_states, np.eye(31), np.eye(31), household_old, household_new,
        1.0, 2.0, 0.0, 1e-9)
    assert panel["classification"] == gate.DESCRIPTIVE
    assert panel["raw_ra0"]["euclidean_norm"] > 0.0
    assert panel["rah"]["euclidean_norm"] > 0.0
    assert set(panel["aggregate_state_changes"]) == set(gate.STATE_FIELDS)


def test_successive_ratios_have_no_convergence_acceptance_condition() -> None:
    base_panel = {"transition": "a", "raw_ra0": {"euclidean_norm": 2.0},
        "rah": {"euclidean_norm": 4.0}, "portfolio_shares": {"frobenius_norm": 8.0},
        "aggregate_state_changes": {name: {"euclidean_norm": 2.0} for name in gate.STATE_FIELDS}}
    next_panel = {"transition": "b", "raw_ra0": {"euclidean_norm": 1.0},
        "rah": {"euclidean_norm": 2.0}, "portfolio_shares": {"frobenius_norm": 4.0},
        "aggregate_state_changes": {name: {"euclidean_norm": 1.0} for name in gate.STATE_FIELDS}}
    receipt = gate.trajectory_panel([base_panel, next_panel])
    assert receipt["classification"] == gate.DESCRIPTIVE
    assert receipt["convergence_claim"] is False
    assert receipt["fixed_point_tolerance"] is None
    assert receipt["successive_change_norm_ratios"][0]["ratios"]["raw_ra0_euclidean"] == 0.5


def test_combined_ledger_uses_two_turn_ceiling_and_turn7_zero() -> None:
    left, right = gate.new_ledger(5), gate.new_ledger(6)
    left["source_native_initializations"] = right["source_native_initializations"] = 31
    left["turn5_household_calls"] = 1
    right["turn6_household_calls"] = 1
    receipt = gate.combined_ledger({5: left, 6: right})
    assert receipt["status"] == "PASS"
    assert receipt["source_native_initializations"] == 62
    assert receipt["turn7_household_calls"] == 0
