from pathlib import Path
import importlib.util

import numpy as np


REPO = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO / "validators/multi_province/monotonicity_preserving_hjb_relaxation_scientific_design_gate/run.py"
SPEC = importlib.util.spec_from_file_location("relaxation_gate", MODULE_PATH)
run = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(run)


def inputs():
    return run.load_inputs(REPO)


def test_all_three_updates_have_760_affine_edge_constraints():
    states, _ = inputs()
    rows = [run.feasibility(states[n], states[n + 1], f"{n}->{n+1}") for n in range(3)]
    assert [row["edge_count"] for row in rows] == [760, 760, 760]
    assert [row["full_all_strictly_positive"] for row in rows] == [True, True, False]
    assert rows[0]["unrestricted_critical_alpha"] > 1
    assert rows[1]["unrestricted_critical_alpha"] > 1


def test_checkpoint2_to_3_binding_edge_and_critical_alpha_are_exact():
    states, _ = inputs()
    row = run.feasibility(states[2], states[3], "2->3")
    edge = row["binding_edge"]
    assert edge["left_flat_f_zero_based"] == 62
    assert edge["right_flat_f_zero_based"] == 63
    assert edge["old_slope"] == 0.018363586699392222
    assert edge["full_candidate_slope"] == -0.0002428532863339202
    assert row["unrestricted_critical_alpha"] == 0.9869478908098366
    assert len(row["constraints_binding_inside_0_1"]) == 2


def test_deterministic_halving_is_inactive_then_accepts_half():
    states, _ = inputs()
    chosen = [run.halving_alpha(states[n], states[n + 1]) for n in range(3)]
    assert chosen == [(1.0, 0), (1.0, 0), (0.5, 1)]
    replay = run.replay(states[2], states[3], "halving", 0.5)
    assert replay["strict_positive_pass"]
    assert replay["positive_edges"] == 760
    assert replay["minimum_raw_b_slope"] == 0.005032838660371801


def test_single_float_predecessor_does_not_guarantee_represented_strict_positivity():
    states, _ = inputs()
    critical = run.feasibility(states[2], states[3], "2->3")["unrestricted_critical_alpha"]
    receipt = run.predecessor_diagnostic(states[2], states[3], critical)
    assert receipt["single_predecessor_is_sufficient"] is False
    assert receipt["first_passing_predecessor_steps_with_prescribed_convex_expression"] == 4
    assert receipt["first_passing_row"]["minimum_raw_b_slope"] > 0


def test_relaxed_state_does_not_claim_frozen_linear_system_solution():
    states, updates = inputs()
    full = run.residual_diagnostic(updates[2], states[2], 1.0, "full")
    half = run.residual_diagnostic(updates[2], states[2], 0.5, "half")
    assert full["frozen_checkpoint2_residual_inf"] < 2e-14
    assert half["frozen_checkpoint2_residual_inf"] > 1e-3
