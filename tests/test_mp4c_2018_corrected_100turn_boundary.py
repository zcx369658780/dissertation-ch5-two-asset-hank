"""Static and synthetic gates for the bounded trajectory; no scientific calls."""
from types import SimpleNamespace

import numpy as np
from scipy import sparse

from validators.multi_province.corrected_2018_100turn_boundary import finalize, run


def _summary(ra: int, wage: int) -> dict:
    return {
        "firm_rate_regions": {"lower": ra, "interior": 31 - ra, "upper": 0},
        "wage_regions": {"lower": 0, "interior": 31 - wage, "upper": wage},
    }


def test_literal_science_budget_and_second_run_guards() -> None:
    source = open(run.__file__, encoding="utf-8").read()
    assert "for turn_index in range(1, 101):" in source
    assert '>= 3100' in source
    assert '"authorized_turns": 100' in source
    assert "scientific trajectory already started; retry prohibited" in source


def test_live_predecessor_package_hashes_are_bound() -> None:
    paths = {
        "turn_by_turn_observables": run.ACCEPTED_DIR / "turn_by_turn_observables.json",
        "transition_summary": run.ACCEPTED_DIR / "transition_summary.json",
        "manifest": run.ACCEPTED_DIR / "manifest.json",
    }
    assert {name: run.single.file_sha256(path) for name, path in paths.items()} == run.ACCEPTED_SHA256


def test_window_classifier_zero_partial_persistent_and_oscillatory() -> None:
    zero = [_summary(max(0, 10 - i), max(0, 10 - i)) for i in range(100)]
    partial = [_summary(max(2, 20 - i // 3), 5) for i in range(100)]
    persistent = [_summary(31, 31) for _ in range(100)]
    oscillatory = [_summary(20 + (i % 2) * 5, 20) for i in range(100)]
    assert run.classify_boundary_path(zero, "ra") == "BOUNDARY_HITS_DECAY_TO_ZERO"
    assert run.classify_boundary_path(partial, "ra") == "BOUNDARY_HITS_MATERIALLY_DECLINE_BUT_NOT_ZERO"
    assert run.classify_boundary_path(persistent, "ra") == "BOUNDARY_HITS_PERSIST_HIGH"
    assert run.classify_boundary_path(oscillatory, "ra") == "BOUNDARY_HITS_OSCILLATE_WITHOUT_DECAY"


def test_primary_verdict_requires_both_price_families_to_improve() -> None:
    both_zero = [_summary(max(0, 10 - i), max(0, 8 - i)) for i in range(100)]
    one_persistent = [_summary(max(0, 10 - i), 31) for i in range(100)]
    assert run.trajectory_verdict(both_zero) == run.VERDICT_PASS
    assert run.trajectory_verdict(one_persistent) == run.VERDICT_FAIL


def test_hjb_operator_diagnostic_preserves_negative_offdiagonal_blocker() -> None:
    operator = sparse.csr_matrix(np.array([[-1.0, -0.2], [0.1, -1.0]]))
    hjb = SimpleNamespace(post_convergence_operator=SimpleNamespace(full=operator))
    result = run.hjb_operator_diagnostics(hjb)
    assert result["classification"] == "DIAGNOSTIC_ONLY"
    assert result["negative_offdiagonal_count"] == 1
    assert result["minimum_offdiagonal"] == -0.2


def test_persistent_offender_uses_longest_consecutive_run() -> None:
    rows = [
        {"family": "ra", "bound": "lower", "province": "安徽", "turn": turn}
        for turn in (1, 2, 4, 5, 6)
    ]
    result = finalize.longest_runs(rows)
    assert result[0]["longest_consecutive_turns"] == 3
    assert result[0]["run_start"] == 4
    assert result[0]["run_end"] == 6
