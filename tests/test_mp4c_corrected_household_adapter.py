from __future__ import annotations

import inspect
import hashlib
import json
from pathlib import Path

import numpy as np
import pytest

from ch5_two_asset_hank.multi_province import corrected_household_adapter as adapter


def _inputs(**changes: object) -> adapter.CorrectedHouseholdAggregateInputs:
    shape = (2, 2, 2)
    p = np.arange(1.0, 9.0).reshape(shape, order="F")
    p /= p.sum()
    values: dict[str, object] = {
        "consumption": np.arange(1.0, 9.0).reshape(shape, order="F"),
        "labor": np.full(shape, 0.5),
        "b_grid": np.array([-1.0, 2.0]),
        "a_grid": np.array([0.0, 4.0]),
        "z_grid": np.array([0.8, 1.2]),
        "effective_r_a": np.broadcast_to(
            np.array([0.09, 0.081])[None, :, None], shape
        ),
        "probability_mass": p,
        "density": p / 0.25,
        "omega": 0.25,
        "source_r_a": 0.09,
    }
    values.update(changes)
    return adapter.CorrectedHouseholdAggregateInputs(**values)


def test_f_order_mass_and_density_aggregates_are_equivalent() -> None:
    inputs = _inputs()
    result = adapter.evaluate_corrected_household_aggregates(inputs)
    p = inputs.probability_mass.ravel(order="F")
    c = inputs.consumption.ravel(order="F")

    assert result.axis_order == ("b", "a", "z")
    assert result.flatten_order == "F"
    assert result.Ct.mass_form == pytest.approx(float(np.dot(c, p)))
    for name in ("Ct", "Lt", "At", "Bt", "total_assets", "AtTax"):
        comparison = getattr(result, name)
        assert comparison.equivalent
        assert comparison.absolute_difference <= comparison.prospective_bound


def test_attax_uses_source_return_minus_tapered_return_flow() -> None:
    inputs = _inputs()
    result = adapter.evaluate_corrected_household_aggregates(inputs)
    shape = inputs.consumption.shape
    a = np.broadcast_to(inputs.a_grid[None, :, None], shape).ravel(order="F")
    effective = inputs.effective_r_a.ravel(order="F")
    p = inputs.probability_mass.ravel(order="F")
    expected = result.At.mass_form * inputs.source_r_a - float(np.dot(a * effective, p))

    assert result.AtTax.mass_form == pytest.approx(expected)
    frozen = result.frozen_output(converged=True, convergence_statistic=1e-9)
    assert frozen.AtTax == result.AtTax.mass_form


def test_adapter_fails_closed_on_shape_or_mass_density_mismatch() -> None:
    with pytest.raises(ValueError, match="shape"):
        _inputs(consumption=np.ones((2, 2, 1)))
    bad_density = _inputs().density.copy()
    bad_density[0, 0, 0] += 1.0
    with pytest.raises(ValueError, match="inconsistent"):
        _inputs(density=bad_density)


def test_opt_in_adapter_has_no_solver_or_hidden_default_route() -> None:
    source = inspect.getsource(adapter)
    assert "solve_household_steady_state" not in source
    assert "spsolve" not in source
    assert "scipy" not in source
    signature = inspect.signature(adapter.CorrectedHouseholdAggregateInputs)
    assert all(parameter.default is inspect.Parameter.empty for parameter in signature.parameters.values())


def test_exact_accepted_checkpoint11_and_mass_artifacts_are_bound() -> None:
    repository = Path(__file__).resolve().parents[1]
    policy_root = repository / (
        "reports/ch5_mp4c_2018_kfe_d123_checkpoint10_to_checkpoint12_"
        "bounded_nonlinear_continuation_20260920_run001"
    )
    mass_root = repository / (
        "reports/ch5_mp4c_2018_kfe_d123_checkpoint11_terminal_"
        "source_free_kfe_validation_20260920_run001"
    )

    def digest(path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest().upper()

    assert digest(policy_root / "sealed_manifest.json") == (
        "5E67E595B32024213EC5E6517389A7DCA6462A24FB735B06EB2F85D6E1621E41"
    )
    assert digest(mass_root / "sealed_manifest.json") == (
        "B7C06E3C369B6A5400DE76252DD70A539EFF1F2E4072C04639A1E93E512F5C1D"
    )
    checkpoint = policy_root / "checkpoint_011"
    manifest = json.loads((checkpoint / "checkpoint_manifest.json").read_text("utf-8"))
    assert manifest["value_sha256"] == (
        "A097A3DDA767B979224638A51CEDC53EA635687CCDEFBE190FED0B899606921F"
    )
    assert manifest["policy_identity_sha256"] == (
        "89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3"
    )
    assert manifest["utility_sha256"] == (
        "2E9A077FFA809F2DECEE385FD9E7F50C03E16750C2A074F990C0F3CBCC212648"
    )
    assert digest(checkpoint / "q_generator.npz") == (
        "33367258F3EADB1482D4A5CB30A64A8574830C993B0E5280C451499CBD6913AD"
    )
    assert digest(mass_root / "stationary_mass_arrays.npz") == (
        "1DD70201EAC5EED0AE768362D99A76736276BFB4D5E6AF0D8DBDB4E9D6FE7D16"
    )
