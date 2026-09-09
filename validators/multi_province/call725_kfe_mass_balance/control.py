"""Capture real synthetic-test logs for the zero-science attribution task."""

import base64
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys


REPO = Path(__file__).resolve().parents[3]
TEST = REPO / "tests/test_mp4c_call725_kfe_mass_balance.py"


def write(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main(root, output):
    root = Path(root).resolve()
    output = Path(output).resolve()
    root.mkdir(parents=True, exist_ok=True)
    output.mkdir(parents=True, exist_ok=True)
    command = [sys.executable, "-B", str(TEST)]
    environment = dict(os.environ)
    environment["PYTHONIOENCODING"] = "utf-8"
    result = subprocess.run(command, cwd=REPO, env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    number = len(list(root.glob("tests_*.raw.json"))) + 1
    stem = root / f"tests_{number:02d}"
    raw = result.stdout
    text = raw.decode("utf-8").replace("\r\n", "\n")
    write(stem.with_suffix(".raw.json"), {"command": command, "returncode": result.returncode, "sha256": hashlib.sha256(raw).hexdigest().upper(), "base64": base64.b64encode(raw).decode()})
    stem.with_suffix(".txt").write_text(text, encoding="utf-8", newline="\n")
    match = re.search(r"Ran (\d+) tests", text)
    receipt = {
        "passed": result.returncode == 0 and "\nOK\n" in text,
        "ran": int(match.group(1)) if match else None,
        "individual_ok": len(re.findall(r" \.\.\. ok$", text, re.M)),
        "LF_sha256": hashlib.sha256(text.encode()).hexdigest().upper(),
        "scientific_calls": 0,
        "solver_calls": 0,
    }
    write(stem.with_suffix(".receipt.json"), receipt)
    for path in root.glob(f"tests_{number:02d}.*"):
        shutil.copyfile(path, output / path.name)
    print(text)
    print(json.dumps(receipt))
    if not receipt["passed"] or receipt["ran"] != receipt["individual_ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
