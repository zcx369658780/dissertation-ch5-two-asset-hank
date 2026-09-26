"""Future-only C9 timed-risk exception; import and default CLI are inert.

The science path uses the C9 delegate only after a separate Owner contract,
independent review, and one-shot execution task. This file grants none.
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
OUTPUT = Path("reports/ch5_k1b_turn9_timed_risk_exception_run001")
TIMED_RUNNER = Path("validators/multi_province/k1b_turn9_timed_risk_exception/run.py")
DELEGATE = Path("validators/multi_province/k1b_turn9_outer_r2/run.py")
ACCEPTED_C8_RUNNER_SHA = "10920535BD50E688D1794B7E69C34F8A5C3C56456CAF6E8DF52FA8D9DFE31831"
SRC_TREE = "00682b2e1a7ba23665f6e16f6acf48ad35874883"
C8_ROOT = Path("reports/ch5_k1b_turn8_outer_r2_20260925_run001")
C8_MANIFEST_SHA = "5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301"
C8_ENTERING_SHA = "40200B60729A5B4173E24661843980851F8610A9FA2186F7E411B7FE9E5CDC65"
C8_READBACK_SHA = "E428D105600D091979B526ADD6BF61E0FC294050B9FAB97FE8B87A29A1012F85"
TASK_ID = "CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_EXECUTION"
TASK_STATUS = "ACTIVE__ONE_SHOT_C9_TIMED_RISK_EXCEPTION"
TASK_COPY = Path("tasks/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_EXECUTION.md")
OWNER_ADOPTION = Path("docs/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_EXECUTION_OWNER_ADOPTION.md")
CONTRACT = Path("tasks/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_INACTIVE_CONTRACT.json")
INDEPENDENT_REVIEW = Path("docs/CH5_K1B_TURN9_TIMED_RISK_EXCEPTION_RUNNER_INDEPENDENT_REVIEW.md")
PREPARATION_TASK_ID = "CH5_K1B_C9_TIMED_EXCEPTION_STATIC_RUNNER_PREPARATION_20260926"


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


def load_delegate(repo: Path):
    contract = json.loads((repo / CONTRACT).read_text(encoding="utf-8"))
    expected = contract.get("delegate_sha256")
    if not isinstance(expected, str) or sha(repo / DELEGATE) != expected:
        raise TimingBlocked("BLOCKED__C9_DELEGATE_IDENTITY")
    spec = importlib.util.spec_from_file_location("c9_timed_risk_delegate", repo / DELEGATE)
    if spec is None or spec.loader is None:
        raise TimingBlocked("BLOCKED__C9_DELEGATE_LOAD")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def static_preflight(repo: Path = REPOSITORY, require_inactive: bool = True) -> dict[str, Any]:
    """Read-only input, contract and delegate checks; no science or output."""
    repo = repo.resolve()
    contract = json.loads((repo / CONTRACT).read_text(encoding="utf-8"))
    checks = {
        "repository": git(repo, "rev-parse", "--show-toplevel").replace("\\", "/").casefold()
                      == repo.as_posix().casefold(),
        "src_tree": git(repo, "rev-parse", "HEAD:src") == SRC_TREE,
        "src_clean": not git(repo, "status", "--porcelain=v1", "--", "src"),
        "candidate_absent": not os.path.lexists(repo / OUTPUT),
        "candidate_parent_safe": not os.path.lexists(repo / OUTPUT) and
                                 all(not os.path.islink(p) for p in (repo / OUTPUT).parents),
        "c8_manifest": sha(repo / C8_ROOT / "execution_artifact_manifest.json") == C8_MANIFEST_SHA,
        "c8_entering": sha(repo / C8_ROOT / "turn9_entering_bundle_manifest.json") == C8_ENTERING_SHA,
        "c8_readback": sha(repo / C8_ROOT / "turn9_entering_bundle_readback.json") == C8_READBACK_SHA,
        "contract_schema": contract.get("schema") == "CH5_K1B_C9_TIMED_RISK_EXCEPTION_CONTRACT_V1",
        "contract_output": contract.get("output_root") == OUTPUT.as_posix(),
        "contract_state": ((contract.get("active") is False and
                            contract.get("resource_wall_seconds") is None and
                            contract.get("execution_id") is None) if require_inactive else
                            (contract.get("active") is True and
                             type(contract.get("resource_wall_seconds")) in (int, float) and
                             math.isfinite(contract["resource_wall_seconds"]) and
                             contract["resource_wall_seconds"] > 0)),
        "delegate_hash": sha(repo / DELEGATE) == contract.get("delegate_sha256"),
        "sealed_input_hashes": contract.get("sealed_input_sha256") == {
            "manifest": C8_ENTERING_SHA, "readback": C8_READBACK_SHA,
            "json": "FBB18A5B8B4FD94F337510DBB4E62F94188C27863EED1F79FE2E1A71B5BC39AB",
            "npz": "E7E6AF79864F67A28386ECF8BEB3B71C6080E9A6C6E64F4CBA8125E1C19D34DD"},
        "owner_selection": contract.get("owner_selection_sha256") == sha(
            repo / "docs/CH5_K1B_C9_SINGLE_TURN_TIMED_RISK_EXCEPTION_OWNER_SELECTION_20260926.md"),
        "ceiling_adoption": contract.get("ceiling_adoption_sha256") == sha(
            repo / "docs/CH5_K1B_C9_C10_CALL_CEILINGS_OWNER_ADOPTION_20260925.md"),
        "c8_manifest_contract": contract.get("c8_execution_manifest_sha256") == C8_MANIFEST_SHA,
    }
    if not all(checks.values()):
        raise TimingBlocked("BLOCKED__C9_STATIC_IDENTITY", checks)
    c9 = load_delegate(repo)
    delegated = c9.preflight(repo)
    if (not all(delegated["checks"].values()) or
            delegated["C8_entering"]["json"] != c9.SEALED["turn9_k1b_input_candidate.json"] or
            contract.get("per_category_attempt_ceiling") != c9.CEILINGS or
            contract.get("per_province_attempt_ceiling") != c9.PER_PROVINCE or
            contract.get("c9_c10_cumulative_ceiling") != c9.TWO_TURN_CEILINGS):
        raise TimingBlocked("BLOCKED__C9_BUDGET_OR_INPUT_BINDING")
    return {"status": "BLOCKED__INACTIVE_CONTRACT" if require_inactive else "PASS__ACTIVE_PREFLIGHT_ONLY", "checks": checks,
            "delegated_checks": delegated["checks"], "src_tree": SRC_TREE,
            "c8_entering": delegated["C8_entering"],
            "output_candidate": str(repo / OUTPUT), "scientific_calls": 0,
            "c9_attempts": 0, "c10_attempts": 0, "results_eligibility": False}


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


def future_gate(repo: Path, execution_id: str | None, c9: Any) -> dict[str, Any]:
    """Every activation, authority and identity check precedes output creation."""
    contract = json.loads((repo / CONTRACT).read_text(encoding="utf-8"))
    if contract.get("active") is not True or contract.get("resource_wall_seconds") is None:
        raise TimingBlocked("BLOCKED__INACTIVE_CONTRACT")
    if not execution_id or re.fullmatch(r"[A-Za-z0-9_-]{1,80}", execution_id) is None:
        raise TimingBlocked("EXECUTION_AUTHORIZATION_REQUIRED")
    wrapper_sha = committed_file(repo, TIMED_RUNNER)
    delegate_sha = committed_file(repo, DELEGATE)
    if delegate_sha != contract.get("delegate_sha256"):
        raise TimingBlocked("BLOCKED__C9_DELEGATE_IDENTITY")
    current_sha = committed_file(repo, Path("TASK_CURRENT.md"))
    task = (repo / "TASK_CURRENT.md").read_text(encoding="utf-8")
    required = (f"Task ID: '{TASK_ID}'", f"Status: '{TASK_STATUS}'",
                f"Execution authorization ID: '{execution_id}'",
                f"Authorized output root: '{OUTPUT.as_posix()}'")
    # Accept only the exact backtick-delimited authority fields.
    required = tuple(item.replace("'", chr(96)) for item in required)
    if not all(field in task for field in required):
        raise TimingBlocked("BLOCKED__FRESH_C9_TASK_GATE")
    if committed_file(repo, TASK_COPY) != current_sha or not all(
            field in (repo / TASK_COPY).read_text(encoding="utf-8") for field in required):
        raise TimingBlocked("BLOCKED__C9_TASK_COPY")
    review_sha = committed_file(repo, INDEPENDENT_REVIEW)
    review = (repo / INDEPENDENT_REVIEW).read_text(encoding="utf-8")
    if ("Verdict: ACCEPT__C9_TIMED_RISK_EXCEPTION_RUNNER" not in review or
            f"Wrapper path: '{TIMED_RUNNER.as_posix()}'".replace("'", chr(96)) not in review or
            f"Wrapper SHA-256: '{wrapper_sha}'".replace("'", chr(96)) not in review or
            f"Delegate SHA-256: '{delegate_sha}'".replace("'", chr(96)) not in review or
            "Reviewer: GPT Work" not in review):
        raise TimingBlocked("BLOCKED__INDEPENDENT_C9_REVIEW_IDENTITY")
    adoption_sha = committed_file(repo, OWNER_ADOPTION)
    contract_sha = committed_file(repo, CONTRACT)
    bindings = (f"Owner adoption SHA-256: '{adoption_sha}'",
                f"C9 contract SHA-256: '{contract_sha}'",
                f"Independent review SHA-256: '{review_sha}'",
                f"Wrapper SHA-256: '{wrapper_sha}'",
                f"Delegate SHA-256: '{delegate_sha}'")
    if not all(item.replace("'", chr(96)) in task for item in bindings):
        raise TimingBlocked("BLOCKED__C9_TASK_CONTRACT_BINDING")
    adoption = (repo / OWNER_ADOPTION).read_text(encoding="utf-8")
    if (f"Execution authorization ID: '{execution_id}'".replace("'", chr(96)) not in adoption or
            f"Authorized output root: '{OUTPUT.as_posix()}'".replace("'", chr(96)) not in adoption or
            f"C9 contract SHA-256: '{contract_sha}'".replace("'", chr(96)) not in adoption or
            f"Independent review SHA-256: '{review_sha}'".replace("'", chr(96)) not in adoption or
            "OWNER_ADOPTED__SINGLE_C9_TIMED_RISK_EXCEPTION" not in adoption):
        raise TimingBlocked("BLOCKED__OWNER_C9_ADOPTION")
    cap = contract.get("resource_wall_seconds")
    if (contract.get("execution_id") != execution_id or
            contract.get("output_root") != OUTPUT.as_posix() or
            contract.get("attempts") != 1 or contract.get("retries") != 0 or
            contract.get("budget_namespace") != "C8_START_C9_C10_WINDOW" or
            contract.get("wrapper_sha256") != wrapper_sha or
            contract.get("independent_review_sha256") != review_sha or
            contract.get("resource_policy") != "COOPERATIVE_PROCESS_WALL_CAP" or
            type(cap) not in (int, float) or not math.isfinite(cap) or cap <= 0):
        raise TimingBlocked("BLOCKED__C9_CONTRACT_IDENTITY")
    ceilings = _contract_numbers(contract.get("per_category_attempt_ceiling"), c9.CEILINGS)
    province = _contract_numbers(contract.get("per_province_attempt_ceiling"), c9.PER_PROVINCE)
    cumulative = _contract_numbers(contract.get("c9_c10_cumulative_ceiling"), c9.TWO_TURN_CEILINGS)
    if ceilings != c9.CEILINGS or province != c9.PER_PROVINCE or cumulative != c9.TWO_TURN_CEILINGS:
        raise TimingBlocked("BLOCKED__C9_BUDGET_BINDING")
    if os.path.lexists(repo / OUTPUT) or not c9.path_components_safe(repo / OUTPUT):
        raise TimingBlocked("BLOCKED__C9_OUTPUT_EXISTS_OR_UNSAFE")
    return {"execution_id": execution_id, "ceilings": ceilings, "per_province": province,
            "cumulative": cumulative, "wall_seconds": float(cap),
            "contract_sha256": contract_sha, "owner_adoption_sha256": adoption_sha,
            "independent_review_sha256": review_sha, "wrapper_sha256": wrapper_sha}


def seal_science_outputs(c9: Any, output: Path, runtime: Mapping[str, Any]) -> dict[str, Any]:
    """Seal and independently read back science outputs before the elapsed end."""
    if not c9.owns_output_root(output, runtime):
        raise TimingBlocked("BLOCKED__MEASUREMENT_OUTPUT_REPLACED")
    excluded = {"science_artifact_manifest.json", "science_artifact_readback.json", "timing_receipt.json", "pause_receipt.json"}
    files = sorted(p for p in output.rglob("*") if p.is_file() and p.name not in excluded)
    if not all(c9.path_components_safe(p) for p in files):
        raise TimingBlocked("BLOCKED__C9_SCIENCE_REPARSE_POINT")
    entries = [{"path": p.relative_to(output).as_posix(), "bytes": p.stat().st_size,
                "sha256": sha(p)} for p in files]
    manifest = {"schema": "CH5_K1B_TIMED_C9_SCIENCE_ARTIFACT_MANIFEST_V1",
                "entry_count": len(entries), "entries": entries}
    c9.write_output_json(output, runtime, output / "science_artifact_manifest.json", manifest)
    bad = [row["path"] for row in entries if not (output / row["path"]).is_file()
           or (output / row["path"]).stat().st_size != row["bytes"]
           or sha(output / row["path"]) != row["sha256"]]
    if bad or not c9.owns_output_root(output, runtime):
        raise TimingBlocked("BLOCKED__MEASUREMENT_SEAL_READBACK", bad)
    digest = sha(output / "science_artifact_manifest.json")
    c9.write_output_json(output, runtime, output / "science_artifact_readback.json",
                         {"status": "PASS", "manifest_sha256": digest, "bad_paths": []})
    return {"manifest_sha256": digest, "entry_count": len(entries)}


def _instrumented_action(c9: Any, repo: Path, gate: Mapping[str, Any], start: Mapping[str, Any],
                         record: dict[str, Any], runtime: dict[str, Any]) -> str:
    output = repo / OUTPUT
    base_guard = c9.BudgetGuard
    original_output, original_task = c9.OUTPUT, c9.FUTURE_TASK_RELATIVE
    original_province, original_guard = c9.PER_PROVINCE, c9.BudgetGuard
    deadline = int(start["monotonic_ns"] + gate["wall_seconds"] * 1e9)
    intervals: list[dict[str, Any]] = []
    sequence = 0

    class MeasuredGuard(base_guard):
        def __init__(self, *args: Any, **kwargs: Any):
            super().__init__(ceilings=gate["ceilings"], prior={}, combined=gate["cumulative"])
            self.open_province: dict[int, dict[str, Any]] = {}
            self.integration_start: dict[str, Any] | None = None
            self.household_start: dict[str, Any] | None = None

        def journal(self, event: str, detail: Any = None) -> None:
            nonlocal sequence
            sequence += 1
            try:
                c9.write_output_json(output, runtime, output / f"attempt_journal_{sequence:07d}.json",
                                     {"event": event, "detail": detail, "execution_id": gate["execution_id"],
                                      "monotonic_ns": time.monotonic_ns(), "attempted": dict(self.attempted),
                                      "per_province": self.per_province,
                                      "budget_namespace": "C8_START_C9_C10_WINDOW"})
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
            if key == "frozen_k1b_quantity_allocations":
                # The source's feedback counter names the same frozen allocation event.
                self.reserve({"frozen_k1b_quantity_allocations": 1,
                              "k1b_feedback_calls": 1}, province)
                self.attempted["frozen_k1b_quantity_allocations"] += 1
                self.attempted["k1b_feedback_calls"] += 1
                self.journal("attempted_before_source_call", {"alias": [
                    "frozen_k1b_quantity_allocations", "k1b_feedback_calls"],
                    "province": province})
            else:
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
        c9.OUTPUT = OUTPUT
        c9.FUTURE_TASK_RELATIVE = TASK_COPY
        c9.PER_PROVINCE = gate["per_province"]
        c9.BudgetGuard = MeasuredGuard
        runtime["c9_wrapper_contract_sha256"] = gate["contract_sha256"]
        runtime["c9_wrapper_execution_id"] = gate["execution_id"]
        result = c9._execute_after_gate(repo, gate["execution_id"], runtime)
        record["intervals"] = intervals
        record["source_terminal"] = result
        record["attempted"] = dict(runtime["guard"].attempted)
        record["source_ledger"] = dict(runtime["ledger"])
        return result
    finally:
        c9.OUTPUT, c9.FUTURE_TASK_RELATIVE = original_output, original_task
        c9.PER_PROVINCE, c9.BudgetGuard = original_province, original_guard


def run_timed_action(repo: Path, gate: Mapping[str, Any], c9: Any,
                     action: Any = None, clock: Any = time, utc_now: Any = None) -> dict[str, Any]:
    """Production uses the accepted delegate; tests pass inert actions only."""
    output = repo / OUTPUT
    if os.path.lexists(output) or not c9.path_components_safe(output):
        raise TimingBlocked("BLOCKED__C9_OUTPUT_EXISTS_OR_UNSAFE")
    start = clock_sample(clock, utc_now)
    record: dict[str, Any] = {}
    runtime_box: dict[str, Any] = {}
    def invoke(runtime: dict[str, Any]) -> str:
        runtime_box["runtime"] = runtime
        return (action or _instrumented_action)(c9, repo, gate, start, record, runtime)
    original_output = c9.OUTPUT
    try:
        c9.OUTPUT = OUTPUT
        result = c9.run_after_valid_gate(repo, gate["execution_id"], invoke)
        end_science = clock_sample(clock, utc_now)
        runtime = runtime_box["runtime"]
        seal_start = clock_sample(clock, utc_now)
        sealed = seal_science_outputs(c9, output, runtime)
        if result not in ("VALID__C9_NINE_COMPONENT_LEVEL_MET",
                          "VALID__C9_NINE_COMPONENT_LEVEL_NOT_MET"):
            raise TimingBlocked("BLOCKED__C9_NUMERICAL_TERMINAL_UNEXPECTED")
        guard = runtime.get("guard")
        if guard is None or (runtime.get("state") or {}).get("ledger_unresolved"):
            raise TimingBlocked("CALL_LEDGER_UNRESOLVED")
        attempted = dict(guard.attempted)
        remaining_cumulative = {key: gate["cumulative"][key] - attempted[key]
                                for key in gate["cumulative"]}
        remaining_C9 = {key: gate["ceilings"][key] - attempted[key]
                        for key in gate["ceilings"]}
        remaining_per_province = {
            str(index): {key: limit - guard.per_province.get(index, {}).get(key, 0)
                         for key, limit in gate["per_province"].items()}
            for index in range(31)}
        if any(value < 0 for value in (*remaining_cumulative.values(),
                                      *remaining_C9.values(),
                                      *(value for row in remaining_per_province.values()
                                        for value in row.values()))):
            raise TimingBlocked("CALL_LEDGER_UNRESOLVED")
        pause = {"terminal": "SAFE_PAUSE_AFTER_SEALED_C9",
                 "original_numerical_terminal": result,
                 "execution_id": gate["execution_id"],
                 "science_manifest_sha256": sealed["manifest_sha256"],
                 "entering_C10_manifest_sha256": c9.sha(output / "turn10_entering_bundle_manifest.json"),
                 "entering_C10_readback_sha256": c9.sha(output / "turn10_entering_bundle_readback.json"),
                 "attempted_C9": attempted,
                 "attempted_C9_C10_cumulative": attempted,
                 "attempted_per_province_C9": guard.per_province,
                 "remaining_C9": remaining_C9,
                 "remaining_C9_C10_cumulative": remaining_cumulative,
                 "remaining_per_province_C9": remaining_per_province,
                 "output_identity": runtime.get("output_identity"),
                 "src_tree": SRC_TREE,
                 "sealed_C8_entering_C9_manifest_sha256": C8_ENTERING_SHA,
                 "start_clock": start, "seal_clock": clock_sample(clock, utc_now),
                 "cooperative_resource_wall_seconds": gate["wall_seconds"],
                 "normal_duration_gate": "BLOCKED__DURATION_BOUND_UNAVAILABLE",
                 "C10_started": False, "C10_authorized": False,
                 "results_eligibility": False}
        c9.write_output_json(output, runtime, output / "pause_receipt.json", pause)
        end = clock_sample(clock, utc_now)
        elapsed = elapsed_clock(start, end)
        seal_interval = {"stage": "seal_and_readback", "start": seal_start,
                         "end": end, "elapsed_ns": elapsed_clock(seal_start, end)}
        receipt = {"terminal": "SAFE_PAUSE_AFTER_SEALED_C9", "original_numerical_terminal": result,
                   "classification": "SINGLE_C9_TIMED_RISK_EXCEPTION_OBSERVED_ONLY",
                   "execution_id": gate["execution_id"], "start": start, "science_end": end_science,
                   "complete_seal_end": end, "elapsed_ns": elapsed,
                   "science_artifacts": sealed,
                   "stage_intervals": record.get("intervals", []) + [seal_interval],
                   "attempted": record.get("attempted"), "source_ledger": record.get("source_ledger"),
                   "environment": c9.environment_snapshot(), "pid": os.getpid(),
                   "argv": list(sys.argv), "output_root": str(output),
                   "owner_adoption_sha256": gate["owner_adoption_sha256"],
                   "c9_contract_sha256": gate["contract_sha256"],
                   "pause_receipt_sha256": c9.sha(output / "pause_receipt.json"),
                   "c9_c10_upper_duration_bound": None, "results_eligibility": False}
        c9.write_output_json(output, runtime, output / "timing_receipt.json", receipt)
        return receipt
    except BaseException as exc:
        original = getattr(exc, "terminal", type(exc).__name__)
        runtime = runtime_box.get("runtime", {})
        guard = runtime.get("guard")
        ambiguous = (guard is None or bool(getattr(guard, "open_province", {})) or
                     getattr(guard, "integration_start", None) is not None or
                     bool((runtime.get("state") or {}).get("ledger_unresolved")))
        terminal = "CALL_LEDGER_UNRESOLVED" if ambiguous else original
        if runtime.get("output_identity") is not None and c9.owns_output_root(output, runtime):
            try:
                c9.write_output_json(output, runtime, output / "timing_failure.json",
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
        c9.OUTPUT = original_output


def execute_once(repo: Path = REPOSITORY, execution_id: str | None = None) -> dict[str, Any]:
    """Future-only gate. Never call from the zero-science preparation task."""
    repo = repo.resolve()
    contract = json.loads((repo / CONTRACT).read_text(encoding="utf-8"))
    if contract.get("active") is not True or contract.get("resource_wall_seconds") is None:
        raise TimingBlocked("BLOCKED__INACTIVE_CONTRACT")
    c9 = load_delegate(repo)
    gate = future_gate(repo, execution_id, c9)
    static_preflight(repo, require_inactive=False)
    return run_timed_action(repo, gate, c9)


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
