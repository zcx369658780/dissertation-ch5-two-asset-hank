import importlib, sys, types
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"src/ch5_two_asset_hank/reconciled_hank"
if "v009" not in sys.modules:
    pkg=types.ModuleType("v009"); pkg.__path__=[str(P)]; sys.modules["v009"]=pkg

import pytest
from v009.stationary import acceptance, irf_missing
from v009.contracts import Ledger,case,dominant_snapshot
from v009.accounts import positive_prices
def test_missing_frozen_phi_stops_before_any_scientific_reservation():
    ledger=Ledger();before=dict(ledger.data["totals"])
    for n in (1,2):
        missing=dict(case(n),phi=None)
        with pytest.raises(ValueError,match="FROZEN_CES_PHI_NOT_SPECIFIED"):
            positive_prices(missing,[1.]*n)
    assert ledger.data["totals"]==before
def test_frozen_phi_B_source_destination_and_external_reference():
    c=case(2);p=c["phi"];ref=c["pgdp_ref"]
    assert ref==(1.,2.) and c["max_phi"]==.3
    assert case(1)["phi"]==((1.,),)
    assert p[1][0]==.9 and p[0][1]==1.1 and p[0][0]==p[1][1]==1.
    for j in range(2):
        for i in range(2):
            assert p[j][i]==pytest.approx(1+.3*(ref[i]-ref[j])/(ref[i]+ref[j]))
    # Richer destination has lower disutility; columns are NOT normalized.
    assert p[1][0]<p[0][0] and p[0][1]>p[1][1]
    assert sum(row[0] for row in p)==pytest.approx(1.9)
    assert sum(row[1] for row in p)==pytest.approx(2.1)
    c["Y"]=(1000.,1.);c["N"]=(2.,3.)
    assert c["phi"]==case(2)["phi"]
def test_ledger_recovery_keeps_higher_calls_and_rejects_conflicting_snapshots():
    a=dict(started=1.,households={},macros={},totals=dict(selector_root=8,scalar_root=2))
    b=dict(a,totals=dict(selector_root=8,scalar_root=3))
    assert dominant_snapshot([a,b])["totals"]["scalar_root"]==3
    conflict=dict(a,totals=dict(selector_root=9,scalar_root=1))
    with pytest.raises(RuntimeError,match="NONMONOTONE"):
        dominant_snapshot([b,conflict])
def test_no_metadata_steady_state_or_irf_pass():
    with pytest.raises((ValueError,KeyError)): acceptance({"success":True})
    assert irf_missing()["status"]=="IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE"
def test_corrupted_saved_gate_cannot_pass():
    # An account identity cannot replace converged household and mass evidence.
    with pytest.raises((ValueError,KeyError)):
        acceptance({"households":[],"residuals":[0.],"accounting":[0.]})
