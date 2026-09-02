from __future__ import annotations
import json
from pathlib import Path
import h5py
import numpy as np
import pytest
from validators.multi_province import mp4c_matlab_runtime_cache as cache
from validators.multi_province import mp4c_python_annual_empirical as empirical
from ch5_two_asset_hank.multi_province.annual import _xlsx_sheet_rows,DecoupledAnnualIndex

REPO=Path(__file__).resolve().parents[1]
MAT=REPO/"data_local/matlab_runtime_snapshot/数据估计结果_1000_100_0.mat"
DATA=REPO/"data_local/matlab_primary_source_snapshot"

def test_owner_designated_cache_identity_and_structure():
    structure=cache.inspect_cache(MAT)
    assert structure["cache_sha256"]==cache.EXPECTED_CACHE_SHA256
    assert structure["top_level_variables"]==["mydata2"] and structure["entry_count"]==15

@pytest.mark.parametrize("year",range(2009,2024))
def test_all_fifteen_runtime_inputs_map_exactly_and_are_admissible(year):
    item=cache.load_runtime_year(MAT,year)
    assert item["representation"]==cache.REPRESENTATION
    assert item["cache_entry_index_matlab_1based"]==item["cache_data_year_index_matlab_1based"]==year-2008
    assert len(item["province_order"])==31
    assert all(np.isfinite(np.asarray(v,float)).all() for v in item["vectors"].values())
    assert all(v>0 for v in item["vectors"]["CAP"])

@pytest.mark.parametrize("year",(2022,2023))
def test_2022_2023_runtime_capital_is_positive_while_workbook_negatives_are_preserved(year):
    runtime=cache.load_runtime_year(MAT,year)
    assert min(runtime["vectors"]["CAP"])>0
    rows=_xlsx_sheet_rows(DATA/"2000年后各省数据_填充NA.xlsx","总资本存量")
    physical=DecoupledAnnualIndex.for_calendar_year(year).workbook_data_row_index+1
    assert any(float(rows[physical][column])<0 for column in range(3,34))

def test_wrong_sha_fails_closed():
    with pytest.raises(ValueError,match="SHA mismatch"):cache.load_runtime_year(MAT,2009,"0"*64)

def test_wrong_top_level_schema_fails_closed(tmp_path:Path):
    bad=tmp_path/"bad.mat"
    with h5py.File(bad,"w") as h5:h5.create_dataset("wrong",data=[1])
    with pytest.raises(ValueError):cache.inspect_cache(bad,cache.file_sha256(bad))

def test_wrong_year_mapping_fails_closed():
    with pytest.raises(ValueError):cache.load_runtime_year(MAT,2024)

def test_wrong_province_order_fails_closed(monkeypatch):
    monkeypatch.setattr(cache,"PROVINCE_ORDER",tuple(reversed(cache.PROVINCE_ORDER)))
    with pytest.raises(ValueError,match="province order"):cache.load_runtime_year(MAT,2009)

def test_distance_support_is_exact_and_no_mixed_runtime_fallback():
    item=cache.add_runtime_support(cache.load_runtime_year(MAT,2009),distance_workbook=DATA/"中国各省省会地理距离矩阵.xlsx",distance_sha256=empirical.SOURCE_HASHES["中国各省省会地理距离矩阵.xlsx"],max_sigmau=.5)
    assert np.asarray(item["runtime_support"]["sigmau_destination_origin"]).shape==(31,31)
    text=(REPO/"validators/multi_province/mp4c_python_annual_production.py").read_text(encoding="utf-8")
    assert "load_primary_annual_input" not in text and "load_runtime_year" in text

def test_runtime_entry_states_are_complete_and_finite():
    item=cache.load_runtime_year(MAT,2009);scalars=empirical.accepted_source_scalars().__dict__
    states=cache.entry_states(item,scalars)
    assert len(states)==31 and all(state["Kt0"]>0 for state in states)

def test_cache_copy_is_byte_identical_to_protected_source():
    protected=Path(r"C:\MatlabProgram\2023年12月2日 多省份神经网络HANK\数据估计结果_1000_100_0.mat")
    assert cache.file_sha256(protected)==cache.file_sha256(MAT)==cache.EXPECTED_CACHE_SHA256
