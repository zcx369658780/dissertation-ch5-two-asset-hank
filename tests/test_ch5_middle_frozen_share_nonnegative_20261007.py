"""Two invented-only cases for the frozen-share pre-spy nonnegative guard."""
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import sys
from types import SimpleNamespace
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def direct_fixture(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


context = direct_fixture(
    "_share_fix_context",
    "src/ch5_two_asset_hank/corrected_diagnostic/annual_observed_labor_context.py",
)
adapter = direct_fixture(
    "_share_fix_adapter",
    "src/ch5_two_asset_hank/corrected_diagnostic/annual_labor_array_adapter.py",
)
seam = direct_fixture(
    "_share_fix_seam",
    "validators/multi_province/annual_observed_labor_diagnostic/integration.py",
)
middle = direct_fixture(
    "_share_fix_middle",
    "validators/multi_province/annual_observed_labor_diagnostic/middle_stage.py",
)
AXIS = ((1, "Invented Low"), (2, "Invented High"), (3, "Invented Middle"))
MAPPING = tuple((index, full, short) for (index, full), short
                in zip(AXIS, ("Low", "High", "Middle")))
KEYS = ("source_faithful_labor_reconstructions", "frozen_k1b_quantity_allocations",
        "k1b_feedback_calls", "c1_residual_govinv_constructions",
        "firm_evaluations", "composite_wage_batches")
FIELDS = ("Kt", "Lt", "Yt", "mt", "KNratio", "wt0", "wjt", "rk", "Thetat",
          "It", "PIt", "Corptax", "ra0", "ra", "Govinc")


def independent_share_hash(shares):
    encoded = b"".join(struct.pack("<d", float(shares[j, i]))
                       for i in range(3) for j in range(3))
    return hashlib.sha256(encoded).hexdigest().upper()


class FrozenShareNonnegativeTests(unittest.TestCase):
    def setUp(self):
        fixture = dict(
            schema="CH5_INVENTED_ANNUAL_FIXTURE_V1", input_kind="synthetic",
            province_axis=[list(row) for row in AXIS], target_year=2018,
            observation_year=2017, price_basis="synthetic_fixture",
            price_verified=False,
            records=[[1, 2017, 1000.0, 10.0], [2, 2017, 2000.0, 10.0],
                     [3, 2017, 1500.0, 10.0]],
        )
        raw = json.dumps(fixture, sort_keys=True, separators=(",", ":")).encode("utf-8")
        sha = hashlib.sha256(raw).hexdigest().upper()
        self.ctx = context.prepare_synthetic_context(
            raw, expected_fixture_sha256=sha, province_axis=AXIS, target_year=2018)
        self.meta = dict(target_year=2018, province_axis=AXIS, source_sha256=sha,
                         input_kind="synthetic", price_basis="synthetic_fixture",
                         price_verified=False)
        self.carrier = adapter.prepare_annual_array(
            self.ctx, province_mapping=MAPPING, **self.meta)
        self.params = dict(ga=2.0, phi_l=5.0, alphal=1.0, epsilon=10.0,
                           theta=100.0, delta=0.025)
        self.distance = ((0.0, 1.0, 2.0), (3.0, 0.0, 4.0), (5.0, 6.0, 0.0))
        self.batch = SimpleNamespace(ct=(1.0, 2.0, 3.0), at=(2.0, 2.0, 2.0),
                                     at_tax=(0.1, 0.2, 0.3),
                                     household_lt=(7.0, 8.0, 9.0))
        self.rows = tuple(
            dict(name=short, province_index=index, source_province_name=full,
                 N=10.0, wjt=3.0 + index, tau=0.1, inter_prv_ratio=0.5,
                 Kt0=target, alpha=0.3, Zt=1.0, pit=0.02, Kt_prev=50.0,
                 Zt_1=1.0, pit_1=0.02, rk=0.01, corptau=0.2, Tt=1.0,
                 ramin=0.0, ramax=1.0, wjtmin=0.0, wjtmax=20.0)
            for (index, full, short), target in zip(MAPPING, (30.0, 20.0, 10.0)))
        self.ledger = dict(engineering_fixture_label="invented-share-guard-three-province",
                           **{key: 0 for key in KEYS})
        self.events = []
        self.deliveries = []

        def c1(*, Ktarget_MU, Kprivate_current_MU, province_order):
            self.events.append("c1")
            self.assertEqual(tuple(province_order), ("Low", "High", "Middle"))
            target = np.asarray(Ktarget_MU)
            private = np.asarray(Kprivate_current_MU)
            self.assertEqual(tuple(private), (20.0, 20.0, 20.0))
            return SimpleNamespace(
                province_order=tuple(province_order),
                GovInv_residual_MU=np.maximum(target - private, 0.0),
                firm_K_accounting_MU=np.maximum(target, private))

        def firm(source, private, labor, params):
            index = source["province_index"] - 1
            self.events.append("firm:" + str(index + 1))
            self.assertEqual(dict(params), self.params)
            expected = dict(self.rows[index])
            expected.update(GovInv=(10.0, 0.0, 0.0)[index],
                            AtTax=self.batch.at_tax[index],
                            Lt_prev=self.batch.household_lt[index])
            self.assertEqual(source, expected)
            self.assertEqual(private, 20.0)
            values = dict.fromkeys(FIELDS, 1.0)
            values.update(Kt=private + source["GovInv"], Lt=labor,
                          wjt=6.0 + index, ra0=0.2, ra=0.1)
            return SimpleNamespace(**values, as_source_dict=lambda: dict(values))

        deps = middle.FixtureDependencies(c1, firm, "invented-share-guard")
        self.stage = middle.prepare_middle_stage(
            annual_context=self.ctx, prepared_array=self.carrier,
            province_mapping=MAPPING, ledger=self.ledger, dependencies=deps)

        def factory(**kwargs):
            self.events.append("inputs")
            self.deliveries.append(kwargs["phi_destination_origin"])
            self.assertIs(kwargs["migration_wedge_destination_origin"], self.distance)
            return SimpleNamespace(**kwargs)

        def labor(inputs):
            self.events.append("labor")
            return SimpleNamespace(lt_supply=(11.0, 22.0, 33.0))

        def opaque(*args):
            raise AssertionError("opaque firm route must not be called")

        def wage(provinces, firm_wages, phi, distance, *, phi_l, alphal):
            self.events.append("wages")
            self.deliveries.append(phi)
            self.assertIs(distance, self.distance)
            self.assertEqual(firm_wages, [6.0, 7.0, 8.0])
            return (101.0, 202.0, 303.0)

        self.spies = seam.SyntheticSpies(factory, labor, opaque, wage)

    def run_invented(self, shares, sha):
        return seam.integrate_turn(
            None, None, None, 5, self.rows, self.batch, shares, sha, self.ledger, [],
            annual_context=self.ctx, prepared_array=self.carrier,
            province_mapping=MAPPING, prepared_middle_stage=self.stage,
            params=self.params, migration_wedge_destination_origin=self.distance,
            spies=self.spies, **self.meta)

    def test_negative_offdiagonal_rejected_before_attempts_and_callbacks(self):
        shares = np.array(((0.5, 0.75, -0.25), (-0.25, 0.5, 0.75),
                           (0.75, -0.25, 0.5)), dtype=np.float64)
        original = shares.tobytes()
        sha = independent_share_hash(shares)
        self.assertEqual(sha, middle._field_sha256(shares))
        np.testing.assert_array_equal(np.sum(shares, axis=0), np.ones(3))
        np.testing.assert_array_equal(np.diag(shares), np.full(3, 0.5))
        np.testing.assert_array_equal(shares @ np.full(3, 20.0), np.full(3, 20.0))
        with self.assertRaisesRegex(ValueError, "frozen capital shares must be non-negative"):
            self.run_invented(shares, sha)
        self.assertEqual(shares.tobytes(), original)
        self.assertEqual({key: self.ledger[key] for key in KEYS},
                         {key: 0 for key in KEYS})
        self.assertEqual(self.events, [])
        self.assertEqual(self.deliveries, [])
        self.assertFalse(self.ctx.model_activation)
        print("NEGATIVE_CASE_PASS correct_hash=True input_unchanged=True "
              "attempted_counters=[0,0,0,0,0,0] callbacks=[]", flush=True)

    def test_nonnegative_three_province_capital_c1_and_ledger_preserved(self):
        shares = np.array(((0.5, 0.25, 0.25), (0.25, 0.5, 0.25),
                           (0.25, 0.25, 0.5)), dtype=np.float64)
        original = shares.tobytes()
        rows_before = tuple(dict(row) for row in self.rows)
        sha = independent_share_hash(shares)
        self.assertEqual(sha, middle._field_sha256(shares))
        result = self.run_invented(shares, sha)
        capital, c1 = result["middle_result"].capital, result["middle_result"].c1
        self.assertEqual(tuple(capital.wealth), (20.0, 20.0, 20.0))
        self.assertEqual(tuple(capital.private), (20.0, 20.0, 20.0))
        self.assertEqual(tuple(capital.domestic), (10.0, 10.0, 10.0))
        self.assertEqual(capital.flows, ((10.0, 5.0, 5.0),
                                        (5.0, 10.0, 5.0), (5.0, 5.0, 10.0)))
        self.assertEqual(capital.capital_residual, 0.0)
        self.assertEqual(tuple(c1.GovInv_residual_MU), (10.0, 0.0, 0.0))
        self.assertEqual(tuple(c1.firm_K_accounting_MU), (30.0, 20.0, 20.0))
        self.assertEqual(tuple(firm.Kt for firm in result["middle_result"].firms),
                         (30.0, 20.0, 20.0))
        self.assertEqual(tuple(firm.Lt for firm in result["middle_result"].firms),
                         (11.0, 22.0, 33.0))
        self.assertEqual({key: self.ledger[key] for key in KEYS},
                         dict(zip(KEYS, (1, 1, 1, 1, 3, 1))))
        self.assertEqual(self.events,
                         ["inputs", "labor", "c1", "firm:1", "firm:2", "firm:3", "wages"])
        self.assertTrue(all(phi is self.carrier.phi_destination_origin
                            for phi in self.deliveries))
        self.assertEqual(shares.tobytes(), original)
        self.assertEqual(self.rows, rows_before)
        self.assertFalse(result["model_activation"])
        self.assertFalse(result["full_outer_runtime_integrated"])
        self.assertFalse(any(name == "ch5_two_asset_hank" or
                             name.startswith("ch5_two_asset_hank.") for name in sys.modules))
        print("NORMAL_CASE_PASS wealth=[20,20,20] private=[20,20,20] "
              "GovInv=[10,0,0] firm_K=[30,20,20] "
              "attempted_counters=[1,1,1,1,3,1] input_unchanged=True "
              "same_phi_master=True model_activation=False", flush=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
