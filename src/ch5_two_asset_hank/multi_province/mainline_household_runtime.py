"""V010 synthetic conditional HA driver; no data readers or historical execute calls.

Policy selection, raw derivatives, boundary adaptation, Q construction and value
relaxation are the accepted corrected mathematical components. This module owns
only the explicit-input iteration, operation accounting and homogeneous KFE gate.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import math
from pathlib import Path
import json
import warnings
import sys

import numpy as np
from scipy import linalg, sparse
from scipy.optimize import brentq
from scipy.sparse import csgraph
from scipy.sparse.linalg import spsolve

from ..corrected_diagnostic.contracts import CorrectedDiagnosticGrid
from ..corrected_diagnostic.generator import assemble_consumed_drift_generator
from ..corrected_diagnostic.option_a_step import (
    raw_derivative_fields, boundary_cell_derivatives, coordinate_action_receipt,
)
from ..corrected_diagnostic.nonlinear_continuation import monotonicity_preserving_relaxation
from ..corrected_diagnostic.selector import (
    CorrectedSelectorCell, CorrectedSelectorParameters, SelectorBudget,
    select_constrained_policy,
)
from .corrected_household_adapter import (
    CorrectedHouseholdAggregateInputs, evaluate_corrected_household_aggregates,
)


class ScienceFailure(RuntimeError):
    """A scientific gate failed; downstream work must not start."""


def array_sha(values):
    return hashlib.sha256(np.asarray(values, dtype='<f8').tobytes(order='F')).hexdigest().upper()


def seal_json(path, payload):
    path = Path(path)
    # Receipts are new, independent objects; never overwrite an earlier attempt.
    with path.open('x', encoding='utf-8', newline='\n') as stream:
        json.dump(payload, stream, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
        stream.write('\n')


@dataclass(frozen=True)
class HAInputs:
    rb: float
    rah: float
    w_eff: float
    transfer: float
    rb_gap: float
    parameters: dict
    grid_spec: dict

    def validate(self):
        if not np.isfinite([self.rb, self.rah, self.w_eff, self.transfer, self.rb_gap]).all():
            raise ValueError('nonfinite HA prices')
        if self.w_eff <= 0:
            raise ValueError('effective wage must be positive; tax has already been deducted')
        if self.grid_spec['shape_b_a_z'] != [20, 20, 2]:
            raise ValueError('V010 grid must remain 20x20x2')
        if self.parameters['HJB_Delta'] != 1000:
            raise ValueError('frozen HJB Delta changed')


def make_grid(spec):
    return CorrectedDiagnosticGrid(
        np.linspace(spec['b_min'], spec['b_max'], 20),
        np.linspace(spec['a_min'], spec['a_max'], 20), np.asarray(spec['z'], dtype=float))


def initial_labor_foc(labor, *, u, resources, parameters):
    c = u * labor + resources
    if c <= 0 or not math.isfinite(c):
        raise ScienceFailure('V0_CONSUMPTION_DOMAIN')
    return labor - (u / parameters['alphal']) ** (1 / parameters['phi_l']) * c ** (
        -parameters['gamma_c'] / parameters['phi_l'])


def construct_v0(inputs, grid, begin_root):
    """Frozen V0, including capital income exactly once; no floor or old seed."""
    p = inputs.parameters
    value = np.empty(grid.shape, order='F')
    consumption = np.empty_like(value)
    labor = np.empty_like(value)
    max_foc = 0.0
    for flat in range(grid.size):
        ix = tuple(np.unravel_index(flat, grid.shape, order='F'))
        ib, ia, iz = ix
        b, a, z = grid.b[ib], grid.a[ia], grid.z[iz]
        u = inputs.w_eff * z
        rb = inputs.rb + (inputs.rb_gap if b < 0 else 0)
        ra = inputs.rah * (1 - 0.1 * (a / grid.a[-1]) ** 9)
        resources = rb * b + ra * a + inputs.transfer
        lower, upper = max(0.0, -resources / u) + 1e-12, 1024.0
        def f(l):
            return initial_labor_foc(l, u=u, resources=resources, parameters=p)
        if lower >= upper or f(lower) * f(upper) > 0:
            raise ScienceFailure('V0_ROOT_NOT_BRACKETED')
        begin_root()
        l = brentq(f, lower, upper, xtol=1e-12, rtol=1e-12, maxiter=100)
        c = u * l + resources
        # Independently evaluated marginal-utility FOC, rather than f(l) alone.
        foc = abs(p['alphal'] * l ** p['phi_l'] - u * c ** (-p['gamma_c']))
        scale = max(1.0, abs(u * c ** (-p['gamma_c'])))
        if foc / scale > 1e-9:
            raise ScienceFailure('V0_FOC_ORACLE_REJECTED')
        max_foc = max(max_foc, foc / scale)
        consumption[ix], labor[ix] = c, l
        value[ix] = (p['alphac'] * c ** (1-p['gamma_c']) / (1-p['gamma_c'])
                     - p['alphal'] * l ** (1+p['phi_l']) / (1+p['phi_l'])) / p['rho']
    slopes = np.diff(value, axis=0) / np.diff(grid.b)[:, None, None]
    if not np.isfinite(value).all() or not (slopes > 0).all():
        raise ScienceFailure('V0_RAW_B_SLOPE_NOT_POSITIVE')
    return value, {'V0_sha256': array_sha(value), 'l0_sha256': array_sha(labor),
                   'c0_sha256': array_sha(consumption), 'max_relative_FOC': max_foc,
                   'minimum_raw_b_slope': float(slopes.min()), 'layout': 'F_ORDER_B_FASTEST'}


def terminal_kfe(q, omega):
    """Exact-positive SCC, one closed class, one restricted homogeneous GESVD."""
    n = q.shape[0]
    off = q.copy().tocsr(); off.setdiag(0); off.eliminate_zeros()
    if not np.isfinite(q.data).all() or (off.data < 0).any():
        raise ScienceFailure('KFE_ILLEGAL_GENERATOR')
    graph = off.copy(); graph.data = (graph.data > 0).astype(float); graph.eliminate_zeros()
    count, labels = csgraph.connected_components(graph, directed=True, connection='strong')
    closed = np.ones(count, dtype=bool)
    rows, cols = graph.nonzero()
    for i, j in zip(rows, cols):
        if labels[i] != labels[j]:
            closed[labels[i]] = False
    classes = np.flatnonzero(closed)
    if len(classes) != 1:
        raise ScienceFailure(f'KFE_CLOSED_CLASSES={len(classes)}')
    members = np.flatnonzero(labels == classes[0])
    a = q[members][:, members].T.toarray()
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        _, s, vh = linalg.svd(a, full_matrices=True, lapack_driver='gesvd', check_finite=True)
    eps = np.finfo(float).eps
    gamma = lambda k: k * eps / (1-k * eps)
    tau_rank = gamma(len(members)+64) * max(1.0, float(s[0]))
    if caught or np.count_nonzero(s <= tau_rank) != 1:
        raise ScienceFailure('KFE_RANK_OR_SVD_WARNING')
    raw = vh[-1]
    total = math.fsum(map(float, raw))
    if abs(total) <= gamma(len(members)+64) * math.fsum(map(float, abs(raw))):
        raise ScienceFailure('KFE_SIGN_ORIENTATION_AMBIGUOUS')
    mass = np.zeros(n); mass[members] = raw / total
    residual = q.T @ mass
    scale = max(1.0, float(np.max(np.asarray(abs(q.T).sum(axis=1)).ravel())) * float(abs(mass).max()))
    nonnegative_bound = gamma(n+64) * max(1.0, float(abs(mass).max()))
    if (float(mass.min()) < -nonnegative_bound
            or math.fsum(map(float, -mass[mass < 0])) > n * nonnegative_bound
            or abs(math.fsum(map(float, mass))-1) > gamma(n+64)
            or float(abs(residual).max()) > gamma(n+64)*scale):
        raise ScienceFailure('KFE_MASS_OR_STATIONARITY')
    return mass, {'closed_classes': 1, 'closed_class_size': len(members),
                  'SCC_count': int(count), 'restricted_nullity': 1,
                  'stationarity_inf': float(abs(residual).max()),
                  'stationarity_bound': gamma(n+64)*scale, 'minimum_mass': float(mass.min()),
                  'mass_sum': math.fsum(map(float, mass)), 'omega': omega}


def solve_conditioned_household(inputs, receipt_directory, global_ledger):
    """One already charged HA attempt. All calls, including failed V0, accumulate."""
    inputs.validate()
    output = Path(receipt_directory); output.mkdir(parents=True, exist_ok=False)
    grid = make_grid(inputs.grid_spec); p = inputs.parameters
    local = {'roots': 0, 'maps': 0, 'updates': 0, 'cells': 0, 'kfe': 0}
    selector_budget = None
    history = []
    def root():
        if local['roots'] >= 400000 or global_ledger['roots'] >= 10400000:
            raise ScienceFailure('ROOT_BUDGET')
        local['roots'] += 1; global_ledger['roots'] += 1
    try:
        import scipy
        code_hashes = {name: hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()
                       for name,module in tuple(sys.modules.items())
                       if name.startswith('ch5_two_asset_hank') and getattr(module,'__file__',None)}
        seal_json(output/'input.json', {'input': asdict(inputs), 'numpy': np.__version__,
                                       'scipy': scipy.__version__, 'tax_HA': 0,
                                       'python':sys.version,'code_hashes':code_hashes,
                                       'layout': 'F_ORDER_B_FASTEST'})
        value, v0_receipt = construct_v0(inputs, grid, root)
        seal_json(output/'V0_before_HJB.json', v0_receipt)
        selector_budget = SelectorBudget(max_selector_evaluations=80800,
              max_root_invocations=min(400000-local['roots'],10400000-global_ledger['roots']))
        pars = CorrectedSelectorParameters(p['gamma_c'], p['phi_l'], p['alphal'],
                                          p['chi_0'], p['chi_1'], p['a_bar'])
        previous = None; checkpoint_identities = []; past_values = []
        for checkpoint in range(101):
            if local['maps'] >= 101:
                raise ScienceFailure('POLICY_MAP_BUDGET')
            local['maps'] += 1
            fields = raw_derivative_fields(value, grid)
            arrays = {name: np.empty(grid.shape, order='F') for name in ('c','l','g_b','g_a','utility')}
            policy_digest = hashlib.sha256()
            for flat in range(grid.size):
                if global_ledger['cells'] >= 2100800:
                    raise ScienceFailure('GLOBAL_SELECTOR_BUDGET')
                ix = tuple(np.unravel_index(flat, grid.shape, order='F'))
                ib, ia, iz = ix; b, a, z = grid.b[ib], grid.a[ia], grid.z[iz]
                derivatives, _ = boundary_cell_derivatives(fields, ix, grid)
                cell = CorrectedSelectorCell(f'cp{checkpoint}_f{flat}', b,a,z,
                    grid.b[0],grid.b[-1],grid.a[0],grid.a[-1],inputs.w_eff*z,
                    inputs.rb+(inputs.rb_gap if b<0 else 0),inputs.transfer,
                    inputs.rah*(1-0.1*(a/grid.a[-1])**9),derivatives)
                before = selector_budget.root_invocations
                global_ledger['cells'] += 1; local['cells'] += 1
                try:
                    result = select_constrained_policy(cell, pars, budget=selector_budget)
                finally:
                    used = selector_budget.root_invocations-before
                    local['roots'] += used; global_ledger['roots'] += used
                if local['roots'] > 400000 or global_ledger['roots'] > 10400000:
                    raise ScienceFailure('ROOT_BUDGET')
                if result.outcome != 'SELECTED_ADMISSIBLE' or result.selected is None:
                    seal_json(output/'first_failed_cell.json', {'checkpoint': checkpoint,
                              'flat_F': flat, 'cell': asdict(cell), 'result': asdict(result)})
                    raise ScienceFailure(f'POLICY_{result.outcome}_CP{checkpoint}_F{flat}')
                for name in arrays:
                    arrays[name][ix] = getattr(result.selected, name)
                policy_digest.update(repr(result.selected).encode('utf-8'))
            assembled = assemble_consumed_drift_generator(grid, mu_b=arrays['g_b'], mu_a=arrays['g_a'],
                           z_generator=np.asarray(inputs.grid_spec['z_transition_generator']))
            q = assembled.q
            coordinate = coordinate_action_receipt(q,grid,arrays['g_b'],arrays['g_a'])
            if (assembled.minimum_offdiagonal < 0 or assembled.diagonal_construction_error != 0
                    or assembled.max_abs_q_one > assembled.arithmetic_tolerance
                    or not coordinate['b']['passes'] or not coordinate['a']['passes']):
                raise ScienceFailure('D2_OPERATOR_GATE')
            bellman = float(abs(p['rho']*value.ravel(order='F')-arrays['utility'].ravel(order='F')
                                 -q@value.ravel(order='F')).max())
            change = None if previous is None else float(abs(value-previous).max())
            identity = (array_sha(value), array_sha(q.data), array_sha(q.indices),
                        array_sha(q.indptr), policy_digest.hexdigest())
            history.append({'checkpoint': checkpoint, 'B': bellman, 'D': change,
                            'Q_one_inf': assembled.max_abs_q_one, 'V_sha': identity[0],
                            'Q_data_sha': identity[1]})
            if change is not None and bellman <= 1e-8 and change <= 1e-7:
                local['kfe'] += 1
                omega = (grid.b[1]-grid.b[0])*(grid.a[1]-grid.a[0])
                mass, kfe_receipt = terminal_kfe(q, omega)
                effective_ra = np.broadcast_to(inputs.rah*(1-0.1*(grid.a[None,:,None]/grid.a[-1])**9), grid.shape)
                agg = evaluate_corrected_household_aggregates(CorrectedHouseholdAggregateInputs(
                    b_grid=grid.b, a_grid=grid.a, z_grid=grid.z, consumption=arrays['c'],
                    labor=arrays['l'], probability_mass=mass.reshape(grid.shape, order='F'),
                    density=(mass/omega).reshape(grid.shape, order='F'), omega=omega,
                    source_r_a=inputs.rah, effective_r_a=effective_ra))
                if agg.At.mass_form <= 0 or agg.Lt.mass_form <= 0:
                    raise ScienceFailure('HA_DEGENERATE_ASSETS_OR_LABOR')
                frozen = agg.frozen_output(converged=True, convergence_statistic=bellman)
                seal_json(output/'qualified.json', {'outputs': asdict(frozen), 'KFE': kfe_receipt,
                          'history': history, 'policy_hashes': {k:array_sha(v) for k,v in arrays.items()}})
                return frozen, {'B':bellman,'D':change,'KFE':kfe_receipt,'V0':v0_receipt}
            if identity in checkpoint_identities[:-1]:
                raise ScienceFailure('EXACT_CYCLE')
            past_values.append(value.copy()); checkpoint_identities.append(identity)
            for period in (2,3):
                if len(past_values) >= 2*period and all(
                    float(abs(past_values[j]-past_values[j-period]).max()) <= 1e-8
                    for j in range(len(past_values)-period, len(past_values))):
                    raise ScienceFailure(f'APPROXIMATE_PERIOD_{period}_CYCLE')
            if checkpoint == 100:
                raise ScienceFailure('HJB_MAX100_NONCONVERGED')
            matrix = (p['rho']+1/1000)*sparse.eye(grid.size,format='csr')-q
            rhs = arrays['utility'].ravel(order='F')+value.ravel(order='F')/1000
            local['updates'] += 1
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter('always'); full = spsolve(matrix,rhs)
            residual = float(abs(matrix@full-rhs).max())
            denominator = float(np.asarray(abs(matrix).sum(axis=1)).max())*float(abs(full).max())+float(abs(rhs).max())
            error = residual/denominator if denominator else residual
            if caught or not np.isfinite(full).all() or error > 1e-12:
                raise ScienceFailure('HJB_DIRECT_SOLVE_GATE')
            previous = value
            value, relax = monotonicity_preserving_relaxation(value,full.reshape(grid.shape,order='F'),grid.b)
            history[-1].update(backward_error=error, alpha=relax['accepted_alpha'],
                               halvings=relax['accepted_halvings'])
            seal_json(output/f'update_{checkpoint:03d}.json', {'solve_backward_error':error,'relaxation':relax})
    finally:
        seal_json(output/'attempt_summary.json', {'local_calls':local, 'history':history,
                  'selector_budget': None if selector_budget is None else asdict(selector_budget)})
