from __future__ import annotations

import ast
import copy
import json
from pathlib import Path

import pytest

from validators.multi_province.mp1_fixture_arithmetic import (
    assert_close,
    evaluate_fixture,
    load_fixture,
    validate_fixture,
)


REPO = Path(__file__).resolve().parents[1]
FIXTURE_PATH = REPO / "tests" / "fixtures" / "multi_province" / "mp1_asymmetric_one_turn.json"


@pytest.fixture()
def fixture_data() -> dict:
    return load_fixture(FIXTURE_PATH)


def test_fixture_is_reproducible_from_independent_source_formula_arithmetic(fixture_data: dict) -> None:
    assert_close(evaluate_fixture(fixture_data), fixture_data["expected"])


def test_transpose_changes_destination_labor_and_fails(fixture_data: dict) -> None:
    actual = evaluate_fixture(fixture_data)
    transposed = [list(row) for row in zip(*actual["Lt_mat"])]
    wrong_supply = [sum(row) for row in transposed]
    with pytest.raises(AssertionError):
        assert_close(wrong_supply, fixture_data["expected"]["Lt_supply"])


def test_at_plus_bt_is_forbidden_and_bt_alone_is_productive_capital_invariant(fixture_data: dict) -> None:
    expected = evaluate_fixture(fixture_data)
    bt_changed = copy.deepcopy(fixture_data)
    for i, province in enumerate(bt_changed["provinces"], start=1):
        province["Bt"] += 10.0 * i
    changed = evaluate_fixture(bt_changed)
    assert_close(changed["capital_contribution"], expected["capital_contribution"])
    assert_close(changed["Kt_supply"], expected["Kt_supply"])

    provinces = fixture_data["provinces"]
    wrong = [p["inter_prv_ratio"] * (p["At"] + p["Bt"]) * p["N"] for p in provinces]
    with pytest.raises(AssertionError):
        assert_close(wrong, expected["capital_contribution"])


def test_literal_source_rah_is_not_generic_matrix_average(fixture_data: dict) -> None:
    expected_rah = evaluate_fixture(fixture_data)["rah"]
    provinces = fixture_data["provinces"]
    # A plausible generic row-normalized W @ r is intentionally not the MATLAB formula.
    generic = []
    for i, household in enumerate(provinces):
        outside = sum(p["ra"] for j, p in enumerate(provinces) if j != i) / 2.0
        generic.append((1.0 - household["inter_prv_ratio"]) * household["ra"] + household["inter_prv_ratio"] * outside)
    with pytest.raises(AssertionError):
        assert_close(generic, expected_rah)


def test_order_and_shape_mutations_fail_closed(fixture_data: dict) -> None:
    reordered = copy.deepcopy(fixture_data)
    reordered["province_order"][0], reordered["province_order"][1] = (
        reordered["province_order"][1], reordered["province_order"][0]
    )
    with pytest.raises(ValueError, match="province records"):
        validate_fixture(reordered)

    malformed = copy.deepcopy(fixture_data)
    malformed["sigmau_mat"][0].pop()
    with pytest.raises(ValueError, match="shape"):
        validate_fixture(malformed)


def test_no_legacy_r5_import_in_active_mp1_python() -> None:
    roots = [REPO / "validators" / "multi_province", REPO / "src" / "ch5_two_asset_hank" / "multi_province"]
    forbidden = {"chapter5_model", "dissertation-ch5-r5-python-model"}
    violations: list[str] = []
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*.py"):
            source = path.read_text(encoding="utf-8")
            tree = ast.parse(source, filename=str(path))
            imported = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imported.extend(alias.name for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imported.append(node.module)
            if any(any(name == item or name.startswith(item + ".") for item in forbidden) for name in imported):
                violations.append(str(path.relative_to(REPO)))
    assert violations == []


def test_fixture_contains_no_empirical_or_legacy_payload(fixture_data: dict) -> None:
    text = json.dumps(fixture_data, ensure_ascii=False).lower()
    assert fixture_data["classification"] == "NON_CALIBRATION_SYNTHETIC_OR_SOURCE_FORMULA_FIXTURE"
    assert ".mat" not in text and ".xlsx" not in text
    assert "chapter5_model" not in text and "dissertation-ch5-r5-python-model" not in text
    injected = copy.deepcopy(fixture_data)
    injected["runtime_import"] = "chapter5_model"
    with pytest.raises(ValueError, match="legacy R5"):
        validate_fixture(injected)
