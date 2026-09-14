from __future__ import annotations

import numpy as np
import pytest

from validators.multi_province.k1_household_asset_grid_precision_sensitivity import (
    finalize,
    run,
)


def test_exact_precision_ladders_and_frozen_state() -> None:
    assert run.PHASE_POINTS == {
        "P1": ((20, 40), (20, 80), (20, 160)),
        "P2": ((40, 160), (80, 160)),
    }
    p1 = [run.precision_spec("P1", index) for index in range(3)]
    assert [item["da"] for item in p1] == pytest.approx(
        [100.0 / 39.0, 100.0 / 79.0, 100.0 / 159.0]
    )
    assert all(item["I"] == 20 and item["db"] == pytest.approx(22.0 / 19.0) for item in p1)
    p2 = [run.precision_spec("P2", index) for index in range(2)]
    assert [(item["I"], item["J"]) for item in p2] == [(40, 160), (80, 160)]
    assert [item["db"] for item in p2] == pytest.approx([22.0 / 39.0, 22.0 / 79.0])
    for item in p1 + p2:
        assert (item["rb"], item["ra"], item["wage"], item["h"]) == (0.02, 0.0675, 15.5, 1.0)
        assert (item["amin"], item["amax"], item["bmin"], item["bmax"]) == (0.0, 100.0, -2.0, 20.0)


def test_outside_precision_ladder_is_rejected_without_initialization() -> None:
    with pytest.raises(ValueError, match="outside"):
        run.precision_spec("P1", 3)
    with pytest.raises(ValueError, match="phase"):
        run.precision_spec("P3", 0)


def test_signed_cdf_distance_is_deterministic_and_zero_for_identity() -> None:
    grid = np.array([0.0, 1.0, 2.0])
    mass = np.array([0.2, 0.5, 0.3])
    assert finalize.signed_cdf_l1_distance(grid, mass, grid, mass) == pytest.approx(0.0)
    coarse_grid = np.array([0.0, 2.0])
    coarse_mass = np.array([0.2, 0.8])
    first = finalize.signed_cdf_l1_distance(grid, mass, coarse_grid, coarse_mass)
    second = finalize.signed_cdf_l1_distance(coarse_grid, coarse_mass, grid, mass)
    assert first == pytest.approx(second)
    assert first > 0.0


def test_runner_contains_no_forbidden_routes_or_warm_start_parameter() -> None:
    text = run.Path(run.__file__).read_text(encoding="utf-8")
    for forbidden in (
        "evaluate_firm(", "solve_multi_province", "solve_steady_state(",
        "matlab.engine", "subprocess", "os.system", "warm_start=",
    ):
        assert forbidden not in text
