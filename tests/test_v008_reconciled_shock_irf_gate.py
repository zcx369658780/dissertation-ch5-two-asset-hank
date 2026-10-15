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

import json
import os
d=importlib.import_module("v008.reconciled_shock_diagnostic")
s=importlib.import_module("v008.reconciled_stationary")
gate=importlib.import_module("v008.reconciled_irf_gate")

@pytest.mark.skipif(os.environ.get("V008_RUN_PATHS")!="1",reason="four frozen paths already consumed; no rerun")
def test_four_real_conditional_paths():
    directory=Path(os.environ["V008_LEDGER_DIR"])
    baseline=json.loads((directory/"root_001.json").read_text())
    case=s.artificial_case(1)
    zero=d.shock_path(case,baseline,40,0)
    full=d.shock_path(case,baseline,40,1e-4)
    half=d.shock_path(case,baseline,40,5e-5)
    prefix=d.shock_path(case,baseline,20,1e-4)
    comparison=d.compare_paths(zero,full,half,prefix,baseline)
    with (directory/"path_comparison.json").open("x",encoding="utf-8") as f:
        json.dump(comparison,f,indent=2)
    assert comparison["success"], comparison
    assert full["exogenous_states"][0][0]>0
    assert full["exogenous_states"][10][1]>0
    assert full["exogenous_states"][20][2]>0

def test_irf_blocked_and_baseline_rejection():
    r=gate.irf_gate()
    assert r["status"]=="IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE"
    assert len(r["missing"])==8 and not r["dynamic_execution_authorized"]
    assert gate.irf_gate({k:True for k in gate.REQUIRED})["missing"]==list(gate.REQUIRED)
    with pytest.raises(ValueError): d.require_baseline(dict(success=False))

def test_saved_path_public_capital_financing_bridge():
    directory=Path(os.environ["V008_LEDGER_DIR"])
    if not (directory/"path_006.json").exists():
        pytest.skip("requires completed, budgeted Gate C receipts")
    path=json.loads((directory/"path_006.json").read_text())
    rows=d.public_capital_endowment_bridge(s.artificial_case(1),path)
    assert rows[20]["in_kind_grant"]>0
    assert rows[21]["in_kind_grant"]<0
    assert all(row["cash_grant"]==0 for row in rows)
    assert max(abs(row["resource_with_grant_residual"]) for row in rows)<5e-11
    assert all(row["government_asset_change"]+row["external_donor_asset_change"]==0 for row in rows)
    with (directory/"public_capital_financing_bridge.json").open("x",encoding="utf-8") as file:
        json.dump(rows,file,indent=2)
