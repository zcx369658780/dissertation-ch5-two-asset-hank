from __future__ import annotations

import numpy as np

from exports import matlab_faithful_two_asset_ha as oracle
from validators.multi_province.k1_g1_vs_g2_ha_hjb_instrumented import run as accepted
from validators.multi_province.k1_g1_vs_g2_ha_hjb_instrumented.instrumented_hjb import solve_with_trace
from validators.multi_province.k1_transfer_control_raw_candidate_census.run import _result_equality
from validators.multi_province.k1_transfer_control_d1_1e5.finalize import arrays_equal, d1_aggregates
from validators.multi_province.k1_transfer_control_d1_1e5.receipt import write_d1_call_chunk


D1 = 1.0e5


def test_finalizer_array_equality_handles_unicode_labels() -> None:
    assert arrays_equal(np.asarray(["B", "F"]), np.asarray(["B", "F"]))
    assert not arrays_equal(np.asarray(["B", "F"]), np.asarray(["B", "0"]))


def test_d1_pure_raw_candidate_filter_is_inclusive_and_never_clips() -> None:
    raw = (-100001.0, 100000.0, -20.0, 30.0)
    result = oracle.select_matlab_faithful_transfer_candidates_from_raw(
        *raw,
        at_lower_a=False,
        at_upper_a=False,
        at_lower_b=False,
        tolerance=1.0e-12,
        transfer_candidate_abs_limit=D1,
    )

    assert result.raw == raw
    assert result.d1_admissible == (False, True, True, True)
    assert result.existing_feasible == (True, True, True, True)
    assert result.d_b == 100000.0
    assert result.d_f == 10.0
    assert result.zero_transfer_available
    assert -100000.0 not in result.raw


def test_d1_keeps_existing_boundary_feasibility_separate_and_zero_available() -> None:
    result = oracle.select_matlab_faithful_transfer_candidates_from_raw(
        -200000.0,
        200001.0,
        -300000.0,
        300001.0,
        at_lower_a=True,
        at_upper_a=False,
        at_lower_b=True,
        tolerance=1.0e-12,
        transfer_candidate_abs_limit=D1,
    )

    assert result.d1_admissible == (False, False, False, False)
    assert result.existing_feasible == (False, True, False, True)
    assert result.d_b == 0.0
    assert result.d_f == 0.0
    assert result.zero_transfer_available


def test_d1_no_hit_fixture_has_exact_scientific_and_raw_parity() -> None:
    args = accepted._fixture()
    off_observations = []
    on_observations = []
    off, _ = solve_with_trace(
        *args,
        iteration_observer=lambda number, values: off_observations.append((number, values)),
    )
    on, _ = solve_with_trace(
        *args,
        iteration_observer=lambda number, values: on_observations.append((number, values)),
        transfer_candidate_abs_limit=D1,
    )

    assert all(_result_equality(off, on).values())
    assert len(off_observations) == len(on_observations)
    for (off_number, off_values), (on_number, on_values) in zip(off_observations, on_observations):
        assert off_number == on_number
        for branch in ("d_bb", "d_bf", "d_fb", "d_ff"):
            assert np.array_equal(off_values[branch], on_values[branch])
            assert np.max(np.abs(off_values[branch])) <= D1


def test_d1_comparison_observer_and_lossless_receipt_roundtrip(tmp_path) -> None:
    args = accepted._fixture()
    observations = []
    result, _ = solve_with_trace(
        *args,
        transfer_candidate_abs_limit=D1,
        policy_comparison_observer=lambda number, values: observations.append((number, values)),
    )
    assert observations
    assert all(not value.flags.writeable for _, values in observations for value in values.values())
    assert all(np.array_equal(values["selected_transfer"], values["control_transfer"])
               for _, values in observations)

    path = tmp_path / "d1_call.npz"
    receipt = write_d1_call_chunk(
        path,
        observations,
        grid=args[0],
        numerics=args[-1],
        metadata={"path_id": "D1", "turn": 2, "province": "fixture"},
        d1_active=True,
        final_converged=result.converged,
        final_convergence_statistic=result.convergence_statistic,
    )
    assert receipt["d1_inadmissible_count"] == 0
    assert receipt["winner_changed_count"] == 0
    with np.load(path, allow_pickle=False) as payload:
        assert payload["raw_d"].shape == (len(observations), 4, 2, 2, 2)
        assert bool(np.all(payload["d1_admissible"]))
        assert not bool(np.any(payload["winner_changed"]))
        raw_shape = payload["raw_d"].shape
        bits = np.asarray(payload["boundary_bits"])
        expected = {
            "INTERIOR": int(np.count_nonzero(np.broadcast_to(bits == 0, raw_shape))),
            "LOWER_A": int(np.count_nonzero(np.broadcast_to((bits & 1) != 0, raw_shape))),
            "UPPER_A": int(np.count_nonzero(np.broadcast_to((bits & 2) != 0, raw_shape))),
            "LOWER_B": int(np.count_nonzero(np.broadcast_to((bits & 4) != 0, raw_shape))),
            "UPPER_B": int(np.count_nonzero(np.broadcast_to((bits & 8) != 0, raw_shape))),
        }

    aggregates, _, _ = d1_aggregates({(2, "fixture"): path})
    assert {
        name: row["raw_candidate_count"]
        for name, row in aggregates["by_boundary"].items()
    } == expected
