import ast
from pathlib import Path

import numpy as np
import pytest

from validators.multi_province.k1_j160_cross_state_finalizer_common_support_repair import (
    finalize,
)


def legacy_same_support_distance(x1, m1, x2, m2):
    common = np.union1d(x1, x2)
    cdf1 = np.interp(common, x1, np.cumsum(m1))
    cdf2 = np.interp(common, x2, np.cumsum(m2))
    return float(np.trapezoid(np.abs(cdf1 - cdf2), common) / (common[-1] - common[0]))


def test_same_support_exactly_regresses_accepted_metric():
    x1 = np.array([0.0, 1.0, 3.0])
    m1 = np.array([0.2, -0.05, 0.85])
    x2 = np.array([0.0, 2.0, 3.0])
    m2 = np.array([0.1, 0.4, 0.5])
    expected = legacy_same_support_distance(x1, m1, x2, m2)
    assert finalize.domain_plus_grid_cdf_distance(x1, m1, x2, m2) == expected


@pytest.mark.parametrize(
    "x1,x2",
    [
        (np.linspace(0.0, 10.0, 20), np.linspace(0.0, 100.0, 160)),
        (np.linspace(-2.0, 5.0, 20), np.linspace(-2.0, 20.0, 20)),
    ],
)
def test_different_support_is_finite_deterministic(x1, x2):
    m1 = np.linspace(-1e-18, 1.0, x1.size)
    m2 = np.linspace(1.0, -2e-18, x2.size)
    first = finalize.domain_plus_grid_cdf_distance(x1, m1, x2, m2)
    second = finalize.domain_plus_grid_cdf_distance(x1, m1, x2, m2)
    assert np.isfinite(first)
    assert first == second


def test_cdf_extension_uses_zero_below_and_raw_total_above():
    grid = np.array([1.0, 2.0, 4.0])
    mass = np.array([0.3, -0.2, 0.5])
    probes = np.array([0.0, 1.0, 3.0, 4.0, 5.0])
    actual = finalize.extended_raw_signed_cdf(grid, mass, probes)
    assert actual[0] == 0.0
    assert actual[-1] == pytest.approx(0.6)
    assert actual[1] == pytest.approx(0.3)
    assert actual[2] == pytest.approx(0.35)


def test_signed_mass_is_not_clipped_or_renormalized():
    grid = np.array([0.0, 1.0, 2.0])
    mass = np.array([0.4, -0.3, 0.2])
    probes = np.array([0.0, 1.0, 2.0, 3.0])
    assert finalize.extended_raw_signed_cdf(grid, mass, probes).tolist() == pytest.approx(
        [0.4, 0.1, 0.3, 0.3]
    )


@pytest.mark.parametrize(
    "grid,mass",
    [
        ([0.0], [1.0]),
        ([0.0, 0.0], [0.5, 0.5]),
        ([1.0, 0.0], [0.5, 0.5]),
        ([0.0, 1.0], [1.0]),
        ([0.0, np.nan], [0.5, 0.5]),
        ([0.0, 1.0], [0.5, np.inf]),
    ],
)
def test_invalid_or_zero_width_support_fails_closed(grid, mass):
    with pytest.raises(ValueError):
        finalize.domain_plus_grid_cdf_distance(grid, mass, [0.0, 1.0], [0.5, 0.5])


def test_task_owned_finalizer_has_no_solver_or_run_imports():
    tree = ast.parse(Path(finalize.__file__).read_text(encoding="utf-8"))
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    assert not any("solver" in name.lower() or name.endswith(".run") for name in imports)
