import inspect

import numpy as np

from ch5_two_asset_hank.corrected_diagnostic import selector
from ch5_two_asset_hank.corrected_diagnostic.contracts import CorrectedDiagnosticGrid
from ch5_two_asset_hank.corrected_diagnostic.generator import (
    assemble_consumed_drift_generator,
)
from ch5_two_asset_hank.corrected_diagnostic.option_a_step import (
    BOUNDARY_ADAPTER_MARKER,
    boundary_cell_derivatives,
    coordinate_action_receipt,
    iter_f_order_indices,
    raw_derivative_fields,
)


def _grid() -> CorrectedDiagnosticGrid:
    return CorrectedDiagnosticGrid(
        b=np.array([-2.0, 0.0, 5.0]),
        a=np.array([0.0, 2.0, 10.0]),
        z=np.array([0.8]),
    )


def test_option_a_derivative_adapter_uses_raw_one_sided_differences() -> None:
    grid = _grid()
    b, a, z = np.meshgrid(grid.b, grid.a, grid.z, indexing="ij")
    value = 3.0 * b + 5.0 * a + 7.0 * z

    fields = raw_derivative_fields(value, grid)

    assert np.allclose(fields.p_b_forward, 3.0)
    assert np.allclose(fields.p_b_backward, 3.0)
    assert np.allclose(fields.p_a_forward, 5.0)
    assert np.allclose(fields.p_a_backward, 5.0)

    lower, lower_markers = boundary_cell_derivatives(fields, (0, 0, 0), grid)
    upper, upper_markers = boundary_cell_derivatives(fields, (2, 2, 0), grid)
    assert np.isclose(lower.p_b_backward, lower.p_b_forward)
    assert np.isclose(lower.p_a_backward, lower.p_a_forward)
    assert np.isclose(upper.p_b_forward, upper.p_b_backward)
    assert np.isclose(upper.p_a_forward, upper.p_a_backward)
    assert lower_markers == {"b": BOUNDARY_ADAPTER_MARKER, "a": BOUNDARY_ADAPTER_MARKER}
    assert upper_markers == {"b": BOUNDARY_ADAPTER_MARKER, "a": BOUNDARY_ADAPTER_MARKER}


def test_option_a_map_indices_are_exact_f_order() -> None:
    indices = list(iter_f_order_indices((3, 2, 2)))

    assert indices[:4] == [(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0)]
    assert indices[-1] == (2, 1, 1)
    assert [
        np.ravel_multi_index(index, (3, 2, 2), order="F") for index in indices
    ] == list(range(12))


def test_selector_boundary_path_statically_consumes_only_inward_slot() -> None:
    inward_source = inspect.getsource(selector._inward_derivative)
    public_source = inspect.getsource(selector.select_constrained_policy)

    assert 'branch = "forward" if face.startswith("lower") else "backward"' in inward_source
    assert 'b_options = [_inward_derivative(cell, "b", faces["b"])]' in public_source
    assert 'a_options = [_inward_derivative(cell, "a", faces["a"])]' in public_source


def test_coordinate_action_receipt_accepts_generator_roundoff_with_fixed_support() -> None:
    grid = _grid()
    mu_b = np.zeros(grid.shape)
    mu_a = np.zeros(grid.shape)
    mu_b[1, 1, 0] = 0.125
    mu_a[1, 1, 0] = -0.25
    generator = assemble_consumed_drift_generator(
        grid, mu_b=mu_b, mu_a=mu_a, z_generator=np.zeros((1, 1))
    )

    receipt = coordinate_action_receipt(generator.q, grid, mu_b, mu_a)

    assert receipt["fixed_pre_outcome_max_row_terms"] == 4
    assert receipt["b"]["passes"]
    assert receipt["a"]["passes"]
    assert receipt["b"]["max_abs_error"] <= receipt["b"]["max_bound"]
    assert receipt["a"]["max_abs_error"] <= receipt["a"]["max_bound"]
