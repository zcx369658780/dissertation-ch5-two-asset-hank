"""Four fixed invented tests/five scopes; project IO is audited, production code unchanged."""
import os
from pathlib import Path
import sys
import json
import hashlib
import importlib.util
import importlib.machinery
import time
import unittest
from types import SimpleNamespace
from dataclasses import FrozenInstanceError

ROOT = Path(__file__).resolve().parents[1]
DIAG = ROOT / 'validators/multi_province/annual_observed_labor_diagnostic'
ANNUAL = ROOT / 'src/ch5_two_asset_hank/corrected_diagnostic'
PROJECT_PATHS = {
    'integration': DIAG / 'integration.py',
    'pipeline': DIAG / 'staged_frozen_pipeline.py',
    'binding': DIAG / 'fixed_c8_input_binding.py',
    'middle': DIAG / 'middle_stage.py',
    'context': ANNUAL / 'annual_observed_labor_context.py',
    'array': ANNUAL / 'annual_labor_array_adapter.py',
    'helper': ANNUAL / 'lagged_observed_gdp_wedge.py',
    'adapter': DIAG / 'synthetic_c8_lifetime_adapter.py',
    'test': Path(__file__).resolve(),
}
ROOT_KEY = os.path.normcase(os.path.abspath(ROOT))
ALLOWED = {os.path.normcase(os.path.abspath(p)): k for k, p in PROJECT_PATHS.items()}
IO = {'observed_project_opens': 0, 'helper_opens': 0, 'by_file': {}, 'violation': None,
      'system_package_file_reads': 'UNKNOWN',
      'initial_test_script_open_before_hook': 'NOT_OBSERVED',
      'project_open_cap': 256, 'helper_open_cap': 128}

def audit_project_open(event, args):
    if event != 'open' or not isinstance(args[0], (str, bytes, os.PathLike)):
        return
    key = os.path.normcase(os.path.abspath(os.fsdecode(args[0])))
    if key != ROOT_KEY and not key.startswith(ROOT_KEY + os.sep):
        return
    name = ALLOWED.get(key)
    mode, flags = args[1], args[2]
    writing = (isinstance(mode, str) and any(c in mode for c in 'wax+')) or (
        isinstance(flags, int) and bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)))
    if name is None or writing:
        IO['violation'] = 'project path outside source allowlist or write attempt'
        raise RuntimeError(IO['violation'])
    IO['observed_project_opens'] += 1
    IO['by_file'][name] = IO['by_file'].get(name, 0) + 1
    if name == 'helper':
        IO['helper_opens'] += 1
    # Reserve one for the interpreter's pre-hook script read, which cannot be observed here.
    if IO['observed_project_opens'] + 1 > 256 or IO['helper_opens'] > 128:
        IO['violation'] = 'project/helper open cap exceeded'
        raise RuntimeError(IO['violation'])

sys.addaudithook(audit_project_open)
import numpy as np

CURRENT_PINS = {
    "validators/multi_province/annual_observed_labor_diagnostic/integration.py": "56494072026A140C97EAC30EAD7A2E46BF0C2C6AEF8F5B65BCFDB14D883E60A7",
    "validators/multi_province/annual_observed_labor_diagnostic/staged_frozen_pipeline.py": "2DBBA7083A548EF286B905A0DF7632402543FE39472A7178818DDE3DCC6C2FD9",
    "validators/multi_province/annual_observed_labor_diagnostic/fixed_c8_input_binding.py": "D846E0EC2DF047E6E15C0682B18967B5E1DD8D7AAF6BF986CAA2F9632A1D9538",
    "validators/multi_province/annual_observed_labor_diagnostic/middle_stage.py": "9AB2B3A06C5FB8524C78EB2714BC89D82C74E68E95D309C2C897F0B774676562",
    "src/ch5_two_asset_hank/corrected_diagnostic/annual_observed_labor_context.py": "0AA27B67030115DEC06F9F7A5F78F0113380ABC857D3F08189982EB90E3D8AFE",
    "src/ch5_two_asset_hank/corrected_diagnostic/annual_labor_array_adapter.py": "137BFB6C3F0B3D7F4672A78ECCB006A776CB1A40B258CB30A3B18437D4BFCF41",
    "src/ch5_two_asset_hank/corrected_diagnostic/lagged_observed_gdp_wedge.py": "7B9A490F382E3007820E70C68D2EFB5992DE25BC8455EDE8B265CA33F384AF56",
    "validators/multi_province/annual_observed_labor_diagnostic/synthetic_c8_lifetime_adapter.py": "8F4336CD676561158BF729EB30399541A7CC191D44424BC19A18B9DC34C6FA6B"
}

class ExactSourceLoader(importlib.machinery.SourceFileLoader):
    def get_code(self, fullname):
        # Legitimate source loading only; do not attempt existing project pyc files.
        source = self.get_data(self.path)
        relative = Path(self.path).relative_to(ROOT).as_posix()
        if relative in CURRENT_PINS and hashlib.sha256(source).hexdigest().upper() != CURRENT_PINS[relative]:
            raise RuntimeError('exact current source pin changed at runtime')
        return self.source_to_code(source, self.path)

def load_exact(label):
    path = PROJECT_PATHS[label]
    name = '_annual_accepted_wedge_helper' if label == 'helper' else '_c8_lifetime_' + label
    spec = importlib.util.spec_from_file_location(name, path, loader=ExactSourceLoader(name, str(path)))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

# Preload the exact allowed helper; the unchanged context _helper still reads/checks its pin.
HELPER = load_exact('helper')
CONTEXT = load_exact('context')
ARRAY = load_exact('array')
PIPELINE = load_exact('pipeline')
BINDING = load_exact('binding')
INTEGRATION = load_exact('integration')
MIDDLE = load_exact('middle')
ADAPTER = load_exact('adapter')
RESULTS = []
SCOPES = []
START = time.time_ns()

def stable_inputs(b):
    scalars = json.dumps({'states': b['states'], 'params': b['params']},
                        sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
    arrays = tuple((label, arr.shape, arr.dtype.str, arr.tobytes(order='F' if label == 'S' else 'C').hex())
        for label, arr in [('S', b['frozen_shares']), ('distance', b['distance'])] +
        [(k, getattr(b['batch'], k)) for k in ('ct', 'at', 'bt', 'at_tax', 'household_lt')])
    digest = hashlib.sha256(scalars + json.dumps(arrays).encode('utf-8')).hexdigest().upper()
    refs = (b['states'], *b['states'], b['frozen_shares'], b['batch'], b['params'], b['distance'],
            *(getattr(b['batch'], k) for k in ('ct', 'at', 'bt', 'at_tax', 'household_lt')))
    return digest, refs

class LifetimeTests(unittest.TestCase):
    def make_case(self, label, wrong_stage=False, mutation=False, c1_input_mutation=False,
                  cleanup_failures=False):
        n = 31
        axis = tuple((i + 1, 'invented-full-' + str(i)) for i in range(n))
        mapping = tuple((i + 1, full, 'invented-short-' + str(i)) for i, (_, full) in enumerate(axis))
        fixture = dict(schema='CH5_INVENTED_ANNUAL_FIXTURE_V1', input_kind='synthetic',
            target_year=2018, observation_year=2017, province_axis=axis,
            price_basis='synthetic_fixture', price_verified=False,
            records=[(i + 1, 2017, 10.0 + i, 10.0) for i in range(n)])
        raw = json.dumps(fixture, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
        sha = hashlib.sha256(raw).hexdigest().upper()
        context = CONTEXT.prepare_synthetic_context(raw, expected_fixture_sha256=sha,
                                                    province_axis=axis, target_year=2018)
        meta = dict(target_year=2018, province_axis=axis, source_sha256=sha, input_kind='synthetic',
                    price_basis='synthetic_fixture', price_verified=False)
        array = ARRAY.prepare_annual_array(context, province_mapping=mapping, **meta)
        states = tuple(dict(name=short, province_index=i, source_province_name=full,
            N=10.0, wjt=1.0, tau=0.1, inter_prv_ratio=0.5, Kt0=30.0, alpha=0.3, Zt=1.0,
            pit=1.0, Kt_prev=30.0, Zt_1=1.0, pit_1=1.0, rk=0.02, corptau=0.2, Tt=0.1,
            ramin=0.0, ramax=1.0, wjtmin=0.0, wjtmax=10.0)
            for i, (_, full, short) in enumerate(mapping))
        shares = np.full((n, n), 0.5 / 30, dtype=np.float64)
        np.fill_diagonal(shares, 0.5)
        batch = SimpleNamespace(ct=np.full(n, 1.0), at=np.full(n, 2.0), bt=np.full(n, 0.1),
                                at_tax=np.full(n, 0.2), household_lt=np.full(n, 0.5))
        params = dict(ga=0.2, phi_l=2.0, alphal=0.3, epsilon=2.0, theta=0.1, delta=0.05)
        distance = np.ones((n, n), dtype=np.float64)
        model_axis = tuple((i, short) for i, (_, _, short) in enumerate(mapping))
        external_rows = tuple((1007 + i * 13, axis[i][1]) for i in reversed(range(n)))
        consumer_external = BINDING.ExternalSourceAxis('invented_fixture', sha, 'synthetic_identifier', external_rows)
        units = tuple((field, 'dimensionless' if field == 'S' else 'invented-unit-' + field)
                      for field in BINDING.REQUIRED_UNITS)
        declarations = tuple(BINDING.InputDeclaration(model_axis, axis,
            'wrong-household-stage' if wrong_stage and i == 2 else stage, units,
            BINDING.ExternalSourceAxis('invented_fixture', sha, 'synthetic_identifier', external_rows))
            for i, stage in enumerate(BINDING.STAGES))
        c8map = tuple((i, short, annual, full) for i, (annual, full, short) in enumerate(mapping))
        by_full = {full: identifier for identifier, full in external_rows}
        extmap = tuple((i, by_full[full], full) for i, (_, full) in enumerate(axis))
        binding = BINDING.FixedC8InputBinding(states, shares, batch, *declarations, c8map, extmap)
        ledger = dict(engineering_fixture_label='invented-' + label, **{k: 0 for k in MIDDLE.LEDGER_KEYS})
        events, observed_phi = [], []
        resource = dict(provider=0, carrier_factory=0, handle_factory=0, handle_acquire=0,
                        handle_close=0, provider_close=0, binding_validate=0, integration=0, middle=0)
        tokens = []
        cleanup_order = []
        cleanup_markers = (RuntimeError('invented handle cleanup failure'),
                           RuntimeError('invented provider cleanup failure'))
        def migration_factory(**kwargs):
            events.append('factory')
            self.assertIs(kwargs['phi_destination_origin'], array.phi_destination_origin)
            self.assertIs(kwargs['migration_wedge_destination_origin'], distance)
            self.assertIs(kwargs['consumption_by_origin'], batch.ct)
            self.assertEqual(kwargs['population_by_origin'], [10.0] * n)
            observed_phi.append(kwargs['phi_destination_origin'])
            return SimpleNamespace(**kwargs)
        def labor(inputs):
            events.append('labor')
            self.assertIs(inputs.phi_destination_origin, array.phi_destination_origin)
            return SimpleNamespace(lt_supply=np.full(n, 5.0))
        def unused_firm(*args, **kwargs):
            self.fail('opaque firm callback must not replace prepared middle')
        def c1(*, Ktarget_MU, Kprivate_current_MU, province_order):
            events.append('c1')
            if c1_input_mutation:
                Ktarget_MU[0] += 1.0  # Local callback input only; never borrowed source values.
            self.assertEqual(province_order, array.province_order)
            return SimpleNamespace(province_order=province_order,
                GovInv_residual_MU=tuple(np.maximum(Ktarget_MU - Kprivate_current_MU, 0.0)),
                firm_K_accounting_MU=tuple(np.maximum(Ktarget_MU, Kprivate_current_MU)))
        def firm(source, private, labor_supply, supplied_params):
            events.append('firm')
            self.assertEqual(source['AtTax'], 0.2)
            self.assertEqual(source['Lt_prev'], 0.5)
            self.assertEqual(dict(supplied_params), params)
            values = {k: 1.0 for k in MIDDLE.FIRM_FIELDS}
            values.update(Kt=max(source['Kt0'], private), Lt=labor_supply)
            return SimpleNamespace(**values)
        def wages(provinces, wage_vector, phi, supplied_distance, **kwargs):
            events.append('wage')
            self.assertIs(phi, array.phi_destination_origin)
            self.assertIs(supplied_distance, distance)
            observed_phi.append(phi)
            self.assertEqual(wage_vector, [1.0] * n)
            for i, row in enumerate(provinces):
                self.assertEqual((row['province_index'], row['source_province_name']), axis[i])
                self.assertIs(row['_fixed_c8_original_state'], states[i])
                self.assertEqual(row['_fixed_c8_model_identity'], model_axis[i])
            return tuple(1.0 for _ in range(n))
        spies = INTEGRATION.SyntheticSpies(migration_factory, labor, unused_firm, wages)
        middle = MIDDLE.prepare_middle_stage(annual_context=context, prepared_array=array,
            province_mapping=mapping, ledger=ledger,
            dependencies=MIDDLE.FixtureDependencies(c1, firm, 'invented-c1-firm-' + label))
        expected_share_sha = hashlib.sha256(shares.astype('<f8', copy=False).tobytes(order='F')).hexdigest().upper()
        borrowed = dict(states=states, batch=batch, frozen_shares=shares, params=params,
            distance=distance, annual_context=context, prepared_array=array, province_mapping=mapping,
            fixed_c8_binding=binding, fixed_c8_external_source=consumer_external,
            prepared_middle_stage=middle, spies=spies, ledger=ledger, expected_share_sha=expected_share_sha)
        def handle_factory(token):
            resource['handle_factory'] += 1
            tokens.append(token)
            if mutation:
                states[0]['N'] = 11.0
            return SimpleNamespace(token=token)
        def handle_acquire(handle):
            resource['handle_acquire'] += 1
            tokens.append(handle.token)
            return handle.token
        def handle_close(handle):
            resource['handle_close'] += 1
            cleanup_order.append('handle')
            if cleanup_failures:
                raise cleanup_markers[0]
        def provider_close():
            resource['provider_close'] += 1
            cleanup_order.append('provider')
            if cleanup_failures:
                raise cleanup_markers[1]
        session = ADAPTER.prepare_synthetic_c8_session(borrowed_inputs=borrowed,
            pipeline_class=PIPELINE.SharedInputPipeline, provider_close=provider_close,
            handle_factory=handle_factory, handle_acquire=handle_acquire, handle_close=handle_close)
        code_keys = {BINDING.FixedC8InputBinding.validate.__code__: 'binding_validate',
                     INTEGRATION.integrate_turn.__code__: 'integration',
                     MIDDLE.PreparedMiddleStage.run.__code__: 'middle',
                     session.pipeline._provider.__code__: 'provider',
                     ADAPTER.SyntheticC8Session.make_metadata_token.__code__: 'carrier_factory'}
        def profile(frame, event, arg):
            if event == 'call':
                key = code_keys.get(frame.f_code)
                if key:
                    resource[key] += 1
        return SimpleNamespace(label=label, b=borrowed, session=session, resource=resource,
            events=events, phi=observed_phi, tokens=tokens, profile=profile, before=stable_inputs(borrowed),
            original_states=tuple(dict(row) for row in states),
            cleanup_order=cleanup_order, cleanup_markers=cleanup_markers)

    def invoke(self, case):
        SCOPES.append(case.label)
        sys.setprofile(case.profile)
        try:
            return case.session.integrate_once(integration_callback=INTEGRATION.integrate_turn,
                spies=case.b['spies'], prepared_middle_stage=case.b['prepared_middle_stage'],
                ledger=case.b['ledger'], expected_share_sha=case.b['expected_share_sha'])
        finally:
            sys.setprofile(None)

    def record(self, case, error=None):
        after = stable_inputs(case.b)
        RESULTS.append(dict(label=case.label, resources=dict(case.resource), events=list(case.events),
            ledger=[case.b['ledger'][k] for k in MIDDLE.LEDGER_KEYS],
            error=type(error).__name__ if error else None, error_message=str(error) if error else None,
            closed=case.session.closed, pipeline_state=case.session.pipeline.state,
            cleanup_errors=len(case.session.pipeline.cleanup_errors),
            before_sha256=case.before[0], after_sha256=after[0],
            original_refs_unchanged=all(a is b for a, b in zip(case.before[1], after[1])),
            first_N_before=case.original_states[0]['N'], first_N_after=case.b['states'][0]['N'],
            production_model_consumer_calls=0, source_authenticated=False,
            original_live_identity_restored=False, scientific_validity_established=False,
            model_activation=False, execution_admitted=False))

    def assert_closed(self, case, acquire, binding, integration, economic):
        self.assertTrue(case.session.closed)
        self.assertEqual(case.session.pipeline.state, 'closed')
        self.assertEqual(case.resource, dict(provider=1, carrier_factory=1, handle_factory=1,
            handle_acquire=acquire, handle_close=1, provider_close=1, binding_validate=binding,
            integration=integration, middle=integration))
        self.assertEqual(case.session.pipeline.cleanup_errors, ())
        self.assertEqual([case.b['ledger'][k] for k in MIDDLE.LEDGER_KEYS], economic)
        self.assertTrue(all(token is case.tokens[0] for token in case.tokens))
        after_refs = stable_inputs(case.b)[1]
        self.assertEqual(len(after_refs), len(case.before[1]))
        self.assertTrue(all(a is b for a, b in zip(after_refs, case.before[1])))
        self.assertIsNone(case.session._b)
        with self.assertRaises(RuntimeError):
            self.invoke_again_without_scope(case)

    def invoke_again_without_scope(self, case):
        return case.session.integrate_once(integration_callback=INTEGRATION.integrate_turn,
            spies=case.b['spies'], prepared_middle_stage=case.b['prepared_middle_stage'],
            ledger=case.b['ledger'], expected_share_sha=case.b['expected_share_sha'])

    def test_T1_normal(self):
        case = self.make_case('T1')
        try:
            result = self.invoke(case)
            self.assert_closed(case, 9, 2, 1, [1, 1, 1, 1, 31, 1])
            self.assertEqual(case.events, ['factory', 'labor', 'c1'] + ['firm'] * 31 + ['wage'])
            self.assertIs(case.phi[0], case.phi[1])
            self.assertEqual(stable_inputs(case.b)[0], case.before[0])
            self.assertEqual(case.b['states'], case.original_states)
            token = case.tokens[0]
            with self.assertRaises((AttributeError, FrozenInstanceError)):
                token.axes = ()
            with self.assertRaises(AttributeError):
                token.axes[0].name = 'changed'
            self.assertFalse(any(isinstance(value, (dict, list, np.ndarray))
                                 for value in (token.axes, token.vectors, token.calendar, token.source)))
            self.assertFalse(result['model_activation'])
            self.assertFalse(result['full_outer_runtime_integrated'])
            middle = result['middle_result']
            np.testing.assert_allclose(middle.capital.wealth, [20.0] * 31, rtol=0.0, atol=1e-12)
            np.testing.assert_allclose(middle.capital.private, [20.0] * 31, rtol=0.0, atol=1e-12)
            np.testing.assert_allclose(np.sum(middle.capital.flows, axis=0), middle.capital.wealth,
                                       rtol=0.0, atol=1e-12 * 620.0)
            self.assertEqual(middle.capital.domestic, (10.0,) * 31)
            self.assertLessEqual(abs(middle.capital.capital_residual), 1e-12 * 620.0)
            self.assertEqual(middle.c1.firm_K_accounting_MU, (30.0,) * 31)
            self.assertEqual(middle.c1.GovInv_residual_MU,
                             tuple(max(30.0 - p, 0.0) for p in middle.capital.private))
            self.assertEqual(tuple(f.Kt for f in middle.firms), (30.0,) * 31)
            self.assertFalse(middle.model_activation)
            self.assertFalse(middle.full_outer_runtime_integrated)
        finally:
            self.record(case)

    def test_T2_failures(self):
        for label, wrong_stage, mutation in [('F1', True, False), ('F2', False, True)]:
            with self.subTest(label=label):
                case = self.make_case(label, wrong_stage, mutation)
                expected_type = ADAPTER.BorrowedValueChanged if mutation else ValueError
                error = None
                try:
                    try:
                        self.invoke(case)
                    except expected_type as caught:
                        error = caught
                    else:
                        self.fail('fixed failure case was admitted')
                    if mutation:
                        self.assertIs(type(error), ADAPTER.BorrowedValueChanged)
                        self.assertIn('preflight: states changed', str(error))
                        self.assertEqual(case.b['states'][0]['N'], 11.0)
                        restored_comparison = tuple(dict(row) for row in case.b['states'])
                        restored_comparison[0]['N'] = 10.0  # copy only; never roll back the borrowed state.
                        self.assertEqual(restored_comparison, case.original_states)
                        self.assertNotEqual(stable_inputs(case.b)[0], case.before[0])
                    else:
                        self.assertIs(type(error), ValueError)
                        self.assertIn('stage mismatch', str(error))
                        self.assertEqual(stable_inputs(case.b)[0], case.before[0])
                    self.assertEqual(case.events, [])
                    self.assert_closed(case, 2, 0 if mutation else 1, 0, [0] * 6)
                finally:
                    self.record(case, error)
                # subTest normally continues after failure; this task must stop on its first failure.
                if self._outcome.result.failures or self._outcome.result.errors:
                    break

    def test_T3_C1_input_mutation(self):
        case = self.make_case('T3_C1_input_mutation', c1_input_mutation=True)
        error = None
        try:
            with self.assertRaises(ValueError) as raised:
                self.invoke(case)
            error = raised.exception
            self.assertIs(type(error), ValueError)
            self.assertEqual(str(error), 'C1 callback mutated frozen capital inputs')
            self.assertEqual(case.events, ['factory', 'labor', 'c1'])
            # prepare:1 + preflight:1 + factory before/after:2 + labor before/after:2.
            # Adapter preflight binding:1 + integration fixed-C8 binding:1.
            self.assert_closed(case, 6, 2, 1, [1, 1, 1, 1, 0, 0])
            after = stable_inputs(case.b)
            self.assertEqual(after[0], case.before[0])
            self.assertEqual(len(after[1]), len(case.before[1]))
            self.assertTrue(all(a is b for a, b in zip(after[1], case.before[1])))
            self.assertEqual(case.b['states'], case.original_states)
        finally:
            self.record(case, error)

    def test_T4_double_cleanup_failure(self):
        case = self.make_case('T4_double_cleanup_failure', cleanup_failures=True)
        error = None
        SCOPES.append(case.label)
        sys.setprofile(case.profile)
        try:
            case.session.pipeline.prepare()
            self.assertEqual(case.session.pipeline.state, 'prepared')
            with self.assertRaises(PIPELINE.CleanupError) as raised:
                case.session.close()
            error = raised.exception
            self.assertIs(type(error), PIPELINE.CleanupError)
            self.assertEqual(str(error), 'pipeline cleanup failed; see errors')
            self.assertIs(type(error.errors), tuple)
            self.assertIs(type(case.session.pipeline.cleanup_errors), tuple)
            self.assertEqual(len(error.errors), 2)
            self.assertEqual(len(case.session.pipeline.cleanup_errors), 2)
            for actual, marker in zip(error.errors, case.cleanup_markers):
                self.assertIs(actual, marker)
            for actual, marker in zip(case.session.pipeline.cleanup_errors, case.cleanup_markers):
                self.assertIs(actual, marker)
            self.assertEqual(case.cleanup_order, ['handle', 'provider'])
            self.assertTrue(case.session.closed)
            self.assertEqual(case.session.pipeline.state, 'closed')
            self.assertIsNone(case.session._b)
            self.assertIsNone(case.session._baseline)
            self.assertEqual(case.session._refs, ())
            self.assertIsNone(case.session.pipeline._carrier)
            self.assertIsNone(case.session.pipeline._handle)
            self.assertFalse(case.session.pipeline._handle_returned)
            self.assertFalse(case.session.pipeline._provider_attempted)
            expected_resources = dict(provider=1, carrier_factory=1, handle_factory=1,
                handle_acquire=1, handle_close=1, provider_close=1,
                binding_validate=0, integration=0, middle=0)
            self.assertEqual(case.resource, expected_resources)
            self.assertEqual(case.events, [])
            self.assertEqual([case.b['ledger'][k] for k in MIDDLE.LEDGER_KEYS], [0] * 6)
            after = stable_inputs(case.b)
            self.assertEqual(after[0], case.before[0])
            self.assertEqual(len(after[1]), len(case.before[1]))
            self.assertTrue(all(a is b for a, b in zip(after[1], case.before[1])))
            self.assertEqual(case.b['states'], case.original_states)
            case.session.close()  # Failed cleanup ownership is consumed; no retry.
            self.assertEqual(case.resource, expected_resources)
            self.assertEqual(case.cleanup_order, ['handle', 'provider'])
            self.assertEqual(len(case.session.pipeline.cleanup_errors), 2)
            for actual, marker in zip(case.session.pipeline.cleanup_errors, case.cleanup_markers):
                self.assertIs(actual, marker)
            with self.assertRaises(RuntimeError):
                self.invoke_again_without_scope(case)
        finally:
            sys.setprofile(None)
            self.record(case, error)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2, failfast=True)
    result = runner.run(unittest.TestSuite([LifetimeTests('test_T1_normal'), LifetimeTests('test_T2_failures'),
                                          LifetimeTests('test_T3_C1_input_mutation'),
                                          LifetimeTests('test_T4_double_cleanup_failure')]))
    summary = dict(tests_run=result.testsRun, successful=result.wasSuccessful(), failures=len(result.failures),
        errors=len(result.errors), scope_labels=SCOPES, cases=RESULTS, project_io=IO,
        test_elapsed_ms=(time.time_ns() - START) // 1_000_000,
        actual_integration_calls=sum(c['resources']['integration'] for c in RESULTS),
        production_model_consumer_hjb_kfe_calls=0,
        added_coverage=['C1 callback input mutation rejection', 'explicit double cleanup failure'],
        untested=['primary-exception cleanup failure', 'late mutation',
                  'callback restores transient mutation', 'concurrent TOCTOU'])
    print(json.dumps(summary, ensure_ascii=False, separators=(',', ':')), flush=True)
    sys.exit(0 if result.wasSuccessful() and IO['violation'] is None else 1)