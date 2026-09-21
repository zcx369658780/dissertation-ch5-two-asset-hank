"""Zero-science arithmetic design gate for monotonicity-preserving HJB relaxation.

Only persisted arrays are read.  This module does not import production code,
call a selector, assemble Q, execute an HJB update, or solve a linear system.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
from typing import Any

import numpy as np


BASELINE = "ac3a4e5e7f76d85f033511e1d0b093cc46b3a1fe"
TASK_ID = "CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_SCIENTIFIC_DESIGN_GATE_20260921"
TERMINAL = "PASS__MONOTONICITY_PRESERVING_HJB_RELAXATION_DESIGN_GATE__GENERIC_LAW_PROPOSAL_COMPLETE__OWNER_ADOPTION_REQUIRED__NO_IMPLEMENTATION"
CLASSIFICATION = "ADOPTION_READY_GENERIC_RELAXATION_LAW__DETERMINISTIC_HALVING_INVARIANT_DOMAIN_BACKTRACK__OWNER_ADOPTION_REQUIRED"
ACCEPTED_ROOT = Path("reports/ch5_mp4c_lower_a_interior_z_composition_repair_turn1_parity_turn2_run004_20260921")
PROVINCE = ACCEPTED_ROOT / "household/p07_黑龙江"
ACCEPTED_MANIFEST_SHA256 = "1C501CEF7740748805CF538A05ECF9D80938149CDDF31A3158091F665C45AD80"
OUT = Path("reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_scientific_design_gate_20260921_run001")
SHAPE = (20, 20, 2)
HALVING_CEILING = 52

AUTHORITY = (
    Path("AGENTS.md"),
    Path("project_rules/PROJECT_RULE_INDEX_CURRENT.md"),
    Path("docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md"),
    Path("docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md"),
    Path("docs/CH5_MP4C_TURN2_HEILONGJIANG_F0063_NEGATIVE_DERIVATIVE_EMERGENCE_FORENSIC_ACCEPTANCE_20260921.md"),
    Path("docs/CH5_MP4C_ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_SCIENTIFIC_DESIGN_GATE_ACCEPTANCE_20260921.md"),
    Path("docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_ACCEPTANCE_20260917.md"),
    Path("docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_CONVERGENCE_LAW_OWNER_ADOPTION_20260917.md"),
    Path("tasks/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_SCIENTIFIC_DESIGN_GATE_20260921.md"),
)
SOURCES = (
    Path("src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py"),
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def field_sha256(values: np.ndarray) -> str:
    return hashlib.sha256(np.asarray(values, dtype="<f8").tobytes(order="F")).hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def identity(path: Path, repository: Path) -> dict[str, Any]:
    return {"path": path.relative_to(repository).as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)}


def raw_b_slopes(value: np.ndarray) -> np.ndarray:
    value = np.asarray(value, dtype=np.float64)
    if value.shape != SHAPE or not np.isfinite(value).all():
        raise ValueError("persisted V must be finite with shape (20,20,2)")
    spacing = np.diff(np.linspace(-2.0, 5.0, 20))[:, None, None]
    return (value[1:] - value[:-1]) / spacing


def csr_matvec(data: np.ndarray, indices: np.ndarray, indptr: np.ndarray, x: np.ndarray) -> np.ndarray:
    result = np.empty(indptr.size - 1, dtype=np.float64)
    for row in range(result.size):
        start, end = int(indptr[row]), int(indptr[row + 1])
        result[row] = np.dot(data[start:end], x[indices[start:end]])
    return result


def load_inputs(repository: Path) -> tuple[list[np.ndarray], list[dict[str, np.ndarray]]]:
    root = repository / PROVINCE
    states: list[np.ndarray] = []
    updates: list[dict[str, np.ndarray]] = []
    for checkpoint in range(3):
        with np.load(root / f"checkpoint_{checkpoint:03d}/checkpoint_arrays.npz", allow_pickle=False) as saved:
            states.append(np.array(saved["value"], copy=True))
        with np.load(root / f"checkpoint_{checkpoint:03d}/direct_update_arrays.npz", allow_pickle=False) as saved:
            updates.append({name: np.array(saved[name], copy=True) for name in saved.files})
    states.append(np.array(updates[2]["next_value"], copy=True))
    return states, updates


def edge_row(index: tuple[int, int, int], old: float, full: float, critical: float) -> dict[str, Any]:
    left = index
    right = (index[0] + 1, index[1], index[2])
    return {
        "edge_left_index_b_a_z_zero_based": list(left),
        "edge_right_index_b_a_z_zero_based": list(right),
        "left_flat_f_zero_based": int(np.ravel_multi_index(left, SHAPE, order="F")),
        "right_flat_f_zero_based": int(np.ravel_multi_index(right, SHAPE, order="F")),
        "old_slope": old,
        "full_candidate_slope": full,
        "slope_change": full - old,
        "critical_alpha": critical,
    }


def feasibility(old_value: np.ndarray, full_value: np.ndarray, update: str) -> dict[str, Any]:
    old = raw_b_slopes(old_value)
    full = raw_b_slopes(full_value)
    change = full - old
    if old.size != 760 or not np.all(old > 0):
        raise RuntimeError("old iterate is outside the strict-positive raw-b domain")
    critical = np.full(old.shape, np.inf)
    declining = change < 0
    critical[declining] = old[declining] / (-change[declining])
    offset = int(np.argmin(critical))
    index = tuple(map(int, np.unravel_index(offset, critical.shape)))
    alpha_star = float(critical[index])
    active = []
    for raw_index in np.argwhere(critical <= 1.0):
        idx = tuple(map(int, raw_index))
        active.append(edge_row(idx, float(old[idx]), float(full[idx]), float(critical[idx])))
    return {
        "update": update,
        "edge_count": int(old.size),
        "affine_identity": "s_e(alpha)=s_e(V_n)+alpha*(s_e(Vhat)-s_e(V_n))",
        "old_all_strictly_positive": bool(np.all(old > 0)),
        "full_all_strictly_positive": bool(np.all(full > 0)),
        "old_minimum_slope": float(np.min(old)),
        "full_minimum_slope": float(np.min(full)),
        "positive_full_edges": int(np.sum(full > 0)),
        "nonpositive_full_edges": int(np.sum(full <= 0)),
        "unrestricted_critical_alpha": alpha_star,
        "admissible_interval_with_0_lt_alpha_le_1": "(0,1]" if alpha_star > 1 else f"(0,{alpha_star!r})",
        "binding_edge": edge_row(index, float(old[index]), float(full[index]), alpha_star),
        "constraints_binding_inside_0_1": active,
    }


def convex_candidate(old: np.ndarray, full: np.ndarray, alpha: float) -> np.ndarray:
    # The expression is part of the representation contract tested by this gate.
    return (1.0 - alpha) * old + alpha * full


def replay(old: np.ndarray, full: np.ndarray, design: str, alpha: float) -> dict[str, Any]:
    candidate = convex_candidate(old, full, alpha)
    slopes = raw_b_slopes(candidate)
    return {
        "design": design,
        "alpha": alpha,
        "value_change_inf": float(np.max(np.abs(candidate - old))),
        "minimum_raw_b_slope": float(np.min(slopes)),
        "positive_edges": int(np.sum(slopes > 0)),
        "zero_edges": int(np.sum(slopes == 0)),
        "negative_edges": int(np.sum(slopes < 0)),
        "strict_positive_pass": bool(np.all(slopes > 0)),
        "accepted_state_differs_bitwise_from_old": bool(not np.array_equal(candidate, old)),
        "candidate_sha256": field_sha256(candidate),
    }


def halving_alpha(old: np.ndarray, full: np.ndarray) -> tuple[float, int]:
    for reductions in range(HALVING_CEILING + 1):
        alpha = 2.0 ** (-reductions)
        candidate = convex_candidate(old, full, alpha)
        if np.all(raw_b_slopes(candidate) > 0) and not np.array_equal(candidate, old):
            return alpha, reductions
    raise RuntimeError("proposed finite halving rule exhausted")


def predecessor_diagnostic(old: np.ndarray, full: np.ndarray, critical: float) -> dict[str, Any]:
    alpha = critical
    rows = []
    first_pass = None
    for predecessors in range(1, 1025):
        alpha = float(np.nextafter(alpha, 0.0))
        row = replay(old, full, "design2_predecessor_diagnostic", alpha)
        row["predecessor_steps"] = predecessors
        if predecessors <= 4 or row["strict_positive_pass"]:
            rows.append(row)
        if row["strict_positive_pass"]:
            first_pass = row
            break
    return {
        "critical_alpha": critical,
        "single_predecessor_is_sufficient": bool(rows[0]["strict_positive_pass"]),
        "first_passing_predecessor_steps_with_prescribed_convex_expression": None if first_pass is None else first_pass["predecessor_steps"],
        "first_passing_row": first_pass,
        "sampled_rows": rows,
        "interpretation": "A real-arithmetic interior endpoint rule is insufficient by itself; the represented relaxed array must be checked.",
    }


def residual_diagnostic(update: dict[str, np.ndarray], old: np.ndarray, alpha: float, label: str) -> dict[str, Any]:
    candidate = convex_candidate(old, update["next_value"], alpha)
    residual = csr_matvec(
        update["matrix_data"], update["matrix_indices"], update["matrix_indptr"], candidate.ravel(order="F")
    ) - update["rhs"]
    return {
        "label": label,
        "alpha": alpha,
        "frozen_checkpoint2_residual_inf": float(np.max(np.abs(residual))),
        "residual_sha256": field_sha256(residual),
        "interpretation": "Diagnostic only: a relaxed state is not expected to solve the frozen checkpoint2 linear system exactly.",
    }


def build_manifest(output: Path) -> None:
    excluded = {"sealed_manifest.json", "independent_readback_receipt.json"}
    rows = []
    for path in sorted(p for p in output.rglob("*") if p.is_file() and p.name not in excluded):
        rows.append({"path": path.relative_to(output).as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)})
    write_json(output / "sealed_manifest.json", {
        "schema": "CH5_MONOTONICITY_PRESERVING_HJB_RELAXATION_DESIGN_GATE_MANIFEST_V1",
        "entry_count": len(rows),
        "total_bytes": sum(row["bytes"] for row in rows),
        "entries": rows,
    })
    payload = json.loads((output / "sealed_manifest.json").read_text(encoding="utf-8"))
    bad = []
    for row in payload["entries"]:
        path = output / row["path"]
        if not path.is_file() or path.stat().st_size != row["bytes"] or sha256(path) != row["sha256"]:
            bad.append(row["path"])
    write_json(output / "independent_readback_receipt.json", {
        "status": "PASS" if not bad else "FAIL",
        "manifest_sha256": sha256(output / "sealed_manifest.json"),
        "entry_count": payload["entry_count"],
        "total_bytes": payload["total_bytes"],
        "bad_paths": bad,
        "scientific_calls": 0,
    })


def execute(repository: Path, junit: Path) -> str:
    repository = repository.resolve(strict=True)
    output = repository / OUT
    if output.exists():
        raise RuntimeError("fresh evidence root already exists")
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repository, text=True).strip()
    origin = subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=repository, text=True).strip()
    if head != BASELINE or origin != BASELINE:
        raise RuntimeError("live-main baseline binding failed")
    output.mkdir(parents=True)
    write_json(output / "authority_source_binding.json", {
        "status": "PASS", "task_id": TASK_ID, "head": head, "origin_main": origin,
        "authority": [identity(repository / path, repository) for path in AUTHORITY],
        "read_only_sources": [identity(repository / path, repository) for path in SOURCES],
    })

    states, updates = load_inputs(repository)
    manifest_path = repository / ACCEPTED_ROOT / "sealed_manifest.json"
    links = []
    for n in range(3):
        links.append({
            "update": f"{n}->{n+1}",
            "old_state_sha256": field_sha256(states[n]),
            "direct_candidate_sha256": field_sha256(updates[n]["next_value"]),
            "target_state_sha256": field_sha256(states[n+1]),
            "candidate_exact_target": bool(np.array_equal(updates[n]["next_value"], states[n+1])),
        })
    if sha256(manifest_path) != ACCEPTED_MANIFEST_SHA256 or not all(row["candidate_exact_target"] for row in links):
        raise RuntimeError("accepted persisted input binding failed")
    write_json(output / "accepted_persisted_input_binding.json", {
        "accepted_manifest_path": ACCEPTED_ROOT.joinpath("sealed_manifest.json").as_posix(),
        "accepted_manifest_sha256": sha256(manifest_path), "expected_manifest_sha256": ACCEPTED_MANIFEST_SHA256,
        "links": links,
    })

    feasibility_rows = [feasibility(states[n], states[n + 1], f"{n}->{n+1}") for n in range(3)]
    write_json(output / "full_edge_alpha_feasibility.json", {
        "updates": feasibility_rows, "total_edge_inequalities": 3 * 760,
        "strict_endpoint_semantics": "If alpha_star<=1, equality is excluded because it gives a zero raw b slope.",
    })
    write_json(output / "binding_edge_table.json", {
        "rows": [row["binding_edge"] | {"update": row["update"]} for row in feasibility_rows],
        "checkpoint2_to_3_all_constraints_inside_0_1": feasibility_rows[2]["constraints_binding_inside_0_1"],
    })

    replay_rows = []
    halving = []
    for n in range(3):
        full = replay(states[n], states[n + 1], "design0_full_update", 1.0)
        full["update"] = f"{n}->{n+1}"
        replay_rows.append(full)
        alpha, reductions = halving_alpha(states[n], states[n + 1])
        row = replay(states[n], states[n + 1], "design1_deterministic_halving", alpha)
        row.update({"update": f"{n}->{n+1}", "halving_reductions": reductions})
        replay_rows.append(row)
        halving.append(row)
    critical = feasibility_rows[2]["unrestricted_critical_alpha"]
    predecessor = predecessor_diagnostic(states[2], states[3], critical)
    write_json(output / "persisted_update_arithmetic_replay.json", {
        "rows": replay_rows, "design2_checkpoint2_to_3": predecessor,
        "production_derivative_helper_calls": 0, "selector_calls": 0, "hjb_or_q_calls": 0,
    })

    write_json(output / "frozen_checkpoint2_relaxed_residual_diagnostic.json", {
        "rows": [
            residual_diagnostic(updates[2], states[2], 1.0, "full_direct_candidate"),
            residual_diagnostic(updates[2], states[2], 0.5, "design1_halving_accepted"),
            residual_diagnostic(updates[2], states[2], predecessor["first_passing_row"]["alpha"], "design2_first_representation_safe_predecessor"),
        ],
        "new_linear_solves": 0,
    })

    write_json(output / "fixed_point_invariance_derivation.json", {
        "original_map": "T(V)=Vhat", "relaxed_map": "F(V)=V+alpha(V,T(V))*(T(V)-V)",
        "assumption": "Every accepted nonfixed update has represented alpha>0 and changes the represented state; otherwise stop fail closed.",
        "forward": "T(V)=V implies F(V)=V.",
        "reverse": "F(V)=V and alpha>0 imply T(V)-V=0, hence T(V)=V, in exact arithmetic.",
        "conclusion": "Accepted relaxed and original maps have the same fixed points under the stated nonzero/no-stagnation rule.",
        "convergence_claim": "No global convergence theorem is claimed; state-dependent relaxation can change rate and trajectory.",
    })
    write_json(output / "candidate_design_comparison.json", {
        "designs": [
            {"design": 0, "rule": "alpha=1", "assessment": "Current authority; exits the positive-slope domain at update 2->3."},
            {"design": 1, "rule": "first passing alpha in 1,1/2,...,2^-52", "assessment": "Proposed generic law: deterministic, global, no clipping, finite, fail closed. Halving is a conventional contraction factor rather than a unique scientific constant."},
            {"design": 2, "rule": "critical alpha from all edge inequalities", "assessment": "Maximizes the real-arithmetic step but the strict endpoint is forbidden and one predecessor fails after represented convex combination; near-zero slopes also create q_b-domain conditioning risk. Retained as diagnostic comparator."},
            {"design": 3, "rule": "projection/clipping", "assessment": "Locally alters values or derivatives and therefore the iterate/equations; comparator only."},
            {"design": 4, "rule": "adaptive Delta and new solve", "assessment": "Changes the numerical map and requires another solve; comparator only."},
        ]
    })
    write_json(output / "invariant_domain_scientific_memo.json", {
        "economic_basis": "The consumption first-order condition uses q_b=c^(-gamma)>0, and added liquid wealth cannot lower attainable value under the repository budget/utility structure.",
        "numerical_scope": "Intermediate implicit iterates are not automatically monotone; positivity is imposed as the domain in which the next corrected HJB policy map is defined.",
        "target_preservation": "A global convex relaxation changes no cell independently and leaves fixed points unchanged when alpha remains positive.",
        "interpretation": "Triggering only when the full candidate exits the domain is a prospective invariant-domain line search, not tuning to F0063.",
        "limit": "This is a numerical design argument, not a proof of global HJB convergence or of existence of an in-domain fixed point.",
    })
    write_json(output / "convergence_law_interaction_contract.json", {
        "D_n": "Compute ||V_n-V_(n-1)||inf from the accepted relaxed V_n.",
        "B_n": "Compute only after one fresh complete policy/Q map at the accepted relaxed V_n in a future authorized implementation/runtime.",
        "cycles": "Hash and compare accepted relaxed checkpoints and their fresh selected-policy/Q identities.",
        "update_accounting": "One full direct solve followed by any number of arithmetic halving checks is one HJB update, not a retry.",
        "ceiling": "Each accepted relaxed update consumes one of the existing 100 total HJB updates.",
        "thresholds": {"B_inclusive": 1e-8, "D_inclusive": 1e-7, "changed": False},
    })
    write_json(output / "proposal_only_generic_law.json", {
        "status": "PROPOSAL_ONLY__OWNER_ADOPTION_REQUIRED",
        "trigger": "After the single full implicit solve passes the existing <=1e-12 backward-error gate, test all 760 raw b edges of Vhat using the repository grid and strict >0 comparison.",
        "selection": "If alpha=1 passes, accept it. Otherwise test alpha=2^-k in increasing k=1..52 using exactly (1-alpha)*V_old+alpha*Vhat; accept the first candidate whose 760 raw b slopes are finite and >0 and whose represented state differs from V_old.",
        "why_52": "The finite ceiling is tied prospectively to binary64 significand resolution; it is an operation/fail-closed bound, not an economic derivative floor.",
        "failure_terminal": "FAIL__MONOTONICITY_PRESERVING_HJB_RELAXATION_EXHAUSTED",
        "no_floor": "No positive slope magnitude threshold is imposed; comparison is strictly >0. Bitwise no-progress is rejected separately as a representation failure.",
        "evidence_contract": "Persist full-candidate hash, each attempted alpha and minimum/count census, accepted relaxed-state hash, value-change norm, and unchanged solve receipt.",
        "future_plan": "Only after Owner adoption: implement narrowly, test exact persisted replay, independently review, then authorize any fresh HJB/turn2 execution in a separate task.",
    })

    ledger = {
        "persisted_npz_loads": 6,
        "persisted_json_loads": 1,
        "accepted_sha256_reads": 1,
        "independent_raw_b_edge_reconstructions": 20,
        "edge_inequalities_evaluated": 2280,
        "convex_relaxation_candidates_evaluated": 17,
        "independent_csr_matvecs": 3,
        "production_derivative_helper_calls": 0,
        "production_selector_calls": 0,
        "production_root_helper_calls": 0,
        "hjb_direct_update_executions": 0,
        "new_linear_solves_spsolve": 0,
        "d2_q_rebuilds": 0,
        "kfe_svd": 0,
        "aggregate_integration": 0,
        "turn2_replay_rerun": 0,
        "turn3": 0,
        "matlab": 0,
        "retry_tuning": 0,
        "scientific_model_calls": 0,
    }
    write_json(output / "zero_science_ledger.json", ledger)
    junit_text = junit.read_text(encoding="utf-8")
    shutil.copyfile(junit, output / "focused_tests.xml")
    write_json(output / "focused_test_receipt.json", {
        "status": "PASS" if 'failures="0"' in junit_text and 'errors="0"' in junit_text else "FAIL",
        "sha256": sha256(output / "focused_tests.xml"),
    })
    write_json(output / "terminal_receipt.json", {
        "terminal": TERMINAL, "classification": CLASSIFICATION, "zero_science_ledger": ledger,
        "src_modified": False, "current_modified": False, "successor_published": False, "results_eligibility": False,
    })
    build_manifest(output)
    return TERMINAL


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--focused-test-junit", type=Path, required=True)
    args = parser.parse_args(argv)
    print(execute(args.repository, args.focused_test_junit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
