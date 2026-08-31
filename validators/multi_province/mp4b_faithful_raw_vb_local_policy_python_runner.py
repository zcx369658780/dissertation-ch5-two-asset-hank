"""Direct-file-safe replacement runner for the frozen MP4B local-policy cases."""

from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import sys


THIS_FILE = Path(__file__).resolve()
REPO_ROOT = THIS_FILE.parents[2]
SRC_ROOT = (REPO_ROOT / "src").resolve()
if not SRC_ROOT.is_dir() or SRC_ROOT.parent != REPO_ROOT.resolve():
    raise RuntimeError("wrong repository src root")
sys.path.insert(0, str(SRC_ROOT))

import numpy as np  # noqa: E402
from ch5_two_asset_hank.contracts import EconomicParams, HouseholdInputs  # noqa: E402
from ch5_two_asset_hank.matlab_faithful_policy import (  # noqa: E402
    select_matlab_faithful_local_policy,
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def _verify_origins() -> dict[str, str]:
    origins: dict[str, str] = {}
    for name, module in sorted(sys.modules.items()):
        if name == "chapter5_model" or name.startswith("chapter5_model."):
            raise RuntimeError("historical chapter5_model import detected")
        if name.startswith("ch5_two_asset_hank"):
            origin = getattr(module, "__file__", None)
            if origin is None:
                continue
            resolved = Path(origin).resolve()
            if not resolved.is_relative_to(SRC_ROOT):
                raise RuntimeError(f"outside-repository module origin: {name}={resolved}")
            origins[name] = str(resolved)
    required = {
        "ch5_two_asset_hank.contracts",
        "ch5_two_asset_hank.economics",
        "ch5_two_asset_hank.matlab_faithful_policy",
    }
    if not required <= origins.keys():
        raise RuntimeError("required candidate module origin missing")
    return origins


def _identity() -> dict[str, object]:
    origins = _verify_origins()
    economics = SRC_ROOT / "ch5_two_asset_hank" / "economics.py"
    policy = SRC_ROOT / "ch5_two_asset_hank" / "matlab_faithful_policy.py"
    return {
        "repo_root": str(REPO_ROOT.resolve()),
        "src_root": str(SRC_ROOT),
        "module_origins": origins,
        "candidate_hashes": {
            "economics.py": _sha256(economics),
            "matlab_faithful_policy.py": _sha256(policy),
        },
    }


def _run_cases(manifest_path: Path) -> list[dict[str, object]]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    p = manifest["parameters"]
    params = EconomicParams(
        p["rho"], p["gamma_c"], p["phi"], p["chi_0"], p["chi_1"], p["a_bar"], 0.2, 0.1
    )
    inputs = HouseholdInputs(
        p["r_a"], p["r_b"], p["tau"], np.array([p["wage"]]), np.array([0.0]),
        np.array([p["labor_weight"]]),
    )
    rows = []
    for case in manifest["cases"]:
        result = select_matlab_faithful_local_policy(
            **{key: value for key, value in case.items() if key != "case_id"},
            transfer_income=p["transfer_income"], borrowing_rate_gap=p["borrowing_rate_gap"],
            a_max=p["a_max"], da=p["da"], db=p["db"], inputs=inputs, params=params,
            tolerance=p["drift_tolerance"],
        )
        rows.append({"case_id": case["case_id"], **asdict(result)})
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    identity = _identity()
    if args.smoke:
        payload = {**identity, "case_count": 0, "policy_calls": 0, "rows": []}
    else:
        if args.manifest is None:
            raise ValueError("--manifest is required for scientific execution")
        rows = _run_cases(args.manifest.resolve())
        payload = {**identity, "case_count": len(rows), "policy_calls": len(rows), "rows": rows}
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
