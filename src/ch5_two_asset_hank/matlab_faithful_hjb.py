"""Distinct HJB driver reproducing the designated MATLAB finite-difference source."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import sparse
from scipy.sparse import linalg

from .contracts import EconomicParams, HouseholdInputs
from .matlab_faithful_operator import MatlabFaithfulOperator, assemble_source_operator
from .matlab_faithful_policy import select_matlab_faithful_local_policy


@dataclass(frozen=True)
class MatlabFaithfulHJBGrid:
    b: np.ndarray
    a: np.ndarray
    z: np.ndarray
    switch_matrix: np.ndarray

    def __post_init__(self) -> None:
        for name in ("b", "a", "z"):
            value = np.asarray(getattr(self, name), dtype=float)
            if value.ndim != 1 or value.size < 2 or not np.isfinite(value).all() or not np.all(np.diff(value) > 0):
                raise ValueError(f"{name} must be finite and strictly increasing")
            object.__setattr__(self, name, value)
        switch = np.asarray(self.switch_matrix, dtype=float)
        if switch.shape != (self.z.size, self.z.size) or not np.isfinite(switch).all():
            raise ValueError("switch matrix shape is incompatible with z")
        object.__setattr__(self, "switch_matrix", switch)


@dataclass(frozen=True)
class MatlabFaithfulHJBNumerics:
    delta: float
    convergence_tolerance: float
    max_iterations: int
    drift_tolerance: float


@dataclass(frozen=True)
class MatlabFaithfulHJBResult:
    value: np.ndarray
    initial_value: np.ndarray
    consumption: np.ndarray
    labor: np.ndarray
    transfer: np.ndarray
    adjustment_cost: np.ndarray
    effective_illiquid_return: np.ndarray
    mu_a: np.ndarray
    mu_b: np.ndarray
    utility: np.ndarray
    liquid_label: np.ndarray
    transfer_label: np.ndarray
    operator: MatlabFaithfulOperator
    post_convergence_operator: MatlabFaithfulOperator
    iterations: int
    converged: bool
    convergence_statistic: float


def solve_matlab_faithful_hjb(
    grid: MatlabFaithfulHJBGrid,
    params: EconomicParams,
    inputs: HouseholdInputs,
    initial_value: np.ndarray,
    baseline_labor: np.ndarray,
    transfer_income: float,
    borrowing_rate_gap: float,
    numerics: MatlabFaithfulHJBNumerics,
) -> MatlabFaithfulHJBResult:
    shape = (grid.b.size, grid.a.size, grid.z.size)
    value = np.asarray(initial_value, dtype=float).copy()
    labor0 = np.asarray(baseline_labor, dtype=float)
    if value.shape != shape or labor0.shape != shape or not np.isfinite(value).all() or not np.isfinite(labor0).all():
        raise ValueError("initial arrays do not match the faithful MATLAB grid")
    if inputs.wages.size != 1 or numerics.delta <= 0 or numerics.convergence_tolerance <= 0 or numerics.max_iterations < 1:
        raise ValueError("invalid faithful HJB inputs")
    initial = value.copy(); db = float(grid.b[1] - grid.b[0]); da = float(grid.a[1] - grid.a[0])
    arrays: dict[str, np.ndarray] = {}; operator = None; statistic = np.inf; converged = False
    for iteration in range(1, numerics.max_iterations + 1):
        old = value.copy()
        vb_f = np.zeros(shape); vb_b = np.zeros(shape); va_f = np.zeros(shape); va_b = np.zeros(shape)
        vb_f[:-1] = (old[1:] - old[:-1]) / db; vb_b[1:] = vb_f[:-1]
        for j, a in enumerate(grid.a):
            for nz, z in enumerate(grid.z):
                for i in (0, grid.b.size - 1):
                    rb = inputs.r_b + (borrowing_rate_gap if grid.b[i] < 0 else 0.0)
                    resources = (1-inputs.tau)*inputs.wages[0]*z*labor0[i,j,nz] + transfer_income + rb*grid.b[i]
                    marginal = resources ** (-params.gamma_c)
                    if i == 0: vb_b[i,j,nz] = marginal
                    else: vb_f[i,j,nz] = marginal
        va_f[:, :-1] = (old[:, 1:] - old[:, :-1]) / da; va_b[:, 1:] = va_f[:, :-1]
        names = ("consumption","labor","transfer","adjustment_cost","effective_illiquid_return","mu_a","mu_b","utility")
        arrays = {name: np.empty(shape) for name in names}
        liquid = np.empty(shape, dtype="U1"); transfer_label = np.empty(shape, dtype="U1")
        bb = np.empty(shape); bf = np.empty(shape); ab = np.empty(shape); af = np.empty(shape)
        for nz, z in enumerate(grid.z):
            for j, a in enumerate(grid.a):
                for i, b in enumerate(grid.b):
                    policy = select_matlab_faithful_local_policy(a=float(a),b=float(b),z=float(z),v_a_forward=float(va_f[i,j,nz]),v_a_backward=float(va_b[i,j,nz]),v_b_forward=float(vb_f[i,j,nz]),v_b_backward=float(vb_b[i,j,nz]),baseline_labor=float(labor0[i,j,nz]),transfer_income=transfer_income,borrowing_rate_gap=borrowing_rate_gap,a_max=float(grid.a[-1]),da=da,db=db,at_lower_a=j==0,at_upper_a=j+1==grid.a.size,at_lower_b=i==0,at_upper_b=i+1==grid.b.size,inputs=inputs,params=params,tolerance=numerics.drift_tolerance)
                    for name in names: arrays[name][i,j,nz] = getattr(policy, name)
                    liquid[i,j,nz]=policy.liquid_label; transfer_label[i,j,nz]=policy.transfer_label
                    bb[i,j,nz]=policy.iteration_b_backward_rate; bf[i,j,nz]=policy.iteration_b_forward_rate
                    ab[i,j,nz]=policy.a_backward_rate; af[i,j,nz]=policy.a_forward_rate
        operator = assemble_source_operator(bb,bf,ab,af,grid.switch_matrix)
        matrix = (1/numerics.delta + params.rho)*sparse.eye(np.prod(shape),format="csr") - operator.full
        rhs = arrays["utility"].ravel(order="F") + old.ravel(order="F")/numerics.delta
        value = linalg.spsolve(matrix,rhs).reshape(shape,order="F")
        statistic = float(np.max(np.abs(value-old)))
        if statistic < numerics.convergence_tolerance: converged=True; break
    assert operator is not None
    post = assemble_source_operator(np.maximum(-arrays["mu_b"],0)/db,np.maximum(arrays["mu_b"],0)/db,np.maximum(-arrays["mu_a"],0)/da,np.maximum(arrays["mu_a"],0)/da,grid.switch_matrix)
    return MatlabFaithfulHJBResult(value,initial,arrays["consumption"],arrays["labor"],arrays["transfer"],arrays["adjustment_cost"],arrays["effective_illiquid_return"],arrays["mu_a"],arrays["mu_b"],arrays["utility"],liquid,transfer_label,operator,post,iteration,converged,statistic)
