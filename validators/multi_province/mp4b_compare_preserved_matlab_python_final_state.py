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
EXPECTED_PROVINCE_COUNT = 31
EXPECTED_MATLAB_SUFFIX_PROJECTION_CHANGES = 25


def _scalar(group, name: str) -> float:
    return float(np.asarray(group[name])[0, 0])


def _text(dataset) -> str:
    values = np.asarray(dataset).reshape(-1)
    return "".join(chr(int(value)) for value in values)


def project_matlab_province_name(raw_name: str) -> str:
    """Return the sole accepted MATLAB-to-canonical province-name projection."""
    return raw_name[:-1] if raw_name.endswith(("省", "市")) else raw_name


def _category_counts(states: list[dict[str, object]]) -> dict[str, int]:
    return {
        "final_household_converged_count": sum(bool(state["convergent"]) for state in states),
        "ra_upper_count": sum(state["ra"] == state["ramax"] for state in states),
        "ra_lower_count": sum(state["ra"] == state["ramin"] for state in states),
        "wage_upper_count": sum(state["wjt"] == state["wjtmax"] for state in states),
        "wage_lower_count": sum(state["wjt"] == state["wjtmin"] for state in states),
    }


def load_preserved_matlab_state(path: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
    states: list[dict[str, object]] = []
    with h5py.File(path, "r") as handle:
        refs = np.asarray(handle["st/results"]).reshape(-1, order="F")
        grid_refs = np.asarray(handle["st/grids"]).reshape(-1, order="F")
        for result_ref, grid_ref in zip(refs, grid_refs, strict=True):
            result = handle[result_ref]
            grid = handle[grid_ref]
            raw_name = _text(result["prvname"])
            state = {"name": raw_name, "raw_matlab_province": raw_name}
            state.update({field: _scalar(result, field) for field in FIELDS})
            state["convergent"] = bool(_scalar(result, "convergent"))
            state.update({name: _scalar(grid, name) for name in ("ramin", "ramax", "wjtmin", "wjtmax")})
            states.append(state)
    return states, _category_counts(states)


def validate_province_identity(
    matlab: list[dict[str, object]], python: list[dict[str, object]],
) -> tuple[list[str], dict[str, object]]:
    """Fail closed unless the bounded raw-MATLAB suffix projection aligns exactly."""
    raw_matlab = [str(state["raw_matlab_province"]) for state in matlab]
    raw_python = [str(state["name"]) for state in python]
    if len(raw_matlab) != EXPECTED_PROVINCE_COUNT or len(raw_python) != EXPECTED_PROVINCE_COUNT:
        raise ValueError("province identity requires exactly 31 MATLAB and Python states")
    if len(set(raw_matlab)) != EXPECTED_PROVINCE_COUNT:
        raise ValueError("raw MATLAB province names must be unique")
    projected = [project_matlab_province_name(name) for name in raw_matlab]
    if len(set(projected)) != EXPECTED_PROVINCE_COUNT:
        raise ValueError("projected MATLAB province names must be unique; projection collision")
    if len(set(raw_python)) != EXPECTED_PROVINCE_COUNT:
        raise ValueError("Python province names must be unique")
    changed_indices = [index + 1 for index, (raw, key) in enumerate(zip(raw_matlab, projected, strict=True)) if raw != key]
    if len(changed_indices) != EXPECTED_MATLAB_SUFFIX_PROJECTION_CHANGES:
        raise ValueError("MATLAB suffix projection must change exactly the diagnosed 25 names")
    if projected != raw_python:
        raise ValueError("projected MATLAB province sequence must equal Python province sequence exactly")
    evidence = {
        "raw_matlab_province_names": raw_matlab,
        "raw_python_province_names": raw_python,
        "comparison_keys": projected,
        "projection_changed_indices_1based": changed_indices,
        "projection_changed_count": len(changed_indices),
    }
    return projected, evidence


def build_comparison_payload(
    matlab: list[dict[str, object]],
    python: list[dict[str, object]],
    matlab_outer_turn_count: int | None,
    python_outer_turn_count: int | None,
) -> dict[str, object]:
    """Build aligned evidence only after the bounded representation contract passes."""
    comparison_keys, identity = validate_province_identity(matlab, python)
    rows = []
    for matlab_state, python_state, comparison_key in zip(matlab, python, comparison_keys, strict=True):
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
        rows.append({
            "province": comparison_key,
            "raw_matlab_province": matlab_state["raw_matlab_province"],
            "raw_python_province": python_state["name"],
            "comparison_key": comparison_key,
            "continuous": differences,
            "convergent_exact": bool(matlab_state["convergent"]) == bool(python_state["convergent"]),
        })
    national = {}
    for field in ("Ct", "At", "Bt", "Yt"):
        m_value = sum(float(state[field]) for state in matlab)
        p_value = sum(float(state[field]) for state in python)
        absolute = abs(m_value - p_value)
        national[field] = {"matlab": m_value, "python": p_value, "absolute": absolute,
                           "relative": absolute / max(abs(m_value), abs(p_value)),
                           "normalized": absolute / max(1.0, abs(m_value), abs(p_value))}
    matlab_categories = _category_counts(matlab)
    python_categories = _category_counts(python)
    categories = {"outer_turn_count": {"matlab": matlab_outer_turn_count, "python": python_outer_turn_count}}
    categories.update({field: {"matlab": matlab_categories[field], "python": python_categories[field]}
                       for field in matlab_categories})
    for values in categories.values():
        values["exact"] = values["matlab"] == values["python"]
    return {
        "schema": "MP4B_PRESERVED_MATLAB_PYTHON_FINAL_STATE_COMPARISON_V2",
        "province_identity": identity,
        "province_rows": rows,
        "national": national,
        "terminal_categories": categories,
        "matlab_categories": matlab_categories,
        "python_categories": python_categories,
    }


def compare_terminal(
    matlab_path: Path,
    python_terminal_path: Path,
    output_path: Path,
    matlab_terminal_status_path: Path | None = None,
) -> dict[str, object]:
    if output_path.exists():
        raise FileExistsError(f"refusing to overwrite {output_path}")
    matlab, matlab_categories = load_preserved_matlab_state(matlab_path)
    terminal = json.loads(python_terminal_path.read_text(encoding="utf-8"))
    matlab_outer_turn_count = None
    if matlab_terminal_status_path is not None:
        matlab_status = json.loads(matlab_terminal_status_path.read_text(encoding="utf-8"))
        matlab_outer_turn_count = int(matlab_status["outer_turn_call_count"])
    payload = build_comparison_payload(
        matlab, terminal["final_state"], matlab_outer_turn_count, terminal.get("iteration_count"),
    )
    output_path.write_text(json.dumps(payload, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    return payload


__all__ = [
    "EXPECTED_MATLAB_SUFFIX_PROJECTION_CHANGES", "EXPECTED_PROVINCE_COUNT", "FIELDS",
    "build_comparison_payload", "compare_terminal", "load_preserved_matlab_state",
    "project_matlab_province_name", "validate_province_identity",
]
