"""Hash-bound intake for the exact preregistered ten-cell call725 panel."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.io import loadmat

from .selector import (
    CellDerivatives,
    CorrectedSelectorCell,
    CorrectedSelectorParameters,
)


PANEL_SPEC = (
    ("M143_corner_000", "matlab_M143_FINAL", 0),
    ("M143_corner_019", "matlab_M143_FINAL", 19),
    ("M143_corner_380", "matlab_M143_FINAL", 380),
    ("M143_corner_399", "matlab_M143_FINAL", 399),
    ("M143_corner_400", "matlab_M143_FINAL", 400),
    ("M143_corner_419", "matlab_M143_FINAL", 419),
    ("M143_corner_780", "matlab_M143_FINAL", 780),
    ("M143_corner_799", "matlab_M143_FINAL", 799),
    ("MATLAB_step52_row799", "matlab_trajectory_52", 799),
    ("MATLAB_step57_row379", "matlab_trajectory_57", 379),
)


@dataclass(frozen=True)
class BoundPanelCell:
    panel_id: str
    source_snapshot_id: str
    source_path: str
    source_sha256: str
    source_bytes: int
    source_row_label: int
    index: tuple[int, int, int]
    flat_index_f: int
    scalar_binding_path: str
    scalar_binding_sha256: str
    scalar_binding_bytes: int
    grid_b: tuple[float, ...]
    grid_a: tuple[float, ...]
    grid_z: tuple[float, ...]
    selector_cell: CorrectedSelectorCell
    selector_parameters: CorrectedSelectorParameters
    bound_inputs: dict[str, float]


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def _json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def _verified_file(path_text: str, receipt: dict[str, object]) -> Path:
    path = Path(path_text)
    if not path.is_file():
        raise FileNotFoundError(path)
    actual_bytes = path.stat().st_size
    actual_hash = _sha256(path)
    if actual_bytes != int(receipt["bytes"]) or actual_hash != str(receipt["sha256"]).upper():
        raise ValueError(f"accepted panel source identity mismatch: {path}")
    return path


def bind_preregistered_panel(repository: str | Path) -> tuple[BoundPanelCell, ...]:
    """Resolve the ten accepted zero-based/F-order cells without a policy call."""

    root = Path(repository)
    evidence = root / "reports/call725_boundary_generator_repair_spec_20260907"
    snapshots = _json(evidence / "snapshots.json")
    consumed = _json(evidence / "consumed_inputs.json")
    binding_identity = _json(evidence / "binding_identity.json")
    if not isinstance(snapshots, list) or not isinstance(consumed, dict):
        raise ValueError("accepted panel provenance schema is invalid")
    snapshot_by_id = {str(row["id"]): row for row in snapshots}
    receipts = {str(row["path"]): row for row in consumed["consumed_entries"]}
    binding_path_text = str(binding_identity["path"])
    binding_path = _verified_file(binding_path_text, receipts[binding_path_text])
    if _sha256(binding_path) != str(binding_identity["sha256"]).upper():
        raise ValueError("binding identity and consumed receipt disagree")
    scalar_document = _json(binding_path)
    scalar = scalar_document["scalar_binding"]
    parameters = scalar["parameters"]
    selector_parameters = CorrectedSelectorParameters(
        gamma_c=float(parameters["gamma_c"]),
        phi=float(parameters["phi"]),
        labor_weight=float(parameters["labor_weight"]),
        chi_0=float(parameters["chi_0"]),
        chi_1=float(parameters["chi_1"]),
        a_bar=float(parameters["a_bar"]),
    )

    loaded: dict[str, tuple[dict[str, object], dict[str, object], Path]] = {}
    result: list[BoundPanelCell] = []
    for panel_id, snapshot_id, row_label in PANEL_SPEC:
        snapshot = snapshot_by_id[snapshot_id]
        if snapshot.get("language") != "matlab" or not snapshot.get("eligible", False):
            raise ValueError(f"panel source is not the accepted MATLAB object: {snapshot_id}")
        path_text = str(snapshot["path"])
        if snapshot_id not in loaded:
            path = _verified_file(path_text, receipts[path_text])
            arrays = loadmat(path, squeeze_me=True, struct_as_record=False)
            loaded[snapshot_id] = (arrays, receipts[path_text], path)
        arrays, receipt, path = loaded[snapshot_id]
        b_grid = np.asarray(arrays["b"], dtype=float)
        a_grid = np.asarray(arrays["ah"], dtype=float)
        z_grid = np.asarray(arrays["z"], dtype=float)
        shape = (b_grid.size, a_grid.size, z_grid.size)
        if shape != (20, 20, 2):
            raise ValueError(f"accepted call725 panel shape changed: {shape}")
        if row_label < 0 or row_label >= int(np.prod(shape)):
            raise ValueError(f"panel row is outside the accepted shape: {row_label}")
        index = tuple(map(int, np.unravel_index(row_label, shape, order="F")))
        flat_index = int(np.ravel_multi_index(index, shape, order="F"))
        if flat_index != row_label:
            raise ValueError("BLOCKED_PANEL_IDENTITY_AMBIGUOUS")
        i_b, i_a, i_z = index
        b = float(b_grid[i_b])
        a = float(a_grid[i_a])
        z = float(z_grid[i_z])
        effective_r_b = float(parameters["r_b"]) + (
            float(parameters["borrowing_rate_gap"]) if b < 0.0 else 0.0
        )
        net_wage = float((1.0 - float(parameters["tau"])) * float(parameters["wage"]) * z)
        derivative_values = {
            "p_b_backward": float(np.asarray(arrays["VbB"])[index]),
            "p_b_forward": float(np.asarray(arrays["VbF"])[index]),
            "p_a_backward": float(np.asarray(arrays["VahB"])[index]),
            "p_a_forward": float(np.asarray(arrays["VahF"])[index]),
        }
        raw_values = {
            "raw_p_b_backward": float(np.asarray(arrays["raw_VbB"])[index]),
            "raw_p_b_forward": float(np.asarray(arrays["raw_VbF"])[index]),
            "raw_p_a_backward": float(np.asarray(arrays["raw_VahB"])[index]),
            "raw_p_a_forward": float(np.asarray(arrays["raw_VahF"])[index]),
        }
        selector_cell = CorrectedSelectorCell(
            cell_id=panel_id,
            b=b,
            a=a,
            z=z,
            b_lower=float(b_grid[0]),
            b_upper=float(b_grid[-1]),
            a_lower=float(a_grid[0]),
            a_upper=float(a_grid[-1]),
            net_wage=net_wage,
            effective_r_b=effective_r_b,
            transfer_income=float(parameters["transfer_income"]),
            effective_r_a=float(np.asarray(arrays["Rah"])[index]),
            derivatives=CellDerivatives(**derivative_values),
        )
        bound_inputs = {
            "b": b,
            "a": a,
            "z": z,
            "net_wage": net_wage,
            "effective_r_b": effective_r_b,
            "transfer_income": float(parameters["transfer_income"]),
            "effective_r_a": selector_cell.effective_r_a,
            "historical_l0": float(np.asarray(arrays["l0"])[index]),
            "historical_initial_value": float(np.asarray(arrays["initial_value"])[index]),
            **derivative_values,
            **raw_values,
        }
        result.append(
            BoundPanelCell(
                panel_id=panel_id,
                source_snapshot_id=snapshot_id,
                source_path=str(path),
                source_sha256=str(receipt["sha256"]).upper(),
                source_bytes=int(receipt["bytes"]),
                source_row_label=row_label,
                index=index,
                flat_index_f=flat_index,
                scalar_binding_path=str(binding_path),
                scalar_binding_sha256=str(binding_identity["sha256"]).upper(),
                scalar_binding_bytes=int(binding_identity["bytes"]),
                grid_b=tuple(map(float, b_grid)),
                grid_a=tuple(map(float, a_grid)),
                grid_z=tuple(map(float, z_grid)),
                selector_cell=selector_cell,
                selector_parameters=selector_parameters,
                bound_inputs=bound_inputs,
            )
        )
    if tuple(cell.panel_id for cell in result) != tuple(row[0] for row in PANEL_SPEC):
        raise ValueError("BLOCKED_PANEL_IDENTITY_AMBIGUOUS")
    return tuple(result)
