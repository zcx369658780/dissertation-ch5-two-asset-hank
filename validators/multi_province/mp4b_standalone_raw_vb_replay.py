"""One-shot standalone-only raw-Vb helper and local-policy replay."""
from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

import numpy as np

REPO = Path(__file__).resolve().parents[2]
STANDALONE = REPO / "exports" / "matlab_faithful_two_asset_ha.py"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def load_module():
    spec = importlib.util.spec_from_file_location("mp4b_standalone_candidate", STANDALONE)
    if spec is None or spec.loader is None:
        raise RuntimeError("standalone import spec unavailable")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    if Path(module.__file__).resolve() != STANDALONE.resolve():
        raise RuntimeError("standalone origin mismatch")
    return module


def classify(value: float) -> str:
    if math.isnan(value):
        return "NaN"
    if math.isinf(value):
        return "+Inf" if value > 0 else "-Inf"
    return "finite"


def helper_replay(module, manifest: dict) -> dict:
    params = module.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)
    rows = []
    mismatches = []
    for source in manifest["cases"]:
        value = module.transfer_candidate_matlab_faithful_raw_vb(
            source["pa"], source["pb"], source["a"], params
        )
        actual_class = classify(value)
        row = {"case_id": source["case_id"], "output_class": actual_class,
               "output_value": None if actual_class != "finite" else format(value, ".17g"),
               "negative_zero": actual_class == "finite" and value == 0.0 and math.copysign(1.0, value) < 0}
        rows.append(row)
        if actual_class != source["output_class"]:
            mismatches.append({"case_id": source["case_id"], "field": "output_class"})
        elif actual_class == "finite":
            expected = float(source["output_value"])
            bound = 128 * sys.float_info.epsilon * max(1.0, abs(expected), abs(value))
            if abs(expected - value) > bound or (expected == 0.0 and math.copysign(1.0, expected) != math.copysign(1.0, value)):
                mismatches.append({"case_id": source["case_id"], "field": "output_value",
                                   "difference": abs(expected-value), "bound": bound})
    return {"case_count": len(rows), "helper_calls": len(rows), "rows": rows,
            "mismatches": mismatches, "result": "PASS" if not mismatches else "MATERIAL_MISMATCH"}


def policy_replay(module, manifest: dict, matlab_rows: list[dict]) -> dict:
    p = manifest["parameters"]
    params = module.EconomicParams(p["rho"], p["gamma_c"], p["phi"], p["chi_0"],
                                   p["chi_1"], p["a_bar"], 0.2, 0.1)
    inputs = module.HouseholdInputs(p["r_a"], p["r_b"], p["tau"], np.array([p["wage"]]),
                                    np.array([0.0]), np.array([p["labor_weight"]]))
    rows = []
    for case in manifest["cases"]:
        result = module.select_matlab_faithful_local_policy(
            **{k: v for k, v in case.items() if k != "case_id"},
            transfer_income=p["transfer_income"], borrowing_rate_gap=p["borrowing_rate_gap"],
            a_max=p["a_max"], da=p["da"], db=p["db"], inputs=inputs, params=params,
            tolerance=p["drift_tolerance"])
        rows.append({"case_id": case["case_id"], **asdict(result)})
    expected = {r["case_id"]: r for r in matlab_rows}; actual = {r["case_id"]: r for r in rows}
    continuous = ("consumption","labor","transfer","adjustment_cost","effective_illiquid_return",
                  "mu_a","mu_b","utility","b_backward_rate","b_forward_rate","a_backward_rate","a_forward_rate")
    categorical = ("liquid_label","transfer_label","liquid_direction","illiquid_direction")
    mismatches = []
    if list(expected) != list(actual):
        mismatches.append({"field": "case_order"})
    for case_id in expected.keys() & actual.keys():
        for field in categorical:
            if expected[case_id][field] != actual[case_id][field]:
                mismatches.append({"case_id": case_id, "field": field})
        for field in continuous:
            x, y = float(expected[case_id][field]), float(actual[case_id][field])
            bound = 128 * sys.float_info.epsilon * max(1.0, abs(x), abs(y))
            if not math.isfinite(abs(x-y)) or abs(x-y) > bound:
                mismatches.append({"case_id": case_id, "field": field, "difference": abs(x-y), "bound": bound})
    return {"case_count": len(rows), "policy_calls": len(rows), "comparator_calls": 1,
            "beijing_witness": actual.get("beijing_iteration5_5_18_1"), "rows": rows,
            "mismatches": mismatches, "result": "PASS" if not mismatches else "MATERIAL_MISMATCH"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--edge", type=Path, required=True)
    parser.add_argument("--policy-manifest", type=Path, required=True)
    parser.add_argument("--matlab-policy", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    module = load_module()
    payload = {"standalone_path": str(STANDALONE.resolve()), "standalone_sha256": sha(STANDALONE),
               "edge_manifest_sha256": sha(args.edge), "policy_manifest_sha256": sha(args.policy_manifest),
               "matlab_policy_sha256": sha(args.matlab_policy)}
    payload["helper_replay"] = helper_replay(module, json.loads(args.edge.read_text(encoding="utf-8")))
    payload["policy_replay"] = policy_replay(module,
        json.loads(args.policy_manifest.read_text(encoding="utf-8")),
        json.loads(args.matlab_policy.read_text(encoding="utf-8")))
    payload["call_ledger"] = {"standalone_helper": 10, "standalone_local_policy": 12,
        "standalone_comparator": 1, "matlab_scalar": 0, "matlab_local_policy": 0,
        "matlab_household": 0, "python_household": 0, "hjb_50state": 0, "stationary": 0,
        "mp2": 0, "mp3": 0, "annual_batch_shocks_dynamics_irf_r5_results": 0}
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False)+"\n", encoding="utf-8")
    return 0 if payload["helper_replay"]["result"] == payload["policy_replay"]["result"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
