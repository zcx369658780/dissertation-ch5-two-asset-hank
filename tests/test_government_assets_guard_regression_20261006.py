"""Bounded synthetic regression: load exactly two project modules, no package init."""
import importlib.util
from pathlib import Path
import sys
import types
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "src" / "ch5_two_asset_hank" / "multi_province"
PACKAGE = "_government_asset_guard_20261006"
package = types.ModuleType(PACKAGE)
package.__path__ = []
sys.modules[PACKAGE] = package
LOADED = []
for leaf in ("province_contracts", "government_assets"):
    path = SOURCE_DIR / (leaf + ".py")
    spec = importlib.util.spec_from_file_location(PACKAGE + "." + leaf, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    LOADED.append(str(path))
contracts = sys.modules[PACKAGE + ".province_contracts"]
assets = sys.modules[PACKAGE + ".government_assets"]
ORDER = contracts.PROVINCE_ORDER


class GovernmentAssetGuards(unittest.TestCase):
    def batch(self, target, private, order=ORDER):
        return assets.residual_government_asset_levels(
            Ktarget_MU=target, Kprivate_current_MU=private, province_order=order
        )

    def test_original_bool_batch_inputs_rejected(self):
        variants = {
            "bool_array": np.ones(31, dtype=bool),
            "object_array": np.array([np.bool_(True)] + [2.0] * 30, dtype=object),
            "mixed_bool_list": [2.0] * 30 + [True],
            "mixed_numpy_bool_list": [np.bool_(True)] + [2.0] * 30,
        }
        for kind, values in variants.items():
            for field in ("target", "private"):
                with self.subTest(kind=kind, field=field):
                    target = values if field == "target" else [2.0] * 31
                    private = values if field == "private" else [1.0] * 31
                    with self.assertRaises(ValueError):
                        self.batch(target, private)

    def test_scalar_bool_inputs_rejected(self):
        for value in (True, np.bool_(True)):
            for field in ("target", "private"):
                with self.subTest(value_type=type(value).__name__, field=field):
                    with self.assertRaises(ValueError):
                        assets.residual_government_asset_level(
                            Ktarget_MU=value if field == "target" else 2.0,
                            Kprivate_current_MU=value if field == "private" else 1.0,
                        )

    def test_scalar_derived_nonfinite_rejected(self):
        with self.assertRaises(ValueError):
            assets.residual_government_asset_level(
                Ktarget_MU=1e-308, Kprivate_current_MU=1e308
            )

    def test_batch_derived_nonfinite_rejected(self):
        target, private = [2.0] * 31, [1.0] * 31
        target[7], private[7] = 1e-308, 1e308
        with self.assertRaises(ValueError):
            self.batch(target, private)

    def test_scalar_formula_and_floor_status_preserved(self):
        for private, gov, capital, floor in (
            (0.0, 10.0, 10.0, False),
            (4.0, 6.0, 10.0, False),
            (10.0, 0.0, 10.0, True),
            (15.0, 0.0, 15.0, True),
        ):
            with self.subTest(private=private):
                result = assets.residual_government_asset_level(
                    Ktarget_MU=10.0, Kprivate_current_MU=private
                )
                self.assertEqual(result.GovInv_residual_MU, gov)
                self.assertEqual(result.firm_K_accounting_MU, capital)
                self.assertEqual(result.residual_floor_binding, floor)
                self.assertEqual(result.private_at_or_above_target, floor)
                self.assertEqual(result.firm_K_over_target, capital / 10.0)
                self.assertEqual(result.capital_gap_before_MU, 10.0 - private)
                self.assertEqual(result.capital_gap_after_MU, 10.0 - capital)
                self.assertEqual(result.capital_unit, "MU_10WAN_YUAN")
                self.assertEqual(result.status,
                    assets.RESIDUAL_PUBLIC_ASSET_ZERO_PRIVATE_AT_OR_ABOVE_TARGET
                    if floor else assets.RESIDUAL_PUBLIC_ASSET_POSITIVE)

    def test_batch_formula_readonly_independent_outputs_preserved(self):
        for kind in ("numeric_list", "float_array"):
            with self.subTest(kind=kind):
                target = np.full(31, 10.0)
                private = np.resize(np.array([0.0, 4.0, 10.0, 15.0]), 31)
                before_target, before_private = target.copy(), private.copy()
                values = (target.tolist(), private.tolist()) if kind == "numeric_list" else (target, private)
                result = self.batch(*values)
                self.assertEqual(result.province_order, ORDER)
                self.assertEqual(result.capital_unit, "MU_10WAN_YUAN")
                np.testing.assert_array_equal(result.GovInv_residual_MU, np.maximum(10.0 - private, 0.0))
                np.testing.assert_array_equal(result.firm_K_accounting_MU, np.maximum(10.0, private))
                fields = (
                    "Ktarget_MU", "Kprivate_current_MU", "GovInv_residual_MU",
                    "firm_K_accounting_MU", "firm_K_over_target",
                    "private_at_or_above_target", "residual_floor_binding",
                    "capital_gap_before_MU", "capital_gap_after_MU",
                )
                for name in fields:
                    output = getattr(result, name)
                    self.assertEqual(output.shape, (31,))
                    self.assertFalse(output.flags.writeable)
                    self.assertFalse(np.shares_memory(output, target))
                    self.assertFalse(np.shares_memory(output, private))
                    self.assertTrue(np.all(np.isfinite(output)))
                np.testing.assert_array_equal(target, before_target)
                np.testing.assert_array_equal(private, before_private)
                target[0], private[0] = 999.0, 888.0
                self.assertEqual(result.Ktarget_MU[0], 10.0)
                self.assertEqual(result.Kprivate_current_MU[0], 0.0)
                with self.assertRaises(ValueError):
                    result.GovInv_residual_MU[0] = 999.0

    def test_existing_axis_shape_sign_and_finite_guards_preserved(self):
        invalid = (
            ([2.0] * 30, [1.0] * 30, ORDER),
            (np.ones((31, 1)), [1.0] * 31, ORDER),
            ([2.0] * 31, [1.0] * 31, tuple(reversed(ORDER))),
            ([0.0] + [2.0] * 30, [1.0] * 31, ORDER),
            ([2.0] * 31, [-1.0] + [1.0] * 30, ORDER),
            ([float("nan")] + [2.0] * 30, [1.0] * 31, ORDER),
            ([2.0] * 31, [float("inf")] + [1.0] * 30, ORDER),
        )
        for index, args in enumerate(invalid):
            with self.subTest(index=index):
                with self.assertRaises(ValueError):
                    self.batch(*args)

    def test_loaded_project_module_boundary(self):
        self.assertEqual(len(LOADED), 2)
        self.assertEqual(
            {name for name in sys.modules if name.startswith(PACKAGE + ".")},
            {PACKAGE + ".province_contracts", PACKAGE + ".government_assets"},
        )
        self.assertNotIn("ch5_two_asset_hank", sys.modules)
        self.assertNotIn("one_turn", sys.modules)
        self.assertNotIn("integration", sys.modules)


if __name__ == "__main__":
    print("PROJECT_MODULE_FILES=" + repr(LOADED), flush=True)
    unittest.main(verbosity=2)
