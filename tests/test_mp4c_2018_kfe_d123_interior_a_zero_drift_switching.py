import pytest

from ch5_two_asset_hank.corrected_diagnostic.selector import (
    CellDerivatives,
    CorrectedSelectorCell,
    CorrectedSelectorParameters,
    SelectorBudget,
    select_constrained_policy,
)


def _parameters() -> CorrectedSelectorParameters:
    return CorrectedSelectorParameters(
        gamma_c=2.0,
        phi=5.0,
        labor_weight=1.0,
        chi_0=0.1,
        chi_1=2.0,
        a_bar=1.0e-6,
    )


def _cell100() -> CorrectedSelectorCell:
    return CorrectedSelectorCell(
        cell_id="v002_f0100_b000_a005_z000_interior_a_switching",
        b=-2.0,
        a=2.6315789473684212,
        z=0.8,
        b_lower=-2.0,
        b_upper=5.0,
        a_lower=0.0,
        a_upper=10.0,
        net_wage=12.783312529860462,
        effective_r_b=0.09000000000000001,
        transfer_income=0.1,
        effective_r_a=0.08999994552589044,
        derivatives=CellDerivatives(
            p_b_backward=0.012333311206716577,
            p_b_forward=0.012333311206716577,
            p_a_backward=0.00903315440190679,
            p_a_forward=0.008957007194295222,
        ),
    )


def _budget() -> SelectorBudget:
    return SelectorBudget(
        max_selector_evaluations=1,
        max_root_invocations=32,
        max_interior_z_root_invocations=8,
        max_interior_a_switching_root_invocations=8,
    )


def test_cell100_adds_one_legal_interior_a_zero_drift_switching_policy() -> None:
    result = select_constrained_policy(_cell100(), _parameters(), budget=_budget())

    switching = [
        candidate
        for candidate in result.candidates
        if candidate.interior_a_switching_receipt is not None
    ]
    assert len(switching) == 1
    candidate = switching[0]
    receipt = candidate.interior_a_switching_receipt
    assert receipt is not None
    assert receipt.strict_crossing
    assert receipt.endpoint_drifts["backward"] == pytest.approx(
        0.00670682022114244
    )
    assert receipt.endpoint_drifts["forward"] == pytest.approx(
        -0.0005429159000894801
    )
    assert receipt.d_z == pytest.approx(-0.23684196191023801)
    assert receipt.transfer_regime == "negative"
    assert receipt.d3_ratio == pytest.approx(0.72000010894821909)
    assert receipt.derivative_interval == pytest.approx(
        (0.008957007194295222, 0.00903315440190679)
    )
    assert receipt.implied_q_b_interval == pytest.approx(
        (0.012440285887428097, 0.012546045881996438)
    )
    assert receipt.root_interval == pytest.approx(receipt.implied_q_b_interval)
    assert receipt.root_endpoint_drifts[0] < 0.0 < receipt.root_endpoint_drifts[1]
    assert candidate.root_status == "ROOT_CONVERGED"
    assert candidate.q_b is not None
    assert receipt.root_interval[0] < candidate.q_b < receipt.root_interval[1]
    assert candidate.q_a is not None
    assert receipt.derivative_interval[0] < candidate.q_a < receipt.derivative_interval[1]
    assert candidate.g_a == 0.0
    assert candidate.g_b == 0.0
    assert candidate.admissible
    assert candidate.d2_assembler_admissible
    assert candidate.transfer_kkt_residual == pytest.approx(0.0, abs=1.0e-15)
    assert candidate.multipliers["lower_b"] >= 0.0
    assert result.selected == candidate
    assert result.outcome == "SELECTED_ADMISSIBLE"
    assert result.interior_a_switching_root_invocations == 1


@pytest.mark.parametrize("boundary_a", [0.0, 10.0])
def test_switching_does_not_trigger_at_an_a_boundary(boundary_a: float) -> None:
    interior = _cell100()
    boundary = CorrectedSelectorCell(
        **{
            **interior.__dict__,
            "cell_id": "a-boundary-no-switch",
            "a": boundary_a,
        }
    )
    result = select_constrained_policy(boundary, _parameters(), budget=_budget())
    assert not any(
        candidate.interior_a_switching_receipt is not None
        for candidate in result.candidates
    )
    assert result.interior_a_switching_root_invocations == 0


@pytest.mark.parametrize("shared_a_shadow", [0.00903315440190679, 0.008957007194295222])
def test_switching_does_not_trigger_without_two_strict_opposed_endpoints(
    shared_a_shadow: float,
) -> None:
    cell = _cell100()
    cell = CorrectedSelectorCell(
        **{
            **cell.__dict__,
            "cell_id": "no-strict-a-crossing",
            "derivatives": CellDerivatives(
                p_b_backward=cell.derivatives.p_b_backward,
                p_b_forward=cell.derivatives.p_b_forward,
                p_a_backward=shared_a_shadow,
                p_a_forward=shared_a_shadow,
            ),
        }
    )
    result = select_constrained_policy(cell, _parameters(), budget=_budget())
    assert not any(
        candidate.interior_a_switching_receipt is not None
        for candidate in result.candidates
    )
    assert result.interior_a_switching_root_invocations == 0


def test_no_candidate_combines_new_a_switching_with_liquid_z_switching() -> None:
    result = select_constrained_policy(_cell100(), _parameters(), budget=_budget())
    assert not any(
        candidate.interior_a_switching_receipt is not None
        and candidate.interior_z_receipt is not None
        for candidate in result.candidates
    )
    assert all(
        candidate.derivative_branches.get("b") != "zero"
        for candidate in result.candidates
        if candidate.interior_a_switching_receipt is not None
    )
