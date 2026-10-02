"""Explicit synthetic C8 declarations; no archive loader or runtime attestation.

A receipt cannot reconstruct household aggregates. Callers supply the already
constructed batch separately. Units and provenance are declarations only; this
module does not inspect numerical arrays or establish Objective A protection.
"""
from dataclasses import dataclass


STAGES = ('entering_c8', 'frozen_entering_c8', 'completed_c8_household_pre_outer')
REQUIRED_UNITS = ('N', 'wjt', 'tau', 'ct', 'household_lt', 'at', 'bt', 'at_tax', 'S')


def _label(value):
    return (type(value) is str and bool(value.strip())
            and value.strip().upper() not in {'UNKNOWN', 'UNRESOLVED', 'NONE', 'NULL'})


def _axis(value, start):
    if type(value) is not tuple or not value:
        raise ValueError('explicit immutable index/name axis required')
    for index, row in enumerate(value, start):
        if (type(row) is not tuple or len(row) != 2
                or type(row[0]) is not int or row[0] != index
                or not _label(row[1])):
            raise ValueError('model/annual axis must retain its declared index base')
    if len({row[1] for row in value}) != len(value):
        raise ValueError('duplicate axis label')
    return value


def _units(value):
    if type(value) is not tuple:
        raise ValueError('explicit immutable unit contract required')
    if any(type(row) is not tuple or len(row) != 2
           or not _label(row[0]) or not _label(row[1]) for row in value):
        raise ValueError('unknown or invalid unit declaration')
    names = tuple(row[0] for row in value)
    if len(set(names)) != len(names) or not set(REQUIRED_UNITS) <= set(names):
        raise ValueError('unique units for state/household/share fields required')
    if dict(value)['S'] != 'dimensionless':
        raise ValueError('frozen shares must be declared dimensionless')
    return value


@dataclass(frozen=True)
class InputDeclaration:
    """Each component repeats the same combined unit contract, without inference."""
    model_axis: tuple
    annual_axis: tuple
    stage: str
    unit_contract: tuple


@dataclass(frozen=True, eq=False)
class FixedC8InputBinding:
    """Synthetic object-reference binding, not a seal or original live identity."""
    states: object
    frozen_shares: object
    batch: object
    state_declaration: InputDeclaration
    share_declaration: InputDeclaration
    household_declaration: InputDeclaration
    province_mapping: tuple  # (model index, short name, annual index, full name)

    def validate(self, *, states, frozen_shares, batch, turn, province_axis,
                 province_mapping, input_kind):
        if type(self) is not FixedC8InputBinding:
            raise ValueError('exact synthetic C8 binding required')
        if input_kind != 'synthetic' or type(turn) is not int or turn != 8:
            raise ValueError('binding is only for synthetic fixed C8')
        if self.states is not states or self.frozen_shares is not frozen_shares or self.batch is not batch:
            raise ValueError('C8 state/share/aggregate object reference mismatch')
        declarations = (self.state_declaration, self.share_declaration, self.household_declaration)
        if any(type(item) is not InputDeclaration for item in declarations):
            raise ValueError('three exact input declarations required')
        model_axis = _axis(self.state_declaration.model_axis, 0)
        annual_axis = _axis(self.state_declaration.annual_axis, 1)
        units = _units(self.state_declaration.unit_contract)
        for declaration, stage in zip(declarations, STAGES):
            if type(declaration.stage) is not str or declaration.stage != stage:
                raise ValueError('C8 entering/frozen/completed-household stage mismatch')
            if (_axis(declaration.model_axis, 0) != model_axis
                    or _axis(declaration.annual_axis, 1) != annual_axis
                    or _units(declaration.unit_contract) != units):
                raise ValueError('C8 inputs require the same model/annual axes and units')
        mapping = self.province_mapping
        if type(mapping) is not tuple or len(mapping) != len(model_axis) or len(mapping) != len(annual_axis):
            raise ValueError('explicit model-zero/annual-one correspondence required')
        for row, model, annual in zip(mapping, model_axis, annual_axis):
            if (type(row) is not tuple or len(row) != 4
                    or type(row[0]) is not int or type(row[2]) is not int
                    or not _label(row[1]) or not _label(row[3])
                    or (row[0], row[1]) != model or (row[2], row[3]) != annual):
                raise ValueError('explicit mapping must match both ordered identities')
        if type(province_axis) is not tuple or province_axis != annual_axis:
            raise ValueError('C8 declaration must match annual index/full-name axis')
        annual_mapping = tuple((annual, full, short) for _, short, annual, full in mapping)
        if province_mapping is not None and province_mapping != annual_mapping:
            raise ValueError('C8 mapping must match prepared model-name mapping')
        if type(states) is not tuple or len(states) != len(model_axis):
            raise ValueError('explicit ordered model state tuple required')
        views = []
        for row, (model_index, short, annual_index, full) in zip(states, mapping):
            if (type(row) is not dict or type(row.get('name')) is not str
                    or row.get('name') != short):
                raise ValueError('original model state name must match zero-based axis')
            # Old states need not repeat the enclosing row's index/full-name labels.
            # If present, validate them; never require caller-side relabelling.
            if ('province_index' in row
                    and (type(row['province_index']) is not int
                         or row['province_index'] != model_index)):
                raise ValueError('original model index must remain zero-based')
            if ('source_province_name' in row
                    and (type(row['source_province_name']) is not str
                         or row['source_province_name'] != full)):
                raise ValueError('existing source full-name conflicts with mapping')
            if any(key in row for key in ('_fixed_c8_original_state', '_fixed_c8_model_identity')):
                raise ValueError('reserved adapter provenance keys already present')
            # A separate annual view serves the existing middle contract. Original
            # object/labels remain intact and referenced; numerical values unchanged.
            view = dict(row)
            view['province_index'] = annual_index
            view['source_province_name'] = full
            view['_fixed_c8_original_state'] = row
            view['_fixed_c8_model_identity'] = (model_index, short)
            views.append(view)
        # Declarations and views do not authenticate old inputs or prove units.
        return tuple(views)
