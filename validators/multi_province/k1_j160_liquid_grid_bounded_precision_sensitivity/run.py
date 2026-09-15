"""Run exactly the two authorized liquid-grid refinements at fixed J160."""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any

import numpy as np

from validators.multi_province.k1_household_asset_grid_precision_sensitivity import run as accepted
from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import run as coarse
from validators.multi_province.k1_household_k_unit_asset_domain_stagewise import run as stagewise


REPO = Path(__file__).resolve().parents[3]
BASELINE = "ec6b7941739ee405c026aa8faf5275ee8bfb0251"
POINTS = ((40, 160), (80, 160))
ACCEPTED_ROOT = REPO / "docs/evidence/ch5_mp4c_k1_household_asset_grid_precision_receipt_repair_reexecution"
ACCEPTED_POINTS = ACCEPTED_ROOT / "point_receipts.json"
ACCEPTED_INPUT = ACCEPTED_ROOT / "input_invariance_receipt.json"
ACCEPTED_MANIFEST = ACCEPTED_ROOT / "sealed_manifest_sha256.json"
ACCEPTED_HASHES = {
    ACCEPTED_POINTS: "6C0C75A726232A36F521FDEA9FEFBA8AEB2F212EB2E54013536172827749EFE1",
    ACCEPTED_MANIFEST: "2895FD31A7759F4F62DF2008B7BDCBCAE69D5B254B56B6110D3E632A32CB2C88",
}
FORBIDDEN_LEDGER_KEYS = (
    "accepted_reference_hjb_calls", "accepted_reference_kfe_calls", "i160_calls",
    "j320_calls", "j640_calls", "j1280_calls", "global_outer_calls", "firm_calls",
    "matlab_calls", "k1b_calls", "k2_calls", "ge_calls", "downstream_calls",
    "shock_calls", "irf_calls", "results_writes",
)


def canonical_sha256(path: Path) -> str:
    from hashlib import sha256
    return sha256(Path(path).read_text(encoding="utf-8").encode("utf-8")).hexdigest().upper()


def liquid_precision_spec(index: int) -> dict[str, Any]:
    if index not in (0, 1):
        raise ValueError("point is outside the authorized liquid-grid ladder")
    spec = copy.deepcopy(accepted.precision_spec("P2", index))
    spec["task"] = "J160_LIQUID_GRID_BOUNDED_PRECISION_SENSITIVITY"
    return spec


def build_fixture(spec: dict[str, Any]) -> coarse.Fixture:
    authorized = [liquid_precision_spec(index) for index in range(2)]
    if spec not in authorized:
        raise ValueError("fixture is outside the authorized liquid-grid ladder")
    accepted_spec = copy.deepcopy(spec)
    accepted_spec.pop("task")
    return accepted.build_fixture(accepted_spec)


def _accepted_reference_config() -> dict[str, Any]:
    receipt = json.loads(ACCEPTED_INPUT.read_text(encoding="utf-8"))
    candidates = [item for item in receipt["P1"]["configurations"] if len(item["grid.a"]) == 160 and len(item["grid.b"]) == 20]
    if len(candidates) != 1:
        raise ValueError("accepted I20/J160 input configuration is not unique")
    return candidates[0]


def input_invariance_receipt(fixtures: list[coarse.Fixture]) -> dict[str, Any]:
    if len(fixtures) != 2:
        raise ValueError("exactly two fresh fixtures are required")
    configurations = [coarse.fixture_config(item) for item in fixtures]
    varying = sorted(key for key in configurations[0] if configurations[0][key] != configurations[1][key])
    reference = _accepted_reference_config()
    changed_vs_reference = [
        sorted(key for key in configuration if configuration[key] != reference[key])
        for configuration in configurations
    ]
    receipt = {
        "schema": "CH5_MP4C_K1_J160_LIQUID_GRID_INPUT_INVARIANCE_V1",
        "specifications": [liquid_precision_spec(index) for index in range(2)],
        "configurations": configurations,
        "varying_fields": varying,
        "allowed_varying_fields": ["grid.b"],
        "unexpected_varying_fields": [key for key in varying if key != "grid.b"],
        "changed_fields_vs_accepted_i20_j160": changed_vs_reference,
        "fresh_initial_value_object_count": len({id(item.initial_value) for item in fixtures}),
        "fresh_baseline_labor_object_count": len({id(item.baseline_labor) for item in fixtures}),
        "initial_arrays": [{
            "I": fixture.grid.b.size,
            "initial_value_sha256": coarse.array_sha256(fixture.initial_value),
            "baseline_labor_sha256": coarse.array_sha256(fixture.baseline_labor),
            "finite": bool(np.isfinite(fixture.initial_value).all() and np.isfinite(fixture.baseline_labor).all()),
        } for fixture in fixtures],
        "fresh_source_initialization": True,
        "warm_start": False,
    }
    receipt["pass"] = bool(
        varying == ["grid.b"]
        and all(changed == ["grid.b"] for changed in changed_vs_reference)
        and receipt["fresh_initial_value_object_count"] == 2
        and receipt["fresh_baseline_labor_object_count"] == 2
        and all(item["finite"] for item in receipt["initial_arrays"])
    )
    return receipt


def source_identity_receipt() -> dict[str, Any]:
    accepted_source = accepted.source_receipt()
    identities = {}
    for path, expected_hash in ACCEPTED_HASHES.items():
        byte_hash = coarse.file_sha256(path)
        canonical_hash = canonical_sha256(path)
        identities[path.name] = {
            "path": str(path.resolve()), "expected_sha256": expected_hash,
            "actual_byte_sha256": byte_hash, "actual_canonical_lf_sha256": canonical_hash,
            "pass": expected_hash in {byte_hash, canonical_hash},
        }
    receipt = {
        "schema": "CH5_MP4C_K1_J160_LIQUID_GRID_SOURCE_IDENTITY_V1",
        "actual_baseline": BASELINE,
        "accepted_scientific_source": accepted_source,
        "accepted_i20_j160_evidence": identities,
        "accepted_runner": {"path": str(Path(accepted.__file__).resolve()), "sha256": coarse.file_sha256(Path(accepted.__file__))},
        "accepted_hjb_receipt_runner": {"path": str(Path(coarse.__file__).resolve()), "sha256": coarse.file_sha256(Path(coarse.__file__))},
        "matlab_runtime_calls": 0,
    }
    receipt["pass"] = bool(accepted_source["pass"] and all(item["pass"] for item in identities.values()))
    return receipt


def empty_ledger() -> dict[str, Any]:
    ledger = {
        "schema": "CH5_MP4C_K1_J160_LIQUID_GRID_CALL_LEDGER_V1",
        "hjb_budget": 2, "hjb_calls_started": 0, "hjb_calls_completed": 0,
        "kfe_budget": 2, "kfe_calls_started": 0, "kfe_calls_completed": 0,
        "kfe_numeric_solves_returned": 0, "scientific_arrays_persisted": 0,
        "scientific_retries": 0, "engineering_retries": 1,
        "engineering_retry_reason": "initial desktop cwd pointed at the Zotero workflow remote; corrected before any scientific call",
        "points": [],
    }
    ledger.update({key: 0 for key in FORBIDDEN_LEDGER_KEYS})
    return ledger


def execute(output_root: Path) -> int:
    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=False)
    source = source_identity_receipt()
    coarse.write_json(root / "source_identity.json", source)
    if not source["pass"]:
        raise RuntimeError("source identity failed before HJB")
    fixtures = [build_fixture(liquid_precision_spec(index)) for index in range(2)]
    invariance = input_invariance_receipt(fixtures)
    coarse.write_json(root / "input_invariance_receipt.json", invariance)
    if not invariance["pass"]:
        raise RuntimeError("input invariance failed before HJB")
    ledger = empty_ledger()
    coarse.write_json(root / "pre_science_call_ledger.json", ledger)
    stopped = False
    for index, fixture in enumerate(fixtures):
        spec = liquid_precision_spec(index)
        point_id = f"i{spec['I']:03d}_j160"
        coarse.write_json(root / f"{point_id}_started.json", {
            "point_id": point_id, "specification": spec, "fresh_initialization": True,
            "initial_value_sha256": coarse.array_sha256(fixture.initial_value),
            "baseline_labor_sha256": coarse.array_sha256(fixture.baseline_labor),
        })
        ledger["hjb_calls_started"] += 1
        coarse.write_json(root / f"ledger_before_{point_id}_hjb.json", ledger)
        hjb, hjb_receipt = coarse.run_hjb(fixture)
        ledger["hjb_calls_completed"] += 1
        point = {
            "point_id": point_id, "specification": spec,
            "fresh_initialization": {"used": True, "source": "source_initial_arrays", "warm_start": False,
                "initial_value_sha256": coarse.array_sha256(fixture.initial_value),
                "baseline_labor_sha256": coarse.array_sha256(fixture.baseline_labor)},
            "hjb": hjb_receipt, "kfe": {"ran": False},
        }
        if coarse.kfe_authorized(hjb_receipt["classification"]):
            ledger["kfe_calls_started"] += 1
            arrays_path = root / f"{point_id}_scientific_arrays.npz"
            try:
                _, _, kfe_receipt = accepted.run_kfe_persist_first(fixture, hjb, arrays_path)
                ledger["kfe_numeric_solves_returned"] += 1
                ledger["scientific_arrays_persisted"] += 1
                ledger["kfe_calls_completed"] += 1
                kfe_receipt["completed"] = True
                point["kfe"] = kfe_receipt
            except Exception as exc:
                stopped = True
                persisted = arrays_path.is_file()
                if persisted:
                    ledger["kfe_numeric_solves_returned"] += 1
                    ledger["scientific_arrays_persisted"] += 1
                point["kfe"] = {"ran": True, "completed": False, "scientific_arrays_persisted": persisted,
                                "hard_error": f"{type(exc).__name__}: {exc}"}
        else:
            stopped = True
        coarse.write_json(root / f"{point_id}_result.json", point)
        ledger["points"].append({"point_id": point_id, "I": spec["I"], "J": spec["J"],
            "hjb_classification": hjb_receipt["classification"], "kfe_ran": point["kfe"].get("ran", False),
            "kfe_valid": stagewise.kfe_valid(point)})
        if stopped:
            break
    coarse.write_json(root / "final_call_ledger.json", ledger)
    coarse.write_json(root / "execution_complete.json", {
        "status": "J160_LIQUID_GRID_EXECUTION_STOPPED" if stopped else "J160_LIQUID_GRID_EXECUTION_COMPLETE",
        "hjb_calls": ledger["hjb_calls_started"], "kfe_calls": ledger["kfe_calls_started"],
        "results_eligibility": False,
    })
    return 1 if stopped else 0


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("output_root", type=Path)
    return execute(parser.parse_args().output_root)


if __name__ == "__main__":
    raise SystemExit(main())
