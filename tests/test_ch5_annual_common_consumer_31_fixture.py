"""Wholly invented31 spy orchestration only; no original consumer formulas."""
import sys
sys.dont_write_bytecode = True
import hashlib
import importlib.abc
import json
from pathlib import Path
from types import ModuleType, SimpleNamespace
from dataclasses import replace
import unittest
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PINS = {
    "src/ch5_two_asset_hank/corrected_diagnostic/lagged_observed_gdp_wedge.py": "7B9A490F382E3007820E70C68D2EFB5992DE25BC8455EDE8B265CA33F384AF56",
    "src/ch5_two_asset_hank/corrected_diagnostic/annual_observed_labor_context.py": "0AA27B67030115DEC06F9F7A5F78F0113380ABC857D3F08189982EB90E3D8AFE",
    "src/ch5_two_asset_hank/corrected_diagnostic/annual_labor_array_adapter.py": "137BFB6C3F0B3D7F4672A78ECCB006A776CB1A40B258CB30A3B18437D4BFCF41",
    "validators/multi_province/annual_observed_labor_diagnostic/integration.py": "BB594FA2A34340B330638459D1CF58524D405DEA2FB059194D43C3C79E48345A",
    "validators/multi_province/annual_observed_labor_diagnostic/middle_stage.py": "82665113213CBC93286468A87069C8E014B64A12415A2B947FFA7EFDF3579F81"
}
LOAD_NAMES = ("_annual_accepted_wedge_helper", "_invented31_context",
              "_invented31_array", "_invented31_integration", "_invented31_middle")
N = 31
WEALTH = [2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824,2147483648]
PRIVATE = [536870913.5,2.5,4,18,20,32,144,160,256,1152,1280,2048,9216,10240,16384,73728,81920,131072,589824,655360,1048576,4718592,5242880,8388608,37748736,41943040,67108864,301989888,335544320,536870912,2415919104]
TARGETS = [536870921.5,10.5,12,26,28,40,152,168,264,1160,1288,2056,9224,10248,16392,73736,81928,131080,589832,655368,1048584,4718600,5242888,8388616,37748744,41943048,67108872,301989896,335544328,536870920,2415919112]
THETA = [0.25,0.5,0.75,0.25,0.5,0.75,0.25,0.5,0.75,0.25,0.5,0.75,0.25,0.5,0.75,0.25,0.5,0.75,0.25,0.5,0.75,0.25,0.5,0.75,0.25,0.5,0.75,0.25,0.5,0.75,0.25]
FIELDS = ("Kt", "Lt", "Yt", "mt", "KNratio", "wt0", "wjt", "rk",
          "Thetat", "It", "PIt", "Corptax", "ra0", "ra", "Govinc")
COUNTS = ("source_faithful_labor_reconstructions",
          "frozen_k1b_quantity_allocations", "k1b_feedback_calls",
          "c1_residual_govinv_constructions", "firm_evaluations",
          "composite_wage_batches")
PREPARATION_ATTEMPTS = {"synthetic_context": 0, "synthetic_array": 0,
                        "synthetic_middle": 0}


class NoOriginalImports(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".")[0] in {"ch5_two_asset_hank", "validators", "scipy"}:
            raise AssertionError("original scientific/package import forbidden: " + fullname)
        return None


class SourceScope:
    """Execute only hash-bound source bytes, never an initializer or pyc."""
    def __enter__(self):
        self.saved = {name: sys.modules.get(name) for name in LOAD_NAMES}
        self.present = {name: name in sys.modules for name in LOAD_NAMES}
        self.guard = NoOriginalImports()
        sys.meta_path.insert(0, self.guard)
        try:
            modules = []
            for name, (relative, pin) in zip(LOAD_NAMES, PINS.items()):
                path = (ROOT / relative).resolve()
                if path != ROOT.resolve() / relative:
                    raise AssertionError("source path escaped exact tree")
                raw = path.read_bytes()
                if hashlib.sha256(raw).hexdigest().upper() != pin:
                    raise AssertionError("source identity changed: " + relative)
                module = ModuleType(name)
                module.__file__ = str(path)
                module.__package__ = ""
                sys.modules[name] = module
                exec(compile(raw, str(path), "exec"), module.__dict__)
                if Path(module.__file__).resolve() != path:
                    raise AssertionError("source module locator changed")
                modules.append(module)
            self.modules = tuple(modules)
            return self
        except BaseException:
            self.__exit__(None, None, None)
            raise

    def __exit__(self, *unused):
        sys.meta_path.remove(self.guard)
        for name in LOAD_NAMES:
            if self.present[name]:
                sys.modules[name] = self.saved[name]
            else:
                sys.modules.pop(name, None)
        for name in LOAD_NAMES:
            assert (name in sys.modules) == self.present[name]
            if self.present[name]:
                assert sys.modules[name] is self.saved[name]


def frozen_digest(values):
    return hashlib.sha256(np.asarray(values, dtype="<f8").tobytes(order="F")).hexdigest().upper()


class Invented31(unittest.TestCase):
    def setUp(self):
        self.scope = SourceScope()
        self.scope.__enter__()
        self.addCleanup(self.scope.__exit__, None, None, None)
        self.helper, self.context_module, self.adapter, self.integration, self.middle = self.scope.modules
        self.axis = tuple((i + 1, "Invented Source %02d" % (i + 1)) for i in range(N))
        self.mapping = tuple((i, full, "Invented Model %02d" % i) for i, full in self.axis)
        raw = json.dumps({
            "schema": "CH5_INVENTED_ANNUAL_FIXTURE_V1", "input_kind": "synthetic",
            "province_axis": self.axis, "target_year": 2018, "observation_year": 2017,
            "price_basis": "synthetic_fixture", "price_verified": False,
            "records": [[i + 1, 2017, 100 + 7 * i, 10 + i] for i in range(N)]
        }, separators=(",", ":")).encode()
        sha = hashlib.sha256(raw).hexdigest().upper()
        PREPARATION_ATTEMPTS["synthetic_context"] += 1
        self.context = self.context_module.prepare_synthetic_context(
            raw, expected_fixture_sha256=sha, province_axis=self.axis, target_year=2018)
        self.meta = dict(target_year=2018, province_axis=self.axis, source_sha256=sha,
                         input_kind="synthetic", price_basis="synthetic_fixture", price_verified=False)
        PREPARATION_ATTEMPTS["synthetic_array"] += 1
        self.array = self.adapter.prepare_annual_array(
            self.context, province_mapping=self.mapping, **self.meta)
        self.master = self.array.phi_destination_origin
        self.distance = tuple(tuple((3 * j + i + 1) / 1024 for i in range(N)) for j in range(N))
        self.batch = SimpleNamespace(
            ct=tuple(1 + i / 32 for i in range(N)),
            at=tuple(WEALTH[i] / (2 ** (i % 3)) for i in range(N)),
            at_tax=tuple((i - 15) / 16 for i in range(N)),
            household_lt=tuple(2 + i / 8 for i in range(N)))
        self.labor = tuple(10 + i / 4 for i in range(N))
        self.firm_wages = tuple(700 + i for i in range(N))
        self.wage_output = tuple(900 + i for i in range(N))
        self.states = tuple(dict(
            province_index=i + 1, source_province_name=self.axis[i][1], name=self.mapping[i][2],
            N=2 ** (i % 3), wjt=100 + i, tau=i / 128, inter_prv_ratio=THETA[i],
            Kt0=TARGETS[i], alpha=0.5, Zt=2 + i / 32, pit=1, Kt_prev=1,
            Zt_1=1, pit_1=1, rk=1, corptau=1, Tt=1, ramin=0, ramax=2,
            wjtmin=0, wjtmax=1000, GovInv=-100, AtTax=-200, Lt_prev=-300,
            invented_tag="Fixture-%02d" % i) for i in range(N))
        self.params = dict(ga=2, phi_l=3, alphal=4, epsilon=5, theta=0.5, delta=0.25)
        self.shares = np.zeros((N, N), dtype=np.float64)
        for i in range(N):
            self.shares[i, i] = 1 - THETA[i]
            self.shares[(i + 1) % N, i] = THETA[i]
        self.share_sha = frozen_digest(self.shares)
        self.ledger = {key: 0 for key in COUNTS}
        self.ledger["engineering_fixture_label"] = "wholly-invented31"
        self.events = []
        self.mode = None
        self.reconstruction_calls = 0
        self.firm_index = 0
        self.dependencies = self.middle.FixtureDependencies(
            self.c1_spy, self.firm_spy, "explicit-invented31-spies")
        PREPARATION_ATTEMPTS["synthetic_middle"] += 1
        self.prepared = self.middle.prepare_middle_stage(
            annual_context=self.context, prepared_array=self.array,
            province_mapping=self.mapping, ledger=self.ledger, dependencies=self.dependencies)
        self.spies = self.integration.SyntheticSpies(
            self.factory_spy, self.labor_spy, self.forbidden_firm_stage, self.wage_spy)

    def counters(self):
        return tuple(self.ledger[key] for key in COUNTS)

    def factory_spy(self, **kw):
        self.events.append("factory")
        self.assertEqual(self.counters(), (1, 0, 0, 0, 0, 0))
        self.assertIs(kw["consumption_by_origin"], self.batch.ct)
        self.assertEqual(kw["population_by_origin"], [r["N"] for r in self.states])
        self.assertEqual(kw["old_firm_wage_by_destination"], [r["wjt"] for r in self.states])
        self.assertEqual(kw["tax_by_origin"], [r["tau"] for r in self.states])
        self.assertIs(kw["phi_destination_origin"], self.master)
        self.assertIs(kw["migration_wedge_destination_origin"], self.distance)
        self.assertEqual((kw["gamma_c"], kw["phi_l"]), (2, 3))
        self.assertEqual(set(kw), {"consumption_by_origin", "population_by_origin",
            "old_firm_wage_by_destination", "tax_by_origin", "phi_destination_origin",
            "migration_wedge_destination_origin", "gamma_c", "phi_l"})
        if self.mode == "factory":
            raise ValueError("invented factory failure")
        return SimpleNamespace(**kw)

    def labor_spy(self, carrier):
        self.events.append("labor")
        self.reconstruction_calls += 1
        self.assertIs(carrier.phi_destination_origin, self.master)
        return SimpleNamespace(lt_supply=((0,) + self.labor[1:] if self.mode == "labor" else self.labor))

    def c1_spy(self, *, Ktarget_MU, Kprivate_current_MU, province_order):
        self.events.append("c1")
        self.assertEqual(self.counters(), (1, 1, 1, 1, 0, 0))
        self.assertEqual(tuple(Ktarget_MU), tuple(TARGETS))
        self.assertEqual(tuple(Kprivate_current_MU), tuple(PRIVATE))
        self.assertEqual(province_order, tuple(row[2] for row in self.mapping))
        if self.mode == "c1_tamper":
            Ktarget_MU[0] += 1
        # Fixed fixture answers, not a residual-government model.
        gov = ((7,) + (8,) * 30 if self.mode == "c1_mismatch" else (8,) * N)
        return SimpleNamespace(province_order=province_order,
            GovInv_residual_MU=gov, firm_K_accounting_MU=tuple(TARGETS))

    def firm_spy(self, source, private, labor, params):
        i = self.firm_index
        self.firm_index += 1
        self.events.append("firm:%02d" % i)
        self.assertEqual(self.ledger["firm_evaluations"], i + 1)
        expected = dict(self.states[i])
        expected.update(GovInv=8.0, AtTax=self.batch.at_tax[i], Lt_prev=self.batch.household_lt[i])
        self.assertEqual(source, expected)
        self.assertEqual(private, PRIVATE[i])
        self.assertEqual(labor, self.labor[i])
        self.assertEqual(dict(params), self.params)
        if self.mode == "firm" and i == 15:
            raise ValueError("invented firm failure at index15")
        values = {field: 1.0 for field in FIELDS}
        values.update(Kt=TARGETS[i], Lt=self.labor[i], wjt=self.firm_wages[i])
        return SimpleNamespace(**values)

    def forbidden_firm_stage(self, *unused):
        raise AssertionError("prepared middle must bypass opaque firm_stage")

    def wage_spy(self, provinces, wages, phi, distance, *, phi_l, alphal):
        self.events.append("wage")
        self.assertEqual(self.counters(), (1, 1, 1, 1, N, 1))
        self.assertEqual(tuple(dict(r) for r in provinces), self.states)
        self.assertEqual(tuple(wages), self.firm_wages)
        self.assertIs(phi, self.master)
        self.assertIs(distance, self.distance)
        self.assertEqual((phi_l, alphal), (3, 4))
        return self.wage_output

    def run_seam(self, **changes):
        kwargs = dict(annual_context=self.context, params=self.params,
            migration_wedge_destination_origin=self.distance, spies=self.spies,
            prepared_array=self.array, province_mapping=self.mapping,
            prepared_middle_stage=self.prepared, **self.meta)
        kwargs.update(changes)
        return self.integration.integrate_turn(ROOT, ROOT, ROOT, 1, self.states,
            self.batch, self.shares, self.share_sha, self.ledger, (), **kwargs)

    def failure(self, pattern, counts, events=None, **changes):
        with self.assertRaisesRegex(ValueError, pattern):
            self.run_seam(**changes)
        self.assertEqual(self.counters(), counts)
        self.assertNotIn("wage", self.events)
        if events is not None:
            self.assertEqual(self.events, events)

    def test_success_asymmetric31(self):
        before_states = tuple(dict(row) for row in self.states)
        before_shares = self.shares.copy()
        result = self.run_seam()
        self.assertEqual(self.counters(), (1, 1, 1, 1, 31, 1))
        self.assertEqual(self.events, ["factory", "labor", "c1"] +
                         ["firm:%02d" % i for i in range(N)] + ["wage"])
        self.assertEqual(self.master.shape, (31, 31))
        self.assertFalse(np.array_equal(self.master, self.master.T))
        self.assertFalse(np.array_equal(np.asarray(self.distance), np.asarray(self.distance).T))
        self.assertFalse(np.array_equal(self.shares, self.shares.T))
        self.assertFalse(self.master.flags.writeable)
        self.assertTrue(self.master.flags.c_contiguous)
        self.assertIsInstance(self.array.backing_bytes, bytes)
        with self.assertRaises(ValueError):
            self.master.setflags(write=True)
        self.assertEqual(self.master.tobytes(order="C"), self.array.backing_bytes)
        self.assertIs(result["inputs"].phi_destination_origin, self.master)
        self.assertIs(result["annual_context"], self.context)
        self.assertEqual(result["inputs"].province_order, tuple(row[2] for row in self.mapping))
        capital = result["middle_result"].capital
        self.assertEqual(capital.wealth, tuple(WEALTH))
        self.assertEqual(capital.private, tuple(PRIVATE))
        self.assertEqual(capital.domestic, tuple((1 - THETA[i]) * WEALTH[i] for i in range(N)))
        flow = np.asarray(capital.flows)
        self.assertEqual(flow.shape, (31, 31))
        for i in range(N):
            self.assertEqual(flow[i, i], (1 - THETA[i]) * WEALTH[i])
            self.assertEqual(flow[(i + 1) % N, i], THETA[i] * WEALTH[i])
            self.assertEqual(np.count_nonzero(flow[:, i]), 2)
        self.assertEqual(capital.capital_residual, 0)
        self.assertTrue(capital.no_same_turn_share_recomputation)
        self.assertEqual(result["middle_result"].c1.GovInv_residual_MU, (8,) * N)
        self.assertEqual(result["middle_result"].c1.firm_K_accounting_MU, tuple(TARGETS))
        self.assertEqual(result["middle_result"].c1.capital_unit, "MU_10WAN_YUAN")
        self.assertEqual(tuple(f.wjt for f in result["middle_result"].firms), self.firm_wages)
        self.assertIs(result["wages"], self.wage_output)
        self.assertFalse(result["model_activation"])
        self.assertFalse(result["full_outer_runtime_integrated"])
        self.assertFalse(result["middle_result"].model_activation)
        np.testing.assert_array_equal(self.shares, before_shares)
        self.assertEqual(self.states, before_states)
        self.assertEqual(frozen_digest(self.shares), self.share_sha)
        self.assertNotEqual(self.share_sha, hashlib.sha256(self.shares.tobytes(order="C")).hexdigest().upper())
        self.assertNotEqual(self.share_sha, hashlib.sha256(self.array.backing_bytes).hexdigest().upper())

    def test_wrong_hash(self):
        self.share_sha = "0" * 64
        self.failure("hash|identity", (0, 0, 0, 0, 0, 0), [])

    def test_wrong_axis(self):
        self.states[8]["source_province_name"] = "Invented Wrong Source"
        self.failure("axis|order", (0, 0, 0, 0, 0, 0), [])

    def test_wrong_mapping(self):
        wrong = self.mapping[:-2] + (self.mapping[-1], self.mapping[-2])
        self.failure("seal", (0, 0, 0, 0, 0, 0), [], province_mapping=wrong)

    def test_unsealed_array_copy(self):
        # A normal dataclass copy loses its init=False seal; no token/seal is fabricated.
        self.failure("prepared|seal", (0, 0, 0, 0, 0, 0), [], prepared_array=replace(self.array))

    def test_capital_column_violation(self):
        self.shares[0, 0] -= 0.125
        self.share_sha = frozen_digest(self.shares)
        self.failure("columns", (1, 1, 1, 0, 0, 0), ["factory", "labor"])

    def test_capital_home_violation(self):
        self.shares[0, 0] -= 0.125
        self.shares[1, 0] += 0.125
        self.share_sha = frozen_digest(self.shares)
        self.failure("home-retained", (1, 1, 1, 0, 0, 0), ["factory", "labor"])

    def test_c1_authority_tamper(self):
        self.mode = "c1_tamper"
        self.failure("mutated", (1, 1, 1, 1, 0, 0), ["factory", "labor", "c1"])

    def test_c1_output_mismatch(self):
        self.mode = "c1_mismatch"
        self.failure("residual/accounting", (1, 1, 1, 1, 0, 0), ["factory", "labor", "c1"])

    def test_mid_index_firm_failure(self):
        self.mode = "firm"
        self.failure("index15", (1, 1, 1, 1, 16, 0),
                     ["factory", "labor", "c1"] + ["firm:%02d" % i for i in range(16)])

    def test_factory_failure_not_reconstruction(self):
        self.mode = "factory"
        self.failure("factory failure", (1, 0, 0, 0, 0, 0), ["factory"])
        self.assertEqual(self.reconstruction_calls, 0)

    def test_invalid_migration_before_allocation(self):
        self.mode = "labor"
        self.failure("positive destination", (1, 0, 0, 0, 0, 0), ["factory", "labor"])
        self.assertEqual(self.reconstruction_calls, 1)


if __name__ == "__main__":
    program = unittest.main(verbosity=2, failfast=True, exit=False)
    print(json.dumps({"tests_run": program.result.testsRun,
                      "successful": program.result.wasSuccessful(),
                      "preparation_attempts": PREPARATION_ATTEMPTS}, sort_keys=True))
    sys.exit(0 if program.result.wasSuccessful() else 1)
