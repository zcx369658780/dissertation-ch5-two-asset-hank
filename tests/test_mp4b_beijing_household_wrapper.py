from __future__ import annotations

import re
from pathlib import Path, PureWindowsPath


ROOT = Path(__file__).resolve().parents[1]
WRAPPER = ROOT / "validators/multi_province/matlab/mp4b_beijing_household_wrapper.m"
TEXT = WRAPPER.read_text(encoding="utf-8")
LOGICAL = PureWindowsPath(r"C:\MatlabProgram\2023年12月2日 多省份神经网络HANK")
PHYSICAL = PureWindowsPath(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK")


def normalized(path: PureWindowsPath) -> str:
    return str(path).replace("/", "\\").rstrip("\\").lower()


def allowed(candidate: PureWindowsPath) -> bool:
    return normalized(candidate) in {normalized(LOGICAL), normalized(PHYSICAL)}


def exact_ordered_pair(logical: PureWindowsPath, physical: PureWindowsPath) -> bool:
    return normalized(logical) == normalized(LOGICAL) and normalized(physical) == normalized(PHYSICAL)


def test_smoke_return_dominates_protected_call() -> None:
    smoke = TEXT.index('if mode == "smoke"')
    return_at = TEXT.index("    return", smoke)
    call = TEXT.index("manifest = HANK_2ASSETS_HJB(")
    assert smoke < return_at < call
    protected = ("HANK_mp_1turn(", "HANK_mp_1eq(", "mpHANK_equilibrium_2000(",
                 "multi_prov_HANK_12sts(")
    assert all(token not in TEXT for token in protected)


def test_r2022b_no_overwrite_reservation_and_complete_write() -> None:
    assert "fopen(path,'x')" not in TEXT
    assert ".mkdir()" in TEXT and ".createNewFile()" in TEXT
    assert "fopen(path,'w')" in TEXT
    assert "count ~= numel(encoded)" in TEXT and "close_status ~= 0" in TEXT
    assert "run_root already exists" in TEXT


def test_exact_source_binding_and_negative_paths() -> None:
    assert exact_ordered_pair(LOGICAL, PHYSICAL)
    assert not exact_ordered_pair(PHYSICAL, PHYSICAL)
    assert not exact_ordered_pair(LOGICAL, LOGICAL)
    assert not exact_ordered_pair(PHYSICAL, LOGICAL)
    assert allowed(LOGICAL) and allowed(PHYSICAL)
    assert not allowed(PureWindowsPath(str(PHYSICAL) + "-sibling"))
    assert not allowed(PureWindowsPath(r"D:\MatlabProgram\other-model"))
    forbidden = ("startsWith", "contains(", "getCanonicalPath", "canonical_root")
    assert all(token not in TEXT for token in forbidden)
    assert "target_count',1" in TEXT and "sole_target','D:\\MatlabProgram'" in TEXT
    assert "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE" in TEXT


def test_manifest_schema_has_marker_identities_and_complete_zero_ledger() -> None:
    required = (
        "MP4B_BEIJING_MATLAB_HOUSEHOLD_WRAPPER_ZERO_CALL_SMOKE_PASS",
        "wrapper_path", "wrapper_sha256", "logical_protected_root", "physical_protected_root",
        "resolved_hjb_path", "resolved_hjb_sha256", "same_input_contract_path",
        "same_input_contract_sha256", "matlab_version", "matlab_release",
        "HANK_2ASSETS_HJB_calls", "HJB_calls", "KFE_calls", "scientific_household_calls",
        "multi_province_calls", "stationary_calls", "MP2_calls", "MP3_calls",
        "annual_batch_calls", "shocks_calls", "transition_calls", "dynamics_calls",
        "IRF_calls", "R5_calls", "Results_calls",
    )
    assert all(token in TEXT for token in required)
    ledger = TEXT[TEXT.index("function ledger = complete_zero_ledger()"):TEXT.index("function value = normalize_root")]
    assert not re.search(r"_calls',\s*[1-9]", ledger)


def test_fresh_root_is_exact_direct_child_contract() -> None:
    assert 'normalize_root(run_parent) ~= normalize_root("D:\\ProjectTemp")' in TEXT
    assert "strlength(run_name + run_ext) == 0" in TEXT
    assert "mkdir" in TEXT and "rmdir" not in TEXT and "delete(" not in TEXT
