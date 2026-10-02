"""Narrow inert K1B dual-consumer seam; full outer runner is NOT integrated."""
from dataclasses import dataclass
from types import MappingProxyType
from pathlib import Path
from numbers import Real
import math
import sys


@dataclass(frozen=True)
class OneTurnInputs:
    province_order: tuple
    old_provinces: tuple
    params: object
    phi_destination_origin: object
    migration_wedge_destination_origin: object
    household_outputs: object


@dataclass(frozen=True)
class SyntheticSpies:
    migration_inputs_factory: object
    reconstruct_migration_labor: object
    firm_stage: object
    composite_household_wages: object


def _finite_scalar(value):
    return not isinstance(value, bool) and isinstance(value, Real) and math.isfinite(value)


def _validate_input_axes(consumption, distance, n):
    """Refuse nested/nonfinite cells without copying or changing source values."""
    if getattr(consumption, 'ndim', 1) != 1 or getattr(distance, 'ndim', 2) != 2:
        raise ValueError('consumption must be 1d and distance must be 2d')
    try:
        valid = (len(consumption) == n and all(_finite_scalar(v) for v in consumption)
                 and len(distance) == n and all(
                     len(row) == n and all(_finite_scalar(v) for v in row)
                     for row in distance))
    except (TypeError, OverflowError):
        raise ValueError('household/distance finite scalar axes required') from None
    if not valid:
        raise ValueError('household/distance finite scalar axes mismatch')


def integrate_turn(repository, task_root, turn_root, turn, states, batch,
                   frozen_shares, expected_share_sha, ledger, household_rows, *,
                   annual_context, target_year, province_axis, source_sha256,
                   input_kind, price_basis, price_verified, params,
                   migration_wedge_destination_origin, spies,
                   prepared_array=None, province_mapping=None,
                   prepared_middle_stage=None, fixed_c8_binding=None):
    """Mirror historical arguments, add explicit annual carrier; spies only.

    The default firm_stage remains an opaque synthetic test boundary. An explicit
    prepared middle stage provides the separately prepared engineering bridge;
    neither mode activates production consumers, household or outer runtime.
    """
    module = sys.modules.get(type(annual_context).__module__)
    expected = Path(__file__).resolve().parents[3] / 'src/ch5_two_asset_hank/corrected_diagnostic/annual_observed_labor_context.py'
    if module is None or getattr(module, 'AnnualContext', None) is not type(annual_context) or Path(getattr(module, '__file__', '')).resolve() != expected:
        raise ValueError('exact engineering annual context type required')
    module.AnnualContext.validate(annual_context, target_year=target_year, province_axis=province_axis,
        source_sha256=source_sha256, input_kind=input_kind,
        price_basis=price_basis, price_verified=price_verified)
    if annual_context.input_kind != 'synthetic' or type(spies) is not SyntheticSpies:
        raise ValueError('production consumers blocked pending science/Objective A contracts')
    if prepared_middle_stage is not None and prepared_array is None:
        raise ValueError('explicit middle stage requires prepared annual array carrier')
    phi = annual_context.phi_destination_origin
    province_order = tuple(i for i, _ in province_axis)
    if prepared_array is None:
        if province_mapping is not None:
            raise ValueError('mapping requires explicitly prepared annual array carrier')
    else:
        adapter = sys.modules.get(type(prepared_array).__module__)
        adapter_path = expected.with_name('annual_labor_array_adapter.py')
        if (adapter is None or getattr(adapter, 'AnnualArrayCarrier', None) is not type(prepared_array)
                or Path(getattr(adapter, '__file__', '')).resolve() != adapter_path):
            raise ValueError('exact prepared annual array adapter required')
        adapter.AnnualArrayCarrier.validate(prepared_array, annual_context=annual_context,
            target_year=target_year, province_axis=province_axis, source_sha256=source_sha256,
            input_kind=input_kind, price_basis=price_basis, price_verified=price_verified,
            province_mapping=province_mapping)
        phi = prepared_array.phi_destination_origin
        province_order = prepared_array.province_order
    n = len(province_axis)
    if type(states) is not tuple or len(states) != n or any(type(r) is not dict for r in states):
        raise ValueError('explicit states on annual axis required')
    if any(not {'N', 'wjt', 'tau'} <= set(r) for r in states):
        raise ValueError('source-faithful labor input keys missing')
    use_c8_binding = turn == 8 or fixed_c8_binding is not None
    if not use_c8_binding:
        if any(type(r.get('province_index')) is not int or type(r.get('source_province_name')) is not str
               for r in states) or tuple((r.get('province_index'), r.get('source_province_name')) for r in states) != province_axis:
            raise ValueError('each state must match exact annual index/source-name order')
    if prepared_array is not None and any(type(r.get('name')) is not str
            or r['name'] != province_mapping[i][2] for i, r in enumerate(states)):
        raise ValueError('existing state model short-name must match exact mapping')
    if not {'ga', 'phi_l', 'alphal'} <= set(params):
        raise ValueError('unchanged source parameters required')
    # C8 requires explicit declarations; other historical synthetic turns retain
    # their existing interface. The caller explicitly loads the binding module.
    input_states = states
    if use_c8_binding:
        binding_module = sys.modules.get(type(fixed_c8_binding).__module__)
        binding_path = Path(__file__).with_name('fixed_c8_input_binding.py').resolve()
        if (binding_module is None
                or getattr(binding_module, 'FixedC8InputBinding', None) is not type(fixed_c8_binding)
                or Path(getattr(binding_module, '__file__', '')).resolve() != binding_path):
            raise ValueError('explicitly loaded synthetic fixed C8 binding required')
        input_states = binding_module.FixedC8InputBinding.validate(fixed_c8_binding,
            states=states, frozen_shares=frozen_shares, batch=batch, turn=turn,
            province_axis=province_axis, province_mapping=province_mapping,
            input_kind=annual_context.input_kind)
    _validate_input_axes(batch.ct, migration_wedge_destination_origin, n)
    inputs = OneTurnInputs(province_order,
        tuple(MappingProxyType(dict(r)) for r in input_states), MappingProxyType(dict(params)),
        phi, migration_wedge_destination_origin, batch)
    middle_module = None
    if prepared_middle_stage is not None:
        middle_module = sys.modules.get(type(prepared_middle_stage).__module__)
        middle_path = Path(__file__).with_name('middle_stage.py').resolve()
        if (middle_module is None
                or getattr(middle_module, 'PreparedMiddleStage', None) is not type(prepared_middle_stage)
                or Path(getattr(middle_module, '__file__', '')).resolve() != middle_path):
            raise ValueError('exact prepared engineering middle stage required')
        middle_module.PreparedMiddleStage.validate_pre_spy(prepared_middle_stage,
            inputs, frozen_shares, expected_share_sha, annual_context=annual_context,
            prepared_array=prepared_array, province_mapping=province_mapping, ledger=ledger)
    provinces, household = inputs.old_provinces, inputs.household_outputs
    if prepared_middle_stage is not None:
        ledger['source_faithful_labor_reconstructions'] += 1
    migration = spies.reconstruct_migration_labor(spies.migration_inputs_factory(
        consumption_by_origin=household.ct, population_by_origin=[r['N'] for r in provinces],
        old_firm_wage_by_destination=[r['wjt'] for r in provinces], tax_by_origin=[r['tau'] for r in provinces],
        phi_destination_origin=inputs.phi_destination_origin,
        migration_wedge_destination_origin=inputs.migration_wedge_destination_origin,
        gamma_c=inputs.params['ga'], phi_l=inputs.params['phi_l']))
    middle_result = None
    if prepared_middle_stage is None:
        firms = spies.firm_stage(inputs, migration, frozen_shares, expected_share_sha)
    else:
        middle_result = middle_module.PreparedMiddleStage.run(prepared_middle_stage,
            inputs, migration, frozen_shares, expected_share_sha)
        firms = middle_result.firms
    if len(firms) != n:
        raise ValueError('firm-wage stage axis mismatch')
    if prepared_middle_stage is not None:
        ledger['composite_wage_batches'] += 1
    wages = spies.composite_household_wages(provinces, [f.wjt for f in firms],
        inputs.phi_destination_origin, inputs.migration_wedge_destination_origin,
        phi_l=inputs.params['phi_l'], alphal=inputs.params['alphal'])
    return {'inputs': inputs, 'migration': migration, 'wages': wages,
            'middle_result': middle_result,
            'annual_context': annual_context, 'full_outer_runtime_integrated': False,
            'model_activation': False}
