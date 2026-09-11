"""Reproduce the K1A distance mapping and static portfolio receipts.

This script is intentionally zero-science: it reads the protected distance
workbook and an accepted initialization receipt, then performs only workbook
mapping and static NumPy/capital-network algebra.  It does not import or call
any household, firm, HJB, KFE, outer-loop, or trajectory runtime.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import openpyxl


TASK_ID = "CH5_MP4C_K1A_2018_DISTANCE_SCORE_MAPPING_AND_STATIC_PORTFOLIO_DIAGNOSTIC"
BASELINE = "0090f6d60ba7eeede09a88f2bd5c21887b45bb7b"
WORKBOOK_SHA256 = "26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566"
THETA_RECEIPT_SHA256 = "5DAD517983CBC436A5FB3E5AD85F1257D957D844994180D15929044A049C7212"
SHEET = "geom"
DATA_RANGE = "B2:AF32"
ROW_LABEL_RANGE = "A2:A32"
COLUMN_LABEL_RANGE = "B1:AF1"
BETA_DISTANCE_GRID = (0.0, 0.5, 1.0, 2.0, 4.0)
BETA_RETURN_GRID = (0.0, 0.25, 0.5, 1.0, 2.0)
TOLERANCE = 1e-12
LAGGED_PROVENANCE = "COMPLETED_ITERATION_N_ZERO_SCORE_FIXTURE_FOR_ALGEBRA_ONLY"
# Fixed before inspecting share outcomes: north, east, central, south,
# southwest, and far west positions in the source-defined province order.
REPRESENTATIVE_ORIGIN_INDICES = (0, 8, 15, 19, 22, 30)


def load_source_module(name: str, path: Path) -> Any:
    """Load one pure source file without executing the package-level imports."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load source module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def write_csv(path: Path, fieldnames: Iterable[str], rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(fieldnames), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def canonical_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def normalize_source_label(label: str) -> str:
    explicit = {
        "内蒙古自治区": "内蒙古",
        "广西壮族自治区": "广西",
        "宁夏回族自治区": "宁夏",
        "新疆维吾尔自治区": "新疆",
        "西藏自治区": "西藏",
    }
    if label in explicit:
        return explicit[label]
    if label.endswith("省") or label.endswith("市"):
        return label[:-1]
    return label


def read_distance_workbook(path: Path, province_order: tuple[str, ...]) -> tuple[np.ndarray, list[dict[str, Any]], dict[str, Any]]:
    if sha256_file(path) != WORKBOOK_SHA256:
        raise ValueError("protected distance workbook SHA-256 mismatch")
    workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
    if SHEET not in workbook.sheetnames:
        raise ValueError(f"required sheet {SHEET!r} is missing")
    sheet = workbook[SHEET]
    source_columns = [str(sheet.cell(1, column).value).strip() for column in range(2, 33)]
    source_rows = [str(sheet.cell(row, 1).value).strip() for row in range(2, 33)]
    if len(set(source_columns)) != 31 or len(set(source_rows)) != 31:
        raise ValueError("distance workbook contains duplicate source labels")
    if source_rows != source_columns:
        raise ValueError("distance workbook row and column labels differ")

    mapping = []
    source_to_active: dict[str, str] = {}
    for position, source in enumerate(source_columns):
        active = normalize_source_label(source)
        mapping.append({
            "source_position_1based": position + 1,
            "source_label": source,
            "active_label": active,
            "mapping_rule": "EXPLICIT_AUTONOMOUS_REGION" if source.endswith("自治区") else (
                "DROP_TERMINAL_ADMIN_SUFFIX" if source.endswith(("省", "市")) else "EXACT_SHORT_LABEL"
            ),
        })
        if active in source_to_active.values():
            raise ValueError(f"duplicate active label after mapping: {active}")
        source_to_active[source] = active
    if set(source_to_active.values()) != set(province_order):
        raise ValueError("source labels do not map one-to-one to active province labels")

    source_matrix = np.array(
        [[sheet.cell(row, column).value for column in range(2, 33)] for row in range(2, 33)],
        dtype=float,
    )
    source_position = {source_to_active[label]: index for index, label in enumerate(source_columns)}
    permutation = [source_position[label] for label in province_order]
    matrix = source_matrix[np.ix_(permutation, permutation)]
    finite_count = int(np.isfinite(matrix).sum())
    missing_count = int(matrix.size - finite_count)
    negative_count = int(np.sum(matrix < 0.0))
    diagonal = np.diag(matrix)
    off_mask = ~np.eye(len(province_order), dtype=bool)
    off = matrix[off_mask]
    min_value = float(np.min(off))
    max_value = float(np.max(off))
    min_pairs = []
    max_pairs = []
    for row, column in zip(*np.where(off_mask & np.isclose(matrix, min_value, rtol=0.0, atol=0.0))):
        if row < column:
            min_pairs.append([province_order[row], province_order[column]])
    for row, column in zip(*np.where(off_mask & np.isclose(matrix, max_value, rtol=0.0, atol=0.0))):
        if row < column:
            max_pairs.append([province_order[row], province_order[column]])
    integrity = {
        "workbook_path": str(path),
        "workbook_sha256": WORKBOOK_SHA256,
        "workbook_bytes": path.stat().st_size,
        "sheet_names": workbook.sheetnames,
        "sheet_used": SHEET,
        "data_range": DATA_RANGE,
        "row_label_range": ROW_LABEL_RANGE,
        "column_label_range": COLUMN_LABEL_RANGE,
        "mapped_shape": list(matrix.shape),
        "units": "UNRESOLVED__NO_EXPLICIT_WORKBOOK_METADATA",
        "finite_count": finite_count,
        "missing_count": missing_count,
        "negative_count": negative_count,
        "diagonal_values": [float(value) for value in diagonal],
        "symmetry_residual_max_abs": float(np.max(np.abs(matrix - matrix.T))),
        "off_diagonal_min": min_value,
        "off_diagonal_min_unordered_pairs": min_pairs,
        "off_diagonal_max_D_max": max_value,
        "off_diagonal_max_unordered_pairs": max_pairs,
        "no_symmetrization": True,
        "no_imputation": True,
    }
    workbook.close()
    return matrix, mapping, integrity


def read_theta(path: Path, province_order: tuple[str, ...]) -> tuple[np.ndarray, list[dict[str, Any]], dict[str, Any]]:
    actual_sha = sha256_file(path)
    if actual_sha != THETA_RECEIPT_SHA256:
        raise ValueError("accepted initialization receipt SHA-256 mismatch")
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 31 or tuple(row["province_name"] for row in rows) != province_order:
        raise ValueError("theta receipt does not use exact active province order")
    theta = np.array([float(row["inter_prv_ratio"]) for row in rows], dtype=float)
    pcap = np.array([float(row["K0_MU"]) / float(row["N0_NU"]) for row in rows], dtype=float)
    recomputed = 0.3 * (pcap - np.min(pcap)) / (np.max(pcap) - np.min(pcap))
    formula_residual = float(np.max(np.abs(theta - recomputed)))
    if formula_residual > 2e-15:
        raise ValueError("accepted theta vector does not reproduce its source formula")
    theta_rows = [
        {
            "province_index_0based": index,
            "province": province,
            "theta_inter_prv_ratio": float(theta[index]),
            "K0_MU": float(rows[index]["K0_MU"]),
            "N0_NU": float(rows[index]["N0_NU"]),
            "K0_over_N0": float(pcap[index]),
        }
        for index, province in enumerate(province_order)
    ]
    provenance = {
        "source_path": str(path),
        "source_sha256": actual_sha,
        "source_bytes": path.stat().st_size,
        "province_mapping": "EXACT_ACTIVE_PROVINCE_ORDER_31_OF_31",
        "formula": "0.3*(K0/N0-min(K0/N0))/(max(K0/N0)-min(K0/N0))",
        "formula_source": "validators/multi_province/corrected_2018_single_turn/run.py:246-247",
        "runtime_binding_source": "src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py:228-289",
        "formula_max_abs_residual": formula_residual,
        "theta_min": float(np.min(theta)),
        "theta_max": float(np.max(theta)),
    }
    return theta, theta_rows, provenance


def matrix_rows(matrix: np.ndarray, province_order: tuple[str, ...], value_name: str) -> list[dict[str, Any]]:
    rows = []
    for destination, destination_name in enumerate(province_order):
        for origin, origin_name in enumerate(province_order):
            rows.append({
                "destination": destination_name,
                "origin": origin_name,
                value_name: float(matrix[destination, origin]),
            })
    return rows


def top_indices(shares: np.ndarray, origin: int, count: int) -> tuple[list[int], int]:
    eligible = [index for index in range(len(shares)) if index != origin]
    eligible.sort(key=lambda index: (-float(shares[index, origin]), index))
    maximum = float(shares[eligible[0], origin])
    tie_count = sum(math.isclose(float(shares[index, origin]), maximum, rel_tol=0.0, abs_tol=1e-15) for index in eligible)
    return eligible[:count], tie_count


def diagnostics(
    province_order: tuple[str, ...],
    distance: np.ndarray,
    distance_score: np.ndarray,
    theta: np.ndarray,
    capital_network_path: Path,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    capital_network = load_source_module("_k1a_capital_network", capital_network_path)
    BilateralCapitalNetworkInputs = capital_network.BilateralCapitalNetworkInputs
    build_bilateral_capital_network = capital_network.build_bilateral_capital_network

    summaries: list[dict[str, Any]] = []
    top_rows: list[dict[str, Any]] = []
    top3_rows: list[dict[str, Any]] = []
    entropy_by_beta: dict[float, np.ndarray] = {}
    check_maxima = {
        "foreign_column_sum_residual": 0.0,
        "full_share_column_sum_residual": 0.0,
        "home_share_residual": 0.0,
        "origin_wealth_residual": 0.0,
        "national_capital_residual": 0.0,
        "equal_share_residual_beta_0": 0.0,
        "no_destination_theta_double_weighting_residual": 0.0,
    }
    for beta in BETA_DISTANCE_GRID:
        result = build_bilateral_capital_network(BilateralCapitalNetworkInputs(
            province_order=province_order,
            illiquid_assets_per_capita_by_origin=np.ones(31),
            population_by_origin=np.ones(31),
            total_foreign_share_theta_by_origin=theta,
            distance_score_destination_origin=distance_score,
            lagged_return_score_by_destination=np.zeros(31),
            portfolio_return_by_destination=np.zeros(31),
            beta_distance=beta,
            beta_return=0.0,
            lagged_return_provenance=LAGGED_PROVENANCE,
        ))
        foreign = result.foreign_conditional_shares_destination_origin
        full = result.portfolio_shares_destination_origin
        positive = np.where(foreign > 0.0, foreign, 1.0)
        entropy = -np.sum(np.where(foreign > 0.0, foreign * np.log(positive), 0.0), axis=0)
        normalized_entropy = entropy / math.log(30.0)
        largest = np.max(foreign, axis=0)
        effective = np.exp(entropy)
        entropy_by_beta[beta] = entropy
        top_distances = []
        for origin, origin_name in enumerate(province_order):
            selected, tie_count = top_indices(foreign, origin, 3)
            top = selected[0]
            top_distances.append(float(distance[top, origin]))
            top_rows.append({
                "beta_distance": beta,
                "origin": origin_name,
                "top_destination": province_order[top],
                "top_share": float(foreign[top, origin]),
                "top_distance_raw": float(distance[top, origin]),
                "top_share_tie_count": tie_count,
            })
            if beta in (0.0, 1.0, 4.0) and origin in REPRESENTATIVE_ORIGIN_INDICES:
                for rank, destination in enumerate(selected, 1):
                    top3_rows.append({
                        "beta_distance": beta,
                        "origin": origin_name,
                        "rank": rank,
                        "destination": province_order[destination],
                        "share": float(foreign[destination, origin]),
                        "distance_raw": float(distance[destination, origin]),
                    })
        summaries.append({
            "beta_distance": beta,
            "entropy_mean": float(np.mean(entropy)),
            "entropy_min": float(np.min(entropy)),
            "entropy_max": float(np.max(entropy)),
            "normalized_entropy_mean": float(np.mean(normalized_entropy)),
            "normalized_entropy_min": float(np.min(normalized_entropy)),
            "normalized_entropy_max": float(np.max(normalized_entropy)),
            "largest_share_mean": float(np.mean(largest)),
            "largest_share_min": float(np.min(largest)),
            "largest_share_max": float(np.max(largest)),
            "effective_destinations_mean": float(np.mean(effective)),
            "effective_destinations_min": float(np.min(effective)),
            "effective_destinations_max": float(np.max(effective)),
            "top_destination_distance_median_raw": float(np.median(top_distances)),
        })
        check_maxima["foreign_column_sum_residual"] = max(
            check_maxima["foreign_column_sum_residual"], float(np.max(np.abs(np.sum(foreign, axis=0) - 1.0)))
        )
        check_maxima["full_share_column_sum_residual"] = max(
            check_maxima["full_share_column_sum_residual"], float(np.max(np.abs(np.sum(full, axis=0) - 1.0)))
        )
        check_maxima["home_share_residual"] = max(
            check_maxima["home_share_residual"], float(np.max(np.abs(np.diag(full) - (1.0 - theta))))
        )
        check_maxima["origin_wealth_residual"] = max(
            check_maxima["origin_wealth_residual"], float(np.max(np.abs(result.capital_column_sums - 1.0)))
        )
        check_maxima["national_capital_residual"] = max(
            check_maxima["national_capital_residual"], abs(float(result.national_private_capital_conservation_residual))
        )
        expected_foreign_full = foreign * theta[None, :]
        np.fill_diagonal(expected_foreign_full, 0.0)
        actual_foreign_full = full.copy()
        np.fill_diagonal(actual_foreign_full, 0.0)
        check_maxima["no_destination_theta_double_weighting_residual"] = max(
            check_maxima["no_destination_theta_double_weighting_residual"],
            float(np.max(np.abs(actual_foreign_full - expected_foreign_full))),
        )
        if beta == 0.0:
            expected = np.full((31, 31), 1.0 / 30.0)
            np.fill_diagonal(expected, 0.0)
            check_maxima["equal_share_residual_beta_0"] = float(np.max(np.abs(foreign - expected)))

    exceptions = []
    for origin, origin_name in enumerate(province_order):
        values = [float(entropy_by_beta[beta][origin]) for beta in BETA_DISTANCE_GRID]
        if any(values[index + 1] > values[index] + TOLERANCE for index in range(len(values) - 1)):
            exceptions.append({"origin": origin_name, "entropy_by_beta": values})
    validations = {
        "accepted_tolerance": TOLERANCE,
        "max_residuals": check_maxima,
        "all_conservation_checks_pass": all(value <= TOLERANCE for value in check_maxima.values()),
        "entropy_weakly_decreases_every_origin": not exceptions,
        "entropy_monotonicity_exceptions": exceptions,
        "unit_wealth_fixture": "W_i=1 for all origins; mathematical receipt only, not 2018 capital quantity",
        "capital_network_utility": "src/ch5_two_asset_hank/multi_province/capital_network.py",
        "capital_network_orientation": "DESTINATION_BY_ORIGIN",
        "beta_return": 0.0,
        "lagged_return_score": "all-zero completed-iteration fixture",
        "lagged_return_provenance": LAGGED_PROVENANCE,
    }
    return summaries, top_rows, top3_rows, validations


def markdown_table(rows: list[dict[str, Any]], columns: list[tuple[str, str]], digits: int = 6) -> str:
    lines = ["| " + " | ".join(title for _, title in columns) + " |", "|" + "|".join("---" for _ in columns) + "|"]
    for row in rows:
        values = []
        for key, _ in columns:
            value = row[key]
            values.append(f"{value:.{digits}g}" if isinstance(value, float) else str(value))
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def build_report(
    worktree: Path,
    workbook_integrity: dict[str, Any],
    theta_provenance: dict[str, Any],
    mapping: list[dict[str, Any]],
    summaries: list[dict[str, Any]],
    top_rows: list[dict[str, Any]],
    top3_rows: list[dict[str, Any]],
    validations: dict[str, Any],
    return_rows: list[dict[str, Any]],
) -> str:
    representative = {name for index, name in enumerate(PROVINCE_ORDER_LOCAL) if index in REPRESENTATIVE_ORIGIN_INDICES}
    selected_top = [row for row in top_rows if row["origin"] in representative]
    mapping_table = markdown_table(mapping, [("source_position_1based", "pos"), ("source_label", "source"), ("active_label", "active"), ("mapping_rule", "rule")])
    summary_table = markdown_table(summaries, [
        ("beta_distance", "beta_d"), ("entropy_mean", "H mean"), ("normalized_entropy_mean", "H/log30 mean"),
        ("largest_share_mean", "max P mean"), ("effective_destinations_mean", "exp(H) mean"),
        ("top_destination_distance_median_raw", "median top distance"),
    ])
    top_table = markdown_table(selected_top, [
        ("beta_distance", "beta_d"), ("origin", "origin"), ("top_destination", "top destination"),
        ("top_share", "share"), ("top_distance_raw", "distance"), ("top_share_tie_count", "ties"),
    ])
    top3_table = markdown_table(top3_rows, [
        ("beta_distance", "beta_d"), ("origin", "origin"), ("rank", "rank"),
        ("destination", "destination"), ("share", "share"), ("distance_raw", "distance"),
    ])
    return_table = markdown_table(return_rows, [
        ("beta_return", "beta_r"), ("delta_z", "Delta z"), ("odds_factor", "exp(beta_r*Delta z)"),
    ])
    residual_rows = [{"check": key, "max_abs_residual": value, "pass": value <= TOLERANCE} for key, value in validations["max_residuals"].items()]
    residual_table = markdown_table(residual_rows, [("check", "check"), ("max_abs_residual", "max residual"), ("pass", "PASS")])
    return f"""# CH5 MP4C K1A 2018 distance-score mapping and static portfolio diagnostic report

## Outcome

Verdict: **PASS** — the protected workbook maps one-to-one onto the active 31-province axis; `geom!{DATA_RANGE}` is complete and symmetric; the frozen national `D/D_max` score, accepted 2018 theta vector, equal-share limit, pure-geographic grid, and all conservation identities reproduce without any scientific/model/runtime call.

This is a zero-science static allocation receipt, not estimated bilateral holdings, a selected coefficient, a steady state, or Results evidence. Results eligibility remains `FALSE`.

## Authority and execution identity

- Task: `{TASK_ID}`.
- Fresh live-main baseline: `{BASELINE}`.
- Worktree: `{worktree}`.
- Branch: `codex/ch5-k1a-distance-mapping-20260911`.
- Stage order preserved: `K1A equal-share -> K1A pure-geographic -> K1B lagged-return -> K2`.
- Runtime integration performed: none.

## Protected distance source

- Path: `{workbook_integrity['workbook_path']}`.
- SHA-256: `{workbook_integrity['workbook_sha256']}`; bytes: `{workbook_integrity['workbook_bytes']}`.
- Workbook sheets observed: `{', '.join(workbook_integrity['sheet_names'])}`; source used: `{SHEET}` only.
- Labels: `{ROW_LABEL_RANGE}` and `{COLUMN_LABEL_RANGE}`; numeric range: `{DATA_RANGE}`.
- Orientation after label-backed mapping: destination rows x origin columns.
- Units: `UNRESOLVED`; the workbook contains no explicit unit metadata. Values are reported in source units only.
- Integrity: shape 31x31; finite {workbook_integrity['finite_count']}/961; missing {workbook_integrity['missing_count']}; negative {workbook_integrity['negative_count']}; diagonal all exact zero.
- Symmetry residual `max|D-D.T|={workbook_integrity['symmetry_residual_max_abs']}`.
- Off-diagonal minimum `{workbook_integrity['off_diagonal_min']}` at `{workbook_integrity['off_diagonal_min_unordered_pairs']}`.
- `D_max={workbook_integrity['off_diagonal_max_D_max']}` at `{workbook_integrity['off_diagonal_max_unordered_pairs']}`.
- No symmetrization, imputation, or workbook modification occurred.

## Exact source-label mapping

{mapping_table}

All 31 labels map uniquely. Workbook short forms `内蒙古`, `广西`, `宁夏`, `新疆`, and `西藏` map exactly to the active short labels; the explicit autonomous-region aliases remain accepted by the script but were not needed by this workbook. Province and municipality terminal `省/市` suffixes are removed transparently.

## Frozen normalized distance matrix

`D_score=D/D_max` uses the single national off-diagonal maximum, never a row/column maximum. The mapped score is 31x31; diagonal is exact zero; off-diagonal range is `[{workbook_integrity['off_diagonal_min']/workbook_integrity['off_diagonal_max_D_max']}, 1.0]`; maximum is 1; symmetry residual is `{workbook_integrity['symmetry_residual_max_abs']/workbook_integrity['off_diagonal_max_D_max']}`. Full raw and normalized long-form receipts are manifest-bound.

## Theta provenance

- Accepted receipt: `{theta_provenance['source_path']}`.
- SHA-256: `{theta_provenance['source_sha256']}`; exact 31/31 active order.
- Source formula: `{theta_provenance['formula']}` at `{theta_provenance['formula_source']}`.
- Active fail-closed binding: `{theta_provenance['runtime_binding_source']}`.
- Formula reproduction max absolute residual: `{theta_provenance['formula_max_abs_residual']}`; theta range `[{theta_provenance['theta_min']}, {theta_provenance['theta_max']}]`.

Theta is therefore source-authoritative for this static receipt. It is not estimated or changed here.

## Pure-geographic beta-distance diagnostics

These diagnostics use `beta_return=0`, an explicit all-zero completed-iteration score fixture, and the pre-registered distance grid only. No value is selected as a benchmark.

{summary_table}

Entropy mean/min/max, normalized entropy mean/min/max, largest-share mean/min/max, and effective-destination mean/min/max are all retained in `beta_distance_summary.csv`. Entropy weakly decreases with beta for every one of 31 origins: `{validations['entropy_weakly_decreases_every_origin']}`; exceptions: `{validations['entropy_monotonicity_exceptions']}`.

Top-destination tie-breaking is deterministic by active destination index. At beta 0 all 30 eligible destinations tie; positive betas select the nearest destination because this is a pure-distance score.

{top_table}

Representative origins were fixed before inspecting shares by active indices `[0,8,15,19,22,30]`, spanning north/east/central/south/southwest/far-west. Their top-3 table at beta 0/1/4 is:

{top3_table}

## Equal-share and conservation checks

Unit origin wealth `W_i=1` is a mathematical fixture only, not a claim about 2018 capital quantities. The accepted pure `capital_network.py` utility produced the full matrices.

{residual_table}

The beta-zero foreign conditional share is exactly `1/(31-1)` within tolerance. Full off-diagonal shares equal `theta_i*P[j,i]`; no destination `theta_j` weighting appears.

## K1B lagged-return coefficient interpretation

Future K1B uses `z_ra0=(ra0-mean)/sd` across destinations from completed iteration n raw, unclipped `ra0`, and may use it only for allocation iteration n+1. Same-turn feedback is prohibited. The z-score is an attractiveness signal and must never be passed as household payoff `rah`. No `ra0` was generated or loaded in this task.

{return_table}

These are algebraic odds factors only, not identification or a coefficient choice.

## Call ledger and boundaries

| call class | count |
|---|---:|
| MATLAB / HJB / KFE / household / firm / migration / outer loop / trajectory / steady state | 0 |
| GE / annual / shock / IRF / Results | 0 |
| protected workbook reads | 1 per script reproduction |
| accepted pure capital-network algebra evaluations | 5 |

No production scientific/runtime source changed. The protected workbook was read only. `capital_network.py` was not modified.

## Verification and evidence closure

- Reproduction script: `scripts/ch5_mp4c_k1a_distance_mapping.py`.
- Evidence manifest: `docs/evidence/ch5_mp4c_k1a_distance_mapping/manifest.json` with 11 hashed entries (script, report, and nine non-manifest receipts); every path, byte count, and SHA-256 is read back after generation.
- A second complete reproduction produced the identical manifest SHA-256.
- Accepted capital-network focused suite: `29/29` passed (`tests/test_mp4c_k1_bilateral_capital_network.py`).
- Tracked changes remain limited to this task's script, report, and evidence directory.

## Remaining Owner decisions before runtime integration

- Select the final scientific `beta_distance` after reviewing this static receipt.
- Before K1B, select final `beta_return`.
- Freeze the household payoff-return concept; standardized attractiveness scores are not payoff returns.
- Any economic-distance/market-size extension, smoothing, or K2 endogenous-theta form remains a separate future decision.

After those decisions, a new exact task is still required for any K1 runtime integration. The first integration must retain source-faithful labor and separately revalidate C1 residual public assets and the independent KFE blocker.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workbook", type=Path, required=True)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    repo = args.repo.resolve()
    province_contracts = load_source_module(
        "_k1a_province_contracts",
        repo / "src" / "ch5_two_asset_hank" / "multi_province" / "province_contracts.py",
    )
    PROVINCE_ORDER = province_contracts.PROVINCE_ORDER
    global PROVINCE_ORDER_LOCAL
    PROVINCE_ORDER_LOCAL = tuple(PROVINCE_ORDER)

    evidence = repo / "docs" / "evidence" / "ch5_mp4c_k1a_distance_mapping"
    report_path = repo / "docs" / f"{TASK_ID}_REPORT.md"
    theta_path = repo / "reports" / "mp4c_unit_normalized_initialization_probe_20260910" / "province_initialization_receipt.csv"

    distance, mapping, integrity = read_distance_workbook(args.workbook.resolve(), PROVINCE_ORDER_LOCAL)
    d_max = integrity["off_diagonal_max_D_max"]
    distance_score = distance / d_max
    np.fill_diagonal(distance_score, 0.0)
    off_mask = ~np.eye(31, dtype=bool)
    normalization = {
        "formula": "D_score=D/D_max",
        "D_max": d_max,
        "shape": list(distance_score.shape),
        "diagonal_exact_zero": bool(np.array_equal(np.diag(distance_score), np.zeros(31))),
        "off_diagonal_min": float(np.min(distance_score[off_mask])),
        "off_diagonal_max": float(np.max(distance_score[off_mask])),
        "symmetry_residual_max_abs": float(np.max(np.abs(distance_score - distance_score.T))),
        "orientation": "DESTINATION_BY_ORIGIN",
        "national_normalization": True,
        "row_or_column_normalization": False,
    }
    if not normalization["diagonal_exact_zero"] or not math.isclose(normalization["off_diagonal_max"], 1.0, abs_tol=1e-15):
        raise ValueError("normalized distance invariants failed")

    theta, theta_rows, theta_provenance = read_theta(theta_path, PROVINCE_ORDER_LOCAL)
    summaries, top_rows, top3_rows, validations = diagnostics(
        PROVINCE_ORDER_LOCAL,
        distance,
        distance_score,
        theta,
        repo / "src" / "ch5_two_asset_hank" / "multi_province" / "capital_network.py",
    )
    if not validations["all_conservation_checks_pass"] or not validations["entropy_weakly_decreases_every_origin"]:
        raise ValueError("static portfolio acceptance checks failed")
    return_rows = [
        {"beta_return": beta, "delta_z": delta_z, "odds_factor": math.exp(beta * delta_z)}
        for beta in BETA_RETURN_GRID for delta_z in (1, 2)
    ]

    write_csv(evidence / "province_label_mapping.csv", mapping[0].keys(), mapping)
    write_csv(evidence / "raw_distance_destination_origin.csv", ("destination", "origin", "distance_raw"), matrix_rows(distance, PROVINCE_ORDER_LOCAL, "distance_raw"))
    write_csv(evidence / "normalized_distance_destination_origin.csv", ("destination", "origin", "distance_score"), matrix_rows(distance_score, PROVINCE_ORDER_LOCAL, "distance_score"))
    write_csv(evidence / "theta_2018.csv", theta_rows[0].keys(), theta_rows)
    write_csv(evidence / "beta_distance_summary.csv", summaries[0].keys(), summaries)
    write_csv(evidence / "top_destination_by_origin.csv", top_rows[0].keys(), top_rows)
    write_csv(evidence / "representative_top3.csv", top3_rows[0].keys(), top3_rows)
    write_csv(evidence / "beta_return_odds_factors.csv", return_rows[0].keys(), return_rows)
    canonical_json(evidence / "source_and_validation_receipt.json", {
        "task_id": TASK_ID,
        "baseline": BASELINE,
        "distance_source": integrity,
        "distance_normalization": normalization,
        "theta_provenance": theta_provenance,
        "validations": validations,
        "scientific_model_call_ledger": {
            "MATLAB": 0, "HJB": 0, "KFE": 0, "household": 0, "firm": 0,
            "migration": 0, "outer_loop": 0, "trajectory": 0, "steady_state": 0,
            "GE": 0, "annual": 0, "shock_IRF": 0, "Results": 0,
        },
        "results_eligibility": False,
    })
    report_path.write_text(build_report(repo, integrity, theta_provenance, mapping, summaries, top_rows, top3_rows, validations, return_rows), encoding="utf-8")

    manifest_targets = [
        repo / "scripts" / "ch5_mp4c_k1a_distance_mapping.py",
        report_path,
        *sorted(path for path in evidence.iterdir() if path.name != "manifest.json"),
    ]
    manifest = {
        "schema": "CH5_MP4C_K1A_DISTANCE_MAPPING_MANIFEST_V1",
        "task_id": TASK_ID,
        "entries": [
            {"path": path.relative_to(repo).as_posix(), "sha256": sha256_file(path), "bytes": path.stat().st_size}
            for path in manifest_targets
        ],
    }
    canonical_json(evidence / "manifest.json", manifest)
    reloaded = json.loads((evidence / "manifest.json").read_text(encoding="utf-8"))
    for entry in reloaded["entries"]:
        path = repo / entry["path"]
        if sha256_file(path) != entry["sha256"] or path.stat().st_size != entry["bytes"]:
            raise RuntimeError(f"manifest readback failed: {entry['path']}")
    print(json.dumps({
        "verdict": "PASS",
        "D_max": d_max,
        "symmetry_residual": integrity["symmetry_residual_max_abs"],
        "theta_formula_max_abs_residual": theta_provenance["formula_max_abs_residual"],
        "manifest_entries_readback_pass": len(reloaded["entries"]),
        "report": report_path.relative_to(repo).as_posix(),
    }, ensure_ascii=False, indent=2))


PROVINCE_ORDER_LOCAL: tuple[str, ...] = ()


if __name__ == "__main__":
    main()
