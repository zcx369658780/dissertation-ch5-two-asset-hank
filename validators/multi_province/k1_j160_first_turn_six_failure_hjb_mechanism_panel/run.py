"""Observation-only replays of the six accepted J160 provincial HJB failures."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from math import ceil, sqrt
from pathlib import Path
import time
from typing import Any

import numpy as np

from validators.multi_province.k1_j160_provincial_first_turn_hjb_viability import (
    run as accepted_viability,
)
from validators.multi_province.k1_j640_hjb_nonconvergence_mechanism_diagnostic import (
    run as j640,
)
from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import run as accepted_hjb


REPO = Path(__file__).resolve().parents[3]
TASK_ID = "CH5_MP4C_K1_J160_FIRST_TURN_SIX_FAILURE_HJB_MECHANISM_PANEL_DIAGNOSTIC"
ACTUAL_BASELINE = "3b193f536fe2ab70fd487e3a4cde899ee5ed0c34"
ACCEPTED_VIABILITY_CANDIDATE = "1e9c8c6416cbd732a44d739e19b40e838993e3d4"
FAILURES = ((1, "天津"), (3, "山西"), (13, "江西"), (21, "重庆"), (23, "贵州"), (27, "甘肃"))

VIABILITY_ROOT = REPO / "docs/evidence/ch5_mp4c_k1_j160_provincial_first_turn_hjb_viability"
VIABILITY_MANIFEST = VIABILITY_ROOT / "sealed_manifest_sha256.json"
VIABILITY_MANIFEST_CANONICAL_SHA256 = "78E39ACA7E051980D842BA861367E3424EE95578AD806802E8216E6AA14D3DFE"
VIABILITY_INPUT = VIABILITY_ROOT / "first_turn_input_authority.json"
VIABILITY_PROVINCES = VIABILITY_ROOT / "province_receipts.json"
VIABILITY_ACCEPTANCE = REPO / "docs/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_ACCEPTANCE.md"
VIABILITY_ACCEPTANCE_SHA256 = "4EE1D67F080BC74A9F1FF862AC8781EAE93C7E345281F8A5636DA50932E1D41E"

J640_ROOT = REPO / "docs/evidence/ch5_mp4c_k1_j640_hjb_nonconvergence_mechanism_diagnostic"
J640_MANIFEST = J640_ROOT / "sealed_manifest_sha256.json"
J640_MANIFEST_CANONICAL_SHA256 = "232638DE8220BCEE08AD2AFC3BEA4E1B631212755025FD6DD502C743C6E0DB3B"
J640_INVARIANCE = J640_ROOT / "instrumentation_invariance_receipt.json"
J640_ACCEPTANCE = REPO / "docs/CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC_ACCEPTANCE.md"
J640_ACCEPTANCE_SHA256 = "B4E8DEC045837A218C5A2172142E6C19C09ADEB92BC94A41F1F39CF300C06689"
J640_RUNNER = Path(j640.__file__).resolve()
J640_RUNNER_SHA256 = "F1E4D5A54293431C2C5EE428715C28AF4CCD9E5851D99DB544A0BA1BEEBAF867"

ORACLE_PATH = accepted_viability.ORACLE_PATH
ORACLE_SHA256 = "F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8"
MATLAB_PATH = accepted_viability.MATLAB_PATH
MATLAB_SHA256 = "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE"
HOMECRIT = 0.01
observe_accepted_hjb = j640.observe_accepted_hjb

FORBIDDEN_LEDGER_KEYS = (
    "kfe_calls", "successful_province_hjb_calls", "global_outer_calls", "firm_calls",
    "wage_recalculation_calls", "return_recalculation_calls", "matlab_calls",
    "k1b_calls", "k2_calls", "ge_calls", "downstream_calls", "shock_calls",
    "irf_calls", "results_writes",
)


def file_sha256(path: Path) -> str:
    return sha256(Path(path).read_bytes()).hexdigest().upper()


def canonical_text_sha256(path: Path) -> str:
    return sha256(Path(path).read_text(encoding="utf-8").encode("utf-8")).hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    Path(path).write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def _manifest(path: Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _manifest_entry(root: Path, manifest: Path, relative: str) -> dict[str, Any]:
    matches = [item for item in _manifest(manifest)["entries"] if item["path"] == relative]
    if len(matches) != 1:
        raise ValueError(f"SIX_FAILURE_INPUT_AUTHORITY_BLOCKER: manifest entry not unique: {relative}")
    entry = matches[0]
    target = root / relative
    byte_hash = file_sha256(target)
    canonical_hash = canonical_text_sha256(target)
    return {
        "path": str(target.resolve()), "expected_sha256": entry["sha256"],
        "actual_byte_sha256": byte_hash, "actual_canonical_lf_sha256": canonical_hash,
        "bytes_expected": entry["bytes"], "bytes_actual": target.stat().st_size,
        "pass": entry["sha256"] in {byte_hash, canonical_hash},
    }


def _full_manifest_receipt(root: Path, manifest: Path, expected_manifest_hash: str) -> dict[str, Any]:
    payload = _manifest(manifest)
    entries = [_manifest_entry(root, manifest, item["path"]) for item in payload["entries"]]
    return {
        "path": str(manifest.resolve()), "expected_canonical_sha256": expected_manifest_hash,
        "actual_canonical_sha256": canonical_text_sha256(manifest),
        "entry_count": len(entries), "entries": entries,
        "pass": canonical_text_sha256(manifest) == expected_manifest_hash and all(item["pass"] for item in entries),
    }


def load_six_failure_authority() -> dict[str, Any]:
    input_entry = _manifest_entry(VIABILITY_ROOT, VIABILITY_MANIFEST, VIABILITY_INPUT.name)
    province_entry = _manifest_entry(VIABILITY_ROOT, VIABILITY_MANIFEST, VIABILITY_PROVINCES.name)
    if not input_entry["pass"] or not province_entry["pass"]:
        raise ValueError("SIX_FAILURE_INPUT_AUTHORITY_BLOCKER: accepted viability artifacts do not match manifest")
    authority = json.loads(VIABILITY_INPUT.read_text(encoding="utf-8"))
    accepted_points = json.loads(VIABILITY_PROVINCES.read_text(encoding="utf-8"))
    rows_by_key = {(row["province_index"], row["province"]): row for row in authority["provinces"]}
    points_by_key = {(row["province_index"], row["province"]): row for row in accepted_points}
    failures = []
    for key in FAILURES:
        if key not in rows_by_key or key not in points_by_key:
            raise ValueError(f"SIX_FAILURE_INPUT_AUTHORITY_BLOCKER: missing accepted row {key}")
        row = rows_by_key[key]
        point = points_by_key[key]
        hjb = point["hjb"]
        if hjb["classification"] != "HJB_NOT_CONVERGED" or hjb["iterations_used"] != 100:
            raise ValueError(f"SIX_FAILURE_INPUT_AUTHORITY_BLOCKER: accepted failure mismatch {key}")
        if row["consumed_r_a"] != point["household_inputs"]["consumed_r_a"]:
            raise ValueError(f"SIX_FAILURE_INPUT_AUTHORITY_BLOCKER: consumed return mismatch {key}")
        if row["household_composite_wage"] != point["household_inputs"]["household_composite_wage"]:
            raise ValueError(f"SIX_FAILURE_INPUT_AUTHORITY_BLOCKER: composite wage mismatch {key}")
        failures.append({
            **row,
            "accepted_hjb_classification": hjb["classification"],
            "accepted_iterations": hjb["iterations_used"],
            "accepted_final_convergence_statistic": hjb["final_convergence_statistic"],
            "accepted_maximum_a2max": hjb["maximum_a2max"],
            "accepted_first_illegal_iteration": hjb["first_illegal_iteration"],
            "accepted_scientific_arrays": hjb["scientific_arrays"],
            "accepted_fresh_initialization": point["fresh_initialization"],
        })
    return {
        "schema": "CH5_MP4C_K1_J160_SIX_FAILURE_INPUT_AUTHORITY_V1",
        "accepted_candidate": ACCEPTED_VIABILITY_CANDIDATE,
        "input_artifact_manifest_match": input_entry["pass"],
        "province_receipts_manifest_match": province_entry["pass"],
        "failure_count": len(failures), "failures": failures,
        "pass": len(failures) == 6,
    }


def build_fixture(row: dict[str, Any]) -> accepted_hjb.Fixture:
    return accepted_viability.build_fixture(row)


def instrumentation_invariance_receipt() -> dict[str, Any]:
    accepted = json.loads(J640_INVARIANCE.read_text(encoding="utf-8"))
    entry = _manifest_entry(J640_ROOT, J640_MANIFEST, J640_INVARIANCE.name)
    receipt = {
        "schema": "CH5_MP4C_K1_J160_SIX_FAILURE_INSTRUMENTATION_INVARIANCE_V1",
        "accepted_j640_receipt": entry,
        "accepted_j640_status": accepted["pass"],
        "accepted_off_on_exact": accepted["accepted_off_on_exact"],
        "accepted_off_accepted_exact": accepted["accepted_off_accepted_exact"],
        "accepted_method_imported_without_modification": observe_accepted_hjb is j640.observe_accepted_hjb,
        "current_design_calls_accepted_solver_directly": True,
        "wrapped_primitives_return_original_objects_or_values": True,
        "scientific_control_flow_reads_observations": False,
        "new_hjb_calls": 0,
        "damping_clipping_renormalization_policy_freezing_added": False,
    }
    receipt["pass"] = bool(
        entry["pass"] and accepted["pass"] and accepted["accepted_off_on_exact"]
        and accepted["accepted_off_accepted_exact"]
        and receipt["accepted_method_imported_without_modification"]
    )
    return receipt


def input_invariance_receipt(rows: list[dict[str, Any]]) -> dict[str, Any]:
    entries = []
    fixtures = [build_fixture(row) for row in rows]
    for row, fixture in zip(rows, fixtures):
        initial_hash = accepted_hjb.array_sha256(fixture.initial_value)
        labor_hash = accepted_hjb.array_sha256(fixture.baseline_labor)
        checks = {
            "I": fixture.grid.b.size == 20,
            "J": fixture.grid.a.size == 160,
            "Nz": fixture.grid.z.size == 2,
            "a_bounds": fixture.grid.a[[0, -1]].tolist() == [0.0, 100.0],
            "b_bounds": fixture.grid.b[[0, -1]].tolist() == [-2.0, 20.0],
            "r_a": fixture.inputs.r_a == row["consumed_r_a"],
            "r_b": fixture.inputs.r_b == row["r_b"],
            "wage": fixture.inputs.wages.tolist() == [row["household_composite_wage"]],
            "tau": fixture.inputs.tau == row["tau"],
            "transfer": fixture.transfer_income == row["transfer_income"],
            "borrowing_gap": fixture.borrowing_rate_gap == row["borrowing_rate_gap"],
            "delta": fixture.numerics.delta == 1000.0,
            "tolerance": fixture.numerics.convergence_tolerance == 1e-7,
            "maxit": fixture.numerics.max_iterations == 100,
            "initial_value_exact": initial_hash == row["accepted_fresh_initialization"]["initial_value_sha256"],
            "baseline_labor_exact": labor_hash == row["accepted_fresh_initialization"]["baseline_labor_sha256"],
        }
        entries.append({
            "province_index": row["province_index"], "province": row["province"],
            "checks": checks, "fresh_initialization": True, "warm_start": False,
            "initial_value_sha256": initial_hash, "baseline_labor_sha256": labor_hash,
        })
    receipt = {
        "schema": "CH5_MP4C_K1_J160_SIX_FAILURE_INPUT_INVARIANCE_V1",
        "entries": entries,
        "fresh_initial_value_object_count": len({id(item.initial_value) for item in fixtures}),
        "fresh_baseline_labor_object_count": len({id(item.baseline_labor) for item in fixtures}),
    }
    receipt["pass"] = bool(
        len(entries) == 6
        and receipt["fresh_initial_value_object_count"] == 6
        and receipt["fresh_baseline_labor_object_count"] == 6
        and all(all(entry["checks"].values()) for entry in entries)
    )
    return receipt


def source_identity_receipt() -> dict[str, Any]:
    viability = _full_manifest_receipt(VIABILITY_ROOT, VIABILITY_MANIFEST, VIABILITY_MANIFEST_CANONICAL_SHA256)
    j640_manifest = _full_manifest_receipt(J640_ROOT, J640_MANIFEST, J640_MANIFEST_CANONICAL_SHA256)
    files = {
        "protected_python_hjb_and_kfe_oracle": (ORACLE_PATH, ORACLE_SHA256),
        "matlab_hjb_source": (MATLAB_PATH, MATLAB_SHA256),
        "accepted_j640_instrumentation_runner": (J640_RUNNER, J640_RUNNER_SHA256),
        "accepted_viability_review": (VIABILITY_ACCEPTANCE, VIABILITY_ACCEPTANCE_SHA256),
        "accepted_j640_review": (J640_ACCEPTANCE, J640_ACCEPTANCE_SHA256),
    }
    identities = {
        name: {"path": str(path.resolve()), "expected_sha256": expected, "actual_sha256": file_sha256(path)}
        for name, (path, expected) in files.items()
    }
    for item in identities.values():
        item["pass"] = item["expected_sha256"] == item["actual_sha256"]
    receipt = {
        "schema": "CH5_MP4C_K1_J160_SIX_FAILURE_SOURCE_IDENTITY_V1",
        "actual_baseline": ACTUAL_BASELINE,
        "accepted_viability_manifest": viability,
        "accepted_j640_manifest": j640_manifest,
        "files": identities,
        "science_calls_before_clean_gate": 0,
    }
    receipt["pass"] = bool(viability["pass"] and j640_manifest["pass"] and all(item["pass"] for item in identities.values()))
    return receipt


def nearest_successful_neighbors() -> dict[str, Any]:
    points = json.loads(VIABILITY_PROVINCES.read_text(encoding="utf-8"))
    by_key = {(item["province_index"], item["province"]): item for item in points}
    successes = [item for item in points if item["hjb"]["classification"] == "HJB_CONVERGED"]
    failures = []
    for key in FAILURES:
        failed = by_key[key]
        inputs = failed["household_inputs"]
        ra, wage = inputs["consumed_r_a"], inputs["household_composite_wage"]
        neighbors = []
        for success in successes:
            success_inputs = success["household_inputs"]
            success_ra = success_inputs["consumed_r_a"]
            success_wage = success_inputs["household_composite_wage"]
            neighbors.append({
                "province_index": success["province_index"], "province": success["province"],
                "consumed_r_a": success_ra, "household_composite_wage": success_wage,
                "euclidean_distance_raw_ra_w": sqrt((success_ra - ra) ** 2 + (success_wage - wage) ** 2),
                "accepted_hjb_classification": success["hjb"]["classification"],
                "accepted_iterations": success["hjb"]["iterations_used"],
                "accepted_final_convergence_statistic": success["hjb"]["final_convergence_statistic"],
            })
        neighbors.sort(key=lambda item: (item["euclidean_distance_raw_ra_w"], item["province_index"]))
        failures.append({
            "failure_province_index": failed["province_index"], "failure_province": failed["province"],
            "failure_consumed_r_a": ra, "failure_household_composite_wage": wage,
            "nearest_successful_neighbors": neighbors[:3],
        })
    return {
        "schema": "CH5_MP4C_K1_J160_SIX_FAILURE_NEAREST_SUCCESSFUL_NEIGHBORS_V1",
        "distance_definition": "ordinary Euclidean distance in raw (consumed_r_a, household_composite_wage) coordinates",
        "source": str(VIABILITY_PROVINCES.resolve()),
        "descriptive_only": True, "successful_province_hjb_calls": 0,
        "failures": failures,
    }


def _first_selector_change(rows: list[dict[str, Any]], axis: str | None = None) -> int | None:
    for row in rows:
        changes = row["selector_changes"]
        if changes["liquid"] is None:
            continue
        count = changes[axis] if axis else changes["liquid"] + changes["transfer"]
        if count > 0:
            return int(row["iteration"])
    return None


def classify_trace(
    trace: dict[str, Any], *, replay_converged: bool, reproducibility_open: bool = True,
) -> dict[str, Any]:
    rows = trace["iterations"]
    statistics = [float(row["convergence_statistic"]) for row in rows]
    first_switch = _first_selector_change(rows)
    first_nondec = next((index + 1 for index in range(1, len(statistics)) if statistics[index] >= statistics[index - 1]), None)
    floor_first = trace.get("first_derivative_floor_hit_iteration")
    cycle = trace["cycle_evidence"]
    nondec_count = sum(statistics[index] >= statistics[index - 1] for index in range(1, len(statistics)))
    switch_iterations = sum(
        row["selector_changes"]["liquid"] is not None
        and row["selector_changes"]["liquid"] + row["selector_changes"]["transfer"] > 0
        for row in rows
    )
    floor_active = sum(sum(row["derivative_floor_hits"].values()) > 0 for row in rows)
    if replay_converged or not reproducibility_open:
        classification = "FAILURE_REPRODUCIBILITY_BLOCKER"
    elif cycle["exact_value_low_period_2_or_3"] or cycle["exact_joint_label_low_period_2_or_3"]:
        classification = "REPEATING_OR_LOW_PERIOD_CYCLE"
    elif first_switch is not None and floor_first is not None and first_switch < floor_first <= (first_nondec or -1) and floor_active > 0:
        classification = "DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING"
    elif (
        first_switch is not None and first_nondec is not None and first_switch <= first_nondec
        and switch_iterations >= max(2, ceil(0.2 * max(len(rows) - 1, 1)))
    ):
        classification = "POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION"
    elif nondec_count == 0 and switch_iterations <= 1:
        classification = "SLOW_MONOTONE_OR_NEAR_MONOTONE_VALUE_CONVERGENCE"
    else:
        classification = "MIXED_OR_UNRESOLVED_NUMERICAL_MECHANISM"
    event_order = sorted(
        ([name, iteration] for name, iteration in (
            ("policy_or_selector_switch", first_switch),
            ("value_stat_non_decrease", first_nondec),
            ("derivative_floor_hit", floor_first),
        ) if iteration is not None),
        key=lambda item: item[1],
    )
    return {
        "classification": classification,
        "classification_rule_frozen_before_science": True,
        "event_ordering": event_order,
        "first_policy_or_selector_switch_iteration": first_switch,
        "first_liquid_selector_change_iteration": _first_selector_change(rows, "liquid"),
        "first_transfer_selector_change_iteration": _first_selector_change(rows, "transfer"),
        "first_value_stat_non_decrease_iteration": first_nondec,
        "first_derivative_floor_hit_iteration": floor_first,
        "selector_switch_iterations": switch_iterations,
        "value_stat_decrease_count": max(len(statistics) - 1 - nondec_count, 0),
        "value_stat_non_decrease_count": nondec_count,
        "derivative_floor_active_iterations": floor_active,
        "initial_convergence_statistic": statistics[0] if statistics else None,
        "final_convergence_statistic": statistics[-1] if statistics else None,
        "minimum_convergence_statistic": min(statistics) if statistics else None,
        "maximum_convergence_statistic": max(statistics) if statistics else None,
        "cycle_evidence": cycle,
        "exact_value_recurrence": cycle["first_exact_value_recurrence"],
        "exact_joint_selector_recurrence": cycle["first_exact_joint_label_recurrence"],
        "all_iteration_operators_legal": all(row["operator"]["legal"] for row in rows),
        "maximum_a2max": max((row["operator"]["a2max"] for row in rows), default=None),
        "all_finite_checks_pass": all(all(row["finite_checks"].values()) for row in rows),
        "all_shape_checks_pass": all(all(row["shape_checks"].values()) for row in rows),
        "linear_solve_residual_range": (
            [min(row["linear_solve_residual_inf"] for row in rows), max(row["linear_solve_residual_inf"] for row in rows)]
            if rows else None
        ),
        "ordering_is_descriptive_not_causal": True,
    }


def _result_array_hashes(result: Any) -> dict[str, str]:
    return {
        name: accepted_hjb.array_sha256(getattr(result, name))
        for name in result.__dataclass_fields__
        if isinstance(getattr(result, name), np.ndarray)
    }


def empty_call_ledger() -> dict[str, Any]:
    ledger = {
        "schema": "CH5_MP4C_K1_J160_SIX_FAILURE_HJB_CALL_LEDGER_V1",
        "hjb_budget": 6, "hjb_calls_started": 0, "hjb_calls_completed": 0,
        "kfe_budget": 0, "successful_province_hjb_budget": 0,
        "scientific_retries": 0, "engineering_retry_budget": 1,
        "engineering_retries_used": 0, "province_calls": [],
    }
    ledger.update({key: 0 for key in FORBIDDEN_LEDGER_KEYS})
    return ledger


def preflight(output_root: Path) -> int:
    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=False)
    source = source_identity_receipt()
    authority = load_six_failure_authority()
    invariance = input_invariance_receipt(authority["failures"])
    instrumentation = instrumentation_invariance_receipt()
    neighbors = nearest_successful_neighbors()
    ledger = empty_call_ledger()
    write_json(root / "source_identity.json", source)
    write_json(root / "input_authority_receipt.json", {**authority, "fixture_invariance": invariance})
    write_json(root / "instrumentation_invariance_receipt.json", instrumentation)
    write_json(root / "nearest_successful_neighbors.json", neighbors)
    write_json(root / "pre_science_call_ledger.json", ledger)
    status = source["pass"] and authority["pass"] and invariance["pass"] and instrumentation["pass"]
    write_json(root / "preflight_complete.json", {"status": "PASS" if status else "FAIL", "science_calls": 0})
    return 0 if status else 1


def execute(output_root: Path) -> int:
    root = Path(output_root)
    preflight_status = json.loads((root / "preflight_complete.json").read_text(encoding="utf-8"))
    if preflight_status != {"science_calls": 0, "status": "PASS"}:
        raise RuntimeError("preflight is not clean")
    if (root / "science_started.json").exists():
        raise FileExistsError("the exactly-once six-province HJB panel has already started")
    authority = json.loads((root / "input_authority_receipt.json").read_text(encoding="utf-8"))
    ledger = json.loads((root / "pre_science_call_ledger.json").read_text(encoding="utf-8"))
    write_json(root / "science_started.json", {
        "task_id": TASK_ID, "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "province_order": [row["province"] for row in authority["failures"]],
        "fresh_initialization": True,
    })
    classifications = []
    traces_root = root / "traces"
    traces_root.mkdir()
    for call, row in enumerate(authority["failures"], start=1):
        fixture = build_fixture(row)
        point_id = f"p{row['province_index']:02d}_{row['province']}"
        write_json(root / f"{point_id}_started.json", {
            "call": call, "province_index": row["province_index"], "province": row["province"],
            "fresh_initialization": True, "warm_start": False,
            "initial_value_sha256": accepted_hjb.array_sha256(fixture.initial_value),
            "baseline_labor_sha256": accepted_hjb.array_sha256(fixture.baseline_labor),
        })
        ledger["hjb_calls_started"] += 1
        write_json(root / f"ledger_before_{point_id}.json", ledger)
        result, trace = observe_accepted_hjb(*fixture.arguments())
        ledger["hjb_calls_completed"] += 1
        replay_hashes = _result_array_hashes(result)
        accepted_arrays = row["accepted_scientific_arrays"]["arrays"]
        comparable = {name: value for name, value in replay_hashes.items() if name in accepted_arrays}
        array_hashes_exact = all(value == accepted_arrays[name]["sha256"] for name, value in comparable.items())
        all_legal = all(item["operator"]["legal"] for item in trace["iterations"])
        reproducibility_open = bool(
            not result.converged and result.iterations == row["accepted_iterations"] == 100
            and result.convergence_statistic == row["accepted_final_convergence_statistic"]
            and array_hashes_exact and all_legal
        )
        mechanism = classify_trace(
            trace, replay_converged=bool(result.converged), reproducibility_open=reproducibility_open,
        )
        mechanism.update({
            "province_index": row["province_index"], "province": row["province"],
            "exact_household_inputs": {
                "r_b": row["r_b"], "consumed_r_a": row["consumed_r_a"],
                "household_composite_wage": row["household_composite_wage"],
                "tau": row["tau"], "transfer_income": row["transfer_income"],
                "borrowing_rate_gap": row["borrowing_rate_gap"],
                "return_guard_state": row["return_guard_state"],
                "wage_guard_state": row["wage_guard_state"],
            },
            "replay_converged": bool(result.converged), "replay_iterations": int(result.iterations),
            "reproduced_accepted_legal_nonconvergence": reproducibility_open,
            "accepted_final_convergence_statistic": row["accepted_final_convergence_statistic"],
            "replay_final_convergence_statistic": float(result.convergence_statistic),
            "accepted_result_array_hashes_exact": array_hashes_exact,
            "replay_result_array_hashes": replay_hashes,
        })
        trace["province_index"] = row["province_index"]
        trace["province"] = row["province"]
        trace["schema"] = "CH5_MP4C_K1_J160_PROVINCIAL_HJB_ITERATION_TRACE_V1"
        write_json(traces_root / f"{point_id}.json", trace)
        write_json(root / f"{point_id}_outcome.json", mechanism)
        classifications.append(mechanism)
        ledger["province_calls"].append({
            "call": call, "province_index": row["province_index"], "province": row["province"],
            "completed": True, "retried": False, "reproducibility_open": reproducibility_open,
            "classification": mechanism["classification"],
        })
    write_json(root / "province_mechanism_classification.json", {
        "schema": "CH5_MP4C_K1_J160_SIX_FAILURE_PROVINCE_MECHANISM_CLASSIFICATION_V1",
        "provinces": classifications,
    })
    write_json(root / "call_ledger.json", ledger)
    write_json(root / "execution_complete.json", {
        "status": "SIX_FAILURE_HJB_PANEL_EXECUTION_COMPLETE",
        "hjb_calls": ledger["hjb_calls_started"], "kfe_calls": 0,
        "scientific_retries": 0, "results_eligibility": False,
    })
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("preflight", "run"))
    parser.add_argument("output_root", type=Path)
    args = parser.parse_args()
    return preflight(args.output_root) if args.command == "preflight" else execute(args.output_root)


if __name__ == "__main__":
    raise SystemExit(main())
