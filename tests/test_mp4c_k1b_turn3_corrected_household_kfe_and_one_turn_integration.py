from pathlib import Path

import numpy as np

from validators.multi_province.k1b_turn3_corrected_household_kfe_and_one_turn_integration import run


REPOSITORY = Path(__file__).resolve().parents[1]


def test_preflight_binds_live_main_production_and_exact_k1b_inputs():
    gate = run.preflight(REPOSITORY)
    assert gate["status"] == "PASS"
    assert all(gate["checks"].values())


def test_entering_state_and_frozen_share_plan_are_exact():
    states, shares, receipt = run.load_entering_and_shares(REPOSITORY)
    assert receipt["status"] == "PASS"
    assert all(receipt["checks"].values())
    assert len(states) == 31
    assert run.base._field_sha256(shares) == run.TURN3_SHARE_SHA256
    assert run.base._field_sha256(np.asarray([state["rah"] for state in states])) == run.TURN3_RAH_SHA256


def test_relaxation_ledger_starts_at_zero():
    ledger = run.new_relaxation_ledger()
    assert ledger["helper_invocations"] == 0
    assert ledger["alpha_candidates_evaluated"] == 0
    assert ledger["failure"] is None


def test_turn4_ordered_arithmetic_is_the_accepted_population_convention():
    raw = np.arange(31, dtype=np.float64)
    mean, sigma, score = run.safety.ordered_population_zscore(raw)
    assert mean == 15.0
    assert sigma == np.sqrt(80.0)
    assert abs(sum(float(x) ** 2 for x in score) / 31.0 - 1.0) < 1e-15
    assert np.array_equal(run.safety.ordered_payoff(raw, np.eye(31)), raw)
