import importlib, sys, types
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"src/ch5_two_asset_hank/reconciled_hank"
if "v009" not in sys.modules:
    pkg=types.ModuleType("v009"); pkg.__path__=[str(P)]; sys.modules["v009"]=pkg

import numpy as np
import pytest
from v009.accounts import capital_flows, fiscal_accounts, check_funding
from v009.contracts import case
def test_cross_province_R_paper_oracle():
    # Exact Astra paper counterexample: A=(100,100), r=(.1,.2), D=0.
    f=capital_flows([[.8,.2],[.2,.8]],[100.,100.],[.1,.2],[0.,0.],.1)
    assert f["rah"]==pytest.approx([.12,.18])
    assert f["R"]==pytest.approx([3.2,-3.2])
    assert f["dotK"]==pytest.approx([13.2,16.8],abs=1e-14)
    assert sum(f["R"])==pytest.approx(0.)
    with pytest.raises(ValueError): check_funding(f,np.array(f["Iprivate"])-f["R"])
def test_public_gross_rent_maintenance_and_signed_transfer():
    c=case(1); f=fiscal_accounts(c,[1.],[2.],[.04],.02,-.1)
    assert f["public_gross"]==pytest.approx(.028)
    assert f["public_maintenance"]==pytest.approx(.02)
    assert f["budget"]==pytest.approx(.1+.008-.06-.008+.1)
    with pytest.raises(ValueError): fiscal_accounts(c,[1.],[2.],[.04],.02,0.,maintenance=.04)
def test_capital_rejects_axis_and_nonconservation():
    with pytest.raises(ValueError): capital_flows([[.8,.3],[.2,.8]],[1.,2.],[.1,.2],[0.,0.],.1)
    with pytest.raises(ValueError): capital_flows([[1.]],[1.],[-.2],[0.],.1)
