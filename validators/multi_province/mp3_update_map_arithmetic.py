"""Independent MP3 source-formula evaluator; never imports production MP3 code."""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

from .mp1_fixture_arithmetic import evaluate_fixture, load_fixture as load_mp1_fixture


CLASSIFICATION = "NON_CALIBRATION_SYNTHETIC_OR_SOURCE_FORMULA_FIXTURE"


def load_fixture(path: str | Path) -> dict[str, Any]:
    with Path(path).open(encoding="utf-8") as stream:
        fixture = json.load(stream)
    if fixture.get("classification") != CLASSIFICATION:
        raise ValueError("MP3 fixture classification mismatch")
    if not isinstance(fixture.get("scenarios"), dict) or not fixture["scenarios"]:
        raise ValueError("MP3 fixture requires named scenarios")
    return fixture


def _scenario_objects(fixture: dict[str, Any], scenario: dict[str, Any], root: Path):
    base = load_mp1_fixture(root / fixture["base_fixture"])
    states = copy.deepcopy(base["provinces"])
    for state in states:
        state.update({"Yt": 1.0, "Yt0": 1.0, "ramin": -10.0, "ramax": 10.0,
                      "wjtmin": 0.01, "wjtmax": 10.0})
    for index, override in enumerate(scenario.get("initial_overrides", [])):
        states[index].update(override)
    batches = scenario["batches"]
    return base, states, batches


def _turn(base: dict[str, Any], states: list[dict[str, Any]], batch: dict[str, Any]):
    provinces = copy.deepcopy(states)
    vector_fields = {"ct": "Ct", "household_lt": "Lt", "at": "At", "bt": "Bt", "at_tax": "AtTax"}
    for source, target in vector_fields.items():
        values = batch.get(source, [p[target] for p in provinces])
        for index, value in enumerate(values):
            provinces[index][target] = value
    turn_fixture = {
        "classification": CLASSIFICATION, "province_order": base["province_order"],
        "params": base["params"], "phi_mat": base["phi_mat"],
        "sigmau_mat": base["sigmau_mat"], "provinces": provinces,
    }
    output = evaluate_fixture(turn_fixture)
    converged = batch.get("converged", [True] * len(provinces))
    updated = []
    for i, old in enumerate(states):
        firm = output["firm"][i]
        state = copy.deepcopy(provinces[i])
        state.update({
            "convergent": bool(converged[i]), "Lt_supply": output["Lt_supply"][i],
            "Kt_supply": output["Kt_supply"][i], "rah": output["rah"][i],
            "w": output["household_composite_wage"][i], "rb": output["rb"],
            "Yt_1": old["Yt"], "Kt_prev": firm["Kt"], "Lt_prev": firm["Lt"],
            "Zt_1": old["Zt"], "pit_1": old["pit"],
        })
        state.update(firm)
        updated.append(state)
    return output, updated, tuple(bool(value) for value in converged)


def evaluate_scenario(fixture: dict[str, Any], name: str, root: str | Path) -> dict[str, Any]:
    scenario = fixture["scenarios"][name]
    base, states, batches = _scenario_objects(fixture, scenario, Path(root))
    n = len(states)
    tkn = [3.0] * n
    history = []
    reason = "SOURCE_MAX_ITERATION_EXHAUSTED"
    max_iterations = int(scenario["max_iterations"])
    for iteration in range(1, max_iterations + 1):
        if iteration > len(batches):
            return {"termination_reason": "MISSING_HOUSEHOLD_BATCH", "iteration_count": iteration - 1,
                    "history": history}
        _, post, flags = _turn(base, states, batches[iteration - 1])
        nk = [abs(post[i]["KNratio"] / tkn[i] - 1.0) for i in range(n)]
        yg = [abs(post[i]["Yt"] / post[i]["Yt_1"] - 1.0) for i in range(n)]
        ra_upper = sum(post[i]["ra"] == post[i]["ramax"] for i in range(n))
        ra_lower = sum(post[i]["ra"] == post[i]["ramin"] for i in range(n))
        wage_upper = sum(post[i]["wjt"] == post[i]["wjtmax"] for i in range(n))
        wage_lower = sum(post[i]["wjt"] == post[i]["wjtmin"] for i in range(n))
        household_count = sum(flags)
        threshold = float(scenario["reg_threshold"])
        accepted = (max(nk) < threshold and max(yg) < threshold and household_count == n
                    and ra_upper == 0 and ra_lower == 0)
        tkn_before = list(tkn)
        actions = []
        if accepted:
            tkn_after = list(tkn)
        else:
            allow = max(nk) < 0.1 and bool(scenario.get("steady_state", True))
            for state in post:
                z_before = state["Zt"]
                g_before = state["GovInv"]
                z_after, g_after, action, z_changed = z_before, g_before, "NONE", False
                if allow:
                    discrepancy = state["Yt"] / state["Yt0"] - 1.0
                    if discrepancy > 0.01 or discrepancy < -0.01:
                        z_after = state["Yt0"] * state["Kt"] ** (-state["alpha"]) * state["Lt"] ** (state["alpha"] - 1.0)
                        state["Zt"], z_changed = z_after, True
                    if state["ra"] < state["ramin"] + 0.02:
                        g_after, action = g_before * 0.9, "LOW_RA_DECREASE_0P9"
                        state["GovInv"] = g_after
                    elif state["ra"] > state["ramax"] - 0.02:
                        g_after, action = g_before * 1.1, "HIGH_RA_INCREASE_1P1"
                        state["GovInv"] = g_after
                actions.append({"province": state["name"], "zt_adjusted": z_changed,
                                "zt_before": z_before, "zt_after": z_after,
                                "govinv_action": action, "govinv_before": g_before,
                                "govinv_after": g_after})
            tkn_after = [0.6 * post[i]["KNratio"] + 0.4 * tkn[i] for i in range(n)]
        if accepted:
            actions = [{"province": state["name"], "zt_adjusted": False,
                        "zt_before": state["Zt"], "zt_after": state["Zt"],
                        "govinv_action": "NONE", "govinv_before": state["GovInv"],
                        "govinv_after": state["GovInv"]} for state in post]
        history.append({
            "iteration": iteration, "nk_ratio_gap": nk, "yt_gap": yg,
            "household_converged_count": household_count,
            "household_all_converged": household_count == n,
            "ra_upper_count": ra_upper, "ra_lower_count": ra_lower,
            "wage_upper_count": wage_upper, "wage_lower_count": wage_lower,
            "converged": accepted, "tkn_ratio_before": tkn_before,
            "tkn_ratio_after": tkn_after, "adaptive_actions": actions,
            "previous_output_yt": [state["Yt_1"] for state in post],
            "new_output_yt": [state["Yt"] for state in post],
        })
        states, tkn = post, tkn_after
        if accepted:
            reason = "SOURCE_CONVERGED"
            break
    return {"termination_reason": reason, "iteration_count": len(history), "history": history,
            "final_state": [{key: state[key] for key in ("name", "Zt", "GovInv", "Yt", "Kt", "Lt", "KNratio")}
                            for state in states]}
