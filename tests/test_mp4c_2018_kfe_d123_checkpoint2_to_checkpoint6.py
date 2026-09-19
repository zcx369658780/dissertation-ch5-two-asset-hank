from pathlib import Path

import numpy as np
import pytest

from ch5_two_asset_hank.corrected_diagnostic.checkpoint2_to_checkpoint6 import (
    FailClosed,
    _check_task_ledger,
    _load_accepted_checkpoint2,
    _new_ledger,
    classify_checkpoint,
    detect_authorized_approximate_cycle,
)
from ch5_two_asset_hank.corrected_diagnostic.option_a_step import bind_option_a_inputs


def test_checkpoint_gate_order_is_primary_then_exact_then_approximate() -> None:
    converged = classify_checkpoint(
        checkpoint=4,
        bellman_residual=1.0e-8,
        value_change=1.0e-7,
        exact_period=2,
        approximate_cycle={"period": 2},
    )
    assert converged == "HJB_CONVERGENCE_CANDIDATE__TERMINAL_GATE_NOT_RUN"

    exact = classify_checkpoint(
        checkpoint=4,
        bellman_residual=np.nextafter(1.0e-8, np.inf),
        value_change=1.0e-7,
        exact_period=2,
        approximate_cycle={"period": 2},
    )
    assert exact == "EXACT_CYCLE"

    approximate = classify_checkpoint(
        checkpoint=4,
        bellman_residual=1.0,
        value_change=1.0,
        exact_period=None,
        approximate_cycle={"period": 2},
    )
    assert approximate == "APPROXIMATE_PERIOD_2_CYCLE"


def test_checkpoint_six_is_terminal_bounded_evidence() -> None:
    assert (
        classify_checkpoint(
            checkpoint=6,
            bellman_residual=1.0,
            value_change=1.0,
            exact_period=None,
            approximate_cycle=None,
        )
        == "COMPLETE_CHECKPOINT6_NONCONVERGED__TERMINAL_GATE_NOT_RUN"
    )


def test_approximate_cycle_windows_start_only_at_checkpoint_four_and_six() -> None:
    period_two_from_v0 = [
        np.array([0.0]),
        np.array([1.0]),
        np.array([0.0]),
        np.array([1.0]),
    ]
    assert detect_authorized_approximate_cycle(period_two_from_v0, checkpoint=3) is None

    period_two_from_v1 = [
        np.array([9.0]),
        np.array([0.0]),
        np.array([1.0]),
        np.array([0.0]),
        np.array([1.0]),
    ]
    result = detect_authorized_approximate_cycle(period_two_from_v1, checkpoint=4)
    assert result is not None and result["period"] == 2

    period_three_from_v1 = [
        np.array([9.0]),
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
    ]
    result = detect_authorized_approximate_cycle(period_three_from_v1, checkpoint=6)
    assert result is not None and result["period"] == 3
    assert (
        classify_checkpoint(
            checkpoint=5,
            bellman_residual=1.0,
            value_change=1.0,
            exact_period=None,
            approximate_cycle=None,
        )
        is None
    )


def test_task_ledger_enforces_four_update_and_map_ceiling() -> None:
    ledger = _new_ledger()
    ledger.update(
        direct_hjb_solves=4,
        new_corrected_policy_maps=4,
        selector_evaluations=3200,
        d2_assemblies=4,
        checkpoint_evaluations=4,
    )
    _check_task_ledger(ledger)
    ledger["direct_hjb_solves"] = 5
    with pytest.raises(FailClosed):
        _check_task_ledger(ledger)


def test_accepted_checkpoint2_binding_is_exact_and_does_not_remap_v2() -> None:
    repository = Path(__file__).resolve().parents[1]
    seed = Path(
        r"D:\ProjectTemp\ch5-mp4c-2018-call725-matlab-termination-replay-after-path-recertification-20260904-001\hjb100_initialization.mat"
    )
    binding = Path(
        r"D:\ProjectTemp\ch5-mp4c-2018-call725-first-iteration-scalar-binding-repair-20260904-001\call725_first_iteration_scalar_binding.json"
    )
    inputs = bind_option_a_inputs(seed, binding)

    accepted = _load_accepted_checkpoint2(repository, inputs)

    assert accepted["identities"]["v2"] == (
        "A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1"
    )
    assert accepted["identities"]["p2"] == (
        "EBCBABC0593EF163D2E7FA300F6FFEB6E3C187D232D4CCEA5D59AB7180CD1D95"
    )
    assert accepted["identities"]["u2"] == (
        "C222F4B147F48EA177A28AAF289F3ED5EA76F531BC08201070DD63698BF98D73"
    )
    assert accepted["identities"]["q2"] == (
        "346DBCDA13392DAF6897DC185767B0E7C5961AA76A9AAA686053AEDA33C02F9F"
    )
    assert accepted["identities"]["checkpoint2"] == (
        "71DC6975E814060A4F63961A736E6E9DDF766C51CE4672C3EF777E5E15B80C2C"
    )
    assert len(accepted["p2_rows"]) == 800
    assert accepted["v2_policy_map_rerun"] is False
    assert accepted["q2_assembly_rerun"] is False
