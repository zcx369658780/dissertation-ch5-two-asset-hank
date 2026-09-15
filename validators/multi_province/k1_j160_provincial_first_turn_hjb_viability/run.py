"""Run one frozen J160 HJB for each sealed accepted first-turn province input."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np

from exports import matlab_faithful_two_asset_ha as oracle
from validators.multi_province.corrected_2018_single_turn.run import source_initial_arrays
from validators.multi_province.k1_standalone_hjb_ra_wage_3x3 import run as accepted_hjb


REPO = Path(__file__).resolve().parents[3]
BASELINE = "ad5a05d6c4af76b26fa868eb58d8bac3a14157ce"
ACCEPTED_COMMIT = "c6d89327933edef2b942f10f462b58cfa6b52954"
ACCEPTED_ROOT = REPO / "docs/evidence/ch5_mp4c_k1_hjb_convergence_mechanism_turn1_turn2"
ACCEPTED_IDENTITY_PATH = ACCEPTED_ROOT / "identity_receipts.json"
ACCEPTED_MANIFEST_PATH = ACCEPTED_ROOT / "sealed_manifest_sha256.json"
ACCEPTED_ACCEPTANCE_PATH = REPO / "docs/CH5_MP4C_K1_HJB_CONVERGENCE_MECHANISM_TURN1_TURN2_DIAGNOSTIC_ACCEPTANCE.md"
ORACLE_PATH = REPO / "exports/matlab_faithful_two_asset_ha.py"
INITIALIZER_PATH = REPO / "validators/multi_province/corrected_2018_single_turn/run.py"
HJB_RECEIPT_RUNNER_PATH = REPO / "validators/multi_province/k1_standalone_hjb_ra_wage_3x3/run.py"
MATLAB_PATH = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m")

ACCEPTED_IDENTITY_SHA256 = "DB5FD1B183CDC16ADDF67AEFADCC1AD2FD11B9715DA36D55290B1D035808B0D2"
ACCEPTED_MANIFEST_SHA256 = "82A979E15DF22A651348F8C4E35FFE5688513E635877269DA98DF0755D03AF77"
ACCEPTED_ACCEPTANCE_SHA256 = "BE2DCE4A747A80C8D0A4F781A5AC5E3843230428956FC6CA88138C157E970540"
ORACLE_SHA256 = "F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8"
INITIALIZER_SHA256 = "9EAF82373EE564E5F27BEA14D49D2177E0637A6969D946C86F519608FFBAE614"
HJB_RECEIPT_RUNNER_SHA256 = "7F2B5A9DA239521F6A638FAC458B318A2F1908D81ED56C79DF026A107AA570FA"
MATLAB_SHA256 = "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE"

FORBIDDEN_LEDGER_KEYS = (
    "kfe_calls_started", "kfe_calls_completed", "global_outer_calls", "firm_calls",
    "wage_recalculation_calls", "return_recalculation_calls", "matlab_calls",
    "k1b_calls", "k2_calls", "ge_calls", "downstream_calls", "shock_calls",
    "irf_calls", "results_writes",
)


def _block(message: str) -> ValueError:
    return ValueError(f"FIRST_TURN_PROVINCIAL_INPUT_AUTHORITY_BLOCKER: {message}")


def _manifest_identity_entry(manifest_path: Path = ACCEPTED_MANIFEST_PATH) -> dict[str, Any]:
    manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    matches = [entry for entry in manifest.get("entries", []) if entry.get("path") == "identity_receipts.json"]
    if len(matches) != 1:
        raise _block("accepted manifest lacks one unique identity_receipts.json entry")
    return matches[0]


def load_first_turn_authority(
    identity_path: Path = ACCEPTED_IDENTITY_PATH, *, enforce_seal: bool = True,
) -> dict[str, Any]:
    path = Path(identity_path)
    actual_hash = accepted_hjb.file_sha256(path)
    manifest_entry = _manifest_identity_entry()
    if enforce_seal and (
        actual_hash != ACCEPTED_IDENTITY_SHA256
        or manifest_entry.get("sha256") != ACCEPTED_IDENTITY_SHA256
        or manifest_entry.get("bytes") != path.stat().st_size
    ):
        raise _block("accepted compact identity artifact seal mismatch")
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = [item for item in payload if item.get("turn") == 1]
    rows.sort(key=lambda item: item.get("province_index", -1))
    if len(rows) != 31:
        raise _block(f"expected 31 turn-1 rows, found {len(rows)}")
    if [item.get("province_index") for item in rows] != list(range(31)):
        raise _block("province indices are not exactly 0..30")
    if len({item.get("province") for item in rows}) != 31:
        raise _block("province identifiers are not unique")

    required = (
        "province", "province_index", "r_b", "consumed_r_a", "wage", "tau",
        "transfer_income", "borrowing_rate_gap", "return_guard_state",
        "wage_guard_state", "transfer_control_state", "params", "numerics", "checks",
    )
    sealed_rows = []
    for item in rows:
        if any(key not in item for key in required):
            raise _block(f"missing required field for province {item.get('province_index')}")
        if item.get("status") != "PROVEN_EXACT" or not all(item["checks"].values()):
            raise _block(f"provenance is not exact for province {item['province_index']}")
        if item["transfer_control_state"] != "D1_OFF":
            raise _block(f"unexpected transfer control for province {item['province_index']}")
        sealed_rows.append({
            "province_index": int(item["province_index"]),
            "province": str(item["province"]),
            "r_b": float(item["r_b"]),
            "consumed_r_a": float(item["consumed_r_a"]),
            "raw_entering_r_a": float(item["raw_entering_r_a"]),
            "household_composite_wage": float(item["wage"]),
            "tau": float(item["tau"]),
            "transfer_income": float(item["transfer_income"]),
            "borrowing_rate_gap": float(item["borrowing_rate_gap"]),
            "return_guard_state": str(item["return_guard_state"]),
            "wage_guard_state": str(item["wage_guard_state"]),
            "transfer_control_state": str(item["transfer_control_state"]),
            "params": item["params"],
            "accepted_numerics": item["numerics"],
            "accepted_initial_value_sha256": item["initial_value_sha256"],
            "accepted_baseline_labor_sha256": item["baseline_labor_sha256"],
            "provenance_checks_pass": True,
            "input_semantics": {
                "household_composite_wage": "accepted consumed w; not raw wjt",
                "return": "accepted consumed r_a/rah; no return recomputation",
            },
        })
    return {
        "schema": "CH5_MP4C_K1_J160_FIRST_TURN_INPUT_AUTHORITY_V1",
        "pass": True,
        "accepted_candidate": ACCEPTED_COMMIT,
        "accepted_identity_receipts_path": str(path.resolve()),
        "accepted_identity_receipts_sha256": actual_hash,
        "accepted_manifest_path": str(ACCEPTED_MANIFEST_PATH.resolve()),
        "accepted_manifest_sha256": accepted_hjb.file_sha256(ACCEPTED_MANIFEST_PATH),
        "manifest_entry_matches_identity_artifact": bool(
            manifest_entry["sha256"] == actual_hash and manifest_entry["bytes"] == path.stat().st_size
        ),
        "compact_evidence_boundary": (
            "The exact-input artifact is retained and sealed. Historical raw traces listed by the "
            "accepted full manifest are not all repersisted in the compact repository evidence."
        ),
        "province_count": 31,
        "provinces": sealed_rows,
    }


def build_fixture(row: dict[str, Any]) -> accepted_hjb.Fixture:
    params_data = row["params"]
    grid = oracle.MatlabFaithfulHJBGrid(
        np.linspace(-2.0, 20.0, 20),
        np.linspace(0.0, 100.0, 160),
        np.array([0.8, 1.3]),
        np.array([[-1.0 / 3.0, 1.0 / 3.0], [1.0 / 3.0, -1.0 / 3.0]]),
    )
    params = oracle.EconomicParams(
        params_data["rho"], params_data["gamma_c"], params_data["phi"],
        params_data["chi_0"], params_data["chi_1"], params_data["a_bar"],
        params_data["mu_z"], params_data["sigma_z"],
    )
    state = {
        "rah": row["consumed_r_a"], "rb": row["r_b"],
        "rb_gap": row["borrowing_rate_gap"], "Tt": row["transfer_income"],
        "tau": row["tau"], "w": row["household_composite_wage"],
    }
    initial_value, baseline_labor = source_initial_arrays(state, grid, params)
    inputs = oracle.HouseholdInputs(
        row["consumed_r_a"], row["r_b"], row["tau"],
        np.array([row["household_composite_wage"]]), np.zeros(1), np.ones(1),
    )
    numerics = oracle.MatlabFaithfulHJBNumerics(1000.0, 1e-7, 100, 1e-12)
    return accepted_hjb.Fixture(
        grid, params, inputs, initial_value, baseline_labor,
        row["transfer_income"], row["borrowing_rate_gap"], numerics,
    )


def source_identity_receipt() -> dict[str, Any]:
    identities = {
        "accepted_input_artifact": (ACCEPTED_IDENTITY_PATH, ACCEPTED_IDENTITY_SHA256),
        "accepted_historical_manifest": (ACCEPTED_MANIFEST_PATH, ACCEPTED_MANIFEST_SHA256),
        "accepted_review": (ACCEPTED_ACCEPTANCE_PATH, ACCEPTED_ACCEPTANCE_SHA256),
        "accepted_python_hjb": (ORACLE_PATH, ORACLE_SHA256),
        "source_initializer": (INITIALIZER_PATH, INITIALIZER_SHA256),
        "hjb_receipt_runner": (HJB_RECEIPT_RUNNER_PATH, HJB_RECEIPT_RUNNER_SHA256),
        "matlab_source": (MATLAB_PATH, MATLAB_SHA256),
    }
    files = {
        name: {
            "path": str(path.resolve()), "expected_sha256": expected,
            "actual_sha256": accepted_hjb.file_sha256(path),
        }
        for name, (path, expected) in identities.items()
    }
    for item in files.values():
        item["pass"] = item["expected_sha256"] == item["actual_sha256"]
    receipt = {
        "schema": "CH5_MP4C_K1_J160_PROVINCIAL_HJB_SOURCE_IDENTITY_V1",
        "actual_baseline": BASELINE,
        "accepted_first_turn_candidate": ACCEPTED_COMMIT,
        "files": files,
        "matlab_runtime_calls": 0,
    }
    receipt["pass"] = all(item["pass"] for item in files.values())
    return receipt


def input_invariance_receipt(rows: list[dict[str, Any]], fixtures: list[accepted_hjb.Fixture]) -> dict[str, Any]:
    if len(rows) != 31 or len(fixtures) != 31:
        raise _block("input invariance requires exactly 31 rows and fixtures")
    entries = []
    for row, fixture in zip(rows, fixtures):
        expected = {
            "r_a": row["consumed_r_a"], "r_b": row["r_b"], "tau": row["tau"],
            "wage": row["household_composite_wage"],
            "transfer_income": row["transfer_income"],
            "borrowing_rate_gap": row["borrowing_rate_gap"],
        }
        actual = {
            "r_a": fixture.inputs.r_a, "r_b": fixture.inputs.r_b, "tau": fixture.inputs.tau,
            "wage": float(fixture.inputs.wages[0]),
            "transfer_income": fixture.transfer_income,
            "borrowing_rate_gap": fixture.borrowing_rate_gap,
        }
        entries.append({
            "province_index": row["province_index"], "province": row["province"],
            "exact_household_inputs": expected, "fixture_household_inputs": actual,
            "inputs_exact": expected == actual,
            "grid": {"I": 20, "J": 160, "amin": 0.0, "amax": 100.0, "bmin": -2.0, "bmax": 20.0},
            "initial_value_sha256": accepted_hjb.array_sha256(fixture.initial_value),
            "baseline_labor_sha256": accepted_hjb.array_sha256(fixture.baseline_labor),
            "initial_value_finite": bool(np.isfinite(fixture.initial_value).all()),
            "baseline_labor_finite": bool(np.isfinite(fixture.baseline_labor).all()),
            "fresh_source_initialization": True, "warm_start": False,
        })
    receipt = {
        "schema": "CH5_MP4C_K1_J160_PROVINCIAL_HJB_INPUT_INVARIANCE_V1",
        "province_count": 31,
        "fresh_initial_value_object_count": len({id(item.initial_value) for item in fixtures}),
        "fresh_baseline_labor_object_count": len({id(item.baseline_labor) for item in fixtures}),
        "entries": entries,
    }
    receipt["pass"] = bool(
        receipt["fresh_initial_value_object_count"] == 31
        and receipt["fresh_baseline_labor_object_count"] == 31
        and all(item["inputs_exact"] and item["initial_value_finite"] and item["baseline_labor_finite"] for item in entries)
    )
    return receipt


def empty_call_ledger() -> dict[str, Any]:
    ledger = {
        "schema": "CH5_MP4C_K1_J160_PROVINCIAL_HJB_CALL_LEDGER_V1",
        "hjb_budget": 31, "hjb_calls_started": 0, "hjb_calls_completed": 0,
        "kfe_budget": 0, "scientific_retries": 0,
        "engineering_retry_budget": 1, "engineering_retries_used": 0,
        "province_calls": [],
    }
    ledger.update({key: 0 for key in FORBIDDEN_LEDGER_KEYS})
    return ledger


def execute(output_root: Path) -> int:
    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=False)
    source = source_identity_receipt()
    accepted_hjb.write_json(root / "source_identity.json", source)
    if not source["pass"]:
        raise RuntimeError("source identity failed before HJB")
    authority = load_first_turn_authority()
    accepted_hjb.write_json(root / "first_turn_input_authority.json", authority)
    rows = authority["provinces"]
    fixtures = [build_fixture(row) for row in rows]
    invariance = input_invariance_receipt(rows, fixtures)
    accepted_hjb.write_json(root / "input_invariance_receipt.json", invariance)
    if not invariance["pass"]:
        raise RuntimeError("input invariance failed before HJB")
    ledger = empty_call_ledger()
    accepted_hjb.write_json(root / "pre_science_call_ledger.json", ledger)

    for row, fixture in zip(rows, fixtures):
        index = row["province_index"]
        point_id = f"p{index:02d}_{row['province']}"
        fresh = {
            "source": "fresh source-style initialization from sealed consumed household inputs",
            "warm_start": False,
            "initial_value_sha256": accepted_hjb.array_sha256(fixture.initial_value),
            "baseline_labor_sha256": accepted_hjb.array_sha256(fixture.baseline_labor),
        }
        accepted_hjb.write_json(root / f"{point_id}_started.json", {
            "point_id": point_id, "province_index": index, "province": row["province"],
            "household_inputs": {
                "r_b": row["r_b"], "consumed_r_a": row["consumed_r_a"],
                "household_composite_wage": row["household_composite_wage"],
                "tau": row["tau"], "transfer_income": row["transfer_income"],
                "borrowing_rate_gap": row["borrowing_rate_gap"],
            },
            "fresh_initialization": fresh,
        })
        ledger["hjb_calls_started"] += 1
        result, hjb_receipt = accepted_hjb.run_hjb(fixture)
        ledger["hjb_calls_completed"] += 1
        scientific_checks = hjb_receipt.get("scientific_arrays", {})
        point = {
            "point_id": point_id, "province_index": index, "province": row["province"],
            "household_inputs": {
                "r_b": row["r_b"], "consumed_r_a": row["consumed_r_a"],
                "household_composite_wage": row["household_composite_wage"],
                "tau": row["tau"], "transfer_income": row["transfer_income"],
                "borrowing_rate_gap": row["borrowing_rate_gap"],
                "return_guard_state": row["return_guard_state"],
                "wage_guard_state": row["wage_guard_state"],
            },
            "fresh_initialization": fresh,
            "hjb": hjb_receipt,
            "finite_shape_checks": {
                "result_returned": result is not None,
                "all_arrays_finite_shape_valid": scientific_checks.get("all_arrays_finite_shape_valid", False),
                "label_domains_valid": scientific_checks.get("label_domains_valid", False),
            },
            "kfe": {"ran": False, "reason": "KFE budget is zero"},
        }
        accepted_hjb.write_json(root / f"{point_id}_result.json", point)
        ledger["province_calls"].append({
            "call": ledger["hjb_calls_started"], "point_id": point_id,
            "province_index": index, "province": row["province"],
            "classification": hjb_receipt["classification"], "retried": False,
        })
    accepted_hjb.write_json(root / "final_call_ledger.json", ledger)
    accepted_hjb.write_json(root / "execution_complete.json", {
        "status": "EXACT_31_PROVINCE_HJB_EXECUTION_COMPLETE",
        "hjb_calls": ledger["hjb_calls_started"], "kfe_calls": 0,
        "scientific_retries": 0, "results_eligibility": False,
    })
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_root", type=Path)
    return execute(parser.parse_args().output_root)


if __name__ == "__main__":
    raise SystemExit(main())
