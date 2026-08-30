"""Pure arithmetic for the MP1 three-province fixture.

This module is deliberately outside the production package.  It reproduces only
the source formulas needed to freeze MP1 expectations and never calls an HA,
HJB, KFE, fixed-point, MATLAB, or other scientific solver.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


DEFER_TO_MP2_SOURCE_FIXTURE = "DEFER_TO_MP2_SOURCE_FIXTURE"


def load_fixture(path: str | Path) -> dict[str, Any]:
    with Path(path).open(encoding="utf-8") as stream:
        fixture = json.load(stream)
    validate_fixture(fixture)
    return fixture


def validate_fixture(fixture: dict[str, Any]) -> None:
    if fixture.get("classification") != "NON_CALIBRATION_SYNTHETIC_OR_SOURCE_FORMULA_FIXTURE":
        raise ValueError("fixture classification is not the frozen MP1 classification")
    order = fixture.get("province_order")
    provinces = fixture.get("provinces")
    if not isinstance(order, list) or len(order) != 3 or len(set(order)) != 3:
        raise ValueError("fixture must have three unique ordered synthetic provinces")
    if not isinstance(provinces, list) or [p.get("name") for p in provinces] != order:
        raise ValueError("province records must exactly match province_order")
    for name in ("phi_mat", "sigmau_mat"):
        matrix = fixture.get(name)
        if not isinstance(matrix, list) or len(matrix) != 3 or any(
            not isinstance(row, list) or len(row) != 3 for row in matrix
        ):
            raise ValueError(f"{name} must have destination-by-origin shape (3, 3)")
    forbidden = json.dumps(fixture, sort_keys=True).lower()
    if "chapter5_model" in forbidden:
        raise ValueError("legacy R5 runtime dependency is forbidden")


def _labor_matrix(fixture: dict[str, Any]) -> list[list[float]]:
    """Lt_seperate.m:6-14; result[row destination][column origin]."""
    p = fixture["params"]
    provinces = fixture["provinces"]
    phi = fixture["phi_mat"]
    sigma = fixture["sigmau_mat"]
    matrix: list[list[float]] = [[0.0] * 3 for _ in range(3)]
    for origin in range(3):
        for destination in range(3):
            base = (
                provinces[destination]["wjt"]
                * (1.0 - provinces[origin]["tau"] - sigma[destination][origin])
                / phi[destination][origin]
            )
            if base < 0.0:
                raise ValueError("Lt_seperate source power would be non-real")
            matrix[destination][origin] = (
                provinces[origin]["Ct"] ** (-p["ga"] / p["phi_l"])
                * base ** (1.0 / p["phi_l"])
                * provinces[origin]["N"]
            )
    return matrix


def _capital_and_rah(fixture: dict[str, Any]) -> tuple[list[float], list[float], list[float]]:
    """HANK_mp_1turn.m:29-40, including its literal rah ratio placement."""
    provinces = fixture["provinces"]
    n_prov = len(provinces)
    contributions = [p["inter_prv_ratio"] * p["At"] * p["N"] for p in provinces]
    total_k = sum(contributions)
    total_ra = sum(p["inter_prv_ratio"] * p["ra"] for p in provinces)
    kt_supply = [(total_k - contribution) / (n_prov - 1) for contribution in contributions]
    rah = [
        (1.0 - p["inter_prv_ratio"]) * p["ra"]
        + p["inter_prv_ratio"]
        * (total_ra - p["inter_prv_ratio"] * p["ra"])
        / (n_prov - 1)
        for p in provinces
    ]
    return contributions, kt_supply, rah


def _firm(province: dict[str, float], kt_supply: float, labor: float, params: dict[str, float]) -> dict[str, float]:
    """Feasible steady-state branch of HANK_firm.m:5-98."""
    kt = kt_supply + province["GovInv"]
    alpha = province["alpha"]
    yt = province["Zt"] * kt**alpha * labor ** (1.0 - alpha)
    mstar = 1.0 - 1.0 / params["epsilon"]
    mt = (
        (
            province["rk"]
            - (province["Zt_1"] - province["Zt"]) / province["Zt"]
            - alpha * (province["Kt_prev"] - kt) / kt
            - (1.0 - alpha) * (province["Lt_prev"] - labor) / labor
        )
        * province["pit"]
        * params["theta"]
        / params["epsilon"]
        + mstar
        - (province["pit"] - province["pit_1"]) * params["theta"] / params["epsilon"]
    )
    knratio = kt / labor
    wt0 = mt * (1.0 - alpha) * province["Zt"] * knratio**alpha
    rk = mt * alpha / (kt / yt)
    thetat = params["theta"] * province["pit"] ** 2 * yt / 2.0
    investment = kt - province["Kt_prev"] + params["delta"] * kt
    profit = max((1.0 - mt) * yt - thetat, 0.0)
    corporate_tax = profit * province["corptau"]
    ra0 = rk - params["delta"] + profit * (1.0 - province["corptau"]) / kt
    ra = min(max(ra0, province["ramin"]), province["ramax"])
    if ra0 > province["ramax"]:
        corporate_tax += (ra0 - province["ramax"]) * kt
    elif ra0 < province["ramin"]:
        corporate_tax -= (province["ramin"] - ra0) * kt
    wjt = min(max(wt0, province["wjtmin"]), province["wjtmax"])
    if wt0 < province["wjtmin"]:
        corporate_tax -= (province["wjtmin"] - wt0) * labor
    elif wt0 > province["wjtmax"]:
        corporate_tax += (wt0 - province["wjtmax"]) * labor
    govinc = (
        corporate_tax
        + labor * province["tau"]
        + province["AtTax"]
        + province["GovInv"] * ra
        - province["Tt"]
    )
    return {
        "Kt": kt, "Lt": labor, "Yt": yt, "mt": mt, "KNratio": knratio,
        "wt0": wt0, "wjt": wjt, "rk": rk, "Thetat": thetat, "It": investment,
        "PIt": profit, "Corptax": corporate_tax, "ra0": ra0, "ra": ra,
        "Govinc": govinc,
    }


def _composite_wages(fixture: dict[str, Any], firm: list[dict[str, float]]) -> list[float]:
    """wage_caculate.m:4-16; output indexed by origin, tax indexed by destination."""
    params = fixture["params"]
    phi = fixture["phi_mat"]
    sigma = fixture["sigmau_mat"]
    provinces = fixture["provinces"]
    exponent = 1.0 + 1.0 / params["phi_l"]
    outer_exponent = params["phi_l"] / (1.0 + params["phi_l"])
    wages = []
    for origin in range(3):
        total = sum(
            phi[destination][origin]
            * (
                firm[destination]["wjt"]
                * (1.0 - provinces[destination]["tau"] - sigma[destination][origin])
                / phi[destination][origin]
            ) ** exponent
            for destination in range(3)
        )
        wages.append(params["alphal"] ** (-outer_exponent) * total**outer_exponent)
    return wages


def evaluate_fixture(fixture: dict[str, Any]) -> dict[str, Any]:
    validate_fixture(fixture)
    labor_matrix = _labor_matrix(fixture)
    labor_supply = [sum(row) for row in labor_matrix]
    contributions, kt_supply, rah = _capital_and_rah(fixture)
    firm = [
        _firm(province, kt_supply[i], labor_supply[i], fixture["params"])
        for i, province in enumerate(fixture["provinces"])
    ]
    composite_wage = _composite_wages(fixture, firm)
    params = fixture["params"]
    rb = params["istar"] + params["rho_pi"] * params["totalpit"] + params["epsilon_pi"] - params["totalpit"]
    gov_surplus = sum(
        firm[i]["Govinc"] - p["Bt"] * rb * p["N"]
        for i, p in enumerate(fixture["provinces"])
    )
    return {
        "Lt_mat": labor_matrix,
        "Lt_supply": labor_supply,
        "capital_contribution": contributions,
        "Kt_supply": kt_supply,
        "rah": rah,
        "firm": firm,
        "household_composite_wage": composite_wage,
        "rb": rb,
        "Govinc": [item["Govinc"] for item in firm],
        "GovSurplus": gov_surplus,
        "dynamic_or_fixed_point_objects": DEFER_TO_MP2_SOURCE_FIXTURE,
    }


def assert_close(actual: Any, expected: Any, *, tolerance: float = 1e-12) -> None:
    if isinstance(expected, dict):
        if set(actual) != set(expected):
            raise AssertionError(f"key mismatch: {set(actual) ^ set(expected)}")
        for key in expected:
            assert_close(actual[key], expected[key], tolerance=tolerance)
    elif isinstance(expected, list):
        if len(actual) != len(expected):
            raise AssertionError("length mismatch")
        for left, right in zip(actual, expected):
            assert_close(left, right, tolerance=tolerance)
    elif isinstance(expected, (int, float)) and not isinstance(expected, bool):
        if not math.isclose(float(actual), float(expected), rel_tol=tolerance, abs_tol=tolerance):
            raise AssertionError(f"{actual!r} != {expected!r}")
    elif actual != expected:
        raise AssertionError(f"{actual!r} != {expected!r}")
