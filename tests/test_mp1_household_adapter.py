from __future__ import annotations

import numpy as np
import pytest
from types import SimpleNamespace

from ch5_two_asset_hank.multi_province.household_adapter import (
    ACCEPTED_HA_PUBLIC_API,
    MATLAB_TO_ACCEPTED_HA_FIELD_MAP,
    MATLAB_TO_ACCEPTED_HA_OUTPUT_MAP,
    NO_LEGACY_R5_RUNTIME_DEPENDENCY,
    FrozenHouseholdOutputs,
    MultiProvinceHouseholdInputs,
    build_static_household_call,
    reject_legacy_runtime_references,
)


def _outer_inputs(**changes: object) -> MultiProvinceHouseholdInputs:
    values: dict[str, object] = {
        "rah": 0.041,
        "rb": 0.018,
        "tau": 0.13,
        "composite_wage": 1.27,
        "composite_migration_cost": 0.0,
        "composite_labor_weight": 1.6,
        "transfer_income": 0.09,
        "borrowing_rate_gap": 0.025,
        "grid": SimpleNamespace(
            b=np.array([-1.0, 1.0]),
            a=np.array([0.0, 1.0, 2.0]),
            z=np.array([0.8, 1.2]),
            switch_matrix=np.array([[-0.1, 0.1], [0.1, -0.1]]),
        ),
        "economic_params": SimpleNamespace(
            rho=0.05,
            gamma_c=2.0,
            phi=5.0,
            chi_0=0.1,
            chi_1=2.0,
            a_bar=1e-6,
            mu_z=0.0,
            sigma_z=0.0,
        ),
        "initial_value": np.ones((2, 3, 2)),
        "baseline_labor": np.full((2, 3, 2), 0.4),
        "numerics": SimpleNamespace(
            delta=1000.0,
            convergence_tolerance=1e-7,
            max_iterations=100,
            drift_tolerance=1e-12,
        ),
    }
    values.update(changes)
    return MultiProvinceHouseholdInputs(**values)


def test_static_call_maps_outer_roles_to_the_accepted_api_without_solving() -> None:
    call = build_static_household_call(_outer_inputs())

    assert ACCEPTED_HA_PUBLIC_API.solver_symbol == (
        "exports.matlab_faithful_two_asset_ha.solve_household_steady_state"
    )
    assert call.household_input_kwargs == {
        "r_a": 0.041,
        "r_b": 0.018,
        "tau": 0.13,
        "wages": (1.27,),
        "migration_costs": (0.0,),
        "labor_weights": (1.6,),
    }
    assert call.transfer_income == 0.09
    assert call.borrowing_rate_gap == 0.025
    assert call.scientific_solver_called is False


def test_immutable_source_to_accepted_api_crosswalk_is_exact() -> None:
    assert dict(MATLAB_TO_ACCEPTED_HA_FIELD_MAP) == {
        "results.rah": "HouseholdInputs.r_a",
        "results.rb": "HouseholdInputs.r_b",
        "results.tau": "HouseholdInputs.tau",
        "results.w": "HouseholdInputs.wages[0]",
        "composite_zero_migration_wedge": "HouseholdInputs.migration_costs[0]",
        "param.alphal": "HouseholdInputs.labor_weights[0]",
        "results.Tt": "solve_household_steady_state.transfer_income",
        "results.rb_gap": "solve_household_steady_state.borrowing_rate_gap",
        "param.rho": "EconomicParams.rho",
        "param.ga": "EconomicParams.gamma_c",
        "1 / param.frisch_l": "EconomicParams.phi",
        "CHIh.chi0": "EconomicParams.chi_0",
        "CHIh.chi1": "EconomicParams.chi_1",
        "CHIh.a_bar": "EconomicParams.a_bar",
        "grid.la_mat": "MatlabFaithfulHJBGrid.switch_matrix",
        "linspace(grid.amin, grid.amax, grid.J)": "MatlabFaithfulHJBGrid.a",
        "linspace(grid.bmin, grid.bmax, grid.I)": "MatlabFaithfulHJBGrid.b",
        "grid.z": "MatlabFaithfulHJBGrid.z",
        "results.V": "solve_household_steady_state.initial_value",
        "results.l": "solve_household_steady_state.baseline_labor",
        "num": "solve_household_steady_state.numerics",
    }
    assert dict(MATLAB_TO_ACCEPTED_HA_OUTPUT_MAP) == {
        "results.Ct": "HouseholdSteadyStateResult.aggregates.c_ss",
        "results.Lt": "HouseholdSteadyStateResult.aggregates.l_ss",
        "results.At": "HouseholdSteadyStateResult.aggregates.a_ss",
        "results.Bt": "HouseholdSteadyStateResult.aggregates.b_ss",
        "results.AtTax": "post_solve_reconstruction.AtTax_from_density_and_tapered_illiquid_return",
        "results.convergent": "HouseholdSteadyStateResult.hjb.converged",
        "HJB convergence statistic": "HouseholdSteadyStateResult.hjb.convergence_statistic",
    }
    with pytest.raises(TypeError):
        MATLAB_TO_ACCEPTED_HA_FIELD_MAP["results.rb"] = "wrong"  # type: ignore[index]


def test_composite_household_labor_and_post_solve_reconstruction_are_separate() -> None:
    call = build_static_household_call(_outer_inputs())

    assert call.pre_solve_composite_fields == (
        "w",
        "rah",
        "rb",
        "tau",
        "Tt",
        "rb_gap",
    )
    assert "Lt_mat" not in call.household_input_kwargs
    assert call.post_solve_reconstruction == (
        "AtTax_from_density_and_tapered_illiquid_return",
        "Lt_mat_from_Ct_and_destination_firm_wages",
        "Lt_supply_as_destination_row_sum",
    )


def test_static_call_cannot_mutate_the_frozen_outer_state() -> None:
    call = build_static_household_call(_outer_inputs())

    with pytest.raises(TypeError):
        call.household_input_kwargs["r_a"] = 99.0  # type: ignore[index]
    with pytest.raises(ValueError):
        call.initial_value[0, 0, 0] = 99.0


def test_outer_outputs_keep_household_labor_distinct_from_firm_labor() -> None:
    output = FrozenHouseholdOutputs(
        Ct=1.1,
        Lt=0.7,
        At=0.8,
        Bt=-0.2,
        AtTax=0.01,
        converged=True,
        convergence_statistic=1.0e-9,
    )

    assert output.Lt == 0.7
    assert not hasattr(output, "Lt_supply")


@pytest.mark.parametrize(
    "changes",
    [
        {"composite_wage": float("nan")},
        {"grid": None},
        {"initial_value": None},
        {"baseline_labor": None},
        {"numerics": None},
    ],
)
def test_adapter_has_no_hidden_economic_or_numerical_defaults(changes: dict[str, object]) -> None:
    with pytest.raises(ValueError):
        _outer_inputs(**changes)


def test_adapter_rejects_non_api_objects_and_grid_shape_mismatch() -> None:
    with pytest.raises(ValueError, match="missing accepted public fields"):
        _outer_inputs(grid=object())
    with pytest.raises(ValueError, match=r"grid shape \(b,a,z\)"):
        _outer_inputs(initial_value=np.ones((3, 2, 2)))
    repeated = _outer_inputs().grid
    repeated.b = np.array([-1.0, -1.0])
    with pytest.raises(ValueError, match="strictly increasing"):
        _outer_inputs(grid=repeated)


def test_legacy_r5_runtime_dependency_fails_closed() -> None:
    assert NO_LEGACY_R5_RUNTIME_DEPENDENCY
    reject_legacy_runtime_references(("numpy", "ch5_two_asset_hank.contracts"))
    with pytest.raises(ValueError, match="legacy R5"):
        reject_legacy_runtime_references(("chapter5_model.households",))
    with pytest.raises(ValueError, match="legacy R5"):
        reject_legacy_runtime_references(("D:/ResearchCode/dissertation-ch5-r5-python-model",))
