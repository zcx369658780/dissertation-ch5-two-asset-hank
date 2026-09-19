from pathlib import Path

import numpy as np
import pytest

from ch5_two_asset_hank.corrected_diagnostic.checkpoint2_to_checkpoint6 import (
    detect_authorized_approximate_cycle,
)
from ch5_two_asset_hank.corrected_diagnostic.checkpoint6_to_checkpoint10 import (
    ACCEPTED_CHECKPOINT_IDENTITIES,
    ACCEPTED_P6_IDENTITY,
    ACCEPTED_Q6_ARTIFACT_SHA256,
    ACCEPTED_SEALED_MANIFEST_SHA256,
    ACCEPTED_U6_SHA256,
    ACCEPTED_VALUE_SHA256,
    _apply_checkpoint10_ceiling,
    _check_task_ledger,
    _load_accepted_checkpoint6,
    _new_ledger,
)
from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import FailClosed


def test_accepted_checkpoint6_binding_is_exact_without_remapping() -> None:
    repository = Path(__file__).resolve().parents[1]

    accepted = _load_accepted_checkpoint6(repository)

    assert accepted["manifest_entry_count"] == 1633
    assert accepted["v6_policy_map_rerun"] is False
    assert accepted["q6_assembly_rerun"] is False
    assert len(accepted["p6_rows"]) == 800
    assert accepted["checkpoint_manifests"][6]["value_sha256"] == ACCEPTED_VALUE_SHA256[6]
    assert (
        accepted["checkpoint_manifests"][6]["policy_identity_sha256"]
        == ACCEPTED_P6_IDENTITY
    )
    assert accepted["checkpoint_manifests"][6]["utility_sha256"] == ACCEPTED_U6_SHA256
    assert (
        accepted["checkpoint_manifests"][6]["q_artifact_sha256"]
        == ACCEPTED_Q6_ARTIFACT_SHA256
    )
    assert (
        accepted["checkpoint_manifests"][6]["checkpoint_identity_sha256"]
        == ACCEPTED_CHECKPOINT_IDENTITIES[6]
    )
    assert len(ACCEPTED_SEALED_MANIFEST_SHA256) == 64


def test_task_ledger_allows_only_four_updates_maps_and_checkpoints() -> None:
    ledger = _new_ledger()
    ledger.update(
        direct_hjb_solves=4,
        hjb_updates=4,
        new_corrected_policy_maps=4,
        selector_evaluations=3200,
        d2_assemblies=4,
        checkpoint_evaluations=4,
    )
    _check_task_ledger(ledger)

    ledger["checkpoint_evaluations"] = 5
    with pytest.raises(FailClosed):
        _check_task_ledger(ledger)


def test_task_ledger_forbids_v6_map_and_q6_reruns() -> None:
    ledger = _new_ledger()
    ledger["v6_policy_map_reruns"] = 1
    with pytest.raises(FailClosed):
        _check_task_ledger(ledger)

    ledger = _new_ledger()
    ledger["q6_assembly_reruns"] = 1
    with pytest.raises(FailClosed):
        _check_task_ledger(ledger)


def test_multidimensional_approximate_cycle_uses_f_order_vector_norm(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    pattern = np.arange(8, dtype=float).reshape((2, 2, 2), order="F") * 1.0e-10
    values = [
        np.full((2, 2, 2), 99.0),
        np.zeros((2, 2, 2)),
        np.zeros((2, 2, 2)),
        pattern,
        pattern,
    ]
    original_norm = np.linalg.norm
    observed: list[np.ndarray] = []

    def checked_norm(value: np.ndarray, *args: object, **kwargs: object) -> float:
        array = np.asarray(value)
        assert array.ndim == 1
        observed.append(array.copy())
        return float(original_norm(array, *args, **kwargs))

    monkeypatch.setattr(np.linalg, "norm", checked_norm)
    result = detect_authorized_approximate_cycle(values, checkpoint=4)

    assert result is not None and result["period"] == 2
    assert len(observed) == 2
    assert np.array_equal(observed[0], pattern.ravel(order="F"))
    assert np.array_equal(observed[1], pattern.ravel(order="F"))


def test_checkpoint10_ceiling_preserves_earlier_terminal_order() -> None:
    convergence = "HJB_CONVERGENCE_CANDIDATE__TERMINAL_GATE_NOT_RUN"
    assert _apply_checkpoint10_ceiling(10, convergence) == convergence
    assert _apply_checkpoint10_ceiling(9, None) is None
    assert (
        _apply_checkpoint10_ceiling(10, None)
        == "COMPLETE_CHECKPOINT10_NONCONVERGED__TERMINAL_GATE_NOT_RUN"
    )
