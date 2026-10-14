"""Joint admission and refusal, exclusively invented terminal objects."""
from dataclasses import replace
import math
from types import SimpleNamespace
import pytest
from test_v006_source_loading_boundary import Fixture, archive, contract, joint


def test_complete_five_fields_preserve_mass_form_and_negative_zero():
    f = Fixture()
    for i in range(31):
        assert (f.batch.ct[i], f.batch.household_lt[i], f.batch.at[i], f.batch.bt[i], f.batch.at_tax[i]) == (
            1+i/100, .3+i/100, 2+i/5, -0. if i==0 else -i/100, i/1000)
    assert math.copysign(1.,f.batch.bt[0]) == -1.
    assert f.contract.source_authenticated is False
    assert f.contract.economic_units == 'ECONOMIC_UNIT_UNVERIFIED'


@pytest.mark.parametrize('field', ['Ct','Lt','At','Bt','AtTax'])
def test_missing_mass_field_rejected(field):
    f = Fixture()
    del f.terminals[4].receipt['aggregates'][field]
    with pytest.raises(ValueError, match='mass_form'):
        archive.adapt_terminal_receipts(f.terminals, expected_declaration=f.archive_decl)
    assert f.events == []


@pytest.mark.parametrize('bad', [True, float('nan'), float('inf'), [1.]])
def test_invalid_scalar_rejected_before_consumers(bad):
    f = Fixture()
    f.terminals[0].receipt['aggregates']['Bt']['mass_form'] = bad
    with pytest.raises(ValueError):
        archive.adapt_terminal_receipts(f.terminals, expected_declaration=f.archive_decl)
    assert f.events == []


@pytest.mark.parametrize('change', ['units','source','stage','checkpoint','model_axis','external_id','evidence','year','price','population'])
def test_joint_conflicts_rejected_before_consumer_ledger(change):
    f = Fixture()
    if change == 'units':
        f.contract = replace(f.contract, archive_declaration=replace(f.archive_decl,
            unit_contract=tuple((k,'wrong') for k in contract.FIELDS)))
    elif change == 'source':
        f.contract = replace(f.contract, archive_declaration=replace(f.archive_decl, source_sha256='b'*64))
    elif change == 'stage':
        bad = replace(f.declarations[0],stage='completed_c8_household_pre_outer')
        f.contract = replace(f.contract,state_declaration=bad)
    elif change == 'checkpoint':
        f.contract = replace(f.contract,terminal_checkpoints=(99,)*31)
    elif change == 'model_axis':
        f.bound = replace(f.bound,province_mapping=tuple(reversed(f.model_mapping)))
    elif change == 'external_id':
        f.bound = replace(f.bound,external_mapping=tuple((i,i+1,name) for i,(_,name) in enumerate(f.axis)))
    elif change == 'evidence':
        f.contract = replace(f.contract,source_evidence='CONTENT_MATCHED')
    elif change == 'year':
        f.contract = replace(f.contract,observation_year=2018)
    elif change == 'price':
        f.contract = replace(f.contract,direct_price_verified=True)
    else:
        f.contract = replace(f.contract,population_basis='households_N=P/3')
    with pytest.raises(ValueError):
        f.prepare()
    assert f.events == []
    assert all(f.ledger[k] == 0 for k in f.ledger if k != 'engineering_fixture_label')


def test_external_panel_ids_join_by_full_name_not_source_position():
    f = Fixture()
    f.run()
    assert f.source.axis[0][0] == 7210
    assert f.bound.external_mapping[0][1] == 7000
    assert f.events[-1] == 'wage'


def test_missing_bt_and_mutated_state_stop_before_calls():
    f = Fixture()
    object.__setattr__(f.batch,'bt',None)
    with pytest.raises(ValueError):
        f.run()
    assert f.events == []
    assert (f.prepared.attempted,f.prepared.failed,f.prepared.completed) == (1,1,0)


def test_s_transpose_negative_bool_and_corder_hash_refused():
    import hashlib
    for bad in ('transpose','negative','bool','hash'):
        f = Fixture()
        if bad == 'transpose': f.shares[:] = f.shares.T.copy()
        if bad == 'negative': f.shares[0,1] = -.1
        if bad == 'bool': f.distance = tuple(tuple(True for _ in range(31)) for _ in range(31))
        if bad == 'hash': f.share_sha = hashlib.sha256(f.shares.tobytes(order='C')).hexdigest().upper()
        with pytest.raises(ValueError): f.prepare()
        assert f.events == []


@pytest.mark.parametrize('field,value', [('payoff_timing','SAME_TURN'),
    ('share_orientation','origin_by_destination'), ('annual_layout','float64_F_order')])
def test_role_changes_refused(field, value):
    f = Fixture()
    f.contract = replace(f.contract, **{field:value})
    with pytest.raises(ValueError,match='role conflict'): f.prepare()
    assert f.events == []
