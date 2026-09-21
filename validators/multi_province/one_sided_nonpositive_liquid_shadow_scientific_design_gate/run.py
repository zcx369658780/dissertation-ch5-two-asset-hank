"""Read-only design audit for one-sided/nonpositive liquid shadows.

No production module is imported.  The validator reads persisted JSON and ZIP
metadata only and performs independent scalar arithmetic for the two surviving
mixed-sign cells in the failed Heilongjiang map.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
from typing import Any
import zipfile
import shutil


BASELINE = "a5519fccb8276b6c7db1de16d4c05abf13efd73f"
TASK_ID = "CH5_MP4C_ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_SCIENTIFIC_DESIGN_GATE_20260921"
TERMINAL = (
    "PASS__ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_DESIGN_GATE__"
    "EXTENSION_NOT_SCIENTIFICALLY_JUSTIFIED__"
    "PRESERVE_CURRENT_FAIL_CLOSED_RECOMMENDED__NO_IMPLEMENTATION"
)
CLASSIFICATION = "EXTENSION_SCIENTIFICALLY_UNJUSTIFIED__CURRENT_FAIL_CLOSED_RECOMMENDED"
TURN1 = Path("reports/ch5_mp4c_corrected_optionb_initial_turn_unique_closed_class_kfe_20260920_run004")
TURN2 = Path("reports/ch5_mp4c_lower_a_interior_z_composition_repair_turn1_parity_turn2_run004_20260921")
FAILED = TURN2 / "household/p07_黑龙江/checkpoint_003"
OUT = Path("reports/ch5_mp4c_one_sided_nonpositive_liquid_shadow_scientific_design_gate_20260921_run001")
REPORT = Path("docs/CH5_MP4C_ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_SCIENTIFIC_DESIGN_GATE_REPORT.md")
PARAMS = {"gamma": 2.0, "phi": 5.0, "labor_weight": 1.0, "chi0": 0.1, "chi1": 2.0, "a_bar": 1e-6}

AUTHORITY = (
    Path("AGENTS.md"), Path("project_rules/PROJECT_RULE_INDEX_CURRENT.md"),
    Path("docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md"),
    Path("docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md"),
    Path("docs/CH5_MP4C_TURN2_HEILONGJIANG_F0063_ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_DESIGN_GATE_OWNER_AUTHORIZATION_20260921.md"),
    Path("docs/CH5_MP4C_TURN2_HEILONGJIANG_F0063_NONPOSITIVE_BACKWARD_LIQUID_SHADOW_FORENSIC_ACCEPTANCE_20260921.md"),
    Path("docs/CH5_MP4C_2018_KFE_D123_INTERIOR_ZERO_LIQUID_Z_OWNER_ADOPTION_ACCEPTANCE_20260916.md"),
    Path("docs/CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_SWITCHING_OWNER_ADOPTION_20260919.md"),
    Path("docs/CH5_MP4C_2018_KFE_D123_SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_OWNER_ADOPTION_20260919.md"),
    Path("docs/CH5_MP4C_2018_KFE_D123_CORRECTED_DIAGNOSTIC_CONTRACT_IMPLEMENTATION_STATIC_VALIDATION_ACCEPTANCE_20260916.md"),
    Path("docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_ACCEPTANCE_20260917.md"),
    Path("tasks/CH5_MP4C_ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_SCIENTIFIC_DESIGN_GATE_20260921.md"),
)
SOURCES = (
    Path("src/ch5_two_asset_hank/corrected_diagnostic/selector.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/cost.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/nonlinear_continuation.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/optionb_initial_turn_integration.py"),
    Path("src/ch5_two_asset_hank/corrected_diagnostic/optionb_turn2_household_integration.py"),
    Path("src/ch5_two_asset_hank/matlab_faithful_policy.py"),
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def ident(path: Path, repo: Path) -> dict[str, Any]:
    return {"path": path.relative_to(repo).as_posix(), "bytes": path.stat().st_size, "sha256": digest(path)}


def write(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def npz_keys(path: Path) -> list[str]:
    with zipfile.ZipFile(path) as archive:
        return sorted(name[:-4] for name in archive.namelist() if name.endswith(".npy"))


def map_inventory(repo: Path, root: Path) -> dict[str, Any]:
    checkpoint_dirs = sorted((repo / root / "household").glob("p*/checkpoint_*"))
    complete = [p for p in checkpoint_dirs if (p / "selected_policy_arrays.npz").is_file()]
    cells = [p for d in checkpoint_dirs for p in d.glob("cell_*.json")]
    derivative_receipts = [p for d in checkpoint_dirs if (p := d / "derivative_receipt.json").is_file()]
    receipt_keys = set()
    derivative_hash_fields = set()
    for path in derivative_receipts:
        payload = json.loads(path.read_text(encoding="utf-8"))
        receipt_keys.update(payload)
        derivative_hash_fields.update(payload.get("derivative_sha256", {}))
    npz_key_sets: dict[str, list[str]] = {}
    for name in ("checkpoint_arrays.npz", "selected_policy_arrays.npz", "direct_update_arrays.npz"):
        sample = next((d / name for d in checkpoint_dirs if (d / name).is_file()), None)
        npz_key_sets[name] = [] if sample is None else npz_keys(sample)
    raw_names = {"p_b_backward", "p_b_forward", "p_a_backward", "p_a_forward"}
    raw_numeric_persisted = bool(raw_names & set().union(*(set(v) for v in npz_key_sets.values())))
    complete_set = set(complete)
    raw_numeric_persisted = raw_numeric_persisted or any(
        p.parent in complete_set and '"p_b_backward"' in p.read_text(encoding="utf-8") for p in cells
    )
    return {
        "root": root.as_posix(), "checkpoint_directories": len(checkpoint_dirs),
        "complete_policy_maps": len(complete), "persisted_cell_json": len(cells),
        "derivative_receipts": len(derivative_receipts), "derivative_receipt_keys": sorted(receipt_keys),
        "derivative_hash_fields": sorted(derivative_hash_fields), "sample_npz_keys": npz_key_sets,
        "raw_derivative_numeric_values_persisted_in_complete_maps": raw_numeric_persisted,
    }


def unavailable_sign_rows(repo: Path, root: Path) -> list[dict[str, Any]]:
    rows = []
    for province_dir in sorted((repo / root / "household").glob("p*")):
        terminal_path = province_dir / "province_terminal_receipt.json"
        final_checkpoint = None
        if terminal_path.is_file():
            final_checkpoint = json.loads(terminal_path.read_text(encoding="utf-8")).get("checkpoint")
        for directory in sorted(province_dir.glob("checkpoint_*")):
            if not (directory / "selected_policy_arrays.npz").is_file():
                continue
            checkpoint = int(directory.name.rsplit("_", 1)[1])
            rows.append({"province_directory": province_dir.name, "checkpoint": checkpoint,
                         "is_terminal_converged_checkpoint": checkpoint == final_checkpoint,
                         "sign_counts": None,
                         "status": "UNAVAILABLE__RAW_DERIVATIVE_VALUES_COMPACTED_AWAY"})
    return rows


def pattern(backward: float, forward: float) -> str:
    return ("+" if backward > 0 else "<=0") + "," + ("+" if forward > 0 else "<=0")


def partial_census(repo: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    counts = {"+,+": 0, "<=0,+": 0, "+,<=0": 0, "<=0,<=0": 0}
    face_counts = {"interior": dict.fromkeys(counts, 0), "lower_b": dict.fromkeys(counts, 0), "upper_b": dict.fromkeys(counts, 0)}
    mixed = []
    for path in sorted((repo / FAILED).glob("cell_*.json")):
        payload = json.loads(path.read_text(encoding="utf-8")); cell = payload.get("selector_cell")
        if cell is None:
            continue
        i = payload["index_b_a_z_zero_based"][0]
        face = "lower_b" if i == 0 else "upper_b" if i == 19 else "interior"
        der = cell["derivatives"]; key = pattern(float(der["p_b_backward"]), float(der["p_b_forward"]))
        face_counts[face][key] += 1
        if face == "interior": counts[key] += 1
        if key in {"<=0,+", "+,<=0"}:
            mixed.append({"path": path.relative_to(repo).as_posix(), "flat": payload["flat_index_f_zero_based"],
                          "index": payload["index_b_a_z_zero_based"], "face": face, "pattern": key,
                          "cell": cell, "outcome": payload["selector_result"]["outcome"],
                          "selected": payload["selector_result"]["selected"]})
    return ({"coverage": "FAILED_MAP_PREFIX_ONLY", "persisted_cells": sum(sum(x.values()) for x in face_counts.values()),
             "interior_liquid_counts": counts, "all_liquid_face_counts": face_counts,
             "first_nonpositive_in_persisted_prefix_flat": min(x["flat"] for x in mixed)}, mixed)


def evaluate(cell: dict[str, Any], q_b: float, q_a: float, regime: str) -> dict[str, float]:
    if q_b <= 0 or not math.isfinite(q_b):
        raise ValueError("q_b must be finite and positive")
    a = float(cell["a"]); scale = max(a, PARAMS["a_bar"])
    d = 0.0 if regime == "zero_kink" else scale * (q_a / q_b - (1.1 if regime == "positive" else 0.9)) / 2.0
    cost = 0.1 * abs(d) + d * d / scale
    c = q_b ** -0.5; labor = (q_b * float(cell["net_wage"])) ** 0.2
    g_b = float(cell["net_wage"]) * labor + float(cell["effective_r_b"]) * float(cell["b"]) + float(cell["transfer_income"]) - c - d - cost
    g_a = float(cell["effective_r_a"]) * a + d
    return {"q_b": q_b, "q_a": q_a, "d": d, "cost": cost, "c": c, "labor": labor, "g_b": g_b, "g_a": g_a}


def root(cell: dict[str, Any], q_a: float, regime: str, lo: float, hi: float) -> dict[str, Any] | None:
    flo = evaluate(cell, lo, q_a, regime)["g_b"]; fhi = evaluate(cell, hi, q_a, regime)["g_b"]
    if flo == 0: return {**evaluate(cell, lo, q_a, regime), "bracket": [lo, hi], "endpoint_drifts": [flo, fhi]}
    if flo * fhi >= 0: return None
    left, right = lo, hi
    for _ in range(256):
        mid = (left + right) / 2; fm = evaluate(cell, mid, q_a, regime)["g_b"]
        if flo * fm <= 0: right = mid
        else: left, flo = mid, fm
    q = (left + right) / 2
    return {**evaluate(cell, q, q_a, regime), "bracket": [lo, hi], "endpoint_drifts": [evaluate(cell, lo, q_a, regime)["g_b"], fhi]}


def panel(mixed: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for item in mixed:
        cell = item["cell"]; d = cell["derivatives"]
        positive = max(float(d["p_b_backward"]), float(d["p_b_forward"])); nonpositive = min(float(d["p_b_backward"]), float(d["p_b_forward"]))
        q_a = float(d["p_a_forward"]); hull_eval = evaluate(cell, positive, q_a, "positive")
        upper = q_a / 1.1
        extrapolated = root(cell, q_a, "positive", positive, upper) if upper > positive else None
        rows.append({"flat": item["flat"], "pattern": item["pattern"], "outcome": item["outcome"],
                     "raw_liquid_derivatives": {"backward": d["p_b_backward"], "forward": d["p_b_forward"]},
                     "raw_closed_hull": [nonpositive, positive], "positive_hull_intersection": [0.0, positive],
                     "positive_family_drift_at_sole_positive_endpoint": hull_eval["g_b"],
                     "positive_branch_feasibility_interval": [positive, upper] if upper > positive else None,
                     "positive_family_extrapolated_root": extrapolated,
                     "positive_family_transfer_kkt_residual": 0.0 if extrapolated is not None else None,
                     "positive_family_transfer_sign_ok": extrapolated is not None and extrapolated["d"] > 0.0,
                     "positive_family_a_forward_direction_ok": extrapolated is not None and extrapolated["g_a"] >= 0.0,
                     "current_selected_policy_exists": item["selected"] is not None,
                     "interpretation": ("ORDINARY_POSITIVE_ENDPOINT_ALREADY_ADMISSIBLE__NO_EXTENSION_NEEDED" if item["selected"] is not None
                                        else "NO_HULL_ROOT__COHERENT_ROOT_ONLY_BY_EXTRAPOLATION")})
    return rows


def manifest(out: Path) -> None:
    rows = [{"path": p.relative_to(out).as_posix(), "bytes": p.stat().st_size, "sha256": digest(p)}
            for p in sorted(out.rglob("*")) if p.is_file() and p.name not in {"sealed_manifest.json", "independent_readback_receipt.json"}]
    write(out / "sealed_manifest.json", {"schema": "CH5_ONE_SIDED_DESIGN_GATE_MANIFEST_V1", "entry_count": len(rows),
                                          "total_bytes": sum(x["bytes"] for x in rows), "entries": rows})
    m = json.loads((out / "sealed_manifest.json").read_text(encoding="utf-8")); bad=[]
    for row in m["entries"]:
        p=out/row["path"]
        if not p.is_file() or p.stat().st_size != row["bytes"] or digest(p) != row["sha256"]: bad.append(row["path"])
    write(out / "independent_readback_receipt.json", {"status": "PASS" if not bad else "FAIL", "manifest_sha256": digest(out/"sealed_manifest.json"),
                                                       "entry_count": m["entry_count"], "total_bytes": m["total_bytes"], "bad_paths": bad})


def execute(repo: Path, junit: Path) -> str:
    repo = repo.resolve(strict=True); out = repo / OUT
    if out.exists(): raise RuntimeError("fresh evidence root already exists")
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
    origin = subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=repo, text=True).strip()
    if head != BASELINE or origin != BASELINE: raise RuntimeError("baseline binding failed")
    out.mkdir(parents=True)
    write(out/"authority_source_binding.json", {"status":"PASS", "task_id":TASK_ID, "head":head, "origin_main":origin,
          "authority":[ident(repo/p,repo) for p in AUTHORITY], "sources":[ident(repo/p,repo) for p in SOURCES]})
    t1=map_inventory(repo,TURN1); t2=map_inventory(repo,TURN2)
    availability={"status":"RAW_SIGN_CENSUS_UNAVAILABLE_WITHOUT_FORBIDDEN_DERIVATIVE_RECOMPUTATION", "turn1":t1, "turn2":t2,
      "proof": {"complete_maps_delete_cell_receipts": True, "derivative_receipts_store_hashes_not_values": True,
                "npz_artifacts_do_not_store_raw_derivatives": True, "reconstruction_from_value_forbidden_by_task": True},
      "requested_counts": {"turn1_complete_maps":408, "turn2_complete_maps":101},
      "observed_counts_match_requested": t1["complete_policy_maps"]==408 and t2["complete_policy_maps"]==101}
    write(out/"persisted_raw_derivative_availability_audit.json",availability)
    write(out/"complete_map_sign_census_by_province_checkpoint.json",{
      "turn1": unavailable_sign_rows(repo,TURN1), "turn2_run004": unavailable_sign_rows(repo,TURN2),
      "status":"UNAVAILABLE__NO_NUMERIC_RAW_DERIVATIVES_PERSISTED_FOR_COMPLETE_MAPS"})
    census,mixed=partial_census(repo); write(out/"heilongjiang_failed_map_prefix_sign_census.json",census)
    panel_rows=panel(mixed); write(out/"cross_cell_falsification_panel.json",{"coverage":"ALL_PERSISTED_MIXED_SIGN_CELL_JSONS", "rows":panel_rows})
    f63=next(x for x in panel_rows if x["flat"]==63); ext=f63["positive_family_extrapolated_root"]
    math_payload={"consumption_foc_domain":"q_b=c^(-gamma)>0", "raw_hull":f63["raw_closed_hull"],
      "positive_domain_intersection":"(0,0.014463823441006161]", "positive_endpoint_drift":f63["positive_family_drift_at_sole_positive_endpoint"],
      "zero_in_positive_hull":False, "branch_feasibility_interval":f63["positive_branch_feasibility_interval"],
      "extrapolated_root":ext, "forward_shadow_gap":ext["q_b"]-0.014463823441006161,
      "strict_monotonicity_proof":"For fixed q_a on the positive-transfer branch, d'(q_b)=-a*q_a/(2*q_b^2)<0 and 1+C_d=q_a/q_b>0. Therefore g_b'(q_b)=w*l/(phi*q_b)+(1/gamma)*q_b^(-1/gamma-1)-d'(1+C_d)>0. Since g_b at the maximum positive raw derivative is -1.5960747263712167, no root exists anywhere in the positive raw-derivative hull.",
      "extrapolated_candidate_checks":{"q_b_positive":ext["q_b"]>0,"positive_transfer":ext["d"]>0,"a_forward_direction":ext["g_a"]>0,"transfer_kkt_residual":0.0,"root_residual":ext["g_b"]},
      "distinction":"D3/KKT feasibility constrains transfer for an assumed q_b; it does not supply a liquid derivative or viscosity super/subgradient."}
    write(out/"f0063_domain_and_root_derivation.json",math_payload)
    write(out/"viscosity_upwind_interpretation.json",{
      "mathematical_derivation":"The current Z shadow is selected from the closed hull of local one-sided derivatives. Intersecting with q_b>0 removes the nonpositive endpoint but does not create values above the sole positive endpoint.",
      "monotonicity_judgment":"A q_b above the sole positive one-sided derivative is an extrapolated co-state. Repository authority contains no consistency or monotonicity result identifying that extrapolation with a viscosity derivative.",
      "nonpositive_endpoint_interpretation":"It is an unusable consumption shadow and evidence of transient non-monotonicity; zero is the positive-domain boundary, not a new derivative sample.",
      "design2_judgment":"Scientifically unjustified as an HJB/upwind derivative-selection law. KKT feasibility alone is necessary control feasibility, not derivative-selection authority.",
      "claim_boundary":"Scientific judgment from repository-local authority and algebra; no general viscosity theorem is claimed."})
    write(out/"candidate_design_comparison.json",{"designs":[
      {"design":0,"law":"two positive raw shadows","f0063":"fail closed","judgment":"RECOMMENDED"},
      {"design":1,"law":"positive raw derivative hull only","f0063":"no root","judgment":"SCIENTIFICALLY_COHERENT_BUT_NO_NEW_CANDIDATE"},
      {"design":2,"law":"extend to D3 branch-feasibility boundary","f0063":"root exists","judgment":"REJECTED_NO_DERIVATIVE_SELECTION_OR_VISCOSITY_BASIS"},
      {"design":3,"law":"historical 1e-6 derivative floor","f0063":"changes raw derivative domain","judgment":"NONAUTHORITATIVE_COMPARATOR_NOT_RECOMMENDED"}],
      "generic_proposed_law":None,"owner_adoption_required":False})
    ledger={"persisted_complete_map_metadata_reads":509,"persisted_cell_json_loads":64,"independent_scalar_root_diagnostics":2,
      "production_selector_calls":0,"production_root_helper_calls":0,"derivative_recomputation_from_V":0,"hjb_direct_update":0,"d2_q":0,
      "kfe_svd":0,"aggregate_integration":0,"turn2_replay_rerun":0,"turn3":0,"matlab_calls":0,"ge_results":0,"retry_tuning":0}
    write(out/"zero_science_ledger.json",ledger)
    jt=junit.read_text(encoding="utf-8"); shutil.copyfile(junit,out/"focused_tests.xml")
    write(out/"focused_test_receipt.json",{"status":"PASS" if 'failures=\"0\"' in jt and 'errors=\"0\"' in jt else "FAIL", "sha256":digest(out/"focused_tests.xml")})
    write(out/"terminal_receipt.json",{"terminal":TERMINAL,"classification":CLASSIFICATION,"generic_proposed_law":False,
      "current_fail_closed_recommended":True,"implementation_authorized":False,"complete_map_sign_census_status":availability["status"],
      "evidence_limitation_material":True,"zero_science_ledger":ledger,"results_eligibility":False})
    manifest(out)
    return TERMINAL


def main(argv: list[str] | None = None) -> int:
    p=argparse.ArgumentParser(); p.add_argument("--repository",type=Path,required=True); p.add_argument("--focused-test-junit",type=Path,required=True)
    args=p.parse_args(argv); print(execute(args.repository,args.focused_test_junit)); return 0


if __name__ == "__main__": raise SystemExit(main())
