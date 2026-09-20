from __future__ import annotations

from pathlib import Path

import pytest

from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import FailClosed
from ch5_two_asset_hank.corrected_diagnostic.raw_ra0_safety_panel import (
    FROZEN_SCALARS,
    PANEL,
    _accepted_checkpoint11,
    _check_ledger,
    _new_ledger,
    _point_inputs,
    derive_panel,
)


REPOSITORY = Path(__file__).resolve().parents[1]


def test_accepted_csv_independently_reproduces_preregistered_path_b_panel() -> None:
    receipt = derive_panel(
        REPOSITORY
        / "docs/evidence/ch5_mp4c_k1a_payoff_return_reaudit/"
        "static_no_feedback_payoff_counterfactual.csv"
    )

    assert receipt["status"] == "PASS"
    assert receipt["path_b_rows"] == 775
    assert receipt["median_sorted_zero_based_index"] == 387
    assert [row["label"] for row in receipt["points"]] == ["LOW", "MEDIAN", "HIGH"]
    assert [row["r_a_decimal"] for row in receipt["points"]] == [row[4] for row in PANEL]


def test_exact_checkpoint11_load_binds_value_policy_utility_q_and_grid() -> None:
    accepted = _accepted_checkpoint11(REPOSITORY)

    assert accepted["manifest_entry_count"] == 819
    assert all(accepted["checks"].values())
    assert len(accepted["rows"]) == 800
    assert accepted["value"].shape == (20, 20, 2)
    assert accepted["q"].shape == (800, 800)


def test_panel_inputs_change_only_r_a_and_preserve_raw_value() -> None:
    accepted = _accepted_checkpoint11(REPOSITORY)
    inputs = _point_inputs(accepted, float(PANEL[-1][4]))

    assert inputs.scalars["r_a"] == float(PANEL[-1][4])
    assert inputs.scalars["r_a"] > 0.09
    assert {key: value for key, value in inputs.scalars.items() if key != "r_a"} == {
        key: value for key, value in FROZEN_SCALARS.items() if key != "r_a"
    }


def test_task_ledger_allows_exact_panel_budget_and_fails_above_it() -> None:
    ledger = _new_ledger()
    ledger.update(
        new_corrected_policy_maps=3,
        selector_evaluations=2400,
        d2_assemblies=3,
        direct_hjb_solves=3,
        hjb_updates=3,
        complete_one_step_panel_evaluations=3,
        scalar_root_invocations=933_768,
        interior_z_root_invocations=855_360,
        interior_a_switching_root_invocations=2400,
        joint_switching_root_invocations=2400,
    )
    _check_ledger(ledger)

    ledger["hjb_updates"] = 4
    with pytest.raises(FailClosed):
        _check_ledger(ledger)
