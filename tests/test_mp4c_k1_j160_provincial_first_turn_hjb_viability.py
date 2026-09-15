from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from validators.multi_province.k1_j160_provincial_first_turn_hjb_viability import (
    finalize,
    run,
)


def test_authority_recovers_exact_sealed_turn1_vector() -> None:
    receipt = run.load_first_turn_authority()
    rows = receipt["provinces"]
    assert receipt["pass"] is True
    assert len(rows) == 31
    assert [row["province_index"] for row in rows] == list(range(31))
    assert len({row["province"] for row in rows}) == 31
    assert all(row["provenance_checks_pass"] for row in rows)
    assert all(row["r_b"] == pytest.approx(0.02) for row in rows)
    assert all(row["tau"] == pytest.approx(0.05) for row in rows)
    assert all(row["transfer_income"] == pytest.approx(0.1) for row in rows)
    assert all(row["borrowing_rate_gap"] == pytest.approx(0.07) for row in rows)
    assert receipt["accepted_identity_receipts_sha256"] == run.ACCEPTED_IDENTITY_SHA256
    assert receipt["manifest_entry_matches_identity_artifact"] is True


def test_fixture_is_frozen_j160_and_fresh_per_province() -> None:
    rows = run.load_first_turn_authority()["provinces"][:2]
    fixtures = [run.build_fixture(row) for row in rows]
    for row, fixture in zip(rows, fixtures):
        assert fixture.grid.b.shape == (20,)
        assert fixture.grid.a.shape == (160,)
        assert (fixture.grid.b[0], fixture.grid.b[-1]) == pytest.approx((-2.0, 20.0))
        assert (fixture.grid.a[0], fixture.grid.a[-1]) == pytest.approx((0.0, 100.0))
        assert fixture.inputs.r_a == pytest.approx(row["consumed_r_a"])
        assert fixture.inputs.r_b == pytest.approx(row["r_b"])
        assert float(fixture.inputs.wages[0]) == pytest.approx(row["household_composite_wage"])
        assert fixture.transfer_income == pytest.approx(row["transfer_income"])
        assert fixture.borrowing_rate_gap == pytest.approx(row["borrowing_rate_gap"])
        assert fixture.numerics.delta == pytest.approx(1000.0)
        assert fixture.numerics.convergence_tolerance == pytest.approx(1e-7)
        assert fixture.numerics.max_iterations == 100
        assert np.isfinite(fixture.initial_value).all()
        assert np.isfinite(fixture.baseline_labor).all()
    assert fixtures[0].initial_value is not fixtures[1].initial_value
    assert fixtures[0].baseline_labor is not fixtures[1].baseline_labor


def test_mutated_or_incomplete_authority_fails_closed(tmp_path: Path) -> None:
    payload = json.loads(run.ACCEPTED_IDENTITY_PATH.read_text(encoding="utf-8"))
    path = tmp_path / "identity_receipts.json"
    path.write_text(json.dumps(payload[1:], ensure_ascii=False), encoding="utf-8")
    with pytest.raises(ValueError, match="FIRST_TURN_PROVINCIAL_INPUT_AUTHORITY_BLOCKER"):
        run.load_first_turn_authority(path, enforce_seal=False)


def test_call_ledger_has_exact_budget_and_all_forbidden_routes_zero() -> None:
    ledger = run.empty_call_ledger()
    assert ledger["hjb_budget"] == 31
    assert ledger["kfe_budget"] == 0
    assert ledger["scientific_retries"] == 0
    assert ledger["engineering_retry_budget"] == 1
    assert all(ledger[key] == 0 for key in run.FORBIDDEN_LEDGER_KEYS)


def test_support_comparison_is_descriptive_and_frozen() -> None:
    assert finalize.support_location(0.06, 13.0) == "ON_ACCEPTED_J160_BOUNDARY"
    assert finalize.support_location(0.0675, 15.5) == "INSIDE_ACCEPTED_J160_RECTANGLE"
    assert finalize.support_location(0.07, 18.0) == "ON_ACCEPTED_J160_BOUNDARY"
    assert finalize.support_location(0.08, 18.5) == "OUTSIDE_ACCEPTED_J160_RECTANGLE"


def test_terminal_requires_all_31_legal_and_converged() -> None:
    good = [{"hjb": {"classification": "HJB_CONVERGED"}} for _ in range(31)]
    assert finalize.terminal_classification(good) == "J160_FIRST_TURN_PROVINCIAL_HJB_VIABILITY_PASS"
    bad = [*good[:-1], {"hjb": {"classification": "HJB_NOT_CONVERGED"}}]
    assert finalize.terminal_classification(bad) == "J160_FIRST_TURN_PROVINCIAL_HJB_VIABILITY_BLOCKED"
    with pytest.raises(ValueError, match="31"):
        finalize.terminal_classification(good[:-1])
