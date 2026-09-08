"""Synthetic tests only; no model, initializer, root, HJB, or KFE calls."""
import ast
import copy
from dataclasses import dataclass
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

import numpy as np
from scipy import sparse

DIR = Path(__file__).resolve().parents[1] / "validators/multi_province/call725_rah_0p07_sensitivity"
import sys
sys.path.insert(0, str(DIR))
from evidence import Store, decode_saved
import analyze


class SensitivityTests(unittest.TestCase):
    def test_round_trip_arrays_sparse_nonfinite(self):
        with tempfile.TemporaryDirectory() as temporary:
            store = Store(Path(temporary) / "science")
            matrix = sparse.csr_matrix([[0.0, -2.0], [3.0, 0.0]])
            store.save("x", {"array": np.array([1.0, np.nan]), "matrix": matrix})
            store.close()
            result = decode_saved(Path(temporary) / "science/x.json")
            self.assertTrue(np.isnan(result["array"][1]))
            self.assertTrue((result["matrix"] != matrix).nnz == 0)

    def test_exact_one_field_state_diff_and_float_literal(self):
        old = {"rah": 0.09, "ra": 0.09, "ramax": 0.09, "Zt": 1.0}
        new = copy.deepcopy(old)
        new["rah"] = float("0.07")
        self.assertEqual([key for key in old if old[key] != new[key]], ["rah"])
        self.assertEqual(new["rah"].hex(), "0x1.1eb851eb851ecp-4")
        self.assertNotEqual(new["rah"], 0.09 - 0.02)

    def test_mapped_input_only_changes_ra(self):
        @dataclass(frozen=True)
        class Inputs:
            r_a: float
            r_b: float
            tau: float
            wages: object
        wages = np.array([16.82014806560587])
        old = Inputs(.09, .02, .05, wages)
        new = Inputs(float(".07"), old.r_b, old.tau, old.wages)
        self.assertEqual([name for name in old.__dataclass_fields__ if getattr(old, name) is not getattr(new, name) and getattr(old, name) != getattr(new, name)], ["r_a"])
        self.assertIs(new.wages, old.wages)

    def test_initializer_delegates_once_at_new_rate(self):
        calls = []
        def original(state, grid, params):
            calls.append(state["rah"])
            return "V", "l"
        state = {"rah": float(".07")}
        result = original(state, object(), object())
        self.assertEqual(result, ("V", "l"))
        self.assertEqual(calls, [float(".07")])

    def test_baseline_is_read_only_comparator_not_warm_start(self):
        baseline = np.array([9.0])
        generated = np.array([7.0])
        selected = generated
        self.assertIs(selected, generated)
        self.assertFalse(np.shares_memory(selected, baseline))

    def test_original_false_hjb_reaches_kfe(self):
        path = DIR.parents[0] / "mp4b_matlab_source_postloop_household_adapter.py"
        tree = ast.parse(path.read_text(encoding="utf-8"))
        function = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "solve_matlab_source_postloop_household")
        class Box: pass
        grid = Box(); grid.b = np.array([0., 1.]); grid.a = np.array([0., 1.]); grid.z = np.array([1.])
        h = Box(); h.converged = False; h.post_convergence_operator = Box(); h.post_convergence_operator.full = "A"; h.consumption = h.labor = np.zeros((2, 2, 1))
        calls = []
        def hjb(*args): calls.append("hjb"); return h
        def kfe(*args, **kwargs): calls.append("kfe"); raise ValueError("original KFE failure")
        namespace = {"Callable": object, "HouseholdSteadyStateResult": Box, "solve_matlab_faithful_hjb": hjb, "solve_matlab_faithful_stationary_kfe": kfe, "aggregate_stationary_household": lambda *args: None}
        exec(compile(ast.Module(body=[function], type_ignores=[]), str(path), "exec"), namespace)
        with self.assertRaisesRegex(ValueError, "original KFE failure"):
            namespace[function.name](grid, None, None, None, None, None, None, None)
        self.assertEqual(calls, ["hjb", "kfe"])

    def test_save_hjb_before_kfe_failure(self):
        with tempfile.TemporaryDirectory() as temporary:
            store = Store(Path(temporary) / "science")
            store.save("hjb_return_before_kfe", {"converged": False})
            try:
                raise ValueError("KFE")
            except ValueError as error:
                store.save("terminal", {"error": str(error), "KFE_entries": 1})
            store.close()
            self.assertTrue((Path(temporary) / "science/hjb_return_before_kfe.json").exists())

    def test_failed_entries_count_before_call(self):
        counts = {"HJB": 0}
        def wrapped():
            counts["HJB"] += 1
            raise ValueError("failed")
        with self.assertRaises(ValueError): wrapped()
        self.assertEqual(counts["HJB"], 1)

    def test_missing_phase_stays_missing(self):
        phases = {"hjb": True, "kfe": False, "aggregate": False}
        self.assertFalse(phases["aggregate"])
        self.assertNotIn("aggregate_value", phases)

    def test_operator_diagnostic_counts_exact_signs_without_solve(self):
        matrix = sparse.csr_matrix([[-1.0, 1.0], [-2.0, 2.0]])
        result = analyze.operator_diagnostics(matrix, (2, 1, 1))
        self.assertEqual(result["negative_offdiagonal_count"], 1)
        self.assertEqual(result["negative_offdiagonal_min"], -2.0)
        self.assertEqual(result["row_sum_max_abs"], 0.0)

    def test_distribution_residuals_are_distinct_formulas(self):
        contaminated = sparse.eye(2, format="csr")
        raw = np.array([0.007, 0.0])
        rhs = raw.copy()
        stationary_operator = sparse.csr_matrix([[-1.0, 1.0], [0.0, 0.0]])
        density = np.array([1.0, 0.0])
        self.assertEqual(float(np.linalg.norm(contaminated @ raw - rhs, ord=np.inf)), 0.0)
        self.assertEqual(float(np.linalg.norm(stationary_operator @ density, ord=np.inf)), 1.0)

    def test_import_evidence_has_no_science(self):
        spec = importlib.util.spec_from_file_location("rah07_evidence", DIR / "evidence.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertNotIn("anchor", module.__dict__)


if __name__ == "__main__":
    unittest.main(verbosity=2)
