"""Preflight, two-call omega=1 parity gate, and omega=0.5 exact-input treatment."""

from __future__ import annotations

import argparse
import json
import os
import platform
import sys
import time
from hashlib import sha256
from pathlib import Path
from typing import Any

import numpy as np

REPO = Path(__file__).resolve().parents[3]
for item in (REPO / "src", REPO):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))

from validators.multi_province.k1_hjb_convergence_mechanism import run as prior  # noqa: E402
from validators.multi_province.k1_hjb_convergence_mechanism.instrumented_hjb import _operator_metrics  # noqa: E402
from validators.multi_province.k1_hjb_value_relaxation.relaxed_hjb import solve_with_value_relaxation  # noqa: E402

TASK_ID = "CH5_MP4C_K1_HJB_FIXED_POINT_VALUE_UPDATE_RELAXATION_OMEGA_0P5_SAME_INPUT_DIAGNOSTIC"
MECHANISM_MANIFEST_SHA256 = "82A979E15DF22A651348F8C4E35FFE5688513E635877269DA98DF0755D03AF77"
PARITY_KEYS = ((1, 0, "北京", "ACCEPTED_CONVERGED"), (1, 11, "安徽", "ACCEPTED_CEILING_FAILURE"))


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _sha_file(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest().upper()


def _verify_sealed_root(root: Path, expected_manifest_sha: str) -> dict[str, dict[str, Any]]:
    manifest_path = root / "sealed_manifest_sha256.json"
    if _sha_file(manifest_path) != expected_manifest_sha:
        raise ValueError(f"sealed manifest SHA mismatch: {root}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    mapping = {str(item["path"]): item for item in manifest["entries"]}
    for relative, item in mapping.items():
        target = root / relative
        if not target.is_file() or target.stat().st_size != item["bytes"] or _sha_file(target) != item["sha256"]:
            raise ValueError(f"sealed evidence entry mismatch: {target}")
    return mapping


def _operator_exact(actual: Any, expected: Any) -> bool:
    difference = (actual.tocsr() - expected.tocsr()).tocsr()
    return not difference.nnz or bool(np.all(difference.data == 0))


def _accepted_full_equal(result: Any, path: Path) -> tuple[bool, list[str]]:
    exact, mismatches = prior._accepted_npz_equal(result, path)
    with np.load(path, allow_pickle=True) as stored:
        for name, actual in (("operator", result.operator.full),
                             ("post_convergence_operator", result.post_convergence_operator.full)):
            if not _operator_exact(actual, stored[name].item()):
                mismatches.append(name)
    return exact and not mismatches, mismatches


def _save_result(path: Path, result: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        path,
        value=result.value, initial_value=result.initial_value,
        consumption=result.consumption, labor=result.labor, transfer=result.transfer,
        adjustment_cost=result.adjustment_cost, effective_illiquid_return=result.effective_illiquid_return,
        mu_a=result.mu_a, mu_b=result.mu_b, utility=result.utility,
        liquid_label=result.liquid_label, transfer_label=result.transfer_label,
        operator=result.operator.full.toarray(), post_convergence_operator=result.post_convergence_operator.full.toarray(),
        iterations=np.array(result.iterations), converged=np.array(result.converged),
        convergence_statistic=np.array(result.convergence_statistic),
    )


def preflight(accepted_parent: Path, mechanism_parent: Path, output_root: Path) -> int:
    accepted_parent = Path(accepted_parent)
    mechanism_parent = Path(mechanism_parent)
    output_root = Path(output_root)
    if output_root.exists():
        raise FileExistsError("fresh no-overwrite evidence root already exists")
    output_root.mkdir(parents=True)
    _verify_sealed_root(mechanism_parent, MECHANISM_MANIFEST_SHA256)
    prior_manifest_path, prior_mapping = prior._manifest_map(accepted_parent)
    root = accepted_parent / "annual_g2_control"
    grid, params, numerics = prior._objects()
    historical = json.loads((mechanism_parent / "identity_receipts.json").read_text(encoding="utf-8"))
    receipts: list[dict[str, Any]] = []
    for item in historical:
        turn = int(item["turn"])
        index = int(item["province_index"])
        _, identity = prior._call_inputs(root, turn, index, grid, params, numerics)
        relevant = [
            f"annual_g2_control/turn_{turn:02d}/entering_state.json",
            f"annual_g2_control/turn_{turn:02d}/d1_instrumentation/p{index:02d}_{identity['province']}_hjb_trace.json",
            f"annual_g2_control/turn_{turn:02d}/household/p{index:02d}_{identity['province']}/hjb_return.npz",
        ]
        manifest_checks = {relative: prior._verify_manifest_entry(accepted_parent, prior_mapping, relative) for relative in relevant}
        # The accepted mechanism package later adjudicated its receipt-level wage-guard
        # labels as metadata-only errors.  Bind the scientific input identity to all
        # unaffected fields and recompute guarded wjt/state from the sealed entering
        # state instead of requiring equality to those two superseded labels.
        current_core = {key: identity[key] for key in (
            "turn", "province_index", "province", "initial_value_sha256", "baseline_labor_sha256", "grid_sha256",
            "params", "numerics", "raw_entering_r_a", "consumed_r_a", "return_guard_state", "wage",
            "r_b", "tau", "transfer_income", "borrowing_rate_gap", "transfer_control_state",
            "source_faithful_labor")}
        history_core = {key: item.get(key) for key in current_core}
        identity["accepted_iterations"] = item["accepted_iterations"]
        identity["accepted_converged"] = item["accepted_converged"]
        identity["accepted_convergence_statistic"] = item["accepted_convergence_statistic"]
        identity["manifest_entries"] = manifest_checks
        identity["historical_identity_exact"] = current_core == history_core
        identity["wage_guard_metadata_adjudication"] = {
            "status": "RECOMPUTED_FROM_SEALED_ENTERING_STATE",
            "historical_guarded_wjt": item.get("guarded_wjt"),
            "historical_wage_guard_state": item.get("wage_guard_state"),
            "guarded_wjt": identity["guarded_wjt"],
            "wage_guard_state": identity["wage_guard_state"],
            "scientific_input_affected": False,
        }
        identity["status"] = "PROVEN_EXACT" if identity["historical_identity_exact"] and item["status"] == "PROVEN_EXACT" else "REPLAY_INPUT_IDENTITY_UNPROVEN"
        receipts.append(identity)
    proven = [item for item in receipts if item["status"] == "PROVEN_EXACT"]
    parity_registration = []
    for turn, index, province, accepted_class in PARITY_KEYS:
        match = next((item for item in proven if item["turn"] == turn and item["province_index"] == index), None)
        parity_registration.append({"turn": turn, "province_index": index, "province": province,
                                    "accepted_class": accepted_class, "identity_status": match["status"] if match else "UNPROVEN"})
    source_paths = [
        REPO / "exports/matlab_faithful_two_asset_ha.py",
        REPO / "validators/multi_province/k1_hjb_convergence_mechanism/instrumented_hjb.py",
        REPO / "validators/multi_province/k1_hjb_value_relaxation/relaxed_hjb.py",
        REPO / "validators/multi_province/k1_hjb_value_relaxation/run.py",
    ]
    _write_json(output_root / "identity_receipts.json", receipts)
    _write_json(output_root / "preflight.json", {
        "schema": "CH5_MP4C_K1_HJB_VALUE_RELAXATION_PREFLIGHT_V1", "task_id": TASK_ID,
        "status": "PASS" if len(proven) == 62 and all(x["identity_status"] == "PROVEN_EXACT" for x in parity_registration) else "PARTIAL_IDENTITY",
        "accepted_manifest_path": str(prior_manifest_path), "accepted_manifest_sha256": prior.ACCEPTED_MANIFEST_SHA256,
        "mechanism_manifest_path": str(mechanism_parent / "sealed_manifest_sha256.json"),
        "mechanism_manifest_sha256": MECHANISM_MANIFEST_SHA256, "exact_input_coverage": len(proven),
        "unproven_calls": 62 - len(proven), "parity_preregistration": parity_registration,
        "omega_treatment": 0.5, "raw_tolerance": numerics.convergence_tolerance,
        "science_calls_before_gate": 0, "engineering_retries_consumed": 1,
        "source_sha256": {path.relative_to(REPO).as_posix(): _sha_file(path) for path in source_paths},
        "scientific_budget": {"omega1_parity_hjb_exactly": 2, "omega0p5_treatment_hjb_maximum": 62,
                              "total_hjb_maximum": 64, "scientific_retries": 0, "kfe": 0, "matlab": 0,
                              "outer_trajectory_advancements": 0, "firm": 0, "k1b": 0, "k2": 0,
                              "ge": 0, "irf": 0, "results": 0},
    })
    return 0


def run(accepted_parent: Path, mechanism_parent: Path, output_root: Path) -> int:
    accepted_parent = Path(accepted_parent)
    mechanism_parent = Path(mechanism_parent)
    output_root = Path(output_root)
    preflight_receipt = json.loads((output_root / "preflight.json").read_text(encoding="utf-8"))
    if preflight_receipt["status"] not in ("PASS", "PARTIAL_IDENTITY"):
        raise RuntimeError("preflight did not establish executable identity")
    if (output_root / "science_started.json").exists():
        raise FileExistsError("scientific execution is no-overwrite and non-retryable")
    identities = json.loads((output_root / "identity_receipts.json").read_text(encoding="utf-8"))
    proven = [item for item in identities if item["status"] == "PROVEN_EXACT"]
    by_key = {(item["turn"], item["province_index"]): item for item in proven}
    _write_json(output_root / "science_started.json", {
        "schema": "CH5_MP4C_K1_HJB_VALUE_RELAXATION_SCIENCE_STARTED_V1", "task_id": TASK_ID,
        "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "process_id": os.getpid(),
        "python": sys.version, "platform": platform.platform(), "proven_exact_calls": len(proven),
        "scientific_retries": 0,
    })
    root = accepted_parent / "annual_g2_control"
    grid, params, numerics = prior._objects()
    ledger: list[dict[str, Any]] = []
    parity_rows: list[dict[str, Any]] = []
    for call_number, (turn, index, province, accepted_class) in enumerate(PARITY_KEYS, start=1):
        identity = by_key.get((turn, index))
        if identity is None:
            parity_rows.append({"status": "FAIL", "reason": "PREREGISTERED_INPUT_UNPROVEN", "turn": turn, "province": province})
            break
        args, _ = prior._call_inputs(root, turn, index, grid, params, numerics)
        result, trace = solve_with_value_relaxation(*args, omega=1.0)
        exact, mismatches = _accepted_full_equal(result, Path(identity["accepted_hjb_path"]))
        expected_operator = prior._accepted_final_operator_hash(Path(identity["trace_path"]))
        operator_hash = _operator_metrics(result.operator.full)["full_sha256"]
        operator_exact = operator_hash == expected_operator
        row = {"status": "PASS" if exact and operator_exact else "FAIL", "call": call_number,
               "turn": turn, "province_index": index, "province": province, "accepted_class": accepted_class,
               "omega": 1.0, "accepted_full_result_exact": exact, "mismatches": mismatches,
               "accepted_final_operator_sha256": expected_operator, "actual_final_operator_sha256": operator_hash,
               "final_operator_exact": operator_exact, "iterations": int(result.iterations),
               "converged": bool(result.converged), "raw_fixed_point_gap": float(result.convergence_statistic),
               "direct_solves": trace["direct_solves"], "raw_gap_contract": trace["convergence_contract"]}
        parity_rows.append(row)
        ledger.append({"call": call_number, "phase": "OMEGA1_PARITY", "turn": turn, "province": province,
                       "consumed": True, "direct_solves": trace["direct_solves"], "status": row["status"]})
        if row["status"] != "PASS":
            break
    parity_ok = len(parity_rows) == 2 and all(row["status"] == "PASS" for row in parity_rows)
    _write_json(output_root / "omega1_equivalence.json", {"status": "PASS" if parity_ok else "FAIL",
                                                            "preregistered_calls": parity_rows})
    if not parity_ok:
        _write_json(output_root / "call_ledger.json", {"hjb_calls": len(ledger), "parity_hjb_calls": len(ledger),
                                                        "treatment_hjb_calls": 0, "scientific_retries": 0,
                                                        "kfe_calls": 0, "outer_trajectory_advancements": 0,
                                                        "matlab_calls": 0, "firm_calls": 0, "calls": ledger})
        _write_json(output_root / "terminal_result.json", {"status": "HARD_STOP_OMEGA1_PARITY_FAILURE",
                                                            "results_eligible": False})
        return 2

    treatment_rows: list[dict[str, Any]] = []
    for call_number, identity in enumerate(proven, start=3):
        args, _ = prior._call_inputs(root, identity["turn"], identity["province_index"], grid, params, numerics)
        result, trace = solve_with_value_relaxation(*args, omega=0.5)
        finite_fields = {name: bool(np.isfinite(np.asarray(getattr(result, name))).all())
                         for name in prior.SCIENTIFIC_FIELDS if np.asarray(getattr(result, name)).dtype.kind not in "US"}
        label_domain = bool(set(np.unique(result.liquid_label)).issubset({"B", "F", "0"}) and
                            set(np.unique(result.transfer_label)).issubset({"B", "F", "0"}))
        normal = all(finite_fields.values()) and label_domain and all(
            row["finite"]["v_old"] and row["finite"]["v_solve"] and row["finite"]["v_next"]
            and all(row["finite"]["scientific_arrays"].values()) for row in trace["iterations"])
        trace.update({
            "task_id": TASK_ID, "turn": identity["turn"], "province": identity["province"],
            "province_index": identity["province_index"], "input_identity_status": identity["status"],
            "consumed_r_a": identity["consumed_r_a"], "raw_entering_r_a": identity["raw_entering_r_a"],
            "return_guard_state": identity["return_guard_state"], "consumed_household_composite_wage": identity["wage"],
            "guarded_wjt": identity["guarded_wjt"], "wage_guard_state": identity["wage_guard_state"],
            "d1_active": False, "final_converged": bool(result.converged),
            "final_iterations": int(result.iterations), "final_raw_fixed_point_gap": float(result.convergence_statistic),
            "output_normal": normal, "finite_scientific_fields": finite_fields, "policy_label_domain_valid": label_domain,
            "scientific_exception": None,
        })
        stem = f"p{identity['province_index']:02d}_{identity['province']}"
        trace_path = output_root / "traces" / f"turn_{identity['turn']:02d}" / f"{stem}.json"
        result_path = output_root / "results" / f"turn_{identity['turn']:02d}" / f"{stem}.npz"
        _write_json(trace_path, trace)
        _save_result(result_path, result)
        treatment_rows.append({
            "turn": identity["turn"], "province_index": identity["province_index"], "province": identity["province"],
            "converged": bool(result.converged), "iterations": int(result.iterations),
            "raw_fixed_point_gap": float(result.convergence_statistic),
            "relaxed_state_update": float(trace["iterations"][-1]["relaxed_state_update"]),
            "direct_solves": trace["direct_solves"], "output_normal": normal,
            "trace_path": str(trace_path), "result_path": str(result_path),
            "accepted_hjb_path": identity["accepted_hjb_path"],
        })
        ledger.append({"call": call_number, "phase": "OMEGA0P5_TREATMENT", "turn": identity["turn"],
                       "province": identity["province"], "consumed": True, "direct_solves": trace["direct_solves"],
                       "converged": bool(result.converged), "output_normal": normal})
    _write_json(output_root / "treatment_summary.json", treatment_rows)
    _write_json(output_root / "call_ledger.json", {
        "schema": "CH5_MP4C_K1_HJB_VALUE_RELAXATION_CALL_LEDGER_V1", "hjb_calls": len(ledger),
        "parity_hjb_calls": 2, "treatment_hjb_calls": len(treatment_rows), "scientific_retries": 0,
        "kfe_calls": 0, "outer_trajectory_advancements": 0, "matlab_calls": 0, "firm_calls": 0,
        "k1b_calls": 0, "k2_calls": 0, "ge_calls": 0, "irf_calls": 0, "results_calls": 0,
        "calls": ledger,
    })
    parity_solves = sum(row["direct_solves"] for row in parity_rows)
    treatment_solves = sum(row["direct_solves"] for row in treatment_rows)
    _write_json(output_root / "direct_solve_count_receipt.json", {
        "schema": "CH5_MP4C_K1_HJB_VALUE_RELAXATION_DIRECT_SOLVE_COUNT_V1",
        "counting_identity": "one accepted scipy.sparse.linalg.spsolve invocation per HJB internal iteration",
        "parity_hjb_calls": 2, "parity_hjb_direct_solves": parity_solves,
        "treatment_hjb_calls": len(treatment_rows), "treatment_hjb_direct_solves": treatment_solves,
        "total_hjb_calls": len(ledger), "total_hjb_direct_solves": parity_solves + treatment_solves,
        "scientific_retries": 0,
    })
    _write_json(output_root / "terminal_result.json", {
        "status": "TREATMENT_COMPLETE", "exact_input_coverage": len(proven), "hjb_calls": len(ledger),
        "turn1_converged": sum(row["turn"] == 1 and row["converged"] for row in treatment_rows),
        "turn2_converged": sum(row["turn"] == 2 and row["converged"] for row in treatment_rows),
        "all_converged": sum(row["converged"] for row in treatment_rows),
        "output_normal_count": sum(row["output_normal"] for row in treatment_rows),
        "scientific_exceptions": 0, "results_eligible": False,
    })
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("preflight", "run"):
        item = sub.add_parser(name)
        item.add_argument("accepted_parent", type=Path)
        item.add_argument("mechanism_parent", type=Path)
        item.add_argument("output_root", type=Path)
    args = parser.parse_args(argv)
    return preflight(args.accepted_parent, args.mechanism_parent, args.output_root) if args.command == "preflight" else run(args.accepted_parent, args.mechanism_parent, args.output_root)


if __name__ == "__main__":
    raise SystemExit(main())
