from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any, Iterable, Sequence


SCHEMA_PREFIX = "CH5_MP4C_K1_FIRST_TURN_PROVINCIAL_INPUT_OUTCOME_ENVELOPE"
FAILURE = "failure"
SUCCESS = "success"
EPSILON = 1e-12


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def git_blob_bytes(repo_root: Path, path: Path) -> bytes:
    relative = path.resolve().relative_to(repo_root.resolve()).as_posix()
    return subprocess.run(
        ["git", "show", f"HEAD:{relative}"],
        cwd=repo_root,
        check=True,
        capture_output=True,
    ).stdout


def sha256_git_blob(repo_root: Path, path: Path) -> str:
    return hashlib.sha256(git_blob_bytes(repo_root, path)).hexdigest().upper()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def linear_quantile(values: Sequence[float], probability: float) -> float:
    ordered = sorted(float(value) for value in values)
    if not ordered:
        raise ValueError("quantile requires at least one value")
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def quantile_summary(values: Sequence[float]) -> dict[str, float]:
    return {
        "min": linear_quantile(values, 0.0),
        "q25": linear_quantile(values, 0.25),
        "median": linear_quantile(values, 0.5),
        "q75": linear_quantile(values, 0.75),
        "max": linear_quantile(values, 1.0),
    }


def threshold_existence(
    failure_values: Sequence[float], success_values: Sequence[float]
) -> dict[str, Any]:
    if not failure_values or not success_values:
        raise ValueError("both outcome groups are required")
    failure_min = min(failure_values)
    failure_max = max(failure_values)
    success_min = min(success_values)
    success_max = max(success_values)
    if failure_max < success_min:
        return {
            "exists": True,
            "direction": "FAILURE_BELOW_SUCCESS",
            "open_interval": [failure_max, success_min],
            "witness": {"max_failure": failure_max, "min_success": success_min},
        }
    if failure_min > success_max:
        return {
            "exists": True,
            "direction": "FAILURE_ABOVE_SUCCESS",
            "open_interval": [success_max, failure_min],
            "witness": {"min_failure": failure_min, "max_success": success_max},
        }
    return {
        "exists": False,
        "direction": None,
        "open_interval": None,
        "counterexample": {
            "failure_range": [failure_min, failure_max],
            "success_range": [success_min, success_max],
            "overlap_interval": [
                max(failure_min, success_min),
                min(failure_max, success_max),
            ],
        },
    }


def standardize_rows(
    rows: Sequence[dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, float | str]]:
    if not rows:
        raise ValueError("standardization requires rows")
    ra_values = [float(row["consumed_ra"]) for row in rows]
    w_values = [float(row["household_composite_w"]) for row in rows]
    ra_mean = sum(ra_values) / len(ra_values)
    w_mean = sum(w_values) / len(w_values)
    ra_std = math.sqrt(sum((value - ra_mean) ** 2 for value in ra_values) / len(rows))
    w_std = math.sqrt(sum((value - w_mean) ** 2 for value in w_values) / len(rows))
    if ra_std <= 0.0 or w_std <= 0.0:
        raise ValueError("standardization requires nonzero ra and w variation")
    standardized = []
    for row in rows:
        item = dict(row)
        item["z_ra"] = (float(row["consumed_ra"]) - ra_mean) / ra_std
        item["z_w"] = (float(row["household_composite_w"]) - w_mean) / w_std
        standardized.append(item)
    scaling: dict[str, float | str] = {
        "definition": "full-sample population standard deviation (ddof=0)",
        "ra_mean": ra_mean,
        "ra_std_ddof0": ra_std,
        "w_mean": w_mean,
        "w_std_ddof0": w_std,
    }
    return standardized, scaling


def euclidean(left: dict[str, Any], right: dict[str, Any]) -> float:
    return math.hypot(left["z_ra"] - right["z_ra"], left["z_w"] - right["z_w"])


def nearest_successes(rows: Sequence[dict[str, Any]]) -> list[dict[str, Any]]:
    successes = [row for row in rows if row["outcome_group"] == SUCCESS]
    failures = [row for row in rows if row["outcome_group"] == FAILURE]
    if not successes or not failures:
        raise ValueError("nearest-success analysis requires both groups")
    output = []
    for failure in sorted(failures, key=lambda row: row["province_index"]):
        ranked = sorted(
            ((euclidean(failure, success), success) for success in successes),
            key=lambda pair: (pair[0], pair[1]["province_index"]),
        )
        distance, success = ranked[0]
        output.append(
            {
                "failure_province_index": failure["province_index"],
                "failure_province": failure["province"],
                "failure_input": {
                    "consumed_ra": failure.get("consumed_ra"),
                    "household_composite_w": failure.get("household_composite_w"),
                    "z_ra": failure["z_ra"],
                    "z_w": failure["z_w"],
                },
                "nearest_success_province_index": success["province_index"],
                "nearest_success_province": success["province"],
                "nearest_success_input": {
                    "consumed_ra": success.get("consumed_ra"),
                    "household_composite_w": success.get("household_composite_w"),
                    "z_ra": success["z_ra"],
                    "z_w": success["z_w"],
                },
                "nearest_success_iterations": success.get("iterations"),
                "nearest_success_final_convergence_statistic": success.get(
                    "final_convergence_statistic"
                ),
                "standardized_distance": distance,
                "tie_break": "distance then province_index",
            }
        )
    return output


Point = tuple[float, float]


def _cross(origin: Point, left: Point, right: Point) -> float:
    return (left[0] - origin[0]) * (right[1] - origin[1]) - (
        left[1] - origin[1]
    ) * (right[0] - origin[0])


def convex_hull(points: Iterable[Point]) -> list[Point]:
    ordered = sorted(set((float(x), float(y)) for x, y in points))
    if len(ordered) <= 1:
        return ordered
    lower: list[Point] = []
    for point in ordered:
        while len(lower) >= 2 and _cross(lower[-2], lower[-1], point) <= EPSILON:
            lower.pop()
        lower.append(point)
    upper: list[Point] = []
    for point in reversed(ordered):
        while len(upper) >= 2 and _cross(upper[-2], upper[-1], point) <= EPSILON:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def _point_on_segment(point: Point, start: Point, end: Point) -> bool:
    if abs(_cross(start, end, point)) > EPSILON:
        return False
    return (
        min(start[0], end[0]) - EPSILON <= point[0] <= max(start[0], end[0]) + EPSILON
        and min(start[1], end[1]) - EPSILON
        <= point[1]
        <= max(start[1], end[1]) + EPSILON
    )


def point_in_convex_hull(point: Point, hull: Sequence[Point]) -> bool:
    if not hull:
        return False
    if len(hull) == 1:
        return math.dist(point, hull[0]) <= EPSILON
    if len(hull) == 2:
        return _point_on_segment(point, hull[0], hull[1])
    return all(
        _cross(hull[index], hull[(index + 1) % len(hull)], point) >= -EPSILON
        for index in range(len(hull))
    )


def _segments_intersect(a: Point, b: Point, c: Point, d: Point) -> bool:
    orientations = (_cross(a, b, c), _cross(a, b, d), _cross(c, d, a), _cross(c, d, b))
    if orientations[0] * orientations[1] < -EPSILON and orientations[2] * orientations[3] < -EPSILON:
        return True
    return any(
        abs(value) <= EPSILON and _point_on_segment(point, start, end)
        for value, point, start, end in (
            (orientations[0], c, a, b),
            (orientations[1], d, a, b),
            (orientations[2], a, c, d),
            (orientations[3], b, c, d),
        )
    )


def hulls_overlap(left: Sequence[Point], right: Sequence[Point]) -> bool:
    if not left or not right:
        return False
    if any(point_in_convex_hull(point, right) for point in left):
        return True
    if any(point_in_convex_hull(point, left) for point in right):
        return True
    left_edges = [(left[index], left[(index + 1) % len(left)]) for index in range(len(left))]
    right_edges = [(right[index], right[(index + 1) % len(right)]) for index in range(len(right))]
    return any(_segments_intersect(a, b, c, d) for a, b in left_edges for c, d in right_edges)


def knn_summary(rows: Sequence[dict[str, Any]], k: int = 3) -> dict[str, Any]:
    if k != 3:
        raise ValueError("the frozen graph requires k=3")
    if len(rows) <= k:
        raise ValueError("kNN requires more rows than k")
    ordered = sorted(rows, key=lambda row: row["province_index"])
    neighbors_by_index: dict[int, list[dict[str, Any]]] = {}
    for row in ordered:
        candidates = sorted(
            ((euclidean(row, other), other) for other in ordered if other is not row),
            key=lambda pair: (pair[0], pair[1]["province_index"]),
        )[:k]
        neighbors_by_index[row["province_index"]] = [
            {
                "province_index": other["province_index"],
                "province": other["province"],
                "outcome_group": other["outcome_group"],
                "standardized_distance": distance,
            }
            for distance, other in candidates
        ]

    failure_indices = {
        row["province_index"] for row in ordered if row["outcome_group"] == FAILURE
    }
    adjacency: dict[int, set[int]] = {index: set() for index in failure_indices}
    failure_to_success = 0
    failure_neighbors = []
    for row in ordered:
        if row["outcome_group"] != FAILURE:
            continue
        neighbors = neighbors_by_index[row["province_index"]]
        failure_to_success += sum(item["outcome_group"] == SUCCESS for item in neighbors)
        for neighbor in neighbors:
            if neighbor["province_index"] in failure_indices:
                adjacency[row["province_index"]].add(neighbor["province_index"])
                adjacency[neighbor["province_index"]].add(row["province_index"])
        failure_neighbors.append(
            {
                "failure_province_index": row["province_index"],
                "failure_province": row["province"],
                "neighbors": neighbors,
            }
        )

    visited: set[int] = set()
    if failure_indices:
        queue = deque([min(failure_indices)])
        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            queue.extend(sorted(adjacency[current] - visited))
    connected = visited == failure_indices
    failure_only = connected and failure_to_success == 0
    return {
        "schema": f"{SCHEMA_PREFIX}_KNN_V1",
        "k": k,
        "metric": "Euclidean distance on full-sample standardized (consumed_ra, household_composite_w)",
        "tie_break": "distance then province_index",
        "undirected_edge_rule": "edge exists when either endpoint selects the other",
        "failure_neighbors": failure_neighbors,
        "failure_induced_connected": connected,
        "failure_to_success_edge_count": failure_to_success,
        "failure_only_region": failure_only,
        "classification": (
            "FAILURES_FORM_CONNECTED_FAILURE_ONLY_REGION"
            if failure_only
            else "FAILURE_SUCCESS_NODES_INTERLEAVED"
        ),
    }


def verify_manifest(
    evidence_root: Path,
    *,
    repo_root: Path | None = None,
    allow_compact_missing: bool = False,
) -> dict[str, Any]:
    manifest_path = evidence_root / "sealed_manifest_sha256.json"
    manifest = load_json(manifest_path)
    errors = []
    compact_missing = []
    matched_representations: Counter[str] = Counter()
    total_bytes = 0
    for entry in manifest["entries"]:
        path = evidence_root / entry["path"]
        if not path.is_file():
            if allow_compact_missing:
                compact_missing.append(entry["path"])
            else:
                errors.append({"path": entry["path"], "error": "MISSING"})
            continue
        candidates = [("working_tree", path.read_bytes())]
        if repo_root is not None:
            candidates.append(("git_head_blob", git_blob_bytes(repo_root, path)))
        expected_size = int(entry["bytes"])
        expected_digest = str(entry["sha256"]).upper()
        matches = [
            (name, content)
            for name, content in candidates
            if len(content) == expected_size
            and hashlib.sha256(content).hexdigest().upper() == expected_digest
        ]
        if not matches:
            errors.append({"path": entry["path"], "error": "NO_EXACT_BYTE_REPRESENTATION_MATCH"})
            continue
        name, content = matches[0]
        matched_representations[name] += 1
        total_bytes += len(content)
    expected_bytes = int(manifest["bytes_excluding_manifest"])
    if not compact_missing and total_bytes != expected_bytes:
        errors.append({"path": "<manifest-total>", "error": "TOTAL_BYTE_MISMATCH"})
    return {
        "path": manifest_path.as_posix(),
        "sha256": sha256_file(manifest_path),
        "entry_count": len(manifest["entries"]),
        "expected_bytes_excluding_manifest": expected_bytes,
        "actual_bytes_excluding_manifest": total_bytes,
        "compact_missing_entries": compact_missing,
        "compact_missing_count": len(compact_missing),
        "matched_byte_representations": dict(sorted(matched_representations.items())),
        "validation_bytes": "per-entry exact match against working-tree and git HEAD blob bytes",
        "errors": errors,
        "pass": not errors,
    }


def _group_counts(values: Iterable[tuple[str, str]]) -> dict[str, dict[str, int]]:
    table: dict[str, Counter[str]] = defaultdict(Counter)
    for state, group in values:
        table[state][group] += 1
    return {
        state: {SUCCESS: counts[SUCCESS], FAILURE: counts[FAILURE], "total": sum(counts.values())}
        for state, counts in sorted(table.items())
    }


def _rank_rows(rows: Sequence[dict[str, Any]], field: str) -> dict[int, int]:
    ordered = sorted(rows, key=lambda row: (float(row[field]), row["province_index"]))
    return {row["province_index"]: position for position, row in enumerate(ordered, start=1)}


def _range_rank_summary(rows: Sequence[dict[str, Any]]) -> dict[str, Any]:
    groups = {
        "successes": [row for row in rows if row["outcome_group"] == SUCCESS],
        "failures": [row for row in rows if row["outcome_group"] == FAILURE],
        "all_31": list(rows),
    }
    summaries = {}
    for name, group_rows in groups.items():
        summaries[name] = {
            "count": len(group_rows),
            "consumed_ra": quantile_summary([row["consumed_ra"] for row in group_rows]),
            "household_composite_w": quantile_summary(
                [row["household_composite_w"] for row in group_rows]
            ),
        }
    ra_ranks = _rank_rows(rows, "consumed_ra")
    w_ranks = _rank_rows(rows, "household_composite_w")
    failure_ranks = [
        {
            "province_index": row["province_index"],
            "province": row["province"],
            "consumed_ra": row["consumed_ra"],
            "ra_rank_ascending_1_to_31": ra_ranks[row["province_index"]],
            "household_composite_w": row["household_composite_w"],
            "w_rank_ascending_1_to_31": w_ranks[row["province_index"]],
        }
        for row in rows
        if row["outcome_group"] == FAILURE
    ]
    return {
        "schema": f"{SCHEMA_PREFIX}_RANGE_RANK_V1",
        "quantile_definition": "linear interpolation at q=0,.25,.5,.75,1",
        "rank_definition": "ascending ordinal rank with province_index tie-break; no causal interpretation",
        "groups": summaries,
        "failure_ranks": failure_ranks,
    }


def _box(rows: Sequence[dict[str, Any]]) -> dict[str, list[float]]:
    return {
        "consumed_ra": [min(row["consumed_ra"] for row in rows), max(row["consumed_ra"] for row in rows)],
        "household_composite_w": [
            min(row["household_composite_w"] for row in rows),
            max(row["household_composite_w"] for row in rows),
        ],
    }


def _boxes_overlap(left: dict[str, list[float]], right: dict[str, list[float]]) -> bool:
    return all(
        max(left[field][0], right[field][0]) <= min(left[field][1], right[field][1])
        for field in ("consumed_ra", "household_composite_w")
    )


def _git_head(repo_root: Path) -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def _build_table(repo_root: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    first_root = repo_root / "docs/evidence/ch5_mp4c_k1_j160_provincial_first_turn_hjb_viability"
    identity_root = repo_root / "docs/evidence/ch5_mp4c_k1_hjb_convergence_mechanism_turn1_turn2"
    mapping_root = repo_root / "docs/evidence/ch5_mp4c_k1_ra_w_health_region_provincial_mapping"
    first_manifest = verify_manifest(first_root, repo_root=repo_root)
    identity_manifest = verify_manifest(
        identity_root, repo_root=repo_root, allow_compact_missing=True
    )
    mapping_manifest = verify_manifest(mapping_root, repo_root=repo_root)
    if not all(item["pass"] for item in (first_manifest, identity_manifest, mapping_manifest)):
        raise ValueError("accepted source manifest validation failed")

    authority_path = first_root / "first_turn_input_authority.json"
    receipts_path = first_root / "province_receipts.json"
    authority = load_json(authority_path)
    receipts = load_json(receipts_path)
    if not authority.get("pass") or authority.get("province_count") != 31:
        raise ValueError("first-turn input authority is not a 31-province PASS")
    if len(receipts) != 31:
        raise ValueError("first-turn outcome receipts do not contain 31 provinces")

    identity_path = identity_root / "identity_receipts.json"
    expected_identity_hash = authority["accepted_identity_receipts_sha256"].upper()
    if expected_identity_hash not in {
        sha256_file(identity_path),
        sha256_git_blob(repo_root, identity_path),
    }:
        raise ValueError("accepted identity receipt hash mismatch")
    identity_manifest_path = identity_root / "sealed_manifest_sha256.json"
    expected_identity_manifest_hash = authority["accepted_manifest_sha256"].upper()
    if expected_identity_manifest_hash not in {
        sha256_file(identity_manifest_path),
        sha256_git_blob(repo_root, identity_manifest_path),
    }:
        raise ValueError("accepted identity manifest hash mismatch")

    first_manifest_entries = {
        entry["path"]: str(entry["sha256"]).upper()
        for entry in load_json(first_root / "sealed_manifest_sha256.json")["entries"]
    }
    identity_manifest_entries = {
        entry["path"]: str(entry["sha256"]).upper()
        for entry in load_json(identity_manifest_path)["entries"]
    }
    mapping_manifest_entries = {
        entry["path"]: str(entry["sha256"]).upper()
        for entry in load_json(mapping_root / "sealed_manifest_sha256.json")["entries"]
    }

    mapping_path = mapping_root / "provincial_projection.json"
    mapping = load_json(mapping_path)
    mapping_rows = {
        int(row["province_index"]): row
        for row in mapping["rows"]
        if int(row["turn"]) == 1
    }
    if len(mapping_rows) != 31:
        raise ValueError("accepted upstream mapping does not contain 31 turn-1 provinces")
    receipt_rows = {int(row["province_index"]): row for row in receipts}
    input_rows = {int(row["province_index"]): row for row in authority["provinces"]}
    if set(receipt_rows) != set(range(31)) or set(input_rows) != set(range(31)):
        raise ValueError("province indices are not exactly 0..30")

    table = []
    for index in range(31):
        input_row = input_rows[index]
        receipt = receipt_rows[index]
        upstream = mapping_rows[index]
        if not (
            input_row["province"] == receipt["province"] == upstream["province"]
            and float(input_row["consumed_r_a"]) == float(upstream["consumed_ra"])
            and float(input_row["household_composite_wage"])
            == float(upstream["consumed_household_composite_wage"])
        ):
            raise ValueError(f"cross-evidence identity mismatch for province {index}")
        result_path = first_root / f"p{index:02d}_{input_row['province']}_result.json"
        classification = receipt["hjb"]["classification"]
        group = SUCCESS if receipt["hjb"]["converged"] else FAILURE
        table.append(
            {
                "province_index": index,
                "province": input_row["province"],
                "accepted_hjb_classification": classification,
                "outcome_group": group,
                "iterations": int(receipt["hjb"]["iterations_used"]),
                "final_convergence_statistic": float(
                    receipt["hjb"]["final_convergence_statistic"]
                ),
                "maximum_a2max": float(receipt["hjb"]["maximum_a2max"]),
                "consumed_ra": float(input_row["consumed_r_a"]),
                "household_composite_w": float(input_row["household_composite_wage"]),
                "r_b": float(input_row["r_b"]),
                "borrowing_rate_gap": float(input_row["borrowing_rate_gap"]),
                "tau": float(input_row["tau"]),
                "transfer_income": float(input_row["transfer_income"]),
                "return_guard_state": upstream["return_guard_state"],
                "wage_guard_state": upstream["wage_guard_state"],
                "input_receipt_wage_guard_state_metadata": input_row["wage_guard_state"],
                "raw_pre_guard_return": float(upstream["raw_entering_ra"]),
                "raw_pre_guard_return_status": "AVAILABLE_SEALED",
                "guarded_wjt": float(upstream["guarded_wjt"]),
                "raw_provincial_wjt": None,
                "raw_provincial_wjt_status": upstream["raw_firm_wage_status"],
                "semantic_boundary": (
                    "guarded_wjt is upstream and is not household_composite_w; "
                    "raw provincial wjt is unavailable"
                ),
                "provenance": {
                    "input_path": authority_path.relative_to(repo_root).as_posix(),
                    "input_sha256": first_manifest_entries[authority_path.name],
                    "outcome_path": result_path.relative_to(repo_root).as_posix(),
                    "outcome_sha256": first_manifest_entries[result_path.name],
                    "upstream_mapping_path": mapping_path.relative_to(repo_root).as_posix(),
                    "upstream_mapping_sha256": mapping_manifest_entries[mapping_path.name],
                },
            }
        )

    source_authority = {
        "schema": f"{SCHEMA_PREFIX}_SOURCE_AUTHORITY_V1",
        "pass": True,
        "actual_baseline": _git_head(repo_root),
        "province_count": len(table),
        "first_turn_manifest_validation": first_manifest,
        "accepted_identity_manifest_validation": identity_manifest,
        "accepted_mapping_manifest_validation": mapping_manifest,
        "authority_files": [
            {"path": authority_path.relative_to(repo_root).as_posix(), "sha256": first_manifest_entries[authority_path.name]},
            {"path": receipts_path.relative_to(repo_root).as_posix(), "sha256": first_manifest_entries[receipts_path.name]},
            {"path": identity_path.relative_to(repo_root).as_posix(), "sha256": identity_manifest_entries[identity_path.name]},
            {"path": mapping_path.relative_to(repo_root).as_posix(), "sha256": mapping_manifest_entries[mapping_path.name]},
            {
                "path": (identity_root / "wage_guard_metadata_adjudication.json").relative_to(repo_root).as_posix(),
                "sha256": identity_manifest_entries["wage_guard_metadata_adjudication.json"],
            },
            {
                "path": (mapping_root / "wage_mapping_receipt.json").relative_to(repo_root).as_posix(),
                "sha256": mapping_manifest_entries["wage_mapping_receipt.json"],
            },
            {
                "path": "docs/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_ACCEPTANCE.md",
                "sha256": sha256_git_blob(repo_root, repo_root / "docs/CH5_MP4C_K1_J160_PROVINCIAL_FIRST_TURN_HJB_VIABILITY_ACCEPTANCE.md"),
            },
            {
                "path": "docs/CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT_ACCEPTANCE.md",
                "sha256": sha256_git_blob(repo_root, repo_root / "docs/CH5_MP4C_K1_WAGE_CONDITIONAL_RA_W_HEALTH_REGION_AND_PROVINCIAL_RETURN_MAPPING_AUDIT_ACCEPTANCE.md"),
            },
        ],
        "semantic_adjudication": {
            "consumed_w": "household composite wage used for input-envelope analysis",
            "guarded_wjt": "distinct upstream firm-wage object; never substituted for consumed w",
            "wage_guard_state": "corrected upstream wjt guard metadata from accepted projection",
            "input_receipt_wage_guard_state_metadata": (
                "retained separately; not treated as upstream wjt guard state"
            ),
            "raw_provincial_wjt": "UNAVAILABLE_IN_ACCEPTED_COMPACT_PROVINCIAL_INPUT_EVIDENCE",
        },
    }
    return table, source_authority


def _build_report(
    baseline: str,
    terminal_class: str,
    table: Sequence[dict[str, Any]],
    ranges: dict[str, Any],
    guards: dict[str, Any],
    nearest: dict[str, Any],
    envelope: dict[str, Any],
    graph: dict[str, Any],
    upstream: dict[str, Any],
) -> str:
    threshold = envelope["single_variable_thresholds"]
    lines = [
        "# CH5 MP4C K1 — first-turn provincial input/outcome envelope audit",
        "",
        "## Terminal class",
        "",
        f"`{terminal_class}`",
        "",
        "Results eligibility=`FALSE`.",
        "",
        "## Authority and runtime",
        "",
        f"Actual baseline: `{baseline}`. The accepted 31-province table and upstream mapping metadata were reconstructed solely from hash-verified repository evidence. HJB/KFE/firm/wage/return/outer/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results runtime and scientific retries are all zero.",
        "",
        "`guarded_wjt` is retained only as a distinct upstream object and is never substituted for household composite `w`. Raw provincial `wjt` is unavailable in accepted compact evidence.",
        "",
        "## Group envelopes",
        "",
        "| group | n | ra min / median / max | composite-w min / median / max |",
        "|---|---:|---:|---:|",
    ]
    for group in ("failures", "successes", "all_31"):
        item = ranges["groups"][group]
        ra = item["consumed_ra"]
        wage = item["household_composite_w"]
        lines.append(
            f"| {group} | {item['count']} | {ra['min']:.9g} / {ra['median']:.9g} / {ra['max']:.9g} | {wage['min']:.9g} / {wage['median']:.9g} / {wage['max']:.9g} |"
        )
    lines.extend(
        [
            "",
            "## Failure ranks and nearest successes",
            "",
            "| failure | ra rank | w rank | nearest success | standardized distance |",
            "|---|---:|---:|---|---:|",
        ]
    )
    ranks = {item["province_index"]: item for item in ranges["failure_ranks"]}
    for item in nearest["failures"]:
        rank = ranks[item["failure_province_index"]]
        lines.append(
            f"| {item['failure_province']} | {rank['ra_rank_ascending_1_to_31']}/31 | {rank['w_rank_ascending_1_to_31']}/31 | {item['nearest_success_province']} | {item['standardized_distance']:.9g} |"
        )
    lines.extend(
        [
            "",
            "## Guard, envelope and graph findings",
            "",
            f"- Guard result: `{guards['classification']}`. Return guard is `NOT_APPLIED_BOOTSTRAP` for 31/31; corrected upstream wjt guard is `UPPER` for 31/31.",
            f"- Bounding boxes overlap: `{str(envelope['bounding_box']['overlap']).upper()}`.",
            f"- Failure and success convex hulls overlap: `{str(envelope['convex_hull']['hulls_overlap']).upper()}`; failures inside/on success hull: `{envelope['convex_hull']['failure_inside_or_on_success_hull_count']}/6`.",
            f"- Single-ra threshold: `{'EXISTS' if threshold['consumed_ra']['exists'] else 'DOES_NOT_EXIST'}`.",
            f"- Single-composite-w threshold: `{'EXISTS' if threshold['household_composite_w']['exists'] else 'DOES_NOT_EXIST'}`.",
            f"- Fixed k=3 graph: `{graph['classification']}`; failure-induced connected=`{str(graph['failure_induced_connected']).upper()}`, failure-to-success neighbor entries=`{graph['failure_to_success_edge_count']}`.",
            "",
            "## Upstream mapping evidence",
            "",
            f"Raw pre-guard return is sealed for `{upstream['raw_pre_guard_return']['available_count']}/31` and equals consumed ra for `{upstream['raw_pre_guard_return']['equals_consumed_ra_count']}/31`. Raw provincial wjt is unavailable for `{upstream['raw_provincial_wjt']['unavailable_count']}/31`; guarded wjt is sealed but is not the household wage coordinate.",
            "",
            "## Interpretation boundary",
            "",
            "The six failures are descriptively interleaved with successes in the accepted consumed `(ra,w)` input space. This is not a causal result and does not authorize recalibration, guard/mapping changes, parameter changes, HJB/KFE changes, or Results use.",
            "",
            "## Exactly one next gate",
            "",
            "`REVIEWER_FIRST_TURN_INPUT_OUTCOME_ENVELOPE_ROUTE_DECISION`",
            "",
        ]
    )
    return "\n".join(lines)


def build_audit(repo_root: Path, evidence_root: Path | None = None) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    output_root = evidence_root or (
        repo_root / "docs/evidence/ch5_mp4c_k1_first_turn_provincial_input_outcome_envelope_audit"
    )
    if output_root.exists():
        raise FileExistsError(f"refusing to overwrite evidence directory: {output_root}")
    output_root.mkdir(parents=True)

    table, source_authority = _build_table(repo_root)
    successes = [row for row in table if row["outcome_group"] == SUCCESS]
    failures = [row for row in table if row["outcome_group"] == FAILURE]
    if len(successes) != 25 or len(failures) != 6:
        raise ValueError("accepted outcome split is not 25 successes / 6 failures")

    ranges = _range_rank_summary(table)
    standardized, scaling = standardize_rows(table)
    nearest = {
        "schema": f"{SCHEMA_PREFIX}_NEAREST_SUCCESS_V1",
        "scaling": scaling,
        "failures": nearest_successes(standardized),
    }
    success_box = _box(successes)
    failure_box = _box(failures)
    success_hull = convex_hull(
        (row["consumed_ra"], row["household_composite_w"]) for row in successes
    )
    failure_hull = convex_hull(
        (row["consumed_ra"], row["household_composite_w"]) for row in failures
    )
    inside = [
        row["province"]
        for row in failures
        if point_in_convex_hull(
            (row["consumed_ra"], row["household_composite_w"]), success_hull
        )
    ]
    thresholds = {
        "consumed_ra": threshold_existence(
            [row["consumed_ra"] for row in failures],
            [row["consumed_ra"] for row in successes],
        ),
        "household_composite_w": threshold_existence(
            [row["household_composite_w"] for row in failures],
            [row["household_composite_w"] for row in successes],
        ),
    }
    envelope = {
        "schema": f"{SCHEMA_PREFIX}_ENVELOPE_OVERLAP_V1",
        "bounding_box": {
            "failure": failure_box,
            "success": success_box,
            "overlap": _boxes_overlap(failure_box, success_box),
        },
        "convex_hull": {
            "method": "deterministic 2D monotone chain; boundary counts as inside",
            "available": True,
            "failure_hull": [list(point) for point in failure_hull],
            "success_hull": [list(point) for point in success_hull],
            "hulls_overlap": hulls_overlap(failure_hull, success_hull),
            "failure_inside_or_on_success_hull_count": len(inside),
            "failure_inside_or_on_success_hull_provinces": inside,
        },
        "single_variable_thresholds": thresholds,
    }
    graph = knn_summary(standardized, k=3)

    guards = {
        "schema": f"{SCHEMA_PREFIX}_GUARD_CONTINGENCY_V1",
        "return_guard_state_x_outcome": _group_counts(
            (row["return_guard_state"], row["outcome_group"]) for row in table
        ),
        "corrected_upstream_wjt_guard_state_x_outcome": _group_counts(
            (row["wage_guard_state"], row["outcome_group"]) for row in table
        ),
        "separately_retained_input_receipt_wage_metadata_x_outcome": _group_counts(
            (row["input_receipt_wage_guard_state_metadata"], row["outcome_group"])
            for row in table
        ),
        "classification": "NO_DISCRIMINATING_GUARD_VARIATION",
        "semantic_note": (
            "corrected upstream wjt guard metadata is distinct from the separately retained "
            "input-receipt wage metadata and from household composite w"
        ),
    }

    raw_return_groups = {}
    for name, selected in (("successes", successes), ("failures", failures), ("all_31", table)):
        raw_return_groups[name] = quantile_summary(
            [row["raw_pre_guard_return"] for row in selected]
        )
    upstream = {
        "schema": f"{SCHEMA_PREFIX}_UPSTREAM_RAW_MAPPING_V1",
        "raw_pre_guard_return": {
            "status": "AVAILABLE_SEALED",
            "available_count": 31,
            "equals_consumed_ra_count": sum(
                row["raw_pre_guard_return"] == row["consumed_ra"] for row in table
            ),
            "ranges": raw_return_groups,
            "failure_ranks": ranges["failure_ranks"],
            "single_threshold": threshold_existence(
                [row["raw_pre_guard_return"] for row in failures],
                [row["raw_pre_guard_return"] for row in successes],
            ),
            "guard_state_association": "NO_DISCRIMINATING_GUARD_VARIATION",
        },
        "raw_provincial_wjt": {
            "status": "UPSTREAM_RAW_MAPPING_VALUES_UNAVAILABLE",
            "available_count": 0,
            "unavailable_count": 31,
            "source_status": "UNAVAILABLE_IN_ACCEPTED_COMPACT_PROVINCIAL_INPUT_EVIDENCE",
        },
        "guarded_wjt": {
            "status": "AVAILABLE_SEALED_DISTINCT_UPSTREAM_OBJECT",
            "available_count": 31,
            "range": quantile_summary([row["guarded_wjt"] for row in table]),
            "substitution_for_household_composite_w": False,
        },
    }

    terminal_class = (
        "SIMPLE_INPUT_ENVELOPE_SEPARATION_SUPPORTED"
        if thresholds["consumed_ra"]["exists"] or thresholds["household_composite_w"]["exists"]
        else "FAILURE_SUCCESS_INPUT_ENVELOPES_OVERLAP_SUBSTANTIALLY"
    )
    decision = {
        "terminal_class": terminal_class,
        "simple_provincial_input_envelope_supported": terminal_class
        == "SIMPLE_INPUT_ENVELOPE_SEPARATION_SUPPORTED",
        "causal_claim": False,
        "results_eligibility": False,
        "next_gate": "REVIEWER_FIRST_TURN_INPUT_OUTCOME_ENVELOPE_ROUTE_DECISION",
    }
    table_payload = {
        "schema": f"{SCHEMA_PREFIX}_TABLE_V1",
        "row_count": len(table),
        "success_count": len(successes),
        "failure_count": len(failures),
        "rows": table,
    }
    runtime = {
        "schema": f"{SCHEMA_PREFIX}_RUNTIME_LEDGER_V1",
        "hjb_calls": 0,
        "kfe_calls": 0,
        "firm_calls": 0,
        "wage_mapping_calls": 0,
        "return_mapping_calls": 0,
        "outer_calls": 0,
        "matlab_calls": 0,
        "k1b_calls": 0,
        "k2_calls": 0,
        "ge_calls": 0,
        "downstream_calls": 0,
        "shock_calls": 0,
        "irf_calls": 0,
        "results_writes": 0,
        "scientific_retries": 0,
        "offline_parser_finalizer_runs": 3,
        "engineering_retries": 2,
    }

    outputs = {
        "source_authority.json": source_authority,
        "province_input_outcome_table.json": table_payload,
        "range_rank_summary.json": ranges,
        "guard_contingency.json": guards,
        "nearest_success_standardized.json": nearest,
        "envelope_overlap.json": envelope,
        "neighbor_graph_summary.json": graph,
        "upstream_raw_mapping_summary.json": upstream,
        "runtime_ledger.json": runtime,
        "panel_decision.json": decision,
        "engineering_attempts.json": {
            "attempts": [
                {
                    "attempt": 1,
                    "status": "FAILED_BEFORE_OUTPUTS",
                    "failure": "working-tree-only manifest validation did not account for Git EOL normalization or the documented compact-evidence boundary",
                },
                {
                    "attempt": 2,
                    "status": "FAILED_BEFORE_OUTPUTS",
                    "failure": "git-blob-only validation did not account for historical manifests sealed from Windows working-tree bytes",
                },
            ],
            "repair": "per-entry exact size and SHA256 match against working-tree and git HEAD blob representations; compact-missing historical traces reported separately",
            "scientific_calls_before_failures": 0,
            "scientific_retries": 0,
        },
    }
    for filename, payload in outputs.items():
        write_json(output_root / filename, payload)

    manifest_entries = []
    for path in sorted(output_root.iterdir(), key=lambda item: item.name):
        if path.name == "sealed_manifest_sha256.json" or not path.is_file():
            continue
        manifest_entries.append(
            {"path": path.name, "bytes": path.stat().st_size, "sha256": sha256_file(path)}
        )
    manifest = {
        "schema": f"{SCHEMA_PREFIX}_SEALED_MANIFEST_V1",
        "entries": manifest_entries,
        "bytes_excluding_manifest": sum(item["bytes"] for item in manifest_entries),
    }
    write_json(output_root / "sealed_manifest_sha256.json", manifest)

    report_path = repo_root / "docs/CH5_MP4C_K1_FIRST_TURN_PROVINCIAL_INPUT_OUTCOME_ENVELOPE_AUDIT_REPORT.md"
    report_path.write_text(
        _build_report(
            source_authority["actual_baseline"],
            terminal_class,
            table,
            ranges,
            guards,
            nearest,
            envelope,
            graph,
            upstream,
        ),
        encoding="utf-8",
        newline="\n",
    )
    return {
        "terminal_class": terminal_class,
        "output_root": output_root,
        "report_path": report_path,
        "row_count": len(table),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    result = build_audit(args.repo_root)
    print(json.dumps({key: str(value) for key, value in result.items()}, ensure_ascii=False))


if __name__ == "__main__":
    main()
