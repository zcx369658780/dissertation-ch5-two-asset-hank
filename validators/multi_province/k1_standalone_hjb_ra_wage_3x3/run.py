"""Run the exact Owner-approved standalone HJB ra x wage 3x3 scan.

The accepted standalone HJB and KFE callables remain unchanged.  A temporary
assembler observer records the MATLAB ``A2max=max(abs(sum(A,2)))`` statistic;
its records never feed back into the accepted scientific solve.
"""
from __future__ import annotations

import argparse
import json
import warnings
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable

import numpy as np
from scipy import sparse

from exports import matlab_faithful_two_asset_ha as oracle
from validators.multi_province.corrected_2018_single_turn.run import source_initial_arrays


REPO = Path(__file__).resolve().parents[3]
POINTS = tuple((ra, wage) for ra in (0.02, 0.055, 0.09) for wage in (0.8, 1.05, 1.3))
ORACLE_PATH = REPO / "exports" / "matlab_faithful_two_asset_ha.py"
ORACLE_SHA256 = "F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8"
MATLAB_PATH = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m")
MATLAB_SHA256 = "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE"
HOMECRIT = 0.01
HJB_CLASSES = {
    "HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX",
    "HJB_NOT_CONVERGED",
    "HJB_CONVERGED",
}


@dataclass
class Fixture:
    grid: Any
    params: Any
    inputs: Any
    initial_value: np.ndarray
    baseline_labor: np.ndarray
    transfer_income: float
    borrowing_rate_gap: float
    numerics: Any

    @property
    def db(self) -> float:
        return float(self.grid.b[1] - self.grid.b[0])

    @property
    def da(self) -> float:
        return float(self.grid.a[1] - self.grid.a[0])

    def arguments(self) -> tuple[Any, ...]:
        return (
            self.grid, self.params, self.inputs, self.initial_value,
            self.baseline_labor, self.transfer_income,
            self.borrowing_rate_gap, self.numerics,
        )


def file_sha256(path: Path) -> str:
    digest = sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def array_sha256(value: np.ndarray) -> str:
    array = np.asarray(value)
    header = f"{array.dtype.str}|{array.shape}|C|".encode("ascii")
    return sha256(header + np.ascontiguousarray(array).tobytes()).hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    def convert(item: Any) -> Any:
        if isinstance(item, np.ndarray):
            return item.tolist()
        if isinstance(item, np.generic):
            return item.item()
        if isinstance(item, Path):
            return str(item.resolve())
        if isinstance(item, dict):
            return {str(key): convert(val) for key, val in item.items()}
        if isinstance(item, (tuple, list)):
            return [convert(val) for val in item]
        return item

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(convert(value), stream, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
        stream.write("\n")


def build_fixture(ra: float, wage: float) -> Fixture:
    if (ra, wage) not in POINTS:
        raise ValueError("parameter point is outside the preregistered Cartesian grid")
    grid = oracle.MatlabFaithfulHJBGrid(
        np.linspace(-2.0, 5.0, 20),
        np.linspace(0.0, 10.0, 20),
        np.array([0.8, 1.3]),
        np.array([[-1.0 / 3.0, 1.0 / 3.0], [1.0 / 3.0, -1.0 / 3.0]]),
    )
    params = oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    state = {"rah": ra, "rb": 0.02, "rb_gap": 0.07, "Tt": 0.1, "tau": 0.05, "w": wage}
    initial_value, baseline_labor = source_initial_arrays(state, grid, params)
    inputs = oracle.HouseholdInputs(
        ra, 0.02, 0.05, np.array([wage]), np.zeros(1), np.ones(1),
    )
    numerics = oracle.MatlabFaithfulHJBNumerics(1000.0, 1e-7, 100, 1e-12)
    return Fixture(grid, params, inputs, initial_value, baseline_labor, 0.1, 0.07, numerics)


def fixture_config(fixture: Fixture) -> dict[str, Any]:
    return {
        "grid.b": fixture.grid.b.tolist(), "grid.a": fixture.grid.a.tolist(),
        "grid.z": fixture.grid.z.tolist(), "grid.switch_matrix": fixture.grid.switch_matrix.tolist(),
        "params.rho": fixture.params.rho, "params.gamma_c": fixture.params.gamma_c,
        "params.phi": fixture.params.phi, "params.chi_0": fixture.params.chi_0,
        "params.chi_1": fixture.params.chi_1, "params.a_bar": fixture.params.a_bar,
        "params.mu_z": fixture.params.mu_z, "params.sigma_z": fixture.params.sigma_z,
        "inputs.r_a": fixture.inputs.r_a, "inputs.r_b": fixture.inputs.r_b,
        "inputs.tau": fixture.inputs.tau, "inputs.wages[0]": float(fixture.inputs.wages[0]),
        "inputs.migration_costs": fixture.inputs.migration_costs.tolist(),
        "inputs.labor_weights": fixture.inputs.labor_weights.tolist(),
        "transfer_income": fixture.transfer_income,
        "borrowing_rate_gap": fixture.borrowing_rate_gap,
        "numerics.delta": fixture.numerics.delta,
        "numerics.convergence_tolerance": fixture.numerics.convergence_tolerance,
        "numerics.max_iterations": fixture.numerics.max_iterations,
        "numerics.drift_tolerance": fixture.numerics.drift_tolerance,
    }


def input_invariance_receipt(fixtures: Iterable[Fixture]) -> dict[str, Any]:
    configurations = [fixture_config(item) for item in fixtures]
    if not configurations:
        raise ValueError("at least one fixture is required")
    varying = sorted(
        key for key in configurations[0]
        if any(configuration[key] != configurations[0][key] for configuration in configurations[1:])
    )
    allowed = ["inputs.r_a", "inputs.wages[0]"]
    return {
        "point_count": len(configurations),
        "varying_fields": varying,
        "allowed_varying_fields": allowed,
        "unexpected_varying_fields": [key for key in varying if key not in allowed],
        "all_non_scanned_fields_identical": all(key in allowed for key in varying),
        "configurations": configurations,
    }


def operator_legality_receipt(matrix: Any, *, iteration: int) -> dict[str, Any]:
    value = sparse.csr_matrix(matrix, dtype=float)
    row_sums = np.asarray(value.sum(axis=1)).ravel()
    a2max = float(np.max(np.abs(row_sums)))
    coo = value.tocoo()
    off = coo.data[coo.row != coo.col]
    return {
        "iteration": int(iteration), "a2max": a2max, "homecrit": HOMECRIT,
        "legal": bool(np.isfinite(a2max) and a2max <= HOMECRIT),
        "row_sum_nonfinite_count": int(np.count_nonzero(~np.isfinite(row_sums))),
        "minimum_stored_off_diagonal": float(np.min(off)) if off.size else 0.0,
        "matrix_shape": list(value.shape), "matrix_nnz": int(value.nnz),
    }


def classify_hjb(*, converged: bool, hard_error: str | None,
                 first_illegal_iteration: int | None) -> str:
    if hard_error is not None or first_illegal_iteration is not None:
        return "HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX"
    return "HJB_CONVERGED" if converged else "HJB_NOT_CONVERGED"


def kfe_authorized(classification: str) -> bool:
    if classification not in HJB_CLASSES:
        raise ValueError("unknown HJB classification")
    return classification == "HJB_CONVERGED"


def distribution_receipt(grid: Any, density: np.ndarray) -> dict[str, Any]:
    value = np.asarray(density, dtype=float)
    shape = (grid.b.size, grid.a.size, grid.z.size)
    if value.shape != shape:
        raise ValueError("density shape mismatch")
    db = float(grid.b[1] - grid.b[0]); da = float(grid.a[1] - grid.a[0])
    cell_weight = db * da
    b_mass = np.sum(value, axis=(1, 2)) * cell_weight
    a_mass = np.sum(value, axis=(0, 2)) * cell_weight

    def ratio(numerator: float, denominator: float) -> float | None:
        return float(numerator / denominator) if denominator != 0.0 else None

    b_modes = np.flatnonzero(b_mass == np.max(b_mass))
    a_modes = np.flatnonzero(a_mass == np.max(a_mass))
    return {
        "density_shape": list(value.shape),
        "density_finite": bool(np.isfinite(value).all()),
        "density_min": float(np.min(value)), "density_negative_count": int(np.count_nonzero(value < 0.0)),
        "total_mass": float(np.sum(value) * cell_weight),
        "b_marginal_mass": b_mass.tolist(), "a_marginal_mass": a_mass.tolist(),
        "boundary_mass_shares": {
            "bmin": float(b_mass[0]), "bmax": float(b_mass[-1]),
            "amin": float(a_mass[0]), "amax": float(a_mass[-1]),
        },
        "upper_endpoint_comparison": {
            "bmax": float(b_mass[-1]), "b_adjacent_1": float(b_mass[-2]),
            "b_adjacent_2": float(b_mass[-3]),
            "bmax_to_adjacent_1_ratio": ratio(float(b_mass[-1]), float(b_mass[-2])),
            "amax": float(a_mass[-1]), "a_adjacent_1": float(a_mass[-2]),
            "a_adjacent_2": float(a_mass[-3]),
            "amax_to_adjacent_1_ratio": ratio(float(a_mass[-1]), float(a_mass[-2])),
        },
        "modal_b": [float(grid.b[index]) for index in b_modes],
        "modal_a": [float(grid.a[index]) for index in a_modes],
    }


def scientific_array_receipt(result: Any, shape: tuple[int, int, int]) -> dict[str, Any]:
    fields = (
        "value", "initial_value", "consumption", "labor", "transfer",
        "adjustment_cost", "effective_illiquid_return", "mu_a", "mu_b", "utility",
    )
    arrays = {}
    for name in fields:
        value = np.asarray(getattr(result, name))
        arrays[name] = {
            "shape": list(value.shape), "expected_shape": value.shape == shape,
            "finite": bool(np.isfinite(value).all()), "sha256": array_sha256(value),
        }
    return {
        "arrays": arrays,
        "liquid_label_shape": list(result.liquid_label.shape),
        "transfer_label_shape": list(result.transfer_label.shape),
        "liquid_label_domain": sorted(set(map(str, result.liquid_label.ravel()))),
        "transfer_label_domain": sorted(set(map(str, result.transfer_label.ravel()))),
        "all_arrays_finite_shape_valid": all(item["finite"] and item["expected_shape"] for item in arrays.values()),
        "label_domains_valid": set(map(str, result.liquid_label.ravel())) <= {"B", "F", "0"}
        and set(map(str, result.transfer_label.ravel())) <= {"B", "F", "0"},
    }


def run_hjb(fixture: Fixture) -> tuple[Any | None, dict[str, Any]]:
    original_assembler = oracle.assemble_source_operator
    operator_records: list[dict[str, Any]] = []

    def observed_assembler(*args: Any, **kwargs: Any) -> Any:
        assembled = original_assembler(*args, **kwargs)
        operator_records.append(operator_legality_receipt(assembled.full, iteration=len(operator_records) + 1))
        return assembled

    result = None
    hard_error = None
    caught_warnings: list[str] = []
    oracle.assemble_source_operator = observed_assembler
    try:
        with warnings.catch_warnings(record=True) as captured:
            warnings.simplefilter("always")
            result = oracle.solve_matlab_faithful_hjb(*fixture.arguments())
            caught_warnings = [f"{item.category.__name__}: {item.message}" for item in captured]
    except Exception as exc:  # a scientific hard error is an intended point outcome
        hard_error = f"{type(exc).__name__}: {exc}"
    finally:
        oracle.assemble_source_operator = original_assembler

    iteration_count = int(result.iterations) if result is not None else len(operator_records)
    iteration_records = operator_records[:iteration_count]
    post_record = operator_records[iteration_count] if len(operator_records) > iteration_count else None
    first_illegal = next((item["iteration"] for item in iteration_records if not item["legal"]), None)
    classification = classify_hjb(
        converged=bool(result.converged) if result is not None else False,
        hard_error=hard_error,
        first_illegal_iteration=first_illegal,
    )
    receipt = {
        "classification": classification, "hard_error": hard_error,
        "warnings": caught_warnings, "iterations_used": iteration_count,
        "converged": bool(result.converged) if result is not None else False,
        "final_convergence_statistic": float(result.convergence_statistic) if result is not None else None,
        "first_illegal_iteration": first_illegal,
        "maximum_a2max": max((item["a2max"] for item in iteration_records), default=None),
        "minimum_stored_off_diagonal": min(
            (item["minimum_stored_off_diagonal"] for item in iteration_records), default=None
        ),
        "iteration_operator_legality": iteration_records,
        "post_convergence_operator_receipt": post_record,
    }
    if result is not None:
        receipt["scientific_arrays"] = scientific_array_receipt(
            result, (fixture.grid.b.size, fixture.grid.a.size, fixture.grid.z.size)
        )
    return result, receipt


def run_kfe(fixture: Fixture, hjb: Any) -> tuple[Any, Any, dict[str, Any]]:
    shape = (fixture.grid.b.size, fixture.grid.a.size, fixture.grid.z.size)
    kfe = oracle.solve_matlab_faithful_stationary_kfe(
        hjb.post_convergence_operator.full, shape=shape, db=fixture.db, da=fixture.da,
    )
    aggregates = oracle.aggregate_stationary_household(
        fixture.grid, hjb.consumption, hjb.labor, kfe.density,
    )
    distribution = distribution_receipt(fixture.grid, kfe.density)
    b = np.broadcast_to(fixture.grid.b[:, None, None], shape)
    weighted = kfe.density * fixture.db * fixture.da
    distribution.update({
        "Bt_pos": float(np.sum(np.where(b > 0.0, b, 0.0) * weighted)),
        "Bt_neg": float(np.sum(np.where(b < 0.0, b, 0.0) * weighted)),
    })
    receipt = {
        "ran": True,
        "aggregates": {
            "Ct": aggregates.c_ss, "Lt": aggregates.l_ss,
            "At": aggregates.a_ss, "Bt": aggregates.b_ss,
            "total_assets": aggregates.total_assets,
            "density_normalization": aggregates.density_normalization,
        },
        "kfe": {
            "contaminated_row_index": kfe.contaminated_row_index,
            "normalization_factor": kfe.normalization_factor,
            "raw_residual_inf": kfe.raw_residual_inf,
            "density_vector_shape": list(kfe.density_vector.shape),
            "density_sha256": array_sha256(kfe.density),
        },
        "distribution": distribution,
        "preliminary_quality_label": "PENDING_OFFLINE_DESCRIPTIVE_REVIEW",
    }
    return kfe, aggregates, receipt


def execute(evidence_root: Path) -> int:
    root = Path(evidence_root)
    root.mkdir(parents=True, exist_ok=False)
    source_receipt = {
        "oracle": {"path": ORACLE_PATH, "expected_sha256": ORACLE_SHA256, "actual_sha256": file_sha256(ORACLE_PATH)},
        "matlab": {"path": MATLAB_PATH, "expected_sha256": MATLAB_SHA256, "actual_sha256": file_sha256(MATLAB_PATH)},
        "matlab_runtime_calls": 0,
    }
    source_receipt["pass"] = all(
        item["expected_sha256"] == item["actual_sha256"]
        for key, item in source_receipt.items() if key in {"oracle", "matlab"}
    )
    write_json(root / "source_identity.json", source_receipt)
    if not source_receipt["pass"]:
        raise RuntimeError("source identity preflight failed before HJB")

    fixtures = [build_fixture(ra, wage) for ra, wage in POINTS]
    invariance = input_invariance_receipt(fixtures)
    invariance["fresh_initial_value_object_count"] = len({id(item.initial_value) for item in fixtures})
    invariance["fresh_baseline_labor_object_count"] = len({id(item.baseline_labor) for item in fixtures})
    invariance["initial_arrays"] = [
        {
            "ra": ra, "wage": wage,
            "initial_value_sha256": array_sha256(fixture.initial_value),
            "baseline_labor_sha256": array_sha256(fixture.baseline_labor),
            "initial_value_finite": bool(np.isfinite(fixture.initial_value).all()),
            "baseline_labor_finite": bool(np.isfinite(fixture.baseline_labor).all()),
        }
        for (ra, wage), fixture in zip(POINTS, fixtures)
    ]
    write_json(root / "input_invariance.json", invariance)
    if invariance["unexpected_varying_fields"] or invariance["fresh_initial_value_object_count"] != 9:
        raise RuntimeError("input invariance/fresh initialization preflight failed before HJB")

    ledger = {
        "schema": "CH5_MP4C_K1_STANDALONE_HJB_RA_WAGE_3X3_LEDGER_V1",
        "hjb_budget": 9, "hjb_calls_started": 0, "hjb_calls_completed": 0,
        "kfe_budget": 9, "kfe_calls_started": 0, "kfe_calls_completed": 0,
        "initialization_constructions": 9, "scalar_labor_roots": 7200,
        "scientific_retries": 0, "global_multi_province_outer_turns": 0,
        "firm_runtime_calls": 0, "matlab_runtime_calls": 0,
        "k1b_calls": 0, "k2_calls": 0, "ge_calls": 0,
        "annual_downstream_calls": 0, "shock_calls": 0, "irf_calls": 0,
        "results_writes": 0, "points": [],
    }
    write_json(root / "pre_science_ledger.json", ledger)

    for index, ((ra, wage), fixture) in enumerate(zip(POINTS, fixtures), start=1):
        point_id = f"p{index:02d}_ra_{ra:.3f}_w_{wage:.2f}".replace(".", "p")
        write_json(root / f"{point_id}_started.json", {"point_index": index, "r_b": 0.02, "r_a": ra, "wage": wage})
        ledger["hjb_calls_started"] += 1
        hjb, hjb_receipt = run_hjb(fixture)
        ledger["hjb_calls_completed"] += 1
        point = {"point_index": index, "point_id": point_id, "r_b": 0.02, "r_a": ra, "wage": wage,
                 "hjb": hjb_receipt, "kfe": {"ran": False},
                 "preliminary_quality_label": None}
        if kfe_authorized(hjb_receipt["classification"]):
            assert hjb is not None
            ledger["kfe_calls_started"] += 1
            try:
                kfe, _, kfe_receipt = run_kfe(fixture, hjb)
                ledger["kfe_calls_completed"] += 1
                point["kfe"] = kfe_receipt
                np.savez_compressed(
                    root / f"{point_id}_scientific_arrays.npz",
                    value=hjb.value, consumption=hjb.consumption, labor=hjb.labor,
                    transfer=hjb.transfer, mu_a=hjb.mu_a, mu_b=hjb.mu_b,
                    density=kfe.density,
                )
            except Exception as exc:  # no retry; preserve the first KFE outcome
                point["kfe"] = {"ran": True, "completed": False, "hard_error": f"{type(exc).__name__}: {exc}"}
        write_json(root / f"{point_id}_result.json", point)
        ledger["points"].append({
            "point_index": index, "point_id": point_id,
            "hjb_classification": hjb_receipt["classification"],
            "kfe_ran": bool(point["kfe"]["ran"]),
        })

    write_json(root / "final_call_ledger.json", ledger)
    write_json(root / "execution_complete.json", {
        "status": "EXACT_3X3_EXECUTION_COMPLETE", "results_eligibility": False,
        "hjb_calls": ledger["hjb_calls_started"], "kfe_calls": ledger["kfe_calls_started"],
    })
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_root", type=Path)
    args = parser.parse_args()
    return execute(args.evidence_root)


if __name__ == "__main__":
    raise SystemExit(main())
