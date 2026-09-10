"""Prepare and run exactly one corrected-2018 bounded 100-turn trajectory."""
from __future__ import annotations

import argparse
import csv
import json
import os
import platform
import sys
import time
from collections import Counter
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

import numpy as np

REPO = Path(__file__).resolve().parents[3]
for item in (REPO / "src", REPO):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))

from validators.multi_province.corrected_2018_single_turn import run as single
from ch5_two_asset_hank.multi_province import one_turn as one_turn_module
from ch5_two_asset_hank.multi_province.one_turn import OneTurnInputs, PreFrozenHouseholdOutputBatch
from ch5_two_asset_hank.multi_province.steady_state import (
    AdaptiveAction, _adapt, _diagnostics, _freeze_state, _post_turn_states,
)

VERDICT_PASS = "CORRECTED_2018_100TURN_DIAGNOSTIC_PASS__BOUNDARY_HITS_DECAY_AND_SOURCE_PATH_APPROACHES_INTERIOR"
VERDICT_PARTIAL = "CORRECTED_2018_100TURN_DIAGNOSTIC_PARTIAL__BOUNDARY_HITS_DECLINE_BUT_PERSIST"
VERDICT_FAIL = "CORRECTED_2018_100TURN_DIAGNOSTIC_FAIL__BOUNDARY_HITS_PERSIST_OR_OSCILLATE"
VERDICT_BLOCKED = "CORRECTED_2018_100TURN_DIAGNOSTIC_BLOCKED__EARLY_HARD_SCIENTIFIC_FAILURE"
VERDICT_TURN_MISMATCH = {
    1: "CORRECTED_2018_100TURN_DIAGNOSTIC_BLOCKED__TURN1_REPRODUCTION_MISMATCH",
    2: "CORRECTED_2018_100TURN_DIAGNOSTIC_BLOCKED__TURN2_REPRODUCTION_MISMATCH",
    3: "CORRECTED_2018_100TURN_DIAGNOSTIC_BLOCKED__TURN3_REPRODUCTION_MISMATCH",
}
ACCEPTED_DIR = REPO / "reports/mp4c_2018_corrected_three_turn_reexec_20260909"
ACCEPTED_SHA256 = {
    "turn_by_turn_observables": "E3E9CA4FE2AE6E62D2B43928621D735D56939AA025298255891B5F14C84AB22A",
    "transition_summary": "CA1E2871A7488E07D6EA8727A85A9D9B60B2250629CA4B12C4906BB26BD0253F",
    "manifest": "E96D89CF74CB27BADAFE85C601C88FFC05A20DD6E82FC339B07B8A1CD2A02B5C",
}
THREAD_ENV = ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS")


def write_json(path: Path, value: Any) -> None:
    single.write_json(path, value)


def _canonical_bytes(value: Any) -> bytes:
    return (json.dumps(single.jsonable(value), ensure_ascii=False, sort_keys=True,
                       separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def _value_sha(value: Any) -> str:
    return sha256(_canonical_bytes(value)).hexdigest().upper()


def prepare(canonical_workbook: Path, distance_workbook: Path, evidence_root: Path) -> None:
    root = Path(evidence_root)
    root.mkdir(parents=True, exist_ok=False)
    payload = single.build_runtime_payload(canonical_workbook, distance_workbook)
    payload["schema"] = "CH5_CORRECTED_2018_100TURN_BOUNDARY_RUNTIME_INPUT_V1"
    payload_path = root / "runtime_input_payload.json"
    write_json(payload_path, payload)
    accepted_paths = {
        "turn_by_turn_observables": ACCEPTED_DIR / "turn_by_turn_observables.json",
        "transition_summary": ACCEPTED_DIR / "transition_summary.json",
        "manifest": ACCEPTED_DIR / "manifest.json",
    }
    if not all(path.is_file() for path in accepted_paths.values()):
        raise ValueError("accepted three-turn predecessor evidence is missing")
    accepted_actual = {name: single.file_sha256(path) for name, path in accepted_paths.items()}
    if accepted_actual != ACCEPTED_SHA256:
        raise ValueError(f"accepted turn-1 evidence identity mismatch: {accepted_actual}")
    write_json(root / "runtime_input_receipt.json", {
        "schema": "CH5_CORRECTED_2018_100TURN_BOUNDARY_RUNTIME_RECEIPT_V1",
        "canonical_workbook_sha256": payload["canonical_workbook"]["sha256"],
        "runtime_payload_sha256": single.file_sha256(payload_path),
        "temporal_contract": single.CONTRACT, "province_count": 31,
        "province_order": payload["province_order"],
        "grid": {"I": 20, "b": [-2.0, 5.0], "J": 20, "a": [0.0, 10.0],
                 "Nz": 2, "z": [0.8, 1.3]},
        "accepted_predecessor": {name: {"path": str(path.relative_to(REPO)).replace("\\", "/"),
                                    "sha256": accepted_actual[name]}
                           for name, path in accepted_paths.items()},
        "scientific_calls": 0,
    })
    write_json(root / "source_code_identity.json", {
        "schema": "CH5_CORRECTED_2018_100TURN_BOUNDARY_SOURCE_IDENTITY_V1",
        "files": {str(path.relative_to(REPO)).replace("\\", "/"): single.file_sha256(path)
                  for path in (Path(__file__), Path(single.__file__),
                               REPO / "exports/matlab_faithful_two_asset_ha.py",
                               REPO / "src/ch5_two_asset_hank/multi_province/one_turn.py",
                               REPO / "src/ch5_two_asset_hank/multi_province/steady_state.py",
                               REPO / "src/ch5_two_asset_hank/multi_province/firm.py")},
        "scientific_calls": 0,
    })
    write_json(root / "engineering_preflight.json", {
        "schema": "CH5_CORRECTED_2018_100TURN_ENGINEERING_PREFLIGHT_V1",
        "scientific_calls": 0,
        "trajectory_ceiling": 1,
        "turn_ceiling": 100,
        "province_update_ceiling": 3100,
        "second_run_guard": "science_started.json existence rejects every later launch",
        "incremental_persistence": "unique per-turn JSON plus per-province JSON/CSV",
        "required_repo_ledgers": [
            "turn_ledger.csv", "boundary_hit_province_ledger.csv", "window_decay_summary.csv",
            "anhui_trace.csv", "controller_action_summary.csv", "scientific_validity_ledger.csv",
            "call_ledger.json",
        ],
        "engineering_retry_count": 1,
        "engineering_retry": {
            "failed_root": r"D:\ProjectTemp\ch5-corrected-2018-100turn-boundary-trajectory-20260910-001",
            "failure": "stale inherited predecessor SHA constants rejected fresh live-main accepted package",
            "scientific_state_advanced": False,
            "scientific_calls": 0,
        },
    })


def compare_predecessor(turn: int, rows: list[dict[str, Any]], summary: dict[str, Any]) -> dict[str, Any]:
    accepted_all = json.loads((ACCEPTED_DIR / "turn_by_turn_observables.json").read_text(encoding="utf-8"))
    accepted_rows = accepted_all[f"turn_{turn}"]
    accepted_summary = json.loads((ACCEPTED_DIR / "transition_summary.json").read_text(encoding="utf-8"))["turns"][turn - 1]
    mismatches: list[dict[str, Any]] = []
    if len(rows) != len(accepted_rows):
        mismatches.append({"path": "rows.length", "fresh": len(rows), "accepted": len(accepted_rows)})
    else:
        for index, accepted in enumerate(accepted_rows):
            for key, expected in accepted.items():
                actual = rows[index].get(key, "__MISSING__")
                if actual != expected:
                    mismatches.append({"path": f"rows[{index}].{key}", "fresh": actual, "accepted": expected})
    for key, expected in accepted_summary.items():
        actual = summary.get(key, "__MISSING__")
        if actual != expected:
            mismatches.append({"path": f"summary.{key}", "fresh": actual, "accepted": expected})
    return {
        "schema": "CH5_CORRECTED_2018_PREDECESSOR_TURN_REPRODUCTION_V1",
        "turn": turn,
        "comparison_rule": "EXACT_JSON_VALUE_AND_SOURCE_ORDER_IDENTITY",
        "accepted_package_sha256": ACCEPTED_SHA256["turn_by_turn_observables"],
        "fresh_rows_value_sha256": _value_sha(rows),
        "mismatch_count": len(mismatches), "mismatches": mismatches,
        "passed": not mismatches,
    }


def rah_provenance(turn: int, index: int, states: tuple[Mapping[str, object], ...],
                   prior_states: tuple[Mapping[str, object], ...] | None = None) -> dict[str, Any]:
    if turn == 1:
        return {"entering_state_field": "rah", "source": "canonical_initial_state.scalars.rah",
                "value": float(states[index]["rah"]), "manual_override": False}
    if prior_states is None:
        raise ValueError("lagged rah provenance requires prior entering states")
    ratios = np.array([float(state["inter_prv_ratio"]) for state in prior_states])
    old_ra = np.array([float(state["ra"]) for state in prior_states])
    # Match capital_allocation.allocate_productive_capital's ordered Python
    # summation exactly; np.sum can differ by one binary64 ulp.
    weighted_total = sum(float(ratios[i] * old_ra[i]) for i in range(len(prior_states)))
    own_ratio = float(ratios[index])
    own_old_ra = float(old_ra[index])
    rebuilt = ((1.0 - own_ratio) * own_old_ra
               + own_ratio * (weighted_total - own_ratio * own_old_ra) / (len(states) - 1))
    actual = float(states[index]["rah"])
    if actual != rebuilt:
        raise ValueError("native turn-2 rah does not match capital-allocation lag formula")
    return {
        "entering_state_field": "rah",
        "source": f"turn_{turn - 1}.one_turn.capital.household_illiquid_return_rah -> steady_state._post_turn_states.rah",
        "formula": "(1-ratio_i)*old_ra_i + ratio_i*(sum_j(ratio_j*old_ra_j)-ratio_i*old_ra_i)/(n-1)",
        "source_old_ra_turn": turn - 1, "source_old_ra_field": f"turn_{turn - 1}.entering_state.ra",
        "own_inter_prv_ratio": own_ratio, "own_old_ra": own_old_ra,
        "weighted_old_ra_total": weighted_total, "value": actual,
        "source_old_ra_vector_sha256": _value_sha(old_ra.tolist()), "manual_override": False,
    }


def national_summary(turn: int, rows: list[dict[str, Any]], controller: dict[str, Any]) -> dict[str, Any]:
    raw_ra = np.array([row["firm_ra0"] for row in rows], dtype=float)
    used_ra = np.array([row["firm_ra_used"] for row in rows], dtype=float)
    raw_wage = np.array([row["firm_wage_raw"] for row in rows], dtype=float)
    used_wage = np.array([row["firm_wage_used"] for row in rows], dtype=float)
    rah = np.array([row["household_rah"] for row in rows], dtype=float)
    household_w = np.array([row["household_composite_wage"] for row in rows], dtype=float)
    nk = np.array([row["nk_gap"] for row in rows], dtype=float)
    yt = np.array([row["yt_gap"] for row in rows], dtype=float)
    gdp = np.array([row["gdp_level_gap"] for row in rows], dtype=float)
    rate_regions = Counter("lower" if row["firm_ra0"] < row["ramin"] else
                           "upper" if row["firm_ra0"] > row["ramax"] else "interior" for row in rows)
    wage_regions = Counter("lower" if row["firm_wage_raw"] < row["wjtmin"] else
                           "upper" if row["firm_wage_raw"] > row["wjtmax"] else "interior" for row in rows)
    def stats(values: np.ndarray) -> dict[str, float]:
        return {"min": float(np.min(values)), "median": float(np.median(values)), "max": float(np.max(values))}
    result = {
        "turn": turn,
        "firm_rate_regions": {key: rate_regions.get(key, 0) for key in ("lower", "interior", "upper")},
        "wage_regions": {key: wage_regions.get(key, 0) for key in ("lower", "interior", "upper")},
        "ra_lower_hit_provinces": [row["province"] for row in rows if row["ra_clipped_lower"]],
        "ra_upper_hit_provinces": [row["province"] for row in rows if row["ra_clipped_upper"]],
        "wage_lower_hit_provinces": [row["province"] for row in rows if row["wage_clipped_lower"]],
        "wage_upper_hit_provinces": [row["province"] for row in rows if row["wage_clipped_upper"]],
        "raw_ra0": {**stats(raw_ra), "min_province": rows[int(np.argmin(raw_ra))]["province"],
                    "max_province": rows[int(np.argmax(raw_ra))]["province"]},
        "used_ra": stats(used_ra), "raw_wage": stats(raw_wage), "used_wage": stats(used_wage),
        "household_rah": stats(rah), "household_composite_wage": stats(household_w),
        "nk_gap": stats(nk), "yt_gap": stats(yt), "gdp_level_gap": stats(gdp),
        "hjb_iterations": stats(np.array([row["hjb_iterations"] for row in rows], dtype=float)),
        "hjb_iteration_distribution": dict(sorted(Counter(str(row["hjb_iterations"]) for row in rows).items())),
        "hjb_failures": sum(not row["hjb_converged"] for row in rows),
        "kfe_failures": sum(not row["kfe_returned"] for row in rows),
        "source_converged": bool(controller["source_converged"]),
        "source_predicate": {
            "max_nk_gap_below_1e_9": float(np.max(nk)) < 1e-9,
            "max_yt_gap_below_1e_9": float(np.max(yt)) < 1e-9,
            "all_households_converged": controller["household_converged_count"] == 31,
            "ra_has_no_boundary_hits": rate_regions.get("lower", 0) + rate_regions.get("upper", 0) == 0,
        },
        "controller": {"adaptation_gate_open": controller["adaptation_allowed"],
                       "zt_adjusted_count": sum(action["zt_adjusted"] for action in controller["actions"]),
                       "govinv_action_counts": dict(Counter(action["govinv_action"] for action in controller["actions"]))},
    }
    for field in ("A", "B", "A_plus_B", "L", "C", "At", "Bt", "Lt", "Ct",
                  "GovInv", "govinv_after"):
        result[field] = stats(np.array([row[field] for row in rows], dtype=float))
    result["kfe_diagnostic_status_counts"] = dict(Counter(row["kfe_diagnostic_status"] for row in rows))
    result["kfe_source_free_residual"] = stats(
        np.array([row["kfe_source_free_residual_inf"] for row in rows], dtype=float))
    result["kfe_source_free_ratio"] = stats(
        np.array([row["kfe_source_free_normwise_ratio"] for row in rows], dtype=float))
    result["kfe_upper_b_leak_cells"] = int(sum(row["kfe_upper_b_leak_count"] for row in rows))
    result["hjb_negative_offdiagonals"] = int(sum(row["hjb_negative_offdiagonal_count"] for row in rows))
    return result


WINDOWS = ((1, 10), (11, 25), (26, 50), (51, 75), (76, 100))


def classify_boundary_path(summaries: list[dict[str, Any]], family: str) -> str:
    """Classify one boundary-count path by a frozen count-based rule."""
    if not summaries:
        return "INSUFFICIENT_TURNS_DUE_TO_EARLY_HARD_FAILURE"
    key = "firm_rate_regions" if family == "ra" else "wage_regions"
    counts = [int(row[key]["lower"]) + int(row[key]["upper"]) for row in summaries]
    first = counts[:min(10, len(counts))]
    final = counts[max(0, len(counts) - 25):]
    if len(counts) < 10:
        return "INSUFFICIENT_TURNS_DUE_TO_EARLY_HARD_FAILURE"
    if max(final) == 0:
        return "BOUNDARY_HITS_DECAY_TO_ZERO"
    first_mean = float(np.mean(first))
    final_mean = float(np.mean(final))
    if first_mean > 0.0 and final_mean <= 0.5 * first_mean and counts[-1] < counts[0]:
        return "BOUNDARY_HITS_MATERIALLY_DECLINE_BUT_NOT_ZERO"
    deltas = np.diff(np.asarray(counts, dtype=float))
    nonzero = deltas[deltas != 0.0]
    direction_changes = int(np.count_nonzero(nonzero[1:] * nonzero[:-1] < 0.0))
    if direction_changes >= 3 and final_mean > 0.75 * first_mean:
        return "BOUNDARY_HITS_OSCILLATE_WITHOUT_DECAY"
    return "BOUNDARY_HITS_PERSIST_HIGH"


def trajectory_verdict(summaries: list[dict[str, Any]]) -> str:
    classes = [classify_boundary_path(summaries, family) for family in ("ra", "wage")]
    if all(value == "BOUNDARY_HITS_DECAY_TO_ZERO" for value in classes):
        return VERDICT_PASS
    if all(value in {"BOUNDARY_HITS_DECAY_TO_ZERO",
                     "BOUNDARY_HITS_MATERIALLY_DECLINE_BUT_NOT_ZERO"} for value in classes):
        return VERDICT_PARTIAL
    return VERDICT_FAIL


def hjb_operator_diagnostics(hjb: Any) -> dict[str, Any]:
    """Pure post-processing of the returned HJB-loop operator; no solve."""
    matrix = hjb.post_convergence_operator.full.tocsr()
    off = matrix.copy()
    off.setdiag(0.0)
    off.eliminate_zeros()
    values = off.data
    negative = values[values < -1e-12]
    return {
        "schema": "CH5_CORRECTED_2018_100TURN_HJB_OPERATOR_DIAGNOSTIC_V1",
        "classification": "VALID" if negative.size == 0 else "DIAGNOSTIC_ONLY",
        "negative_offdiagonal_count": int(negative.size),
        "minimum_offdiagonal": float(negative.min()) if negative.size else 0.0,
        "pure_post_processing": True,
        "additional_solves": 0,
    }


def kfe_distribution_diagnostics(hjb: Any, kfe: Any) -> dict[str, Any]:
    """Pure post-processing of the returned operator, density, and drifts; no solve."""
    eps = np.finfo(float).eps
    density = np.asarray(kfe.density_vector, dtype=float)
    transpose = kfe.transpose.tocsr()
    stationary = np.asarray(transpose @ density, dtype=float)
    source_numerator = float(np.linalg.norm(stationary, ord=np.inf))
    source_scale = float(np.max(np.asarray(abs(transpose).sum(axis=1)).ravel())
                         * np.linalg.norm(density, ord=np.inf))
    source_ratio = source_numerator / source_scale if source_scale else 0.0
    raw_residual = np.asarray(kfe.contaminated_matrix @ kfe.raw_solve_vector - kfe.rhs)
    raw_numerator = float(np.linalg.norm(raw_residual, ord=np.inf))
    raw_scale = float(np.max(np.asarray(abs(kfe.contaminated_matrix).sum(axis=1)).ravel())
                      * np.linalg.norm(kfe.raw_solve_vector, ord=np.inf)
                      + np.linalg.norm(kfe.rhs, ord=np.inf))
    mu_b = np.asarray(hjb.mu_b, dtype=float)
    mu_a = np.asarray(hjb.mu_a, dtype=float)
    faces = {
        "lower_b": np.maximum(-mu_b[0, :, :], 0.0) / kfe.db,
        "upper_b": np.maximum(mu_b[-1, :, :], 0.0) / kfe.db,
        "lower_a": np.maximum(-mu_a[:, 0, :], 0.0) / kfe.da,
        "upper_a": np.maximum(mu_a[:, -1, :], 0.0) / kfe.da,
    }
    boundary = {name: {"outward_leak_count": int(np.count_nonzero(rate > 0.0)),
                       "max_outward_leak_rate": float(rate.max(initial=0.0)),
                       "sum_outward_leak_rate": float(rate.sum())}
                for name, rate in faces.items()}
    mass = float(density.sum() * kfe.cell_weight)
    negative_count = int(np.count_nonzero(density < 0.0))
    negative_mass = float(np.minimum(density, 0.0).sum() * kfe.cell_weight)
    finite = bool(np.isfinite(density).all() and np.isfinite(stationary).all())
    mass_ok = abs(mass - 1.0) <= 128.0 * eps
    sign_ok = float(density.min()) >= -1e-12
    stationarity_ok = source_ratio <= 128.0 * eps
    boundary_ok = not any(item["max_outward_leak_rate"] > 1e-12 for item in boundary.values())
    status = "VALID" if finite and mass_ok and sign_ok and stationarity_ok and boundary_ok else "DIAGNOSTIC_ONLY"
    return {
        "schema": "CH5_CORRECTED_2018_100TURN_BOUNDARY_KFE_DISTRIBUTION_DIAGNOSTIC_V1",
        "classification": status, "pure_post_processing": True, "additional_solves": 0,
        "normalized_mass": mass, "density_min": float(density.min()),
        "density_max": float(density.max()), "negative_entry_count": negative_count,
        "weighted_negative_mass": negative_mass,
        "contaminated_row_residual_numerator": raw_numerator,
        "contaminated_row_residual_scale": raw_scale,
        "contaminated_row_residual_ratio": raw_numerator / raw_scale if raw_scale else 0.0,
        "source_reported_contaminated_residual_inf": float(kfe.raw_residual_inf),
        "source_free_residual_numerator": source_numerator,
        "source_free_residual_scale": source_scale,
        "source_free_residual_ratio": source_ratio,
        "boundary_outward_leak": boundary,
        "upper_b_face_probability_mass": float(np.sum(kfe.density[-1, :, :]) * kfe.cell_weight),
        "checks": {"finite": finite, "normalized_mass": mass_ok, "density_sign": sign_ok,
                   "source_free_stationarity": stationarity_ok, "boundary_no_material_outward_leak": boundary_ok},
        "thresholds": {"mass_absolute": 128.0 * eps, "density_min": -1e-12,
                       "source_free_normwise_ratio": 128.0 * eps,
                       "boundary_max_outward_rate": 1e-12},
    }


def execute(evidence_root: Path) -> int:
    root = Path(evidence_root)
    payload_path = root / "runtime_input_payload.json"
    if not payload_path.is_file() or not (root / "runtime_input_receipt.json").is_file():
        raise ValueError("prepared runtime input is missing")
    if (root / "science_started.json").exists():
        raise RuntimeError("scientific trajectory already started; retry prohibited")
    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    if payload["canonical_workbook"]["sha256"] != single.CANONICAL_SHA256:
        raise ValueError("prepared canonical identity mismatch")
    counters = {key: 0 for key in (
        "turns_entered", "turns_completed", "province_updates_attempted", "province_updates_completed",
        "household_calls_attempted", "household_calls_returned", "household_calls_failed",
        "native_initializations_attempted", "native_initializations_returned",
        "labor_roots_attempted", "labor_roots_returned", "brentq_calls_attempted", "brentq_calls_returned",
        "hjb_calls", "hjb_returns", "hjb_direct_solves", "kfe_calls", "kfe_returns", "kfe_direct_solves",
        "aggregate_calls", "aggregate_returns", "one_turn_executions", "one_turn_returns",
        "migration_calls", "capital_allocation_calls", "firm_calls", "firm_returns",
        "wage_batch_calls", "wage_province_outputs", "controller_calls", "adaptation_calls",
        "adaptation_gate_open_count")}
    counters.update({"scientific_processes": 1, "trajectory_attempts": 1,
                     "trajectory_returns": 0, "scientific_retries": 0})
    write_json(root / "science_started.json", {
        "schema": "CH5_CORRECTED_2018_100TURN_BOUNDARY_LAUNCH_V1",
        "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "process_id": os.getpid(), "python": sys.version, "platform": platform.platform(),
        "thread_environment": {key: os.environ.get(key) for key in THREAD_ENV},
        "authorized_trajectory_count": 1, "authorized_turns": 100, "scientific_retries": 0,
        "runtime_payload_sha256": single.file_sha256(payload_path),
    })
    states = tuple(dict(item) for item in payload["states"])
    initial_states = states
    prior_entering_states: tuple[Mapping[str, object], ...] | None = None
    tkn_ratio = np.full(31, 3.0)
    wedges = np.array(payload["matrices"]["sigmau_destination_origin"], dtype=float)
    grid = single.oracle.MatlabFaithfulHJBGrid(np.linspace(-2, 5, 20), np.linspace(0, 10, 20),
        np.array([0.8, 1.3]), np.array([[-1/3, 1/3], [1/3, -1/3]]))
    params = single.oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    numerics = single.oracle.MatlabFaithfulHJBNumerics(1000.0, 1e-7, 100, 1e-12)
    model_params = MappingProxyType({"ga": 2.0, "phi_l": 5.0, "alphal": 1.0, "epsilon": 10.0,
        "theta": 100.0, "delta": 0.025, "istar": 0.015, "rho_pi": 1.25,
        "totalpit": 0.02, "epsilon_pi": 0.0})
    current = {"stage": "PRE_SCIENCE", "turn": 0, "province_index": None, "province": None}
    original_spsolve = single.oracle.linalg.spsolve
    original_brentq = single.LABOR_BRENTQ
    started = time.monotonic()
    verdict = VERDICT_BLOCKED
    error = None
    turn_summaries: list[dict[str, Any]] = []
    predecessor_reproduction: list[dict[str, Any]] = []

    def counted_spsolve(*args, **kwargs):
        key = "hjb_direct_solves" if current["stage"] == "HJB" else "kfe_direct_solves"
        counters[key] += 1
        return original_spsolve(*args, **kwargs)
    def counted_brentq(*args, **kwargs):
        counters["brentq_calls_attempted"] += 1
        result = original_brentq(*args, **kwargs)
        counters["brentq_calls_returned"] += 1
        return result

    single.oracle.linalg.spsolve = counted_spsolve
    single.LABOR_BRENTQ = counted_brentq
    try:
        for turn_index in range(1, 101):
            if counters["turns_entered"] >= 100:
                raise RuntimeError("authorized 100-turn ceiling would be exceeded")
            current.update(stage="TURN_ENTRY", turn=turn_index, province_index=None, province=None)
            counters["turns_entered"] += 1
            turn_root = root / f"turn_{turn_index:02d}"
            outputs: list[dict[str, Any]] = []
            provenance = [rah_provenance(turn_index, index, states, prior_entering_states) for index in range(31)]
            write_json(turn_root / "entering_state.json", {"turn": turn_index, "states": states,
                "rah_provenance": provenance, "tkn_ratio": tkn_ratio})
            productivity = np.array([float(state["Yt"]) / float(state["Lt"]) for state in states])
            phi = 1.0 + 0.3 * (productivity[:, None] - productivity[None, :]) / (productivity[:, None] + productivity[None, :])
            for index, state in enumerate(states):
                province = payload["province_order"][index]
                province_root = turn_root / "household" / f"p{index:02d}_{province}"
                current.update(stage="NATIVE_INITIALIZATION", province_index=index, province=province)
                counters["household_calls_attempted"] += 1
                counters["native_initializations_attempted"] += 1
                def enter_root() -> None: counters["labor_roots_attempted"] += 1
                def return_root() -> None: counters["labor_roots_returned"] += 1
                initial, labor = single.source_initial_arrays(state, grid, params, enter_root, return_root)
                counters["native_initializations_returned"] += 1
                current["stage"] = "HJB"; counters["hjb_calls"] += 1
                hjb = single.oracle.solve_matlab_faithful_hjb(grid, params, single.oracle.HouseholdInputs(
                    float(state["rah"]), float(state["rb"]), float(state["tau"]),
                    np.array([state["w"]]), np.array([0.0]), np.array([1.0])), initial, labor,
                    float(state["Tt"]), float(state["rb_gap"]), numerics)
                counters["hjb_returns"] += 1
                single._save_hjb(province_root / "hjb_return.npz", hjb)
                hjb_diagnostic = hjb_operator_diagnostics(hjb)
                write_json(province_root / "hjb_operator_diagnostic.json", hjb_diagnostic)
                write_json(province_root / "hjb_receipt.json", {"turn": turn_index, "province_index": index,
                    "province": province, "converged": hjb.converged, "iterations": hjb.iterations,
                    "convergence_statistic": hjb.convergence_statistic, "persisted_before_kfe": True})
                if not hjb.converged:
                    raise RuntimeError("HJB did not converge")
                current["stage"] = "KFE"; counters["kfe_calls"] += 1
                kfe = single.oracle.solve_matlab_faithful_stationary_kfe(hjb.post_convergence_operator.full,
                    shape=(20, 20, 2), db=float(grid.b[1]-grid.b[0]), da=float(grid.a[1]-grid.a[0]))
                counters["kfe_returns"] += 1
                single._save_kfe(province_root / "kfe_return.npz", kfe)
                kfe_diagnostic = kfe_distribution_diagnostics(hjb, kfe)
                write_json(province_root / "kfe_distribution_diagnostic.json", kfe_diagnostic)
                current["stage"] = "AGGREGATE"; counters["aggregate_calls"] += 1
                aggregate = single.oracle.aggregate_stationary_household(grid, hjb.consumption, hjb.labor, kfe.density)
                counters["aggregate_returns"] += 1
                effective = single.oracle.matlab_faithful_illiquid_return(grid.a, grid.a[-1], float(state["rah"]))
                at_tax = aggregate.a_ss * float(state["rah"]) - float(
                    np.sum(grid.a[None,:,None] * effective[None,:,None] * kfe.density) * kfe.cell_weight)
                output = {"hjb_converged": hjb.converged, "hjb_iterations": hjb.iterations,
                    "hjb_statistic": hjb.convergence_statistic, "kfe_returned": True,
                    "kfe_raw_residual_inf": kfe.raw_residual_inf, "C": aggregate.c_ss, "L": aggregate.l_ss,
                    "A": aggregate.a_ss, "B": aggregate.b_ss, "A_plus_B": aggregate.a_ss + aggregate.b_ss,
                    "AtTax": at_tax}
                output.update({
                    "kfe_diagnostic_status": kfe_diagnostic["classification"],
                    "kfe_normalized_mass": kfe_diagnostic["normalized_mass"],
                    "kfe_density_min": kfe_diagnostic["density_min"],
                    "kfe_density_max": kfe_diagnostic["density_max"],
                    "kfe_negative_entry_count": kfe_diagnostic["negative_entry_count"],
                    "kfe_weighted_negative_mass": kfe_diagnostic["weighted_negative_mass"],
                    "kfe_source_free_residual_inf": kfe_diagnostic["source_free_residual_numerator"],
                    "kfe_source_free_residual_scale": kfe_diagnostic["source_free_residual_scale"],
                    "kfe_source_free_normwise_ratio": kfe_diagnostic["source_free_residual_ratio"],
                    "kfe_upper_b_face_mass": kfe_diagnostic["upper_b_face_probability_mass"],
                    "kfe_upper_b_leak_count":
                        kfe_diagnostic["boundary_outward_leak"]["upper_b"]["outward_leak_count"],
                    "kfe_upper_b_max_leak_rate":
                        kfe_diagnostic["boundary_outward_leak"]["upper_b"]["max_outward_leak_rate"],
                    "hjb_operator_status": hjb_diagnostic["classification"],
                    "hjb_negative_offdiagonal_count": hjb_diagnostic["negative_offdiagonal_count"],
                    "hjb_minimum_offdiagonal": hjb_diagnostic["minimum_offdiagonal"],
                })
                if not all(np.isfinite(float(output[key])) for key in
                           ("hjb_statistic", "kfe_raw_residual_inf", "C", "L", "A", "B",
                            "A_plus_B", "AtTax", "kfe_normalized_mass", "kfe_density_min",
                            "kfe_density_max", "kfe_source_free_residual_inf",
                            "kfe_source_free_residual_scale", "kfe_source_free_normwise_ratio")):
                    raise RuntimeError("nonfinite household or aggregate output")
                write_json(province_root / "household_return.json", output)
                outputs.append(output); counters["household_calls_returned"] += 1

            batch = PreFrozenHouseholdOutputBatch(
                ct=[row["C"] for row in outputs], household_lt=[row["L"] for row in outputs],
                at=[row["A"] for row in outputs], bt=[row["B"] for row in outputs],
                at_tax=[row["AtTax"] for row in outputs], converged=tuple(row["hjb_converged"] for row in outputs),
                diagnostics=tuple({"hjb_converged": row["hjb_converged"], "hjb_iterations": row["hjb_iterations"],
                    "hjb_statistic": row["hjb_statistic"], "kfe_returned": True} for row in outputs))

            original = {name: getattr(one_turn_module, name) for name in
                        ("evaluate_firm", "composite_household_wages", "reconstruct_migration_labor", "allocate_productive_capital")}
            def observed_firm(province, *args, **kwargs):
                if counters["province_updates_attempted"] >= 3100:
                    raise RuntimeError("authorized 3100 province-update ceiling would be exceeded")
                counters["firm_calls"] += 1; counters["province_updates_attempted"] += 1
                current.update(stage="FIRM", province=province["name"], province_index=payload["province_order"].index(province["name"]))
                result = original["evaluate_firm"](province, *args, **kwargs)
                counters["firm_returns"] += 1; counters["province_updates_completed"] += 1
                return result
            def observed_wage(*args, **kwargs):
                counters["wage_batch_calls"] += 1; result = original["composite_household_wages"](*args, **kwargs)
                counters["wage_province_outputs"] += len(result); return result
            def observed_migration(*args, **kwargs):
                counters["migration_calls"] += 1; return original["reconstruct_migration_labor"](*args, **kwargs)
            def observed_capital(*args, **kwargs):
                counters["capital_allocation_calls"] += 1; return original["allocate_productive_capital"](*args, **kwargs)
            one_turn_module.evaluate_firm = observed_firm
            one_turn_module.composite_household_wages = observed_wage
            one_turn_module.reconstruct_migration_labor = observed_migration
            one_turn_module.allocate_productive_capital = observed_capital
            try:
                current.update(stage="ONE_TURN", province=None, province_index=None)
                counters["one_turn_executions"] += 1
                turn = one_turn_module.run_source_faithful_one_turn(OneTurnInputs(
                    tuple(payload["province_order"]), states, model_params, phi, wedges, batch))
                counters["one_turn_returns"] += 1
            finally:
                for name, function in original.items(): setattr(one_turn_module, name, function)

            current["stage"] = "CONTROLLER"
            before = _post_turn_states(states, batch, turn)
            nk_gap, yt_gap, household_count, ra_upper, ra_lower, wage_upper, wage_lower, converged = _diagnostics(
                before, batch, tkn_ratio, 1e-9)
            counters["controller_calls"] += 1
            if converged:
                next_states = before
                actions = tuple(AdaptiveAction(str(state["name"]), False, float(state["Zt"]), float(state["Zt"]),
                    "NONE", float(state["GovInv"]), float(state["GovInv"])) for state in before)
                tkn_after = np.array(tkn_ratio, copy=True)
            else:
                next_states, actions = _adapt(before, float(np.max(nk_gap)), True)
                counters["adaptation_calls"] += 1
                tkn_after = np.array([0.6 * float(state["KNratio"]) + 0.4 * tkn_ratio[i]
                                      for i, state in enumerate(next_states)])
            controller = {"household_converged_count": household_count,
                "all_household_hjb_converged": household_count == 31,
                "max_nk_gap": float(np.max(nk_gap)),
                "max_nk_gap_province": payload["province_order"][int(np.argmax(nk_gap))],
                "max_yt_gap": float(np.max(yt_gap)), "ra_upper_count": ra_upper, "ra_lower_count": ra_lower,
                "wage_upper_count": wage_upper, "wage_lower_count": wage_lower,
                "source_converged": converged, "adaptation_allowed": float(np.max(nk_gap)) < 0.1,
                "actions": single.jsonable(actions)}
            counters["adaptation_gate_open_count"] += int(controller["adaptation_allowed"])
            rows = []
            for index, state in enumerate(states):
                firm = turn.firms[index]; action = actions[index]; output = outputs[index]
                row = {"turn": turn_index, "province_index": index, "province": state["name"],
                    "GDP": state["Yt0"], "POP": state["N"], "CAP": state["Kt0"], "alpha": state["alpha"],
                    "same_year_Zt": state["Zt"], "GovInv": state["GovInv"], "entering_Yt": state["Yt"],
                    "entering_firm_ra": state["ra"], "household_rah": state["rah"],
                    "rah_source": provenance[index]["source"], "rah_source_value": provenance[index]["value"],
                    "household_rb": state["rb"], "household_composite_wage": state["w"],
                    "entering_Lt_prev": state["Lt_prev"], "firm_source_Lt_prev": output["L"],
                    "household_Lt_return": output["L"], "destination_lt_supply": turn.migration.lt_supply[index],
                    "firm_ra0": firm.ra0, "firm_ra_used": firm.ra, "firm_rk": firm.rk,
                    "firm_wage_raw": firm.wt0, "firm_wage_used": firm.wjt,
                    "ramin": state["ramin"], "ramax": state["ramax"],
                    "wjtmin": state["wjtmin"], "wjtmax": state["wjtmax"],
                    "hjb_converged": output["hjb_converged"], "hjb_iterations": output["hjb_iterations"],
                    "hjb_statistic": output["hjb_statistic"], "kfe_returned": True,
                    "kfe_raw_residual_inf": output["kfe_raw_residual_inf"], "C": output["C"], "L": output["L"],
                    "A": output["A"], "B": output["B"], "A_plus_B": output["A_plus_B"],
                    "Ct": output["C"], "Lt": output["L"], "At": output["A"], "Bt": output["B"],
                    "kfe_diagnostic_status": output["kfe_diagnostic_status"],
                    "kfe_normalized_mass": output["kfe_normalized_mass"],
                    "kfe_density_min": output["kfe_density_min"],
                    "kfe_density_max": output["kfe_density_max"],
                    "kfe_negative_entry_count": output["kfe_negative_entry_count"],
                    "kfe_weighted_negative_mass": output["kfe_weighted_negative_mass"],
                    "kfe_source_free_residual_inf": output["kfe_source_free_residual_inf"],
                    "kfe_source_free_residual_scale": output["kfe_source_free_residual_scale"],
                    "kfe_source_free_normwise_ratio": output["kfe_source_free_normwise_ratio"],
                    "kfe_upper_b_face_mass": output["kfe_upper_b_face_mass"],
                    "kfe_upper_b_leak_count": output["kfe_upper_b_leak_count"],
                    "kfe_upper_b_max_leak_rate": output["kfe_upper_b_max_leak_rate"],
                    "hjb_operator_status": output["hjb_operator_status"],
                    "hjb_negative_offdiagonal_count": output["hjb_negative_offdiagonal_count"],
                    "hjb_minimum_offdiagonal": output["hjb_minimum_offdiagonal"],
                    "Kt_supply": float(turn.capital.kt_supply[index]),
                    "firm_K": firm.Kt, "firm_Y": firm.Yt, "firm_mt": firm.mt,
                    "next_household_rah": float(turn.capital.household_illiquid_return_rah[index]),
                    "next_household_composite_wage": float(turn.household_composite_wage[index]),
                    "nk_gap": nk_gap[index], "yt_gap": yt_gap[index],
                    "gdp_level_gap": abs(firm.Yt / float(state["Yt0"]) - 1.0),
                    "adaptation_gate_open": controller["adaptation_allowed"],
                    "ra_clipped_lower": firm.ra == state["ramin"] and firm.ra0 < state["ramin"],
                    "ra_clipped_upper": firm.ra == state["ramax"] and firm.ra0 > state["ramax"],
                    "wage_clipped_lower": firm.wjt == state["wjtmin"] and firm.wt0 < state["wjtmin"],
                    "wage_clipped_upper": firm.wjt == state["wjtmax"] and firm.wt0 > state["wjtmax"],
                    "zt_adjusted": action.zt_adjusted, "zt_after": action.zt_after,
                    "govinv_action": action.govinv_action, "govinv_after": action.govinv_after}
                rows.append(row)
            write_json(turn_root / "per_province_observables.json", rows)
            with (turn_root / "per_province_observables.csv").open("x", encoding="utf-8-sig", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
            write_json(turn_root / "controller_observables.json", controller)
            summary = national_summary(turn_index, rows, controller)
            write_json(turn_root / "national_summary.json", summary)
            turn_summaries.append(summary)
            counters["turns_completed"] += 1
            write_json(root / "turn_ledger_incremental" / f"turn_{turn_index:03d}.json", summary)
            if turn_index in (1, 2, 3):
                reproduction = compare_predecessor(turn_index, rows, summary)
                predecessor_reproduction.append(reproduction)
                write_json(root / f"turn{turn_index}_reproduction.json", reproduction)
                if not reproduction["passed"] or turn_index == 3:
                    write_json(root / "predecessor_reproduction.json", {
                        "schema": "CH5_CORRECTED_2018_PREDECESSOR_REPRODUCTION_V1",
                        "turns": predecessor_reproduction,
                        "passed": all(item["passed"] for item in predecessor_reproduction),
                    })
                if not reproduction["passed"]:
                    verdict = VERDICT_TURN_MISMATCH[turn_index]
                    break
            prior_entering_states = states
            states = _freeze_state(next_states)
            tkn_ratio = tkn_after
            if converged:
                counters["trajectory_returns"] = 1
                break
        else:
            counters["trajectory_returns"] = 1
        if not any(not item["passed"] for item in predecessor_reproduction):
            verdict = trajectory_verdict(turn_summaries)
    except Exception as exc:
        counters["household_calls_failed"] = counters["household_calls_attempted"] - counters["household_calls_returned"]
        error = {"type": type(exc).__name__, "message": str(exc), "turn": current["turn"],
                 "stage": current["stage"], "province_index": current["province_index"],
                 "province": current["province"]}
        verdict = VERDICT_BLOCKED
        write_json(root / "scientific_failure.json", error)
    finally:
        single.oracle.linalg.spsolve = original_spsolve
        single.LABOR_BRENTQ = original_brentq
    counters["household_calls_failed"] = counters["household_calls_attempted"] - counters["household_calls_returned"]
    write_json(root / "transition_summary.json", {"schema": "CH5_CORRECTED_2018_100TURN_BOUNDARY_TRANSITION_V1",
        "turns": turn_summaries, "trajectory_completed": counters["turns_completed"] == 100})
    write_json(root / "call_ledger.json", {"schema": "CH5_CORRECTED_2018_100TURN_BOUNDARY_CALL_LEDGER_V1",
        "counts": counters, "elapsed_seconds": time.monotonic() - started, "failed_calls_counted": True,
        "authorized_max_turns": 100, "authorized_max_province_updates": 3100,
        "matlab_calls": 0, "turn101_or_later_calls": 0, "steady_state_calls": 0, "ge_calls": 0,
        "annual_model_calls": 0, "irf_calls": 0, "results_calls": 0})
    write_json(root / "terminal_result.json", {"schema": "CH5_CORRECTED_2018_100TURN_BOUNDARY_TERMINAL_V1",
        "verdict": verdict, "error": error, "completed_turns": counters["turns_completed"],
        "stop_reason": ("PREDECESSOR_REPRODUCTION_MISMATCH" if "REPRODUCTION_MISMATCH" in verdict else
                        "EARLY_HARD_SCIENTIFIC_FAILURE" if error else
                        "SOURCE_FINAL_PREDICATE" if turn_summaries and turn_summaries[-1]["source_converged"]
                        else "AUTHORIZED_100_TURN_CEILING"),
        "boundary_classification": {
            "ra": classify_boundary_path(turn_summaries, "ra"),
            "wage": classify_boundary_path(turn_summaries, "wage"),
        },
        "turn101_plus_authorized": "NO",
        "steady_state_authorized": "NO", "results_eligible": False})
    return 2 if verdict == VERDICT_BLOCKED or "REPRODUCTION_MISMATCH" in verdict else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(); sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare"); prep.add_argument("canonical_workbook", type=Path)
    prep.add_argument("distance_workbook", type=Path); prep.add_argument("evidence_root", type=Path)
    launch = sub.add_parser("run"); launch.add_argument("evidence_root", type=Path)
    args = parser.parse_args(argv)
    if args.command == "prepare":
        prepare(args.canonical_workbook, args.distance_workbook, args.evidence_root); return 0
    return execute(args.evidence_root)


if __name__ == "__main__":
    raise SystemExit(main())
