"""Synthetic/static checks; no scientific solver or private workbook is used."""
from __future__ import annotations

from pathlib import Path

import pytest

from validators.multi_province.corrected_2018_two_turn import finalize, run


def _state(name: str, ratio: float, ra: float, rah: float = 0.0):
    return {"name": name, "inter_prv_ratio": ratio, "ra": ra, "rah": rah}


def test_turn2_rah_uses_prior_entering_ra_composite() -> None:
    prior = tuple(_state(str(i), ratio, ra) for i, (ratio, ra) in enumerate(((0.1, .09), (0.2, .09), (0.3, .09))))
    weighted = sum(state["inter_prv_ratio"] * state["ra"] for state in prior)
    ratio = prior[1]["inter_prv_ratio"]
    expected = (1-ratio)*.09 + ratio*(weighted-ratio*.09)/2
    states = tuple({**state, "rah": expected if i == 1 else 0.0} for i, state in enumerate(prior))
    result = run.rah_provenance(2, 1, states, prior)
    assert result["value"] == expected
    assert result["source_old_ra_turn"] == 1
    assert result["manual_override"] is False


def test_turn2_rah_fails_closed_on_manual_substitution() -> None:
    prior = tuple(_state(str(i), .1, .09) for i in range(3))
    states = tuple({**state, "rah": .02} for state in prior)
    with pytest.raises(ValueError, match="lag formula"):
        run.rah_provenance(2, 0, states, prior)


def test_national_summary_regions_and_iterations() -> None:
    rows = [
        {"province": "A", "firm_ra0": .01, "firm_wage_raw": .7, "ramin": .02, "ramax": .09,
         "wjtmin": .8, "wjtmax": 1.3, "nk_gap": 2.0, "yt_gap": .2, "hjb_iterations": 10,
         "hjb_converged": True, "kfe_returned": True},
        {"province": "B", "firm_ra0": .05, "firm_wage_raw": 1.0, "ramin": .02, "ramax": .09,
         "wjtmin": .8, "wjtmax": 1.3, "nk_gap": 1.0, "yt_gap": .1, "hjb_iterations": 11,
         "hjb_converged": True, "kfe_returned": True},
        {"province": "C", "firm_ra0": .10, "firm_wage_raw": 1.4, "ramin": .02, "ramax": .09,
         "wjtmin": .8, "wjtmax": 1.3, "nk_gap": 3.0, "yt_gap": .3, "hjb_iterations": 10,
         "hjb_converged": False, "kfe_returned": True},
    ]
    controller = {"adaptation_allowed": False, "actions": [
        {"zt_adjusted": False, "govinv_action": "NONE"} for _ in rows]}
    result = run.national_summary(1, rows, controller)
    assert result["firm_rate_regions"] == {"lower": 1, "interior": 1, "upper": 1}
    assert result["wage_regions"] == {"lower": 1, "interior": 1, "upper": 1}
    assert result["hjb_iteration_distribution"] == {"10": 2, "11": 1}
    assert result["hjb_failures"] == 1


def test_science_guard_has_exactly_two_turns_and_no_stationary_loop() -> None:
    source = Path(run.__file__).read_text(encoding="utf-8")
    assert "for turn_index in (1, 2):" in source
    assert "run_online_stationary" not in source
    assert "scientific trajectory already started; retry prohibited" in source
    assert '"third_turns": 0' in source


def test_anhui_forensic_answers_are_derived_from_saved_fields() -> None:
    turn1 = {"household_rah": .09, "firm_ra_used": .02, "firm_wage_raw": 2.5,
             "firm_wage_used": 1.3, "hjb_converged": True, "kfe_returned": True}
    turn2 = {"household_rah": .083, "firm_ra0": -.025, "firm_ra_used": .02,
             "firm_wage_raw": 2.1, "firm_wage_used": 1.3,
             "hjb_converged": True, "kfe_returned": True}
    provenance = {"formula": "native_formula", "value": .083}
    result = finalize.build_anhui(turn1, turn2, provenance)
    assert result["answers"]["turn1_ra_0p02_directly_became_turn2_rah"] is False
    assert result["answers"]["turn2_firm_raw_return_region"] == "LOWER"
    assert result["answers"]["hjb_kfe_executable_after_propagation"] is True
