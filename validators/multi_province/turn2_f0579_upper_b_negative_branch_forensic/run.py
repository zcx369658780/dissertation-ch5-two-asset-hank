"""Bounded one-cell F0579 upper-b negative-transfer root forensic."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import time
from typing import Any, Callable

import numpy as np

from ch5_two_asset_hank.corrected_diagnostic.cost import check_transfer_kkt
from ch5_two_asset_hank.corrected_diagnostic.selector import (
    CellDerivatives,
    CorrectedSelectorCell,
    CorrectedSelectorParameters,
    SelectorBudget,
    _controls,
    _direction_ok,
    _fp_bound,
    _liquid_drift_for_root,
    _one_scalar_root,
    _transfer_from_regime,
    _transfer_ratio,
)


TASK_ID = "CH5_MP4C_TURN2_BEIJING_F0579_UPPER_B_NEGATIVE_BRANCH_ROOT_FORENSIC_20260920"
BASELINE_SHA = "5bc00486955100884005530bc6d7f05fd6acd5b0"
TERMINAL = "PASS__TURN2_BEIJING_F0579_UPPER_B_NEGATIVE_BRANCH_ROOT_FORENSIC_COMPLETE__NO_SELECTOR_CHANGE"
CLASS_A = "TURN2_F0579_UPPER_B_NEGATIVE_PRE_ROOT_UNIQUENESS_FALSE_NEGATIVE_CONFIRMED"
CLASS_B = "TURN2_F0579_TRUE_NO_ADMISSIBLE_POLICY_CONFIRMED"
CLASS_C = "TURN2_F0579_MULTIPLE_POST_ROOT_ADMISSIBLE_POLICIES_CONFIRMED__OWNER_DECISION_REQUIRED"
CLASS_D = "TURN2_F0579_FORENSIC_INCONSISTENT__NO_SELECTOR_DECISION"

RUN_ROOT = Path("reports/ch5_mp4c_corrected_optionb_turn2_unique_closed_class_kfe_20260920_run001")
CELL_RELATIVE = RUN_ROOT / "household/p00_北京/checkpoint_002/cell_0579.json"
OUTPUT_RELATIVE = Path("reports/ch5_mp4c_turn2_beijing_f0579_upper_b_negative_branch_forensic_20260920_run001")
TASK_RELATIVE = Path("tasks/CH5_MP4C_TURN2_BEIJING_F0579_UPPER_B_NEGATIVE_BRANCH_ROOT_FORENSIC_20260920.md")
SELECTOR_RELATIVE = Path("src/ch5_two_asset_hank/corrected_diagnostic/selector.py")
COST_RELATIVE = Path("src/ch5_two_asset_hank/corrected_diagnostic/cost.py")
TEST_RELATIVE = Path("tests/test_mp4c_turn2_f0579_upper_b_negative_branch_forensic.py")
VALIDATOR_RELATIVE = Path("validators/multi_province/turn2_f0579_upper_b_negative_branch_forensic/run.py")

MANIFEST_SHA256 = "50D2E87C94E762D3936C64E3AAD416F600118AEBB8DCE1588DB369938FA2351A"
CELL_BLOB = "799294deb8119e4581486d279bbf5704784588b2"
CELL_SHA256 = "290630D26A63F2BEF3FFF1C9C6EE014E95ED5B3B470A7A5EC0FC8F3129178700"
SELECTOR_BLOB = "7e13fb53138788ec71541316a9e9815b5eb7c1f4"
COST_BLOB = "435705a50238aaeebe918430156bcc14df1ff794"

EXPECTED = {
    "p_b_backward": 0.005058006084641677,
    "p_b_forward": 0.005058006084641677,
    "p_a_backward": -0.00014542975673859096,
    "p_a_forward": -0.0004814219651986697,
    "effective_r_a": 0.8815438210537105,
    "effective_r_b": 0.02,
    "net_wage": 21.428042860932116,
    "transfer_income": 0.1,
}
PARAMETERS = CorrectedSelectorParameters(2.0, 5.0, 1.0, 0.1, 2.0, 1.0e-6)


class ForensicFailure(RuntimeError):
    pass


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def _array_sha256(value: np.ndarray) -> str:
    array = np.ascontiguousarray(np.asarray(value, dtype="<f8"))
    return hashlib.sha256(array.tobytes(order="C")).hexdigest().upper()


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")


def _git(repository: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repository, text=True).strip()


def _blob(repository: Path, relative: Path) -> str:
    return _git(repository, "rev-parse", f"HEAD:{relative.as_posix()}")


def verify_manifest(repository: Path) -> dict[str, Any]:
    root = repository / RUN_ROOT
    manifest_path = root / "sealed_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bad = []
    for entry in manifest["entries"]:
        path = root / entry["path"]
        if not path.is_file() or path.stat().st_size != entry["bytes"] or _sha256(path) != entry["sha256"]:
            bad.append(entry["path"])
    readback = json.loads((root / "independent_readback_receipt.json").read_text(encoding="utf-8"))
    checks = {
        "manifest_sha256": _sha256(manifest_path) == MANIFEST_SHA256,
        "entry_count_612": manifest["entry_count"] == 612,
        "total_bytes_9677554": manifest["total_bytes"] == 9_677_554,
        "entries_read_back": not bad,
        "accepted_readback_pass": readback.get("status") == "PASS" and not readback.get("bad_paths"),
    }
    return {"status": "PASS" if all(checks.values()) else "FAIL", "checks": checks, "bad_paths": bad}


def load_cell(repository: Path) -> tuple[dict[str, Any], CorrectedSelectorCell]:
    path = repository / CELL_RELATIVE
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw = payload["selector_cell"]
    derivatives = raw["derivatives"]
    checks = {
        "blob": _blob(repository, CELL_RELATIVE) == CELL_BLOB,
        "sha256": _sha256(path) == CELL_SHA256,
        "checkpoint": payload.get("checkpoint") == 2,
        "flat": payload.get("flat_index_f_zero_based") == 579,
        "index": payload.get("index_b_a_z_zero_based") == [19, 8, 1],
        "cell_id": raw.get("cell_id") == "v002_f0579_b019_a008_z001",
        "outcome": payload["selector_result"].get("outcome") == "NO_ADMISSIBLE_POLICY",
        "persisted_values": all(float(derivatives.get(k, raw.get(k))) == v for k, v in EXPECTED.items()),
    }
    if not all(checks.values()):
        raise ForensicFailure(f"failure-cell provenance mismatch: {checks}")
    cell = CorrectedSelectorCell(
        cell_id=raw["cell_id"], b=raw["b"], a=raw["a"], z=raw["z"],
        b_lower=raw["b_lower"], b_upper=raw["b_upper"],
        a_lower=raw["a_lower"], a_upper=raw["a_upper"],
        net_wage=raw["net_wage"], effective_r_b=raw["effective_r_b"],
        transfer_income=raw["transfer_income"], effective_r_a=raw["effective_r_a"],
        derivatives=CellDerivatives(**derivatives),
    )
    return payload, cell


def reproduce_candidates(payload: dict[str, Any]) -> dict[str, Any]:
    candidates = payload["selector_result"]["candidates"]
    rows = [{
        "ordinal": i,
        "active_constraints": row["active_constraints"],
        "transfer_branch": row["transfer_branch"],
        "derivative_branches": row["derivative_branches"],
        "root_invoked": row["root_invoked"],
        "root_status": row["root_status"],
        "admissible": row["admissible"],
        "rejection_reasons": row["rejection_reasons"],
    } for i, row in enumerate(candidates)]
    checks = {
        "seven_persisted_candidates": len(rows) == 7,
        "all_inadmissible": all(not row["admissible"] for row in rows),
        "active_negative_pre_root": rows[4]["rejection_reasons"] == ["DERIVATIVE_BRANCH_NOT_UNIQUE_BEFORE_ROOT"],
        "active_zero_no_unique_bracket": rows[5]["root_status"] == "ROOT_FAILURE_NO_UNIQUE_BRACKET",
        "active_positive_sign_and_kkt": set(rows[6]["rejection_reasons"]) == {"TRANSFER_SIGN_INCONSISTENT_POSITIVE", "TRANSFER_KKT_RESIDUAL"},
        "inactive_reasons_preserved": all(rows[i]["rejection_reasons"] == candidates[i]["rejection_reasons"] for i in range(4)),
    }
    return {"status": "PASS" if all(checks.values()) else "FAIL", "checks": checks, "candidates": rows}


def _root_with_screen(
    branch: str,
    p_a: float,
    p_b: float,
    cell: CorrectedSelectorCell,
    budget: SelectorBudget,
) -> tuple[float | None, str, dict[str, Any]]:
    calls: list[tuple[float, float]] = []

    def function(q_b: float) -> float:
        d = _transfer_from_regime(regime="negative", q_a=p_a, q_b=q_b, a=cell.a, parameters=PARAMETERS)
        value = _liquid_drift_for_root(q_b, d, cell, PARAMETERS)
        calls.append((float(q_b), float(value)))
        return value

    root, status = _one_scalar_root(function, lower_b_face=False, p_b=p_b, budget=budget)
    screen = np.asarray(calls[:513], dtype=np.float64)
    if screen.shape != (513, 2):
        raise ForensicFailure(f"{branch} root screen did not persist 513 evaluations")
    exact = np.flatnonzero(screen[:, 1] == 0.0).tolist()
    brackets = [i for i in range(512) if (screen[i, 1] < 0.0 < screen[i+1, 1]) or (screen[i+1, 1] < 0.0 < screen[i, 1])]
    receipt = {
        "branch": branch,
        "domain": {"strict_lower": 0.0, "inclusive_upper": p_b},
        "screen_points": 513,
        "screen_sha256": _array_sha256(screen),
        "q_endpoint": [float(screen[0, 0]), float(screen[-1, 0])],
        "residual_endpoint": [float(screen[0, 1]), float(screen[-1, 1])],
        "minimum_residual": float(np.min(screen[:, 1])),
        "maximum_residual": float(np.max(screen[:, 1])),
        "exact_grid_indices": exact,
        "sign_change_left_indices": brackets,
        "bracket_count": len(brackets),
        "bracket": None if len(brackets) != 1 else [float(screen[brackets[0], 0]), float(screen[brackets[0]+1, 0])],
        "root_status": status,
        "root": root,
        "brent_solve": int(status == "ROOT_CONVERGED"),
        "total_function_evaluations": len(calls),
    }
    return root, status, receipt


def evaluate_post_root(branch: str, p_a: float, p_b: float, root: float | None, status: str, cell: CorrectedSelectorCell) -> dict[str, Any]:
    if root is None:
        return {"branch": branch, "root_status": status, "admissible": False, "rejection_reasons": [status]}
    q_b = float(root)
    q_a = float(p_a)
    d = _transfer_from_regime(regime="negative", q_a=q_a, q_b=q_b, a=cell.a, parameters=PARAMETERS)
    c, l, cost, raw_g_b, raw_g_a, utility = _controls(q_b, d, cell, PARAMETERS)
    tolerance = _fp_bound(c, l, d, cost, raw_g_b, raw_g_a, q_b, q_a, p_b, p_a, operations=96)
    g_b = 0.0 if abs(raw_g_b) <= tolerance else raw_g_b
    g_a = raw_g_a
    slack = -g_b
    multiplier = p_b - q_b
    complementarity = multiplier * slack
    kkt = check_transfer_kkt(d=d, a=cell.a, q_a=q_a, q_b=q_b, chi_0=PARAMETERS.chi_0, chi_1=PARAMETERS.chi_1, a_bar=PARAMETERS.a_bar, tolerance=tolerance)
    reasons: list[str] = []
    q_b_domain_ok = 0.0 < q_b <= p_b
    if not q_b_domain_ok:
        reasons.append("UPPER_B_Q_B_DOMAIN_INVALID")
    if d >= -tolerance:
        reasons.append("TRANSFER_SIGN_INCONSISTENT_NEGATIVE")
    if slack < -tolerance:
        reasons.append("upper_b_PRIMAL_INFEASIBLE")
    if abs(raw_g_b) > tolerance:
        reasons.append("upper_b_ACTIVE_EQUALITY_RESIDUAL")
    if multiplier < -tolerance:
        reasons.append("upper_b_NEGATIVE_MULTIPLIER")
    if abs(complementarity) > _fp_bound(multiplier, slack, operations=8):
        reasons.append("upper_b_COMPLEMENTARITY_RESIDUAL")
    b_direction = _direction_ok("backward", g_b, tolerance)
    a_direction = _direction_ok(branch, g_a, tolerance)
    if not b_direction:
        reasons.append("B_DERIVATIVE_DIRECTION_INCONSISTENT")
    if not a_direction:
        reasons.append("A_DERIVATIVE_DIRECTION_INCONSISTENT")
    if not kkt.satisfied:
        reasons.append("TRANSFER_KKT_RESIDUAL")
    raw_hamiltonian = utility + p_b * raw_g_b + p_a * raw_g_a
    hamiltonian = utility + p_b * g_b + p_a * g_a
    finite = all(math.isfinite(x) for x in (q_b, q_a, d, cost, c, l, raw_g_b, raw_g_a, g_b, g_a, slack, multiplier, complementarity, tolerance, raw_hamiltonian, hamiltonian))
    if not finite:
        reasons.append("NONFINITE_CANDIDATE")
    return {
        "branch": branch, "root_status": status, "q_b": q_b, "q_a": q_a,
        "d": d, "cost": cost, "c": c, "l": l, "raw_g_b": raw_g_b,
        "g_b": g_b, "g_a": g_a, "upper_b_slack": slack,
        "upper_b_multiplier": multiplier, "complementarity_residual": complementarity,
        "q_b_domain_ok": q_b_domain_ok,
        "active_equality_raw_residual": raw_g_b,
        "active_equality_within_arithmetic_bound": abs(raw_g_b) <= tolerance,
        "closed_face_feasible": slack >= -tolerance,
        "d2_assembler_admissible": slack >= 0.0 and math.isfinite(g_b) and math.isfinite(g_a),
        "b_derivative_direction_consistent": b_direction,
        "a_derivative_direction_consistent": a_direction,
        "transfer_sign_consistent": d < -tolerance,
        "transfer_kkt_satisfied": kkt.satisfied,
        "transfer_kkt_residual": kkt.residual,
        "transfer_target_interval": list(kkt.target_interval),
        "finite": finite, "arithmetic_tolerance": tolerance,
        "utility": utility, "raw_hamiltonian": raw_hamiltonian,
        "hamiltonian": hamiltonian, "rejection_reasons": reasons,
        "admissible": not reasons,
    }


def switching_prerequisite(cell: CorrectedSelectorCell, backward: dict[str, Any], forward: dict[str, Any], p_b: float) -> dict[str, Any]:
    strict_crossing = bool(
        backward.get("g_a") is not None and forward.get("g_a") is not None
        and backward["g_a"] > backward["arithmetic_tolerance"]
        and forward["g_a"] < -forward["arithmetic_tolerance"]
    )
    d_z = -cell.effective_r_a * cell.a
    ratio = _transfer_ratio(d_z, cell.a, PARAMETERS)
    derivative_interval = sorted((cell.derivatives.p_a_forward, cell.derivatives.p_a_backward))
    implied = [derivative_interval[0] / ratio, derivative_interval[1] / ratio]
    intersection = [max(implied[0], 0.0), min(implied[1], p_b)]
    intersection_nonempty = intersection[0] < intersection[1]
    prerequisite = strict_crossing and d_z < 0.0 and ratio > 0.0 and implied[0] > 0.0 and intersection_nonempty
    return {
        "d_z": d_z, "transfer_regime": "negative" if d_z < 0.0 else "other",
        "negative_transfer_ratio": ratio,
        "derivative_interval": derivative_interval,
        "implied_q_b_interval": implied,
        "upper_b_q_b_domain": {"strict_lower": 0.0, "inclusive_upper": p_b},
        "intersection": intersection, "intersection_nonempty": intersection_nonempty,
        "strict_drift_crossing": strict_crossing,
        "prerequisite_satisfied": prerequisite,
        "switching_root_invocations": 0,
        "reason": "PREREQUISITE_FALSE__NO_SWITCHING_ROOT" if not prerequisite else "PREREQUISITE_TRUE__SEPARATE_SWITCHING_ROOT_NOT_NEEDED_FOR_BRANCH_CLASSIFICATION",
    }


def classify(backward: dict[str, Any], forward: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    admissible = [row for row in (backward, forward) if row["admissible"]]
    policies: list[dict[str, Any]] = []
    for row in admissible:
        values = tuple(float(row[name]) for name in ("c", "l", "d", "cost", "g_b", "g_a"))
        duplicate = False
        for existing in policies:
            other = tuple(float(existing[name]) for name in ("c", "l", "d", "cost", "g_b", "g_a"))
            bound = _fp_bound(*(values + other), operations=128)
            if all(abs(a - b) <= bound for a, b in zip(values, other)):
                duplicate = True
                break
        if not duplicate:
            policies.append(row)
    comparison = {
        "admissible_branch_count": len(admissible),
        "distinct_admissible_policy_count": len(policies),
        "unique_selected": None,
        "hamiltonian_gap": None,
        "comparison_tolerance": None,
    }
    if not policies:
        return CLASS_B, comparison
    if len(policies) == 1:
        comparison["unique_selected"] = policies[0]["branch"]
        return CLASS_A, comparison
    ordered = sorted(policies, key=lambda row: row["hamiltonian"], reverse=True)
    tolerance = _fp_bound(ordered[0]["hamiltonian"], ordered[1]["hamiltonian"], operations=128)
    gap = ordered[0]["hamiltonian"] - ordered[1]["hamiltonian"]
    comparison.update({"hamiltonian_gap": gap, "comparison_tolerance": tolerance})
    if gap <= tolerance:
        return CLASS_C, comparison
    comparison["unique_selected"] = ordered[0]["branch"]
    return CLASS_A, comparison


def _manifest(output: Path) -> dict[str, Any]:
    excluded = {"sealed_manifest.json", "independent_readback_receipt.json"}
    entries = []
    for path in sorted(p for p in output.rglob("*") if p.is_file() and p.name not in excluded):
        entries.append({"path": path.relative_to(output).as_posix(), "sha256": _sha256(path), "bytes": path.stat().st_size})
    manifest = {"schema": "CH5_MP4C_TURN2_F0579_BRANCH_ROOT_FORENSIC_V1", "entries": entries, "entry_count": len(entries), "total_bytes": sum(row["bytes"] for row in entries)}
    _write_json(output / "sealed_manifest.json", manifest)
    return manifest


def _readback(output: Path) -> dict[str, Any]:
    manifest_path = output / "sealed_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bad = [row["path"] for row in manifest["entries"] if _sha256(output / row["path"]) != row["sha256"] or (output / row["path"]).stat().st_size != row["bytes"]]
    receipt = {"status": "PASS" if not bad else "FAIL", "manifest_sha256": _sha256(manifest_path), "entry_count": manifest["entry_count"], "total_bytes": manifest["total_bytes"], "bad_paths": bad, "scientific_calls": 0}
    _write_json(output / "independent_readback_receipt.json", receipt)
    return receipt


def execute(repository: Path) -> tuple[str, str]:
    repository = repository.resolve(strict=True)
    output = repository / OUTPUT_RELATIVE
    output.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    manifest = verify_manifest(repository)
    payload, cell = load_cell(repository)
    reproduction = reproduce_candidates(payload)
    authority = {
        "status": "PASS",
        "baseline": BASELINE_SHA,
        "head": _git(repository, "rev-parse", "HEAD"),
        "origin_main": _git(repository, "rev-parse", "origin/main"),
        "worktree_clean_before_execution": not _git(repository, "status", "--porcelain"),
        "run001_manifest": manifest,
        "cell_blob": _blob(repository, CELL_RELATIVE), "cell_sha256": _sha256(repository / CELL_RELATIVE),
        "selector_blob": _blob(repository, SELECTOR_RELATIVE), "cost_blob": _blob(repository, COST_RELATIVE),
        "parameters": PARAMETERS.__dict__,
    }
    checks = {
        "origin_main": authority["origin_main"] == BASELINE_SHA,
        "clean": authority["worktree_clean_before_execution"],
        "manifest": manifest["status"] == "PASS",
        "cell": authority["cell_blob"] == CELL_BLOB and authority["cell_sha256"] == CELL_SHA256,
        "selector": authority["selector_blob"] == SELECTOR_BLOB,
        "cost": authority["cost_blob"] == COST_BLOB,
        "reproduction": reproduction["status"] == "PASS",
    }
    authority["checks"] = checks
    if not all(checks.values()):
        raise ForensicFailure(f"authority gate failed: {checks}")
    _write_json(output / "authority_binding.json", authority)
    _write_json(output / "current_candidate_reproduction_receipt.json", reproduction)

    budget = SelectorBudget(max_selector_evaluations=0, max_root_invocations=2, max_interior_z_root_invocations=0, max_interior_a_switching_root_invocations=0, max_joint_switching_root_invocations=0)
    p_b = EXPECTED["p_b_backward"]
    receipts = {}
    posts = {}
    brent_solves = 0
    for branch in ("backward", "forward"):
        p_a = EXPECTED[f"p_a_{branch}"]
        root, status, receipt = _root_with_screen(branch, p_a, p_b, cell, budget)
        receipts[branch] = receipt
        posts[branch] = evaluate_post_root(branch, p_a, p_b, root, status, cell)
        brent_solves += receipt["brent_solve"]
        _write_json(output / f"{branch}_branch_root_screen_receipt.json", receipt)
        _write_json(output / f"{branch}_branch_post_root_receipt.json", posts[branch])
    switching = switching_prerequisite(cell, posts["backward"], posts["forward"], p_b)
    _write_json(output / "switching_prerequisite_receipt.json", switching)
    classification, comparison = classify(posts["backward"], posts["forward"])
    _write_json(output / "branch_post_root_admissibility_receipt.json", {"status": "PASS", "branches": posts, "hamiltonian_comparison": comparison})
    _write_json(output / "classification_receipt.json", {"terminal_marker": TERMINAL, "classification": classification, "hamiltonian_comparison": comparison})
    ledger = {
        "failure_cell_json_loads": 1,
        "scalar_branch_root_invocations": budget.root_invocations,
        "brent_solves": brent_solves,
        "interior_a_switching_roots": 0,
        "full_selector_calls": 0, "policy_maps": 0, "d2_q_assemblies": 0,
        "hjb_direct_solves": 0, "kfe_svd_calls": 0, "aggregate_integration_calls": 0,
        "scientific_retries": 0, "turn3_household_calls": 0,
        "wall_seconds": time.perf_counter() - started,
    }
    if budget.root_invocations != 2 or brent_solves > 2 or switching["switching_root_invocations"] != 0:
        raise ForensicFailure(f"scientific ledger breach: {ledger}")
    _write_json(output / "scientific_ledger.json", ledger)
    _write_json(output / "terminal_receipt.json", {"terminal_marker": TERMINAL, "classification": classification, "selector_changed": False, "hjb_rerun": False})
    _manifest(output)
    readback = _readback(output)
    if readback["status"] != "PASS":
        raise ForensicFailure("independent readback failed")
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
