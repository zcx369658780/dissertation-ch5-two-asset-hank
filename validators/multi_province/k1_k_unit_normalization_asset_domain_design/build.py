"""Build deterministic evidence for the k-unit/domain design audit.

This module reads accepted receipts and source files only.  It imports and
invokes no HJB, KFE, firm, MATLAB, outer-loop, or Results runtime.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import statistics
from pathlib import Path
from typing import Any, Iterable


REPO = Path(__file__).resolve().parents[3]
MATLAB = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK")
ALPHA = 0.7380939146868483
MONEY_FACTOR = 100.0  # current MU=100k currency -> proposed k currency
PERSON_FACTOR = 100.0  # current NU=100 persons -> persons


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    with Path(path).open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
        stream.write("\n")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    with Path(path).open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)


def rebase_identity(y: float, n: float, k: float, *, alpha: float) -> dict[str, float]:
    y_new = y * MONEY_FACTOR; n_new = n * PERSON_FACTOR; k_new = k * MONEY_FACTOR
    productivity_factor = MONEY_FACTOR / (
        MONEY_FACTOR**alpha * PERSON_FACTOR ** (1.0 - alpha)
    )
    return {
        "money_factor": MONEY_FACTOR, "person_factor": PERSON_FACTOR,
        "old_y_over_n": y / n, "new_y_over_n": y_new / n_new,
        "old_k_over_n": k / n, "new_k_over_n": k_new / n_new,
        "productivity_factor": productivity_factor,
        "firm_wage_factor": productivity_factor * (MONEY_FACTOR / PERSON_FACTOR) ** alpha,
    }


def household_rescale_transform(scale: float, *, gamma: float) -> dict[str, float]:
    """Generic per-capita money rescale under the wage-aggregation-compatible gauge.

    With x'=s*x, keep utility/value cardinal levels and labor disutility fixed;
    the CRRA consumption weight must scale s^(gamma-1).  This is a conditional
    derivation, not authority to apply an unproven household scale.
    """
    if scale <= 0.0:
        raise ValueError("household scale must be positive")
    return {
        "monetary_levels": scale, "consumption_utility_weight_alphac": scale ** (gamma - 1.0),
        "labor_disutility_weight_alphal": 1.0, "value_function": 1.0,
        "a_bar": scale, "derivative_floor": 1.0 / scale,
        "drift_tolerance": scale, "chi0": 1.0, "chi1": 1.0,
        "rates": 1.0, "time_step": 1.0, "convergence_tolerance_on_value": 1.0,
    }


def asset_domain_design() -> dict[str, Any]:
    current = {"amin": 0.0, "amax": 10.0, "bmin": -2.0, "bmax": 5.0,
               "I": 20, "J": 20, "da": 10.0 / 19.0, "db": 7.0 / 19.0}
    candidates = [
        {"bmin": -2.0, "bmax": bmax, "I": 20, "db": (bmax + 2.0) / 19.0,
         "relative_to_current_db": ((bmax + 2.0) / 19.0) / current["db"],
         "interpretation_if_bridge_accepted": f"liquid upper bound {bmax:.0f}k per person"}
        for bmax in (20.0, 50.0)
    ]
    return {
        "current": current,
        "proposed_a": {"amin": 0.0, "amax": 100.0, "J": 20, "da": 100.0 / 19.0,
                       "relative_to_current_da": 10.0,
                       "interpretation": "individual household state-grid bound, never an At cap"},
        "b_candidates": candidates, "bmax_decision": "BMAX_OWNER_SELECTION_REQUIRED",
        "b_candidate_basis": {
            "accepted_Bt_range": [1.609508492120329, 4.699508302009303],
            "accepted_bmax_mass_range": [0.13089555280363818, 0.6834030069036136],
            "accepted_b_mode_at_current_bmax": "9/9",
            "conditional_household_wage_range_k_per_period": [13.0, 18.0],
            "rationale": "20 spans roughly one wage-flow unit and >4x observed maximum Bt; 50 is near median per-capita GDP and >10x observed maximum Bt. Evidence cannot select between them without runtime, so neither is frozen.",
        },
        "bmin": {"proposal": -2.0, "status": "PRESERVE_FOR_FIRST_DIAGNOSTIC_ONLY",
                 "conditional_interpretation": "-2k per person if the household bridge is accepted",
                 "evidence": "no accepted lower-b pile-up; not a claim that borrowing calibration is final"},
        "precision_conclusion": "I=J=20_IS_ACCEPTABLE_ONLY_FOR_FIRST_DOMAIN_DIAGNOSTIC__SEPARATE_PRECISION_SENSITIVITY_MANDATORY_BEFORE_PRODUCTION",
    }


def dimension_rows() -> list[dict[str, str]]:
    items = [
        ("GDP/Y", "MONETARY_FLOW", "province aggregate flow", "current MU; proposed total k"),
        ("K", "MONETARY_STOCK", "province aggregate stock", "current MU; proposed total k"),
        ("I", "MONETARY_FLOW", "province aggregate investment flow", "source series/firm flow roles differ"),
        ("GovInv", "MONETARY_STOCK", "added to Kt in source", "name says investment but equation role is stock"),
        ("C", "PER_CAPITA_MONETARY_FLOW", "household consumption", "k/person/period only if bridge accepted"),
        ("Tt", "PER_CAPITA_MONETARY_FLOW", "household transfer", "k/person/period only if bridge accepted"),
        ("tax flows", "MONETARY_FLOW", "Corptax/Govinc/AtTax", "aggregate or per-capita role must remain explicit"),
        ("a", "PER_CAPITA_MONETARY_STOCK", "individual illiquid state", "k/person only if bridge accepted"),
        ("b", "PER_CAPITA_MONETARY_STOCK", "individual liquid state", "k/person only if bridge accepted"),
        ("At", "PER_CAPITA_MONETARY_STOCK", "stationary mean illiquid asset", "not amax and not provincial total"),
        ("Bt", "PER_CAPITA_MONETARY_STOCK", "stationary mean liquid asset", "not bmax and not provincial total"),
        ("adjustment cost", "PER_CAPITA_MONETARY_FLOW", "household transfer cost", "same unit as d and C"),
        ("transfer control d", "PER_CAPITA_MONETARY_FLOW", "asset flow between a and b", "same monetary/time unit as drifts"),
        ("wjt", "DIMENSION_UNRESOLVED", "firm wage per labor", "numeric k/person/period mapping plausible but unproven"),
        ("household composite w", "DIMENSION_UNRESOLVED", "HJB wage input", "homogeneous wage aggregation; real-money bridge unproven"),
        ("population", "PERSON_QUANTITY", "province population", "current NU=100 persons; proposed persons"),
        ("labor", "PERSON_QUANTITY", "firm Lt_supply", "household l is time/intensity; do not conflate"),
        ("household labor l", "RATE_OR_DIMENSIONLESS", "individual labor intensity/time", "not province headcount"),
        ("productivity", "DIMENSION_UNRESOLVED", "Cobb-Douglas residual", "numeric invariant only under joint money/person rebase"),
        ("ra", "RATE_OR_DIMENSIONLESS", "illiquid return rate", "monetary rescale leaves unchanged"),
        ("rb", "RATE_OR_DIMENSIONLESS", "liquid return rate", "monetary rescale leaves unchanged"),
        ("borrowing gap", "RATE_OR_DIMENSIONLESS", "rate spread", "monetary rescale leaves unchanged"),
        ("delta", "RATE_OR_DIMENSIONLESS", "depreciation rate", "time-base conflict remains separate"),
        ("rho", "RATE_OR_DIMENSIONLESS", "discount rate", "time-base conflict remains separate"),
        ("tax rates", "RATE_OR_DIMENSIONLESS", "tau/corptau", "unchanged"),
        ("price/return guards", "RATE_OR_DIMENSIONLESS", "ra guard is a rate", "wjt guard inherits unresolved wage dimension"),
        ("chi0", "RATE_OR_DIMENSIONLESS", "proportional transfer cost", "monetary-scale invariant"),
        ("chi1", "RATE_OR_DIMENSIONLESS", "quadratic transfer time coefficient", "monetary-scale invariant; time-base not resolved"),
        ("a_bar", "PER_CAPITA_MONETARY_STOCK", "cost denominator floor", "must follow household asset scale"),
        ("CRRA gamma", "RATE_OR_DIMENSIONLESS", "curvature", "unchanged"),
        ("labor weight alphal", "UTILITY_VALUE_OBJECT", "labor disutility/wage aggregator weight", "unchanged in canonical value gauge"),
        ("consumption weight alphac", "UTILITY_VALUE_OBJECT", "hard-coded consumption utility weight", "changes if household money numerics change"),
        ("value function", "UTILITY_VALUE_OBJECT", "discounted utility", "kept numerically invariant in canonical gauge"),
        ("derivative floor", "NUMERICAL_ONLY", "marginal-value floor", "inverse household money-scale transform required"),
        ("HJB convergence tolerance", "NUMERICAL_ONLY", "value-space tolerance", "unchanged in canonical value gauge"),
        ("drift tolerance", "NUMERICAL_ONLY", "asset-flow direction tolerance", "follows household money scale"),
    ]
    return [{"variable": a, "classification": b, "source_role": c, "k_unit_status": d} for a, b, c, d in items]


def original_scaling_trace() -> dict[str, Any]:
    return {
        "schema": "CH5_MP4C_K1_ORIGINAL_MATLAB_SCALING_TRACE_V1",
        "comparatively_good_version_comment": {
            "source": "multi_prov_HANK_12sts.m:80-81",
            "comment": "param.GDP_multiplier=1000; param.POP_multiplier = 100; % 比较好的一个版本",
            "active_values": {"GDP_multiplier": 1000, "POP_multiplier": 100},
        },
        "variables": [
            {"variable": "GDP total", "raw_unit": "亿元", "internal": "raw*GDP_multiplier=raw*1000", "model_unit": "MU=10万元", "export": "/1000", "source": "load_GDPdata.m:3,93; main.m:167-168"},
            {"variable": "sector GDP", "raw_unit": "GDP share percent", "internal": "total*share/100", "model_unit": "source ambiguity: sector line lacks GDP_multiplier", "export": "not separately traced", "source": "load_GDPdata.m:95,97,99"},
            {"variable": "capital", "raw_unit": "legacy comment: investment 万元", "internal": "PIM then *GDP_multiplier=1000", "model_unit": "legacy dimensional rationale unresolved; corrected Track-A is 亿元*1000 MU", "export": "/1000", "source": "load_GDPdata.m:3,55-61,94; main.m:169-170"},
            {"variable": "investment/PIM", "raw_unit": "legacy source comment 万元", "internal": "K0=I0/0.1; Kt=(1-.096)Kt-1+It-1", "model_unit": "inherited capital route", "export": "none found", "source": "It_to_Kt.m:1-10; multi_prov_HANK_12sts.m:128"},
            {"variable": "firm investment", "raw_unit": "model capital flow", "internal": "It=Kt-Kt_1+.025Kt", "model_unit": "capital units/model period", "export": "none found", "source": "HANK_firm.m:47"},
            {"variable": "population", "raw_unit": "万人", "internal": "raw*POP_multiplier=raw*100", "model_unit": "NU=100 persons", "export": "/100", "source": "load_GDPdata.m:3,101-104; main.m:171"},
            {"variable": "firm labor", "raw_unit": "person proxy/allocated labor", "internal": "N initialized as L; household hours*N", "model_unit": "NU-weighted labor", "export": "/100", "source": "mpHANK_equilibrium_2000.m:29-30; Lt_seperate.m:6-14; main.m:172"},
            {"variable": "GovInv", "raw_unit": "capital stock role", "internal": "Kt0*GovInv_ratio; ratio=1", "model_unit": "capital units", "export": "none found", "source": "mpHANK_equilibrium_2000.m:40; multi_prov_HANK_12sts.m:83"},
            {"variable": "consumption C/Ct", "raw_unit": "unproven household money flow", "internal": "no GDP multiplier/divisor found; Ct is density mean; Ct_total=Ct*N", "model_unit": "household per-capita flow / aggregate after N", "export": "none found", "source": "HANK_2ASSETS_HJB.m:124-136,354; HANK_firm.m:89"},
            {"variable": "transfer Tt", "raw_unit": "unproven household money flow", "internal": "initial .1; enters liquid budget additively", "model_unit": "same as C if coherent", "export": "none found", "source": "multi_prov_HANK_12sts.m:94; HANK_2ASSETS_HJB.m:111,263"},
            {"variable": "a/b/At/Bt", "raw_unit": "unproven household per-capita money stock", "internal": "a=[0,10], b=[-2,5]; density means", "model_unit": "household asset units", "export": "none found", "source": "multi_prov_HANK_12sts.m:34-42; HANK_2ASSETS_HJB.m:348-351"},
            {"variable": "wjt", "raw_unit": "unproven wage per labor", "internal": "marginal product then guard [.8,1.3]", "model_unit": "firm wage scale", "export": "none found", "source": "HANK_firm.m:43,66-81"},
            {"variable": "household composite w", "raw_unit": "unproven wage per household labor", "internal": "nonlinear homogeneous aggregation across 31 wjt", "model_unit": "HJB wage input", "export": "none found", "source": "wage_caculate.m:1-17"},
            {"variable": "productivity Z", "raw_unit": "derived", "internal": "Y*K^-alpha*N^(alpha-1); Ztratio=1", "model_unit": "scale-dependent residual", "export": "none found", "source": "load_GDPdata.m:126-137; multi_prov_HANK_12sts.m:82"},
        ],
        "not_found": ["global all-variables /1000 rule", "household money-to-MU bridge", "nominal-to-real deflator", "x10000/x1e4/x1e8 conversion in designated chain"],
    }


def equation_transforms() -> dict[str, Any]:
    return {
        "schema": "CH5_MP4C_K1_EQUATION_SCALING_TRANSFORM_V1",
        "conventions": {
            "aggregate_money": "Y',K',I',GovInv',tax'=100*x (MU to k)",
            "persons": "N',L'=100*x (NU to persons)",
            "per_capita_money": "h*x; proposed h=1 only if household bridge is accepted",
            "rates": "unchanged", "canonical_utility_gauge": "V'=V and alphal'=alphal",
        },
        "equations": [
            {"name": "CRRA utility", "equation": "u=alphac*c^(1-gamma)/(1-gamma)-alphal*l^(1+phi)/(1+phi)", "transform": "c'=h*c; alphac'=h^(gamma-1)*alphac; alphal'=alphal; u'=u; V'=V", "status": "conditional on h"},
            {"name": "marginal utility/consumption FOC", "equation": "c=(Vb/alphac)^(-1/gamma)", "transform": "Vb'=Vb/h and alphac'=h^(gamma-1)alphac imply c'=h*c", "status": "exact symbolic equivalence"},
            {"name": "labor FOC", "equation": "l=(Vb*net_wage/alphal)^(1/phi)", "transform": "Vb'=Vb/h; wage'=h*w; alphal unchanged => l'=l", "status": "exact symbolic equivalence"},
            {"name": "liquid drift", "equation": "mu_b=rb*b+net_wage*l+Tt-d-cost-c", "transform": "b,w,Tt,d,cost,c all *h; rates unchanged => mu_b'=h*mu_b", "status": "homogeneous"},
            {"name": "illiquid drift", "equation": "mu_a=r_a_eff*a+d", "transform": "a,d *h; r_a unchanged => mu_a'=h*mu_a", "status": "homogeneous"},
            {"name": "adjustment cost", "equation": "chi0*abs(d)+.5*chi1*d^2/max(a,a_bar)", "transform": "d,a,a_bar *h; chi0,chi1 unchanged => cost'=h*cost", "status": "homogeneous only if a_bar scales"},
            {"name": "transfer FOC", "equation": "d=a/chi1*[min(Va/Vb-1+chi0,0)+max(Va/Vb-1-chi0,0)]", "transform": "Va/Vb invariant; a*h; chi0/chi1 unchanged => d'=h*d", "status": "exact symbolic equivalence"},
            {"name": "borrowing spread", "equation": "Rb=rb+gap when b<0", "transform": "rb and gap unchanged; Rb*b scales h", "status": "homogeneous"},
            {"name": "wjt to household w", "equation": "w=alphal^(-phi/(1+phi))*sum(phi*(wjt*wedge/phi)^(1+1/phi))^(phi/(1+phi))", "transform": "with alphal unchanged, scaling all wjt by h scales w by h", "status": "homogeneous degree one; monetary bridge still unproven"},
            {"name": "firm output", "equation": "Y=Z*K^alpha*L^(1-alpha)", "transform": "Y,K,L all *100 => Z unchanged", "status": "exact under joint aggregate money/person rebase"},
            {"name": "firm wage", "equation": "wt0=mt*(1-alpha)*Z*(K/L)^alpha", "transform": "K/L unchanged and Z unchanged => wage numeric unchanged, reinterpreted k/person", "status": "macro identity; household bridge unproven"},
            {"name": "firm investment", "equation": "I=K-Kprev+delta*K", "transform": "K and I *100; delta unchanged", "status": "homogeneous"},
            {"name": "capital return", "equation": "rk=mt*alpha*Y/K; ra0=rk-delta+profit*(1-tax)/K", "transform": "Y,K,profit all *100; rates unchanged", "status": "monetary invariant; separate time-base conflict remains"},
            {"name": "government account", "equation": "Govinc=Corptax+Lt*tau+AtTax+GovInv*ra-Tt", "transform": "source mixes aggregate and transfer roles; all monetary terms must be placed on the same aggregate basis before implementation", "status": "DIMENSION_UNRESOLVED"},
            {"name": "HJB numerics", "equation": "derivatives, drift directions, implicit value solve", "transform": "if h!=1: derivative floor /h, drift tolerance *h; value convergence tolerance unchanged in canonical gauge", "status": "non-homogeneous numerical constants must transform"},
        ],
        "bridge_conclusion": "MONETARY_UNIT_BRIDGE_UNPROVEN",
    }


def parameter_rows() -> list[dict[str, str]]:
    rows = [
        ("GDP_multiplier", "1000", "100000", "unit conversion", "1亿元=100000k"),
        ("POP_multiplier", "100", "10000", "quantity-unit conversion", "1万人=10000 persons"),
        ("aggregate Y/K/I/GovInv/taxes", "x", "100*x", "unit conversion", "MU to k"),
        ("N and aggregate firm labor", "x", "100*x", "quantity-unit conversion", "NU to persons"),
        ("Z", "x", "x", "derived invariant", "money and person factors both 100"),
        ("wjt/wjt guards", "x", "x", "conditional invariant", "K/L numeric unchanged; real-money bridge must be frozen"),
        ("household w/C/Tt/a/b/At/Bt", "x", "x", "conditional invariant", "only if current per-capita household unit is accepted as k/person"),
        ("alphac", "1 hard-coded", "1 if h=1; h^(gamma-1) otherwise", "utility normalization", "required for unit-equivalent CRRA under h!=1"),
        ("alphal/labor weights", "x", "x", "utility normalization", "canonical V-invariant gauge and wage aggregation"),
        ("a_bar", "1e-6", "1e-6 if h=1; h*1e-6 otherwise", "unit conversion", "same unit as a"),
        ("derivative floor", "1e-6", "1e-6 if h=1; 1e-6/h otherwise", "numerical unit conversion", "marginal value scales 1/h"),
        ("drift tolerance", "1e-12", "1e-12 if h=1; h*1e-12 otherwise", "numerical unit conversion", "asset drift scales h"),
        ("chi0", ".1", ".1", "unchanged", "proportional cost"),
        ("chi1", "2", "2", "unchanged for money rebase", "time dimension remains separate unresolved calibration"),
        ("ra/rb/borrowing gap", "source values", "unchanged", "rate", "never rescale with money"),
        ("rho/Qz/delta/tax rates", "source values", "unchanged", "rate/dimensionless", "time-base conflict is outside money-unit conversion"),
        ("I/J", "20/20", "20/20 first diagnostic", "precision controls", "later sensitivity mandatory"),
        ("amin/amax", "0/10", "0/100", "economic domain expansion", "not a unit conversion and not an At cap"),
        ("bmin/bmax", "-2/5", "-2/{20 or 50}", "economic domain expansion", "Owner selection required"),
    ]
    return [{"object": a, "current_numeric": b, "proposed_numeric": c, "change_type": d, "reason": e} for a, b, c, d, e in rows]


def _stats(values: Iterable[float]) -> str:
    values = list(values)
    return json.dumps({"min": min(values), "median": statistics.median(values), "max": max(values)}, separators=(",", ":"))


def macro_rows() -> list[dict[str, str]]:
    receipt = REPO / "reports/mp4c_unit_normalized_initialization_probe_20260910/province_initialization_receipt.csv"
    with receipt.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    points_path = REPO / "docs/evidence/ch5_mp4c_k1_real_composite_wage_domain_macro_scale_audit/points.csv"
    with points_path.open(encoding="utf-8-sig", newline="") as stream:
        points = list(csv.DictReader(stream))
    if len(rows) != 31 or len(points) != 9:
        raise ValueError("accepted macro/standalone evidence row count mismatch")
    values = lambda key: [float(row[key]) for row in rows]
    point_values = lambda key: [float(row[key]) for row in points]
    data = [
        ("province GDP", "Y0_MU", "MU=100k aggregate", "total k", "*100", _stats(values("Y0_MU")), _stats(x * 100 for x in values("Y0_MU")), "PROVEN"),
        ("population", "N0_NU", "NU=100 persons", "persons", "*100", _stats(values("N0_NU")), _stats(x * 100 for x in values("N0_NU")), "PROVEN"),
        ("per-capita GDP", "Y0_MU/N0_NU", "algebraic k/person", "k/person", "unchanged", _stats(values("Y_to_N")), _stats(values("Y_to_N")), "PROVEN_MACRO_RATIO"),
        ("capital", "K0_MU", "MU=100k aggregate", "total k", "*100", _stats(values("K0_MU")), _stats(x * 100 for x in values("K0_MU")), "PROVEN"),
        ("investment", "I", "source/firm flow", "total k/period", "*100 if same aggregate route", "UNAVAILABLE_FROM_ACCEPTED_EVIDENCE", "UNAVAILABLE_FROM_ACCEPTED_EVIDENCE", "FORMULA_ONLY"),
        ("raw firm wage", "raw_wjt0", "MU/NU algebra", "k/person/period", "numeric unchanged", _stats(values("raw_wjt0")), _stats(values("raw_wjt0")), "MACRO_FORMULA_PROVEN__HOUSEHOLD_BRIDGE_UNPROVEN"),
        ("guarded wjt", "used_wjt0", "legacy guard scale", "candidate k/person/period", "numeric unchanged conditionally", _stats(values("used_wjt0")), _stats(values("used_wjt0")), "MONETARY_UNIT_BRIDGE_UNPROVEN"),
        ("household composite wage", "w0", "household wage scale", "candidate k/person/period", "numeric unchanged conditionally", _stats(values("w0")), _stats(values("w0")), "MONETARY_UNIT_BRIDGE_UNPROVEN"),
        ("household At", "At", "household mean asset", "candidate k/person", "numeric unchanged conditionally", _stats(point_values("At")), _stats(point_values("At")), "MONETARY_UNIT_BRIDGE_UNPROVEN"),
        ("household Bt", "Bt", "household mean asset", "candidate k/person", "numeric unchanged conditionally", _stats(point_values("Bt")), _stats(point_values("Bt")), "MONETARY_UNIT_BRIDGE_UNPROVEN"),
    ]
    return [{"variable": a, "source_object": b, "current_unit_status": c, "proposed_k_unit": d,
             "numeric_transform": e, "accepted_current_range": f, "proposed_range": g, "authority": h}
            for a, b, c, d, e, f, g, h in data]


def implementation_proposal() -> dict[str, Any]:
    return {
        "schema": "CH5_MP4C_K1_K_UNIT_ASSET_DOMAIN_IMPLEMENTATION_PROPOSAL_V1",
        "status": "BLOCKED_PENDING_OWNER_HOUSEHOLD_BRIDGE_AND_BMAX_SELECTION",
        "unit_conversion": {
            "aggregate_money_factor": 100.0, "person_factor": 100.0,
            "GDP_multiplier": 100000.0, "POP_multiplier": 10000.0,
            "rescale": ["Y/Y0", "K/K0/Kprev/Kt_supply/GovInv", "I", "profit", "corporate/government aggregate money flows", "N and firm aggregate labor"],
            "conditional_numeric_invariants": ["per-capita GDP", "K/N", "Z", "raw wjt", "household composite w", "C/Tt/a/b/At/Bt"],
            "rates_unchanged": ["ra", "rb", "borrowing gap", "rho", "Qz", "delta", "tax rates", "inflation rates"],
        },
        "required_owner_freezes": [
            "Accept or reject identity: current household w/C/Tt/a/b/At/Bt numeric unit equals k per person(/period).",
            "Select bmax=20 or bmax=50; neither is selected by this audit.",
            "Keep bmin=-2 for first diagnostic or issue a separate borrowing-domain calibration.",
        ],
        "domain_after_selection": {"amin": 0.0, "amax": 100.0, "bmin": -2.0,
                                   "bmax": "OWNER_SELECT_20_OR_50", "I": 20, "J": 20,
                                   "da": 100.0 / 19.0,
                                   "db": {"if_bmax_20": 22.0 / 19.0, "if_bmax_50": 52.0 / 19.0}},
        "candidate_changed_files": [
            "src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py",
            "validators/multi_province/corrected_2018_single_turn/run.py",
            "task-owned future normalization/domain adapter and tests",
        ],
        "protected_no_change_without_separate_authority": [
            "exports/matlab_faithful_two_asset_ha.py", "protected MATLAB",
            "HJB/KFE equations", "wjt/return guard semantics", "ra mapping", "time-base calibration",
        ],
        "pre_science_parity_checks": [
            "31/31 raw-to-k identities: GDP and K *100; N *100; Y/N and K/N invariant",
            "31/31 Cobb-Douglas Y identity with unchanged Z and alpha",
            "31/31 raw firm wage and return identities numerically invariant before guards",
            "wjt-to-composite-w homogeneity receipt and household bridge assertion",
            "household equation symbolic/unit parity including CRRA weight, a_bar, derivative floor and drift tolerance",
            "grid endpoints/counts/spacing exact and fresh initialization; no warm start",
        ],
        "first_post_implementation_standalone_grid": {
            "condition": "only after Owner freezes household bridge and one bmax",
            "rb": [0.02], "ra": [0.06, 0.0675, 0.07], "household_w_k": [13.0, 15.5, 18.0],
            "amin": 0.0, "amax": 100.0, "bmin": -2.0, "bmax": "OWNER_SELECTED_20_OR_50",
            "I": 20, "J": 20, "points": 9, "fresh_initialization": True,
        },
        "falsifiers_and_hard_stops": [
            "Any source identity mismatch or failed raw-to-k exact identity stops before HJB.",
            "Any need to alter rates, HJB/KFE equations, wjt guard, ra mapping or time base stops and returns to Owner.",
            "If household monetary bridge remains unproven, no scientific run is authorized.",
            "Any parity mismatch at common physical states stops; do not tune scaling or bounds.",
            "First diagnostic cannot establish production precision; separate I/J sensitivity is mandatory.",
        ],
        "run_now": False, "successor_task_published": False,
    }


def seal(root: Path) -> None:
    target = root / "sealed_manifest_sha256.json"
    entries = [{"path": path.name, "bytes": path.stat().st_size, "sha256": sha256(path)}
               for path in sorted(root.iterdir()) if path.is_file() and path != target]
    write_json(target, {"schema": "CH5_MP4C_K1_K_UNIT_ASSET_DOMAIN_DESIGN_MANIFEST_V1",
                        "entry_count": len(entries), "entries": entries})


def build(output: Path) -> int:
    root = Path(output)
    if root.exists():
        if not root.is_dir() or any(root.iterdir()):
            raise FileExistsError(f"evidence output must be a new or empty directory: {root}")
    else:
        root.mkdir(parents=True, exist_ok=False)
    write_json(root / "original_matlab_scaling_trace.json", original_scaling_trace())
    write_csv(root / "dimension_classification.csv", dimension_rows())
    write_json(root / "equation_scaling_transform.json", equation_transforms())
    write_csv(root / "parameter_transform_table.csv", parameter_rows())
    domain = asset_domain_design()
    write_json(root / "asset_domain_design.json", domain)
    write_json(root / "grid_spacing_receipt.json", {
        "schema": "CH5_MP4C_K1_GRID_SPACING_RECEIPT_V1", "current": domain["current"],
        "proposed_a": domain["proposed_a"], "b_candidates": domain["b_candidates"],
        "precision_conclusion": domain["precision_conclusion"]})
    write_csv(root / "macro_k_unit_mapping.csv", macro_rows())
    write_json(root / "implementation_proposal.json", implementation_proposal())
    sources = [
        REPO / "exports/matlab_faithful_two_asset_ha.py",
        REPO / "src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py",
        REPO / "src/ch5_two_asset_hank/multi_province/firm.py",
        REPO / "src/ch5_two_asset_hank/multi_province/wage.py",
        REPO / "reports/mp4c_unit_normalized_initialization_probe_20260910/province_initialization_receipt.csv",
        REPO / "docs/evidence/ch5_mp4c_k1_real_composite_wage_domain_macro_scale_audit/points.csv",
        MATLAB / "multi_prov_HANK_12sts.m", MATLAB / "load_GDPdata.m", MATLAB / "It_to_Kt.m",
        MATLAB / "HANK_2ASSETS_HJB.m", MATLAB / "HANK3_cost.m", MATLAB / "HANK3_FOC.m",
        MATLAB / "HANK_firm.m", MATLAB / "wage_caculate.m", MATLAB / "Lt_seperate.m", MATLAB / "main.m",
    ]
    write_json(root / "source_identity.json", {
        "schema": "CH5_MP4C_K1_K_UNIT_ASSET_DOMAIN_SOURCE_IDENTITY_V1",
        "files": [{"path": str(path.resolve()), "bytes": path.stat().st_size, "sha256": sha256(path)} for path in sources],
        "source_reads_only": True,
    })
    write_json(root / "call_ledger.json", {
        "schema": "CH5_MP4C_K1_K_UNIT_ASSET_DOMAIN_ZERO_RUNTIME_LEDGER_V1",
        "hjb": 0, "kfe": 0, "global_outer": 0, "firm_runtime": 0, "matlab_runtime": 0,
        "k1b": 0, "k2": 0, "ge": 0, "downstream": 0, "shock": 0, "irf": 0,
        "results": 0, "scientific_retries": 0, "parameter_or_grid_changes": 0,
        "deterministic_offline_audit_builds": 1,
    })
    seal(root)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("output", type=Path)
    return build(parser.parse_args().output)


if __name__ == "__main__":
    raise SystemExit(main())
