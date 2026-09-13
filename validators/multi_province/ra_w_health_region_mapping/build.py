from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path
from typing import Mapping


BASELINE_SHA = "44df9bb331770a930d8ff465c23d59d6fe5cb65a"
WAGE_GATE = "WAGE_VARIABLE_IDENTITY_PROVEN_DIRECTLY_COMPARABLE"
NEXT_GATE = "OWNER_REVIEW_TWO_DIMENSIONAL_HEALTH_REGION_UNRESOLVED"
UNOBSERVED = "UNOBSERVED_OR_INTERPOLATION_NOT_AUTHORIZED"
DESCRIPTIVE_ONLY = "DESCRIPTIVE_ONLY__NOT_ADMISSIBILITY_CLASSIFICATION"

CANONICAL_HEALTH_LABELS = {
    "INTERIOR_A_DISTRIBUTION_CANDIDATE",
    "TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED",
    "LOWER_A_BOUNDARY_DOMINATED",
    "UPPER_A_BOUNDARY_PILEUP",
    "KFE_NUMERICALLY_PATHOLOGICAL",
}

STANDALONE_INPUTS = (
    (
        "coarse",
        Path("docs/evidence/ch5_mp4c_k1_standalone_hjb_ra_wage_coarse_3x3/points.csv"),
        Path("docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_COARSE_3X3_SCAN_ACCEPTANCE.md"),
        "5f55b474780d70921bfcf3ea2f863039c61814c1",
    ),
    (
        "first_refinement",
        Path("docs/evidence/ch5_mp4c_k1_standalone_hjb_ra_transition_refinement_3x3/points.csv"),
        Path("docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_TRANSITION_REFINEMENT_3X3_SCAN_ACCEPTANCE.md"),
        "cdaba87bae181280e182f639d4cf8fa5a5bae773",
    ),
    (
        "narrow",
        Path("docs/evidence/ch5_mp4c_k1_standalone_hjb_ra_wage_frontier_narrow_3x3/points.csv"),
        Path("docs/CH5_MP4C_K1_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_FRONTIER_NARROW_3X3_SCAN_ACCEPTANCE.md"),
        "d1401fc5154a6fb77989b0de343da20329bf724a",
    ),
)

MATLAB_SOURCES = (
    ("HANK_2ASSETS_HJB.m", "HANK_2ASSETS_HJB.m:26-31"),
    ("HANK_firm.m", "HANK_firm.m:55-81"),
    ("HANK_mp_1turn.m", "HANK_mp_1turn.m:13-16,44-52"),
    ("wage_caculate.m", "wage_caculate.m:1-17"),
)

PYTHON_SOURCES = (
    (Path("src/ch5_two_asset_hank/multi_province/wage.py"), "wage.py:11-76"),
    (Path("src/ch5_two_asset_hank/multi_province/household_adapter.py"), "household_adapter.py:43-65,95-137,200-219"),
    (Path("src/ch5_two_asset_hank/multi_province/steady_state.py"), "steady_state.py:147-168"),
    (Path("validators/multi_province/corrected_2018_two_turn/run.py"), "run.py:242-376"),
)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _decimal(value: str | float | int | Decimal) -> Decimal:
    return value if isinstance(value, Decimal) else Decimal(str(value))


def _decimal_text(value: Decimal) -> str:
    if value == 0:
        return "0"
    return format(value.normalize(), "f")


def _first_scalar(value: str) -> Decimal:
    text = value.strip()
    if text.startswith("["):
        parsed = json.loads(text)
        if not parsed:
            raise ValueError("expected a nonempty scalar list")
        return _decimal(parsed[0])
    return _decimal(text)


def canonical_health_label(
    *,
    source_label: str,
    modal_a: Decimal,
    amin: Decimal,
    amax: Decimal,
    kfe_pathological: bool,
) -> tuple[str, str]:
    """Return observed modal label and conservative health-map label."""

    if source_label in {
        "INTERIOR_A_DISTRIBUTION_CANDIDATE",
        "TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED",
        "LOWER_A_BOUNDARY_DOMINATED",
        "UPPER_A_BOUNDARY_PILEUP",
    }:
        distribution = source_label
    elif modal_a == amin:
        distribution = "LOWER_A_BOUNDARY_DOMINATED"
    elif modal_a == amax:
        distribution = "UPPER_A_BOUNDARY_PILEUP"
    else:
        raise ValueError(f"cannot map legacy source label {source_label!r}")
    health = "KFE_NUMERICALLY_PATHOLOGICAL" if kfe_pathological else distribution
    if distribution not in CANONICAL_HEALTH_LABELS or health not in CANONICAL_HEALTH_LABELS:
        raise ValueError("noncanonical health label")
    return distribution, health


def classify_projection(
    ra: Decimal,
    wage: Decimal,
    observed: Mapping[tuple[Decimal, Decimal], str],
) -> str:
    label = observed.get((ra, wage))
    if label is None:
        return UNOBSERVED
    if label == "INTERIOR_A_DISTRIBUTION_CANDIDATE":
        return "EXACT_OBSERVED_INTERIOR_MATCH"
    if label == "TRANSITION_AMBIGUOUS__OWNER_REVIEW_REQUIRED":
        return "EXACT_OBSERVED_AMBIGUOUS_MATCH"
    return "EXACT_OBSERVED_UNHEALTHY_MATCH"


def nearest_observed_coordinate(
    ra: Decimal,
    wage: Decimal,
    observed: Mapping[tuple[Decimal, Decimal], str],
) -> dict[str, str]:
    """Choose closest wage slice first, then closest return within that slice."""

    nearest_ra, nearest_wage = min(
        observed,
        key=lambda coordinate: (
            abs(coordinate[1] - wage),
            abs(coordinate[0] - ra),
            coordinate[1],
            coordinate[0],
        ),
    )
    return {
        "ra": _decimal_text(nearest_ra),
        "wage": _decimal_text(nearest_wage),
        "distance_ra": _decimal_text(abs(nearest_ra - ra)),
        "distance_wage": _decimal_text(abs(nearest_wage - wage)),
        "observed_health_label": observed[(nearest_ra, nearest_wage)],
        "selection_rule": "MIN_ABSOLUTE_WAGE_DISTANCE_THEN_MIN_ABSOLUTE_RA_DISTANCE",
        "use": DESCRIPTIVE_ONLY,
    }


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"refusing to write empty CSV: {path}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _standalone_rows(repo: Path) -> tuple[list[dict[str, object]], dict[tuple[Decimal, Decimal], str]]:
    output: list[dict[str, object]] = []
    observed: dict[tuple[Decimal, Decimal], str] = {}
    for scan_name, relative_csv, report, candidate in STANDALONE_INPUTS:
        source_path = repo / relative_csv
        for row in _read_csv(source_path):
            ra = _decimal(row["ra"])
            wage = _decimal(row["wage"])
            amin_mass = _decimal(row["amin_mass"])
            amax_mass = _decimal(row["amax_mass"])
            total_mass = _decimal(row["total_mass"])
            interior_text = row.get("interior_a_mass", "")
            interior_mass = _decimal(interior_text) if interior_text else total_mass - amin_mass - amax_mass
            at = _decimal(row["At"])
            density_min = _decimal(row["density_min"])
            severe_pathology = (
                amin_mass > Decimal("1")
                and amax_mass < Decimal("0")
                and interior_mass < Decimal("0")
                and at < Decimal("0")
                and density_min < Decimal("-0.001")
            )
            modal_a = _first_scalar(row["modal_a"])
            source_label = row.get("distribution_label") or row.get("quality_label") or ""
            distribution_label, health_label = canonical_health_label(
                source_label=source_label,
                modal_a=modal_a,
                amin=Decimal("0"),
                amax=Decimal("10"),
                kfe_pathological=severe_pathology,
            )
            coordinate = (ra, wage)
            if coordinate in observed:
                raise ValueError(f"duplicate accepted coordinate: {coordinate}")
            observed[coordinate] = health_label
            output.append({
                "scan": scan_name,
                "point_id": row["point_id"],
                "rb": row["rb"],
                "ra": row["ra"],
                "standalone_household_wage": row["wage"],
                "hjb_legal": str(not bool(row.get("first_illegal_iteration"))).lower(),
                "hjb_converged": str(row["hjb_classification"] == "HJB_CONVERGED").lower(),
                "hjb_iterations": row["iterations"],
                "source_distribution_label": source_label,
                "distribution_label": distribution_label,
                "health_map_label": health_label,
                "Ct": row["Ct"],
                "Lt": row["Lt"],
                "At": row["At"],
                "Bt": row["Bt"],
                "amin_mass": row["amin_mass"],
                "amax_mass": row["amax_mass"],
                "interior_a_mass": _decimal_text(interior_mass),
                "interior_a_mass_provenance": "DIRECT" if interior_text else "DERIVED_TOTAL_MINUS_AMIN_MINUS_AMAX",
                "modal_a": _decimal_text(modal_a),
                "kfe_signed_pathology": str(severe_pathology).lower(),
                "density_min": row["density_min"],
                "density_negative_count": row["density_negative_count"],
                "source_points_csv": relative_csv.as_posix(),
                "source_points_sha256": _sha256(source_path),
                "source_acceptance_report": report.as_posix(),
                "accepted_candidate_sha": candidate,
            })
    output.sort(key=lambda row: (_decimal(str(row["ra"])), _decimal(str(row["standalone_household_wage"]))))
    if len(output) != 27:
        raise ValueError(f"expected 27 accepted standalone points, got {len(output)}")
    return output, observed


def _frontier_position(ra: Decimal, closest_wage: Decimal, observed: Mapping[tuple[Decimal, Decimal], str]) -> str:
    slice_returns = sorted(key[0] for key in observed if key[1] == closest_wage)
    if ra < slice_returns[0]:
        return "BELOW_LOWEST_OBSERVED_RA_AT_CLOSEST_WAGE_SLICE"
    if ra > slice_returns[-1]:
        return "ABOVE_HIGHEST_OBSERVED_RA_AT_CLOSEST_WAGE_SLICE"
    if ra in slice_returns:
        return "EXACT_RA_AT_CLOSEST_WAGE_SLICE__WAGE_NOT_EXACT"
    return "BETWEEN_OBSERVED_RA_POINTS_AT_CLOSEST_WAGE_SLICE"


def _projection_rows(repo: Path, observed: Mapping[tuple[Decimal, Decimal], str]) -> list[dict[str, object]]:
    source = repo / "docs/evidence/ch5_mp4c_k1_hjb_convergence_mechanism_turn1_turn2/province_metrics.csv"
    output: list[dict[str, object]] = []
    for row in _read_csv(source):
        ra = _decimal(row["consumed_r_a"])
        raw_ra = _decimal(row["raw_entering_r_a"])
        wage = _decimal(row["consumed_household_composite_wage"])
        nearest = nearest_observed_coordinate(ra, wage, observed)
        closest_wage = _decimal(nearest["wage"])
        output.append({
            "turn": int(row["turn"]),
            "province_index": int(row["province_index"]),
            "province": row["province"],
            "raw_entering_ra": row["raw_entering_r_a"],
            "consumed_ra": row["consumed_r_a"],
            "return_guard_state": row["return_guard_state"],
            "return_guard_delta_consumed_minus_raw": _decimal_text(ra - raw_ra),
            "raw_firm_wage": "",
            "raw_firm_wage_status": "UNAVAILABLE_IN_ACCEPTED_COMPACT_PROVINCIAL_INPUT_EVIDENCE",
            "source_entering_firm_wage_variable": "wjt",
            "guarded_wjt": row["guarded_wjt"],
            "wage_guard_state": row["wage_guard_state"],
            "source_entering_household_wage_variable": "w / results.w",
            "consumed_household_composite_wage": row["consumed_household_composite_wage"],
            "standalone_comparable_wage": row["consumed_household_composite_wage"],
            "wage_identity": "results.w == HouseholdInputs.wages[0] == standalone HouseholdInputs.wages[0]",
            "wage_mapping_receipt": "wage_mapping_receipt.json",
            "projection_class": classify_projection(ra, wage, observed),
            "nearest_observed_ra": nearest["ra"],
            "nearest_observed_wage": nearest["wage"],
            "distance_ra": nearest["distance_ra"],
            "distance_wage": nearest["distance_wage"],
            "nearest_observed_health_label": nearest["observed_health_label"],
            "nearest_selection_rule": nearest["selection_rule"],
            "closest_wage_slice_ra_position": _frontier_position(ra, closest_wage, observed),
            "descriptive_use_only": DESCRIPTIVE_ONLY,
            "accepted_hjb_converged": row["converged"].lower(),
            "accepted_hjb_iterations": int(row["iterations"]),
            "accepted_output_exact": row["accepted_output_exact"].lower(),
            "source_province_metrics": source.relative_to(repo).as_posix(),
            "source_province_metrics_sha256": _sha256(source),
        })
    if len(output) != 62:
        raise ValueError(f"expected 62 accepted provincial calls, got {len(output)}")
    return output


def _range(values: list[Decimal]) -> dict[str, str]:
    return {"min": _decimal_text(min(values)), "max": _decimal_text(max(values))}


def _mean(values: list[Decimal]) -> str:
    return _decimal_text(sum(values, Decimal("0")) / Decimal(len(values)))


def _association(rows: list[dict[str, object]]) -> dict[str, object]:
    by_turn: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_turn[int(row["turn"])].append(row)
    turn_summary: dict[str, object] = {}
    for turn, group in sorted(by_turn.items()):
        converged = Counter(str(row["accepted_hjb_converged"]) for row in group)
        projection = Counter(str(row["projection_class"]) for row in group)
        projection_counts = {
            label: projection[label]
            for label in (
                "EXACT_OBSERVED_INTERIOR_MATCH",
                "EXACT_OBSERVED_UNHEALTHY_MATCH",
                "EXACT_OBSERVED_AMBIGUOUS_MATCH",
                UNOBSERVED,
            )
        }
        returns = [_decimal(str(row["consumed_ra"])) for row in group]
        wages = [_decimal(str(row["consumed_household_composite_wage"])) for row in group]
        return_deltas = [_decimal(str(row["return_guard_delta_consumed_minus_raw"])) for row in group]
        outcome_groups: dict[str, object] = {}
        for outcome in ("true", "false"):
            outcome_rows = [row for row in group if row["accepted_hjb_converged"] == outcome]
            if not outcome_rows:
                continue
            outcome_returns = [_decimal(str(row["consumed_ra"])) for row in outcome_rows]
            outcome_wages = [_decimal(str(row["consumed_household_composite_wage"])) for row in outcome_rows]
            outcome_groups["converged" if outcome == "true" else "failed"] = {
                "count": len(outcome_rows),
                "consumed_ra_mean": _mean(outcome_returns),
                "consumed_ra_range": _range(outcome_returns),
                "consumed_household_composite_wage_mean": _mean(outcome_wages),
                "consumed_household_composite_wage_range": _range(outcome_wages),
                "return_guard_state_counts": dict(sorted(Counter(str(row["return_guard_state"]) for row in outcome_rows).items())),
                "wage_guard_state_counts": dict(sorted(Counter(str(row["wage_guard_state"]) for row in outcome_rows).items())),
            }
        turn_summary[str(turn)] = {
            "calls": len(group),
            "converged": converged["true"],
            "failed": converged["false"],
            "projection_class_counts": projection_counts,
            "consumed_ra_range": _range(returns),
            "consumed_household_composite_wage_range": _range(wages),
            "return_guard_delta_range": _range(return_deltas),
            "return_guard_state_counts": dict(sorted(Counter(str(row["return_guard_state"]) for row in group).items())),
            "wage_guard_state_counts": dict(sorted(Counter(str(row["wage_guard_state"]) for row in group).items())),
            "outcome_groups": outcome_groups,
        }

    indexed = {(int(row["province_index"]), int(row["turn"])): row for row in rows}
    transition: list[dict[str, object]] = []
    for province_index in range(31):
        turn1 = indexed[(province_index, 1)]
        turn2 = indexed[(province_index, 2)]
        if turn1["accepted_hjb_converged"] == "true" and turn2["accepted_hjb_converged"] == "false":
            transition.append({
                "province_index": province_index,
                "province": turn1["province"],
                "delta_consumed_ra": _decimal(str(turn2["consumed_ra"])) - _decimal(str(turn1["consumed_ra"])),
                "delta_consumed_wage": _decimal(str(turn2["consumed_household_composite_wage"])) - _decimal(str(turn1["consumed_household_composite_wage"])),
            })
    return_deltas = [row["delta_consumed_ra"] for row in transition]
    wage_deltas = [row["delta_consumed_wage"] for row in transition]
    return {
        "analysis_type": "DESCRIPTIVE_ASSOCIATION_ONLY__NO_CAUSAL_CLAIM",
        "wage_gate": WAGE_GATE,
        "standalone_wage_coverage": {"min": "0.8", "max": "1.3"},
        "turn_summary": turn_summary,
        "turn1_converged_to_turn2_failed": {
            "count": len(transition),
            "higher_consumed_ra_count": sum(value > 0 for value in return_deltas),
            "lower_consumed_ra_count": sum(value < 0 for value in return_deltas),
            "unchanged_consumed_ra_count": sum(value == 0 for value in return_deltas),
            "mean_delta_consumed_ra": _mean(return_deltas),
            "higher_consumed_wage_count": sum(value > 0 for value in wage_deltas),
            "lower_consumed_wage_count": sum(value < 0 for value in wage_deltas),
            "unchanged_consumed_wage_count": sum(value == 0 for value in wage_deltas),
            "mean_delta_consumed_wage": _mean(wage_deltas),
            "rows": [
                {
                    **row,
                    "delta_consumed_ra": _decimal_text(row["delta_consumed_ra"]),
                    "delta_consumed_wage": _decimal_text(row["delta_consumed_wage"]),
                }
                for row in transition
            ],
        },
        "coverage_blocker": "62/62 accepted provincial consumed composite wages exceed the maximum observed standalone wage; no provincial point has an exact observed (ra,w) coordinate",
        "supported_inference": "variable identity is aligned, but observed health-map coverage does not support provincial admissibility classification or a claim that return mapping caused turn2 failure",
        "guard_association_interpretation": "return and wage guard states coexist with failure and convergence in accepted evidence and do not provide an exclusive separator",
        "primary_unresolved_issue": "INSUFFICIENT_OBSERVED_HEALTH_MAP_COVERAGE_AT_PROVINCIAL_COMPOSITE_WAGE_SCALE",
        "next_owner_gate": NEXT_GATE,
    }


def _wage_semantic_trace() -> dict[str, object]:
    return {
        "gate_result": WAGE_GATE,
        "gate_subject": "standalone household wage versus multi-province household-HJB consumed wage",
        "matlab_chain": [
            {
                "object": "firm raw wage",
                "variable": "wt0",
                "dimension": "one scalar per destination province",
                "operation": "guard to [grids.wjtmin, grids.wjtmax]",
                "location": "HANK_firm.m:66-73",
            },
            {
                "object": "guarded provincial firm wage",
                "variable": "results{j}.wjt",
                "dimension": "N_prov destination vector across j",
                "operation": "input to wage_caculate; distinct from household results.w",
                "location": "HANK_firm.m:81; wage_caculate.m:7-11",
            },
            {
                "object": "household composite wage",
                "variable": "wt_vec(i) -> results{i}.w",
                "dimension": "one scalar per origin household province i",
                "operation": "destination aggregation over j; assigned for next household turn",
                "location": "wage_caculate.m:3-17; HANK_mp_1turn.m:49-52",
            },
            {
                "object": "household-HJB consumed wage",
                "variable": "w = results.w",
                "dimension": "scalar for the province household call",
                "operation": "read directly by HANK_2ASSETS_HJB",
                "location": "HANK_2ASSETS_HJB.m:26-31",
            },
        ],
        "python_chain": [
            {
                "object": "guarded provincial firm wages",
                "variable": "firm_wages[destination]",
                "dimension": "length-N destination vector",
                "operation": "source-faithful input to composite_household_wages",
                "location": "src/ch5_two_asset_hank/multi_province/wage.py:11-34,55-75",
            },
            {
                "object": "household composite wages",
                "variable": "output[origin] / turn.household_composite_wage[i] / state['w']",
                "dimension": "length-N origin vector then scalar per province state",
                "operation": "persisted into post-turn state",
                "location": "src/ch5_two_asset_hank/multi_province/wage.py:52-76; steady_state.py:147-168",
            },
            {
                "object": "household-HJB consumed wage",
                "variable": "MultiProvinceHouseholdInputs.composite_wage -> HouseholdInputs.wages[0]",
                "dimension": "scalar represented as a singleton labor-choice vector",
                "operation": "direct static call mapping",
                "location": "src/ch5_two_asset_hank/multi_province/household_adapter.py:43-65,95-137,200-219",
            },
        ],
        "standalone_identity": {
            "standalone_object": "HouseholdInputs.wages[0]",
            "provincial_consumed_object": "results.w / HouseholdInputs.wages[0]",
            "identity_result": "SAME_SOURCE_ROLE_AND_SAME_API_SLOT__NO_ADDITIONAL_UNIT_OR_NORMALIZATION_CONVERSION_DEFINED",
            "units": "NOT_EXPLICIT_IN_DESIGNATED_SOURCE",
            "normalization": "NO_ADDITIONAL_NORMALIZATION_EXPLICIT_BETWEEN_RESULTS_W_AND_HOUSEHOLDINPUTS_WAGES_0",
        },
        "important_nonidentity": "guarded wjt is not the standalone wage object and cannot be used as a direct projection coordinate",
        "scale_observation": {
            "standalone_observed_wage_values": [0.8, 1.05, 1.3],
            "accepted_provincial_consumed_composite_wage_range": "computed in association_summary.json",
            "interpretation": "same consumed object, disjoint observed numerical coverage",
        },
    }


def _mapping_receipt() -> dict[str, object]:
    return {
        "purpose": "document the source-defined wjt-to-results.w transformation; it is not an outcome-fitted rescaling",
        "wage_gate": WAGE_GATE,
        "gate_note": "No transformation is needed between standalone w and provincial consumed results.w; this receipt explains the upstream transformation from guarded wjt.",
        "matlab_formula": "results.w(i) = alphal^(-phi_l/(1+phi_l)) * (sum_j phi_l_mat(j,i) * (results{j}.wjt * (1-results{j}.tau-sigmau_MAT(j,i)) / phi_l_mat(j,i))^(1+1/phi_l))^(phi_l/(1+phi_l))",
        "indices": {"j": "destination", "i": "origin household province"},
        "inputs": ["guarded results{j}.wjt", "destination results{j}.tau", "phi_l_mat(j,i)", "sigmau_MAT(j,i)", "param.phi_l", "param.alphal"],
        "output": "wt_vec(i), assigned to results{i}.w for the next household HJB turn",
        "matlab_location": "wage_caculate.m:1-17; HANK_mp_1turn.m:49-52",
        "python_location": "src/ch5_two_asset_hank/multi_province/wage.py:11-76; steady_state.py:147-168",
        "prohibited_use": "Do not rescale a provincial composite wage into [0.8,1.3], and do not substitute guarded wjt as the standalone coordinate.",
    }


def build(repo: Path, matlab_root: Path, output: Path) -> None:
    repo = repo.resolve()
    matlab_root = matlab_root.resolve()
    output.mkdir(parents=True, exist_ok=True)
    standalone, observed = _standalone_rows(repo)
    projection = _projection_rows(repo, observed)
    association = _association(projection)
    if any(row["projection_class"] != UNOBSERVED for row in projection):
        raise ValueError("unexpected exact observed provincial projection")
    if min(_decimal(str(row["consumed_household_composite_wage"])) for row in projection) <= Decimal("1.3"):
        raise ValueError("provincial wage coverage assertion no longer holds")

    _write_csv(output / "standalone_health_map.csv", standalone)
    _write_json(output / "standalone_health_map.json", {"point_count": 27, "canonical_labels": sorted(CANONICAL_HEALTH_LABELS), "points": standalone})
    _write_json(output / "wage_semantic_trace.json", _wage_semantic_trace())
    _write_json(output / "wage_mapping_receipt.json", _mapping_receipt())
    _write_csv(output / "provincial_projection.csv", projection)
    _write_json(output / "provincial_projection.json", {"wage_gate": WAGE_GATE, "row_count": 62, "rows": projection})
    _write_json(output / "association_summary.json", association)

    evidence_paths = [repo / item[1] for item in STANDALONE_INPUTS]
    evidence_paths += [repo / item[2] for item in STANDALONE_INPUTS]
    evidence_paths += [repo / "docs/evidence/ch5_mp4c_k1_hjb_convergence_mechanism_turn1_turn2/province_metrics.csv"]
    evidence_paths += [repo / "docs/evidence/ch5_mp4c_k1_hjb_convergence_mechanism_turn1_turn2/identity_receipts.json"]
    evidence_paths += [repo / "docs/evidence/ch5_mp4c_k1_hjb_convergence_mechanism_turn1_turn2/wage_guard_metadata_adjudication.json"]
    source_identity = {
        "baseline_sha": BASELINE_SHA,
        "accepted_evidence": [{"path": path.relative_to(repo).as_posix(), "sha256": _sha256(path)} for path in evidence_paths],
        "matlab_sources": [{"path": str(matlab_root / name), "location": location, "sha256": _sha256(matlab_root / name)} for name, location in MATLAB_SOURCES],
        "python_sources": [{"path": path.as_posix(), "location": location, "sha256": _sha256(repo / path)} for path, location in PYTHON_SOURCES],
        "audit_implementation": [
            {
                "path": "validators/multi_province/ra_w_health_region_mapping/build.py",
                "sha256": _sha256(repo / "validators/multi_province/ra_w_health_region_mapping/build.py"),
            },
            {
                "path": "tests/test_k1_ra_w_health_region_mapping.py",
                "sha256": _sha256(repo / "tests/test_k1_ra_w_health_region_mapping.py"),
            },
        ],
        "external_sources_read_only": True,
    }
    _write_json(output / "source_identity.json", source_identity)
    _write_json(output / "call_ledger.json", {
        "task_id": "CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT",
        "operation": "accepted-evidence parsing and deterministic offline tabulation only",
        "hjb_calls": 0,
        "kfe_calls": 0,
        "global_outer_turns": 0,
        "matlab_runtime_calls": 0,
        "firm_runtime_calls": 0,
        "k1b_calls": 0,
        "k2_calls": 0,
        "ge_calls": 0,
        "annual_downstream_calls": 0,
        "shock_calls": 0,
        "irf_calls": 0,
        "results_calls": 0,
        "scientific_retries": 0,
    })
    manifest_entries = []
    for path in sorted(output.iterdir(), key=lambda item: item.name):
        if path.name == "sealed_manifest_sha256.json" or not path.is_file():
            continue
        manifest_entries.append({
            "path": path.name,
            "bytes": path.stat().st_size,
            "sha256": _sha256(path).upper(),
        })
    _write_json(output / "sealed_manifest_sha256.json", {
        "schema": "CH5_MP4C_K1_RA_W_HEALTH_REGION_PROVINCIAL_MAPPING_SEALED_MANIFEST_V1",
        "bytes_excluding_manifest": sum(entry["bytes"] for entry in manifest_entries),
        "entries": manifest_entries,
    })


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--matlab-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build(args.repo, args.matlab_root, args.output)


if __name__ == "__main__":
    main()
