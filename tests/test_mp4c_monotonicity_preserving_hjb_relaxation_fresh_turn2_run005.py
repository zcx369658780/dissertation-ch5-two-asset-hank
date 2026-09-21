from pathlib import Path

from validators.multi_province.monotonicity_preserving_hjb_relaxation_fresh_turn2_run005 import run


REPO = Path(__file__).resolve().parents[1]


def test_preflight_binds_live_main_sources_and_entering_state():
    receipt = run.preflight(REPO)
    assert receipt["status"] == "PASS"
    assert all(receipt["checks"].values())


def test_runtime_contract_constants_are_exact():
    assert run.ENTERING_BLOB == "85df3f0bdcc3b0bb3e7b12f0ba35dbb9abda764d"
    assert run.ENTERING_SHA256 == "E519E468B04D7EDC631F6A931FF367A7EDE5C3D510ED4E0979AB2FC8E13C5E11"
    assert run.ENTERING_PAYOFF_SHA256 == "D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414"
    assert run.HLJ_EXPECTED[2]["alpha"] == 0.5
    assert run.HLJ_EXPECTED[2]["accepted"] == "987A20DE9252104ECFAB59436433F0C73EEB8C513589B8B0FA98DB64018B66BF"


def test_relaxation_ledger_starts_at_zero():
    ledger = run.new_relaxation_ledger()
    assert ledger["helper_invocations"] == 0
    assert ledger["alpha_candidates_evaluated"] == 0
    assert ledger["relaxed_updates_alpha_lt_1"] == 0
