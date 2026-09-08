"""Preflight, synthetic tests, and one-process launch. No scientific imports."""
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

REPO = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
BASELINE = Path(r"D:\ProjectTemp\ch5-2018-observable-prefix-replay-20260908-001")
RUNTIME = BASELINE / "source_runtime"
BASE = Path(r"D:\ProjectTemp\ch5-call725-rah-0p07-native-init-20260908-001")
SOURCE_BLOBS = {
    "validators/multi_province/mp4b_python_empirical.py": "b1710ae3c5d8d7baf96e85c932d777fa5f3b908c",
    "validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py": "0033baee136c0328e80ffb8b794a88d4405c976c",
    "validators/multi_province/mp4c_python_annual_production.py": "7473e04418744d745000afb21d84588273cc5bca",
    "exports/matlab_faithful_two_asset_ha.py": "9e7dc9556a2b76811e78f89999abecc045886106",
}
CONSUMED = (
    "capture/call_0725/entry.json", "capture/call_0725/entry.npz",
    "capture/call_0725/hjb_entry.json", "capture/call_0725/hjb_entry.npz",
    "capture/call_0725/native_initialization_return.json", "capture/call_0725/native_initialization_return.npz",
    "capture/call_0725/hjb_return_before_kfe.json", "capture/call_0725/hjb_return_before_kfe.npz",
    "capture/call_0725/kfe_entry.json", "capture/call_0725/kfe_direct_input.json",
    "capture/call_0725/kfe_direct_input.npz", "capture/call_0725/kfe_direct_return.json",
    "capture/call_0725/kfe_direct_return.npz", "capture/terminal.json", "capture/index.jsonl",
)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()


def write(path, value):
    with Path(path).open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, allow_nan=False, indent=2)
        stream.write("\n")


def git(*args):
    return subprocess.run(["git", *args], cwd=REPO, check=True, stdout=subprocess.PIPE).stdout.decode().strip()


def prepare():
    root = BASE
    suffix = 1
    while root.exists():
        suffix += 1
        root = BASE.with_name(BASE.name[:-3] + f"{suffix:03d}")
    root.mkdir()
    assert sha(BASELINE / "manifest_02.json") == "4C18B9AA14C23356594F1A0ECCBA346B3DB2AE668B7204A73D88A226B98B0146"
    manifest = json.loads((BASELINE / "manifest_02.json").read_text(encoding="utf-8"))
    known = {item["path"]: item["sha256"] for section in ("inputs", "captures", "outputs") for item in manifest[section]}
    published_index = next(item for item in manifest["outputs"] if item["path"].replace("\\", "/").endswith("reports/2018_observable_prefix_replay_20260908/capture_index.jsonl"))
    index_rows = [json.loads(line) for line in (BASELINE / "capture/index.jsonl").read_text(encoding="utf-8").splitlines()]
    indexed = {}
    for row in index_rows:
        for key in ("json", "npz"):
            if key in row:
                indexed[row[key]] = row[f"{key}_sha256"]
    consumed = []
    for relative in CONSUMED:
        path = BASELINE / relative
        actual = sha(path)
        expected = indexed.get(str(path), known.get(str(path)))
        if relative == "capture/index.jsonl":
            expected = published_index["sha256"]
        assert expected == actual, relative
        consumed.append({"path": str(path), "sha256": actual, "identity_source": "capture_index" if str(path) in indexed else "manifest_02"})
    sources = []
    for relative, blob in SOURCE_BLOBS.items():
        assert git("rev-parse", f"origin/main:{relative}") == blob
        path = RUNTIME / relative
        expected = hashlib.sha256(subprocess.run(["git", "cat-file", "blob", blob], cwd=REPO, check=True, stdout=subprocess.PIPE).stdout).hexdigest().upper()
        assert sha(path) == expected
        sources.append({"path": str(path), "blob": blob, "raw_sha256": sha(path), "module_runtime": str(RUNTIME)})
    protected = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m")
    assert sha(protected) == "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE"
    disk = shutil.disk_usage(root)
    assert disk.free > 1024 ** 3
    write(root / "preflight.json", {"passed": True, "live_main": git("rev-parse", "origin/main"), "branch": git("branch", "--show-current"), "baseline_manifest_sha256": sha(BASELINE / "manifest_02.json"), "consumed_baseline": consumed, "sources": sources, "protected_HJB_sha256": sha(protected), "disk_free_bytes": disk.free, "scientific_entry": 0, "intervention": {"expression": "float('0.07')", "repr": repr(float("0.07")), "hex": float("0.07").hex()}, "limits": {"native_initialization": 1, "labor_root": 800, "HJB": 1, "HJB_direct_solve": 100, "KFE": 1, "KFE_direct_solve": 1, "aggregate": 1, "science_seconds": 900}})
    print(root)


def tests(root):
    command = [sys.executable, "-B", str(REPO / "tests/test_mp4c_call725_rah_0p07_sensitivity.py")]
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    result = subprocess.run(command, cwd=REPO, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    number = len(list(root.glob("tests_*.raw.json"))) + 1
    raw = result.stdout
    text = raw.decode("utf-8").replace("\r\n", "\n")
    stem = root / f"tests_{number:02d}"
    write(stem.with_suffix(".raw.json"), {"command": command, "returncode": result.returncode, "sha256": hashlib.sha256(raw).hexdigest().upper(), "base64": base64.b64encode(raw).decode()})
    stem.with_suffix(".txt").write_text(text, encoding="utf-8", newline="\n")
    match = re.search(r"Ran (\d+) tests", text)
    receipt = {"passed": result.returncode == 0 and "\nOK\n" in text, "ran": int(match.group(1)) if match else None, "individual_ok": len(re.findall(r" \.\.\. ok$", text, re.M)), "lf_sha256": sha(stem.with_suffix(".txt"))}
    write(stem.with_suffix(".receipt.json"), receipt)
    print(text)
    print(receipt)
    if not receipt["passed"] or receipt["ran"] != receipt["individual_ok"]:
        raise SystemExit(1)


def launch(root):
    preflight = json.loads((root / "preflight.json").read_text(encoding="utf-8"))
    assert preflight["passed"] and preflight["scientific_entry"] == 0
    tests_found = sorted(root.glob("tests_*.receipt.json"))
    assert tests_found and json.loads(tests_found[-1].read_text(encoding="utf-8"))["passed"]
    for source in preflight["sources"]:
        assert sha(source["path"]) == source["raw_sha256"]
    with (root / "launch_marker.json").open("x", encoding="utf-8") as stream:
        json.dump({"created_epoch": time.time(), "scientific_restart_authority": False}, stream)
    env = dict(os.environ)
    for name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
        env[name] = "1"
    env.update(PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1", CH5_RAH07_RUNTIME=str(RUNTIME), CH5_RAH07_BASELINE=str(BASELINE))
    command = [sys.executable, "-B", str(HERE / "run.py"), str(root)]
    with (root / "stdout.txt").open("xb") as stdout, (root / "stderr.txt").open("xb") as stderr:
        process = subprocess.Popen(command, cwd=REPO, env=env, stdout=stdout, stderr=stderr)
        write(root / "launch_receipt.json", {"pid": process.pid, "command": command, "cwd": str(REPO), "start_epoch": time.time(), "runtime": str(RUNTIME), "threads": {name: env[name] for name in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS")}, "observer_sources": {path.name: sha(path) for path in HERE.glob("*.py")}})
        print(json.dumps({"pid": process.pid, "root": str(root)}), flush=True)
        timed_out = False
        try:
            code = process.wait(timeout=900)
        except subprocess.TimeoutExpired:
            timed_out = True
            process.kill()
            code = process.wait()
        write(root / "process_receipt.json", {"returncode": code, "external_timeout": timed_out, "terminal_saved": (root / "science/terminal.json").exists(), "end_epoch": time.time(), "scientific_restart": False})
        print((root / "process_receipt.json").read_text(encoding="utf-8"))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if sys.argv[1] == "prepare":
        prepare()
    elif sys.argv[1] == "tests":
        tests(Path(sys.argv[2]))
    elif sys.argv[1] == "launch":
        launch(Path(sys.argv[2]))
