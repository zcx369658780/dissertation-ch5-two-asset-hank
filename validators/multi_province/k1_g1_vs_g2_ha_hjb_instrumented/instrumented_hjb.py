"""Task-bounded observational clone of the accepted faithful HJB loop.

The scientific operations and their ordering mirror the frozen export.  Extra
work only observes values after the accepted policy calculation and never feeds
diagnostics back into the scientific result.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from typing import Any, Callable, Iterable

import numpy as np
from scipy import sparse

from exports import matlab_faithful_two_asset_ha as oracle


def array_hash(value: np.ndarray) -> str:
    array = np.asarray(value)
    header = f"{array.dtype.str}|{array.shape}|C|".encode("ascii")
    return sha256(header + np.ascontiguousarray(array).tobytes()).hexdigest().upper()


def numeric_summary(value: np.ndarray) -> dict[str, Any]:
    array = np.asarray(value, dtype=float)
    finite = array[np.isfinite(array)]
    result: dict[str, Any] = {
        "count": int(array.size),
        "nonfinite_count": int(array.size - finite.size),
    }
    if finite.size:
        result.update({
            "min": float(np.min(finite)),
            "median": float(np.median(finite)),
            "p95": float(np.quantile(finite, 0.95)),
            "p99": float(np.quantile(finite, 0.99)),
            "max": float(np.max(finite)),
            "abs_max": float(np.max(np.abs(finite))),
        })
    return result


def array_record(value: np.ndarray) -> dict[str, Any]:
    array = np.asarray(value)
    record = {**numeric_summary(array), "sha256": array_hash(array)}
    finite_abs = np.where(np.isfinite(array), np.abs(array), -np.inf)
    if np.any(np.isfinite(array)):
        index = tuple(int(x) for x in np.unravel_index(int(np.argmax(finite_abs)), array.shape))
        record["abs_max_witness"] = {
            "grid_index_zero_based": {"i_b": index[0], "i_a": index[1], "i_z": index[2]},
            "value": float(array[index]),
        }
    return record


def _local_diagnostics(
    *, a: float, b: float, z: float, v_a_forward: float, v_a_backward: float,
    v_b_forward: float, v_b_backward: float, baseline_labor: float,
    transfer_income: float, borrowing_rate_gap: float, a_max: float,
    da: float, db: float,
    at_lower_a: bool, at_upper_a: bool, at_lower_b: bool, at_upper_b: bool,
    inputs: Any, params: Any, tolerance: float, policy: Any,
    transfer_candidate_abs_limit: float | None = None,
) -> dict[str, Any]:
    del da, db
    effective_r_b = inputs.r_b + (borrowing_rate_gap if b < 0.0 else 0.0)
    local_inputs = oracle.HouseholdInputs(
        inputs.r_a, effective_r_b, inputs.tau, inputs.wages,
        inputs.migration_costs, inputs.labor_weights,
    )
    vb_b = max(v_b_backward, oracle.MATLAB_DERIVATIVE_FLOOR)
    vb_f = max(v_b_forward, oracle.MATLAB_DERIVATIVE_FLOOR)
    consumption_b = oracle.consumption_from_vb(vb_b, params)
    consumption_f = oracle.consumption_from_vb(vb_f, params)
    labor_b = float(oracle.labor_from_vb(vb_b, z, local_inputs, params)[0])
    labor_f = float(oracle.labor_from_vb(vb_f, z, local_inputs, params)[0])
    net_wage = float(local_inputs.wages[0] *
                     (1.0 - local_inputs.tau - local_inputs.migration_costs[0]) * z)
    sc_b = net_wage * labor_b + transfer_income + effective_r_b * b - consumption_b
    sc_f = net_wage * labor_f + transfer_income + effective_r_b * b - consumption_f
    use_liquid_b = sc_b < -tolerance
    use_liquid_f = sc_f > tolerance and not use_liquid_b

    d_bb = oracle.transfer_candidate_matlab_faithful_raw_vb(v_a_backward, v_b_backward, a, params)
    d_bf = oracle.transfer_candidate_matlab_faithful_raw_vb(v_a_forward, v_b_backward, a, params)
    d_fb = oracle.transfer_candidate_matlab_faithful_raw_vb(v_a_backward, v_b_forward, a, params)
    d_ff = oracle.transfer_candidate_matlab_faithful_raw_vb(v_a_forward, v_b_forward, a, params)
    candidates = oracle.select_matlab_faithful_transfer_candidates_from_raw(
        d_bb,
        d_bf,
        d_fb,
        d_ff,
        at_lower_a=at_lower_a,
        at_upper_a=at_upper_a,
        at_lower_b=at_lower_b,
        tolerance=tolerance,
        transfer_candidate_abs_limit=transfer_candidate_abs_limit,
    )
    d_b, d_f = candidates.d_b, candidates.d_f
    cost_b = float(oracle.asset_drifts_matlab_faithful(
        a, b, z, 0.0, np.array([0.0]), d_b, local_inputs, params, a_max)[2])
    cost_f = float(oracle.asset_drifts_matlab_faithful(
        a, b, z, 0.0, np.array([0.0]), d_f, local_inputs, params, a_max)[2])
    sdh_b, sdh_f = -d_b - cost_b, -d_f - cost_f
    use_transfer_f = sdh_f > tolerance
    use_transfer_b = sdh_b < -tolerance and not use_transfer_f
    if at_lower_b:
        use_transfer_b = False
    if at_upper_b:
        use_transfer_f, use_transfer_b = False, True
    effective_return = float(oracle.matlab_faithful_illiquid_return(a, a_max, inputs.r_a))
    return {
        "raw_derivatives": {
            "va_forward": float(v_a_forward), "va_backward": float(v_a_backward),
            "vb_forward": float(v_b_forward), "vb_backward": float(v_b_backward),
        },
        "floored_liquid_derivatives": {"vb_forward": float(vb_f), "vb_backward": float(vb_b)},
        "derivative_floor_activated": {
            "vb_forward": bool(v_b_forward < oracle.MATLAB_DERIVATIVE_FLOOR),
            "vb_backward": bool(v_b_backward < oracle.MATLAB_DERIVATIVE_FLOOR),
        },
        "liquid_candidates": {
            "consumption_b": float(consumption_b), "consumption_f": float(consumption_f),
            "labor_b": labor_b, "labor_f": labor_f, "sc_b": float(sc_b), "sc_f": float(sc_f),
        },
        "liquid_selector": {"use_liquid_b": bool(use_liquid_b), "use_liquid_f": bool(use_liquid_f)},
        "transfer_candidates": {key: float(value) for key, value in {
            "d_bb": d_bb, "d_bf": d_bf, "d_fb": d_fb, "d_ff": d_ff,
            "d_b": d_b, "d_f": d_f, "cost_b": cost_b, "cost_f": cost_f,
        }.items()},
        "transfer_selector": {
            "sdh_b": float(sdh_b), "sdh_f": float(sdh_f),
            "use_transfer_b": bool(use_transfer_b), "use_transfer_f": bool(use_transfer_f),
            "comparison_criterion": "sdh_f>tolerance; else sdh_b<-tolerance; boundary overrides",
        },
        "effective_illiquid_return": effective_return,
        "effective_illiquid_return_contribution": float(effective_return * a),
        "boundary": {"lower_a": at_lower_a, "upper_a": at_upper_a,
                     "lower_b": at_lower_b, "upper_b": at_upper_b},
        "selected": {
            "liquid_label": policy.liquid_label, "transfer_label": policy.transfer_label,
            "consumption": float(policy.consumption), "labor": float(policy.labor),
            "transfer": float(policy.transfer), "adjustment_cost": float(policy.adjustment_cost),
            "mu_a": float(policy.mu_a), "mu_b": float(policy.mu_b),
        },
    }


def solve_with_trace(
    grid: Any, params: Any, inputs: Any, initial_value: np.ndarray,
    baseline_labor: np.ndarray, transfer_income: float, borrowing_rate_gap: float,
    numerics: Any, *, checkpoint_cells: Iterable[tuple[int, int, int]] = (),
    iteration_observer: Callable[[int, dict[str, np.ndarray]], None] | None = None,
    transfer_candidate_abs_limit: float | None = None,
    policy_comparison_observer: Callable[[int, dict[str, np.ndarray]], None] | None = None,
) -> tuple[Any, dict[str, Any]]:
    shape = (grid.b.size, grid.a.size, grid.z.size)
    value = np.asarray(initial_value, dtype=float).copy()
    labor0 = np.asarray(baseline_labor, dtype=float)
    if value.shape != shape or labor0.shape != shape or not np.isfinite(value).all() or not np.isfinite(labor0).all():
        raise ValueError("initial arrays do not match the faithful MATLAB grid")
    if inputs.wages.size != 1 or numerics.delta <= 0 or numerics.convergence_tolerance <= 0 or numerics.max_iterations < 1:
        raise ValueError("invalid faithful HJB inputs")
    checkpoints = {tuple(int(x) for x in cell) for cell in checkpoint_cells}
    initial = value.copy(); db = float(grid.b[1] - grid.b[0]); da = float(grid.a[1] - grid.a[0])
    arrays: dict[str, np.ndarray] = {}; operator = None; statistic = np.inf; converged = False
    traces: list[dict[str, Any]] = []
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
        candidate_fields = ("d_bb", "d_bf", "d_fb", "d_ff", "d_b", "d_f", "cost_b", "cost_f", "sc_b", "sc_f", "sdh_b", "sdh_f")
        candidate_arrays = {name: np.empty(shape) for name in candidate_fields}
        control_arrays = ({
            name: np.empty(shape) for name in (
                "transfer", "adjustment_cost", "mu_a", "mu_b", "consumption", "labor",
            )
        } if policy_comparison_observer is not None else None)
        control_transfer_label = (np.empty(shape, dtype="U1")
                                  if policy_comparison_observer is not None else None)
        control_liquid_label = (np.empty(shape, dtype="U1")
                                if policy_comparison_observer is not None else None)
        checkpoint_rows: list[dict[str, Any]] = []
        dynamic_witnesses: dict[str, tuple[float, dict[str, Any]]] = {}
        for nz, z in enumerate(grid.z):
            for j, a in enumerate(grid.a):
                for i, b in enumerate(grid.b):
                    kwargs = dict(a=float(a),b=float(b),z=float(z),v_a_forward=float(va_f[i,j,nz]),v_a_backward=float(va_b[i,j,nz]),v_b_forward=float(vb_f[i,j,nz]),v_b_backward=float(vb_b[i,j,nz]),baseline_labor=float(labor0[i,j,nz]),transfer_income=transfer_income,borrowing_rate_gap=borrowing_rate_gap,a_max=float(grid.a[-1]),da=da,db=db,at_lower_a=j==0,at_upper_a=j+1==grid.a.size,at_lower_b=i==0,at_upper_b=i+1==grid.b.size,inputs=inputs,params=params,tolerance=numerics.drift_tolerance)
                    policy = oracle.select_matlab_faithful_local_policy(
                        **kwargs,
                        transfer_candidate_abs_limit=transfer_candidate_abs_limit,
                    )
                    for name in names: arrays[name][i,j,nz] = getattr(policy, name)
                    liquid[i,j,nz]=policy.liquid_label; transfer_label[i,j,nz]=policy.transfer_label
                    bb[i,j,nz]=policy.iteration_b_backward_rate; bf[i,j,nz]=policy.iteration_b_forward_rate
                    ab[i,j,nz]=policy.a_backward_rate; af[i,j,nz]=policy.a_forward_rate
                    observed = _local_diagnostics(
                        **kwargs,
                        policy=policy,
                        transfer_candidate_abs_limit=transfer_candidate_abs_limit,
                    )
                    if control_arrays is not None:
                        raw_values = tuple(
                            float(observed["transfer_candidates"][name])
                            for name in ("d_bb", "d_bf", "d_fb", "d_ff")
                        )
                        has_d1_hit = (
                            transfer_candidate_abs_limit is not None
                            and any(abs(value) > transfer_candidate_abs_limit for value in raw_values)
                        )
                        control_policy = (oracle.select_matlab_faithful_local_policy(**kwargs)
                                          if has_d1_hit else policy)
                        for name in control_arrays:
                            control_arrays[name][i, j, nz] = getattr(control_policy, name)
                        assert control_transfer_label is not None and control_liquid_label is not None
                        control_transfer_label[i, j, nz] = control_policy.transfer_label
                        control_liquid_label[i, j, nz] = control_policy.liquid_label
                    for name in candidate_fields:
                        section = "liquid_candidates" if name.startswith("sc_") else "transfer_selector" if name.startswith("sdh_") else "transfer_candidates"
                        candidate_arrays[name][i,j,nz] = observed[section][name]
                        magnitude = abs(float(observed[section][name]))
                        if np.isfinite(magnitude) and (name not in dynamic_witnesses or magnitude > dynamic_witnesses[name][0]):
                            witness = dict(observed)
                            witness["grid_index_zero_based"] = {"i_b": i, "i_a": j, "i_z": nz}
                            witness["coordinate"] = {"b": float(b), "a": float(a), "z": float(z)}
                            witness["witness_reason"] = f"dynamic_abs_max_{name}"
                            dynamic_witnesses[name] = (magnitude, witness)
                    if (i, j, nz) in checkpoints:
                        observed["grid_index_zero_based"] = {"i_b": i, "i_a": j, "i_z": nz}
                        observed["coordinate"] = {"b": float(b), "a": float(a), "z": float(z)}
                        checkpoint_rows.append(observed)
        checkpoint_rows.extend(item[1] for item in dynamic_witnesses.values())
        operator = oracle.assemble_source_operator(bb,bf,ab,af,grid.switch_matrix)
        matrix = (1/numerics.delta + params.rho)*sparse.eye(np.prod(shape),format="csr") - operator.full
        rhs = arrays["utility"].ravel(order="F") + old.ravel(order="F")/numerics.delta
        value = oracle.linalg.spsolve(matrix,rhs).reshape(shape,order="F")
        statistic = float(np.max(np.abs(value-old)))
        operator_digest = array_hash(operator.full.toarray())
        derivative_arrays = {"vb_forward_raw": vb_f, "vb_backward_raw": vb_b,
                             "va_forward_raw": va_f, "va_backward_raw": va_b}
        traces.append({
            "iteration": iteration, "convergence_statistic": statistic,
            "converged": bool(statistic < numerics.convergence_tolerance),
            "value_old": numeric_summary(old), "value_new": numeric_summary(value),
            "value_old_sha256": array_hash(old), "value_new_sha256": array_hash(value),
            "derivatives": {name: array_record(array)
                            for name, array in derivative_arrays.items()},
            "derivative_floor_activation_counts": {
                "vb_forward": int(np.count_nonzero(vb_f < oracle.MATLAB_DERIVATIVE_FLOOR)),
                "vb_backward": int(np.count_nonzero(vb_b < oracle.MATLAB_DERIVATIVE_FLOOR)),
            },
            "derivative_floor_activation_coordinates": {
                "vb_forward": np.argwhere(vb_f < oracle.MATLAB_DERIVATIVE_FLOOR).tolist(),
                "vb_backward": np.argwhere(vb_b < oracle.MATLAB_DERIVATIVE_FLOOR).tolist(),
            },
            "candidate_objects": {name: array_record(array)
                                  for name, array in candidate_arrays.items()},
            "selected_objects": {name: array_record(arrays[name])
                                 for name in ("consumption", "labor", "transfer", "adjustment_cost",
                                              "effective_illiquid_return", "mu_a", "mu_b")},
            "liquid_label_counts": dict(Counter(map(str, liquid.ravel()))),
            "transfer_label_counts": dict(Counter(map(str, transfer_label.ravel()))),
            "liquid_label_sha256": array_hash(liquid),
            "transfer_label_sha256": array_hash(transfer_label),
            "operator_sha256": operator_digest,
            "checkpoint_cells": checkpoint_rows,
        })
        if iteration_observer is not None:
            observed_arrays = {
                name: np.array(candidate_arrays[name], copy=True)
                for name in ("d_bb", "d_bf", "d_fb", "d_ff")
            }
            observed_arrays.update({
                "selected_transfer": np.array(arrays["transfer"], copy=True),
                "selected_adjustment_cost": np.array(arrays["adjustment_cost"], copy=True),
                "transfer_label": np.array(transfer_label, copy=True),
            })
            for observed_array in observed_arrays.values():
                observed_array.setflags(write=False)
            iteration_observer(iteration, observed_arrays)
        if policy_comparison_observer is not None:
            assert control_arrays is not None
            assert control_transfer_label is not None and control_liquid_label is not None
            comparison_arrays = {
                name: np.array(candidate_arrays[name], copy=True)
                for name in ("d_bb", "d_bf", "d_fb", "d_ff")
            }
            comparison_arrays.update({
                "selected_transfer": np.array(arrays["transfer"], copy=True),
                "selected_adjustment_cost": np.array(arrays["adjustment_cost"], copy=True),
                "selected_mu_a": np.array(arrays["mu_a"], copy=True),
                "selected_mu_b": np.array(arrays["mu_b"], copy=True),
                "selected_consumption": np.array(arrays["consumption"], copy=True),
                "selected_labor": np.array(arrays["labor"], copy=True),
                "selected_transfer_label": np.array(transfer_label, copy=True),
                "selected_liquid_label": np.array(liquid, copy=True),
                "control_transfer": np.array(control_arrays["transfer"], copy=True),
                "control_adjustment_cost": np.array(control_arrays["adjustment_cost"], copy=True),
                "control_mu_a": np.array(control_arrays["mu_a"], copy=True),
                "control_mu_b": np.array(control_arrays["mu_b"], copy=True),
                "control_consumption": np.array(control_arrays["consumption"], copy=True),
                "control_labor": np.array(control_arrays["labor"], copy=True),
                "control_transfer_label": np.array(control_transfer_label, copy=True),
                "control_liquid_label": np.array(control_liquid_label, copy=True),
                "value_new": np.array(value, copy=True),
                "convergence_statistic": np.asarray(statistic),
                "operator_sha256": np.asarray(operator_digest),
            })
            for comparison_array in comparison_arrays.values():
                comparison_array.setflags(write=False)
            policy_comparison_observer(iteration, comparison_arrays)
        if statistic < numerics.convergence_tolerance: converged=True; break
    assert operator is not None
    post = oracle.assemble_source_operator(np.maximum(-arrays["mu_b"],0)/db,np.maximum(arrays["mu_b"],0)/db,np.maximum(-arrays["mu_a"],0)/da,np.maximum(arrays["mu_a"],0)/da,grid.switch_matrix)
    result = oracle.MatlabFaithfulHJBResult(value,initial,arrays["consumption"],arrays["labor"],arrays["transfer"],arrays["adjustment_cost"],arrays["effective_illiquid_return"],arrays["mu_a"],arrays["mu_b"],arrays["utility"],liquid,transfer_label,operator,post,iteration,converged,statistic)
    trace = {
        "schema": "CH5_K1_G1_VS_G2_HA_HJB_ITERATION_TRACE_V1",
        "scientific_output_parity_role": "OBSERVATION_ONLY",
        "initial_value_sha256": array_hash(initial),
        "grid_sha256": {"b": array_hash(grid.b), "a": array_hash(grid.a), "z": array_hash(grid.z),
                        "switch_matrix": array_hash(grid.switch_matrix)},
        "params": {name: float(getattr(params, name)) for name in params.__dataclass_fields__},
        "numerics": {name: float(getattr(numerics, name)) if name != "max_iterations" else int(getattr(numerics, name))
                     for name in numerics.__dataclass_fields__},
        "inputs": {"r_a": float(inputs.r_a), "r_b": float(inputs.r_b), "tau": float(inputs.tau),
                   "wages": np.asarray(inputs.wages, dtype=float).tolist(),
                   "migration_costs": np.asarray(inputs.migration_costs, dtype=float).tolist(),
                   "labor_weights": np.asarray(inputs.labor_weights, dtype=float).tolist(),
                   "transfer_income": float(transfer_income), "borrowing_rate_gap": float(borrowing_rate_gap)},
        "iterations": traces,
        "final_iteration_count": iteration,
        "final_converged": bool(converged),
        "final_convergence_statistic": statistic,
    }
    return result, trace
