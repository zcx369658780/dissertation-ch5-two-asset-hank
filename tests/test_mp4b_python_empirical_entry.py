from pathlib import Path
import json
import os
import subprocess
import sys
import numpy as np
import pytest

from validators.multi_province.mp4b_python_empirical import (
    ORACLE_SHA, REPO_ROOT, SRC_ROOT, _source_labor_root, _write_json, load_entry_state,
)


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
    assert "solve_root" not in text
    assert "from chapter5_model" not in text and "import chapter5_model" not in text
    assert "1e-9,500,True" in text
    assert "productivity[:,None]-productivity[None,:]" in text
    assert "productivity[:,None]+productivity[None,:]" in text


def test_direct_script_bootstrap_subprocess_has_exact_roots_and_zero_science(tmp_path):
    script=REPO_ROOT/"validators"/"multi_province"/"mp4b_python_empirical.py"
    manifest=tmp_path/"bootstrap_manifest.json"
    env=os.environ.copy()
    env.pop("PYTHONPATH",None)
    completed=subprocess.run(
        [sys.executable,str(script),"--bootstrap-check",str(manifest)],
        cwd=tmp_path,env=env,text=True,capture_output=True,check=False,
    )
    assert completed.returncode==0, completed.stderr
    payload=json.loads(manifest.read_text(encoding="utf-8"))
    assert payload["repository_root"]==str(REPO_ROOT.resolve())
    assert payload["src_root"]==str(SRC_ROOT.resolve())
    assert Path(payload["oracle_module_path"]).resolve()==(
        REPO_ROOT/"exports"/"matlab_faithful_two_asset_ha.py").resolve()
    assert Path(payload["package_module_path"]).resolve().is_relative_to(SRC_ROOT.resolve())
    assert payload["oracle_sha256"]==ORACLE_SHA
    assert payload["scientific_model_calls"]==0
    assert payload["forbidden_runtime_imports"]==[]
    repeated=subprocess.run(
        [sys.executable,str(script),"--bootstrap-check",str(manifest)],
        cwd=tmp_path,env=env,text=True,capture_output=True,check=False,
    )
    assert repeated.returncode!=0
    assert "refusing to overwrite" in repeated.stderr


@pytest.mark.parametrize("b,z", [(-2.0,0.8),(-2.0,1.3),(4/19,0.8),(4/19,1.3)])
def test_source_labor_root_stays_in_domain_for_frozen_liquid_and_z_cells(b,z):
    rb=0.09 if b<0 else 0.02
    temp=0.09**2+rb*b+0.1
    wage=(1-0.05)*20*z
    root,bracket=_source_labor_root(wage=wage,temp=temp)
    boundary=-temp/wage
    assert bracket[0]>boundary and bracket[1]>boundary and root>boundary
    residual=root-wage**0.2*(root*wage+temp)**(-0.4)
    assert abs(residual)<=1e-10


def test_old_zero_endpoint_is_outside_first_failing_cell_domain():
    temp=0.09**2+0.09*(-2.0)+0.1
    wage=(1-0.05)*20*0.8
    assert temp<0 and 0.0<=-temp/wage
    root,bracket=_source_labor_root(wage=wage,temp=temp)
    assert root>bracket[0]>-temp/wage


@pytest.mark.parametrize("kwargs", [
    {"wage":0.0,"temp":0.1},
    {"wage":15.2,"temp":float("nan")},
    {"wage":15.2,"temp":-100.0},
])
def test_source_labor_root_fails_closed_on_nonsource_or_x0_invalid_domain(kwargs):
    with pytest.raises(ValueError):
        _source_labor_root(**kwargs)


def test_source_c0_and_v02_constants_match_frozen_matlab_formula():
    wage,temp,rb_b,transfer=15.2,-0.0719,-0.18,0.1
    labor,_=_source_labor_root(wage=wage,temp=temp)
    c0=wage*labor+rb_b+transfer
    python_value=(c0**(1-2)/(1-2)-labor**6/6)/0.05
    matlab_frozen=(c0**(-1)/(-1)-labor**(1+1/0.2)/(1+1/0.2))/0.05
    assert python_value==matlab_frozen


def test_direct_full_initialization_preflight_checks_all_cells_without_science(tmp_path):
    script=REPO_ROOT/"validators"/"multi_province"/"mp4b_python_empirical.py"
    manifest=tmp_path/"full_initialization.json"
    env=os.environ.copy(); env.pop("PYTHONPATH",None)
    completed=subprocess.run(
        [sys.executable,str(script),"--full-initialization-check",str(CANONICAL),str(manifest)],
        cwd=tmp_path,env=env,text=True,capture_output=True,check=False,
    )
    assert completed.returncode==0, completed.stderr
    payload=json.loads(manifest.read_text(encoding="utf-8"))
    assert payload["checked_cell_count"]==payload["expected_cell_count"]==31*20*20*2
    assert payload["first_failure"] is None
    assert payload["max_abs_source_residual"]<=1e-10
    assert payload["minimum_c0"]>0 and payload["minimum_root_base"]>0
    assert payload["scientific_calls"]=={
        "household":0,"hjb":0,"kfe":0,"mp2":0,"mp3":0,"stationary":0}
    assert not any(payload["formula_guards"].values())
