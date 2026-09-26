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
import stat
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping
from zoneinfo import ZoneInfo

REPOSITORY = Path(__file__).resolve().parents[3]
OUTPUT = Path("reports/ch5_k1b_turn9_post_failure_new_attempt_001")
TIMED_RUNNER = Path("validators/multi_province/k1b_turn9_post_failure_new_attempt_timed/run.py")
DELEGATE = Path("validators/multi_province/k1b_turn9_post_failure_new_attempt_outer_r2/run.py")
ACCEPTED_C8_RUNNER_SHA = "10920535BD50E688D1794B7E69C34F8A5C3C56456CAF6E8DF52FA8D9DFE31831"
SRC_TREE = "00682b2e1a7ba23665f6e16f6acf48ad35874883"
C8_ROOT = Path("reports/ch5_k1b_turn8_outer_r2_20260925_run001")
C8_MANIFEST_SHA = "5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301"
C8_ENTERING_SHA = "40200B60729A5B4173E24661843980851F8610A9FA2186F7E411B7FE9E5CDC65"
C8_READBACK_SHA = "E428D105600D091979B526ADD6BF61E0FC294050B9FAB97FE8B87A29A1012F85"
TASK_ID = "CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION"
TASK_STATUS = "ACTIVE__ONE_SHOT_NEW_C9_POST_FAILURE"
TASK_COPY = Path("tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION.md")
OWNER_ADOPTION = Path("docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_EXECUTION_OWNER_ADOPTION.md")
CONTRACT = Path("tasks/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_CONTRACT.json")
INDEPENDENT_REVIEW = Path("docs/CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_RUNNER_INDEPENDENT_REVIEW.md")
PREPARATION_TASK_ID = "CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_STATIC_RUNNER_PREPARATION_20260926"
NEW_EXECUTION_ID = "C9_POST_FAILURE_NEW_ATTEMPT_001"
NEW_BUDGET_NAMESPACE = "C8_START_C9_POST_FAILURE_NEW_ATTEMPT_001_C10_PROSPECTIVE"
OLD_EXECUTION_ID = "C9_TIMED_RISK_RUN001"
OLD_OUTPUT = Path("reports/ch5_k1b_turn9_timed_risk_exception_run001")
OLD_FAILURE_SHA = "21D7579449AD0DCDE532B9D7695E83FF188AD3E09D9D02A798D574000DEED2E0"
BUDGET_PROPOSAL = Path("EVIDENCE/ch5_k1b_c9_new_budget_failed_ledger_policy_zero_science_proposal_20260926/proposed_budget.json")
BUDGET_PROPOSAL_SHA = "66C2C028B07E2CB41FFBB05B643C6EF644291A0FC94C8DAF2FE888518D240460"
BUDGET_ADOPTION = Path("docs/CH5_K1B_C9_NEW_BUDGET_FAILED_LEDGER_POLICY_OWNER_ADOPTION_20260926.md")
BUDGET_ADOPTION_SHA = "C1D88891C08D7526996F72DE6F77AA6D0FA2C593BAD91017877C8B8A0A51573D"
C8_JSON_SHA = "FBB18A5B8B4FD94F337510DBB4E62F94188C27863EED1F79FE2E1A71B5BC39AB"
C8_NPZ_SHA = "E7E6AF79864F67A28386ECF8BEB3B71C6080E9A6C6E64F4CBA8125E1C19D34DD"
MAP_SHA = {
    "category": "F76B958C8D57CEAD22B61A497FCCFBF45143E1DC2AA07CCC656EBA6252464C20",
    "province": "FDA5A76D45B639FD0B793E6270D051255CCFC0F85E7E982A152A4AA7743D7028",
    "cumulative": "3E2DF35B6D867A0680E1ABBBB778205982F1845139D775A63A9D4672B7D6CA3A",
    "lifetime": "D5C5D10AD030FFD2F12AA81FFFD8DBD5CF8655D4870452593C7AA3B5A224604C",
}
PROTECTED_MANIFESTS = {
    Path("reports/ch5_turn6_same_frozen_input_repeat_20260923_run001/execution_artifact_manifest.json"):
        "7890720D502AC1C04D672978C6F662DD51F9D2BA27F321701877ABE9214CDE61",
    Path("reports/ch5_k1b_turn7_outer_r2_20260925_run001/execution_artifact_manifest.json"):
        "413A0279C244820A28B043452C6BEA45EB2C0B5CF8E7CDF460DBBEC45DD61D91",
    Path("reports/ch5_k1b_turn8_outer_r2_20260925_run001/execution_artifact_manifest.json"):
        "5C1D740CDEAC77A232657668EA22AA79403B708DA154FF141472127534574301",
    Path("reports/ch5_k1b_turn8_same_frozen_timing_measurement_run001/science_artifact_manifest.json"):
        "5DD433E8DD0D8A3C6DB59C3FE370C4EF8770BBCCCA3F8D79211D93938CFA654D",
    Path("reports/ch5_k1b_turn9_timed_risk_exception_run001/partial_artifact_manifest.json"):
        "80BD0D42CB73B4E39B811E759505480542D5A73227014F30B732C34A8AC1FDC3",
}


class TimingBlocked(RuntimeError):
    def __init__(self, terminal: str, detail: Any = None):
        super().__init__(terminal)
        self.terminal, self.detail = terminal, detail


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def path_components_safe(path: Path) -> bool:
    """Read-only lstat walk; reject symlink and Windows reparse components."""
    path = path.absolute()
    for component in reversed((path, *path.parents)):
        try:
            identity = component.lstat()
        except FileNotFoundError:
            return component == path  # Only the final output child may be absent.
        except OSError:
            return False
        if stat.S_ISLNK(identity.st_mode):
            return False
        attributes = getattr(identity, "st_file_attributes", None)
        if attributes is not None and attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0):
            return False
        if os.name == "nt" and attributes is None:
            return False
    return True


def safe_regular_file(path: Path) -> bool:
    if not path_components_safe(path):
        return False
    try:
        return stat.S_ISREG(path.lstat().st_mode)
    except OSError:
        return False


SEALED_EVIDENCE = {
    C8_ROOT / "execution_artifact_manifest.json": C8_MANIFEST_SHA,
    C8_ROOT / "turn9_entering_bundle_manifest.json": C8_ENTERING_SHA,
    C8_ROOT / "turn9_entering_bundle_readback.json": C8_READBACK_SHA,
    C8_ROOT / "turn9_k1b_input_candidate.json": C8_JSON_SHA,
    C8_ROOT / "turn9_k1b_frozen_share_payoff_plan.npz": C8_NPZ_SHA,
    C8_ROOT / "comparison_receipt.json": "7F70FB73EAAE0D2BA4C2F60AC5FE071AA963D42EA77A64950D4F94562CB364FC",
    C8_ROOT / "terminal_receipt.json": "01BBF375DA61B387F697A581A9137C57FC87A3DC7CBC937838933A25F7297A7D",
    OLD_OUTPUT / "partial_artifact_manifest.json": PROTECTED_MANIFESTS[OLD_OUTPUT / "partial_artifact_manifest.json"],
    OLD_OUTPUT / "timing_failure.json": OLD_FAILURE_SHA,
}


def sealed_evidence_checks(repo: Path) -> dict[str, bool]:
    checks = {}
    for relative, expected in SEALED_EVIDENCE.items():
        path = repo / relative
        try:
            checks[relative.as_posix()] = safe_regular_file(path) and sha(path) == expected
        except OSError:
            checks[relative.as_posix()] = False
    return checks


def protected_manifest_checks(repo: Path) -> dict[str, bool]:
    checks = {}
    for relative, expected in PROTECTED_MANIFESTS.items():
        path = repo / relative
        try:
            checks[relative.as_posix()] = (
                safe_regular_file(path) and sha(path) == expected)
        except OSError:
            checks[relative.as_posix()] = False
    return checks


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()


def committed_file(repo: Path, relative: Path) -> str:
    """Return the raw digest when Git's filtered worktree equals HEAD."""
    path = repo / relative
    if (not path.is_file() or not path_components_safe(path) or
            git(repo, "status", "--porcelain=v1", "--", relative.as_posix())):
        raise TimingBlocked("BLOCKED__MEASUREMENT_AUTHORITY_DIRTY_OR_MISSING", relative.as_posix())
    try:
        head_blob = git(repo, "rev-parse", f"HEAD:{relative.as_posix()}")
        worktree_blob = git(repo, "hash-object", f"--path={relative.as_posix()}",
                            relative.as_posix())
    except subprocess.CalledProcessError as exc:
        raise TimingBlocked("BLOCKED__MEASUREMENT_AUTHORITY_NOT_COMMITTED", relative.as_posix()) from exc
    if worktree_blob != head_blob:
        raise TimingBlocked("BLOCKED__MEASUREMENT_AUTHORITY_NOT_COMMITTED", relative.as_posix())
    return sha(path)


def load_delegate(repo: Path, enforce_contract_hash: bool = True):
    if not all(sealed_evidence_checks(repo).values()) or not all(protected_manifest_checks(repo).values()):
        raise TimingBlocked("BLOCKED__NEW_C9_SEALED_EVIDENCE_PATH")
    if os.path.lexists(repo / OUTPUT) or not path_components_safe(repo / OUTPUT):
        raise TimingBlocked("BLOCKED__NEW_C9_OUTPUT_EXISTS_OR_UNSAFE")
    preimport_authority_gate(repo, NEW_EXECUTION_ID)
    contract_sha = committed_file(repo, CONTRACT)
    delegate_sha = committed_file(repo, DELEGATE)
    contract = json.loads((repo / CONTRACT).read_text(encoding="utf-8"))
    expected = contract.get("delegate_sha256")
    if (sha(repo / CONTRACT) != contract_sha or not isinstance(expected, str) or
            (enforce_contract_hash and delegate_sha != expected)):
        raise TimingBlocked("BLOCKED__C9_DELEGATE_IDENTITY")
    source = (repo / DELEGATE).read_bytes()
    if hashlib.sha256(source).hexdigest().upper() != delegate_sha:
        raise TimingBlocked("BLOCKED__C9_DELEGATE_IDENTITY")
    spec = importlib.util.spec_from_file_location("c9_timed_risk_delegate", repo / DELEGATE)
    if spec is None or spec.loader is None:
        raise TimingBlocked("BLOCKED__C9_DELEGATE_LOAD")
    module = importlib.util.module_from_spec(spec)
    exec(compile(source, str(repo / DELEGATE), "exec"), module.__dict__)
    return module


def _canonical_map_sha(value: Mapping[str, int]) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True,
                     separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest().upper()


def _adopted_budget(repo: Path) -> dict[str, Any]:
    if sha(repo / BUDGET_PROPOSAL) != BUDGET_PROPOSAL_SHA:
        raise TimingBlocked("BLOCKED__NEW_C9_BUDGET_PROPOSAL_IDENTITY")
    if sha(repo / BUDGET_ADOPTION) != BUDGET_ADOPTION_SHA:
        raise TimingBlocked("BLOCKED__NEW_C9_BUDGET_ADOPTION_IDENTITY")
    budget = json.loads((repo / BUDGET_PROPOSAL).read_text(encoding="utf-8"))
    maps = {
        "category": budget["proposed_c9_per_category_attempt_ceiling"],
        "province": budget["proposed_c9_per_province_attempt_ceiling"],
        "cumulative": budget["proposed_c9_plus_future_c10_cumulative_ceiling"],
        "lifetime": budget["full_old_turn_charge_project_lifetime_governance_ceiling_if_new_grant_adopted_not_calls"],
    }
    if (budget.get("old_execution", {}).get("terminal") != "CALL_LEDGER_UNRESOLVED"
            or budget.get("old_execution", {}).get("attempt_consumed") is not True
            or budget.get("old_execution", {}).get("old_namespace_reset") is not False
            or budget.get("proposed_new_execution_id") != NEW_EXECUTION_ID
            or budget.get("proposed_exclusive_output_root") != OUTPUT.as_posix()
            or budget.get("proposed_new_budget_namespace") != NEW_BUDGET_NAMESPACE
            or budget.get("adopted") is not False
            or budget.get("execution_authorized") is not False
            or budget.get("C10_authorized") is not False
            or budget.get("retries_allowed") != 0
            or any(_canonical_map_sha(value) != MAP_SHA[name]
                   for name, value in maps.items())
            or len(maps["category"]) != 39 or len(maps["province"]) != 5
            or len(maps["cumulative"]) != 39 or len(maps["lifetime"]) != 39
            or any(type(n) is not int or n < 0
                   for value in maps.values() for n in value.values())):
        raise TimingBlocked("BLOCKED__NEW_C9_BUDGET_MAP_IDENTITY")
    charge = {key: row["full_old_turn_governance_charge_not_calls"]
              for key, row in budget["old_failure_category_matrix"].items()}
    if (charge != maps["category"] or
            any(charge[key] + maps["cumulative"][key] != maps["lifetime"][key]
                for key in maps["category"])):
        raise TimingBlocked("BLOCKED__NEW_C9_LIFETIME_GOVERNANCE_IDENTITY")
    return budget


def static_preflight(repo: Path = REPOSITORY, require_inactive: bool = True) -> dict[str, Any]:
    """Validate candidate identities without importing delegate or model science."""
    repo = repo.resolve()
    if type(require_inactive) is not bool:
        raise TimingBlocked("BLOCKED__NEW_C9_PREFLIGHT_STATE")
    sealed = sealed_evidence_checks(repo)
    if not all(sealed.values()):
        raise TimingBlocked("BLOCKED__NEW_C9_SEALED_EVIDENCE_PATH", sealed)
    budget = _adopted_budget(repo)
    checks = {
        "repository": git(repo, "rev-parse", "--show-toplevel").replace("\\", "/").casefold()
                      == repo.as_posix().casefold(),
        "src_tree": git(repo, "rev-parse", "HEAD:src") == SRC_TREE,
        "src_clean": not git(repo, "status", "--porcelain=v1", "--", "src"),
        "new_root_absent": not os.path.lexists(repo / OUTPUT),
        "new_root_path_safe": path_components_safe(repo / OUTPUT),
        "old_root_preserved": sha(repo / OLD_OUTPUT / "partial_artifact_manifest.json")
            == "80BD0D42CB73B4E39B811E759505480542D5A73227014F30B732C34A8AC1FDC3",
        "old_failure_unresolved": sha(repo / OLD_OUTPUT / "timing_failure.json") == OLD_FAILURE_SHA
            and json.loads((repo / OLD_OUTPUT / "timing_failure.json").read_text(encoding="utf-8"))
                .get("terminal") == "CALL_LEDGER_UNRESOLVED",
        "budget_adoption": sha(repo / BUDGET_ADOPTION) == BUDGET_ADOPTION_SHA,
        "budget_proposal": sha(repo / BUDGET_PROPOSAL) == BUDGET_PROPOSAL_SHA,
        "frozen_c8_manifest": sha(repo / C8_ROOT / "execution_artifact_manifest.json") == C8_MANIFEST_SHA,
        "frozen_c8_entering": sha(repo / C8_ROOT / "turn9_entering_bundle_manifest.json") == C8_ENTERING_SHA,
        "frozen_c8_readback": sha(repo / C8_ROOT / "turn9_entering_bundle_readback.json") == C8_READBACK_SHA,
        "frozen_c8_json": sha(repo / C8_ROOT / "turn9_k1b_input_candidate.json") == C8_JSON_SHA,
        "frozen_c8_npz": sha(repo / C8_ROOT / "turn9_k1b_frozen_share_payoff_plan.npz") == C8_NPZ_SHA,
        "new_runner_pair_present": (repo / TIMED_RUNNER).is_file() and (repo / DELEGATE).is_file(),
    }
    if require_inactive:
        checks.update({
            "future_live_contract_absent": not os.path.lexists(repo / CONTRACT),
            "future_execution_adoption_absent": not os.path.lexists(repo / OWNER_ADOPTION),
            "future_execution_task_absent": not os.path.lexists(repo / TASK_COPY),
            "future_independent_review_absent": not os.path.lexists(repo / INDEPENDENT_REVIEW),
        })
    else:
        preimport_authority_gate(repo, NEW_EXECUTION_ID)
        checks["active_authority_committed_and_bound"] = True
    checks.update({f"protected_manifest:{name}": valid
                   for name, valid in protected_manifest_checks(repo).items()})
    if not all(checks.values()):
        raise TimingBlocked("BLOCKED__NEW_C9_STATIC_IDENTITY", checks)
    compile((repo / DELEGATE).read_bytes(), str(repo / DELEGATE), "exec")
    return {
        "status": ("BLOCKED__NEW_LIVE_AUTHORITY_ABSENT__PREPARATION_ONLY"
                   if require_inactive else "ACTIVE_AUTHORITY_STATIC_PREFLIGHT_ONLY__NO_SCIENCE"),
        "checks": checks, "new_execution_id": NEW_EXECUTION_ID,
        "new_budget_namespace": NEW_BUDGET_NAMESPACE,
        "old_actual_ledger": "CALL_LEDGER_UNRESOLVED",
        "old_governance_charge": "FULL_OLD_C9_TURN_CAP__NOT_ACTUAL_CALLS",
        "proposed_map_sha256": MAP_SHA,
        "candidate_wrapper_sha256": sha(repo / TIMED_RUNNER),
        "candidate_delegate_sha256": sha(repo / DELEGATE),
        "output_candidate": str(repo / OUTPUT),
        "scientific_calls": 0, "c9_attempts": 0, "c10_attempts": 0,
        "results_eligibility": False,
    }

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


def cooperative_wall_expired(now_ns: int, deadline_ns: int) -> bool:
    """Only entry checks use this predicate; an in-flight call is not interrupted."""
    return now_ns >= deadline_ns


def _contract_numbers(value: Any, candidate: Mapping[str, int]) -> dict[str, int]:
    if not isinstance(value, dict) or set(value) != set(candidate):
        raise TimingBlocked("BLOCKED__MEASUREMENT_BUDGET_CATEGORY_SET")
    if any(type(value[key]) is not int or not 0 <= value[key] <= candidate[key] for key in candidate):
        raise TimingBlocked("BLOCKED__MEASUREMENT_BUDGET_VALUE")
    return dict(value)


def _exact_int_map(value: Any, expected: Mapping[str, int]) -> bool:
    return (isinstance(value, dict) and set(value) == set(expected) and
            all(type(value[key]) is int and value[key] == expected[key]
                for key in expected))


def preimport_authority_gate(repo: Path, execution_id: str | None) -> dict[str, Any]:
    """Validate the complete committed authority chain without importing modules."""
    if not all(sealed_evidence_checks(repo).values()):
        raise TimingBlocked("BLOCKED__NEW_C9_SEALED_EVIDENCE_PATH")
    if not all(protected_manifest_checks(repo).values()):
        raise TimingBlocked("BLOCKED__NEW_C9_PROTECTED_MANIFEST_IDENTITY")
    if os.path.lexists(repo / OUTPUT) or not path_components_safe(repo / OUTPUT):
        raise TimingBlocked("BLOCKED__NEW_C9_OUTPUT_EXISTS_OR_UNSAFE")
    if execution_id != NEW_EXECUTION_ID:
        raise TimingBlocked("BLOCKED__NEW_C9_EXECUTION_ID")
    if not (repo / CONTRACT).is_file():
        raise TimingBlocked("BLOCKED__NEW_LIVE_CONTRACT_ABSENT")
    budget = _adopted_budget(repo)
    contract_sha = committed_file(repo, CONTRACT)
    wrapper_sha = committed_file(repo, TIMED_RUNNER)
    delegate_sha = committed_file(repo, DELEGATE)
    contract = json.loads((repo / CONTRACT).read_text(encoding="utf-8"))
    category = budget["proposed_c9_per_category_attempt_ceiling"]
    province = budget["proposed_c9_per_province_attempt_ceiling"]
    cumulative = budget["proposed_c9_plus_future_c10_cumulative_ceiling"]
    lifetime = budget["full_old_turn_charge_project_lifetime_governance_ceiling_if_new_grant_adopted_not_calls"]
    old_charge = {key: row["full_old_turn_governance_charge_not_calls"]
                  for key, row in budget["old_failure_category_matrix"].items()}
    if (contract.get("schema") != "CH5_K1B_C9_POST_FAILURE_NEW_ATTEMPT_CONTRACT_V1"
            or contract.get("active") is not True
            or contract.get("execution_id") != NEW_EXECUTION_ID
            or contract.get("output_root") != OUTPUT.as_posix()
            or contract.get("budget_namespace") != NEW_BUDGET_NAMESPACE
            or contract.get("old_execution_id") != OLD_EXECUTION_ID
            or contract.get("old_actual_ledger") != "CALL_LEDGER_UNRESOLVED"
            or contract.get("old_namespace_frozen") is not True
            or contract.get("old_c10_closed") is not True
            or not _exact_int_map(contract.get("old_governance_charge_per_category"), old_charge)
            or not _exact_int_map(contract.get("project_lifetime_governance_ceiling"), lifetime)
            or not _exact_int_map(contract.get("per_category_attempt_ceiling"), category)
            or not _exact_int_map(contract.get("per_province_attempt_ceiling"), province)
            or not _exact_int_map(contract.get("c9_c10_cumulative_ceiling"), cumulative)
            or contract.get("budget_proposal_sha256") != BUDGET_PROPOSAL_SHA
            or contract.get("budget_owner_adoption_sha256") != BUDGET_ADOPTION_SHA
            or contract.get("wrapper_sha256") != wrapper_sha
            or contract.get("delegate_sha256") != delegate_sha
            or contract.get("src_tree") != SRC_TREE
            or type(contract.get("attempts")) is not int or contract.get("attempts") != 1
            or type(contract.get("retries")) is not int or contract.get("retries") != 0
            or type(contract.get("resource_wall_seconds")) is not int
            or contract.get("resource_wall_seconds") != 36000
            or contract.get("resource_policy") != "COOPERATIVE_PROCESS_WALL_CAP"
            or contract.get("automatic_c10_authorization") is not False
            or contract.get("results_eligibility") is not False
            or contract.get("sealed_input_sha256") != {
                "manifest": C8_ENTERING_SHA, "readback": C8_READBACK_SHA,
                "json": C8_JSON_SHA, "npz": C8_NPZ_SHA}):
        raise TimingBlocked("BLOCKED__NEW_C9_CONTRACT_IDENTITY")
    if (sha(repo / C8_ROOT / "execution_artifact_manifest.json") != C8_MANIFEST_SHA
            or sha(repo / C8_ROOT / "turn9_entering_bundle_manifest.json") != C8_ENTERING_SHA
            or sha(repo / C8_ROOT / "turn9_entering_bundle_readback.json") != C8_READBACK_SHA
            or sha(repo / C8_ROOT / "turn9_k1b_input_candidate.json") != C8_JSON_SHA
            or sha(repo / C8_ROOT / "turn9_k1b_frozen_share_payoff_plan.npz") != C8_NPZ_SHA
            or sha(repo / OLD_OUTPUT / "timing_failure.json") != OLD_FAILURE_SHA):
        raise TimingBlocked("BLOCKED__NEW_C9_FROZEN_EVIDENCE_IDENTITY")
    if os.path.lexists(repo / OUTPUT) or not path_components_safe(repo / OUTPUT):
        raise TimingBlocked("BLOCKED__NEW_C9_OUTPUT_EXISTS_OR_UNSAFE")
    current_sha = committed_file(repo, Path("TASK_CURRENT.md"))
    if committed_file(repo, TASK_COPY) != current_sha:
        raise TimingBlocked("BLOCKED__NEW_C9_TASK_COPY")
    task = (repo / "TASK_CURRENT.md").read_text(encoding="utf-8")
    required = (
        f"Task ID: `{TASK_ID}`", f"Status: `{TASK_STATUS}`",
        f"Execution authorization ID: `{NEW_EXECUTION_ID}`",
        f"Authorized output root: `{OUTPUT.as_posix()}`",
        f"Owner adoption SHA-256: `{committed_file(repo, OWNER_ADOPTION)}`",
        f"C9 contract SHA-256: `{contract_sha}`",
        f"Wrapper SHA-256: `{wrapper_sha}`",
        f"Delegate SHA-256: `{delegate_sha}`",
    )
    if not all(item in task for item in required):
        raise TimingBlocked("BLOCKED__NEW_C9_TASK_IDENTITY")
    review_sha = committed_file(repo, INDEPENDENT_REVIEW)
    review = (repo / INDEPENDENT_REVIEW).read_text(encoding="utf-8")
    if ("Reviewer: GPT Work" not in review or
            "Verdict: ACCEPT__C9_POST_FAILURE_NEW_ATTEMPT_RUNNER" not in review or
            f"Wrapper SHA-256: `{wrapper_sha}`" not in review or
            f"Delegate SHA-256: `{delegate_sha}`" not in review or
            contract.get("independent_review_sha256") != review_sha or
            f"Independent review SHA-256: `{review_sha}`" not in task):
        raise TimingBlocked("BLOCKED__NEW_C9_INDEPENDENT_REVIEW_IDENTITY")
    adoption = (repo / OWNER_ADOPTION).read_text(encoding="utf-8")
    if ("OWNER_ADOPTED__SINGLE_NEW_C9_POST_FAILURE" not in adoption or
            f"Execution authorization ID: `{NEW_EXECUTION_ID}`" not in adoption or
            f"Authorized output root: `{OUTPUT.as_posix()}`" not in adoption or
            f"C9 contract SHA-256: `{contract_sha}`" not in adoption or
            f"Independent review SHA-256: `{review_sha}`" not in adoption):
        raise TimingBlocked("BLOCKED__NEW_C9_OWNER_EXECUTION_ADOPTION")
    return {
        "execution_id": NEW_EXECUTION_ID, "ceilings": category,
        "per_province": province, "cumulative": cumulative,
        "old_governance_charge": old_charge, "lifetime_ceiling": lifetime,
        "wall_seconds": 36000, "contract_sha256": contract_sha,
        "owner_adoption_sha256": sha(repo / OWNER_ADOPTION),
        "independent_review_sha256": review_sha, "wrapper_sha256": wrapper_sha,
        "old_actual_ledger": "CALL_LEDGER_UNRESOLVED",
    }


def future_gate(repo: Path, execution_id: str | None, c9: Any) -> dict[str, Any]:
    """Recheck pre-import identities and delegate-specific guards before science."""
    authority = preimport_authority_gate(repo, execution_id)
    if (c9.CEILINGS != authority["ceilings"] or
            c9.PER_PROVINCE != authority["per_province"] or
            c9.TWO_TURN_CEILINGS != authority["cumulative"]):
        raise TimingBlocked("BLOCKED__NEW_C9_DELEGATE_BUDGET_IDENTITY")
    if os.path.lexists(repo / OUTPUT) or not c9.path_components_safe(repo / OUTPUT):
        raise TimingBlocked("BLOCKED__NEW_C9_OUTPUT_EXISTS_OR_UNSAFE")
    return authority

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

def seal_partial_outputs(c9: Any, output: Path, runtime: Mapping[str, Any]) -> dict[str, Any]:
    """Seal only files already present; never classify a failed turn as complete."""
    if not c9.owns_output_root(output, runtime):
        raise TimingBlocked("CALL_LEDGER_UNRESOLVED", "partial root ownership lost")
    excluded = {"partial_artifact_manifest.json", "partial_artifact_readback.json",
                "timing_failure.json"}
    paths = list(output.rglob("*"))
    if not all(c9.path_components_safe(path) for path in paths):
        raise TimingBlocked("CALL_LEDGER_UNRESOLVED", "partial path unsafe")
    files = sorted(path for path in paths if path.is_file() and path.name not in excluded)
    entries = [{"path": path.relative_to(output).as_posix(), "bytes": path.stat().st_size,
                "sha256": sha(path)} for path in files]
    manifest = {"schema": "CH5_K1B_C9_PARTIAL_ARTIFACT_MANIFEST_V1",
                "complete_outer_turn": False, "safe_pause": False,
                "entry_count": len(entries), "entries": entries}
    manifest_path = output / "partial_artifact_manifest.json"
    c9.write_output_json(output, runtime, manifest_path, manifest)
    bad = [row["path"] for row in entries if not (output / row["path"]).is_file()
           or (output / row["path"]).stat().st_size != row["bytes"]
           or sha(output / row["path"]) != row["sha256"]]
    if not c9.owns_output_root(output, runtime):
        bad.append("OUTPUT_ROOT_REPLACED")
    readback = {"status": "PASS" if not bad else "FAIL", "manifest_sha256": sha(manifest_path),
                "bad_paths": bad, "complete_outer_turn": False, "safe_pause": False}
    c9.write_output_json(output, runtime, output / "partial_artifact_readback.json", readback)
    return {"status": readback["status"], "manifest_sha256": readback["manifest_sha256"],
            "readback_sha256": sha(output / "partial_artifact_readback.json"),
            "entry_count": len(entries), "bad_paths": bad}


def run_timed_action(repo: Path, gate: Mapping[str, Any], *,
                     clock: Any = time, utc_now: Any = None) -> dict[str, Any]:
    """Revalidate authority even for direct callers; action is fixed in production."""
    repo = repo.resolve()
    if not all(sealed_evidence_checks(repo).values()) or not all(protected_manifest_checks(repo).values()):
        raise TimingBlocked("BLOCKED__NEW_C9_SEALED_EVIDENCE_PATH")
    if os.path.lexists(repo / OUTPUT) or not path_components_safe(repo / OUTPUT):
        raise TimingBlocked("BLOCKED__NEW_C9_OUTPUT_EXISTS_OR_UNSAFE")
    c9 = load_delegate(repo)
    gate = future_gate(repo, gate.get("execution_id"), c9)
    output = repo / OUTPUT
    if os.path.lexists(output) or not c9.path_components_safe(output):
        raise TimingBlocked("BLOCKED__C9_OUTPUT_EXISTS_OR_UNSAFE")
    start = clock_sample(clock, utc_now)
    record: dict[str, Any] = {}
    runtime_box: dict[str, Any] = {}
    def instrumented_action(start: Mapping[str, Any], record: dict[str, Any],
                            runtime: dict[str, Any]) -> str:
        nonlocal gate
        gate = future_gate(repo, gate.get("execution_id"), c9)
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
                if (self.old_governance != gate["old_governance_charge"] or
                        self.lifetime_governance != gate["lifetime_ceiling"]):
                    raise TimingBlocked("BLOCKED__NEW_C9_LIFETIME_GOVERNANCE_IDENTITY")
                self.open_province: dict[int, dict[str, Any]] = {}
                self.integration_start: dict[str, Any] | None = None
                self.household_start: dict[str, Any] | None = None

            def begin_province(self, province: int, ledger: Mapping[str, Any],
                               envelope: Mapping[str, int]) -> None:
                super().begin_province(province, ledger, envelope)
                self.journal("province_baseline_and_reserved_exposure", {
                    "province": province, "baseline": self.province_baseline[province],
                    "reserved_exposure": dict(envelope), "confirmed_attempted": dict(self.attempted)})

            def reconcile_province(self, province: int, ledger: Mapping[str, Any]) -> None:
                super().reconcile_province(province, ledger)
                self.journal("province_actual_counts_reconciled", {
                    "province": province, "actual": dict(self.per_province[province])})

            def journal(self, event: str, detail: Any = None) -> None:
                nonlocal sequence
                sequence += 1
                try:
                    c9.write_output_json(output, runtime, output / f"attempt_journal_{sequence:07d}.json",
                                         {"event": event, "detail": detail, "execution_id": gate["execution_id"],
                                          "monotonic_ns": time.monotonic_ns(), "attempted": dict(self.attempted),
                                          "per_province": self.per_province,
                                          "budget_namespace": NEW_BUDGET_NAMESPACE,
                                          "old_actual_ledger": "CALL_LEDGER_UNRESOLVED",
                                          "old_governance_charge_not_calls": self.old_governance})
                except BaseException:
                    if runtime.get("state") is not None:
                        runtime["state"]["ledger_unresolved"] = True
                    raise

            def resource_check(self) -> None:
                if cooperative_wall_expired(time.monotonic_ns(), deadline):
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

            def reconcile(self, ledger: Mapping[str, Any], province: int | None = None) -> None:
                super().reconcile(ledger, province)
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
            runtime["c9_timed_guard"] = MeasuredGuard()
            result = c9._execute_after_gate(repo, gate["execution_id"], runtime)
            record["intervals"] = intervals
            record["source_terminal"] = result
            record["attempted"] = dict(runtime["guard"].attempted)
            record["source_ledger"] = dict(runtime["ledger"])
            return result
        finally:
            c9.OUTPUT, c9.FUTURE_TASK_RELATIVE = original_output, original_task
            c9.PER_PROVINCE, c9.BudgetGuard = original_province, original_guard

    def invoke(runtime: dict[str, Any]) -> str:
        runtime_box["runtime"] = runtime
        return instrumented_action(start, record, runtime)
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
        end = clock_sample(clock, utc_now)
        elapsed = elapsed_clock(start, end)
        seal_interval = {"stage": "seal_and_readback", "start": seal_start,
                         "end": end, "elapsed_ns": elapsed_clock(seal_start, end)}
        receipt = {"terminal": result, "safe_pause_pending": True,
                   "original_numerical_terminal": result,
                   "classification": "SINGLE_C9_TIMED_RISK_EXCEPTION_OBSERVED_ONLY",
                   "execution_id": gate["execution_id"], "start": start, "science_end": end_science,
                   "complete_seal_end": end, "elapsed_ns": elapsed,
                   "science_artifacts": sealed,
                   "stage_intervals": record.get("intervals", []) + [seal_interval],
                   "attempted": record.get("attempted"), "source_ledger": record.get("source_ledger"),
                   "environment": c9.environment_snapshot(), "pid": os.getpid(),
                   "argv": list(sys.argv), "output_root": str(output),
                   "budget_namespace": NEW_BUDGET_NAMESPACE,
                   "old_actual_ledger": "CALL_LEDGER_UNRESOLVED",
                   "old_governance_charge_not_calls": gate["old_governance_charge"],
                   "project_lifetime_governance_ceiling_not_calls": gate["lifetime_ceiling"],
                   "owner_adoption_sha256": gate["owner_adoption_sha256"],
                   "c9_contract_sha256": gate["contract_sha256"],
                   "c9_c10_upper_duration_bound": None, "results_eligibility": False}
        c9.write_output_json(output, runtime, output / "timing_receipt.json", receipt)
        pause["timing_receipt_sha256"] = c9.sha(output / "timing_receipt.json")
        pause["pause_clock"] = clock_sample(clock, utc_now)
        # Final write: no later fallible operation may precede the safe-pause verdict.
        c9.write_output_json(output, runtime, output / "pause_receipt.json", pause)
        return {**receipt, "terminal": "SAFE_PAUSE_AFTER_SEALED_C9",
                "safe_pause_pending": False}
    except BaseException as exc:
        runtime = runtime_box.get("runtime", {})
        state = runtime.get("state") or {}
        original = state.get("original_terminal") or getattr(exc, "terminal", type(exc).__name__)
        guard = runtime.get("guard")
        ambiguous = (guard is None or bool(getattr(guard, "open_province", {})) or
                     getattr(guard, "integration_start", None) is not None or
                     bool(state.get("ledger_unresolved")))
        terminal = "CALL_LEDGER_UNRESOLVED" if ambiguous else original
        partial = None
        owned = runtime.get("output_identity") is not None and c9.owns_output_root(output, runtime)
        if owned:
            try:
                partial = seal_partial_outputs(c9, output, runtime)
                if partial["status"] != "PASS":
                    terminal = "CALL_LEDGER_UNRESOLVED"
            except BaseException as seal_failure:
                terminal = "CALL_LEDGER_UNRESOLVED"
                partial = {"status": "UNRESOLVED", "cause":
                           getattr(seal_failure, "terminal", type(seal_failure).__name__)}
            try:
                c9.write_output_json(output, runtime, output / "timing_failure.json",
                                     {"terminal": terminal, "original_terminal": original,
                                      "execution_id": gate["execution_id"], "start": start,
                                      "end": clock_sample(clock, utc_now),
                                      "confirmed_attempted": dict(guard.attempted) if guard else None,
                                      "per_province_attempted": guard.per_province if guard else None,
                                      "reserved_exposure": runtime.get("reserved_exposure_at_interruption"),
                                      "inflight_province": runtime.get("inflight_province"),
                                      "source_ledger": runtime.get("ledger"),
                                      "budget_namespace": NEW_BUDGET_NAMESPACE,
                                      "old_actual_ledger": "CALL_LEDGER_UNRESOLVED",
                                      "old_governance_charge_not_calls": gate.get("old_governance_charge"),
                                      "project_lifetime_governance_ceiling_not_calls": gate.get("lifetime_ceiling"),
                                      "partial_artifacts": partial,
                                      "complete_outer_turn": False, "safe_pause": False,
                                      "retry_allowed": False})
            except BaseException:
                terminal = "CALL_LEDGER_UNRESOLVED"
        elif runtime.get("output_identity") is not None:
            terminal = "CALL_LEDGER_UNRESOLVED"
        raise TimingBlocked(terminal, {"original_terminal": original,
                                      "partial_artifacts": partial,
                                      "retry_allowed": False}) from exc
    finally:
        c9.OUTPUT = original_output


def execute_once(repo: Path = REPOSITORY, execution_id: str | None = None) -> dict[str, Any]:
    """Future-only gate. Never call from the zero-science preparation task."""
    repo = repo.resolve()
    if execution_id != NEW_EXECUTION_ID:
        raise TimingBlocked("BLOCKED__NEW_C9_EXECUTION_ID")
    if not (repo / CONTRACT).is_file():
        raise TimingBlocked("BLOCKED__NEW_LIVE_CONTRACT_ABSENT")
    if not (repo / OWNER_ADOPTION).is_file() or not (repo / TASK_COPY).is_file() or not (repo / INDEPENDENT_REVIEW).is_file():
        raise TimingBlocked("BLOCKED__NEW_EXECUTION_AUTHORITY_ABSENT")
    return run_timed_action(repo, {"execution_id": execution_id})


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
