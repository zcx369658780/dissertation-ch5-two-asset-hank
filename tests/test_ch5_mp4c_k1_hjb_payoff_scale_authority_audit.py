from __future__ import annotations

import ast
import importlib.util
from pathlib import Path

import pytest


REPO = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO / "validators/multi_province/hjb_payoff_scale_authority_audit/build.py"
SPEC = importlib.util.spec_from_file_location("payoff_scale_audit", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def test_builder_has_no_scientific_imports() -> None:
    tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
    imported = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    }
    assert not any(name.startswith(("src", "ch5_two_asset_hank", "exports", "numpy", "scipy")) for name in imported)


def test_authority_classification_preserves_conflict_and_no_identity_authority() -> None:
    by_object = {row["object"]: row for row in MODULE.time_unit_rows()}
    assert by_object["firm delta=.025"]["authority"] == "CONFLICTING_SOURCE_AUTHORITY"
    assert by_object["firm ra0"]["authority"] == "CONFLICTING_SOURCE_AUTHORITY"
    mappings = {row["candidate"]: row for row in MODULE.mapping_rows()}
    assert mappings["A identity r_a=ra0"]["status"] == "NOT_AUTHORIZED"
    assert mappings["B annual firm-flow to quarterly HJB flow"]["status"] == "OWNER_SOURCE_FREEZE_REQUIRED"


def test_build_writes_readback_manifest_and_refuses_overwrite(tmp_path: Path) -> None:
    output = tmp_path / "evidence"
    MODULE.build(output)
    expected = {
        "source_identity.json", "time_unit_authority.csv", "hard_bound_inventory.csv",
        "candidate_mapping_table.csv", "zero_science_call_ledger.json", "manifest.sha256",
    }
    assert {path.name for path in output.iterdir()} == expected
    manifest = (output / "manifest.sha256").read_text(encoding="ascii")
    assert "zero_science_call_ledger.json" in manifest
    with pytest.raises(FileExistsError):
        MODULE.build(output)
