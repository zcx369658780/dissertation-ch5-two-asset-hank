"""Explicit synthetic middle bridge; no production imports or runtime authority."""
from dataclasses import dataclass, field
import hashlib
import math
from numbers import Real
from pathlib import Path
import re
import sys

import numpy as np


CONSERVATION_TOLERANCE = 1e-12
LEDGER_KEYS = ('source_faithful_labor_reconstructions',
    'frozen_k1b_quantity_allocations', 'k1b_feedback_calls',
    'c1_residual_govinv_constructions', 'firm_evaluations', 'composite_wage_batches')
FIRM_FIELDS = ('Kt', 'Lt', 'Yt', 'mt', 'KNratio', 'wt0', 'wjt', 'rk', 'Thetat',
               'It', 'PIt', 'Corptax', 'ra0', 'ra', 'Govinc')
STATE_FIELDS = ('N', 'wjt', 'tau', 'inter_prv_ratio', 'Kt0', 'alpha', 'Zt',
    'pit', 'Kt_prev', 'Zt_1', 'pit_1', 'rk', 'corptau', 'Tt',
    'ramin', 'ramax', 'wjtmin', 'wjtmax')
PARAM_FIELDS = ('ga', 'phi_l', 'alphal', 'epsilon', 'theta', 'delta')
_PREPARED = object()


def _scalar(value):
    try:
        valid = not isinstance(value, (bool, np.bool_)) and isinstance(value, Real) and math.isfinite(value)
    except (OverflowError, TypeError, ValueError):
        valid = False
    if not valid:
        raise ValueError('finite non-boolean numeric scalar required')
    return value


def _vector(values, n):
    if getattr(values, 'ndim', 1) != 1:
        raise ValueError('one-dimensional vector required')
    try:
        if len(values) != n:
            raise ValueError('vector axis mismatch')
        return tuple(_scalar(value) for value in values)
    except TypeError:
        raise ValueError('explicit scalar vector required') from None


def _shares(values, n):
    if getattr(values, 'ndim', 2) != 2:
        raise ValueError('destination-origin shares must be two-dimensional')
    try:
        if len(values) != n or any(len(row) != n for row in values):
            raise ValueError('shares axis mismatch')
        for row in values:
            for value in row:
                _scalar(value)
    except TypeError:
        raise ValueError('explicit scalar share matrix required') from None
    return np.asarray(values, dtype=np.float64)


def _field_sha256(values):
    encoded = np.asarray(values, dtype='<f8').tobytes(order='F')
    return hashlib.sha256(encoded).hexdigest().upper()


def _ledger(ledger):
    if (type(ledger) is not dict or type(ledger.get('engineering_fixture_label')) is not str
            or not ledger['engineering_fixture_label'].strip()):
        raise ValueError('explicitly labelled invented engineering ledger required')
    if any(type(ledger.get(key)) is not int or ledger[key] < 0 for key in LEDGER_KEYS):
        raise ValueError('existing nonnegative built-in attempted counters required')
    return ledger


@dataclass(frozen=True)
class FixtureDependencies:
    c1_residual: object
    evaluate_firm: object
    fixture_label: str


@dataclass(frozen=True)
class CapitalResult:
    wealth: tuple
    flows: tuple
    private: tuple
    domestic: tuple
    capital_residual: float
    no_same_turn_share_recomputation: bool = True


@dataclass(frozen=True)
class C1Result:
    province_order: tuple
    GovInv_residual_MU: tuple
    firm_K_accounting_MU: tuple
    capital_unit: str = 'MU_10WAN_YUAN'


@dataclass(frozen=True)
class FirmResult:
    Kt: float
    Lt: float
    Yt: float
    mt: float
    KNratio: float
    wt0: float
    wjt: float
    rk: float
    Thetat: float
    It: float
    PIt: float
    Corptax: float
    ra0: float
    ra: float
    Govinc: float


@dataclass(frozen=True)
class MiddleStageResult:
    firms: tuple
    capital: CapitalResult
    c1: C1Result
    model_activation: bool = False
    full_outer_runtime_integrated: bool = False


@dataclass(frozen=True)
class _MiddleSeal:
    owner: object
    annual_context: object
    prepared_array: object
    array_seal: object
    province_mapping: tuple
    ledger: dict
    ledger_label: str
    dependencies: FixtureDependencies
    callbacks: tuple


@dataclass(frozen=True)
class PreparedMiddleStage:
    annual_context: object
    prepared_array: object
    province_mapping: tuple
    ledger: dict
    dependencies: FixtureDependencies
    _preparation_token: object = field(default=None, repr=False, compare=False)
    _seal: object = field(default=None, init=False, repr=False, compare=False)

    def __post_init__(self):
        if self._preparation_token is not _PREPARED:
            raise ValueError('explicit fixture middle preparation required')

    def _validate(self, *, annual_context, prepared_array, province_mapping, ledger):
        seal = self._seal
        if (type(self) is not PreparedMiddleStage or type(seal) is not _MiddleSeal
                or seal.owner is not self or self._preparation_token is not _PREPARED
                or self.annual_context is not annual_context or seal.annual_context is not annual_context
                or self.prepared_array is not prepared_array or seal.prepared_array is not prepared_array
                or seal.array_seal is not prepared_array._seal
                or self.province_mapping != province_mapping or seal.province_mapping != province_mapping
                or self.ledger is not ledger or seal.ledger is not ledger
                or self.dependencies is not seal.dependencies
                or self.dependencies.c1_residual is not seal.callbacks[0]
                or self.dependencies.evaluate_firm is not seal.callbacks[1]
                or self.dependencies.fixture_label != seal.callbacks[2]):
            raise ValueError('middle preparation seal mismatch')
        _ledger(ledger)
        if ledger['engineering_fixture_label'] != seal.ledger_label:
            raise ValueError('fixture ledger label changed')
        _validate_carrier(annual_context, prepared_array, province_mapping)

    def validate_pre_spy(self, inputs, frozen_shares, expected_share_sha, *,
                         annual_context, prepared_array, province_mapping, ledger):
        self._validate(annual_context=annual_context, prepared_array=prepared_array,
                       province_mapping=province_mapping, ledger=ledger)
        _validate_inputs(inputs, prepared_array, province_mapping)
        shares = _shares(frozen_shares, len(province_mapping))
        if (type(expected_share_sha) is not str or re.fullmatch(r'[0-9A-F]{64}', expected_share_sha) is None
                or _field_sha256(shares) != expected_share_sha):
            raise ValueError('frozen share byte identity mismatch')

    def run(self, inputs, migration, frozen_shares, expected_share_sha):
        self.validate_pre_spy(inputs, frozen_shares, expected_share_sha,
            annual_context=self.annual_context, prepared_array=self.prepared_array,
            province_mapping=self.province_mapping, ledger=self.ledger)
        n = len(self.province_mapping)
        try:
            labor = _vector(migration.lt_supply, n)
        except AttributeError:
            raise ValueError('destination migration labor output required') from None
        if any(value <= 0 for value in labor):
            raise ValueError('positive destination firm labor required')
        self.ledger['frozen_k1b_quantity_allocations'] += 1
        self.ledger['k1b_feedback_calls'] += 1
        shares = _shares(frozen_shares, n)
        provinces, household = inputs.old_provinces, inputs.household_outputs
        population = np.asarray([row['N'] for row in provinces], dtype=np.float64)
        theta = np.asarray([row['inter_prv_ratio'] for row in provinces], dtype=np.float64)
        wealth = np.asarray(household.at, dtype=np.float64) * population
        flows = shares * wealth[None, :]
        private = np.sum(flows, axis=1)
        domestic = np.diag(flows).copy()
        if not all(np.all(np.isfinite(value)) for value in (wealth, flows, private, domestic)):
            raise ValueError('nonfinite frozen capital arithmetic')
        scale = max(1.0, float(np.sum(wealth)))
        if not np.allclose(np.sum(shares, axis=0), 1.0, rtol=0.0, atol=CONSERVATION_TOLERANCE):
            raise ValueError('frozen share columns do not conserve capital')
        if not np.allclose(np.sum(flows, axis=0), wealth, rtol=0.0,
                           atol=CONSERVATION_TOLERANCE * scale):
            raise ValueError('origin capital conservation failure')
        residual = float(np.sum(private) - np.sum(wealth))
        if not math.isfinite(residual) or abs(residual) > CONSERVATION_TOLERANCE * scale:
            raise ValueError('national capital conservation failure')
        if not np.array_equal(domestic, (1.0 - theta) * wealth):
            raise ValueError('home-retained diagonal mismatch')
        if np.any(private < 0):
            raise ValueError('negative destination private capital')
        targets = np.asarray([row['Kt0'] for row in provinces], dtype=np.float64)
        # Preserve pre-call authority independently of callback-visible arrays.
        target_authority = tuple(float(value) for value in targets)
        private_authority = tuple(float(value) for value in private)
        self.ledger['c1_residual_govinv_constructions'] += 1
        accounting = self.dependencies.c1_residual(Ktarget_MU=targets,
            Kprivate_current_MU=private, province_order=inputs.province_order)
        if (targets.shape != (n,) or private.shape != (n,)
                or not np.array_equal(targets, target_authority)
                or not np.array_equal(private, private_authority)):
            raise ValueError('C1 callback mutated frozen capital inputs')
        try:
            if tuple(accounting.province_order) != inputs.province_order:
                raise ValueError('C1 province order mismatch')
            gov = np.asarray(_vector(accounting.GovInv_residual_MU, n), dtype=np.float64)
            firm_capital = np.asarray(_vector(accounting.firm_K_accounting_MU, n), dtype=np.float64)
        except (AttributeError, TypeError):
            raise ValueError('complete ordered C1 fixture outputs required') from None
        expected_targets = np.asarray(target_authority, dtype=np.float64)
        expected_private = np.asarray(private_authority, dtype=np.float64)
        if (not np.array_equal(gov, np.maximum(expected_targets - expected_private, 0.0)) or np.any(gov < 0)
                or not np.array_equal(firm_capital, np.maximum(expected_targets, expected_private))):
            raise ValueError('C1 residual/accounting mismatch')
        if self.ledger['c1_residual_govinv_constructions'] != 1:
            raise ValueError('C1 construction must occur exactly once in this turn ledger')
        c1 = C1Result(inputs.province_order, tuple(gov), tuple(firm_capital))
        firms = []
        for index, province in enumerate(provinces):
            source = dict(province)
            source.update(GovInv=float(gov[index]), AtTax=float(household.at_tax[index]),
                          Lt_prev=float(household.household_lt[index]))
            self.ledger['firm_evaluations'] += 1
            raw = self.dependencies.evaluate_firm(source, private_authority[index],
                                                  float(labor[index]), inputs.params)
            try:
                values = tuple(_scalar(getattr(raw, name)) for name in FIRM_FIELDS)
            except AttributeError:
                raise ValueError('complete finite firm output required') from None
            if hasattr(raw, 'as_source_dict'):
                for value in raw.as_source_dict().values():
                    _scalar(value)
            firm = FirmResult(*values)
            expected = firm_capital[index]
            if abs(firm.Kt - expected) > 1e-12 * max(1.0, abs(expected)):
                raise ValueError('firm capital accounting mismatch')
            firms.append(firm)
        capital = CapitalResult(tuple(wealth), tuple(tuple(row) for row in flows),
                                private_authority, tuple(domestic), residual)
        return MiddleStageResult(tuple(firms), capital, c1)


def _validate_carrier(context, carrier, mapping):
    module = sys.modules.get(type(carrier).__module__)
    expected = Path(__file__).resolve().parents[3] / 'src/ch5_two_asset_hank/corrected_diagnostic/annual_labor_array_adapter.py'
    if (module is None or getattr(module, 'AnnualArrayCarrier', None) is not type(carrier)
            or Path(getattr(module, '__file__', '')).resolve() != expected):
        raise ValueError('exact annual array carrier required')
    try:
        if context.input_kind != 'synthetic':
            raise ValueError('production/observed middle execution blocked')
        module.AnnualArrayCarrier.validate(carrier, annual_context=context,
            target_year=context.target_year, province_axis=context.province_axis,
            source_sha256=context.source_sha256, input_kind=context.input_kind,
            price_basis=context.price_basis, price_verified=context.price_verified,
            province_mapping=mapping)
    except AttributeError:
        raise ValueError('exact prepared context metadata required') from None


def _validate_inputs(inputs, carrier, mapping):
    module = sys.modules.get(type(inputs).__module__)
    expected = Path(__file__).with_name('integration.py').resolve()
    if (module is None or getattr(module, 'OneTurnInputs', None) is not type(inputs)
            or Path(getattr(module, '__file__', '')).resolve() != expected):
        raise ValueError('exact inert input carrier required')
    n = len(mapping)
    if inputs.province_order != carrier.province_order or inputs.phi_destination_origin is not carrier.phi_destination_origin:
        raise ValueError('prepared model order/master identity mismatch')
    if type(inputs.old_provinces) is not tuple or len(inputs.old_provinces) != n:
        raise ValueError('ordered source records required')
    for row, (index, full, short) in zip(inputs.old_provinces, mapping):
        if (type(row.get('province_index')) is not int or row.get('province_index') != index
                or type(row.get('source_province_name')) is not str or row.get('source_province_name') != full
                or type(row.get('name')) is not str or row.get('name') != short):
            raise ValueError('middle state index/source/model axis mismatch')
        if not set(STATE_FIELDS) <= set(row):
            raise ValueError('complete source firm/labor/capital fields required')
        for name in STATE_FIELDS:
            _scalar(row[name])
        if row['N'] <= 0 or row['Kt0'] <= 0 or not 0 < row['alpha'] < 1 or row['Zt'] <= 0:
            raise ValueError('source firm/capital scalar constraints violated')
        if row['ramin'] > row['ramax'] or row['wjtmin'] > row['wjtmax']:
            raise ValueError('source clipping bounds inverted')
    if not set(PARAM_FIELDS) <= set(inputs.params):
        raise ValueError('complete unchanged source parameters required')
    for name in PARAM_FIELDS:
        _scalar(inputs.params[name])
    if inputs.params['epsilon'] == 0:
        raise ValueError('source epsilon must be nonzero')
    household = inputs.household_outputs
    for name in ('ct', 'at', 'at_tax', 'household_lt'):
        try:
            values = _vector(getattr(household, name), n)
        except AttributeError:
            raise ValueError('complete pre-frozen household vectors required') from None
        if name == 'at' and any(value < 0 for value in values):
            raise ValueError('nonnegative illiquid household wealth required')
        if name == 'ct' and any(value <= 0 for value in values):
            raise ValueError('positive pre-frozen consumption required')
        if name == 'household_lt' and any(value < 0 for value in values):
            raise ValueError('nonnegative pre-frozen household labor required')
    _shares(inputs.migration_wedge_destination_origin, n)


def prepare_middle_stage(*, annual_context, prepared_array, province_mapping, ledger, dependencies):
    """Explicit invented dependencies/ledger only; never wires real consumers."""
    _ledger(ledger)
    if (type(dependencies) is not FixtureDependencies or type(dependencies.fixture_label) is not str
            or not dependencies.fixture_label.strip() or not callable(dependencies.c1_residual)
            or not callable(dependencies.evaluate_firm)):
        raise ValueError('explicit labelled fixture dependencies required')
    _validate_carrier(annual_context, prepared_array, province_mapping)
    result = PreparedMiddleStage(annual_context, prepared_array, province_mapping,
        ledger, dependencies, _preparation_token=_PREPARED)
    object.__setattr__(result, '_seal', _MiddleSeal(result, annual_context, prepared_array,
        prepared_array._seal, province_mapping, ledger, ledger['engineering_fixture_label'],
        dependencies, (dependencies.c1_residual, dependencies.evaluate_firm, dependencies.fixture_label)))
    return result
