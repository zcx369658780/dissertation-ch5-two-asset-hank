from __future__ import annotations

from types import SimpleNamespace

import numpy as np
import pytest

from validators.multi_province.k1_household_asset_grid_precision_sensitivity import (
    finalize,
    run,
)


def test_exact_precision_ladders_and_frozen_state() -> None:
    assert run.PHASE_POINTS == {
        "P1": ((20, 40), (20, 80), (20, 160)),
        "P2": ((40, 160), (80, 160)),
    }
    p1 = [run.precision_spec("P1", index) for index in range(3)]
    assert [item["da"] for item in p1] == pytest.approx(
        [100.0 / 39.0, 100.0 / 79.0, 100.0 / 159.0]
    )
    assert all(item["I"] == 20 and item["db"] == pytest.approx(22.0 / 19.0) for item in p1)
    p2 = [run.precision_spec("P2", index) for index in range(2)]
    assert [(item["I"], item["J"]) for item in p2] == [(40, 160), (80, 160)]
    assert [item["db"] for item in p2] == pytest.approx([22.0 / 39.0, 22.0 / 79.0])
    for item in p1 + p2:
        assert (item["rb"], item["ra"], item["wage"], item["h"]) == (0.02, 0.0675, 15.5, 1.0)
        assert (item["amin"], item["amax"], item["bmin"], item["bmax"]) == (0.0, 100.0, -2.0, 20.0)


def test_outside_precision_ladder_is_rejected_without_initialization() -> None:
    with pytest.raises(ValueError, match="outside"):
        run.precision_spec("P1", 3)
    with pytest.raises(ValueError, match="phase"):
        run.precision_spec("P3", 0)


def test_signed_cdf_distance_is_deterministic_and_zero_for_identity() -> None:
    grid = np.array([0.0, 1.0, 2.0])
    mass = np.array([0.2, 0.5, 0.3])
    assert finalize.signed_cdf_l1_distance(grid, mass, grid, mass) == pytest.approx(0.0)
    coarse_grid = np.array([0.0, 2.0])
    coarse_mass = np.array([0.2, 0.8])
    first = finalize.signed_cdf_l1_distance(grid, mass, coarse_grid, coarse_mass)
    second = finalize.signed_cdf_l1_distance(coarse_grid, coarse_mass, grid, mass)
    assert first == pytest.approx(second)
    assert first > 0.0


def test_runner_contains_no_forbidden_routes_or_warm_start_parameter() -> None:
    text = run.Path(run.__file__).read_text(encoding="utf-8")
    for forbidden in (
        "evaluate_firm(", "solve_multi_province", "solve_steady_state(",
        "matlab.engine", "subprocess", "os.system", "warm_start=",
    ):
        assert forbidden not in text


@pytest.mark.parametrize(
    ("i_size", "j_size"),
    ((20, 20), (20, 40), (20, 80), (20, 160), (40, 160), (80, 160)),
)
def test_grid_generic_distribution_receipt_uses_actual_support(
    i_size: int, j_size: int
) -> None:
    grid = run.oracle.MatlabFaithfulHJBGrid(
        np.linspace(-2.0, 20.0, i_size),
        np.linspace(0.0, 100.0, j_size),
        np.array([0.8, 1.3]),
        np.array([[-1.0 / 3.0, 1.0 / 3.0], [1.0 / 3.0, -1.0 / 3.0]]),
    )
    density = np.arange(1, i_size * j_size * 2 + 1, dtype=float).reshape(
        i_size, j_size, 2
    )
    receipt = run.grid_generic_distribution_receipt(grid, density)

    assert receipt["density_shape"] == [i_size, j_size, 2]
    assert receipt["grid_support"]["b"] == pytest.approx(grid.b)
    assert receipt["grid_support"]["a"] == pytest.approx(grid.a)
    assert len(receipt["b_marginal_mass"]) == i_size
    assert len(receipt["a_marginal_mass"]) == j_size
    assert receipt["b_marginal_shape"] == [i_size]
    assert receipt["a_marginal_shape"] == [j_size]
    assert sum(receipt["b_marginal_mass"]) == pytest.approx(receipt["total_mass"])
    assert sum(receipt["a_marginal_mass"]) == pytest.approx(receipt["total_mass"])
    assert len(receipt["top_3_b_bins"]) == 3
    assert len(receipt["top_3_a_bins"]) == 3
    assert receipt["modal_b"] == [float(grid.b[-1])]
    assert receipt["modal_a"] == [float(grid.a[-1])]
    assert receipt["boundary_mass_shares"]["bmin"] == pytest.approx(
        receipt["b_marginal_mass"][0]
    )
    assert receipt["boundary_mass_shares"]["amax"] == pytest.approx(
        receipt["a_marginal_mass"][-1]
    )


def test_grid_generic_j20_receipt_preserves_accepted_semantics() -> None:
    fixture = run.build_fixture(run.precision_spec("P1", 0))
    grid = run.oracle.MatlabFaithfulHJBGrid(
        fixture.grid.b,
        np.linspace(0.0, 100.0, 20),
        fixture.grid.z,
        fixture.grid.switch_matrix,
    )
    density = np.arange(1, 20 * 20 * 2 + 1, dtype=float).reshape(20, 20, 2)
    accepted = run.coarse.distribution_receipt(grid, density)
    fixed_j20 = run.stagewise.accepted.illiquid_transition_receipt(
        grid.a, accepted["a_marginal_mass"]
    )
    generic = run.grid_generic_distribution_receipt(grid, density)

    for key, value in accepted.items():
        assert generic[key] == value
    for key, value in fixed_j20.items():
        assert generic[key] == value


def test_scientific_arrays_are_persisted_before_receipt_validation(
    tmp_path: run.Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fixture = run.build_fixture(run.precision_spec("P1", 0))
    shape = (fixture.grid.b.size, fixture.grid.a.size, fixture.grid.z.size)
    density = np.arange(1, np.prod(shape) + 1, dtype=float).reshape(shape)
    fake_kfe = SimpleNamespace(
        density=density,
        density_vector=density.reshape(-1, order="F"),
        contaminated_row_index=0,
        normalization_factor=1.0,
        raw_residual_inf=0.0,
    )
    hjb = SimpleNamespace(
        post_convergence_operator=SimpleNamespace(full=np.zeros((1, 1))),
        value=np.ones(shape),
        consumption=np.ones(shape),
        labor=np.ones(shape),
        transfer=np.ones(shape),
        mu_a=np.ones(shape),
        mu_b=np.ones(shape),
    )
    monkeypatch.setattr(
        run.oracle, "solve_matlab_faithful_stationary_kfe", lambda *args, **kwargs: fake_kfe
    )
    monkeypatch.setattr(
        run,
        "grid_generic_distribution_receipt",
        lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("after-persist")),
    )
    output = tmp_path / "scientific_arrays.npz"

    with pytest.raises(RuntimeError, match="after-persist"):
        run.run_kfe_persist_first(fixture, hjb, output)

    with np.load(output) as saved:
        assert set(saved.files) == {
            "value", "consumption", "labor", "transfer", "mu_a", "mu_b",
            "density", "grid_a", "grid_b", "density_shape",
        }
        assert saved["density"] == pytest.approx(density)
        assert saved["grid_a"] == pytest.approx(fixture.grid.a)
        assert saved["grid_b"] == pytest.approx(fixture.grid.b)
        assert saved["density_shape"].tolist() == list(shape)


def test_j20_full_kfe_receipt_matches_accepted_route(
    tmp_path: run.Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fixture = run.stagewise.build_fixture("A", 0.0675, 15.5)
    shape = (fixture.grid.b.size, fixture.grid.a.size, fixture.grid.z.size)
    density = np.arange(1, np.prod(shape) + 1, dtype=float).reshape(shape)
    density[0, 0, 0] = -np.finfo(float).eps
    fake_kfe = SimpleNamespace(
        density=density,
        density_vector=density.reshape(-1, order="F"),
        contaminated_row_index=0,
        normalization_factor=1.0,
        raw_residual_inf=1e-16,
    )
    hjb = SimpleNamespace(
        post_convergence_operator=SimpleNamespace(full=np.zeros((1, 1))),
        value=np.ones(shape),
        consumption=np.ones(shape),
        labor=np.ones(shape),
        transfer=np.ones(shape),
        mu_a=np.ones(shape),
        mu_b=np.ones(shape),
    )
    monkeypatch.setattr(
        run.oracle, "solve_matlab_faithful_stationary_kfe", lambda *args, **kwargs: fake_kfe
    )

    _, accepted_aggregates, accepted_receipt = run.coarse.run_kfe(fixture, hjb)
    _, repaired_aggregates, repaired_receipt = run.run_kfe_persist_first(
        fixture, hjb, tmp_path / "j20_scientific_arrays.npz"
    )

    assert repaired_aggregates == accepted_aggregates
    for key in ("aggregates", "kfe", "preliminary_quality_label"):
        assert repaired_receipt[key] == accepted_receipt[key]
    for key, value in accepted_receipt["distribution"].items():
        assert repaired_receipt["distribution"][key] == value
    assert repaired_receipt["distribution"]["density_min"] == -np.finfo(float).eps
    assert repaired_receipt["distribution"]["density_negative_count"] == 1
