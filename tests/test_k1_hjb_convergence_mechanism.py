from pathlib import Path
import json

import numpy as np
from scipy import sparse

from validators.multi_province.k1_hjb_convergence_mechanism.instrumented_hjb import _operator_metrics, _summary
from validators.multi_province.k1_hjb_convergence_mechanism.run import _objects, _sha_array


def test_frozen_objects_are_exact() -> None:
    grid, params, numerics = _objects()
    assert np.array_equal(grid.b, np.linspace(-2, 5, 20))
    assert np.array_equal(grid.a, np.linspace(0, 10, 20))
    assert params.rho == 0.05 and params.chi_0 == 0.1 and params.chi_1 == 2.0
    assert numerics.delta == 1000.0 and numerics.convergence_tolerance == 1e-7
    assert numerics.max_iterations == 100 and numerics.drift_tolerance == 1e-12


def test_observation_helpers_do_not_mutate_arrays() -> None:
    values = np.array([3.0, -1.0, 2.0])
    before = values.copy()
    summary = _summary(values)
    assert np.array_equal(values, before)
    assert summary["min"] == -1.0 and summary["max"] == 3.0
    matrix = sparse.csr_matrix([[-1.0, 1.0], [2.0, -2.0]])
    metrics = _operator_metrics(matrix)
    assert metrics["max_abs_row_sum_defect"] == 0.0
    assert metrics["minimum_stored_off_diagonal"] == 1.0


def test_array_identity_uses_accepted_dtype_shape_header() -> None:
    values = np.array([1.0, 2.0], dtype="<f8")
    from hashlib import sha256
    expected = sha256(b"<f8|(2,)|C|" + values.tobytes()).hexdigest().upper()
    assert _sha_array(values) == expected


def test_no_forbidden_science_tokens_in_runner() -> None:
    source = Path(__file__).parents[1] / "validators/multi_province/k1_hjb_convergence_mechanism/run.py"
    text = source.read_text(encoding="utf-8")
    assert "solve_matlab_faithful_stationary_kfe(" not in text
    assert "transfer_candidate_abs_limit" not in text


def test_compact_evidence_budget_and_replay_closure() -> None:
    root = Path(__file__).parents[1] / "docs/evidence/ch5_mp4c_k1_hjb_convergence_mechanism_turn1_turn2"
    terminal = json.loads((root / "terminal_result.json").read_text(encoding="utf-8"))
    ledger = json.loads((root / "call_ledger.json").read_text(encoding="utf-8"))
    analysis = json.loads((root / "analysis_summary.json").read_text(encoding="utf-8"))
    solves = json.loads((root / "direct_solve_count_receipt.json").read_text(encoding="utf-8"))
    assert terminal["exact_input_coverage"] == 62
    assert terminal["accepted_output_exact_count"] == terminal["final_operator_exact_count"] == 62
    assert (terminal["turn1_converged"], terminal["turn2_converged"]) == (20, 2)
    assert ledger["hjb_calls"] == 64 and ledger["parity_hjb_calls"] == 2 and ledger["replay_hjb_calls"] == 62
    assert ledger["scientific_retries"] == ledger["kfe_calls"] == ledger["matlab_calls"] == 0
    assert solves["total_hjb_direct_solves"] == 4689
    assert analysis["results_eligible"] is False and analysis["longer_iteration_ceiling_supported"] is False
