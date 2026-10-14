"""Single-use synthetic joint preflight; no imports of model packages or files.

Explicit exact engineering modules are supplied by a reviewed caller. Module
path checks below restrict accidental mixing, not hostile same-privilege code.
"""
from dataclasses import dataclass, field
import hashlib
import math
from pathlib import Path
import struct
import sys


def exact_module(obj, symbol, relative):
    module = sys.modules.get(type(obj).__module__)
    root = Path(__file__).resolve().parents[3]
    if (module is None or getattr(module, symbol, None) is not type(obj)
            or Path(getattr(module, '__file__', '')).resolve() != root / relative):
        raise ValueError('exact isolated engineering module required: ' + symbol)
    return module


def snapshot(states, shares, batch, params, distance, contract_module):
    n = 31
    if type(states) is not tuple or len(states) != n:
        raise ValueError('31 immutable state references required')
    rows = []
    for state in states:
        if type(state) is not dict:
            raise ValueError('original state dictionaries required')
        # Original source states are scalar records; reject hidden mutable payloads.
        row = []
        for key, value in state.items():
            if type(key) is not str:
                raise ValueError('string state keys required')
            if type(value) is str:
                row.append((key, value))
            else:
                row.append((key, struct.pack('<d', contract_module.scalar(value))))
        rows.append(tuple(sorted(row)))
    def matrix(value, name):
        if getattr(value, 'ndim', 2) != 2 or len(value) != n:
            raise ValueError(name + ' must have 31 destination rows')
        result = []
        for row in value:
            if len(row) != n:
                raise ValueError(name + ' must have 31 origin columns')
            cells = []
            for v in row:
                # numpy float64 is admitted here only after excluding boolean kinds.
                if isinstance(v, bool) or getattr(getattr(v, 'dtype', None), 'kind', '') == 'b':
                    raise ValueError('boolean matrix entry')
                if not isinstance(v, (int, float)) or not math.isfinite(v):
                    raise ValueError('finite real matrix entry required')
                cells.append(float(v))
            result.append(tuple(cells))
        return tuple(result)
    s = matrix(shares, 'S')
    d = matrix(distance, 'migration wedge')
    if any(v < 0 for row in s for v in row):
        raise ValueError('negative frozen S')
    for i in range(n):
        if abs(math.fsum(s[j][i] for j in range(n)) - 1.) > 1e-12:
            raise ValueError('frozen S origin-column conservation')
        if s[i][i] != 1. - states[i]['inter_prv_ratio']:
            raise ValueError('frozen S home diagonal')
    if type(params) is not dict:
        raise ValueError('explicit original parameter dictionary required')
    if (not {'ga', 'phi_l', 'alphal', 'epsilon', 'theta', 'delta'} <= set(params)
            or any(contract_module.scalar(params[k]) <= 0 for k in ('ga', 'phi_l', 'alphal'))
            or contract_module.scalar(params['epsilon']) == 0):
        raise ValueError('complete unchanged valid synthetic parameter roles required')
    p = tuple(sorted((k, struct.pack('<d', contract_module.scalar(v))) for k, v in params.items()))
    vectors = contract_module.five_vectors(batch, n)
    encoded = tuple(tuple(struct.pack('<d', v) for v in row) for row in vectors)
    # Preserve sign bits as well as values, including zero-valued frozen entries.
    bits = tuple(b''.join(struct.pack('<d', v) for row in m for v in row) for m in (s, d))
    return tuple(rows), s, encoded, p, d, bits


@dataclass
class JointPreparation:
    contract: object
    binding: object
    annual_context: object
    prepared_array: object
    params: dict
    distance: object
    _snapshot: tuple = field(repr=False)
    _modules: tuple = field(repr=False)
    _binding_signature: tuple = field(repr=False)
    _phase: str = field(default='READY', init=False)
    attempted: int = field(default=0, init=False)
    completed: int = field(default=0, init=False)
    failed: int = field(default=0, init=False)

    def _check(self, *, states, batch, frozen_shares, annual_context, prepared_array,
               params, distance, fixed_c8_binding, external_source, turn):
        contract_module, archive, binding_module, adapter = self._modules
        if (annual_context is not self.annual_context or prepared_array is not self.prepared_array
                or params is not self.params or distance is not self.distance
                or fixed_c8_binding is not self.binding or type(turn) is not int or turn != 8):
            raise ValueError('joint preparation reference/calendar mismatch')
        self.contract.validate(archive_module=archive, binding_module=binding_module,
                               mapping=self.binding.province_mapping)
        if tuple(getattr(self.binding, name) for name in
                 ('state_declaration', 'share_declaration', 'household_declaration',
                  'province_mapping', 'external_mapping')) != self._binding_signature:
            raise ValueError('joint binding changed')
        adapter.AnnualArrayCarrier.validate(prepared_array, annual_context=annual_context,
            target_year=2018, province_axis=annual_context.province_axis,
            source_sha256=annual_context.source_sha256, input_kind='synthetic',
            price_basis='synthetic_fixture', price_verified=False,
            province_mapping=prepared_array.province_mapping)
        if annual_context.observation_year != 2017:
            raise ValueError('joint observation year mismatch')
        if (tuple((d.province_index, d.province) for d in batch.diagnostics)
                != self.contract.archive_declaration.province_axis
                or tuple(d.checkpoint for d in batch.diagnostics) != self.contract.terminal_checkpoints
                or any(getattr(batch, name, None) is not False for name in
                       ('source_authenticated', 'original_live_identity_restored',
                        'scientific_validity_established', 'model_activation'))):
            raise ValueError('terminal checkpoint/identity/evidence conflict')
        binding_module.FixedC8InputBinding.validate(self.binding, states=states,
            frozen_shares=frozen_shares, batch=batch, turn=turn,
            province_axis=annual_context.province_axis,
            province_mapping=prepared_array.province_mapping, input_kind='synthetic',
            external_source=external_source,
            source_identifier=annual_context.wedge.binding.source_identifier,
            source_sha256=annual_context.source_sha256)
        if (batch.declaration != self.contract.archive_declaration
                or snapshot(states, frozen_shares, batch, params, distance, contract_module) != self._snapshot):
            raise ValueError('original synthetic input content/lifetime changed')

    def begin(self, **kwargs):
        if self._phase != 'READY':
            raise ValueError('joint preparation expired or already attempted')
        self.attempted += 1
        try:
            self._check(**kwargs)
        except BaseException:
            self.failed += 1
            self._phase = 'CLOSED'
            raise
        self._phase = 'ATTEMPTED'

    def recheck(self, **kwargs):
        if self._phase != 'ATTEMPTED':
            raise ValueError('joint preparation not in active attempt')
        self._check(**kwargs)

    def close(self):
        if self._phase == 'ATTEMPTED' and self.completed == 0:
            self.failed += 1
        self._phase = 'CLOSED'

    def complete(self, **kwargs):
        self.recheck(**kwargs)
        self.completed += 1


def prepare_joint(*, contract, binding, annual_context, prepared_array, params,
                  distance, expected_share_sha):
    """No source read, numerical reconstruction or real consumer authorization."""
    cm = exact_module(contract, 'FixedC8SourceContract',
        'src/ch5_two_asset_hank/multi_province/fixed_c8_source_contract.py')
    bm = exact_module(binding, 'FixedC8InputBinding',
        'validators/multi_province/annual_observed_labor_diagnostic/fixed_c8_input_binding.py')
    am = exact_module(binding.batch, 'ArchiveDerivedAggregateCarrier',
        'validators/multi_province/annual_observed_labor_diagnostic/archive_aggregate_adapter.py')
    adapter = exact_module(prepared_array, 'AnnualArrayCarrier',
        'src/ch5_two_asset_hank/corrected_diagnostic/annual_labor_array_adapter.py')
    if annual_context.input_kind != 'synthetic':
        raise ValueError('real/observed preparation blocked')
    if (binding.state_declaration is not contract.state_declaration
            or binding.share_declaration is not contract.share_declaration
            or binding.household_declaration is not contract.household_declaration):
        raise ValueError('joint contract must reuse all three original declarations')
    content = snapshot(binding.states, binding.frozen_shares, binding.batch, params, distance, cm)
    encoded = b''.join(struct.pack('<d', content[1][j][i]) for i in range(31) for j in range(31))
    if expected_share_sha != hashlib.sha256(encoded).hexdigest().upper():
        raise ValueError('S little-endian F-order field hash mismatch')
    signature = tuple(getattr(binding, name) for name in
        ('state_declaration', 'share_declaration', 'household_declaration', 'province_mapping', 'external_mapping'))
    result = JointPreparation(contract, binding, annual_context, prepared_array, params,
                              distance, content, (cm, am, bm, adapter), signature)
    result._check(states=binding.states, batch=binding.batch, frozen_shares=binding.frozen_shares,
        annual_context=annual_context, prepared_array=prepared_array, params=params,
        distance=distance, fixed_c8_binding=binding, external_source=contract.state_declaration.external_source, turn=8)
    return result
