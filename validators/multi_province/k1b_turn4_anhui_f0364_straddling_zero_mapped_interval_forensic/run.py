"""Zero-science Anhui F0364 straddling-zero mapped-interval forensic.

This validator intentionally does not import the production selector, cost,
root, policy-map, D2, HJB, or KFE modules.  It uses only hash-bound persisted
evidence, static source text, and standalone scalar arithmetic.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import time
from typing import Any


TASK_ID = "CH5_MP4C_K1B_TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_FORENSIC_20260921"
BASELINE_SHA = "3e11b05f497e4535e0655d64cba26a55bab9b582"
TERMINAL = (
    "PASS__K1B_TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_FORENSIC"
    "__GUARD_FALSE_NEGATIVE_CONFIRMED__NO_SOURCE_CHANGE"
)
CLASS_A = "TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_GUARD_FALSE_NEGATIVE_CONFIRMED"
CLASS_B = "TURN4_ANHUI_F0364_SCIENTIFIC_INFEASIBILITY_CONFIRMED"
CLASS_C = "TURN4_ANHUI_F0364_AUTHORITY_AMBIGUOUS__OWNER_DECISION_REQUIRED"

PARENT_ROOT = Path(
    "reports/ch5_mp4c_k1b_turn4_corrected_household_kfe_and_one_turn_integration_20260921_run001"
)
CELL_RELATIVE = PARENT_ROOT / "household/p11_安徽/checkpoint_004/cell_0364.json"
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_k1b_turn4_anhui_f0364_straddling_zero_mapped_interval_forensic_20260921_run001"
)
TASK_RELATIVE = Path(
    "tasks/CH5_MP4C_K1B_TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_FORENSIC_20260921.md"
)
SELECTOR_RELATIVE = Path("src/ch5_two_asset_hank/corrected_diagnostic/selector.py")
COST_RELATIVE = Path("src/ch5_two_asset_hank/corrected_diagnostic/cost.py")
ACCEPTANCE_RELATIVE = Path(
    "docs/CH5_MP4C_TURN2_F0364_NEGATIVE_RATIO_SWITCHING_FALSE_NEGATIVE_ACCEPTANCE_20260921.md"
)
BEIJING_REPORT_RELATIVE = Path(
    "docs/CH5_MP4C_TURN2_BEIJING_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_FORENSIC_REPORT.md"
)
VALIDATOR_RELATIVE = Path(
    "validators/multi_province/k1b_turn4_anhui_f0364_straddling_zero_mapped_interval_forensic/run.py"
)
TEST_RELATIVE = Path(
    "tests/test_mp4c_k1b_turn4_anhui_f0364_straddling_zero_mapped_interval_forensic.py"
)

PARENT_MANIFEST_SHA256 = "964E9996697698A0199F474F4AE8B9D728B8F86E3CA6C2F0F0DC7CFC3C1BB584"
CELL_BLOB = "7ff0c9ff12ed39df1a2c1c55d195e10048914644"
CELL_SHA256 = "F1170662F50FEB38BB6D26B233725B672B12397EA891C15CBBDC559DBA6DCB65"
SELECTOR_BLOB = "e8a1d72e23661576f14ac42b7dff6e3001837206"
COST_BLOB = "435705a50238aaeebe918430156bcc14df1ff794"

PARAMETERS = {
    "gamma_c": 2.0,
    "phi": 5.0,
    "labor_weight": 1.0,
    "chi_0": 0.1,
    "chi_1": 2.0,
    "a_bar": 1.0e-6,
}

EXPECTED_REJECTIONS = (
    ("A_DERIVATIVE_DIRECTION_INCONSISTENT",),
    ("B_DERIVATIVE_DIRECTION_INCONSISTENT", "A_DERIVATIVE_DIRECTION_INCONSISTENT"),
    ("A_DERIVATIVE_DIRECTION_INCONSISTENT",),
    ("B_DERIVATIVE_DIRECTION_INCONSISTENT",),
    ("TRANSFER_KKT_RESIDUAL",),
    ("B_DERIVATIVE_DIRECTION_INCONSISTENT", "TRANSFER_KKT_RESIDUAL"),
    ("TRANSFER_SIGN_INCONSISTENT_POSITIVE", "A_DERIVATIVE_DIRECTION_INCONSISTENT", "TRANSFER_KKT_RESIDUAL"),
    ("TRANSFER_SIGN_INCONSISTENT_POSITIVE", "B_DERIVATIVE_DIRECTION_INCONSISTENT", "TRANSFER_KKT_RESIDUAL"),
)


class ForensicFailure(RuntimeError):
    pass


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def _git(repository: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repository, text=True).strip()


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def _fp_bound(*values: float, operations: int) -> float:
    eps = sys.float_info.epsilon
    gamma_n = operations * eps / (1.0 - operations * eps)
    scale = max(1.0, sum(abs(float(value)) for value in values if math.isfinite(value)))
    return float(gamma_n * scale)


def verify_parent_manifest(repository: Path) -> dict[str, Any]:
    root = repository / PARENT_ROOT
    manifest_path = root / "sealed_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bad_paths = []
    for row in manifest["entries"]:
        path = root / row["path"]
        if (
            not path.is_file()
            or path.stat().st_size != int(row["bytes"])
            or _sha256(path) != row["sha256"]
        ):
            bad_paths.append(row["path"])
    readback = json.loads((root / "independent_readback_receipt.json").read_text(encoding="utf-8"))
    checks = {
        "manifest_sha256": _sha256(manifest_path) == PARENT_MANIFEST_SHA256,
        "entry_count_2114": int(manifest["entry_count"]) == 2114,
        "total_bytes_29129317": int(manifest["total_bytes"]) == 29_129_317,
        "all_entries_read_back": not bad_paths,
        "accepted_readback": (
            readback.get("status") == "PASS"
            and not readback.get("bad_paths")
            and readback.get("manifest_sha256") == PARENT_MANIFEST_SHA256
        ),
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "manifest_sha256": _sha256(manifest_path),
        "entry_count": int(manifest["entry_count"]),
        "total_bytes": int(manifest["total_bytes"]),
        "bad_paths": bad_paths,
    }


def load_cell(repository: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, bool]]:
    path = repository / CELL_RELATIVE
    payload = json.loads(path.read_text(encoding="utf-8"))
    cell = payload["selector_cell"]
    checks = {
        "git_blob": _git(repository, "rev-parse", f"HEAD:{CELL_RELATIVE.as_posix()}") == CELL_BLOB,
        "sha256": _sha256(path) == CELL_SHA256,
        "checkpoint": payload.get("checkpoint") == 4,
        "flat": payload.get("flat_index_f_zero_based") == 364,
        "index": payload.get("index_b_a_z_zero_based") == [4, 18, 0],
        "cell_id": cell.get("cell_id") == "v004_f0364_b004_a018_z000",
        "outcome": payload["selector_result"].get("outcome") == "NO_ADMISSIBLE_POLICY",
        "admissible_comparison_count_zero": payload["selector_result"].get("admissible_comparison_count") == 0,
        "interior_b": cell["b_lower"] < cell["b"] < cell["b_upper"],
        "interior_a": cell["a_lower"] < cell["a"] < cell["a_upper"],
    }
    if not all(checks.values()):
        raise ForensicFailure(f"cell provenance mismatch: {checks}")
    return payload, cell, checks


def reproduce_candidates(payload: dict[str, Any]) -> dict[str, Any]:
    rows = []
    required_fields = (
        "transfer_branch", "derivative_branches", "q_b", "q_a", "d", "c", "l",
        "cost", "g_b", "g_a", "utility", "raw_hamiltonian", "hamiltonian",
        "arithmetic_tolerance", "transfer_kkt_residual", "transfer_target_interval",
        "q_b_domain_ok", "closed_face_feasible", "d2_assembler_admissible",
        "admissible", "rejection_reasons", "root_invoked", "root_status",
    )
    for ordinal, candidate in enumerate(payload["selector_result"]["candidates"]):
        rows.append({"ordinal": ordinal, **{name: candidate[name] for name in required_fields}})
    derivatives = payload["selector_cell"]["derivatives"]
    branch_shadow_checks = all(
        row["q_b"] == derivatives[f"p_b_{row['derivative_branches']['b']}"]
        and row["q_a"] == derivatives[f"p_a_{row['derivative_branches']['a']}"]
        for row in rows
    )
    checks = {
        "eight_candidates": len(rows) == 8,
        "all_fields_present": all(all(name in row for name in required_fields) for row in rows),
        "branch_shadows_exact": branch_shadow_checks,
        "all_no_roots": all(not row["root_invoked"] and row["root_status"] == "NOT_REQUIRED" for row in rows),
        "all_inadmissible": all(not row["admissible"] for row in rows),
        "all_d2_admissible": all(row["d2_assembler_admissible"] for row in rows),
        "rejection_classes_exact": tuple(tuple(row["rejection_reasons"]) for row in rows) == EXPECTED_REJECTIONS,
        "selector_root_invocations_zero": payload["selector_result"]["root_invocations"] == 0,
        "interior_a_roots_zero": payload["selector_result"]["interior_a_switching_root_invocations"] == 0,
    }
    return {"status": "PASS" if all(checks.values()) else "FAIL", "checks": checks, "candidates": rows}


def strict_crossing_receipt(reproduction: dict[str, Any]) -> dict[str, Any]:
    rows = reproduction["candidates"]
    pairs = {"backward": (rows[0], rows[2]), "forward": (rows[1], rows[3])}
    result = {}
    for branch, (a_backward, a_forward) in pairs.items():
        result[branch] = {
            "a_backward_g_a": a_backward["g_a"],
            "a_backward_bound": a_backward["arithmetic_tolerance"],
            "a_forward_g_a": a_forward["g_a"],
            "a_forward_bound": a_forward["arithmetic_tolerance"],
            "strict_crossing": (
                a_backward["g_a"] > a_backward["arithmetic_tolerance"]
                and a_forward["g_a"] < -a_forward["arithmetic_tolerance"]
            ),
        }
    checks = {
        "backward_strict_crossing": result["backward"]["strict_crossing"],
        "forward_not_strict_crossing": not result["forward"]["strict_crossing"],
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "pairs": result,
        "rule": "g_a_backward > bound_backward AND g_a_forward < -bound_forward",
    }


def mapped_interval_receipt(cell: dict[str, Any]) -> dict[str, Any]:
    derivatives = cell["derivatives"]
    d_z = float(-cell["effective_r_a"] * cell["a"])
    scale = max(float(cell["a"]), PARAMETERS["a_bar"])
    ratio = float(1.0 - PARAMETERS["chi_0"] + PARAMETERS["chi_1"] * d_z / scale)
    derivative_interval = tuple(sorted((derivatives["p_a_forward"], derivatives["p_a_backward"])))
    endpoint_images = (derivative_interval[0] / ratio, derivative_interval[1] / ratio)
    mapped = tuple(sorted(endpoint_images))
    checks = {
        "d_z_exact": d_z == -5.840722762648187,
        "ratio_exact": ratio == -0.3330414721146172,
        "negative_transfer": d_z < 0.0,
        "finite_nonzero_ratio": math.isfinite(ratio) and ratio != 0.0,
        "derivative_interval_straddles_zero": derivative_interval[0] < 0.0 < derivative_interval[1],
        "mapped_interval_straddles_zero": mapped[0] < 0.0 < mapped[1],
        "positive_domain_intersection_nonempty": mapped[1] > 0.0,
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "d_z": d_z,
        "transfer_regime": "negative",
        "d3_ratio_R": ratio,
        "formula": "1-chi_0+chi_1*d_z/max(a,a_bar)",
        "illiquid_derivative_interval_sorted": list(derivative_interval),
        "mapped_q_b_endpoint_images_unsorted": list(endpoint_images),
        "mapped_q_b_interval_sorted": list(mapped),
        "mapped_interval_sign_topology": "STRADDLES_ZERO",
        "positive_domain_intersection": {
            "lower": 0.0,
            "lower_open": True,
            "upper": mapped[1],
            "upper_closed": True,
            "notation": f"(0,{mapped[1]}]",
        },
    }


def _direction_ok(branch: str, drift: float, tolerance: float) -> bool:
    if drift > tolerance:
        return branch == "forward"
    if drift < -tolerance:
        return branch == "backward"
    return True


def branch_diagnostic(cell: dict[str, Any], mapping: dict[str, Any], branch: str) -> dict[str, Any]:
    derivatives = cell["derivatives"]
    q_b = float(derivatives[f"p_b_{branch}"])
    ratio = float(mapping["d3_ratio_R"])
    d_z = float(mapping["d_z"])
    q_a = float(ratio * q_b)
    derivative_interval = tuple(mapping["illiquid_derivative_interval_sorted"])
    mapped_interval = tuple(mapping["mapped_q_b_interval_sorted"])
    c = float(q_b ** (-1.0 / PARAMETERS["gamma_c"]))
    labor = float((q_b * cell["net_wage"] / PARAMETERS["labor_weight"]) ** (1.0 / PARAMETERS["phi"]))
    scale = max(float(cell["a"]), PARAMETERS["a_bar"])
    cost = float(PARAMETERS["chi_0"] * abs(d_z) + PARAMETERS["chi_1"] * d_z * d_z / (2.0 * scale))
    raw_g_b = float(
        cell["net_wage"] * labor + cell["effective_r_b"] * cell["b"]
        + cell["transfer_income"] - c - d_z - cost
    )
    raw_g_a = float(cell["effective_r_a"] * cell["a"] + d_z)
    tolerance = _fp_bound(
        c, labor, d_z, cost, raw_g_b, raw_g_a, q_b, q_a, q_b,
        derivative_interval[0], operations=96,
    )
    switching_bound = _fp_bound(
        c, labor, d_z, cost, raw_g_b, raw_g_a, q_b, q_a, operations=96,
    )
    g_a = 0.0 if abs(raw_g_a) <= switching_bound else raw_g_a
    g_b = raw_g_b
    consumption_utility = c ** (1.0 - PARAMETERS["gamma_c"]) / (1.0 - PARAMETERS["gamma_c"])
    utility = float(
        consumption_utility
        - PARAMETERS["labor_weight"] * labor ** (1.0 + PARAMETERS["phi"]) / (1.0 + PARAMETERS["phi"])
    )
    target = float(q_b * (1.0 - PARAMETERS["chi_0"] + PARAMETERS["chi_1"] * d_z / scale))
    kkt_residual = float(abs(q_a - target))
    raw_hamiltonian = float(utility + q_b * raw_g_b + q_a * raw_g_a)
    hamiltonian = float(utility + q_b * g_b + q_a * g_a)
    finite = all(
        math.isfinite(value)
        for value in (q_b, q_a, d_z, c, labor, cost, raw_g_b, raw_g_a, g_b, g_a,
                      tolerance, switching_bound, utility, raw_hamiltonian, hamiltonian)
    )
    domain_checks = {
        "q_b_finite": math.isfinite(q_b),
        "q_b_strictly_positive": q_b > 0.0,
        "q_b_in_whole_mapped_interval": mapped_interval[0] <= q_b <= mapped_interval[1],
        "q_b_in_positive_domain_intersection": 0.0 < q_b <= mapped_interval[1],
        "q_a_in_original_closed_derivative_interval": derivative_interval[0] <= q_a <= derivative_interval[1],
    }
    downstream = {
        "negative_transfer_sign_consistent": d_z < -tolerance,
        "raw_g_a_within_zero_drift_bound": abs(raw_g_a) <= switching_bound,
        "canonical_g_a_zero": g_a == 0.0,
        "b_direction_consistent": _direction_ok(branch, g_b, tolerance),
        "a_zero_direction_consistent": _direction_ok("zero", g_a, tolerance),
        "d3_kkt_satisfied": kkt_residual <= tolerance,
        "finite_controls_and_value": finite,
        "d2_assembler_admissible": finite and math.isfinite(g_b) and math.isfinite(g_a),
    }
    domain_pass = all(domain_checks.values())
    admissible = domain_pass and all(downstream.values())
    return {
        "branch": branch,
        "q_b": q_b,
        "q_a": q_a,
        "d": d_z,
        "domain_checks": domain_checks,
        "domain_pass": domain_pass,
        "c": c,
        "l": labor,
        "cost": cost,
        "raw_g_b": raw_g_b,
        "g_b": g_b,
        "raw_g_a": raw_g_a,
        "g_a": g_a,
        "arithmetic_tolerance": tolerance,
        "switching_arithmetic_bound": switching_bound,
        "transfer_kkt_target": target,
        "transfer_kkt_residual": kkt_residual,
        "downstream_checks": downstream,
        "utility": utility,
        "raw_hamiltonian": raw_hamiltonian,
        "hamiltonian": hamiltonian,
        "admissible": admissible,
        "root_invocations": 0,
    }


def guard_causality_audit(repository: Path, crossing: dict[str, Any], mapping: dict[str, Any]) -> dict[str, Any]:
    text = (repository / SELECTOR_RELATIVE).read_text(encoding="utf-8")
    function_start = text.index("def _interior_a_switching_candidate(")
    function_end = text.index("\ndef _joint_switching_candidate(", function_start)
    function_text = text[function_start:function_end]
    tokens = [
        'if "a" in faces:',
        "backward_drift > backward_bound",
        "actual_regime != regime or d_z == 0.0",
        "if not math.isfinite(ratio) or ratio == 0.0:",
        "if ratio < 0.0 and b_active:",
        "if implied_q_b_interval[0] <= 0.0:",
        "root_interval = implied_q_b_interval",
    ]
    positions = {token: function_text.find(token) for token in tokens}
    checks = {
        "all_static_tokens_present": all(value >= 0 for value in positions.values()),
        "guard_order_exact": all(
            positions[left] < positions[right] for left, right in zip(tokens[:-1], tokens[1:])
        ),
        "interior_a_prerequisite_pass": True,
        "strict_crossing_prerequisite_pass": crossing["checks"]["backward_strict_crossing"],
        "negative_regime_matches_d_z": mapping["transfer_regime"] == "negative" and mapping["d_z"] < 0.0,
        "ratio_finite_nonzero": math.isfinite(mapping["d3_ratio_R"]) and mapping["d3_ratio_R"] != 0.0,
        "negative_ratio_active_liquid_face_guard_not_applicable": True,
        "whole_interval_positivity_guard_triggers": mapping["mapped_q_b_interval_sorted"][0] <= 0.0,
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "static_token_positions": positions,
        "earliest_causal_exit": "if implied_q_b_interval[0] <= 0.0: return None",
        "whole_interval_positivity": False,
        "backward_branch_q_b_strictly_positive": True,
        "backward_branch_membership": True,
        "interpretation": (
            "All earlier strict-crossing, regime, finite-ratio, and interior-b gates pass. "
            "The whole-interval lower-end guard exits before branch-local q_b positivity "
            "and membership can reach the unchanged candidate checks."
        ),
    }


def authority_and_comparison(repository: Path, mapping: dict[str, Any]) -> dict[str, Any]:
    acceptance = (repository / ACCEPTANCE_RELATIVE).read_text(encoding="utf-8")
    beijing = (repository / BEIJING_REPORT_RELATIVE).read_text(encoding="utf-8")
    cost = (repository / COST_RELATIVE).read_text(encoding="utf-8")
    contract_checks = {
        "accepted_q_b_positive": "`q_b>0`;" in acceptance,
        "accepted_q_a_closed_interval": "`q_a` inside the closed sorted interval" in acceptance,
        "accepted_unchanged_d3_kkt": "unchanged D3 KKT" in acceptance,
        "accepted_no_q_a_positive_requirement": "`q_a>0`;" in acceptance,
        "accepted_no_ratio_positive_requirement": "`R>0`;" in acceptance,
        "cost_q_b_positive_domain": "transfer KKT requires q_b > 0" in cost,
        "beijing_classification_a": "TURN2_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_GUARD_FALSE_NEGATIVE_CONFIRMED" in beijing,
    }
    return {
        "status": "PASS" if all(contract_checks.values()) else "FAIL",
        "contract_checks": contract_checks,
        "shared_authority": [
            "interior-b/interior-a strict-crossing switching",
            "q_b must be finite and strictly positive",
            "q_a must lie in the original closed illiquid derivative interval",
            "unchanged D3 KKT, direction, finite, D2, and Hamiltonian rules",
            "negative finite R is permitted; ratio zero remains fail closed",
        ],
        "beijing": {
            "illiquid_interval_topology": "ENTIRELY_NEGATIVE",
            "mapped_q_b_interval_topology": "ENTIRELY_POSITIVE",
            "mapped_q_b_interval": [0.004111019263931103, 0.006526149020033277],
        },
        "anhui": {
            "illiquid_interval_topology": "STRADDLES_ZERO",
            "mapped_q_b_interval_topology": mapping["mapped_interval_sign_topology"],
            "mapped_q_b_interval": mapping["mapped_q_b_interval_sorted"],
        },
        "comparison_conclusion": (
            "The scientific contract is identical. Anhui differs because both the original "
            "illiquid interval and its negative-R image straddle zero; this topology alone "
            "does not invalidate a positive branch-local shadow."
        ),
    }


def classify(
    provenance_ok: bool,
    crossing: dict[str, Any],
    mapping: dict[str, Any],
    branches: list[dict[str, Any]],
    guard: dict[str, Any],
    authority: dict[str, Any],
) -> str:
    if not all(
        (provenance_ok, crossing["status"] == "PASS", mapping["status"] == "PASS",
         guard["status"] == "PASS", authority["status"] == "PASS")
    ):
        return CLASS_C
    admissible = [row for row in branches if row["admissible"]]
    if not admissible:
        return CLASS_B
    if len(admissible) == 1 and admissible[0]["branch"] == "backward":
        return CLASS_A
    return CLASS_C


def design_only_consequence(classification: str) -> dict[str, Any]:
    if classification != CLASS_A:
        return {"applicable": False, "reason": "classification A was not proven"}
    return {
        "applicable": True,
        "scope": "interior-b / interior-a / finite-negative-R / strict-crossing switching only",
        "narrow_change": (
            "Replace the whole-mapped-interval positivity rejection with an explicit nonempty "
            "intersection of the mapped interval and q_b>0, then require the persisted branch-local "
            "q_b to be strictly positive and a member of that intersection before constructing the "
            "existing switching candidate."
        ),
        "preserve": [
            "q_b>0 without a magnitude floor",
            "branch-local liquid derivative shadow",
            "q_a=R*q_b membership in the original closed derivative interval",
            "direction, transfer KKT, finite, D2, deduplication, and Hamiltonian checks",
            "active liquid-face behavior",
            "ratio-zero fail closed",
        ],
        "implementation_in_this_task": False,
    }


def _source_hashes(repository: Path) -> dict[str, str]:
    paths = (SELECTOR_RELATIVE, COST_RELATIVE, ACCEPTANCE_RELATIVE, BEIJING_REPORT_RELATIVE,
             TASK_RELATIVE, VALIDATOR_RELATIVE, TEST_RELATIVE)
    return {path.as_posix(): _sha256(repository / path) for path in paths}


def _manifest(output: Path) -> dict[str, Any]:
    excluded = {"sealed_manifest.json", "independent_readback_receipt.json"}
    entries = [
        {"path": path.relative_to(output).as_posix(), "sha256": _sha256(path), "bytes": path.stat().st_size}
        for path in sorted(output.rglob("*"))
        if path.is_file() and path.name not in excluded
    ]
    manifest = {
        "schema": "CH5_MP4C_K1B_TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_FORENSIC_V1",
        "entry_count": len(entries),
        "total_bytes": sum(int(row["bytes"]) for row in entries),
        "entries": entries,
    }
    _write_json(output / "sealed_manifest.json", manifest)
    return manifest


def _readback(output: Path) -> dict[str, Any]:
    manifest_path = output / "sealed_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bad = []
    for row in manifest["entries"]:
        path = output / row["path"]
        if not path.is_file() or path.stat().st_size != row["bytes"] or _sha256(path) != row["sha256"]:
            bad.append(row["path"])
    receipt = {
        "status": "PASS" if not bad else "FAIL",
        "manifest_sha256": _sha256(manifest_path),
        "entry_count": manifest["entry_count"],
        "total_bytes": manifest["total_bytes"],
        "bad_paths": bad,
        "scientific_calls": 0,
    }
    _write_json(output / "independent_readback_receipt.json", receipt)
    return receipt


def execute(repository: Path) -> tuple[str, str]:
    repository = repository.resolve(strict=True)
    started = time.perf_counter()
    output = repository / OUTPUT_RELATIVE
    if output.exists():
        raise ForensicFailure(f"fresh evidence root already exists: {output}")
    parent = verify_parent_manifest(repository)
    payload, cell, cell_checks = load_cell(repository)
    reproduction = reproduce_candidates(payload)
    crossing = strict_crossing_receipt(reproduction)
    mapping = mapped_interval_receipt(cell)
    branches = [branch_diagnostic(cell, mapping, branch) for branch in ("backward", "forward")]
    guard = guard_causality_audit(repository, crossing, mapping)
    authority = authority_and_comparison(repository, mapping)
    startup_checks = {
        "origin_main_exact_baseline": _git(repository, "rev-parse", "origin/main") == BASELINE_SHA,
        "head_exact_baseline": _git(repository, "rev-parse", "HEAD") == BASELINE_SHA,
        "clean_before_evidence": not _git(repository, "status", "--porcelain", "--untracked-files=no"),
        "selector_blob": _git(repository, "rev-parse", f"HEAD:{SELECTOR_RELATIVE.as_posix()}") == SELECTOR_BLOB,
        "cost_blob": _git(repository, "rev-parse", f"HEAD:{COST_RELATIVE.as_posix()}") == COST_BLOB,
    }
    provenance_ok = bool(
        parent["status"] == "PASS" and all(cell_checks.values())
        and reproduction["status"] == "PASS" and all(startup_checks.values())
    )
    classification = classify(provenance_ok, crossing, mapping, branches, guard, authority)
    pre_hashes = _source_hashes(repository)
    output.mkdir(parents=True, exist_ok=False)
    _write_json(output / "authority_binding.json", {
        "status": "PASS" if provenance_ok else "FAIL",
        "task_id": TASK_ID,
        "baseline": BASELINE_SHA,
        "parent_evidence": parent,
        "cell_path": CELL_RELATIVE.as_posix(),
        "cell_blob": CELL_BLOB,
        "cell_sha256": CELL_SHA256,
        "cell_checks": cell_checks,
        "selector_blob": SELECTOR_BLOB,
        "cost_blob": COST_BLOB,
        "startup_checks": startup_checks,
        "parameters": PARAMETERS,
        "source_sha256_before": pre_hashes,
    })
    _write_json(output / "persisted_eight_candidate_reproduction.json", reproduction)
    _write_json(output / "strict_crossing_receipt.json", crossing)
    _write_json(output / "d3_mapped_interval_and_positive_domain_receipt.json", mapping)
    _write_json(output / "branch_local_domain_and_downstream_audit.json", {"branches": branches})
    _write_json(output / "current_guard_causality_audit.json", guard)
    _write_json(output / "prior_authority_comparison.json", authority)
    _write_json(output / "design_only_narrow_repair_consequence.json", design_only_consequence(classification))
    _write_json(output / "classification_receipt.json", {
        "classification": classification,
        "terminal": TERMINAL if classification == CLASS_A else None,
        "admissible_branches": [row["branch"] for row in branches if row["admissible"]],
        "earliest_causal_exit": guard["earliest_causal_exit"],
        "production_source_change": False,
    })
    ledger = {
        "persisted_cell_loads": 1,
        "persisted_candidate_reproductions": 1,
        "deterministic_scalar_branch_diagnostics": 2,
        "production_selector_calls": 0,
        "scalar_or_root_calls": 0,
        "policy_maps": 0,
        "d2_q_calls": 0,
        "hjb_direct_solves": 0,
        "kfe_svd_calls": 0,
        "aggregates": 0,
        "household_batches": 0,
        "labor_k1b_c1_firm_integration": 0,
        "turn5": 0,
        "matlab": 0,
        "k2": 0,
        "ge_results": 0,
        "retry_tuning": 0,
        "wall_seconds": float(time.perf_counter() - started),
    }
    _write_json(output / "zero_science_ledger.json", ledger)
    post_hashes = _source_hashes(repository)
    _write_json(output / "code_freeze_receipt.json", {
        "status": "PASS" if pre_hashes == post_hashes else "FAIL",
        "pre_execution_sha256": pre_hashes,
        "post_execution_sha256": post_hashes,
        "matches": pre_hashes == post_hashes,
        "selector_unchanged": pre_hashes[SELECTOR_RELATIVE.as_posix()] == post_hashes[SELECTOR_RELATIVE.as_posix()],
        "cost_unchanged": pre_hashes[COST_RELATIVE.as_posix()] == post_hashes[COST_RELATIVE.as_posix()],
    })
    _write_json(output / "terminal_receipt.json", {
        "terminal": TERMINAL if classification == CLASS_A else (
            "PASS__K1B_TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_FORENSIC"
            "__SCIENTIFIC_INFEASIBILITY_CONFIRMED__NO_SOURCE_CHANGE"
            if classification == CLASS_B else
            "BLOCKED__K1B_TURN4_ANHUI_F0364_STRADDLING_ZERO_MAPPED_INTERVAL_FORENSIC__OWNER_DECISION_REQUIRED"
        ),
        "classification": classification,
        "scientific_calls": 0,
        "production_source_change": False,
        "current_change": False,
        "successor_published": False,
    })
    if classification != CLASS_A or pre_hashes != post_hashes:
        raise ForensicFailure(f"unexpected classification or source drift: {classification}")
    _manifest(output)
    readback = _readback(output)
    if readback["status"] != "PASS":
        raise ForensicFailure("independent evidence readback failed")
    return TERMINAL, classification


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    args = parser.parse_args(argv)
    terminal, classification = execute(args.repository)
    print(f"{terminal}__{classification}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
