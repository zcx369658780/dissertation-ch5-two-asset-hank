"""Static corrected-2018 input-contract tests; scientific/model calls are zero."""

from __future__ import annotations

import json
from dataclasses import asdict, replace
from pathlib import Path

import pytest

from ch5_two_asset_hank.multi_province.corrected_2018_runtime import (
    CAPITAL_ROUTE,
    MONEY_UNIT,
    Corrected2018RuntimeInputs,
    Corrected2018RuntimeMetadata,
    build_corrected_2018_runtime_inputs,
    payload_sha256,
    validate_serialized_payload,
)
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER


REPO = Path(__file__).resolve().parents[1]
LEDGER = REPO / "reports/mp4c_2018_raw_nbs_rebuild_20260910/corrected_2018_vs_matlab_ledger.csv"
EXPECTED = REPO / "reports/mp4c_unit_normalized_initialization_probe_20260910/province_initialization_receipt.csv"
WEDGES = tuple(tuple(0.0 for _ in range(31)) for _ in range(31))


def runtime() -> Corrected2018RuntimeInputs:
    return build_corrected_2018_runtime_inputs(
        LEDGER, EXPECTED, WEDGES,
        {"sha256": "STATIC_TEST_DISTANCE", "bytes": 0, "role": "CROSS_PROVINCE_DISTANCE_ONLY"},
    )


def test_builder_matches_accepted_31_province_receipt() -> None:
    value = runtime()
    value.validate_pre_science()
    assert len(value.provinces) == 31
    assert tuple(item.province for item in value.provinces) == PROVINCE_ORDER
    anhui = value.provinces[11]
    assert (anhui.y0_mu, anhui.n0_nu, anhui.k0_mu, anhui.alpha_used) == (
        34010900.0, 607600.0, 70182433.35888097, 0.7380939146868483)
    assert anhui.zt0 == pytest.approx(1.681124916844091, rel=2e-15)
    assert anhui.gov_inv0_mu == anhui.k0_mu


def test_corrected_route_cannot_be_confused_with_legacy_schema() -> None:
    metadata = asdict(runtime().metadata)
    assert metadata["capital_route"] == CAPITAL_ROUTE
    assert metadata["capital_unit"] == MONEY_UNIT
    assert "canonical" not in metadata["capital_route"].lower()
    with pytest.raises(ValueError, match="metadata mismatch"):
        validate_serialized_payload({**runtime().to_payload(), "metadata": {
            **metadata, "capital_route": "LEGACY_CANONICAL_TRANSFORMED_CAPITAL"}})


def test_rejected_old_scale_anhui_is_blocked_before_science() -> None:
    payload = runtime().to_payload()
    payload["states"][11]["Kt0"] = 1357314108201.3684
    payload["states"][11]["GovInv"] = 1357314108201.3684
    payload["states"][11]["Zt"] = 0.0006934644495858679
    with pytest.raises(ValueError, match="active state/input mismatch|old-scale"):
        validate_serialized_payload(payload)


def test_any_province_value_change_is_blocked_even_if_state_matches() -> None:
    payload = runtime().to_payload()
    payload["province_inputs"][0]["k0_mu"] += 1.0
    payload["states"][0]["Kt0"] += 1.0
    with pytest.raises(ValueError, match="immutable accepted receipt"):
        validate_serialized_payload(payload)


def test_serialization_round_trip_preserves_routes_units_and_roles() -> None:
    payload = runtime().to_payload()
    restored = json.loads(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    validate_serialized_payload(restored)
    assert restored["metadata"] == payload["metadata"]
    assert restored["metadata"]["population_proxy_role"] == "population_proxy_NU"
    assert restored["metadata"]["household_labor_role"] == "household_labor_per_capita"
    assert restored["metadata"]["firm_labor_role"] == "firm_Lt_supply"


@pytest.mark.parametrize(("section", "key", "replacement"), [
    ("metadata", "capital_route", "OTHER_ROUTE"),
    ("metadata", "capital_unit", "YUAN"),
    ("states", 11, "capital_value"),
])
def test_payload_hash_changes_with_route_unit_or_value(section: str, key: object, replacement: str) -> None:
    payload = runtime().to_payload()
    original = payload_sha256(payload)
    changed = json.loads(json.dumps(payload, ensure_ascii=False))
    if section == "states":
        changed["states"][int(key)]["Kt0"] += 1.0
    else:
        changed[section][str(key)] = replacement
    assert payload_sha256(changed) != original


def test_province_order_mismatch_fails() -> None:
    value = runtime()
    swapped = (value.provinces[1], value.provinces[0], *value.provinces[2:])
    with pytest.raises(ValueError, match="province order"):
        replace(value, provinces=swapped).validate_pre_science()


def test_missing_corrected_input_fails_closed(tmp_path: Path) -> None:
    missing = tmp_path / "missing.csv"
    with pytest.raises(FileNotFoundError):
        build_corrected_2018_runtime_inputs(missing, EXPECTED, WEDGES, {})


def test_govinv_capital_unit_mismatch_fails() -> None:
    value = runtime()
    bad_metadata = replace(value.metadata, gov_inv0_unit="YUAN")
    with pytest.raises(ValueError, match="metadata mismatch|identical declared units"):
        replace(value, metadata=bad_metadata).validate_pre_science()


def test_module_is_solver_free_and_test_budget_is_zero() -> None:
    source = (REPO / "src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py").read_text(encoding="utf-8")
    forbidden = ("solve_matlab_faithful_hjb(", "stationary_kfe(", "evaluate_firm(",
                 "brentq(", "run_source_faithful_one_turn(", "Lt_seperate(")
    assert all(token not in source for token in forbidden)
