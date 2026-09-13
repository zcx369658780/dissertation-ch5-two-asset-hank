"""Execute the exact Owner-approved narrow ra-by-wage frontier 3x3 scan."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import numpy as np

from exports import matlab_faithful_two_asset_ha as oracle
from validators.multi_province.corrected_2018_single_turn.run import source_initial_arrays
from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import run as coarse


REPO = Path(__file__).resolve().parents[3]
POINTS = tuple((ra, wage) for ra in (0.06, 0.0675, 0.07) for wage in (0.8, 1.05, 1.3))
ORACLE_PATH = REPO / "exports" / "matlab_faithful_two_asset_ha.py"
ORACLE_SHA256 = "F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8"
MATLAB_PATH = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m")
MATLAB_SHA256 = "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE"


def build_fixture(ra: float, wage: float) -> coarse.Fixture:
    if (ra, wage) not in POINTS:
        raise ValueError("parameter point is outside the preregistered narrow grid")
    grid = oracle.MatlabFaithfulHJBGrid(
        np.linspace(-2.0, 5.0, 20),
        np.linspace(0.0, 10.0, 20),
        np.array([0.8, 1.3]),
        np.array([[-1.0 / 3.0, 1.0 / 3.0], [1.0 / 3.0, -1.0 / 3.0]]),
    )
    params = oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    state = {"rah": ra, "rb": 0.02, "rb_gap": 0.07, "Tt": 0.1, "tau": 0.05, "w": wage}
    initial_value, baseline_labor = source_initial_arrays(state, grid, params)
    inputs = oracle.HouseholdInputs(
        ra, 0.02, 0.05, np.array([wage]), np.zeros(1), np.ones(1),
    )
    numerics = oracle.MatlabFaithfulHJBNumerics(1000.0, 1e-7, 100, 1e-12)
    return coarse.Fixture(grid, params, inputs, initial_value, baseline_labor, 0.1, 0.07, numerics)


def illiquid_transition_receipt(a_grid: np.ndarray, a_marginal_mass: np.ndarray) -> dict[str, Any]:
    a = np.asarray(a_grid, dtype=float)
    mass = np.asarray(a_marginal_mass, dtype=float)
    if a.ndim != 1 or mass.shape != a.shape or a.size != 20:
        raise ValueError("expected the frozen 20-bin illiquid marginal")
    order = np.argsort(-mass, kind="stable")[:3]
    adjacent = float(mass[-2])
    return {
        "interior_a_mass": float(np.sum(mass[1:-1])),
        "top_3_a_bins": [
            {"a": float(a[index]), "mass": float(mass[index]), "index_zero_based": int(index)}
            for index in order
        ],
        "amax_to_adjacent_interior_ratio": float(mass[-1] / adjacent) if adjacent != 0.0 else None,
        "a_marginal_finite": bool(np.isfinite(mass).all()),
        "a_marginal_shape": list(mass.shape),
        "a_marginal_sum": float(np.sum(mass)),
    }


def run_kfe(fixture: coarse.Fixture, hjb: Any) -> tuple[Any, Any, dict[str, Any]]:
    kfe, aggregates, receipt = coarse.run_kfe(fixture, hjb)
    receipt["distribution"].update(
        illiquid_transition_receipt(fixture.grid.a, receipt["distribution"]["a_marginal_mass"])
    )
    receipt["preliminary_quality_label"] = "PENDING_OFFLINE_DESCRIPTIVE_REVIEW"
    return kfe, aggregates, receipt


def execute(evidence_root: Path) -> int:
    root = Path(evidence_root)
    root.mkdir(parents=True, exist_ok=False)
    source_receipt = {
        "oracle": {
            "path": ORACLE_PATH, "expected_sha256": ORACLE_SHA256,
            "actual_sha256": coarse.file_sha256(ORACLE_PATH),
        },
        "matlab": {
            "path": MATLAB_PATH, "expected_sha256": MATLAB_SHA256,
            "actual_sha256": coarse.file_sha256(MATLAB_PATH),
        },
        "matlab_runtime_calls": 0,
    }
    source_receipt["pass"] = all(
        item["expected_sha256"] == item["actual_sha256"]
        for key, item in source_receipt.items() if key in {"oracle", "matlab"}
    )
    coarse.write_json(root / "source_identity.json", source_receipt)
    if not source_receipt["pass"]:
        raise RuntimeError("source identity preflight failed before HJB")

    fixtures = [build_fixture(ra, wage) for ra, wage in POINTS]
    invariance = coarse.input_invariance_receipt(fixtures)
    invariance["fresh_initial_value_object_count"] = len({id(item.initial_value) for item in fixtures})
    invariance["fresh_baseline_labor_object_count"] = len({id(item.baseline_labor) for item in fixtures})
    invariance["initial_arrays"] = [
        {
            "ra": ra, "wage": wage,
            "initial_value_sha256": coarse.array_sha256(fixture.initial_value),
            "baseline_labor_sha256": coarse.array_sha256(fixture.baseline_labor),
            "initial_value_finite": bool(np.isfinite(fixture.initial_value).all()),
            "baseline_labor_finite": bool(np.isfinite(fixture.baseline_labor).all()),
        }
        for (ra, wage), fixture in zip(POINTS, fixtures)
    ]
    coarse.write_json(root / "input_invariance.json", invariance)
    if (
        invariance["unexpected_varying_fields"]
        or not invariance["all_non_scanned_fields_identical"]
        or invariance["fresh_initial_value_object_count"] != 9
        or invariance["fresh_baseline_labor_object_count"] != 9
    ):
        raise RuntimeError("input invariance/fresh initialization preflight failed before HJB")

    ledger = {
        "schema": "CH5_MP4C_K1_STANDALONE_HJB_RA_WAGE_FRONTIER_NARROW_3X3_LEDGER_V1",
        "hjb_budget": 9, "hjb_calls_started": 0, "hjb_calls_completed": 0,
        "kfe_budget": 9, "kfe_calls_started": 0, "kfe_calls_completed": 0,
        "initialization_constructions": 9, "scalar_labor_roots": 7200,
        "scientific_retries": 0, "engineering_retries": 0,
        "global_multi_province_outer_turns": 0, "firm_runtime_calls": 0,
        "matlab_runtime_calls": 0, "k1b_calls": 0, "k2_calls": 0,
        "ge_calls": 0, "annual_downstream_calls": 0, "shock_calls": 0,
        "irf_calls": 0, "results_writes": 0, "points": [],
    }
    coarse.write_json(root / "pre_science_ledger.json", ledger)

    for index, ((ra, wage), fixture) in enumerate(zip(POINTS, fixtures), start=1):
        point_id = f"p{index:02d}_ra_{ra:.4f}_w_{wage:.2f}".replace(".", "p")
        coarse.write_json(
            root / f"{point_id}_started.json",
            {"point_index": index, "r_b": 0.02, "r_a": ra, "wage": wage},
        )
        ledger["hjb_calls_started"] += 1
        hjb, hjb_receipt = coarse.run_hjb(fixture)
        ledger["hjb_calls_completed"] += 1
        point = {
            "point_index": index, "point_id": point_id, "r_b": 0.02,
            "r_a": ra, "wage": wage, "hjb": hjb_receipt,
            "kfe": {"ran": False}, "distribution_label": None,
        }
        if coarse.kfe_authorized(hjb_receipt["classification"]):
            assert hjb is not None
            ledger["kfe_calls_started"] += 1
            try:
                kfe, _, kfe_receipt = run_kfe(fixture, hjb)
                ledger["kfe_calls_completed"] += 1
                point["kfe"] = kfe_receipt
                np.savez_compressed(
                    root / f"{point_id}_scientific_arrays.npz",
                    value=hjb.value, consumption=hjb.consumption, labor=hjb.labor,
                    transfer=hjb.transfer, mu_a=hjb.mu_a, mu_b=hjb.mu_b,
                    density=kfe.density,
                )
            except Exception as exc:
                point["kfe"] = {
                    "ran": True, "completed": False,
                    "hard_error": f"{type(exc).__name__}: {exc}",
                }
        coarse.write_json(root / f"{point_id}_result.json", point)
        ledger["points"].append({
            "point_index": index, "point_id": point_id,
            "hjb_classification": hjb_receipt["classification"],
            "kfe_ran": bool(point["kfe"]["ran"]),
        })

    coarse.write_json(root / "final_call_ledger.json", ledger)
    coarse.write_json(root / "execution_complete.json", {
        "status": "EXACT_NARROW_FRONTIER_3X3_EXECUTION_COMPLETE",
        "results_eligibility": False,
        "hjb_calls": ledger["hjb_calls_started"],
        "kfe_calls": ledger["kfe_calls_started"],
    })
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_root", type=Path)
    args = parser.parse_args()
    return execute(args.evidence_root)


if __name__ == "__main__":
    raise SystemExit(main())
