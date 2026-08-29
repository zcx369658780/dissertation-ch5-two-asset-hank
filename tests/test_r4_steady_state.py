import numpy as np

from ch5_two_asset_hank.steady_state import (
    FIXTURE_ID,
    run_frozen_r4_steady_state,
)


def test_frozen_r4_synthetic_endogenous_a_connectivity_steady_state():
    result = run_frozen_r4_steady_state()
    diagnostics = result.diagnostics

    assert diagnostics.fixture_id == FIXTURE_ID
    assert result.primary_grid.shape == (3, 3, 25)
    assert result.buffer_grid.shape == (3, 3, 29)
    assert diagnostics.primary_hjb_residual <= 1e-7
    assert diagnostics.buffer_hjb_residual <= 1e-7
    assert diagnostics.primary_kkt_residual <= 1e-7
    assert diagnostics.buffer_kkt_residual <= 1e-7
    assert diagnostics.primary_generator_row_sum <= 1e-11
    assert diagnostics.buffer_generator_row_sum <= 1e-11
    assert max(
        diagnostics.value_core_change,
        diagnostics.consumption_core_change,
        diagnostics.transfer_core_change,
        diagnostics.labor_core_change,
    ) <= 1e-3
    assert diagnostics.upward_a_edges > 0
    assert diagnostics.downward_a_edges > 0
    assert diagnostics.closed_class_count == 1
    assert len(diagnostics.closed_class_a_indices) >= 2
    assert 1 in diagnostics.closed_class_a_indices
    assert diagnostics.closed_class_a_indices != (2,)
    assert diagnostics.left_nullity == 1
    assert diagnostics.stationarity_sup <= 1e-10
    assert diagnostics.normalization_error <= 1e-10
    assert diagnostics.minimum_mass >= -1e-12
    assert diagnostics.negative_mass_count == 0
    assert diagnostics.mass_density_error <= 1e-10
    assert np.isfinite(diagnostics.a_hh)
    assert np.isfinite(diagnostics.b_hh)
