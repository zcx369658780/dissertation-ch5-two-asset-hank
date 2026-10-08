"""SOURCE CANDIDATE ONLY: synthetic dispatch/axis bridge, not numerical proof.

Real integration, array preparation/validation and middle preparation/pre-spy
validation run against an explicit NumPy-shaped stub. Middle.run is replaced
with a dispatch stub: no capital, C1 or firm arithmetic is executed. This cannot
establish actual NumPy behavior, numerical middle fidelity or output protection.
No real input paths/CLI arguments, production dependencies or package imports.
Review before the single future command; no execution is authorized by this file.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import sys
from types import ModuleType, SimpleNamespace
import unittest

ROOT = Path(__file__).resolve().parents[1]
SEAM = ROOT / 'validators/multi_province/annual_observed_labor_diagnostic'
SOURCE = ROOT / 'src/ch5_two_asset_hank/corrected_diagnostic'


class StubBool:
    pass


class StubArray:
    """Only shape/backing/encoding operations used by the real pre-spy checks.

    The encoding below is fixture behavior, not a replacement numerical library.
    It implements no arithmetic, sums, matrix products, conservation or firms.
    """
    def __init__(self, backing, shape):
        self.base = backing
        self.shape = shape
        self.ndim = len(shape)
        self.dtype = 'float64'
        self.flags = SimpleNamespace(c_contiguous=True, writeable=False)
        self.strides = (shape[1] * 8, 8) if self.ndim == 2 else (8,)
        self.values = struct.unpack('<' + 'd' * (len(backing) // 8), backing)

    def __len__(self):
        return self.shape[0]

    def __iter__(self):
        if self.ndim == 1:
            return iter(self.values)
        return iter(tuple(self.values[j * self.shape[1]:(j + 1) * self.shape[1]])
                    for j in range(self.shape[0]))

    def __getitem__(self, key):
        if type(key) is tuple:
            j, i = key
            return self.values[j * self.shape[1] + i]
        return tuple(self)[key]

    def reshape(self, shape):
        if len(shape) != 2 or shape[0] * shape[1] * 8 != len(self.base):
            raise ValueError('stub fixture reshape mismatch')
        return StubArray(self.base, shape)

    def tobytes(self, order='C'):
        if order == 'C' or self.ndim == 1:
            return self.base
        if order != 'F':
            raise ValueError('stub encoding order unknown')
        values = tuple(self[j, i] for i in range(self.shape[1]) for j in range(self.shape[0]))
        return struct.pack('<' + 'd' * len(values), *values)


def stub_asarray(values, dtype=None, order='C'):
    if type(values) is StubArray:
        return values
    rows = tuple(values)
    nested = bool(rows) and isinstance(rows[0], (tuple, list))
    shape = (len(rows), len(rows[0])) if nested else (len(rows),)
    cells = tuple(value for row in rows for value in row) if nested else rows
    return StubArray(struct.pack('<' + 'd' * len(cells), *cells), shape)


# No installed NumPy is imported. This test runs alone, and refuses an existing
# NumPy module rather than mixing the stub with a real library in one process.
if 'numpy' in sys.modules:
    raise RuntimeError('isolated stub-only process required')
numpy_stub = ModuleType('numpy')
numpy_stub.ndarray = StubArray
numpy_stub.bool_ = StubBool
numpy_stub.float64 = float
numpy_stub.dtype = lambda value: 'float64'
numpy_stub.asarray = stub_asarray
numpy_stub.frombuffer = lambda backing, dtype: StubArray(backing, (len(backing) // 8,))
sys.modules['numpy'] = numpy_stub


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


binding = load('_c8_bridge_binding_test', SEAM / 'fixed_c8_input_binding.py')
integration = load('_c8_bridge_integration_test', SEAM / 'integration.py')
context = load('_c8_bridge_context_test', SOURCE / 'annual_observed_labor_context.py')
array_adapter = load('_c8_bridge_array_test', SOURCE / 'annual_labor_array_adapter.py')
middle = load('_c8_bridge_middle_test', SEAM / 'middle_stage.py')


def blocked(*args, **kwargs):
    raise AssertionError('observed input/real firm or C1 execution outside stub test')


for name in ('authenticate_observed_binding', 'prepare_observed_context',
             'prepare_observed_data_only_context', '_prepare_authenticated_observed_context',
             '_preload_data_only_helper'):
    setattr(context, name, blocked)

AXIS = ((1, 'Invented Alpha Province'), (2, 'Invented Beta Province'))
ANNUAL_MAPPING = ((1, AXIS[0][1], 'Alpha'), (2, AXIS[1][1], 'Beta'))
MODEL = ((0, 'Alpha'), (1, 'Beta'))
MODEL_MAPPING = ((0, 'Alpha', 1, AXIS[0][1]), (1, 'Beta', 2, AXIS[1][1]))


class StubBridgeTests(unittest.TestCase):
    def setUp(self):
        raw = json.dumps({'schema': 'CH5_INVENTED_ANNUAL_FIXTURE_V1',
            'input_kind': 'synthetic', 'province_axis': [list(row) for row in AXIS],
            'target_year': 2018, 'observation_year': 2017,
            'price_basis': 'synthetic_fixture', 'price_verified': False,
            'records': [[1, 2017, 2.0, 4.0], [2, 2017, 3.0, 4.0]]}).encode('utf-8')
        self.sha = hashlib.sha256(raw).hexdigest().upper()
        self.context = context.prepare_synthetic_context(raw,
            expected_fixture_sha256=self.sha, province_axis=AXIS, target_year=2018)
        self.array = array_adapter.prepare_annual_array(self.context,
            target_year=2018, province_axis=AXIS, source_sha256=self.sha,
            input_kind='synthetic', price_basis='synthetic_fixture', price_verified=False,
            province_mapping=ANNUAL_MAPPING)
        self.ledger = dict.fromkeys(middle.LEDGER_KEYS, 0)
        self.ledger['engineering_fixture_label'] = 'invented_stub_bridge'
        dependencies = middle.FixtureDependencies(blocked, blocked, 'invented_stub_dependencies')
        self.middle = middle.prepare_middle_stage(annual_context=self.context,
            prepared_array=self.array, province_mapping=ANNUAL_MAPPING,
            ledger=self.ledger, dependencies=dependencies)
        self.source = binding.ExternalSourceAxis('invented_fixture', self.sha,
            'synthetic_identifier', ((907, AXIS[1][1]), (101, AXIS[0][1])))
        self.states = []
        for index, short in MODEL:
            row = dict.fromkeys(middle.STATE_FIELDS, 1.0)
            row.update(name=short, province_index=index, source_province_name=AXIS[index][1],
                N=4.0, wjt=2.0, tau=.1, inter_prv_ratio=.2, Kt0=2.0, alpha=.3,
                ramin=0.0, ramax=2.0, wjtmin=0.0, wjtmax=3.0)
            self.states.append(row)
        self.states = tuple(self.states)
        self.batch = SimpleNamespace(ct=(1.0, 2.0), household_lt=(1.0, 1.0),
            at=(1.0, 1.0), bt=(0.0, 0.0), at_tax=(0.0, 0.0))
        self.shares = ((.8, .2), (.2, .8))
        self.share_sha = hashlib.sha256(stub_asarray(self.shares).tobytes(order='F')).hexdigest().upper()
        units = tuple((key, 'invented_unit') for key in binding.REQUIRED_UNITS if key != 'S') + (('S', 'dimensionless'),)
        declarations = tuple(binding.InputDeclaration(MODEL, AXIS, stage, units, self.source)
                             for stage in binding.STAGES)
        self.bound = binding.FixedC8InputBinding(self.states, self.shares, self.batch,
            *declarations, MODEL_MAPPING, ((0, 101, AXIS[0][1]), (1, 907, AXIS[1][1])))
        self.calls = []
        self.dispatched_inputs = []
        def factory(**kwargs):
            self.calls.append('factory')
            self.assertIs(kwargs['phi_destination_origin'], self.array.phi_destination_origin)
            return kwargs
        def migration(value):
            self.calls.append('migration')
            return SimpleNamespace(lt_supply=(1.0, 1.0))
        def wages(provinces, firm_wages, phi, distance, **kwargs):
            self.calls.append('wages')
            self.assertIs(phi, self.array.phi_destination_origin)
            return ('invented dispatch result',)
        self.spies = integration.SyntheticSpies(factory, migration, blocked, wages)
        original_run = middle.PreparedMiddleStage.run
        def dispatch_stub(stage, inputs, migration, shares, share_sha):
            # The true preparation and pre-spy contracts are exercised; the
            # numerical middle.run body is deliberately NOT exercised.
            middle.PreparedMiddleStage.validate_pre_spy(stage, inputs, shares, share_sha,
                annual_context=stage.annual_context, prepared_array=stage.prepared_array,
                province_mapping=stage.province_mapping, ledger=stage.ledger)
            self.calls.append('middle_dispatch_stub')
            self.assertIs(stage, self.middle)
            self.assertIs(inputs.household_outputs, self.batch)
            self.dispatched_inputs.append(inputs)
            return middle.MiddleStageResult((SimpleNamespace(wjt=2.0),
                SimpleNamespace(wjt=3.0)), capital=None, c1=None)
        middle.PreparedMiddleStage.run = dispatch_stub
        self.addCleanup(setattr, middle.PreparedMiddleStage, 'run', original_run)

    def invoke(self, **changes):
        args = dict(repository=None, task_root=None, turn_root=None, turn=8,
            states=self.states, batch=self.batch, frozen_shares=self.shares,
            expected_share_sha=self.share_sha, ledger=self.ledger, household_rows=(),
            annual_context=self.context, target_year=2018, province_axis=AXIS,
            source_sha256=self.sha, input_kind='synthetic', price_basis='synthetic_fixture',
            price_verified=False, params=dict(ga=.5, phi_l=1.0, alphal=.5,
                epsilon=2.0, theta=1.0, delta=.025),
            migration_wedge_destination_origin=((1.0, 2.0), (3.0, 1.0)),
            spies=self.spies, prepared_array=self.array, province_mapping=ANNUAL_MAPPING,
            prepared_middle_stage=self.middle, fixed_c8_binding=self.bound,
            fixed_c8_external_source=self.source)
        args.update(changes)
        return integration.integrate_turn(**args)

    def reject(self, **changes):
        ledger = changes.get('ledger', self.ledger)
        before = dict(ledger)
        self.calls.clear()
        with self.assertRaises(ValueError):
            self.invoke(**changes)
        self.assertEqual(ledger, before)
        self.assertEqual(self.calls, [])

    def test_stub_dispatch_reuses_bound_views_order_master_and_batch(self):
        originals = tuple(dict(row) for row in self.states)
        result = self.invoke()
        self.assertEqual(self.calls, ['factory', 'migration', 'middle_dispatch_stub', 'wages'])
        inputs = result['inputs']
        self.assertIs(inputs, self.dispatched_inputs[0])
        self.assertIs(inputs.phi_destination_origin, self.array.phi_destination_origin)
        self.assertEqual(inputs.province_order, ('Alpha', 'Beta'))
        self.assertEqual(self.states, originals)
        for index, view in enumerate(inputs.old_provinces):
            self.assertIs(view['_fixed_c8_original_state'], self.states[index])
            self.assertEqual((view['province_index'], view['source_province_name']), AXIS[index])
        self.assertEqual(self.ledger['source_faithful_labor_reconstructions'], 1)
        self.assertEqual(self.ledger['composite_wage_batches'], 1)
        for key in middle.LEDGER_KEYS:
            if key not in ('source_faithful_labor_reconstructions', 'composite_wage_batches'):
                self.assertEqual(self.ledger[key], 0, 'numerical middle body was not tested')
        self.assertIsNone(result['middle_result'].capital)
        self.assertIsNone(result['middle_result'].c1)
        self.assertFalse(result['model_activation'])

    def test_changed_mapping_and_missing_array_reject_before_spies(self):
        self.reject(province_mapping=tuple(reversed(ANNUAL_MAPPING)))
        self.reject(prepared_array=None)

    def test_changed_ledger_object_and_share_identity_reject_before_spies(self):
        self.reject(ledger=dict(self.ledger))
        self.reject(expected_share_sha='0' * 64)

    def test_external_axis_conflict_rejects_before_middle_dispatch(self):
        conflict = binding.ExternalSourceAxis('invented_fixture', self.sha,
            'synthetic_identifier', tuple(reversed(self.source.axis)))
        self.reject(fixed_c8_external_source=conflict)


if __name__ == '__main__':
    if len(sys.argv) != 1:
        raise SystemExit('No arguments or real input files accepted.')
    unittest.main(verbosity=2)
