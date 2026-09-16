import pytest

from ch5_two_asset_hank.corrected_diagnostic.selector import (
    CellDerivatives,
    CorrectedSelectorCell,
    CorrectedSelectorParameters,
    SelectorBudget,
    active_lower_a_zero_kink_shadow,
    select_constrained_policy,
)


def _parameters() -> CorrectedSelectorParameters:
    return CorrectedSelectorParameters(
        gamma_c=2.0,
        phi=1.0,
        labor_weight=1.0,
        chi_0=0.1,
        chi_1=2.0,
        a_bar=1.0e-6,
    )


def _lower_a_cell(*, p_a: float) -> CorrectedSelectorCell:
    return CorrectedSelectorCell(
        cell_id=f"lower-a-zero-kink-{p_a}",
        b=0.0,
        a=0.0,
        z=1.0,
        b_lower=-1.0,
        b_upper=1.0,
        a_lower=0.0,
        a_upper=1.0,
        net_wage=1.0,
        effective_r_b=0.0,
        transfer_income=0.0,
        effective_r_a=0.1,
        derivatives=CellDerivatives(
            p_b_backward=1.0,
            p_b_forward=1.0,
            p_a_backward=p_a,
            p_a_forward=p_a,
        ),
    )


def _candidate(result, *, active: tuple[str, ...], regime: str):
    return next(
        candidate
        for candidate in result.candidates
        if candidate.active_constraints == active
        and candidate.transfer_branch == regime
    )


def test_active_lower_a_zero_kink_uses_positive_multiplier_interval_minimum() -> None:
    result = select_constrained_policy(
        _lower_a_cell(p_a=0.0),
        _parameters(),
        budget=SelectorBudget(1, 12),
    )

    candidate = _candidate(result, active=("lower_a",), regime="zero_kink")
    receipt = candidate.lower_a_zero_kink_multiplier_receipt
    assert candidate.admissible
    assert candidate.q_b == pytest.approx(1.0)
    assert candidate.q_a == pytest.approx(0.9)
    assert candidate.multipliers["lower_a"] == pytest.approx(0.9)
    assert candidate.d == 0.0
    assert candidate.g_a == 0.0
    assert candidate.transfer_kkt_residual == 0.0
    assert receipt is not None
    assert receipt.raw_kink_interval == pytest.approx((0.9, 1.1))
    assert receipt.raw_multiplier_interval_lower == 0.0
    assert receipt.chosen_q_a == pytest.approx(0.9)
    assert receipt.lambda_a == pytest.approx(0.9)
    assert receipt.marker == "ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_CANONICAL_MIN"
    slack = _candidate(result, active=(), regime="zero_kink")
    assert (
        candidate.c,
        candidate.l,
        candidate.d,
        candidate.cost,
        candidate.g_b,
        candidate.g_a,
        candidate.utility,
        candidate.hamiltonian,
    ) == pytest.approx(
        (
            slack.c,
            slack.l,
            slack.d,
            slack.cost,
            slack.g_b,
            slack.g_a,
            slack.utility,
            slack.hamiltonian,
        )
    )


def test_active_lower_a_zero_kink_keeps_p_a_when_already_inside_interval() -> None:
    result = select_constrained_policy(
        _lower_a_cell(p_a=1.0),
        _parameters(),
        budget=SelectorBudget(1, 12),
    )

    candidate = _candidate(result, active=("lower_a",), regime="zero_kink")
    receipt = candidate.lower_a_zero_kink_multiplier_receipt
    assert candidate.admissible
    assert candidate.q_a == pytest.approx(1.0)
    assert candidate.multipliers["lower_a"] == 0.0
    assert receipt is not None
    assert receipt.chosen_q_a == pytest.approx(1.0)
    assert receipt.lambda_a == 0.0


def test_active_lower_a_zero_kink_empty_intersection_fails_closed() -> None:
    result = select_constrained_policy(
        _lower_a_cell(p_a=1.2),
        _parameters(),
        budget=SelectorBudget(1, 12),
    )

    candidate = _candidate(result, active=("lower_a",), regime="zero_kink")
    receipt = candidate.lower_a_zero_kink_multiplier_receipt
    assert not candidate.admissible
    assert candidate.rejection_reasons == (
        "ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERSECTION_EMPTY",
    )
    assert receipt is not None
    assert not receipt.intersection_nonempty
    assert receipt.chosen_q_a is None
    assert receipt.lambda_a is None
    assert receipt.marker == "ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_EMPTY"


def test_slack_lower_a_zero_kink_remains_unrepaired_with_zero_multiplier() -> None:
    result = select_constrained_policy(
        _lower_a_cell(p_a=0.0),
        _parameters(),
        budget=SelectorBudget(1, 12),
    )

    candidate = _candidate(result, active=(), regime="zero_kink")
    assert not candidate.admissible
    assert candidate.q_a == 0.0
    assert candidate.multipliers["lower_a"] == 0.0
    assert candidate.lower_a_zero_kink_multiplier_receipt is None
    assert candidate.rejection_reasons == ("TRANSFER_KKT_RESIDUAL",)


def test_upper_a_and_nonzero_transfer_active_branches_are_unchanged() -> None:
    upper = CorrectedSelectorCell(
        cell_id="upper-a-negative-transfer",
        b=0.0,
        a=1.0,
        z=1.0,
        b_lower=-1.0,
        b_upper=1.0,
        a_lower=0.0,
        a_upper=1.0,
        net_wage=1.0,
        effective_r_b=0.0,
        transfer_income=0.0,
        effective_r_a=0.1,
        derivatives=CellDerivatives(1.0, 1.0, 1.0, 1.0),
    )
    result = select_constrained_policy(
        upper,
        _parameters(),
        budget=SelectorBudget(1, 12),
    )

    negative = _candidate(result, active=("upper_a",), regime="negative")
    zero_kink = _candidate(result, active=("upper_a",), regime="zero_kink")
    assert negative.q_a == pytest.approx(0.7)
    assert negative.d == pytest.approx(-0.1)
    assert negative.lower_a_zero_kink_multiplier_receipt is None
    assert zero_kink.rejection_reasons == ("ACTIVE_A_EQUALITY_NOT_ZERO_KINK",)
    assert zero_kink.lower_a_zero_kink_multiplier_receipt is None


def test_historical_option_a_cell_zero_interval_is_nonempty_without_selector_call() -> None:
    receipt = active_lower_a_zero_kink_shadow(
        p_a=0.0,
        q_b=0.023046602641887657,
        chi_0=0.1,
    )

    assert receipt.raw_kink_interval == pytest.approx(
        (0.020741942377698892, 0.025351262906076425)
    )
    assert receipt.intersection_nonempty
    assert receipt.chosen_q_a == pytest.approx(0.020741942377698892)
    assert receipt.lambda_a == pytest.approx(0.020741942377698892)
