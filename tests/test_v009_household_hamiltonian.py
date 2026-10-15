import importlib, sys, types
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"src/ch5_two_asset_hank/reconciled_hank"
if "v009" not in sys.modules:
    pkg=types.ModuleType("v009"); pkg.__path__=[str(P)]; sys.modules["v009"]=pkg

import numpy as np
import pytest
from v009.contracts import case, grid, calibration_hash, Ledger
from v009.household import local_policy, derivatives
from v009.accounts import labor,positive_prices
def test_grid_and_frozen_manifest():
    g=grid(); assert g.shape==(20,20,2)
    assert np.ravel_multi_index((3,4,1),g.shape,order="F")==483
    V=-1/(.05*(1+g.b[:,None,None]+g.a[None,:,None]+g.z[None,None,:]))
    assert np.all(derivatives(V,g)[0]>0)
    assert calibration_hash(case(1))==calibration_hash(case(1))
    with pytest.raises(ValueError): case(31)
def test_interior_hamiltonian_and_kink():
    # q_b=1, q_a=1 implies d=0, c=1, ell=(1.9)^(1/5).
    p=local_policy(b=.5,a=1.,z=1.,W=1.9,ra=.04,rb=.02,T=0.,
        pbB=1.,pbF=1.,paB=1.,paF=1.,kappa=1.,ledger=Ledger())
    assert p["c"]==pytest.approx(1.)
    assert p["l"]==pytest.approx(1.9**.2)
    assert p["d"]==pytest.approx(0.)
    assert p["g_a"]==pytest.approx(.04)
    assert p["g_b"]==pytest.approx(1.9*p["l"]+.01-1.)
    assert p["utility"]==pytest.approx(-1.-p["l"]**6/6)
    with pytest.raises(RuntimeError):
        local_policy(b=.5,a=1.,z=1.,W=1.,ra=.04,rb=.02,T=0.,
            pbB=-1.,pbF=-1.,paB=1.,paF=1.,kappa=1.,ledger=Ledger())
def test_ces_duality_and_population():
    c=dict(case(2),phi=((1.,1.4),(1.2,1.))); w=np.array([1.,1.7]); ell=[np.array([.4,.8]),np.array([.7,.3])]
    mu=[np.array([.25,.75]),np.array([.6,.4])]; z=np.array([.8,1.2])
    W,h,L= labor(c,w,ell,mu,z)
    for i in range(2):
        assert np.sum(np.array(c["phi"])[:,i,None]*h[i]**2,axis=0)==pytest.approx(ell[i]**2)
        assert np.sum((.95*w)[:,None]*h[i],axis=0)==pytest.approx(W[i]*ell[i])
    cc=dict(c,N=(2.,2.2)); _,_,LL=labor(cc,w,ell,mu,z)
    assert LL==pytest.approx(2*L)
    with pytest.raises(ValueError): labor(c,w,ell,[np.array([-.1,1.1]),mu[1]],z)
    with pytest.raises(ValueError): positive_prices(c,w,wage_role="net_already_taxed")
    with pytest.raises(ValueError): positive_prices(c,w,units=("yuan","person","annual"))
def test_negative_transfer_kkt_independent_oracle():
    # Independent D3 derivative: q_a/q_b=1-.1+2*d/a=-.5 => d=-.7.
    p=local_policy(b=.5,a=1.,z=1.,W=1.9,ra=.04,rb=.02,T=0.,
        pbB=1.,pbF=1.,paB=-.5,paF=-.5,kappa=1.,ledger=Ledger())
    assert p["d"]==pytest.approx(-.7)
    assert p["cost"]==pytest.approx(.1*.7+2*.7**2/2)
    assert p["q_a"]-p["q_b"]*(1-.1+2*p["d"])==pytest.approx(0.,abs=1e-14)
