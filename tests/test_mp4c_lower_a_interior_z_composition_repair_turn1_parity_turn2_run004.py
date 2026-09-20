from __future__ import annotations

import inspect
from pathlib import Path

from validators.multi_province.lower_a_interior_z_composition_repair_turn1_parity_turn2_run004 import (
    run,
)
from validators.multi_province.lower_a_interior_z_composition_repair_turn1_parity_turn2_run004.run import (
    accepted_turn1_map_inventory,
)


REPOSITORY = Path(__file__).resolve().parents[1]


def test_accepted_turn1_policy_map_inventory_is_exact_and_ordered() -> None:
    rows = accepted_turn1_map_inventory(REPOSITORY)

    assert len(rows) == 408
    assert rows[0]["province_index"] == 0
    assert rows[0]["province"] == "北京"
    assert rows[0]["checkpoint"] == 0
    assert rows[-1]["province_index"] == 30
    assert rows[-1]["province"] == "新疆"
    assert rows[-1]["checkpoint"] == 11
    assert all(
        rows[index]["province_index"] <= rows[index + 1]["province_index"]
        for index in range(len(rows) - 1)
    )


def test_compatibility_replay_has_no_downstream_science_entrypoint() -> None:
    source = inspect.getsource(run.replay_turn1_policy_identities)

    for forbidden in (
        "_map_checkpoint(",
        "_solve_province(",
        "_policy_arrays(",
        "assemble_consumed_drift_generator(",
        "_direct_update(",
        "_terminal_kfe(",
        "integrate_one_turn(",
    ):
        assert forbidden not in source
    assert '"hjb_direct_updates": 0' in source
    assert '"d2_q_assemblies": 0' in source
    assert '"scc_kfe_svd": 0' in source
    assert '"aggregates_integration": 0' in source
