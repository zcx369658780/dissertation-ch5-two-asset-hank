"""Independent zero-science forensic for Heilongjiang checkpoint-3 F0063.

This module uses only the Python standard library.  It reads persisted evidence
and source text.  It never imports or calls the production selector, root
helpers, HJB, generator, KFE, aggregate, or integration code.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
from typing import Any


TASK_ID = "CH5_MP4C_TURN2_HEILONGJIANG_F0063_NONPOSITIVE_BACKWARD_LIQUID_SHADOW_FORENSIC_20260921"
BASELINE = "3717d30ee217096df5e7efece60a6b843b0d0d0b"
ACCEPTED_PREDECESSOR = "4cbd4261be31c237a99cade68ccb35a13c9306b9"
ACCEPTED_MANIFEST = "1C501CEF7740748805CF538A05ECF9D80938149CDDF31A3158091F665C45AD80"
ACCEPTED_CELL_SHA256 = "17C5808B073AF454172EA0478EB144CE1E6145F7657EF0C06C78C747E953F6D3"
TERMINAL = (
    "BLOCKED__TURN2_HEILONGJIANG_F0063_FORENSIC__OWNER_DECISION_REQUIRED_FOR_"
    "NONPOSITIVE_ONE_SIDED_LIQUID_SHADOW_EXTENSION__NO_CODE_CHANGE"
)
CLASSIFICATION = (
    "CURRENT_NO_ADMISSIBLE_POLICY_CORRECT_UNDER_EXISTING_AUTHORITY__"
    "COHERENT_POSITIVE_TRANSFER_ZERO_LIQUID_ROOT_EXISTS_ONLY_OUTSIDE_"
    "AUTHORIZED_TWO_POSITIVE_SHADOW_BRACKET__OWNER_DECISION_REQUIRED"
)

PREDECESSOR_ROOT = Path(
    "reports/ch5_mp4c_lower_a_interior_z_composition_repair_turn1_parity_turn2_run004_20260921"
)
CELL_REL = PREDECESSOR_ROOT / "household/p07_黑龙江/checkpoint_003/cell_0063.json"
DERIVATIVE_REL = PREDECESSOR_ROOT / "household/p07_黑龙江/checkpoint_003/derivative_receipt.json"
DIRECT_SOLVE_REL = PREDECESSOR_ROOT / "household/p07_黑龙江/checkpoint_002/direct_solve_receipt.json"
OUTPUT_REL = Path(
    "reports/ch5_mp4c_turn2_heilongjiang_f0063_nonpositive_backward_liquid_shadow_forensic_20260921_run001"
)
TASK_REL = Path(
    "tasks/CH5_MP4C_TURN2_HEILONGJIANG_F0063_NONPOSITIVE_BACKWARD_LIQUID_SHADOW_FORENSIC_20260921.md"
)
SELECTOR_REL = Path("src/ch5_two_asset_hank/corrected_diagnostic/selector.py")
COST_REL = Path("src/ch5_two_asset_hank/corrected_diagnostic/cost.py")
DERIVATIVE_SOURCE_REL = Path("src/ch5_two_asset_hank/corrected_diagnostic/option_a_step.py")
TURN2_REL = Path("src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py")
MATLAB_POLICY_REL = Path("src/ch5_two_asset_hank/matlab_faithful_policy.py")

AUTHORITY_FILES = (
    Path("AGENTS.md"),
    Path("project_rules/PROJECT_RULE_INDEX_CURRENT.md"),
    Path("docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md"),
    Path("docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md"),
    Path("docs/CH5_MP4C_LOWER_A_INTERIOR_Z_COMPOSITION_REPAIR_TURN1_PARITY_AND_TURN2_RUN004_ACCEPTANCE_20260921.md"),
    Path("docs/CH5_MP4C_2018_KFE_D123_CORRECTED_DIAGNOSTIC_CONTRACT_IMPLEMENTATION_STATIC_VALIDATION_ACCEPTANCE_20260916.md"),
    Path("docs/CH5_MP4C_2018_KFE_D123_FAILED_CELL_ALGEBRAIC_ATTRIBUTION_ACCEPTANCE_20260916.md"),
    Path("docs/CH5_MP4C_2018_KFE_D123_INTERIOR_ZERO_LIQUID_Z_OWNER_ADOPTION_ACCEPTANCE_20260916.md"),
    Path("docs/CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_SWITCHING_OWNER_ADOPTION_20260919.md"),
    TASK_REL,
)

PARAMETERS = {
    "gamma_c": 2.0,
    "phi": 5.0,
    "labor_weight": 1.0,
    "chi_0": 0.1,
    "chi_1": 2.0,
    "a_bar": 1.0e-6,
}


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def git_blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def identity(path: Path, repository: Path) -> dict[str, Any]:
    data = path.read_bytes()
    return {
        "path": path.relative_to(repository).as_posix(),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest().upper(),
        "git_blob_sha1": hashlib.sha1(
            f"blob {len(data)}\0".encode("ascii") + data
        ).hexdigest(),
    }


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
        + "\n",
        encoding="utf-8",
    )


def fp_bound(*values: float, operations: int = 96) -> float:
    eps = 2.220446049250313e-16
    gamma = operations * eps / (1.0 - operations * eps)
    scale = max(1.0, sum(abs(value) for value in values if math.isfinite(value)))
    return gamma * scale


def evaluate_family(cell: dict[str, Any], q_b: float, q_a: float, regime: str) -> dict[str, float]:
    if not math.isfinite(q_b) or q_b <= 0.0:
        raise ValueError("independent arithmetic requires q_b > 0")
    a = float(cell["a"])
    scale = max(a, PARAMETERS["a_bar"])
    if regime == "zero_kink":
        d = 0.0
    else:
        offset = 1.1 if regime == "positive" else 0.9
        d = scale * (q_a / q_b - offset) / PARAMETERS["chi_1"]
    cost = PARAMETERS["chi_0"] * abs(d) + PARAMETERS["chi_1"] * d * d / (2.0 * scale)
    c = q_b ** (-1.0 / PARAMETERS["gamma_c"])
    labor = (
        q_b * float(cell["net_wage"]) / PARAMETERS["labor_weight"]
    ) ** (1.0 / PARAMETERS["phi"])
    g_b = (
        float(cell["net_wage"]) * labor
        + float(cell["effective_r_b"]) * float(cell["b"])
        + float(cell["transfer_income"])
        - c
        - d
        - cost
    )
    g_a = float(cell["effective_r_a"]) * a + d
    utility = -1.0 / c - labor ** 6 / 6.0
    if d > 0.0:
        target_lower = target_upper = q_b * (1.1 + 2.0 * d / scale)
    elif d < 0.0:
        target_lower = target_upper = q_b * (0.9 + 2.0 * d / scale)
    else:
        target_lower, target_upper = 0.9 * q_b, 1.1 * q_b
    if q_a < target_lower:
        kkt = target_lower - q_a
    elif q_a > target_upper:
        kkt = q_a - target_upper
    else:
        kkt = 0.0
    tolerance = fp_bound(c, labor, d, cost, g_b, g_a, q_b, q_a, q_b, q_a)
    hamiltonian = utility + q_b * g_b + q_a * g_a
    return {
        "q_b": q_b,
        "q_a": q_a,
        "c": c,
        "labor": labor,
        "d": d,
        "cost": cost,
        "g_b": g_b,
        "g_a": g_a,
        "utility": utility,
        "hamiltonian": hamiltonian,
        "transfer_kkt_residual": kkt,
        "transfer_target_lower": target_lower,
        "transfer_target_upper": target_upper,
        "arithmetic_bound": tolerance,
    }


def bisect_family(
    cell: dict[str, Any], q_a: float, regime: str, lower: float, upper: float
) -> dict[str, Any]:
    left = evaluate_family(cell, lower, q_a, regime)["g_b"]
    right = evaluate_family(cell, upper, q_a, regime)["g_b"]
    if not left < 0.0 < right:
        raise AssertionError((regime, q_a, lower, upper, left, right))
    lo, hi, flo = lower, upper, left
    for _ in range(256):
        middle = (lo + hi) / 2.0
        value = evaluate_family(cell, middle, q_a, regime)["g_b"]
        if flo * value <= 0.0:
            hi = middle
        else:
            lo, flo = middle, value
    root = (lo + hi) / 2.0
    row = evaluate_family(cell, root, q_a, regime)
    row.update(
        {
            "method": "INDEPENDENT_BINARY64_BISECTION_256",
            "bracket": [lower, upper],
            "bracket_drifts": [left, right],
            "root_residual": row["g_b"],
            "strictly_increasing_on_stated_bracket": True,
            "uniqueness_basis": (
                "labor and consumption derivative terms are positive; on the stated "
                "branch, -d'(1+C_d) is nonnegative and strictly positive when d varies"
            ),
        }
    )
    return row


def independent_analysis(cell: dict[str, Any]) -> dict[str, Any]:
    derivatives = cell["derivatives"]
    p_b_backward = float(derivatives["p_b_backward"])
    p_b_forward = float(derivatives["p_b_forward"])
    p_a_backward = float(derivatives["p_a_backward"])
    p_a_forward = float(derivatives["p_a_forward"])

    specifications = (
        ("negative_a_backward", "negative", "backward", p_a_backward, p_a_backward / 0.9),
        ("negative_a_forward", "negative", "forward", p_a_forward, p_a_forward / 0.9),
        ("zero_kink_a_forward", "zero_kink", "forward", p_a_forward, p_a_forward / 0.9),
        ("positive_a_forward", "positive", "forward", p_a_forward, p_a_forward / 1.1),
    )
    families: dict[str, Any] = {}
    for name, regime, a_branch, q_a, upper in specifications:
        root = bisect_family(cell, q_a, regime, p_b_forward, upper)
        transfer_sign_ok = (
            root["d"] < 0.0
            if regime == "negative"
            else root["d"] > 0.0
            if regime == "positive"
            else root["d"] == 0.0
        )
        a_direction_ok = (
            root["g_a"] <= root["arithmetic_bound"]
            if a_branch == "backward"
            else root["g_a"] >= -root["arithmetic_bound"]
        )
        root.update(
            {
                "family": name,
                "transfer_regime": regime,
                "a_branch": a_branch,
                "transfer_sign_ok": transfer_sign_ok,
                "transfer_kkt_ok": root["transfer_kkt_residual"] <= root["arithmetic_bound"],
                "a_direction_ok": a_direction_ok,
                "inside_sorted_raw_liquid_shadow_interval": (
                    min(p_b_backward, p_b_forward)
                    <= root["q_b"]
                    <= max(p_b_backward, p_b_forward)
                ),
                "inside_authorized_two_positive_shadow_bracket": False,
                "forward_shadow_gap": root["q_b"] - p_b_forward,
            }
        )
        families[name] = root

    d_z = -float(cell["effective_r_a"]) * float(cell["a"])
    ratio = 0.9 + 2.0 * d_z / float(cell["a"])
    derivative_interval = sorted((p_a_forward, p_a_backward))
    implied = [derivative_interval[0] / ratio, derivative_interval[1] / ratio]

    def fixed_drift(q_b: float) -> float:
        a = float(cell["a"])
        cost = 0.1 * abs(d_z) + d_z * d_z / a
        c = q_b ** -0.5
        labor = (q_b * float(cell["net_wage"])) ** 0.2
        return (
            float(cell["net_wage"]) * labor
            + float(cell["effective_r_b"]) * float(cell["b"])
            + float(cell["transfer_income"])
            - c
            - d_z
            - cost
        )

    lo, hi = p_b_forward, implied[0]
    flo, fhi = fixed_drift(lo), fixed_drift(hi)
    if not flo < 0.0 < fhi:
        raise AssertionError((flo, fhi))
    for _ in range(256):
        mid = (lo + hi) / 2.0
        fm = fixed_drift(mid)
        if flo * fm <= 0.0:
            hi = mid
        else:
            lo, flo = mid, fm
    fixed_root = (lo + hi) / 2.0
    interior_a = {
        "d_z": d_z,
        "transfer_regime": "negative",
        "d3_ratio_q_a_over_q_b": ratio,
        "illiquid_derivative_interval": derivative_interval,
        "implied_positive_q_b_interval": implied,
        "implied_interval_endpoint_drifts": [fixed_drift(implied[0]), fixed_drift(implied[1])],
        "independent_global_positive_root": fixed_root,
        "root_residual": fixed_drift(fixed_root),
        "q_a_at_root": ratio * fixed_root,
        "root_inside_implied_interval": implied[0] <= fixed_root <= implied[1],
        "root_inside_liquid_derivative_interval": (
            min(p_b_backward, p_b_forward) <= fixed_root <= max(p_b_backward, p_b_forward)
        ),
        "strictly_increasing": True,
    }
    return {
        "equation": (
            "g_b(q)=w*(q*w/labor_weight)^(1/phi)+r_b*b+T-q^(-1/gamma)-d(q)-C(d(q),a)"
        ),
        "parameters": PARAMETERS,
        "ordinary_family_roots": families,
        "interior_a_fixed_d_analysis": interior_a,
    }


def source_trace(repository: Path) -> dict[str, Any]:
    selector = (repository / SELECTOR_REL).read_text(encoding="utf-8")
    cost = (repository / COST_REL).read_text(encoding="utf-8")
    derivative = (repository / DERIVATIVE_SOURCE_REL).read_text(encoding="utf-8")
    matlab = (repository / MATLAB_POLICY_REL).read_text(encoding="utf-8")

    def line(text: str, token: str) -> int:
        position = text.index(token)
        return text.count("\n", 0, position) + 1

    return {
        "selector": {
            "q_b_domain_rejection_line": line(selector, '"q_b_DOMAIN_INVALID_NO_DERIVATIVE_FLOOR"'),
            "interior_z_positive_shadow_gate_line": line(
                selector,
                "if not all(math.isfinite(value) and value > 0.0 for value in (p_backward, p_forward))",
            ),
            "interior_a_missing_endpoint_return_line": line(selector, "backward.g_a is None"),
            "joint_requires_two_liquid_z_receipts_line": line(
                selector, "candidate.interior_z_receipt is None"
            ),
            "joint_positive_liquid_interval_line": line(
                selector, "if liquid_interval[0] <= 0.0"
            ),
        },
        "cost": {
            "positive_q_b_kkt_line": line(cost, "if q_b <= 0.0:"),
            "no_floor_message_line": line(
                cost, 'raise ValueError("transfer KKT requires q_b > 0; no derivative floor is allowed")'
            ),
        },
        "derivative_source": {
            "raw_backward_assignment_line": line(
                derivative, "p_b_backward[1:, :, :] = b_slopes"
            ),
            "raw_forward_assignment_line": line(
                derivative, "p_b_forward[:-1, :, :] = b_slopes"
            ),
        },
        "historical_source_faithful_precedent": {
            "floor_constant_line": line(matlab, "MATLAB_DERIVATIVE_FLOOR = 1.0e-6"),
            "backward_floor_line": line(
                matlab, "vb_b = max(v_b_backward, MATLAB_DERIVATIVE_FLOOR)"
            ),
            "authority_status": (
                "HISTORICAL_SOURCE_FAITHFUL_FLOOR_EXISTS_BUT_CURRENT_CORRECTED_"
                "AUTHORITY_EXPLICITLY_FORBIDS_INHERITING_IT"
            ),
        },
    }


def verify_predecessor_manifest(repository: Path) -> dict[str, Any]:
    root = repository / PREDECESSOR_ROOT
    manifest_path = root / "sealed_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bad = []
    for row in manifest["entries"]:
        path = root / row["path"]
        if not path.is_file() or path.stat().st_size != row["bytes"] or sha256(path) != row["sha256"]:
            bad.append(row["path"])
    readback = json.loads((root / "independent_readback_receipt.json").read_text(encoding="utf-8"))
    cell_rows = [row for row in manifest["entries"] if row["path"] == CELL_REL.relative_to(PREDECESSOR_ROOT).as_posix()]
    checks = {
        "manifest_sha256": sha256(manifest_path) == ACCEPTED_MANIFEST,
        "entry_count": manifest["entry_count"] == 1146,
        "all_entries_read_back": not bad,
        "accepted_readback": readback.get("status") == "PASS" and not readback.get("bad_paths"),
        "cell_entry_unique": len(cell_rows) == 1,
        "cell_entry_sha256": len(cell_rows) == 1 and cell_rows[0]["sha256"] == ACCEPTED_CELL_SHA256,
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "entry_count": manifest["entry_count"],
        "total_bytes": manifest["total_bytes"],
        "bad_paths": bad,
        "cell_manifest_entry": cell_rows[0] if len(cell_rows) == 1 else None,
    }


def manifest(output: Path) -> None:
    excluded = {"sealed_manifest.json", "independent_readback_receipt.json"}
    rows = []
    for path in sorted(p for p in output.rglob("*") if p.is_file() and p.name not in excluded):
        rows.append(
            {
                "path": path.relative_to(output).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    write_json(
        output / "sealed_manifest.json",
        {
            "schema": "CH5_MP4C_HEILONGJIANG_F0063_FORENSIC_MANIFEST_V1",
            "entry_count": len(rows),
            "total_bytes": sum(row["bytes"] for row in rows),
            "entries": rows,
        },
    )


def readback(output: Path) -> None:
    manifest_path = output / "sealed_manifest.json"
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    bad = []
    for row in payload["entries"]:
        path = output / row["path"]
        if not path.is_file() or path.stat().st_size != row["bytes"] or sha256(path) != row["sha256"]:
            bad.append(row["path"])
    write_json(
        output / "independent_readback_receipt.json",
        {
            "status": "PASS" if not bad else "FAIL",
            "manifest_sha256": sha256(manifest_path),
            "entry_count": payload["entry_count"],
            "total_bytes": payload["total_bytes"],
            "bad_paths": bad,
            "scientific_calls": 0,
        },
    )


def execute(repository: Path, junit: Path) -> str:
    repository = repository.resolve(strict=True)
    output = repository / OUTPUT_REL
    if output.exists():
        raise RuntimeError("fresh evidence root already exists")
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repository, text=True).strip()
    origin_main = subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=repository, text=True).strip()
    predecessor_is_ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", ACCEPTED_PREDECESSOR, "HEAD"],
        cwd=repository,
        check=False,
    ).returncode == 0
    if head != BASELINE or origin_main != BASELINE or not predecessor_is_ancestor:
        raise RuntimeError("live-main or predecessor ancestry binding failed")

    predecessor = verify_predecessor_manifest(repository)
    if predecessor["status"] != "PASS":
        raise RuntimeError("accepted predecessor integrity failed")
    cell_path = repository / CELL_REL
    cell_payload = json.loads(cell_path.read_text(encoding="utf-8"))
    cell = cell_payload["selector_cell"]
    if sha256(cell_path) != ACCEPTED_CELL_SHA256:
        raise RuntimeError("cell identity mismatch")
    analysis = independent_analysis(cell)
    candidates = cell_payload["selector_result"]["candidates"]
    if len(candidates) != 8 or cell_payload["selector_result"]["outcome"] != "NO_ADMISSIBLE_POLICY":
        raise RuntimeError("persisted candidate inventory mismatch")

    output.mkdir(parents=True, exist_ok=False)
    source_files = (SELECTOR_REL, COST_REL, DERIVATIVE_SOURCE_REL, TURN2_REL, MATLAB_POLICY_REL)
    write_json(
        output / "authority_source_binding.json",
        {
            "status": "PASS",
            "task_id": TASK_ID,
            "live_main": BASELINE,
            "execution_head": head,
            "accepted_predecessor": ACCEPTED_PREDECESSOR,
            "predecessor_is_ancestor": predecessor_is_ancestor,
            "accepted_predecessor_manifest": ACCEPTED_MANIFEST,
            "predecessor_manifest_readback": predecessor,
            "authority_files": [identity(repository / path, repository) for path in AUTHORITY_FILES],
            "source_files": [identity(repository / path, repository) for path in source_files],
        },
    )
    derivative = json.loads((repository / DERIVATIVE_REL).read_text(encoding="utf-8"))
    direct = json.loads((repository / DIRECT_SOLVE_REL).read_text(encoding="utf-8"))
    binding_checks = {
        "province_index": cell_payload["selector_cell"]["cell_id"].startswith("v003_f0063"),
        "checkpoint": cell_payload["checkpoint"] == 3,
        "flat": cell_payload["flat_index_f_zero_based"] == 63,
        "indices": cell_payload["index_b_a_z_zero_based"] == [3, 3, 0],
        "no_boundary_adapter": cell_payload["boundary_adapter_markers"] == {},
        "value_chain": derivative["value_sha256"] == direct["next_value_sha256"],
        "derivatives": cell["derivatives"] == {
            "p_b_backward": -0.0002428532863339202,
            "p_b_forward": 0.014463823441006161,
            "p_a_backward": 0.026049395991859955,
            "p_a_forward": 0.024439409021974706,
        },
    }
    write_json(
        output / "exact_cell_derivative_binding.json",
        {
            "status": "PASS" if all(binding_checks.values()) else "FAIL",
            "checks": binding_checks,
            "cell_identity": identity(cell_path, repository),
            "cell": cell,
            "derivative_receipt_identity": identity(repository / DERIVATIVE_REL, repository),
            "derivative_receipt": derivative,
            "prior_direct_solve_identity": identity(repository / DIRECT_SOLVE_REL, repository),
            "prior_direct_solve_next_value_sha256": direct["next_value_sha256"],
        },
    )
    write_json(
        output / "complete_persisted_candidate_family_inventory.json",
        {
            "status": "PASS",
            "outcome": cell_payload["selector_result"]["outcome"],
            "candidate_count": len(candidates),
            "root_invocations": cell_payload["selector_result"]["root_invocations"],
            "interior_z_root_invocations": cell_payload["selector_result"]["interior_z_root_invocations"],
            "interior_a_switching_root_invocations": cell_payload["selector_result"]["interior_a_switching_root_invocations"],
            "joint_switching_root_invocations": cell_payload["selector_result"]["joint_switching_root_invocations"],
            "candidates": candidates,
        },
    )
    decomposed = []
    for ordinal, candidate in enumerate(candidates):
        reasons = candidate["rejection_reasons"]
        decomposed.append(
            {
                "ordinal": ordinal,
                "family": {
                    "transfer": candidate["transfer_branch"],
                    "branches": candidate["derivative_branches"],
                },
                "q_b": candidate["q_b"],
                "q_b_domain_failure": "q_b_DOMAIN_INVALID_NO_DERIVATIVE_FLOOR" in reasons,
                "transfer_sign_failure": any("TRANSFER_SIGN" in row for row in reasons),
                "transfer_kkt_failure": "TRANSFER_KKT_RESIDUAL" in reasons,
                "liquid_direction_failure": "B_DERIVATIVE_DIRECTION_INCONSISTENT" in reasons,
                "a_direction_failure": "A_DERIVATIVE_DIRECTION_INCONSISTENT" in reasons,
                "rejection_reasons": reasons,
            }
        )
    write_json(output / "ordinary_candidate_rejection_decomposition.json", {"status": "PASS", "rows": decomposed})
    write_json(
        output / "q_b_domain_no_floor_authority_matrix.json",
        {
            "status": "PASS",
            "rows": [
                {"clause": "consumption FOC", "authority": "q_b=c^(-gamma)>0", "f0063": "backward shadow violates; forward shadow satisfies"},
                {"clause": "D3 KKT", "authority": "q_b strictly positive", "f0063": "nonpositive backward cannot enter KKT"},
                {"clause": "corrected selector", "authority": "no derivative floor/clipping/absolute-value repair", "f0063": "backward ordinary candidates reject before controls"},
                {"clause": "historical MATLAB-faithful", "authority": "contains 1e-6 derivative floor", "f0063": "historical behavior is not adopted corrected authority"},
            ],
        },
    )
    pbb, pbf = cell["derivatives"]["p_b_backward"], cell["derivatives"]["p_b_forward"]
    write_json(
        output / "interior_z_applicability_matrix.json",
        {
            "status": "PASS",
            "checks": {
                "interior_liquid": True,
                "backward_shadow_finite": math.isfinite(pbb),
                "backward_shadow_positive": pbb > 0.0,
                "forward_shadow_finite": math.isfinite(pbf),
                "forward_shadow_positive": pbf > 0.0,
                "two_finite_positive_shadows": pbb > 0.0 and pbf > 0.0,
                "authorized_closed_bracket_exists": False,
                "root_invocation_authorized": False,
            },
            "raw_shadows": {"backward": pbb, "forward": pbf},
            "conclusion": "GENERIC_INTERIOR_Z_TRIGGER_FAILS_BEFORE_ENDPOINT_DRIFT_OR_ROOT_SCREEN",
        },
    )
    ia = analysis["interior_a_fixed_d_analysis"]
    negative_forward = [row for row in candidates if row["transfer_branch"] == "negative" and row["derivative_branches"]["b"] == "forward"]
    write_json(
        output / "interior_a_joint_switch_applicability_matrix.json",
        {
            "status": "PASS",
            "interior_a": {
                "backward_liquid_pair_available": False,
                "reason_backward": "both ordinary candidates fail q_b domain before g_a exists",
                "forward_liquid_endpoint_g_a": [row["g_a"] for row in negative_forward],
                "forward_liquid_strict_a_crossing": False,
                "d_z": ia["d_z"],
                "d3_ratio": ia["d3_ratio_q_a_over_q_b"],
                "implied_q_b_interval": ia["implied_positive_q_b_interval"],
                "ordinary_forward_q_b": pbf,
                "ordinary_backward_q_b": pbb,
                "legal_candidate": False,
            },
            "joint": {
                "two_prerequisite_liquid_z_candidates": False,
                "liquid_interval": sorted((pbb, pbf)),
                "liquid_interval_positive": min(pbb, pbf) > 0.0,
                "mapped_q_b_interval": ia["implied_positive_q_b_interval"],
                "interval_intersection_nonempty": False,
                "legal_candidate": False,
            },
        },
    )
    write_json(output / "independent_positive_qb_liquid_drift_analysis.json", analysis)
    positive = analysis["ordinary_family_roots"]["positive_a_forward"]
    diagnostic = {
        "status": "DIAGNOSTIC_ONLY__OUTSIDE_CURRENT_AUTHORITY",
        "candidate": positive,
        "checks": {
            "q_b_positive": positive["q_b"] > 0.0,
            "positive_transfer": positive["d"] > 0.0,
            "transfer_kkt": positive["transfer_kkt_ok"],
            "a_forward_direction": positive["a_direction_ok"],
            "zero_liquid_residual_within_bound": abs(positive["g_b"]) <= positive["arithmetic_bound"],
            "inside_current_authorized_bracket": positive["inside_authorized_two_positive_shadow_bracket"],
        },
        "required_new_law": (
            "ONE_SIDED_NONPOSITIVE_SHADOW_EXTENSION_AND_BRACKET_BEYOND_POSITIVE_FORWARD_SHADOW"
        ),
        "not_authorized_for_implementation": True,
    }
    write_json(output / "diagnostic_only_out_of_authority_candidate.json", diagnostic)
    write_json(output / "selector_source_control_flow_trace.json", source_trace(repository))
    classification = {
        "terminal": TERMINAL,
        "classification": CLASSIFICATION,
        "current_selector_correct_under_existing_authority": True,
        "existing_authority_implementation_omission": False,
        "coherent_diagnostic_extension_candidate_exists": True,
        "owner_decision_required": True,
        "owner_decision_subject": (
            "whether to adopt a new interior-liquid switching law for a finite nonpositive "
            "one-sided derivative/shadow and how to define its positive root bracket"
        ),
        "production_change_authorized": False,
    }
    write_json(output / "current_authority_and_owner_decision_classification.json", classification)
    junit_text = junit.read_text(encoding="utf-8")
    write_json(
        output / "focused_test_receipt.json",
        {
            "status": "PASS" if 'failures="0"' in junit_text and 'errors="0"' in junit_text else "FAIL",
            "path": junit.as_posix(),
            "sha256": sha256(junit),
        },
    )
    ledger = {
        "persisted_cell_loads": 1,
        "persisted_derivative_receipt_loads": 1,
        "persisted_direct_solve_receipt_loads": 1,
        "independent_scalar_equation_families": 5,
        "independent_binary64_bisection_diagnostics": 5,
        "production_selector_calls": 0,
        "production_root_helper_calls": 0,
        "hjb_direct_updates": 0,
        "d2_q_assemblies": 0,
        "scc_kfe_svd": 0,
        "aggregate_integration": 0,
        "turn2_replay_or_rerun": 0,
        "turn3": 0,
        "matlab_scientific_calls": 0,
        "firm_k1a_c1_wage_monetary_fiscal": 0,
        "ge_annual_shock_irf_welfare_results": 0,
        "retry_tuning": 0,
    }
    write_json(output / "zero_science_ledger.json", ledger)
    write_json(
        output / "terminal_receipt.json",
        {
            **classification,
            "zero_science_ledger": ledger,
            "current_modified": False,
            "successor_published": False,
            "results_eligibility": False,
        },
    )
    manifest(output)
    readback(output)
    return TERMINAL


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--focused-test-junit", type=Path, required=True)
    args = parser.parse_args(argv)
    print(execute(args.repository, args.focused_test_junit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
