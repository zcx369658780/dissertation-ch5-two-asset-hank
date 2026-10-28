"""Bounded synthetic contracts; no household solver or production imports."""
from __future__ import annotations

import dataclasses
import importlib.util
import math
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PHASE = "candidate"


def load_file(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def fixture():
    return dict(
        consumption_by_origin=(1.0, 4.0),
        population_by_origin=(2.0, 3.0),
        old_firm_wage_by_destination=(2.0, 4.0),
        tax_by_destination=(0.1, 0.3),
        phi_destination_origin=((1.0, 2.0), (4.0, 1.0)),
        migration_wedge_destination_origin=((0.0, 0.1), (0.2, 0.0)),
        gamma_c=2.0, phi_l=1.0,
    )


class WorksiteTaxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.legacy = load_file("temp31_legacy_migration", "src/ch5_two_asset_hank/multi_province/migration_labor.py")
        if PHASE == "candidate":
            cls.new = load_file("temp31_candidate_tax", "src/ch5_two_asset_hank/multi_province/temp31_worksite_tax.py")

    def assertMatrix(self, actual, expected):
        self.assertEqual(len(actual), len(expected))
        for row, target in zip(actual, expected):
            self.assertEqual(len(row), len(target))
            for value, wanted in zip(row, target):
                self.assertTrue(math.isclose(float(value), wanted, rel_tol=1e-12, abs_tol=1e-12), (value, wanted))

    def old_inputs(self, values, normalized=False):
        args = dict(values)
        args["tax_by_origin"] = args.pop("tax_by_destination")
        if normalized:
            args["household_labor_per_capita_by_origin"] = (0.5, 2.0)
            return self.legacy.OriginPreservingNormalizedMigrationLaborInputs(**args)
        return self.legacy.MigrationLaborInputs(**args)

    def test_destination_tax_asymmetric_golden(self):
        """First run deliberately rejects origin-tax history as TEMP31 target."""
        values = fixture()
        if PHASE == "legacy":
            matrix = self.legacy.reconstruct_migration_labor(self.old_inputs(values)).lt_mat
        else:
            result = self.new.reconstruct_temp31_worksite_labor(self.new.Temp31LaborInputs(**values))
            matrix = result.lt_mat
            self.assertMatrix((result.lt_supply,), ((3.75, 1.525),))
        self.assertMatrix(matrix, ((3.6, 0.15), (1.0, 0.525)))

    def test_normalized_origin_mass_and_nonzero_difference(self):
        result = self.new.reconstruct_temp31_normalized_worksite_labor(self.new.Temp31LaborInputs(**fixture()), (0.5, 2.0))
        self.assertMatrix(result.raw_attractiveness, ((1.8, 0.05), (0.5, 0.175)))
        self.assertMatrix(result.shares, ((18/23, 2/9), (5/23, 7/9)))
        self.assertMatrix(result.lt_mat, ((18/23, 4/3), (5/23, 14/3)))
        self.assertMatrix((result.origin_mass,), ((1.0, 6.0),))
        self.assertMatrix((tuple(sum(row[i] for row in result.lt_mat) for i in range(2)),), (result.origin_mass,))
        self.assertAlmostEqual(sum(result.lt_supply), 7.0)
        old = self.legacy.reconstruct_origin_preserving_normalized_migration_labor(self.old_inputs(fixture(), True))
        self.assertFalse(math.isclose(old.M[0, 1], result.lt_mat[0][1], rel_tol=1e-8))

    def test_history_golden_and_wrong_origin_detection(self):
        old = self.legacy.reconstruct_migration_labor(self.old_inputs(fixture()))
        self.assertMatrix(old.lt_mat, ((3.6, 0.1125), (1.4, 0.525)))
        with self.assertRaises(AssertionError):
            self.assertMatrix(old.lt_mat, ((3.6, 0.15), (1.0, 0.525)))
        normalized = self.legacy.reconstruct_origin_preserving_normalized_migration_labor(self.old_inputs(fixture(), True))
        self.assertMatrix(normalized.s, ((18/25, 3/17), (7/25, 14/17)))

    def test_independent_destination_and_origin_permutations(self):
        f = fixture()
        base = self.new.reconstruct_temp31_worksite_labor(self.new.Temp31LaborInputs(**f)).lt_mat
        for axis in ("destination", "origin"):
            swapped = dict(f)
            names = ("old_firm_wage_by_destination", "tax_by_destination") if axis == "destination" else ("consumption_by_origin", "population_by_origin")
            for name in names:
                swapped[name] = tuple(reversed(f[name]))
            for name in ("phi_destination_origin", "migration_wedge_destination_origin"):
                swapped[name] = tuple(reversed(f[name])) if axis == "destination" else tuple(tuple(reversed(row)) for row in f[name])
            got = self.new.reconstruct_temp31_worksite_labor(self.new.Temp31LaborInputs(**swapped)).lt_mat
            wanted = tuple(reversed(base)) if axis == "destination" else tuple(tuple(reversed(row)) for row in base)
            self.assertMatrix(got, wanted)

    def test_tax_swap_changes_destination_rows(self):
        f = fixture()
        f["tax_by_destination"] = (0.3, 0.1)
        result = self.new.reconstruct_temp31_worksite_labor(self.new.Temp31LaborInputs(**f))
        self.assertMatrix(result.lt_mat, ((2.8, 0.1125), (1.4, 0.675)))

    def test_zero_tax_zero_sigma_and_same_rate_limit(self):
        f = fixture()
        f.update(consumption_by_origin=(1, 1), population_by_origin=(1, 1), tax_by_destination=(0, 0), phi_destination_origin=((1, 1), (1, 1)), migration_wedge_destination_origin=((0, 0), (0, 0)))
        result = self.new.reconstruct_temp31_worksite_labor(self.new.Temp31LaborInputs(**f))
        self.assertMatrix(result.lt_mat, ((2, 2), (4, 4)))
        normalized = self.new.reconstruct_temp31_normalized_worksite_labor(self.new.Temp31LaborInputs(**f), (0.5, 2))
        self.assertMatrix(normalized.shares, ((1/3, 1/3), (2/3, 2/3)))
        f["tax_by_destination"] = (0.2, 0.2)
        new = self.new.reconstruct_temp31_worksite_labor(self.new.Temp31LaborInputs(**f))
        old = self.legacy.reconstruct_migration_labor(self.old_inputs(f))
        self.assertMatrix(new.lt_mat, tuple(tuple(float(x) for x in row) for row in old.lt_mat))

    def test_consumption_elasticity_and_single_population_multiplier(self):
        f = fixture()
        f.update(old_firm_wage_by_destination=(4, 9), tax_by_destination=(0, 0), phi_destination_origin=((1, 1), (1, 1)), migration_wedge_destination_origin=((0, 0), (0, 0)), phi_l=2)
        result = self.new.reconstruct_temp31_worksite_labor(self.new.Temp31LaborInputs(**f))
        self.assertMatrix(result.lt_mat, ((4, 1.5), (6, 2.25)))
        a = self.new.reconstruct_temp31_normalized_worksite_labor(self.new.Temp31LaborInputs(**f), (0.5, 2))
        f["population_by_origin"] = (4, 6)
        b = self.new.reconstruct_temp31_normalized_worksite_labor(self.new.Temp31LaborInputs(**f), (0.5, 2))
        self.assertMatrix(b.lt_mat, tuple(tuple(2*x for x in row) for row in a.lt_mat))

    def test_invalid_shapes_phi_power_base_and_zero_normalizer(self):
        for change in ({"tax_by_destination": (0.1,)}, {"phi_destination_origin": ((0, 1), (1, 1))}, {"tax_by_destination": (2, 0.3)}, {"consumption_by_origin": (float("nan"), 4)}):
            with self.assertRaises(ValueError):
                self.new.reconstruct_temp31_worksite_labor(self.new.Temp31LaborInputs(**(fixture() | change)))
        zero = self.new.Temp31LaborInputs(**(fixture() | {"old_firm_wage_by_destination": (0, 0)}))
        with self.assertRaises(ValueError):
            self.new.reconstruct_temp31_normalized_worksite_labor(zero, (0.5, 2))
        with self.assertRaises(ValueError):
            self.new.reconstruct_temp31_normalized_worksite_labor(self.new.Temp31LaborInputs(**fixture()), (-1, 2))

    def test_net_composite_views_equal_and_raw_mechanisms_preserved(self):
        wage = load_file("temp31_legacy_wage", "src/ch5_two_asset_hank/multi_province/wage.py")
        f = fixture()
        net = wage.composite_household_wages([{"tau": t} for t in f["tax_by_destination"]], f["old_firm_wage_by_destination"], f["phi_destination_origin"], f["migration_wedge_destination_origin"], phi_l=1, alphal=1)
        self.assertMatrix((net,), ((math.sqrt(4.24), math.sqrt(9.12)),))
        views = self.new.adapt_temp31_net_composite_wage(net, semantic=self.new.NET_COMPOSITE, tax_by_destination=f["tax_by_destination"], migration_wedge_destination_origin=f["migration_wedge_destination_origin"])
        self.assertIs(views.initialization, views.hjb)
        self.assertEqual(views.tax_by_destination, (0.1, 0.3))
        self.assertEqual(views.migration_wedge_destination_origin, ((0.0, 0.1), (0.2, 0.0)))
        for i, item in enumerate(views.hjb):
            self.assertEqual(item.w_for_HA, net[i])
            self.assertEqual(item.effective_wage, net[i])
            self.assertEqual((item.tau_for_HA, item.sigma_for_HA, item.labor_weight_for_HA), (0, 0, 1))

    def test_double_tax_injection_is_detected(self):
        f = fixture()
        views = self.new.adapt_temp31_net_composite_wage((2, 3), semantic=self.new.NET_COMPOSITE, tax_by_destination=f["tax_by_destination"], migration_wedge_destination_origin=f["migration_wedge_destination_origin"])
        for i, item in enumerate(views.hjb):
            wrong = item.w_for_HA * (1 - f["tax_by_destination"][i])
            with self.assertRaises(AssertionError):
                self.assertAlmostEqual(wrong, item.w_for_HA)
            with self.assertRaises(ValueError):
                dataclasses.replace(item, tau_for_HA=f["tax_by_destination"][i])
            with self.assertRaises(ValueError):
                dataclasses.replace(item, sigma_for_HA=0.1)

    def test_gross_unproven_or_misaligned_wage_semantics_rejected(self):
        f = fixture()
        for semantic, wages in (("GROSS", (2, 3)), ("UNKNOWN_FIRST_PRODUCTION_ROUND", (2, 3)), (self.new.NET_COMPOSITE, (2,))):
            with self.assertRaises(ValueError):
                self.new.adapt_temp31_net_composite_wage(wages, semantic=semantic, tax_by_destination=f["tax_by_destination"], migration_wedge_destination_origin=f["migration_wedge_destination_origin"])

    def test_fiscal_is_only_conditional_and_national_sum(self):
        d = self.new.diagnose_temp31_conditional_wage_tax((0.1, 0.3), (2, 4), (3, 5))
        self.assertMatrix((d.legacy_lt_times_tau,), ((0.3, 1.5),))
        self.assertMatrix((d.conditional_wage_tax,), ((0.6, 6.0),))
        self.assertAlmostEqual(d.conditional_national_tax, 6.6)
        self.assertEqual(d.scientific_status, "SCIENTIFIC_PENDING")

