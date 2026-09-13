from __future__ import annotations

import json

import numpy as np

from validators.multi_province.k1_g1_vs_g2_ha_hjb_instrumented import run as accepted
from validators.multi_province.k1_g1_vs_g2_ha_hjb_instrumented.instrumented_hjb import solve_with_trace
from validators.multi_province.k1_transfer_control_raw_candidate_census.census import (
    BRANCHES, boundary_bits, selected_raw_masks, write_call_chunk,
)
from validators.multi_province.k1_transfer_control_raw_candidate_census.run import _result_equality


def test_iteration_observer_is_read_only_and_scientifically_neutral() -> None:
    args = accepted._fixture()
    baseline, _ = solve_with_trace(*args)
    observations = []

    def observe(number, values):
        observations.append((number, values))

    actual, trace = solve_with_trace(*args, iteration_observer=observe)
    assert all(_result_equality(baseline, actual).values())
    assert len(observations) == len(trace["iterations"])
    assert all(not value.flags.writeable for _, values in observations for value in values.values())
    assert set(observations[0][1]) == {
        *BRANCHES, "selected_transfer", "selected_adjustment_cost", "transfer_label",
    }


def test_selected_raw_masks_reconstruct_composite_and_boundary_controls() -> None:
    raw = np.zeros((1, 4, 2, 3, 1))
    labels = np.asarray([[[["B"], ["F"], ["B"]], [["0"], ["B"], ["F"]]]])
    raw[:, 0] = -2.0
    raw[:, 1] = 3.0
    raw[:, 2] = -5.0
    raw[:, 3] = 7.0
    mask, direction = selected_raw_masks(raw, labels, 1e-12)
    reconstructed = np.sum(np.where(mask, raw, 0.0), axis=1)
    assert reconstructed[0, 0, 0, 0] == 3.0
    assert reconstructed[0, 0, 1, 0] == 2.0
    assert reconstructed[0, 0, 2, 0] == -2.0
    assert reconstructed[0, 1, 0, 0] == 0.0
    assert reconstructed[0, 1, 1, 0] == 1.0
    assert reconstructed[0, 1, 2, 0] == -5.0
    assert direction[0, :, 0, 0, 0].tolist() == [True, True, False, False]
    assert boundary_bits((2, 3, 1))[:, 1, 0].tolist() == [4, 8]


def test_lossless_call_chunk_roundtrip_and_reconciliation(tmp_path) -> None:
    args = accepted._fixture()
    observations = []
    result, _ = solve_with_trace(*args, iteration_observer=lambda number, values: observations.append((number, values)))
    path = tmp_path / "call.npz"
    receipt = write_call_chunk(
        path, observations, grid=args[0], numerics=args[-1],
        metadata={"path_id": "G1", "province": "fixture"},
        final_converged=result.converged,
        final_convergence_statistic=result.convergence_statistic,
    )
    assert receipt["raw_candidate_count"] == len(observations) * 4 * 8
    assert receipt["raw_candidate_count"] == receipt["raw_finite_count"]
    assert receipt["selected_transfer_reconstruction_equal_count"] == len(observations) * 8
    with np.load(path, allow_pickle=False) as payload:
        assert payload["raw_d"].shape == (len(observations), 4, 2, 2, 2)
        assert json.loads(str(payload["metadata_json"]))["province"] == "fixture"
