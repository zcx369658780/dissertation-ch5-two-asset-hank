"""Single-use invented C8 boundary adapter; no production or source attestation."""
from dataclasses import dataclass
from collections import namedtuple
from pathlib import Path
from types import SimpleNamespace
import hashlib
import math
import struct
import sys
import numpy as np
_KEYS = ('states', 'batch', 'frozen_shares', 'params', 'distance', 'annual_context',
         'prepared_array', 'province_mapping', 'fixed_c8_binding',
         'fixed_c8_external_source', 'prepared_middle_stage', 'spies', 'ledger',
         'expected_share_sha')
_BATCH = ('ct', 'at', 'bt', 'at_tax', 'household_lt')
_SCALARS = (type(None), bool, int, float, str)
_SOURCE = Path(__file__).resolve().parents[3] / 'src/ch5_two_asset_hank/corrected_diagnostic'
class BorrowedValueChanged(ValueError):
    """Declared boundary detected a borrowed reference/value change."""
Axis = namedtuple('Axis', 'source_id name order')
Vector = namedtuple('Vector', 'field unit')
Calendar = namedtuple('Calendar', 'target_year observation_year label')
Source = namedtuple('Source', 'source_id label')
@dataclass(frozen=True, slots=True)
class SyntheticC8CarrierToken:
    axes: tuple; vectors: tuple
    calendar: Calendar; source: Source; session_key: object
def _module(value, name, path, is_class=False):
    module = sys.modules.get(value.__module__ if is_class else type(value).__module__)
    target = value if is_class else type(value)
    if (module is None or getattr(module, name, None) is not target
            or Path(getattr(module, '__file__', '')).resolve() != path.resolve()):
        raise ValueError('exact admitted module/type required: ' + name)
    return module
def _encode(value, order='C'):
    kind = type(value)
    if kind is type(None):
        return b'n'
    if kind is bool:
        return b'b1' if value else b'b0'
    if kind is int:
        data = str(value).encode('ascii')
        tag = b'i'
    elif kind is float:
        if not math.isfinite(value):
            raise ValueError('finite exact float required')
        return b'f' + struct.pack('<d', value)
    elif kind is str:
        data, tag = value.encode('utf-8', 'strict'), b's'
    elif kind is tuple:
        data, tag = b''.join(_encode(v) for v in value), b't'
    elif kind is dict:
        if any(type(k) is not str for k in value):
            raise ValueError('exact string keys required')
        data, tag = _encode(tuple((k, value[k]) for k in sorted(value))), b'd'
    elif kind is np.ndarray:
        if value.dtype != np.dtype('<f8') or not np.isfinite(value).all():
            raise ValueError('finite exact little-endian float64 array required')
        data = _encode((value.shape, value.dtype.str, order)) + value.tobytes(order=order)
        tag = b'a'
    else:
        raise ValueError('undeclared borrowed type: ' + kind.__name__)
    return tag + struct.pack('<Q', len(data)) + data
def _fields(value):
    return tuple((k, getattr(value, k)) for k in value.__dataclass_fields__
                 if not k.startswith('_'))
class SyntheticC8Session:
    def __init__(self, *, borrowed_inputs, pipeline_class, provider_close,
                 handle_factory, handle_acquire, handle_close):
        self._b, self._closed, self._used = borrowed_inputs, False, False
        self._key, self._token = object(), None
        self._pipeline_module = _module(pipeline_class, 'SharedInputPipeline', Path(__file__).with_name('staged_frozen_pipeline.py'), True)
        self._admit()
        self._baseline, self._refs = self._snapshot()
        b, c, binding = self._b, self._b['annual_context'], self._b['fixed_c8_binding']
        expected = dict(axes=[dict(source_id=i, name=short, order=i)
                             for i, short, _, _ in binding.province_mapping],
            field_names=[f for f, _ in binding.state_declaration.unit_contract],
            units=dict(binding.state_declaration.unit_contract),
            calendar=dict(target_year=2018, observation_year=2017, label='invented_fixture'),
            source=dict(source_id='invented_fixture', label='synthetic_identifier'))
        self.pipeline = pipeline_class(provider=lambda: {}, provider_close=provider_close,
            carrier_factory=self.make_metadata_token, handle_factory=handle_factory,
            handle_acquire=handle_acquire, handle_close=handle_close, expected=expected)
    @property
    def closed(self):
        return self._closed
    def _admit(self):
        b = self._b
        if type(b) is not dict or set(b) != set(_KEYS):
            raise ValueError('exact declared borrowed bundle required')
        c, a, binding = b['annual_context'], b['prepared_array'], b['fixed_c8_binding']
        cm = _module(c, 'AnnualContext', _SOURCE / 'annual_observed_labor_context.py')
        am = _module(a, 'AnnualArrayCarrier', _SOURCE / 'annual_labor_array_adapter.py')
        self._binding_module = _module(binding, 'FixedC8InputBinding', Path(__file__).with_name('fixed_c8_input_binding.py'))
        self._integration_module = _module(b['spies'], 'SyntheticSpies', Path(__file__).with_name('integration.py'))
        mm = _module(b['prepared_middle_stage'], 'PreparedMiddleStage', Path(__file__).with_name('middle_stage.py'))
        if (type(c.target_year) is not int or c.target_year != 2018
                or type(c.observation_year) is not int or c.observation_year != 2017
                or c.input_kind != 'synthetic' or c.price_basis != 'synthetic_fixture'
                or c.price_verified is not False or c.model_activation is not False
                or c.wedge.binding.source_identifier != 'invented_fixture'
                or len(c.province_axis) != 31):
            raise ValueError('invented 31-axis 2018/2017 only')
        metadata = dict(target_year=2018, province_axis=c.province_axis,
            source_sha256=c.source_sha256, input_kind=c.input_kind,
            price_basis=c.price_basis, price_verified=False)
        cm.AnnualContext.validate(c, **metadata)
        am.AnnualArrayCarrier.validate(a, annual_context=c,
            province_mapping=b['province_mapping'], **metadata)
        mm.PreparedMiddleStage._validate(b['prepared_middle_stage'], annual_context=c,
            prepared_array=a, province_mapping=b['province_mapping'], ledger=b['ledger'])
        if type(b['states']) is not tuple or len(b['states']) != 31:
            raise ValueError('exact 31-state tuple required')
        for row in b['states']:
            if (type(row) is not dict or not set(mm.STATE_FIELDS) <= set(row)
                    or any(type(k) is not str or type(v) not in _SCALARS for k, v in row.items())):
                raise ValueError('complete primitive state schema required')
        if (type(b['params']) is not dict or not set(mm.PARAM_FIELDS) <= set(b['params'])
                or any(type(k) is not str or type(v) not in _SCALARS + (np.ndarray,)
                       for k, v in b['params'].items())):
            raise ValueError('explicit primitive/array parameter schema required')
        if type(b['batch']) is not SimpleNamespace or set(vars(b['batch'])) != set(_BATCH):
            raise ValueError('exact five-vector invented batch required')
        for values, shape in [(b['frozen_shares'], (31, 31)), (b['distance'], (31, 31))] + [
                (getattr(b['batch'], k), (31,)) for k in _BATCH]:
            if type(values) is not np.ndarray or values.shape != shape:
                raise ValueError('exact declared ndarray axes required')
            _encode(values)
        declarations = (binding.state_declaration, binding.share_declaration,
                        binding.household_declaration)
        for declaration in declarations:
            if (type(declaration) is not self._binding_module.InputDeclaration
                    or type(declaration.external_source) is not self._binding_module.ExternalSourceAxis):
                raise ValueError('exact component declarations required')
        ext = b['fixed_c8_external_source']
        if (type(ext) is not self._binding_module.ExternalSourceAxis
                or any(e.identifier_kind != 'synthetic_identifier' for e in
                       (ext,) + tuple(d.external_source for d in declarations))):
            raise ValueError('explicit synthetic external identifiers required')
    def _snapshot(self):
        b, c, a = self._b, self._b['annual_context'], self._b['prepared_array']
        binding, middle = b['fixed_c8_binding'], b['prepared_middle_stage']
        ds = (binding.state_declaration, binding.share_declaration, binding.household_declaration)
        ext = b['fixed_c8_external_source']
        values = dict(states=b['states'], params=b['params'], S=_encode(b['frozen_shares'], 'F').hex(),
            batch=tuple((k, getattr(b['batch'], k)) for k in _BATCH), distance=b['distance'],
            metadata=(c.target_year, c.observation_year, c.province_axis, c.source_sha256,
                c.input_kind, c.price_basis, c.price_verified, c.model_activation, c.provenance,
                c.phi_destination_origin, _fields(c.wedge.binding), c.wedge.per_capita_gdp,
                c.wedge.amplitude, c.wedge.target_year, c.wedge.observation_year, c.wedge.province_order,
                b['province_mapping'], binding.province_mapping, binding.external_mapping,
                tuple((d.model_axis, d.annual_axis, d.stage, d.unit_contract,
                       _fields(d.external_source)) for d in ds), _fields(ext),
                a.province_order, middle.dependencies.fixture_label, b['expected_share_sha']))
        refs = [b] + [b[k] for k in _KEYS] + list(b['states']) + [getattr(b['batch'], k) for k in _BATCH]
        refs += [c._seal, c.wedge, c.wedge.binding, c.phi_destination_origin,
                 a._seal, a.phi_destination_origin, a.backing_bytes, middle._seal, middle.dependencies]
        refs += [binding.states, binding.frozen_shares, binding.batch, binding.province_mapping,
                 binding.external_mapping, middle.annual_context, middle.prepared_array, middle.ledger,
                 middle.province_mapping, c._preparation_token, a._preparation_token]
        refs += [v for d in ds for v in (d.model_axis, d.annual_axis, d.unit_contract)]
        refs += list(ds) + [d.external_source for d in ds] + [
            getattr(b['spies'], k) for k in b['spies'].__dataclass_fields__]
        refs += [middle.dependencies.c1_residual, middle.dependencies.evaluate_firm]
        refs += [v for v in b['params'].values() if type(v) is np.ndarray]
        return {k: hashlib.sha256(_encode(v)).digest() for k, v in values.items()}, tuple(refs)
    def make_metadata_token(self, **payload):
        if payload or self._token is not None:
            raise ValueError('single inert metadata preparation required')
        d = self._b['fixed_c8_binding'].state_declaration
        self._token = SyntheticC8CarrierToken(tuple(Axis(i, n, i) for i, n in d.model_axis),
            tuple(Vector(f, u) for f, u in d.unit_contract), Calendar(2018, 2017, 'invented_fixture'),
            Source('invented_fixture', 'synthetic_identifier'), self._key)
        return self._token
    def guard_boundary(self, stage):
        token = self.pipeline.acquire()
        if type(token) is not SyntheticC8CarrierToken or token is not self._token or token.session_key is not self._key:
            raise BorrowedValueChanged(stage + ': token identity changed')
        try:
            self._pipeline_module._check_metadata(token, self.pipeline._expected)
            if any(type(v) is not Axis for v in token.axes) or any(type(v) is not Vector for v in token.vectors):
                raise ValueError('exact immutable token metadata required')
            if type(token.calendar) is not Calendar or type(token.source) is not Source:
                raise ValueError('exact immutable token calendar/source required')
            self._admit()
            current, refs = self._snapshot()
        except Exception as error:
            raise BorrowedValueChanged(stage + ': borrowed schema/metadata changed') from error
        if len(refs) != len(self._refs) or any(x is not y for x, y in zip(refs, self._refs)):
            raise BorrowedValueChanged(stage + ': borrowed references changed')
        for key in current:
            if current[key] != self._baseline[key]:
                raise BorrowedValueChanged(stage + ': ' + key + ' changed')
    def wrap_fixture_callback(self, stage, callback):
        def wrapped(*args, **kwargs):
            self.guard_boundary(stage + '.before')
            try:
                result = callback(*args, **kwargs)
            except BaseException as primary:
                try:
                    self.guard_boundary(stage + '.after_failure')
                except BaseException as secondary:
                    primary.add_note('secondary boundary error: ' + str(secondary))
                raise
            self.guard_boundary(stage + '.after')
            return result
        return wrapped
    def integrate_once(self, *, integration_callback, spies, prepared_middle_stage,
                       ledger, expected_share_sha, household_rows=()):
        if self._closed or self._used: raise RuntimeError('single-use session already consumed')
        self._used = True
        b, c = self._b, self._b['annual_context']
        try:
            if (integration_callback is not self._integration_module.integrate_turn or
                    spies is not b['spies'] or prepared_middle_stage is not b['prepared_middle_stage'] or
                    ledger is not b['ledger'] or expected_share_sha != b['expected_share_sha'] or
                    type(household_rows) is not tuple or household_rows):
                raise ValueError('exact integration and declared borrowed arguments required')
            with self.pipeline:
                self.guard_boundary('preflight')
                self._binding_module.FixedC8InputBinding.validate(b['fixed_c8_binding'],
                    states=b['states'], frozen_shares=b['frozen_shares'], batch=b['batch'], turn=8,
                    province_axis=c.province_axis, province_mapping=b['province_mapping'], input_kind='synthetic',
                    external_source=b['fixed_c8_external_source'], source_identifier='invented_fixture',
                    source_sha256=c.source_sha256)
                wrapped = self._integration_module.SyntheticSpies(
                    self.wrap_fixture_callback('factory', spies.migration_inputs_factory),
                    self.wrap_fixture_callback('labor', spies.reconstruct_migration_labor),
                    spies.firm_stage, self.wrap_fixture_callback('wage', spies.composite_household_wages))
                result = integration_callback(None, None, None, 8, b['states'], b['batch'],
                    b['frozen_shares'], expected_share_sha, ledger, (), annual_context=c, target_year=2018,
                    province_axis=c.province_axis, source_sha256=c.source_sha256, input_kind='synthetic',
                    price_basis=c.price_basis, price_verified=False, params=b['params'],
                    migration_wedge_destination_origin=b['distance'], spies=wrapped, prepared_array=b['prepared_array'],
                    province_mapping=b['province_mapping'], prepared_middle_stage=prepared_middle_stage,
                    fixed_c8_binding=b['fixed_c8_binding'], fixed_c8_external_source=b['fixed_c8_external_source'])
                self.guard_boundary('final')
            return result
        finally:
            if self.pipeline.state == 'new': self.pipeline.close()
            self._closed, self._b, self._baseline, self._refs = True, None, None, ()
    def close(self):
        try:
            self.pipeline.close()
        finally:
            self._closed, self._b, self._baseline, self._refs = True, None, None, ()
def prepare_synthetic_c8_session(**kwargs):
    return SyntheticC8Session(**kwargs)
