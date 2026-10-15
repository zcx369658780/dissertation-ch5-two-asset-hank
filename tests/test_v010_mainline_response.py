import math
import pytest
from ch5_two_asset_hank.multi_province.mainline_response import run_mainline_response


def test_response_requires_verified_baseline():
    with pytest.raises(ValueError):
        run_mainline_response({}, {'status':'OUTER_ITERATION_CONVERGED'},None)


@pytest.mark.parametrize('zero',[True,False])
def test_recursive_reset_and_carry_without_calibration(zero):
    baseline=tuple(dict(name=n,Zt=2.,GovInv=10.,tau=.1,corptau=.2,Yt=100.,Ct=5.,Kt=20.,Lt=3.,carry=0)
                   for n in ('A','B'))
    seen=[]
    def solver(states,stage):
        seen.append((states,stage));return 'STUB_NO_HA'
    def turn(states,batch,fixture):
        assert batch == 'STUB_NO_HA'
        assert all(s['GovInv']==10 and s['tau']==.1 and s['corptau']==.2 for s in states)
        return {'states':tuple(dict(s,carry=s['carry']+1,GovInv=999) for s in states)}
    out=run_mainline_response({'response':{'periods':3}},
        {'status':'TARGET_CALIBRATION_VERIFIED','states':baseline},solver,zero=zero,turn_function=turn)
    for t,(states,stage) in enumerate(seen,1):
        assert states[0]['Zt'] == pytest.approx(2*(1+(0 if zero else .01*math.exp(-.5*(t-1)))))
        assert states[1]['Zt'] == 2
        assert states[0]['carry'] == t-1
    assert out['outer_recalibration'] is False and out['lagged_NKPC'] is True
