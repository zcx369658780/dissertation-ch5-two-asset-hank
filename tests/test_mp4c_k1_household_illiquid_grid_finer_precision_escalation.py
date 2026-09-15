from __future__ import annotations

import numpy as np
import pytest

from validators.multi_province.k1_household_illiquid_grid_finer_precision_escalation import (
    finalize,
    run,
)


def test_exact_finer_ladder_and_frozen_state() -> None:
    assert run.POINTS == ((20, 320), (20, 640), (20, 1280))
    specs = [run.precision_spec(index) for index in range(3)]
    assert [item["da"] for item in specs] == pytest.approx(
        [100.0 / 319.0, 100.0 / 639.0, 100.0 / 1279.0]
    )
    for item in specs:
        assert (item["I"], item["Nz"]) == (20, 2)
        assert (item["amin"], item["amax"], item["bmin"], item["bmax"]) == (
            0.0,
            100.0,
            -2.0,
            20.0,
        )
        assert (item["rb"], item["ra"], item["wage"], item["h"]) == (
            0.02,
            0.0675,
            15.5,
            1.0,
        )


def test_outside_finer_ladder_is_rejected() -> None:
    with pytest.raises(ValueError, match="outside"):
        run.precision_spec(3)
    with pytest.raises(ValueError, match="outside"):
        run.precision_spec(-1)


def test_runner_contains_no_forbidden_routes_or_warm_start() -> None:
    text = run.Path(run.__file__).read_text(encoding="utf-8")
    for forbidden in (
        "evaluate_firm(",
        "solve_multi_province",
        "solve_steady_state(",
        "matlab.engine",
        "warm_start=",
        "2560",
        "5120",
    ):
        assert forbidden not in text


def test_accepted_reference_is_j160_and_reused_without_runtime() -> None:
    point = finalize.accepted_reference()
    assert (point["specification"]["I"], point["specification"]["J"]) == (20, 160)
    assert point["accepted_evidence_reused_without_runtime"] is True
    assert point["kfe"]["aggregates"]["At"] == pytest.approx(89.29782530984971)


def test_signed_quantiles_are_deterministic_when_supported() -> None:
    grid = np.array([0.0, 1.0, 2.0, 3.0])
    mass = np.array([0.1, 0.4, 0.3, 0.2])
    assert finalize.upper_quantile_locations(grid, mass) == {
        "p90": 3.0,
        "p95": 3.0,
        "p99": 3.0,
    }
    assert finalize.upper_quantile_locations(grid, np.array([0.2, -0.1, 0.6, 0.3])) is None


def test_frozen_signed_cdf_method_is_reused() -> None:
    grid = np.array([0.0, 1.0, 2.0])
    first = np.array([0.2, 0.5, 0.3])
    second = np.array([0.1, 0.6, 0.3])
    assert finalize.signed_cdf_l1_distance(grid, first, grid, first) == pytest.approx(0.0)
    assert finalize.signed_cdf_l1_distance(grid, first, grid, second) == pytest.approx(
        finalize.signed_cdf_l1_distance(grid, second, grid, first)
    )


def test_live_source_and_accepted_j160_hash_preflight_passes() -> None:
    receipt = run.source_receipt()
    assert receipt["pass"] is True
    assert receipt["oracle"]["actual_sha256"] == receipt["oracle"]["expected_sha256"]
    assert receipt["matlab"]["actual_sha256"] == receipt["matlab"]["expected_sha256"]
    assert all(
        item["actual_sha256"] == item["expected_sha256"]
        for item in receipt["accepted_j160_evidence"].values()
    )
