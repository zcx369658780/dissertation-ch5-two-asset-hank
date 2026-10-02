"""Inert annual binding; no scientific-package import or implicit calendar mapping."""
from dataclasses import dataclass, field
import math
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from types import MappingProxyType

PINS = MappingProxyType({
    'manifest': '4F28039F5192172E1A7524018DD6679BED1E5A1F4C837B8251B9596473C8C566',
    'attribution': 'E94C976FBD93262D98E776777E295EC9DDBA92B26E1D48A7E0D2496CC6C0E91B',
    'audit': '1D3DE27EBAE90EBE8D2F3CB42880BD2FBDB68CFA22BEBBE866479180380BC936',
    'gdp': '5129836B3781ECAE9FA21D7082193A22ACF5B1A40389605ABB0ACC30AD1127CB',
    'population': 'F837137765DDE99B56578E8404621218A4CA716FEF40BF8F16E75B8F8C79F0C3',
    'adapter': '0BEB77FA60C95227E79EFC32C497C2F28D9C2DEBADC09987A3512A96384A226D',
    'helper': '7B9A490F382E3007820E70C68D2EFB5992DE25BC8455EDE8B265CA33F384AF56',
})
PROVINCE_NAMES = ('北京市','天津市','河北省','山西省','内蒙古自治区','辽宁省',
    '吉林省','黑龙江省','上海市','江苏省','浙江省','安徽省','福建省','江西省',
    '山东省','河南省','湖北省','湖南省','广东省','广西壮族自治区','海南省',
    '重庆市','四川省','贵州省','云南省','西藏自治区','陕西省','甘肃省','青海省',
    '宁夏回族自治区','新疆维吾尔自治区')
CANONICAL_AXIS = tuple(enumerate(PROVINCE_NAMES, 1))
_OBSERVED_MANIFEST_IDENTIFIER = 'EVIDENCE/ch5_methodological_price_binding_20260930/source_binding_manifest.json'
_PREPARED = object()


class ProductionBlocked(ValueError):
    pass


def _digest(raw):
    if type(raw) is not bytes:
        raise ValueError('saved raw bytes required')
    return hashlib.sha256(raw).hexdigest().upper()


def _json(raw):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('duplicate JSON key')
            result[key] = value
        return result
    return json.loads(raw.decode('utf-8-sig'), object_pairs_hook=unique)


def _helper():
    path = Path(__file__).with_name('lagged_observed_gdp_wedge.py')
    if _digest(path.read_bytes()) != PINS['helper']:
        raise ValueError('accepted helper identity changed')
    # This exact helper has standard-library imports only; never import package init.
    name = '_annual_accepted_wedge_helper'
    if name in sys.modules:
        return sys.modules[name]  # code import cache only; never an annual/data cache
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _axis(axis):
    if type(axis) is not tuple or not axis:
        raise ValueError('explicit immutable index/source-name axis required')
    if any(type(row) is not tuple or len(row) != 2 or type(row[0]) is not int
           or row[0] < 1 or type(row[1]) is not str or not row[1] for row in axis):
        raise ValueError('invalid source axis')
    if len({r[0] for r in axis}) != len(axis) or len({r[1] for r in axis}) != len(axis):
        raise ValueError('duplicate source axis')
    return axis


@dataclass(frozen=True)
class _PreparationSeal:
    wedge: object
    metadata: tuple


@dataclass(frozen=True)
class AnnualContext:
    target_year: int
    observation_year: int
    province_axis: tuple
    source_sha256: str
    input_kind: str
    price_basis: str
    price_verified: bool
    provenance: tuple
    wedge: object
    phi_destination_origin: tuple
    model_activation: bool = False
    _preparation_token: object = field(default=None, repr=False, compare=False)
    _seal: object = field(default=None, init=False, repr=False, compare=False)

    def __post_init__(self):
        if self._preparation_token is not _PREPARED:
            raise ValueError('context must originate at explicit annual preparation')

    def validate(self, *, target_year, province_axis, source_sha256,
                 input_kind, price_basis, price_verified):
        if type(self) is not AnnualContext or type(target_year) is not int:
            raise ValueError('explicit annual context/year required')
        if self._preparation_token is not _PREPARED:
            raise ValueError('unprepared annual context')
        metadata = (self.target_year, self.observation_year, self.province_axis,
                    self.source_sha256, self.input_kind, self.price_basis,
                    self.price_verified, self.provenance, self.model_activation)
        if type(self._seal) is not _PreparationSeal or self._seal.wedge is not self.wedge or self._seal.metadata != metadata:
            raise ValueError('annual preparation seal mismatch')
        helper = sys.modules.get('_annual_accepted_wedge_helper')
        if helper is None or type(self.wedge) is not helper.AnnualLaborWedge:
            raise ValueError('accepted immutable wedge type required')
        coefficients = self.phi_destination_origin
        n = len(self.province_axis)
        if type(coefficients) is not tuple or len(coefficients) != n or any(
            type(row) is not tuple or len(row) != n or any(type(v) is not float for v in row)
            for row in coefficients):
            raise ValueError('strong immutable coefficient backing required')
        q = self.wedge.per_capita_gdp
        if type(q) is not tuple or len(q) != n or any(type(v) is not float or not math.isfinite(v) or v <= 0 for v in q):
            raise ValueError('immutable positive annual proxy required')
        if self.wedge.amplitude != .3 or any(not math.isfinite(v) or not .7 < v < 1.3
                                            for row in coefficients for v in row):
            raise ValueError('accepted finite amplitude bounds required')
        if any(coefficients[i][i] != 1. for i in range(n)) or any(
            (q[i] < q[j] and not coefficients[j][i] < 1.) or
            (q[i] > q[j] and not coefficients[j][i] > 1.) for j in range(n) for i in range(n)):
            raise ValueError('destination/origin coefficient direction invalid')
        if type(self.provenance) is not tuple or any(type(row) is not tuple for row in self.provenance):
            raise ValueError('immutable provenance required')
        if target_year != self.target_year or self.observation_year != target_year - 1:
            raise ValueError('annual snapshot year mismatch')
        if _axis(province_axis) != self.province_axis or source_sha256 != self.source_sha256:
            raise ValueError('annual source axis/identity mismatch')
        if (input_kind, price_basis, price_verified) != (self.input_kind, self.price_basis, self.price_verified):
            raise ValueError('annual provenance metadata mismatch')
        if type(price_verified) is not bool or self.model_activation is not False:
            raise ValueError('inactive metadata required')
        if self.phi_destination_origin is not self.wedge.coefficients:
            raise ValueError('authoritative coefficients must be reused')
        if self.wedge.target_year != target_year or self.wedge.province_order != tuple(i for i, _ in province_axis):
            raise ValueError('wedge identity mismatch')
        if self.wedge.observation_year != self.observation_year:
            raise ValueError('wedge observation calendar mismatch')
        binding = self.wedge.binding
        helper._binding_snapshot(binding)
        if self.input_kind == 'synthetic' and (binding.source_identifier != 'invented_fixture'
            or self.provenance != (('fixture_sha256', self.source_sha256),)):
            raise ValueError('immutable canonical fixture provenance required')
        if (binding.input_kind, binding.source_sha256, binding.price_basis,
            binding.price_verified) != (self.input_kind, self.source_sha256,
                                        self.price_basis, self.price_verified):
            raise ValueError('authoritative wedge provenance mismatch')


def prepare_synthetic_context(raw_fixture, *, expected_fixture_sha256, province_axis, target_year):
    """Invented fixtures only; fixture pins cannot authenticate observed inputs."""
    if _digest(raw_fixture) != expected_fixture_sha256:
        raise ValueError('fixture byte identity mismatch')
    d = _json(raw_fixture)
    axis = _axis(province_axis)
    if d.get('schema') != 'CH5_INVENTED_ANNUAL_FIXTURE_V1' or d.get('input_kind') != 'synthetic':
        raise ValueError('observed data cannot enter fixture API')
    if d.get('province_axis') != [list(r) for r in axis] or d.get('target_year') != target_year:
        raise ValueError('fixture axis/year mismatch')
    if type(target_year) is not int or d.get('observation_year') != target_year - 1:
        raise ValueError('explicit lagged fixture calendar required')
    if d.get('price_basis') != 'synthetic_fixture' or d.get('price_verified') is not False:
        raise ValueError('fixture price metadata required')
    helper = _helper()
    raw_records = d.get('records')
    if type(raw_records) is not list or any(type(row) is not list or len(row) != 4
                                           for row in raw_records):
        raise ValueError('explicit four-column fixture records required')
    names = dict(axis)
    if any(type(row[0]) is not int or row[0] not in names for row in raw_records):
        raise ValueError('fixture record index mismatch')
    records = _records_to_gdp_records(
        tuple((row[0], names[row[0]], *row[1:]) for row in raw_records),
        province_axis=axis, observation_year=target_year - 1)
    binding = helper.ProvenanceBinding('synthetic', 'invented_fixture', expected_fixture_sha256,
                                      'year_end_resident', 'synthetic_fixture', False)
    wedge = helper.build_annual_labor_wedge(records, target_year,
        province_order=tuple(i for i, _ in axis), binding=binding)
    result = AnnualContext(target_year, target_year - 1, axis, expected_fixture_sha256,
        'synthetic', 'synthetic_fixture', False, (('fixture_sha256', expected_fixture_sha256),),
        wedge, wedge.coefficients, _preparation_token=_PREPARED)
    metadata = (result.target_year, result.observation_year, result.province_axis,
                result.source_sha256, result.input_kind, result.price_basis,
                result.price_verified, result.provenance, result.model_activation)
    object.__setattr__(result, '_seal', _PreparationSeal(wedge, metadata))
    return result


def _records_to_gdp_records(raw_records, *, province_axis, observation_year):
    """Pure unit-preserving conversion, shared by fixtures and the dormant kernel.

    This function grants no observed authentication token or execution permission.
    It delegates all numerical wedge arithmetic to the accepted helper.
    """
    axis = _axis(province_axis)
    if type(observation_year) is not int or observation_year < 1:
        raise ValueError('explicit observation year required')
    if type(raw_records) is not tuple or len(raw_records) != len(axis):
        raise ValueError('complete immutable raw records required')
    expected = dict(axis)
    seen = set()
    helper = _helper()
    result = []
    for position, row in enumerate(raw_records):
        if type(row) is not tuple or len(row) != 5:
            raise ValueError('immutable five-column raw record required')
        index, name, year, gdp, population = row
        if type(index) is not int or index not in expected or index in seen:
            raise ValueError('raw record index mismatch')
        if type(name) is not str or name != expected[index]:
            raise ValueError('raw record source name mismatch')
        if (index, name) != axis[position]:
            raise ValueError('raw record order must match explicit source axis')
        if type(year) is not int or year != observation_year:
            raise ValueError('raw record observation year mismatch')
        # Validate raw amounts without unit conversion or replacement/rounding.
        if type(gdp) not in (int, float) or type(population) not in (int, float):
            raise ValueError('built-in numeric raw amounts excluding bool required')
        helper._positive_float(gdp)
        helper._positive_float(population)
        seen.add(index)
        result.append(helper.GDPRecord(index, year, gdp, population))
    return tuple(result)


@dataclass(frozen=True)
class _ObservedAuthenticationSeal:
    owner: object
    metadata: tuple


@dataclass(frozen=True)
class AuthenticatedObservedSnapshot:
    province_axis: tuple
    raw_records: tuple
    provenance: tuple
    target_year: int = 2018
    observation_year: int = 2017
    information_set: str = 'retrospective_revised'
    population_basis: str = 'year_end_resident'
    price_basis: str = 'current_price_methodologically_attributed'
    price_verified: bool = False
    official_release_date: None = None
    model_activation: bool = False
    _authentication_seal: object = field(default=None, init=False, repr=False, compare=False)


def _observed_snapshot_metadata(snapshot):
    return (snapshot.province_axis, snapshot.raw_records, snapshot.provenance,
            snapshot.target_year, snapshot.observation_year, snapshot.information_set,
            snapshot.population_basis, snapshot.price_basis, snapshot.price_verified,
            snapshot.official_release_date, snapshot.model_activation)


def _validate_observed_snapshot(snapshot):
    """Require the exact immutable object issued by the raw-pinned authenticator."""
    if type(snapshot) is not AuthenticatedObservedSnapshot:
        raise ValueError('authenticator-originated observed snapshot required')
    seal = snapshot._authentication_seal
    if (type(seal) is not _ObservedAuthenticationSeal or seal.owner is not snapshot
            or seal.metadata != _observed_snapshot_metadata(snapshot)):
        raise ValueError('observed authentication seal mismatch')
    if snapshot.province_axis != CANONICAL_AXIS or type(snapshot.raw_records) is not tuple:
        raise ValueError('immutable canonical observed axis/records required')
    if (type(snapshot.target_year) is not int or type(snapshot.observation_year) is not int
            or (snapshot.target_year, snapshot.observation_year, snapshot.information_set,
                snapshot.population_basis, snapshot.price_basis, snapshot.price_verified,
                snapshot.official_release_date, snapshot.model_activation) !=
            (2018, 2017, 'retrospective_revised', 'year_end_resident',
             'current_price_methodologically_attributed', False, None, False)
            or snapshot.price_verified is not False or snapshot.model_activation is not False):
        raise ValueError('accepted inactive observed metadata required')
    if type(snapshot.provenance) is not tuple or any(type(row) is not tuple for row in snapshot.provenance):
        raise ValueError('immutable observed provenance required')
    return snapshot


def authenticate_observed_binding(raw_sources, *, province_axis=CANONICAL_AXIS):
    """Future raw-byte boundary. Authenticate ALL pins before decode/conversion.

    No expected-pin override; this function is not called with real sources by this task.
    Numerical observed loading and matrix preparation remain explicitly blocked below.
    """
    if type(raw_sources) is not dict or set(raw_sources) != set(PINS):
        raise ValueError('complete accepted raw-source bundle required')
    for key, pin in PINS.items():
        if _digest(raw_sources[key]) != pin:
            raise ValueError('accepted raw source identity mismatch: ' + key)
    if _axis(province_axis) != CANONICAL_AXIS:
        raise ValueError('accepted observed index/source-name order required')
    manifest, attribution, audit = (_json(raw_sources[k]) for k in ('manifest', 'attribution', 'audit'))
    if (manifest.get('target_year'), manifest.get('observation_year'),
        manifest.get('information_set'), manifest.get('population_basis')) != (
        2018, 2017, 'retrospective_revised', 'year_end_resident'):
        raise ValueError('accepted calendar/source metadata mismatch')
    if manifest.get('price_attribution_sha256') != PINS['attribution']:
        raise ValueError('attribution not bound')
    if manifest.get('price_basis') != 'current_price_methodologically_attributed' or manifest.get('price_verified') is not False:
        raise ValueError('methodological attribution must remain unverified')
    if manifest.get('price_base_year') is not None or manifest.get('official_release_date') is not None:
        raise ValueError('unknown release/no base year required')
    if attribution.get('evidence_use_adopted') is not True or attribution.get('direct_price_verified') is not False:
        raise ValueError('adopted evidence category required')
    if audit.get('display_capture_times') != manifest.get('display_capture_times'):
        raise ValueError('capture provenance mismatch')
    expected_sources = [
        {'path': 'EVIDENCE/ch5_revised_data_table_20260930/data_audit.json', 'sha256': PINS['audit']},
        {'path': 'EVIDENCE/ch5_revised_data_table_20260930/nbs_gdp_display.json', 'sha256': PINS['gdp']},
        {'path': 'EVIDENCE/ch5_revised_data_table_20260930/nbs_population_display.json', 'sha256': PINS['population']},
    ]
    if manifest.get('sources') != expected_sources or audit.get('schema') != 'CH5_REVISED_DATA_CANDIDATE_V1':
        raise ValueError('accepted audit/display binding required')
    hashes = audit.get('display_hashes', {})
    if hashes.get('nbs_gdp_display.json') != PINS['gdp'] or hashes.get('nbs_population_display.json') != PINS['population']:
        raise ValueError('audit must bind both display sources')
    records = audit.get('records')
    if type(records) is not list or len(records) != 124:
        raise ValueError('complete authenticated audit records required')
    selected, seen = {}, set()
    for row in records:
        if type(row) is not dict or row.get('province') not in PROVINCE_NAMES or type(row.get('year')) is not int:
            raise ValueError('authenticated record source axis invalid')
        key = (row['province'], row['year'])
        if key in seen or row['year'] not in range(2015, 2019):
            raise ValueError('audit coverage invalid')
        seen.add(key)
        if row['year'] == 2017:
            selected[row['province']] = (row['new_gdp'], row['new_population'])
    if seen != {(name, year) for name in PROVINCE_NAMES for year in range(2015, 2019)}:
        raise ValueError('audit coverage incomplete')
    capture_times = manifest.get('display_capture_times')
    if type(capture_times) is not dict or any(type(key) is not str or type(value) is not str
                                            for key, value in capture_times.items()):
        raise ValueError('immutable string capture provenance required')
    raw_records = tuple((i, name, 2017, *selected[name]) for i, name in CANONICAL_AXIS)
    for _, _, _, gdp, population in raw_records:
        for amount in (gdp, population):
            if type(amount) not in (int, float):
                raise ValueError('observed amount must exclude bool and mutable values')
            try:
                valid = math.isfinite(amount) and amount > 0
            except OverflowError as exc:
                raise ValueError('observed amount is unrepresentable') from exc
            if not valid:
                raise ValueError('finite positive observed amount required')
    provenance = (('manifest_sha256', PINS['manifest']), ('audit_sha256', PINS['audit']),
            ('gdp_sha256', PINS['gdp']), ('population_sha256', PINS['population']),
            ('attribution_sha256', PINS['attribution']),
            ('information_set', 'retrospective_revised'),
            ('population_basis', 'year_end_resident'),
            ('per_person_proxy', 'year_end_population_proxy_not_official_per_capita_gdp'),
            ('price_basis', 'current_price_methodologically_attributed'),
            ('price_verified', False),
            ('official_release_date', None),
            ('price_base_year', None),
            ('target_year', 2018),
            ('observation_year', 2017),
            ('capture_times', tuple(sorted(capture_times.items()))))
    # Values stay raw and are derived only from the authenticated audit, never caller records.
    snapshot = AuthenticatedObservedSnapshot(CANONICAL_AXIS, raw_records, provenance)
    object.__setattr__(snapshot, '_authentication_seal',
                       _ObservedAuthenticationSeal(snapshot, _observed_snapshot_metadata(snapshot)))
    return snapshot


def _prepare_authenticated_observed_context(snapshot):
    """Dormant implementation only: real-data conversion execution is NOT authorized.

    The public preparation entry below never calls this kernel. Invented fixtures
    may exercise the pure record converter, but cannot issue this seal.
    """
    snapshot = _validate_observed_snapshot(snapshot)  # reject before loading helper
    records = _records_to_gdp_records(snapshot.raw_records,
        province_axis=snapshot.province_axis, observation_year=snapshot.observation_year)
    helper = _helper()
    binding = helper.ProvenanceBinding('observed', _OBSERVED_MANIFEST_IDENTIFIER,
        PINS['manifest'], snapshot.population_basis, snapshot.price_basis,
        snapshot.price_verified, price_base_year=None,
        price_attribution_sha256=PINS['attribution'])
    wedge = helper.build_annual_labor_wedge(records, snapshot.target_year,
        province_order=tuple(i for i, _ in snapshot.province_axis), binding=binding)
    result = AnnualContext(snapshot.target_year, snapshot.observation_year,
        snapshot.province_axis, PINS['manifest'], 'observed', snapshot.price_basis,
        snapshot.price_verified, snapshot.provenance, wedge, wedge.coefficients,
        _preparation_token=_PREPARED)
    metadata = (result.target_year, result.observation_year, result.province_axis,
                result.source_sha256, result.input_kind, result.price_basis,
                result.price_verified, result.provenance, result.model_activation)
    object.__setattr__(result, '_seal', _PreparationSeal(wedge, metadata))
    return result


def prepare_observed_context(raw_sources, **_):
    authenticate_observed_binding(raw_sources)
    raise ProductionBlocked('observed numerical loading/matrix preparation requires separate authority')


def _preload_data_only_helper(raw_helper):
    """Load only exact pin-validated helper bytes, without a source loader/cache."""
    if _digest(raw_helper) != PINS['helper']:
        raise ValueError('accepted helper identity changed')
    from types import ModuleType
    name = '_annual_accepted_wedge_helper'
    helper_path = str(Path(__file__).with_name('lagged_observed_gdp_wedge.py'))
    code = compile(raw_helper, helper_path, 'exec')
    module = ModuleType(name)
    module.__file__ = helper_path
    module.__package__ = ''
    sys.modules[name] = module
    try:
        exec(code, module.__dict__)
    except BaseException:
        if sys.modules.get(name) is module:
            del sys.modules[name]
        raise
    return module


def prepare_observed_data_only_context(raw_sources, *, data_only, progress):
    """Explicit inactive data-only preparation from the unchanged raw-byte pins.

    The caller owns an exact built-in string list, never an injected callback.
    Attempt events are retained if authentication or the sealed kernel raises.
    This entry grants no scientific-consumer or filesystem-write authority.
    """
    if data_only is not True:
        raise ProductionBlocked('explicit data-only preparation required')
    if type(progress) is not list or any(type(event) is not str for event in progress):
        raise ValueError('exact mutable string progress list required')
    owned_events = (
        'data_only.authentication_attempted',
        'data_only.authentication_completed',
        'data_only.helper_code_binding_attempted',
        'data_only.helper_code_binding_completed',
        'data_only.annual_conversion_attempted',
        'data_only.annual_conversion_completed',
        'data_only.accepted_helper_completed',
        'data_only.annual_master_completed',
    )
    if any(event in owned_events for event in progress):
        raise ValueError('data-only preparation already attempted in this progress list')
    progress.append('data_only.authentication_attempted')
    snapshot = authenticate_observed_binding(raw_sources)
    progress.append('data_only.authentication_completed')
    progress.append('data_only.helper_code_binding_attempted')
    _preload_data_only_helper(raw_sources['helper'])
    progress.append('data_only.helper_code_binding_completed')
    progress.append('data_only.annual_conversion_attempted')
    result = _prepare_authenticated_observed_context(snapshot)
    progress.append('data_only.annual_conversion_completed')
    progress.append('data_only.accepted_helper_completed')
    progress.append('data_only.annual_master_completed')
    return result
