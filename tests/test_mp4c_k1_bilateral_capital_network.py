from __future__ import annotations

import ast
from hashlib import sha256
from pathlib import Path

import numpy as np
import pytest

from ch5_two_asset_hank.multi_province.capital_allocation import (
    CapitalAllocationInputs,
    allocate_productive_capital,
)
from ch5_two_asset_hank.multi_province.capital_network import (
    LAGGED_TIMING_CONTRACT,
    ORIENTATION,
    BilateralCapitalNetworkInputs,
    ForeignConditionalShareInputs,
    build_bilateral_capital_network,
    foreign_conditional_shares,
)


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src/ch5_two_asset_hank/multi_province/capital_network.py"
LEGACY = ROOT / "src/ch5_two_asset_hank/multi_province/capital_allocation.py"
LEGACY_BASELINE_SHA256 = "BB3F283BD782399A5C1C9AEE06DC50BBA61A0599BF062669DE0B1EBBB01AEE40"


def fixture_inputs(**changes: object) -> BilateralCapitalNetworkInputs:
    values: dict[str, object] = {
        "province_order": ("甲", "乙", "丙"),
        "illiquid_assets_per_capita_by_origin": np.array([10.0, 20.0, 30.0]),
        "population_by_origin": np.array([2.0, 3.0, 4.0]),
        "total_foreign_share_theta_by_origin": np.array([0.2, 0.5, 0.8]),
        "distance_score_destination_origin": np.array([
            [0.0, 1.0, 4.0],
            [2.0, 0.0, 1.5],
            [1.0, 3.0, 0.0],
        ]),
        "lagged_return_score_by_destination": np.array([0.1, 0.4, -0.2]),
        "portfolio_return_by_destination": np.array([0.02, 0.05, 0.09]),
        "beta_distance": 0.7,
        "beta_return": 1.3,
        "lagged_return_provenance": "COMPLETED_ITERATION_N",
    }
    values.update(changes)
    return BilateralCapitalNetworkInputs(**values)  # type: ignore[arg-type]


def test_destination_by_origin_orientation_and_destination_row_sums() -> None:
    result = build_bilateral_capital_network(fixture_inputs())
    assert result.orientation == ORIENTATION == "DESTINATION_BY_ORIGIN"
    assert result.portfolio_shares_destination_origin.shape == (3, 3)
    np.testing.assert_allclose(
        result.destination_private_productive_capital,
        result.bilateral_private_capital_destination_origin.sum(axis=1),
    )


def test_foreign_columns_normalize_with_zero_diagonal() -> None:
    result = build_bilateral_capital_network(fixture_inputs())
    np.testing.assert_array_equal(
        np.diag(result.foreign_conditional_shares_destination_origin), np.zeros(3)
    )
    np.testing.assert_allclose(result.foreign_conditional_shares_destination_origin.sum(axis=0), 1.0)


def test_full_share_columns_normalize_and_home_share_is_exact() -> None:
    inputs = fixture_inputs()
    result = build_bilateral_capital_network(inputs)
    np.testing.assert_allclose(result.share_column_sums, 1.0)
    np.testing.assert_allclose(
        np.diag(result.portfolio_shares_destination_origin),
        1.0 - inputs.total_foreign_share_theta_by_origin,
    )


def test_foreign_outflow_and_origin_capital_conservation() -> None:
    inputs = fixture_inputs()
    result = build_bilateral_capital_network(inputs)
    wealth = inputs.illiquid_assets_per_capita_by_origin * inputs.population_by_origin
    np.testing.assert_allclose(
        result.foreign_outflow_by_origin,
        inputs.total_foreign_share_theta_by_origin * wealth,
    )
    np.testing.assert_allclose(result.capital_column_sums, wealth)


def test_national_private_capital_conservation() -> None:
    result = build_bilateral_capital_network(fixture_inputs())
    assert result.destination_private_productive_capital.sum() == pytest.approx(
        result.origin_private_wealth.sum()
    )
    assert result.national_private_capital_conservation_residual == pytest.approx(0.0, abs=1e-12)


def test_rah_uses_the_identical_full_portfolio_matrix() -> None:
    inputs = fixture_inputs()
    result = build_bilateral_capital_network(inputs)
    expected = inputs.portfolio_return_by_destination @ result.portfolio_shares_destination_origin
    np.testing.assert_allclose(result.household_portfolio_return_by_origin, expected)


def test_common_return_invariance() -> None:
    result = build_bilateral_capital_network(
        fixture_inputs(portfolio_return_by_destination=np.full(3, 0.073))
    )
    np.testing.assert_allclose(result.household_portfolio_return_by_origin, 0.073)


def test_theta_zero_is_home_only() -> None:
    result = build_bilateral_capital_network(
        fixture_inputs(total_foreign_share_theta_by_origin=np.array([0.0, 0.5, 0.8]))
    )
    assert result.household_portfolio_return_by_origin[0] == pytest.approx(0.02)
    assert result.domestic_retained_capital_by_origin[0] == pytest.approx(20.0)
    assert result.foreign_outflow_by_origin[0] == pytest.approx(0.0)


def test_theta_one_is_foreign_only() -> None:
    result = build_bilateral_capital_network(
        fixture_inputs(total_foreign_share_theta_by_origin=np.array([0.2, 1.0, 0.8]))
    )
    assert result.portfolio_shares_destination_origin[1, 1] == 0.0
    expected = (
        result.foreign_conditional_shares_destination_origin[:, 1]
        @ np.array([0.02, 0.05, 0.09])
    )
    assert result.household_portfolio_return_by_origin[1] == pytest.approx(expected)


def test_zero_coefficients_give_equal_foreign_shares() -> None:
    result = build_bilateral_capital_network(fixture_inputs(beta_distance=0.0, beta_return=0.0))
    p = result.foreign_conditional_shares_destination_origin
    for origin in range(3):
        np.testing.assert_allclose(p[np.arange(3) != origin, origin], 0.5)


def test_higher_lagged_return_score_raises_eligible_destination_share() -> None:
    base = build_bilateral_capital_network(fixture_inputs())
    raised = build_bilateral_capital_network(
        fixture_inputs(lagged_return_score_by_destination=np.array([0.1, 0.8, -0.2]))
    )
    for origin in (0, 2):
        assert (
            raised.foreign_conditional_shares_destination_origin[1, origin]
            > base.foreign_conditional_shares_destination_origin[1, origin]
        )


def test_higher_bilateral_distance_lowers_that_link_share() -> None:
    base_inputs = fixture_inputs()
    base = build_bilateral_capital_network(base_inputs)
    changed_distance = np.array(base_inputs.distance_score_destination_origin, copy=True)
    changed_distance[2, 0] += 2.0
    changed = build_bilateral_capital_network(
        fixture_inputs(distance_score_destination_origin=changed_distance)
    )
    assert (
        changed.foreign_conditional_shares_destination_origin[2, 0]
        < base.foreign_conditional_shares_destination_origin[2, 0]
    )


def test_signal_and_payoff_are_separate_api_objects() -> None:
    base = build_bilateral_capital_network(fixture_inputs())
    changed = build_bilateral_capital_network(
        fixture_inputs(portfolio_return_by_destination=np.array([0.20, 0.05, 0.09]))
    )
    np.testing.assert_array_equal(
        changed.portfolio_shares_destination_origin, base.portfolio_shares_destination_origin
    )
    assert not np.array_equal(
        changed.household_portfolio_return_by_origin, base.household_portfolio_return_by_origin
    )


def test_same_turn_provenance_is_rejected_and_no_firm_module_is_imported() -> None:
    with pytest.raises(ValueError, match="same-turn"):
        fixture_inputs(lagged_return_provenance="same-turn current firm return")
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
    imported = "\n".join(
        ast.unparse(node)
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
    ).lower()
    for forbidden in ("firm", "wage", "household", "hjb", "kfe", "controller", "trajectory"):
        assert forbidden not in imported
    assert LAGGED_TIMING_CONTRACT.startswith("ALLOCATION_ITERATION_N_PLUS_1")


def test_full_31_by_31_contract_and_conservation() -> None:
    n = 31
    inputs = BilateralCapitalNetworkInputs(
        province_order=tuple(f"省{i + 1}" for i in range(n)),
        illiquid_assets_per_capita_by_origin=np.linspace(1.0, 3.0, n),
        population_by_origin=np.linspace(10.0, 40.0, n),
        total_foreign_share_theta_by_origin=np.linspace(0.0, 1.0, n),
        distance_score_destination_origin=np.abs(
            np.arange(n)[:, None] - np.arange(n)[None, :]
        ),
        lagged_return_score_by_destination=np.linspace(-0.2, 0.2, n),
        portfolio_return_by_destination=np.linspace(0.01, 0.11, n),
        beta_distance=0.3,
        beta_return=0.8,
        lagged_return_provenance="LAGGED_SYNTHETIC_31_PROVINCE_FIXTURE",
    )
    result = build_bilateral_capital_network(inputs)
    assert result.portfolio_shares_destination_origin.shape == (31, 31)
    assert result.bilateral_private_capital_destination_origin.shape == (31, 31)
    np.testing.assert_allclose(result.share_column_sums, 1.0, rtol=0.0, atol=1e-12)
    np.testing.assert_allclose(
        result.capital_column_sums, result.origin_private_wealth, rtol=0.0, atol=1e-12
    )
    assert result.destination_private_productive_capital.sum() == pytest.approx(
        result.origin_private_wealth.sum()
    )


@pytest.mark.parametrize("field", ["distance", "lagged", "payoff"])
def test_nonfinite_score_or_payoff_inputs_fail_closed(field: str) -> None:
    changes: dict[str, object]
    if field == "distance":
        value = np.zeros((3, 3)); value[1, 0] = np.nan
        changes = {"distance_score_destination_origin": value}
    elif field == "lagged":
        changes = {"lagged_return_score_by_destination": np.array([0.1, np.inf, 0.2])}
    else:
        changes = {"portfolio_return_by_destination": np.array([0.1, 0.2, np.nan])}
    with pytest.raises(ValueError, match="finite"):
        fixture_inputs(**changes)


def test_nonfinite_attractiveness_from_overflow_fails_closed() -> None:
    inputs = ForeignConditionalShareInputs(
        province_order=("甲", "乙"),
        distance_score_destination_origin=np.full((2, 2), 1e308),
        lagged_return_score_by_destination=np.zeros(2),
        beta_distance=1e308,
        beta_return=0.0,
        lagged_return_provenance="LAGGED_SYNTHETIC",
    )
    with pytest.raises(ValueError, match="attractiveness"):
        foreign_conditional_shares(inputs)


@pytest.mark.parametrize("theta", [np.array([-0.1, 0.2, 0.3]), np.array([0.1, 1.1, 0.3])])
def test_theta_outside_unit_interval_fails_closed(theta: np.ndarray) -> None:
    with pytest.raises(ValueError, match=r"\[0, 1\]"):
        fixture_inputs(total_foreign_share_theta_by_origin=theta)


@pytest.mark.parametrize(
    "changes",
    [
        {"province_order": ("甲", "甲", "丙")},
        {"population_by_origin": np.ones(2)},
        {"distance_score_destination_origin": np.ones((3, 2))},
        {"lagged_return_score_by_destination": np.ones(4)},
    ],
)
def test_province_order_and_shapes_fail_closed(changes: dict[str, object]) -> None:
    with pytest.raises(ValueError):
        fixture_inputs(**changes)


def test_all_returned_arrays_are_read_only() -> None:
    result = build_bilateral_capital_network(fixture_inputs())
    arrays = [value for value in result.__dict__.values() if isinstance(value, np.ndarray)]
    assert arrays and all(not value.flags.writeable for value in arrays)
    foreign = foreign_conditional_shares(ForeignConditionalShareInputs(
        province_order=("甲", "乙"),
        distance_score_destination_origin=np.zeros((2, 2)),
        lagged_return_score_by_destination=np.zeros(2),
        beta_distance=0.0,
        beta_return=0.0,
        lagged_return_provenance="LAGGED_READ_ONLY_TEST",
    ))
    foreign_arrays = [
        value for value in foreign.__dict__.values() if isinstance(value, np.ndarray)
    ]
    assert foreign_arrays and all(not value.flags.writeable for value in foreign_arrays)
    with pytest.raises(ValueError):
        result.portfolio_shares_destination_origin[0, 0] = 0.0


def test_legacy_equal_share_discrepancy_and_repaired_conservation() -> None:
    inputs = fixture_inputs(beta_distance=0.0, beta_return=0.0)
    repaired = build_bilateral_capital_network(inputs)
    legacy = allocate_productive_capital(CapitalAllocationInputs(
        illiquid_assets_at=inputs.illiquid_assets_per_capita_by_origin,
        population=inputs.population_by_origin,
        inter_province_ratio=inputs.total_foreign_share_theta_by_origin,
        old_firm_return_ra=inputs.portfolio_return_by_destination,
    ))
    missing_home = (1.0 - inputs.total_foreign_share_theta_by_origin) * repaired.origin_private_wealth
    np.testing.assert_allclose(
        repaired.destination_private_productive_capital - legacy.kt_supply, missing_home
    )
    n = len(inputs.province_order)
    theta = inputs.total_foreign_share_theta_by_origin
    legacy_weight_sums = np.array([
        1.0 - theta[i] + theta[i] * (theta.sum() - theta[i]) / (n - 1)
        for i in range(n)
    ])
    assert np.all(legacy_weight_sums < 1.0)
    np.testing.assert_allclose(repaired.share_column_sums, 1.0)


def test_legacy_capital_allocation_source_is_byte_identical() -> None:
    assert sha256(LEGACY.read_bytes()).hexdigest().upper() == LEGACY_BASELINE_SHA256


def test_source_has_no_scientific_coefficients_or_runtime_defaults() -> None:
    signature = ast.parse(SOURCE.read_text(encoding="utf-8"))
    classes = [node for node in signature.body if isinstance(node, ast.ClassDef)]
    input_class = next(node for node in classes if node.name == "BilateralCapitalNetworkInputs")
    annotated = [node for node in input_class.body if isinstance(node, ast.AnnAssign)]
    beta_nodes = [node for node in annotated if getattr(node.target, "id", "") in {"beta_distance", "beta_return"}]
    assert len(beta_nodes) == 2 and all(node.value is None for node in beta_nodes)
    text = SOURCE.read_text(encoding="utf-8").lower()
    for forbidden in ("portfolio_adjustment_speed", "pgdp_coefficient", "industrial_distance_coefficient"):
        assert forbidden not in text
