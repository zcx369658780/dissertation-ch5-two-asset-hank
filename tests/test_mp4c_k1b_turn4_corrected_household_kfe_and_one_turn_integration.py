from pathlib import Path

import numpy as np

from validators.multi_province.k1b_turn4_corrected_household_kfe_and_one_turn_integration import run


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
    assert run.base._field_sha256(shares) == run.TURN4_SHARE_SHA256
    assert run.base._field_sha256(np.asarray([state["rah"] for state in states])) == run.TURN4_RAH_SHA256


def test_relaxation_ledger_starts_at_zero():
    ledger = run.new_relaxation_ledger()
    assert ledger["helper_invocations"] == 0
    assert ledger["alpha_candidates_evaluated"] == 0
    assert ledger["failure"] is None


def test_turn5_ordered_arithmetic_is_the_accepted_population_convention():
    raw = np.arange(31, dtype=np.float64)
    mean, sigma, score = run.safety.ordered_population_zscore(raw)
    assert mean == 15.0
    assert sigma == np.sqrt(80.0)
    assert abs(sum(float(x) ** 2 for x in score) / 31.0 - 1.0) < 1e-15
    assert np.array_equal(run.safety.ordered_payoff(raw, np.eye(31)), raw)


def test_prior_turn3_diagnostics_are_bound_for_cross_turn_panel():
    prior = run.load_prior_diagnostics(REPOSITORY)
    assert prior["status"] == "PASS"
    assert all(prior["checks"].values())
    assert len(prior["household"]["rows"]) == 31
    assert run.base._field_sha256(prior["raw_ra0_turn3"]) == run.TURN3_RAW_RA0_SHA256


def test_cross_turn_panel_is_descriptive_and_serializable(tmp_path):
    states, shares, _ = run.load_entering_and_shares(REPOSITORY)
    prior = run.load_prior_diagnostics(REPOSITORY)
    next_states = [{"state": dict(state)} for state in states]
    panel = run.write_cross_turn_panel(
        REPOSITORY,
        tmp_path,
        states,
        next_states,
        prior["household"]["rows"],
        prior["raw_ra0_turn3"],
        float(prior["score"]["ordered_mean"]),
        float(prior["score"]["population_standard_deviation"]),
        shares,
        float(prior["c1"]["GovInv_C1_total"]),
    )
    assert panel["status"] == "PASS"
    assert panel["acceptance_condition"] == "NONE__DESCRIPTIVE_PANEL_ONLY"
    assert panel["raw_ra0"]["maximum_absolute_change"] == 0.0
    assert panel["portfolio_shares"]["maximum_absolute_change"] == 0.0
    assert (tmp_path / "turn3_vs_turn4_cross_turn_diagnostic_panel.json").is_file()
