from __future__ import annotations

from pathlib import Path

from validators.multi_province.turn2_f0364_negative_ratio_switching_forensic.run import (
    CLASS_A,
    authority_audit,
    classify,
    load_cell,
    ratio_receipt,
    reproduce_candidates,
    strict_crossing_receipt,
    switching_diagnostic,
    verify_parent_manifest,
)


REPOSITORY = Path(__file__).resolve().parents[1]


def _objects():
    payload, cell, checks = load_cell(REPOSITORY)
    reproduction = reproduce_candidates(payload)
    crossing = strict_crossing_receipt(reproduction)
    ratio = ratio_receipt(cell)
    backward = switching_diagnostic(cell, ratio, "backward")
    forward = switching_diagnostic(cell, ratio, "forward")
    authority = authority_audit(REPOSITORY)
    return checks, reproduction, crossing, ratio, backward, forward, authority


def test_exact_parent_and_failure_cell_binding() -> None:
    assert verify_parent_manifest(REPOSITORY)["status"] == "PASS"
    checks, reproduction, *_ = _objects()
    assert all(checks.values())
    assert reproduction["status"] == "PASS"
    assert len(reproduction["candidates"]) == 8


def test_persisted_ordinary_candidates_prove_only_backward_liquid_crossing() -> None:
    _, _, crossing, *_ = _objects()
    assert crossing["status"] == "PASS"
    assert crossing["checks"]["p_b_backward_strict_crossing"] is True
    assert crossing["checks"]["p_b_forward_not_strict_crossing"] is True


def test_negative_ratio_maps_negative_qa_interval_to_positive_qb_interval() -> None:
    _, _, _, ratio, *_ = _objects()
    assert ratio["d_z"] == -7.8384208979658965
    assert ratio["d3_ratio_R"] == -0.7547777451261338
    assert ratio["sign_aware_mapped_positive_q_b_interval"] == [
        0.004111019263931103,
        0.006526149020033277,
    ]
    assert ratio["checks"]["p_b_backward_inside"] is True
    assert ratio["checks"]["p_b_forward_outside"] is True


def test_backward_shadow_is_unique_numerically_admissible_candidate() -> None:
    _, _, _, _, backward, forward, _ = _objects()
    assert backward["q_a"] == -0.0045978913784868415
    assert backward["raw_g_a"] == backward["g_a"] == 0.0
    assert backward["transfer_kkt"]["satisfied"] is True
    assert backward["b_derivative_direction_consistent"] is True
    assert backward["q_a_in_original_derivative_interval"] is True
    assert backward["rejection_reasons"] == []
    assert backward["admissible"] is True
    assert forward["q_a"] == -0.0061739839155502164
    assert forward["admissible"] is False
    assert forward["rejection_reasons"] == [
        "INTERIOR_A_SWITCHING_SHADOW_OUTSIDE_DERIVATIVE_INTERVAL",
        "B_DERIVATIVE_DIRECTION_INCONSISTENT",
    ]
    assert backward["root_invocations"] == forward["root_invocations"] == 0


def test_authority_and_classification_are_a_without_selector_call() -> None:
    checks, _, crossing, _, backward, forward, authority = _objects()
    assert authority["status"] == "PASS"
    assert authority["explicit_accepted_authority_requires_q_a_positive"] is False
    assert authority["explicit_accepted_authority_requires_d3_ratio_positive"] is False
    assert authority["explicit_accepted_authority_requires_interior_a_switching_ratio_positive"] is False
    assert authority["ratio_positive_is_current_implementation_guard"] is True
    assert classify(all(checks.values()), crossing, backward, forward, authority) == CLASS_A
