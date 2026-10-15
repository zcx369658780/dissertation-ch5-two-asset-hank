import numpy as np
import pytest
from ch5_two_asset_hank.multi_province.steady_state import _adapt,mainline_outer_diagnostics


def state(ra):
    return dict(name='A',Zt=2,GovInv=100,Yt=100,Yt0=100,Kt=10,Lt=5,alpha=.6,
                ra=ra,ramin=.02,ramax=.09,Yt_1=100,KNratio=2,convergent=True)


@pytest.mark.parametrize('ra,factor',[(.02,.9),(.09,1.1),(.055,1)])
def test_original_govinv_boundary(ra,factor):
    new,actions=_adapt([state(ra)],.01,True)
    assert new[0]['GovInv'] == pytest.approx(100*factor)
    assert actions[0].govinv_before == 100


@pytest.mark.parametrize('gap,calibrate',[(.1,True),(.01,False)])
def test_adapt_gate_is_strict(gap,calibrate):
    new,_=_adapt([state(.02)],gap,calibrate)
    assert new[0]['GovInv'] == 100


def test_zt_update_then_govinv_no_c1():
    s=state(.09);s['Yt']=130
    new,_=_adapt([s],.01,True)
    assert new[0]['Zt'] == pytest.approx(100*10**(-.6)*5**(-.4))
    assert new[0]['GovInv'] == pytest.approx(110)


def test_outer_convergence_does_not_certify_target():
    s=state(.055);s['Yt0']=50
    result=mainline_outer_diagnostics([s],np.array([2.]))
    assert result['OUTER_ITERATION_CONVERGED']
    assert result['target_gap'] == [1]
    assert result['TARGET_CALIBRATION_VERIFIED'] is False


def test_return_boundary_veto():
    assert not mainline_outer_diagnostics([state(.09)],np.array([2.]))['OUTER_ITERATION_CONVERGED']
