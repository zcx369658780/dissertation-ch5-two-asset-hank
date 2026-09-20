from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import FailClosed
from ch5_two_asset_hank.corrected_diagnostic.optionb_initial_turn_integration import (
    EXPECTED_C1_BLOB,
    EXPECTED_INITIALIZATION_BLOB,
    EXPECTED_K1A_BLOB,
    EXPECTED_SOURCE_INITIALIZATION_BLOB,
    INITIALIZATION_RELATIVE,
    _blob,
    _check_ledger,
    _new_ledger,
    load_initial_states,
    same_s_raw_next_payoff,
)
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER


REPOSITORY = Path(__file__).resolve().parents[1]


def test_exact_initialization_binding_and_state_order() -> None:
    states, receipt = load_initial_states(REPOSITORY)
    assert receipt["status"] == "PASS"
    assert receipt["git_blob"] == EXPECTED_INITIALIZATION_BLOB
    assert receipt["row_count"] == 31
    assert tuple(state["name"] for state in states) == PROVINCE_ORDER
    assert [row["province_index"] for row in receipt["rows"]] == list(range(31))
    assert all(all(row["checks"].values()) for row in receipt["rows"])


def test_published_component_blobs_are_exact() -> None:
    assert _blob(REPOSITORY, INITIALIZATION_RELATIVE) == EXPECTED_INITIALIZATION_BLOB
    assert _blob(REPOSITORY, Path("validators/multi_province/corrected_2018_single_turn/run.py")) == EXPECTED_SOURCE_INITIALIZATION_BLOB
    assert _blob(REPOSITORY, Path("src/ch5_two_asset_hank/multi_province/k1a_runtime_adapter.py")) == EXPECTED_K1A_BLOB
    assert _blob(REPOSITORY, Path("src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py")) == EXPECTED_C1_BLOB


def test_same_s_raw_payoff_uses_destination_by_origin_orientation() -> None:
    raw = np.arange(31, dtype=float) / 10.0
    shares = np.eye(31)
    shares[:, 0] = 0.0
    shares[1, 0] = 0.25
    shares[2, 0] = 0.75
    result = same_s_raw_next_payoff(raw, shares)
    assert result[0] == 0.25 * raw[1] + 0.75 * raw[2]
    assert np.array_equal(result[1:], raw[1:])


def test_scientific_ledger_accepts_ceiling_and_rejects_overrun() -> None:
    ledger = _new_ledger()
    ledger.update(
        source_native_initializations=31,
        scalar_labor_roots_attempted=24_800,
        scalar_labor_roots_returned=24_800,
        corrected_policy_maps=1_581,
        selector_evaluations=1_264_800,
        d2_q_assemblies=1_581,
        direct_hjb_updates=1_550,
    )
    _check_ledger(ledger)
    ledger["direct_hjb_updates"] += 1
    with pytest.raises(FailClosed):
        _check_ledger(ledger)
