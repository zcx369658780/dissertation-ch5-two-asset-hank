"""New V006 tests only. Explicit leaf loading; no package/old-test imports.

All receipts below are invented in memory. No original consumer is loaded.
"""
import sys
sys.dont_write_bytecode = True
import hashlib
import importlib.abc
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'src/ch5_two_asset_hank/'
SEAM = 'validators/multi_province/annual_observed_labor_diagnostic/'


class NoScientificImports(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split('.')[0] in {'ch5_two_asset_hank', 'validators', 'exports', 'scipy'}:
            raise ImportError('V006 scientific/package import denied: ' + fullname)
        return None


GUARD = NoScientificImports()
sys.meta_path.insert(0, GUARD)


def leaf(name, relative):
    path = ROOT / relative
    if path.resolve() != path or any(p.is_symlink() for p in (path, *path.parents)):
        raise AssertionError('exact non-link candidate source required')
    expected = json.loads((ROOT.parent / 'receipts/view-hashes.json').read_text(encoding='utf-8'))
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest().upper() != expected[relative]:
        raise AssertionError('candidate source hash mismatch: ' + relative)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    # Execute reviewed candidate bytes, not package initializers or path loaders.
    exec(compile(raw, str(path), 'exec'), module.__dict__)
    return module


helper = leaf('_annual_accepted_wedge_helper', SOURCE + 'corrected_diagnostic/lagged_observed_gdp_wedge.py')
context = leaf('_v006_context', SOURCE + 'corrected_diagnostic/annual_observed_labor_context.py')
adapter = leaf('_v006_array', SOURCE + 'corrected_diagnostic/annual_labor_array_adapter.py')
archive = leaf('_v006_archive', SEAM + 'archive_aggregate_adapter.py')
binding = leaf('_v006_binding', SEAM + 'fixed_c8_input_binding.py')
integration = leaf('_v006_integration', SEAM + 'integration.py')
middle = leaf('_v006_middle', SEAM + 'middle_stage.py')
contract = leaf('_v006_contract', SOURCE + 'multi_province/fixed_c8_source_contract.py')
joint = leaf('_v006_joint', SEAM + 'fixed_c8_joint_preparation.py')


def forbidden(*args, **kwargs):
    raise AssertionError('real/observed input or loader forbidden in V006 tests')


for key in ('authenticate_observed_binding', 'prepare_observed_context',
            'prepare_observed_data_only_context', '_prepare_authenticated_observed_context',
            '_preload_data_only_helper'):
    setattr(context, key, forbidden)


class Fixture:
    def __init__(self):
        self.n = 31
        self.axis = tuple((i+1, 'Invented Province %02d' % i) for i in range(31))
        self.mapping = tuple((i+1, full, 'SYNTH_%02d' % i) for i, (_, full) in enumerate(self.axis))
        self.model_mapping = tuple((i, short, one, full) for i, (one, full, short) in enumerate(self.mapping))
        self.model = tuple((i, short) for i, (_, _, short) in enumerate(self.mapping))
        raw = json.dumps(dict(schema='CH5_INVENTED_ANNUAL_FIXTURE_V1', input_kind='synthetic',
            province_axis=self.axis, target_year=2018, observation_year=2017,
            price_basis='synthetic_fixture', price_verified=False,
            records=[(i+1, 2017, 10+i, 2) for i in range(31)])).encode()
        self.sha = hashlib.sha256(raw).hexdigest().upper()
        self.context = context.prepare_synthetic_context(raw, expected_fixture_sha256=self.sha,
                                                        province_axis=self.axis, target_year=2018)
        self.meta = dict(target_year=2018, province_axis=self.axis, source_sha256=self.sha,
                        input_kind='synthetic', price_basis='synthetic_fixture', price_verified=False)
        self.array = adapter.prepare_annual_array(self.context, province_mapping=self.mapping, **self.meta)
        self.source = binding.ExternalSourceAxis('invented_fixture', self.sha, 'synthetic_identifier',
            tuple((7000 + 7*i, full) for i, (_, full) in reversed(tuple(enumerate(self.axis)))))
        self.units = tuple((key, 'dimensionless' if key == 'S' else 'synthetic_' + key)
                           for key in binding.REQUIRED_UNITS)
        self.declarations = tuple(binding.InputDeclaration(self.model, self.axis, stage,
                                  self.units, self.source) for stage in binding.STAGES)
        self.archive_decl = archive.ArchiveDeclaration('SIM_C8_INVENTED', 'a'*64, self.model,
            archive.HOUSEHOLD_STAGE, tuple((k, 'synthetic_' + k) for k in contract.FIELDS))
        self.terminals = tuple(archive.DeclaredTerminal(dict(province_index=i, province=short,
            checkpoint=i+1, B=1e-9, D=1e-8, aggregates={
                'Ct': {'mass_form': 1.+i/100}, 'Lt': {'mass_form': .3+i/100},
                'At': {'mass_form': 2.+i/5}, 'Bt': {'mass_form': -0. if i == 0 else -i/100},
                'AtTax': {'mass_form': i/1000}}), self.archive_decl)
            for i, short in self.model)
        self.batch = archive.adapt_terminal_receipts(self.terminals, expected_declaration=self.archive_decl)
        self.states = tuple(dict(name=short, N=2.+i/10, wjt=1.+i/30, tau=.03+i/1000,
            inter_prv_ratio=.25, Kt0=100., alpha=.4, Zt=1.2, pit=.02, Kt_prev=5.,
            Zt_1=1.2, pit_1=.02, rk=.03, corptau=.1, Tt=.1,
            ramin=0., ramax=1., wjtmin=0., wjtmax=10.) for i, short in self.model)
        self.shares = np.zeros((31,31), dtype=np.float64)
        for i in range(31):
            self.shares[i,i] = .75
            self.shares[(i+1)%31,i] = .25
        self.share_sha = hashlib.sha256(self.shares.astype('<f8').tobytes(order='F')).hexdigest().upper()
        self.distance = tuple(tuple(.002*(1+(j+2*i)%7) for i in range(31)) for j in range(31))
        self.params = dict(ga=2., phi_l=5., alphal=1.2, epsilon=10., theta=100., delta=.025,
                           istar=.015, rho_pi=1.25, totalpit=.02, epsilon_pi=0.)
        self.bound = binding.FixedC8InputBinding(self.states, self.shares, self.batch,
            *self.declarations, self.model_mapping,
            tuple((i, 7000+7*i, full) for i, (_, full) in enumerate(self.axis)))
        self.contract = contract.FixedC8SourceContract(self.archive_decl, *self.declarations,
                                                      tuple(range(1,32)))
        self.events = []
        self.mode = None
        self.ledger = dict(engineering_fixture_label='V006_NEW_SYNTHETIC',
                           **{k:0 for k in middle.LEDGER_KEYS})
        self.prepared = None
        self.prepare()

    def prepare(self):
        self.prepared = joint.prepare_joint(contract=self.contract, binding=self.bound,
            annual_context=self.context, prepared_array=self.array, params=self.params,
            distance=self.distance, expected_share_sha=self.share_sha)
        self.middle = middle.prepare_middle_stage(annual_context=self.context,
            prepared_array=self.array, province_mapping=self.mapping, ledger=self.ledger,
            dependencies=middle.FixtureDependencies(self.c1, self.firm, 'V006_INVENTED_CALLBACKS'))

    def factory(self, **kw):
        self.events.append('factory')
        assert kw['phi_destination_origin'] is self.array.phi_destination_origin
        self.labor_input = kw
        return SimpleNamespace(**kw)

    def labor(self, x):
        self.events.append('labor')
        # Explicit invented boundary formula; no original migration callback.
        values = tuple(sum(x.population_by_origin[i] * x.consumption_by_origin[i]**(-2/5)
            * (x.old_firm_wage_by_destination[j]*(1-x.tax_by_origin[i]-self.distance[j][i])
               / x.phi_destination_origin[j,i])**(1/5) for i in range(31)) for j in range(31))
        if self.mode == 'labor_failure':
            raise ValueError('invented labor failure')
        if self.mode == 'mutate':
            self.states[0]['N'] += 1
        return SimpleNamespace(lt_supply=values)

    def c1(self, *, Ktarget_MU, Kprivate_current_MU, province_order):
        self.events.append('c1')
        gov = tuple(max(float(t)-float(k),0.) for t,k in zip(Ktarget_MU,Kprivate_current_MU))
        return SimpleNamespace(province_order=province_order, GovInv_residual_MU=gov,
                               firm_K_accounting_MU=tuple(float(k)+g for k,g in zip(Kprivate_current_MU,gov)))

    def firm(self, row, private, labor, params):
        i = len([e for e in self.events if e.startswith('firm:')])
        self.events.append('firm:%d' % i)
        if self.mode == 'firm_failure' and i == 7:
            raise ValueError('invented firm failure')
        assert row['Lt_prev'] == self.batch.household_lt[i]
        assert row['AtTax'] == self.batch.at_tax[i]
        assert labor > 0
        fields = {name:1. for name in middle.FIRM_FIELDS}
        fields.update(Kt=private+row['GovInv'], Lt=labor, wjt=2.+i*.03)
        return SimpleNamespace(**fields)

    def wage(self, provinces, wages, phi, distance, *, phi_l, alphal):
        self.events.append('wage')
        assert phi is self.array.phi_destination_origin
        assert distance is self.distance
        self.wage_input = (provinces, wages, phi, distance)
        # Synthetic oracle interface uses destination tax and new destination wages.
        return tuple(alphal**(-phi_l/(1+phi_l)) * sum(phi[j,i] *
            (wages[j]*(1-provinces[j]['tau']-distance[j][i])/phi[j,i])**(1+1/phi_l)
            for j in range(31))**(phi_l/(1+phi_l)) for i in range(31))

    def run(self, **changes):
        kwargs = dict(annual_context=self.context, params=self.params,
            migration_wedge_destination_origin=self.distance,
            spies=integration.SyntheticSpies(self.factory,self.labor,forbidden,self.wage),
            prepared_array=self.array, province_mapping=self.mapping,
            prepared_middle_stage=self.middle, fixed_c8_binding=self.bound,
            fixed_c8_external_source=self.source, joint_preparation=self.prepared, **self.meta)
        kwargs.update(changes)
        return integration.integrate_turn(None,None,None,8,self.states,self.batch,
            self.shares,self.share_sha,self.ledger,(),**kwargs)


def test_no_model_package_or_old_tests_loaded():
    assert not any(k.split('.')[0] in {'ch5_two_asset_hank','validators','exports','scipy'} for k in sys.modules)
    assert not any(k.startswith('test_') and not k.startswith('test_v006_') for k in sys.modules)
    with pytest.raises(ImportError, match='denied'):
        __import__('ch5_two_asset_hank')
    print('V006_RUNTIME ' + json.dumps(dict(python=sys.version.split()[0],
        numpy=np.__version__, pytest=pytest.__version__,
        numpy_file=np.__file__, python_executable=sys.executable,
        engineering_modules={m.__name__:m.__file__ for m in
            (helper,context,adapter,archive,binding,integration,middle,contract,joint)})))


def test_only_three_new_tests_and_no_initializers_exported():
    assert {p.name for p in (ROOT/'tests').glob('*.py')} == {
        'test_v006_fixed_c8_joint_contract.py','test_v006_annual_dual_boundary.py',
        'test_v006_source_loading_boundary.py'}
    assert not list(ROOT.rglob('__init__.py'))


def test_observed_entry_traps_and_readonly_canonical_mapping():
    with pytest.raises(AssertionError, match='forbidden'):
        context.prepare_observed_context({})
    provinces = leaf('_v006_provinces', SOURCE+'multi_province/province_contracts.py')
    assert tuple(r[2] for r in adapter.CANONICAL_PROVINCE_MAPPING) == provinces.PROVINCE_ORDER
    assert tuple((r[0],r[1]) for r in adapter.CANONICAL_PROVINCE_MAPPING) == context.CANONICAL_AXIS


def test_v001_v002_restrictions_reused_without_importing_scientific_chain():
    assert contract.SOURCE_KIND == 'SYNTHETIC/NOT_REAL_SOURCE'
    for name in ('synthetic_household_bridge.py','household_source_contract.py'):
        text = (ROOT/SOURCE/'multi_province'/name).read_text(encoding='utf-8')
        assert 'SOURCE_KIND' in text and 'synthetic' in text
    assert 'ch5_two_asset_hank.multi_province.one_turn' not in sys.modules
