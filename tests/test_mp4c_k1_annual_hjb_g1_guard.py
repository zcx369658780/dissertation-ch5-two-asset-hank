from __future__ import annotations

from types import SimpleNamespace

import numpy as np
import pytest

from ch5_two_asset_hank.multi_province.capital_allocation import CapitalAllocationInputs
from validators.multi_province.k1_annual_hjb_g1_guard.run import (
    ANNUAL_DELTA,
    ANNUAL_RAW,
    BOOTSTRAP,
    RETURN_GUARD,
    annual_model_params,
    annual_ra0_residual,
    hjb_consumed_return,
    select_allocation_payoff,
)


def inputs() -> CapitalAllocationInputs:
    return CapitalAllocationInputs(np.ones(31), np.ones(31), np.full(31, 0.1), np.linspace(0.02, 0.09, 31))


def firms():
    return [(SimpleNamespace(ra=0.09, ra0=0.10 + i / 100.0), 0.25) for i in range(31)]


@pytest.mark.parametrize("path_id", ["U", "G1"])
def test_turn1_is_common_accepted_bootstrap(path_id: str) -> None:
    mode, source, turn, payoff = select_allocation_payoff(
        path_id=path_id, allocation_turn=1, inputs=inputs(), prior_firms=None,
    )
    assert (mode, source, turn) == (BOOTSTRAP, "accepted_entering_state.ra", None)
    np.testing.assert_array_equal(payoff, inputs().old_firm_return_ra)


@pytest.mark.parametrize("path_id", ["U", "G1"])
def test_turn2_uses_own_prior_completed_unclipped_annual_ra0(path_id: str) -> None:
    mode, source, turn, payoff = select_allocation_payoff(
        path_id=path_id, allocation_turn=2, inputs=inputs(), prior_firms=firms(),
    )
    assert (mode, turn) == (ANNUAL_RAW, 1)
    assert source.endswith("completed_turn_1.firm.ra0_annual")
    np.testing.assert_array_equal(payoff, [item[0].ra0 for item in firms()])
    assert payoff.max() > 0.20


def test_nonbootstrap_missing_or_nonfinite_ra0_fails_closed() -> None:
    with pytest.raises(ValueError, match="unavailable"):
        select_allocation_payoff(path_id="U", allocation_turn=2, inputs=inputs(), prior_firms=None)
    broken = firms()
    broken[0] = (SimpleNamespace(ra=0.09, ra0=np.nan), 0.25)
    with pytest.raises(ValueError, match="finite"):
        select_allocation_payoff(path_id="G1", allocation_turn=2, inputs=inputs(), prior_firms=broken)


def test_annual_delta_override_is_exact_and_other_params_unchanged() -> None:
    source = {"ga": 2.0, "phi_l": 5.0, "alphal": 1.0, "epsilon": 10.0, "theta": 100.0,
              "delta": 0.025, "istar": 0.015}
    result = annual_model_params(source)
    assert result["delta"] == ANNUAL_DELTA == 0.10
    assert source["delta"] == 0.025
    assert {key: value for key, value in result.items() if key != "delta"} == {
        key: value for key, value in source.items() if key != "delta"
    }


def test_annual_ra0_receipt_does_not_retain_point025_residual() -> None:
    assert annual_ra0_residual(0.50, 0.05, 0.45) == pytest.approx(0.0)
    assert annual_ra0_residual(0.50, 0.05, 0.46) == pytest.approx(0.01)


@pytest.mark.parametrize("value,expected,hit", [
    (-0.10, -0.05, "LOWER"), (-0.05, -0.05, "UNSATURATED"),
    (0.12, 0.12, "UNSATURATED"), (0.20, 0.20, "UNSATURATED"), (0.50, 0.20, "UPPER"),
])
def test_g1_guard_applies_only_at_hjb_interface_from_turn2(value: float, expected: float, hit: str) -> None:
    consumed, observed = hjb_consumed_return("G1", 2, value)
    assert (consumed, observed) == (expected, hit)
    assert RETURN_GUARD == (-0.05, 0.20)


def test_turn1_and_unguarded_path_do_not_apply_return_guard() -> None:
    assert hjb_consumed_return("G1", 1, 0.50) == (0.50, "NOT_APPLIED_BOOTSTRAP")
    assert hjb_consumed_return("U", 5, 0.50) == (0.50, "UNGUARDED")


def test_invalid_path_and_nonfinite_return_fail_closed() -> None:
    with pytest.raises(ValueError):
        hjb_consumed_return("G2", 2, 0.1)
    with pytest.raises(ValueError, match="finite"):
        hjb_consumed_return("G1", 2, np.inf)
