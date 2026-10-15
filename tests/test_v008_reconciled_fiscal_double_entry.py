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

f=importlib.import_module("v008.reconciled_fiscal")
p=importlib.import_module("v008.reconciled_household_prices")

@pytest.mark.parametrize("owner",["resource","intermediary","government_fee"])
def test_positive_mobility_double_entry(owner):
    j=f.Journal()
    assert f.record_wage(j,200,.15,.1,owner)==pytest.approx(150)
    assert sum(j.balances().values())==pytest.approx(0)
    assert j.balances()["government"]==pytest.approx(50 if owner=="government_fee" else 30)
    assert p.net_prices([2],.15,[[.1]],owner)==[[1.5]]

@pytest.mark.parametrize("owner",["government","intermediary","resource"])
def test_gap_exclusive_scenarios(owner):
    j=f.Journal(); f.record_asset_gap(j,3,owner)
    assert j.balances()[owner]==3
    with pytest.raises(ValueError): f.record_asset_gap(j,3,owner,recipients=["government","intermediary"])

def test_ownership_duplicate_clip_and_transfer():
    assert f.capital_claims(10,8,2,.2)==pytest.approx((1.6,.4))
    with pytest.raises(ValueError): f.capital_claims(10,8,2,.2,claimed=(1.6,1.2))
    with pytest.raises(ValueError): f.capital_claims(10,8,2,.2,used_return=.1)
    with pytest.raises(ValueError): f.capital_claims(10,10,2,.2)
    assert f.transfer_total([2,7],[.1,.3])==pytest.approx(2.3)
    with pytest.raises(ValueError): f.government_interest(2,.1,"unknown_bank")
    j=f.Journal()
    with pytest.raises(ValueError): f.record_asset_gap(j,1)

def test_provincial_analysis_has_one_national_account():
    case=dict(scenario="SYNTHETIC_SCENARIO",n=2,N=[2,7],tax=.1,markup=.9,
        corporate_tax=.2,Kg=[1,2],rb=.01,G_share=.08,
        mu=[[dict(p=1,b=.1)],[dict(p=1,b=.3)]])
    result=dict(w=[2,3],L=[4,5],Y=[10,20],returns=[.2,.3],transfer=.1)
    rows=f.provincial_analysis(case,result)
    assert rows[0]["resident_transfer"]==pytest.approx(.2)
    assert rows[1]["resident_transfer"]==pytest.approx(.7)
    assert rows[1]["wage_tax"]==pytest.approx(1.5)
    assert sum(r["net_contribution"] for r in rows)==pytest.approx(
        2.3+.6+.8-.9-.023-2.4)
