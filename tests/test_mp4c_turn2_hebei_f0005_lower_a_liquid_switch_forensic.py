from __future__ import annotations

import inspect
import json
from pathlib import Path

from validators.multi_province.turn2_hebei_f0005_lower_a_liquid_switch_forensic import run


REPO = Path(__file__).resolve().parents[1]


def _cell() -> dict:
    _, cell = run.load_cell(REPO)
    return cell


def test_validator_has_no_production_or_scipy_import() -> None:
    source = inspect.getsource(run)
    import_lines = [line.strip() for line in source.splitlines() if line.startswith(("import ", "from "))]
    assert all("ch5_two_asset_hank" not in line for line in import_lines)
    assert all("scipy" not in line for line in import_lines)


def test_exact_persisted_cell_and_missing_combined_family() -> None:
    cell = _cell()
    assert cell["checkpoint"] == 1
    assert cell["flat_index_f_zero_based"] == 5
    assert cell["index_b_a_z_zero_based"] == [5, 0, 0]
    assert cell["selector_cell"]["cell_id"] == "v001_f0005_b005_a000_z000"
    inventory = run.candidate_inventory(cell)
    assert inventory["persisted_candidate_count"] == 15
    assert inventory["persisted_admissible_count"] == 0
    assert inventory["persisted_active_lower_a_interior_z_count"] == 0


def test_independent_root_and_existing_lower_a_kkt_compose_uniquely() -> None:
    selector_cell = _cell()["selector_cell"]
    root = run.reconstruct_root(selector_cell)
    combined = run.reconstruct_combined_candidate(selector_cell, root)
    q_b = float(root["q_b"])
    assert selector_cell["derivatives"]["p_b_forward"] < q_b
    assert q_b < selector_cell["derivatives"]["p_b_backward"]
    assert abs(q_b - 0.012085132579009492) <= 2e-17
    assert combined["active_constraints"] == ["lower_a"]
    assert combined["derivative_branches"] == {"a": "forward", "b": "zero"}
    assert combined["transfer_regime"] == "zero_kink"
    assert combined["lower_a_multiplier_decimal"].startswith("0.000284898632")
    assert combined["lower_a_multiplier_binary64"] == 0.00028489863234105843
    assert combined["q_a_binary64"] == combined["lower_a_kink_interval_binary64"][0]
    assert combined["transfer_kkt_residual"] == 0.0
    assert combined["admissible_under_existing_clauses"] is True


def test_control_flow_omits_combined_candidate_before_comparison() -> None:
    trace = run.source_trace(REPO)
    locations = trace["locations"]
    assert locations["endpoint_empty_return"] < locations["controls_after_kink_reconstruction"]
    assert locations["interior_z_requires_backward_g_b"] < locations["interior_z_candidate_call"]
    assert locations["interior_z_candidate_call"] < locations["hamiltonian_comparison"]
    assert trace["omission_before_hamiltonian_comparison"] is True
