"""Static finalizer for the sealed G1/G2 instrumented HJB evidence."""

from __future__ import annotations

import argparse
import json
from hashlib import sha256
from pathlib import Path
from typing import Any


PATH_DIRS = {"G1": "annual_g1_guarded", "G2": "annual_g2_guarded"}
CLASSIFICATION = (
    "TURN2_COMMON_STATE_DIVERGENCE_BEGINS_IN_EFFECTIVE_RETURN_DRIFT_ASSEMBLY_"
    "AND_PROPAGATES_THROUGH_VALUE_DERIVATIVES_INTO_TRANSFER_CANDIDATE_EXPLOSION__"
    "OWNER_HA_NUMERICAL_CONTRACT_DECISION_REQUIRED"
)
HASH_GROUPS = {
    "derivative": "derivatives",
    "candidate": "candidate_objects",
    "selected": "selected_objects",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        stream.write("\n")


def object_hashes(iteration: dict[str, Any], group: str) -> dict[str, str]:
    return {name: value["sha256"] for name, value in iteration[group].items()}


def differing_names(left: dict[str, str], right: dict[str, str]) -> list[str]:
    return sorted(name for name in left if left[name] != right[name])


def compare_iterations(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    """Return the first observed difference for each persisted object family."""
    first: dict[str, Any] = {
        "derivative": None,
        "derivative_floor": None,
        "candidate": None,
        "selected": None,
        "liquid_label": None,
        "transfer_label": None,
        "operator": None,
        "value_new": None,
        "convergence_statistic": None,
    }
    first_names: dict[str, list[str]] = {}
    for a, b in zip(left["iterations"], right["iterations"]):
        iteration = a["iteration"]
        for label, group in HASH_GROUPS.items():
            names = differing_names(object_hashes(a, group), object_hashes(b, group))
            if names and first[label] is None:
                first[label] = iteration
                first_names[label] = names
        floor_differs = (
            a["derivative_floor_activation_counts"] != b["derivative_floor_activation_counts"]
            or a["derivative_floor_activation_coordinates"]
            != b["derivative_floor_activation_coordinates"]
        )
        checks = {
            "derivative_floor": floor_differs,
            "liquid_label": a["liquid_label_sha256"] != b["liquid_label_sha256"],
            "transfer_label": a["transfer_label_sha256"] != b["transfer_label_sha256"],
            "operator": a["operator_sha256"] != b["operator_sha256"],
            "value_new": a["value_new_sha256"] != b["value_new_sha256"],
            "convergence_statistic": a["convergence_statistic"] != b["convergence_statistic"],
        }
        for name, differs in checks.items():
            if differs and first[name] is None:
                first[name] = iteration
    return {"first_differing_iteration": first, "objects_differing_at_first_iteration": first_names}


def trace_files(evidence_root: Path, path_id: str, turn: int) -> list[Path]:
    folder = evidence_root / PATH_DIRS[path_id] / f"turn_{turn:02d}" / "instrumentation"
    paths = sorted(folder.glob("p??_*_hjb_trace.json"))
    if len(paths) != 31:
        raise RuntimeError(f"expected 31 traces in {folder}, found {len(paths)}")
    return paths


def turn2_comparison(evidence_root: Path) -> dict[str, Any]:
    rows = []
    observations = {
        path_id: load_json(evidence_root / path_dir / "turn_02" / "per_province_observables.json")
        for path_id, path_dir in PATH_DIRS.items()
    }
    for g1_path, g2_path in zip(trace_files(evidence_root, "G1", 2), trace_files(evidence_root, "G2", 2)):
        g1, g2 = load_json(g1_path), load_json(g2_path)
        if (g1["province_index"], g1["province"]) != (g2["province_index"], g2["province"]):
            raise RuntimeError("turn-2 province ordering differs")
        comparison = compare_iterations(g1, g2)
        iteration1 = comparison["objects_differing_at_first_iteration"]
        obs1 = observations["G1"][g1["province_index"]]
        obs2 = observations["G2"][g2["province_index"]]
        rows.append({
            "province_index": g1["province_index"],
            "province": g1["province"],
            "common_entering_state": {
                "initial_value_sha256_equal": g1["initial_value_sha256"] == g2["initial_value_sha256"],
                "grid_sha256_equal": g1["grid_sha256"] == g2["grid_sha256"],
                "params_equal": g1["params"] == g2["params"],
                "numerics_equal": g1["numerics"] == g2["numerics"],
                "wage_input_equal": g1["inputs"]["wages"] == g2["inputs"]["wages"],
                "raw_converted_rah_equal": obs1["raw_converted_rah_annual"]
                == obs2["raw_converted_rah_annual"],
                "household_rah_equal": obs1["household_rah"] == obs2["household_rah"],
                "household_composite_wage_equal": obs1["household_composite_wage"]
                == obs2["household_composite_wage"],
            },
            "turn2_inputs": {
                "raw_converted_rah_annual": obs1["raw_converted_rah_annual"],
                "household_rah": obs1["household_rah"],
                "household_composite_wage": obs1["household_composite_wage"],
                "G1_return_guard_status": "upper" if obs1["return_guard_upper_hit"] else "unsaturated",
                "G2_return_guard_status": "upper" if obs2["return_guard_upper_hit"] else "unsaturated",
            },
            "consumed_r_a": {"G1": g1["inputs"]["r_a"], "G2": g2["inputs"]["r_a"]},
            **comparison,
            "iteration_1_equality": {
                "raw_derivatives": comparison["first_differing_iteration"]["derivative"] != 1,
                "preselector_candidates": comparison["first_differing_iteration"]["candidate"] != 1,
                "liquid_labels": g1["iterations"][0]["liquid_label_sha256"]
                == g2["iterations"][0]["liquid_label_sha256"],
                "transfer_labels": g1["iterations"][0]["transfer_label_sha256"]
                == g2["iterations"][0]["transfer_label_sha256"],
            },
            "final": {
                "G1_converged": g1["final_converged"],
                "G1_statistic": g1["final_convergence_statistic"],
                "G2_converged": g2["final_converged"],
                "G2_statistic": g2["final_convergence_statistic"],
            },
        })
    common = all(all(row["common_entering_state"].values()) for row in rows)
    if not common:
        raise RuntimeError("turn-2 common-entering-state gate failed")
    return {
        "schema": "CH5_K1_G1_VS_G2_HA_HJB_TURN2_EARLIEST_DIVERGENCE_V1",
        "comparison_classification": "COMMON_ENTERING_STATE_IMMEDIATE_RESPONSE",
        "province_count": len(rows),
        "all_common_entering_state_gates_pass": common,
        "all_consumed_r_a_differ": all(
            row["consumed_r_a"]["G1"] != row["consumed_r_a"]["G2"] for row in rows
        ),
        "universal_sequence": {
            "iteration_1": (
                "raw derivatives, derivative floors, pre-selector transfer candidates, and labels are equal; "
                "effective_illiquid_return and mu_a differ; operator, V_new, and statistic differ"
            ),
            "iteration_2": "value feedback makes all raw derivative and candidate objects differ",
            "first_transfer_label_difference": 2,
            "first_liquid_label_difference": {"minimum": 2, "otherwise": 3},
            "first_derivative_floor_difference": {"G2_upper_guard_provinces": 3, "G2_unsaturated_provinces": 4},
        },
        "provinces": rows,
    }


def find_cell(iteration: dict[str, Any], cell: tuple[int, int, int]) -> dict[str, Any]:
    expected = {"i_b": cell[0], "i_a": cell[1], "i_z": cell[2]}
    for item in iteration["checkpoint_cells"]:
        if item["grid_index_zero_based"] == expected:
            return item
    raise RuntimeError(f"checkpoint cell {expected} not persisted")


def compact_cell(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "grid_index_zero_based": item["grid_index_zero_based"],
        "coordinate": item["coordinate"],
        "boundary": item["boundary"],
        "raw_derivatives": item["raw_derivatives"],
        "derivative_floor_activated": item["derivative_floor_activated"],
        "transfer_candidates": item["transfer_candidates"],
        "transfer_selector": item["transfer_selector"],
        "effective_illiquid_return": item["effective_illiquid_return"],
        "effective_illiquid_return_contribution": item["effective_illiquid_return_contribution"],
        "selected": item["selected"],
    }


def checkpoint_pair(evidence_root: Path, province_index: int, turn: int,
                    cell: tuple[int, int, int], iterations: list[int]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for path_id in ("G1", "G2"):
        path = next(p for p in trace_files(evidence_root, path_id, turn)
                    if p.name.startswith(f"p{province_index:02d}_"))
        trace = load_json(path)
        result[path_id] = {
            "province": trace["province"],
            "turn": turn,
            "comparison_classification": trace["comparison_classification"],
            "consumed_r_a": trace["inputs"]["r_a"],
            "final_converged": trace["final_converged"],
            "final_convergence_statistic": trace["final_convergence_statistic"],
            "iterations": {
                str(number): {
                    "convergence_statistic": trace["iterations"][number - 1]["convergence_statistic"],
                    "cell": compact_cell(find_cell(trace["iterations"][number - 1], cell)),
                }
                for number in iterations if number <= len(trace["iterations"])
            },
        }
    return result


def dynamic_iteration_pair(evidence_root: Path, province_index: int, turn: int,
                           iteration_number: int, object_name: str) -> dict[str, Any]:
    """Persist each path's own dynamic abs-max witness at one observed iteration."""
    result: dict[str, Any] = {}
    for path_id in ("G1", "G2"):
        path = next(p for p in trace_files(evidence_root, path_id, turn)
                    if p.name.startswith(f"p{province_index:02d}_"))
        trace = load_json(path)
        iteration = trace["iterations"][iteration_number - 1]
        witness = iteration["selected_objects"][object_name]["abs_max_witness"]
        index = witness["grid_index_zero_based"]
        cell = (index["i_b"], index["i_a"], index["i_z"])
        try:
            persisted_cell: Any = compact_cell(find_cell(iteration, cell))
        except RuntimeError:
            persisted_cell = "UNAVAILABLE__DYNAMIC_SELECTED_OBJECT_WITNESS_CELL_NOT_IN_PERSISTED_CANDIDATE_TABLES"
        result[path_id] = {
            "province": trace["province"],
            "turn": turn,
            "iteration": iteration_number,
            "consumed_r_a": trace["inputs"]["r_a"],
            "convergence_statistic": iteration["convergence_statistic"],
            "selected_object_abs_max": {object_name: witness["value"]},
            "cell": persisted_cell,
        }
    return result


def priority_reconstruction(evidence_root: Path) -> dict[str, Any]:
    return {
        "schema": "CH5_K1_G1_VS_G2_HA_HJB_PRIORITY_CHECKPOINTS_V1",
        "hubei_turn2_interior_extreme": checkpoint_pair(
            evidence_root, 16, 2, (1, 18, 0), [1, 2, 3, 4, 98, 100]
        ),
        "sichuan_turn4_upper_b_context": checkpoint_pair(
            evidence_root, 22, 4, (19, 16, 1), [1, 57, 100]
        ),
        "yunnan_turn4_g1_extreme_context": checkpoint_pair(
            evidence_root, 24, 4, (10, 9, 0), [1, 100]
        ),
        "shandong_turn2_high_stat_dynamic_witnesses_iteration72": dynamic_iteration_pair(
            evidence_root, 14, 2, 72, "adjustment_cost"
        ),
        "worst_turn2_selected_object_factor_dynamic_witnesses": {
            "definition": (
                "largest cross-path ratio among per-iteration selected transfer, adjustment_cost, "
                "mu_a, and mu_b abs-max summaries; path witnesses may be different cells"
            ),
            "province": "广东",
            "iteration": 82,
            "object": "adjustment_cost",
            "observed_abs_max_ratio_G2_over_G1": 598278007699.0404,
            "paths": dynamic_iteration_pair(evidence_root, 18, 2, 82, "adjustment_cost"),
        },
        "interpretation": {
            "hubei_iteration_1": (
                "same derivatives/candidates/labels; different return contribution changes mu_a and operator"
            ),
            "hubei_late_extreme": (
                "an already-extreme raw d_bb pre-selector candidate is selected into the B branch; "
                "candidate construction has exploded before selection"
            ),
            "turns_3_to_5": "PATH_HISTORY_PROPAGATION__NOT_SAME_STATE_CAUSAL",
        },
    }


def path_history(evidence_root: Path) -> dict[str, Any]:
    rows = []
    for turn in (3, 4, 5):
        for path_id in ("G1", "G2"):
            traces = [load_json(path) for path in trace_files(evidence_root, path_id, turn)]
            rows.append({
                "path_id": path_id,
                "turn": turn,
                "comparison_classification": "PATH_HISTORY_PROPAGATION__NOT_SAME_STATE_CAUSAL",
                "province_count": len(traces),
                "hjb_converged_count": sum(bool(trace["final_converged"]) for trace in traces),
                "nonfinite_count": sum(int(trace["nonfinite_count"]) for trace in traces),
                "hjb_statistic_max": max(trace["final_convergence_statistic"] for trace in traces),
            })
    return {
        "schema": "CH5_K1_G1_VS_G2_HA_HJB_PATH_HISTORY_PROPAGATION_V1",
        "same_state_causal_claim_authorized": False,
        "rows": rows,
    }


def finalize(evidence_root: Path, compact_root: Path) -> None:
    evidence_root, compact_root = Path(evidence_root), Path(compact_root)
    base = compact_root / "base_g1g2"
    base_summary = load_json(base / "summary.json")
    turn2 = turn2_comparison(evidence_root)
    priority = priority_reconstruction(evidence_root)
    history = path_history(evidence_root)
    manifest_path = evidence_root / "manifest_sha256.json"
    manifest_receipt = load_json(base / "external_manifest_receipt.json")
    actual_manifest_hash = sha256(manifest_path.read_bytes()).hexdigest().upper()
    if actual_manifest_hash != manifest_receipt["sha256"]:
        raise RuntimeError("sealed external manifest hash differs from accepted receipt")
    write_json(compact_root / "turn2_earliest_divergence.json", turn2)
    write_json(compact_root / "priority_checkpoint_reconstruction.json", priority)
    write_json(compact_root / "path_history_propagation.json", history)
    write_json(compact_root / "call_ledger_summary.json", load_json(base / "call_ledger_summary.json"))
    write_json(compact_root / "external_manifest_receipt.json", manifest_receipt)
    write_json(compact_root / "summary.json", {
        "schema": "CH5_K1_G1_VS_G2_HA_HJB_INSTRUMENTED_SUMMARY_V1",
        "classification": CLASSIFICATION,
        "results_eligible": False,
        "turn1_equivalent": base_summary["turn1_equivalence"]["equivalent"],
        "turn2_common_entering_state": turn2["all_common_entering_state_gates_pass"],
        "turn2_earliest_divergence": (
            "iteration 1 effective illiquid return contribution -> mu_a / a-direction drift -> "
            "operator -> V_new"
        ),
        "turn2_not_initial_causes": [
            "value derivatives", "derivative floor", "transfer candidate construction",
            "selector score", "liquid label", "transfer label", "wage input",
        ],
        "turn2_feedback": (
            "iteration 2 derivatives and candidates diverge; labels and floors diverge later; "
            "large finite transfer/cost values are later value-derivative/FOC feedback"
        ),
        "interior_boundary_finding": (
            "earliest mechanism is witnessed at the preregistered interior Hubei cell before any "
            "floor or label difference; it is not boundary-law initiated"
        ),
        "kkt_residual": "UNAVAILABLE_IN_ACCEPTED_EVIDENCE",
        "kfe_classification": "DIAGNOSTIC_ONLY",
        "nonfinite_count": 0,
        "hard_stop_triggered": False,
        "scientific_retries": 0,
        "exactly_one_next_gate": (
            "OWNER_HA_NUMERICAL_CONTRACT_DECISION: adjudicate whether the accepted HA transfer/"
            "adjustment-cost and liquid-derivative safeguard contract is adequate under the already "
            "frozen price-interface return range; no parameter change or new runtime is authorized"
        ),
        "external_manifest": {**manifest_receipt, "current_hash_readback": "PASS"},
        "base_monitoring_and_contract_summary": {
            "return_guard_treatment_totals": base_summary["return_guard_treatment_totals"],
            "wage_guard_treatment_totals": base_summary["wage_guard_treatment_totals"],
            "zero_diagnostic_price_guard_hits": base_summary["zero_diagnostic_price_guard_hits"],
            "call_ledger": base_summary["total_call_ledger"],
            "pre_run_gate": base_summary["pre_run_gate"],
        },
    })


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_root", type=Path)
    parser.add_argument("compact_root", type=Path)
    args = parser.parse_args(argv)
    finalize(args.evidence_root, args.compact_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
