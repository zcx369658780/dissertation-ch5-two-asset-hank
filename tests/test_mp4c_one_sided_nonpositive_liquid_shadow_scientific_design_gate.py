from pathlib import Path

from validators.multi_province.one_sided_nonpositive_liquid_shadow_scientific_design_gate import run


REPO = Path(__file__).resolve().parents[1]


def test_complete_map_inventory_proves_raw_values_were_compacted_away():
    t1 = run.map_inventory(REPO, run.TURN1)
    t2 = run.map_inventory(REPO, run.TURN2)
    assert t1["complete_policy_maps"] == 408
    assert t2["complete_policy_maps"] == 101
    assert not t1["raw_derivative_numeric_values_persisted_in_complete_maps"]
    assert not t2["raw_derivative_numeric_values_persisted_in_complete_maps"]


def test_failed_prefix_has_two_opposite_mixed_sign_interior_cells():
    census, mixed = run.partial_census(REPO)
    assert census["persisted_cells"] == 64
    assert census["interior_liquid_counts"]["+,<=0"] == 1
    assert census["interior_liquid_counts"]["<=0,+"] == 1
    assert [x["flat"] for x in mixed] == [62, 63]


def test_f0063_has_no_root_in_positive_raw_hull_and_only_extrapolated_root():
    _, mixed = run.partial_census(REPO)
    row = next(x for x in run.panel(mixed) if x["flat"] == 63)
    assert row["positive_family_drift_at_sole_positive_endpoint"] < 0
    ext = row["positive_family_extrapolated_root"]
    assert ext is not None
    assert ext["q_b"] > row["positive_hull_intersection"][1]
    assert abs(ext["g_b"]) < 1e-14
    assert abs(ext["q_b"] - 0.01801822665826406) < 1e-15


def test_validator_has_no_production_imports():
    source = (REPO / "validators/multi_province/one_sided_nonpositive_liquid_shadow_scientific_design_gate/run.py").read_text(encoding="utf-8")
    assert "from ch5_two_asset_hank" not in source
    assert "import ch5_two_asset_hank" not in source
