from pathlib import Path
import ast
import json

import numpy as np

from validators.multi_province.k1_hjb_convergence_mechanism.run import _objects
from validators.multi_province.k1_hjb_value_relaxation.relaxed_hjb import (
    ALLOWED_OMEGAS,
    raw_fixed_point_converged,
    relaxed_value_state,
)


def test_only_preregistered_relaxation_values_are_allowed() -> None:
    old = np.array([2.0, -4.0])
    solved = np.array([6.0, 8.0])
    assert ALLOWED_OMEGAS == (0.5, 1.0)
    assert np.array_equal(relaxed_value_state(old, solved, 1.0), solved)
    assert np.array_equal(relaxed_value_state(old, solved, 0.5), 0.5 * old + 0.5 * solved)
    try:
        relaxed_value_state(old, solved, 0.25)
    except ValueError:
        pass
    else:
        raise AssertionError("an unregistered omega was accepted")


def test_convergence_uses_raw_gap_not_mechanically_halved_update() -> None:
    old = np.array([0.0])
    solved = np.array([1.5e-7])
    relaxed = relaxed_value_state(old, solved, 0.5)
    assert np.max(np.abs(relaxed - old)) < 1e-7
    assert np.max(np.abs(solved - old)) >= 1e-7
    assert raw_fixed_point_converged(old, solved, 1e-7) is False


def test_frozen_grid_parameters_and_numerics() -> None:
    grid, params, numerics = _objects()
    assert np.array_equal(grid.b, np.linspace(-2, 5, 20))
    assert np.array_equal(grid.a, np.linspace(0, 10, 20))
    assert np.array_equal(grid.z, np.array([0.8, 1.3]))
    assert params.rho == 0.05 and params.chi_0 == 0.1 and params.chi_1 == 2.0
    assert numerics.delta == 1000.0 and numerics.convergence_tolerance == 1e-7
    assert numerics.max_iterations == 100 and numerics.drift_tolerance == 1e-12


def test_runner_has_no_forbidden_runtime_calls() -> None:
    source = Path(__file__).parents[1] / "validators/multi_province/k1_hjb_value_relaxation/run.py"
    tree = ast.parse(source.read_text(encoding="utf-8"))
    called = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                called.add(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                called.add(node.func.attr)
    forbidden = {
        "solve_matlab_faithful_stationary_kfe", "run_corrected_2018_trajectory",
        "solve_firm", "run_k1b", "run_k2", "run_ge", "run_irf", "write_results",
    }
    assert called.isdisjoint(forbidden)


def test_intervention_occurs_after_direct_solve_and_raw_gap_is_checked() -> None:
    source = (Path(__file__).parents[1] /
              "validators/multi_province/k1_hjb_value_relaxation/relaxed_hjb.py").read_text(encoding="utf-8")
    solve_position = source.index("solved = oracle.linalg.spsolve")
    intervention_position = source.index("value_next = relaxed_value_state")
    convergence_position = source.index("if raw_fixed_point_converged")
    assert solve_position < intervention_position < convergence_position
    assert "value_next - old" not in source[convergence_position:convergence_position + 160]


def test_compact_evidence_closes_budget_raw_gap_and_normality() -> None:
    root = (Path(__file__).parents[1] /
            "docs/evidence/ch5_mp4c_k1_hjb_value_update_relaxation_omega_0p5")
    final = json.loads((root / "final_analysis.json").read_text(encoding="utf-8"))
    ledger = json.loads((root / "call_ledger.json").read_text(encoding="utf-8"))
    solves = json.loads((root / "direct_solve_count_receipt.json").read_text(encoding="utf-8"))
    parity = json.loads((root / "omega1_equivalence.json").read_text(encoding="utf-8"))
    source = json.loads((root / "execution_source_adjudication.json").read_text(encoding="utf-8"))
    assert parity["status"] == "PASS" and len(parity["preregistered_calls"]) == 2
    assert ledger["hjb_calls"] == 64 and ledger["parity_hjb_calls"] == 2
    assert ledger["treatment_hjb_calls"] == 62 and ledger["scientific_retries"] == 0
    assert all(ledger[name] == 0 for name in (
        "kfe_calls", "outer_trajectory_advancements", "matlab_calls", "firm_calls",
        "k1b_calls", "k2_calls", "ge_calls", "irf_calls", "results_calls"))
    assert solves["total_hjb_direct_solves"] == 4823
    assert final["exact_input_coverage"] == 62
    assert final["convergence"] == {
        "turn1": {"baseline": 20, "treatment": 23},
        "turn2": {"baseline": 2, "treatment": 0},
        "all": {"baseline": 22, "treatment": 23},
    }
    assert final["raw_gap_vs_relaxed_update"]["converged_calls_raw_gap_below_1e7"] == 23
    assert final["output_normality"]["recomputed_normal_calls"] == 62
    assert final["results_eligible"] is False and final["production_contract_ready"] is False
    assert source["executed_relaxed_hjb_sha256"] == source["candidate_relaxed_hjb_sha256"]
    assert source["scientific_control_flow_changed"] is False and source["scientific_rerun"] is False
