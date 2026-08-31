import json
from pathlib import Path

from validators.multi_province.mp4b_compare_preserved_matlab_python_final_state import (
    FIELDS, load_preserved_matlab_state,
)


ROOT = Path(__file__).parents[1]
FIELD_MAP = ROOT / "validators/multi_province/mp4b_preserved_matlab_python_final_state_field_map.json"


def test_field_map_is_frozen_before_python_output_and_excludes_invalid_aliases():
    payload = json.loads(FIELD_MAP.read_text(encoding="utf-8"))
    assert payload["marker"] == "MP4B_PRESERVED_MATLAB_PYTHON_FINAL_STATE_FIELD_MAP_FROZEN"
    assert payload["frozen_before_python_output"] is True
    assert tuple(payload["provincial_continuous_exact_name_map"]) == FIELDS
    assert set(payload["national_sums"]) == {"Ct", "At", "Bt", "Yt"}
    assert set(payload["excluded"]) == {"AtTax", "household_Lt", "At_plus_Bt"}


def test_preserved_matlab_schema_exposes_exact_31_province_mapped_state():
    payload = json.loads(FIELD_MAP.read_text(encoding="utf-8"))
    states, categories = load_preserved_matlab_state(Path(payload["matlab_artifact"]["path"]))
    assert len(states) == 31 and len({state["name"] for state in states}) == 31
    assert all(set(FIELDS).issubset(state) for state in states)
    assert categories["final_household_converged_count"] == 31
    assert categories["wage_upper_count"] == 7
    assert categories["wage_lower_count"] == 17
