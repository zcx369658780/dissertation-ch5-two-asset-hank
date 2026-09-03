"""Zero-science durability checks for the 2018 singularity diagnostic."""
from __future__ import annotations

import numpy as np
import pytest
from scipy import sparse

from validators.multi_province import mp4c_2018_first_singularity_diagnostic as diagnostic
import exports.matlab_faithful_two_asset_ha as faithful


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
