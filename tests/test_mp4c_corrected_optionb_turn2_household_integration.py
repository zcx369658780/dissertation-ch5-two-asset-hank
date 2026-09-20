from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import pytest

from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import FailClosed
from ch5_two_asset_hank.corrected_diagnostic.optionb_turn2_household_integration import (
    ENTERING_STATE_RELATIVE,
    EXPECTED_ENTERING_PAYOFF_SHA256,
    EXPECTED_ENTERING_STATE_BLOB,
    EXPECTED_HOUSEHOLD_MANIFEST_SHA256,
    EXPECTED_INTEGRATION_MANIFEST_SHA256,
    _blob,
    _check_ledger,
    _movement_diagnostics,
    _new_ledger,
    _verify_sealed_manifest,
    load_initial_states,
    same_s_raw_next_payoff,
)
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER


REPOSITORY = Path(__file__).resolve().parents[1]


def test_exact_entering_turn2_state_binding_and_order() -> None:
    states, receipt = load_initial_states(REPOSITORY)
    assert _blob(REPOSITORY, ENTERING_STATE_RELATIVE) == EXPECTED_ENTERING_STATE_BLOB
    assert receipt["status"] == "PASS"
    assert receipt["raw_next_payoff_sha256"] == EXPECTED_ENTERING_PAYOFF_SHA256
    assert receipt["row_count"] == 31
    assert tuple(state["name"] for state in states) == PROVINCE_ORDER
    assert all(all(row["checks"].values()) for row in receipt["rows"])


def test_both_accepted_predecessor_manifests_read_back_exactly() -> None:
    integration = _verify_sealed_manifest(
        REPOSITORY / ENTERING_STATE_RELATIVE.parent,
        EXPECTED_INTEGRATION_MANIFEST_SHA256,
        17,
    )
    household = _verify_sealed_manifest(
        REPOSITORY
        / "reports/ch5_mp4c_corrected_optionb_initial_turn_unique_closed_class_kfe_20260920_run004",
        EXPECTED_HOUSEHOLD_MANIFEST_SHA256,
        4353,
    )
    assert integration["status"] == household["status"] == "PASS"


def test_canonical_payoff_is_ordered_math_fsum() -> None:
    raw = np.linspace(0.1, 3.1, 31, dtype=np.float64)
    shares = np.arange(1, 31 * 31 + 1, dtype=np.float64).reshape(31, 31)
    shares /= shares.sum(axis=0)
    actual = same_s_raw_next_payoff(raw, shares)
    expected = np.asarray([
        math.fsum(float(raw[j]) * float(shares[j, i]) for j in range(31))
        for i in range(31)
    ])
    assert np.array_equal(actual, expected)


def test_canonical_payoff_rejects_wrong_axes_or_nonfinite() -> None:
    with pytest.raises(ValueError):
        same_s_raw_next_payoff(np.ones(30), np.eye(31))
    shares = np.eye(31)
    shares[0, 0] = np.nan
    with pytest.raises(ValueError):
        same_s_raw_next_payoff(np.ones(31), shares)


def test_movement_diagnostics_use_fixed_entering_denominator() -> None:
    old = tuple({
        "rah": 0.0, "w": 2.0, "rb": 0.02, "Ct": 1.0, "At": 2.0,
        "Bt": 3.0, "AtTax": 4.0, "Kt": 5.0, "Yt": 6.0,
        "GovInv": 7.0, "ra0": 8.0,
    } for _ in range(31))
    rows = [{"state": dict(old[i], rah=float(i + 1))} for i in range(31)]
    result = _movement_diagnostics(old, rows, np.arange(31, dtype=float))
    assert result["relative_denominator"] == "max(abs(entering_value),1e-12)"
    assert result["classification"] == "DESCRIPTIVE_ONLY__NOT_OUTER_CONVERGENCE"
    assert result["fields"]["rah"]["max_absolute_change_province_index"] == 30
    assert result["fields"]["rah"]["max_relative_change"] == pytest.approx(31e12)


def test_turn2_scientific_ledger_limits_and_turn3_zero() -> None:
    ledger = _new_ledger()
    ledger.update(
        source_native_initializations=31,
        scalar_labor_roots_attempted=24_800,
        scalar_labor_roots_returned=24_800,
        corrected_policy_maps=1_581,
        selector_evaluations=1_264_800,
        d2_q_assemblies=1_581,
        direct_hjb_updates=1_550,
        hjb_checkpoint_evaluations_after_update=1_550,
        scc_decompositions=31,
        restricted_dense_scipy_linalg_svd_gesvd=31,
        normalized_stationary_candidates=31,
        q_transpose_times_p=31,
        corrected_aggregate_evaluations=31,
    )
    _check_ledger(ledger)
    assert ledger["turn3_household_calls"] == 0
    assert ledger["third_outer_turns"] == 0
    ledger["direct_hjb_updates"] += 1
    with pytest.raises(FailClosed):
        _check_ledger(ledger)
