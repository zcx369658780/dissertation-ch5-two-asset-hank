"""Offline classification and evidence builder for the real-wage scan and scale audit."""
from __future__ import annotations

import argparse
import csv
import json
import statistics
from pathlib import Path
from typing import Any

import numpy as np

from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import run as coarse
from validators.multi_province.k1_standalone_hjb_ra_wage_frontier_narrow_3x3.finalize import seal


REPO = Path(__file__).resolve().parents[3]
RA_VALUES = (0.06, 0.0675, 0.07)
WAGES = (13.0, 15.5, 18.0)
LABELS = {
    "LOWER_A_BOUNDARY_DOMINATED", "INTERIOR_A_DISTRIBUTION_CANDIDATE",
    "UPPER_A_BOUNDARY_PILEUP", "TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED",
    "KFE_NUMERICALLY_PATHOLOGICAL",
}


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def descriptive_distribution_label(a_mass: np.ndarray, kfe: dict[str, Any]) -> str:
    """Apply a machine-precision pathology guard and order-only boundary rules."""
    mass = np.asarray(a_mass, dtype=float)
    distribution = kfe.get("distribution", {})
    rounding_band = 100.0 * np.finfo(float).eps
    if (not np.isfinite(mass).all() or not distribution.get("density_finite", False)
            or float(distribution.get("density_min", 0.0)) < -rounding_band
            or float(distribution.get("total_mass", 0.0)) <= 0.0):
        return "KFE_NUMERICALLY_PATHOLOGICAL"
    maximum = float(np.max(mass)); modes = set(map(int, np.flatnonzero(mass == maximum)))
    interior_mass = float(np.sum(mass[1:-1]))
    top_two = set(map(int, np.argsort(-mass, kind="stable")[:2]))
    if mass.size - 1 in modes:
        return "UPPER_A_BOUNDARY_PILEUP"
    if modes == {0} and float(mass[0]) > interior_mass:
        return "LOWER_A_BOUNDARY_DOMINATED"
    if modes and all(0 < i < mass.size - 1 for i in modes) and all(0 < i < mass.size - 1 for i in top_two):
        if float(mass[0]) < maximum and float(mass[-1]) < maximum:
            return "INTERIOR_A_DISTRIBUTION_CANDIDATE"
    return "TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED"


def _stats(values: list[float]) -> dict[str, float]:
    return {"min": min(values), "median": statistics.median(values), "max": max(values)}


def build_macro_artifacts(compact_root: Path) -> dict[str, Any]:
    receipt = REPO / "reports/mp4c_unit_normalized_initialization_probe_20260910/province_initialization_receipt.csv"
    with receipt.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 31:
        raise ValueError("accepted initialization receipt must have 31 provinces")
    fields = {
        "province_gdp_raw_100m_yuan": "Y0_raw_亿元", "province_gdp_Y0_MU": "Y0_MU",
        "population_raw_10k_persons": "POP_raw_万人", "population_N0_NU": "N0_NU",
        "per_capita_output_Y0_over_N0": "Y_to_N", "capital_raw_100m_yuan": "K0_trackA_亿元",
        "capital_K0_MU": "K0_MU", "initial_labor_proxy_L0_NU": "L0",
        "productivity_Zt0": "Zt0", "raw_firm_wage_wjt0": "raw_wjt0",
        "guarded_firm_wage_wjt0": "used_wjt0", "household_composite_wage_w0": "w0",
    }
    stats = {name: _stats([float(row[column]) for row in rows]) for name, column in fields.items()}
    trace = {
        "schema": "CH5_MP4C_K1_MACRO_SCALE_TRACE_V1", "accepted_same_state": "CORRECTED_2018_INITIALIZATION_ONLY",
        "province_count": 31, "statistics": stats,
        "wage_mapping": {
            "formula": "w_i=alphal^(-phi_l/(1+phi_l))*[sum_j phi(j,i)*(wjt_j*(1-tau_j-sigmau(j,i))/phi(j,i))^(1+1/phi_l)]^(phi_l/(1+phi_l))",
            "source": "wage_caculate.m:1-17; HANK_mp_1turn.m:49-53",
            "interpretation": "Cross-province CES-style destination aggregation can map O(1) guarded wjt to O(10) composite w; monetary units are not proven.",
        },
        "scalings": [
            {"variable": "GDP", "source": "load_GDPdata.m:93; corrected_2018_runtime.py", "formula": "Y0_MU=GDP_raw*1000", "factor": 1000.0, "authority": "ACCEPTED_CORRECTED_2018", "raw_unit": "亿元", "model_unit": "MU_10WAN_YUAN"},
            {"variable": "population", "source": "load_GDPdata.m:101-104; corrected_2018_runtime.py", "formula": "N0_NU=POP_raw*100", "factor": 100.0, "authority": "ACCEPTED_CORRECTED_2018", "raw_unit": "万人", "model_unit": "NU_100_PERSONS"},
            {"variable": "Track-A capital", "source": "load_GDPdata.m:55-61,94; It_to_Kt.m:1-10", "formula": "K0_MU=K_raw*1000; K_1=I_1/0.1; K_t=(1-delta)K_(t-1)+I_(t-1)", "factor": 1000.0, "divisor": 0.1, "delta": 0.096, "authority": "ACCEPTED_CORRECTED_2018", "raw_unit": "亿元", "model_unit": "MU_10WAN_YUAN"},
            {"variable": "per-capita GDP", "source": "load_GDPdata.m:126; mpHANK_equilibrium_2000.m:38,42", "formula": "Y0_MU/N0_NU", "factor": 1.0, "authority": "ACCEPTED_CORRECTED_2018_RATIO", "implied_unit": "1000 yuan/person/model period"},
            {"variable": "productivity", "source": "load_GDPdata.m:132-137; corrected_2018_runtime.py", "formula": "Zt0=Y0*K0^(-alpha)*N0^(alpha-1)", "factor": 1.0, "alpha": 0.7380939146868483, "authority": "ACCEPTED_CORRECTED_2018"},
            {"variable": "labor initialization", "source": "mpHANK_equilibrium_2000.m:29-30; corrected_2018_runtime.py", "formula": "L0=N0", "factor": 1.0, "authority": "ACCEPTED_POPULATION_PROXY_ONLY", "warning": "not household labor"},
            {"variable": "GovInv initialization", "source": "mpHANK_equilibrium_2000.m:40; corrected_2018_runtime.py", "formula": "GovInv0=K0*1", "factor": 1.0, "authority": "SOURCE_FAITHFUL_INITIALIZATION__REDESIGN_PENDING"},
            {"variable": "firm output/investment", "source": "HANK_firm.m:30,47", "formula": "Y=Z*K^alpha*L^(1-alpha); I=K-K_prev+delta_firm*K", "factor": 1.0, "delta_firm": 0.025, "authority": "PROTECTED_SOURCE_FORMULA"},
            {"variable": "firm wage guard", "source": "HANK_firm.m:43,66-74", "formula": "wjt=clip(mt*(1-alpha)*Z*(K/L)^alpha,0.8,1.3)", "lower": 0.8, "upper": 1.3, "authority": "PROTECTED_SOURCE_GUARD"},
            {"variable": "province share", "source": "mpHANK_equilibrium_2000.m:46-50", "formula": "0.3*(pcap-min)/(max-min)", "factor": 0.3, "authority": "PROTECTED_SOURCE_NORMALIZATION"},
            {"variable": "distance migration wedge", "source": "load_distdata.m:6-8", "formula": "distance/max(distance)*0.5", "factor": 0.5, "authority": "PROTECTED_SOURCE_NORMALIZATION"},
            {"variable": "sector GDP shares", "source": "load_GDPdata.m:95,97,99", "formula": "sector share/100", "divisor": 100.0, "authority": "PROTECTED_SOURCE_TRANSFORM"},
            {"variable": "legacy PIM capital", "source": "unit_scaling_audit.csv", "formula": "documented raw 万元*1000", "factor": 1000.0, "authority": "LEGACY_HISTORICAL_ONLY", "warning": "dimensional rationale unresolved; not active corrected Track-A route"},
        ],
        "dimensional_conclusion": "DIMENSIONAL_RELATION_UNRESOLVED",
        "same_state_triple": "GDP, population-derived Y/N, guarded wjt and composite w0 coexist in the accepted corrected-2018 initialization receipt; direct monetary comparability to wage is not proven.",
    }
    coarse.write_json(compact_root / "macro_scale_trace.json", trace)
    summary_rows = [
        ["province GDP", "Y0_MU", "corrected_2018_runtime.py", "亿元", "MU_10WAN_YUAN", "raw*1000", "1000", json.dumps(stats["province_gdp_Y0_MU"], separators=(",", ":")), "no"],
        ["province per-capita GDP", "Y0_MU/N0_NU", "load_GDPdata.m; receipt", "derived", "1000 yuan/person/model period (implied)", "Y0/N0", "1", json.dumps(stats["per_capita_output_Y0_over_N0"], separators=(",", ":")), "no"],
        ["firm wage", "wjt", "HANK_firm.m", "not proven", "MODEL_NORMALIZED", "guard(raw wage,0.8,1.3)", "guard", json.dumps(stats["guarded_firm_wage_wjt0"], separators=(",", ":")), "no"],
        ["household composite wage", "results.w/w0", "wage_caculate.m", "not proven", "MODEL_NORMALIZED_SCALE__MONETARY_UNIT_NOT_PROVEN", "cross-province aggregation", "nonlinear", json.dumps(stats["household_composite_wage_w0"], separators=(",", ":")), "no"],
        ["investment", "It", "load_GDPdata.m; HANK_firm.m", "亿元 in corrected source series", "MU status follows K flow", "PIM input; K-Kprev+delta*K", "delta .096/.025 by role", "UNAVAILABLE_FROM_ACCEPTED_EVIDENCE", "unknown"],
        ["capital", "K0_MU", "corrected_2018_runtime.py", "亿元", "MU_10WAN_YUAN", "raw*1000", "1000", json.dumps(stats["capital_K0_MU"], separators=(",", ":")), "yes with GDP only"],
        ["population", "N0_NU", "corrected_2018_runtime.py", "万人", "NU_100_PERSONS", "raw*100", "100", json.dumps(stats["population_N0_NU"], separators=(",", ":")), "yes for Y/N"],
        ["labor", "L0", "mpHANK_equilibrium_2000.m", "population proxy", "NU proxy", "L0=N0", "1", json.dumps(stats["initial_labor_proxy_L0_NU"], separators=(",", ":")), "not with household labor"],
        ["productivity", "Zt0", "corrected_2018_runtime.py", "derived", "MODEL_DERIVED", "Y*K^-alpha*N^(alpha-1)", "alpha=.7380939146868483", json.dumps(stats["productivity_Zt0"], separators=(",", ":")), "no standalone monetary comparison"],
    ]
    with (compact_root / "macro_scale_summary.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream); writer.writerow(["Variable", "Source object", "Source file/function", "Raw/statistical unit", "Model-normalized unit/status", "Transformation", "Multiplier/divisor", "Accepted numerical order of magnitude", "Can compare directly?"]); writer.writerows(summary_rows)
    return trace


def build(external_root: Path, compact_root: Path) -> int:
    external_root = Path(external_root); compact_root = Path(compact_root)
    if not (external_root / "execution_complete.json").is_file():
        raise ValueError("external execution is incomplete")
    compact_root.mkdir(parents=True, exist_ok=False)
    external_manifest = seal(external_root, "CH5_MP4C_K1_REAL_COMPOSITE_WAGE_3X3_EXTERNAL_V1")
    points = [read_json(path) for path in sorted(external_root.glob("p*_result.json"))]
    if len(points) != 9:
        raise ValueError("expected exactly nine point receipts")
    rows = []; marginals = []
    for point in points:
        hjb = point["hjb"]; kfe = point["kfe"]; dist = kfe.get("distribution", {}); agg = kfe.get("aggregates", {})
        label = None
        if hjb["classification"] == "HJB_CONVERGED" and kfe.get("ran") and kfe.get("completed", True):
            label = descriptive_distribution_label(np.asarray(dist["a_marginal_mass"]), kfe)
            marginals.append({"point_id": point["point_id"], "r_a": point["r_a"], "wage": point["wage"],
                              "a_grid": np.linspace(0, 10, 20).tolist(), "a_marginal_mass": dist["a_marginal_mass"],
                              "b_grid": np.linspace(-2, 5, 20).tolist(), "b_marginal_mass": dist["b_marginal_mass"]})
        point["distribution_label"] = label
        rows.append({"point_index": point["point_index"], "point_id": point["point_id"], "rb": point["r_b"], "ra": point["r_a"], "wage": point["wage"],
                     "hjb_classification": hjb["classification"], "iterations": hjb["iterations_used"], "final_statistic": hjb["final_convergence_statistic"],
                     "maximum_A2max": hjb["maximum_a2max"], "first_illegal_iteration": hjb["first_illegal_iteration"], "kfe_ran": kfe.get("ran", False),
                     "distribution_label": label, "Ct": agg.get("Ct"), "Lt": agg.get("Lt"), "At": agg.get("At"), "Bt": agg.get("Bt"),
                     "Bt_pos": dist.get("Bt_pos"), "Bt_neg": dist.get("Bt_neg"), "amin_mass": dist.get("boundary_mass_shares", {}).get("amin"),
                     "amax_mass": dist.get("boundary_mass_shares", {}).get("amax"), "bmin_mass": dist.get("boundary_mass_shares", {}).get("bmin"),
                     "bmax_mass": dist.get("boundary_mass_shares", {}).get("bmax"), "interior_a_mass": dist.get("interior_a_mass"),
                     "modal_a": json.dumps(dist.get("modal_a"), separators=(",", ":")), "modal_b": json.dumps(dist.get("modal_b"), separators=(",", ":")),
                     "top_3_a_bins": json.dumps(dist.get("top_3_a_bins"), separators=(",", ":")), "amax_to_adjacent_ratio": dist.get("amax_to_adjacent_interior_ratio"),
                     "total_mass": dist.get("total_mass"), "density_min": dist.get("density_min"), "density_negative_count": dist.get("density_negative_count"),
                     "kfe_raw_residual_inf": kfe.get("kfe", {}).get("raw_residual_inf")})
    macro = build_macro_artifacts(compact_root)
    robust = [ra for ra in RA_VALUES if all(any(row["ra"] == ra and row["wage"] == wage and row["distribution_label"] == "INTERIOR_A_DISTRIBUTION_CANDIDATE" for row in rows) for wage in WAGES)]
    unresolved = macro["dimensional_conclusion"] == "DIMENSIONAL_RELATION_UNRESOLVED"
    next_gate = "OWNER_REVIEW_JOINT_WJT_RA_MACRO_SCALE_RECALIBRATION" if unresolved or any(row["hjb_classification"] != "HJB_CONVERGED" or row["distribution_label"] == "KFE_NUMERICALLY_PATHOLOGICAL" for row in rows) else "OWNER_REVIEW_REAL_WAGE_DOMAIN_PROVINCIAL_PROJECTION"
    terminal = "REAL_WAGE_SCAN_COMPLETE__MACRO_DIMENSIONAL_RELATION_UNRESOLVED__JOINT_RECALIBRATION_OWNER_REVIEW_REQUIRED"
    summary = {"terminal_classification": terminal, "results_eligibility": False,
               "grid": {"rb": [0.02], "ra": list(RA_VALUES), "wage": list(WAGES)},
               "counts": {name: sum(row["distribution_label"] == name for row in rows) for name in sorted(LABELS)},
               "hjb_counts": {name: sum(row["hjb_classification"] == name for row in rows) for name in coarse.HJB_CLASSES},
               "wage_robust_interior_ra_values": robust, "recommended_next_gate": {"name": next_gate, "run_now": False},
               "dimensional_conclusion": macro["dimensional_conclusion"],
               "classification_semantics": {"post_result_fitted_cutoff": False,
                    "pathology_rounding_band": "100*IEEE754_float64_epsilon",
                    "distribution_basis": "raw signed evidence followed by exact modal/top-two endpoint ordering"},
               "kfe_caveat": "Accepted standalone contaminated-row KFE only; no negative mass was clipped; corrected-2018 multi-province finite-box/pinning issues remain separate."}
    coarse.write_json(compact_root / "summary.json", summary); coarse.write_json(compact_root / "marginals.json", marginals)
    coarse.write_json(compact_root / "point_receipts.json", points)
    source = read_json(external_root / "source_identity.json"); source["macro_accepted_receipt"] = {"path": str((REPO / "reports/mp4c_unit_normalized_initialization_probe_20260910/province_initialization_receipt.csv").resolve()), "sha256": coarse.file_sha256(REPO / "reports/mp4c_unit_normalized_initialization_probe_20260910/province_initialization_receipt.csv")}
    coarse.write_json(compact_root / "source_identity.json", source)
    for src, dst in (("input_invariance.json", "input_invariance_receipt.json"), ("final_call_ledger.json", "call_ledger.json"), ("sealed_manifest_sha256.json", "external_manifest.json")):
        coarse.write_json(compact_root / dst, read_json(external_root / src))
    with (compact_root / "points.csv").open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
    seal(compact_root, "CH5_MP4C_K1_REAL_COMPOSITE_WAGE_MACRO_SCALE_COMPACT_V1")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("external_root", type=Path); parser.add_argument("compact_root", type=Path)
    args = parser.parse_args(); return build(args.external_root, args.compact_root)


if __name__ == "__main__":
    raise SystemExit(main())
