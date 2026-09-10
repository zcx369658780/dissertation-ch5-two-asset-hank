"""Prepare and run exactly one corrected-2018 three-turn trajectory."""
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

VERDICT_PASS = "CORRECTED_2018_THREE_TURN_PASS__DIRECT_CORRECTED_RATE_PROPAGATION_OBSERVED"
VERDICT_MISMATCH = "CORRECTED_2018_THREE_TURN_FAIL__PREDECESSOR_REPRODUCTION_MISMATCH"
VERDICT_HOUSEHOLD = "CORRECTED_2018_THREE_TURN_FAIL__HOUSEHOLD_OR_NUMERICAL_BLOCKER"
VERDICT_UPSTREAM = "CORRECTED_2018_THREE_TURN_FAIL__UPSTREAM_STATE_OR_FIRM_BLOCKER"
ACCEPTED_DIR = REPO / "reports/mp4c_2018_corrected_two_turn_20260909"
ACCEPTED_SHA256 = {
    "turn_by_turn_observables": "42D420D6BEAEE25941D9E304E89C0B5EE84DF1189949AF7BB12C8652D1A71B0A",
    "transition_summary": "54B4F9D58D32A2B48B6C97F37C633FAB939F4BA2C5BB9D76A67B2F52EC9E12AF",
    "manifest": "B4B3D643D573ECBA12F5EF5F407CADA3300401FAD9C039740641B3C0859305C7",
}
THREAD_ENV = ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS")


def write_json(path: Path, value: Any) -> None:
    single.write_json(path, value)


def _canonical_bytes(value: Any) -> bytes:
    return (json.dumps(single.jsonable(value), ensure_ascii=False, sort_keys=True,
                       separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def _value_sha(value: Any) -> str:
    return sha256(_canonical_bytes(value)).hexdigest().upper()


def prepare(distance_workbook: Path, evidence_root: Path) -> None:
    root = Path(evidence_root)
    root.mkdir(parents=True, exist_ok=False)
    payload = single.build_runtime_payload(distance_workbook)
    payload["schema"] = "CH5_CORRECTED_2018_THREE_TURN_RUNTIME_INPUT_V1"
    payload_path = root / "runtime_input_payload.json"
    write_json(payload_path, payload)
    accepted_paths = {
        "turn_by_turn_observables": ACCEPTED_DIR / "turn_by_turn_observables.json",
        "transition_summary": ACCEPTED_DIR / "transition_summary.json",
        "manifest": ACCEPTED_DIR / "manifest.json",
    }
    if not all(path.is_file() for path in accepted_paths.values()):
        raise ValueError("accepted turn-1 evidence is missing")
    accepted_actual = {name: single.file_sha256(path) for name, path in accepted_paths.items()}
    if accepted_actual != ACCEPTED_SHA256:
        raise ValueError(f"accepted turn-1 evidence identity mismatch: {accepted_actual}")
    write_json(root / "runtime_input_receipt.json", {
        "schema": "CH5_CORRECTED_2018_THREE_TURN_RUNTIME_RECEIPT_V1",
        "corrected_source_identities": payload["source_identities"],
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
        "schema": "CH5_CORRECTED_2018_THREE_TURN_SOURCE_IDENTITY_V1",
        "files": {str(path.relative_to(REPO)).replace("\\", "/"): single.file_sha256(path)
                  for path in (Path(__file__), Path(single.__file__),
                               REPO / "exports/matlab_faithful_two_asset_ha.py",
                               REPO / "src/ch5_two_asset_hank/multi_province/one_turn.py",
                               REPO / "src/ch5_two_asset_hank/multi_province/steady_state.py",
                               REPO / "src/ch5_two_asset_hank/multi_province/firm.py")},
        "scientific_calls": 0,
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
    raw_wage = np.array([row["firm_wage_raw"] for row in rows], dtype=float)
    rah = np.array([row["household_rah"] for row in rows], dtype=float)
    nk = np.array([row["nk_gap"] for row in rows], dtype=float)
    yt = np.array([row["yt_gap"] for row in rows], dtype=float)
    rate_regions = Counter("lower" if row["firm_ra0"] < row["ramin"] else
                           "upper" if row["firm_ra0"] > row["ramax"] else "interior" for row in rows)
    wage_regions = Counter("lower" if row["firm_wage_raw"] < row["wjtmin"] else
                           "upper" if row["firm_wage_raw"] > row["wjtmax"] else "interior" for row in rows)
    def stats(values: np.ndarray) -> dict[str, float]:
        return {"min": float(np.min(values)), "median": float(np.median(values)), "max": float(np.max(values))}
    return {
        "turn": turn,
        "firm_rate_regions": {key: rate_regions.get(key, 0) for key in ("lower", "interior", "upper")},
        "wage_regions": {key: wage_regions.get(key, 0) for key in ("lower", "interior", "upper")},
        "raw_ra0": {**stats(raw_ra), "min_province": rows[int(np.argmin(raw_ra))]["province"],
                    "max_province": rows[int(np.argmax(raw_ra))]["province"]},
        "raw_wage": stats(raw_wage), "household_rah": stats(rah),
        "nk_gap": stats(nk), "yt_gap": stats(yt),
        "hjb_iterations": stats(np.array([row["hjb_iterations"] for row in rows], dtype=float)),
        "hjb_iteration_distribution": dict(sorted(Counter(str(row["hjb_iterations"]) for row in rows).items())),
        "hjb_failures": sum(not row["hjb_converged"] for row in rows),
        "kfe_failures": sum(not row["kfe_returned"] for row in rows),
        "controller": {"adaptation_gate_open": controller["adaptation_allowed"],
                       "zt_adjusted_count": sum(action["zt_adjusted"] for action in controller["actions"]),
                       "govinv_action_counts": dict(Counter(action["govinv_action"] for action in controller["actions"]))},
    }


def execute(evidence_root: Path) -> int:
    root = Path(evidence_root)
    payload_path = root / "runtime_input_payload.json"
    if not payload_path.is_file() or not (root / "runtime_input_receipt.json").is_file():
        raise ValueError("prepared runtime input is missing")
    if (root / "science_started.json").exists():
        raise RuntimeError("scientific trajectory already started; retry prohibited")
    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    single.validate_serialized_payload(payload)
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
        "schema": "CH5_CORRECTED_2018_THREE_TURN_LAUNCH_V1",
        "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "process_id": os.getpid(), "python": sys.version, "platform": platform.platform(),
        "thread_environment": {key: os.environ.get(key) for key in THREAD_ENV},
        "authorized_trajectory_count": 1, "authorized_turns": 3, "scientific_retries": 0,
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
    verdict = VERDICT_HOUSEHOLD
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
        for turn_index in (1, 2, 3):
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
                if not all(np.isfinite(float(output[key])) for key in
                           ("hjb_statistic", "kfe_raw_residual_inf", "C", "L", "A", "B", "A_plus_B", "AtTax")):
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
                    "nk_gap": nk_gap[index], "yt_gap": yt_gap[index],
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
            if turn_index in (1, 2):
                reproduction = compare_predecessor(turn_index, rows, summary)
                predecessor_reproduction.append(reproduction)
                write_json(root / f"turn{turn_index}_reproduction.json", reproduction)
                if not reproduction["passed"] or turn_index == 2:
                    write_json(root / "predecessor_reproduction.json", {
                        "schema": "CH5_CORRECTED_2018_PREDECESSOR_REPRODUCTION_V1",
                        "turns": predecessor_reproduction,
                        "passed": all(item["passed"] for item in predecessor_reproduction),
                    })
                if not reproduction["passed"]:
                    verdict = VERDICT_MISMATCH
                    break
            prior_entering_states = states
            states = _freeze_state(next_states)
            tkn_ratio = tkn_after
        else:
            verdict = VERDICT_PASS
            counters["trajectory_returns"] = 1
    except Exception as exc:
        counters["household_calls_failed"] = counters["household_calls_attempted"] - counters["household_calls_returned"]
        error = {"type": type(exc).__name__, "message": str(exc), "turn": current["turn"],
                 "stage": current["stage"], "province_index": current["province_index"],
                 "province": current["province"]}
        verdict = VERDICT_UPSTREAM if current["stage"] in ("ONE_TURN", "FIRM", "CONTROLLER") else VERDICT_HOUSEHOLD
        write_json(root / "scientific_failure.json", error)
    finally:
        single.oracle.linalg.spsolve = original_spsolve
        single.LABOR_BRENTQ = original_brentq
    counters["household_calls_failed"] = counters["household_calls_attempted"] - counters["household_calls_returned"]
    write_json(root / "transition_summary.json", {"schema": "CH5_CORRECTED_2018_THREE_TURN_TRANSITION_V1",
        "turns": turn_summaries, "turn3_completed": counters["turns_completed"] == 3})
    write_json(root / "call_ledger.json", {"schema": "CH5_CORRECTED_2018_THREE_TURN_CALL_LEDGER_V1",
        "counts": counters, "elapsed_seconds": time.monotonic() - started, "failed_calls_counted": True,
        "matlab_calls": 0, "fourth_or_later_turns": 0, "steady_state_calls": 0, "ge_calls": 0,
        "annual_model_calls": 0, "irf_calls": 0, "results_calls": 0})
    write_json(root / "terminal_result.json", {"schema": "CH5_CORRECTED_2018_THREE_TURN_TERMINAL_V1",
        "verdict": verdict, "error": error, "turn4_authorized": "NO",
        "steady_state_authorized": "NO", "results_eligible": False})
    return 0 if verdict == VERDICT_PASS else 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(); sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("distance_workbook", type=Path); prep.add_argument("evidence_root", type=Path)
    launch = sub.add_parser("run"); launch.add_argument("evidence_root", type=Path)
    args = parser.parse_args(argv)
    if args.command == "prepare":
        prepare(args.distance_workbook, args.evidence_root); return 0
    return execute(args.evidence_root)


if __name__ == "__main__":
    raise SystemExit(main())
