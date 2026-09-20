"""Zero-root F0364 negative-ratio interior-a switching forensic."""
from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import json
import math
from pathlib import Path
import subprocess
import time
from typing import Any

from ch5_two_asset_hank.corrected_diagnostic.cost import check_transfer_kkt
from ch5_two_asset_hank.corrected_diagnostic.selector import (
    CellDerivatives,
    CorrectedSelectorCell,
    CorrectedSelectorParameters,
    _controls,
    _direction_ok,
    _fp_bound,
    _transfer_ratio,
)


TASK_ID = "CH5_MP4C_TURN2_BEIJING_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_FORENSIC_20260920"
BASELINE_SHA = "fddaef785bca01373492576047d574f07761d084"
TERMINAL = "PASS__TURN2_BEIJING_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_FORENSIC_COMPLETE__NO_SELECTOR_CHANGE"
CLASS_A = "TURN2_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_GUARD_FALSE_NEGATIVE_CONFIRMED"
CLASS_B = "TURN2_F0364_TRUE_NO_ADMISSIBLE_POLICY_AFTER_SIGN_AWARE_SWITCHING_DIAGNOSTIC"
CLASS_C = "TURN2_F0364_NEGATIVE_RATIO_SWITCHING_NUMERICALLY_ADMISSIBLE__OWNER_DOMAIN_DECISION_REQUIRED"
CLASS_D = "TURN2_F0364_FORENSIC_INCONSISTENT__NO_SELECTOR_DECISION"

PARENT_ROOT = Path(
    "reports/ch5_mp4c_corrected_optionb_turn2_upper_b_negative_repair_20260920_run002"
)
CELL_RELATIVE = PARENT_ROOT / "household/p00_北京/checkpoint_005/cell_0364.json"
OUTPUT_RELATIVE = Path(
    "reports/ch5_mp4c_turn2_beijing_f0364_negative_ratio_switching_forensic_20260920_run001"
)
TASK_RELATIVE = Path(
    "tasks/CH5_MP4C_TURN2_BEIJING_F0364_NEGATIVE_RATIO_INTERIOR_A_SWITCHING_FORENSIC_20260920.md"
)
SELECTOR_RELATIVE = Path("src/ch5_two_asset_hank/corrected_diagnostic/selector.py")
COST_RELATIVE = Path("src/ch5_two_asset_hank/corrected_diagnostic/cost.py")
OWNER_ADOPTION_RELATIVE = Path(
    "docs/CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_SWITCHING_OWNER_ADOPTION_20260919.md"
)
ADJUDICATION_RELATIVE = Path(
    "docs/CH5_MP4C_2018_KFE_D123_V2_CELL100_INTERIOR_A_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_ACCEPTANCE_20260919.md"
)
VALIDATOR_RELATIVE = Path(
    "validators/multi_province/turn2_f0364_negative_ratio_switching_forensic/run.py"
)
TEST_RELATIVE = Path("tests/test_mp4c_turn2_f0364_negative_ratio_switching_forensic.py")

PARENT_MANIFEST_SHA256 = "A2A882B8D79A6897D0518447FA84F7775609E31D34452A5EB2F7B7773E9FD0B0"
CELL_BLOB = "5e6528e07998cb6fe3b571cb21c778f3acf3775a"
CELL_SHA256 = "F63B2D685F02D74ED3ED560F5DBD02FE5D7FF2B80ABF6D4F64414FFE1FCC7632"
SELECTOR_BLOB = "2c674b96fa7b665dab84f0ff3d98fbc5b8b16e22"
COST_BLOB = "435705a50238aaeebe918430156bcc14df1ff794"

PARAMETERS = CorrectedSelectorParameters(
    gamma_c=2.0,
    phi=5.0,
    labor_weight=1.0,
    chi_0=0.1,
    chi_1=2.0,
    a_bar=1.0e-6,
)

EXPECTED_CELL = {
    "b": -0.5263157894736843,
    "a": 9.473684210526315,
    "z": 0.8,
    "effective_r_a": 0.8273888725630669,
    "effective_r_b": 0.09000000000000001,
    "net_wage": 13.186487914419764,
    "transfer_income": 0.1,
}
EXPECTED_DERIVATIVES = {
    "p_b_backward": 0.006091715618507631,
    "p_b_forward": 0.008179870108012337,
    "p_a_backward": -0.0031029058502000167,
    "p_a_forward": -0.004925792041697845,
}
EXPECTED_REJECTIONS = (
    ("A_DERIVATIVE_DIRECTION_INCONSISTENT",),
    ("B_DERIVATIVE_DIRECTION_INCONSISTENT", "A_DERIVATIVE_DIRECTION_INCONSISTENT"),
    ("A_DERIVATIVE_DIRECTION_INCONSISTENT",),
    ("B_DERIVATIVE_DIRECTION_INCONSISTENT",),
    ("TRANSFER_KKT_RESIDUAL",),
    ("B_DERIVATIVE_DIRECTION_INCONSISTENT", "TRANSFER_KKT_RESIDUAL"),
    ("TRANSFER_SIGN_INCONSISTENT_POSITIVE", "A_DERIVATIVE_DIRECTION_INCONSISTENT", "TRANSFER_KKT_RESIDUAL"),
    ("TRANSFER_SIGN_INCONSISTENT_POSITIVE", "B_DERIVATIVE_DIRECTION_INCONSISTENT", "A_DERIVATIVE_DIRECTION_INCONSISTENT", "TRANSFER_KKT_RESIDUAL"),
)


class ForensicFailure(RuntimeError):
    pass


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def _git(repository: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repository, text=True).strip()


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def verify_parent_manifest(repository: Path) -> dict[str, Any]:
    root = repository / PARENT_ROOT
    manifest_path = root / "sealed_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bad_paths = []
    for row in manifest["entries"]:
        path = root / row["path"]
        if (
            not path.is_file()
            or path.stat().st_size != int(row["bytes"])
            or _sha256(path) != row["sha256"]
        ):
            bad_paths.append(row["path"])
    readback = json.loads((root / "independent_readback_receipt.json").read_text(encoding="utf-8"))
    checks = {
        "manifest_sha256": _sha256(manifest_path) == PARENT_MANIFEST_SHA256,
        "entry_count_430": int(manifest["entry_count"]) == 430,
        "total_bytes_6449626": int(manifest["total_bytes"]) == 6_449_626,
        "all_entries_read_back": not bad_paths,
        "accepted_readback": readback.get("status") == "PASS" and not readback.get("bad_paths"),
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "manifest_sha256": _sha256(manifest_path),
        "entry_count": int(manifest["entry_count"]),
        "total_bytes": int(manifest["total_bytes"]),
        "bad_paths": bad_paths,
    }


def load_cell(repository: Path) -> tuple[dict[str, Any], CorrectedSelectorCell, dict[str, Any]]:
    path = repository / CELL_RELATIVE
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw = payload["selector_cell"]
    checks = {
        "git_blob": _git(repository, "rev-parse", f"HEAD:{CELL_RELATIVE.as_posix()}") == CELL_BLOB,
        "sha256": _sha256(path) == CELL_SHA256,
        "checkpoint": payload.get("checkpoint") == 5,
        "flat": payload.get("flat_index_f_zero_based") == 364,
        "index": payload.get("index_b_a_z_zero_based") == [4, 18, 0],
        "cell_id": raw.get("cell_id") == "v005_f0364_b004_a018_z000",
        "outcome": payload["selector_result"].get("outcome") == "NO_ADMISSIBLE_POLICY",
        "cell_values": all(float(raw[name]) == value for name, value in EXPECTED_CELL.items()),
        "derivatives": all(float(raw["derivatives"][name]) == value for name, value in EXPECTED_DERIVATIVES.items()),
    }
    if not all(checks.values()):
        raise ForensicFailure(f"F0364 provenance mismatch: {checks}")
    cell = CorrectedSelectorCell(
        cell_id=raw["cell_id"],
        b=raw["b"],
        a=raw["a"],
        z=raw["z"],
        b_lower=raw["b_lower"],
        b_upper=raw["b_upper"],
        a_lower=raw["a_lower"],
        a_upper=raw["a_upper"],
        net_wage=raw["net_wage"],
        effective_r_b=raw["effective_r_b"],
        transfer_income=raw["transfer_income"],
        effective_r_a=raw["effective_r_a"],
        derivatives=CellDerivatives(**raw["derivatives"]),
    )
    return payload, cell, checks


def reproduce_candidates(payload: dict[str, Any]) -> dict[str, Any]:
    candidates = payload["selector_result"]["candidates"]
    rows = []
    for ordinal, candidate in enumerate(candidates):
        rows.append(
            {
                "ordinal": ordinal,
                "active_constraints": candidate["active_constraints"],
                "transfer_branch": candidate["transfer_branch"],
                "derivative_branches": candidate["derivative_branches"],
                "q_b": candidate["q_b"],
                "q_a": candidate["q_a"],
                "d": candidate["d"],
                "g_b": candidate["g_b"],
                "g_a": candidate["g_a"],
                "arithmetic_tolerance": candidate["arithmetic_tolerance"],
                "transfer_kkt_residual": candidate["transfer_kkt_residual"],
                "hamiltonian": candidate["hamiltonian"],
                "admissible": candidate["admissible"],
                "rejection_reasons": candidate["rejection_reasons"],
                "root_invoked": candidate["root_invoked"],
                "root_status": candidate["root_status"],
            }
        )
    checks = {
        "eight_candidates": len(rows) == 8,
        "all_ordinary_no_roots": all(not row["root_invoked"] and row["root_status"] == "NOT_REQUIRED" for row in rows),
        "all_inadmissible": all(not row["admissible"] for row in rows),
        "rejection_classes_exact": tuple(tuple(row["rejection_reasons"]) for row in rows) == EXPECTED_REJECTIONS,
        "selector_outcome": payload["selector_result"]["outcome"] == "NO_ADMISSIBLE_POLICY",
        "selector_root_invocations_zero": payload["selector_result"]["root_invocations"] == 0,
        "interior_a_roots_zero": payload["selector_result"]["interior_a_switching_root_invocations"] == 0,
    }
    return {"status": "PASS" if all(checks.values()) else "FAIL", "checks": checks, "candidates": rows}


def strict_crossing_receipt(reproduction: dict[str, Any]) -> dict[str, Any]:
    rows = reproduction["candidates"]
    backward_pair = (rows[0], rows[2])
    forward_pair = (rows[1], rows[3])

    def crossing(pair: tuple[dict[str, Any], dict[str, Any]]) -> bool:
        backward, forward = pair
        return bool(
            backward["g_a"] > backward["arithmetic_tolerance"]
            and forward["g_a"] < -forward["arithmetic_tolerance"]
        )

    checks = {
        "p_b_backward_a_backward_g_a": backward_pair[0]["g_a"] == 1.1624821053092704,
        "p_b_backward_a_forward_g_a": backward_pair[1]["g_a"] == -0.25497146700720563,
        "p_b_backward_strict_crossing": crossing(backward_pair),
        "p_b_forward_a_backward_g_a": forward_pair[0]["g_a"] == 1.7784160012824266,
        "p_b_forward_a_forward_g_a": forward_pair[1]["g_a"] == 0.7228095000823842,
        "p_b_forward_not_strict_crossing": not crossing(forward_pair),
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "p_b_backward_pair": list(backward_pair),
        "p_b_forward_pair": list(forward_pair),
        "crossing_rule": "backward_g_a > backward_bound AND forward_g_a < -forward_bound",
    }


def ratio_receipt(cell: CorrectedSelectorCell) -> dict[str, Any]:
    d_z = float(-cell.effective_r_a * cell.a)
    ratio = _transfer_ratio(d_z, cell.a, PARAMETERS)
    derivative_interval = tuple(sorted((cell.derivatives.p_a_forward, cell.derivatives.p_a_backward)))
    mapped = tuple(sorted((derivative_interval[0] / ratio, derivative_interval[1] / ratio)))
    checks = {
        "d_z_exact": d_z == -7.8384208979658965,
        "ratio_exact": ratio == -0.7547777451261338,
        "ratio_negative": ratio < 0.0,
        "mapped_interval_positive": mapped[0] > 0.0 and mapped[1] > 0.0,
        "p_b_backward_inside": mapped[0] <= cell.derivatives.p_b_backward <= mapped[1],
        "p_b_forward_outside": not (mapped[0] <= cell.derivatives.p_b_forward <= mapped[1]),
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "d_z": d_z,
        "transfer_regime": "negative",
        "d3_ratio_R": ratio,
        "formula": "1-chi_0+chi_1*d_z/max(a,a_bar)",
        "derivative_interval_sorted": list(derivative_interval),
        "unsorted_q_b_endpoint_images": [derivative_interval[0] / ratio, derivative_interval[1] / ratio],
        "sign_aware_mapped_positive_q_b_interval": list(mapped),
        "current_implementation_guard": "if not finite(ratio) or ratio <= 0.0: return None",
    }


def switching_diagnostic(
    cell: CorrectedSelectorCell,
    ratio: dict[str, Any],
    branch: str,
) -> dict[str, Any]:
    q_b = float(getattr(cell.derivatives, f"p_b_{branch}"))
    d = float(ratio["d_z"])
    r = float(ratio["d3_ratio_R"])
    interval = tuple(float(value) for value in ratio["derivative_interval_sorted"])
    mapped = tuple(float(value) for value in ratio["sign_aware_mapped_positive_q_b_interval"])
    q_a = float(r * q_b)
    c, labor, cost, raw_g_b, raw_g_a, utility = _controls(q_b, d, cell, PARAMETERS)
    tolerance = _fp_bound(
        c,
        labor,
        d,
        cost,
        raw_g_b,
        raw_g_a,
        q_b,
        q_a,
        q_b,
        interval[0],
        operations=96,
    )
    switching_bound = _fp_bound(
        c, labor, d, cost, raw_g_b, raw_g_a, q_b, q_a, operations=96
    )
    g_a = 0.0 if abs(raw_g_a) <= switching_bound else raw_g_a
    g_b = raw_g_b
    q_a_in_interval = interval[0] <= q_a <= interval[1]
    q_b_in_mapped_interval = mapped[0] <= q_b <= mapped[1]
    b_direction = _direction_ok(branch, g_b, tolerance)
    a_direction = _direction_ok("zero", g_a, tolerance)
    transfer_sign = d < -tolerance
    kkt = check_transfer_kkt(
        d=d,
        a=cell.a,
        q_a=q_a,
        q_b=q_b,
        chi_0=PARAMETERS.chi_0,
        chi_1=PARAMETERS.chi_1,
        a_bar=PARAMETERS.a_bar,
        tolerance=tolerance,
    )
    raw_hamiltonian = float(utility + q_b * raw_g_b + q_a * raw_g_a)
    hamiltonian = float(utility + q_b * g_b + q_a * g_a)
    finite = all(
        math.isfinite(value)
        for value in (
            q_b, q_a, d, c, labor, cost, raw_g_b, raw_g_a, g_b, g_a,
            tolerance, switching_bound, utility, raw_hamiltonian, hamiltonian,
        )
    )
    reasons = []
    if not q_b_in_mapped_interval or not q_a_in_interval:
        reasons.append("INTERIOR_A_SWITCHING_SHADOW_OUTSIDE_DERIVATIVE_INTERVAL")
    if abs(raw_g_a) > switching_bound:
        reasons.append("INTERIOR_A_SWITCHING_ZERO_DRIFT_RESIDUAL_BOUND_EXCEEDED")
    if not b_direction:
        reasons.append("B_DERIVATIVE_DIRECTION_INCONSISTENT")
    if not a_direction:
        reasons.append("A_DERIVATIVE_DIRECTION_INCONSISTENT")
    if not transfer_sign:
        reasons.append("TRANSFER_SIGN_INCONSISTENT_NEGATIVE")
    if not kkt.satisfied:
        reasons.append("TRANSFER_KKT_RESIDUAL")
    if not finite:
        reasons.append("NONFINITE_CANDIDATE")
    return {
        "branch": branch,
        "q_b": q_b,
        "q_b_in_sign_aware_mapped_interval": q_b_in_mapped_interval,
        "q_a": q_a,
        "q_a_in_original_derivative_interval": q_a_in_interval,
        "d": d,
        "c": c,
        "l": labor,
        "cost": cost,
        "raw_g_b": raw_g_b,
        "g_b": g_b,
        "raw_g_a": raw_g_a,
        "g_a": g_a,
        "arithmetic_tolerance": tolerance,
        "switching_arithmetic_bound": switching_bound,
        "zero_a_drift_within_arithmetic_bound": abs(raw_g_a) <= switching_bound,
        "b_derivative_direction_consistent": b_direction,
        "a_zero_direction_consistent": a_direction,
        "transfer_sign_consistent": transfer_sign,
        "transfer_kkt": asdict(kkt),
        "finite": finite,
        "utility": utility,
        "raw_hamiltonian": raw_hamiltonian,
        "hamiltonian": hamiltonian,
        "d2_assembler_admissible": finite,
        "rejection_reasons": reasons,
        "admissible": not reasons,
        "root_invocations": 0,
    }


def authority_audit(repository: Path) -> dict[str, Any]:
    owner_text = (repository / OWNER_ADOPTION_RELATIVE).read_text(encoding="utf-8")
    cost_text = (repository / COST_RELATIVE).read_text(encoding="utf-8")
    selector_text = (repository / SELECTOR_RELATIVE).read_text(encoding="utf-8")
    positive_contract = {
        "owner_requires_q_b_positive": "Require `q_b>0`." in owner_text,
        "owner_requires_q_a_in_closed_sorted_interval": (
            "`q_a in [min(p_a^F,p_a^B), max(p_a^F,p_a^B)]`." in owner_text
        ),
        "owner_requires_unchanged_d3_kkt": (
            "`0 in q_a-q_b(1+partial_d C(d_Z,a))`." in owner_text
        ),
        "cost_requires_q_b_positive": "transfer KKT requires q_b > 0" in cost_text,
        "selector_has_ratio_nonpositive_guard": "not math.isfinite(ratio) or ratio <= 0.0" in selector_text,
    }
    explicit_positive_q_a = False
    explicit_positive_ratio = False
    explicit_positive_interior_ratio = False
    return {
        "status": "PASS" if all(positive_contract.values()) else "FAIL",
        "designated_authority": [
            OWNER_ADOPTION_RELATIVE.as_posix(),
            ADJUDICATION_RELATIVE.as_posix(),
            SELECTOR_RELATIVE.as_posix(),
            COST_RELATIVE.as_posix(),
        ],
        "authority_sha256": {
            path.as_posix(): _sha256(repository / path)
            for path in (OWNER_ADOPTION_RELATIVE, ADJUDICATION_RELATIVE, SELECTOR_RELATIVE, COST_RELATIVE)
        },
        "positive_contract_checks": positive_contract,
        "explicit_accepted_authority_requires_q_a_positive": explicit_positive_q_a,
        "explicit_accepted_authority_requires_d3_ratio_positive": explicit_positive_ratio,
        "explicit_accepted_authority_requires_interior_a_switching_ratio_positive": explicit_positive_interior_ratio,
        "ratio_positive_is_current_implementation_guard": True,
        "interpretation": (
            "The Owner-adopted contract positively defines q_b>0, unchanged D3 KKT, "
            "and q_a membership in the closed sorted derivative interval. It states no "
            "additional q_a or ratio positivity domain law; the ratio<=0 condition is "
            "present only in the current implementation guard."
        ),
        "absence_not_used_as_standalone_permission": True,
    }


def classify(
    provenance_ok: bool,
    crossing: dict[str, Any],
    backward: dict[str, Any],
    forward: dict[str, Any],
    authority: dict[str, Any],
) -> str:
    if not provenance_ok or crossing["status"] != "PASS" or authority["status"] != "PASS":
        return CLASS_D
    admissible = [row for row in (backward, forward) if row["admissible"]]
    if not admissible:
        return CLASS_B
    unresolved = any(
        authority[name]
        for name in (
            "explicit_accepted_authority_requires_q_a_positive",
            "explicit_accepted_authority_requires_d3_ratio_positive",
            "explicit_accepted_authority_requires_interior_a_switching_ratio_positive",
        )
    )
    if unresolved:
        return CLASS_C
    if (
        len(admissible) == 1
        and admissible[0]["branch"] == "backward"
        and admissible[0]["q_a_in_original_derivative_interval"]
        and crossing["checks"]["p_b_backward_strict_crossing"]
    ):
        return CLASS_A
    return CLASS_D


def _source_hashes(repository: Path) -> dict[str, str]:
    return {
        path.as_posix(): _sha256(repository / path)
        for path in (
            SELECTOR_RELATIVE,
            COST_RELATIVE,
            OWNER_ADOPTION_RELATIVE,
            ADJUDICATION_RELATIVE,
            TASK_RELATIVE,
            VALIDATOR_RELATIVE,
            TEST_RELATIVE,
        )
    }


def _manifest(output: Path) -> dict[str, Any]:
    excluded = {"sealed_manifest.json", "independent_readback_receipt.json"}
    entries = [
        {
            "path": path.relative_to(output).as_posix(),
            "sha256": _sha256(path),
            "bytes": path.stat().st_size,
        }
        for path in sorted(output.rglob("*"))
        if path.is_file() and path.name not in excluded
    ]
    manifest = {
        "schema": "CH5_MP4C_TURN2_F0364_NEGATIVE_RATIO_SWITCHING_FORENSIC_V1",
        "entry_count": len(entries),
        "total_bytes": sum(int(row["bytes"]) for row in entries),
        "entries": entries,
    }
    _write_json(output / "sealed_manifest.json", manifest)
    return manifest


def _readback(output: Path) -> dict[str, Any]:
    manifest_path = output / "sealed_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    bad = []
    for row in manifest["entries"]:
        path = output / row["path"]
        if (
            not path.is_file()
            or path.stat().st_size != int(row["bytes"])
            or _sha256(path) != row["sha256"]
        ):
            bad.append(row["path"])
    receipt = {
        "status": "PASS" if not bad else "FAIL",
        "manifest_sha256": _sha256(manifest_path),
        "entry_count": int(manifest["entry_count"]),
        "total_bytes": int(manifest["total_bytes"]),
        "bad_paths": bad,
        "scientific_calls": 0,
    }
    _write_json(output / "independent_readback_receipt.json", receipt)
    return receipt


def execute(repository: Path) -> tuple[str, str]:
    repository = repository.resolve(strict=True)
    started = time.perf_counter()
    output = repository / OUTPUT_RELATIVE
    if output.exists():
        raise ForensicFailure(f"fresh evidence root already exists: {output}")
    parent = verify_parent_manifest(repository)
    payload, cell, cell_checks = load_cell(repository)
    reproduction = reproduce_candidates(payload)
    crossing = strict_crossing_receipt(reproduction)
    ratio = ratio_receipt(cell)
    backward = switching_diagnostic(cell, ratio, "backward")
    forward = switching_diagnostic(cell, ratio, "forward")
    authority = authority_audit(repository)
    changed_paths = sorted(
        filter(
            None,
            _git(repository, "diff", "--name-only", f"{BASELINE_SHA}...HEAD").splitlines(),
        )
    )
    startup_checks = {
        "origin_main_exact_baseline": _git(repository, "rev-parse", "origin/main") == BASELINE_SHA,
        "baseline_is_ancestor": subprocess.run(
            ["git", "merge-base", "--is-ancestor", BASELINE_SHA, "HEAD"],
            cwd=repository,
            check=False,
        ).returncode == 0,
        "clean_code_freeze_worktree": not _git(repository, "status", "--porcelain"),
        "changed_paths_exact": changed_paths
        == sorted((VALIDATOR_RELATIVE.as_posix(), TEST_RELATIVE.as_posix())),
    }
    provenance_ok = bool(
        parent["status"] == "PASS"
        and all(cell_checks.values())
        and reproduction["status"] == "PASS"
        and ratio["status"] == "PASS"
        and all(startup_checks.values())
        and _git(repository, "rev-parse", f"HEAD:{SELECTOR_RELATIVE.as_posix()}") == SELECTOR_BLOB
        and _git(repository, "rev-parse", f"HEAD:{COST_RELATIVE.as_posix()}") == COST_BLOB
    )
    classification = classify(provenance_ok, crossing, backward, forward, authority)
    pre_hashes = _source_hashes(repository)
    output.mkdir(parents=True, exist_ok=False)
    _write_json(output / "authority_binding.json", {
        "status": "PASS" if provenance_ok else "FAIL",
        "task_id": TASK_ID,
        "actual_live_main_baseline": BASELINE_SHA,
        "execution_head": _git(repository, "rev-parse", "HEAD"),
        "parent_evidence": parent,
        "cell_path": CELL_RELATIVE.as_posix(),
        "cell_blob": _git(repository, "rev-parse", f"HEAD:{CELL_RELATIVE.as_posix()}"),
        "cell_sha256": _sha256(repository / CELL_RELATIVE),
        "cell_checks": cell_checks,
        "startup_checks": startup_checks,
        "changed_paths": changed_paths,
        "effective_r_b_representation": {
            "task_display_decimal": 0.09,
            "hash_bound_json_float": float(payload["selector_cell"]["effective_r_b"]),
            "same_model_input_at_display_precision": True,
        },
        "selector_blob": _git(repository, "rev-parse", f"HEAD:{SELECTOR_RELATIVE.as_posix()}"),
        "cost_blob": _git(repository, "rev-parse", f"HEAD:{COST_RELATIVE.as_posix()}"),
        "parameters": asdict(PARAMETERS),
        "source_sha256_before": pre_hashes,
    })
    _write_json(output / "current_candidate_reproduction.json", reproduction)
    _write_json(output / "strict_crossing_receipt.json", crossing)
    _write_json(output / "ratio_sign_aware_mapped_interval_receipt.json", ratio)
    _write_json(output / "p_b_backward_switching_diagnostic.json", backward)
    _write_json(output / "p_b_forward_switching_diagnostic.json", forward)
    _write_json(output / "scientific_authority_domain_audit.json", authority)
    _write_json(output / "classification_receipt.json", {
        "terminal_marker": TERMINAL,
        "classification": classification,
        "provenance_consistent": provenance_ok,
        "strict_crossing_confirmed": crossing["checks"]["p_b_backward_strict_crossing"],
        "numerically_admissible_branches": [row["branch"] for row in (backward, forward) if row["admissible"]],
        "selector_change": False,
    })
    ledger = {
        "f0364_cell_loads": 1,
        "persisted_candidate_reproductions": 1,
        "deterministic_scalar_diagnostics": 2,
        "full_selector_calls": 0,
        "scalar_roots": 0,
        "interior_a_switching_roots": 0,
        "policy_maps": 0,
        "d2_q_assemblies": 0,
        "hjb_direct_solves_or_updates": 0,
        "kfe_svd_calls": 0,
        "aggregate_integration_calls": 0,
        "scientific_retries": 0,
        "turn3_household_calls": 0,
        "wall_seconds": float(time.perf_counter() - started),
    }
    _write_json(output / "scientific_ledger.json", ledger)
    post_hashes = _source_hashes(repository)
    _write_json(output / "code_freeze_receipt.json", {
        "status": "PASS" if post_hashes == pre_hashes else "FAIL",
        "pre_execution_sha256": pre_hashes,
        "post_execution_sha256": post_hashes,
        "matches": post_hashes == pre_hashes,
        "selector_unchanged": pre_hashes[SELECTOR_RELATIVE.as_posix()] == post_hashes[SELECTOR_RELATIVE.as_posix()],
        "cost_unchanged": pre_hashes[COST_RELATIVE.as_posix()] == post_hashes[COST_RELATIVE.as_posix()],
    })
    _write_json(output / "terminal_receipt.json", {
        "terminal_marker": TERMINAL,
        "classification": classification,
        "selector_changed": False,
        "hjb": 0,
        "d2_q": 0,
        "kfe": 0,
        "turn3": 0,
        "successor_published": False,
    })
    if classification == CLASS_D or post_hashes != pre_hashes:
        raise ForensicFailure("forensic consistency or code-freeze failure")
    _manifest(output)
    readback = _readback(output)
    if readback["status"] != "PASS":
        raise ForensicFailure("independent evidence readback failed")
    return TERMINAL, classification


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    args = parser.parse_args(argv)
    terminal, classification = execute(args.repository)
    print(f"{terminal}__{classification}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
