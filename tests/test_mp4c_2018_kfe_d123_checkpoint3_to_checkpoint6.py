from pathlib import Path

import numpy as np
import pytest

from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import FailClosed
from ch5_two_asset_hank.corrected_diagnostic.checkpoint3_to_checkpoint6 import (
    ACCEPTED_CHECKPOINT3_IDENTITY,
    ACCEPTED_P3_IDENTITY,
    ACCEPTED_Q3_ARTIFACT_SHA256,
    ACCEPTED_U3_SHA256,
    ACCEPTED_V3_SHA256,
    _check_task_ledger,
    _load_accepted_checkpoint3,
    _new_ledger,
    detect_authorized_approximate_cycle,
)


def test_accepted_checkpoint3_binding_is_exact_without_remapping() -> None:
    repository = Path(__file__).resolve().parents[1]

    accepted = _load_accepted_checkpoint3(repository)

    assert accepted["identities"]["v3"] == ACCEPTED_V3_SHA256
    assert accepted["identities"]["p3"] == ACCEPTED_P3_IDENTITY
    assert accepted["identities"]["u3"] == ACCEPTED_U3_SHA256
    assert accepted["identities"]["q3"] == ACCEPTED_Q3_ARTIFACT_SHA256
    assert accepted["identities"]["checkpoint3"] == ACCEPTED_CHECKPOINT3_IDENTITY
    assert len(accepted["p3_rows"]) == 800
    assert accepted["v3_policy_map_rerun"] is False
    assert accepted["q3_assembly_rerun"] is False


def test_task_ledger_allows_only_three_updates_maps_and_checkpoints() -> None:
    ledger = _new_ledger()
    ledger.update(
        direct_hjb_solves=3,
        hjb_updates=3,
        new_corrected_policy_maps=3,
        selector_evaluations=2400,
        d2_assemblies=3,
        checkpoint_evaluations=3,
    )
    _check_task_ledger(ledger)

    ledger["direct_hjb_solves"] = 4
    with pytest.raises(FailClosed):
        _check_task_ledger(ledger)


def test_task_ledger_forbids_v3_map_and_q3_reruns() -> None:
    ledger = _new_ledger()
    ledger["v3_policy_map_reruns"] = 1
    with pytest.raises(FailClosed):
        _check_task_ledger(ledger)

    ledger = _new_ledger()
    ledger["q3_assembly_reruns"] = 1
    with pytest.raises(FailClosed):
        _check_task_ledger(ledger)


def test_approximate_cycle_windows_use_accepted_history() -> None:
    values_through_v4 = [
        np.array([99.0]),
        np.array([0.0]),
        np.array([1.0]),
        np.array([0.0]),
        np.array([1.0]),
    ]
    result = detect_authorized_approximate_cycle(values_through_v4, checkpoint=4)
    assert result is not None and result["period"] == 2

    values_through_v6 = [
        np.array([99.0]),
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
        np.array([0.0]),
        np.array([1.0]),
        np.array([2.0]),
    ]
    result = detect_authorized_approximate_cycle(values_through_v6, checkpoint=6)
    assert result is not None and result["period"] == 3
