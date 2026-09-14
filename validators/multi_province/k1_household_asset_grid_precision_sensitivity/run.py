"""Execute one frozen precision phase without changing household science."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np

from exports import matlab_faithful_two_asset_ha as oracle
from validators.multi_province.corrected_2018_single_turn.run import source_initial_arrays
from validators.multi_province.k1_household_k_unit_asset_domain_stagewise import (
    run as stagewise,
)
from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import run as coarse


REPO = Path(__file__).resolve().parents[3]
PHASE_POINTS = {
    "P1": ((20, 40), (20, 80), (20, 160)),
    "P2": ((40, 160), (80, 160)),
}
ORACLE_PATH = REPO / "exports/matlab_faithful_two_asset_ha.py"
ORACLE_SHA256 = "F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8"
MATLAB_PATH = Path(
    r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m"
)
MATLAB_SHA256 = "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE"
ACCEPTED_ROOT = (
    REPO / "docs/evidence/ch5_mp4c_k1_household_k_unit_asset_domain_stagewise"
)
ACCEPTED_POINTS = ACCEPTED_ROOT / "point_receipts.json"
ACCEPTED_INPUT = ACCEPTED_ROOT / "input_invariance_receipt.json"


def precision_spec(phase: str, index: int) -> dict[str, Any]:
    if phase not in PHASE_POINTS:
        raise ValueError("phase must be P1 or P2")
    try:
        i_size, j_size = PHASE_POINTS[phase][index]
    except IndexError as exc:
        raise ValueError("point index is outside the authorized precision ladder") from exc
    return {
        "phase": phase,
        "phase_point_index": index + 1,
        "I": i_size,
        "J": j_size,
        "Nz": 2,
        "amin": 0.0,
        "amax": 100.0,
        "bmin": -2.0,
        "bmax": 20.0,
        "da": 100.0 / (j_size - 1),
        "db": 22.0 / (i_size - 1),
        "rb": 0.02,
        "ra": 0.0675,
        "wage": 15.5,
        "h": 1.0,
    }


def build_fixture(spec: dict[str, Any]) -> coarse.Fixture:
    allowed = [precision_spec(phase, index) for phase in PHASE_POINTS for index in range(len(PHASE_POINTS[phase]))]
    if spec not in allowed:
        raise ValueError("fixture specification is outside the authorized precision ladder")
    grid = oracle.MatlabFaithfulHJBGrid(
        np.linspace(spec["bmin"], spec["bmax"], spec["I"]),
        np.linspace(spec["amin"], spec["amax"], spec["J"]),
        np.array([0.8, 1.3]),
        np.array([[-1.0 / 3.0, 1.0 / 3.0], [1.0 / 3.0, -1.0 / 3.0]]),
    )
    params = oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    state = {
        "rah": spec["ra"],
        "rb": spec["rb"],
        "rb_gap": 0.07,
        "Tt": 0.1,
        "tau": 0.05,
        "w": spec["wage"],
    }
    initial_value, baseline_labor = source_initial_arrays(state, grid, params)
    inputs = oracle.HouseholdInputs(
        spec["ra"], spec["rb"], 0.05, np.array([spec["wage"]]), np.zeros(1), np.ones(1)
    )
    numerics = oracle.MatlabFaithfulHJBNumerics(1000.0, 1e-7, 100, 1e-12)
    return coarse.Fixture(
        grid, params, inputs, initial_value, baseline_labor, 0.1, 0.07, numerics
    )


def _accepted_central_point() -> dict[str, Any]:
    points = json.loads(ACCEPTED_POINTS.read_text(encoding="utf-8"))
    selected = [
        point
        for point in points
        if point["stage"] == "A" and point["r_a"] == 0.0675 and point["wage"] == 15.5
    ]
    if len(selected) != 1:
        raise ValueError("accepted central Stage A reference is not unique")
    return selected[0]


def _accepted_central_config() -> dict[str, Any]:
    receipt = json.loads(ACCEPTED_INPUT.read_text(encoding="utf-8"))
    configurations = receipt["stage_a"]["configurations"]
    selected = [
        item
        for item in configurations
        if item["inputs.r_a"] == 0.0675 and item["inputs.wages[0]"] == 15.5
    ]
    if len(selected) != 1:
        raise ValueError("accepted central Stage A configuration is not unique")
    return selected[0]


def source_receipt() -> dict[str, Any]:
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
        "accepted_stage_a_points": {
            "path": ACCEPTED_POINTS.resolve(),
            "sha256": coarse.file_sha256(ACCEPTED_POINTS),
        },
        "accepted_stage_a_input": {
            "path": ACCEPTED_INPUT.resolve(),
            "sha256": coarse.file_sha256(ACCEPTED_INPUT),
        },
        "accepted_stagewise_runner": {
            "path": Path(stagewise.__file__).resolve(),
            "sha256": coarse.file_sha256(Path(stagewise.__file__)),
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
    phase: str, specs: list[dict[str, Any]], fixtures: list[coarse.Fixture]
) -> dict[str, Any]:
    configurations = [coarse.fixture_config(fixture) for fixture in fixtures]
    varying = sorted(
        key
        for key in configurations[0]
        if any(item[key] != configurations[0][key] for item in configurations[1:])
    )
    expected_varying = ["grid.a"] if phase == "P1" else ["grid.b"]
    accepted_config = _accepted_central_config()
    comparison_config = configurations[0]
    changed_vs_accepted = sorted(
        key for key in comparison_config if comparison_config[key] != accepted_config[key]
    )
    expected_vs_accepted = ["grid.a"] if phase == "P1" else ["grid.a", "grid.b"]
    return {
        "phase": phase,
        "specifications": specs,
        "temporary_household_bridge_h": 1.0,
        "configurations": configurations,
        "varying_fields_within_phase": varying,
        "expected_varying_fields_within_phase": expected_varying,
        "changed_fields_vs_accepted_J20_I20": changed_vs_accepted,
        "expected_changed_fields_vs_accepted_J20_I20": expected_vs_accepted,
        "fresh_initial_value_object_count": len({id(item.initial_value) for item in fixtures}),
        "fresh_baseline_labor_object_count": len({id(item.baseline_labor) for item in fixtures}),
        "initial_arrays": [
            {
                "I": spec["I"],
                "J": spec["J"],
                "initial_value_sha256": coarse.array_sha256(fixture.initial_value),
                "baseline_labor_sha256": coarse.array_sha256(fixture.baseline_labor),
                "initial_value_finite": bool(np.isfinite(fixture.initial_value).all()),
                "baseline_labor_finite": bool(np.isfinite(fixture.baseline_labor).all()),
            }
            for spec, fixture in zip(specs, fixtures)
        ],
    }


def _validate_invariance(receipt: dict[str, Any], point_count: int) -> None:
    if (
        receipt["varying_fields_within_phase"]
        != receipt["expected_varying_fields_within_phase"]
        or receipt["changed_fields_vs_accepted_J20_I20"]
        != receipt["expected_changed_fields_vs_accepted_J20_I20"]
        or receipt["fresh_initial_value_object_count"] != point_count
        or receipt["fresh_baseline_labor_object_count"] != point_count
        or any(
            not row["initial_value_finite"] or not row["baseline_labor_finite"]
            for row in receipt["initial_arrays"]
        )
    ):
        raise RuntimeError("precision input invariance preflight failed")


def execute(phase: str, evidence_root: Path) -> int:
    if phase not in PHASE_POINTS:
        raise ValueError("phase must be P1 or P2")
    root = Path(evidence_root)
    root.mkdir(parents=True, exist_ok=False)
    source = source_receipt()
    coarse.write_json(root / "source_identity.json", source)
    if not source["pass"]:
        raise RuntimeError("source identity preflight failed before HJB")
    _accepted_central_point()

    specs = [precision_spec(phase, index) for index in range(len(PHASE_POINTS[phase]))]
    fixtures = [build_fixture(spec) for spec in specs]
    invariance = _invariance_receipt(phase, specs, fixtures)
    _validate_invariance(invariance, len(specs))
    coarse.write_json(root / "input_invariance.json", invariance)

    scalar_roots = sum(spec["I"] * spec["J"] * spec["Nz"] for spec in specs)
    ledger = {
        "schema": "CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_PHASE_LEDGER_V1",
        "phase": phase,
        "hjb_budget": len(specs),
        "hjb_calls_started": 0,
        "hjb_calls_completed": 0,
        "kfe_budget": len(specs),
        "kfe_calls_started": 0,
        "kfe_calls_completed": 0,
        "scientific_retries": 0,
        "engineering_retries": 0,
        "initialization_constructions": len(specs),
        "scalar_labor_roots": scalar_roots,
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

    for spec, fixture in zip(specs, fixtures):
        point_id = f"{phase.lower()}_i{spec['I']:03d}_j{spec['J']:03d}"
        coarse.write_json(
            root / f"{point_id}_started.json",
            {
                "point_id": point_id,
                "specification": spec,
                "fresh_initialization": True,
                "initial_value_sha256": coarse.array_sha256(fixture.initial_value),
                "baseline_labor_sha256": coarse.array_sha256(fixture.baseline_labor),
            },
        )
        ledger["hjb_calls_started"] += 1
        hjb, hjb_receipt = coarse.run_hjb(fixture)
        ledger["hjb_calls_completed"] += 1
        point = {
            "point_id": point_id,
            "phase": phase,
            "specification": spec,
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
            try:
                kfe, _, kfe_receipt = stagewise.accepted.run_kfe(fixture, hjb)
                kfe_receipt["completed"] = True
                point["kfe"] = kfe_receipt
                ledger["kfe_calls_completed"] += 1
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
                "point_id": point_id,
                "I": spec["I"],
                "J": spec["J"],
                "hjb_classification": hjb_receipt["classification"],
                "kfe_ran": bool(point["kfe"]["ran"]),
                "kfe_valid": stagewise.kfe_valid(point),
            }
        )

    coarse.write_json(root / "final_call_ledger.json", ledger)
    coarse.write_json(
        root / "execution_complete.json",
        {
            "status": f"HOUSEHOLD_ASSET_GRID_PRECISION_{phase}_COMPLETE",
            "phase": phase,
            "results_eligibility": False,
            "hjb_calls": ledger["hjb_calls_started"],
            "kfe_calls": ledger["kfe_calls_started"],
        },
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=sorted(PHASE_POINTS))
    parser.add_argument("evidence_root", type=Path)
    args = parser.parse_args()
    return execute(args.phase, args.evidence_root)


if __name__ == "__main__":
    raise SystemExit(main())
