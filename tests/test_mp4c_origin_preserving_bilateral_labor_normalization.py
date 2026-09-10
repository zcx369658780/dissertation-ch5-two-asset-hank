"""Zero-science contracts for origin-preserving bilateral labor normalization."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from ch5_two_asset_hank.multi_province import (
    OneTurnInputs,
    OriginPreservingNormalizedOneTurnResult,
    PreFrozenHouseholdOutputBatch,
    run_origin_preserving_normalized_one_turn,
    run_source_faithful_one_turn,
)
from ch5_two_asset_hank.multi_province.migration_labor import (
    MigrationLaborInputs,
    OriginPreservingNormalizedMigrationLaborInputs,
    OriginPreservingNormalizedMigrationLaborResult,
    reconstruct_migration_labor,
    reconstruct_origin_preserving_normalized_migration_labor,
)
from validators.multi_province.mp1_fixture_arithmetic import load_fixture


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "tests/fixtures/multi_province/mp1_asymmetric_one_turn.json"


def _inputs(
    *,
    household_labor_per_capita_by_origin: object = (1.0, 1.0, 1.0),
    population_by_origin: object = (50.0, 20.0, 30.0),
    old_firm_wage_by_destination: object = (10.0, 10.0, 10.0),
    migration_wedge_destination_origin: object | None = None,
) -> OriginPreservingNormalizedMigrationLaborInputs:
    # With C=phi=1 and tax=0, q is exactly wage * (1 - wedge).
    wedges = (
        np.array(
            [[0.94, 0.95, 0.97], [0.976, 0.975, 0.97], [0.984, 0.975, 0.96]],
            dtype=float,
        )
        if migration_wedge_destination_origin is None
        else migration_wedge_destination_origin
    )
    return OriginPreservingNormalizedMigrationLaborInputs(
        consumption_by_origin=(1.0, 1.0, 1.0),
        population_by_origin=population_by_origin,
        household_labor_per_capita_by_origin=household_labor_per_capita_by_origin,
        old_firm_wage_by_destination=old_firm_wage_by_destination,
        tax_by_origin=(0.0, 0.0, 0.0),
        phi_destination_origin=np.ones((3, 3)),
        migration_wedge_destination_origin=wedges,
        gamma_c=1.0,
        phi_l=1.0,
    )


def test_legacy_literal_fixture_regression_is_unchanged() -> None:
    fixture = load_fixture(FIXTURE_PATH)
    provinces = fixture["provinces"]
    result = reconstruct_migration_labor(
        MigrationLaborInputs(
            consumption_by_origin=[province["Ct"] for province in provinces],
            population_by_origin=[province["N"] for province in provinces],
            old_firm_wage_by_destination=[province["wjt"] for province in provinces],
            tax_by_origin=[province["tau"] for province in provinces],
            phi_destination_origin=fixture["phi_mat"],
            migration_wedge_destination_origin=fixture["sigmau_mat"],
            gamma_c=fixture["params"]["ga"],
            phi_l=fixture["params"]["phi_l"],
        )
    )
    np.testing.assert_allclose(result.lt_mat, fixture["expected"]["Lt_mat"], rtol=1e-12, atol=1e-12)
    np.testing.assert_allclose(result.lt_supply, fixture["expected"]["Lt_supply"], rtol=1e-12, atol=1e-12)


def test_normalized_matrix_is_destination_by_origin_and_retains_provenance() -> None:
    result = reconstruct_origin_preserving_normalized_migration_labor(_inputs())
    assert "destination" in result.orientation.lower()
    assert "origin" in result.orientation.lower()
    assert result.bilateral_labor_flow_destination_origin.shape == (3, 3)
    # Origin zero: 50 splits to destination rows 0, 1, 2 as 30, 12, 8.
    np.testing.assert_allclose(result.normalized_shares_destination_origin[:, 0], (0.6, 0.24, 0.16))
    np.testing.assert_allclose(result.bilateral_labor_flow_destination_origin[:, 0], (30.0, 12.0, 8.0))


def test_share_flow_and_national_conservation_hold_but_province_totals_can_differ() -> None:
    result = reconstruct_origin_preserving_normalized_migration_labor(_inputs())
    np.testing.assert_allclose(result.share_column_sums_by_origin, np.ones(3), rtol=0.0, atol=1e-12)
    np.testing.assert_allclose(result.flow_column_sums_by_origin, result.origin_labor_mass_by_origin, rtol=0.0, atol=1e-12)
    np.testing.assert_allclose(
        result.destination_firm_labor_by_destination,
        result.bilateral_labor_flow_destination_origin.sum(axis=1),
        rtol=0.0,
        atol=1e-12,
    )
    assert result.national_conservation_residual == pytest.approx(0.0, abs=1e-12)
    assert not np.allclose(result.destination_firm_labor_by_destination, result.origin_labor_mass_by_origin)
    np.testing.assert_allclose(
        result.net_labor_flow_by_province,
        result.destination_firm_labor_by_destination - result.origin_labor_mass_by_origin,
        rtol=0.0,
        atol=1e-12,
    )


def test_population_is_multiplied_once_and_labor_perturbation_only_scales_its_origin_column() -> None:
    baseline = reconstruct_origin_preserving_normalized_migration_labor(_inputs())
    changed = reconstruct_origin_preserving_normalized_migration_labor(
        _inputs(household_labor_per_capita_by_origin=(1.0, 2.0, 1.0))
    )
    np.testing.assert_allclose(baseline.origin_labor_mass_by_origin, (50.0, 20.0, 30.0))
    np.testing.assert_allclose(changed.origin_labor_mass_by_origin, (50.0, 40.0, 30.0))
    np.testing.assert_allclose(changed.bilateral_labor_flow_destination_origin[:, 0], baseline.bilateral_labor_flow_destination_origin[:, 0])
    np.testing.assert_allclose(changed.bilateral_labor_flow_destination_origin[:, 1], 2.0 * baseline.bilateral_labor_flow_destination_origin[:, 1])
    np.testing.assert_allclose(changed.bilateral_labor_flow_destination_origin[:, 2], baseline.bilateral_labor_flow_destination_origin[:, 2])


def test_destination_wage_perturbation_changes_directions_but_not_origin_column_mass() -> None:
    baseline = reconstruct_origin_preserving_normalized_migration_labor(_inputs())
    changed = reconstruct_origin_preserving_normalized_migration_labor(
        _inputs(old_firm_wage_by_destination=(20.0, 10.0, 10.0))
    )
    np.testing.assert_allclose(changed.flow_column_sums_by_origin, baseline.flow_column_sums_by_origin, rtol=0.0, atol=1e-12)
    assert np.all(changed.normalized_shares_destination_origin[0, :] > baseline.normalized_shares_destination_origin[0, :])


def test_zero_invalid_and_nonfinite_columns_fail_closed() -> None:
    with pytest.raises(ValueError):
        reconstruct_origin_preserving_normalized_migration_labor(
            _inputs(old_firm_wage_by_destination=(0.0, 0.0, 0.0))
        )
    with pytest.raises(ValueError):
        _inputs(household_labor_per_capita_by_origin=(1.0, -1.0, 1.0))
    with pytest.raises(ValueError):
        _inputs(household_labor_per_capita_by_origin=(1.0, float("nan"), 1.0))
    with pytest.raises(ValueError):
        reconstruct_origin_preserving_normalized_migration_labor(
            _inputs(migration_wedge_destination_origin=np.full((3, 3), 2.0))
        )


@pytest.mark.parametrize(
    ("taxes", "wedges"),
    [
        ((-0.2, 0.0, 0.0), np.zeros((3, 3))),
        ((0.0, 0.0, 0.0), np.full((3, 3), -0.2)),
    ],
)
def test_negative_tax_or_wedge_preserves_literal_kernel_when_power_base_is_valid(
    taxes: tuple[float, float, float], wedges: np.ndarray
) -> None:
    inputs = OriginPreservingNormalizedMigrationLaborInputs(
        consumption_by_origin=(1.0, 1.5, 2.0),
        household_labor_per_capita_by_origin=(1.0, 1.0, 1.0),
        population_by_origin=(10.0, 20.0, 30.0),
        old_firm_wage_by_destination=(1.0, 2.0, 3.0),
        tax_by_origin=taxes,
        phi_destination_origin=np.ones((3, 3)),
        migration_wedge_destination_origin=wedges,
        gamma_c=2.0,
        phi_l=1.5,
    )
    result = reconstruct_origin_preserving_normalized_migration_labor(inputs)
    expected_q = np.empty((3, 3))
    for origin in range(3):
        for destination in range(3):
            expected_q[destination, origin] = inputs.consumption_by_origin[origin] ** (
                -inputs.gamma_c / inputs.phi_l
            ) * (
                inputs.old_firm_wage_by_destination[destination]
                * (1.0 - inputs.tax_by_origin[origin] - wedges[destination, origin])
            ) ** (1.0 / inputs.phi_l)
    np.testing.assert_allclose(result.raw_attractiveness_destination_origin, expected_q)
    np.testing.assert_allclose(
        result.normalized_shares_destination_origin,
        expected_q / expected_q.sum(axis=0, keepdims=True),
    )


def test_normalized_api_schema_is_explicitly_distinct_from_source_faithful_route() -> None:
    inputs = _inputs()
    result = reconstruct_origin_preserving_normalized_migration_labor(inputs)
    assert isinstance(result, OriginPreservingNormalizedMigrationLaborResult)
    assert not isinstance(inputs, MigrationLaborInputs)
    assert not hasattr(result, "lt_mat")
    assert not hasattr(result, "lt_supply")
    expected = {
        "orientation",
        "raw_attractiveness_destination_origin",
        "normalized_shares_destination_origin",
        "origin_labor_mass_by_origin",
        "bilateral_labor_flow_destination_origin",
        "destination_firm_labor_by_destination",
        "share_column_sums_by_origin",
        "flow_column_sums_by_origin",
        "net_labor_flow_by_province",
        "national_conservation_residual",
    }
    assert expected <= set(result.__dataclass_fields__)


def test_separate_normalized_one_turn_consumes_destination_row_sums() -> None:
    fixture = load_fixture(FIXTURE_PATH)
    provinces = fixture["provinces"]
    inputs = OneTurnInputs(
        province_order=tuple(fixture["province_order"]),
        old_provinces=tuple(provinces),
        params=fixture["params"],
        phi_destination_origin=fixture["phi_mat"],
        migration_wedge_destination_origin=fixture["sigmau_mat"],
        household_outputs=PreFrozenHouseholdOutputBatch(
            ct=[province["Ct"] for province in provinces],
            household_lt=[province["Lt"] for province in provinces],
            at=[province["At"] for province in provinces],
            bt=[province["Bt"] for province in provinces],
            at_tax=[province["AtTax"] for province in provinces],
            converged=(True,) * len(provinces),
            diagnostics=tuple({"fixture": "pre-frozen"} for _ in provinces),
        ),
    )
    legacy = run_source_faithful_one_turn(inputs)
    normalized = run_origin_preserving_normalized_one_turn(inputs)

    assert isinstance(normalized, OriginPreservingNormalizedOneTurnResult)
    assert type(normalized) is not type(legacy)
    np.testing.assert_allclose(
        [firm.Lt for firm in normalized.firms],
        normalized.migration.destination_firm_labor_by_destination,
        rtol=0.0,
        atol=1e-12,
    )
    np.testing.assert_allclose(
        normalized.migration.flow_column_sums_by_origin,
        inputs.household_outputs.household_lt
        * np.asarray([province["N"] for province in provinces]),
        rtol=0.0,
        atol=1e-12,
    )


def test_full_31_by_31_provenance_shape_and_conservation() -> None:
    n = 31
    result = reconstruct_origin_preserving_normalized_migration_labor(
        OriginPreservingNormalizedMigrationLaborInputs(
            consumption_by_origin=np.linspace(1.0, 2.0, n),
            household_labor_per_capita_by_origin=np.linspace(0.5, 1.5, n),
            population_by_origin=np.linspace(10.0, 40.0, n),
            old_firm_wage_by_destination=np.linspace(1.0, 2.0, n),
            tax_by_origin=np.full(n, 0.1),
            phi_destination_origin=np.ones((n, n)),
            migration_wedge_destination_origin=np.zeros((n, n)),
            gamma_c=2.0,
            phi_l=1.5,
        )
    )
    assert result.raw_attractiveness_destination_origin.shape == (31, 31)
    assert result.normalized_shares_destination_origin.shape == (31, 31)
    assert result.bilateral_labor_flow_destination_origin.shape == (31, 31)
    np.testing.assert_allclose(result.share_column_sums_by_origin, 1.0, rtol=0.0, atol=1e-12)
    np.testing.assert_allclose(
        result.flow_column_sums_by_origin,
        result.origin_labor_mass_by_origin,
        rtol=1e-12,
        atol=1e-12,
    )
    assert result.national_conservation_residual == pytest.approx(0.0, abs=1e-12)
