from __future__ import annotations

import ast
from pathlib import Path

import numpy as np
import pytest

from validators.multi_province.initial_private_k_residual_govinv_probe.run import (
    residual_govinv_accounting,
)


ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "validators/multi_province/initial_private_k_residual_govinv_probe/run.py"


def test_g0_and_g1_accounting_and_binding() -> None:
    result = residual_govinv_accounting(
        np.array([100.0, 100.0, 100.0]), np.array([2.0, 100.0, 125.0])
    )
    np.testing.assert_array_equal(result["govinv_g0"], [100.0, 100.0, 100.0])
    np.testing.assert_array_equal(result["g0_total"], [102.0, 200.0, 225.0])
    np.testing.assert_array_equal(result["govinv_g1"], [98.0, 0.0, 0.0])
    np.testing.assert_array_equal(result["g1_total"], [100.0, 100.0, 125.0])
    np.testing.assert_allclose(result["beta_star"], [50.0, 1.0, 0.8])


def test_accounting_fails_closed() -> None:
    with pytest.raises(ValueError):
        residual_govinv_accounting(np.array([1.0, 2.0]), np.array([1.0]))
    with pytest.raises(ValueError):
        residual_govinv_accounting(np.array([1.0, 2.0]), np.array([1.0, np.nan]))
    with pytest.raises(ValueError):
        residual_govinv_accounting(np.array([1.0, 0.0]), np.array([1.0, 1.0]))


def test_probe_has_no_forbidden_runtime_route_import_or_call() -> None:
    source = RUN.read_text(encoding="utf-8")
    tree = ast.parse(source)
    forbidden_calls = {
        "reconstruct_migration_labor", "reconstruct_origin_preserving_normalized_migration_labor",
        "evaluate_firm",
        "composite_household_wages", "run_source_faithful_one_turn",
        "run_origin_preserving_normalized_one_turn", "run_manual_steady_state", "_adapt",
    }
    imported_modules = {
        node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom) and node.module
    }
    assert not any("migration_labor" in module or module.endswith(".firm") or module.endswith(".wage")
                   for module in imported_modules)
    called_names = {
        node.func.id for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    assert not (called_names & forbidden_calls)
    allocation_calls = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        and node.func.id == "allocate_productive_capital"
    ]
    assert len(allocation_calls) == 1


def test_bridge_homogeneity_is_algebraic_not_a_second_parameter_cell() -> None:
    at = np.array([2.0, 3.0, 4.0])
    population = np.array([10.0, 20.0, 30.0])
    ratio = np.array([0.1, 0.2, 0.3])
    contribution = ratio * at * population
    private = (contribution.sum() - contribution) / 2.0
    beta = 7.25
    scaled = (beta * contribution.sum() - beta * contribution) / 2.0
    np.testing.assert_allclose(scaled, beta * private)


def test_at_times_n_is_distinct_from_ratio_weighted_contribution() -> None:
    at = np.array([2.0, 3.0])
    population = np.array([10.0, 20.0])
    ratio = np.array([0.1, 0.2])
    np.testing.assert_array_equal(at * population, [20.0, 60.0])
    np.testing.assert_allclose(ratio * at * population, [2.0, 12.0], rtol=0.0, atol=2e-15)
