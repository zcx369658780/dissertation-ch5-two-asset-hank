from __future__ import annotations

import hashlib
import json

import numpy as np
import pytest

from validators.multi_province.k1_transfer_control_admissibility_design.analyze import (
    analyze_evidence,
    adjudicate_candidate,
    assess_raw_candidate_resolution,
    exact_interval_hits,
    raw_summary_interval_bounds,
    summarize_numeric,
    write_outputs,
)


def test_numeric_summary_and_raw_resolution_keep_receipts_distinct() -> None:
    summary = summarize_numeric(np.array([-10.0, -1.0, 0.0, 2.0, np.nan, np.inf]))

    assert summary["count"] == 6
    assert summary["finite_count"] == 4
    assert summary["nan_count"] == 1
    assert summary["positive_infinity_count"] == 1
    assert summary["positive_share_of_finite"] == 0.25
    assert summary["negative_share_of_finite"] == 0.5
    assert summary["quantiles"]["p50"] == -0.5
    assert summary["abs_quantiles"]["p100"] == 10.0
    assert summary["positive_tail_quantiles"]["p100"] == 2.0
    assert summary["absolute_negative_tail_quantiles"]["p100"] == 10.0

    resolution = assess_raw_candidate_resolution(
        {
            "count": 800,
            "nonfinite_count": 0,
            "min": -10.0,
            "median": 0.0,
            "p95": 2.0,
            "p99": 5.0,
            "max": 9.0,
            "sha256": "A" * 64,
        }
    )
    assert resolution["raw_candidate_arrays_persisted"] is False
    assert resolution["exact_hit_shares_supported"] is False
    assert resolution["available_order_statistics"] == ["min", "median", "p95", "p99", "max"]


def test_interval_adjudication_separates_exact_values_from_summary_bounds() -> None:
    exact = exact_interval_hits(np.array([-11.0, -10.0, 0.0, 10.0, 12.0]), -10.0, 10.0)
    assert exact == {
        "count": 5,
        "preserved_unchanged_count": 3,
        "inadmissible_count": 2,
        "hit_share": 0.4,
        "lower_hit_count": 1,
        "upper_hit_count": 1,
    }

    bounds = raw_summary_interval_bounds(
        [
            {"count": 4, "nonfinite_count": 0, "min": -2.0, "max": 2.0},
            {"count": 4, "nonfinite_count": 0, "min": -12.0, "max": 3.0},
            {"count": 4, "nonfinite_count": 0, "min": -3.0, "max": 13.0},
        ],
        -10.0,
        10.0,
    )
    assert bounds["represented_candidate_count"] == 12
    assert bounds["definite_inadmissible_lower_bound"] == 2
    assert bounds["possible_inadmissible_upper_bound"] == 8
    assert bounds["exact_hit_share_supported"] is False

    outside = adjudicate_candidate(-12.0, -10.0, 10.0)
    assert outside == {
        "raw_status": "inadmissible_lower",
        "A_candidate_rejection": "excluded",
        "B_candidate_clipping": -10.0,
        "C_fallback_to_existing_zero": "excluded__existing_zero_remains",
    }
    assert adjudicate_candidate(3.0, -10.0, 10.0)["B_candidate_clipping"] == 3.0


def test_evidence_analysis_reports_exact_selected_hits_and_bounded_raw_hits(tmp_path) -> None:
    relative_trace = "annual_g1_guarded/turn_02/instrumentation/p00_Test_hjb_trace.json"
    relative_npz = "annual_g1_guarded/turn_02/household/p00_Test/hjb_return.npz"
    relative_obs = "annual_g1_guarded/turn_02/per_province_observables.json"
    trace_path = tmp_path / relative_trace
    npz_path = tmp_path / relative_npz
    obs_path = tmp_path / relative_obs
    trace_path.parent.mkdir(parents=True)
    npz_path.parent.mkdir(parents=True)
    obs_path.parent.mkdir(parents=True, exist_ok=True)

    candidate_summary = {
        "count": 4,
        "nonfinite_count": 0,
        "min": -20.0,
        "median": 0.0,
        "p95": 15.0,
        "p99": 19.0,
        "max": 20.0,
        "abs_max": 20.0,
        "sha256": "A" * 64,
        "abs_max_witness": {"grid_index_zero_based": {"i_b": 0, "i_a": 0, "i_z": 0}, "value": -20.0},
    }
    trace = {
        "schema": "CH5_K1_G1_VS_G2_HA_HJB_ITERATION_TRACE_V1",
        "path_id": "G1",
        "province": "Test",
        "province_index": 0,
        "turn": 2,
        "final_converged": False,
        "final_convergence_statistic": 1.0,
        "iterations": [{
            "iteration": 1,
            "candidate_objects": {name: candidate_summary for name in ("d_bb", "d_bf", "d_fb", "d_ff")},
            "checkpoint_cells": [],
        }],
    }
    trace_path.write_text(json.dumps(trace), encoding="utf-8")
    np.savez(
        npz_path,
        transfer=np.array([[[-20.0], [0.0]], [[5.0], [30.0]]]),
        adjustment_cost=np.ones((2, 2, 1)),
        transfer_label=np.array([[['B'], ['0']], [['F'], ['B']]]),
    )
    obs_path.write_text(json.dumps([{
        "province": "Test",
        "province_index": 0,
        "return_guard_lower_hit": False,
        "return_guard_upper_hit": True,
        "return_guard_unsaturated": False,
        "wage_guard_lower_hit": False,
        "wage_guard_upper_hit": False,
        "wage_guard_unsaturated": True,
    }]), encoding="utf-8")

    entries = []
    for relative in (relative_trace, relative_npz, relative_obs):
        content = (tmp_path / relative).read_bytes()
        entries.append({"path": relative, "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest().upper()})
    manifest_path = tmp_path / "manifest_sha256.json"
    manifest_path.write_text(json.dumps({"schema": "TEST", "file_count": 3, "files": entries}), encoding="utf-8")
    manifest_sha = hashlib.sha256(manifest_path.read_bytes()).hexdigest().upper()

    result = analyze_evidence(tmp_path, manifest_sha, symmetric_thresholds=(10.0,))
    assert result["input_identity"]["consumed_file_hashes_verified"] == 3
    assert result["selected_control"]["overall"]["count"] == 4
    assert result["selected_control"]["symmetric_interval_hits"]["[-10,10]"]["inadmissible_count"] == 2
    assert result["raw_candidates"]["exact_hit_shares_supported"] is False
    assert result["raw_candidates"]["symmetric_interval_bounds"]["[-10,10]"]["definite_inadmissible_lower_bound"] == 8

    outputs = write_outputs(result, tmp_path / "derived")
    assert [path.name for path in outputs] == [
        "analysis.json",
        "raw_candidate_interval_bounds.csv",
        "selected_control_interval_hits.csv",
    ]
    assert json.loads(outputs[0].read_text(encoding="utf-8"))["new_scientific_call_ledger"]["HJB"] == 0
    assert "exact_hit_share_supported" in outputs[1].read_text(encoding="utf-8")
    assert "inadmissible_count" in outputs[2].read_text(encoding="utf-8")
    with pytest.raises(FileExistsError):
        write_outputs(result, tmp_path / "derived")
