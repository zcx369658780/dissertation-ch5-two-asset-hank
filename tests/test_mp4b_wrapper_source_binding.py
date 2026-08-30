from pathlib import Path
from validators.multi_province.mp4b_path_guard import helper_is_in_verified_pair


ROOT = Path(__file__).resolve().parents[1]
WRAPPER = ROOT / "validators/multi_province/matlab/mp4b_calendar2009_stationary_wrapper.m"
RUNNER = ROOT / "validators/multi_province/matlab/mp4b_execute_once.m"


def test_source_binding_repair_is_explicit_and_fail_closed() -> None:
    source = WRAPPER.read_text(encoding="utf-8")
    assert "global N_prov;" in source
    assert "N_prov = 31;" in source
    assert "~isequal(N_prov,31)" in source
    assert "addpath(protected_root)" in source
    assert "allowed_roots" in source
    assert "fileparts(resolved)" in source
    assert "fileread(logical_file),fileread(physical_file)" in source
    assert "data_year = 10;" in source
    assert "data_MAT_index = 1;" in source
    assert "multi_prov_HANK_12sts" not in source.split("% The protected annual wrapper")[1]


def test_profiler_only_observability_counts_household_calls() -> None:
    source = RUNNER.read_text(encoding="utf-8")
    assert "profile on" in source and "profile off" in source
    assert "HANK_2ASSETS_HJB" in source
    assert "HANK_mp_1turn" in source
    forbidden = ("N_prov=", "reg_threshold=", "max3iter=", "data_year=")
    assert all(token not in source.replace(" ", "") for token in forbidden)


def test_finite_logical_physical_pair_only() -> None:
    logical = r"C:\MatlabProgram\model"
    physical = r"D:\MatlabProgram\model"
    assert helper_is_in_verified_pair(r"C:\MatlabProgram\model\HANK_mp_1eq.m", logical, physical)
    assert helper_is_in_verified_pair(r"D:\MatlabProgram\model\HANK_mp_1eq.m", logical, physical)
    assert not helper_is_in_verified_pair(r"D:\MatlabProgram\sibling\HANK_mp_1eq.m", logical, physical)
    assert not helper_is_in_verified_pair(r"D:\unrelated\HANK_mp_1eq.m", logical, physical)
    assert not helper_is_in_verified_pair(r"C:\other\HANK_mp_1eq.m", logical, physical)


def test_no_active_mp4b_helper_uses_char_plus_suffix() -> None:
    matlab_root = ROOT / "validators/multi_province/matlab"
    for path in matlab_root.glob("mp4b*.m"):
        source = path.read_text(encoding="utf-8")
        assert "+'.m'" not in source
        assert '+".m"' not in source
    wrapper = WRAPPER.read_text(encoding="utf-8")
    smoke = (matlab_root / "mp4b_path_equivalence_smoke.m").read_text(encoding="utf-8")
    assert "[required_helpers{helper_index} '.m']" in wrapper
    assert "[helpers{i} '.m']" in smoke
