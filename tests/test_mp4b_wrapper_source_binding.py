from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WRAPPER = ROOT / "validators/multi_province/matlab/mp4b_calendar2009_stationary_wrapper.m"
RUNNER = ROOT / "validators/multi_province/matlab/mp4b_execute_once.m"


def test_source_binding_repair_is_explicit_and_fail_closed() -> None:
    source = WRAPPER.read_text(encoding="utf-8")
    assert "global N_prov;" in source
    assert "N_prov = 31;" in source
    assert "~isequal(N_prov,31)" in source
    assert "addpath(protected_root)" in source
    assert "startsWith(string(resolved),protected_root)" in source
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
