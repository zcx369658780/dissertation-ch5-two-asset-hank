from __future__ import annotations

import ast
from pathlib import Path

import numpy as np
import pytest

from validators.multi_province.g1_residual_govinv_25turn_isolated.run import (
    VERDICT_FAIL,
    VERDICT_PARTIAL,
    build_g1_initial_states,
    classify_completed_path,
)

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "validators/multi_province/g1_residual_govinv_25turn_isolated/run.py"


def test_g1_replaces_only_govinv_and_aligns_below_target() -> None:
    states = (
        {"name": "甲", "GovInv": 10.0, "Yt": 2.0, "ra": 0.09},
        {"name": "乙", "GovInv": 20.0, "Yt": 3.0, "ra": 0.08},
    )
    result, accounting = build_g1_initial_states(states, np.array([10.0, 20.0]), np.array([2.0, 5.0]))
    assert [row["GovInv"] for row in result] == [8.0, 15.0]
    assert np.array_equal(accounting["g1_total"], np.array([10.0, 20.0]))
    for old, new in zip(states, result):
        assert {key: value for key, value in new.items() if key != "GovInv"} == {
            key: value for key, value in old.items() if key != "GovInv"
        }


def test_g1_retains_private_overshoot_and_zeroes_govinv() -> None:
    states = ({"name": "甲", "GovInv": 10.0, "Yt": 2.0}, {"name": "乙", "GovInv": 20.0, "Yt": 3.0})
    result, accounting = build_g1_initial_states(states, np.array([10.0, 20.0]), np.array([12.0, 5.0]))
    assert [row["GovInv"] for row in result] == [0.0, 15.0]
    assert np.array_equal(accounting["g1_total"], np.array([12.0, 20.0]))


def test_g1_state_count_mismatch_fails_closed() -> None:
    with pytest.raises(ValueError, match="counts differ"):
        build_g1_initial_states(({"name": "甲", "GovInv": 1.0},), np.array([1.0, 2.0]), np.array([0.5, 0.5]))


def test_initialization_and_trajectory_are_explicit_separate_stages() -> None:
    source = RUN.read_text(encoding="utf-8")
    assert '"INITIALIZATION_OBSERVATION", 0' in source
    assert '"TRAJECTORY", turn_index' in source
    assert source.index('"INITIALIZATION_OBSERVATION", 0') < source.index("for turn_index in range(1, 26)")


def test_single_process_and_no_retry_guard_precede_science() -> None:
    source = RUN.read_text(encoding="utf-8")
    marker = source.index('write_json(root / "science_started.json"')
    first_household = source.index("init_outputs = _household_pass", marker)
    assert marker < first_household
    assert 'if (root / "science_started.json").exists()' in source
    assert '"scientific_retries": 0' in source


def test_exactly_one_explicit_initial_at_only_allocation() -> None:
    tree = ast.parse(RUN.read_text(encoding="utf-8"))
    execute = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "execute")
    calls = [node for node in ast.walk(execute) if isinstance(node, ast.Call)
             and isinstance(node.func, ast.Name) and node.func.id == "allocate_productive_capital"]
    assert len(calls) == 1


def test_source_faithful_labor_route_only() -> None:
    source = RUN.read_text(encoding="utf-8")
    assert "run_source_faithful_one_turn" in source
    assert "run_origin_preserving_normalized_one_turn" not in source
    assert "reconstruct_origin_preserving_normalized_migration_labor" not in source


def test_historical_controller_is_reused_not_reimplemented() -> None:
    source = RUN.read_text(encoding="utf-8")
    assert "_adapt(before, float(np.max(nk_gap)), True)" in source
    assert "0.6 * float(state[\"KNratio\"]) + 0.4 * tkn_ratio[i]" in source
    assert "GovInv *= " not in source


def test_hjb_and_kfe_continuation_validators_are_reused() -> None:
    source = RUN.read_text(encoding="utf-8")
    assert "g0.validate_hjb_return_for_continuation(hjb)" in source
    assert "g0.validate_kfe_return_for_continuation(kfe)" in source
    assert "g0.all_household_hjb_converged(batch)" in source


def test_budget_has_one_initialization_plus_25_turns() -> None:
    source = RUN.read_text(encoding="utf-8")
    assert "for turn_index in range(1, 26)" in source
    assert '"second_initialization_passes": 0' in source
    assert '"second_trajectory_calls": 0' in source
    assert '"beta_parameter_cells": 0' in source


def test_results_and_production_routes_remain_zero() -> None:
    source = RUN.read_text(encoding="utf-8")
    for field in ("matlab_calls", "steady_state_calls", "ge_calls", "annual_model_calls", "irf_calls", "results_calls"):
        assert f'"{field}": 0' in source


def test_initial_receipt_contains_full_state_and_required_aggregates() -> None:
    source = RUN.read_text(encoding="utf-8")
    for field in ("At_initial", "Bt_initial", "Lt_initial", "Ct_initial", "Kt_supply_initial_MU_beta1",
                  "GovInv0_G0_MU", "GovInv0_G1_MU", "beta_a_star", "outer_turn_1_initial_state_json"):
        assert field in source


def test_required_turn_diagnostics_are_present() -> None:
    source = RUN.read_text(encoding="utf-8")
    for field in ("firm_ra0", "firm_ra_used", "firm_wage_raw", "firm_wage_used", "household_rah",
                  "nk_gap", "yt_gap", "GDP_level_gap", "Zt_before", "Zt_after", "govinv_action",
                  "source_final_predicate"):
        assert field in source


def test_completed_path_classifier_flags_controller_recreated_overshoot() -> None:
    summaries = [{"firm_K_total_over_Ktarget": {"median": 1.0},
                  "controller": {"govinv_action_counts": {}}} for _ in range(25)]
    summaries[-1]["firm_K_total_over_Ktarget"]["median"] = 2.8
    summaries[4]["controller"]["govinv_action_counts"] = {"HIGH_RA_INCREASE_1P1": 10}
    assert classify_completed_path(summaries) == VERDICT_FAIL
    assert classify_completed_path(summaries[:24]) == VERDICT_PARTIAL
