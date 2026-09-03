"""Zero-science durability checks for the 2018 singularity diagnostic."""
from __future__ import annotations

import csv
import json
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import pytest
from scipy import sparse

from validators.multi_province import mp4c_2018_first_singularity_diagnostic as diagnostic
import exports.matlab_faithful_two_asset_ha as faithful
from ch5_two_asset_hank.multi_province.one_turn import OneTurnInputs, PreFrozenHouseholdOutputBatch, run_source_faithful_one_turn
from validators.multi_province.mp1_fixture_arithmetic import load_fixture


def _grid():
    return faithful.MatlabFaithfulHJBGrid(
        np.array([0.0, 1.0]), np.array([0.0, 2.0]), np.array([0.8, 1.3]),
        np.array([[-1 / 3, 1 / 3], [1 / 3, -1 / 3]]),
    )


def _dummy_household_result(grid, index):
    calls = []
    hjb = type("H", (), {
        "post_convergence_operator": type("O", (), {"full": sparse.eye(8, format="csr")})(),
        "consumption": np.ones((2, 2, 2)), "labor": np.ones((2, 2, 2)),
        "converged": index == 0, "iterations": 11 + index,
        "convergence_statistic": 0.001 * (index + 1),
    })()
    kfe = type("K", (), {"density": np.full((2, 2, 2), 0.1 * (index + 1)), "cell_weight": 0.25})()
    aggregates = type("A", (), {"c_ss": 3.0 + index, "l_ss": 4.0 + index, "a_ss": 5.0 + index, "b_ss": 6.0 + index})()

    def dummy_hjb(*_args):
        calls.append("hjb")
        return hjb

    def dummy_kfe(*_args, **_kwargs):
        calls.append("kfe")
        return kfe

    def dummy_aggregate(*_args):
        calls.append("aggregate")
        return aggregates

    result = diagnostic.solve_matlab_source_postloop_household(
        grid, None, None, None, None, 0.0, 0.0, None,
        hjb_solver=dummy_hjb, kfe_solver=dummy_kfe, aggregator=dummy_aggregate,
    )
    assert calls == ["hjb", "kfe", "aggregate"]
    return result


def _one_turn_inputs(phi, at_tax):
    fixture = load_fixture(Path(__file__).parent / "fixtures/multi_province/mp1_asymmetric_one_turn.json")
    provinces = fixture["provinces"]
    household = PreFrozenHouseholdOutputBatch(
        ct=[item["Ct"] for item in provinces], household_lt=[item["Lt"] for item in provinces],
        at=[item["At"] for item in provinces], bt=[item["Bt"] for item in provinces],
        at_tax=at_tax, converged=(True,) * len(provinces),
        diagnostics=tuple({"zero_science": True} for _ in provinces),
    )
    return OneTurnInputs(
        province_order=tuple(fixture["province_order"]), old_provinces=tuple(provinces), params=fixture["params"],
        phi_destination_origin=phi, migration_wedge_destination_origin=fixture["sigmau_mat"], household_outputs=household,
    )


def _dummy_normal_completion_result():
    order = tuple(f"DUMMY_{index:02d}" for index in range(31))
    final_state = tuple(
        {"name": name, **{field: float(index + 1) for field in diagnostic.FINAL_FIELDS}}
        for index, name in enumerate(order)
    )
    last = SimpleNamespace(
        household_converged_count=31, ra_upper_count=0, ra_lower_count=0,
        wage_upper_count=0, wage_lower_count=0,
        nk_ratio_gap=np.full(31, 2.5e-10), yt_gap=np.full(31, 5.0e-10),
    )
    return order, SimpleNamespace(
        converged=True, termination_reason=diagnostic.TERMINATION_CONVERGED,
        iteration_count=2, final_state=final_state, history=(last, last),
    )


def test_phase_a_hjb_ledger_closure_is_durable_before_dummy_kfe(tmp_path, monkeypatch):
    fsync_calls = []
    original_fsync = diagnostic.os.fsync

    def record_fsync(fd):
        fsync_calls.append(fd)
        return original_fsync(fd)

    monkeypatch.setattr(diagnostic.os, "fsync", record_fsync)
    diagnostic.phase(tmp_path)

    receipt = json.loads((tmp_path / "phase_a_zero_science_test_receipt.json").read_text(encoding="utf-8"))
    rows = list(csv.DictReader((tmp_path / "hjb_return_ledger.csv").open(encoding="utf-8")))
    assert receipt["marker"] == "MP4C_2018_HJB_LEDGER_CLOSURE_REPAIR_ZERO_SCIENCE_PASS__ONE_DURABLE_2018_CHILD_AUTHORIZED"
    assert receipt["faithful_hjb_identity"] == "exports.matlab_faithful_two_asset_ha"
    assert receipt["faithful_kfe_identity"] == "exports.matlab_faithful_two_asset_ha"
    assert receipt["adapter_dummy_sequence"] == ["hjb", "kfe", "aggregate", "hjb", "kfe", "aggregate"]
    assert receipt["hjb_ledger_header_count"] == 1
    assert len(rows) == 2
    assert rows[0]["province"] == "DUMMY_A"
    assert rows[0]["hjb_converged"] == "True"
    assert rows[0]["kfe_path"] == "HJB_CONVERGED"
    assert rows[1]["province"] == "DUMMY_B"
    assert rows[1]["hjb_converged"] == "False"
    assert rows[1]["kfe_path"] == "MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE"
    assert len(fsync_calls) >= 2
    assert receipt["scientific_calls"] == {"stationary": 0, "household": 0, "HJB": 0, "KFE": 0, "MATLAB": 0, "R_PLM": 0}


def test_capture_flushes_raw_evidence_then_postmortem_is_separate(tmp_path):
    capture = diagnostic.Capture(tmp_path)
    operator = sparse.csr_matrix([[0.0]])
    capture.ctx = {"province": "DUMMY", "global_household_call_number": 1}
    capture.hjb = {"hjb_converged": False, "kfe_path": "MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE"}
    capture.before(operator)

    with pytest.raises(diagnostic.FirstSingularityCaptured):
        capture.solve(lambda: faithful.linalg.spsolve(operator, np.array([1.0])))

    raw = (
        "first_singularity_operator_A.npz",
        "first_singularity_operator_transpose.npz",
        "first_singularity_contaminated_matrix.npz",
        "first_singularity_rhs.npy",
        "first_singularity_raw_solve_vector.npy",
        "first_singularity_warning_and_traceback.txt",
    )
    assert all((tmp_path / name).is_file() for name in raw)
    assert not (tmp_path / "postmortem_rank_nullity.json").exists()

    diagnostic.postmortem(tmp_path)
    assert (tmp_path / "postmortem_operator_summary.json").is_file()
    assert (tmp_path / "postmortem_scc_closed_classes.json").is_file()
    assert (tmp_path / "postmortem_rank_nullity.json").is_file()


def test_phi_matches_production_literal_orientation_and_recomputes_in_place():
    first = ({"Yt": 12.0, "Lt": 3.0}, {"Yt": 15.0, "Lt": 5.0}, {"Yt": 7.0, "Lt": 7.0})
    phi = np.ones((3, 3))
    original_id = id(phi)
    first_prod = np.array([item["Yt"] / item["Lt"] for item in first])
    expected_first = 1 + 0.3 * (first_prod[:, None] - first_prod[None, :]) / (first_prod[:, None] + first_prod[None, :])
    assert diagnostic.recompute_phi_destination_origin(first, phi) is phi
    assert id(phi) == original_id
    np.testing.assert_array_equal(phi, expected_first)
    assert phi[2, 0] != phi[0, 2]

    second = ({"Yt": 6.0, "Lt": 3.0}, {"Yt": 25.0, "Lt": 5.0}, {"Yt": 21.0, "Lt": 7.0})
    second_prod = np.array([item["Yt"] / item["Lt"] for item in second])
    expected_second = 1 + 0.3 * (second_prod[:, None] - second_prod[None, :]) / (second_prod[:, None] + second_prod[None, :])
    diagnostic.recompute_phi_destination_origin(second, phi)
    np.testing.assert_array_equal(phi, expected_second)
    assert not np.array_equal(phi, expected_first)
    assert not np.array_equal(phi, np.ones((3, 3)))


def test_attax_matches_production_literal_and_is_not_hardcoded_zero():
    grid = _grid()
    state = {"rah": 0.1}
    density = np.array([[[0.1, 0.2], [0.3, 0.4]], [[0.5, 0.6], [0.7, 0.8]]])
    result = type("R", (), {
        "aggregates": type("A", (), {"a_ss": 2.0})(),
        "kfe": type("K", (), {"density": density, "cell_weight": 0.25})(),
    })()
    effective = faithful.matlab_faithful_illiquid_return(grid.a, grid.a[-1], state["rah"])
    expected = result.aggregates.a_ss * state["rah"] - float(np.sum(grid.a[None, :, None] * effective[None, :, None] * density) * result.kfe.cell_weight)
    actual = diagnostic.production_literal_at_tax(grid, state, result)
    assert actual == pytest.approx(expected)
    assert expected != 0.0


def test_diagnostic_batch_materialization_matches_production_fields_with_injected_dummies():
    grid = _grid()
    for province_count in (2, 3):
        states = tuple({"rah": 0.1 * (index + 1)} for index in range(province_count))
        results = tuple(_dummy_household_result(grid, index) for index in range(province_count))
        batch = diagnostic.pre_frozen_household_output_batch(grid, tuple(zip(states, results)), iteration=9)
        expected_tax = [diagnostic.production_literal_at_tax(grid, state, result) for state, result in zip(states, results)]
        for values in (batch.ct, batch.household_lt, batch.at, batch.bt, batch.at_tax, batch.converged, batch.diagnostics):
            assert len(values) == province_count
        np.testing.assert_array_equal(batch.ct, [3.0 + index for index in range(province_count)])
        np.testing.assert_array_equal(batch.household_lt, [4.0 + index for index in range(province_count)])
        np.testing.assert_array_equal(batch.at, [5.0 + index for index in range(province_count)])
        np.testing.assert_array_equal(batch.bt, [6.0 + index for index in range(province_count)])
        np.testing.assert_allclose(batch.at_tax, expected_tax)
        assert batch.converged == tuple(index == 0 for index in range(province_count))
        assert tuple(dict(item) for item in batch.diagnostics) == tuple(
            {"hjb_converged": index == 0, "hjb_iterations": 11 + index, "hjb_statistic": 0.001 * (index + 1), "iteration": 9}
            for index in range(province_count)
        )
        assert not np.allclose(batch.at_tax[:-1], batch.at_tax[-1])


def test_pure_one_turn_sensitivity_exposes_phi_and_attax_path_dependence():
    fixture = load_fixture(Path(__file__).parent / "fixtures/multi_province/mp1_asymmetric_one_turn.json")
    baseline_phi = np.asarray(fixture["phi_mat"], dtype=float)
    baseline_tax = [item["AtTax"] for item in fixture["provinces"]]
    baseline = run_source_faithful_one_turn(_one_turn_inputs(baseline_phi, baseline_tax))
    changed_phi = np.array(baseline_phi, copy=True)
    changed_phi[0, 1] *= 1.5
    phi_changed = run_source_faithful_one_turn(_one_turn_inputs(changed_phi, baseline_tax))
    assert not np.allclose(phi_changed.migration.lt_mat, baseline.migration.lt_mat)
    assert not np.allclose(phi_changed.household_composite_wage, baseline.household_composite_wage)

    changed_tax = np.asarray(baseline_tax, dtype=float) + np.arange(1, len(baseline_tax) + 1, dtype=float)
    tax_changed = run_source_faithful_one_turn(_one_turn_inputs(baseline_phi, changed_tax))
    assert not np.allclose([firm.Govinc for firm in tax_changed.firms], [firm.Govinc for firm in baseline.firms])
    assert not np.allclose(tax_changed.fiscal.Govinc, baseline.fiscal.Govinc)


def test_normal_completion_summary_is_durable_exact_and_dummy_only(tmp_path, monkeypatch):
    fsync_calls = []
    original_fsync = diagnostic.os.fsync

    def record_fsync(fd):
        fsync_calls.append(fd)
        return original_fsync(fd)

    monkeypatch.setattr(diagnostic.os, "fsync", record_fsync)
    order, result = _dummy_normal_completion_result()
    digest = diagnostic.normal_completion_summary(tmp_path, result, 62, order)
    path = tmp_path / "normal_completion_summary.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert digest == diagnostic.sha(path)
    assert payload["converged"] is True
    assert payload["termination_reason"] == diagnostic.TERMINATION_CONVERGED
    assert payload["iteration_count"] == 2
    assert payload["household_call_count"] == 62
    assert payload["household_converged_count"] == 31
    assert payload["ra_upper_count"] == 0 and payload["ra_lower_count"] == 0
    assert payload["wage_upper_count"] == 0 and payload["wage_lower_count"] == 0
    assert payload["max_final_nk_ratio_gap"] == 2.5e-10
    assert payload["max_final_yt_gap"] == 5.0e-10
    assert payload["province_order"] == list(order)
    assert len(payload["final_31x20"]) == 31
    assert payload["final_31x20"][0]["name"] == order[0]
    assert payload["final_state_fields"] == list(diagnostic.FINAL_FIELDS)
    assert fsync_calls
    with pytest.raises(FileExistsError):
        diagnostic.normal_completion_summary(tmp_path, result, 62, order)
