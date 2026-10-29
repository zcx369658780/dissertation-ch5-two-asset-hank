"""One scientific child per phase; external 30s timeout, no retries or tuning."""
from __future__ import annotations
import argparse
import ctypes
from ctypes import wintypes
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

REPORT = Path(__file__).resolve().parent
WORK = REPORT.parents[1]
EV = REPORT / "evidence"
ENTRY = "validators/multi_province/temp31_real_ha_tinygrid_smoke_isolated.py"
THREAD_KEYS = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
               "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "BLIS_NUM_THREADS")


def write_json(path, value):
    with path.open("x", encoding="utf-8", newline="\n") as f:
        json.dump(value, f, indent=2); f.write("\n")


def restrict_memory(process):
    """Windows process-commit cap, not a claim of a separately measured RSS cap."""
    if os.name != "nt":
        return None, {"status": "MEMORY_HARD_LIMIT_UNAVAILABLE", "reason": "Windows Job API unavailable"}, None
    class IO_COUNTERS(ctypes.Structure):
        _fields_ = [(name, ctypes.c_ulonglong) for name in
                    ("ReadOperationCount", "WriteOperationCount", "OtherOperationCount",
                     "ReadTransferCount", "WriteTransferCount", "OtherTransferCount")]
    class BASIC(ctypes.Structure):
        _fields_ = [("PerProcessUserTimeLimit", ctypes.c_longlong), ("PerJobUserTimeLimit", ctypes.c_longlong),
                    ("LimitFlags", wintypes.DWORD), ("MinimumWorkingSetSize", ctypes.c_size_t),
                    ("MaximumWorkingSetSize", ctypes.c_size_t), ("ActiveProcessLimit", wintypes.DWORD),
                    ("Affinity", ctypes.c_size_t), ("PriorityClass", wintypes.DWORD), ("SchedulingClass", wintypes.DWORD)]
    class EXTENDED(ctypes.Structure):
        _fields_ = [("BasicLimitInformation", BASIC), ("IoInfo", IO_COUNTERS),
                    ("ProcessMemoryLimit", ctypes.c_size_t), ("JobMemoryLimit", ctypes.c_size_t),
                    ("PeakProcessMemoryUsed", ctypes.c_size_t), ("PeakJobMemoryUsed", ctypes.c_size_t)]
    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel.CreateJobObjectW.argtypes = (ctypes.c_void_p, wintypes.LPCWSTR)
    kernel.CreateJobObjectW.restype = wintypes.HANDLE
    kernel.SetInformationJobObject.argtypes = (wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD)
    kernel.SetInformationJobObject.restype = wintypes.BOOL
    kernel.AssignProcessToJobObject.argtypes = (wintypes.HANDLE, wintypes.HANDLE)
    kernel.AssignProcessToJobObject.restype = wintypes.BOOL
    kernel.CloseHandle.argtypes = (wintypes.HANDLE,)
    kernel.CloseHandle.restype = wintypes.BOOL
    kernel.QueryInformationJobObject.argtypes = (wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD, ctypes.c_void_p)
    kernel.QueryInformationJobObject.restype = wintypes.BOOL
    job = kernel.CreateJobObjectW(None, None)
    if not job:
        return None, {"status": "MEMORY_HARD_LIMIT_UNAVAILABLE", "winerror": ctypes.get_last_error()}, None
    info = EXTENDED()
    info.BasicLimitInformation.LimitFlags = 0x100 | 0x2000 | 0x8
    info.BasicLimitInformation.ActiveProcessLimit = 1
    info.ProcessMemoryLimit = 1024 ** 3
    if not kernel.SetInformationJobObject(job, 9, ctypes.byref(info), ctypes.sizeof(info)):
        error = ctypes.get_last_error(); kernel.CloseHandle(job)
        return None, {"status": "MEMORY_HARD_LIMIT_UNAVAILABLE", "winerror": error}, None
    if not kernel.AssignProcessToJobObject(job, wintypes.HANDLE(int(process._handle))):
        error = ctypes.get_last_error(); kernel.CloseHandle(job)
        return None, {"status": "MEMORY_HARD_LIMIT_UNAVAILABLE", "winerror": error}, None
    def close():
        observed = EXTENDED()
        peak = None
        if kernel.QueryInformationJobObject(job, 9, ctypes.byref(observed), ctypes.sizeof(observed), None):
            peak = int(observed.PeakProcessMemoryUsed)
        kernel.CloseHandle(job)
        return peak
    return job, {"status": "PROCESS_MEMORY_HARD_LIMIT_ENFORCED", "bytes": 1024 ** 3,
                 "kind": "Windows Job process committed memory", "RSS_hard_cap": "NOT_SEPARATELY_ENFORCED",
                 "active_process_limit": 1, "kill_on_job_close": True,
                 "applied_before_scientific_import_handshake": True}, close


def redact(raw):
    output = raw; changes = []
    for prefix, label in ((str(WORK), "<ISOLATED_CANDIDATE_ROOT>"),
                          (str(Path(sys.executable).parent), "<PYTHON_RUNTIME_ROOT>")):
        variants = {prefix, prefix.replace("\\", "/"), json.dumps(prefix)[1:-1]}
        for variant in sorted(variants, key=len, reverse=True):
            needle = variant.encode(); count = output.count(needle)
            if count:
                output = output.replace(needle, label.encode())
                changes.append({"prefix_category": label, "prefix_sha256": hashlib.sha256(needle).hexdigest(), "replacements": count})
    return output, changes


def main(phase, source_root):
    number = 1 if phase == "import-initial-policy" else 2
    budget_path = REPORT / "test_command_budget.json"
    budget = json.loads(budget_path.read_text(encoding="utf-8"))
    assert budget["commands_started"] == number - 1, "STOP_COMMAND_BUDGET_OR_REPEAT"
    if number == 2:
        prior = json.loads((EV / "phase_1_receipt.json").read_text(encoding="utf-8"))
        assert prior["exit_code"] == 0 and prior["passed"] and not prior["timed_out"], "STOP_PHASE1_FAILED"
    command = [sys.executable, "-B", ENTRY, "--phase", phase, "--source-root", str(source_root)]
    claim = {"command_number": number, "phase": phase, "command": ["python", "-B", *command[2:]],
             "working_directory": "<ISOLATED_CANDIDATE_ROOT>", "hard_timeout_seconds": 30,
             "source_commit": "b4f5471aeca304f60da4bd2340e4238561c5a92d",
             "entry_sha256": hashlib.sha256((WORK / ENTRY).read_bytes()).hexdigest(),
             "supervisor_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             "parameter_file_sha256": hashlib.sha256((REPORT / "grid_and_parameters.json").read_bytes()).hexdigest(),
             "claimed_at_utc": datetime.now(timezone.utc).isoformat(),
             "science_child_processes": 1, "retry_allowed": False,
             "phase_limits": {"initializer_batches": 1, "root_cells": 8,
                             "direct_policy_cells": 1 if number == 1 else 0,
                             "hjb_driver_calls": 0 if number == 1 else 1,
                             "hjb_iterations": 0 if number == 1 else 1,
                             "hjb_policy_cells": 0 if number == 1 else 8, "KFE_GE_IRF": 0}}
    write_json(EV / f"phase_{number}_claim.json", claim)
    budget["commands_started"] = number
    budget_path.write_text(json.dumps(budget, indent=2) + "\n", encoding="utf-8", newline="\n")
    env = dict(os.environ, **{key: "1" for key in THREAD_KEYS}, PYTHONDONTWRITEBYTECODE="1", PYTHONNOUSERSITE="1")
    env.pop("PYTHONPATH", None)
    start = time.monotonic()
    process = subprocess.Popen(command, cwd=WORK, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    close_job = None
    timed_out = False
    memory = {"status": "MEMORY_HARD_LIMIT_UNAVAILABLE"}
    try:
        _, memory, close_job = restrict_memory(process)
        stdout, stderr = process.communicate(input=b"GO\n", timeout=max(0.001, 30 - (time.monotonic() - start)))
    except subprocess.TimeoutExpired:
        timed_out = True; process.kill(); stdout, stderr = process.communicate()
    except BaseException:
        process.kill(); process.communicate()
        raise
    finally:
        if close_job is not None:
            memory["observed_peak_process_committed_bytes"] = close_job()
    elapsed = time.monotonic() - start
    (EV / f"LOCAL_ONLY_phase_{number}_stdout_raw.txt").write_bytes(stdout)
    (EV / f"LOCAL_ONLY_phase_{number}_stderr_raw.txt").write_bytes(stderr)
    public_stdout, stdout_changes = redact(stdout)
    public_stderr, stderr_changes = redact(stderr)
    (EV / f"phase_{number}_stdout_public.txt").write_bytes(public_stdout)
    (EV / f"phase_{number}_stderr_public.txt").write_bytes(public_stderr)
    events = [json.loads(line) for line in stdout.decode("utf-8", "replace").splitlines() if line.startswith('{"event":')]
    final = next((item for item in reversed(events) if item["event"] == "phase_result"), None)
    passed = process.returncode == 0 and not timed_out and final is not None and final["outcome"] == "PASS_BOUNDED_RUNTIME_SMOKE"
    if final:
        for key in ("initializer_batches", "root_cells", "direct_policy_cells", "hjb_driver_calls", "hjb_policy_cells"):
            budget[key] = budget.get(key, 0) + final["counts"][key]
    budget["phase_" + str(number)] = "PASS_BOUNDED_RUNTIME_SMOKE" if passed else "FAILED_STOP_NO_RETRY"
    if not passed:
        budget["future_phase"] = "NOT_EXECUTED_AFTER_FAILURE"
    budget_path.write_text(json.dumps(budget, indent=2) + "\n", encoding="utf-8", newline="\n")
    redaction = {"transformation": "exact workspace/runtime prefix replacements only; original bytes retained LOCAL_ONLY",
                 "stdout": {"raw_bytes": len(stdout), "raw_sha256": hashlib.sha256(stdout).hexdigest(),
                            "public_bytes": len(public_stdout), "public_sha256": hashlib.sha256(public_stdout).hexdigest(), "changes": stdout_changes},
                 "stderr": {"raw_bytes": len(stderr), "raw_sha256": hashlib.sha256(stderr).hexdigest(),
                            "public_bytes": len(public_stderr), "public_sha256": hashlib.sha256(public_stderr).hexdigest(), "changes": stderr_changes}}
    write_json(EV / f"phase_{number}_redaction_record.json", redaction)
    public_events = [json.loads(line) for line in public_stdout.decode("utf-8", "replace").splitlines() if line.startswith('{"event":')]
    public_final = next((item for item in reversed(public_events) if item["event"] == "phase_result"), None)
    receipt = {"phase": phase, "command_number": number, "exit_code": process.returncode,
               "passed": passed, "timed_out": timed_out, "hard_timeout_seconds": 30,
               "elapsed_seconds": elapsed, "memory_limit": memory, "science_child_processes": 1,
               "final_event": public_final, "raw_log_identity": redaction, "retries": 0}
    write_json(EV / f"phase_{number}_receipt.json", receipt)
    print(public_stdout.decode("utf-8", "replace"))
    if public_stderr:
        print(public_stderr.decode("utf-8", "replace"), file=sys.stderr)
    print(json.dumps(receipt), flush=True)
    return 0 if passed else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", choices=("import-initial-policy", "tiny-hjb-one-iteration"), required=True)
    parser.add_argument("--source-root", type=Path, default=Path("src"))
    args = parser.parse_args()
    raise SystemExit(main(args.phase, args.source_root))
