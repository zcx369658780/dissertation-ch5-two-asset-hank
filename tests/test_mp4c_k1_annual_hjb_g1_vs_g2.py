from __future__ import annotations

from types import SimpleNamespace

import numpy as np
import pytest

from ch5_two_asset_hank.multi_province.capital_allocation import CapitalAllocationInputs
from validators.multi_province.k1_annual_hjb_g1_vs_g2.run import (
    ANNUAL_DELTA, ANNUAL_RAW, BOOTSTRAP, PATHS, RETURN_GUARDS,
    annual_model_params, annual_ra0_residual, hjb_consumed_return, select_allocation_payoff,
    wage_boundary_flags,
)
from validators.multi_province.k1_annual_hjb_g1_vs_g2.finalize import route_decision


def inputs() -> CapitalAllocationInputs:
    return CapitalAllocationInputs(np.ones(31), np.ones(31), np.full(31, .1), np.linspace(.02, .09, 31))


def firms():
    return [(SimpleNamespace(ra=.09, ra0=.10 + i / 100), .25) for i in range(31)]


@pytest.mark.parametrize("path_id", PATHS)
def test_turn1_common_bootstrap(path_id: str) -> None:
    mode, source, turn, payoff = select_allocation_payoff(
        path_id=path_id, allocation_turn=1, inputs=inputs(), prior_firms=None)
    assert (mode, source, turn) == (BOOTSTRAP, "accepted_entering_state.ra", None)
    np.testing.assert_array_equal(payoff, inputs().old_firm_return_ra)
    assert hjb_consumed_return(path_id, 1, .50) == (.50, "NOT_APPLIED_BOOTSTRAP")


@pytest.mark.parametrize("path_id", PATHS)
def test_turn2_uses_own_prior_unclipped_ra0(path_id: str) -> None:
    mode, source, turn, payoff = select_allocation_payoff(
        path_id=path_id, allocation_turn=2, inputs=inputs(), prior_firms=firms())
    assert (mode, turn) == (ANNUAL_RAW, 1)
    assert source == "same_path.completed_turn_1.firm.ra0_annual"
    np.testing.assert_array_equal(payoff, [x[0].ra0 for x in firms()])
    assert payoff.max() > .35


@pytest.mark.parametrize("path_id,value,expected,hit", [
    ("G1", -.10, -.05, "LOWER"), ("G1", -.05, -.05, "UNSATURATED"),
    ("G1", .12, .12, "UNSATURATED"), ("G1", .20, .20, "UNSATURATED"),
    ("G1", .50, .20, "UPPER"), ("G2", -.20, -.10, "LOWER"),
    ("G2", -.10, -.10, "UNSATURATED"), ("G2", .25, .25, "UNSATURATED"),
    ("G2", .35, .35, "UNSATURATED"), ("G2", .50, .35, "UPPER"),
])
def test_guard_boundaries(path_id: str, value: float, expected: float, hit: str) -> None:
    assert hjb_consumed_return(path_id, 2, value) == (expected, hit)


def test_g2_restores_variation_between_point20_and_point35() -> None:
    assert hjb_consumed_return("G1", 2, .25) == (.20, "UPPER")
    assert hjb_consumed_return("G2", 2, .25) == (.25, "UNSATURATED")
    assert RETURN_GUARDS == {"G1": (-.05, .20), "G2": (-.10, .35)}


def test_fail_closed_for_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        hjb_consumed_return("U", 2, .1)
    with pytest.raises(ValueError, match="finite"):
        hjb_consumed_return("G2", 2, np.inf)
    with pytest.raises(ValueError, match="unavailable"):
        select_allocation_payoff(path_id="G1", allocation_turn=2, inputs=inputs(), prior_firms=None)
    broken = firms(); broken[0] = (SimpleNamespace(ra=.09, ra0=np.nan), .25)
    with pytest.raises(ValueError, match="finite"):
        select_allocation_payoff(path_id="G2", allocation_turn=2, inputs=inputs(), prior_firms=broken)


def test_annual_calibration_is_exact_and_source_unchanged() -> None:
    source = {"ga": 2., "phi_l": 5., "alphal": 1., "epsilon": 10., "theta": 100.,
              "delta": .025, "istar": .015}
    result = annual_model_params(source)
    assert result["delta"] == ANNUAL_DELTA == .10 and source["delta"] == .025
    assert annual_ra0_residual(.50, .05, .45) == pytest.approx(0.)


def test_route_never_auto_authorizes_unfrozen_materiality_threshold() -> None:
    g1 = [{"hjb_converged_count": 31}, {"hjb_converged_count": 10}]
    assert route_decision(g1, [{"hjb_converged_count": 31}, {"hjb_converged_count": 10}], .25) == (
        "REVIEW_REQUIRED__NO_AUTOMATIC_LONGER_G2_ROUTE")


@pytest.mark.parametrize("value,expected", [
    (.8, (True, False, False)), (1.3, (False, True, False)), (1.0, (False, False, True)),
])
def test_wage_hit_uses_literal_guarded_wjt_equality(value: float, expected: tuple[bool, bool, bool]) -> None:
    assert wage_boundary_flags(value) == expected
    with pytest.raises(ValueError, match="finite"):
        wage_boundary_flags(np.nan)
