"""Independent asymmetric scalar oracles for the two synthetic boundaries."""
from fractions import Fraction
import math
import pytest
from test_v006_source_loading_boundary import Fixture, forbidden


def test_same_master_tax_wages_s_c1_and_order():
    f = Fixture()
    out = f.run()
    assert f.events == ['factory','labor','c1'] + ['firm:%d'%i for i in range(31)] + ['wage']
    assert out['inputs'].phi_destination_origin is f.array.phi_destination_origin
    assert f.labor_input['tax_by_origin'] == [r['tau'] for r in f.states]
    assert f.labor_input['old_firm_wage_by_destination'] == [r['wjt'] for r in f.states]
    # Analytic ratio, separately derived from GDP/population; origin minus destination.
    phi = 1 + float(Fraction(3,10)*Fraction(11-10,11+10))
    assert f.array.phi_destination_origin[0,1] == pytest.approx(phi)
    assert f.array.phi_destination_origin[1,0] < 1 < phi
    expected_labor = []
    for j in range(31):
        contributions = []
        for i in range(31):
            p = 1 + .3*((10+i)-(10+j))/((10+i)+(10+j))
            contributions.append((2+i/10)*(1+i/100)**(-.4)*
                ((1+j/30)*(1-(.03+i/1000)-f.distance[j][i])/p)**.2)
        expected_labor.append(math.fsum(contributions))
    assert [x.Lt for x in out['middle_result'].firms] == pytest.approx(expected_labor)
    # S has only home and next-destination entries: independent two-term oracle.
    for j, private in enumerate(out['middle_result'].capital.private):
        prior = (j-1)%31
        expected = .75*(2+j/5)*(2+j/10) + .25*(2+prior/5)*(2+prior/10)
        assert private == pytest.approx(expected)
        assert out['middle_result'].c1.GovInv_residual_MU[j] == pytest.approx(max(100-expected,0))
    w = []
    wrong = []
    for i in range(31):
        terms, swapped = [], []
        for j in range(31):
            p = 1+.3*((10+i)-(10+j))/((10+i)+(10+j))
            terms.append(p*((2+j*.03)*(1-(.03+j/1000)-f.distance[j][i])/p)**1.2)
            swapped.append(p*((2+j*.03)*(1-(.03+i/1000)-f.distance[j][i])/p)**1.2)
        w.append(1.2**(-5/6)*math.fsum(terms)**(5/6))
        wrong.append(1.2**(-5/6)*math.fsum(swapped)**(5/6))
    assert out['wages'] == pytest.approx(w)
    assert abs(w[0]-wrong[0]) > .001
    assert (f.prepared.attempted,f.prepared.completed,f.prepared.failed) == (1,1,0)
    assert out['model_activation'] is False and out['full_outer_runtime_integrated'] is False


def test_single_use_and_explicit_close_refuse_before_next_calls():
    for completed in (False,True):
        f = Fixture()
        if completed: f.run()
        else: f.prepared.close()
        previous = list(f.events)
        with pytest.raises(ValueError, match='expired'): f.run()
        assert f.events == previous


@pytest.mark.parametrize('mode,expected', [('labor_failure',['factory','labor']),
    ('mutate',['factory','labor']), ('firm_failure',['factory','labor','c1']+['firm:%d'%i for i in range(8)])])
def test_failure_preserves_attempt_and_suppresses_later_boundaries(mode, expected):
    f = Fixture()
    f.mode = mode
    with pytest.raises(ValueError): f.run()
    assert f.events == expected
    assert (f.prepared.attempted,f.prepared.completed,f.prepared.failed) == (1,0,1)
    with pytest.raises(ValueError,match='expired'): f.run()


def test_equal_array_replacement_and_missing_joint_refused():
    f = Fixture()
    from dataclasses import replace
    with pytest.raises(ValueError): f.run(joint_preparation=None)
    assert f.events == []
    with pytest.raises(ValueError): f.run(params=dict(f.params))
    assert f.events == []


def test_original_five_field_and_state_values_unchanged():
    f = Fixture()
    before = tuple(dict(r) for r in f.states)
    five = tuple(getattr(f.batch,k) for k in ('ct','household_lt','at','bt','at_tax'))
    out = f.run()
    assert f.states == before
    assert tuple(getattr(f.batch,k) for k in ('ct','household_lt','at','bt','at_tax')) == five
    assert all(v['_fixed_c8_original_state'] is f.states[i] for i,v in enumerate(out['inputs'].old_provinces))


def test_context_tuple_and_array_backing_distinct_but_same_values():
    f = Fixture()
    assert f.context.phi_destination_origin is not f.array.phi_destination_origin
    assert f.array.phi_destination_origin.tolist() == [list(r) for r in f.context.phi_destination_origin]
    with pytest.raises(ValueError): f.array.phi_destination_origin.setflags(write=True)


def test_same_s_quantity_and_prior_raw_payoff_orientation_oracle():
    f = Fixture()
    result = f.run()
    raw_prior = tuple(.01+.002*j for j in range(31))
    # Fixture-only payoff, never original callback: two nonzero destinations per origin.
    payoff = tuple(math.fsum(f.shares[j,i]*raw_prior[j] for j in range(31)) for i in range(31))
    assert payoff == pytest.approx(tuple(.75*raw_prior[i]+.25*raw_prior[(i+1)%31] for i in range(31)))
    assert payoff[0] != pytest.approx(.75*raw_prior[0]+.25*raw_prior[-1])
    assert result['middle_result'].capital.no_same_turn_share_recomputation


def test_replaced_equal_master_context_and_frozen_signed_zero_refused():
    from dataclasses import replace
    for mode in ('array','context','signed_zero'):
        f = Fixture()
        changes = {}
        if mode == 'array': changes['prepared_array'] = replace(f.array)
        if mode == 'context': changes['annual_context'] = replace(f.context)
        if mode == 'signed_zero': f.shares[0,2] = -0.
        with pytest.raises(ValueError): f.run(**changes)
        assert f.events == []
