from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np
import pytest

from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import (
    MONOTONICITY_RELAXATION_EXHAUSTED,
    FailClosed,
    monotonicity_preserving_relaxation,
)


REPO = Path(__file__).resolve().parents[1]
PROVINCE = REPO / (
    "reports/ch5_mp4c_lower_a_interior_z_composition_repair_turn1_parity_"
    "turn2_run004_20260921/household/p07_黑龙江"
)
B_NODES = np.linspace(-2.0, 5.0, 20)
SHAPE = (20, 20, 2)


def field_sha256(value: np.ndarray) -> str:
    return hashlib.sha256(np.asarray(value, dtype="<f8").tobytes(order="F")).hexdigest().upper()


def increasing_value(slope: float = 1.0, offset: float = 0.0) -> np.ndarray:
    line = offset + slope * np.arange(20, dtype=np.float64)
    return np.broadcast_to(line[:, None, None], SHAPE).copy()


def load_update(checkpoint: int) -> tuple[np.ndarray, np.ndarray]:
    directory = PROVINCE / f"checkpoint_{checkpoint:03d}"
    with np.load(directory / "checkpoint_arrays.npz", allow_pickle=False) as saved:
        old = np.array(saved["value"], copy=True)
    with np.load(directory / "direct_update_arrays.npz", allow_pickle=False) as saved:
        full = np.array(saved["next_value"], copy=True)
    return old, full


def test_alpha_one_returns_full_candidate_bitwise_unchanged():
    old, full = load_update(0)
    accepted, receipt = monotonicity_preserving_relaxation(old, full, B_NODES)
    assert accepted.tobytes(order="F") == full.tobytes(order="F")
    assert receipt["accepted_alpha"] == 1.0
    assert receipt["accepted_halvings"] == 0
    assert receipt["attempts"][0]["positive_edges"] == 760


def test_one_halving_exact_persisted_replay():
    old, full = load_update(2)
    accepted, receipt = monotonicity_preserving_relaxation(old, full, B_NODES)
    assert receipt["accepted_alpha"] == 0.5
    assert receipt["accepted_halvings"] == 1
    assert field_sha256(accepted) == "987A20DE9252104ECFAB59436433F0C73EEB8C513589B8B0FA98DB64018B66BF"
    assert receipt["attempts"][-1]["minimum_raw_b_slope"] == 0.005032838660371801
    assert receipt["attempts"][-1]["positive_edges"] == 760
    assert receipt["accepted_value_change_inf"] == 0.017682618173863407


@pytest.mark.parametrize("which", ["old", "full"])
def test_nonfinite_input_rejects(which: str):
    old = increasing_value(1.0)
    full = increasing_value(2.0, 1.0)
    (old if which == "old" else full)[0, 0, 0] = np.nan
    with pytest.raises(FailClosed) as caught:
        monotonicity_preserving_relaxation(old, full, B_NODES)
    assert caught.value.terminal == "FAIL__MONOTONICITY_PRESERVING_HJB_RELAXATION_INPUT_INVALID"


def test_wrong_shape_rejects():
    with pytest.raises(FailClosed) as caught:
        monotonicity_preserving_relaxation(
            np.zeros((19, 20, 2)), np.zeros(SHAPE), B_NODES
        )
    assert caught.value.terminal == "FAIL__MONOTONICITY_PRESERVING_HJB_RELAXATION_INPUT_INVALID"


def test_bitwise_stagnation_rejects_and_exhausts_exactly():
    old = increasing_value(1.0)
    with pytest.raises(FailClosed) as caught:
        monotonicity_preserving_relaxation(old, old.copy(), B_NODES)
    assert caught.value.terminal == MONOTONICITY_RELAXATION_EXHAUSTED
    assert len(caught.value.detail["attempts"]) == 53
    assert all(row["bitwise_identical_to_value_old"] for row in caught.value.detail["attempts"])


def test_signed_zero_difference_is_not_bitwise_stagnation():
    old = increasing_value(1.0)
    full = old.copy()
    full[0, 0, 0] = -0.0
    accepted, receipt = monotonicity_preserving_relaxation(old, full, B_NODES)
    assert accepted.tobytes(order="F") == full.tobytes(order="F")
    assert receipt["accepted_alpha"] == 1.0
    assert receipt["attempts"][0]["bitwise_identical_to_value_old"] is False


def test_no_positive_slope_candidate_exhausts_exact_terminal():
    old = np.zeros(SHAPE, dtype=np.float64)
    full = -increasing_value(1.0)
    with pytest.raises(FailClosed) as caught:
        monotonicity_preserving_relaxation(old, full, B_NODES)
    assert caught.value.terminal == MONOTONICITY_RELAXATION_EXHAUSTED
    assert [row["halvings"] for row in caught.value.detail["attempts"]] == list(range(53))


def test_zero_slope_fails_strict_positivity_then_half_passes():
    old = increasing_value(1.0)
    full = np.ones(SHAPE, dtype=np.float64)
    _, receipt = monotonicity_preserving_relaxation(old, full, B_NODES)
    assert receipt["attempts"][0]["zero_edges"] == 760
    assert receipt["attempts"][0]["strict_positive_pass"] is False
    assert receipt["accepted_alpha"] == 0.5


def test_no_positive_slope_magnitude_floor():
    old = np.zeros(SHAPE, dtype=np.float64)
    full = increasing_value(np.finfo(np.float64).tiny)
    accepted, receipt = monotonicity_preserving_relaxation(old, full, np.arange(20.0))
    assert np.array_equal(accepted, full)
    assert 0.0 < receipt["attempts"][0]["minimum_raw_b_slope"] < 1.0e-300
    assert receipt["accepted_alpha"] == 1.0
