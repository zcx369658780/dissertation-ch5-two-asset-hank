"""Synthetic/static tests; no scientific solver or private workbook is used."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from validators.multi_province.corrected_2018_single_turn import run
from validators.multi_province.corrected_2018_single_turn import finalize


def test_column_requires_one_prefix_match() -> None:
    assert run._column({"Final-use GDP (unit)": 3.0}, "Final-use GDP") == 3.0
    with pytest.raises(ValueError):
        run._column({"x": 1.0}, "Final-use GDP")


def test_json_writer_refuses_overwrite_and_serializes_numpy(tmp_path: Path) -> None:
    path = tmp_path / "receipt.json"
    run.write_json(path, {"x": np.array([1.0]), "y": np.float64(2.0)})
    assert json.loads(path.read_text(encoding="utf-8")) == {"x": [1.0], "y": 2.0}
    with pytest.raises(FileExistsError):
        run.write_json(path, {})


def test_runtime_verdict_contract_is_closed() -> None:
    assert run.VERDICT_PASS == "CORRECTED_2018_SINGLE_TURN_PASS__FULL_ORDERED_TURN_COMPLETED"
    assert run.VERDICT_HOUSEHOLD == "CORRECTED_2018_SINGLE_TURN_FAIL__HOUSEHOLD_OR_NUMERICAL_BLOCKER"
    assert run.VERDICT_UPSTREAM == "CORRECTED_2018_SINGLE_TURN_FAIL__UPSTREAM_FIRM_OR_STATE_BLOCKER"


def test_native_initializer_matches_frozen_scalar_formula() -> None:
    grid = run.oracle.MatlabFaithfulHJBGrid(
        np.array([-2.0, 5.0]), np.array([0.0, 10.0]), np.array([0.8, 1.3]),
        np.array([[-1 / 3, 1 / 3], [1 / 3, -1 / 3]]))
    params = run.oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    state = {"rah": 0.09, "rb": 0.02, "rb_gap": 0.07, "Tt": 0.1, "tau": 0.05, "w": 20.0}
    roots = []
    value, labor = run.source_initial_arrays(state, grid, params, lambda: roots.append(1))
    assert value.shape == labor.shape == (2, 2, 2)
    assert len(roots) == 8
    assert np.isfinite(value).all() and np.isfinite(labor).all() and np.all(labor > 0)


def test_execute_has_one_turn_and_retry_guards() -> None:
    source = Path(run.__file__).read_text(encoding="utf-8")
    assert '"one_turn_executions"] += 1' in source
    assert '"scientific_retries": 0' in source
    assert "scientific execution already started; retry prohibited" in source
    assert "run_online_stationary" not in source


def test_saved_old_comparison_is_descriptive_only(tmp_path: Path) -> None:
    path = tmp_path / "old.csv"
    path.write_text(
        "step,index_0,input_Yt0,input_N,input_Kt0,input_alpha,input_Zt,ra0,ra,wt0,wjt,input_rah\n"
        "1,11,10,20,30,.7,.01,-.02,.02,.5,.8,.09\n", encoding="utf-8")
    old = finalize.old_anhui_turn1(path)
    new = {"GDP": 11, "POP": 21, "CAP": 31, "alpha": .7, "same_year_Zt": .02,
           "firm_ra0": -.01, "firm_ra_used": .02, "firm_wage_raw": .6,
           "firm_wage_used": .8, "household_rah": .09}
    result = finalize.build_comparison(old, new)
    assert result["classification"] == "DESCRIPTIVE_INPUT_CORRECTION_EFFECT_ONLY"
    assert result["old_model_rerun"] is False
