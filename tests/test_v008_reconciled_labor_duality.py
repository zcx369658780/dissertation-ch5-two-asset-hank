import importlib
import sys
import types
from pathlib import Path
import pytest
BASE=Path(__file__).resolve().parents[1]/"src/ch5_two_asset_hank/multi_province"
if "v008" not in sys.modules:
    pkg=types.ModuleType("v008")
    pkg.__path__=[str(BASE)]
    sys.modules["v008"]=pkg

from math import sqrt
prices=importlib.import_module("v008.reconciled_household_prices")
labor=importlib.import_module("v008.reconciled_labor")

@pytest.mark.parametrize("n",[1,2,31])
@pytest.mark.parametrize("tax",[0,.17])
def test_duality_and_integrated_income(n,tax):
    w=[.7+.03*j for j in range(n)]
    phi=[[1+.01*(2*j+i) for i in range(n)] for j in range(n)]
    v=prices.net_prices(w,tax,[[0]*n for _ in range(n)])
    W=labor.dual_wages(v,phi,2)
    mu=[[dict(p=.25,z=.7),dict(p=.75,z=1.3)] for _ in range(n)]
    ell=[[.4+.01*i,1.1+.01*i] for i in range(n)]
    pop=[2+i for i in range(n)]
    flows,L=labor.integrate_distribution(pop,mu,ell,v,phi,2)
    for i in range(n):
        for l in ell[i]:
            h=labor.bilateral_controls(l,i,v,phi,2)
            assert sum(phi[j][i]*h[j]**3 for j in range(n)) == pytest.approx(l**3,rel=2e-12)
            assert sum(v[j][i]*h[j] for j in range(n)) == pytest.approx(W[i]*l,rel=2e-12)
        assert sum(v[j][i]*flows[j][i] for j in range(n)) == pytest.approx(
            pop[i]*W[i]*sum(s["p"]*s["z"]*l for s,l in zip(mu[i],ell[i])),rel=2e-12)
    assert L==pytest.approx([sum(row) for row in flows])

def test_independent_quadratic_primal_oracle():
    v=[[1,2],[3,4]]; phi=[[1,2],[4,1]]
    W=labor.dual_wages(v,phi,1)
    assert W==pytest.approx([sqrt(1+9/4),sqrt(4/2+16)])
    W2=labor.dual_wages([[1,1],[1,1]],[[1,1],[1,1]],1)
    h=labor.bilateral_controls(1,0,[[1,1],[1,1]],[[1,1],[1,1]],1,W2)
    assert h==pytest.approx([1/sqrt(2)]*2)
    assert sum(h)!=pytest.approx(1)

def test_direction_scaling_jensen_and_foc_units():
    v=[[1,2],[4,3]]; phi=[[1,1.2],[1.1,1]]
    mu=[[dict(p=.5,z=.8),dict(p=.5,z=1.2)]]*2
    f,L=labor.integrate_distribution([2,7],mu,[[1,2],[2,1]],v,phi,1)
    f2,L2=labor.integrate_distribution([4,14],mu,[[1,2],[2,1]],v,phi,1)
    assert L2==pytest.approx([2*x for x in L])
    assert f[0][1]!=f[1][0]
    assert .5/1+.5/3 > 1/(.5*1+.5*3)
    k=prices.rescale_labor_weight(3,7,2)
    assert (1/2**2)*4/3 == pytest.approx((1/(7*2)**2)*(7*4)/k)

def test_bad_prices_and_double_tax_rejected():
    with pytest.raises(ValueError): prices.net_prices([1],.1,[[.2]])
    with pytest.raises(ValueError): prices.net_prices([1],.1,[[0]],units=("yuan","people","annual"))
    with pytest.raises(ValueError): prices.check_income(1,.81,.1,0)
    with pytest.raises(ValueError): labor.dual_wages([[1]],[[0]],1)

def test_labor_reference_refuses_mean_or_iteration():
    args=dict(previous_role="household_mean",current_role="destination_total",
        previous_unit="H",current_unit="NU*H",previous_axis="origin_0",current_axis="destination_0",
        previous_time="iteration_k_minus_1",current_time="economic_t")
    with pytest.raises(ValueError): labor.comparable_labor_reference(1,100,**args)
