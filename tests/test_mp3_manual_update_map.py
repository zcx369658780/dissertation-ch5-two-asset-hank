from __future__ import annotations

import ast
import copy
import json
from pathlib import Path

import pytest

from ch5_two_asset_hank.multi_province import (
    SOURCE_MAX_ITERATIONS,
    ManualSteadyStateInputs,
    PreFrozenHouseholdOutputBatch,
    SteadyStateConvergenceError,
    run_manual_steady_state,
)
from validators.multi_province.mp1_fixture_arithmetic import load_fixture as load_mp1
from validators.multi_province.mp3_update_map_arithmetic import (
    evaluate_scenario,
    load_fixture as load_mp3,
)
from ch5_two_asset_hank.multi_province.steady_state import _adapt


ROOT = Path(__file__).resolve().parents[1]
MP3_PATH = ROOT / "tests/fixtures/multi_province/mp3_tiny_multi_turn.json"
PRODUCTION = ROOT / "src/ch5_two_asset_hank/multi_province/steady_state.py"


def _build(name: str, *, drop_last_batch: bool = False) -> ManualSteadyStateInputs:
    fixture = load_mp3(MP3_PATH)
    scenario = fixture["scenarios"][name]
    base = load_mp1(ROOT / fixture["base_fixture"])
    states = copy.deepcopy(base["provinces"])
    for state in states:
        state.update({"Yt": 1.0, "Yt0": 1.0, "ramin": -10.0, "ramax": 10.0,
                      "wjtmin": 0.01, "wjtmax": 10.0})
    for index, override in enumerate(scenario.get("initial_overrides", [])):
        states[index].update(override)
    batches = []
    for spec in scenario["batches"]:
        def vector(key: str, source: str):
            return spec.get(key, [province[source] for province in states])
        batches.append(PreFrozenHouseholdOutputBatch(
            ct=vector("ct", "Ct"), household_lt=vector("household_lt", "Lt"),
            at=vector("at", "At"), bt=vector("bt", "Bt"), at_tax=vector("at_tax", "AtTax"),
            converged=tuple(spec.get("converged", [True] * len(states))),
            diagnostics=tuple({"fixture": name} for _ in states),
        ))
    if drop_last_batch:
        batches = batches[:-1]
    return ManualSteadyStateInputs(
        province_order=tuple(base["province_order"]), initial_provinces=tuple(states),
        params=base["params"], phi_destination_origin=base["phi_mat"],
        migration_wedge_destination_origin=base["sigmau_mat"], household_batches=tuple(batches),
        reg_threshold=scenario["reg_threshold"], max_iterations=scenario["max_iterations"],
        steady_state=scenario.get("steady_state", True),
    )


def _run(name: str):
    try:
        return run_manual_steady_state(_build(name))
    except SteadyStateConvergenceError as exc:
        return exc.result


def _summary(result) -> dict:
    history = []
    for record in result.history:
        history.append({
            "iteration": record.iteration,
            "nk_ratio_gap": record.nk_ratio_gap.tolist(), "yt_gap": record.yt_gap.tolist(),
            "household_converged_count": record.household_converged_count,
            "household_all_converged": record.household_all_converged,
            "ra_upper_count": record.ra_upper_count, "ra_lower_count": record.ra_lower_count,
            "wage_upper_count": record.wage_upper_count, "wage_lower_count": record.wage_lower_count,
            "converged": record.converged,
            "tkn_ratio_before": record.tkn_ratio_before.tolist(),
            "tkn_ratio_after": record.tkn_ratio_after.tolist(),
            "adaptive_actions": [vars(action) for action in record.adaptive_actions],
            "previous_output_yt": [state["Yt_1"] for state in record.state_before_adaptation],
            "new_output_yt": [state["Yt"] for state in record.state_before_adaptation],
        })
    return {
        "termination_reason": result.termination_reason,
        "iteration_count": result.iteration_count,
        "history": history,
        "final_state": [{key: state[key] for key in ("name", "Zt", "GovInv", "Yt", "Kt", "Lt", "KNratio")}
                        for state in result.final_state],
    }


def _assert_close(actual, expected) -> None:
    if isinstance(expected, dict):
        assert set(actual) == set(expected)
        for key in expected:
            _assert_close(actual[key], expected[key])
    elif isinstance(expected, list):
        assert len(actual) == len(expected)
        for left, right in zip(actual, expected):
            _assert_close(left, right)
    elif isinstance(expected, bool) or isinstance(expected, str) or isinstance(expected, int):
        assert actual == expected
    else:
        assert float(actual) == pytest.approx(float(expected), rel=1e-12, abs=1e-12)


@pytest.mark.parametrize("name", [
    "delayed_convergence", "adaptive_updates", "household_veto", "ra_boundary_veto",
    "wage_bound_diagnostic_only", "strict_threshold_equality", "max_iteration_exhaustion",
])
def test_complete_tiny_fixture_parity(name: str) -> None:
    fixture = load_mp3(MP3_PATH)
    actual = _summary(_run(name))
    expected = evaluate_scenario(fixture, name, ROOT)
    _assert_close(actual, expected)


def test_delayed_convergence_and_snapshot_timing() -> None:
    result = _run("delayed_convergence")
    assert result.converged and result.iteration_count == 9
    assert all(record.household_all_converged for record in result.history)
    assert all(not record.converged for record in result.history[:-1])
    assert result.history[-1].converged
    for previous, current in zip(result.history, result.history[1:]):
        assert current.tkn_ratio_before.tolist() == previous.tkn_ratio_after.tolist()
        assert [state["Yt"] for state in current.state_entering_turn] == [
            state["Yt_1"] for state in current.state_before_adaptation
        ]


def test_independently_frozen_expectation_summary() -> None:
    fixture = load_mp3(MP3_PATH)
    frozen = fixture["frozen_expectations"]
    delayed = _run("delayed_convergence")
    assert delayed.iteration_count == frozen["delayed_convergence"]["iteration_count"]
    assert delayed.termination_reason == frozen["delayed_convergence"]["termination_reason"]
    _assert_close(
        delayed.history[-1].tkn_ratio_before.tolist(),
        frozen["delayed_convergence"]["final_tkn_ratio_before"],
    )
    adaptive = _run("adaptive_updates")
    actions = adaptive.history[0].adaptive_actions
    _assert_close([action.zt_after for action in actions], frozen["adaptive_updates"]["zt_after"])
    assert [action.govinv_action for action in actions] == frozen["adaptive_updates"]["govinv_actions"]
    _assert_close([action.govinv_after for action in actions], frozen["adaptive_updates"]["govinv_after"])
    for name in ("household_veto", "ra_boundary_veto", "wage_bound_diagnostic_only",
                 "strict_threshold_equality", "max_iteration_exhaustion"):
        assert _run(name).termination_reason == frozen[name]["termination_reason"]
    assert _run("household_veto").history[0].household_converged_count == frozen["household_veto"]["household_count"]
    assert _run("ra_boundary_veto").history[0].ra_upper_count == frozen["ra_boundary_veto"]["ra_upper_count"]
    assert _run("wage_bound_diagnostic_only").history[0].wage_upper_count == frozen["wage_bound_diagnostic_only"]["wage_upper_count"]
    assert _run("max_iteration_exhaustion").iteration_count == frozen["max_iteration_exhaustion"]["iteration_count"]


def test_adaptive_rules_and_within_turn_snapshot_boundary() -> None:
    record = _run("adaptive_updates").history[0]
    actions = record.adaptive_actions
    assert actions[0].zt_adjusted and actions[0].govinv_action == "LOW_RA_DECREASE_0P9"
    assert not actions[1].zt_adjusted and actions[1].govinv_action == "HIGH_RA_INCREASE_1P1"
    assert not actions[2].zt_adjusted and actions[2].govinv_action == "NONE"
    assert record.state_before_adaptation[0]["Zt"] == actions[0].zt_before
    assert record.state_for_next_turn[0]["Zt"] == actions[0].zt_after
    assert actions[0].govinv_after == pytest.approx(actions[0].govinv_before * 0.9)
    assert actions[1].govinv_after == pytest.approx(actions[1].govinv_before * 1.1)
    assert actions[0].govinv_after != pytest.approx(actions[0].govinv_before * 1.1)
    assert actions[1].govinv_after != pytest.approx(actions[1].govinv_before * 0.9)
    first_state = record.state_before_adaptation[0]
    source_zt = (
        first_state["Yt0"] * first_state["Kt"] ** (-first_state["alpha"])
        * first_state["Lt"] ** (first_state["alpha"] - 1.0)
    )
    wrong_zt = (
        first_state["Yt"] * first_state["Kt"] ** (-first_state["alpha"])
        * first_state["Lt"] ** (first_state["alpha"] - 1.0)
    )
    assert actions[0].zt_after == pytest.approx(source_zt)
    assert actions[0].zt_after != pytest.approx(wrong_zt)
    for index, state in enumerate(record.state_before_adaptation):
        expected = 0.6 * state["KNratio"] + 0.4 * record.tkn_ratio_before[index]
        assert record.tkn_ratio_after[index] == pytest.approx(expected)
    damping_record = _run("delayed_convergence").history[0]
    for index, state in enumerate(damping_record.state_before_adaptation):
        wrong = 0.4 * state["KNratio"] + 0.6 * damping_record.tkn_ratio_before[index]
        assert damping_record.tkn_ratio_after[index] != pytest.approx(wrong)


def test_zt_trigger_is_source_one_percent_not_a_looser_replacement() -> None:
    state = {
        "name": "Synthetic", "Zt": 2.0, "Yt": 1.015, "Yt0": 1.0,
        "Kt": 2.0, "Lt": 3.0, "alpha": 0.4, "GovInv": 0.5,
        "ra": 0.5, "ramin": -1.0, "ramax": 2.0,
    }
    _, actions = _adapt([state], max_nk_gap=0.05, steady_state=True)
    assert actions[0].zt_adjusted  # a wrong 2% trigger would leave Zt unchanged
    unchanged = dict(state, Zt=2.0, Yt=1.005)
    _, below = _adapt([unchanged], max_nk_gap=0.05, steady_state=True)
    assert not below[0].zt_adjusted


def test_convergence_vetoes_strict_inequality_and_wage_diagnostic_only() -> None:
    household = _run("household_veto").history[0]
    assert not household.converged and household.household_converged_count == 2
    assert max(household.nk_ratio_gap) < 10 and max(household.yt_gap) < 10
    assert max(household.nk_ratio_gap) < 10 and max(household.yt_gap) < 10  # omission would accept
    boundary = _run("ra_boundary_veto").history[0]
    assert not boundary.converged and boundary.ra_upper_count == 1
    assert boundary.household_all_converged  # omission of only the ra veto would accept
    wage = _run("wage_bound_diagnostic_only").history[0]
    assert wage.converged and wage.wage_upper_count == 2
    assert not (wage.converged and wage.wage_upper_count == 0)  # invented wage veto disagrees
    strict = _run("strict_threshold_equality").history[0]
    assert max(strict.nk_ratio_gap) == _build("strict_threshold_equality").reg_threshold
    assert not strict.converged
    generic_norm = sum(value * value for value in strict.nk_ratio_gap) ** 0.5
    assert generic_norm != max(strict.nk_ratio_gap)


def test_exhaustion_raises_and_missing_batch_fails_closed() -> None:
    with pytest.raises(SteadyStateConvergenceError) as caught:
        run_manual_steady_state(_build("max_iteration_exhaustion"))
    assert not caught.value.result.converged
    assert caught.value.result.termination_reason == "SOURCE_MAX_ITERATION_EXHAUSTED"
    with pytest.raises(ValueError, match="batch is unavailable"):
        run_manual_steady_state(_build("max_iteration_exhaustion", drop_last_batch=True))


def test_source_default_and_no_forbidden_solver_or_import() -> None:
    assert SOURCE_MAX_ITERATIONS == 500
    tree = ast.parse(PRODUCTION.read_text(encoding="utf-8"), filename=str(PRODUCTION))
    forbidden_imports = {"chapter5_model", "validators", "tests"}
    forbidden_calls = {
        "solve_matlab_faithful_hjb", "solve_stationary_kfe", "solve_household_steady_state",
        "brentq", "newton", "fsolve", "least_squares", "run_transition", "run_dynamics", "run_irf",
    }
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            assert not ({alias.name.split(".")[0] for alias in node.names} & forbidden_imports)
        elif isinstance(node, ast.ImportFrom) and node.module:
            assert node.module.split(".")[0] not in forbidden_imports
        elif isinstance(node, ast.Call):
            name = node.func.id if isinstance(node.func, ast.Name) else (
                node.func.attr if isinstance(node.func, ast.Attribute) else ""
            )
            assert name not in forbidden_calls
    source = PRODUCTION.read_text(encoding="utf-8").lower()
    assert "residual_vector" not in source and "jacobian" not in source
