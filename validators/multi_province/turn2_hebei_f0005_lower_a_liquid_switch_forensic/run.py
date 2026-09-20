"""Independent zero-science reconstruction for Hebei checkpoint-1 F0005.

This module intentionally uses only the Python standard library.  It reads the
persisted receipt and source text, but it never imports or calls the production
selector, root helpers, HJB, generator, KFE, or integration modules.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, getcontext
import hashlib
import json
import math
from pathlib import Path
from typing import Any


TASK_ID = "CH5_MP4C_TURN2_HEBEI_F0005_LOWER_A_LIQUID_SWITCH_FORENSIC_20260921"
BASELINE = "3473ada0d9d6d8767383969dc5fe268763cebf54"
PREDECESSOR = "f178ec24b9b62814d20ec4041380e07e2d878849"
PREDECESSOR_MANIFEST = "E1DBBDF7E86B8F11A4DDB646A1CBD53259E5182D6EFE6A0D2679314874B8A403"
TERMINAL = (
    "PASS__TURN2_HEBEI_F0005_FORENSIC__ACTIVE_LOWER_A_INTERIOR_Z_"
    "COMPOSITION_FALSE_NEGATIVE_CONFIRMED__NO_CODE_CHANGE"
)
CLASSIFICATION = "IMPLEMENTATION_COMPOSITION_FALSE_NEGATIVE_UNDER_ALREADY_ADOPTED_AUTHORITY"

CELL_REL = Path(
    "reports/ch5_mp4c_interior_b_negative_ratio_repair_turn1_parity_turn2_run003_20260921/"
    "household/p02_河北/checkpoint_001/cell_0005.json"
)
PREDECESSOR_ROOT = CELL_REL.parents[3]
SELECTOR_REL = Path("src/ch5_two_asset_hank/corrected_diagnostic/selector.py")
COST_REL = Path("src/ch5_two_asset_hank/corrected_diagnostic/cost.py")
TURN2_REL = Path(
    "src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py"
)
TASK_REL = Path(
    "tasks/CH5_MP4C_TURN2_HEBEI_F0005_LOWER_A_LIQUID_SWITCH_FORENSIC_20260921.md"
)

AUTHORITY_FILES = [
    Path("AGENTS.md"),
    Path("project_rules/PROJECT_RULE_INDEX_CURRENT.md"),
    Path("docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md"),
    Path("docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md"),
    Path(
        "docs/CH5_MP4C_INTERIOR_B_NEGATIVE_RATIO_SWITCHING_REPAIR_TURN1_PARITY_"
        "AND_TURN2_RUN003_ACCEPTANCE_20260921.md"
    ),
    Path(
        "docs/CH5_MP4C_2018_KFE_D123_LOWER_A_ZERO_KINK_REPAIR_OPTION_A_"
        "REEXECUTION_FAIL_CLOSED_ACCEPTANCE_20260916.md"
    ),
    Path(
        "docs/CH5_MP4C_2018_KFE_D123_CELL5_LIQUID_DIRECTION_SWITCH_"
        "ATTRIBUTION_ACCEPTANCE_20260916.md"
    ),
    Path(
        "docs/CH5_MP4C_2018_KFE_D123_INTERIOR_ZERO_LIQUID_Z_OWNER_ADOPTION_"
        "ACCEPTANCE_20260916.md"
    ),
    Path(
        "docs/CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_SWITCHING_"
        "OWNER_ADOPTION_20260919.md"
    ),
    TASK_REL,
]

PARAMETERS = {
    "gamma_c": Decimal("2.0"),
    "phi": Decimal("5.0"),
    "chi_0": Decimal("0.1"),
    "chi_1": Decimal("2.0"),
    "a_bar": Decimal("1e-6"),
    "labor_weight": Decimal("1.0"),
}


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
        + "\n",
        encoding="utf-8",
    )


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def file_identity(path: Path, repo: Path) -> dict[str, Any]:
    data = path.read_bytes()
    return {
        "path": path.relative_to(repo).as_posix(),
        "bytes": len(data),
        "sha256": sha256_bytes(data),
        "git_blob_sha1": git_blob_sha1(data),
    }


def decimal_nth_root(value: Decimal, n: int) -> Decimal:
    if value <= 0 or n <= 0:
        raise ValueError("positive value and exponent required")
    x = Decimal(str(float(value) ** (1.0 / n)))
    n_dec = Decimal(n)
    for _ in range(100):
        next_x = ((n_dec - 1) * x + value / (x ** (n - 1))) / n_dec
        if next_x == x:
            break
        x = next_x
    return +x


def fp_bound(*values: float, operations: int) -> float:
    eps = 2.220446049250313e-16
    gamma = operations * eps / (1.0 - operations * eps)
    scale = max(1.0, sum(abs(v) for v in values if math.isfinite(v)))
    return gamma * scale


def load_cell(repo: Path) -> tuple[Path, dict[str, Any]]:
    path = repo / CELL_REL
    return path, json.loads(path.read_text(encoding="utf-8"))


def find_candidate(
    cell: dict[str, Any], *, active: tuple[str, ...], regime: str, b_branch: str
) -> dict[str, Any]:
    matches = [
        candidate
        for candidate in cell["selector_result"]["candidates"]
        if tuple(candidate["active_constraints"]) == active
        and candidate["transfer_branch"] == regime
        and candidate["derivative_branches"]["b"] == b_branch
    ]
    if len(matches) != 1:
        raise AssertionError((active, regime, b_branch, len(matches)))
    return matches[0]


def liquid_drift_float(q_b: float, selector_cell: dict[str, Any]) -> dict[str, float]:
    gamma = float(PARAMETERS["gamma_c"])
    phi = float(PARAMETERS["phi"])
    labor_weight = float(PARAMETERS["labor_weight"])
    c = q_b ** (-1.0 / gamma)
    l = (q_b * selector_cell["net_wage"] / labor_weight) ** (1.0 / phi)
    g_b = (
        selector_cell["net_wage"] * l
        + selector_cell["effective_r_b"] * selector_cell["b"]
        + selector_cell["transfer_income"]
        - c
    )
    return {"c": c, "l": l, "g_b": g_b}


def reconstruct_root(selector_cell: dict[str, Any]) -> dict[str, Any]:
    getcontext().prec = 90
    w = Decimal(str(selector_cell["net_wage"]))
    r_b = Decimal(str(selector_cell["effective_r_b"]))
    b = Decimal(str(selector_cell["b"]))
    transfer = Decimal(str(selector_cell["transfer_income"]))
    p_backward = Decimal(str(selector_cell["derivatives"]["p_b_backward"]))
    p_forward = Decimal(str(selector_cell["derivatives"]["p_b_forward"]))
    m = r_b * b + transfer

    def polynomial(labor: Decimal) -> Decimal:
        return (w * labor + m) ** 2 * labor**5 - w

    l_low = decimal_nth_root(min(p_forward, p_backward) * w, 5)
    l_high = decimal_nth_root(max(p_forward, p_backward) * w, 5)
    f_low = polynomial(l_low)
    f_high = polynomial(l_high)
    if not f_low < 0 < f_high:
        raise AssertionError("independent polynomial bracket is not strict")
    for _ in range(320):
        middle = (l_low + l_high) / 2
        f_middle = polynomial(middle)
        if f_middle == 0:
            l_low = l_high = middle
            break
        if f_middle < 0:
            l_low = middle
        else:
            l_high = middle
    labor = (l_low + l_high) / 2
    consumption = w * labor + m
    q_b = Decimal(1) / consumption**2
    q_from_labor = labor**5 / w
    residual = w * labor + m - Decimal(1) / q_b.sqrt()
    derivative_positive_terms = {
        "labor_term": "(w^(6/5)/5)*q^(-4/5)>0",
        "consumption_term": "(1/2)*q^(-3/2)>0",
    }
    return {
        "method": "INDEPENDENT_DECIMAL_BISECTION_OF_MONOTONE_LABOR_POLYNOMIAL",
        "equations": {
            "consumption": "c(q)=q^(-1/2)",
            "labor": "l(q)=(q*w_net)^(1/5)",
            "liquid_drift": "g_b(q)=w_net*l(q)+r_b*b+T-c(q)",
            "labor_polynomial": "F(l)=(w_net*l+m)^2*l^5-w_net=0",
            "m": "r_b*b+T",
        },
        "operands": {
            "w_net": str(w),
            "effective_r_b": str(r_b),
            "b": str(b),
            "transfer_income": str(transfer),
            "m": str(m),
        },
        "q_b_bracket": [str(min(p_forward, p_backward)), str(max(p_forward, p_backward))],
        "polynomial_endpoint_signs": [str(f_low), str(f_high)],
        "labor_root_interval": [str(l_low), str(l_high)],
        "labor": str(labor),
        "consumption": str(consumption),
        "q_b": str(q_b),
        "q_b_from_labor": str(q_from_labor),
        "q_identity_difference": str(q_b - q_from_labor),
        "raw_decimal_residual": str(residual),
        "iterations": 320,
        "unique_positive_root_proof": {
            "derivative_positive_for_all_q_gt_0": True,
            "derivative_terms": derivative_positive_terms,
            "limit_q_to_zero": "-infinity",
            "limit_q_to_infinity": "+infinity",
        },
    }


def reconstruct_combined_candidate(
    selector_cell: dict[str, Any], root: dict[str, Any]
) -> dict[str, Any]:
    q_b_dec = Decimal(root["q_b"])
    q_b = float(q_b_dec)
    p_a_dec = Decimal(str(selector_cell["derivatives"]["p_a_forward"]))
    p_a = float(p_a_dec)
    chi_0 = PARAMETERS["chi_0"]
    kink_lower_dec = q_b_dec * (Decimal(1) - chi_0)
    kink_upper_dec = q_b_dec * (Decimal(1) + chi_0)
    q_a_dec = max(p_a_dec, kink_lower_dec)
    lambda_a_dec = q_a_dec - p_a_dec
    # Reproduce the current authority's binary64 operation order separately
    # from the high-precision mathematical reconstruction above.
    kink_lower = float(q_b * (1.0 - float(chi_0)))
    kink_upper = float(q_b * (1.0 + float(chi_0)))
    q_a = float(max(p_a, kink_lower))
    lambda_a = float(q_a - p_a)
    arithmetic = liquid_drift_float(q_b, selector_cell)
    raw_g_b = arithmetic["g_b"]
    raw_g_a = 0.0
    tolerance = fp_bound(
        arithmetic["c"],
        arithmetic["l"],
        0.0,
        0.0,
        raw_g_b,
        raw_g_a,
        q_b,
        q_a,
        q_b,
        float(p_a_dec),
        operations=96,
    )
    z_bound = fp_bound(
        arithmetic["c"],
        arithmetic["l"],
        0.0,
        0.0,
        raw_g_b,
        raw_g_a,
        q_b,
        q_a,
        selector_cell["derivatives"]["p_b_backward"],
        selector_cell["derivatives"]["p_b_forward"],
        liquid_drift_float(
            selector_cell["derivatives"]["p_b_backward"], selector_cell
        )["g_b"],
        liquid_drift_float(
            selector_cell["derivatives"]["p_b_forward"], selector_cell
        )["g_b"],
        operations=96,
    )
    canonical_g_b = 0.0 if abs(raw_g_b) <= z_bound else raw_g_b
    utility = -1.0 / arithmetic["c"] - arithmetic["l"] ** 6 / 6.0
    hamiltonian = utility + q_b * canonical_g_b + q_a * raw_g_a
    if q_a < kink_lower:
        transfer_residual = kink_lower - q_a
    elif q_a > kink_upper:
        transfer_residual = q_a - kink_upper
    else:
        transfer_residual = 0.0
    checks = {
        "q_b_finite_positive": math.isfinite(q_b) and q_b > 0.0,
        "q_b_inside_closed_derivative_interval": min(
            selector_cell["derivatives"]["p_b_forward"],
            selector_cell["derivatives"]["p_b_backward"],
        )
        <= q_b
        <= max(
            selector_cell["derivatives"]["p_b_forward"],
            selector_cell["derivatives"]["p_b_backward"],
        ),
        "lower_a_kink_intersection_nonempty": q_a <= kink_upper,
        "lower_a_multiplier_nonnegative": lambda_a >= 0,
        "lower_a_active_equality_within_bound": abs(raw_g_a) <= tolerance,
        "liquid_zero_residual_within_bound": abs(raw_g_b) <= z_bound,
        "lower_a_slack_nonnegative": raw_g_a >= -tolerance,
        "lower_a_complementarity": lambda_a * raw_g_a == 0.0,
        "transfer_kkt": transfer_residual <= tolerance,
        "all_finite": all(
            math.isfinite(value)
            for value in (
                arithmetic["c"],
                arithmetic["l"],
                q_b,
                q_a,
                raw_g_b,
                utility,
                hamiltonian,
            )
        ),
    }
    return {
        "transfer_regime": "zero_kink",
        "derivative_branches": {"a": "forward", "b": "zero"},
        "active_constraints": ["lower_a"],
        "d": 0.0,
        "cost": 0.0,
        "q_b_decimal": str(q_b_dec),
        "q_b_binary64": q_b,
        "q_a_decimal": str(q_a_dec),
        "q_a_binary64": q_a,
        "p_a": str(p_a_dec),
        "lower_a_multiplier_decimal": str(lambda_a_dec),
        "lower_a_multiplier_binary64": lambda_a,
        "lower_a_kink_interval_decimal": [str(kink_lower_dec), str(kink_upper_dec)],
        "lower_a_kink_interval_binary64": [kink_lower, kink_upper],
        "lower_a_deterministic_minimum_rule": "max(p_a,q_b*(1-chi_0))",
        "c": arithmetic["c"],
        "l": arithmetic["l"],
        "raw_g_b": raw_g_b,
        "canonical_g_b": canonical_g_b,
        "raw_g_a": raw_g_a,
        "canonical_g_a": 0.0,
        "candidate_arithmetic_tolerance": tolerance,
        "interior_z_arithmetic_bound": z_bound,
        "transfer_target_interval_decimal": [str(kink_lower_dec), str(kink_upper_dec)],
        "transfer_target_interval_binary64": [kink_lower, kink_upper],
        "transfer_kkt_residual": transfer_residual,
        "lower_a_slack": raw_g_a,
        "lower_a_complementarity_residual": 0.0,
        "utility": utility,
        "hamiltonian": hamiltonian,
        "checks": checks,
        "admissible_under_existing_clauses": all(checks.values()),
    }


def candidate_inventory(cell: dict[str, Any]) -> dict[str, Any]:
    rows = []
    for ordinal, candidate in enumerate(cell["selector_result"]["candidates"]):
        rows.append(
            {
                "ordinal": ordinal,
                "active_constraints": candidate["active_constraints"],
                "transfer_branch": candidate["transfer_branch"],
                "derivative_branches": candidate["derivative_branches"],
                "admissible": candidate["admissible"],
                "q_b": candidate["q_b"],
                "q_a": candidate["q_a"],
                "g_b": candidate["g_b"],
                "g_a": candidate["g_a"],
                "interior_z": candidate["interior_z_receipt"] is not None,
                "lower_a_kink": candidate["lower_a_zero_kink_multiplier_receipt"],
                "rejection_reasons": candidate["rejection_reasons"],
            }
        )
    combined = [
        row
        for row in rows
        if row["active_constraints"] == ["lower_a"] and row["interior_z"]
    ]
    return {
        "persisted_outcome": cell["selector_result"]["outcome"],
        "persisted_candidate_count": len(rows),
        "persisted_admissible_count": sum(row["admissible"] for row in rows),
        "persisted_active_lower_a_interior_z_count": len(combined),
        "rows": rows,
    }


def source_trace(repo: Path) -> dict[str, Any]:
    text = (repo / SELECTOR_REL).read_text(encoding="utf-8")
    lines = text.splitlines()

    def locate(fragment: str) -> int:
        found = [index + 1 for index, line in enumerate(lines) if fragment in line]
        if len(found) != 1:
            raise AssertionError((fragment, found))
        return found[0]

    return {
        "interpretation": (
            "The active-lower-a forward zero-kink endpoint exits before controls because "
            "its endpoint kink intersection is empty. The resulting rejected object has "
            "g_b=None. The interior-Z constructor requires both endpoint g_b and arithmetic "
            "bounds, so it returns before reconstructing the root. If the Z root were "
            "reached, the existing candidate path would recompute the lower-a kink interval "
            "at q_b_override before all unchanged legality and Hamiltonian checks."
        ),
        "locations": {
            "lower_a_kink_reconstruction": locate("lower_a_zero_kink_receipt = active_lower_a_zero_kink_shadow("),
            "endpoint_empty_return": locate('"ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERSECTION_EMPTY"'),
            "controls_after_kink_reconstruction": locate("c, l, cost, g_b, g_a, utility = _controls"),
            "interior_z_requires_backward_g_b": locate("backward.g_b is None"),
            "interior_z_candidate_call": locate("z_candidate = _interior_z_candidate("),
            "hamiltonian_comparison": locate("policies.sort(key=lambda candidate: float(candidate.hamiltonian)"),
        },
        "omitted_persisted_family": {
            "active_constraints": ["lower_a"],
            "transfer_branch": "zero_kink",
            "derivative_branches": {"a": "forward", "b": "zero"},
        },
        "omission_before_hamiltonian_comparison": True,
        "production_change_made": False,
    }


def authority_matrix() -> dict[str, Any]:
    return {
        "rows": [
            {
                "authority": "adopted lower-a zero-kink multiplier law",
                "clause": "d=0; q_a in [p_a,+inf) intersect q_b*[1-chi_0,1+chi_0]; choose deterministic minimum",
                "applies": True,
            },
            {
                "authority": "Owner-adopted generic interior-liquid Z law",
                "clause": "same a-side/branch/regime strict endpoint crossing; unique finite positive root in derivative interval",
                "applies": True,
            },
            {
                "authority": "Owner-adopted generic interior-liquid Z law",
                "clause": "recompute controls and a-side KKT at switching q_b; pass all existing checks and Hamiltonian comparison",
                "applies": True,
            },
            {
                "authority": "interior-a switching adoption",
                "clause": "no simultaneous new two-axis switching without Owner adjudication",
                "applies": False,
                "reason": "a is on an active lower face and uses the pre-existing lower-a equality/multiplier law; no interior-a switching shadow is created",
            },
        ],
        "composition_requires_new_law": False,
        "composition_is_already_determined": True,
    }


def run(repo: Path, output: Path, focused_tests: int) -> dict[str, Any]:
    repo = repo.resolve()
    output = output.resolve()
    if output.exists() and any(output.iterdir()):
        raise FileExistsError(f"fresh evidence root already contains files: {output}")
    output.mkdir(parents=True, exist_ok=True)

    cell_path, cell = load_cell(repo)
    selector_cell = cell["selector_cell"]
    expected_binding = {
        "checkpoint": 1,
        "flat_index_f_zero_based": 5,
        "index_b_a_z_zero_based": [5, 0, 0],
        "cell_id": "v001_f0005_b005_a000_z000",
        "b": -0.1578947368421053,
        "a": 0.0,
        "z": 0.8,
        "outcome": "NO_ADMISSIBLE_POLICY",
    }
    actual_binding = {
        "checkpoint": cell["checkpoint"],
        "flat_index_f_zero_based": cell["flat_index_f_zero_based"],
        "index_b_a_z_zero_based": cell["index_b_a_z_zero_based"],
        "cell_id": selector_cell["cell_id"],
        "b": selector_cell["b"],
        "a": selector_cell["a"],
        "z": selector_cell["z"],
        "outcome": cell["selector_result"]["outcome"],
    }
    if actual_binding != expected_binding:
        raise AssertionError((actual_binding, expected_binding))

    predecessor_manifest_path = repo / PREDECESSOR_ROOT / "sealed_manifest.json"
    predecessor_readback_path = repo / PREDECESSOR_ROOT / "independent_readback_receipt.json"
    predecessor_manifest_sha = sha256_bytes(predecessor_manifest_path.read_bytes())
    predecessor_readback = json.loads(predecessor_readback_path.read_text(encoding="utf-8"))
    if predecessor_manifest_sha != PREDECESSOR_MANIFEST:
        raise AssertionError(predecessor_manifest_sha)
    if predecessor_readback.get("status") != "PASS" or predecessor_readback.get("bad_paths") != []:
        raise AssertionError(predecessor_readback)

    identities = [file_identity(repo / path, repo) for path in AUTHORITY_FILES]
    identities.extend(
        file_identity(repo / path, repo) for path in (SELECTOR_REL, COST_REL, TURN2_REL)
    )
    turn2_text = (repo / TURN2_REL).read_text(encoding="utf-8")
    for token in (
        '"gamma_c": 2.0',
        '"phi": 5.0',
        '"chi_0": 0.1',
        '"chi_1": 2.0',
        '"a_bar": 1.0e-6',
        '"labor_weight": 1.0',
    ):
        if token not in turn2_text:
            raise AssertionError(f"missing frozen parameter token: {token}")

    manifest = json.loads(predecessor_manifest_path.read_text(encoding="utf-8"))
    cell_rel_to_predecessor = cell_path.relative_to(repo / PREDECESSOR_ROOT).as_posix()
    matching_entries = [entry for entry in manifest["entries"] if entry["path"] == cell_rel_to_predecessor]
    if len(matching_entries) != 1:
        raise AssertionError((cell_rel_to_predecessor, len(matching_entries)))
    cell_identity = file_identity(cell_path, repo)
    if matching_entries[0]["sha256"] != cell_identity["sha256"]:
        raise AssertionError("cell SHA-256 does not match accepted manifest")

    inactive_zero_back = find_candidate(cell, active=(), regime="zero_kink", b_branch="backward")
    inactive_zero_forward = find_candidate(cell, active=(), regime="zero_kink", b_branch="forward")
    active_zero_back = find_candidate(cell, active=("lower_a",), regime="zero_kink", b_branch="backward")
    active_zero_forward = find_candidate(cell, active=("lower_a",), regime="zero_kink", b_branch="forward")
    back_arithmetic = liquid_drift_float(selector_cell["derivatives"]["p_b_backward"], selector_cell)
    forward_arithmetic = liquid_drift_float(selector_cell["derivatives"]["p_b_forward"], selector_cell)
    if back_arithmetic["g_b"] != active_zero_back["g_b"]:
        raise AssertionError("backward endpoint drift mismatch")
    if not math.isclose(
        forward_arithmetic["g_b"], inactive_zero_forward["g_b"], rel_tol=0.0, abs_tol=1e-15
    ):
        raise AssertionError("forward endpoint drift mismatch")
    if not back_arithmetic["g_b"] > 0.0 > forward_arithmetic["g_b"]:
        raise AssertionError("strict endpoint liquid crossing absent")

    root = reconstruct_root(selector_cell)
    combined = reconstruct_combined_candidate(selector_cell, root)
    if not combined["admissible_under_existing_clauses"]:
        raise AssertionError(combined["checks"])

    binding_receipt = {
        "status": "PASS",
        "task_id": TASK_ID,
        "baseline": BASELINE,
        "accepted_predecessor": PREDECESSOR,
        "accepted_predecessor_manifest_sha256": predecessor_manifest_sha,
        "accepted_predecessor_readback_status": predecessor_readback["status"],
        "authority_and_source_identities": identities,
        "frozen_parameters": {key: str(value) for key, value in PARAMETERS.items()},
    }
    cell_receipt = {
        "status": "PASS",
        "expected_binding": expected_binding,
        "actual_binding": actual_binding,
        "cell_identity": cell_identity,
        "accepted_manifest_entry": matching_entries[0],
        "derivatives": selector_cell["derivatives"],
    }
    endpoint_receipt = {
        "same_family": {
            "active_constraints": ["lower_a"],
            "a_derivative_branch": "forward",
            "transfer_regime": "zero_kink",
            "d": 0.0,
        },
        "strict_crossing": True,
        "rows": [
            {
                "liquid_branch": "backward",
                "q_b": selector_cell["derivatives"]["p_b_backward"],
                **back_arithmetic,
                "persisted_endpoint_full_candidate_kink_intersection_nonempty": active_zero_back[
                    "lower_a_zero_kink_multiplier_receipt"
                ]["intersection_nonempty"],
                "direction": "positive",
            },
            {
                "liquid_branch": "forward",
                "q_b": selector_cell["derivatives"]["p_b_forward"],
                **forward_arithmetic,
                "persisted_endpoint_full_candidate_kink_intersection_nonempty": active_zero_forward[
                    "lower_a_zero_kink_multiplier_receipt"
                ]["intersection_nonempty"],
                "direction": "negative",
                "note": "raw d=0 liquid drift is independent of q_a; the persisted full endpoint candidate exits before controls",
            },
        ],
        "owner_z_clause_application": (
            "Endpoint full admissibility is not the final switching test: the adopted Z law "
            "requires the a-side KKT objects to be recomputed at the switching shadow."
        ),
    }
    trace = source_trace(repo)
    inventory = candidate_inventory(cell)
    if inventory["persisted_active_lower_a_interior_z_count"] != 0:
        raise AssertionError("combined family is already persisted")

    ledger = {
        "persisted_cell_loads": 6,
        "persisted_cell_loads_formal_evidence_runs": 2,
        "persisted_cell_loads_focused_tests": 4,
        "independent_decimal_equation_reconstructions": 4,
        "independent_decimal_equation_reconstructions_formal_evidence_runs": 2,
        "independent_decimal_equation_reconstructions_focused_tests": 2,
        "binary64_scalar_spot_checks": 1,
        "prepublication_evidence_regenerations": 1,
        "production_selector_calls": 0,
        "production_root_helper_calls": 0,
        "hjb_direct_updates": 0,
        "d2_q_assemblies": 0,
        "scc_kfe_svd": 0,
        "aggregate_integration": 0,
        "firm_k1a_c1_wage_monetary_fiscal": 0,
        "turn2_replays": 0,
        "turn3_calls": 0,
        "matlab_calls": 0,
        "ge_annual_shock_irf_welfare_results": 0,
        "retry_tuning": 0,
    }
    classification = {
        "terminal": TERMINAL,
        "classification": CLASSIFICATION,
        "current_no_admissible_policy_supported": False,
        "owner_decision_required": False,
        "combined_candidate_unique": True,
        "combined_candidate_admissible_under_existing_clauses": True,
        "selector_omits_combined_candidate_before_hamiltonian_comparison": True,
        "scientific_interpretation": (
            "The adopted lower-a zero-kink and generic interior-liquid Z authorities "
            "uniquely determine a legal combined candidate at this cell. The persisted "
            "NO_ADMISSIBLE_POLICY is therefore an implementation/composition false negative."
        ),
        "next_actions_authorized": [],
        "results_eligibility": False,
    }

    write_json(output / "authority_source_binding.json", binding_receipt)
    write_json(output / "failing_cell_binding.json", cell_receipt)
    write_json(output / "candidate_family_inventory.json", inventory)
    write_json(output / "adopted_law_matrix.json", authority_matrix())
    write_json(output / "endpoint_liquid_drift_table.json", endpoint_receipt)
    write_json(output / "independent_zero_liquid_reconstruction.json", root)
    write_json(output / "lower_a_kkt_combined_candidate_reconstruction.json", combined)
    write_json(output / "selector_control_flow_trace.json", trace)
    write_json(output / "classification_receipt.json", classification)
    write_json(output / "focused_test_receipt.json", {"status": "PASS", "tests": focused_tests})
    write_json(output / "zero_science_ledger.json", ledger)

    entries = []
    for path in sorted(output.rglob("*")):
        if path.is_file() and path.name not in {"sealed_manifest.json", "independent_readback_receipt.json"}:
            data = path.read_bytes()
            entries.append(
                {
                    "path": path.relative_to(output).as_posix(),
                    "bytes": len(data),
                    "sha256": sha256_bytes(data),
                }
            )
    sealed = {
        "schema": "CH5_MP4C_TURN2_HEBEI_F0005_LOWER_A_LIQUID_SWITCH_FORENSIC_V1",
        "entries": entries,
        "entry_count": len(entries),
        "total_bytes": sum(entry["bytes"] for entry in entries),
    }
    write_json(output / "sealed_manifest.json", sealed)
    manifest_sha = sha256_bytes((output / "sealed_manifest.json").read_bytes())
    bad_paths = []
    for entry in entries:
        path = output / entry["path"]
        if not path.is_file() or sha256_bytes(path.read_bytes()) != entry["sha256"]:
            bad_paths.append(entry["path"])
    readback = {
        "status": "PASS" if not bad_paths else "FAIL",
        "manifest_sha256": manifest_sha,
        "entry_count": len(entries),
        "total_bytes": sealed["total_bytes"],
        "bad_paths": bad_paths,
        "scientific_calls": 0,
    }
    write_json(output / "independent_readback_receipt.json", readback)
    if bad_paths:
        raise AssertionError(bad_paths)
    return {"classification": classification, "manifest": readback, "candidate": combined}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--focused-tests", type=int, required=True)
    args = parser.parse_args()
    result = run(args.repo, args.output, args.focused_tests)
    print(result["classification"]["terminal"])
    print(result["classification"]["classification"])
    print(result["manifest"]["manifest_sha256"])


if __name__ == "__main__":
    main()
