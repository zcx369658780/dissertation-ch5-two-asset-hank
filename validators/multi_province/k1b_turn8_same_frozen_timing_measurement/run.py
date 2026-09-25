"""Future-only C8-input timing measurement; import and default CLI are static.

The science path reuses the accepted C8 runner in memory. It requires a later,
committed Owner measurement contract and execution task. This file grants neither.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping
from zoneinfo import ZoneInfo

REPOSITORY = Path(__file__).resolve().parents[3]
OUTPUT = Path("reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001")
MEASUREMENT_RUNNER = Path("validators/multi_province/k1b_turn8_same_frozen_timing_measurement/run.py")
ACCEPTED_RUNNER = Path("validators/multi_province/k1b_turn8_outer_r2/run.py")
ACCEPTED_RUNNER_SHA = "10920535BD50E688D1794B7E69C34F8A5C3C56456CAF6E8DF52FA8D9DFE31831"
SRC_TREE = "00682b2e1a7ba23665f6e16f6acf48ad35874883"
C7_ROOT = Path("reports/ch5_k1b_turn7_outer_r2_20260925_run001")
C7_MANIFEST_SHA = "413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91"
C7_ENTERING_SHA = "20861D4ADDBDF1099854EB86B00D24A097C627838B3F6EF5AFAEDABFFD647E5E"
C7_READBACK_SHA = "5EB75667132473C2F283666B0F3B73BB18FDF00A83C09382827E4C44958246FA"
TASK_ID = "CH5_K1B_TURN8_SAME_FROZEN_TIMING_MEASUREMENT_EXECUTION"
TASK_STATUS = "ACTIVE__ONE_SHOT_SEPARATE_C8_TIMING_MEASUREMENT"
TASK_COPY = Path("tasks/CH5_K1B_TURN8_SAME_FROZEN_TIMING_MEASUREMENT_EXECUTION.md")
OWNER_ADOPTION = Path("docs/CH5_K1B_TURN8_SAME_FROZEN_TIMING_MEASUREMENT_OWNER_ADOPTION.md")
CONTRACT = Path("tasks/CH5_K1B_TURN8_SAME_FROZEN_TIMING_MEASUREMENT_CONTRACT.json")
PREPARATION_TASK_ID = "CH5_K1B_TURN8_SAME_FROZEN_TIMING_RUNNER_ZERO_SCIENCE_PREPARATION_20260925"


class TimingBlocked(RuntimeError):
    def __init__(self, terminal: str, detail: Any = None):
        super().__init__(terminal)
        self.terminal, self.detail = terminal, detail


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()


def committed_file(repo: Path, relative: Path) -> str:
    """Return the worktree digest only when it matches the committed blob."""
    path = repo / relative
    if not path.is_file() or git(repo, "status", "--porcelain=v1", "--", relative.as_posix()):
        raise TimingBlocked("BLOCKED__MEASUREMENT_AUTHORITY_DIRTY_OR_MISSING", relative.as_posix())
    try:
        blob = subprocess.check_output(["git", "show", f"HEAD:{relative.as_posix()}"], cwd=repo,
                                       stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as exc:
        raise TimingBlocked("BLOCKED__MEASUREMENT_AUTHORITY_NOT_COMMITTED", relative.as_posix()) from exc
    digest = sha(path)
    if digest != hashlib.sha256(blob).hexdigest().upper():
        raise TimingBlocked("BLOCKED__MEASUREMENT_AUTHORITY_NOT_COMMITTED", relative.as_posix())
    return digest


def accepted_runner(repo: Path):
    if committed_file(repo, ACCEPTED_RUNNER) != ACCEPTED_RUNNER_SHA:
        raise TimingBlocked("BLOCKED__ACCEPTED_C8_RUNNER_IDENTITY")
    spec = importlib.util.spec_from_file_location("accepted_c8_timing_delegate", repo / ACCEPTED_RUNNER)
    if spec is None or spec.loader is None:
        raise TimingBlocked("BLOCKED__ACCEPTED_C8_RUNNER_LOAD")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def static_preflight(repo: Path = REPOSITORY) -> dict[str, Any]:
    """Read-only identity check. No output root and no model import."""
    repo = repo.resolve()
    checks = {
        "repository": git(repo, "rev-parse", "--show-toplevel").replace("\\", "/").casefold()
                      == repo.as_posix().casefold(),
        "src_tree": git(repo, "rev-parse", "HEAD:src") == SRC_TREE,
        "src_clean": not git(repo, "status", "--porcelain=v1", "--", "src"),
        "candidate_absent": not os.path.lexists(repo / OUTPUT),
        "c7_manifest": sha(repo / C7_ROOT / "execution_artifact_manifest.json") == C7_MANIFEST_SHA,
        "c7_entering": sha(repo / C7_ROOT / "turn8_entering_bundle_manifest.json") == C7_ENTERING_SHA,
        "c7_readback": sha(repo / C7_ROOT / "turn8_entering_bundle_readback.json") == C7_READBACK_SHA,
        "accepted_runner": committed_file(repo, ACCEPTED_RUNNER) == ACCEPTED_RUNNER_SHA,
    }
    if not all(checks.values()):
        raise TimingBlocked("BLOCKED__STATIC_MEASUREMENT_IDENTITY", checks)
    c8 = accepted_runner(repo)
    previous = c8.OUTPUT
    try:
        c8.OUTPUT = OUTPUT
        delegated = c8.preflight(repo)
    finally:
        c8.OUTPUT = previous
    if not all(delegated["checks"].values()) or delegated["C7_entering"]["json"] != c8.SEALED["turn8_k1b_input_candidate.json"]:
        raise TimingBlocked("BLOCKED__ACCEPTED_C8_PREFLIGHT")
    return {"status": "PASS__STATIC_PREFLIGHT_ONLY", "checks": checks,
            "delegated_checks": delegated["checks"], "src_tree": SRC_TREE,
            "c7_entering": delegated["C7_entering"],
            "measurement_output_candidate": str(repo / OUTPUT), "scientific_calls": 0,
            "duration_upper_bound_claim": False}


def clock_sample(clock: Any = time, utc_now: Any = None) -> dict[str, Any]:
    utc_now = utc_now or (lambda: datetime.now(timezone.utc))
    mono = clock.monotonic_ns()
    utc = utc_now()
    if utc.tzinfo is None or utc.utcoffset() is None:
        raise TimingBlocked("BLOCKED__CLOCK_MAPPING_INVALID")
    utc = utc.astimezone(timezone.utc)
    return {"monotonic_ns": mono, "utc": utc.isoformat(),
            "asia_shanghai": utc.astimezone(ZoneInfo("Asia/Shanghai")).isoformat(),
            "timezone": "Asia/Shanghai"}


def elapsed_clock(start: Mapping[str, Any], end: Mapping[str, Any]) -> int:
    try:
        ns = int(end["monotonic_ns"]) - int(start["monotonic_ns"])
        wall = (datetime.fromisoformat(end["utc"]) - datetime.fromisoformat(start["utc"])).total_seconds()
    except (KeyError, TypeError, ValueError) as exc:
        raise TimingBlocked("BLOCKED__CLOCK_MAPPING_INVALID") from exc
    # Engineering clock-consistency guard, not a science tolerance or duration bound.
    if ns < 0 or wall < 0 or abs(wall - ns / 1e9) > 2.0:
        raise TimingBlocked("BLOCKED__CLOCK_MAPPING_INVALID")
    return ns


def _contract_numbers(value: Any, candidate: Mapping[str, int]) -> dict[str, int]:
    if not isinstance(value, dict) or set(value) != set(candidate):
        raise TimingBlocked("BLOCKED__MEASUREMENT_BUDGET_CATEGORY_SET")
    if any(type(value[key]) is not int or not 0 <= value[key] <= candidate[key] for key in candidate):
        raise TimingBlocked("BLOCKED__MEASUREMENT_BUDGET_VALUE")
    return dict(value)


def future_gate(repo: Path, execution_id: str | None, c8: Any) -> dict[str, Any]:
    """Every authority and identity check precedes output creation and science."""
    if not execution_id or re.fullmatch(r"[A-Za-z0-9_-]{1,80}", execution_id) is None:
        raise TimingBlocked("EXECUTION_AUTHORIZATION_REQUIRED")
    committed_file(repo, MEASUREMENT_RUNNER)
    current = committed_file(repo, Path("TASK_CURRENT.md"))
    task = (repo / "TASK_CURRENT.md").read_text(encoding="utf-8")
    required = (f"Task ID: `{TASK_ID}`", f"Status: `{TASK_STATUS}`",
                f"Execution authorization ID: `{execution_id}`",
                f"Authorized output root: `{OUTPUT.as_posix()}`")
    if not all(field in task for field in required):
        raise TimingBlocked("BLOCKED__FRESH_MEASUREMENT_TASK_GATE")
    if committed_file(repo, TASK_COPY) != current or not all(
            field in (repo / TASK_COPY).read_text(encoding="utf-8") for field in required):
        raise TimingBlocked("BLOCKED__MEASUREMENT_TASK_COPY")
    adoption_sha = committed_file(repo, OWNER_ADOPTION)
    contract_sha = committed_file(repo, CONTRACT)
    if f"Owner adoption SHA-256: `{adoption_sha}`" not in task or f"Measurement contract SHA-256: `{contract_sha}`" not in task:
        raise TimingBlocked("BLOCKED__MEASUREMENT_CONTRACT_BINDING")
    adoption = (repo / OWNER_ADOPTION).read_text(encoding="utf-8")
    if (f"Execution authorization ID: `{execution_id}`" not in adoption or
            f"Authorized output root: `{OUTPUT.as_posix()}`" not in adoption or
            f"Measurement contract SHA-256: `{contract_sha}`" not in adoption or
            "OWNER_ADOPTED__SEPARATE_SINGLE_C8_TIMING_BUDGET" not in adoption):
        raise TimingBlocked("BLOCKED__OWNER_MEASUREMENT_ADOPTION")
    contract = json.loads((repo / CONTRACT).read_text(encoding="utf-8"))
    if (contract.get("schema") != "CH5_K1B_SEPARATE_SINGLE_C8_TIMING_CONTRACT_V1" or
            contract.get("execution_id") != execution_id or
            contract.get("output_root") != OUTPUT.as_posix() or
            contract.get("attempts") != 1 or
            contract.get("budget_namespace") != "SEPARATE_C8_TIMING_ONLY" or
            contract.get("resource_policy") != "COOPERATIVE_PROCESS_WALL_CAP"):
        raise TimingBlocked("BLOCKED__MEASUREMENT_CONTRACT_IDENTITY")
    cap = contract.get("resource_wall_seconds")
    if type(cap) not in (int, float) or not math.isfinite(cap) or cap <= 0:
        raise TimingBlocked("BLOCKED__MEASUREMENT_RESOURCE_CAP")
    ceilings = _contract_numbers(contract.get("per_category_attempt_ceiling"), c8.CEILINGS)
    per_province = _contract_numbers(contract.get("per_province_attempt_ceiling"), c8.PER_PROVINCE)
    if not os.path.lexists(repo / OUTPUT) and c8.path_components_safe(repo / OUTPUT):
        return {"execution_id": execution_id, "ceilings": ceilings,
                "per_province": per_province, "wall_seconds": float(cap),
                "contract_sha256": contract_sha, "owner_adoption_sha256": adoption_sha}
    raise TimingBlocked("BLOCKED__MEASUREMENT_OUTPUT_EXISTS_OR_UNSAFE")


def seal_science_outputs(c8: Any, output: Path, runtime: Mapping[str, Any]) -> dict[str, Any]:
    """Seal and independently read back science outputs before the elapsed end."""
    if not c8.owns_output_root(output, runtime):
        raise TimingBlocked("BLOCKED__MEASUREMENT_OUTPUT_REPLACED")
    excluded = {"science_artifact_manifest.json", "science_artifact_readback.json", "timing_receipt.json"}
    files = sorted(p for p in output.rglob("*") if p.is_file() and p.name not in excluded)
    entries = [{"path": p.relative_to(output).as_posix(), "bytes": p.stat().st_size,
                "sha256": sha(p)} for p in files]
    manifest = {"schema": "CH5_K1B_TIMED_C8_SCIENCE_ARTIFACT_MANIFEST_V1",
                "entry_count": len(entries), "entries": entries}
    c8.write_output_json(output, runtime, output / "science_artifact_manifest.json", manifest)
    bad = [row["path"] for row in entries if not (output / row["path"]).is_file()
           or (output / row["path"]).stat().st_size != row["bytes"]
           or sha(output / row["path"]) != row["sha256"]]
    if bad or not c8.owns_output_root(output, runtime):
        raise TimingBlocked("BLOCKED__MEASUREMENT_SEAL_READBACK", bad)
    digest = sha(output / "science_artifact_manifest.json")
    c8.write_output_json(output, runtime, output / "science_artifact_readback.json",
                         {"status": "PASS", "manifest_sha256": digest, "bad_paths": []})
    return {"manifest_sha256": digest, "entry_count": len(entries)}


def _instrumented_action(c8: Any, repo: Path, gate: Mapping[str, Any], start: Mapping[str, Any],
                         record: dict[str, Any], runtime: dict[str, Any]) -> str:
    output = repo / OUTPUT
    base_guard = c8.BudgetGuard
    original_output, original_task, original_terminal = c8.OUTPUT, c8.FUTURE_TASK_RELATIVE, c8.turn8_terminal
    original_province, original_guard = c8.PER_PROVINCE, c8.BudgetGuard
    deadline = int(start["monotonic_ns"] + gate["wall_seconds"] * 1e9)
    intervals: list[dict[str, Any]] = []
    sequence = 0

    class MeasuredGuard(base_guard):
        def __init__(self, *args: Any, **kwargs: Any):
            super().__init__(ceilings=gate["ceilings"], prior={}, combined=gate["ceilings"])
            self.open_province: dict[int, dict[str, Any]] = {}
            self.integration_start: dict[str, Any] | None = None
            self.household_start: dict[str, Any] | None = None

        def journal(self, event: str, detail: Any = None) -> None:
            nonlocal sequence
            sequence += 1
            try:
                c8.write_output_json(output, runtime, output / f"attempt_journal_{sequence:07d}.json",
                                     {"event": event, "detail": detail, "execution_id": gate["execution_id"],
                                      "monotonic_ns": time.monotonic_ns(), "attempted": dict(self.attempted),
                                      "per_province": self.per_province,
                                      "budget_namespace": "SEPARATE_C8_TIMING_ONLY"})
            except BaseException:
                if runtime.get("state") is not None:
                    runtime["state"]["ledger_unresolved"] = True
                raise

        def resource_check(self) -> None:
            if time.monotonic_ns() >= deadline:
                self.journal("cooperative_resource_cap_reached")
                raise TimingBlocked("BLOCKED__MEASUREMENT_RESOURCE_CAP_REACHED")

        def reserve(self, amounts: Mapping[str, int], province: int | None = None) -> None:
            self.resource_check()
            super().reserve(amounts, province)
            self.journal("reserve_before_entry", {"amounts": dict(amounts), "province": province})
            if "full_integrations" in amounts and self.integration_start is None:
                self.integration_start = clock_sample()
                self.journal("integration_start", self.integration_start)
            if province is not None and province not in self.open_province:
                stamp = clock_sample()
                if self.household_start is None:
                    self.household_start = stamp
                self.open_province[province] = stamp
                self.journal("province_start", {"province": province, "clock": stamp})
            if "full_integrations" in amounts and self.household_start is not None:
                closed = clock_sample()
                intervals.append({"stage": "household", "start": self.household_start,
                                  "end": closed, "elapsed_ns": elapsed_clock(self.household_start, closed)})
                self.household_start = None

        def enter(self, key: str, province: int | None = None) -> None:
            super().enter(key, province)
            self.journal("attempted_before_source_call", {"category": key, "province": province})

        def reconcile(self, ledger: Mapping[str, Any]) -> None:
            super().reconcile(ledger)
            self.journal("source_reconciled")
            for province, opened in list(self.open_province.items()):
                closed = clock_sample()
                intervals.append({"stage": "province", "province": province,
                                  "start": opened, "end": closed,
                                  "elapsed_ns": elapsed_clock(opened, closed)})
                del self.open_province[province]

        def reconcile_all(self, ledger: Mapping[str, Any]) -> None:
            super().reconcile_all(ledger)
            self.journal("integration_source_reconciled")
            if self.integration_start is not None:
                closed = clock_sample()
                intervals.append({"stage": "integration", "start": self.integration_start,
                                  "end": closed, "elapsed_ns": elapsed_clock(self.integration_start, closed)})
                self.integration_start = None

    try:
        c8.OUTPUT = OUTPUT
        c8.FUTURE_TASK_RELATIVE = TASK_COPY
        c8.PER_PROVINCE = gate["per_province"]
        c8.BudgetGuard = MeasuredGuard
        c8.turn8_terminal = lambda prior, carrier: "MEASUREMENT_COMPLETE__OBSERVED_SAMPLE_ONLY"
        result = c8._execute_after_gate(repo, gate["execution_id"], runtime)
        record["intervals"] = intervals
        record["source_terminal"] = result
        record["attempted"] = dict(runtime["guard"].attempted)
        record["source_ledger"] = dict(runtime["ledger"])
        return result
    finally:
        c8.OUTPUT, c8.FUTURE_TASK_RELATIVE = original_output, original_task
        c8.PER_PROVINCE, c8.BudgetGuard = original_province, original_guard
        c8.turn8_terminal = original_terminal


def run_timed_action(repo: Path, gate: Mapping[str, Any], c8: Any,
                     action: Any = None, clock: Any = time, utc_now: Any = None) -> dict[str, Any]:
    """Production uses the accepted delegate; tests pass inert actions only."""
    output = repo / OUTPUT
    if os.path.lexists(output):
        raise TimingBlocked("BLOCKED__MEASUREMENT_OUTPUT_EXISTS_OR_UNSAFE")
    start = clock_sample(clock, utc_now)
    record: dict[str, Any] = {}
    runtime_box: dict[str, Any] = {}
    def invoke(runtime: dict[str, Any]) -> str:
        runtime_box["runtime"] = runtime
        return (action or _instrumented_action)(c8, repo, gate, start, record, runtime)
    original_output = c8.OUTPUT
    try:
        c8.OUTPUT = OUTPUT
        result = c8.run_after_valid_gate(repo, gate["execution_id"], invoke)
        end_science = clock_sample(clock, utc_now)
        runtime = runtime_box["runtime"]
        seal_start = clock_sample(clock, utc_now)
        sealed = seal_science_outputs(c8, output, runtime)
        end = clock_sample(clock, utc_now)
        elapsed = elapsed_clock(start, end)
        seal_interval = {"stage": "seal_and_readback", "start": seal_start,
                         "end": end, "elapsed_ns": elapsed_clock(seal_start, end)}
        receipt = {"terminal": result, "classification": "COMPLETE_OBSERVED_ELAPSED_SAMPLE_ONLY",
                   "execution_id": gate["execution_id"], "start": start, "science_end": end_science,
                   "complete_seal_end": end, "elapsed_ns": elapsed,
                   "science_artifacts": sealed,
                   "stage_intervals": record.get("intervals", []) + [seal_interval],
                   "attempted": record.get("attempted"), "source_ledger": record.get("source_ledger"),
                   "environment": c8.environment_snapshot(), "pid": os.getpid(),
                   "argv": list(sys.argv), "output_root": str(output),
                   "owner_adoption_sha256": gate["owner_adoption_sha256"],
                   "measurement_contract_sha256": gate["contract_sha256"],
                   "c9_c10_upper_duration_bound": None, "results_eligibility": False}
        c8.write_output_json(output, runtime, output / "timing_receipt.json", receipt)
        return receipt
    except BaseException as exc:
        original = getattr(exc, "terminal", type(exc).__name__)
        runtime = runtime_box.get("runtime", {})
        guard = runtime.get("guard")
        ambiguous = (guard is None or bool(getattr(guard, "open_province", {})) or
                     getattr(guard, "integration_start", None) is not None or
                     bool((runtime.get("state") or {}).get("ledger_unresolved")))
        terminal = "CALL_LEDGER_UNRESOLVED" if ambiguous else original
        if runtime.get("output_identity") is not None and c8.owns_output_root(output, runtime):
            try:
                c8.write_output_json(output, runtime, output / "timing_failure.json",
                                     {"terminal": terminal, "original_terminal": original,
                                      "execution_id": gate["execution_id"], "start": start,
                                      "end": clock_sample(clock, utc_now),
                                      "attempted": dict(guard.attempted) if guard else None,
                                      "source_ledger": runtime.get("ledger"),
                                      "retry_allowed": False})
            except BaseException:
                terminal = "CALL_LEDGER_UNRESOLVED"
        raise TimingBlocked(terminal, {"original_terminal": original}) from exc
    finally:
        c8.OUTPUT = original_output


def execute_once(repo: Path = REPOSITORY, execution_id: str | None = None) -> dict[str, Any]:
    """Future-only gate. Never call from the zero-science preparation task."""
    repo = repo.resolve()
    c8 = accepted_runner(repo)
    gate = future_gate(repo, execution_id, c8)
    static_preflight(repo)  # Full C7 artifact/entering readback before output creation.
    return run_timed_action(repo, gate, c8)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=REPOSITORY)
    parser.add_argument("--execute", action="store_true", help="requires a later committed task and Owner contract")
    parser.add_argument("--execution-id")
    args = parser.parse_args(argv)
    result = execute_once(args.repository, args.execution_id) if args.execute else static_preflight(args.repository)
    print(json.dumps(result, ensure_ascii=True, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
