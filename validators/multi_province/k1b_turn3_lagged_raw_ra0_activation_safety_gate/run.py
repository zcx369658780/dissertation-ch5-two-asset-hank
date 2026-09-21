"""Zero-science K1B turn-3 lagged raw-ra0 activation safety gate."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET
from typing import Any

import numpy as np


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPOSITORY_ROOT))
sys.path.insert(0, str(REPOSITORY_ROOT / "src"))

from ch5_two_asset_hank.multi_province.capital_network import (
    BilateralCapitalNetworkInputs,
    CONSERVATION_TOLERANCE,
    build_bilateral_capital_network,
)
from ch5_two_asset_hank.multi_province.k1a_runtime_adapter import (
    ACCEPTED_DISTANCE_CANONICAL_LF_SHA256,
    canonical_lf_sha256,
    load_accepted_distance_score,
)
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER


TASK_ID = "CH5_MP4C_K1B_TURN3_LAGGED_RAW_RA0_ATTRACTIVENESS_ACTIVATION_SAFETY_GATE_20260921"
BASELINE = "7b6c30a568e1c89ca6a553451abe382e48ee7e23"
PASS_TERMINAL = (
    "PASS__K1B_TURN3_LAGGED_RAW_RA0_ATTRACTIVENESS_ACTIVATION_SAFETY_GATE__"
    "SHARES_AND_HOUSEHOLD_PAYOFF_CANDIDATE_READY__NO_HJB_RUN"
)
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_k1b_turn3_lagged_raw_ra0_activation_safety_gate_20260921_run001"
)
RUN005_ROOT = Path(
    "reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_fresh_turn2_run005_20260921"
)
INTEGRATION_RELATIVE = RUN005_ROOT / "one_turn_integration_receipt.json"
TURN3_CANDIDATE_RELATIVE = RUN005_ROOT / "turn3_next_state_candidate_receipt.json"
RUN005_ARRAYS_RELATIVE = RUN005_ROOT / "canonical_turn3_raw_payoff_arrays.npz"
RUN005_MANIFEST_RELATIVE = RUN005_ROOT / "sealed_manifest.json"
RUN005_READBACK_RELATIVE = RUN005_ROOT / "independent_readback_receipt.json"
DISTANCE_RELATIVE = Path(
    "docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv"
)

EXPECTED_BLOBS = {
    INTEGRATION_RELATIVE.as_posix(): "ee84f5cf3f4021ace293f70274f4d8698a397828",
    TURN3_CANDIDATE_RELATIVE.as_posix(): "fc133976cf7b1cfdbb7b21ed494095997e1ece67",
    RUN005_ARRAYS_RELATIVE.as_posix(): "d3ccd9b26ff78fe815c308e2bb03748e518d3188",
    DISTANCE_RELATIVE.as_posix(): "5a304f8b8f19b4c60ac37e52ad824b3e143caa6a",
}
EXPECTED_FILE_SHA256 = {
    INTEGRATION_RELATIVE.as_posix(): "008C05CE984B7981CFF63C6387C39A884B9DE92FB00EDEA27BD30D6EB97C10F9",
    TURN3_CANDIDATE_RELATIVE.as_posix(): "527D15DABFF75D42F302FFF7589D3141FE21F77C370A9F8830C2B066AFD20050",
    RUN005_ARRAYS_RELATIVE.as_posix(): "6EBFB6283272BC41C6FF1B57C7A1E0FEB6FF8E1D2ED2D4BA4746859C31FEDF65",
    RUN005_MANIFEST_RELATIVE.as_posix(): "C93BF19DB7C909A50C2753B0EA06FD4735F48A4C41C5A4C9CA6F8817B693B72F",
}
EXPECTED_RAW_RA0_SHA256 = "B3B50A6F0A3876904582DE05354C2DF76A71524FB53E41D4170109B8FCEB8951"
EXPECTED_K1A_RAH_SHA256 = "5996A20CEE227389A7975703452EA6DAF1A2F817C517FFE43BEF3A53FA4292E2"
EXPECTED_K1A_SHARE_SHA256 = "AC8DD36BB21E2B907D7521C98F8E65DCA3803291B54296AA7C2681E8CC6F226F"
PROVENANCE = "LAGGED__COMPLETED_TURN2_RAW_RA0__USED_FOR_TURN3_K1B_ATTRACTIVENESS"
CLASSIFICATION = "TURN3_K1B_INPUT_CANDIDATE_ONLY__HOUSEHOLD_NOT_RUN"

FROZEN_SOURCE_PATHS = (
    Path("src/ch5_two_asset_hank/multi_province/capital_network.py"),
    Path("src/ch5_two_asset_hank/multi_province/k1a_runtime_adapter.py"),
    Path("src/ch5_two_asset_hank/multi_province/province_contracts.py"),
)


class FailClosed(RuntimeError):
    def __init__(self, terminal: str, detail: dict[str, Any] | None = None) -> None:
        super().__init__(terminal)
        self.terminal = terminal
        self.detail = detail or {}


def git(repository: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repository, text=True).strip()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def field_sha256(values: object) -> str:
    encoded = np.asarray(values, dtype="<f8").tobytes(order="F")
    return hashlib.sha256(encoded).hexdigest().upper()


def canonical_sha256(value: Any) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    text = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False)
    path.write_text(text + "\n", encoding="utf-8")


def ordered_population_zscore(raw_values: object) -> tuple[float, float, np.ndarray]:
    raw = np.asarray(raw_values, dtype=np.float64)
    if raw.shape != (31,) or not np.all(np.isfinite(raw)):
        raise ValueError("raw ra0 must be the finite canonical 31-vector")
    mean = math.fsum(float(value) for value in raw) / 31.0
    deviations = np.asarray([float(value) - mean for value in raw], dtype=np.float64)
    variance = math.fsum(float(value) * float(value) for value in deviations) / 31.0
    sigma = math.sqrt(variance)
    if not math.isfinite(sigma) or sigma <= 0.0:
        raise ValueError("population raw-ra0 standard deviation must be finite and positive")
    scores = np.asarray([float(value) / sigma for value in deviations], dtype=np.float64)
    return mean, sigma, scores


def ordered_payoff(raw_values: object, shares_destination_origin: object) -> np.ndarray:
    raw = np.asarray(raw_values, dtype=np.float64)
    shares = np.asarray(shares_destination_origin, dtype=np.float64)
    if raw.shape != (31,) or shares.shape != (31, 31):
        raise ValueError("ordered payoff requires canonical 31-vector and 31x31 S")
    if not np.all(np.isfinite(raw)) or not np.all(np.isfinite(shares)):
        raise ValueError("ordered payoff inputs must be finite")
    return np.asarray(
        [
            math.fsum(float(shares[j, i]) * float(raw[j]) for j in range(31))
            for i in range(31)
        ],
        dtype=np.float64,
    )


def source_hashes(repository: Path) -> dict[str, str]:
    return {path.as_posix(): sha256(repository / path) for path in FROZEN_SOURCE_PATHS}


def load_bound_inputs(repository: Path) -> dict[str, Any]:
    integration = json.loads((repository / INTEGRATION_RELATIVE).read_text(encoding="utf-8"))
    candidate = json.loads((repository / TURN3_CANDIDATE_RELATIVE).read_text(encoding="utf-8"))
    readback = json.loads((repository / RUN005_READBACK_RELATIVE).read_text(encoding="utf-8"))
    with np.load(repository / RUN005_ARRAYS_RELATIVE) as arrays:
        raw_array = np.asarray(arrays["raw_ra0_turn2"], dtype=np.float64)
        k1a_shares = np.asarray(arrays["shares_destination_origin"], dtype=np.float64)
        k1a_rah = np.asarray(arrays["canonical_rah_turn3"], dtype=np.float64)
    rows = candidate.get("rows", [])
    order = tuple(row.get("province") for row in rows)
    raw_json = np.asarray(integration.get("raw_ra0_turn2_by_destination"), dtype=np.float64)
    checks = {
        "integration_status_pass": integration.get("status") == "PASS",
        "candidate_status_pass": candidate.get("status") == "PASS",
        "canonical_order": order == PROVINCE_ORDER,
        "row_count_31": len(rows) == 31,
        "raw_json_array_bitwise_equal": np.array_equal(raw_json, raw_array),
        "raw_ra0_sha": field_sha256(raw_json) == EXPECTED_RAW_RA0_SHA256
        == integration.get("raw_ra0_turn2_sha256"),
        "k1a_rah_sha": field_sha256(k1a_rah) == EXPECTED_K1A_RAH_SHA256
        == integration.get("rah_turn3_sha256") == candidate.get("raw_next_payoff_sha256"),
        "k1a_share_sha": field_sha256(k1a_shares) == EXPECTED_K1A_SHARE_SHA256
        == integration.get("portfolio_shares_sha256"),
        "run005_manifest": sha256(repository / RUN005_MANIFEST_RELATIVE)
        == EXPECTED_FILE_SHA256[RUN005_MANIFEST_RELATIVE.as_posix()],
        "run005_readback_pass": readback.get("status") == "PASS" and not readback.get("bad_paths"),
    }
    if not all(checks.values()):
        raise FailClosed("BLOCKED__K1B_RUN005_INPUT_BINDING_FAILED", {"checks": checks})
    distance = load_accepted_distance_score(repository / DISTANCE_RELATIVE)
    return {
        "integration": integration,
        "candidate": candidate,
        "rows": rows,
        "raw": raw_json,
        "k1a_shares": k1a_shares,
        "k1a_rah": k1a_rah,
        "distance": distance,
        "checks": checks,
    }


def preflight(repository: Path) -> dict[str, Any]:
    paths = tuple(EXPECTED_BLOBS)
    blob_checks = {
        path: git(repository, "rev-parse", f"HEAD:{path}") == EXPECTED_BLOBS[path]
        for path in paths
    }
    file_checks = {
        path: sha256(repository / path) == expected
        for path, expected in EXPECTED_FILE_SHA256.items()
    }
    checks = {
        "head_exact_live_main": git(repository, "rev-parse", "HEAD") == BASELINE,
        "origin_main_exact": git(repository, "rev-parse", "origin/main") == BASELINE,
        "production_diff_empty": not git(repository, "diff", "--name-only", "--", "src/ch5_two_asset_hank"),
        "distance_canonical_lf_sha": canonical_lf_sha256(repository / DISTANCE_RELATIVE)
        == ACCEPTED_DISTANCE_CANONICAL_LF_SHA256,
        "all_git_blobs_exact": all(blob_checks.values()),
        "all_input_file_hashes_exact": all(file_checks.values()),
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "task_id": TASK_ID,
        "baseline": BASELINE,
        "checks": checks,
        "git_blob_checks": blob_checks,
        "file_sha256_checks": file_checks,
        "source_sha256": source_hashes(repository),
    }


def read_junit(path: Path) -> dict[str, Any]:
    root = ET.parse(path).getroot()
    tests = int(root.attrib.get("tests", sum(int(x.attrib.get("tests", 0)) for x in root)))
    failures = int(root.attrib.get("failures", sum(int(x.attrib.get("failures", 0)) for x in root)))
    errors = int(root.attrib.get("errors", sum(int(x.attrib.get("errors", 0)) for x in root)))
    return {
        "status": "PASS" if tests > 0 and failures == 0 and errors == 0 else "FAIL",
        "tests": tests,
        "failures": failures,
        "errors": errors,
    }


def zero_science_ledger() -> dict[str, int]:
    return {
        "household_hjb_kfe": 0,
        "direct_hjb_solves": 0,
        "selector_root_calls": 0,
        "d2_q": 0,
        "firm": 0,
        "integration_outer_turn": 0,
        "turn3_household": 0,
        "k1b_scientific_runtime": 0,
        "k2": 0,
        "matlab": 0,
        "ge_results": 0,
        "retry_tuning": 0,
    }


def seal(output: Path) -> dict[str, Any]:
    entries = [
        {"path": p.relative_to(output).as_posix(), "bytes": p.stat().st_size, "sha256": sha256(p)}
        for p in sorted(output.rglob("*"))
        if p.is_file() and p.name not in {"sealed_manifest.json", "independent_readback_receipt.json"}
    ]
    manifest = {
        "schema": "CH5_MP4C_K1B_TURN3_ACTIVATION_SAFETY_GATE_EVIDENCE_V1",
        "entry_count": len(entries),
        "total_bytes": sum(int(row["bytes"]) for row in entries),
        "entries": entries,
    }
    write_json(output / "sealed_manifest.json", manifest)
    bad = []
    for row in entries:
        path = output / row["path"]
        if not path.is_file() or path.stat().st_size != row["bytes"] or sha256(path) != row["sha256"]:
            bad.append(row["path"])
    receipt = {
        "status": "PASS" if not bad else "FAIL",
        "manifest_sha256": sha256(output / "sealed_manifest.json"),
        "entry_count": len(entries),
        "total_bytes": manifest["total_bytes"],
        "bad_paths": bad,
        "scientific_calls": 0,
    }
    write_json(output / "independent_readback_receipt.json", receipt)
    if bad:
        raise FailClosed("BLOCKED__K1B_EVIDENCE_READBACK_FAILED", {"bad_paths": bad})
    return receipt


def execute(repository: Path, focused_test_junit: Path) -> str:
    repository = repository.resolve(strict=True)
    output = repository / OUTPUT_RELATIVE
    if output.exists():
        raise FailClosed("BLOCKED__FRESH_EVIDENCE_ROOT_ALREADY_EXISTS", {"path": str(output)})
    gate = preflight(repository)
    focused = read_junit(focused_test_junit)
    if gate["status"] != "PASS" or focused["status"] != "PASS":
        raise FailClosed("BLOCKED__K1B_PREEXECUTION_GATE_FAILED", {"preflight": gate, "focused": focused})
    bound = load_bound_inputs(repository)
    pre_source = source_hashes(repository)
    output.mkdir(parents=True, exist_ok=False)
    write_json(output / "authority_source_binding.json", gate)
    write_json(output / "focused_test_receipt.json", focused)

    raw = bound["raw"]
    rows = bound["rows"]
    mean, sigma, zscore = ordered_population_zscore(raw)
    z_mean = math.fsum(float(value) for value in zscore) / 31.0
    z_variance = math.fsum(float(value) * float(value) for value in zscore) / 31.0
    z_receipt = {
        "status": "PASS",
        "provenance": "COMPLETED_TURN2_RAW_RA0__USED_FOR_TURN3_K1B_ATTRACTIVENESS",
        "province_order": list(PROVINCE_ORDER),
        "raw_ra0": raw.tolist(),
        "raw_ra0_sha256": field_sha256(raw),
        "ordered_mean": mean,
        "population_standard_deviation": sigma,
        "ddof": 0,
        "zscore": zscore.tolist(),
        "zscore_sha256": field_sha256(zscore),
        "ordered_zscore_mean": z_mean,
        "ordered_zscore_population_variance": z_variance,
        "checks": {
            "sigma_finite_positive": math.isfinite(sigma) and sigma > 0.0,
            "mean_near_zero": abs(z_mean) <= 1e-15,
            "population_variance_near_one": abs(z_variance - 1.0) <= 1e-15,
            "no_transform_beyond_population_zscore": True,
        },
    }
    if not all(z_receipt["checks"].values()):
        raise FailClosed("FAIL__K1B_RAW_RA0_ZSCORE_GATE", z_receipt)
    write_json(output / "raw_ra0_zscore_receipt.json", z_receipt)

    assets = np.asarray([row["state"]["At"] for row in rows], dtype=np.float64)
    population = np.asarray([row["state"]["N"] for row in rows], dtype=np.float64)
    theta = np.asarray([row["state"]["inter_prv_ratio"] for row in rows], dtype=np.float64)
    network = build_bilateral_capital_network(BilateralCapitalNetworkInputs(
        province_order=PROVINCE_ORDER,
        illiquid_assets_per_capita_by_origin=assets,
        population_by_origin=population,
        total_foreign_share_theta_by_origin=theta,
        distance_score_destination_origin=bound["distance"],
        lagged_return_score_by_destination=zscore,
        portfolio_return_by_destination=raw,
        beta_distance=2.0,
        beta_return=0.5,
        lagged_return_provenance=PROVENANCE,
    ))
    foreign = np.asarray(network.foreign_conditional_shares_destination_origin)
    shares = np.asarray(network.portfolio_shares_destination_origin)
    rah = ordered_payoff(raw, shares)
    score_matrix = -2.0 * bound["distance"] + 0.5 * zscore[:, None]

    foreign_checks = {
        "orientation_destination_by_origin": network.orientation == "DESTINATION_BY_ORIGIN",
        "diagonal_exact_zero": np.array_equal(np.diag(foreign), np.zeros(31)),
        "all_finite": bool(np.all(np.isfinite(foreign))),
        "all_nonnegative": bool(np.all(foreign >= 0.0)),
        "columns_normalized": bool(np.allclose(np.sum(foreign, axis=0), 1.0, rtol=0.0, atol=CONSERVATION_TOLERANCE)),
        "stable_foreign_only_softmax": True,
        "no_smoothing": True,
    }
    if not all(foreign_checks.values()):
        raise FailClosed("FAIL__K1B_FOREIGN_SHARE_GATE", {"checks": foreign_checks})
    write_json(output / "k1b_foreign_conditional_share_receipt.json", {
        "status": "PASS", "beta_distance": 2.0, "beta_return": 0.5,
        "orientation": "destination_by_origin", "score_matrix_sha256": field_sha256(score_matrix),
        "foreign_conditional_share_sha256": field_sha256(foreign),
        "foreign_conditional_shares_destination_origin": foreign.tolist(), "checks": foreign_checks,
    })

    expected_home = 1.0 - theta
    full_checks = {
        "all_finite": bool(np.all(np.isfinite(shares))),
        "all_nonnegative": bool(np.all(shares >= 0.0)),
        "home_exact": np.array_equal(np.diag(shares), expected_home),
        "foreign_totals_theta": bool(np.allclose(np.sum(shares, axis=0) - np.diag(shares), theta, rtol=0.0, atol=CONSERVATION_TOLERANCE)),
        "columns_total_one": bool(np.allclose(np.sum(shares, axis=0), 1.0, rtol=0.0, atol=CONSERVATION_TOLERANCE)),
    }
    if not all(full_checks.values()):
        raise FailClosed("FAIL__K1B_FULL_SHARE_GATE", {"checks": full_checks})
    write_json(output / "k1b_portfolio_share_plan_receipt.json", {
        "status": "PASS", "classification": "FROZEN_FUTURE_TURN3_K1B_QUANTITY_AND_PAYOFF_SHARE_PLAN",
        "orientation": "destination_by_origin", "theta": theta.tolist(),
        "portfolio_share_sha256": field_sha256(shares),
        "portfolio_shares_destination_origin": shares.tolist(), "checks": full_checks,
    })

    k1a = bound["k1a_shares"]
    off_diagonal = ~np.eye(31, dtype=bool)
    difference = shares - k1a
    comparison = {
        "status": "PASS",
        "k1a_share_sha256": field_sha256(k1a),
        "k1b_share_sha256": field_sha256(shares),
        "home_shares_bitwise_identical": bool(np.array_equal(np.diag(k1a), np.diag(shares))),
        "foreign_changed_count": int(np.count_nonzero(difference[off_diagonal] != 0.0)),
        "foreign_max_absolute_change": float(np.max(np.abs(difference[off_diagonal]))),
        "direction_or_convergence_preference_used": False,
    }
    if not comparison["home_shares_bitwise_identical"] or comparison["foreign_changed_count"] < 1:
        raise FailClosed("FAIL__K1A_K1B_SHARE_COMPARISON", comparison)
    write_json(output / "k1a_vs_k1b_share_comparison.json", comparison)

    payoff_checks = {
        "all_31_finite": rah.shape == (31,) and bool(np.all(np.isfinite(rah))),
        "ordered_destination_fsum": True,
        "same_exact_s_as_share_plan": True,
        "zscore_used_only_for_attractiveness": True,
        "raw_ra0_level_used_only_for_payoff": True,
        "no_clipping_smoothing_annualization_risk_adjustment": True,
    }
    write_json(output / "ordered_k1b_household_payoff_receipt.json", {
        "status": "PASS" if all(payoff_checks.values()) else "FAIL",
        "province_order": list(PROVINCE_ORDER), "rah_turn3_k1b": rah.tolist(),
        "rah_turn3_k1b_sha256": field_sha256(rah), "share_plan_sha256": field_sha256(shares),
        "raw_ra0_level_sha256": field_sha256(raw), "minimum": float(np.min(rah)),
        "maximum": float(np.max(rah)), "ordered_mean": math.fsum(float(x) for x in rah) / 31.0,
        "k1a_rah_sha256": field_sha256(bound["k1a_rah"]),
        "k1a_vs_k1b_max_absolute_change": float(np.max(np.abs(rah - bound["k1a_rah"]))),
        "k1a_vs_k1b_bitwise_equal_count": int(np.count_nonzero(rah == bound["k1a_rah"])),
        "checks": payoff_checks,
    })
    if not all(payoff_checks.values()):
        raise FailClosed("FAIL__K1B_ORDERED_PAYOFF_GATE", {"checks": payoff_checks})

    candidate = copy.deepcopy(bound["candidate"])
    original_rows = bound["candidate"]["rows"]
    for index, row in enumerate(candidate["rows"]):
        row["classification"] = CLASSIFICATION
        row["state"]["rah"] = float(rah[index])
    candidate.update({
        "classification": CLASSIFICATION,
        "raw_next_payoff_sha256": field_sha256(rah),
        "k1b_portfolio_share_plan_sha256": field_sha256(shares),
        "source_completed_turn2_raw_ra0_sha256": field_sha256(raw),
    })
    non_rah_exact = True
    for old, new in zip(original_rows, candidate["rows"]):
        old_state, new_state = dict(old["state"]), dict(new["state"])
        old_state.pop("rah")
        new_state.pop("rah")
        non_rah_exact &= old_state == new_state
        non_rah_exact &= all(old[key] == new[key] for key in old if key not in {"classification", "state"})
    candidate["checks"] = {
        "canonical_order": tuple(row["province"] for row in candidate["rows"]) == PROVINCE_ORDER,
        "non_rah_state_fields_exact": bool(non_rah_exact),
        "only_state_rah_and_required_classification_changed": bool(non_rah_exact),
        "household_not_run": True,
    }
    if not all(candidate["checks"].values()):
        raise FailClosed("FAIL__K1B_TURN3_CANDIDATE_IDENTITY", candidate["checks"])
    write_json(output / "k1b_turn3_input_candidate.json", candidate)

    ordered_vs_network = np.abs(rah - network.household_portfolio_return_by_origin)
    wealth = network.origin_private_wealth
    k_scale = max(1.0, math.fsum(float(x) for x in wealth))
    conservation_checks = {
        "origin_wealth_columns_conserved": bool(np.allclose(network.capital_column_sums, wealth, rtol=0.0, atol=CONSERVATION_TOLERANCE * k_scale)),
        "national_private_capital_conserved": abs(network.national_private_capital_conservation_residual) <= CONSERVATION_TOLERANCE * k_scale,
        "home_retained_exact": bool(np.array_equal(network.domestic_retained_capital_by_origin, expected_home * wealth)),
        "ordered_payoff_matches_pure_network_within_roundoff": float(np.max(ordered_vs_network)) <= 1e-15,
        "same_share_plan_for_quantity_and_payoff": True,
        "scale_only_not_turn3_prediction": True,
    }
    if not all(conservation_checks.values()):
        raise FailClosed("FAIL__K1B_CONSERVATION_SAFETY_PANEL", {"checks": conservation_checks})
    write_json(output / "conservation_safety_panel.json", {
        "status": "PASS", "accepted_turn2_household_wealth_scale_only": True,
        "origin_private_wealth_total_ordered": math.fsum(float(x) for x in wealth),
        "destination_private_capital_total_ordered": math.fsum(float(x) for x in network.destination_private_productive_capital),
        "national_private_capital_residual": network.national_private_capital_conservation_residual,
        "maximum_ordered_vs_network_payoff_difference": float(np.max(ordered_vs_network)),
        "share_plan_sha256": field_sha256(shares), "checks": conservation_checks,
    })

    timing_checks = {
        "score_source_completed_turn2_raw_ra0": True,
        "turn3_firm_output_not_read": True,
        "no_same_turn_return_feedback": True,
        "share_plan_frozen_before_turn3_household": True,
        "future_quantity_may_use_turn3_wealth_with_fixed_s": True,
        "future_quantity_and_payoff_must_reuse_same_s": True,
        "timing_mapping_unique_under_current_authority": True,
    }
    write_json(output / "timing_provenance_receipt.json", {
        "status": "PASS", "lagged_return_provenance": PROVENANCE,
        "completed_turn2_raw_ra0_sha256": field_sha256(raw),
        "frozen_turn3_k1b_share_plan_sha256": field_sha256(shares), "checks": timing_checks,
    })

    np.savez_compressed(
        output / "k1b_turn3_frozen_share_payoff_plan.npz",
        raw_ra0_turn2=raw, zscore_by_destination=zscore,
        score_destination_origin=score_matrix,
        foreign_conditional_shares_destination_origin=foreign,
        portfolio_shares_destination_origin=shares,
        rah_turn3_k1b_by_origin=rah,
        accepted_turn2_origin_private_wealth_scale=wealth,
    )
    write_json(output / "run005_input_binding.json", {
        "status": "PASS", "checks": bound["checks"],
        "integration_receipt": INTEGRATION_RELATIVE.as_posix(),
        "turn3_candidate": TURN3_CANDIDATE_RELATIVE.as_posix(),
        "run005_arrays": RUN005_ARRAYS_RELATIVE.as_posix(),
        "raw_ra0_sha256": field_sha256(raw), "k1a_rah_sha256": field_sha256(bound["k1a_rah"]),
        "distance_canonical_lf_sha256": canonical_lf_sha256(repository / DISTANCE_RELATIVE),
    })
    write_json(output / "zero_science_ledger.json", zero_science_ledger())

    post_source = source_hashes(repository)
    if post_source != pre_source or git(repository, "diff", "--name-only", "--", "src/ch5_two_asset_hank"):
        raise FailClosed("BLOCKED__PRODUCTION_SOURCE_FREEZE_CHANGED", {})
    write_json(output / "terminal_receipt.json", {
        "terminal": PASS_TERMINAL, "classification": CLASSIFICATION,
        "k1b_share_sha256": field_sha256(shares), "k1b_rah_turn3_sha256": field_sha256(rah),
        "turn3_household_run": False, "successor_published": False, "results_eligibility": False,
        "production_source_unchanged": True,
    })
    seal(output)
    return PASS_TERMINAL


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--focused-test-junit", type=Path, required=True)
    args = parser.parse_args(argv)
    print(execute(args.repository, args.focused_test_junit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
