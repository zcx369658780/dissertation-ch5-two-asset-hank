from __future__ import annotations

import ast
import copy
from pathlib import Path

import numpy as np
import pytest

import ch5_two_asset_hank.multi_province.one_turn as one_turn_module

from ch5_two_asset_hank.multi_province import (
    OneTurnInputs,
    PreFrozenHouseholdOutputBatch,
    run_source_faithful_one_turn,
)
from ch5_two_asset_hank.multi_province.capital_allocation import CapitalAllocationInputs
from ch5_two_asset_hank.multi_province.firm import evaluate_firm
from ch5_two_asset_hank.multi_province.migration_labor import (
    MigrationLaborInputs,
    reconstruct_migration_labor,
)
from ch5_two_asset_hank.multi_province.wage import composite_household_wages
from validators.multi_province.mp1_fixture_arithmetic import evaluate_fixture, load_fixture


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "tests/fixtures/multi_province/mp1_asymmetric_one_turn.json"
PRODUCTION_DIR = ROOT / "src/ch5_two_asset_hank/multi_province"


def _inputs(payload: dict | None = None) -> OneTurnInputs:
    fixture = load_fixture(FIXTURE_PATH) if payload is None else payload
    provinces = fixture["provinces"]
    household = PreFrozenHouseholdOutputBatch(
        ct=[p["Ct"] for p in provinces],
        household_lt=[p["Lt"] for p in provinces],
        at=[p["At"] for p in provinces],
        bt=[p["Bt"] for p in provinces],
        at_tax=[p["AtTax"] for p in provinces],
        converged=(True,) * len(provinces),
        diagnostics=tuple({"fixture": "pre-frozen"} for _ in provinces),
    )
    return OneTurnInputs(
        province_order=tuple(fixture["province_order"]),
        old_provinces=tuple(provinces),
        params=fixture["params"],
        phi_destination_origin=fixture["phi_mat"],
        migration_wedge_destination_origin=fixture["sigmau_mat"],
        household_outputs=household,
    )


def _actual_dict(result) -> dict:
    return {
        "Lt_mat": result.migration.lt_mat.tolist(),
        "Lt_supply": result.migration.lt_supply.tolist(),
        "capital_contribution": result.capital.productive_contribution.tolist(),
        "Kt_supply": result.capital.kt_supply.tolist(),
        "rah": result.capital.household_illiquid_return_rah.tolist(),
        "firm": [firm.as_source_dict() for firm in result.firms],
        "household_composite_wage": list(result.household_composite_wage),
        "rb": result.monetary.rb,
        "Govinc": list(result.fiscal.Govinc),
        "GovSurplus": result.fiscal.GovSurplus,
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
    else:
        assert float(actual) == pytest.approx(float(expected), rel=1e-12, abs=1e-12)


def test_complete_frozen_fixture_parity_against_json_and_independent_evaluator() -> None:
    fixture = load_fixture(FIXTURE_PATH)
    actual = _actual_dict(run_source_faithful_one_turn(_inputs(fixture)))
    independent = evaluate_fixture(fixture)
    for expected in (fixture["expected"], independent):
        for key, value in actual.items():
            _assert_close(value, expected[key])


def test_orientation_transpose_order_and_shape_fail_closed() -> None:
    fixture = load_fixture(FIXTURE_PATH)
    baseline = run_source_faithful_one_turn(_inputs(fixture))
    transposed = copy.deepcopy(fixture)
    transposed["phi_mat"] = np.asarray(transposed["phi_mat"]).T.tolist()
    changed = run_source_faithful_one_turn(_inputs(transposed))
    assert not np.allclose(changed.migration.lt_mat, baseline.migration.lt_mat, rtol=1e-12, atol=1e-12)
    reordered = copy.deepcopy(fixture)
    reordered["province_order"][0:2] = reversed(reordered["province_order"][0:2])
    with pytest.raises(ValueError, match="exactly match"):
        _inputs(reordered)
    with pytest.raises(ValueError, match="shape"):
        MigrationLaborInputs(
            consumption_by_origin=[1.0, 1.0, 1.0], population_by_origin=[1.0] * 3,
            old_firm_wage_by_destination=[1.0] * 3, tax_by_origin=[0.1] * 3,
            phi_destination_origin=np.ones((3, 2)), migration_wedge_destination_origin=np.zeros((3, 3)),
            gamma_c=2.0, phi_l=1.0,
        )


def test_negative_labor_and_wage_power_bases_fail_closed() -> None:
    fixture = load_fixture(FIXTURE_PATH)
    labor_inputs = _inputs(fixture)
    bad_wedge = np.array(fixture["sigmau_mat"], copy=True)
    bad_wedge[0, 0] = 2.0
    with pytest.raises(ValueError, match="power base"):
        reconstruct_migration_labor(MigrationLaborInputs(
            consumption_by_origin=labor_inputs.household_outputs.ct,
            population_by_origin=[p["N"] for p in fixture["provinces"]],
            old_firm_wage_by_destination=[p["wjt"] for p in fixture["provinces"]],
            tax_by_origin=[p["tau"] for p in fixture["provinces"]],
            phi_destination_origin=fixture["phi_mat"],
            migration_wedge_destination_origin=bad_wedge,
            gamma_c=fixture["params"]["ga"], phi_l=fixture["params"]["phi_l"],
        ))
    bad_wage_wedge = np.array(fixture["sigmau_mat"], copy=True)
    bad_wage_wedge[0, 0] = 2.0
    with pytest.raises(ValueError, match="power base"):
        composite_household_wages(
            fixture["provinces"], [1.0] * 3, fixture["phi_mat"], bad_wage_wedge,
            phi_l=1.0, alphal=1.0,
        )
    bad_phi = np.array(fixture["phi_mat"], copy=True)
    bad_phi[0, 0] = -1.0
    with pytest.raises(ValueError, match="positive"):
        composite_household_wages(
            fixture["provinces"], [1.0] * 3, bad_phi, fixture["sigmau_mat"],
            phi_l=1.0, alphal=1.0,
        )
    with pytest.raises(ValueError, match="positive"):
        composite_household_wages(
            fixture["provinces"], [1.0] * 3, fixture["phi_mat"], fixture["sigmau_mat"],
            phi_l=-2.0, alphal=1.0,
        )


def test_at_only_capital_bt_invariance_and_forbidden_replacements() -> None:
    fixture = load_fixture(FIXTURE_PATH)
    baseline = run_source_faithful_one_turn(_inputs(fixture))
    bt_only = copy.deepcopy(fixture)
    for index, province in enumerate(bt_only["provinces"]):
        province["Bt"] += 10.0 + index
    perturbed = run_source_faithful_one_turn(_inputs(bt_only))
    np.testing.assert_array_equal(
        baseline.capital.productive_contribution, perturbed.capital.productive_contribution
    )
    np.testing.assert_array_equal(baseline.capital.kt_supply, perturbed.capital.kt_supply)
    at_plus_bt = [
        p["inter_prv_ratio"] * (p["At"] + p["Bt"]) * p["N"] for p in fixture["provinces"]
    ]
    assert not np.allclose(at_plus_bt, baseline.capital.productive_contribution, rtol=1e-12, atol=1e-12)
    generic_rah = np.full(3, np.mean([p["ra"] for p in fixture["provinces"]]))
    assert not np.allclose(generic_rah, baseline.capital.household_illiquid_return_rah, rtol=1e-12, atol=1e-12)
    assert "bt" not in CapitalAllocationInputs.__dataclass_fields__


def test_firm_uses_destination_supply_and_clipping_is_literal() -> None:
    fixture = load_fixture(FIXTURE_PATH)
    result = run_source_faithful_one_turn(_inputs(fixture))
    assert [firm.Lt for firm in result.firms] == pytest.approx(result.migration.lt_supply)
    assert not np.allclose(
        [firm.Lt for firm in result.firms], [p["Lt"] for p in fixture["provinces"]]
    )
    first = fixture["provinces"][0]
    unclipped = evaluate_firm(first, result.capital.kt_supply[0], result.migration.lt_supply[0], fixture["params"])
    assert unclipped.ra0 > first["ramax"] and unclipped.ra == first["ramax"]
    assert unclipped.Corptax != pytest.approx(unclipped.PIt * first["corptau"])
    wage_clipped_source = dict(first, wjtmin=1.0, wjtmax=3.0)
    wage_clipped = evaluate_firm(
        wage_clipped_source, result.capital.kt_supply[0], result.migration.lt_supply[0], fixture["params"]
    )
    assert wage_clipped.wjt == 1.0 and wage_clipped.wt0 < 1.0
    assert wage_clipped.Corptax != pytest.approx(unclipped.Corptax)


def test_firm_source_uses_same_turn_household_labor_and_tax_without_mutating_old_state(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fixture = load_fixture(FIXTURE_PATH)
    baseline = _inputs(fixture)
    same_turn_labor = tuple(10.0 + index for index in range(len(fixture["provinces"])))
    same_turn_tax = tuple(0.5 + index for index in range(len(fixture["provinces"])))
    household = PreFrozenHouseholdOutputBatch(
        ct=baseline.household_outputs.ct,
        household_lt=same_turn_labor,
        at=baseline.household_outputs.at,
        bt=baseline.household_outputs.bt,
        at_tax=same_turn_tax,
        converged=baseline.household_outputs.converged,
        diagnostics=baseline.household_outputs.diagnostics,
    )
    inputs = OneTurnInputs(
        province_order=baseline.province_order,
        old_provinces=baseline.old_provinces,
        params=baseline.params,
        phi_destination_origin=baseline.phi_destination_origin,
        migration_wedge_destination_origin=baseline.migration_wedge_destination_origin,
        household_outputs=household,
    )
    old_state = tuple(dict(province) for province in inputs.old_provinces)
    captured: list[tuple[dict, float]] = []
    real_evaluate_firm = one_turn_module.evaluate_firm

    def capture_firm_source(province, kt_supply, lt_supply, params):
        captured.append((dict(province), float(lt_supply)))
        return real_evaluate_firm(province, kt_supply, lt_supply, params)

    monkeypatch.setattr(one_turn_module, "evaluate_firm", capture_firm_source)
    result = run_source_faithful_one_turn(inputs)

    assert [source["Lt_prev"] for source, _ in captured] == list(same_turn_labor)
    assert [source["AtTax"] for source, _ in captured] == list(same_turn_tax)
    assert [lt_supply for _, lt_supply in captured] == pytest.approx(result.migration.lt_supply)
    assert [lt_supply for _, lt_supply in captured] != pytest.approx(same_turn_labor)
    assert tuple(dict(province) for province in inputs.old_provinces) == old_state


def test_remaining_firm_source_conditional_branches() -> None:
    fixture = load_fixture(FIXTURE_PATH)
    result = run_source_faithful_one_turn(_inputs(fixture))
    first = fixture["provinces"][0]
    kt_supply = result.capital.kt_supply[0]
    lt_supply = result.migration.lt_supply[0]

    return_lower_source = dict(first, ramin=2.0, ramax=3.0)
    return_lower = evaluate_firm(return_lower_source, kt_supply, lt_supply, fixture["params"])
    assert return_lower.ra0 < 2.0 and return_lower.ra == 2.0

    wage_upper_source = dict(first, wjtmin=0.1, wjtmax=0.2)
    wage_upper = evaluate_firm(wage_upper_source, kt_supply, lt_supply, fixture["params"])
    assert wage_upper.wt0 > 0.2 and wage_upper.wjt == 0.2

    negative_profit_params = dict(fixture["params"], theta=100.0)
    profit_floor = evaluate_firm(first, kt_supply, lt_supply, negative_profit_params)
    assert profit_floor.PIt == 0.0


def test_fiscal_is_diagnostic_not_balanced_budget() -> None:
    result = run_source_faithful_one_turn(_inputs())
    assert result.fiscal.GovSurplus != 0.0
    assert result.fiscal.GovSurplus == pytest.approx(8.218004268862703, rel=1e-12, abs=1e-12)


def test_production_has_no_forbidden_import_or_solver_invocation() -> None:
    forbidden_import_roots = {"validators", "tests", "chapter5_model"}
    forbidden_calls = {
        "solve_matlab_faithful_hjb", "solve_household_steady_state", "solve_stationary_kfe",
        "fixed_point", "run_transition", "run_dynamics", "run_irf",
    }
    for path in PRODUCTION_DIR.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                assert not ({alias.name.split(".")[0] for alias in node.names} & forbidden_import_roots)
            elif isinstance(node, ast.ImportFrom) and node.module:
                assert node.module.split(".")[0] not in forbidden_import_roots
            elif isinstance(node, ast.Call):
                name = node.func.id if isinstance(node.func, ast.Name) else (
                    node.func.attr if isinstance(node.func, ast.Attribute) else ""
                )
                assert name not in forbidden_calls
