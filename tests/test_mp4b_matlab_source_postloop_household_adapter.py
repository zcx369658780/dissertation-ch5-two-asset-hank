from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

from validators.multi_province.mp4b_matlab_source_postloop_household_adapter import (
    solve_matlab_source_postloop_household,
)


ROOT = Path(__file__).parents[1]
MAP = ROOT / "validators" / "multi_province" / "mp4b_nonconverged_hjb_source_semantics_map.json"
ENTRY = ROOT / "validators" / "multi_province" / "mp4b_python_empirical.py"
ADAPTER = ROOT / "validators" / "multi_province" / "mp4b_matlab_source_postloop_household_adapter.py"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def test_protected_source_semantic_map_is_complete_and_hash_locked():
    payload = json.loads(MAP.read_text(encoding="utf-8"))
    assert payload["adjudication"] == "UNAMBIGUOUS"
    assert payload["junction"] == {
        "path": r"C:\MatlabProgram", "link_type": "Junction", "target": r"D:\MatlabProgram"}
    assert {name: item["sha256"] for name, item in payload["sources"].items()} == {
        "HANK_2ASSETS_HJB.m": "049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE",
        "HANK_mp_1turn.m": "D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF",
        "HANK_mp_1eq.m": "ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF",
    }


def test_protected_sources_match_the_semantic_map_without_execution():
    payload = json.loads(MAP.read_text(encoding="utf-8"))
    root = Path(payload["logical_root"])
    assert {name: _sha256(root / name) for name in payload["sources"]} == {
        name: item["sha256"] for name, item in payload["sources"].items()}


def test_production_export_and_mp2_mp3_authorities_remain_hash_locked():
    expected = {
        "src/ch5_two_asset_hank/economics.py": "F2B67D393D7495A83281C259F6D9CC5F8AFF18B3C4ABDEB7A07F354582DEF2D1",
        "src/ch5_two_asset_hank/matlab_faithful_policy.py": "ECF56FAA7E87A0F5156E5866F1873556D6603E98AA33C8E41C400FD016C75CDC",
        "exports/matlab_faithful_two_asset_ha.py": "B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3",
        "src/ch5_two_asset_hank/multi_province/one_turn.py": "D18C4385745E33E917B79994CAA069BE8825C9F22919A5A9EDE918845312D98D",
        "src/ch5_two_asset_hank/multi_province/steady_state.py": "7065D0FCBFDA6A88C8F773DEBDF277F6E300A8E0195B7CC635F7A0033D74D88C",
    }
    assert {path: _sha256(ROOT / path) for path in expected} == expected


@pytest.mark.parametrize("converged", [False, True])
def test_adapter_uses_one_identical_postloop_composition_path(converged):
    calls = []
    operator = SimpleNamespace(full=object())
    hjb = SimpleNamespace(
        converged=converged, iterations=100 if not converged else 7,
        convergence_statistic=0.25 if not converged else 1e-9,
        post_convergence_operator=operator,
        consumption=object(), labor=object(),
    )
    kfe = SimpleNamespace(density=object())
    aggregates = object()

    def hjb_stub(*args):
        calls.append(("hjb", args))
        return hjb

    def kfe_stub(value, **kwargs):
        calls.append(("kfe", value, kwargs))
        return kfe

    def aggregate_stub(*args):
        calls.append(("aggregate", args))
        return aggregates

    grid = SimpleNamespace(
        b=np.array([-2.0, 5.0]), a=np.array([0.0, 10.0]), z=np.array([0.8, 1.3]))
    result = solve_matlab_source_postloop_household(
        grid, "params", "inputs", "initial", "labor", 0.1, 0.07, "numerics",
        hjb_solver=hjb_stub, kfe_solver=kfe_stub, aggregator=aggregate_stub,
    )
    assert [item[0] for item in calls] == ["hjb", "kfe", "aggregate"]
    assert calls[1][1] is operator.full
    assert calls[1][2] == {"shape": (2, 2, 2), "db": 7.0, "da": 10.0}
    assert calls[2][1] == (grid, hjb.consumption, hjb.labor, kfe.density)
    assert result.hjb is hjb and result.kfe is kfe and result.aggregates is aggregates
    assert (result.hjb.converged, result.hjb.iterations, result.hjb.convergence_statistic) == (
        converged, hjb.iterations, hjb.convergence_statistic)


def test_adapter_has_no_retry_branch_or_import_time_call():
    tree = ast.parse(ADAPTER.read_text(encoding="utf-8"))
    function = next(node for node in tree.body if isinstance(node, ast.FunctionDef))
    calls = [node for node in ast.walk(function) if isinstance(node, ast.Call)]
    names = [node.func.id for node in calls if isinstance(node.func, ast.Name)]
    assert names.count("hjb_solver") == names.count("kfe_solver") == names.count("aggregator") == 1
    assert not any(isinstance(node, (ast.For, ast.While, ast.Try)) for node in ast.walk(function))
    assert all(not isinstance(node, ast.Call) for node in tree.body)


def test_validation_driver_uses_adapter_and_propagates_all_hjb_diagnostics():
    text = ENTRY.read_text(encoding="utf-8")
    assert "solve_matlab_source_postloop_household(" in text
    assert "solve_household_steady_state(" not in text
    for field in ("hjb_converged", "hjb_iterations", "hjb_statistic"):
        assert field in text
    assert "result.hjb.converged" in text
    assert "from chapter5_model" not in text and "import chapter5_model" not in text


def test_validation_import_path_has_no_module_level_model_call():
    tree = ast.parse(ENTRY.read_text(encoding="utf-8"))
    forbidden = {"solve_matlab_source_postloop_household", "run_online_stationary",
                 "solve_matlab_faithful_hjb", "solve_matlab_faithful_stationary_kfe"}
    module_calls = [node for node in tree.body if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)]
    assigned_calls = [node.value for node in tree.body if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call)]
    names = {call.func.id for call in assigned_calls if isinstance(call.func, ast.Name)}
    assert not module_calls and names.isdisjoint(forbidden)
