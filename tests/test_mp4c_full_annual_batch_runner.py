from __future__ import annotations
import json
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import pytest
from scipy.io import loadmat
from validators.multi_province import mp4c_python_annual_production as worker
from validators.multi_province import mp4c_run_full_annual_batch as batch

def test_exact_calendar_scope_and_scheduler_years():
    assert worker.SUPPORTED_YEARS == batch.YEARS == tuple(range(2009, 2024))
    assert len(batch.YEARS) == 15 and batch.DEFAULT_WORKERS == 4

@pytest.mark.parametrize("year", range(2009, 2024))
def test_all_calendar_bindings_are_exact(year):
    binding=worker.empirical.DecoupledAnnualIndex.for_calendar_year(year)
    assert (binding.analysis_index,binding.workbook_data_row_index,binding.data_mat_index,binding.output_filename_year,binding.regression_vintage_key)==(year-2008,year-1999,year-2008,year,year-1999)

def test_frozen_scientific_ceilings_and_zero_reruns():
    assert worker.empirical.MAX_OUTER_TURNS == 250
    assert worker.empirical.MAX_HOUSEHOLD_CALLS == 7750

def test_thread_environment_is_forced_to_one(monkeypatch):
    for key in worker.THREAD_ENV: monkeypatch.setenv(key, "9")
    env=batch.worker_env()
    assert all(env[key] == "1" for key in worker.THREAD_ENV)

def test_complete_31x20_serializer():
    states=tuple({"name":f"p{i}",**{f:float(i+1) for f in worker.FINAL_FIELDS}} for i in range(31))
    rows=worker.serialize_final_state(states)
    assert len(rows)==31 and list(rows[0])==["name",*worker.FINAL_FIELDS]

def test_serializer_rejects_missing_or_nonfinite():
    with pytest.raises(ValueError): worker.serialize_final_state(tuple())
    states=[{"name":f"p{i}",**{f:1.0 for f in worker.FINAL_FIELDS}} for i in range(31)];states[0]["Ct"]=np.nan
    with pytest.raises(ValueError,match="non-finite"):worker.serialize_final_state(tuple(states))

def test_lt_mat_orientation_contract():
    value=np.arange(31*31,dtype=float).reshape(31,31)
    assert worker.validate_lt_mat(value,[f"p{i}" for i in range(31)])[2,3]==value[2,3]
    contract=json.loads((worker.REPO_ROOT/"validators/multi_province/matlab_persistence_contract.json").read_text(encoding="utf-8"))
    assert contract["ltmat_workbook"]["orientation"]=="destination_row_x_origin_column"

def _fake_household():
    a=np.ones((2,2,2));hjb=SimpleNamespace(value=a,initial_value=a,consumption=a,labor=a,transfer=a,adjustment_cost=a,effective_illiquid_return=a,mu_a=a,mu_b=a,utility=a,liquid_label=np.full(a.shape,"F"),transfer_label=np.full(a.shape,"B"),iterations=3,converged=True,convergence_statistic=1e-9)
    return SimpleNamespace(hjb=hjb,kfe=SimpleNamespace(density=a))

def test_checkpoint_schema_and_npz_mat_roundtrip(tmp_path:Path,monkeypatch):
    grid=SimpleNamespace(b=np.array([0.,1.]),a=np.array([0.,1.]),z=np.array([.8,1.3]),switch_matrix=np.eye(2))
    items=[worker.extract_household_checkpoint(_fake_household(),grid,f"p{i}") for i in range(31)]
    monkeypatch.setattr(worker,"scientific_identities",lambda:{"x":"Y"})
    manifest=worker.persist_checkpoint(tmp_path,2009,"A",worker.empirical.SOURCE_HASHES,[f"p{i}" for i in range(31)],items,"T")
    with np.load(tmp_path/"final_household_restart.npz") as payload: assert payload["p00_value"].shape==(2,2,2)
    mat=loadmat(tmp_path/"Python_Multi_Province_12sts_2009.mat");assert mat["p00_value"].shape==(2,2,2)
    assert manifest["schema"]==worker.CHECKPOINT_SCHEMA

def test_terminal_only_source_has_no_per_turn_writes():
    source=Path(worker.__file__).read_text(encoding="utf-8")
    assert "turn_{iteration" not in source and "household_inputs.json" not in source and "household_outputs.json" not in source

def test_resume_requires_exact_success_hashes(tmp_path:Path,monkeypatch):
    yd=tmp_path/"year";yd.mkdir();artifact=yd/"a";artifact.write_text("ok")
    monkeypatch.setattr(worker,"scientific_identities",lambda:{"code":"ID"})
    marker={"schema":"CH5_MP4C_YEAR_SUCCESS_V2","representation":worker.runtime_cache.REPRESENTATION,"year":2009,"status":"SOURCE_CONVERGED","runtime_input_sha256":"C","runtime_cache_sha256":worker.runtime_cache.EXPECTED_CACHE_SHA256,"scientific_code_identities":{"code":"ID"},"checkpoint_schema":worker.CHECKPOINT_SCHEMA,"outputs":{"a":{"sha256":batch.sha(artifact),"bytes":2}}}
    (yd/"SUCCESS.json").write_text(json.dumps(marker),encoding="utf-8")
    assert batch.valid_success(yd,2009,"C")
    artifact.write_text("changed")
    assert not batch.valid_success(yd,2009,"C")

def test_incompatible_marker_fails_closed(tmp_path:Path):
    (tmp_path/"SUCCESS.json").write_text("{}")
    assert not batch.valid_success(tmp_path,2009,"X")

@pytest.mark.parametrize("exit_code,status",[(0,"PASS"),(2,"FAIL"),(1,"SHARED_FAIL")])
def test_worker_exit_classification_supports_failure_isolation(monkeypatch,tmp_path:Path,exit_code,status):
    monkeypatch.setattr(batch.subprocess,"run",lambda *a,**k:SimpleNamespace(returncode=exit_code))
    assert batch.launch_year(2009,tmp_path/"c",tmp_path/"cache",tmp_path/"y")["status"]==status

def test_progress_contract_is_present():
    source=Path(batch.__file__).read_text(encoding="utf-8")
    for token in ("running=", "PASS=", "FAIL=", "elapsed="): assert token in source
    assert "BLOCKED_SHARED_FAILURE" in source

def test_launcher_is_static_and_does_not_embed_science():
    text=(worker.REPO_ROOT/"scripts/run_mp4c_full_annual_batch.ps1").read_text(encoding="utf-8")
    assert "-Workers" not in text or "$Workers" in text
    assert "matlab.exe" not in text.lower() and "mp4c_run_full_annual_batch.py" in text
    assert "数据估计结果" not in text
    assert "*_1000_100_0.mat" in text and "Count -ne 1" in text

def test_protected_paths_are_not_write_targets():
    for path in (Path(worker.__file__),Path(batch.__file__),worker.REPO_ROOT/"scripts/run_mp4c_full_annual_batch.ps1"):
        text=path.read_text(encoding="utf-8")
        assert "C:\\MatlabProgram" not in text and "D:\\MatlabProgram" not in text

def test_2009_reference_identity_is_frozen():
    assert worker.empirical.ACCEPTED_2009_CANONICAL_SHA=="507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48"

def test_source_hashes_are_exact():
    assert set(worker.empirical.SOURCE_HASHES.values())=={"C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929","A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68","26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566"}
