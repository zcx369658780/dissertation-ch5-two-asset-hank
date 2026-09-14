"""Build compact, sealed evidence from the stagewise raw execution."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

import numpy as np

from validators.multi_province.k1_household_k_unit_asset_domain_stagewise import run
from validators.multi_province.k1_real_composite_wage_domain_macro_scale import (
    finalize as accepted_finalize,
)
from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import run as coarse
from validators.multi_province.k1_standalone_hjb_ra_wage_frontier_narrow_3x3.finalize import (
    seal,
)


REPO = Path(__file__).resolve().parents[3]
BASELINE_ROOT = (
    REPO / "docs/evidence/ch5_mp4c_k1_real_composite_wage_domain_macro_scale_audit"
)


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _pathological(distribution: dict[str, Any]) -> bool:
    rounding_band = 100.0 * np.finfo(float).eps
    total = float(distribution.get("total_mass", np.nan))
    density_min = float(distribution.get("density_min", np.nan))
    return bool(
        not distribution.get("density_finite", False)
        or not np.isfinite(total)
        or total <= 0.0
        or not np.isfinite(density_min)
        or density_min < -rounding_band
    )


def classify_a(mass: np.ndarray, distribution: dict[str, Any]) -> str:
    return accepted_finalize.descriptive_distribution_label(
        np.asarray(mass, dtype=float), {"distribution": distribution}
    )


def classify_b(mass: np.ndarray, distribution: dict[str, Any]) -> str:
    value = np.asarray(mass, dtype=float)
    if value.ndim != 1 or value.size < 3 or not np.isfinite(value).all():
        return "KFE_NUMERICALLY_PATHOLOGICAL"
    if _pathological(distribution):
        return "KFE_NUMERICALLY_PATHOLOGICAL"
    maximum = float(np.max(value))
    modes = set(map(int, np.flatnonzero(value == maximum)))
    if value.size - 1 in modes:
        return "B_UPPER_BOUNDARY_PILEUP"
    if 0 in modes:
        return "B_LOWER_BOUNDARY_DOMINATED"
    if modes and all(0 < index < value.size - 1 for index in modes):
        return "B_INTERIOR_DISTRIBUTION_CANDIDATE"
    return "B_TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED"


def _top_bins(grid: np.ndarray, mass: np.ndarray) -> list[dict[str, Any]]:
    indices = np.argsort(-np.asarray(mass), kind="stable")[:3]
    return [
        {"index": int(index), "grid_value": float(grid[index]), "mass": float(mass[index])}
        for index in indices
    ]


def _as_float(value: Any) -> float | None:
    if value in (None, "", "None"):
        return None
    return float(value)


def _delta(old: Any, new: Any) -> dict[str, float | None]:
    old_value = _as_float(old)
    new_value = _as_float(new)
    return {
        "old": old_value,
        "new": new_value,
        "delta": None
        if old_value is None or new_value is None
        else new_value - old_value,
    }


def _baseline_comparison(points: list[dict[str, Any]]) -> dict[str, Any]:
    with (BASELINE_ROOT / "points.csv").open(
        "r", encoding="utf-8-sig", newline=""
    ) as stream:
        old_rows = list(csv.DictReader(stream))
    old_marginals = read_json(BASELINE_ROOT / "marginals.json")
    rows_by_key = {
        (float(row["ra"]), float(row["wage"])): row for row in old_rows
    }
    marginals_by_key = {
        (float(row["r_a"]), float(row["wage"])): row for row in old_marginals
    }
    comparisons = []
    for point in points:
        key = (float(point["r_a"]), float(point["wage"]))
        old = rows_by_key[key]
        old_marginal = marginals_by_key[key]
        distribution = point.get("kfe", {}).get("distribution", {})
        aggregates = point.get("kfe", {}).get("aggregates", {})
        old_a = np.asarray(old_marginal["a_marginal_mass"], dtype=float)
        old_b = np.asarray(old_marginal["b_marginal_mass"], dtype=float)
        comparisons.append(
            {
                "stage": point["stage"],
                "point_id": point["point_id"],
                "r_b": point["r_b"],
                "r_a": point["r_a"],
                "wage": point["wage"],
                "old_domain": {"amin": 0.0, "amax": 10.0, "bmin": -2.0, "bmax": 5.0, "I": 20, "J": 20},
                "new_domain": point["domain"],
                "hjb": {
                    "classification": {
                        "old": old["hjb_classification"],
                        "new": point["hjb"]["classification"],
                    },
                    "iterations": _delta(old["iterations"], point["hjb"]["iterations_used"]),
                    "maximum_A2max": _delta(old["maximum_A2max"], point["hjb"]["maximum_a2max"]),
                },
                "aggregates": {
                    name: _delta(old[name], aggregates.get(name))
                    for name in ("Ct", "Lt", "At", "Bt")
                },
                "a_distribution": {
                    "modal": {"old": json.loads(old["modal_a"]), "new": distribution.get("modal_a")},
                    "amin_mass": _delta(old["amin_mass"], distribution.get("boundary_mass_shares", {}).get("amin")),
                    "amax_mass": _delta(old["amax_mass"], distribution.get("boundary_mass_shares", {}).get("amax")),
                    "old_raw_endpoint_masses": {"amin": float(old_a[0]), "amax": float(old_a[-1])},
                },
                "b_distribution": {
                    "modal": {"old": json.loads(old["modal_b"]), "new": distribution.get("modal_b")},
                    "bmin_mass": _delta(old["bmin_mass"], distribution.get("boundary_mass_shares", {}).get("bmin")),
                    "bmax_mass": _delta(old["bmax_mass"], distribution.get("boundary_mass_shares", {}).get("bmax")),
                    "old_raw_endpoint_masses": {"bmin": float(old_b[0]), "bmax": float(old_b[-1])},
                },
                "kfe": {
                    "raw_residual_inf": _delta(
                        old["kfe_raw_residual_inf"],
                        point.get("kfe", {}).get("kfe", {}).get("raw_residual_inf"),
                    ),
                    "density_min": _delta(old["density_min"], distribution.get("density_min")),
                    "density_negative_count": _delta(
                        old["density_negative_count"], distribution.get("density_negative_count")
                    ),
                    "signed_mass_clipped": False,
                },
            }
        )
    return {
        "schema": "CH5_MP4C_K1_ASSET_DOMAIN_OLD_DOMAIN_COMPARISON_V1",
        "accepted_baseline": "real composite-wage same-input scan, a=[0,10], b=[-2,5]",
        "comparison_is_not_ge_or_calibration_improvement_claim": True,
        "points": comparisons,
    }


def _row(point: dict[str, Any]) -> dict[str, Any]:
    hjb = point["hjb"]
    kfe = point.get("kfe", {})
    distribution = kfe.get("distribution", {})
    aggregates = kfe.get("aggregates", {})
    boundary = distribution.get("boundary_mass_shares", {})
    return {
        "stage": point["stage"],
        "stage_point_index": point["stage_point_index"],
        "point_id": point["point_id"],
        "rb": point["r_b"],
        "ra": point["r_a"],
        "wage": point["wage"],
        "amin": point["domain"]["amin"],
        "amax": point["domain"]["amax"],
        "bmin": point["domain"]["bmin"],
        "bmax": point["domain"]["bmax"],
        "da": point["domain"]["da"],
        "db": point["domain"]["db"],
        "hjb_classification": hjb["classification"],
        "iterations": hjb["iterations_used"],
        "final_statistic": hjb["final_convergence_statistic"],
        "maximum_A2max": hjb["maximum_a2max"],
        "first_illegal_iteration": hjb["first_illegal_iteration"],
        "kfe_ran": kfe.get("ran", False),
        "kfe_valid": run.kfe_valid(point),
        "a_domain_classification": point.get("a_domain_classification"),
        "b_domain_classification": point.get("b_domain_classification"),
        "Ct": aggregates.get("Ct"),
        "Lt": aggregates.get("Lt"),
        "At": aggregates.get("At"),
        "Bt": aggregates.get("Bt"),
        "Bt_pos": distribution.get("Bt_pos"),
        "Bt_neg": distribution.get("Bt_neg"),
        "amin_mass": boundary.get("amin"),
        "amax_mass": boundary.get("amax"),
        "bmin_mass": boundary.get("bmin"),
        "bmax_mass": boundary.get("bmax"),
        "interior_a_mass": distribution.get("interior_a_mass"),
        "interior_b_mass": distribution.get("interior_b_mass"),
        "modal_a": json.dumps(distribution.get("modal_a"), separators=(",", ":")),
        "modal_b": json.dumps(distribution.get("modal_b"), separators=(",", ":")),
        "top_3_a_bins": json.dumps(distribution.get("top_3_a_bins"), separators=(",", ":")),
        "top_3_b_bins": json.dumps(distribution.get("top_3_b_bins"), separators=(",", ":")),
        "total_mass": distribution.get("total_mass"),
        "kfe_raw_residual_inf": kfe.get("kfe", {}).get("raw_residual_inf"),
        "density_min": distribution.get("density_min"),
        "density_negative_count": distribution.get("density_negative_count"),
    }


def build(external_root: Path, compact_root: Path) -> int:
    external_root = Path(external_root)
    compact_root = Path(compact_root)
    if not (external_root / "execution_complete.json").is_file():
        raise ValueError("external execution is incomplete")
    compact_root.mkdir(parents=True, exist_ok=False)

    external_manifest = seal(
        external_root, "CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_EXTERNAL_V1"
    )
    points = [
        read_json(path)
        for path in sorted(external_root.glob("stage_*_p*_result.json"))
    ]
    trigger = read_json(external_root / "stage_trigger_receipt.json")
    expected_count = 18 if trigger["trigger"] else 9
    if len(points) != expected_count:
        raise ValueError(f"expected {expected_count} point receipts")

    marginals = []
    for point in points:
        if not run.kfe_valid(point):
            point["a_domain_classification"] = None
            point["b_domain_classification"] = None
            continue
        distribution = point["kfe"]["distribution"]
        a_mass = np.asarray(distribution["a_marginal_mass"], dtype=float)
        b_mass = np.asarray(distribution["b_marginal_mass"], dtype=float)
        spec = point["domain"]
        a_grid = np.linspace(spec["amin"], spec["amax"], spec["J"])
        b_grid = np.linspace(spec["bmin"], spec["bmax"], spec["I"])
        distribution["interior_a_mass"] = float(np.sum(a_mass[1:-1]))
        distribution["interior_b_mass"] = float(np.sum(b_mass[1:-1]))
        distribution["top_3_a_bins"] = _top_bins(a_grid, a_mass)
        distribution["top_3_b_bins"] = _top_bins(b_grid, b_mass)
        point["a_domain_classification"] = classify_a(a_mass, distribution)
        point["b_domain_classification"] = classify_b(b_mass, distribution)
        marginals.append(
            {
                "stage": point["stage"],
                "point_id": point["point_id"],
                "r_b": point["r_b"],
                "r_a": point["r_a"],
                "wage": point["wage"],
                "a_grid": a_grid.tolist(),
                "a_marginal_mass": a_mass.tolist(),
                "b_grid": b_grid.tolist(),
                "b_marginal_mass": b_mass.tolist(),
            }
        )

    rows = [_row(point) for point in points]
    final_stage = "B" if trigger["trigger"] else "A"
    final_points = [point for point in points if point["stage"] == final_stage]
    serious = len(final_points) != 9 or any(
        point["hjb"]["classification"] != "HJB_CONVERGED"
        or not run.kfe_valid(point)
        for point in final_points
    )
    endpoint_modes = sum(
        point.get("b_domain_classification") == "B_UPPER_BOUNDARY_PILEUP"
        for point in final_points
    )
    if serious or (final_stage == "B" and endpoint_modes):
        terminal = "ASSET_DOMAIN_OR_HOUSEHOLD_SCALE_RECALIBRATION_UNRESOLVED"
        next_gate = "OWNER_REVIEW_ASSET_DOMAIN_OR_HOUSEHOLD_SCALE_RECALIBRATION_UNRESOLVED"
    elif final_stage == "B":
        terminal = "ASSET_DOMAIN_STAGE_B_BOUNDARY_CLEARED__PRECISION_SENSITIVITY_REQUIRED"
        next_gate = "OWNER_REVIEW_ASSET_DOMAIN_STAGE_B_ACCEPTANCE_AND_PRECISION_SENSITIVITY"
    else:
        terminal = "ASSET_DOMAIN_STAGE_A_BOUNDARY_CLEARED__PRECISION_SENSITIVITY_REQUIRED"
        next_gate = "OWNER_REVIEW_ASSET_DOMAIN_STAGE_A_ACCEPTANCE_AND_PRECISION_SENSITIVITY"

    summary = {
        "schema": "CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_SUMMARY_V1",
        "terminal_classification": terminal,
        "results_eligibility": False,
        "temporary_household_bridge_h": 1.0,
        "stage_b_trigger": trigger["trigger"],
        "final_stage": final_stage,
        "final_stage_exact_bmax_modal_point_count": endpoint_modes,
        "boundary_pileup_cleared": not serious and endpoint_modes == 0,
        "recommended_next_gate": {"name": next_gate, "run_now": False},
        "hjb_counts": {
            stage: {
                name: sum(
                    point["stage"] == stage and point["hjb"]["classification"] == name
                    for point in points
                )
                for name in sorted(coarse.HJB_CLASSES)
            }
            for stage in sorted({point["stage"] for point in points})
        },
        "a_domain_counts": {
            stage: {
                name: sum(
                    point["stage"] == stage and point.get("a_domain_classification") == name
                    for point in points
                )
                for name in sorted(
                    {
                        "LOWER_A_BOUNDARY_DOMINATED",
                        "INTERIOR_A_DISTRIBUTION_CANDIDATE",
                        "UPPER_A_BOUNDARY_PILEUP",
                        "TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED",
                        "KFE_NUMERICALLY_PATHOLOGICAL",
                    }
                )
            }
            for stage in sorted({point["stage"] for point in points})
        },
        "b_domain_counts": {
            stage: {
                name: sum(
                    point["stage"] == stage and point.get("b_domain_classification") == name
                    for point in points
                )
                for name in sorted(
                    {
                        "B_INTERIOR_DISTRIBUTION_CANDIDATE",
                        "B_LOWER_BOUNDARY_DOMINATED",
                        "B_UPPER_BOUNDARY_PILEUP",
                        "B_TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED",
                        "KFE_NUMERICALLY_PATHOLOGICAL",
                    }
                )
            }
            for stage in sorted({point["stage"] for point in points})
        },
        "classification_semantics": {
            "post_result_fitted_threshold": False,
            "endpoint_mode_exact": True,
            "pathology_rounding_band": "100*IEEE754_float64_epsilon",
        },
        "precision_caveat": "I=J=20 domain diagnostic only; production precision sensitivity remains mandatory.",
        "kfe_caveat": "Accepted standalone contaminated-row KFE only; raw signed density is not clipped; corrected-2018 multi-province finite-box/pinning remains separate.",
    }

    input_receipt = {
        "schema": "CH5_MP4C_K1_HOUSEHOLD_K_UNIT_INPUT_INVARIANCE_V1",
        "temporary_household_bridge_h": 1.0,
        "stage_a": read_json(external_root / "stage_a_input_invariance.json"),
        "stage_b": read_json(external_root / "stage_b_input_invariance.json")
        if trigger["trigger"]
        else None,
        "no_household_monetary_rescale": True,
        "no_warm_start": True,
    }
    source = read_json(external_root / "source_identity.json")
    source["accepted_baseline_points"] = {
        "path": str((BASELINE_ROOT / "points.csv").resolve()),
        "sha256": coarse.file_sha256(BASELINE_ROOT / "points.csv"),
    }
    source["accepted_baseline_marginals"] = {
        "path": str((BASELINE_ROOT / "marginals.json").resolve()),
        "sha256": coarse.file_sha256(BASELINE_ROOT / "marginals.json"),
    }

    coarse.write_json(compact_root / "input_invariance_receipt.json", input_receipt)
    coarse.write_json(compact_root / "stage_trigger_receipt.json", trigger)
    coarse.write_json(compact_root / "call_ledger.json", read_json(external_root / "final_call_ledger.json"))
    coarse.write_json(compact_root / "point_receipts.json", points)
    coarse.write_json(compact_root / "marginals.json", marginals)
    coarse.write_json(compact_root / "baseline_comparison.json", _baseline_comparison(points))
    coarse.write_json(compact_root / "source_identity.json", source)
    coarse.write_json(compact_root / "external_manifest.json", external_manifest)
    coarse.write_json(compact_root / "summary.json", summary)
    with (compact_root / "points.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    seal(compact_root, "CH5_MP4C_K1_HOUSEHOLD_K_UNIT_ASSET_DOMAIN_STAGEWISE_COMPACT_V1")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("external_root", type=Path)
    parser.add_argument("compact_root", type=Path)
    args = parser.parse_args()
    return build(args.external_root, args.compact_root)


if __name__ == "__main__":
    raise SystemExit(main())
