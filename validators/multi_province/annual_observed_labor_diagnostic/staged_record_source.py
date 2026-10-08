"""Explicit synthetic memory records -> payload for the accepted carrier API.

No carrier/pipeline/package discovery or file/environment/network access. This
adapter never authenticates declarations or interprets economic/scientific units.
Exact built-ins only; inputs must be stable during constructor/call execution.
"""

from dataclasses import dataclass
from math import isfinite


class RecordContractError(ValueError):
    """Schema, record or declaration rejected without normalization."""


class RecordSourceStateError(RuntimeError):
    """A single-use/closed source cannot supply again."""


@dataclass(frozen=True, slots=True)
class _Schema:
    axis_columns: tuple
    fields: tuple
    value_columns: tuple
    units: tuple
    calendar: tuple
    source: tuple


def _mapping(value, keys, label):
    if (type(value) is not dict or any(type(k) is not str for k in value)
            or set(value) != set(keys)):
        raise RecordContractError(f'{label}: exact dict with declared keys required')
    return value


def _sequence(value, label):
    if type(value) not in (list, tuple):
        raise RecordContractError(f'{label}: exact list or tuple required')
    return value


def _text(value, label):
    if type(value) is not str or not value.strip():
        raise RecordContractError(f'{label}: nonblank exact str required')
    return value


def _schema(columns, field_names, units, calendar, source):
    columns = _mapping(columns, ('source_id', 'name', 'order', 'values'), 'columns')
    axis_columns = tuple(_text(columns[k], f'columns.{k}')
                         for k in ('source_id', 'name', 'order'))
    fields = tuple(_text(f, 'field_names') for f in _sequence(field_names, 'field_names'))
    if not fields or len(set(fields)) != len(fields):
        raise RecordContractError('field_names: nonempty unique fields required')
    values = _mapping(columns['values'], fields, 'columns.values')
    value_columns = tuple(_text(values[f], f'columns.values.{f}') for f in fields)
    all_columns = axis_columns + value_columns
    if len(set(all_columns)) != len(all_columns):
        raise RecordContractError('columns: duplicate/conflicting physical column mapping')
    units = _mapping(units, fields, 'units')
    frozen_units = tuple(_text(units[f], f'units.{f}') for f in fields)
    calendar = _mapping(calendar, ('target_year', 'observation_year', 'label'), 'calendar')
    if any(type(calendar[k]) is not int for k in ('target_year', 'observation_year')):
        raise RecordContractError('calendar: exact int years required')
    frozen_calendar = (calendar['target_year'], calendar['observation_year'],
                       _text(calendar['label'], 'calendar.label'))
    source = _mapping(source, ('source_id', 'label'), 'source')
    frozen_source = (_text(source['source_id'], 'source.source_id'),
                     _text(source['label'], 'source.label'))
    return _Schema(axis_columns, fields, value_columns, frozen_units,
                   frozen_calendar, frozen_source)


class RecordSource:
    """Single-use provider with two explicit snapshot times.

    Constructor validates/snapshots schema and declarations, retains records by
    reference (caller mutations BEFORE supply are visible). First __call__ checks
    and snapshots all 31 rows; output has fresh dicts and immutable value tuples.
    It returns one carrier-compatible memory payload, never a FrozenCarrier.
    Repeated supply is rejected after success OR failure; close is idempotent and
    rejects all later supply. Returned payload/references cannot be revoked.

    columns = {source_id: physical column, name: physical column,
               order: physical column, values: {logical field: physical column}}.
    field_names supplies explicit logical order; rows have EXACTLY these columns.
    units/calendar/source use the accepted carrier's explicit declaration schema.

    No external resources are acquired. Caller owns source until registering its
    __call__/close in A2; A2 then calls close once even on provider failure. Source
    releases retained memory on supply failure/success and close; constructor
    failures do not transfer ownership or retain a returned partial resource.
    Single-threaded stable-input contract; no OS/hostile replacement protection.
    """

    def __init__(self, records, *, columns, field_names, units, calendar, source):
        records = _sequence(records, 'records')
        self._schema = _schema(columns, field_names, units, calendar, source)
        self._records = records
        self._state = 'new'
        self._supply_attempts = 0
        self._close_count = 0

    @property
    def state(self):
        return self._state

    @property
    def supply_attempts(self):
        return self._supply_attempts

    @property
    def close_count(self):
        return self._close_count

    def close(self):
        if self._state != 'closed':
            self._state = 'closed'
            self._close_count += 1
            self._records = None
            self._schema = None

    def __call__(self):
        if self._state != 'new':
            raise RecordSourceStateError('record source requires new single-use state')
        self._state = 'supplying'
        self._supply_attempts += 1
        try:
            schema = self._schema
            records = self._records
            if len(records) != 31:
                raise RecordContractError('records: exactly 31 rows required')
            axes, identifiers, names = [], set(), set()
            values = [[] for _ in schema.fields]
            id_type = None
            all_columns = schema.axis_columns + schema.value_columns
            id_column, name_column, order_column = schema.axis_columns
            for position, row in enumerate(records):
                row = _mapping(row, all_columns, f'records[{position}]')
                identifier = row[id_column]
                if type(identifier) not in (int, str):
                    raise RecordContractError(f'records[{position}].ID: exact int or str required')
                if type(identifier) is str:
                    _text(identifier, 'record.ID')
                if id_type is None:
                    id_type = type(identifier)
                if type(identifier) is not id_type:
                    raise RecordContractError('records: mixed ID types')
                name = _text(row[name_column], 'record.name')
                if identifier in identifiers or name in names:
                    raise RecordContractError('records: duplicate ID or name')
                order = row[order_column]
                if type(order) is not int or order != position:
                    raise RecordContractError('record.order: must match zero-based input position')
                identifiers.add(identifier)
                names.add(name)
                axes.append({'source_id': identifier, 'name': name, 'order': order})
                for index, column in enumerate(schema.value_columns):
                    value = row[column]
                    if type(value) not in (int, float):
                        raise RecordContractError(f'record.{column}: exact int or float required')
                    if type(value) is float and not isfinite(value):
                        raise RecordContractError(f'record.{column}: nonfinite value')
                    values[index].append(value)
            calendar = dict(zip(('target_year', 'observation_year', 'label'), schema.calendar))
            source = dict(zip(('source_id', 'label'), schema.source))
            payload = {
                'axes': tuple(axes), 'field_names': schema.fields,
                'units': dict(zip(schema.fields, schema.units)),
                'calendar': calendar, 'source': source,
                'vectors': {
                    field: {'values': tuple(values[index]), 'unit': schema.units[index],
                            'calendar': dict(calendar), 'source': dict(source)}
                    for index, field in enumerate(schema.fields)
                },
            }
            self._state = 'supplied'
            return payload
        except BaseException:
            self._state = 'failed'
            raise
        finally:
            self._records = None
            self._schema = None
