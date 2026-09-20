from __future__ import annotations

import inspect
import json
from pathlib import Path

from validators.multi_province.turn2_heilongjiang_f0063_nonpositive_backward_liquid_shadow_forensic import (
    run,
)


REPOSITORY = Path(__file__).resolve().parents[1]


def _cell():
    payload = json.loads((REPOSITORY / run.CELL_REL).read_text(encoding="utf-8"))
    return payload["selector_cell"]


def test_independent_roots_and_current_authority_boundary() -> None:
    analysis = run.independent_analysis(_cell())
    roots = analysis["ordinary_family_roots"]

    assert roots["negative_a_backward"]["q_b"] == 0.018920460453074793
    assert roots["negative_a_forward"]["q_b"] == 0.01863335288123777
    assert roots["zero_kink_a_forward"]["q_b"] == 0.017192264126029845
    assert roots["positive_a_forward"]["q_b"] == 0.01801822665826406
    assert roots["positive_a_forward"]["transfer_kkt_ok"] is True
    assert roots["positive_a_forward"]["a_direction_ok"] is True
    assert roots["positive_a_forward"]["inside_authorized_two_positive_shadow_bracket"] is False
    assert roots["negative_a_backward"]["transfer_sign_ok"] is False
    assert roots["negative_a_forward"]["transfer_sign_ok"] is False
    assert roots["zero_kink_a_forward"]["transfer_kkt_ok"] is False


def test_interior_a_and_joint_switching_have_no_legal_interval() -> None:
    row = run.independent_analysis(_cell())["interior_a_fixed_d_analysis"]

    assert row["d_z"] == -0.49070799399159126
    assert row["d3_ratio_q_a_over_q_b"] == 0.2784365409439844
    assert row["implied_positive_q_b_interval"] == [
        0.08777371295849923,
        0.09355595319330069,
    ]
    assert row["independent_global_positive_root"] == 0.016292425733501197
    assert row["root_inside_implied_interval"] is False
    assert row["root_inside_liquid_derivative_interval"] is False


def test_validator_has_no_production_science_import_or_call() -> None:
    source = inspect.getsource(run)

    for forbidden in (
        "from ch5_two_asset_hank",
        "import ch5_two_asset_hank",
        "select_constrained_policy(",
        "_one_interior_z_root(",
        "_one_scalar_root(",
        "spsolve(",
        "svd(",
    ):
        assert forbidden not in source
    assert '"production_selector_calls": 0' in source
    assert '"turn2_replay_or_rerun": 0' in source
