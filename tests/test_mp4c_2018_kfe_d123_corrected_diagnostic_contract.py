import numpy as np
import pytest
from scipy import sparse
from pathlib import Path

from ch5_two_asset_hank.corrected_diagnostic import (
    ClosedFaceOutwardDriftError,
    CorrectedDiagnosticGrid,
    assemble_consumed_drift_generator,
    assess_state_constraints,
    check_transfer_kkt,
    load_saved_control_set,
    regularized_adjustment_cost,
    regularized_adjustment_cost_subgradient,
    regularized_scale,
    require_state_constraints,
)


def tiny_grid() -> CorrectedDiagnosticGrid:
    return CorrectedDiagnosticGrid(
        b=np.array([-2.0, -0.5, 1.0]),
        a=np.array([0.0, 0.25, 2.0]),
        z=np.array([0.8, 1.2]),
    )


def test_d1_dual_upper_corner_rejects_both_outward_drifts() -> None:
    grid = tiny_grid()
    mu_b = np.zeros(grid.shape)
    mu_a = np.zeros(grid.shape)
    mu_b[-1, -1, 0] = 0.2
    mu_a[-1, -1, 0] = 0.3

    assessment = assess_state_constraints(grid, mu_b=mu_b, mu_a=mu_a)

    assert not assessment.feasible
    assert {(v.axis, v.side) for v in assessment.violations} == {
        ("b", "upper"),
        ("a", "upper"),
    }
    assert {v.boundary_kind for v in assessment.violations} == {
        "artificial_upper_state_constraint"
    }
    with pytest.raises(ClosedFaceOutwardDriftError) as caught:
        require_state_constraints(grid, mu_b=mu_b, mu_a=mu_a)
    assert len(caught.value.assessment.violations) == 2


def test_d1_inward_and_tangent_faces_pass_with_lower_bounds_distinct() -> None:
    grid = tiny_grid()
    mu_b = np.zeros(grid.shape)
    mu_a = np.zeros(grid.shape)
    mu_b[0, :, :] = 0.1
    mu_b[-1, :, :] = -0.2
    mu_a[:, 0, :] = 0.3
    mu_a[:, -1, :] = 0.0

    assessment = require_state_constraints(grid, mu_b=mu_b, mu_a=mu_a)

    assert assessment.feasible
    by_face = {(face.axis, face.side): face for face in assessment.faces}
    assert by_face[("b", "lower")].boundary_kind == "economic_lower_bound"
    assert by_face[("a", "upper")].boundary_kind == "artificial_upper_state_constraint"
    assert by_face[("b", "upper")].inward_count == grid.a.size * grid.z.size
    assert by_face[("a", "upper")].tangent_count == grid.b.size * grid.z.size


def test_d2_consumed_drift_generator_is_conservative_and_coordinate_exact() -> None:
    grid = tiny_grid()
    mu_b = np.zeros(grid.shape)
    mu_a = np.zeros(grid.shape)
    mu_b[0, :, :] = 0.2
    mu_b[1, :, :] = 0.6
    mu_b[2, :, :] = -0.4
    mu_a[:, 0, :] = 0.5
    mu_a[:, 1, :] = -0.3
    mu_a[:, 2, :] = -0.1

    z_generator = np.array([[-0.4, 0.4], [0.2, -0.2]])
    result = assemble_consumed_drift_generator(
        grid, mu_b=mu_b, mu_a=mu_a, z_generator=z_generator
    )

    off_diagonal = result.q - sparse.diags(result.q.diagonal(), format="csr")
    assert np.min(off_diagonal.data, initial=0.0) >= 0.0
    assert result.max_abs_q_one <= result.arithmetic_tolerance
    assert result.diagonal_construction_error == 0.0
    b_values = np.broadcast_to(grid.b[:, None, None], grid.shape).ravel(order="F")
    a_values = np.broadcast_to(grid.a[None, :, None], grid.shape).ravel(order="F")
    np.testing.assert_allclose(result.q @ b_values, mu_b.ravel(order="F"), atol=1e-15)
    np.testing.assert_allclose(result.q @ a_values, mu_a.ravel(order="F"), atol=1e-15)


def test_d2_rejects_any_outward_closed_face_input_before_assembly() -> None:
    grid = tiny_grid()
    mu_b = np.zeros(grid.shape)
    mu_a = np.zeros(grid.shape)
    mu_b[-1, 1, 0] = np.nextafter(0.0, 1.0)

    with pytest.raises(ClosedFaceOutwardDriftError):
        assemble_consumed_drift_generator(grid, mu_b=mu_b, mu_a=mu_a)


@pytest.mark.parametrize(
    ("a", "expected_scale"),
    [(0.0, 0.5), (0.25, 0.5), (0.5, 0.5), (2.0, 2.0)],
)
def test_d3_cost_derivative_and_kkt_share_regularized_scale(
    a: float, expected_scale: float
) -> None:
    chi_0 = 0.1
    chi_1 = 2.0
    a_bar = 0.5
    assert regularized_scale(a, a_bar=a_bar) == expected_scale
    positive = regularized_adjustment_cost_subgradient(
        0.2, a, chi_0=chi_0, chi_1=chi_1, a_bar=a_bar
    )
    negative = regularized_adjustment_cost_subgradient(
        -0.2, a, chi_0=chi_0, chi_1=chi_1, a_bar=a_bar
    )
    assert positive.point == pytest.approx(chi_0 + chi_1 * 0.2 / expected_scale)
    assert negative.point == pytest.approx(-chi_0 - chi_1 * 0.2 / expected_scale)
    assert regularized_adjustment_cost(
        0.2, a, chi_0=chi_0, chi_1=chi_1, a_bar=a_bar
    ) == pytest.approx(chi_0 * 0.2 + chi_1 * 0.2**2 / (2.0 * expected_scale))
    qa = 2.0 * (1.0 + positive.point)
    assert check_transfer_kkt(
        d=0.2,
        a=a,
        q_a=qa,
        q_b=2.0,
        chi_0=chi_0,
        chi_1=chi_1,
        a_bar=a_bar,
    ).satisfied
    qa_negative = 2.0 * (1.0 + negative.point)
    assert check_transfer_kkt(
        d=-0.2,
        a=a,
        q_a=qa_negative,
        q_b=2.0,
        chi_0=chi_0,
        chi_1=chi_1,
        a_bar=a_bar,
    ).satisfied


def test_d3_zero_transfer_uses_kink_interval_without_floor_or_cap() -> None:
    result = check_transfer_kkt(
        d=0.0,
        a=0.0,
        q_a=2.0,
        q_b=2.0,
        chi_0=0.1,
        chi_1=2.0,
        a_bar=0.5,
    )
    assert result.satisfied
    assert result.target_interval == pytest.approx((1.8, 2.2))
    assert result.residual == 0.0
    outside = check_transfer_kkt(
        d=0.0,
        a=0.0,
        q_a=2.4,
        q_b=2.0,
        chi_0=0.1,
        chi_1=2.0,
        a_bar=0.5,
    )
    assert not outside.satisfied
    assert outside.residual == pytest.approx(0.2)
    with pytest.raises(ValueError, match="no derivative floor"):
        check_transfer_kkt(
            d=0.0,
            a=0.0,
            q_a=1.0,
            q_b=0.0,
            chi_0=0.1,
            chi_1=2.0,
            a_bar=0.5,
        )


def test_saved_control_set_is_exact_and_rejected_without_silent_repair() -> None:
    repository = Path(__file__).resolve().parents[1]
    evidence = repository / "reports/call725_boundary_generator_repair_spec_20260907"

    snapshots = load_saved_control_set(
        evidence / "snapshots.json", evidence / "consumed_inputs.json"
    )

    assert len(snapshots) == 14
    assert len({snapshot.provenance.sha256 for snapshot in snapshots}) == 14
    for snapshot in snapshots:
        assessment = assess_state_constraints(
            snapshot.grid, mu_b=snapshot.mu_b, mu_a=snapshot.mu_a
        )
        assert not assessment.feasible, snapshot.provenance.snapshot_id
        assert {violation.side for violation in assessment.violations} == {"upper"}
        with pytest.raises(ClosedFaceOutwardDriftError):
            assemble_consumed_drift_generator(
                snapshot.grid, mu_b=snapshot.mu_b, mu_a=snapshot.mu_a
            )
