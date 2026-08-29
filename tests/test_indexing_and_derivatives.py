import numpy as np

from ch5_two_asset_hank.contracts import GridSpec
from ch5_two_asset_hank.derivatives import compute_derivatives
from ch5_two_asset_hank.indexing import canonical_index, flatten, inverse_index, matlab_to_canonical, unflatten


def grid():
    return GridSpec(np.array([0.0, 1.0, 2.0]), np.array([-1.0, 0.0, 1.0]), np.array([0.5, 1.0]), -1.0)


def test_a_fast_fortran_round_trip_and_matlab_permutation():
    shape = (3, 2, 2)
    values = np.arange(12.0).reshape(shape, order="F")
    assert canonical_index(2, 1, 1, shape) == 11
    assert inverse_index(7, shape) == (1, 0, 1)
    np.testing.assert_array_equal(unflatten(flatten(values, shape), shape), values)
    matlab = np.transpose(values, (1, 0, 2))
    np.testing.assert_array_equal(matlab_to_canonical(matlab), values)


def test_linear_function_has_exact_interior_and_one_sided_derivatives():
    spec = grid()
    value = 2.0 * spec.a[:, None, None] + 3.0 * spec.b[None, :, None] + 0.0 * spec.z[None, None, :]
    derivatives = compute_derivatives(value, spec)
    np.testing.assert_allclose(derivatives.a_forward[:-1], 2.0)
    np.testing.assert_allclose(derivatives.a_backward[1:], 2.0)
    np.testing.assert_allclose(derivatives.b_forward[:, :-1], 3.0)
    np.testing.assert_allclose(derivatives.b_backward[:, 1:], 3.0)
    assert not derivatives.a_backward_valid[0].any()
    assert not derivatives.b_forward_valid[:, -1].any()
