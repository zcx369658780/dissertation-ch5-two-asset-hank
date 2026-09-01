from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

import pytest

from validators.multi_province.mp4b_canonical_input_binding import (
    BindingContractError,
    BindingMode,
    DEFAULT_SCIENTIFIC_BINDING_MODE,
    construct_binding,
    validate_runtime_overlay,
    write_external_package,
)


CANONICAL = Path(r"D:\ProjectTemp\ch5-mp4a2-2009-input-binding-20260830-001\calendar_2009_primary_premodel_input.json")
CENSUS = Path(r"D:\ProjectTemp\ch5-mp4b-l3-readonly-source-binding-and-early-household-review-20260901-001\initial_zt_31province_binding_census.json")


def test_primary_mode_preserves_bytes_and_is_the_scientific_default():
    binding = construct_binding(BindingMode.PRIMARY_SOURCE_CANONICAL, CANONICAL)
    assert binding.canonical_bytes == CANONICAL.read_bytes()
    assert binding.object == json.loads(CANONICAL.read_text(encoding="utf-8"))
    assert DEFAULT_SCIENTIFIC_BINDING_MODE is BindingMode.PRIMARY_SOURCE_CANONICAL


def test_overlay_changes_only_initialized_zt_and_exact_accepted_census():
    overlay = construct_binding(BindingMode.MATLAB_CACHE_RUNTIME_PARITY_OVERLAY, CANONICAL, cache_census_path=CENSUS)
    census = overlay.field_identity["census"]
    assert census == {"equal_rows": 24, "different_rows": 7, "one_ulp_rows": 5, "two_ulp_rows": 2}
    assert overlay.field_identity["non_initialized_zt_paths_bitwise_identical"]
    changed = [row for row in overlay.overlay_table if row["replacement_applied"]]
    unchanged = [row for row in overlay.overlay_table if not row["replacement_applied"]]
    assert len(changed) == 7 and len(unchanged) == 24
    assert {row["ulp_distance"] for row in changed} == {1, 2}
    assert all(row["cache_runtime_binary64_hex"] == float(overlay.object["vectors"]["initialized_zt"][row["province_index_one_based"] - 1]).hex() for row in changed)
    assert all(row["canonical_binary64_hex"] == row["cache_runtime_binary64_hex"] for row in unchanged)


def test_missing_mode_and_implicit_cache_fallback_fail_closed():
    with pytest.raises(BindingContractError, match="explicit binding mode"):
        construct_binding(None, CANONICAL)
    with pytest.raises(BindingContractError, match="forbids cache"):
        construct_binding(BindingMode.PRIMARY_SOURCE_CANONICAL, CANONICAL, cache_census_path=CENSUS)
    with pytest.raises(BindingContractError, match="requires explicit cache"):
        construct_binding(BindingMode.MATLAB_CACHE_RUNTIME_PARITY_OVERLAY, CANONICAL)


def test_wrong_canonical_or_cache_sha_fails_closed(tmp_path):
    wrong_canonical = tmp_path / "canonical.json"
    wrong_canonical.write_bytes(CANONICAL.read_bytes() + b" ")
    with pytest.raises(BindingContractError, match="canonical SHA"):
        construct_binding(BindingMode.PRIMARY_SOURCE_CANONICAL, wrong_canonical)
    bad_census = json.loads(CENSUS.read_text(encoding="utf-8"))
    bad_census["rows"][0]["cache_provenance"]["sha256"] = "0" * 64
    bad_path = tmp_path / "census.json"
    bad_path.write_text(json.dumps(bad_census), encoding="utf-8")
    with pytest.raises(BindingContractError, match="cache SHA"):
        construct_binding(BindingMode.MATLAB_CACHE_RUNTIME_PARITY_OVERLAY, CANONICAL, cache_census_path=bad_path)


def test_non_zt_change_and_province_permutation_fail_closed():
    primary = construct_binding(BindingMode.PRIMARY_SOURCE_CANONICAL, CANONICAL)
    overlay = construct_binding(BindingMode.MATLAB_CACHE_RUNTIME_PARITY_OVERLAY, CANONICAL, cache_census_path=CENSUS)
    changed_field = deepcopy(overlay.object)
    changed_field["scalars"]["rah"] = 0.0
    with pytest.raises(BindingContractError, match="non-initialized_zt"):
        validate_runtime_overlay(primary.object, changed_field, overlay.cache_evidence)
    permuted = deepcopy(overlay.object)
    permuted["province_order"][0], permuted["province_order"][1] = permuted["province_order"][1], permuted["province_order"][0]
    with pytest.raises(BindingContractError, match="province order"):
        validate_runtime_overlay(primary.object, permuted, overlay.cache_evidence)


def test_external_package_is_no_overwrite_and_records_zero_model_calls(tmp_path):
    primary = construct_binding(BindingMode.PRIMARY_SOURCE_CANONICAL, CANONICAL)
    overlay = construct_binding(BindingMode.MATLAB_CACHE_RUNTIME_PARITY_OVERLAY, CANONICAL, cache_census_path=CENSUS)
    root = tmp_path / "package"
    paths = write_external_package(root, primary, overlay, {"command": "pytest", "passed": True, "scientific_calls": 0})
    assert set(paths) == {"binding_contract", "overlay", "table", "identity", "focused_tests", "manifest"}
    manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
    assert manifest["scientific_calls"] == {"matlab": 0, "stationary": 0, "household": 0, "hjb": 0, "kfe": 0, "mp2": 0, "mp3": 0, "comparator": 0}
    with pytest.raises(FileExistsError, match="refusing to overwrite"):
        write_external_package(root, primary, overlay, {})


def test_validation_helper_has_no_scientific_runtime_import_or_call():
    source = Path(__file__).parents[1] / "validators" / "multi_province" / "mp4b_canonical_input_binding.py"
    text = source.read_text(encoding="utf-8")
    forbidden = ["numpy", "scipy", "solve_household", "run_online_stationary", "HANK_", "compare_terminal", "subprocess"]
    assert not [token for token in forbidden if token in text]
