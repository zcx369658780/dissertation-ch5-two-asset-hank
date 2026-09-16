"""Hash-bound read-only intake for the accepted 14 saved-control snapshots."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.io import loadmat

from .contracts import CorrectedDiagnosticGrid, checked_drift


@dataclass(frozen=True)
class SavedControlProvenance:
    snapshot_id: str
    language: str
    path: str
    sha256: str
    bytes: int


@dataclass(frozen=True)
class SavedControlSnapshot:
    provenance: SavedControlProvenance
    grid: CorrectedDiagnosticGrid
    mu_b: np.ndarray
    mu_a: np.ndarray


def _read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def _readonly_drift(name: str, values: object, shape: tuple[int, int, int]) -> np.ndarray:
    drift = np.array(checked_drift(name, np.asarray(values), shape), copy=True)
    drift.flags.writeable = False
    return drift


def _load_arrays(language: str, path: Path) -> dict[str, object]:
    if language == "matlab":
        source = loadmat(path, squeeze_me=True, struct_as_record=False)
        return {
            "b": source["b"],
            "a": source["ah"],
            "z": source["z"],
            "mu_b": source["mu_b"],
            "mu_a": source["mu_a"],
        }
    if language == "python":
        with np.load(path, allow_pickle=False) as source:
            return {name: np.array(source[name], copy=True) for name in ("b", "a", "z", "mu_b", "mu_a")}
    raise ValueError(f"unsupported saved-control language: {language}")


def load_saved_control_set(
    snapshot_manifest: str | Path,
    consumed_input_receipt: str | Path,
) -> tuple[SavedControlSnapshot, ...]:
    """Load only hash-receipted drifts/grids; never import a model or selector."""

    snapshot_rows = _read_json(Path(snapshot_manifest))
    consumed = _read_json(Path(consumed_input_receipt))
    if not isinstance(snapshot_rows, list) or not isinstance(consumed, dict):
        raise ValueError("saved-control provenance documents have invalid schemas")
    receipt_rows = consumed.get("consumed_entries")
    if not isinstance(receipt_rows, list):
        raise ValueError("consumed-input receipt lacks consumed_entries")
    receipts = {str(row["path"]): row for row in receipt_rows}
    result: list[SavedControlSnapshot] = []
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    for row in snapshot_rows:
        if not row.get("eligible", False):
            raise ValueError(f"snapshot is not accepted eligible: {row.get('id')}")
        snapshot_id = str(row["id"])
        language = str(row["language"])
        path_text = str(row["path"])
        if snapshot_id in seen_ids or path_text in seen_paths:
            raise ValueError("saved-control manifest contains duplicate ids or paths")
        seen_ids.add(snapshot_id)
        seen_paths.add(path_text)
        if path_text not in receipts:
            raise ValueError(f"snapshot lacks an accepted consumed-input receipt: {snapshot_id}")
        path = Path(path_text)
        if not path.is_file():
            raise FileNotFoundError(path)
        receipt = receipts[path_text]
        actual_bytes = path.stat().st_size
        actual_hash = _sha256(path)
        if actual_bytes != int(receipt["bytes"]) or actual_hash != str(receipt["sha256"]).upper():
            raise ValueError(f"saved-control identity mismatch: {snapshot_id}")
        arrays = _load_arrays(language, path)
        grid = CorrectedDiagnosticGrid(arrays["b"], arrays["a"], arrays["z"])
        result.append(
            SavedControlSnapshot(
                provenance=SavedControlProvenance(
                    snapshot_id=snapshot_id,
                    language=language,
                    path=path_text,
                    sha256=actual_hash,
                    bytes=actual_bytes,
                ),
                grid=grid,
                mu_b=_readonly_drift("mu_b", arrays["mu_b"], grid.shape),
                mu_a=_readonly_drift("mu_a", arrays["mu_a"], grid.shape),
            )
        )
    return tuple(result)
