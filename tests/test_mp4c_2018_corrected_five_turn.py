"""Static and synthetic gates; no workbook or scientific model calls."""
from __future__ import annotations

from types import SimpleNamespace

import numpy as np
from scipy import sparse

from validators.multi_province.corrected_2018_five_turn import finalize, run


def _objects(operator: np.ndarray, density: np.ndarray, mu_b=None, mu_a=None):
    matrix = sparse.csr_matrix(operator)
    shape = (2, 2, 1)
    zeros = np.zeros(shape)
    raw = density.copy()
    return (SimpleNamespace(mu_b=zeros if mu_b is None else mu_b,
                            mu_a=zeros if mu_a is None else mu_a),
            SimpleNamespace(density_vector=density, density=density.reshape(shape, order="F"),
                            transpose=matrix.transpose().tocsr(), contaminated_matrix=sparse.eye(4),
                            raw_solve_vector=raw, rhs=raw, raw_residual_inf=0.0,
                            db=1.0, da=1.0, cell_weight=1.0))


def test_five_turn_and_three_turn_reproduction_guards_are_literal() -> None:
    source = open(run.__file__, encoding="utf-8").read()
    assert "for turn_index in (1, 2, 3, 4, 5):" in source
    assert "if turn_index in (1, 2, 3):" in source
    assert '"authorized_turns": 5' in source
    assert run.VERDICT_TURN_MISMATCH[3].endswith("TURN3_REPRODUCTION_MISMATCH")


def test_pure_kfe_diagnostic_accepts_conservative_nonnegative_density() -> None:
    q = np.array([[-1., 1., 0., 0.], [1., -1., 0., 0.],
                  [0., 0., -1., 1.], [0., 0., 1., -1.]])
    hjb, kfe = _objects(q, np.full(4, .25))
    result = run.kfe_distribution_diagnostics(hjb, kfe)
    assert result["classification"] == "VALID"
    assert result["additional_solves"] == 0
    assert result["normalized_mass"] == 1.0


def test_pure_kfe_diagnostic_preserves_source_free_and_boundary_blockers() -> None:
    q = np.diag([-1., -2., -3., -4.])
    mu_b = np.zeros((2, 2, 1)); mu_b[-1, 0, 0] = 2.0
    hjb, kfe = _objects(q, np.full(4, .25), mu_b=mu_b)
    result = run.kfe_distribution_diagnostics(hjb, kfe)
    assert result["classification"] == "DIAGNOSTIC_ONLY"
    assert result["source_free_residual_numerator"] == 1.0
    assert result["boundary_outward_leak"]["upper_b"]["outward_leak_count"] == 1


def test_asset_transition_retains_turn3_collapse_and_flags_later_violence() -> None:
    rows = []
    totals = [10., 10., 1., 10., 10.]
    for turn, total in enumerate(totals, 1):
        rows.append([{"province": str(i), "A": total / 2, "B": total / 2,
                      "A_plus_B": total, "household_rah": .02, "household_rb": .02,
                      "kfe_diagnostic_status": "VALID"} for i in range(31)])
    result = finalize.asset_transition(rows)
    assert result["anhui"]["turns"][2]["ratio_A_plus_B"] == .1
    assert result["violent_transition_signals"][0]["turn"] == 4
