"""Direct-file-safe source-binding launcher for the frozen 50-state HJB runner."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import runpy
import subprocess
import sys


THIS_FILE = Path(__file__).resolve()
REPO_ROOT = THIS_FILE.parents[2]
SRC_ROOT = (REPO_ROOT / "src").resolve()
if not SRC_ROOT.is_dir() or SRC_ROOT.parent != REPO_ROOT.resolve():
    raise RuntimeError("wrong repository src root")
sys.path.insert(0, str(SRC_ROOT))

import ch5_two_asset_hank.economics  # noqa: E402
import ch5_two_asset_hank.matlab_faithful_hjb  # noqa: E402
import ch5_two_asset_hank.matlab_faithful_operator  # noqa: E402
import ch5_two_asset_hank.matlab_faithful_policy  # noqa: E402


EXPECTED_OBJECTS = {
    "economics.py": "810e0875febc873ae85bef7e88edd4de349b00b2",
    "matlab_faithful_policy.py": "2021db630f3057026ffc37d375a43aaddbccec48",
}
EXPECTED_SHA256 = {
    "matlab_faithful_operator.py": "0C9F6C1AE3E6428E49086DE900BE55D5038A10144EC061EDDFB9E7249A4A1AAC",
    "matlab_faithful_hjb.py": "924831362C904A253D8AD6011FE9BB4C099C6DF4268D0C2AA30AB9139569F1DE",
}


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def _verify() -> dict[str, object]:
    origins = {}
    for name, module in sorted(sys.modules.items()):
        if name == "chapter5_model" or name.startswith("chapter5_model."):
            raise RuntimeError("historical chapter5_model import detected")
        if name.startswith("ch5_two_asset_hank"):
            origin = getattr(module, "__file__", None)
            if origin:
                path = Path(origin).resolve()
                if not path.is_relative_to(SRC_ROOT):
                    raise RuntimeError(f"outside repository module: {name}={path}")
                origins[name] = str(path)
    package = SRC_ROOT / "ch5_two_asset_hank"
    objects = {}
    for filename, expected in EXPECTED_OBJECTS.items():
        relative = f"src/ch5_two_asset_hank/{filename}"
        actual = subprocess.check_output(
            ["git", "hash-object", relative], cwd=REPO_ROOT, text=True
        ).strip()
        if actual != expected:
            raise RuntimeError(f"candidate Git object mismatch: {filename}={actual}")
        objects[filename] = actual
    hashes = {}
    for filename, expected in EXPECTED_SHA256.items():
        actual = _sha256(package / filename)
        if actual != expected:
            raise RuntimeError(f"source SHA mismatch: {filename}={actual}")
        hashes[filename] = actual
    return {
        "repo_root": str(REPO_ROOT.resolve()), "src_root": str(SRC_ROOT),
        "module_origins": origins, "candidate_git_objects": objects,
        "unchanged_source_hashes": hashes,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--smoke-output", type=Path)
    parser.add_argument("--runner", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--initialization", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    identity = _verify()
    if args.smoke:
        if args.smoke_output is None or args.smoke_output.exists():
            raise ValueError("fresh --smoke-output is required")
        args.smoke_output.write_text(
            json.dumps({**identity, "hjb_calls": 0, "hjb_iterations": 0}, indent=2, sort_keys=True),
            encoding="utf-8",
        )
        return 0
    required = (args.runner, args.manifest, args.initialization, args.output)
    if any(value is None for value in required) or args.output.exists():
        raise ValueError("fresh runner/manifest/initialization/output paths are required")
    sys.argv = [str(args.runner), str(args.manifest), str(args.initialization), str(args.output)]
    runpy.run_path(str(args.runner.resolve()), run_name="__main__")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
