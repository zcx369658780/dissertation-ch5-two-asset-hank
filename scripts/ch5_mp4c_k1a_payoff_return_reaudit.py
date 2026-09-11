"""Read-only re-audit of accepted K1A payoff-return evidence.

This module deliberately uses only the Python standard library.  It neither
imports project/model modules nor invokes a scientific runtime.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import statistics
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


PATHS = {
    "path_a_equal_share": "A_EQUAL_SHARE",
    "path_b_geographic_beta2": "B_GEOGRAPHIC_BETA2",
}
REQUIRED_FIELDS = {
    "turn", "province_index", "province", "Ktarget_2018_MU",
    "Kt_supply_private_MU", "GovInv_after_MU", "firm_K_total_MU", "Y",
    "firm_ra0", "firm_ra_used", "firm_rk", "firm_profit_over_K",
    "firm_after_tax_profit_component_over_K", "firm_ra0_reconstruction_residual",
    "household_rah_k1a_current_payoff_bridge", "ramin", "ramax",
}
STATIC_LABEL = "STATIC_NO_FEEDBACK_COUNTERFACTUAL"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _percentile(values: list[float], percentile: float) -> float:
    if not values:
        raise ValueError("cannot summarize an empty accepted persisted evidence vector")
    ordered = sorted(values)
    position = (len(ordered) - 1) * percentile / 100.0
    lower, upper = math.floor(position), math.ceil(position)
    if lower == upper:
        return ordered[lower]
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (position - lower)


def _rank(values: list[float]) -> list[float]:
    ordered_indices = sorted(range(len(values)), key=values.__getitem__)
    ranks = [0.0] * len(values)
    cursor = 0
    while cursor < len(values):
        end = cursor + 1
        while end < len(values) and values[ordered_indices[end]] == values[ordered_indices[cursor]]:
            end += 1
        rank = (cursor + 1 + end) / 2.0
        for index in ordered_indices[cursor:end]:
            ranks[index] = rank
        cursor = end
    return ranks


def _pearson(left: list[float], right: list[float]) -> float | None:
    if len(left) != len(right) or len(left) < 2:
        return None
    left_mean, right_mean = statistics.fmean(left), statistics.fmean(right)
    numerator = sum((x - left_mean) * (y - right_mean) for x, y in zip(left, right))
    left_scale = math.sqrt(sum((x - left_mean) ** 2 for x in left))
    right_scale = math.sqrt(sum((y - right_mean) ** 2 for y in right))
    if left_scale == 0.0 or right_scale == 0.0:
        return None
    return numerator / (left_scale * right_scale)


def _spearman(left: list[float], right: list[float]) -> float | None:
    return _pearson(_rank(left), _rank(right))


def _distribution(values: list[float]) -> dict[str, float]:
    """Compact descriptive receipt for an already-persisted numeric vector."""
    return {
        "min": min(values), "p1": _percentile(values, 1), "p5": _percentile(values, 5),
        "p25": _percentile(values, 25), "p50": _percentile(values, 50),
        "p75": _percentile(values, 75), "p95": _percentile(values, 95),
        "p99": _percentile(values, 99), "mean": statistics.fmean(values), "max": max(values),
    }


def _float(row: dict[str, str], field: str) -> float:
    try:
        return float(row[field])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"accepted persisted evidence has invalid {field!r}") from exc


def _read_rows(path: Path, expected_turn: int) -> list[dict[str, Any]]:
    # Accepted CSV receipts may carry a UTF-8 BOM; normalize it before
    # validating literal header identities such as ``turn``.
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None or not REQUIRED_FIELDS.issubset(reader.fieldnames):
            missing = sorted(REQUIRED_FIELDS - set(reader.fieldnames or []))
            raise ValueError(f"accepted persisted evidence missing required columns: {missing}")
        rows = list(reader)
    if not rows or any(int(row["turn"]) != expected_turn for row in rows):
        raise ValueError(f"accepted persisted evidence has invalid turn identities in {path}")
    rows.sort(key=lambda row: int(row["province_index"]))
    if [int(row["province_index"]) for row in rows] != list(range(len(rows))):
        raise ValueError(f"accepted persisted evidence lacks a contiguous province_index in {path}")
    return rows


def _read_allocation(path: Path, province_order: list[str]) -> dict[str, Any]:
    try:
        allocation = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"accepted persisted allocation is unreadable: {path}") from exc
    if allocation.get("orientation") != "DESTINATION_BY_ORIGIN":
        raise ValueError("accepted persisted allocation has unexpected share orientation")
    if allocation.get("province_order") != province_order:
        raise ValueError("accepted persisted allocation province_order does not match observables")
    matrix = allocation.get("portfolio_shares_destination_origin")
    returns = allocation.get("household_portfolio_return_by_origin")
    count = len(province_order)
    if not isinstance(matrix, list) or len(matrix) != count or any(not isinstance(row, list) or len(row) != count for row in matrix):
        raise ValueError("accepted persisted allocation lacks a square destination-by-origin S")
    if not isinstance(returns, list) or len(returns) != count:
        raise ValueError("accepted persisted allocation lacks household portfolio returns")
    return allocation


def _aggregate_destination_to_origin(matrix: list[list[float]], returns: list[float]) -> list[float]:
    return [sum(float(matrix[destination][origin]) * returns[destination] for destination in range(len(returns)))
            for origin in range(len(returns))]


def _matrix_max_abs_delta(left: list[list[float]], right: list[list[float]]) -> float:
    return max(abs(float(a) - float(b)) for left_row, right_row in zip(left, right) for a, b in zip(left_row, right_row))


def _write_csv(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    rows = list(rows)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _path_audit(evidence_root: Path, directory: str, path_label: str) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], dict[str, str], dict[int, list[float]], list[str]]:
    path_root = evidence_root / directory
    if not path_root.is_dir():
        raise ValueError(f"accepted persisted evidence path is missing: {path_root}")
    per_turn: list[dict[str, Any]] = []
    province_upper: Counter[str] = Counter()
    static_rows: list[dict[str, Any]] = []
    raw_all: list[float] = []
    used_all: list[float] = []
    gaps: list[float] = []
    reconstruction: list[float] = []
    source_vectors: dict[str, list[float]] = {key: [] for key in ("firm_rk", "firm_profit_over_K", "firm_after_tax_profit_component_over_K", "firm_K_total_MU", "Kt_supply_private_MU", "Ktarget_2018_MU", "Y")}
    input_hashes: dict[str, str] = {}
    province_order: list[str] | None = None
    raw_by_turn: dict[int, list[float]] = {}
    upper_clipped_count = 0
    lower_clipped_count = 0

    for turn in range(1, 26):
        csv_path = path_root / f"turn_{turn:02d}" / "per_province_observables.csv"
        allocation_path = path_root / "capital_network" / f"allocation_{turn:02d}_turn_{turn:02d}.json"
        if not csv_path.is_file() or not allocation_path.is_file():
            raise ValueError(f"accepted persisted evidence is incomplete for {directory} turn {turn:02d}")
        rows = _read_rows(csv_path, turn)
        if len(rows) != 31:
            raise ValueError(f"accepted persisted evidence must contain 31 provinces in {directory} turn {turn:02d}")
        this_order = [row["province"] for row in rows]
        if province_order is None:
            province_order = this_order
        elif province_order != this_order:
            raise ValueError(f"accepted persisted evidence province alignment changed in {directory} turn {turn:02d}")
        allocation = _read_allocation(allocation_path, province_order)
        input_hashes[str(csv_path.relative_to(evidence_root))] = _sha256(csv_path)
        input_hashes[str(allocation_path.relative_to(evidence_root))] = _sha256(allocation_path)

        raw = [_float(row, "firm_ra0") for row in rows]
        used = [_float(row, "firm_ra_used") for row in rows]
        lower = [_float(row, "ramin") for row in rows]
        upper = [_float(row, "ramax") for row in rows]
        if any(value < minimum or value > maximum for value, minimum, maximum in zip(used, lower, upper)):
            raise ValueError(f"accepted persisted used ra is outside recorded bounds in {directory} turn {turn:02d}")
        if any(abs(value - min(max(raw_value, minimum), maximum)) > 1e-12 for raw_value, value, minimum, maximum in zip(raw, used, lower, upper)):
            raise ValueError(f"accepted persisted used ra does not equal clipped raw ra in {directory} turn {turn:02d}")
        current_lagged_payoff = [float(value) for value in allocation["household_portfolio_return_by_origin"]]
        csv_lagged_payoff = [_float(row, "household_rah_k1a_current_payoff_bridge") for row in rows]
        if max(abs(left - right) for left, right in zip(current_lagged_payoff, csv_lagged_payoff)) > 1e-12:
            raise ValueError(f"accepted persisted allocation payoff does not match CSV lagged rah bridge in {directory} turn {turn:02d}")
        upper_count = sum(raw_value > maximum for raw_value, maximum in zip(raw, upper))
        lower_count = sum(raw_value < minimum for raw_value, minimum in zip(raw, lower))
        exactly_upper_count = sum(value == 0.09 for value in used)
        exactly_lower_count = sum(value == 0.02 for value in used)
        upper_clipped_count += upper_count
        lower_clipped_count += lower_count
        turn_gaps = [raw_value - used_value for raw_value, used_value in zip(raw, used)]
        per_turn.append({
            "path": path_label, "turn": turn, "raw_ra0_std": statistics.pstdev(raw),
            "used_ra_std": statistics.pstdev(used), "raw_used_spearman": _spearman(raw, used),
            "used_ra_unique_count": len(set(used)), "upper_clipped_count": upper_count,
            "upper_clipped_share": upper_count / len(rows), "lower_clipped_count": lower_count,
            "lower_clipped_share": lower_count / len(rows), "share_exactly_0_09": exactly_upper_count / len(rows),
            "share_exactly_0_02": exactly_lower_count / len(rows), "raw_p1": _percentile(raw, 1),
            "raw_p5": _percentile(raw, 5), "raw_p25": _percentile(raw, 25), "raw_p50": _percentile(raw, 50),
            "raw_p75": _percentile(raw, 75), "raw_p95": _percentile(raw, 95), "raw_p99": _percentile(raw, 99),
            "used_p1": _percentile(used, 1), "used_p5": _percentile(used, 5), "used_p25": _percentile(used, 25),
            "used_p50": _percentile(used, 50), "used_p75": _percentile(used, 75), "used_p95": _percentile(used, 95),
            "used_p99": _percentile(used, 99), "gap_p50": _percentile(turn_gaps, 50),
            "gap_min": min(turn_gaps), "gap_mean": statistics.fmean(turn_gaps),
            "gap_p95": _percentile(turn_gaps, 95), "gap_p99": _percentile(turn_gaps, 99), "gap_max": max(turn_gaps),
        })
        for row, raw_value, maximum in zip(rows, raw, upper):
            if raw_value > maximum:
                province_upper[row["province"]] += 1

        matrix = allocation["portfolio_shares_destination_origin"]
        static_raw = _aggregate_destination_to_origin(matrix, raw)
        static_used = _aggregate_destination_to_origin(matrix, used)
        if turn == 25:
            next_payoff: list[float | None] = [None] * len(rows)
            next_validation = "NOT_AVAILABLE_AUTHORIZED_CEILING"
        else:
            next_allocation_path = path_root / "capital_network" / f"allocation_{turn + 1:02d}_turn_{turn + 1:02d}.json"
            if not next_allocation_path.is_file():
                raise ValueError(f"accepted persisted next allocation is missing for {directory} turn {turn:02d}")
            next_allocation = _read_allocation(next_allocation_path, province_order)
            input_hashes[str(next_allocation_path.relative_to(evidence_root))] = _sha256(next_allocation_path)
            if _matrix_max_abs_delta(matrix, next_allocation["portfolio_shares_destination_origin"]) > 1e-12:
                raise ValueError(f"accepted persisted S changes between {directory} turns {turn:02d} and {turn + 1:02d}")
            next_payoff = [float(value) for value in next_allocation["household_portfolio_return_by_origin"]]
            if max(abs(left - right) for left, right in zip(static_used, next_payoff)) > 1e-12:
                raise ValueError(f"accepted persisted next allocation payoff does not match S' * turn {turn:02d} used ra in {directory}")
            next_validation = "VALIDATED_SAME_S_AND_NEXT_ALLOCATION_PAYOFF"
        for origin, row in enumerate(rows):
            static_rows.append({
                "classification": STATIC_LABEL, "path": path_label, "turn": turn,
                "province_index": origin, "province": row["province"], "static_raw_S_transpose_ra0": static_raw[origin],
                "static_clipped_same_turn_S": static_used[origin],
                "persisted_next_allocation_payoff_if_available": next_payoff[origin],
                "next_allocation_payoff_validation_status": next_validation,
                "raw_minus_clipped": static_raw[origin] - static_used[origin],
            })
        raw_all.extend(raw)
        raw_by_turn[turn] = raw
        used_all.extend(used)
        gaps.extend(turn_gaps)
        reconstruction.extend(_float(row, "firm_ra0_reconstruction_residual") for row in rows)
        for key in source_vectors:
            source_vectors[key].extend(_float(row, key) for row in rows)

    if province_order is None:
        raise ValueError("accepted persisted evidence has no province order")
    static_differences = [row["raw_minus_clipped"] for row in static_rows]
    ratio_total = [total / target for total, target in zip(source_vectors["firm_K_total_MU"], source_vectors["Ktarget_2018_MU"])]
    ratio_private = [private / target for private, target in zip(source_vectors["Kt_supply_private_MU"], source_vectors["Ktarget_2018_MU"])]
    ratio_output = [output / total for output, total in zip(source_vectors["Y"], source_vectors["firm_K_total_MU"])]
    implied_delta = [rk + after_tax - raw for rk, after_tax, raw in zip(source_vectors["firm_rk"], source_vectors["firm_after_tax_profit_component_over_K"], raw_all)]
    summary = {
        "path": path_label, "province_turn_rows": len(raw_all), "turns": 25, "provinces": len(province_order),
        "upper_clipped_count": upper_clipped_count, "upper_clipped_share": upper_clipped_count / len(raw_all),
        "lower_clipped_count": lower_clipped_count, "lower_clipped_share": lower_clipped_count / len(raw_all),
        "share_exactly_0_09": sum(value == 0.09 for value in used_all) / len(used_all),
        "share_exactly_0_02": sum(value == 0.02 for value in used_all) / len(used_all),
        "raw_ra0": _distribution(raw_all), "used_ra": _distribution(used_all),
        "clipping_gap_ra0_minus_used": _distribution(gaps),
        "ra0_reconstruction_residual_abs_max": max(abs(value) for value in reconstruction),
        "decomposition_components": {
            "firm_rk": _distribution(source_vectors["firm_rk"]),
            "firm_profit_over_K": _distribution(source_vectors["firm_profit_over_K"]),
            "firm_after_tax_profit_component_over_K": _distribution(source_vectors["firm_after_tax_profit_component_over_K"]),
            "implied_delta_rk_plus_after_tax_minus_ra0": {
                **_distribution(implied_delta), "std": statistics.pstdev(implied_delta),
                "constant_exactly": len(set(implied_delta)) == 1,
            },
        },
        "descriptive_pearson_correlations_not_causal": {
            "firm_rk": _pearson(raw_all, source_vectors["firm_rk"]),
            "firm_profit_over_K": _pearson(raw_all, source_vectors["firm_profit_over_K"]),
            "firm_after_tax_profit_component_over_K": _pearson(raw_all, source_vectors["firm_after_tax_profit_component_over_K"]),
            "firm_K_total_over_Ktarget": _pearson(raw_all, ratio_total),
            "private_K_over_Ktarget": _pearson(raw_all, ratio_private), "Y_over_firm_K_total": _pearson(raw_all, ratio_output),
        },
        "static_raw_payoff_vs_clipped": {"classification": STATIC_LABEL, **_distribution(static_differences)},
    }
    province_rows = [{"path": path_label, "province_index": index, "province": name, "upper_clipped_turns": province_upper[name], "upper_clipped_share_of_25": province_upper[name] / 25.0} for index, name in enumerate(province_order)]
    return summary, per_turn, province_rows, static_rows, input_hashes, raw_by_turn, province_order


def _static_by_province(static_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, int, str], list[float]] = {}
    for row in static_rows:
        key = (row["path"], row["province_index"], row["province"])
        grouped.setdefault(key, []).append(row["raw_minus_clipped"])
    return [
        {
            "classification": STATIC_LABEL, "path": path, "province_index": index, "province": province,
            "difference_min": min(values), "difference_p50": _percentile(values, 50),
            "difference_p95": _percentile(values, 95), "difference_max": max(values),
        }
        for (path, index, province), values in sorted(grouped.items())
    ]


def _cross_path_turn_comparison(a_raw: dict[int, list[float]], b_raw: dict[int, list[float]]) -> list[dict[str, Any]]:
    rows = []
    for turn in range(1, 26):
        if turn not in a_raw or turn not in b_raw or len(a_raw[turn]) != len(b_raw[turn]):
            raise ValueError("accepted persisted evidence lacks same-turn A/B raw return alignment")
        difference = [right - left for left, right in zip(a_raw[turn], b_raw[turn])]
        rows.append({
            "turn": turn, "A_vs_B_raw_ra0_spearman": _spearman(a_raw[turn], b_raw[turn]),
            "B_minus_A_raw_ra0_min": min(difference), "B_minus_A_raw_ra0_mean": statistics.fmean(difference),
            "B_minus_A_raw_ra0_p50": _percentile(difference, 50), "B_minus_A_raw_ra0_p95": _percentile(difference, 95),
            "B_minus_A_raw_ra0_max": max(difference),
        })
    return rows


def run_audit(evidence_root: Path | str, output_root: Path | str) -> Path:
    """Produce a read-only audit receipt, refusing incomplete evidence or overwrite."""
    evidence_root, output_root = Path(evidence_root), Path(output_root)
    if not evidence_root.is_dir():
        raise ValueError("accepted persisted evidence root is missing")
    if output_root.exists():
        raise FileExistsError(f"refusing to overwrite output root: {output_root}")
    summaries, per_turn_rows, province_rows, static_rows, hashes = [], [], [], [], {}
    raw_by_path: dict[str, dict[int, list[float]]] = {}
    province_orders: dict[str, list[str]] = {}
    for directory, label in PATHS.items():
        summary, turns, provinces, static, path_hashes, raw_by_turn, province_order = _path_audit(evidence_root, directory, label)
        summaries.append(summary)
        per_turn_rows.extend(turns)
        province_rows.extend(provinces)
        static_rows.extend(static)
        hashes.update(path_hashes)
        raw_by_path[label] = raw_by_turn
        province_orders[label] = province_order
    if province_orders["A_EQUAL_SHARE"] != province_orders["B_GEOGRAPHIC_BETA2"]:
        raise ValueError("accepted persisted evidence lacks A/B province_order alignment")
    cross_path_rows = _cross_path_turn_comparison(raw_by_path["A_EQUAL_SHARE"], raw_by_path["B_GEOGRAPHIC_BETA2"])
    static_province_rows = _static_by_province(static_rows)
    output_root.mkdir(parents=True)
    _write_csv(output_root / "per_turn_return_clipping.csv", per_turn_rows)
    _write_csv(output_root / "province_upper_clipping_frequency.csv", province_rows)
    _write_csv(output_root / "static_no_feedback_payoff_counterfactual.csv", static_rows)
    _write_csv(output_root / "static_no_feedback_payoff_difference_by_province.csv", static_province_rows)
    _write_csv(output_root / "cross_path_turn_comparison.csv", cross_path_rows)
    receipt = {
        "classification": STATIC_LABEL,
        "read_only_runtime_guard": "standard_library_only__no_project_or_model_runtime_imported",
        "evidence_root": str(evidence_root), "expected_alignment": "25 turns x 31 provinces per path",
        "input_file_sha256": hashes, "paths": summaries,
        "cross_path_raw_ra0": {
            "same_turn_spearman": _distribution([row["A_vs_B_raw_ra0_spearman"] for row in cross_path_rows if row["A_vs_B_raw_ra0_spearman"] is not None]),
            "B_minus_A": _distribution([row["B_minus_A_raw_ra0_p50"] for row in cross_path_rows]),
        },
        "outputs": ["per_turn_return_clipping.csv", "province_upper_clipping_frequency.csv", "static_no_feedback_payoff_counterfactual.csv", "static_no_feedback_payoff_difference_by_province.csv", "cross_path_turn_comparison.csv"],
    }
    (output_root / "reaudit_summary.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return output_root


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence-root", required=True, type=Path)
    parser.add_argument("--output-root", type=Path, default=Path("ch5_mp4c_k1a_payoff_return_reaudit_output"))
    args = parser.parse_args()
    run_audit(args.evidence_root, args.output_root)


if __name__ == "__main__":
    main()
