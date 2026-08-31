"""Frozen comparator for preserved MATLAB and replacement Python local policy."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import sys


CONTINUOUS = (
    "consumption", "labor", "transfer", "adjustment_cost", "effective_illiquid_return",
    "mu_a", "mu_b", "utility", "b_backward_rate", "b_forward_rate",
    "a_backward_rate", "a_forward_rate",
)
CATEGORICAL = ("liquid_label", "transfer_label", "liquid_direction", "illiquid_direction")
BEIJING = "beijing_iteration5_5_18_1"


def compare(matlab_rows, python_rows):
    matlab = {row["case_id"]: row for row in matlab_rows}
    python = {row["case_id"]: row for row in python_rows}
    mismatches = []
    maxima = {}
    if list(matlab) != list(python):
        mismatches.append({"field": "case_order", "matlab": list(matlab), "python": list(python)})
    for field in CONTINUOUS:
        worst = {"difference": 0.0, "bound": 0.0, "case_id": None}
        for case_id in matlab.keys() & python.keys():
            x, y = float(matlab[case_id][field]), float(python[case_id][field])
            difference = abs(x - y)
            bound = 128.0 * sys.float_info.epsilon * max(1.0, abs(x), abs(y))
            if difference > worst["difference"]:
                worst = {"difference": difference, "bound": bound, "case_id": case_id}
            if not math.isfinite(difference) or difference > bound:
                mismatches.append({"case_id": case_id, "field": field, "matlab": x, "python": y, "difference": difference, "bound": bound})
        maxima[field] = worst
    for field in CATEGORICAL:
        for case_id in matlab.keys() & python.keys():
            if matlab[case_id][field] != python[case_id][field]:
                mismatches.append({"case_id": case_id, "field": field, "matlab": matlab[case_id][field], "python": python[case_id][field]})
    witness = python.get(BEIJING)
    if witness is None:
        mismatches.append({"case_id": BEIJING, "field": "presence"})
    return {
        "result": "PASS" if not mismatches else "MATERIAL_MISMATCH",
        "case_count": len(python), "beijing_witness": witness, "maxima": maxima,
        "mismatches": mismatches, "tolerance_rule": "128*eps64*max(1,abs(x),abs(y))",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--matlab", type=Path, required=True)
    parser.add_argument("--python", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    matlab = json.loads(args.matlab.read_text(encoding="utf-8"))
    python_payload = json.loads(args.python.read_text(encoding="utf-8"))
    result = compare(matlab, python_payload["rows"])
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(result["result"])
    return 0 if result["result"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
