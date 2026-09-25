"""Only static and inert-stub checks; never invoke --execute or model science."""
import importlib.util
import io
import json
import os
import sys
from contextlib import redirect_stdout
from datetime import datetime, timezone, timedelta
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.dont_write_bytecode = True
RUNNER = (Path(__file__).resolve().parents[1] /
          "validators/multi_province/k1b_turn8_same_frozen_timing_measurement/run.py")
spec = importlib.util.spec_from_file_location("c8_timing_static", RUNNER)
runner = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(runner)


def test_default_cli_static_and_measurement_root_absent(monkeypatch):
    monkeypatch.setattr(runner, "execute_once", lambda *_: pytest.fail("science path reached"))
    with redirect_stdout(io.StringIO()) as stream:
        assert runner.main([]) == 0
    result = json.loads(stream.getvalue())
    assert result["status"] == "PASS__STATIC_PREFLIGHT_ONLY"
    assert result["scientific_calls"] == 0
    assert result["duration_upper_bound_claim"] is False
    assert all(result["checks"].values()) and all(result["delegated_checks"].values())
    assert not os.path.lexists(runner.REPOSITORY / runner.OUTPUT)
    assert "ch5_two_asset_hank.corrected_diagnostic.optionb_turn2_household_integration" not in sys.modules


def test_current_task_and_wrong_execution_id_refuse_before_output(monkeypatch):
    c8 = runner.accepted_runner(runner.REPOSITORY)
    # The wrapper is being edited in this repair task: isolate the expected
    # pre-commit identity refusal before asserting the later task gate.
    with pytest.raises(runner.TimingBlocked) as err:
        runner.future_gate(runner.REPOSITORY, "inert-id", c8)
    assert err.value.terminal == "BLOCKED__MEASUREMENT_AUTHORITY_DIRTY_OR_MISSING"
    real_committed = runner.committed_file
    monkeypatch.setattr(runner, "committed_file",
                        lambda repo, path: ("INERT_COMMITTED_WRAPPER" if path == runner.MEASUREMENT_RUNNER
                                            else real_committed(repo, path)))
    with pytest.raises(runner.TimingBlocked) as err:
        runner.future_gate(runner.REPOSITORY, "inert-id", c8)
    assert err.value.terminal == "BLOCKED__FRESH_MEASUREMENT_TASK_GATE"
    with pytest.raises(runner.TimingBlocked) as err:
        runner.future_gate(runner.REPOSITORY, "bad/id", c8)
    assert err.value.terminal == "EXECUTION_AUTHORIZATION_REQUIRED"
    assert not os.path.lexists(runner.REPOSITORY / runner.OUTPUT)


@pytest.mark.parametrize("name,value", [
    ("SRC_TREE", "0" * 40), ("C7_MANIFEST_SHA", "0" * 64),
    ("C7_ENTERING_SHA", "0" * 64), ("C7_READBACK_SHA", "0" * 64),
    ("ACCEPTED_RUNNER_SHA", "0" * 64),
])
def test_wrong_source_manifest_or_helper_refuses_static(monkeypatch, name, value):
    monkeypatch.setattr(runner, name, value)
    with pytest.raises(runner.TimingBlocked):
        runner.static_preflight()
    assert not os.path.lexists(runner.REPOSITORY / runner.OUTPUT)


def test_budget_category_value_and_namespace_are_separate(monkeypatch, tmp_path):
    c8 = SimpleNamespace(CEILINGS={"direct_hjb_updates": 1550},
                         PER_PROVINCE={"direct_hjb_updates": 50},
                         path_components_safe=lambda *_: True)
    with pytest.raises(runner.TimingBlocked):
        runner._contract_numbers({"direct_hjb_updates": 1551}, c8.CEILINGS)
    with pytest.raises(runner.TimingBlocked):
        runner._contract_numbers({"firm_evaluations": 1}, c8.CEILINGS)
    execution_id = "inert-measurement"
    required = (f"Task ID: `{runner.TASK_ID}`\nStatus: `{runner.TASK_STATUS}`\n"
                f"Execution authorization ID: `{execution_id}`\n"
                f"Authorized output root: `{runner.OUTPUT.as_posix()}`\n"
                "Owner adoption SHA-256: `ADOPTION`\nMeasurement contract SHA-256: `CONTRACT`\n"
                "Independent review SHA-256: `REVIEW`\nWrapper SHA-256: `RUNNER`\n")
    adoption = ("OWNER_ADOPTED__SEPARATE_SINGLE_C8_TIMING_BUDGET\n"
                f"Execution authorization ID: `{execution_id}`\n"
                f"Authorized output root: `{runner.OUTPUT.as_posix()}`\n"
                "Measurement contract SHA-256: `CONTRACT`\n"
                "Independent review SHA-256: `REVIEW`\nWrapper SHA-256: `RUNNER`")
    review = ("Reviewer: GPT Work\nVerdict: ACCEPT__C8_SAME_FROZEN_TIMING_WRAPPER\n"
              f"Wrapper path: `{runner.MEASUREMENT_RUNNER.as_posix()}`\n"
              "Wrapper SHA-256: `RUNNER`")
    contract = {"schema": "CH5_K1B_SEPARATE_SINGLE_C8_TIMING_CONTRACT_V1",
                "execution_id": execution_id, "output_root": runner.OUTPUT.as_posix(),
                "attempts": 1, "budget_namespace": "C9_C10",  # deliberately wrong
                "wrapper_sha256": "RUNNER", "independent_review_sha256": "REVIEW",
                "resource_policy": "COOPERATIVE_PROCESS_WALL_CAP",
                "resource_wall_seconds": 1,
                "per_category_attempt_ceiling": {"direct_hjb_updates": 50},
                "per_province_attempt_ceiling": {"direct_hjb_updates": 50}}
    texts = {str(tmp_path / "TASK_CURRENT.md"): required,
             str(tmp_path / runner.TASK_COPY): required,
             str(tmp_path / runner.OWNER_ADOPTION): adoption,
             str(tmp_path / runner.INDEPENDENT_REVIEW): review,
             str(tmp_path / runner.CONTRACT): json.dumps(contract)}
    original_read = Path.read_text
    def read_text(path, *args, **kwargs):
        key = str(path)
        return texts[key] if key in texts else original_read(path, *args, **kwargs)
    monkeypatch.setattr(Path, "read_text", read_text)
    monkeypatch.setattr(runner, "committed_file",
                        lambda repo, rel: {runner.MEASUREMENT_RUNNER: "RUNNER",
                                           Path("TASK_CURRENT.md"): "TASK",
                                           runner.TASK_COPY: "TASK",
                                           runner.INDEPENDENT_REVIEW: "REVIEW",
                                           runner.OWNER_ADOPTION: "ADOPTION",
                                           runner.CONTRACT: "CONTRACT"}[rel])
    texts[str(tmp_path / runner.INDEPENDENT_REVIEW)] = review.replace("Wrapper SHA-256: `RUNNER`", "Wrapper SHA-256: `STALE`")
    with pytest.raises(runner.TimingBlocked) as err:
        runner.future_gate(tmp_path, execution_id, c8)
    assert err.value.terminal == "BLOCKED__INDEPENDENT_WRAPPER_REVIEW_IDENTITY"
    texts[str(tmp_path / runner.INDEPENDENT_REVIEW)] = review
    texts[str(tmp_path / "TASK_CURRENT.md")] = required.replace("Wrapper SHA-256: `RUNNER`", "Wrapper SHA-256: `STALE`")
    with pytest.raises(runner.TimingBlocked) as err:
        runner.future_gate(tmp_path, execution_id, c8)
    assert err.value.terminal == "BLOCKED__MEASUREMENT_CONTRACT_BINDING"
    texts[str(tmp_path / "TASK_CURRENT.md")] = required
    texts[str(tmp_path / runner.OWNER_ADOPTION)] = adoption.replace("Wrapper SHA-256: `RUNNER`", "Wrapper SHA-256: `STALE`")
    with pytest.raises(runner.TimingBlocked) as err:
        runner.future_gate(tmp_path, execution_id, c8)
    assert err.value.terminal == "BLOCKED__OWNER_MEASUREMENT_ADOPTION"
    texts[str(tmp_path / runner.OWNER_ADOPTION)] = adoption
    contract["wrapper_sha256"] = "STALE"
    texts[str(tmp_path / runner.CONTRACT)] = json.dumps(contract)
    with pytest.raises(runner.TimingBlocked) as err:
        runner.future_gate(tmp_path, execution_id, c8)
    assert err.value.terminal == "BLOCKED__MEASUREMENT_CONTRACT_IDENTITY"
    contract["wrapper_sha256"] = "RUNNER"
    texts[str(tmp_path / runner.CONTRACT)] = json.dumps(contract)
    with pytest.raises(runner.TimingBlocked) as err:
        runner.future_gate(tmp_path, execution_id, c8)
    assert err.value.terminal == "BLOCKED__MEASUREMENT_CONTRACT_IDENTITY"
    contract["budget_namespace"] = "SEPARATE_C8_TIMING_ONLY"
    texts[str(tmp_path / runner.CONTRACT)] = json.dumps(contract)
    gate = runner.future_gate(tmp_path, execution_id, c8)
    assert gate["ceilings"] == {"direct_hjb_updates": 50}
    assert gate["per_province"] == {"direct_hjb_updates": 50}
    assert gate["wrapper_sha256"] == "RUNNER"
    assert gate["independent_review_sha256"] == "REVIEW"


def test_missing_independent_review_refuses_before_budget(monkeypatch, tmp_path):
    c8 = SimpleNamespace()
    monkeypatch.setattr(runner, "committed_file",
                        lambda repo, rel: (_ for _ in ()).throw(
                            runner.TimingBlocked("BLOCKED__MEASUREMENT_AUTHORITY_DIRTY_OR_MISSING"))
                        if rel == runner.INDEPENDENT_REVIEW else "SAME")
    fields = (f"Task ID: `{runner.TASK_ID}`\nStatus: `{runner.TASK_STATUS}`\n"
              "Execution authorization ID: `inert`\n"
              f"Authorized output root: `{runner.OUTPUT.as_posix()}`")
    monkeypatch.setattr(Path, "read_text", lambda *_args, **_kwargs: fields)
    with pytest.raises(runner.TimingBlocked) as err:
        runner.future_gate(tmp_path, "inert", c8)
    assert err.value.terminal == "BLOCKED__MEASUREMENT_AUTHORITY_DIRTY_OR_MISSING"


def test_inert_original_numerical_terminal_is_not_overridden():
    original = lambda prior, carrier: "VALID__LEVEL_NOT_MET_AT_BUDGET"
    c8 = SimpleNamespace(OUTPUT=Path("protected"), FUTURE_TASK_RELATIVE=Path("original-task"),
                         PER_PROVINCE={}, BudgetGuard=object, turn8_terminal=original)
    terminal = "VALID__LEVEL_NOT_MET_AT_BUDGET"
    def inert_delegate(repo, execution_id, runtime):
        assert c8.turn8_terminal is original
        runtime["guard"] = SimpleNamespace(attempted={"direct_hjb_updates": 0})
        runtime["ledger"] = {"direct_hjb_updates": 0}
        return terminal
    c8._execute_after_gate = inert_delegate
    runtime, record = {}, {}
    result = runner._instrumented_action(c8, Path("unused"),
        {"execution_id": "inert", "wall_seconds": 1, "ceilings": {}, "per_province": {}},
        {"monotonic_ns": runner.time.monotonic_ns()}, record, runtime)
    assert result == record["source_terminal"] == terminal
    assert c8.turn8_terminal is original


def test_preexisting_or_replaced_root_refused_without_science(monkeypatch, tmp_path):
    c8 = SimpleNamespace(OUTPUT=Path("accepted-protected-root"))
    gate = {"execution_id": "inert-id"}
    monkeypatch.setattr(runner.os.path, "lexists", lambda p: True)
    with pytest.raises(runner.TimingBlocked) as err:
        runner.run_timed_action(tmp_path, gate, c8,
                                action=lambda *_: pytest.fail("science path reached"))
    assert err.value.terminal == "BLOCKED__MEASUREMENT_OUTPUT_EXISTS_OR_UNSAFE"
    monkeypatch.setattr(runner.os.path, "lexists", lambda p: False)
    c8.owns_output_root = lambda *_: False
    with pytest.raises(runner.TimingBlocked) as err:
        runner.seal_science_outputs(c8, tmp_path / runner.OUTPUT, {})
    assert err.value.terminal == "BLOCKED__MEASUREMENT_OUTPUT_REPLACED"


def test_monotonic_elapsed_and_invalid_clock_mapping():
    start = {"monotonic_ns": 1_000_000_000,
             "utc": "2026-09-25T12:00:00+00:00"}
    end = {"monotonic_ns": 2_500_000_000,
           "utc": "2026-09-25T12:00:01.500000+00:00"}
    assert runner.elapsed_clock(start, end) == 1_500_000_000
    with pytest.raises(runner.TimingBlocked):
        runner.elapsed_clock(start, {**end, "monotonic_ns": 1})
    with pytest.raises(runner.TimingBlocked):
        runner.elapsed_clock(start, {**end, "utc": "2026-09-25T12:01:00+00:00"})
    with pytest.raises(runner.TimingBlocked):
        runner.clock_sample(SimpleNamespace(monotonic_ns=lambda: 1),
                            lambda: datetime(2026, 9, 25))


@pytest.mark.parametrize("failure,open_province,expected", [
    (runner.TimingBlocked("FIRST_FAILURE"), {}, "FIRST_FAILURE"),
    (KeyboardInterrupt(), {0: {"monotonic_ns": 1}}, "CALL_LEDGER_UNRESOLVED"),
])
def test_inert_first_failure_and_manual_interruption_preserve_attempts(
        monkeypatch, tmp_path, failure, open_province, expected):
    monkeypatch.setattr(runner.os.path, "lexists", lambda p: False)
    attempted = {"direct_hjb_updates": 1}
    runtime = {"guard": SimpleNamespace(attempted=attempted, open_province=open_province),
               "ledger": {"direct_hjb_updates": 0}, "output_identity": None}
    def run_after_gate(repo, execution_id, action):
        action(runtime)
    c8 = SimpleNamespace(OUTPUT=Path("accepted-protected-root"),
                         run_after_valid_gate=run_after_gate)
    def inert_action(*_):
        raise failure
    with pytest.raises(runner.TimingBlocked) as err:
        runner.run_timed_action(tmp_path, {"execution_id": "inert-id"}, c8,
                                action=inert_action)
    assert err.value.terminal == expected
    assert attempted == {"direct_hjb_updates": 1}
    assert c8.OUTPUT == Path("accepted-protected-root")
