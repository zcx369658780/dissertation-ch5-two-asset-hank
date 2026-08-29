import numpy as np
import pytest

from ch5_two_asset_hank.contracts import PolicySnapshot
from ch5_two_asset_hank.policies import (
    _canonicalize_lower_b_near_tie,
    _hamiltonian_tolerance,
)
from ch5_two_asset_hank.steady_state import (
    SteadyStateValidationError,
    _validate_common_core_policy_compatibility,
    _validate_common_core_normalized_changes,
)


def candidate(identifier, hamiltonian=1.0, *, consumption=1.0, labor=(1.0,),
              transfer=0.2, cost=0.1, mu_a=0.2, mu_b=0.0,
              lambda_b=0.0, kkt=0.0):
    return (
        hamiltonian, identifier, consumption, np.array(labor), transfer, cost,
        mu_a, mu_b, 0.0, lambda_b, {"residual": kkt},
    )


@pytest.mark.parametrize("ids", [("FF", "FZ"), ("BF", "BZ")])
def test_active_lower_b_exact_and_near_ties_canonicalize_to_z(ids):
    tau = _hamiltonian_tolerance(1.0, 1.0)
    for gap in (0.0, tau):
        raw, selected, available, observed_gap, bound = _canonicalize_lower_b_near_tie(
            [candidate(ids[0], 1.0 + gap), candidate(ids[1], 1.0)],
            active_lower_b=True, zero_tolerance=1e-12, gamma_c=1.0,
        )
        assert raw[1] == ids[0]
        assert selected[1] == ids[1]
        assert available
        assert observed_gap <= bound


def test_canonicalization_is_permutation_deterministic():
    pair = [candidate("FF"), candidate("FZ")]
    outcomes = []
    for values in (pair, list(reversed(pair))):
        outcomes.append(_canonicalize_lower_b_near_tie(
            values, active_lower_b=True, zero_tolerance=1e-12, gamma_c=1.0,
        )[1][1])
    assert outcomes == ["FZ", "FZ"]


def test_raw_lower_boundary_multiplier_difference_is_allowed_for_equivalent_shadow_policy():
    raw, selected, available, _, _ = _canonicalize_lower_b_near_tie(
        [candidate("FF", lambda_b=0.25), candidate("FZ", lambda_b=0.0)],
        active_lower_b=True, zero_tolerance=1e-12, gamma_c=1.0,
    )
    assert raw[1] == "FF"
    assert selected[1] == "FZ"
    assert available


def test_missing_alias_counterpart_cannot_claim_availability():
    raw, selected, available, gap, bound = _canonicalize_lower_b_near_tie(
        [candidate("FF")], active_lower_b=True,
        zero_tolerance=1e-12, gamma_c=1.0,
    )
    assert selected is raw
    assert not available
    assert np.isnan(gap) and np.isnan(bound)


def test_outside_near_tie_preserves_larger_hamiltonian():
    tau = _hamiltonian_tolerance(1.0, 1.0)
    raw, selected, available, _, _ = _canonicalize_lower_b_near_tie(
        [candidate("FF", 1.0 + 2.0 * tau), candidate("FZ", 1.0)],
        active_lower_b=True, zero_tolerance=1e-12, gamma_c=1.0,
    )
    assert raw[1] == selected[1] == "FF"
    assert not available


@pytest.mark.parametrize("change", [
    {"mu_b": 2e-12}, {"consumption": 1.0 + 1e-12}, {"mu_a": -0.2},
    {"kkt": 2e-7},
])
def test_material_physical_drift_or_kkt_difference_does_not_alias(change):
    raw, selected, available, _, _ = _canonicalize_lower_b_near_tie(
        [candidate("FF"), candidate("FZ", **change)],
        active_lower_b=True, zero_tolerance=1e-12, gamma_c=1.0,
    )
    assert raw[1] == selected[1] == "FF"
    assert not available


@pytest.mark.parametrize("first,second,active", [
    ("FF", "BZ", True), ("FF0", "FZ", True), ("FF", "FZ", False),
])
def test_alias_scope_is_narrow(first, second, active):
    raw, selected, available, _, _ = _canonicalize_lower_b_near_tie(
        [candidate(first), candidate(second)], active_lower_b=active,
        zero_tolerance=1e-12, gamma_c=1.0,
    )
    assert selected[1] == raw[1]
    assert not available


def snapshot(raw, canonical, *, alias=True, c=1.0, labor=1.0, transfer=0.2,
             cost=0.1, mu_a=0.2, mu_b=0.0, shadow=1.0, gap=0.0,
             bound=1e-14, kkt=0.0, boundary=0.0):
    shape = (1, 1, 1)
    zeros = np.zeros(shape)
    return PolicySnapshot(
        np.full(shape, c), np.full(shape + (1,), labor), np.full(shape, transfer),
        np.full(shape, cost), np.full(shape, mu_a), np.full(shape, mu_b), zeros,
        np.full(shape, canonical), zeros, zeros, np.full(shape, kkt), {}, boundary, kkt,
        raw_candidate_id=np.full(shape, raw),
        qualifying_lower_b_alias_available=np.full(shape, alias),
        effective_shadow_b=np.full(shape, shadow),
        alias_hamiltonian_gap=np.full(shape, gap),
        alias_hamiltonian_bound=np.full(shape, bound),
    )


def test_state_compatibility_allows_raw_multiplier_representation_only_with_physical_evidence():
    evidence = _validate_common_core_policy_compatibility(
        snapshot("FF", "FZ"), snapshot("FZ", "FZ"),
        np.array([0]), np.array([0]), np.array([0.0]), np.array([0.0]),
        np.array([0.75]),
    )
    assert evidence[0]["raw_ids"] == ("FF", "FZ")
    assert evidence[0]["canonical_ids"] == ("FZ", "FZ")


def test_cross_truncation_policy_difference_above_machine_scale_can_pass():
    evidence = _validate_common_core_policy_compatibility(
        snapshot("FF", "FZ"),
        snapshot("FZ", "FZ", c=1.0 + 1e-12, shadow=1.0 + 1e-12),
        np.array([0]), np.array([0]), np.array([0.0]), np.array([0.0]),
        np.array([0.75]),
    )
    assert evidence[0]["raw_ids"] == ("FF", "FZ")


def test_value_normalized_guard_fails_independently_above_threshold():
    with pytest.raises(SteadyStateValidationError, match="value"):
        _validate_common_core_normalized_changes(
            np.zeros((1, 1, 1)), np.full((1, 1, 1), 1.001),
            snapshot("FZ", "FZ"), snapshot("FZ", "FZ"),
            np.array([0]), np.array([0]),
        )


@pytest.mark.parametrize("field,match", [
    ("c", "consumption"), ("labor", "labor"), ("transfer", "transfer"),
    ("cost", "adjustment_cost"), ("mu_a", "mu_a"),
])
def test_each_policy_normalized_guard_fails_independently(field, match):
    changes = {field: 1.002 if field in {"c", "labor"} else 0.202}
    with pytest.raises(SteadyStateValidationError, match=match):
        _validate_common_core_normalized_changes(
            np.zeros((1, 1, 1)), np.zeros((1, 1, 1)),
            snapshot("FZ", "FZ"), snapshot("FZ", "FZ", **changes),
            np.array([0]), np.array([0]),
        )


def test_mu_b_drift_classification_mismatch_fails_even_with_small_scalar_change():
    with pytest.raises(SteadyStateValidationError, match="classifications differ"):
        _validate_common_core_policy_compatibility(
            snapshot("FZ", "FZ", mu_b=0.0),
            snapshot("FZ", "FZ", mu_b=2e-12),
            np.array([0]), np.array([0]), np.array([0.0]), np.array([0.0]),
            np.array([0.75]),
        )


def test_canonical_id_mismatch_fails_even_when_raw_ids_agree():
    with pytest.raises(SteadyStateValidationError, match="canonical IDs differ"):
        _validate_common_core_policy_compatibility(
            snapshot("FF", "FZ"), snapshot("FF", "FF"),
            np.array([0]), np.array([0]), np.array([0.0]), np.array([0.0]),
            np.array([0.75]),
        )


@pytest.mark.parametrize("right,match", [
    (snapshot("FZ", "FZ", kkt=2e-7), "KKT"),
    (snapshot("FZ", "FZ", boundary=2e-12), "boundary"),
])
def test_cross_truncation_kkt_and_boundary_fail_closed(right, match):
    with pytest.raises(SteadyStateValidationError, match=match):
        _validate_common_core_policy_compatibility(
            snapshot("FF", "FZ"), right,
            np.array([0]), np.array([0]), np.array([0.0]), np.array([0.0]),
            np.array([0.75]),
        )


@pytest.mark.parametrize("right,match", [
    (snapshot("FZ", "FZ", alias=False), "availability"),
    (snapshot("FZ", "FZ", gap=2e-14, bound=1e-14), "Hamiltonian"),
])
def test_state_compatibility_fails_closed_with_state_and_raw_canonical_ids(right, match):
    with pytest.raises(SteadyStateValidationError) as exc:
        _validate_common_core_policy_compatibility(
            snapshot("FF", "FZ"), right,
            np.array([0]), np.array([0]), np.array([0.0]), np.array([0.0]),
            np.array([0.75]),
        )
    message = str(exc.value)
    assert match.lower() in message.lower()
    assert "raw=('FF', 'FZ')" in message
    assert "canonical=('FZ', 'FZ')" in message
