"""Accepted HJB map with one post-direct-solve value-state relaxation hook."""

from __future__ import annotations

from collections import Counter
from typing import Any

import numpy as np
from scipy import sparse

from exports import matlab_faithful_two_asset_ha as oracle
from validators.multi_province.k1_hjb_convergence_mechanism.instrumented_hjb import (
    _operator_metrics,
    _summary,
)

ALLOWED_OMEGAS = (0.5, 1.0)


def relaxed_value_state(old: np.ndarray, solved: np.ndarray, omega: float) -> np.ndarray:
    """Return the only authorized intervention, applied after the direct solve."""
    if omega not in ALLOWED_OMEGAS:
        raise ValueError("only preregistered omega=0.5 and parity omega=1 are allowed")
    return (1.0 - omega) * old + omega * solved


def raw_fixed_point_converged(old: np.ndarray, solved: np.ndarray, tolerance: float) -> bool:
    """Test the undamped fixed-point residual, never the relaxed update."""
    return bool(np.max(np.abs(solved - old)) < tolerance)


def solve_with_value_relaxation(
    grid: Any,
    params: Any,
    inputs: Any,
    initial_value: np.ndarray,
    baseline_labor: np.ndarray,
    transfer_income: float,
    borrowing_rate_gap: float,
    numerics: Any,
    *,
    omega: float,
) -> tuple[Any, dict[str, Any]]:
    """Run the accepted map; change only the value state after ``V_solve`` exists."""

    if omega not in ALLOWED_OMEGAS:
        raise ValueError("unauthorized omega")
    shape = (grid.b.size, grid.a.size, grid.z.size)
    value = np.asarray(initial_value, dtype=float).copy()
    labor0 = np.asarray(baseline_labor, dtype=float)
    if value.shape != shape or labor0.shape != shape or not np.isfinite(value).all() or not np.isfinite(labor0).all():
        raise ValueError("initial arrays do not match the faithful MATLAB grid")
    if inputs.wages.size != 1 or numerics.delta <= 0 or numerics.convergence_tolerance <= 0 or numerics.max_iterations < 1:
        raise ValueError("invalid faithful HJB inputs")
    initial = value.copy()
    db = float(grid.b[1] - grid.b[0])
    da = float(grid.a[1] - grid.a[0])
    arrays: dict[str, np.ndarray] = {}
    operator = None
    statistic = np.inf
    converged = False
    observations: list[dict[str, Any]] = []
    prior_liquid: np.ndarray | None = None
    prior_transfer: np.ndarray | None = None
    two_back_liquid: np.ndarray | None = None
    two_back_transfer: np.ndarray | None = None
    two_back_value: np.ndarray | None = None
    direct_solves = 0
    solved = value.copy()

    for iteration in range(1, numerics.max_iterations + 1):
        old = value.copy()
        vb_f = np.zeros(shape)
        vb_b = np.zeros(shape)
        va_f = np.zeros(shape)
        va_b = np.zeros(shape)
        vb_f[:-1] = (old[1:] - old[:-1]) / db
        vb_b[1:] = vb_f[:-1]
        for j, a in enumerate(grid.a):
            for nz, z in enumerate(grid.z):
                for i in (0, grid.b.size - 1):
                    rb = inputs.r_b + (borrowing_rate_gap if grid.b[i] < 0 else 0.0)
                    resources = (1-inputs.tau)*inputs.wages[0]*z*labor0[i,j,nz] + transfer_income + rb*grid.b[i]
                    marginal = resources ** (-params.gamma_c)
                    if i == 0:
                        vb_b[i,j,nz] = marginal
                    else:
                        vb_f[i,j,nz] = marginal
        va_f[:, :-1] = (old[:, 1:] - old[:, :-1]) / da
        va_b[:, 1:] = va_f[:, :-1]
        names = ("consumption", "labor", "transfer", "adjustment_cost", "effective_illiquid_return", "mu_a", "mu_b", "utility")
        arrays = {name: np.empty(shape) for name in names}
        liquid = np.empty(shape, dtype="U1")
        transfer_label = np.empty(shape, dtype="U1")
        bb = np.empty(shape)
        bf = np.empty(shape)
        ab = np.empty(shape)
        af = np.empty(shape)
        for nz, z in enumerate(grid.z):
            for j, a in enumerate(grid.a):
                for i, b in enumerate(grid.b):
                    policy = oracle.select_matlab_faithful_local_policy(
                        a=float(a), b=float(b), z=float(z),
                        v_a_forward=float(va_f[i,j,nz]), v_a_backward=float(va_b[i,j,nz]),
                        v_b_forward=float(vb_f[i,j,nz]), v_b_backward=float(vb_b[i,j,nz]),
                        baseline_labor=float(labor0[i,j,nz]), transfer_income=transfer_income,
                        borrowing_rate_gap=borrowing_rate_gap, a_max=float(grid.a[-1]), da=da, db=db,
                        at_lower_a=j == 0, at_upper_a=j + 1 == grid.a.size,
                        at_lower_b=i == 0, at_upper_b=i + 1 == grid.b.size,
                        inputs=inputs, params=params, tolerance=numerics.drift_tolerance,
                    )
                    for name in names:
                        arrays[name][i,j,nz] = getattr(policy, name)
                    liquid[i,j,nz] = policy.liquid_label
                    transfer_label[i,j,nz] = policy.transfer_label
                    bb[i,j,nz] = policy.iteration_b_backward_rate
                    bf[i,j,nz] = policy.iteration_b_forward_rate
                    ab[i,j,nz] = policy.a_backward_rate
                    af[i,j,nz] = policy.a_forward_rate
        operator = oracle.assemble_source_operator(bb, bf, ab, af, grid.switch_matrix)
        matrix = (1/numerics.delta + params.rho)*sparse.eye(np.prod(shape), format="csr") - operator.full
        rhs = arrays["utility"].ravel(order="F") + old.ravel(order="F")/numerics.delta
        solved = oracle.linalg.spsolve(matrix, rhs).reshape(shape, order="F")
        direct_solves += 1

        # The intervention starts here, after the accepted direct solve.
        statistic = float(np.max(np.abs(solved - old)))
        value_next = relaxed_value_state(old, solved, omega)
        relaxed_update = float(np.max(np.abs(value_next - old)))
        update = solved - old
        flat_index = int(np.argmax(np.abs(update)))
        argmax = tuple(int(x) for x in np.unravel_index(flat_index, shape))
        two_step = float(np.max(np.abs(value_next - two_back_value))) if two_back_value is not None else None
        switch_count = (int(np.count_nonzero(liquid != prior_liquid) + np.count_nonzero(transfer_label != prior_transfer))
                        if prior_liquid is not None and prior_transfer is not None else None)
        reversion_count = (int(np.count_nonzero((liquid == two_back_liquid) & (liquid != prior_liquid))
                               + np.count_nonzero((transfer_label == two_back_transfer) & (transfer_label != prior_transfer)))
                           if two_back_liquid is not None and two_back_transfer is not None
                           and prior_liquid is not None and prior_transfer is not None else None)
        floor = oracle.MATLAB_DERIVATIVE_FLOOR
        used_vb_f = np.maximum(vb_f, floor)
        used_vb_b = np.maximum(vb_b, floor)
        residual = matrix @ solved.ravel(order="F") - rhs
        finite_arrays = {name: bool(np.isfinite(array).all()) for name, array in arrays.items()}
        observations.append({
            "iteration": iteration,
            "raw_fixed_point_gap": statistic,
            "relaxed_state_update": relaxed_update,
            "raw_gap_to_relaxed_update_ratio": statistic / relaxed_update if relaxed_update else None,
            "value_update_argmax_zero_based": list(argmax),
            "value_update_signed_at_argmax": float(update[argmax]),
            "value_two_step_inf": two_step,
            "policy_label_switch_count": switch_count,
            "policy_two_step_reversion_count": reversion_count,
            "liquid_label_counts": dict(Counter(map(str, liquid.ravel()))),
            "transfer_label_counts": dict(Counter(map(str, transfer_label.ravel()))),
            "derivatives": {
                "vb_forward_raw": _summary(vb_f), "vb_forward_used": _summary(used_vb_f),
                "vb_backward_raw": _summary(vb_b), "vb_backward_used": _summary(used_vb_b),
                "va_forward_raw": _summary(va_f), "va_forward_used": _summary(va_f),
                "va_backward_raw": _summary(va_b), "va_backward_used": _summary(va_b),
                "floor_hit_counts": {
                    "vb_forward": int(np.count_nonzero(vb_f < floor)),
                    "vb_backward": int(np.count_nonzero(vb_b < floor)), "va_forward": 0, "va_backward": 0,
                },
                "floor_hit_shares": {
                    "vb_forward": float(np.count_nonzero(vb_f < floor) / vb_f.size),
                    "vb_backward": float(np.count_nonzero(vb_b < floor) / vb_b.size), "va_forward": 0.0, "va_backward": 0.0,
                },
                "nonpositive_raw_counts": {
                    "vb_forward": int(np.count_nonzero(vb_f <= 0.0)), "vb_backward": int(np.count_nonzero(vb_b <= 0.0)),
                    "va_forward": int(np.count_nonzero(va_f <= 0.0)), "va_backward": int(np.count_nonzero(va_b <= 0.0)),
                },
                "nonfinite_raw_counts": {
                    "vb_forward": int(np.count_nonzero(~np.isfinite(vb_f))), "vb_backward": int(np.count_nonzero(~np.isfinite(vb_b))),
                    "va_forward": int(np.count_nonzero(~np.isfinite(va_f))), "va_backward": int(np.count_nonzero(~np.isfinite(va_b))),
                },
            },
            "selected": {name: _summary(arrays[name]) for name in ("consumption", "labor", "transfer", "adjustment_cost", "mu_a", "mu_b")},
            "drifts": {"b_backward_rate": _summary(bb), "b_forward_rate": _summary(bf),
                       "a_backward_rate": _summary(ab), "a_forward_rate": _summary(af)},
            "operator": _operator_metrics(operator.full),
            "linear_solve_residual_inf": float(np.linalg.norm(residual, ord=np.inf)),
            "finite": {"v_old": bool(np.isfinite(old).all()), "v_solve": bool(np.isfinite(solved).all()),
                       "v_next": bool(np.isfinite(value_next).all()), "scientific_arrays": finite_arrays},
        })
        two_back_value = old
        two_back_liquid, prior_liquid = prior_liquid, liquid.copy()
        two_back_transfer, prior_transfer = prior_transfer, transfer_label.copy()
        value = value_next
        if raw_fixed_point_converged(old, solved, numerics.convergence_tolerance):
            converged = True
            value = solved
            break
    assert operator is not None
    post = oracle.assemble_source_operator(np.maximum(-arrays["mu_b"],0)/db, np.maximum(arrays["mu_b"],0)/db,
                                           np.maximum(-arrays["mu_a"],0)/da, np.maximum(arrays["mu_a"],0)/da,
                                           grid.switch_matrix)
    result = oracle.MatlabFaithfulHJBResult(value, initial, arrays["consumption"], arrays["labor"], arrays["transfer"],
        arrays["adjustment_cost"], arrays["effective_illiquid_return"], arrays["mu_a"], arrays["mu_b"], arrays["utility"],
        liquid, transfer_label, operator, post, iteration, converged, statistic)
    return result, {
        "schema": "CH5_MP4C_K1_HJB_VALUE_RELAXATION_TRACE_V1",
        "omega": omega,
        "convergence_contract": "RAW_FIXED_POINT_GAP_V_SOLVE_MINUS_V_OLD_INF_LT_TOLERANCE",
        "direct_solves": direct_solves,
        "iterations": observations,
    }
