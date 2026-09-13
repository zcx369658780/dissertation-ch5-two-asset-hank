from __future__ import annotations

import csv
import json

import pytest

from validators.multi_province.k1_k_unit_normalization_asset_domain_design import build


def test_macro_rebase_preserves_per_capita_and_firm_wage_scale() -> None:
    receipt = build.rebase_identity(22716500.0, 393100.0, 67306708.83876626, alpha=build.ALPHA)
    assert receipt["money_factor"] == 100.0
    assert receipt["person_factor"] == 100.0
    assert receipt["old_y_over_n"] == pytest.approx(receipt["new_y_over_n"])
    assert receipt["old_k_over_n"] == pytest.approx(receipt["new_k_over_n"])
    assert receipt["productivity_factor"] == pytest.approx(1.0)
    assert receipt["firm_wage_factor"] == pytest.approx(1.0)


def test_asset_domain_spacing_is_exact() -> None:
    design = build.asset_domain_design()
    assert design["current"]["da"] == pytest.approx(10.0 / 19.0)
    assert design["current"]["db"] == pytest.approx(7.0 / 19.0)
    assert design["proposed_a"]["amax"] == 100.0
    assert design["proposed_a"]["da"] == pytest.approx(100.0 / 19.0)
    assert [item["bmax"] for item in design["b_candidates"]] == [20.0, 50.0]
    assert [item["db"] for item in design["b_candidates"]] == pytest.approx([22.0 / 19.0, 52.0 / 19.0])
    assert design["bmax_decision"] == "BMAX_OWNER_SELECTION_REQUIRED"


def test_household_generic_rescale_identifies_nonhomogeneous_transforms() -> None:
    transformed = build.household_rescale_transform(100.0, gamma=2.0)
    assert transformed["monetary_levels"] == 100.0
    assert transformed["consumption_utility_weight_alphac"] == 100.0
    assert transformed["labor_disutility_weight_alphal"] == 1.0
    assert transformed["value_function"] == 1.0
    assert transformed["a_bar"] == 100.0
    assert transformed["derivative_floor"] == pytest.approx(0.01)
    assert transformed["drift_tolerance"] == 100.0
    assert transformed["chi0"] == 1.0 and transformed["chi1"] == 1.0


def test_build_emits_required_zero_runtime_bundle(tmp_path) -> None:
    assert build.build(tmp_path) == 0
    required = {
        "original_matlab_scaling_trace.json", "dimension_classification.csv",
        "equation_scaling_transform.json", "parameter_transform_table.csv",
        "asset_domain_design.json", "grid_spacing_receipt.json",
        "macro_k_unit_mapping.csv", "implementation_proposal.json",
        "source_identity.json", "call_ledger.json", "sealed_manifest_sha256.json",
    }
    assert {path.name for path in tmp_path.iterdir()} == required
    ledger = json.loads((tmp_path / "call_ledger.json").read_text(encoding="utf-8"))
    for key in ("hjb", "kfe", "global_outer", "firm_runtime", "matlab_runtime", "k1b", "k2", "ge", "downstream", "shock", "irf", "results"):
        assert ledger[key] == 0
    with (tmp_path / "dimension_classification.csv").open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert {row["variable"] for row in rows} >= {"GDP/Y", "K", "I", "GovInv", "C", "Tt", "a", "b", "At", "Bt", "wjt", "household composite w", "population", "labor", "productivity", "ra", "rb", "chi0", "chi1", "value function"}
