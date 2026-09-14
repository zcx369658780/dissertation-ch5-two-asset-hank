"""Execute the frozen Stage A and conditionally authorized Stage B diagnostic.

The accepted MATLAB-faithful HJB/KFE implementation is imported unchanged.
This runner changes only household asset-grid endpoints in task-owned fixtures.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np

from exports import matlab_faithful_two_asset_ha as oracle
from validators.multi_province.corrected_2018_single_turn.run import source_initial_arrays
from validators.multi_province.k1_real_composite_wage_domain_macro_scale import run as accepted
from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import run as coarse


REPO = Path(__file__).resolve().parents[3]
POINTS = tuple(
    (ra, wage)
    for ra in (0.06, 0.0675, 0.07)
    for wage in (13.0, 15.5, 18.0)
)
ORACLE_PATH = REPO / "exports/matlab_faithful_two_asset_ha.py"
ORACLE_SHA256 = "F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8"
MATLAB_PATH = Path(
    r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m"
)
MATLAB_SHA256 = "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE"
BASELINE_INPUT = (
    REPO
    / "docs/evidence/ch5_mp4c_k1_real_composite_wage_domain_macro_scale_audit"
    / "input_invariance_receipt.json"
)


def stage_spec(stage: str) -> dict[str, Any]:
    if stage not in {"A", "B"}:
        raise ValueError("stage must be A or B")
    bmax = 20.0 if stage == "A" else 50.0
    return {
        "stage": stage,
        "amin": 0.0,
        "amax": 100.0,
        "bmin": -2.0,
        "bmax": bmax,
        "I": 20,
        "J": 20,
        "Nz": 2,
        "da": 100.0 / 19.0,
        "db": (bmax + 2.0) / 19.0,
    }


def build_fixture(stage: str, ra: float, wage: float) -> coarse.Fixture:
    if (ra, wage) not in POINTS:
        raise ValueError("parameter point is outside the preregistered grid")
    spec = stage_spec(stage)
    grid = oracle.MatlabFaithfulHJBGrid(
        np.linspace(spec["bmin"], spec["bmax"], spec["I"]),
        np.linspace(spec["amin"], spec["amax"], spec["J"]),
        np.array([0.8, 1.3]),
        np.array([[-1.0 / 3.0, 1.0 / 3.0], [1.0 / 3.0, -1.0 / 3.0]]),
    )
    params = oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    state = {
        "rah": ra,
        "rb": 0.02,
        "rb_gap": 0.07,
        "Tt": 0.1,
        "tau": 0.05,
        "w": wage,
    }
    initial_value, baseline_labor = source_initial_arrays(state, grid, params)
    inputs = oracle.HouseholdInputs(
        ra, 0.02, 0.05, np.array([wage]), np.zeros(1), np.ones(1)
    )
    numerics = oracle.MatlabFaithfulHJBNumerics(1000.0, 1e-7, 100, 1e-12)
    return coarse.Fixture(
        grid,
        params,
        inputs,
        initial_value,
        baseline_labor,
        0.1,
        0.07,
        numerics,
    )


def kfe_valid(point: dict[str, Any]) -> bool:
    if point.get("hjb", {}).get("classification") != "HJB_CONVERGED":
        return False
    kfe = point.get("kfe", {})
    distribution = kfe.get("distribution", {})
    residual = kfe.get("kfe", {}).get("raw_residual_inf")
    rounding_band = 100.0 * np.finfo(float).eps
    return bool(
        kfe.get("ran")
        and kfe.get("completed", True)
        and distribution.get("density_finite", False)
        and np.isfinite(float(distribution.get("total_mass", np.nan)))
        and float(distribution.get("total_mass", 0.0)) > 0.0
        and np.isfinite(float(distribution.get("density_min", np.nan)))
        and float(distribution.get("density_min", -np.inf)) >= -rounding_band
        and residual is not None
        and np.isfinite(float(residual))
    )


def stage_b_trigger(points: list[dict[str, Any]], *, bmax: float) -> dict[str, Any]:
    triggering = []
    for point in points:
        modes = point.get("kfe", {}).get("distribution", {}).get("modal_b", [])
        if kfe_valid(point) and any(float(value) == float(bmax) for value in modes):
            triggering.append(point.get("point_id"))
    return {
        "rule": "at least one HJB-converged KFE-valid point has raw modal_b containing exact stage bmax",
        "inspected_field": "kfe.distribution.modal_b",
        "bmax": float(bmax),
        "trigger": bool(triggering),
        "triggering_point_ids": triggering,
        "post_result_percentage_threshold": False,
    }


def _source_receipt() -> dict[str, Any]:
    receipt = {
        "oracle": {
            "path": ORACLE_PATH,
            "expected_sha256": ORACLE_SHA256,
            "actual_sha256": coarse.file_sha256(ORACLE_PATH),
        },
        "matlab": {
            "path": MATLAB_PATH,
            "expected_sha256": MATLAB_SHA256,
            "actual_sha256": coarse.file_sha256(MATLAB_PATH),
        },
        "accepted_runner": {
            "path": Path(accepted.__file__).resolve(),
            "sha256": coarse.file_sha256(Path(accepted.__file__)),
        },
        "accepted_baseline_input": {
            "path": BASELINE_INPUT.resolve(),
            "sha256": coarse.file_sha256(BASELINE_INPUT),
        },
        "matlab_runtime_calls": 0,
    }
    receipt["pass"] = all(
        item["expected_sha256"] == item["actual_sha256"]
        for key, item in receipt.items()
        if key in {"oracle", "matlab"}
    )
    return receipt


def _invariance_receipt(
    stage: str,
    fixtures: list[coarse.Fixture],
    prior_config: dict[str, Any] | None = None,
) -> dict[str, Any]:
    receipt = coarse.input_invariance_receipt(fixtures)
    receipt.update(
        {
            "stage": stage,
            "stage_spec": stage_spec(stage),
            "temporary_household_bridge_h": 1.0,
            "fresh_initial_value_object_count": len(
                {id(item.initial_value) for item in fixtures}
            ),
            "fresh_baseline_labor_object_count": len(
                {id(item.baseline_labor) for item in fixtures}
            ),
            "initial_arrays": [
                {
                    "r_a": ra,
                    "wage": wage,
                    "initial_value_sha256": coarse.array_sha256(fixture.initial_value),
                    "baseline_labor_sha256": coarse.array_sha256(
                        fixture.baseline_labor
                    ),
                    "initial_value_finite": bool(
                        np.isfinite(fixture.initial_value).all()
                    ),
                    "baseline_labor_finite": bool(
                        np.isfinite(fixture.baseline_labor).all()
                    ),
                }
                for (ra, wage), fixture in zip(POINTS, fixtures)
            ],
        }
    )
    if prior_config is not None:
        current = coarse.fixture_config(fixtures[0])
        receipt["changed_fields_vs_prior_stage_or_old_domain"] = sorted(
            key for key in current if current[key] != prior_config[key]
        )
    return receipt


def _validate_invariance(receipt: dict[str, Any], expected_changed: list[str]) -> None:
    if (
        receipt["unexpected_varying_fields"]
        or not receipt["all_non_scanned_fields_identical"]
        or receipt["fresh_initial_value_object_count"] != 9
        or receipt["fresh_baseline_labor_object_count"] != 9
        or any(
            not item["initial_value_finite"] or not item["baseline_labor_finite"]
            for item in receipt["initial_arrays"]
        )
        or receipt.get("changed_fields_vs_prior_stage_or_old_domain")
        != expected_changed
    ):
        raise RuntimeError("input invariance/fresh initialization preflight failed")


def _run_stage(
    root: Path,
    stage: str,
    fixtures: list[coarse.Fixture],
    ledger: dict[str, Any],
) -> list[dict[str, Any]]:
    points: list[dict[str, Any]] = []
    for index, ((ra, wage), fixture) in enumerate(zip(POINTS, fixtures), start=1):
        point_id = (
            f"stage_{stage.lower()}_p{index:02d}_ra_{ra:.4f}_w_{wage:.1f}"
            .replace(".", "p")
        )
        coarse.write_json(
            root / f"{point_id}_started.json",
            {
                "stage": stage,
                "stage_point_index": index,
                "point_id": point_id,
                "r_b": 0.02,
                "r_a": ra,
                "wage": wage,
                "fresh_initialization": True,
                "initial_value_sha256": coarse.array_sha256(fixture.initial_value),
                "baseline_labor_sha256": coarse.array_sha256(fixture.baseline_labor),
            },
        )
        ledger["hjb_calls_started"] += 1
        ledger["stages"][stage]["hjb_calls_started"] += 1
        hjb, hjb_receipt = coarse.run_hjb(fixture)
        ledger["hjb_calls_completed"] += 1
        ledger["stages"][stage]["hjb_calls_completed"] += 1
        point = {
            "stage": stage,
            "stage_point_index": index,
            "point_id": point_id,
            "r_b": 0.02,
            "r_a": ra,
            "wage": wage,
            "domain": stage_spec(stage),
            "fresh_initialization": {
                "used": True,
                "source": "source_initial_arrays",
                "warm_start": False,
                "initial_value_sha256": coarse.array_sha256(fixture.initial_value),
                "baseline_labor_sha256": coarse.array_sha256(fixture.baseline_labor),
            },
            "hjb": hjb_receipt,
            "kfe": {"ran": False},
        }
        if coarse.kfe_authorized(hjb_receipt["classification"]):
            assert hjb is not None
            ledger["kfe_calls_started"] += 1
            ledger["stages"][stage]["kfe_calls_started"] += 1
            try:
                kfe, _, kfe_receipt = accepted.run_kfe(fixture, hjb)
                kfe_receipt["completed"] = True
                point["kfe"] = kfe_receipt
                ledger["kfe_calls_completed"] += 1
                ledger["stages"][stage]["kfe_calls_completed"] += 1
                np.savez_compressed(
                    root / f"{point_id}_scientific_arrays.npz",
                    value=hjb.value,
                    consumption=hjb.consumption,
                    labor=hjb.labor,
                    transfer=hjb.transfer,
                    mu_a=hjb.mu_a,
                    mu_b=hjb.mu_b,
                    density=kfe.density,
                )
            except Exception as exc:
                point["kfe"] = {
                    "ran": True,
                    "completed": False,
                    "hard_error": f"{type(exc).__name__}: {exc}",
                }
        coarse.write_json(root / f"{point_id}_result.json", point)
        ledger["points"].append(
            {
                "stage": stage,
                "stage_point_index": index,
                "point_id": point_id,
                "hjb_classification": hjb_receipt["classification"],
                "kfe_ran": bool(point["kfe"]["ran"]),
                "kfe_valid": kfe_valid(point),
            }
        )
        points.append(point)
    return points


def execute(evidence_root: Path) -> int:
    root = Path(evidence_root)
    root.mkdir(parents=True, exist_ok=False)

    source = _source_receipt()
    coarse.write_json(root / "source_identity.json", source)
    if not source["pass"]:
        raise RuntimeError("source identity preflight failed before HJB")

    old_receipt = json.loads(BASELINE_INPUT.read_text(encoding="utf-8"))
    old_config = old_receipt["configurations"][0]

    stage_a_fixtures = [build_fixture("A", ra, wage) for ra, wage in POINTS]
    stage_a_invariance = _invariance_receipt("A", stage_a_fixtures, old_config)
    _validate_invariance(stage_a_invariance, ["grid.a", "grid.b"])
    coarse.write_json(root / "stage_a_input_invariance.json", stage_a_invariance)

    ledger = {
        "schema": "CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_LEDGER_V1",
        "hjb_budget": {"stage_a": 9, "stage_b_if_triggered": 9},
        "kfe_budget": {"stage_a": 9, "stage_b_if_triggered": 9},
        "hjb_calls_started": 0,
        "hjb_calls_completed": 0,
        "kfe_calls_started": 0,
        "kfe_calls_completed": 0,
        "scientific_retries": 0,
        "engineering_retries": 1,
        "initialization_constructions": {"stage_a": 9, "stage_b": 0},
        "scalar_labor_roots": {"stage_a": 7200, "stage_b": 0},
        "stages": {
            name: {
                "hjb_calls_started": 0,
                "hjb_calls_completed": 0,
                "kfe_calls_started": 0,
                "kfe_calls_completed": 0,
            }
            for name in ("A", "B")
        },
        "global_multi_province_outer_turns": 0,
        "firm_runtime_calls": 0,
        "matlab_runtime_calls": 0,
        "k1b_calls": 0,
        "k2_calls": 0,
        "ge_calls": 0,
        "annual_downstream_calls": 0,
        "shock_calls": 0,
        "irf_calls": 0,
        "results_writes": 0,
        "points": [],
    }
    coarse.write_json(root / "pre_science_ledger.json", ledger)

    stage_a_points = _run_stage(root, "A", stage_a_fixtures, ledger)
    trigger = stage_b_trigger(stage_a_points, bmax=20.0)
    trigger["stage_b_executed"] = trigger["trigger"]

    if trigger["trigger"]:
        stage_b_fixtures = [build_fixture("B", ra, wage) for ra, wage in POINTS]
        stage_b_invariance = _invariance_receipt(
            "B", stage_b_fixtures, coarse.fixture_config(stage_a_fixtures[0])
        )
        _validate_invariance(stage_b_invariance, ["grid.b"])
        coarse.write_json(root / "stage_b_input_invariance.json", stage_b_invariance)
        ledger["initialization_constructions"]["stage_b"] = 9
        ledger["scalar_labor_roots"]["stage_b"] = 7200
        _run_stage(root, "B", stage_b_fixtures, ledger)

    coarse.write_json(root / "stage_trigger_receipt.json", trigger)
    coarse.write_json(root / "final_call_ledger.json", ledger)
    coarse.write_json(
        root / "execution_complete.json",
        {
            "status": "HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_EXECUTION_COMPLETE",
            "results_eligibility": False,
            "stage_b_trigger": trigger["trigger"],
            "hjb_calls": ledger["hjb_calls_started"],
            "kfe_calls": ledger["kfe_calls_started"],
        },
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_root", type=Path)
    return execute(parser.parse_args().evidence_root)


if __name__ == "__main__":
    raise SystemExit(main())
