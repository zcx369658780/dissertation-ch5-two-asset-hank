from __future__ import annotations

from pathlib import Path

import pytest

from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import FailClosed
from ch5_two_asset_hank.corrected_diagnostic.raw_ra0_safety_panel import _accepted_checkpoint11
from ch5_two_asset_hank.corrected_diagnostic.raw_ra0_turn1_cross_section import (
    PROVINCES,
    _check_ledger,
    _new_ledger,
    compact_recertification,
    derive_cross_section,
)


REPOSITORY = Path(__file__).resolve().parents[1]
CSV = REPOSITORY / "docs/evidence/ch5_mp4c_k1a_payoff_return_reaudit/static_no_feedback_payoff_counterfactual.csv"


def test_exact_turn1_cross_section_derivation() -> None:
    receipt = derive_cross_section(CSV)
    assert receipt["status"] == "PASS"
    assert receipt["row_count"] == 31
    assert [(row["province_index"], row["province"], row["r_a_decimal"]) for row in receipt["rows"]] == list(PROVINCES)
    assert receipt["minimum"] == "0.2826739400149174"
    assert receipt["median"] == "0.4775623850053351"
    assert receipt["maximum"] == "0.8951047990241244"


def test_compact_projection_recertifies_sealed_three_point_evidence(tmp_path: Path) -> None:
    accepted = _accepted_checkpoint11(REPOSITORY)
    receipt = compact_recertification(REPOSITORY, tmp_path, accepted)
    assert receipt["status"] == "PASS"
    assert [row["label"] for row in receipt["points"]] == ["LOW", "MEDIAN", "HIGH"]
    assert all(all(row["checks"].values()) for row in receipt["points"])
    assert receipt["selector_calls"] == receipt["q_assemblies"] == receipt["direct_solves"] == 0


def test_ledger_accepts_exact_budget_and_rejects_overrun() -> None:
    ledger = _new_ledger()
    ledger.update(new_corrected_policy_maps=31, selector_evaluations=24_800, d2_assemblies=31, direct_hjb_solves=31, hjb_updates=31, complete_one_step_cross_section_evaluations=31)
    _check_ledger(ledger)
    ledger["direct_hjb_solves"] = 32
    with pytest.raises(FailClosed):
        _check_ledger(ledger)


def test_all_preregistered_values_are_untransformed_and_inside_global_panel() -> None:
    values = [float(row[2]) for row in PROVINCES]
    assert len(values) == 31
    assert min(values) >= 0.11048158315647279
    assert max(values) <= 1.037811238406538
    assert max(values) > 0.09
