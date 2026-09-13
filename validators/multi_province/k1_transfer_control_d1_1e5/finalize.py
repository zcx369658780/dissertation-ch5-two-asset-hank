"""Zero-science finalizer for the completed control/D1 bounded trajectories."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
from collections import Counter, defaultdict
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable

import numpy as np

from validators.multi_province.k1_transfer_control_raw_candidate_census.census import BRANCHES, file_sha256

from .receipt import D1_LIMIT
from .run import PATHS, TASK_ID


QUANTILES = (0.5, 0.9, 0.95, 0.99, 0.999, 0.9999)
ARRAY_FIELDS = ("transfer", "adjustment_cost", "mu_a", "mu_b", "consumption", "labor")


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        raise FileExistsError(destination)
    destination.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def array_hash(value: np.ndarray) -> str:
    array = np.asarray(value)
    header = f"{array.dtype.str}|{array.shape}|C|".encode("ascii")
    return sha256(header + np.ascontiguousarray(array).tobytes()).hexdigest().upper()


def arrays_equal(left: np.ndarray, right: np.ndarray) -> bool:
    left_array, right_array = np.asarray(left), np.asarray(right)
    equal_nan = np.issubdtype(left_array.dtype, np.inexact) and np.issubdtype(right_array.dtype, np.inexact)
    return bool(np.array_equal(left_array, right_array, equal_nan=equal_nan))


def distribution(values: Iterable[np.ndarray]) -> dict[str, Any]:
    array = np.concatenate([np.asarray(value, dtype=np.float64).reshape(-1) for value in values])
    finite = array[np.isfinite(array)]
    result = {
        "count": int(array.size),
        "finite": int(finite.size),
        "nonfinite": int(array.size - finite.size),
    }
    if finite.size:
        absolute = np.abs(finite)
        result.update({
            "min": float(np.min(finite)),
            "max": float(np.max(finite)),
            "abs_max": float(np.max(absolute)),
            "quantiles": {str(q): float(v) for q, v in zip(QUANTILES, np.quantile(finite, QUANTILES))},
            "abs_quantiles": {str(q): float(v) for q, v in zip(QUANTILES, np.quantile(absolute, QUANTILES))},
        })
    return result


def chunk_map(root: Path, path_id: str) -> dict[tuple[int, str], Path]:
    paths = sorted((root / "d1_cell_receipts" / path_id).glob("turn_*/*.npz"))
    if len(paths) != 155:
        raise RuntimeError(f"{path_id}: expected 155 chunks, found {len(paths)}")
    result = {}
    for path in paths:
        with np.load(path, allow_pickle=False) as payload:
            meta = json.loads(str(payload["metadata_json"]))
        result[(int(meta["turn"]), str(meta["province"]))] = path
    if len(result) != 155:
        raise RuntimeError(f"{path_id}: chunk metadata keys are not unique")
    return result


def scientific_turn_equality(evidence: Path, maps: dict[str, dict[tuple[int, str], Path]]) -> dict[str, Any]:
    c_root = evidence / PATHS["C"][0]
    d_root = evidence / PATHS["D1"][0]
    payload_bytes_equal = c_root.joinpath("runtime_input_payload.json").read_bytes() == d_root.joinpath("runtime_input_payload.json").read_bytes()
    entering_turn1_equal = read_json(c_root / "turn_01" / "entering_state.json")["states"] == read_json(d_root / "turn_01" / "entering_state.json")["states"]
    c_turn2_states = read_json(c_root / "turn_02" / "entering_state.json")["states"]
    d_turn2_states = read_json(d_root / "turn_02" / "entering_state.json")["states"]
    entering_turn2_equal = c_turn2_states == d_turn2_states

    def entering_wage_status(state: dict[str, Any]) -> str:
        wage = float(state["wjt"])
        if wage == float(state["wjtmin"]):
            return "lower"
        if wage == float(state["wjtmax"]):
            return "upper"
        return "unsaturated"

    turn2_wage_status_exact = all(
        left["name"] == right["name"]
        and float(left["wjt"]) == float(right["wjt"])
        and entering_wage_status(left) == entering_wage_status(right)
        for left, right in zip(c_turn2_states, d_turn2_states)
    )
    chunk_fields = (
        "raw_d", "selected_transfer", "selected_transfer_label", "selected_adjustment_cost",
        "selected_mu_a", "selected_mu_b", "selected_consumption", "selected_labor",
        "selected_liquid_label", "value_new", "convergence_statistic", "operator_sha256",
        "grid_b", "grid_a", "grid_z", "grid_switch_matrix", "final_converged",
        "final_convergence_statistic",
    )
    compared_arrays = 0
    turn1_chunk_exact = True
    turn2_first_iteration_raw_exact = True
    turn2_grid_exact = True
    turn2_hjb_inputs_exact = True
    for province in [key[1] for key in maps["C"] if key[0] == 1]:
        with np.load(maps["C"][(1, province)], allow_pickle=False) as left, np.load(maps["D1"][(1, province)], allow_pickle=False) as right:
            for field in chunk_fields:
                compared_arrays += 1
                if not arrays_equal(left[field], right[field]):
                    turn1_chunk_exact = False
    for province in [key[1] for key in maps["C"] if key[0] == 2]:
        with np.load(maps["C"][(2, province)], allow_pickle=False) as left, np.load(maps["D1"][(2, province)], allow_pickle=False) as right:
            if not arrays_equal(left["raw_d"][0], right["raw_d"][0]):
                turn2_first_iteration_raw_exact = False
            for field in ("grid_b", "grid_a", "grid_z", "grid_switch_matrix"):
                if not arrays_equal(left[field], right[field]):
                    turn2_grid_exact = False
            left_meta = json.loads(str(left["metadata_json"]))
            right_meta = json.loads(str(right["metadata_json"]))
            for field in ("province", "province_index", "turn", "hjb_input_r_a", "hjb_input_wage"):
                if left_meta[field] != right_meta[field]:
                    turn2_hjb_inputs_exact = False

    turn2_c = read_json(c_root / "turn_02" / "per_province_observables.json")
    turn2_d = read_json(d_root / "turn_02" / "per_province_observables.json")
    entering_provenance_fields = (
        "raw_converted_rah_annual", "hjb_consumed_r_a",
        "portfolio_shares_sha256", "quantity_and_rah_same_S", "same_turn_household_feedback",
    )
    turn2_entering_provenance_equal = all(
        left["province"] == right["province"]
        and all(left[field] == right[field] for field in entering_provenance_fields)
        for left, right in zip(turn2_c, turn2_d)
    )
    status = all((payload_bytes_equal, entering_turn1_equal, entering_turn2_equal,
                  turn1_chunk_exact, turn2_first_iteration_raw_exact, turn2_grid_exact,
                  turn2_hjb_inputs_exact, turn2_wage_status_exact,
                  turn2_entering_provenance_equal))
    return {
        "status": "PASS" if status else "FAIL",
        "runtime_payload_bytes_equal": payload_bytes_equal,
        "turn1_entering_states_equal": entering_turn1_equal,
        "completed_turn1_entering_turn2_states_equal": entering_turn2_equal,
        "turn1_hjb_scientific_arrays_exact": turn1_chunk_exact,
        "turn1_hjb_arrays_compared": compared_arrays,
        "turn2_first_iteration_raw_candidates_exact": turn2_first_iteration_raw_exact,
        "turn2_grid_arrays_exact": turn2_grid_exact,
        "turn2_hjb_return_and_wage_inputs_exact": turn2_hjb_inputs_exact,
        "turn2_entering_wage_guard_status_exact": turn2_wage_status_exact,
        "turn2_return_and_same_S_provenance_inputs_equal": turn2_entering_provenance_equal,
    }


def path_diagnostics(evidence: Path, path_id: str, paths: dict[tuple[int, str], Path]) -> dict[str, Any]:
    root = evidence / PATHS[path_id][0]
    turns = []
    for turn in range(1, 6):
        call_paths = [path for (number, _), path in paths.items() if number == turn]
        iterations, statistics, converged = [], [], []
        for path in call_paths:
            with np.load(path, allow_pickle=False) as payload:
                iterations.append(int(payload["iteration"].size))
                statistics.append(float(payload["final_convergence_statistic"]))
                converged.append(bool(payload["final_converged"]))
        field_values: dict[str, list[np.ndarray]] = {field: [] for field in ARRAY_FIELDS}
        liquid_labels: Counter[str] = Counter()
        transfer_labels: Counter[str] = Counter()
        for province_index, province in enumerate(read_json(root / f"turn_{turn:02d}" / "per_province_observables.json")):
            hjb_path = root / f"turn_{turn:02d}" / "household" / f"p{province_index:02d}_{province['province']}" / "hjb_return.npz"
            with np.load(hjb_path, allow_pickle=False) as payload:
                for field in ARRAY_FIELDS:
                    field_values[field].append(np.asarray(payload[field]))
                liquid_labels.update(map(str, np.asarray(payload["liquid_label"]).reshape(-1)))
                transfer_labels.update(map(str, np.asarray(payload["transfer_label"]).reshape(-1)))
        rows = read_json(root / f"turn_{turn:02d}" / "per_province_observables.json")
        turns.append({
            "turn": turn,
            "hjb_calls": len(call_paths),
            "hjb_iterations": sum(iterations),
            "hjb_converged_count": sum(converged),
            "hjb_nonconverged_count": len(converged) - sum(converged),
            "iteration_ceiling_hits": sum(value == 100 for value in iterations),
            "hjb_statistic_median": float(np.median(statistics)),
            "hjb_statistic_max": float(np.max(statistics)),
            "arrays": {field: distribution(values) for field, values in field_values.items()},
            "liquid_label_counts": dict(liquid_labels),
            "transfer_label_counts": dict(transfer_labels),
            "material_outward_boundaries": {
                field: sum(int(row[field]) for row in rows)
                for field in ("hjb_lower_a_outward_count", "hjb_upper_a_outward_count",
                              "hjb_lower_b_outward_count", "hjb_upper_b_outward_count")
            },
            "saved_hjb_nonfinite_count": sum(int(row["hjb_saved_array_nonfinite_count"]) for row in rows),
            "outer_residuals": {
                "nk_gap_abs_max": max(abs(float(row["nk_gap"])) for row in rows),
                "GDP_level_gap_abs_max": max(abs(float(row["GDP_level_gap"])) for row in rows),
                "yt_gap_abs_max": max(abs(float(row["yt_gap"])) for row in rows),
            },
        })
    ledger = read_json(root / "call_ledger.json")["counts"]
    return {"path_id": path_id, "turns": turns, "call_ledger": ledger}


def d1_aggregates(paths: dict[tuple[int, str], Path]) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, Any]]:
    branch = {name: [0, 0] for name in BRANCHES}
    sign = {"positive": 0, "negative": 0, "zero": 0}
    boundary = {name: [0, 0] for name in ("INTERIOR", "LOWER_A", "UPPER_A", "LOWER_B", "UPPER_B")}
    convergence = {name: defaultdict(int) for name in ("CONVERGED", "NONCONVERGED")}
    province_turn: dict[tuple[int, str], defaultdict[str, int]] = defaultdict(lambda: defaultdict(int))
    iteration_rows = []
    first: dict[str, Any] = {}
    totals: defaultdict[str, int] = defaultdict(int)
    for (turn, province), path in sorted(paths.items(), key=lambda item: (item[0][0], item[1].name)):
        with np.load(path, allow_pickle=False) as payload:
            raw = np.asarray(payload["raw_d"])
            admissible = np.asarray(payload["d1_admissible"])
            hit = ~admissible
            direction = np.asarray(payload["raw_branch_in_control_winning_direction"])
            contributor = np.asarray(payload["raw_branch_existing_contributor_to_control"])
            changed = np.asarray(payload["winner_changed"])
            fallback = np.asarray(payload["fallback_to_existing_zero"])
            other = np.asarray(payload["switch_to_other_admissible_nonzero"])
            bits = np.asarray(payload["boundary_bits"])
            active = bool(payload["d1_active"])
            if active:
                totals["active_raw_candidate_count"] += raw.size
                totals["d1_inadmissible_count"] += int(np.count_nonzero(hit))
                totals["rejected_never_in_control_winning_direction_count"] += int(np.count_nonzero(hit & ~direction))
                totals["rejected_in_control_winning_direction_count"] += int(np.count_nonzero(hit & direction))
                totals["rejected_control_contributor_count"] += int(np.count_nonzero(hit & contributor))
                totals["winner_changed_count"] += int(np.count_nonzero(changed))
                totals["fallback_to_existing_zero_count"] += int(np.count_nonzero(fallback))
                totals["switch_to_other_admissible_nonzero_count"] += int(np.count_nonzero(other))
                final = -1
                totals["final_iteration_cell_count"] += changed[final].size
                totals["final_winner_changed_count"] += int(np.count_nonzero(changed[final]))
                totals["final_fallback_to_existing_zero_count"] += int(np.count_nonzero(fallback[final]))
                totals["final_switch_to_other_admissible_nonzero_count"] += int(np.count_nonzero(other[final]))
            for index, name in enumerate(BRANCHES):
                branch[name][0] += int(raw[:, index].size) if active else 0
                branch[name][1] += int(np.count_nonzero(hit[:, index]))
            sign["positive"] += int(np.count_nonzero(hit & (raw > 0)))
            sign["negative"] += int(np.count_nonzero(hit & (raw < 0)))
            sign["zero"] += int(np.count_nonzero(hit & (raw == 0)))
            bit_masks = {
                "INTERIOR": bits == 0,
                "LOWER_A": (bits & 1) != 0,
                "UPPER_A": (bits & 2) != 0,
                "LOWER_B": (bits & 4) != 0,
                "UPPER_B": (bits & 8) != 0,
            }
            for name, mask in bit_masks.items():
                expanded = np.broadcast_to(mask, raw.shape)
                boundary[name][0] += int(np.count_nonzero(expanded)) if active else 0
                boundary[name][1] += int(np.count_nonzero(hit & expanded))
            conv_key = "CONVERGED" if bool(payload["final_converged"]) else "NONCONVERGED"
            convergence[conv_key]["raw_candidate_count"] += raw.size if active else 0
            convergence[conv_key]["hit_count"] += int(np.count_nonzero(hit))
            convergence[conv_key]["winner_changed_count"] += int(np.count_nonzero(changed))
            pt = province_turn[(turn, province)]
            pt["raw_candidate_count"] += raw.size if active else 0
            pt["hit_count"] += int(np.count_nonzero(hit))
            pt["winner_changed_count"] += int(np.count_nonzero(changed))
            pt["fallback_to_zero_count"] += int(np.count_nonzero(fallback))
            pt["switch_to_other_nonzero_count"] += int(np.count_nonzero(other))
            for iteration_index in range(raw.shape[0]):
                iteration_rows.append({
                    "turn": turn,
                    "province": province,
                    "iteration": iteration_index + 1,
                    "d1_active": active,
                    "raw_candidate_count": int(raw[iteration_index].size) if active else 0,
                    "hit_count": int(np.count_nonzero(hit[iteration_index])),
                    "winner_changed_count": int(np.count_nonzero(changed[iteration_index])),
                    "fallback_to_zero_count": int(np.count_nonzero(fallback[iteration_index])),
                    "switch_to_other_nonzero_count": int(np.count_nonzero(other[iteration_index])),
                })
            if not first and np.any(hit):
                index = tuple(int(value) for value in np.argwhere(hit)[0])
                iteration_index, branch_index, i_b, i_a, i_z = index
                first = {
                    "turn": turn,
                    "province": province,
                    "iteration": iteration_index + 1,
                    "branch": BRANCHES[branch_index],
                    "grid_index_zero_based": [i_b, i_a, i_z],
                    "raw_d": float(raw[index]),
                    "sign": "POSITIVE" if raw[index] > 0 else "NEGATIVE",
                    "control_winning_direction": bool(direction[index]),
                    "control_selected_contributor": bool(contributor[index]),
                    "control_transfer_label": str(payload["control_transfer_label"][(iteration_index, i_b, i_a, i_z)]),
                    "control_transfer": float(payload["control_transfer"][(iteration_index, i_b, i_a, i_z)]),
                    "d1_transfer_label": str(payload["selected_transfer_label"][(iteration_index, i_b, i_a, i_z)]),
                    "d1_transfer": float(payload["selected_transfer"][(iteration_index, i_b, i_a, i_z)]),
                    "fallback_to_existing_zero": bool(fallback[(iteration_index, i_b, i_a, i_z)]),
                    "switch_to_other_admissible_nonzero": bool(other[(iteration_index, i_b, i_a, i_z)]),
                    "control_adjustment_cost": float(payload["control_adjustment_cost"][(iteration_index, i_b, i_a, i_z)]),
                    "d1_adjustment_cost": float(payload["selected_adjustment_cost"][(iteration_index, i_b, i_a, i_z)]),
                    "control_mu_a": float(payload["control_mu_a"][(iteration_index, i_b, i_a, i_z)]),
                    "d1_mu_a": float(payload["selected_mu_a"][(iteration_index, i_b, i_a, i_z)]),
                    "control_mu_b": float(payload["control_mu_b"][(iteration_index, i_b, i_a, i_z)]),
                    "d1_mu_b": float(payload["selected_mu_b"][(iteration_index, i_b, i_a, i_z)]),
                    "control_liquid_label": str(payload["control_liquid_label"][(iteration_index, i_b, i_a, i_z)]),
                    "d1_liquid_label": str(payload["selected_liquid_label"][(iteration_index, i_b, i_a, i_z)]),
                    "d1_operator_sha256": str(payload["operator_sha256"][iteration_index]),
                    "d1_value_new_sha256": array_hash(payload["value_new"][iteration_index]),
                    "d1_value_new_at_cell": float(payload["value_new"][(iteration_index, i_b, i_a, i_z)]),
                    "d1_hjb_statistic": float(payload["convergence_statistic"][iteration_index]),
                }
    totals["d1_inadmissible_share"] = totals["d1_inadmissible_count"] / totals["active_raw_candidate_count"]
    totals["winner_changed_share_of_iteration_cells"] = totals["winner_changed_count"] / (totals["active_raw_candidate_count"] / 4)
    summary = {
        "d1_limit": D1_LIMIT,
        "totals": dict(totals),
        "by_branch": {name: {"raw_candidate_count": values[0], "hit_count": values[1],
                              "hit_share": values[1] / values[0]} for name, values in branch.items()},
        "hit_sign_counts": sign,
        "by_boundary": {name: {"raw_candidate_count": values[0], "hit_count": values[1],
                                "hit_share": values[1] / values[0] if values[0] else None}
                        for name, values in boundary.items()},
        "by_hjb_final_convergence": {name: dict(values) for name, values in convergence.items()},
        "by_province_turn": [dict(turn=key[0], province=key[1], **values)
                              for key, values in sorted(province_turn.items())],
    }
    return summary, iteration_rows, first


def attach_first_rejection_control(first: dict[str, Any], control_path: Path) -> dict[str, Any]:
    with np.load(control_path, allow_pickle=False) as payload:
        iteration = int(first["iteration"]) - 1
        i_b, i_a, i_z = first["grid_index_zero_based"]
        raw = np.asarray(payload["raw_d"])[iteration, :, i_b, i_a, i_z]
        first.update({
            "control_trajectory_raw_at_cell": raw.astype(float).tolist(),
            "raw_before_eligibility_exact_against_control_trajectory": bool(
                raw[BRANCHES.index(first["branch"])] == first["raw_d"]
            ),
            "control_trajectory_transfer_label": str(payload["selected_transfer_label"][(iteration, i_b, i_a, i_z)]),
            "control_trajectory_transfer": float(payload["selected_transfer"][(iteration, i_b, i_a, i_z)]),
            "control_trajectory_operator_sha256": str(payload["operator_sha256"][iteration]),
            "control_trajectory_value_new_sha256": array_hash(payload["value_new"][iteration]),
            "control_trajectory_value_new_at_cell": float(payload["value_new"][(iteration, i_b, i_a, i_z)]),
            "control_trajectory_hjb_statistic": float(payload["convergence_statistic"][iteration]),
        })
    return first


def price_and_science(evidence: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    monitoring, all_rows = [], []
    for path_id, (folder, _) in PATHS.items():
        for turn in range(1, 6):
            rows = read_json(evidence / folder / f"turn_{turn:02d}" / "per_province_observables.json")
            all_rows.extend(rows)
            def names(field: str) -> list[str]:
                return [str(row["province"]) for row in rows if bool(row[field])]
            monitoring.append({
                "path_id": path_id,
                "turn": turn,
                "return_raw_min": min(float(row["raw_converted_rah_annual"]) for row in rows),
                "return_raw_max": max(float(row["raw_converted_rah_annual"]) for row in rows),
                "return_guarded_min": min(float(row["hjb_consumed_r_a"]) for row in rows),
                "return_guarded_max": max(float(row["hjb_consumed_r_a"]) for row in rows),
                "return_lower_names": names("return_guard_lower_hit"),
                "return_upper_names": names("return_guard_upper_hit"),
                "return_unsaturated_names": names("return_guard_unsaturated"),
                "wage_raw_min": min(float(row["firm_wage_raw"]) for row in rows),
                "wage_raw_max": max(float(row["firm_wage_raw"]) for row in rows),
                "wage_guarded_min": min(float(row["firm_wage_used"]) for row in rows),
                "wage_guarded_max": max(float(row["firm_wage_used"]) for row in rows),
                "wage_lower_names": names("wage_guard_lower_hit"),
                "wage_upper_names": names("wage_guard_upper_hit"),
                "wage_unsaturated_names": names("wage_guard_unsaturated"),
            })
    science = {
        "same_S_all": all(bool(row["quantity_and_rah_same_S"]) for row in all_rows),
        "same_turn_feedback_all_false": all(not bool(row["same_turn_household_feedback"]) for row in all_rows),
        "source_faithful_labor_all": all(bool(row["source_faithful_labor_route"]) for row in all_rows),
        "normalized_labor_all_false": all(not bool(row["normalized_labor_route_active"]) for row in all_rows),
        "capital_column_residual_abs_max": max(abs(float(row["capital_column_residual_MU"])) for row in all_rows),
        "national_private_capital_conservation_residual_abs_max": max(abs(float(row["national_private_capital_conservation_residual_MU"])) for row in all_rows),
        "c1_accounting_abs_residual_max": max(float(row["c1_accounting_abs_residual_MU"]) for row in all_rows),
        "raw_ra0_formula_abs_residual_max": max(float(row["raw_ra0_formula_abs_residual"]) for row in all_rows),
        "hjb_saved_nonfinite_total": sum(int(row["hjb_saved_array_nonfinite_count"]) for row in all_rows),
        "scientific_exceptions": 0,
        "kkt": "UNAVAILABLE_IN_ACCEPTED_EVIDENCE",
        "kfe": "DIAGNOSTIC_ONLY",
    }
    return monitoring, science


def priority_summary(paths: dict[tuple[int, str], Path]) -> list[dict[str, Any]]:
    cases = ((2, "湖北"), (2, "山东"), (2, "广东"), (2, "辽宁"), (2, "吉林"), (4, "四川"), (4, "云南"))
    rows = []
    for turn, province in cases:
        with np.load(paths[(turn, province)], allow_pickle=False) as payload:
            rows.append({
                "turn": turn,
                "province": province,
                "d1_hit_count": int(np.count_nonzero(~payload["d1_admissible"])),
                "winner_changed_count": int(np.count_nonzero(payload["winner_changed"])),
                "fallback_to_zero_count": int(np.count_nonzero(payload["fallback_to_existing_zero"])),
                "switch_to_other_nonzero_count": int(np.count_nonzero(payload["switch_to_other_admissible_nonzero"])),
                "hjb_iterations": int(payload["iteration"].size),
                "hjb_converged": bool(payload["final_converged"]),
                "hjb_statistic": float(payload["final_convergence_statistic"]),
                "selected_transfer_abs_max": float(np.max(np.abs(payload["selected_transfer"][-1]))),
            })
    return rows


def seal_external(evidence: Path) -> dict[str, Any]:
    manifest_path = evidence / "sealed_manifest_sha256.json"
    if manifest_path.exists():
        raise FileExistsError(manifest_path)
    files = sorted(path for path in evidence.rglob("*") if path.is_file())
    entries = [{"path": path.relative_to(evidence).as_posix(), "bytes": path.stat().st_size,
                "sha256": file_sha256(path)} for path in files]
    manifest = {
        "schema": "CH5_K1_TRANSFER_CONTROL_D1_EXTERNAL_MANIFEST_V1",
        "task_id": TASK_ID,
        "entries_excluding_manifest": len(entries),
        "bytes_excluding_manifest": sum(item["bytes"] for item in entries),
        "entries": entries,
    }
    write_json(manifest_path, manifest)
    for item in entries:
        if file_sha256(evidence / item["path"]) != item["sha256"]:
            raise RuntimeError(f"external manifest readback mismatch: {item['path']}")
    return {
        "path": str(manifest_path),
        "sha256": file_sha256(manifest_path),
        "entries_excluding_manifest": len(entries),
        "bytes_excluding_manifest": manifest["bytes_excluding_manifest"],
        "all_entries_readback_verified": True,
    }


def finalize(evidence: Path, compact: Path) -> None:
    evidence, compact = Path(evidence), Path(compact)
    if compact.exists():
        raise FileExistsError(compact)
    maps = {path_id: chunk_map(evidence / folder, path_id) for path_id, (folder, _) in PATHS.items()}
    turn_equality = scientific_turn_equality(evidence, maps)
    if turn_equality["status"] != "PASS":
        raise RuntimeError("turn-1/common-state equality gate failed")
    diagnostics = {path_id: path_diagnostics(evidence, path_id, maps[path_id]) for path_id in PATHS}
    d1, iteration_rows, first = d1_aggregates(maps["D1"])
    first = attach_first_rejection_control(first, maps["C"][(first["turn"], first["province"])])
    monitoring, science = price_and_science(evidence)
    priority = priority_summary(maps["D1"])
    c_total = sum(turn["hjb_converged_count"] for turn in diagnostics["C"]["turns"])
    d_total = sum(turn["hjb_converged_count"] for turn in diagnostics["D1"]["turns"])
    c_post = sum(turn["hjb_converged_count"] for turn in diagnostics["C"]["turns"] if turn["turn"] >= 2)
    d_post = sum(turn["hjb_converged_count"] for turn in diagnostics["D1"]["turns"] if turn["turn"] >= 2)
    summary = {
        "schema": "CH5_K1_TRANSFER_CONTROL_D1_ANALYSIS_V1",
        "task_id": TASK_ID,
        "classification": "D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC_COMPLETE__INDEPENDENT_L3_REVIEW_REQUIRED",
        "turn1_equality": turn_equality,
        "call_ledger": {
            path_id: diagnostics[path_id]["call_ledger"] for path_id in PATHS
        },
        "completed_turns": {"C": 5, "D1": 5},
        "trajectory_invocations": 2,
        "pre_state_engineering_retries": 1,
        "scientific_retries": 0,
        "hjb_calls": 310,
        "kfe_calls": 310,
        "hjb_iterations": {
            path_id: sum(turn["hjb_iterations"] for turn in diagnostics[path_id]["turns"])
            for path_id in PATHS
        },
        "hjb_convergence": {
            "all_turns": {"C": c_total, "D1": d_total, "difference": d_total - c_total},
            "turns_2_5": {"C": c_post, "D1": d_post, "difference": d_post - c_post},
        },
        "d1": d1,
        "first_rejection": first,
        "science_gates": science,
        "longer_d1_authority": "NOT_AUTHORIZED__OWNER_REVIEW_REQUIRED",
        "wider_d_stage_authority": "NOT_AUTHORIZED",
        "results_eligibility": False,
        "kfe": "DIAGNOSTIC_ONLY",
        "kkt": "UNAVAILABLE_IN_ACCEPTED_EVIDENCE",
        "next_gate": "INDEPENDENT_GPT_L3_ACCEPT_OR_REJECT_D1_1E5_BOUNDED_RUNTIME_DIAGNOSTIC_CANDIDATE",
    }
    analysis = evidence / "d1_analysis"
    write_json(analysis / "summary.json", summary)
    write_json(analysis / "path_turn_diagnostics.json", diagnostics)
    write_json(analysis / "turn1_and_turn2_common_state_gate.json", turn_equality)
    write_json(analysis / "d1_hits_and_switches.json", d1)
    write_json(analysis / "first_d1_rejection.json", first)
    write_json(analysis / "price_monitoring.json", monitoring)
    write_json(analysis / "science_gates.json", science)
    write_json(analysis / "priority_checkpoints.json", priority)
    with (analysis / "d1_hits_by_iteration.csv").open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(iteration_rows[0]))
        writer.writeheader()
        writer.writerows(iteration_rows)
    external = seal_external(evidence)
    compact.mkdir(parents=True, exist_ok=False)
    for path in sorted(analysis.iterdir()):
        if path.is_file():
            shutil.copyfile(path, compact / path.name)
    write_json(compact / "external_manifest_receipt.json", external)
    files = sorted(path for path in compact.iterdir() if path.is_file())
    manifest = {
        "schema": "CH5_K1_TRANSFER_CONTROL_D1_COMPACT_MANIFEST_V1",
        "entries_excluding_manifest": len(files),
        "entries": [{"path": path.name, "bytes": path.stat().st_size, "sha256": file_sha256(path)}
                    for path in files],
    }
    write_json(compact / "manifest_sha256.json", manifest)
    print(json.dumps({"summary": summary, "external_manifest": external}, ensure_ascii=False, indent=2))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", type=Path)
    parser.add_argument("compact", type=Path)
    args = parser.parse_args(argv)
    finalize(args.evidence, args.compact)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
