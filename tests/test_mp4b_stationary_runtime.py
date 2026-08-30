from __future__ import annotations

import pytest

from ch5_two_asset_hank.multi_province.stationary_runtime import (
    OnlineStationaryInputs, run_online_stationary,
)
from ch5_two_asset_hank.multi_province.steady_state import SteadyStateConvergenceError
from test_mp3_manual_update_map import _build, _summary


SCENARIOS = (
    "delayed_convergence", "adaptive_updates", "household_veto",
    "ra_boundary_veto", "wage_bound_diagnostic_only",
    "strict_threshold_equality", "max_iteration_exhaustion",
)


@pytest.mark.parametrize("name", SCENARIOS)
def test_online_controller_is_exactly_mp3(name: str) -> None:
    frozen = _build(name)
    batches = frozen.household_batches

    def household_solver(states, iteration):
        assert states is not frozen.initial_provinces or iteration == 1
        return batches[iteration - 1]

    inputs = OnlineStationaryInputs(
        province_order=frozen.province_order,
        initial_provinces=frozen.initial_provinces,
        params=frozen.params,
        phi_destination_origin=frozen.phi_destination_origin,
        migration_wedge_destination_origin=frozen.migration_wedge_destination_origin,
        household_solver=household_solver,
        reg_threshold=frozen.reg_threshold,
        max_iterations=frozen.max_iterations,
        steady_state=frozen.steady_state,
    )
    try:
        actual = run_online_stationary(inputs)
    except SteadyStateConvergenceError as exc:
        actual = exc.result
    try:
        from ch5_two_asset_hank.multi_province.steady_state import run_manual_steady_state
        expected = run_manual_steady_state(frozen)
    except SteadyStateConvergenceError as exc:
        expected = exc.result
    assert _summary(actual) == _summary(expected)


def test_online_runtime_rejects_bad_matrix_before_callback() -> None:
    frozen = _build("adaptive_updates")
    called = False
    def forbidden(states, iteration):
        nonlocal called
        called = True
        return frozen.household_batches[0]
    inputs = OnlineStationaryInputs(
        frozen.province_order, frozen.initial_provinces, frozen.params,
        frozen.phi_destination_origin[:-1], frozen.migration_wedge_destination_origin,
        forbidden, frozen.reg_threshold, frozen.max_iterations, frozen.steady_state,
    )
    with pytest.raises(ValueError, match="wrong shape"):
        run_online_stationary(inputs)
    assert not called
