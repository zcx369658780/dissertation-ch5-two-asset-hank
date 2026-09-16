"""One-shot executor for the frozen preregistered ten-cell selector panel."""

from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import subprocess
from typing import Any

import numpy as np

from .contracts import AUTHORITY_ID, CorrectedDiagnosticGrid
from .generator import assemble_consumed_drift_generator
from .panel import BoundPanelCell, bind_preregistered_panel
from .selector import SelectorBudget, SelectorResult, select_constrained_policy


EVIDENCE_RELATIVE = Path(
    "reports/ch5_mp4c_2018_kfe_d123_selector_active_equality_reexecution_20260916"
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def _write_json(path: Path, value: Any) -> None:
    text = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text + "\n", encoding="utf-8")
    temporary.replace(path)


def _scientific_code_hashes(repository: Path) -> dict[str, str]:
    namespace = repository / "src/ch5_two_asset_hank/corrected_diagnostic"
    return {
        path.relative_to(repository).as_posix(): _sha256(path)
        for path in sorted(namespace.glob("*.py"))
    }


def _git_head(repository: Path) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repository, text=True
    ).strip()


def _panel_identity(cell: BoundPanelCell) -> dict[str, Any]:
    return {
        "panel_id": cell.panel_id,
        "source_snapshot_id": cell.source_snapshot_id,
        "source_path": cell.source_path,
        "source_sha256": cell.source_sha256,
        "source_bytes": cell.source_bytes,
        "source_row_label": cell.source_row_label,
        "index_b_a_z_zero_based": cell.index,
        "flat_index_f_zero_based": cell.flat_index_f,
        "scalar_binding_path": cell.scalar_binding_path,
        "scalar_binding_sha256": cell.scalar_binding_sha256,
        "scalar_binding_bytes": cell.scalar_binding_bytes,
        "bound_inputs": cell.bound_inputs,
        "selector_cell": asdict(cell.selector_cell),
        "selector_parameters": asdict(cell.selector_parameters),
    }


def _d2_check(cell: BoundPanelCell, result: SelectorResult) -> dict[str, Any]:
    if result.selected is None:
        return {"status": "NOT_RUN_NO_SELECTED_POLICY"}
    grid = CorrectedDiagnosticGrid(
        np.asarray(cell.grid_b), np.asarray(cell.grid_a), np.asarray(cell.grid_z)
    )
    mu_b = np.zeros(grid.shape)
    mu_a = np.zeros(grid.shape)
    mu_b[cell.index] = float(result.selected.g_b)
    mu_a[cell.index] = float(result.selected.g_a)
    assembled = assemble_consumed_drift_generator(grid, mu_b=mu_b, mu_a=mu_a)
    return {
        "status": "D2_ASSEMBLER_ADMISSIBLE",
        "minimum_offdiagonal": assembled.minimum_offdiagonal,
        "diagonal_construction_error": assembled.diagonal_construction_error,
        "max_abs_q_one": assembled.max_abs_q_one,
        "arithmetic_tolerance": assembled.arithmetic_tolerance,
        "max_abs_b_coordinate_error": assembled.max_abs_b_coordinate_error,
        "max_abs_a_coordinate_error": assembled.max_abs_a_coordinate_error,
    }


def persist_selector_receipt_then_check_d2(
    evidence: Path,
    *,
    ordinal: int,
    cell: BoundPanelCell,
    result: SelectorResult,
    budget: SelectorBudget,
    code_freeze_identity: dict[str, Any],
) -> dict[str, Any]:
    """Durably record the complete selector return before invoking strict D2."""

    receipt_path = evidence / f"cell_{ordinal:02d}_{cell.panel_id}.json"
    receipt = {
        "panel_ordinal": ordinal,
        "panel_identity": _panel_identity(cell),
        "code_freeze_identity": code_freeze_identity,
        "selector_result": asdict(result),
        "cumulative_selector_evaluations": budget.selector_evaluations,
        "cumulative_scalar_root_invocations": budget.root_invocations,
        "receipt_persistence_order": "SELECTOR_RECEIPT_DURABLE_BEFORE_D2",
        "d2_assembler_check": {"status": "PENDING"},
        "budget_postconditions": {
            "face_active_set_count_lte_4": result.face_active_set_count <= 4,
            "regime_attempt_count_lte_12": result.regime_attempt_count <= 12,
            "cell_root_invocations_lte_12": result.root_invocations <= 12,
            "cumulative_selector_evaluations_lte_10": budget.selector_evaluations <= 10,
            "cumulative_scalar_root_invocations_lte_120": budget.root_invocations <= 120,
        },
    }
    _write_json(receipt_path, receipt)

    if not all(receipt["budget_postconditions"].values()):
        receipt["d2_assembler_check"] = {
            "status": "NOT_RUN_BUDGET_POSTCONDITION_FAILED"
        }
        _write_json(receipt_path, receipt)
        raise RuntimeError("selector budget postcondition failed before D2")

    try:
        d2 = _d2_check(cell, result)
    except Exception as exc:
        receipt["d2_assembler_check"] = {
            "status": "D2_ASSEMBLER_RAISED",
            "exception_type": type(exc).__name__,
            "exception_message": str(exc),
        }
        _write_json(receipt_path, receipt)
        raise

    receipt["d2_assembler_check"] = d2
    _write_json(receipt_path, receipt)
    return receipt


def _ledger(budget: SelectorBudget, completed: int, terminal: str) -> dict[str, Any]:
    return {
        "terminal_classification": terminal,
        "completed_cells": completed,
        "corrected_real_cell_selector_evaluations": budget.selector_evaluations,
        "scalar_root_invocations": budget.root_invocations,
        "scientific_model_calls": {
            "HJB_policy_maps_iterations_direct_solves": 0,
            "KFE_solves": 0,
            "outer_loop": 0,
            "firm_block": 0,
            "wage_return_recalculation": 0,
            "MATLAB_processes": 0,
            "GE": 0,
            "annual_downstream_production": 0,
            "shock": 0,
            "IRF": 0,
            "Results": 0,
        },
        "adverse_numerics_retries": 0,
    }


def _seal_manifest(evidence: Path) -> dict[str, Any]:
    entries = []
    for path in sorted(evidence.glob("*.json")):
        if path.name == "manifest.json":
            continue
        entries.append(
            {
                "path": path.relative_to(evidence).as_posix(),
                "sha256": _sha256(path),
                "bytes": path.stat().st_size,
            }
        )
    manifest = {
        "schema": "CH5_MP4C_2018_KFE_D123_SELECTOR_ACTIVE_EQUALITY_REEXECUTION_MANIFEST_V1",
        "entries": entries,
        "entry_count": len(entries),
        "total_bytes": sum(int(row["bytes"]) for row in entries),
    }
    _write_json(evidence / "manifest.json", manifest)
    return manifest


def execute(repository: Path) -> int:
    repository = repository.resolve()
    evidence = repository / EVIDENCE_RELATIVE
    evidence.mkdir(parents=True, exist_ok=False)
    panel = bind_preregistered_panel(repository)
    if len(panel) != 10:
        raise RuntimeError("BLOCKED_PANEL_IDENTITY_AMBIGUOUS")
    code_hashes = _scientific_code_hashes(repository)
    freeze = {
        "authority_id": AUTHORITY_ID,
        "git_head_before_first_real_selector_call": _git_head(repository),
        "scientific_code_sha256_before_first_real_selector_call": code_hashes,
        "panel": [_panel_identity(cell) for cell in panel],
        "budget": {
            "selector_evaluations": 10,
            "scalar_root_invocations": 120,
            "max_face_active_sets_per_cell": 4,
            "max_transfer_regimes_per_active_set": 3,
            "max_roots_per_regime": 1,
            "adverse_numerics_retries": 0,
        },
    }
    _write_json(evidence / "pre_execution_freeze.json", freeze)
    code_freeze_identity = {
        "authority_id": freeze["authority_id"],
        "git_head_before_first_real_selector_call": freeze[
            "git_head_before_first_real_selector_call"
        ],
        "scientific_code_sha256_before_first_real_selector_call": freeze[
            "scientific_code_sha256_before_first_real_selector_call"
        ],
    }

    budget = SelectorBudget(max_selector_evaluations=10, max_root_invocations=120)
    receipts: list[dict[str, Any]] = []
    _write_json(evidence / "execution_ledger.json", _ledger(budget, 0, "RUNNING"))
    for ordinal, cell in enumerate(panel, start=1):
        try:
            result = select_constrained_policy(
                cell.selector_cell, cell.selector_parameters, budget=budget
            )
        except Exception as exc:
            failure = {
                "panel_ordinal": ordinal,
                "panel_identity": _panel_identity(cell),
                "outcome": "SCIENTIFIC_CODE_DEFECT_OR_UNHANDLED_NUMERICS_AFTER_FREEZE",
                "exception_type": type(exc).__name__,
                "exception_message": str(exc),
            }
            _write_json(evidence / f"cell_{ordinal:02d}_{cell.panel_id}.json", failure)
            receipts.append(failure)
            terminal = "STOPPED_AFTER_SELECTOR_FAILURE__NO_PATCH_OR_RETRY_AUTHORIZED"
            post_hashes = _scientific_code_hashes(repository)
            _write_json(
                evidence / "post_execution_freeze_check.json",
                {
                    "scientific_code_sha256_after_panel": post_hashes,
                    "matches_pre_execution_freeze": post_hashes == code_hashes,
                },
            )
            _write_json(
                evidence / "panel_results.json",
                {
                    "terminal_classification": terminal,
                    "completed_cells": ordinal - 1,
                    "attempted_cells": ordinal,
                    "cells": receipts,
                },
            )
            _write_json(
                evidence / "execution_ledger.json",
                _ledger(budget, ordinal - 1, terminal),
            )
            _seal_manifest(evidence)
            raise

        try:
            receipt = persist_selector_receipt_then_check_d2(
                evidence,
                ordinal=ordinal,
                cell=cell,
                result=result,
                budget=budget,
                code_freeze_identity=code_freeze_identity,
            )
        except Exception:
            receipt_path = evidence / f"cell_{ordinal:02d}_{cell.panel_id}.json"
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            receipts.append(receipt)
            terminal = (
                "STOPPED_AFTER_D2_REJECTION__SELECTOR_RECEIPT_PRESERVED__NO_RETRY"
            )
            post_hashes = _scientific_code_hashes(repository)
            _write_json(
                evidence / "post_execution_freeze_check.json",
                {
                    "scientific_code_sha256_after_panel": post_hashes,
                    "matches_pre_execution_freeze": post_hashes == code_hashes,
                },
            )
            _write_json(
                evidence / "panel_results.json",
                {
                    "terminal_classification": terminal,
                    "completed_cells": ordinal - 1,
                    "attempted_cells": ordinal,
                    "cells": receipts,
                },
            )
            _write_json(
                evidence / "execution_ledger.json",
                _ledger(budget, ordinal - 1, terminal),
            )
            _seal_manifest(evidence)
            raise
        receipts.append(receipt)
        _write_json(
            evidence / "execution_ledger.json", _ledger(budget, ordinal, "RUNNING")
        )

    post_hashes = _scientific_code_hashes(repository)
    freeze_pass = post_hashes == code_hashes
    outcomes = [str(row["selector_result"]["outcome"]) for row in receipts]
    all_selected = all(outcome == "SELECTED_ADMISSIBLE" for outcome in outcomes)
    all_d2 = all(
        row["d2_assembler_check"]["status"] == "D2_ASSEMBLER_ADMISSIBLE"
        for row in receipts
    )
    if not freeze_pass:
        terminal = "FAIL__SCIENTIFIC_CODE_MUTATED_AFTER_FIRST_REAL_SELECTOR_CALL"
    elif all_selected and all_d2:
        terminal = "PASS__ALL_10_SELECTED_ADMISSIBLE__D2_ASSEMBLER_ADMISSIBLE"
    else:
        terminal = "FAIL__ONE_OR_MORE_PANEL_CELLS_NOT_SELECTED_ADMISSIBLE"
    _write_json(
        evidence / "post_execution_freeze_check.json",
        {
            "scientific_code_sha256_after_panel": post_hashes,
            "matches_pre_execution_freeze": freeze_pass,
        },
    )
    _write_json(
        evidence / "panel_results.json",
        {
            "terminal_classification": terminal,
            "outcomes": outcomes,
            "all_10_selected_admissible": all_selected,
            "all_selected_pass_d2_assembler": all_d2,
            "total_selector_evaluations": budget.selector_evaluations,
            "total_scalar_root_invocations": budget.root_invocations,
            "cells": receipts,
        },
    )
    _write_json(evidence / "execution_ledger.json", _ledger(budget, 10, terminal))
    _seal_manifest(evidence)
    print(json.dumps(_ledger(budget, 10, terminal), indent=2, sort_keys=True))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    arguments = parser.parse_args()
    return execute(arguments.repository)


if __name__ == "__main__":
    raise SystemExit(main())
