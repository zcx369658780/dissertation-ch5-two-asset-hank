import importlib, sys, types
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"src/ch5_two_asset_hank/reconciled_hank"
if "v009" not in sys.modules:
    pkg=types.ModuleType("v009"); pkg.__path__=[str(P)]; sys.modules["v009"]=pkg

import pytest
from v009.stationary import acceptance, irf_missing
from v009.contracts import Ledger,case
from v009.accounts import positive_prices
def test_missing_frozen_phi_stops_before_any_scientific_reservation():
    ledger=Ledger();before=dict(ledger.data["totals"])
    for n in (1,2):
        assert case(n)["phi"] is None
        with pytest.raises(ValueError,match="FROZEN_CES_PHI_NOT_SPECIFIED"):
            positive_prices(case(n),[1.]*n)
    assert ledger.data["totals"]==before
def test_no_metadata_steady_state_or_irf_pass():
    with pytest.raises((ValueError,KeyError)): acceptance({"success":True})
    assert irf_missing()["status"]=="IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE"
def test_corrupted_saved_gate_cannot_pass():
    # An account identity cannot replace converged household and mass evidence.
    with pytest.raises((ValueError,KeyError)):
        acceptance({"households":[],"residuals":[0.],"accounting":[0.]})
