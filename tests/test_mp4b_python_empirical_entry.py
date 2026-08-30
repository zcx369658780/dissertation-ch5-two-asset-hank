from pathlib import Path
import json
import numpy as np
import pytest

from validators.multi_province.mp4b_python_empirical import _write_json, load_entry_state


CANONICAL=Path(r"D:\ProjectTemp\ch5-mp4a2-2009-input-binding-20260830-001\calendar_2009_primary_premodel_input.json")


def test_entry_prepares_exact_31_source_states_without_solving():
    canonical,states=load_entry_state(CANONICAL)
    assert len(states)==31
    assert [s["name"] for s in states]==canonical["province_order"]
    assert all(s["Kt"]==s["Kt0"] and s["Lt"]==s["N"] for s in states)
    assert all(s["ramin"]==0.02 and s["ramax"]==0.09 for s in states)


def test_import_has_no_output_or_model_side_effect(tmp_path):
    assert list(tmp_path.iterdir())==[]


def test_json_persistence_handles_arrays_and_is_no_overwrite(tmp_path):
    target=tmp_path/"evidence.json"
    _write_json(target,{"array":np.array([1.0,2.0]),"flag":np.bool_(True)})
    assert json.loads(target.read_text(encoding="utf-8"))=={"array":[1.0,2.0],"flag":True}
    with pytest.raises(FileExistsError,match="refusing to overwrite"):
        _write_json(target,{"changed":True})


def test_entry_freezes_source_controller_and_no_forbidden_runtime_imports():
    source=Path(__file__).parents[1]/"validators"/"multi_province"/"mp4b_python_empirical.py"
    text=source.read_text(encoding="utf-8")
    assert "solve_household_steady_state" in text and "run_online_stationary" in text
    assert "solve_root" not in text and "chapter5_model" not in text
    assert "1e-9,500,True" in text
    assert "productivity[:,None]-productivity[None,:]" in text
    assert "productivity[:,None]+productivity[None,:]" in text
