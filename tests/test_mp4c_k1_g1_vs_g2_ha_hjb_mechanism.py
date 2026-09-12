from __future__ import annotations

import numpy as np
import pytest

from validators.multi_province.k1_g1_vs_g2_ha_hjb_mechanism.analyze import (
    association, boundary_faces, convergence_switch, finite_ratio, hit_state, return_regime,
)


@pytest.mark.parametrize("g1,g2,expected", [
    (True, True, "BOTH_CONVERGED"), (True, False, "G1_CONVERGED_G2_NONCONVERGED"),
    (False, True, "G1_NONCONVERGED_G2_CONVERGED"), (False, False, "BOTH_NONCONVERGED"),
])
def test_convergence_switch(g1: bool, g2: bool, expected: str) -> None:
    assert convergence_switch(g1, g2) == expected


def row(status: str) -> dict[str, bool]:
    return {"return_guard_lower_hit": status == "LOWER", "return_guard_upper_hit": status == "UPPER",
            "return_guard_unsaturated": status == "UNSATURATED"}


def test_return_regimes_and_hit_status() -> None:
    assert hit_state(row("UPPER"), "return_guard") == "UPPER"
    assert return_regime(row("UPPER"), row("UPPER")) == "A_STILL_UPPER_SATURATED"
    assert return_regime(row("UPPER"), row("UNSATURATED")) == "B_NEWLY_UNSATURATED"
    assert return_regime(row("UPPER"), row("LOWER")) == "C_LOWER_HIT"


def test_boundary_faces_are_explicit_and_corner_preserving() -> None:
    assert boundary_faces((1, 1, 0)) == ["interior"]
    assert boundary_faces((0, 0, 0)) == ["lower-a", "lower-b"]
    assert boundary_faces((19, 19, 1)) == ["upper-a", "upper-b"]


def test_ratio_and_association_fail_closed_without_variation() -> None:
    assert finite_ratio(2.0, 0.0) is None
    assert finite_ratio(2.0, 4.0) == 0.5
    result = association([1, 1, 1], [1, 2, 3])
    assert result["pearson"] is None and result["classification"] == "DESCRIPTIVE_ONLY_NOT_CAUSAL"
    varied = association([1, 2, 3], [2, 4, 6])
    assert varied["pearson"] == pytest.approx(1.0)


def test_hit_state_rejects_missing_status() -> None:
    with pytest.raises(ValueError):
        hit_state(row("NONE"), "return_guard")
    broken = row("UPPER")
    broken["return_guard_lower_hit"] = True
    with pytest.raises(ValueError, match="non-exclusive"):
        hit_state(broken, "return_guard")
