from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import pytest

from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import _field_sha256
from ch5_two_asset_hank.corrected_diagnostic.run004_canonical_integration_replay import (
    HOUSEHOLD_BATCH_SHA256,
    FailClosed,
    _new_ledger,
    canonical_same_s_raw_next_payoff,
    reconstruct_accepted_household_batch,
)


REPOSITORY = Path(__file__).resolve().parents[1]


def _fixture() -> tuple[np.ndarray, np.ndarray]:
    raw = np.linspace(0.1, 3.1, 31, dtype=np.float64)
    shares = np.arange(1, 31 * 31 + 1, dtype=np.float64).reshape(31, 31)
    shares /= np.sum(shares, axis=0)
    return raw, shares


def _canonical(raw: np.ndarray, shares: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    return canonical_same_s_raw_next_payoff(
        raw,
        shares,
        orientation="destination_by_origin",
        raw_source="firm.ra0",
        expected_raw_sha256=_field_sha256(raw),
        expected_shares_sha256=_field_sha256(shares),
    )


def test_mathematically_identical_reduction_orders_can_differ_bitwise() -> None:
    terms = [1.0e16, 1.0, -1.0e16]
    assert sum(terms) == 0.0
    assert math.fsum(terms) == 1.0
    assert np.float64(sum(terms)).tobytes() != np.float64(math.fsum(terms)).tobytes()


def test_canonical_fsum_matches_explicit_scalar_term_lists() -> None:
    raw, shares = _fixture()
    payoff, terms = _canonical(raw, shares)
    expected = np.asarray([
        math.fsum(float(raw[j]) * float(shares[j, i]) for j in range(31))
        for i in range(31)
    ])
    assert np.array_equal(payoff, expected)
    assert np.array_equal(terms, raw[:, None] * shares)


def test_transposed_or_mislabeled_orientation_fails_closed() -> None:
    raw, shares = _fixture()
    with pytest.raises(FailClosed, match="PROVENANCE_OR_ORIENTATION"):
        canonical_same_s_raw_next_payoff(
            raw,
            shares.T,
            orientation="destination_by_origin",
            raw_source="firm.ra0",
            expected_raw_sha256=_field_sha256(raw),
            expected_shares_sha256=_field_sha256(shares),
        )
    with pytest.raises(FailClosed, match="PROVENANCE_OR_ORIENTATION"):
        canonical_same_s_raw_next_payoff(
            raw,
            shares,
            orientation="origin_by_destination",
            raw_source="firm.ra0",
            expected_raw_sha256=_field_sha256(raw),
            expected_shares_sha256=_field_sha256(shares),
        )


def test_clipped_or_alternate_return_cannot_replace_raw_ra0() -> None:
    raw, shares = _fixture()
    clipped = np.clip(raw, 0.02, 0.09)
    with pytest.raises(FailClosed, match="PROVENANCE_OR_ORIENTATION"):
        canonical_same_s_raw_next_payoff(
            clipped,
            shares,
            orientation="destination_by_origin",
            raw_source="firm.ra",
            expected_raw_sha256=_field_sha256(raw),
            expected_shares_sha256=_field_sha256(shares),
        )


def test_run004_household_batch_reconstruction_is_exact_and_zero_science() -> None:
    ledger = _new_ledger()
    batch, receipt = reconstruct_accepted_household_batch(REPOSITORY, ledger)
    assert receipt["status"] == "PASS"
    assert receipt["reconstructed_identity_sha256"] == HOUSEHOLD_BATCH_SHA256
    assert batch.ct.shape == (31,)
    assert ledger["household_batch_reconstructions"] == 1
    assert ledger["province_terminal_receipt_loads"] == 31
    assert ledger["stationary_aggregate_receipt_loads"] == 31
    for name in (
        "source_native_initializations",
        "selector_or_root_calls",
        "d2_q_assemblies",
        "hjb_or_direct_solve_calls",
        "scc_or_topology_calls",
        "restricted_gesvd_calls",
        "full_space_gesvd_calls",
        "stationary_mass_candidate_calls",
        "q_transpose_p_calls",
        "corrected_aggregate_evaluations",
    ):
        assert ledger[name] == 0
