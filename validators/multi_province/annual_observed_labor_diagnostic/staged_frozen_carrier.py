"""Inert synthetic carrier. No source authentication or scientific interpretation.

Use create_carrier for validated construction. Only exact built-in dict/list/tuple,
str/int/float inputs are supported, with the schema below; subclasses and bool are
rejected. Frozen records protect ordinary Python mutation, not hostile reflection.
No file, environment, network, model or package access occurs here.
"""

from dataclasses import dataclass
from math import isfinite


class ContractError(ValueError):
    """Explicit input contract rejection."""


class ClosedCarrierError(RuntimeError):
    """A closed handle cannot grant a new reference."""


@dataclass(frozen=True, slots=True)
class Axis:
    source_id: int | str
    name: str
    order: int


@dataclass(frozen=True, slots=True)
class Calendar:
    target_year: int
    observation_year: int
    label: str


@dataclass(frozen=True, slots=True)
class Source:
    source_id: str
    label: str


@dataclass(frozen=True, slots=True)
class Vector:
    field: str
    values: tuple[int | float, ...]
    unit: str


@dataclass(frozen=True, slots=True)
class FrozenCarrier:
    axes: tuple[Axis, ...]
    vectors: tuple[Vector, ...]
    calendar: Calendar
    source: Source


def _mapping(value, keys, label):
    if type(value) is not dict:
        raise ContractError(f"{label}: exact dict required")
    if any(type(key) is not str for key in value) or set(value) != set(keys):
        raise ContractError(f"{label}: exact keys required: {tuple(keys)}")
    return value


def _sequence(value, label):
    if type(value) not in (list, tuple):
        raise ContractError(f"{label}: exact list or tuple required")
    return value


def _text(value, label):
    if type(value) is not str or not value.strip():
        raise ContractError(f"{label}: nonblank exact str required")
    return value  # Validate without stripping or normalizing accepted declarations.


def _calendar(value, label):
    value = _mapping(value, ('target_year', 'observation_year', 'label'), label)
    for key in ('target_year', 'observation_year'):
        if type(value[key]) is not int:
            raise ContractError(f"{label}.{key}: exact int required")
    return Calendar(value['target_year'], value['observation_year'],
                    _text(value['label'], f'{label}.label'))


def _source(value, label):
    value = _mapping(value, ('source_id', 'label'), label)
    return Source(_text(value['source_id'], f'{label}.source_id'),
                  _text(value['label'], f'{label}.label'))


def create_carrier(*, axes, field_names, vectors, units, calendar, source):
    """Snapshot 31 axes and explicit fields, preserving all accepted order/values.

    axes: 31 {source_id: int OR str, name: str, order: zero-based int} records.
      IDs must have one homogeneous exact type; IDs and names must be unique.
    field_names: nonempty ordered list/tuple of unique nonblank str names.
    vectors: exact field-keyed dict; each record has values (31 int/float), unit,
      calendar and source. Per-vector declarations must equal global declarations.
    units: exact field-keyed dict of nonblank strings.
    calendar: {target_year: int, observation_year: int, label: str}.
    source: {source_id: str, label: str}.

    Declarations are compared, never authenticated, converted or economically
    interpreted. In particular no relationship between the two years is inferred.
    """
    axes = _sequence(axes, 'axes')
    if len(axes) != 31:
        raise ContractError('axes: exactly 31 records required')
    frozen_axes = []
    ids, names = set(), set()
    id_type = None
    for order, raw in enumerate(axes):
        raw = _mapping(raw, ('source_id', 'name', 'order'), f'axes[{order}]')
        identifier = raw['source_id']
        if type(identifier) not in (int, str):
            raise ContractError(f'axes[{order}].source_id: exact int or str required')
        if type(identifier) is str:
            _text(identifier, f'axes[{order}].source_id')
        if id_type is None:
            id_type = type(identifier)
        if type(identifier) is not id_type:
            raise ContractError('axes: mixed source-ID types forbidden')
        name = _text(raw['name'], f'axes[{order}].name')
        if identifier in ids or name in names:
            raise ContractError('axes: duplicate source-ID or name')
        if type(raw['order']) is not int or raw['order'] != order:
            raise ContractError(f'axes[{order}].order: must match zero-based input position')
        ids.add(identifier)
        names.add(name)
        frozen_axes.append(Axis(identifier, name, order))

    fields = tuple(_text(f, 'field_names entry')
                   for f in _sequence(field_names, 'field_names'))
    if not fields or len(set(fields)) != len(fields):
        raise ContractError('field_names: nonempty unique names required')
    vectors = _mapping(vectors, fields, 'vectors')
    units = _mapping(units, fields, 'units')
    declared_calendar = _calendar(calendar, 'calendar')
    declared_source = _source(source, 'source')
    frozen_vectors = []
    for field in fields:
        unit = _text(units[field], f'units.{field}')
        raw = _mapping(vectors[field], ('values', 'unit', 'calendar', 'source'),
                       f'vectors.{field}')
        vector_unit = _text(raw['unit'], f'vectors.{field}.unit')
        if (vector_unit != unit
                or _calendar(raw['calendar'], f'vectors.{field}.calendar') != declared_calendar
                or _source(raw['source'], f'vectors.{field}.source') != declared_source):
            raise ContractError(f'vectors.{field}: inconsistent declarations')
        values = _sequence(raw['values'], f'vectors.{field}.values')
        if len(values) != 31:
            raise ContractError(f'vectors.{field}.values: exactly 31 values required')
        for value in values:
            if type(value) not in (int, float):
                raise ContractError(f'vectors.{field}.values: exact int or float required')
            if type(value) is float and not isfinite(value):
                raise ContractError(f'vectors.{field}.values: nonfinite value')
        frozen_vectors.append(Vector(field, tuple(values), unit))
    return FrozenCarrier(tuple(frozen_axes), tuple(frozen_vectors),
                         declared_calendar, declared_source)


class CarrierHandle:
    """Single-owner, non-concurrent lifecycle; close is idempotent.

    acquire returns the same carrier until closed. Context exit closes even on an
    exception. close drops this handle's reference; previously acquired immutable
    objects cannot be revoked. This is not an OS or hostile-replacement boundary.
    """

    __slots__ = ('_carrier',)

    def __init__(self, carrier):
        if type(carrier) is not FrozenCarrier:
            raise ContractError('handle: FrozenCarrier required')
        self._carrier = carrier

    def acquire(self):
        if self._carrier is None:
            raise ClosedCarrierError('carrier handle is closed')
        return self._carrier

    @property
    def closed(self):
        return self._carrier is None

    def close(self):
        self._carrier = None

    def __enter__(self):
        self.acquire()  # Reject re-entry after close.
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False
