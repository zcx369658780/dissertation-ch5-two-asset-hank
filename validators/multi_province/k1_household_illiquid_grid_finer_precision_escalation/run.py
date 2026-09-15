"""Execute the frozen I20/J320-1280 household precision ladder."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import numpy as np

from validators.multi_province.corrected_2018_single_turn.run import source_initial_arrays
from validators.multi_province.k1_household_asset_grid_precision_sensitivity import (
    run as accepted,
)


Path = Path
REPO = Path(__file__).resolve().parents[3]
POINTS = ((20, 320), (20, 640), (20, 1280))
ACCEPTED_COMPACT = (
    REPO
    / "docs/evidence/ch5_mp4c_k1_household_asset_grid_precision_receipt_repair_reexecution"
)
ACCEPTED_FILES = {
    "point_receipts.json": "AD0DDB7ED2D95B8ABC3037B3DF0DC358DD711E168E79A036AD64FDEC1AD8AA94",
    "marginals.json": "7A574D18AD0EFDFACA3E57B838FF2FE9EAAE62A6AFFF236D7830D748C85EEA58",
    "input_invariance_receipt.json": "5A41D359CB9B8CA843E01EF3F7369936D3DEC77EDE587A3F87265A9B6DDFB91B",
}
ACCEPTED_RUNNER_SHA256 = "D5AC8CE26B4CAE0D569A9F3EF25336D0157D7D398249E75BB259B82EFEB4F639"
ACCEPTED_FINALIZER_SHA256 = "BE2822E868096C1E4145CB6C6C7D1CE73B8CB00DFCA57454B2D41E56CDE15FE7"


def precision_spec(index: int) -> dict[str, Any]:
    if index < 0:
        raise ValueError("point index is outside the authorized finer ladder")
    try:
        i_size, j_size = POINTS[index]
    except IndexError as exc:
        raise ValueError("point index is outside the authorized finer ladder") from exc
    return {
        "phase": "FINER",
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


def build_fixture(spec: dict[str, Any]) -> accepted.coarse.Fixture:
    if spec not in [precision_spec(index) for index in range(len(POINTS))]:
        raise ValueError("fixture specification is outside the authorized finer ladder")
    grid = accepted.oracle.MatlabFaithfulHJBGrid(
        np.linspace(spec["bmin"], spec["bmax"], spec["I"]),
        np.linspace(spec["amin"], spec["amax"], spec["J"]),
        np.array([0.8, 1.3]),
        np.array([[-1.0 / 3.0, 1.0 / 3.0], [1.0 / 3.0, -1.0 / 3.0]]),
    )
    params = accepted.oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    state = {
        "rah": spec["ra"],
        "rb": spec["rb"],
        "rb_gap": 0.07,
        "Tt": 0.1,
        "tau": 0.05,
        "w": spec["wage"],
    }
    initial_value, baseline_labor = source_initial_arrays(state, grid, params)
    inputs = accepted.oracle.HouseholdInputs(
        spec["ra"], spec["rb"], 0.05, np.array([spec["wage"]]), np.zeros(1), np.ones(1)
    )
    numerics = accepted.oracle.MatlabFaithfulHJBNumerics(1000.0, 1e-7, 100, 1e-12)
    return accepted.coarse.Fixture(
        grid, params, inputs, initial_value, baseline_labor, 0.1, 0.07, numerics
    )


def source_receipt() -> dict[str, Any]:
    receipt = accepted.source_receipt()
    accepted_paths = {
        name: {
            "path": str((ACCEPTED_COMPACT / name).resolve()),
            "expected_sha256": expected,
            "actual_sha256": accepted.coarse.file_sha256(ACCEPTED_COMPACT / name),
        }
        for name, expected in ACCEPTED_FILES.items()
    }
    runner_path = Path(accepted.__file__).resolve()
    finalizer_path = runner_path.with_name("finalize.py")
    receipt["accepted_grid_generic_runner"] = {
        "path": str(runner_path),
        "expected_sha256": ACCEPTED_RUNNER_SHA256,
        "actual_sha256": accepted.coarse.file_sha256(runner_path),
    }
    receipt["accepted_grid_generic_finalizer"] = {
        "path": str(finalizer_path),
        "expected_sha256": ACCEPTED_FINALIZER_SHA256,
        "actual_sha256": accepted.coarse.file_sha256(finalizer_path),
    }
    receipt["accepted_j160_evidence"] = accepted_paths
    checks = [
        receipt["oracle"],
        receipt["matlab"],
        receipt["accepted_grid_generic_runner"],
        receipt["accepted_grid_generic_finalizer"],
        *accepted_paths.values(),
    ]
    receipt["pass"] = all(item["expected_sha256"] == item["actual_sha256"] for item in checks)
    return receipt


def invariance_receipt(
    specs: list[dict[str, Any]], fixtures: list[accepted.coarse.Fixture]
) -> dict[str, Any]:
    configurations = [accepted.coarse.fixture_config(fixture) for fixture in fixtures]
    varying = sorted(
        key
        for key in configurations[0]
        if any(item[key] != configurations[0][key] for item in configurations[1:])
    )
    return {
        "schema": "CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_INPUT_INVARIANCE_V1",
        "specifications": specs,
        "configurations": configurations,
        "varying_fields_within_ladder": varying,
        "expected_varying_fields_within_ladder": ["grid.a"],
        "accepted_reference_I": 20,
        "accepted_reference_J": 160,
        "accepted_reference_reused_without_runtime": True,
        "fresh_initial_value_object_count": len({id(item.initial_value) for item in fixtures}),
        "fresh_baseline_labor_object_count": len({id(item.baseline_labor) for item in fixtures}),
        "initial_arrays": [
            {
                "I": spec["I"],
                "J": spec["J"],
                "initial_value_sha256": accepted.coarse.array_sha256(fixture.initial_value),
                "baseline_labor_sha256": accepted.coarse.array_sha256(fixture.baseline_labor),
                "initial_value_finite": bool(np.isfinite(fixture.initial_value).all()),
                "baseline_labor_finite": bool(np.isfinite(fixture.baseline_labor).all()),
            }
            for spec, fixture in zip(specs, fixtures)
        ],
        "no_warm_start": True,
    }


def validate_invariance(receipt: dict[str, Any]) -> None:
    count = len(POINTS)
    if (
        receipt["varying_fields_within_ladder"] != ["grid.a"]
        or receipt["fresh_initial_value_object_count"] != count
        or receipt["fresh_baseline_labor_object_count"] != count
        or any(
            not row["initial_value_finite"] or not row["baseline_labor_finite"]
            for row in receipt["initial_arrays"]
        )
    ):
        raise RuntimeError("finer precision input invariance preflight failed")


def execute(evidence_root: Path) -> int:
    root = Path(evidence_root)
    root.mkdir(parents=True, exist_ok=False)
    source = source_receipt()
    accepted.coarse.write_json(root / "source_identity.json", source)
    if not source["pass"]:
        raise RuntimeError("source identity preflight failed before HJB")

    specs = [precision_spec(index) for index in range(len(POINTS))]
    fixtures = [build_fixture(spec) for spec in specs]
    invariance = invariance_receipt(specs, fixtures)
    validate_invariance(invariance)
    accepted.coarse.write_json(root / "input_invariance_receipt.json", invariance)
    ledger = {
        "schema": "CH5_MP4C_K1_HOUSEHOLD_ILLIQUID_GRID_FINER_LEDGER_V1",
        "hjb_budget": 3,
        "hjb_calls_started": 0,
        "hjb_calls_completed": 0,
        "kfe_budget": 3,
        "kfe_calls_started": 0,
        "kfe_calls_completed": 0,
        "kfe_numeric_solves_returned": 0,
        "scientific_arrays_persisted": 0,
        "scientific_retries": 0,
        "engineering_retries": 0,
        "initialization_constructions": 3,
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
    accepted.coarse.write_json(root / "pre_science_ledger.json", ledger)

    stopped = False
    for spec, fixture in zip(specs, fixtures):
        point_id = f"finer_i{spec['I']:03d}_j{spec['J']:04d}"
        accepted.coarse.write_json(
            root / f"{point_id}_started.json",
            {
                "point_id": point_id,
                "specification": spec,
                "fresh_initialization": True,
                "initial_value_sha256": accepted.coarse.array_sha256(fixture.initial_value),
                "baseline_labor_sha256": accepted.coarse.array_sha256(fixture.baseline_labor),
            },
        )
        ledger["hjb_calls_started"] += 1
        hjb, hjb_receipt = accepted.coarse.run_hjb(fixture)
        ledger["hjb_calls_completed"] += 1
        point = {
            "point_id": point_id,
            "phase": "FINER",
            "specification": spec,
            "fresh_initialization": {
                "used": True,
                "source": "source_initial_arrays",
                "warm_start": False,
                "initial_value_sha256": accepted.coarse.array_sha256(fixture.initial_value),
                "baseline_labor_sha256": accepted.coarse.array_sha256(fixture.baseline_labor),
            },
            "hjb": hjb_receipt,
            "kfe": {"ran": False},
        }
        if accepted.coarse.kfe_authorized(hjb_receipt["classification"]):
            assert hjb is not None
            ledger["kfe_calls_started"] += 1
            arrays_path = root / f"{point_id}_scientific_arrays.npz"
            try:
                _, _, kfe_receipt = accepted.run_kfe_persist_first(fixture, hjb, arrays_path)
                ledger["kfe_numeric_solves_returned"] += 1
                ledger["scientific_arrays_persisted"] += 1
                kfe_receipt["completed"] = True
                point["kfe"] = kfe_receipt
                ledger["kfe_calls_completed"] += 1
            except Exception as exc:
                arrays_persisted = arrays_path.is_file()
                if arrays_persisted:
                    ledger["kfe_numeric_solves_returned"] += 1
                    ledger["scientific_arrays_persisted"] += 1
                point["kfe"] = {
                    "ran": True,
                    "completed": False,
                    "scientific_arrays_persisted": arrays_persisted,
                    "scientific_arrays_path": str(arrays_path.resolve()) if arrays_persisted else None,
                    "hard_error": f"{type(exc).__name__}: {exc}",
                }
        valid = accepted.stagewise.kfe_valid(point)
        ledger["points"].append(
            {
                "point_id": point_id,
                "I": spec["I"],
                "J": spec["J"],
                "hjb_classification": hjb_receipt["classification"],
                "kfe_ran": bool(point["kfe"]["ran"]),
                "kfe_valid": valid,
            }
        )
        accepted.coarse.write_json(root / f"{point_id}_result.json", point)
        if hjb_receipt["classification"] != "HJB_CONVERGED" or not valid:
            stopped = True
            break

    accepted.coarse.write_json(root / "final_call_ledger.json", ledger)
    accepted.coarse.write_json(
        root / "execution_complete.json",
        {
            "status": "FINER_PRECISION_STOPPED_ON_INVALID_POINT" if stopped else "FINER_PRECISION_COMPLETE",
            "results_eligibility": False,
            "hjb_calls": ledger["hjb_calls_started"],
            "kfe_calls": ledger["kfe_calls_started"],
        },
    )
    return 1 if stopped else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_root", type=Path)
    return execute(parser.parse_args().evidence_root)


if __name__ == "__main__":
    raise SystemExit(main())
