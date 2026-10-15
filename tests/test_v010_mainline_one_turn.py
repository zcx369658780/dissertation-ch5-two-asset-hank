import json
from pathlib import Path
import numpy as np
import pytest
from ch5_two_asset_hank.multi_province.one_turn import (
    PreFrozenHouseholdOutputBatch, run_mainline_one_turn, prepare_mainline_household_states,
)
from ch5_two_asset_hank.multi_province.stationary_runtime import mainline_initial_states
from ch5_two_asset_hank.multi_province.wage import mainline_phi, mainline_effective_wages
from ch5_two_asset_hank.multi_province.migration_labor import reconstruct_mainline_labor
from ch5_two_asset_hank.multi_province.capital_network import BilateralCapitalNetworkInputs,build_bilateral_capital_network


def fixture():
    return json.loads((Path(__file__).parent/'fixtures/v010_mainline_synthetic_v1.json').read_text(encoding='utf-8'))


def batch(f,strict=True):
    return PreFrozenHouseholdOutputBatch(f['initial_consumption_Ct_per_person'],
        f['initial_household_Lt_per_person'],f['initial_private_assets_At_per_person'],
        f['initial_liquid_assets_Bt_per_person'],[.03,.07],(True,True),
        ({'strict_qualified':strict},{'strict_qualified':strict}))


def test_phi_direction_and_reference():
    phi=mainline_phi([3,4.5])
    np.testing.assert_allclose(phi,[[1,1.06],[.94,1]],rtol=0,atol=1e-15)
    with pytest.raises(ValueError): mainline_phi([0,1])


@pytest.mark.parametrize('tax',[0,.2])
def test_single_destination_wage_tax_closed_form(tax):
    # One destination: q itself is the exact composite net wage for alpha_l=1.
    net=mainline_effective_wages([2],[tax],[[1]],[[0]],phi_l=5,alphal=1)
    assert net[0] == pytest.approx(2*(1-tax),abs=1e-14)
    assert net[0]*1.3 == pytest.approx(2*(1-tax)*1.3)


def test_destination_tax_labor_and_additive_cost():
    out=reconstruct_mainline_labor(consumption=[1,1],population=[10,20],gross_wages=[2,3],
        destination_taxes=[.1,.3],phi=np.ones((2,2)),sigma=[[0,.2],[.1,0]],gamma_c=2,phi_l=5)
    expected=np.array([[1.8**.2*10,1.4**.2*20],[1.8**.2*10,2.1**.2*20]])
    np.testing.assert_allclose(out.lt_mat,expected)
    np.testing.assert_allclose(out.lt_supply,expected.sum(axis=1))


def test_three_province_home_capital_and_same_s_oracle():
    result=build_bilateral_capital_network(BilateralCapitalNetworkInputs(
        ('A','B','C'),np.array([1,2,3]),np.array([10,20,30]),np.array([.2,.3,.4]),
        np.zeros((3,3)),np.zeros(3),np.array([.04,.07,.1]),0,0,'LAGGED_COMPLETED_ITERATION_RAW'))
    np.testing.assert_allclose(result.destination_private_productive_capital,[32,47,61])
    np.testing.assert_allclose(result.household_portfolio_return_by_origin,[.049,.07,.082])
    assert sum(result.destination_private_productive_capital) == pytest.approx(140)


def test_one_turn_previous_firm_labor_fiscal_and_no_c1():
    f=fixture(); states=mainline_initial_states(f); hh=batch(f)
    result=run_mainline_one_turn(states,hh,f)
    for i,(old,new,firm,row) in enumerate(zip(states,result['states'],result['firms'],result['fiscal']['provinces'])):
        assert new['Lt_firm_previous'] == old['Lt_prev']
        assert new['Lt_prev'] == firm.Lt
        assert new['Lt_HA'] == hh.household_lt[i]
        assert new['GovInv'] == old['GovInv']
        assert firm.Kt == pytest.approx(result['capital'].destination_private_productive_capital[i]+old['GovInv'])
        assert row['wage_tax'] == pytest.approx(old['tau']*firm.wt0*firm.Lt)
        expected=firm.Corptax+old['tau']*firm.wt0*firm.Lt+old['N']*hh.at_tax[i]+old['GovInv']*firm.ra-old['N']*old['Tt']
        assert firm.Govinc == pytest.approx(expected)
        # Independent lagged-NKPC expression; household Lt must not enter it.
        k=firm.Kt; l=firm.Lt; alpha=old['alpha']
        mt=((old['rk']-(old['Zt_1']-old['Zt'])/old['Zt']-alpha*(old['Kt_prev']-k)/k
             -(1-alpha)*(old['Lt_prev']-l)/l)*old['pit']*10+.9-(old['pit']-old['pit_1'])*10)
        assert firm.mt == pytest.approx(mt)
    np.testing.assert_allclose(result['raw_next_payoff'],
        np.array([x.ra0 for x in result['firms']]) @ result['shares'])
    assert result['fiscal']['budget_zero_imposed'] is False


def test_incomplete_household_gate_rejected():
    f=fixture()
    with pytest.raises(ValueError,match='HJB/KFE'):
        run_mainline_one_turn(mainline_initial_states(f),batch(f,False),f)


def test_entering_HA_payoff_binds_current_quantity_S_with_lagged_return():
    f=fixture(); states=mainline_initial_states(f)
    prepared=prepare_mainline_household_states(states,f)
    turn=run_mainline_one_turn(prepared,batch(f),f)
    expected=np.asarray(f['initial_lagged_raw_ra0_by_destination']) @ turn['shares']
    np.testing.assert_allclose([s['rah'] for s in prepared],expected,rtol=0,atol=1e-15)
    assert states[0]['rah'] == f['initial_household_rah'][0]  # no mutation of binding input
