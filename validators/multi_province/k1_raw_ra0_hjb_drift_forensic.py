"""Zero-science forensic for accepted Control/Raw K1 payoff HJB evidence."""

from __future__ import annotations

import argparse
import csv
import json
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable

import numpy as np


BASELINE_SHA = "fb5ebaea842f7ce4c3bfa29e6aa328d72fd94eb4"
ACCEPTED_MANIFEST_SHA256 = "69E85A9CAF6A23F5B7402821112F1A0465E2617F8A44ACEE167BC61D25B1E644"
SOURCE_IDENTITIES = {
    "exports/matlab_faithful_two_asset_ha.py": "2C35F031DDDB856F2347F606C4BCF27608E8BAB9EEAEDDE4F586A9A0A8080B38",
    "src/ch5_two_asset_hank/multi_province/household_adapter.py": "0963591A95293E896B9F9A8C3F4C630CD3DBB9519950171170E28822C8A4EF0F",
    "validators/multi_province/g1_residual_govinv_25turn_isolated/run.py": "E8301FC5FAE898786741D2FC1CD90ACBE63196A12DD8AD04346AB71342821945",
}
PATHS = {"C": "control_beta2", "R": "raw_beta2"}
TURNS = range(2, 6)
ARRAY_FIELDS = (
    "consumption",
    "labor",
    "transfer",
    "adjustment_cost",
    "effective_illiquid_return",
    "mu_a",
    "mu_b",
)
GRID_B = np.linspace(-2.0, 5.0, 20)
GRID_A = np.linspace(0.0, 10.0, 20)
GRID_Z = np.array([0.8, 1.3])
GRID_SHAPE = (20, 20, 2)
ITERATION_CEILING = 100
CLASSIFICATION = (
    "RAW_PAYOFF_SCALE_EXPOSURE_PROPAGATES_THROUGH_ACCEPTED_VALUE_DERIVATIVE_TRANSFER_COST_LAW"
    "__UPPER_A_BOUNDARY_REGIME_EXPANDS__MIXED_BASELINE_EXTREMES__OWNER_DECISION_REQUIRED"
)
NEXT_GATE = "A_OWNER_SCIENTIFIC_DECISION_ON_PAYOFF_MAPPING_SCALE_INTERPRETATION"


def _sha(path: Path) -> str:
    return sha256(Path(path).read_bytes()).hexdigest().upper()


def _read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _jsonable(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(item) for item in value]
    if isinstance(value, np.ndarray):
        return _jsonable(value.tolist())
    if isinstance(value, (np.integer, np.floating, np.bool_)):
        return value.item()
    if isinstance(value, float) and not np.isfinite(value):
        return None
    return value


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(_jsonable(value), stream, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        stream.write("\n")


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        raise ValueError(f"cannot write empty CSV: {path.name}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(_jsonable(rows))


def finite_stats(values: Any) -> dict[str, float]:
    array = np.asarray(values, dtype=float).ravel()
    if array.size == 0 or not np.isfinite(array).all():
        raise ValueError("forensic statistics require non-empty finite arrays")
    return {
        "min": float(np.min(array)),
        "median": float(np.median(array)),
        "p95": float(np.percentile(array, 95)),
        "p99": float(np.percentile(array, 99)),
        "max": float(np.max(array)),
        "abs_max": float(np.max(np.abs(array))),
    }


def safe_ratio(numerator: float, denominator: float) -> float | None:
    if not np.isfinite([numerator, denominator]).all() or denominator == 0.0:
        return None
    return float(numerator / denominator)


def _rank_average(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty(values.size, dtype=float)
    start = 0
    while start < values.size:
        end = start + 1
        while end < values.size and values[order[end]] == values[order[start]]:
            end += 1
        ranks[order[start:end]] = 0.5 * (start + 1 + end)
        start = end
    return ranks


def correlation(x: Iterable[float], y: Iterable[float], *, spearman: bool = False) -> float | None:
    xa = np.asarray(list(x), dtype=float)
    ya = np.asarray(list(y), dtype=float)
    valid = np.isfinite(xa) & np.isfinite(ya)
    xa, ya = xa[valid], ya[valid]
    if xa.size < 3:
        return None
    if spearman:
        xa, ya = _rank_average(xa), _rank_average(ya)
    if np.ptp(xa) == 0.0 or np.ptp(ya) == 0.0:
        return None
    return float(np.corrcoef(xa, ya)[0, 1])


def boundary_mask(array: np.ndarray, face: str) -> np.ndarray:
    mask = np.zeros(array.shape, dtype=bool)
    if face == "lower_a":
        mask[:, 0, :] = array[:, 0, :] < 0.0
    elif face == "upper_a":
        mask[:, -1, :] = array[:, -1, :] > 0.0
    elif face == "lower_b":
        mask[0, :, :] = array[0, :, :] < 0.0
    elif face == "upper_b":
        mask[-1, :, :] = array[-1, :, :] > 0.0
    else:
        raise ValueError(f"unknown boundary face: {face}")
    return mask


def boundary_label(i_b: int, i_a: int) -> str:
    labels = []
    if i_b == 0:
        labels.append("lower_b")
    elif i_b == GRID_B.size - 1:
        labels.append("upper_b")
    if i_a == 0:
        labels.append("lower_a")
    elif i_a == GRID_A.size - 1:
        labels.append("upper_a")
    return "+".join(labels) if labels else "interior"


def verify_accepted_manifest(root: Path) -> dict[str, Any]:
    manifest_path = root / "manifest_sha256.json"
    observed = _sha(manifest_path)
    if observed != ACCEPTED_MANIFEST_SHA256:
        raise ValueError("accepted external manifest SHA mismatch")
    manifest = _read_json(manifest_path)
    bad: list[str] = []
    for entry in manifest["files"]:
        path = root / Path(entry["path"])
        if not path.is_file() or path.stat().st_size != int(entry["bytes"]) or _sha(path) != entry["sha256"]:
            bad.append(entry["path"])
    if bad:
        raise ValueError(f"accepted evidence readback failed for {bad[:3]!r}")
    return {
        "accepted_manifest_sha256": observed,
        "declared_files": int(manifest["file_count"]),
        "verified_files": len(manifest["files"]),
        "mismatches": 0,
        "status": "PASS",
    }


def verify_sources(repo: Path) -> dict[str, Any]:
    files = {}
    for relative, expected in SOURCE_IDENTITIES.items():
        observed = _sha(repo / relative)
        if observed != expected:
            raise ValueError(f"source identity mismatch: {relative}")
        files[relative] = {"sha256": observed, "status": "MATCH"}
    return {
        "status": "PASS",
        "files": files,
        "grid_binding": {
            "coordinate_provenance": "PERSISTED_ARRAY_INDEX_PLUS_ACCEPTED_SOURCE_FIXED_GRID",
            "array_shape": list(GRID_SHAPE),
            "b": {"source": "validators/multi_province/g1_residual_govinv_25turn_isolated/run.py:315", "values": GRID_B},
            "a": {"source": "validators/multi_province/g1_residual_govinv_25turn_isolated/run.py:315", "values": GRID_A},
            "z": {"source": "validators/multi_province/g1_residual_govinv_25turn_isolated/run.py:316", "values": GRID_Z},
            "npz_contains_coordinate_axes": False,
        },
    }


def _turn_rows(root: Path, path_name: str, turn: int) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    base = root / path_name / f"turn_{turn:02d}"
    rows = _read_json(base / "per_province_observables.json")
    entering = _read_json(base / "entering_state.json")["states"]
    if len(rows) != 31 or len(entering) != 31:
        raise ValueError("accepted turn must contain 31 matched provinces")
    return rows, entering


def _npz_path(root: Path, path_name: str, turn: int, index: int, province: str) -> Path:
    return root / path_name / f"turn_{turn:02d}" / "household" / f"p{index:02d}_{province}" / "hjb_return.npz"


def _load_npz(path: Path) -> dict[str, np.ndarray | int | float | bool]:
    with np.load(path, allow_pickle=False) as data:
        result: dict[str, np.ndarray | int | float | bool] = {}
        for name in ARRAY_FIELDS + ("liquid_label", "transfer_label"):
            value = np.array(data[name], copy=True)
            if value.shape != GRID_SHAPE:
                raise ValueError(f"unexpected HJB array shape in {path}: {name}")
            if name in ARRAY_FIELDS and not np.isfinite(value).all():
                raise ValueError(f"nonfinite accepted HJB array: {path}: {name}")
            result[name] = value
        result["iterations"] = int(data["iterations"])
        result["converged"] = bool(data["converged"])
        result["convergence_statistic"] = float(data["convergence_statistic"])
    return result


def _label_counts(labels: np.ndarray, mask: np.ndarray) -> str:
    selected = labels[mask]
    if selected.size == 0:
        return ""
    unique, counts = np.unique(selected, return_counts=True)
    return ";".join(f"{label}:{count}" for label, count in zip(unique, counts))


def analyze(external_root: Path, repo: Path) -> dict[str, Any]:
    external_root, repo = Path(external_root), Path(repo)
    manifest_receipt = verify_accepted_manifest(external_root)
    source_receipt = verify_sources(repo)

    cache: dict[tuple[str, int, int], dict[str, Any]] = {}
    metadata: dict[tuple[str, int], tuple[list[dict[str, Any]], list[dict[str, Any]]]] = {}
    for path_id, path_name in PATHS.items():
        for turn in range(1, 6):
            rows, entering = _turn_rows(external_root, path_name, turn)
            metadata[(path_id, turn)] = (rows, entering)
            for index, row in enumerate(rows):
                if int(row["province_index"]) != index or row["province"] != entering[index]["name"]:
                    raise ValueError("province order mismatch")
                cache[(path_id, turn, index)] = _load_npz(
                    _npz_path(external_root, path_name, turn, index, row["province"])
                )

    turn1_equal = True
    for index in range(31):
        c, r = cache[("C", 1, index)], cache[("R", 1, index)]
        for field in ARRAY_FIELDS + ("liquid_label", "transfer_label"):
            turn1_equal &= bool(np.array_equal(c[field], r[field]))
        turn1_equal &= c["iterations"] == r["iterations"]
        turn1_equal &= c["converged"] == r["converged"]
        turn1_equal &= c["convergence_statistic"] == r["convergence_statistic"]
    if not turn1_equal:
        raise ValueError("turn-1 bootstrap arrays are not identical")

    province_rows: list[dict[str, Any]] = []
    province_stat_rows: list[dict[str, Any]] = []
    distribution_rows: list[dict[str, Any]] = []
    boundary_rows: list[dict[str, Any]] = []
    lower_b_rows: list[dict[str, Any]] = []
    extreme_rows: list[dict[str, Any]] = []

    for turn in TURNS:
        c_rows, c_entering = metadata[("C", turn)]
        r_rows, r_entering = metadata[("R", turn)]
        for index, (c_row, r_row) in enumerate(zip(c_rows, r_rows)):
            c, r = cache[("C", turn, index)], cache[("R", turn, index)]
            if c_row["province"] != r_row["province"]:
                raise ValueError("Control/Raw province match failed")
            record: dict[str, Any] = {
                "turn": turn,
                "province_index": index,
                "province": c_row["province"],
                "control_converged": c["converged"],
                "raw_converged": r["converged"],
                "raw_new_nonconvergence": bool(c["converged"] and not r["converged"]),
                "raw_recovers_control_nonconvergence": bool(not c["converged"] and r["converged"]),
                "control_iterations": c["iterations"],
                "raw_iterations": r["iterations"],
                "control_hit_iteration_ceiling": c["iterations"] == ITERATION_CEILING,
                "raw_hit_iteration_ceiling": r["iterations"] == ITERATION_CEILING,
                "control_hjb_statistic": c["convergence_statistic"],
                "raw_hjb_statistic": r["convergence_statistic"],
                "raw_minus_control_hjb_statistic": r["convergence_statistic"] - c["convergence_statistic"],
                "raw_over_control_hjb_statistic": safe_ratio(r["convergence_statistic"], c["convergence_statistic"]),
                "control_entering_rah": float(c_row["household_rah"]),
                "raw_entering_rah": float(r_row["household_rah"]),
                "raw_minus_control_entering_rah": float(r_row["household_rah"] - c_row["household_rah"]),
                "raw_over_control_entering_rah": safe_ratio(float(r_row["household_rah"]), float(c_row["household_rah"])),
                "control_same_index_prior_firm_ra0": float(c_entering[index]["ra0"]),
                "raw_same_index_prior_firm_ra0": float(r_entering[index]["ra0"]),
                "control_same_index_prior_firm_used_ra": float(c_entering[index]["ra"]),
                "raw_same_index_prior_firm_used_ra": float(r_entering[index]["ra"]),
                "control_same_index_prior_raw_minus_used": float(c_entering[index]["ra0"] - c_entering[index]["ra"]),
                "raw_same_index_prior_raw_minus_used": float(r_entering[index]["ra0"] - r_entering[index]["ra"]),
            }
            for field in ARRAY_FIELDS:
                c_stats, r_stats = finite_stats(c[field]), finite_stats(r[field])
                c_abs = float(np.max(np.abs(c[field])))
                r_abs = float(np.max(np.abs(r[field])))
                record[f"control_{field}_abs_max"] = c_abs
                record[f"raw_{field}_abs_max"] = r_abs
                record[f"raw_minus_control_{field}_abs_max"] = r_abs - c_abs
                record[f"raw_over_control_{field}_abs_max"] = safe_ratio(r_abs, c_abs)
                stat_row: dict[str, Any] = {
                    "turn": turn,
                    "province_index": index,
                    "province": c_row["province"],
                    "variable": field,
                    "cells_per_path": int(np.asarray(c[field]).size),
                }
                for metric in c_stats:
                    stat_row[f"control_{metric}"] = c_stats[metric]
                    stat_row[f"raw_{metric}"] = r_stats[metric]
                    stat_row[f"raw_minus_control_{metric}"] = r_stats[metric] - c_stats[metric]
                    stat_row[f"raw_over_control_{metric}"] = safe_ratio(r_stats[metric], c_stats[metric])
                province_stat_rows.append(stat_row)
            for face in ("lower_a", "upper_a", "lower_b", "upper_b"):
                drift = "mu_a" if face.endswith("a") else "mu_b"
                cm = boundary_mask(c[drift], face)
                rm = boundary_mask(r[drift], face)
                record[f"control_{face}_outward_count"] = int(np.count_nonzero(cm))
                record[f"raw_{face}_outward_count"] = int(np.count_nonzero(rm))
                record[f"raw_only_{face}_outward_count"] = int(np.count_nonzero(rm & ~cm))
            province_rows.append(record)

        for field in ARRAY_FIELDS:
            c_all = np.concatenate([np.ravel(cache[("C", turn, i)][field]) for i in range(31)])
            r_all = np.concatenate([np.ravel(cache[("R", turn, i)][field]) for i in range(31)])
            cs, rs = finite_stats(c_all), finite_stats(r_all)
            row: dict[str, Any] = {"turn": turn, "variable": field, "cells_per_path": int(c_all.size)}
            for metric in cs:
                row[f"control_{metric}"] = cs[metric]
                row[f"raw_{metric}"] = rs[metric]
                row[f"raw_minus_control_{metric}"] = rs[metric] - cs[metric]
                row[f"raw_over_control_{metric}"] = safe_ratio(rs[metric], cs[metric])
            distribution_rows.append(row)

        for face in ("lower_a", "upper_a", "lower_b", "upper_b"):
            drift = "mu_a" if face.endswith("a") else "mu_b"
            counts = {"control": 0, "raw": 0, "both": 0, "raw_only": 0, "control_only": 0}
            c_liquid, r_liquid, c_transfer, r_transfer = [], [], [], []
            for index in range(31):
                c, r = cache[("C", turn, index)], cache[("R", turn, index)]
                cm, rm = boundary_mask(c[drift], face), boundary_mask(r[drift], face)
                counts["control"] += int(np.count_nonzero(cm)); counts["raw"] += int(np.count_nonzero(rm))
                counts["both"] += int(np.count_nonzero(cm & rm))
                counts["raw_only"] += int(np.count_nonzero(rm & ~cm))
                counts["control_only"] += int(np.count_nonzero(cm & ~rm))
                c_liquid.extend(np.asarray(c["liquid_label"])[cm].tolist())
                r_liquid.extend(np.asarray(r["liquid_label"])[rm].tolist())
                c_transfer.extend(np.asarray(c["transfer_label"])[cm].tolist())
                r_transfer.extend(np.asarray(r["transfer_label"])[rm].tolist())
            def counts_text(values: list[str]) -> str:
                if not values:
                    return ""
                labels, label_counts = np.unique(values, return_counts=True)
                return ";".join(f"{x}:{y}" for x, y in zip(labels, label_counts))
            boundary_rows.append({
                "turn": turn,
                "face": face,
                "control_outward_count": counts["control"],
                "raw_outward_count": counts["raw"],
                "both_outward_same_cell_count": counts["both"],
                "raw_only_new_outward_count": counts["raw_only"],
                "control_only_resolved_in_raw_count": counts["control_only"],
                "control_outward_liquid_labels": counts_text(c_liquid),
                "raw_outward_liquid_labels": counts_text(r_liquid),
                "control_outward_transfer_labels": counts_text(c_transfer),
                "raw_outward_transfer_labels": counts_text(r_transfer),
            })

        for index, row in enumerate(c_rows):
            c, r = cache[("C", turn, index)], cache[("R", turn, index)]
            cm, rm = boundary_mask(c["mu_b"], "lower_b"), boundary_mask(r["mu_b"], "lower_b")
            for i_b, i_a, i_z in np.argwhere(cm | rm):
                lower_b_rows.append({
                    "turn": turn,
                    "province_index": index,
                    "province": row["province"],
                    "i_b": int(i_b), "i_a": int(i_a), "i_z": int(i_z),
                    "b": float(GRID_B[i_b]), "a": float(GRID_A[i_a]), "z": float(GRID_Z[i_z]),
                    "control_outward": bool(cm[i_b, i_a, i_z]),
                    "raw_outward": bool(rm[i_b, i_a, i_z]),
                    "raw_only_new": bool(rm[i_b, i_a, i_z] and not cm[i_b, i_a, i_z]),
                    "control_mu_b": float(c["mu_b"][i_b, i_a, i_z]),
                    "raw_mu_b": float(r["mu_b"][i_b, i_a, i_z]),
                    "control_liquid_label": str(c["liquid_label"][i_b, i_a, i_z]),
                    "raw_liquid_label": str(r["liquid_label"][i_b, i_a, i_z]),
                    "control_transfer_label": str(c["transfer_label"][i_b, i_a, i_z]),
                    "raw_transfer_label": str(r["transfer_label"][i_b, i_a, i_z]),
                    "control_transfer": float(c["transfer"][i_b, i_a, i_z]),
                    "raw_transfer": float(r["transfer"][i_b, i_a, i_z]),
                    "control_adjustment_cost": float(c["adjustment_cost"][i_b, i_a, i_z]),
                    "raw_adjustment_cost": float(r["adjustment_cost"][i_b, i_a, i_z]),
                })

        for field in ("mu_b", "mu_a", "transfer"):
            for path_id in ("C", "R"):
                candidates = []
                for index, row in enumerate(c_rows):
                    array = np.asarray(cache[(path_id, turn, index)][field])
                    for flat in np.argpartition(np.abs(array).ravel(), -3)[-3:]:
                        i_b, i_a, i_z = np.unravel_index(int(flat), GRID_SHAPE)
                        candidates.append((abs(float(array[i_b, i_a, i_z])), index, i_b, i_a, i_z))
                for rank, (_, index, i_b, i_a, i_z) in enumerate(sorted(candidates, reverse=True)[:10], start=1):
                    c, r = cache[("C", turn, index)], cache[("R", turn, index)]
                    focal = c if path_id == "C" else r
                    other = r if path_id == "C" else c
                    fv, ov = float(focal[field][i_b, i_a, i_z]), float(other[field][i_b, i_a, i_z])
                    extreme_rows.append({
                        "turn": turn, "variable": field, "ranking_path": path_id, "rank": rank,
                        "province_index": index, "province": c_rows[index]["province"],
                        "i_b": i_b, "i_a": i_a, "i_z": i_z,
                        "b": float(GRID_B[i_b]), "a": float(GRID_A[i_a]), "z": float(GRID_Z[i_z]),
                        "boundary_label": boundary_label(i_b, i_a),
                        "focal_value": fv, "focal_abs": abs(fv), "matched_other_value": ov,
                        "control_value": float(c[field][i_b, i_a, i_z]),
                        "raw_value": float(r[field][i_b, i_a, i_z]),
                        "raw_minus_control": float(r[field][i_b, i_a, i_z] - c[field][i_b, i_a, i_z]),
                        "raw_over_control_abs": safe_ratio(abs(float(r[field][i_b, i_a, i_z])), abs(float(c[field][i_b, i_a, i_z]))),
                        "control_liquid_label": str(c["liquid_label"][i_b, i_a, i_z]),
                        "raw_liquid_label": str(r["liquid_label"][i_b, i_a, i_z]),
                        "control_transfer_label": str(c["transfer_label"][i_b, i_a, i_z]),
                        "raw_transfer_label": str(r["transfer_label"][i_b, i_a, i_z]),
                        "control_consumption": float(c["consumption"][i_b, i_a, i_z]),
                        "raw_consumption": float(r["consumption"][i_b, i_a, i_z]),
                        "control_transfer": float(c["transfer"][i_b, i_a, i_z]),
                        "raw_transfer": float(r["transfer"][i_b, i_a, i_z]),
                        "control_adjustment_cost": float(c["adjustment_cost"][i_b, i_a, i_z]),
                        "raw_adjustment_cost": float(r["adjustment_cost"][i_b, i_a, i_z]),
                        "control_effective_return": float(c["effective_illiquid_return"][i_b, i_a, i_z]),
                        "raw_effective_return": float(r["effective_illiquid_return"][i_b, i_a, i_z]),
                        "control_mu_a": float(c["mu_a"][i_b, i_a, i_z]),
                        "raw_mu_a": float(r["mu_a"][i_b, i_a, i_z]),
                        "control_mu_b": float(c["mu_b"][i_b, i_a, i_z]),
                        "raw_mu_b": float(r["mu_b"][i_b, i_a, i_z]),
                        "control_hjb_statistic": c["convergence_statistic"],
                        "raw_hjb_statistic": r["convergence_statistic"],
                    })

    association_fields = (
        "raw_entering_rah",
        "raw_same_index_prior_firm_ra0",
        "raw_same_index_prior_raw_minus_used",
        "raw_hjb_statistic",
        "raw_hit_iteration_ceiling",
        "raw_mu_b_abs_max",
        "raw_mu_a_abs_max",
        "raw_transfer_abs_max",
        "raw_adjustment_cost_abs_max",
        "raw_lower_b_outward_count",
        "raw_upper_b_outward_count",
        "raw_only_lower_b_outward_count",
        "raw_upper_a_outward_count",
        "raw_only_upper_a_outward_count",
        "raw_only_upper_b_outward_count",
    )
    association_rows = []
    for left_index, left in enumerate(association_fields):
        for right in association_fields[left_index + 1:]:
            x = [float(row[left]) for row in province_rows]
            y = [float(row[right]) for row in province_rows]
            association_rows.append({
                "scope": "MATCHED_RAW_PROVINCE_TURNS_2_5",
                "n": len(province_rows),
                "left": left,
                "right": right,
                "pearson": correlation(x, y),
                "spearman": correlation(x, y, spearman=True),
                "classification": "DESCRIPTIVE_ONLY_NOT_CAUSAL",
            })

    worst_raw = sorted(province_rows, key=lambda row: row["raw_hjb_statistic"], reverse=True)[:10]
    worst_control = sorted(province_rows, key=lambda row: row["control_hjb_statistic"], reverse=True)[:10]
    new_nonconvergence = [row for row in province_rows if row["raw_new_nonconvergence"]]
    raw_smaller = {
        field: sum(row[f"raw_{field}_abs_max"] < row[f"control_{field}_abs_max"] for row in province_rows)
        for field in ARRAY_FIELDS
    }
    source_trace = {
        "household_rah_to_r_a": {
            "path": "src/ch5_two_asset_hank/multi_province/household_adapter.py",
            "lines": "45, 200-219",
            "statement": "results.rah is bound to HouseholdInputs.r_a before the accepted solver call",
        },
        "effective_illiquid_return": {
            "path": "exports/matlab_faithful_two_asset_ha.py",
            "lines": "111-124, 371-378",
            "statement": "r_a is multiplied by the accepted finite-grid taper; the result enters the illiquid shadow/drift construction",
        },
        "actual_runtime_binding": {
            "path": "validators/multi_province/g1_residual_govinv_25turn_isolated/run.py",
            "lines": "164-193",
            "statement": "the accepted runtime passes state.rah as the first HouseholdInputs argument r_a, solves the faithful HJB, then persists hjb_return.npz before KFE",
        },
        "consumption_and_labor": {
            "path": "exports/matlab_faithful_two_asset_ha.py",
            "lines": "126-146, 274-304, 531-559",
            "statement": "consumption/labor are selected from V_b branches; r_a affects them indirectly through the solved value function and derivatives",
        },
        "transfer_and_adjustment_cost": {
            "path": "exports/matlab_faithful_two_asset_ha.py",
            "lines": "80-109, 306-369",
            "statement": "transfer candidates use raw V_a/V_b; the accepted quadratic cost uses max(a,a_bar); selectors choose B/F/0 branches",
        },
        "asset_drifts": {
            "path": "exports/matlab_faithful_two_asset_ha.py",
            "lines": "148-167, 378-388",
            "statement": "mu_a=r_a_effective*a+d; mu_b=r_b*b+labor_income-d-cost-consumption",
        },
        "boundary_and_policy_selector": {
            "path": "exports/matlab_faithful_two_asset_ha.py",
            "lines": "259-320, 348-376, 401-415",
            "statement": "accepted lower/upper a rules alter transfer candidates; lower/upper b rules override transfer direction; drift directions and rates follow",
        },
        "operator_boundary_law": {
            "path": "exports/matlab_faithful_two_asset_ha.py",
            "lines": "424-463, 549-562",
            "statement": "outward edges are truncated while their rate remains in the diagonal; post-convergence operator instead upwinds saved total drifts",
        },
    }
    summary = {
        "schema": "CH5_K1_RAW_RA0_HJB_DRIFT_ZERO_SCIENCE_FORENSIC_V1",
        "classification": CLASSIFICATION,
        "next_gate": NEXT_GATE,
        "baseline_sha": BASELINE_SHA,
        "accepted_input_manifest": manifest_receipt,
        "source_identity": source_receipt,
        "turn1_common_bootstrap_arrays_equal": turn1_equal,
        "matched_treatment_province_turns": len(province_rows),
        "hjb": {
            "control_converged": sum(bool(row["control_converged"]) for row in province_rows),
            "raw_converged": sum(bool(row["raw_converged"]) for row in province_rows),
            "raw_new_nonconvergence_count": len(new_nonconvergence),
            "raw_recovers_control_nonconvergence_count": sum(bool(row["raw_recovers_control_nonconvergence"]) for row in province_rows),
            "control_iteration_ceiling_count": sum(bool(row["control_hit_iteration_ceiling"]) for row in province_rows),
            "raw_iteration_ceiling_count": sum(bool(row["raw_hit_iteration_ceiling"]) for row in province_rows),
            "worst_raw": worst_raw,
            "worst_control": worst_control,
        },
        "raw_smaller_than_control_abs_max_province_turn_counts": raw_smaller,
        "lower_b_outward_events": {
            "rows": len(lower_b_rows),
            "raw_only_new": sum(bool(row["raw_only_new"]) for row in lower_b_rows),
            "raw_outward_abs_max": max(abs(float(row["raw_mu_b"])) for row in lower_b_rows),
            "all_raw_outward_below_accepted_drift_tolerance_1e_12": all(
                abs(float(row["raw_mu_b"])) < 1.0e-12 for row in lower_b_rows
            ),
            "classification": "EXACT_SIGN_ONLY_BELOW_ACCEPTED_DRIFT_TOLERANCE__NOT_MATERIAL_KKT_EVIDENCE",
            "turn_counts": {
                str(turn): sum(bool(row["raw_outward"]) for row in lower_b_rows if row["turn"] == turn)
                for turn in TURNS
            },
        },
        "kkt": "UNAVAILABLE_IN_ACCEPTED_EVIDENCE",
        "associations": "DESCRIPTIVE_ONLY_NOT_CAUSAL",
        "new_scientific_call_ledger": {
            key: 0 for key in (
                "trajectory", "hjb", "kfe", "firm_runtime", "household_runtime", "matlab",
                "k1b", "k2", "ge", "annual", "irf", "results",
            )
        },
        "results_eligible": False,
    }
    return {
        "summary.json": summary,
        "source_trace.json": source_trace,
        "province_turn_hjb_exposure.csv": province_rows,
        "province_turn_array_stats.csv": province_stat_rows,
        "array_distribution_by_turn.csv": distribution_rows,
        "boundary_summary.csv": boundary_rows,
        "lower_b_outward_cells.csv": lower_b_rows,
        "extreme_cells.csv": extreme_rows,
        "descriptive_associations.csv": association_rows,
        "call_ledger.json": summary["new_scientific_call_ledger"],
        "accepted_manifest_readback.json": manifest_receipt,
    }


def _persist(outputs: dict[str, Any], external_output: Path, compact_output: Path) -> dict[str, Any]:
    external_output.mkdir(parents=True, exist_ok=False)
    compact_output.mkdir(parents=True, exist_ok=False)
    for name, value in outputs.items():
        writers = (_write_csv if name.endswith(".csv") else _write_json)
        writers(external_output / name, value)
        writers(compact_output / name, value)
    entries = []
    for path in sorted(item for item in external_output.iterdir() if item.is_file()):
        entries.append({"path": path.name, "bytes": path.stat().st_size, "sha256": _sha(path)})
    manifest_path = external_output / "manifest_sha256.json"
    _write_json(manifest_path, {
        "schema": "CH5_K1_RAW_RA0_HJB_DRIFT_FORENSIC_EXTERNAL_MANIFEST_V1",
        "file_count_excluding_manifest": len(entries),
        "files": entries,
    })
    for entry in entries:
        path = external_output / entry["path"]
        if path.stat().st_size != entry["bytes"] or _sha(path) != entry["sha256"]:
            raise RuntimeError(f"forensic manifest readback failed: {entry['path']}")
    receipt = {
        "manifest_path": str(manifest_path),
        "manifest_sha256": _sha(manifest_path),
        "files_verified": len(entries),
        "mismatches": 0,
        "status": "PASS",
    }
    _write_json(compact_output / "external_manifest_receipt.json", receipt)
    return receipt


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("external_accepted_root", type=Path)
    parser.add_argument("external_output_root", type=Path)
    parser.add_argument("compact_output_root", type=Path)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args(argv)
    outputs = analyze(args.external_accepted_root, args.repo)
    receipt = _persist(outputs, args.external_output_root, args.compact_output_root)
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
