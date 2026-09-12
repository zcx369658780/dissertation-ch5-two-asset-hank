from __future__ import annotations

from types import SimpleNamespace

import numpy as np
import pytest

from ch5_two_asset_hank.multi_province.capital_allocation import CapitalAllocationInputs
from ch5_two_asset_hank.multi_province.k1a_runtime_adapter import (
    K1ARuntimeConfig,
    allocate_k1a_capital,
    load_accepted_distance_score,
)
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER
from validators.multi_province.k1_raw_ra0_payoff_bootstrap_safety.run import (
    BOOTSTRAP,
    CONTROL,
    DISTANCE,
    RAW,
    _inputs_with_payoff,
    select_allocation_payoff,
)


def inputs() -> CapitalAllocationInputs:
    return CapitalAllocationInputs(
        np.linspace(1.0, 2.0, 31), np.linspace(10.0, 20.0, 31),
        np.linspace(0.05, 0.3, 31), np.linspace(0.02, 0.09, 31),
    )


def firms() -> list[tuple[SimpleNamespace, float]]:
    return [(SimpleNamespace(ra=0.02 + i / 1000.0, ra0=0.10 + i / 100.0), 0.25) for i in range(31)]


@pytest.mark.parametrize("path_id", ["C", "R"])
@pytest.mark.parametrize("turn", [0, 1])
def test_both_paths_use_identical_clipped_ra_bootstrap(path_id: str, turn: int) -> None:
    source = inputs()
    mode, field, source_turn, payoff = select_allocation_payoff(
        path_id=path_id, allocation_turn=turn, inputs=source, prior_firms=None,
    )
    assert mode == BOOTSTRAP
    assert field == "entering_state.ra"
    assert source_turn is None
    np.testing.assert_array_equal(payoff, source.old_firm_return_ra)


def test_control_turn2_uses_same_path_completed_turn1_used_ra() -> None:
    mode, field, source_turn, payoff = select_allocation_payoff(
        path_id="C", allocation_turn=2, inputs=inputs(), prior_firms=firms(),
    )
    assert (mode, field, source_turn) == (CONTROL, "same_path.completed_turn_1.firm.ra", 1)
    np.testing.assert_array_equal(payoff, [item[0].ra for item in firms()])


def test_raw_turn2_uses_unclipped_same_path_completed_turn1_ra0() -> None:
    mode, field, source_turn, payoff = select_allocation_payoff(
        path_id="R", allocation_turn=2, inputs=inputs(), prior_firms=firms(),
    )
    assert (mode, field, source_turn) == (RAW, "same_path.completed_turn_1.firm.ra0", 1)
    np.testing.assert_array_equal(payoff, [item[0].ra0 for item in firms()])
    assert float(payoff.max()) > 0.09


@pytest.mark.parametrize("path_id", ["C", "R"])
def test_turn2_missing_completed_firm_vector_fails_closed(path_id: str) -> None:
    with pytest.raises(ValueError, match="prior-completed same-path"):
        select_allocation_payoff(path_id=path_id, allocation_turn=2, inputs=inputs(), prior_firms=None)


def test_payoff_switch_preserves_same_S_and_quantities_without_transforming_raw() -> None:
    source = inputs()
    config = K1ARuntimeConfig(PROVINCE_ORDER, load_accepted_distance_score(DISTANCE), 2.0)
    control = allocate_k1a_capital(source, config)
    raw = np.linspace(0.1, 1.0, 31)
    treatment = allocate_k1a_capital(_inputs_with_payoff(source, raw), config)
    np.testing.assert_array_equal(control.network.portfolio_shares_destination_origin,
                                  treatment.network.portfolio_shares_destination_origin)
    np.testing.assert_array_equal(control.kt_supply, treatment.kt_supply)
    np.testing.assert_array_equal(treatment.household_illiquid_return_rah,
                                  raw @ treatment.network.portfolio_shares_destination_origin)


def test_raw_selector_rejects_nonfinite_without_fallback() -> None:
    prior = firms()
    prior[3] = (SimpleNamespace(ra=0.09, ra0=np.nan), 0.25)
    with pytest.raises(ValueError, match="finite"):
        select_allocation_payoff(path_id="R", allocation_turn=2, inputs=inputs(), prior_firms=prior)
