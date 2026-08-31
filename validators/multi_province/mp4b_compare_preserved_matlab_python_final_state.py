"""Read-only comparator for the pre-frozen MATLAB/Python final-state field map."""

from __future__ import annotations

import json
from pathlib import Path

import h5py
import numpy as np


FIELDS = (
    "Ct", "At", "Bt", "Lt", "Lt_supply", "Kt_supply", "rah", "Kt", "Yt",
    "mt", "KNratio", "w", "wjt", "rk", "ra", "GovInv", "rb", "it", "Zt", "Govinc",
)


def _scalar(group, name: str) -> float:
    return float(np.asarray(group[name])[0, 0])


def _text(dataset) -> str:
    values = np.asarray(dataset).reshape(-1)
    return "".join(chr(int(value)) for value in values)


def load_preserved_matlab_state(path: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
    states: list[dict[str, object]] = []
    with h5py.File(path, "r") as handle:
        refs = np.asarray(handle["st/results"]).reshape(-1, order="F")
        grid_refs = np.asarray(handle["st/grids"]).reshape(-1, order="F")
        for result_ref, grid_ref in zip(refs, grid_refs, strict=True):
            result = handle[result_ref]
            grid = handle[grid_ref]
            state = {"name": _text(result["prvname"])}
            state.update({field: _scalar(result, field) for field in FIELDS})
            state["convergent"] = bool(_scalar(result, "convergent"))
            state.update({name: _scalar(grid, name) for name in ("ramin", "ramax", "wjtmin", "wjtmax")})
            states.append(state)
    categories = {
        "final_household_converged_count": sum(bool(state["convergent"]) for state in states),
        "ra_upper_count": sum(state["ra"] == state["ramax"] for state in states),
        "ra_lower_count": sum(state["ra"] == state["ramin"] for state in states),
        "wage_upper_count": sum(state["wjt"] == state["wjtmax"] for state in states),
        "wage_lower_count": sum(state["wjt"] == state["wjtmin"] for state in states),
    }
    return states, categories


def compare_terminal(matlab_path: Path, python_terminal_path: Path, output_path: Path) -> dict[str, object]:
    if output_path.exists():
        raise FileExistsError(f"refusing to overwrite {output_path}")
    matlab, matlab_categories = load_preserved_matlab_state(matlab_path)
    terminal = json.loads(python_terminal_path.read_text(encoding="utf-8"))
    python = terminal["final_state"]
    if [state["name"] for state in matlab] != [state["name"] for state in python]:
        raise ValueError("province order mismatch")
    rows = []
    for matlab_state, python_state in zip(matlab, python, strict=True):
        differences = {}
        for field in FIELDS:
            m_value = float(matlab_state[field]); p_value = float(python_state[field])
            absolute = abs(m_value - p_value)
            scale = max(1.0, abs(m_value), abs(p_value))
            differences[field] = {
                "matlab": m_value, "python": p_value, "absolute": absolute,
                "relative": absolute / max(abs(m_value), abs(p_value)) if max(abs(m_value), abs(p_value)) else 0.0,
                "normalized": absolute / scale,
            }
        rows.append({"province": matlab_state["name"], "continuous": differences,
                     "convergent_exact": bool(matlab_state["convergent"]) == bool(python_state["convergent"])})
    national = {}
    for field in ("Ct", "At", "Bt", "Yt"):
        m_value = sum(float(state[field]) for state in matlab)
        p_value = sum(float(state[field]) for state in python)
        absolute = abs(m_value - p_value)
        national[field] = {"matlab": m_value, "python": p_value, "absolute": absolute,
                           "relative": absolute / max(abs(m_value), abs(p_value)),
                           "normalized": absolute / max(1.0, abs(m_value), abs(p_value))}
    payload = {"schema": "MP4B_PRESERVED_MATLAB_PYTHON_FINAL_STATE_COMPARISON_V1",
               "province_rows": rows, "national": national,
               "matlab_categories": matlab_categories,
               "python_outer_turn_count": terminal.get("iteration_count")}
    output_path.write_text(json.dumps(payload, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    return payload


__all__ = ["FIELDS", "load_preserved_matlab_state", "compare_terminal"]
