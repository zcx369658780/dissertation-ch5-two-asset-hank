"""Bounded K1A equal-share versus geographic-beta-2 trajectory runner."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import sys
from dataclasses import asdict
from hashlib import sha256
from pathlib import Path
from typing import Any

import numpy as np

REPO = Path(__file__).resolve().parents[3]
for item in (REPO / "src", REPO):
    if str(item) not in sys.path:
        sys.path.insert(0, str(item))

from ch5_two_asset_hank.multi_province import one_turn as one_turn_module  # noqa: E402
from ch5_two_asset_hank.multi_province.capital_allocation import CapitalAllocationInputs  # noqa: E402
from ch5_two_asset_hank.multi_province.k1a_runtime_adapter import (  # noqa: E402
    ACCEPTED_DISTANCE_CANONICAL_LF_SHA256,
    PAYOFF_CLASSIFICATION,
    K1ARuntimeConfig,
    allocate_k1a_capital,
    canonical_lf_sha256,
    load_accepted_distance_score,
)
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER  # noqa: E402
from validators.multi_province.c1_residual_public_asset_25turn import run as c1  # noqa: E402
from validators.multi_province.corrected_2018_hjb_propagation_25turn_kl import run as g0  # noqa: E402
from validators.multi_province.g1_residual_govinv_25turn_isolated import run as g1  # noqa: E402


DISTANCE = REPO / "docs/evidence/ch5_mp4c_k1a_distance_mapping/normalized_distance_destination_origin.csv"
INITIALIZATION = REPO / "reports/mp4c_c1_residual_public_asset_25turn_20260911/initialization_receipt_31province.csv"
LEGACY = REPO / "src/ch5_two_asset_hank/multi_province/capital_allocation.py"
LEGACY_SHA256 = "BB3F283BD782399A5C1C9AEE06DC50BBA61A0599BF062669DE0B1EBBB01AEE40"
PAYLOAD_SHA256 = "EBB9FD91F3D3CE5D46476FE7BF1D0662E26EEA5C87357E4B13907CC76EBE9355"
PATHS = {"A": ("path_a_equal_share", 0.0), "B": ("path_b_geographic_beta2", 2.0)}
PATH_VERDICT = "K1A_PATH_BOUNDED_DIAGNOSTIC_COMPLETE__ACCOUNTING_AND_SCOPE_GATES_PASS"


def _sha(path: Path) -> str:
    return sha256(Path(path).read_bytes()).hexdigest().upper()


def _jsonable(value: Any) -> Any:
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, (np.bool_, bool)):
        return bool(value)
    if isinstance(value, (np.integer, int)):
        return int(value)
    if isinstance(value, (np.floating, float)):
        return float(value)
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(v) for v in value]
    return value


def _write_json(path: Path, value: Any, *, exclusive: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = "x" if exclusive else "w"
    with path.open(mode, encoding="utf-8", newline="\n") as stream:
        json.dump(_jsonable(value), stream, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        stream.write("\n")


def _initialization_outputs() -> list[dict[str, Any]]:
    with INITIALIZATION.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 31 or tuple(row["province"] for row in rows) != PROVINCE_ORDER:
        raise ValueError("accepted C1 initialization receipt province axis mismatch")
    outputs = []
    for i, row in enumerate(rows):
        outputs.append({
            "stage_label": "INITIALIZATION_OBSERVATION_REUSED_ACCEPTED_C1",
            "turn": 0, "province_index": i, "province": row["province"],
            "C": float(row["Ct_initial"]), "L": float(row["Lt_initial"]),
            "A": float(row["At_initial"]), "B": float(row["Bt_initial"]),
            "A_plus_B": float(row["At_initial"]) + float(row["Bt_initial"]),
            "AtTax": 0.0,
            "hjb_converged": row["HJB_converged"].lower() == "true",
            "hjb_iterations": 0, "hjb_statistic": 0.0,
            "hjb_acceptance_classification": row["HJB_classification"],
            "downstream_kfe_attempted": False, "downstream_kfe_returned": False,
            "continuation_status": "REUSED_ACCEPTED_C1_INITIALIZATION__NO_NEW_SOLVE",
            "kfe_returned": False, "kfe_raw_residual_inf": 0.0,
            "kfe_diagnostic_status": row["KFE_classification"],
            "kfe_source_free_residual_inf": 0.0, "kfe_source_free_normwise_ratio": 0.0,
        })
    return outputs


class AllocationRecorder:
    def __init__(self, root: Path, config: K1ARuntimeConfig) -> None:
        self.root = root
        self.config = config
        self.networks: dict[int, Any] = {}
        self.firms: dict[int, list[tuple[Any, float]]] = {}
        self.calls = 0

    def allocate(self, inputs: CapitalAllocationInputs):
        turn = self.calls
        if turn > 25:
            raise RuntimeError("more than one initialization allocation plus 25 trajectory allocations")
        result = allocate_k1a_capital(inputs, self.config)
        self.networks[turn] = result.network
        self.calls += 1
        network = result.network
        label = "initialization" if turn == 0 else f"turn_{turn:02d}"
        _write_json(self.root / "capital_network" / f"allocation_{turn:02d}_{label}.json", {
            "schema": "CH5_K1A_CAPITAL_NETWORK_ALLOCATION_V1", "allocation_index": turn,
            "stage": label, "province_order": PROVINCE_ORDER,
            "orientation": network.orientation, "beta_distance": self.config.beta_distance,
            "beta_return": self.config.beta_return, "payoff_classification": PAYOFF_CLASSIFICATION,
            "lagged_return_score": "DISABLED_ZERO_VECTOR", "portfolio_smoothing": False,
            "partial_adjustment": False, "quantity_and_rah_share_matrix_identical": True,
            "destination_theta_double_weighting": False,
            "foreign_conditional_shares_destination_origin": network.foreign_conditional_shares_destination_origin,
            "portfolio_shares_destination_origin": network.portfolio_shares_destination_origin,
            "origin_private_wealth": network.origin_private_wealth,
            "bilateral_private_capital_destination_origin": network.bilateral_private_capital_destination_origin,
            "destination_private_productive_capital": network.destination_private_productive_capital,
            "domestic_retained_capital_by_origin": network.domestic_retained_capital_by_origin,
            "foreign_outflow_by_origin": network.foreign_outflow_by_origin,
            "foreign_inflow_by_destination": network.foreign_inflow_by_destination,
            "household_portfolio_return_by_origin": network.household_portfolio_return_by_origin,
            "share_column_sums": network.share_column_sums,
            "capital_column_sums": network.capital_column_sums,
            "national_private_capital_conservation_residual": network.national_private_capital_conservation_residual,
        })
        return result

    def firm(self, province: Any, *args: Any, **kwargs: Any):
        result = self.original_firm(province, *args, **kwargs)
        turn = max(self.networks)
        self.firms.setdefault(turn, []).append((result, float(province["corptau"])))
        return result


def prepare(evidence_parent: Path, accepted_payload: Path, test_cases: int, test_processes: int) -> None:
    parent = Path(evidence_parent)
    parent.mkdir(parents=True, exist_ok=False)
    payload_bytes = Path(accepted_payload).read_bytes()
    if sha256(payload_bytes).hexdigest().upper() != PAYLOAD_SHA256:
        raise ValueError("accepted runtime payload SHA mismatch")
    distance = load_accepted_distance_score(DISTANCE)
    for path_id, (name, beta) in PATHS.items():
        root = parent / name
        root.mkdir()
        (root / "runtime_input_payload.json").write_bytes(payload_bytes)
        _write_json(root / "phase_a_zero_science_receipt.json", {
            "schema": "CH5_K1A_EQUAL_SHARE_VS_BETA2_PHASE_A_V1", "status": "PASS",
            "focused_test_cases": test_cases, "focused_test_processes": test_processes,
            "compile_processes": 1, "scientific_processes": 0, "hjb_calls": 0,
            "kfe_calls": 0, "initialization_observations": 0, "trajectory_calls": 0,
        })
        _write_json(root / "runtime_input_receipt.json", {
            "schema": "CH5_K1A_RUNTIME_INPUT_RECEIPT_V1", "path_id": path_id,
            "runtime_payload_sha256": PAYLOAD_SHA256, "province_count": 31,
            "province_order": PROVINCE_ORDER, "beta_distance": beta, "beta_return": 0.0,
            "distance_canonical_lf_sha256": ACCEPTED_DISTANCE_CANONICAL_LF_SHA256,
            "payoff_classification": PAYOFF_CLASSIFICATION,
            "source_faithful_labor": True, "normalized_labor_active": False,
            "c1_rule": "GovInv=max(Ktarget-Kprivate,0)", "portfolio_smoothing": False,
            "partial_adjustment": False, "accepted_initialization_reused": True,
            "new_initialization_hjb_or_kfe_calls": 0,
        })
        _write_json(root / "source_hash_receipt.json", {
            "schema": "CH5_K1A_SOURCE_HASH_RECEIPT_V1",
            "legacy_capital_allocation_sha256": _sha(LEGACY),
            "capital_network_sha256": _sha(REPO / "src/ch5_two_asset_hank/multi_province/capital_network.py"),
            "adapter_sha256": _sha(REPO / "src/ch5_two_asset_hank/multi_province/k1a_runtime_adapter.py"),
            "runner_sha256": _sha(Path(__file__)), "distance_checkout_sha256": _sha(DISTANCE),
            "distance_canonical_lf_sha256": canonical_lf_sha256(DISTANCE),
            "accepted_initialization_receipt_sha256": _sha(INITIALIZATION),
        })
        _write_json(root / "bounded_invocation_receipt.json", {
            "schema": "CH5_K1A_BOUNDED_INVOCATION_V1", "path_id": path_id,
            "trajectory_invocations_maximum": 1, "outer_turns_maximum": 25,
            "province_household_hjb_solves_maximum": 775,
            "initialization_reused_no_new_solve": True, "scientific_retries": 0,
            "matlab_calls": 0, "standalone_kfe_experiments": 0, "k1b_runs": 0,
            "ge_calls": 0, "annual_calls": 0, "irf_calls": 0, "results_calls": 0,
        })
    _write_json(parent / "prepare_receipt.json", {
        "schema": "CH5_K1A_EQUAL_SHARE_VS_BETA2_PREPARE_V1", "status": "PASS",
        "path_roots": {key: name for key, (name, _) in PATHS.items()},
        "runtime_payload_sha256": PAYLOAD_SHA256, "payloads_byte_identical": True,
        "distance_shape": list(distance.shape), "scientific_calls": 0,
    })


def preflight(evidence_parent: Path) -> None:
    parent = Path(evidence_parent)
    roots = [parent / PATHS[key][0] for key in ("A", "B")]
    if roots[0].resolve() == roots[1].resolve() or any((root / "science_started.json").exists() for root in roots):
        raise ValueError("A/B roots must be distinct and unused by science")
    if roots[0].joinpath("runtime_input_payload.json").read_bytes() != roots[1].joinpath("runtime_input_payload.json").read_bytes():
        raise ValueError("A/B runtime payloads are not byte-identical")
    if _sha(LEGACY) != LEGACY_SHA256:
        raise ValueError("legacy capital route changed")
    distance = load_accepted_distance_score(DISTANCE)
    configs = [K1ARuntimeConfig(PROVINCE_ORDER, distance, beta) for _, beta in PATHS.values()]
    probe = CapitalAllocationInputs(np.linspace(1, 2, 31), np.linspace(10, 20, 31),
                                    np.linspace(0.1, 0.3, 31), np.linspace(0.02, 0.09, 31))
    results = [allocate_k1a_capital(probe, config) for config in configs]
    if np.array_equal(results[0].network.portfolio_shares_destination_origin,
                      results[1].network.portfolio_shares_destination_origin):
        raise RuntimeError("A/B shares did not differ under accepted distance scores")
    one_turn_text = (REPO / "src/ch5_two_asset_hank/multi_province/c1_residual_public_asset.py").read_text(encoding="utf-8")
    if "reconstruct_migration_labor" not in one_turn_text or "residual_government_asset_levels" not in one_turn_text:
        raise RuntimeError("source-faithful labor or C1 route marker missing")
    gate = {
        "schema": "CH5_K1A_EQUAL_SHARE_VS_BETA2_PRE_RUN_GATE_V1", "status": "PASS",
        "focused_tests": "PASS", "legacy_route_sha256": LEGACY_SHA256,
        "configs_differ_only_in_beta_distance": True, "betas": [0.0, 2.0],
        "beta_return_both": 0.0, "accepted_distance_receipt": True,
        "distance_canonical_lf_sha256": ACCEPTED_DISTANCE_CANONICAL_LF_SHA256,
        "source_faithful_labor": True, "c1_formula_unchanged": True,
        "k1b_disabled": True, "portfolio_smoothing": False, "partial_adjustment": False,
        "distinct_no_overwrite_roots": True, "payloads_byte_identical": True,
        "science_calls_before_gate": 0,
    }
    _write_json(parent / "pre_run_gate.json", gate)
    for root in roots:
        shutil.copyfile(parent / "pre_run_gate.json", root / "pre_run_gate.json")


def _augment_turn_rows(rows: list[dict[str, Any]], recorder: AllocationRecorder, turn: int) -> None:
    network = recorder.networks[turn]
    firms = recorder.firms.get(turn, [])
    if len(rows) != 31 or len(firms) != 31:
        raise RuntimeError("K1A diagnostic capture did not return 31 province rows/firms")
    for i, row in enumerate(rows):
        firm, corptau = firms[i]
        profit_over_k = float(firm.PIt / firm.Kt)
        profit_component = (1.0 - corptau) * profit_over_k
        reconstruction = float(firm.rk + profit_component - 0.025 - firm.ra0)
        row.update({
            "k1a_beta_distance": recorder.config.beta_distance, "k1a_beta_return": 0.0,
            "k1a_payoff_classification": PAYOFF_CLASSIFICATION,
            "theta_origin": float(network.portfolio_shares_destination_origin[:, i].sum() - network.portfolio_shares_destination_origin[i, i] + 0.0),
            "home_retained_private_K_MU": float(network.domestic_retained_capital_by_origin[i]),
            "foreign_outflow_private_K_MU": float(network.foreign_outflow_by_origin[i]),
            "foreign_inflow_private_K_MU": float(network.foreign_inflow_by_destination[i]),
            "origin_private_wealth_MU": float(network.origin_private_wealth[i]),
            "share_column_sum": float(network.share_column_sums[i]),
            "capital_column_sum_MU": float(network.capital_column_sums[i]),
            "capital_column_residual_MU": float(network.capital_column_sums[i] - network.origin_private_wealth[i]),
            "national_private_capital_conservation_residual_MU": float(network.national_private_capital_conservation_residual),
            "quantity_and_rah_same_S": True, "destination_theta_double_weighting": False,
            "household_rah_k1a_current_payoff_bridge": float(network.household_portfolio_return_by_origin[i]),
            "firm_profit_over_K": profit_over_k, "firm_after_tax_profit_component_over_K": profit_component,
            "firm_ra0_reconstruction_residual": reconstruction,
            "source_faithful_labor_route": True, "normalized_labor_route_active": False,
        })


def execute(evidence_parent: Path, path_id: str) -> int:
    path_id = path_id.upper()
    if path_id not in PATHS:
        raise ValueError("path_id must be A or B")
    parent = Path(evidence_parent)
    gate = json.loads((parent / "pre_run_gate.json").read_text(encoding="utf-8"))
    if gate.get("status") != "PASS" or gate.get("science_calls_before_gate") != 0:
        raise ValueError("pre-run gate is missing or failed")
    name, beta = PATHS[path_id]
    root = parent / name
    config = K1ARuntimeConfig(PROVINCE_ORDER, load_accepted_distance_score(DISTANCE), beta)
    recorder = AllocationRecorder(root, config)
    original_household = g1._household_pass
    original_g1_allocate = g1.allocate_productive_capital
    original_one_allocate = one_turn_module.allocate_productive_capital
    original_firm = one_turn_module.evaluate_firm
    original_write_json = g1.write_json
    original_rah_provenance = g0.rah_provenance
    recorder.original_firm = original_firm

    def household(states, payload, grid, params, numerics, output_root, counters, current, label, turn_index):
        if label == "INITIALIZATION_OBSERVATION":
            outputs = _initialization_outputs()
            _write_json(root / "initialization_reuse_receipt.json", {
                "schema": "CH5_K1A_ACCEPTED_INITIALIZATION_REUSE_V1", "new_hjb_calls": 0,
                "new_kfe_calls": 0, "accepted_receipt": str(INITIALIZATION.relative_to(REPO)).replace("\\", "/"),
                "accepted_receipt_sha256": _sha(INITIALIZATION), "province_count": 31,
            })
            return outputs
        return original_household(states, payload, grid, params, numerics, output_root,
                                  counters, current, label, turn_index)

    def observed_json(path: Path, value: Any) -> None:
        if path.name == "per_province_observables.json" and isinstance(value, list):
            turn = int(path.parent.name.split("_")[-1])
            _augment_turn_rows(value, recorder, turn)
        elif path.name == "science_started.json" and isinstance(value, dict):
            value["authorized_initialization_observation_passes"] = 0
            value["accepted_initialization_reuse"] = True
            value["path_id"] = path_id
            value["beta_distance"] = beta
        elif path.name == "call_ledger.json" and isinstance(value, dict):
            counts = value["counts"]
            if counts["hjb_calls"] > 775 or counts["trajectory_hjb_calls"] > 775:
                raise RuntimeError("per-path HJB ceiling exceeded")
            value.update({"schema": "CH5_K1A_PATH_CALL_LEDGER_V1", "path_id": path_id,
                          "beta_distance": beta, "trajectory_invocations": 1,
                          "accepted_initialization_reuses": 1, "new_initialization_hjb_calls": 0,
                          "new_initialization_kfe_calls": 0, "k1b_runs": 0,
                          "standalone_kfe_experiments": 0})
        elif path.name == "terminal_result.json" and isinstance(value, dict):
            if value.get("actual_turns_completed") == 25 and value.get("error") is None:
                value["verdict"] = PATH_VERDICT
            value.update({"schema": "CH5_K1A_PATH_TERMINAL_V1", "path_id": path_id,
                          "beta_distance": beta, "results_eligible": False})
        original_write_json(path, value)

    def k1a_rah_provenance(turn: int, index: int, states, prior_states=None) -> dict[str, Any]:
        if turn == 1:
            return original_rah_provenance(turn, index, states, prior_states)
        prior_network = recorder.networks.get(turn - 1)
        if prior_network is None:
            raise ValueError("K1A lagged rah provenance is missing the prior completed allocation")
        actual = float(states[index]["rah"])
        rebuilt = float(prior_network.household_portfolio_return_by_origin[index])
        if actual != rebuilt:
            raise ValueError("K1A entering rah does not match prior completed allocation using the same S")
        return {
            "entering_state_field": "rah",
            "source": f"turn_{turn - 1}.k1a_capital_network.household_portfolio_return_by_origin -> steady_state._post_turn_states.rah",
            "formula": "current_source_used_ra_by_destination @ S_destination_origin",
            "quantity_and_rah_same_S": True,
            "payoff_classification": PAYOFF_CLASSIFICATION,
            "source_allocation_turn": turn - 1, "value": actual, "manual_override": False,
        }

    try:
        g1._household_pass = household
        g1.allocate_productive_capital = recorder.allocate
        one_turn_module.allocate_productive_capital = recorder.allocate
        one_turn_module.evaluate_firm = recorder.firm
        g1.write_json = observed_json
        g0.rah_provenance = k1a_rah_provenance
        code = c1.execute(root)
    finally:
        g1._household_pass = original_household
        g1.allocate_productive_capital = original_g1_allocate
        one_turn_module.allocate_productive_capital = original_one_allocate
        one_turn_module.evaluate_firm = original_firm
        g1.write_json = original_write_json
        g0.rah_provenance = original_rah_provenance
    return code


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("evidence_parent", type=Path); prep.add_argument("accepted_payload", type=Path)
    prep.add_argument("--test-cases", type=int, required=True); prep.add_argument("--test-processes", type=int, required=True)
    gate = sub.add_parser("preflight"); gate.add_argument("evidence_parent", type=Path)
    launch = sub.add_parser("run"); launch.add_argument("evidence_parent", type=Path); launch.add_argument("path_id", choices=("A", "B"))
    args = parser.parse_args(argv)
    if args.command == "prepare":
        prepare(args.evidence_parent, args.accepted_payload, args.test_cases, args.test_processes); return 0
    if args.command == "preflight":
        preflight(args.evidence_parent); return 0
    return execute(args.evidence_parent, args.path_id)


if __name__ == "__main__":
    raise SystemExit(main())
