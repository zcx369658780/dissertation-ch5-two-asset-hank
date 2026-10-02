"""Inactive retrospective data reader. No model/helper imports or matrices."""
from dataclasses import dataclass
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
import re

PROVINCE_NAMES = ('北京市','天津市','河北省','山西省','内蒙古自治区','辽宁省',
 '吉林省','黑龙江省','上海市','江苏省','浙江省','安徽省','福建省','江西省',
 '山东省','河南省','湖北省','湖南省','广东省','广西壮族自治区','海南省',
 '重庆市','四川省','贵州省','云南省','西藏自治区','陕西省','甘肃省','青海省',
 '宁夏回族自治区','新疆维吾尔自治区')
CANONICAL_AXIS = tuple(enumerate(PROVINCE_NAMES, start=1))

@dataclass(frozen=True)
class Observation:
    province_index: int
    source_province_name: str
    observation_year: int
    gdp_raw_100m_yuan: float
    population_raw_10k_persons: float

@dataclass(frozen=True)
class InactiveSnapshot:
    target_year: int
    observation_year: int
    province_order: tuple
    records: tuple[Observation, ...]
    audit_sha256: str
    display_hashes: tuple
    capture_times: tuple
    information_set: str = 'retrospective_revised'
    population_basis: str = 'year_end_resident'
    price_basis: str = 'current_price_supported_exact_binding_pending'
    release_date: None = None
    price_verified: bool = False
    model_activation: bool = False

def _hash(value):
    if type(value) is not str or re.fullmatch(r'[0-9A-Fa-f]{64}', value) is None:
        raise ValueError('invalid SHA256')
    return value.upper()

def _number(value):
    if type(value) not in (int, float):
        raise ValueError('numeric value required; bool excluded')
    try:
        v = float(value)
    except (ValueError, OverflowError) as exc:
        raise ValueError('unrepresentable value') from exc
    if not math.isfinite(v) or v <= 0:
        raise ValueError('positive finite value required')
    return v

def _unique_object(pairs):
    d = {}
    for k, v in pairs:
        if k in d:
            raise ValueError('duplicate JSON key')
        d[k] = v
    return d

def load_inactive_snapshot(audit_path, expected_sha256, *, target_year, province_order):
    """Read a pinned 31-province audit; never mark observed price verified."""
    if type(target_year) is not int or target_year != 2018:
        raise ValueError('this bounded candidate supports target_year=2018 only')
    order = tuple(province_order)
    if len(order) != 31 or any(type(p) is not tuple or len(p) != 2 or
        type(p[0]) is not int or type(p[1]) is not str for p in order):
        raise ValueError('explicit 31-province index/name axis required')
    if set(order) != set(CANONICAL_AXIS):
        raise ValueError('province identifier/name mismatch, duplicate or missing axis')
    expected = _hash(expected_sha256)
    raw = Path(audit_path).read_bytes()
    actual = hashlib.sha256(raw).hexdigest().upper()
    if actual != expected:
        raise ValueError('audit source identity mismatch')
    d = json.loads(raw.decode('utf-8-sig'), object_pairs_hook=_unique_object)
    if d.get('schema') != 'CH5_REVISED_DATA_CANDIDATE_V1':
        raise ValueError('unsupported source schema')
    for k in ('science_calls', 'model_imports', 'wedge_matrices'):
        if type(d.get(k)) is not int or d[k] != 0:
            raise ValueError('source must remain zero-science evidence')
    if d.get('model_activation') is not False or d.get('results_eligibility') is not False:
        raise ValueError('source must remain inactive')
    hashes = d.get('display_hashes', {})
    required = ('nbs_gdp_dom.txt','nbs_gdp_display.json',
                'nbs_population_dom.txt','nbs_population_display.json')
    if type(hashes) is not dict or set(hashes) != set(required):
        raise ValueError('complete source display identities required')
    frozen_hashes = tuple((k, _hash(hashes[k])) for k in required)
    times = d.get('display_capture_times', {})
    if type(times) is not dict or set(times) != {'gdp','population'}:
        raise ValueError('capture dates required')
    for s in times.values():
        if type(s) is not str or datetime.fromisoformat(s.replace('Z','+00:00')).tzinfo is None:
            raise ValueError('timezone-aware capture date required')
    records = d.get('records')
    if type(records) is not list or len(records) != 124:
        raise ValueError('full 31 x 4 source records required')
    selected = {}
    seen = set()
    for r in records:
        if type(r) is not dict or type(r.get('province')) is not str:
            raise ValueError('invalid source record')
        name, year = r['province'], r.get('year')
        if name not in PROVINCE_NAMES or type(year) is not int or year not in range(2015,2019):
            raise ValueError('unexpected province/year')
        key = (name, year)
        if key in seen:
            raise ValueError('duplicate province/year')
        seen.add(key)
        g, p = _number(r.get('new_gdp')), _number(r.get('new_population'))
        if year == target_year - 1:
            selected[name] = (g, p)
    if seen != {(n,y) for n in PROVINCE_NAMES for y in range(2015,2019)}:
        raise ValueError('incomplete source coverage')
    obs = tuple(Observation(i,n,target_year-1,*selected[n]) for i,n in order)
    return InactiveSnapshot(target_year,target_year-1,order,obs,actual,frozen_hashes,
                            tuple((k,times[k]) for k in ('gdp','population')))
