from __future__ import annotations

import numpy as np
import json
import pytest

from exports import matlab_faithful_two_asset_ha as oracle
from validators.multi_province.corrected_2018_single_turn.run import source_initial_arrays
from validators.multi_province.k1_g1_vs_g2_ha_hjb_instrumented.instrumented_hjb import solve_with_trace
from validators.multi_province.k1_g1_vs_g2_ha_hjb_instrumented.run import (
    checkpoint_cells, focused_parity_gate, write_json,
)
from validators.multi_province.k1_g1_vs_g2_ha_hjb_instrumented.finalize import (
    compare_iterations, differing_names,
)


def fixture():
    grid = oracle.MatlabFaithfulHJBGrid(
        np.array([-2.0, 5.0]),
        np.array([0.0, 10.0]),
        np.array([0.8, 1.3]),
        np.array([[-1 / 3, 1 / 3], [1 / 3, -1 / 3]]),
    )
    params = oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    state = {"rah": 0.2, "rb": 0.02, "rb_gap": 0.07, "Tt": 0.1, "tau": 0.05, "w": 1.1}
    initial, labor = source_initial_arrays(state, grid, params, lambda: None)
    inputs = oracle.HouseholdInputs(0.2, 0.02, 0.05, np.array([1.1]), np.zeros(1), np.ones(1))
    numerics = oracle.MatlabFaithfulHJBNumerics(1000.0, 1e-7, 2, 1e-12)
    return grid, params, inputs, initial, labor, state["Tt"], state["rb_gap"], numerics


def test_instrumentation_is_exactly_scientific_output_neutral() -> None:
    args = fixture()
    expected = oracle.solve_matlab_faithful_hjb(*args)
    actual, trace = solve_with_trace(*args, checkpoint_cells=((1, 1, 0),))
    for field in (
        "value", "initial_value", "consumption", "labor", "transfer", "adjustment_cost",
        "effective_illiquid_return", "mu_a", "mu_b", "utility", "liquid_label", "transfer_label",
    ):
        np.testing.assert_array_equal(getattr(actual, field), getattr(expected, field))
    np.testing.assert_array_equal(actual.operator.full.toarray(), expected.operator.full.toarray())
    np.testing.assert_array_equal(
        actual.post_convergence_operator.full.toarray(), expected.post_convergence_operator.full.toarray()
    )
    assert (actual.iterations, actual.converged, actual.convergence_statistic) == (
        expected.iterations, expected.converged, expected.convergence_statistic
    )
    assert trace["scientific_output_parity_role"] == "OBSERVATION_ONLY"


def test_trace_exposes_real_derivatives_candidates_and_selector_without_nonfinite() -> None:
    result, trace = solve_with_trace(*fixture(), checkpoint_cells=((1, 1, 0),))
    assert len(trace["iterations"]) == result.iterations
    first = trace["iterations"][0]
    assert first["iteration"] == 1
    assert first["value_new"]["nonfinite_count"] == 0
    assert set(first["derivatives"]) == {"vb_forward_raw", "vb_backward_raw", "va_forward_raw", "va_backward_raw"}
    assert set(first["derivative_floor_activation_counts"]) == {"vb_forward", "vb_backward"}
    assert sum(first["liquid_label_counts"].values()) == 8
    assert sum(first["transfer_label_counts"].values()) == 8
    cell = first["checkpoint_cells"][0]
    assert cell["grid_index_zero_based"] == {"i_b": 1, "i_a": 1, "i_z": 0}
    assert {"d_bb", "d_bf", "d_fb", "d_ff", "d_b", "d_f"} <= set(cell["transfer_candidates"])
    assert {"sdh_b", "sdh_f", "use_transfer_b", "use_transfer_f"} <= set(cell["transfer_selector"])
    assert cell["selected"]["transfer_label"] in {"B", "F", "0"}
    assert cell["selected"]["liquid_label"] in {"B", "F", "0"}


def test_focused_parity_gate_and_priority_checkpoint_contract() -> None:
    gate = focused_parity_gate()
    assert gate["status"] == "PASS"
    assert gate["scientific_outputs_exactly_equal"] is True
    assert gate["budgeted_trajectory_calls"] == 0
    assert checkpoint_cells("湖北", 2) == ((1, 18, 0),)
    assert checkpoint_cells("四川", 4) == ((19, 16, 1),)
    assert checkpoint_cells("云南", 4) == ((10, 9, 0),)
    assert checkpoint_cells("北京", 2) == ()


def test_trace_writer_preserves_nonfinite_as_explicit_stop_evidence(tmp_path) -> None:
    path = tmp_path / "trace.json"
    write_json(path, {"positive": np.inf, "negative": -np.inf, "nan": np.nan})
    assert json.loads(path.read_text(encoding="utf-8")) == {
        "positive": "NONFINITE_POSITIVE_INFINITY",
        "negative": "NONFINITE_NEGATIVE_INFINITY",
        "nan": "NONFINITE_NAN",
    }
    with pytest.raises(FileExistsError):
        write_json(path, {})


def test_static_comparator_localizes_first_difference_without_science_call() -> None:
    def summary(value):
        return {"x": {"sha256": value}}

    def iteration(number, *, selected="same", derivative="same", candidate="same",
                  floor=0, liquid="same", transfer="same", operator="same", value="same"):
        return {
            "iteration": number,
            "derivatives": summary(derivative),
            "candidate_objects": summary(candidate),
            "selected_objects": summary(selected),
            "derivative_floor_activation_counts": {"x": floor},
            "derivative_floor_activation_coordinates": {"x": []},
            "liquid_label_sha256": liquid,
            "transfer_label_sha256": transfer,
            "operator_sha256": operator,
            "value_new_sha256": value,
            "convergence_statistic": float(number),
        }

    left = {"iterations": [iteration(1), iteration(2)]}
    right = {"iterations": [
        iteration(1, selected="return", operator="operator", value="value"),
        iteration(2, selected="return2", derivative="derivative", candidate="candidate",
                  floor=1, liquid="liquid", transfer="transfer", operator="operator2", value="value2"),
    ]}
    result = compare_iterations(left, right)
    assert result["first_differing_iteration"] == {
        "derivative": 2,
        "derivative_floor": 2,
        "candidate": 2,
        "selected": 1,
        "liquid_label": 2,
        "transfer_label": 2,
        "operator": 1,
        "value_new": 1,
        "convergence_statistic": None,
    }
    assert result["objects_differing_at_first_iteration"]["selected"] == ["x"]
    assert differing_names({"a": "x", "b": "y"}, {"a": "x", "b": "z"}) == ["b"]
