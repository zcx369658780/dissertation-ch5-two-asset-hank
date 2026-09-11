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
from ch5_two_asset_hank.multi_province.k1a_runtime_adapter import (
    ACCEPTED_DISTANCE_CANONICAL_LF_SHA256,
    PAYOFF_CLASSIFICATION,
    K1ARuntimeConfig,
    allocate_k1a_capital,
    canonical_lf_sha256,
    load_accepted_distance_score,
)
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER
from validators.multi_province.k1a_equal_share_vs_beta2.run import (
    validate_k1a_rah_provenance,
)


ROOT = Path(__file__).resolve().parents[1]
DISTANCE = ROOT / "docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv"
LEGACY = ROOT / "src/ch5_two_asset_hank/multi_province/capital_allocation.py"
LEGACY_SHA256 = "BB3F283BD782399A5C1C9AEE06DC50BBA61A0599BF062669DE0B1EBBB01AEE40"


def inputs() -> CapitalAllocationInputs:
    return CapitalAllocationInputs(
        illiquid_assets_at=np.linspace(1.0, 4.0, 31),
        population=np.linspace(100.0, 400.0, 31),
        inter_province_ratio=np.linspace(0.05, 0.45, 31),
        old_firm_return_ra=np.linspace(0.02, 0.09, 31),
    )


def config(beta: float) -> K1ARuntimeConfig:
    return K1ARuntimeConfig(PROVINCE_ORDER, load_accepted_distance_score(DISTANCE), beta)


def test_accepted_distance_receipt_hash_axis_and_orientation() -> None:
    matrix = load_accepted_distance_score(DISTANCE)
    assert canonical_lf_sha256(DISTANCE) == ACCEPTED_DISTANCE_CANONICAL_LF_SHA256
    assert matrix.shape == (31, 31)
    assert matrix[PROVINCE_ORDER.index("北京"), PROVINCE_ORDER.index("天津")] == pytest.approx(0.030224736871583606)


@pytest.mark.parametrize("beta", [-1.0, 0.5, 1.0, 4.0])
def test_only_preregistered_k1a_distance_betas_are_permitted(beta: float) -> None:
    with pytest.raises(ValueError, match="beta_distance"):
        config(beta)


def test_k1b_return_feedback_is_fail_closed() -> None:
    with pytest.raises(ValueError, match="K1B"):
        K1ARuntimeConfig(PROVINCE_ORDER, load_accepted_distance_score(DISTANCE), 2.0, beta_return=0.5)


def test_path_configs_differ_only_in_beta_distance() -> None:
    a, b = config(0.0), config(2.0)
    assert a.province_order == b.province_order == PROVINCE_ORDER
    np.testing.assert_array_equal(a.distance_score_destination_origin, b.distance_score_destination_origin)
    assert a.beta_return == b.beta_return == 0.0
    assert a.payoff_classification == b.payoff_classification == PAYOFF_CLASSIFICATION


def test_equal_share_and_geographic_shares_are_distinct() -> None:
    a = allocate_k1a_capital(inputs(), config(0.0)).network
    b = allocate_k1a_capital(inputs(), config(2.0)).network
    for origin in range(31):
        eligible = np.arange(31) != origin
        np.testing.assert_allclose(a.foreign_conditional_shares_destination_origin[eligible, origin], 1.0 / 30.0)
    assert not np.array_equal(a.portfolio_shares_destination_origin, b.portfolio_shares_destination_origin)


@pytest.mark.parametrize("beta", [0.0, 2.0])
def test_quantity_rah_home_and_conservation_use_one_share_matrix(beta: float) -> None:
    source = inputs()
    result = allocate_k1a_capital(source, config(beta))
    network = result.network
    wealth = source.illiquid_assets_at * source.population
    shares = network.portfolio_shares_destination_origin
    np.testing.assert_allclose(result.kt_supply, (shares * wealth[None, :]).sum(axis=1))
    np.testing.assert_allclose(result.household_illiquid_return_rah, source.old_firm_return_ra @ shares)
    np.testing.assert_allclose(network.domestic_retained_capital_by_origin, (1.0 - source.inter_province_ratio) * wealth)
    np.testing.assert_allclose(network.capital_column_sums, wealth)
    assert network.destination_private_productive_capital.sum() == pytest.approx(wealth.sum())


def test_destination_theta_is_not_applied_a_second_time() -> None:
    source = inputs()
    network = allocate_k1a_capital(source, config(2.0)).network
    expected = network.bilateral_private_capital_destination_origin.sum(axis=1)
    np.testing.assert_allclose(network.destination_private_productive_capital, expected)
    assert not np.allclose(expected, expected * source.inter_province_ratio)


def test_payoff_is_current_source_used_return_not_standardized_score() -> None:
    source = inputs()
    result = allocate_k1a_capital(source, config(2.0))
    expected = source.old_firm_return_ra @ result.network.portfolio_shares_destination_origin
    np.testing.assert_allclose(result.household_illiquid_return_rah, expected)
    assert result.payoff_classification == PAYOFF_CLASSIFICATION


def test_k1a_rah_provenance_accepts_actual_rah_from_the_same_share_matrix() -> None:
    source = inputs()
    result = allocate_k1a_capital(source, config(2.0))
    same_s_rah = float((source.old_firm_return_ra @ result.network.portfolio_shares_destination_origin)[0])

    validate_k1a_rah_provenance(
        actual_rah=same_s_rah,
        expected_rah=same_s_rah,
    )


def test_k1a_rah_provenance_rejects_tampered_actual_rah_fail_closed() -> None:
    source = inputs()
    result = allocate_k1a_capital(source, config(2.0))
    same_s_rah = float((source.old_firm_return_ra @ result.network.portfolio_shares_destination_origin)[0])

    with pytest.raises(ValueError, match="same S"):
        validate_k1a_rah_provenance(
            actual_rah=same_s_rah + 1e-6,
            expected_rah=same_s_rah,
        )


def test_legacy_allocator_remains_available_and_byte_identical() -> None:
    assert sha256(LEGACY.read_bytes()).hexdigest().upper() == LEGACY_SHA256
    legacy = allocate_productive_capital(inputs())
    assert legacy.kt_supply.shape == (31,)


def test_runner_contains_required_route_markers_without_parallel_science_copy() -> None:
    c1 = (ROOT / "src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py").read_text(encoding="utf-8")
    runner_path = ROOT / "validators/multi_province/k1a_equal_share_vs_beta2/run.py"
    runner = runner_path.read_text(encoding="utf-8")
    assert "reconstruct_migration_labor" in c1
    assert "residual_government_asset_levels" in c1
    assert "accepted_initialization_reuse" in runner
    assert "new_initialization_hjb_calls" in runner
    assert "quantity_and_rah_same_S" in runner
    assert "prior completed allocation using the same S" in runner
    tree = ast.parse(runner)
    functions = {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}
    assert "execute" in functions
    assert "run_c1_residual_public_asset_one_turn" not in functions
