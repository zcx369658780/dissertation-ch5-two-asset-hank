from pathlib import Path
import re


HELPER = Path(__file__).parents[1] / "validators" / "multi_province" / "matlab" / "mp4b_initial_labor_scalar_diagnostic.m"


def test_helper_freezes_exact_cells_parameters_and_source_identity():
    text = HELPER.read_text(encoding="utf-8")
    assert "b = [-2, 4/19]; a = [0,10]; z = [0.8,1.3];" in text
    assert "rb=0.02+0.07*(bb<0);" in text
    assert "raah=0.09" in text and "0.09*(1-0.1*(10/aa)^(-9))" in text
    assert "temp=raah^2+rb*bb+0.1; B=(1-0.05)*20*zz;" in text
    assert "params=[1,1,0.05,20,zz,0.2,temp,2];" in text
    assert "x0=B^(0.2*(1-2)/(1+2*0.2));" in text
    assert "fzero(@(l) lab_solve2(l,params),x0,options)" in text
    assert "74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20" in text


def test_template_and_assigned_row_fields_are_identical_and_eight_rows_are_fixed():
    text = HELPER.read_text(encoding="utf-8")
    fields = ["i","j","k","b","a","z","Rb","raah","tempMat","B","x0","l0","fval","exitflag","root_base"]
    template = re.search(r"template=struct\((.*?)\);", text, re.S).group(1)
    assigned = re.search(r"rows\(n\)=struct\((.*?)\);", text, re.S).group(1)
    assert re.findall(r"'([^']+)'\s*,", template) == fields
    assert re.findall(r"'([^']+)'\s*,", assigned) == fields
    assert "rows=repmat(template,1,8)" in text
    assert text.count("for i") == 3


def test_helper_is_zero_model_and_r2022b_safe_strict_no_overwrite():
    text = HELPER.read_text(encoding="utf-8")
    forbidden = (
        "HANK_2ASSETS_HJB", "KFE", "HANK_mp_1turn", "HANK_mp_1eq",
        "mpHANK_equilibrium_2000", "multi_prov_HANK_12sts",
    )
    assert not any(name in text for name in forbidden)
    assert "fopen(output_json,'x')" not in text
    assert "java.io.File(output_json)" in text
    assert "createNewFile()" in text
    assert "fopen(output_json,'w')" in text
    assert "exist(output_json,'file')" in text
    assert "stationary_model_calls',0" in text
