"""Synthetic arithmetic/static gates; no model or solver calls."""
from __future__ import annotations

import ast
from pathlib import Path

import numpy as np
from scipy import sparse

from validators.multi_province.call725_kfe_mass_balance import ledger
from validators.multi_province.five_turn_kfe_attribution import analyze


def test_analyzer_imports_no_solver_or_model_entrypoint() -> None:
    source = Path(analyze.__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported = {alias.name for node in ast.walk(tree)
                if isinstance(node, (ast.Import, ast.ImportFrom)) for alias in node.names}
    assert not {"linalg", "spsolve", "eig", "eigs"} & imported
    assert "solve_matlab" not in source
    assert "run_source_faithful_one_turn" not in source


def test_mass_balance_localizes_dropped_row_and_escape() -> None:
    q = sparse.csr_matrix([[-1.0, 0.0], [1.0, -1.0]])
    density = np.array([0.5, 0.5])
    result = ledger.build_mass_balance(q, density, 1.0, np.array([0.0, 1.0]), 1)
    assert result["escaped_mass_flow"] == 0.5
    assert result["candidate_pin_source"] == 0.5
    assert result["pin_abs_share"] == 1.0
    assert result["mass_identity_abs_discrepancy"] == 0.0


def test_directional_rates_keep_faces_separate() -> None:
    mb = np.zeros((2, 2, 1)); ma = np.zeros_like(mb)
    mb[-1, 0, 0] = 2.0
    rates = ledger.directional_omitted_rates(mb, ma, 0.5, 1.0)
    assert rates["upper_b"][-1, 0, 0] == 4.0
    assert np.count_nonzero(rates["lower_b"]) == 0
    assert np.count_nonzero(rates["lower_a"]) == 0
    assert np.count_nonzero(rates["upper_a"]) == 0


def test_summary_reports_required_cross_province_fields() -> None:
    row = {"turn": 4, "province": "X",
        "stationarity": {"material": True, "pin_approximately_all": True, "off_pin_max_abs": 1e-16},
        "boundary": {"density_weighted_escape_by_face": {"lower_b": 0.0, "upper_b": 0.5, "lower_a": 0.0, "upper_a": 0.0},
                     "leak_cell_counts": {"lower_b": 0, "upper_b": 2, "lower_a": 0, "upper_a": 0},
                     "density_weighted_total_escape": 0.5, "upper_b_face_probability_mass": 0.6},
        "mass_balance": {"direct_abs_discrepancy": 1e-16},
        "implicit_source": {"direct_abs_discrepancy": 1e-16}}
    summary = analyze.summarize([row], 4)
    assert summary["pin_approximately_all_residual_l1_provinces"] == 1
    assert summary["leak_cell_totals"] == {"lower_b": 0, "upper_b": 2, "lower_a": 0, "upper_a": 0}


def test_pin_concentration_uses_componentwise_frozen_roundoff_rule() -> None:
    passed, bound = analyze.off_pin_is_roundoff(5.4e-15, 0.0017)
    assert passed is True
    assert bound == 128.0 * np.finfo(float).eps
    assert analyze.off_pin_is_roundoff(1e-10, 0.0017)[0] is False
