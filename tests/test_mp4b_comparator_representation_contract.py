import json
from pathlib import Path

import pytest

from validators.multi_province.mp4b_compare_preserved_matlab_python_final_state import (
    EXPECTED_MATLAB_SUFFIX_PROJECTION_CHANGES,
    EXPECTED_PROVINCE_COUNT,
    FIELDS,
    build_comparison_payload,
    load_preserved_matlab_state,
    project_matlab_province_name,
    validate_province_identity,
)


ROOT = Path(__file__).parents[1]
FIELD_MAP = ROOT / "validators/multi_province/mp4b_preserved_matlab_python_final_state_field_map.json"
PYTHON_TERMINAL = Path(
    r"D:\ProjectTemp\ch5-mp4b-python-only-source-postloop-reexecution-authorized-20260831-001\python_terminal_summary.json"
)


def _identity_states(raw_matlab: list[str], python: list[str]):
    return (
        [{"raw_matlab_province": name} for name in raw_matlab],
        [{"name": name} for name in python],
    )


def test_suffix_projection_is_exactly_one_final_character_only():
    assert project_matlab_province_name("北京市") == "北京"
    assert project_matlab_province_name("河北省") == "河北"
    assert project_matlab_province_name("内蒙古") == "内蒙古"
    assert project_matlab_province_name("北京市市") == "北京市"
    assert project_matlab_province_name("北京 ") == "北京 "


def test_projected_name_collision_fails_closed():
    raw = ["北京", "北京市"] + [f"x{index}" for index in range(29)]
    matlab, python = _identity_states(raw, [f"p{index}" for index in range(EXPECTED_PROVINCE_COUNT)])
    with pytest.raises(ValueError, match="projected MATLAB province names must be unique"):
        validate_province_identity(matlab, python)


def test_non_suffix_mismatch_fails_closed():
    python = [f"base{index}" for index in range(EXPECTED_PROVINCE_COUNT)]
    raw = [f"base{index}省" for index in range(EXPECTED_MATLAB_SUFFIX_PROJECTION_CHANGES)]
    raw += ["不匹配"] + python[EXPECTED_MATLAB_SUFFIX_PROJECTION_CHANGES + 1:]
    matlab, python_states = _identity_states(raw, python)
    with pytest.raises(ValueError, match="projected MATLAB province sequence"):
        validate_province_identity(matlab, python_states)


def test_durable_projected_matlab_sequence_equals_python_and_preserves_raw_evidence():
    field_map = json.loads(FIELD_MAP.read_text(encoding="utf-8"))
    matlab, matlab_categories = load_preserved_matlab_state(Path(field_map["matlab_artifact"]["path"]))
    python = json.loads(PYTHON_TERMINAL.read_text(encoding="utf-8"))["final_state"]
    keys, evidence = validate_province_identity(matlab, python)
    assert len(keys) == EXPECTED_PROVINCE_COUNT
    assert keys == [state["name"] for state in python]
    assert evidence["projection_changed_count"] == EXPECTED_MATLAB_SUFFIX_PROJECTION_CHANGES
    assert matlab_categories["wage_upper_count"] == 7
    payload = build_comparison_payload(matlab, python, 184, 184)
    first = payload["province_rows"][0]
    assert first["raw_matlab_province"] == "北京市"
    assert first["raw_python_province"] == "北京"
    assert first["comparison_key"] == "北京"
    assert tuple(first["continuous"]) == FIELDS
    assert payload["terminal_categories"]["wage_upper_count"] == {
        "matlab": 7, "python": 5, "exact": False,
    }


def test_field_map_and_excluded_aliases_remain_frozen():
    field_map = json.loads(FIELD_MAP.read_text(encoding="utf-8"))
    assert tuple(field_map["provincial_continuous_exact_name_map"]) == FIELDS
    assert set(field_map["excluded"]) == {"AtTax", "household_Lt", "At_plus_Bt"}
