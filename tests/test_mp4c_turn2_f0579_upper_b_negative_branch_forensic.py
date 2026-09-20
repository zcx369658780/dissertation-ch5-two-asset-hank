from __future__ import annotations

import ast
import json
import math
from pathlib import Path

from validators.multi_province.turn2_f0579_upper_b_negative_branch_forensic import run


REPOSITORY = Path(__file__).resolve().parents[1]


def test_exact_failure_cell_and_manifest_binding() -> None:
    manifest = run.verify_manifest(REPOSITORY)
    forensic_run001 = run.verify_forensic_run001_manifest(REPOSITORY)
    payload, cell = run.load_cell(REPOSITORY)
    assert manifest["status"] == "PASS"
    assert forensic_run001["status"] == "PASS"
    assert payload["flat_index_f_zero_based"] == 579
    assert cell.cell_id == "v002_f0579_b019_a008_z001"
    assert cell.derivatives.p_b_backward == run.EXPECTED["p_b_backward"]
    assert cell.derivatives.p_a_backward == run.EXPECTED["p_a_backward"]
    assert cell.derivatives.p_a_forward == run.EXPECTED["p_a_forward"]


def test_current_candidates_reproduce_from_persisted_receipt_only() -> None:
    payload, _ = run.load_cell(REPOSITORY)
    receipt = run.reproduce_candidates(payload)
    assert receipt["status"] == "PASS"
    assert receipt["checks"]["active_negative_pre_root"]
    assert receipt["checks"]["active_zero_no_unique_bracket"]
    assert receipt["checks"]["active_positive_sign_and_kkt"]


def test_selector_and_cost_authority_blobs_are_frozen() -> None:
    assert run._blob(REPOSITORY, run.SELECTOR_RELATIVE) == run.SELECTOR_BLOB
    assert run._blob(REPOSITORY, run.COST_RELATIVE) == run.COST_BLOB


def test_raw_negative_infinity_uses_json_safe_frozen_screen_representation() -> None:
    receipt = run.finite_screen_repair_contract()
    assert receipt["status"] == "PASS"
    assert receipt["checks"]["negative_infinity_evidence_is_finite"]
    json.dumps(receipt, allow_nan=False)


def test_capture_changes_only_evidence_and_returns_raw_callback_value() -> None:
    calls: list[tuple[float, float]] = []
    observations = {"raw_nonfinite_observation_count": 0}
    returned = run._capture_root_evaluation(1.0, -math.inf, calls, observations)
    assert returned == -math.inf
    assert calls == [(1.0, -float.fromhex("0x1.fffffffffffffp+1023"))]
    assert observations == {"raw_nonfinite_observation_count": 1}

    finite_calls: list[tuple[float, float]] = []
    finite_observations = {"raw_nonfinite_observation_count": 0}
    finite_returned = run._capture_root_evaluation(
        2.0, 1.25, finite_calls, finite_observations
    )
    assert finite_returned == 1.25
    assert finite_calls == [(2.0, 1.25)]
    assert finite_observations == {"raw_nonfinite_observation_count": 0}


def test_classification_contract_covers_a_b_c_without_new_law() -> None:
    inadmissible = {"admissible": False}
    base = {"c": 1.0, "l": 1.0, "d": -1.0, "cost": 0.1, "g_b": 0.0, "g_a": 1.0}
    admissible_low = {**base, "admissible": True, "branch": "backward", "hamiltonian": 1.0}
    admissible_high = {**base, "c": 2.0, "admissible": True, "branch": "forward", "hamiltonian": 2.0}
    assert run.classify(inadmissible, inadmissible)[0] == run.CLASS_B
    assert run.classify(admissible_low, inadmissible)[0] == run.CLASS_A
    assert run.classify(admissible_low, admissible_high)[0] == run.CLASS_A
    tied = {**base, "c": 2.0, "admissible": True, "branch": "forward", "hamiltonian": 1.0}
    assert run.classify(admissible_low, tied)[0] == run.CLASS_C


def test_validator_has_no_full_selector_or_forbidden_scientific_imports() -> None:
    source = (REPOSITORY / run.VALIDATOR_RELATIVE).read_text(encoding="utf-8")
    tree = ast.parse(source)
    names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
    assert "select_constrained_policy" not in names
    for forbidden in ("spsolve", "svd", "assemble_corrected_generator"):
        assert forbidden not in names
    assert "_one_scalar_root" in source
    assert "_finite_root_value" in source
    assert "max_root_invocations=2" in source
    assert run.sys.executable
