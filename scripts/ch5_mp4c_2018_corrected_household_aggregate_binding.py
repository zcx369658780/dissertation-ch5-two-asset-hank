"""One-shot checkpoint-11 aggregate and opt-in adapter evidence runner."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np

from ch5_two_asset_hank.multi_province.corrected_household_adapter import (
    CorrectedHouseholdAggregateInputs,
    evaluate_corrected_household_aggregates,
)


TASK_ID = "CH5_MP4C_2018_CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATE_AND_ADAPTER_BINDING_20260920"
POLICY_ROOT = Path(
    "reports/ch5_mp4c_2018_kfe_d123_checkpoint10_to_checkpoint12_"
    "bounded_nonlinear_continuation_20260920_run001"
)
MASS_ROOT = Path(
    "reports/ch5_mp4c_2018_kfe_d123_checkpoint11_terminal_"
    "source_free_kfe_validation_20260920_run001"
)
MATLAB_SOURCE = Path(
    r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m"
)
EXPECTED = {
    "V11": "A097A3DDA767B979224638A51CEDC53EA635687CCDEFBE190FED0B899606921F",
    "P11": "89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3",
    "u11": "2E9A077FFA809F2DECEE385FD9E7F50C03E16750C2A074F990C0F3CBCC212648",
    "Q11": "33367258F3EADB1482D4A5CB30A64A8574830C993B0E5280C451499CBD6913AD",
    "checkpoint_identity": "8093BE714CA83531816B20DFEB2BAB3DCB7AF9B971AD255C3596C1CA2A9E2A3B",
    "policy_manifest": "5E67E595B32024213EC5E6517389A7DCA6462A24FB735B06EB2F85D6E1621E41",
    "mass_artifact": "1DD70201EAC5EED0AE768362D99A76736276BFB4D5E6AF0D8DBDB4E9D6FE7D16",
    "p": "E215FAE862DA81AD6DEB603859709EA0CF73B8F6F1897567DF942B186CD65ED7",
    "g": "D02592257722313B81C7A1DB40B799ADED8E8BDB5100A65C469E0997DA22E1CE",
    "mass_manifest": "B7C06E3C369B6A5400DE76252DD70A539EFF1F2E4072C04639A1E93E512F5C1D",
    "matlab_source": "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE",
}
OMEGA = 70.0 / 361.0
SHAPE = (20, 20, 2)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def field_sha256(values: np.ndarray) -> str:
    return hashlib.sha256(
        np.asarray(values, dtype="<f8").tobytes(order="F")
    ).hexdigest().upper()


def integer_sha256(values: np.ndarray) -> str:
    return hashlib.sha256(np.asarray(values, dtype="<i8").tobytes()).hexdigest().upper()


def canonical_sha256(value: Any) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest().upper()


def write_json(path: Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False)
        + "\n",
        encoding="utf-8",
    )


def verify_sealed_root(root: Path, expected_manifest: str) -> dict[str, Any]:
    manifest_path = root / "sealed_manifest.json"
    if sha256(manifest_path) != expected_manifest:
        raise RuntimeError(f"sealed manifest identity mismatch: {root}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = manifest["entries"]
    total_bytes = 0
    for entry in entries:
        path = root / entry["path"]
        if path.stat().st_size != int(entry["bytes"]) or sha256(path) != entry["sha256"]:
            raise RuntimeError(f"sealed entry mismatch: {path}")
        total_bytes += path.stat().st_size
    return {
        "root": root.as_posix(),
        "manifest_sha256": expected_manifest,
        "entries": len(entries),
        "bytes": total_bytes,
        "readback_bad_count": 0,
    }


def selected_identity(selected: dict[str, Any]) -> dict[str, Any]:
    interior = selected.get("interior_z_receipt")
    lower_a = selected.get("lower_a_zero_kink_multiplier_receipt")
    return {
        "derivative_branches": selected.get("derivative_branches"),
        "active_constraints": selected.get("active_constraints"),
        "transfer_branch": selected.get("transfer_branch"),
        "interior_z_marker": None if interior is None else interior.get("marker"),
        "lower_a_zero_kink_marker": None if lower_a is None else lower_a.get("marker"),
    }


def load_bound_policy(checkpoint: Path) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    c = np.empty(SHAPE, dtype=np.float64, order="F")
    labor = np.empty(SHAPE, dtype=np.float64, order="F")
    effective_r_a = np.empty(SHAPE, dtype=np.float64, order="F")
    b = np.empty(SHAPE[0], dtype=np.float64)
    a = np.empty(SHAPE[1], dtype=np.float64)
    z = np.empty(SHAPE[2], dtype=np.float64)
    identities: list[dict[str, Any]] = []
    for flat in range(np.prod(SHAPE)):
        receipt = json.loads(
            (checkpoint / f"cell_{flat:04d}.json").read_text(encoding="utf-8")
        )
        index = tuple(int(item) for item in receipt["index_b_a_z_zero_based"])
        expected_index = tuple(int(item) for item in np.unravel_index(flat, SHAPE, order="F"))
        if receipt["flat_index_f_zero_based"] != flat or index != expected_index:
            raise RuntimeError(f"F-order cell identity mismatch at {flat}")
        cell = receipt["selector_cell"]
        selected = receipt["selector_result"]["selected"]
        if not selected["admissible"] or receipt["selector_result"]["outcome"] != "SELECTED_ADMISSIBLE":
            raise RuntimeError(f"accepted policy receipt is not admissible at {flat}")
        c[index] = float(selected["c"])
        labor[index] = float(selected["l"])
        effective_r_a[index] = float(cell["effective_r_a"])
        b[index[0]] = float(cell["b"])
        a[index[1]] = float(cell["a"])
        z[index[2]] = float(cell["z"])
        identities.append(selected_identity(selected))
    policy_identity = canonical_sha256(identities)
    if policy_identity != EXPECTED["P11"]:
        raise RuntimeError("P11 identity mismatch")
    expected_effective = 0.09 * (1.0 - 0.1 * (a / 10.0) ** 9)
    if not np.array_equal(effective_r_a[0, :, 0], expected_effective):
        raise RuntimeError("effective illiquid return does not match accepted cell operands")
    if not np.all(effective_r_a == effective_r_a[0, :, 0][None, :, None]):
        raise RuntimeError("effective illiquid return varies outside the a axis")
    return (
        {"c": c, "labor": labor, "effective_r_a": effective_r_a, "b": b, "a": a, "z": z},
        {
            "policy_identity_sha256": policy_identity,
            "cell_receipts_loaded": int(np.prod(SHAPE)),
            "shape": list(SHAPE),
            "axis_order": ["b", "a", "z"],
            "flatten_order": "F",
            "source_r_a": 0.09,
            "effective_r_a_by_a": effective_r_a[0, :, 0].tolist(),
        },
    )


def bind_checkpoint(checkpoint: Path) -> dict[str, Any]:
    manifest = json.loads((checkpoint / "checkpoint_manifest.json").read_text(encoding="utf-8"))
    arrays_path = checkpoint / "checkpoint_arrays.npz"
    q_path = checkpoint / "q_generator.npz"
    with np.load(arrays_path, allow_pickle=False) as arrays:
        value_hash = field_sha256(arrays["value"])
        utility_hash = field_sha256(arrays["utility"])
    with np.load(q_path, allow_pickle=False) as q:
        q_identity = {
            "data": field_sha256(q["data"]),
            "indices": integer_sha256(q["indices"]),
            "indptr": integer_sha256(q["indptr"]),
        }
    identity = canonical_sha256(
        {"value": value_hash, "policy": EXPECTED["P11"], "q": q_identity}
    )
    checks = {
        "V11": value_hash == EXPECTED["V11"] == manifest["value_sha256"],
        "P11": manifest["policy_identity_sha256"] == EXPECTED["P11"],
        "u11": utility_hash == EXPECTED["u11"] == manifest["utility_sha256"],
        "Q11": sha256(q_path) == EXPECTED["Q11"] == manifest["q_artifact_sha256"],
        "checkpoint_identity": identity
        == EXPECTED["checkpoint_identity"]
        == manifest["checkpoint_identity_sha256"],
    }
    if not all(checks.values()):
        raise RuntimeError(f"checkpoint-11 binding failed: {checks}")
    return {
        "checks": checks,
        "V11": value_hash,
        "P11": EXPECTED["P11"],
        "u11": utility_hash,
        "Q11": sha256(q_path),
        "checkpoint_identity": identity,
        "q_identity": q_identity,
    }


def comparison_payload(value: Any) -> dict[str, Any]:
    return {
        "mass_form": value.mass_form,
        "density_form": value.density_form,
        "absolute_difference": value.absolute_difference,
        "prospective_bound": value.prospective_bound,
        "equivalent": value.equivalent,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    repository = args.repository.resolve(strict=True)
    output = args.output.resolve()
    if output.exists():
        raise RuntimeError("fresh evidence output already exists")
    output.mkdir(parents=True)

    policy_root = repository / POLICY_ROOT
    mass_root = repository / MASS_ROOT
    policy_seal = verify_sealed_root(policy_root, EXPECTED["policy_manifest"])
    mass_seal = verify_sealed_root(mass_root, EXPECTED["mass_manifest"])
    checkpoint = policy_root / "checkpoint_011"
    binding = bind_checkpoint(checkpoint)
    policy, policy_receipt = load_bound_policy(checkpoint)
    if sha256(MATLAB_SOURCE) != EXPECTED["matlab_source"]:
        raise RuntimeError("designated MATLAB source identity mismatch")

    mass_path = mass_root / "stationary_mass_arrays.npz"
    if sha256(mass_path) != EXPECTED["mass_artifact"]:
        raise RuntimeError("terminal stationary-mass artifact mismatch")
    with np.load(mass_path, allow_pickle=False) as mass:
        p = np.asarray(mass["p"], dtype=np.float64).reshape(SHAPE, order="F")
        g = np.asarray(mass["g"], dtype=np.float64).reshape(SHAPE, order="F")
    if field_sha256(p) != EXPECTED["p"] or field_sha256(g) != EXPECTED["g"]:
        raise RuntimeError("accepted p/g identity mismatch")

    aggregate_inputs = CorrectedHouseholdAggregateInputs(
        consumption=policy["c"],
        labor=policy["labor"],
        b_grid=policy["b"],
        a_grid=policy["a"],
        z_grid=policy["z"],
        effective_r_a=policy["effective_r_a"],
        probability_mass=p,
        density=g,
        omega=OMEGA,
        source_r_a=0.09,
    )

    # The task's single accepted checkpoint-11 aggregate evaluation.
    aggregates = evaluate_corrected_household_aggregates(aggregate_inputs)
    frozen = aggregates.frozen_output(
        converged=True, convergence_statistic=5.456747553811425e-11
    )

    write_json(
        output / "accepted_input_binding.json",
        {
            "task_id": TASK_ID,
            "checkpoint": binding,
            "policy_evidence": policy_seal,
            "terminal_mass_evidence": mass_seal,
            "stationary_mass_artifact_sha256": sha256(mass_path),
            "p_sha256": field_sha256(p),
            "g_sha256": field_sha256(g),
            "omega": OMEGA,
            "policy_receipt": policy_receipt,
        },
    )
    write_json(
        output / "source_formula_mapping.json",
        {
            "matlab_source": str(MATLAB_SOURCE),
            "matlab_source_sha256": EXPECTED["matlab_source"],
            "Ct": {"line": 354, "source": "sum(C.*g*dah*db,'all')"},
            "Lt": {"line": 347, "source": "sum(zzz.*l.*g*dah*db,'all')"},
            "At": {"line": 351, "source": "sum(aaah.*g*dah*db,'all')", "source_name": "Aht"},
            "Bt": {"line": 348, "source": "sum(bbb.*g*dah*db,'all')"},
            "total_assets": {"source": "At + Bt"},
            "AtTax": {
                "line": 365,
                "source": "Aht*rah - sum(aaah.*raah.*g*dah*db,'all')",
                "operands": {
                    "rah": "results.rah; source uniform illiquid return",
                    "raah": "rah*(1-0.1*(ahmax./ah).^(-9)); used tapered illiquid return",
                    "aaah": "illiquid asset state",
                    "g*dah*db": "stationary probability mass",
                },
                "semantics": "aggregate illiquid-return flow gap",
                "units": "household model relative asset-flow units per model period",
                "raw_or_used_return": "uniform source rah minus used state-dependent tapered raah",
            },
            "grid_weight": "omega=dah*db=70/361",
            "forbidden_extra_weights_absent": ["dz", "trapezoid", "endpoint"],
        },
    )
    aggregate_payload = {
        name: comparison_payload(getattr(aggregates, name))
        for name in ("Ct", "Lt", "At", "Bt", "total_assets", "AtTax")
    }
    write_json(
        output / "aggregate_receipt.json",
        {
            "accepted_checkpoint_aggregate_evaluation_ordinal": 1,
            "shape": list(SHAPE),
            "axis_order": list(aggregates.axis_order),
            "flatten_order": aggregates.flatten_order,
            "second_density_normalization_applied": False,
            "aggregates": aggregate_payload,
        },
    )
    write_json(
        output / "adapter_fixture_receipt.json",
        {
            "opt_in_module": "ch5_two_asset_hank.multi_province.corrected_household_adapter",
            "default_route_changed": False,
            "fixture": {
                "Ct": frozen.Ct,
                "Lt": frozen.Lt,
                "At": frozen.At,
                "Bt": frozen.Bt,
                "AtTax": frozen.AtTax,
                "converged": frozen.converged,
                "convergence_statistic": frozen.convergence_statistic,
            },
        },
    )
    write_json(
        output / "scientific_ledger.json",
        {
            "accepted_checkpoint11_aggregate_post_processing_evaluations": 1,
            "hjb_solves_updates": 0,
            "kfe_nullspace_svd_eigen_solves": 0,
            "policy_maps_selectors_roots": 0,
            "q_d2_assemblies": 0,
            "firm_calls": 0,
            "wage_return_calls": 0,
            "capital_labor_allocation_calls": 0,
            "outer_loop_steady_state_trajectory_calls": 0,
            "matlab_scientific_calls": 0,
            "ge_annual_shock_irf_welfare_results_calls": 0,
            "scientific_retries": 0,
        },
    )
    write_json(
        output / "terminal_receipt.json",
        {
            "terminal_verdict": "PASS__CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATES_BOUND__OPT_IN_ADAPTER_FIXTURE_READY",
            "results_eligibility": False,
            "all_required_fields_closed": True,
        },
    )
    print(json.dumps(aggregate_payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
