import importlib, sys, types
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"src/ch5_two_asset_hank/reconciled_hank"
if "v009" not in sys.modules:
    pkg=types.ModuleType("v009"); pkg.__path__=[str(P)]; sys.modules["v009"]=pkg

import numpy as np
import pytest
from scipy import sparse
from v009.contracts import Ledger
from v009.stationary_kfe import stationary_mass
from v009.household import pure
def test_known_closed_class_and_exact_zero_transient():
    q=sparse.csr_matrix([[-2.,2.,0.],[1.,-1.,0.],[0.,3.,-3.]])
    p,d=stationary_mass(q,Ledger(),toy=True)
    assert p==pytest.approx([1/3,2/3,0.],abs=1e-14)
    assert p[2].view(np.uint64)==0
    assert d["closed_size"]==2 and d["rank"]==1
def test_reject_invalid_and_multiple_closed_classes():
    for q in [np.zeros((3,3)),np.array([[-1.,2.],[1.,-1.]]),
              np.array([[1.,-1.],[1.,-1.]])]:
        with pytest.raises(RuntimeError): stationary_mass(sparse.csr_matrix(q),Ledger(),toy=True)
def test_consumed_coordinate_actions_and_boundary():
    g=pure("contracts").CorrectedDiagnosticGrid(np.array([0.,1.]),np.array([0.,1.]),np.array([.8,1.2]))
    b=np.broadcast_to(g.b[:,None,None],g.shape); a=np.broadcast_to(g.a[None,:,None],g.shape)
    gb=1-2*b; ga=1-2*a
    Q=pure("generator").assemble_consumed_drift_generator(g,mu_b=gb,mu_a=ga,
        z_generator=np.array([[-1.,1.],[1.,-1.]])).q
    assert Q@b.ravel(order="F")==pytest.approx(gb.ravel(order="F"))
    assert Q@a.ravel(order="F")==pytest.approx(ga.ravel(order="F"))
    assert Q@np.ones(8)==pytest.approx(np.zeros(8))
    with pytest.raises(ValueError):
        pure("generator").assemble_consumed_drift_generator(g,mu_b=np.ones(g.shape),mu_a=ga)
