"""Static raw-candidate adjustment-cost scale analysis; performs no model call."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from .finalize import THRESHOLDS, chunk_paths, distribution


def analyze(evidence: Path) -> dict:
    costs = []
    threshold_costs = {threshold: [] for threshold in THRESHOLDS}
    for path in chunk_paths(Path(evidence)):
        with np.load(path, allow_pickle=False) as payload:
            raw = np.asarray(payload["raw_d"], dtype=np.float64)
            a = np.asarray(payload["grid_a"], dtype=np.float64)
            scale = np.maximum(a, 1e-6)[None, None, None, :, None]
            cost = 0.1 * np.abs(raw) + raw**2 / scale
            flat_d, flat_cost = raw.reshape(-1), cost.reshape(-1)
            costs.append(flat_cost)
            for threshold in THRESHOLDS:
                threshold_costs[threshold].append(flat_cost[np.abs(flat_d) > threshold])
    all_costs = np.concatenate(costs)
    result = {
        "schema": "CH5_K1_TRANSFER_RAW_CANDIDATE_ADJUSTMENT_COST_SCALE_V1",
        "formula": "chi0*abs(d)+0.5*chi1*d^2/max(a,a_bar)",
        "chi0": 0.1, "chi1_years": 2.0, "a_bar": 1e-6,
        "population": int(all_costs.size),
        "distribution": distribution(all_costs),
        "by_abs_d_threshold": [],
        "scientific_calls": 0,
    }
    for threshold in THRESHOLDS:
        values = np.concatenate(threshold_costs[threshold])
        result["by_abs_d_threshold"].append({"abs_d_threshold": threshold, **distribution(values)})
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", type=Path)
    args = parser.parse_args()
    print(json.dumps(analyze(args.evidence), ensure_ascii=False, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
