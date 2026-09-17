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


def _v2_cell100() -> CorrectedSelectorCell:
    return CorrectedSelectorCell(
        cell_id="v002_f0100_b000_a005_z000_regression",
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
        max_root_invocations=16,
        max_interior_z_root_invocations=8,
    )


def _accepted_upper_b_cell10() -> CorrectedSelectorCell:
    return CorrectedSelectorCell(
        cell_id="accepted-upper-b-cell10-regression",
        b=5.0,
        a=9.473684210526315,
        z=0.8,
        b_lower=-2.0,
        b_upper=5.0,
        a_lower=0.0,
        a_upper=10.0,
        net_wage=12.783312529860462,
        effective_r_b=0.02,
        transfer_income=0.1,
        effective_r_a=0.08446761179431557,
        derivatives=CellDerivatives(
            p_b_backward=0.019561551438254172,
            p_b_forward=0.019561551438254172,
            p_a_backward=0.00814619404677024,
            p_a_forward=-0.016278031249598923,
        ),
    )


def test_v2_cell100_represents_both_active_lower_b_negative_a_directions() -> None:
    result = select_constrained_policy(_v2_cell100(), _parameters(), budget=_budget())

    active_negative = [
        candidate
        for candidate in result.candidates
        if candidate.active_constraints == ("lower_b",)
        and candidate.transfer_branch == "negative"
    ]
    assert [candidate.derivative_branches["a"] for candidate in active_negative] == [
        "backward",
        "forward",
    ]
    assert len(result.candidates) == 8
    assert all(candidate.root_invoked for candidate in active_negative)
    assert result.root_invocations == 4
    assert result.interior_z_root_invocations == 0
    assert not any(candidate.interior_z_receipt for candidate in result.candidates)
    active_positive = next(
        candidate
        for candidate in result.candidates
        if candidate.active_constraints == ("lower_b",)
        and candidate.transfer_branch == "positive"
    )
    assert active_positive.root_status == "ROOT_FAILURE_NO_UNIQUE_BRACKET"
    assert active_positive.q_b is None


def test_upper_b_negative_screen_retains_accepted_multiplier_domain_behavior() -> None:
    result = select_constrained_policy(
        _accepted_upper_b_cell10(), _parameters(), budget=_budget()
    )

    active_negative = [
        candidate
        for candidate in result.candidates
        if candidate.active_constraints == ("upper_b",)
        and candidate.transfer_branch == "negative"
    ]
    assert [candidate.derivative_branches["a"] for candidate in active_negative] == [
        "backward"
    ]
    assert active_negative[0].root_status == "ROOT_CONVERGED"
    assert active_negative[0].q_b is not None
    assert active_negative[0].q_b <= _accepted_upper_b_cell10().derivatives.p_b_backward
