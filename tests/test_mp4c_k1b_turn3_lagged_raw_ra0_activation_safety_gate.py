from pathlib import Path

import numpy as np

from validators.multi_province.k1b_turn3_lagged_raw_ra0_activation_safety_gate import run


REPOSITORY = Path(__file__).resolve().parents[1]


def test_preflight_and_accepted_run005_inputs_are_exact():
    gate = run.preflight(REPOSITORY)
    assert gate["status"] == "PASS"
    assert all(gate["checks"].values())
    bound = run.load_bound_inputs(REPOSITORY)
    assert run.field_sha256(bound["raw"]) == run.EXPECTED_RAW_RA0_SHA256
    assert run.field_sha256(bound["k1a_rah"]) == run.EXPECTED_K1A_RAH_SHA256


def test_population_zscore_uses_ordered_ddof_zero_arithmetic():
    raw = np.arange(31, dtype=np.float64)
    mean, sigma, score = run.ordered_population_zscore(raw)
    assert mean == 15.0
    assert sigma == np.sqrt(80.0)
    assert abs(sum(float(x) for x in score)) < 1e-15
    assert abs(sum(float(x) ** 2 for x in score) / 31.0 - 1.0) < 1e-15


def test_ordered_payoff_keeps_raw_levels_separate_from_scores():
    raw = np.linspace(0.1, 3.1, 31, dtype=np.float64)
    shares = np.eye(31, dtype=np.float64)
    result = run.ordered_payoff(raw, shares)
    assert np.array_equal(result, raw)
    _, _, score = run.ordered_population_zscore(raw)
    assert not np.array_equal(result, score)


def test_zero_science_ledger_is_literal_zero():
    ledger = run.zero_science_ledger()
    assert ledger
    assert set(ledger.values()) == {0}
