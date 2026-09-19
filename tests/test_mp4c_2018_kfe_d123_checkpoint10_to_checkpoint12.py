from pathlib import Path

import pytest

from ch5_two_asset_hank.corrected_diagnostic.checkpoint10_to_checkpoint12 import (
    ACCEPTED_CHECKPOINT_IDENTITIES,
    ACCEPTED_P10_IDENTITY,
    ACCEPTED_Q10_ARTIFACT_SHA256,
    ACCEPTED_SEALED_MANIFEST_SHA256,
    ACCEPTED_U10_SHA256,
    ACCEPTED_VALUE_SHA256,
    _apply_checkpoint12_ceiling,
    _check_task_ledger,
    _load_accepted_checkpoint10,
    _new_ledger,
)
from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import FailClosed


def test_accepted_checkpoint10_binding_is_exact_without_remapping() -> None:
    repository = Path(__file__).resolve().parents[1]
    accepted = _load_accepted_checkpoint10(repository)

    assert accepted["manifest_entry_count"] == 3249
    assert accepted["v10_policy_map_rerun"] is False
    assert accepted["q10_assembly_rerun"] is False
    assert len(accepted["p10_rows"]) == 800
    assert accepted["checkpoint_manifests"][10]["value_sha256"] == ACCEPTED_VALUE_SHA256[10]
    assert accepted["checkpoint_manifests"][10]["policy_identity_sha256"] == ACCEPTED_P10_IDENTITY
    assert accepted["checkpoint_manifests"][10]["utility_sha256"] == ACCEPTED_U10_SHA256
    assert accepted["checkpoint_manifests"][10]["q_artifact_sha256"] == ACCEPTED_Q10_ARTIFACT_SHA256
    assert accepted["checkpoint_manifests"][10]["checkpoint_identity_sha256"] == ACCEPTED_CHECKPOINT_IDENTITIES[10]
    assert len(ACCEPTED_SEALED_MANIFEST_SHA256) == 64


def test_task_ledger_allows_only_two_updates_maps_and_checkpoints() -> None:
    ledger = _new_ledger()
    ledger.update(
        direct_hjb_solves=2,
        hjb_updates=2,
        new_corrected_policy_maps=2,
        selector_evaluations=1600,
        d2_assemblies=2,
        checkpoint_evaluations=2,
    )
    _check_task_ledger(ledger)

    ledger["checkpoint_evaluations"] = 3
    with pytest.raises(FailClosed):
        _check_task_ledger(ledger)


def test_task_ledger_forbids_v10_map_and_q10_reruns() -> None:
    ledger = _new_ledger()
    ledger["v10_policy_map_reruns"] = 1
    with pytest.raises(FailClosed):
        _check_task_ledger(ledger)

    ledger = _new_ledger()
    ledger["q10_assembly_reruns"] = 1
    with pytest.raises(FailClosed):
        _check_task_ledger(ledger)


def test_checkpoint12_ceiling_preserves_earlier_terminal_order() -> None:
    convergence = "HJB_CONVERGENCE_CANDIDATE__TERMINAL_GATE_NOT_RUN"
    assert _apply_checkpoint12_ceiling(12, convergence) == convergence
    assert _apply_checkpoint12_ceiling(11, None) is None
    assert (
        _apply_checkpoint12_ceiling(12, None)
        == "COMPLETE_CHECKPOINT12_NONCONVERGED__TERMINAL_GATE_NOT_RUN"
    )
