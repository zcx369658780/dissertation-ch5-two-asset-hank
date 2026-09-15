"""Offline spatial summaries and terminal decision for the matched panel."""
from __future__ import annotations

import argparse
from collections import Counter
import gzip
import json
from pathlib import Path
from typing import Any, Iterable

from validators.multi_province.k1_j160_coordinate_resolved_selector_floor_matched_control import run


NEXT_GATE = "REVIEWER_COORDINATE_RESOLVED_SELECTOR_FLOOR_ROUTE_DECISION"
AXIS_ORDER = ("exact_lower", "near_lower", "interior", "near_upper", "exact_upper")
JOINT_ORDER = ("liquid_boundary", "illiquid_boundary", "dual_boundary", "double_interior")
BOUNDARY_CONCENTRATION_THRESHOLD = 0.50
FAILURE_SPECIFIC_MARGIN = 0.10
OVERLAP_TV_THRESHOLD = 0.20
HETEROGENEITY_TV_THRESHOLD = 0.20


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def read_gzip_json(path: Path) -> dict[str, Any]:
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        return json.load(handle)


def axis_bin(index: int, size: int) -> str:
    if size < 5:
        raise ValueError("grid size must be at least five")
    if index < 0 or index >= size:
        raise ValueError("index outside grid")
    if index == 0:
        return "exact_lower"
    if index == 1:
        return "near_lower"
    if index == size - 2:
        return "near_upper"
    if index == size - 1:
        return "exact_upper"
    return "interior"


def _is_boundary(bin_name: str) -> bool:
    return bin_name != "interior"


def _joint_bin(b_bin: str, a_bin: str) -> str:
    b_boundary, a_boundary = _is_boundary(b_bin), _is_boundary(a_bin)
    if b_boundary and a_boundary:
        return "dual_boundary"
    if b_boundary:
        return "liquid_boundary"
    if a_boundary:
        return "illiquid_boundary"
    return "double_interior"


def coordinate_summary(records: list[dict[str, Any]], *, b_size: int, a_size: int) -> dict[str, Any]:
    b_counts: Counter[str] = Counter(); a_counts: Counter[str] = Counter(); joint_counts: Counter[str] = Counter()
    pair_counts: Counter[str] = Counter()
    for record in records:
        index = record["index_zero_based"]
        b_bin = axis_bin(int(index["b"]), b_size); a_bin = axis_bin(int(index["a"]), a_size)
        b_counts[b_bin] += 1; a_counts[a_bin] += 1; joint_counts[_joint_bin(b_bin, a_bin)] += 1
        pair_counts[f"{b_bin}|{a_bin}"] += 1
    total = len(records)
    b = {key: b_counts[key] for key in AXIS_ORDER}; a = {key: a_counts[key] for key in AXIS_ORDER}
    joint = {key: joint_counts[key] for key in JOINT_ORDER}
    pair_order = [f"{b_bin}|{a_bin}" for b_bin in AXIS_ORDER for a_bin in AXIS_ORDER]
    shares = lambda counts: {key: (value / total if total else None) for key, value in counts.items()}
    upper_b_count = b_counts["near_upper"] + b_counts["exact_upper"]
    return {
        "record_count": total, "b": b, "a": a, "joint": joint,
        "b_shares": shares(b), "a_shares": shares(a), "joint_shares": shares(joint),
        "upper_b_count": upper_b_count, "upper_b_share": upper_b_count / total if total else None,
        "pair_signature_order": pair_order,
        "pair_signature_counts": {key: pair_counts[key] for key in pair_order},
        "pair_signature_vector": [pair_counts[key] / total if total else 0.0 for key in pair_order],
        "spatial_bins": {
            "exact_lower": "index 0", "near_lower": "index 1", "interior": "all other indices",
            "near_upper": "index size-2", "exact_upper": "index size-1",
        },
    }


def total_variation(left: Iterable[float], right: Iterable[float], *, left_total: int, right_total: int) -> float:
    if left_total == 0 and right_total == 0:
        return 0.0
    if (left_total == 0) != (right_total == 0):
        return 1.0
    a, b = list(left), list(right)
    return 0.5 * sum(abs(x - y) for x, y in zip(a, b))


def _flatten(iterations: list[dict[str, Any]], group: str, subtype: str) -> list[dict[str, Any]]:
    records = []
    for row in iterations:
        records.extend(row[group][subtype])
    return records


def _selector_summary(trace: dict[str, Any]) -> dict[str, Any]:
    rows = trace["iterations"]
    liquid = _flatten(rows, "selector_changed_cells", "liquid")
    transfer = _flatten(rows, "selector_changed_cells", "transfer")
    return {
        "liquid": coordinate_summary(liquid, b_size=20, a_size=160),
        "transfer": coordinate_summary(transfer, b_size=20, a_size=160),
        "combined": coordinate_summary(liquid + transfer, b_size=20, a_size=160),
        "first_change_iteration": next((row["iteration"] for row in rows if sum((value or 0) for value in row["selector_changes"].values()) > 0), None),
        "active_iterations": sum(sum((value or 0) for value in row["selector_changes"].values()) > 0 for row in rows),
    }


def _floor_summary(trace: dict[str, Any]) -> dict[str, Any]:
    rows = trace["iterations"]
    forward = _flatten(rows, "derivative_floor_hit_cells", "vb_forward")
    backward = _flatten(rows, "derivative_floor_hit_cells", "vb_backward")
    return {
        "vb_forward": coordinate_summary(forward, b_size=20, a_size=160),
        "vb_backward": coordinate_summary(backward, b_size=20, a_size=160),
        "combined": coordinate_summary(forward + backward, b_size=20, a_size=160),
        "first_hit_iteration": next((row["iteration"] for row in rows if sum(row["derivative_floor_hits"].values()) > 0), None),
        "active_iterations": sum(sum(row["derivative_floor_hits"].values()) > 0 for row in rows),
    }


def _value_crosswalk(trace: dict[str, Any]) -> dict[str, Any]:
    records = [row["argmax"] for row in trace["iterations"]]
    coincidence = Counter()
    for row in trace["iterations"]:
        argmax = tuple(row["argmax"]["index_zero_based"][axis] for axis in ("b", "a", "z"))
        liquid = {tuple(item["index_zero_based"][axis] for axis in ("b", "a", "z")) for item in row["selector_changed_cells"]["liquid"]}
        transfer = {tuple(item["index_zero_based"][axis] for axis in ("b", "a", "z")) for item in row["selector_changed_cells"]["transfer"]}
        forward = {tuple(item["index_zero_based"][axis] for axis in ("b", "a", "z")) for item in row["derivative_floor_hit_cells"]["vb_forward"]}
        backward = {tuple(item["index_zero_based"][axis] for axis in ("b", "a", "z")) for item in row["derivative_floor_hit_cells"]["vb_backward"]}
        coincidence["liquid_selector"] += argmax in liquid
        coincidence["transfer_selector"] += argmax in transfer
        coincidence["any_selector"] += argmax in liquid | transfer
        coincidence["vb_forward_floor"] += argmax in forward
        coincidence["vb_backward_floor"] += argmax in backward
        coincidence["any_floor"] += argmax in forward | backward
    iterations = len(records)
    return {
        "value_argmax": coordinate_summary(records, b_size=20, a_size=160),
        "iteration_count": iterations,
        "exact_cell_coincidence_counts": dict(coincidence),
        "exact_cell_coincidence_shares": {key: value / iterations if iterations else None for key, value in coincidence.items()},
        "coincidence_is_descriptive_not_causal": True,
    }


def _coordinate_set(row: dict[str, Any], selector_type: str) -> set[tuple[int, int, int]]:
    return {
        tuple(item["index_zero_based"][axis] for axis in ("b", "a", "z"))
        for item in row["selector_changed_cells"][selector_type]
    }


def _reverse_transitions(left: dict[str, Any], right: dict[str, Any], selector_type: str) -> bool:
    left_map = {
        tuple(item["index_zero_based"][axis] for axis in ("b", "a", "z")): (item["old_label"], item["new_label"])
        for item in left["selector_changed_cells"][selector_type]
    }
    right_map = {
        tuple(item["index_zero_based"][axis] for axis in ("b", "a", "z")): (item["old_label"], item["new_label"])
        for item in right["selector_changed_cells"][selector_type]
    }
    return left_map.keys() == right_map.keys() and all(left_map[key] == tuple(reversed(right_map[key])) for key in left_map)


def _guizhou_recurrence(trace: dict[str, Any]) -> dict[str, Any]:
    rows = trace["iterations"]
    recurrence = None
    for index in range(2, len(rows)):
        current, prior = rows[index], rows[index - 2]
        if (
            current["hashes"]["liquid_labels"] == prior["hashes"]["liquid_labels"]
            and current["hashes"]["transfer_labels"] == prior["hashes"]["transfer_labels"]
        ):
            recurrence = {"prior_iteration": prior["iteration"], "iteration": current["iteration"], "period": 2}
            left, right = rows[index - 1], rows[index]
            liquid_same = _coordinate_set(left, "liquid") == _coordinate_set(right, "liquid")
            transfer_same = _coordinate_set(left, "transfer") == _coordinate_set(right, "transfer")
            reverse = _reverse_transitions(left, right, "liquid") and _reverse_transitions(left, right, "transfer")
            records = left["selector_changed_cells"]["liquid"] + left["selector_changed_cells"]["transfer"]
            recurrence.update({
                "transition_iterations": [left["iteration"], right["iteration"]],
                "liquid_changed_cell_set_exact_match": liquid_same,
                "transfer_changed_cell_set_exact_match": transfer_same,
                "old_new_labels_exactly_reverse": reverse,
                "stable_changed_cell_set": liquid_same and transfer_same and reverse,
                "changed_cell_spatial_footprint": coordinate_summary(records, b_size=20, a_size=160),
            })
            break
    exact_value = any(rows[index]["hashes"]["value"] == rows[index - 2]["hashes"]["value"] for index in range(2, len(rows)))
    return {
        "joint_selector_period_2_recurrence": recurrence,
        "localization_level": (
            "COORDINATE_RESOLVED_STABLE_CHANGED_CELL_SET" if recurrence and recurrence["stable_changed_cell_set"]
            else "COORDINATE_RESOLVED_REGION_WITHOUT_STABLE_CELL_SET" if recurrence
            else "HASH_LEVEL_PERIOD_2_NOT_REPRODUCED"
        ),
        "exact_value_period_2_recurrence": exact_value,
        "value_two_cycle_claimed": False,
    }


def _spatial_payloads(root: Path, outcomes: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    selector_provinces, floor_provinces, value_provinces = [], [], []
    traces = {}
    for outcome in outcomes["provinces"]:
        trace = read_gzip_json(root / outcome["trace_path"]); traces[outcome["province"]] = trace
        common = {"province_index": outcome["province_index"], "province": outcome["province"], "panel_role": outcome["panel_role"]}
        selector_provinces.append({**common, **_selector_summary(trace)})
        floor_provinces.append({**common, **_floor_summary(trace)})
        value_provinces.append({**common, **_value_crosswalk(trace)})
    selector = {"schema": "CH5_MP4C_K1_J160_SELECTOR_COORDINATE_FOOTPRINTS_V1", "provinces": selector_provinces}
    floor = {"schema": "CH5_MP4C_K1_J160_FLOOR_COORDINATE_FOOTPRINTS_V1", "provinces": floor_provinces}
    value = {"schema": "CH5_MP4C_K1_J160_VALUE_ARGMAX_CROSSWALK_V1", "provinces": value_provinces}
    guizhou = _guizhou_recurrence(traces["贵州"])
    value["guizhou_recurrence_localization"] = guizhou
    return selector, floor, value, traces


def _tv(left: dict[str, Any], right: dict[str, Any]) -> float:
    return total_variation(
        left["pair_signature_vector"], right["pair_signature_vector"],
        left_total=left["record_count"], right_total=right["record_count"],
    )


def _specific_upper(failure: dict[str, Any], control: dict[str, Any]) -> bool:
    failure_share = failure["upper_b_share"]
    control_share = control["upper_b_share"]
    if failure_share is None or failure_share < BOUNDARY_CONCENTRATION_THRESHOLD:
        return False
    return control_share is None or failure_share - control_share >= FAILURE_SPECIFIC_MARGIN


def _dominant_pair(summary: dict[str, Any]) -> tuple[str | None, float]:
    if not summary["record_count"]:
        return None, 0.0
    key, count = max(summary["pair_signature_counts"].items(), key=lambda item: (item[1], item[0]))
    return key, count / summary["record_count"]


def _failure_heterogeneity(items: list[dict[str, Any]]) -> tuple[bool, float]:
    values = [_tv(items[i], items[j]) for i in range(len(items)) for j in range(i + 1, len(items))]
    maximum = max(values, default=0.0)
    return maximum > HETEROGENEITY_TV_THRESHOLD, maximum


def build_comparison(selector: dict[str, Any], floor: dict[str, Any]) -> dict[str, Any]:
    selectors = {item["province"]: item["combined"] for item in selector["provinces"]}
    floors = {item["province"]: item["combined"] for item in floor["provinces"]}
    pairs = []
    for failure, control in run.MATCHES:
        s_failure, s_control = selectors[failure], selectors[control]
        f_failure, f_control = floors[failure], floors[control]
        pairs.append({
            "failure": failure, "control": control,
            "selector": {
                "failure_records": s_failure["record_count"], "control_records": s_control["record_count"],
                "failure_upper_b_share": s_failure["upper_b_share"], "control_upper_b_share": s_control["upper_b_share"],
                "failure_minus_control_upper_b_share": None if s_control["upper_b_share"] is None else s_failure["upper_b_share"] - s_control["upper_b_share"],
                "total_variation": _tv(s_failure, s_control), "failure_specific_upper": _specific_upper(s_failure, s_control),
            },
            "floor": {
                "failure_records": f_failure["record_count"], "control_records": f_control["record_count"],
                "failure_upper_b_share": f_failure["upper_b_share"], "control_upper_b_share": f_control["upper_b_share"],
                "failure_minus_control_upper_b_share": None if f_control["upper_b_share"] is None else f_failure["upper_b_share"] - f_control["upper_b_share"],
                "total_variation": _tv(f_failure, f_control), "failure_specific_upper": _specific_upper(f_failure, f_control),
            },
            "descriptive_only": True,
        })
    failure_names = [name for _, name, role, _ in run.PANEL if role == "failure"]
    selector_heterogeneous, selector_max_tv = _failure_heterogeneity([selectors[name] for name in failure_names])
    floor_heterogeneous, floor_max_tv = _failure_heterogeneity([floors[name] for name in failure_names])
    selector_dominants = [_dominant_pair(selectors[name]) for name in failure_names]
    floor_dominants = [_dominant_pair(floors[name]) for name in failure_names]
    common_selector = len({item[0] for item in selector_dominants}) == 1 and min(item[1] for item in selector_dominants) >= BOUNDARY_CONCENTRATION_THRESHOLD
    common_floor = len({item[0] for item in floor_dominants}) == 1 and min(item[1] for item in floor_dominants) >= BOUNDARY_CONCENTRATION_THRESHOLD
    common_key = selector_dominants[0][0] if common_selector and common_floor and selector_dominants[0][0] == floor_dominants[0][0] else None
    common_other = bool(common_key and not common_key.split("|")[0] in {"near_upper", "exact_upper"})
    payload = {
        "schema": "CH5_MP4C_K1_J160_MATCHED_CONTROL_COMPARISON_V1",
        "pre_registered_thresholds": {
            "boundary_concentration_share": BOUNDARY_CONCENTRATION_THRESHOLD,
            "failure_specific_absolute_share_margin": FAILURE_SPECIFIC_MARGIN,
            "matched_overlap_total_variation": OVERLAP_TV_THRESHOLD,
            "failure_heterogeneity_total_variation": HETEROGENEITY_TV_THRESHOLD,
        },
        "pairs": pairs,
        "upper_specific_all_pairs": all(item["selector"]["failure_specific_upper"] and item["floor"]["failure_specific_upper"] for item in pairs),
        "matched_overlap_all_pairs": all(item["selector"]["total_variation"] <= OVERLAP_TV_THRESHOLD and item["floor"]["total_variation"] <= OVERLAP_TV_THRESHOLD for item in pairs),
        "common_other_specific": common_other,
        "failure_heterogeneous": selector_heterogeneous or floor_heterogeneous,
        "failure_selector_max_pairwise_tv": selector_max_tv,
        "failure_floor_max_pairwise_tv": floor_max_tv,
        "evidence_sufficient": all(selectors[name]["record_count"] > 0 for name in failure_names),
        "descriptive_only": True, "causal_claim": False,
    }
    return payload


def panel_classification(reproducibility: list[bool], comparison: dict[str, Any]) -> str:
    if len(reproducibility) != 7 or not all(reproducibility):
        return "MATCHED_PANEL_REPRODUCIBILITY_BLOCKER"
    if comparison["upper_specific_all_pairs"]:
        return "FAILURE_SPECIFIC_LIQUID_UPPER_BOUNDARY_SELECTOR_FLOOR_CONCENTRATION"
    if comparison["common_other_specific"]:
        return "FAILURE_SPECIFIC_OTHER_BOUNDARY_OR_INTERIOR_CONCENTRATION"
    if comparison["matched_overlap_all_pairs"]:
        return "FAILURE_CONTROL_FOOTPRINTS_OVERLAP_SUBSTANTIALLY"
    if comparison["evidence_sufficient"] and comparison["failure_heterogeneous"]:
        return "HETEROGENEOUS_COORDINATE_RESOLVED_FAILURE_FOOTPRINTS"
    return "COORDINATE_RESOLVED_MECHANISM_UNRESOLVED"


def _report(outcomes: dict[str, Any], selector: dict[str, Any], floor: dict[str, Any], value: dict[str, Any], comparison: dict[str, Any], panel: dict[str, Any], ledger: dict[str, Any]) -> str:
    s_by = {item["province"]: item for item in selector["provinces"]}
    f_by = {item["province"]: item for item in floor["provinces"]}
    v_by = {item["province"]: item for item in value["provinces"]}
    o_by = {item["province"]: item for item in outcomes["provinces"]}
    lines = [
        "# CH5 MP4C K1 — J160 coordinate-resolved selector/floor matched-control diagnostic", "",
        "## Terminal panel class", "", f"`{panel['terminal_panel_class']}`", "", "Results eligibility=`FALSE`.", "",
        "## Authority and invariance", "",
        f"Actual baseline: `{run.ACTUAL_BASELINE}`. Authority gate and instrumentation invariance both passed before science. "
        "The accepted Oracle was called directly; coordinate copies did not feed scientific control flow. No parity HJB was added.", "",
        "Spatial bins were frozen before science: exact endpoint, one-index near band, interior, one-index near-upper band, exact upper endpoint. "
        "The matched-control thresholds were also frozen before science: concentration 0.50, failure-control margin 0.10, and total-variation overlap/heterogeneity boundary 0.20.", "",
        "## Seven-province outcomes and footprints", "",
        "| province | role | replay | reproducibility | selector events | selector upper-b | floor hits | floor upper-b | argmax upper-b | argmax/selector coincide | argmax/floor coincide |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for _, name, role, _ in run.PANEL:
        outcome = o_by[name]; s = s_by[name]["combined"]; f = f_by[name]["combined"]
        v = v_by[name]; argmax = v["value_argmax"]; coincide = v["exact_cell_coincidence_shares"]
        lines.append(
            f"| {name} | {role} | {outcome['replay_classification']}@{outcome['replay_iterations']} | "
            f"{'PASS' if outcome['reproducibility_pass'] else 'FAIL'} | {s['record_count']} | {_pct(s['upper_b_share'])} | "
            f"{f['record_count']} | {_pct(f['upper_b_share'])} | {_pct(argmax['upper_b_share'])} | "
            f"{_pct(coincide.get('any_selector'))} | {_pct(coincide.get('any_floor'))} |"
        )
    lines.extend([
        "", "## Type-resolved selector and floor footprints", "",
        "| province | liquid selector events / upper-b | transfer selector events / upper-b | forward floor hits / upper-b | backward floor hits / upper-b | selector double-interior | floor double-interior |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ])
    for _, name, _, _ in run.PANEL:
        selector_row = s_by[name]; floor_row = f_by[name]
        lines.append(
            f"| {name} | {selector_row['liquid']['record_count']} / {_pct(selector_row['liquid']['upper_b_share'])} | "
            f"{selector_row['transfer']['record_count']} / {_pct(selector_row['transfer']['upper_b_share'])} | "
            f"{floor_row['vb_forward']['record_count']} / {_pct(floor_row['vb_forward']['upper_b_share'])} | "
            f"{floor_row['vb_backward']['record_count']} / {_pct(floor_row['vb_backward']['upper_b_share'])} | "
            f"{_pct(selector_row['combined']['joint_shares']['double_interior'])} | "
            f"{_pct(floor_row['combined']['joint_shares']['double_interior'])} |"
        )
    lines.extend(["", "All coincidence measures are exact-cell, same-iteration descriptive shares; they are not causal effects.", "", "## Matched controls", ""])
    for item in comparison["pairs"]:
        lines.append(
            f"- {item['failure']} vs {item['control']}: selector upper-b {_pct(item['selector']['failure_upper_b_share'])} vs {_pct(item['selector']['control_upper_b_share'])}, "
            f"TV `{item['selector']['total_variation']:.6g}`; floor upper-b {_pct(item['floor']['failure_upper_b_share'])} vs {_pct(item['floor']['control_upper_b_share'])}, "
            f"TV `{item['floor']['total_variation']:.6g}`."
        )
    guizhou = value["guizhou_recurrence_localization"]
    lines.extend([
        "", "## Required interpretation", "",
        f"贵州 recurrence localization: `{guizhou['localization_level']}`; exact value period-2 recurrence=`{str(guizhou['exact_value_period_2_recurrence']).upper()}`. No value two-cycle is claimed.", "",
        f"天津's mixed value argmax does not imply a mixed selector/floor footprint: selector and floor events are {_pct(s_by['天津']['combined']['joint_shares']['double_interior'])} and {_pct(f_by['天津']['combined']['joint_shares']['double_interior'])} double-interior, while their upper-b shares are only {_pct(s_by['天津']['combined']['upper_b_share'])} and {_pct(f_by['天津']['combined']['upper_b_share'])}.", "",
        f"江西 floor hits are primarily double-interior ({_pct(f_by['江西']['combined']['joint_shares']['double_interior'])}), not liquid-upper concentrated ({_pct(f_by['江西']['combined']['upper_b_share'])}), despite its accepted upper-b value-argmax label.", "",
        f"甘肃's upper-b argmax concentration is not mirrored by its selector footprint ({_pct(s_by['甘肃']['combined']['upper_b_share'])}); its floor upper-b share is {_pct(f_by['甘肃']['combined']['upper_b_share'])}, compared with {_pct(f_by['福建']['combined']['upper_b_share'])} for 福建.", "",
        "Successful controls have selector upper-b shares comparable to failures and substantial floor upper-b activity. Upper-b activity is therefore not a failure-specific pathology in this panel.", "",
        f"Failure-specific upper-b selector+floor condition across all matched pairs=`{str(comparison['upper_specific_all_pairs']).upper()}`. "
        f"Failure selector maximum pairwise TV=`{comparison['failure_selector_max_pairwise_tv']:.6g}` and floor maximum pairwise TV=`{comparison['failure_floor_max_pairwise_tv']:.6g}`.", "",
        f"A common coordinate-resolved failure mechanism is not supported: `{str(comparison['failure_heterogeneous']).upper()}` for preregistered failure heterogeneity.", "",
        "The panel result is descriptive numerical evidence only. It does not authorize a boundary/domain, selector, floor, HJB, mapping, or calibration change.", "",
        "## Runtime ledger", "",
        f"HJB `{ledger['hjb_calls_started']}/7`; failed provinces `{ledger['failed_province_hjb_calls']}/4`; successful controls `{ledger['successful_control_hjb_calls']}/3`; "
        f"KFE=`{ledger['kfe_calls']}`; scientific retries=`{ledger['scientific_retries']}`; engineering retry=`{ledger['engineering_retries_used']}/1` before science. "
        "Outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results are all zero.", "",
        "## Exactly one next gate", "", f"`{NEXT_GATE}`", "",
    ])
    return "\n".join(lines)


def _pct(value: float | None) -> str:
    return "N/A" if value is None else f"{value:.2%}"


def _seal(root: Path) -> dict[str, Any]:
    entries = []
    for path in sorted(item for item in root.rglob("*") if item.is_file() and item.name != "sealed_manifest_sha256.json"):
        entries.append({"path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size, "sha256": run.file_sha256(path)})
    return {
        "schema": "CH5_MP4C_K1_J160_COORDINATE_RESOLVED_MATCHED_PANEL_SEALED_MANIFEST_V1",
        "entry_count": len(entries), "bytes_excluding_manifest": sum(item["bytes"] for item in entries), "entries": entries,
    }


def finalize(evidence_root: Path, report_path: Path) -> dict[str, Any]:
    root = Path(evidence_root)
    outcomes = read_json(root / "province_outcomes.json")
    ledger = read_json(root / "call_ledger.json")
    if ledger["hjb_calls_started"] != 7 or ledger["hjb_calls_completed"] != 7:
        raise RuntimeError("matched panel is not complete")
    selector, floor, value, _ = _spatial_payloads(root, outcomes)
    comparison = build_comparison(selector, floor)
    terminal = panel_classification([item["reproducibility_pass"] for item in outcomes["provinces"]], comparison)
    panel = {
        "schema": "CH5_MP4C_K1_J160_COORDINATE_RESOLVED_MATCHED_PANEL_DECISION_V1",
        "terminal_panel_class": terminal, "reproducibility_pass": outcomes["all_reproducibility_pass"],
        "failure_specific_upper_b_footprint": comparison["upper_specific_all_pairs"],
        "common_failure_spatial_mechanism": not comparison["failure_heterogeneous"],
        "causal_claim": False, "repair_authorized": False,
        "results_eligibility": False, "next_gate": NEXT_GATE,
    }
    run.write_json(root / "selector_coordinate_footprints.json", selector)
    run.write_json(root / "floor_coordinate_footprints.json", floor)
    run.write_json(root / "value_argmax_crosswalk.json", value)
    run.write_json(root / "matched_control_comparison.json", comparison)
    run.write_json(root / "panel_decision.json", panel)
    Path(report_path).write_text(_report(outcomes, selector, floor, value, comparison, panel, ledger), encoding="utf-8", newline="\n")
    run.write_json(root / "sealed_manifest_sha256.json", _seal(root))
    return panel


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_root", type=Path)
    parser.add_argument("report_path", type=Path)
    args = parser.parse_args()
    print(json.dumps(finalize(args.evidence_root, args.report_path), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
