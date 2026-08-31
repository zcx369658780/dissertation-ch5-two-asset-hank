import ntpath
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "validators/multi_province/matlab/mp4b_raw_vb_hank3_foc_edge_diagnostic.m"
TEXT = HELPER.read_text(encoding="utf-8")


def test_frozen_scientific_content_is_exact():
    assert "function mp4b_raw_vb_hank3_foc_edge_diagnostic(run_root, logical_root, physical_root)" in TEXT
    assert "ids = {'localized_BB','localized_BF','localized_FB','localized_FF', ..." in TEXT
    assert "'positive_pb','negative_pb','zero_pb_positive_pa','zero_pb_negative_pa', ..." in TEXT
    assert "'zero_pa_zero_pb','zero_a_negative_pb'};" in TEXT
    assert "pa = [0.0183013418028827,0.029712870660726632,0.0183013418028827,0.029712870660726632, ..." in TEXT
    assert "    1.5,0.5,1,-1,0,1];" in TEXT
    assert "pb = [0.0036470322698923963,0.0036470322698923963,-0.014003744365506235,-0.014003744365506235, ..." in TEXT
    assert "    1,-1,0,0,0,-1];" in TEXT
    assert "a = [9.473684210526315,9.473684210526315,9.473684210526315,9.473684210526315, ..." in TEXT
    assert "    1,1,1,1,1,0];" in TEXT
    assert "chi = struct('chi0',0.1,'chi1',2,'fixcost',0,'fixcost2',0,'a_bar',0.5);" in TEXT
    assert "value = HANK3_FOC(dummy,chi,pa(k),pb(k),a(k),0);" in TEXT
    assert "if isnan(x); out='NaN'; elseif isinf(x) && x>0; out='+Inf'; ..." in TEXT
    assert "elseif isinf(x); out='-Inf'; else; out='finite'; end" in TEXT
    assert "elseif isinf(x); out='-Inf'; else; out=sprintf('%.17g',x); end" in TEXT
    assert "else; out=sprintf('%.17g',x); end" in TEXT


def test_exclusive_fresh_root_and_atomic_artifacts():
    assert "fileparts(normalized_run_root)" in TEXT
    assert 'normalize_root("D:\\ProjectTemp")' in TEXT
    assert "run_dir=java.io.File(char(run_root));" in TEXT
    assert "if ~run_dir.mkdir()" in TEXT
    assert "run_root already exists" in TEXT
    assert "if isfile(run_root) || isfolder(run_root)" in TEXT
    assert "fullfile(run_root,'failure.json')" in TEXT
    assert "fullfile(run_root,'success_manifest.json')" in TEXT
    assert "file.createNewFile()" in TEXT


def test_run_root_contract_rejects_sibling_nested_and_existing_shapes():
    def direct_fresh_child(path: str, exists: bool = False) -> bool:
        normalized = path.replace("/", "\\").rstrip("\\").lower()
        return ntpath.dirname(normalized) == r"d:\projecttemp" and not exists

    assert direct_fresh_child(r"D:\ProjectTemp\fresh-run")
    assert not direct_fresh_child(r"D:\ProjectTemp-sibling\fresh-run")
    assert not direct_fresh_child(r"D:\ProjectTemp\nested\fresh-run")
    assert not direct_fresh_child(r"D:\ProjectTemp\fresh-run", exists=True)


def test_first_error_is_persisted_without_numerical_substitution():
    call = "value = HANK3_FOC(dummy,chi,pa(k),pb(k),a(k),0);"
    assert "catch protected_error" in TEXT
    assert "'case_index',k" in TEXT
    assert "protected_error.identifier" in TEXT
    assert "protected_error.message" in TEXT
    assert "'logical_protected_root',logical_root,'physical_protected_root',physical_root" in TEXT
    assert "'resolved_helper_path',resolved,'resolved_helper_sha256',resolved_sha" in TEXT
    assert "'attempted_protected_calls',attempted_calls" in TEXT
    assert "'completed_protected_calls',completed_calls" in TEXT
    assert "'call_ledger',complete_call_ledger(attempted_calls,completed_calls)" in TEXT
    assert "write_new_json(fullfile(run_root,'failure.json'),failure);" in TEXT
    assert "rethrow(protected_error);" in TEXT
    assert TEXT.index("attempted_calls=attempted_calls+1;") < TEXT.index(call)
    assert TEXT.index(call) < TEXT.index("completed_calls=completed_calls+1;")
    assert "NaN" not in TEXT[TEXT.index("catch protected_error"):TEXT.index("rethrow(protected_error);")]


def test_per_row_source_identity_and_complete_ledgers():
    assert "'resolved_helper_path','','resolved_helper_sha256',''" in TEXT
    assert "'resolved_helper_path',resolved,'resolved_helper_sha256',resolved_sha" in TEXT
    required = (
        "matlab_scalar_batches", "HANK3_FOC_attempted_calls", "HANK3_FOC_completed_calls",
        "matlab_HJB", "matlab_KFE", "matlab_household", "matlab_multi_province",
        "matlab_stationary", "matlab_GE", "python_local_policy", "python_HJB",
        "python_KFE", "python_household", "python_stationary",
        "old_50_state_HJB_parity", "Beijing_household_parity", "MP2_empirical",
        "MP3_empirical", "annual_batch", "shocks", "transition", "dynamics",
        "IRF", "R5", "Results",
    )
    for field in required:
        assert f"'{field}'" in TEXT
    assert TEXT.count("complete_call_ledger(attempted_calls,completed_calls)") >= 2
    ledger_body = TEXT[TEXT.index("function ledger=complete_call_ledger"):TEXT.index("function out=file_sha256")]
    for field in required[3:]:
        assert re.search(rf"'{re.escape(field)}',0(?:,|\))", ledger_body)
    assert "'matlab_scalar_batches',1" in ledger_body


def test_exact_junction_guard_and_forbidden_patterns():
    assert "verify_exact_junction" in TEXT
    assert "LinkType -eq ''Junction''" in TEXT
    assert "$t.Count -eq 1" in TEXT
    assert "D:\\MatlabProgram" in TEXT
    assert "finite_root_membership" in TEXT
    assert "sibling_root_rejected" in TEXT
    assert "unrelated_root_rejected" in TEXT
    for forbidden in ("canonical_root", "getCanonicalPath", "startsWith", "contains(", "strfind(", "regexp("):
        assert forbidden not in TEXT


def test_no_forbidden_scientific_or_production_route_is_introduced():
    allowed_call = "HANK3_FOC(dummy,chi,pa(k),pb(k),a(k),0);"
    assert TEXT.count("HANK3_FOC(") == 1
    assert allowed_call in TEXT
    for forbidden_call in (
        "HANK_2ASSETS_HJB(", "HANK3_cost(", "lab_solve2(", "KFE(",
        "stationary_runtime(", "mp4b_path_equivalence_smoke(",
    ):
        assert forbidden_call not in TEXT
    for forbidden_path in (
        "src/ch5_two_asset_hank", "exports/matlab_faithful_two_asset_ha.py",
        "corrected/reference", "chapter5_model", "MP2/", "MP3/",
    ):
        assert forbidden_path not in TEXT
