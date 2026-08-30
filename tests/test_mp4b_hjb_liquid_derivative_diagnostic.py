from pathlib import Path
import json
import os
import subprocess
import sys

from validators.multi_province.mp4b_hjb_liquid_derivative_diagnostic import diagnose


CANONICAL=Path(r"D:\ProjectTemp\ch5-mp4a2-2009-input-binding-20260830-001\calendar_2009_primary_premodel_input.json")
HJB=Path(r"C:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m")


def test_diagnostic_localizes_without_scientific_calls(tmp_path):
    output=tmp_path/"diagnostic.json"
    payload=diagnose(CANONICAL,HJB,output)
    assert payload["counts"]["cell_count"]==800
    assert payload["counts"]["raw_either_nonpositive"]==0
    assert payload["counts"]["processed_either_nonpositive"]==0
    assert payload["first_offending_cell"] is None
    assert payload["minimum_raw_derivative_cell"]["python_oracle_action"].startswith("proceed")
    assert payload["minimum_raw_derivative_cell"]["matlab_source_action"].startswith("floor")
    assert all(value==0 for value in payload["scientific_model_calls"].values())
    assert json.loads(output.read_text(encoding="utf-8"))["static_ordering_classification"].startswith("PYTHON_IMPLEMENTATION_ERROR")


def test_diagnostic_direct_script_bootstrap_is_zero_science(tmp_path):
    script=Path(__file__).parents[1]/"validators"/"multi_province"/"mp4b_hjb_liquid_derivative_diagnostic.py"
    output=tmp_path/"direct.json"; env=os.environ.copy(); env.pop("PYTHONPATH",None)
    completed=subprocess.run([sys.executable,str(script),str(CANONICAL),str(HJB),str(output)],
        cwd=tmp_path,env=env,text=True,capture_output=True,check=False)
    assert completed.returncode==0,completed.stderr
    payload=json.loads(output.read_text(encoding="utf-8"))
    assert payload["counts"]["raw_either_nonpositive"]==0
    assert all(value==0 for value in payload["scientific_model_calls"].values())
