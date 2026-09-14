from __future__ import annotations

import numpy as np
import pytest

from validators.multi_province.k1_household_k_unit_asset_domain_stagewise import finalize, run


def _point(modal_b: float, *, valid: bool = True) -> dict:
    density_min = -1e-16 if valid else -1e-4
    return {
        "point_id": "synthetic",
        "hjb": {"classification": "HJB_CONVERGED"},
        "kfe": {
            "ran": True,
            "distribution": {
                "density_finite": True,
                "density_min": density_min,
                "total_mass": 1.0,
                "modal_b": [modal_b],
            },
            "kfe": {"raw_residual_inf": 1e-14},
        },
    }


def test_exact_registered_grid_and_stage_domains() -> None:
    assert run.POINTS == tuple(
        (ra, wage)
        for ra in (0.06, 0.0675, 0.07)
        for wage in (13.0, 15.5, 18.0)
    )
    stage_a = run.stage_spec("A")
    stage_b = run.stage_spec("B")
    assert stage_a == {
        "stage": "A", "amin": 0.0, "amax": 100.0,
        "bmin": -2.0, "bmax": 20.0, "I": 20, "J": 20, "Nz": 2,
        "da": pytest.approx(100.0 / 19.0),
        "db": pytest.approx(22.0 / 19.0),
    }
    assert stage_b["bmax"] == 50.0
    assert stage_b["db"] == pytest.approx(52.0 / 19.0)
    assert {key: stage_b[key] for key in ("amin", "amax", "bmin", "I", "J", "Nz")} == {
        key: stage_a[key] for key in ("amin", "amax", "bmin", "I", "J", "Nz")
    }


def test_stage_b_trigger_uses_only_valid_exact_endpoint_modes() -> None:
    assert run.stage_b_trigger([_point(20.0)], bmax=20.0)["trigger"] is True
    assert run.stage_b_trigger([_point(18.0)], bmax=20.0)["trigger"] is False
    assert run.stage_b_trigger([_point(20.0, valid=False)], bmax=20.0)["trigger"] is False
    tied = _point(18.0)
    tied["kfe"]["distribution"]["modal_b"] = [18.0, 20.0]
    assert run.stage_b_trigger([tied], bmax=20.0)["trigger"] is True


def test_asset_labels_are_endpoint_exact_and_pathology_first() -> None:
    interior = np.zeros(20); interior[9] = 0.6; interior[10] = 0.4
    lower = np.zeros(20); lower[0] = 1.0
    upper = np.zeros(20); upper[-1] = 1.0
    healthy = {"density_finite": True, "density_min": -1e-16, "total_mass": 1.0}
    pathological = {"density_finite": True, "density_min": -1e-4, "total_mass": 1.0}
    assert finalize.classify_b(interior, healthy) == "B_INTERIOR_DISTRIBUTION_CANDIDATE"
    assert finalize.classify_b(lower, healthy) == "B_LOWER_BOUNDARY_DOMINATED"
    assert finalize.classify_b(upper, healthy) == "B_UPPER_BOUNDARY_PILEUP"
    assert finalize.classify_b(upper, pathological) == "KFE_NUMERICALLY_PATHOLOGICAL"
    assert finalize.classify_a(interior, healthy) == "INTERIOR_A_DISTRIBUTION_CANDIDATE"


def test_runner_contains_no_forbidden_runtime_routes() -> None:
    text = run.Path(run.__file__).read_text(encoding="utf-8")
    for forbidden in (
        "evaluate_firm(", "solve_multi_province", "solve_steady_state(",
        "matlab.engine", "subprocess", "os.system", "warm_start=",
    ):
        assert forbidden not in text
