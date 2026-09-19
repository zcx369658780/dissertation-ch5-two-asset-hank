from pathlib import Path

import pytest

from ch5_two_asset_hank.corrected_diagnostic.nonlinear_continuation import FailClosed
from ch5_two_asset_hank.corrected_diagnostic.v3_checkpoint3_reexecution import (
    ACCEPTED_V3_ARTIFACT_SHA256,
    ACCEPTED_V3_SHA256,
    _check_task_ledger,
    _load_accepted_v3,
    _new_ledger,
)


def test_accepted_v3_binding_is_exact_and_does_not_rerun_update() -> None:
    repository = Path(__file__).resolve().parents[1]

    value, receipt = _load_accepted_v3(repository)

    assert value.shape == (20, 20, 2)
    assert receipt["value_sha256"] == ACCEPTED_V3_SHA256
    assert receipt["artifact_sha256"] == ACCEPTED_V3_ARTIFACT_SHA256
    assert receipt["v2_to_v3_rerun"] is False


def test_task_ledger_allows_only_one_map_q3_and_checkpoint_evaluation() -> None:
    ledger = _new_ledger()
    ledger.update(
        new_corrected_policy_maps=1,
        selector_evaluations=800,
        d2_assemblies=1,
        checkpoint_evaluations=1,
    )
    _check_task_ledger(ledger)

    ledger["new_corrected_policy_maps"] = 2
    with pytest.raises(FailClosed):
        _check_task_ledger(ledger)


def test_task_ledger_forbids_hjb_solves_and_v3_to_v4_updates() -> None:
    ledger = _new_ledger()
    ledger["direct_hjb_solves"] = 1
    with pytest.raises(FailClosed):
        _check_task_ledger(ledger)

    ledger = _new_ledger()
    ledger["hjb_updates"] = 1
    with pytest.raises(FailClosed):
        _check_task_ledger(ledger)
