from __future__ import annotations

from pathlib import Path

from validators.multi_province.k1b_turn4_anhui_f0364_straddling_zero_mapped_interval_forensic.run import (
    CLASS_A,
    authority_and_comparison,
    branch_diagnostic,
    classify,
    guard_causality_audit,
    load_cell,
    mapped_interval_receipt,
    reproduce_candidates,
    strict_crossing_receipt,
    verify_parent_manifest,
)


REPOSITORY = Path(__file__).resolve().parents[1]


def _objects():
    payload, cell, cell_checks = load_cell(REPOSITORY)
    reproduction = reproduce_candidates(payload)
    crossing = strict_crossing_receipt(reproduction)
    mapping = mapped_interval_receipt(cell)
    branches = [branch_diagnostic(cell, mapping, branch) for branch in ("backward", "forward")]
    guard = guard_causality_audit(REPOSITORY, crossing, mapping)
    authority = authority_and_comparison(REPOSITORY, mapping)
    return cell_checks, reproduction, crossing, mapping, branches, guard, authority


def test_exact_parent_cell_and_source_binding() -> None:
    assert verify_parent_manifest(REPOSITORY)["status"] == "PASS"
    checks, reproduction, *_ = _objects()
    assert all(checks.values())
    assert reproduction["status"] == "PASS"
    assert len(reproduction["candidates"]) == 8


def test_only_backward_liquid_negative_transfer_pair_strictly_crosses() -> None:
    _, _, crossing, *_ = _objects()
    assert crossing["status"] == "PASS"
    assert crossing["checks"] == {
        "backward_strict_crossing": True,
        "forward_not_strict_crossing": True,
    }


def test_negative_ratio_mapping_straddles_zero_with_nonempty_positive_intersection() -> None:
    _, _, _, mapping, *_ = _objects()
    assert mapping["d_z"] == -5.840722762648187
    assert mapping["d3_ratio_R"] == -0.3330414721146172
    assert mapping["illiquid_derivative_interval_sorted"] == [
        -0.000536125311776913,
        8.895604077208148e-05,
    ]
    assert mapping["mapped_q_b_interval_sorted"] == [
        -0.000267101992455363,
        0.0016097854371494127,
    ]
    assert mapping["mapped_interval_sign_topology"] == "STRADDLES_ZERO"
    assert mapping["positive_domain_intersection"]["notation"] == "(0,0.0016097854371494127]"


def test_backward_branch_is_unique_fully_admissible_candidate() -> None:
    _, _, _, _, branches, *_ = _objects()
    backward, forward = branches
    assert backward["q_b"] == 0.0015039676061569449
    assert backward["q_a"] == -0.0005008835855672058
    assert backward["domain_pass"] is True
    assert backward["transfer_kkt_residual"] == 0.0
    assert backward["raw_g_a"] == backward["g_a"] == 0.0
    assert backward["g_b"] == -17.978717494437753
    assert backward["hamiltonian"] == -0.06734914681687235
    assert all(backward["downstream_checks"].values())
    assert backward["admissible"] is True
    assert forward["q_b"] == 0.008487587452625978
    assert forward["domain_pass"] is False
    assert forward["domain_checks"]["q_b_in_whole_mapped_interval"] is False
    assert forward["domain_checks"]["q_a_in_original_closed_derivative_interval"] is False
    assert forward["admissible"] is False


def test_whole_interval_guard_is_earliest_causal_exit() -> None:
    _, _, _, _, _, guard, _ = _objects()
    assert guard["status"] == "PASS"
    assert guard["earliest_causal_exit"] == "if implied_q_b_interval[0] <= 0.0: return None"
    assert guard["checks"]["whole_interval_positivity_guard_triggers"] is True
    assert guard["backward_branch_q_b_strictly_positive"] is True
    assert guard["backward_branch_membership"] is True


def test_authority_supports_classification_a_without_production_calls() -> None:
    checks, _, crossing, mapping, branches, guard, authority = _objects()
    assert authority["status"] == "PASS"
    assert classify(all(checks.values()), crossing, mapping, branches, guard, authority) == CLASS_A
    assert sum(row["root_invocations"] for row in branches) == 0
