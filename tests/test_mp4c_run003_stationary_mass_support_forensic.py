from __future__ import annotations

import ast
import json
import math
from pathlib import Path

import numpy as np

from validators.multi_province.run003_stationary_mass_support_forensic import run


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "validators/multi_province/run003_stationary_mass_support_forensic/run.py"


def test_f_order_coordinate_mapping_b_fastest() -> None:
    assert run.flat_coordinate(0) == (0, 0, 0)
    assert run.flat_coordinate(19) == (19, 0, 0)
    assert run.flat_coordinate(20) == (0, 1, 0)
    assert run.flat_coordinate(399) == (19, 19, 0)
    assert run.flat_coordinate(400) == (0, 0, 1)
    assert run.flat_coordinate(799) == (19, 19, 1)


def test_group_statistics_use_strict_floor_and_math_fsum() -> None:
    p = np.array([0.0, 0.25, -0.1, -0.2, 0.05], dtype=np.float64)
    row = run._group_statistics(p, np.arange(5), 0.1)
    assert row["state_count"] == 5
    assert row["exact_zero_count"] == 1
    assert row["positive_count"] == 2
    assert row["negative_count"] == 2
    assert row["below_negative_tau_breach_count"] == 1
    assert row["minimum_flat_index"] == 3
    assert row["signed_math_fsum_p"] == math.fsum(map(float, p))
    assert row["positive_mass_sum"] == math.fsum([0.25, 0.05])
    assert row["total_negative_mass"] == math.fsum([0.1, 0.2])
    assert row["l1_mass"] == math.fsum(abs(float(value)) for value in p)


def test_classification_contract_is_exclusive() -> None:
    assert run.classify(0, 3, True) == run.CLASSIFICATION_A
    assert run.classify(1, 3, True) == run.CLASSIFICATION_B
    assert run.classify(0, 3, False) == run.CLASSIFICATION_C
    assert run.classify(0, 0, True) == run.CLASSIFICATION_C


def test_residual_statistics_use_persisted_vector_only() -> None:
    residual = np.array([1e-9, -2e-9, 3e-9, -4e-9])
    row = run.residual_statistics(residual, np.array([1, 3]))
    assert row["infinity_norm"] == 4e-9
    assert row["l1_norm"] == math.fsum([2e-9, 4e-9])
    assert row["signed_math_fsum"] == math.fsum([-2e-9, -4e-9])
    assert row["max_absolute_residual_flat_index"] == 3


def test_zero_science_ledger_has_literal_zero_for_every_prohibited_call() -> None:
    ledger = run.zero_science_ledger()
    numeric = {key: value for key, value in ledger.items() if key.endswith("_calls") or key == "scientific_retries"}
    assert numeric
    assert set(numeric.values()) == {0}


def test_runner_imports_no_scientific_runtime_or_scipy() -> None:
    tree = ast.parse(RUNNER.read_text(encoding="utf-8"))
    imports = "\n".join(
        ast.unparse(node)
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
    ).lower()
    for forbidden in (
        "scipy", "ch5_two_asset_hank", "nonlinear_continuation", "selector", "household_adapter"
    ):
        assert forbidden not in imports


def test_accepted_source_manifest_and_field_identities_bind() -> None:
    source_root = ROOT / run.SOURCE_ROOT_RELATIVE
    receipt = run.verify_source_manifest(source_root)
    assert receipt["status"] == "PASS"
    arrays = source_root / "household/p00_北京/terminal_kfe/stationary_mass_arrays.npz"
    assert run.file_sha256(arrays) == run.MASS_ARTIFACT_SHA256
    with np.load(arrays, allow_pickle=False) as archive:
        assert run.field_sha256(archive["p"]) == run.P_SHA256
        assert run.field_sha256(archive["g"]) == run.G_SHA256
        assert run.field_sha256(archive["residual"]) == run.RESIDUAL_SHA256


def test_persisted_forensic_evidence_is_complete_and_classifies_a() -> None:
    evidence = ROOT / run.OUTPUT_ROOT_RELATIVE
    terminal = json.loads((evidence / "terminal_classification.json").read_text(encoding="utf-8"))
    table = json.loads((evidence / "complete_breach_table.json").read_text(encoding="utf-8"))
    stats = json.loads((evidence / "group_statistics.json").read_text(encoding="utf-8"))["groups"]
    assert terminal["terminal_marker"] == run.TERMINAL_MARKER
    assert terminal["classification"] == run.CLASSIFICATION_A
    assert terminal["kfe_status"] == "FAIL_UNCHANGED"
    assert table["row_count"] == 14 == len(table["rows"])
    assert {row["support_class"] for row in table["rows"]} == {"transient"}
    assert stats["closed"]["below_negative_tau_breach_count"] == 0
    assert stats["closed"]["negative_count"] == 0
    assert stats["transient"]["below_negative_tau_breach_count"] == 14


def test_persisted_manifest_independent_readback_passes() -> None:
    evidence = ROOT / run.OUTPUT_ROOT_RELATIVE
    readback = json.loads(
        (evidence / "independent_readback_receipt.json").read_text(encoding="utf-8")
    )
    independently_recomputed = run._readback(evidence)
    assert readback == independently_recomputed
    assert readback["status"] == "PASS"
    assert readback["bad_paths"] == []
