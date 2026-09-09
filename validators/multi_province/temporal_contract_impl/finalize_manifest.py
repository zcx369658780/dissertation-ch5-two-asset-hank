from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys


def digest(path: Path) -> str:
    value = sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest().upper()


def main() -> int:
    if len(sys.argv) < 4:
        raise SystemExit("usage: finalize_manifest.py REPO_ROOT EVIDENCE_ROOT PATH...")
    repo_root, evidence_root = Path(sys.argv[1]), Path(sys.argv[2])
    entries = []
    for raw in sys.argv[3:]:
        path = Path(raw)
        if not path.is_absolute():
            path = repo_root / path
        if not path.is_file():
            raise FileNotFoundError(path)
        entries.append({"path": str(path.resolve()), "bytes": path.stat().st_size, "sha256": digest(path)})
    for path in sorted(item for item in evidence_root.rglob("*") if item.is_file() and item.name != "manifest.json"):
        entries.append({"path": str(path.relative_to(evidence_root)), "bytes": path.stat().st_size, "sha256": digest(path)})
    payload = {
        "schema": "CH5_TEMPORAL_CONTRACT_IMPLEMENTATION_EVIDENCE_MANIFEST_V1",
        "entries": entries,
        "entry_count": len(entries),
    }
    target = evidence_root / "manifest.json"
    target.write_text(json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    readback = json.loads(target.read_text(encoding="utf-8"))
    if readback != payload or any(item["sha256"] != digest(Path(item["path"]) if Path(item["path"]).is_absolute() else evidence_root / item["path"]) for item in entries):
        raise ValueError("manifest readback verification failed")
    print(json.dumps({"manifest": str(target), "sha256": digest(target), "entry_count": len(entries)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
