"""Zero-science durability checks for the 2018 singularity diagnostic."""
from __future__ import annotations

import csv
import json
import numpy as np
import pytest
from scipy import sparse

from validators.multi_province import mp4c_2018_first_singularity_diagnostic as diagnostic
import exports.matlab_faithful_two_asset_ha as faithful


def test_phase_a_hjb_ledger_closure_is_durable_before_dummy_kfe(tmp_path, monkeypatch):
    fsync_calls = []
    original_fsync = diagnostic.os.fsync

    def record_fsync(fd):
        fsync_calls.append(fd)
        return original_fsync(fd)

    monkeypatch.setattr(diagnostic.os, "fsync", record_fsync)
    diagnostic.phase(tmp_path)

    receipt = json.loads((tmp_path / "phase_a_zero_science_test_receipt.json").read_text(encoding="utf-8"))
    rows = list(csv.DictReader((tmp_path / "hjb_return_ledger.csv").open(encoding="utf-8")))
    assert receipt["marker"] == "MP4C_2018_HJB_LEDGER_CLOSURE_REPAIR_ZERO_SCIENCE_PASS__ONE_DURABLE_2018_CHILD_AUTHORIZED"
    assert receipt["faithful_hjb_identity"] == "exports.matlab_faithful_two_asset_ha"
    assert receipt["faithful_kfe_identity"] == "exports.matlab_faithful_two_asset_ha"
    assert receipt["adapter_dummy_sequence"] == ["hjb", "kfe", "aggregate", "hjb", "kfe", "aggregate"]
    assert receipt["hjb_ledger_header_count"] == 1
    assert len(rows) == 2
    assert rows[0]["province"] == "DUMMY_A"
    assert rows[0]["hjb_converged"] == "True"
    assert rows[0]["kfe_path"] == "HJB_CONVERGED"
    assert rows[1]["province"] == "DUMMY_B"
    assert rows[1]["hjb_converged"] == "False"
    assert rows[1]["kfe_path"] == "MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE"
    assert len(fsync_calls) >= 2
    assert receipt["scientific_calls"] == {"stationary": 0, "household": 0, "HJB": 0, "KFE": 0, "MATLAB": 0, "R_PLM": 0}


def test_capture_flushes_raw_evidence_then_postmortem_is_separate(tmp_path):
    capture = diagnostic.Capture(tmp_path)
    operator = sparse.csr_matrix([[0.0]])
    capture.ctx = {"province": "DUMMY", "global_household_call_number": 1}
    capture.hjb = {"hjb_converged": False, "kfe_path": "MATLAB_FAITHFUL_POSTLOOP_AFTER_HJB_NONCONVERGENCE"}
    capture.before(operator)

    with pytest.raises(diagnostic.FirstSingularityCaptured):
        capture.solve(lambda: faithful.linalg.spsolve(operator, np.array([1.0])))

    raw = (
        "first_singularity_operator_A.npz",
        "first_singularity_operator_transpose.npz",
        "first_singularity_contaminated_matrix.npz",
        "first_singularity_rhs.npy",
        "first_singularity_raw_solve_vector.npy",
        "first_singularity_warning_and_traceback.txt",
    )
    assert all((tmp_path / name).is_file() for name in raw)
    assert not (tmp_path / "postmortem_rank_nullity.json").exists()

    diagnostic.postmortem(tmp_path)
    assert (tmp_path / "postmortem_operator_summary.json").is_file()
    assert (tmp_path / "postmortem_scc_closed_classes.json").is_file()
    assert (tmp_path / "postmortem_rank_nullity.json").is_file()
