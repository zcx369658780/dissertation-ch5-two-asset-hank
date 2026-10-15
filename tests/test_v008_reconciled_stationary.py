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

import os
s=importlib.import_module("v008.reconciled_stationary")

@pytest.mark.parametrize("n",[1,2,31])
def test_numeric_conditional_equilibrium(n):
    case=s.artificial_case(n)
    result=s.solve_stationary(case)
    assert result["success"], {k:result[k] for k in ("stop_reason","max_scaled_residual","evaluations")}
    assert result["max_scaled_residual"]<=1e-8
    assert result["max_accounting_residual"]<=5e-11
    assert result["evaluations"]<=200
    assert result["qualification"]=="SYNTHETIC_CONDITIONAL_STATIONARY"
    assert result["initial_vector"]!=result["solution_vector"]
    assert len(result["solution_vector"][0])==n+1
    r=result["results"][0]
    assert max(abs(x) for x in r["sector_balances"].values())/max(1,sum(r["Y"]))<5e-11
    assert all(c>0 for row in r["c"] for c in row)
    fiscal=importlib.import_module("v008.reconciled_fiscal")
    rows=fiscal.provincial_analysis(case,r)
    assert abs(sum(row["net_contribution"] for row in rows))/max(1,sum(r["Y"]))<5e-11
    import json
    out=Path(os.environ["V008_LEDGER_DIR"])/f"provincial_root_{result['attempt']:03d}.json"
    with out.open("x",encoding="utf-8") as stream:
        json.dump(rows,stream,indent=2)

def test_given_assets_are_not_HANK_and_bad_real_config_rejected():
    case=s.artificial_case(2)
    case["asset_gap"]=.1
    with pytest.raises(ValueError): s.evaluate(case,[0,0,.1])
