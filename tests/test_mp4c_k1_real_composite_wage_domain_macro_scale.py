from __future__ import annotations

import numpy as np
import pytest

from validators.multi_province.k1_real_composite_wage_domain_macro_scale import finalize, run


def test_exact_real_wage_grid_and_frozen_fixture() -> None:
    assert run.POINTS == tuple((ra, wage) for ra in (0.06, 0.0675, 0.07) for wage in (13.0, 15.5, 18.0))
    fixture = run.build_fixture(0.0675, 15.5)
    assert fixture.inputs.r_b == 0.02 and fixture.inputs.r_a == 0.0675
    assert fixture.inputs.wages[0] == 15.5 and fixture.inputs.tau == 0.05
    assert fixture.transfer_income == 0.1 and fixture.borrowing_rate_gap == 0.07
    assert np.array_equal(fixture.grid.b, np.linspace(-2, 5, 20))
    assert np.array_equal(fixture.grid.a, np.linspace(0, 10, 20))
    assert fixture.numerics.delta == 1000 and fixture.numerics.convergence_tolerance == 1e-7
    assert fixture.numerics.max_iterations == 100 and fixture.numerics.drift_tolerance == 1e-12


def test_outside_grid_rejected_and_initialization_is_fresh() -> None:
    with pytest.raises(ValueError, match="outside"):
        run.build_fixture(0.0675, 1.3)
    one = run.build_fixture(0.06, 13.0); two = run.build_fixture(0.06, 13.0)
    assert one.initial_value is not two.initial_value and one.baseline_labor is not two.baseline_labor
    assert np.array_equal(one.initial_value, two.initial_value)


def test_pathology_rule_precedes_order_labels() -> None:
    mass = np.zeros(20); mass[9] = 0.7; mass[10] = 0.3
    healthy = {"distribution": {"density_finite": True, "density_min": -1e-16, "density_negative_count": 1, "total_mass": 1.0}}
    signed = {"distribution": {"density_finite": True, "density_min": -1e-6, "density_negative_count": 1, "total_mass": 1.0}}
    assert finalize.descriptive_distribution_label(mass, healthy) == "INTERIOR_A_DISTRIBUTION_CANDIDATE"
    assert finalize.descriptive_distribution_label(mass, signed) == "KFE_NUMERICALLY_PATHOLOGICAL"


def test_macro_audit_uses_accepted_31province_receipt(tmp_path) -> None:
    trace = finalize.build_macro_artifacts(tmp_path)
    assert trace["province_count"] == 31
    assert trace["dimensional_conclusion"] == "DIMENSIONAL_RELATION_UNRESOLVED"
    assert trace["statistics"]["household_composite_wage_w0"]["min"] > 12
    assert (tmp_path / "macro_scale_trace.json").is_file()
    assert (tmp_path / "macro_scale_summary.csv").is_file()


def test_runner_excludes_forbidden_runtime_routes() -> None:
    text = run.Path(run.__file__).read_text(encoding="utf-8")
    for forbidden in ("evaluate_firm(", "solve_multi_province", "solve_steady_state(", "matlab.engine", "subprocess", "os.system", "warm_start"):
        assert forbidden not in text
