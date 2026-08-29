"""Implicit pseudo-time HJB driver for the bounded first slice."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as sparse_linalg

from .contracts import EconomicParams, GridSpec, HJBResult, HouseholdInputs
from .derivatives import compute_derivatives
from .diagnostics import hjb_residual, validate_operator
from .generator import build_operator
from .indexing import flatten, unflatten
from .policies import select_policy


@dataclass(frozen=True)
class HJBNumerics:
    pseudo_time_step: float = 100.0
    change_tolerance: float = 1e-8
    residual_tolerance: float = 1e-7
    generator_tolerance: float = 1e-11
    drift_tolerance: float = 1e-12
    kkt_tolerance: float = 1e-7
    max_iterations: int = 500

    def __post_init__(self) -> None:
        if self.pseudo_time_step <= 0 or self.max_iterations <= 0:
            raise ValueError("pseudo-time step and max iterations must be positive")
        if min(self.change_tolerance, self.residual_tolerance, self.generator_tolerance,
               self.drift_tolerance, self.kkt_tolerance) <= 0:
            raise ValueError("all tolerances must be positive")


class HJBConvergenceError(RuntimeError):
    def __init__(self, message: str, result: HJBResult):
        super().__init__(message)
        self.result = result


def solve_hjb(
    grid: GridSpec,
    params: EconomicParams,
    inputs: HouseholdInputs,
    initial_value: np.ndarray,
    numerics: HJBNumerics | None = None,
) -> HJBResult:
    settings = numerics or HJBNumerics()
    value = np.array(initial_value, dtype=float, copy=True)
    if value.shape != grid.shape or not np.all(np.isfinite(value)):
        raise ValueError("initial value must be finite with canonical logical shape")
    identity = sparse.eye(grid.size, format="csr")
    change = np.inf
    policy = None
    operator = None
    for iteration in range(1, settings.max_iterations + 1):
        derivatives = compute_derivatives(value, grid)
        policy = select_policy(derivatives, grid, params, inputs, settings.drift_tolerance)
        operator = build_operator(grid, params, policy, settings.drift_tolerance)
        validate_operator(operator, settings.generator_tolerance)
        matrix = (params.rho + 1.0 / settings.pseudo_time_step) * identity - operator.g
        rhs = flatten(policy.utility, grid.shape) + flatten(value, grid.shape) / settings.pseudo_time_step
        updated_vector = sparse_linalg.spsolve(matrix, rhs)
        if not np.all(np.isfinite(updated_vector)):
            raise FloatingPointError("implicit HJB update produced non-finite values")
        updated = unflatten(updated_vector, grid.shape)
        change = float(np.max(np.abs(updated - value)))
        value = updated
        if change <= settings.change_tolerance:
            break

    derivatives = compute_derivatives(value, grid)
    policy = select_policy(derivatives, grid, params, inputs, settings.drift_tolerance)
    operator = build_operator(grid, params, policy, settings.drift_tolerance)
    validate_operator(operator, settings.generator_tolerance)
    residual = hjb_residual(value, policy, operator, grid, params)
    residual_sup = float(np.max(np.abs(residual)))
    converged = (change <= settings.change_tolerance and residual_sup <= settings.residual_tolerance
                 and policy.kkt_residual <= settings.kkt_tolerance)
    result = HJBResult(value, policy, operator, iteration, converged, change, residual_sup)
    if not converged:
        raise HJBConvergenceError(
            f"HJB did not meet change/residual/KKT tolerances: change={change:.3e}, "
            f"residual={residual_sup:.3e}, KKT={policy.kkt_residual:.3e}",
            result,
        )
    return result
