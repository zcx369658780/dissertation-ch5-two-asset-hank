from __future__ import annotations

import numpy as np
import pytest

from validators.multi_province.k1_j160_liquid_grid_bounded_precision_sensitivity import (
    finalize,
    run,
)


def test_exact_fresh_liquid_grid_ladder_and_frozen_state() -> None:
    assert run.POINTS == ((40, 160), (80, 160))
    specs = [run.liquid_precision_spec(index) for index in range(2)]
    assert [(item["I"], item["J"]) for item in specs] == [(40, 160), (80, 160)]
    assert [item["db"] for item in specs] == pytest.approx([22.0 / 39.0, 22.0 / 79.0])
    for item in specs:
        assert (item["rb"], item["ra"], item["wage"], item["h"]) == (0.02, 0.0675, 15.5, 1.0)
        assert (item["amin"], item["amax"], item["bmin"], item["bmax"]) == (0.0, 100.0, -2.0, 20.0)
        assert item["da"] == pytest.approx(100.0 / 159.0)


def test_other_points_fail_closed_before_fixture_construction() -> None:
    with pytest.raises(ValueError, match="authorized"):
        run.liquid_precision_spec(2)
    with pytest.raises(ValueError, match="authorized"):
        run.build_fixture({**run.liquid_precision_spec(0), "I": 160})


def test_input_invariance_allows_only_liquid_grid_to_change() -> None:
    fixtures = [run.build_fixture(run.liquid_precision_spec(index)) for index in range(2)]
    receipt = run.input_invariance_receipt(fixtures)
    assert receipt["varying_fields"] == ["grid.b"]
    assert receipt["unexpected_varying_fields"] == []
    assert receipt["fresh_initial_value_object_count"] == 2
    assert receipt["fresh_baseline_labor_object_count"] == 2
    assert receipt["pass"] is True


def test_same_support_grid_precision_distance_matches_accepted_behavior() -> None:
    x1 = np.array([-2.0, 0.0, 20.0])
    x2 = np.array([-2.0, 1.0, 20.0])
    m1 = np.array([0.1, -0.02, 0.92])
    m2 = np.array([0.2, 0.3, 0.5])
    common = np.union1d(x1, x2)
    expected = np.trapezoid(
        np.abs(np.interp(common, x1, np.cumsum(m1)) - np.interp(common, x2, np.cumsum(m2))),
        common,
    ) / 22.0
    assert finalize.same_support_cdf_distance(x1, m1, x2, m2) == expected


def test_grid_precision_distance_rejects_domain_change() -> None:
    with pytest.raises(ValueError, match="same support"):
        finalize.same_support_cdf_distance([0.0, 1.0], [0.5, 0.5], [0.0, 2.0], [0.5, 0.5])


def test_decision_must_be_one_of_two_preregistered_terminals() -> None:
    assert finalize.validate_decision("J160_LIQUID_GRID_PRECISION_PROVISIONALLY_STABILIZED")
    assert finalize.validate_decision("J160_LIQUID_GRID_PRECISION_NOT_STABILIZED")
    assert finalize.validate_decision(
        "J160_LIQUID_GRID_PRECISION_UNRESOLVED__I40_HJB_INVALID_OPERATOR"
    )
    with pytest.raises(ValueError, match="preregistered"):
        finalize.validate_decision("PASS")


def test_runner_has_exact_science_budgets_and_no_forbidden_route_strings() -> None:
    ledger = run.empty_ledger()
    assert ledger["hjb_budget"] == 2
    assert ledger["kfe_budget"] == 2
    assert ledger["scientific_retries"] == 0
    assert ledger["engineering_retries"] == 1
    assert all(ledger[key] == 0 for key in run.FORBIDDEN_LEDGER_KEYS)
    text = run.Path(run.__file__).read_text(encoding="utf-8")
    for forbidden in ("I=160", "J=320", "matlab.engine", "solve_multi_province", "warm_start="):
        assert forbidden not in text
