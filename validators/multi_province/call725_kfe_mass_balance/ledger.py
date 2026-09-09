"""Pure saved-array KFE mass-ledger arithmetic; no solver or model entry points."""

import math

import numpy as np
from scipy import sparse


EPS64 = np.finfo(np.float64).eps


def frozen_bound(left, right):
    left = np.asarray(left, dtype=float)
    right = np.asarray(right, dtype=float)
    return 128.0 * EPS64 * np.maximum(1.0, np.maximum(np.abs(left), np.abs(right)))


def frozen_close(left, right):
    left = np.asarray(left, dtype=float)
    right = np.asarray(right, dtype=float)
    return bool(np.all(np.abs(left - right) <= frozen_bound(left, right)))


def csr_storage_equal(left, right):
    left = sparse.csr_matrix(left)
    right = sparse.csr_matrix(right)
    return (
        left.shape == right.shape
        and np.array_equal(left.indptr, right.indptr)
        and np.array_equal(left.indices, right.indices)
        and np.array_equal(left.data, right.data)
    )


def require_transpose(operator, transpose):
    expected = sparse.csr_matrix(operator).transpose().tocsr()
    if not csr_storage_equal(expected, transpose):
        raise ValueError("stored transpose does not exactly equal Q.T in CSR storage")
    return True


def f_order_index(index, shape):
    n_b, n_a, n_z = map(int, shape)
    if index < 0 or index >= n_b * n_a * n_z:
        raise IndexError(index)
    i_b = index % n_b
    i_a = (index // n_b) % n_a
    i_z = index // (n_b * n_a)
    return i_b, i_a, i_z


def normalize_raw(raw, cell_weight):
    raw = np.asarray(raw, dtype=float)
    factor = float(np.sum(raw) * cell_weight)
    density = raw / factor
    probability = cell_weight * density
    return factor, density, probability


def verify_row_replacement(transpose, contaminated, rhs, row, pin_value=0.007):
    transpose = sparse.csr_matrix(transpose)
    contaminated = sparse.csr_matrix(contaminated)
    rhs = np.asarray(rhs, dtype=float)
    difference = (contaminated - transpose).tocsr()
    changed_rows = np.unique(difference.nonzero()[0])
    replacement = contaminated.getrow(row)
    valid = (
        np.array_equal(changed_rows, np.array([row]))
        and replacement.nnz == 1
        and replacement.indices[0] == row
        and replacement.data[0] == 1.0
        and np.array_equal(np.flatnonzero(rhs), np.array([row]))
        and rhs[row] == pin_value
    )
    if not valid:
        raise ValueError("B is not the exact stored one-row pin replacement of T")
    return {"changed_rows": changed_rows.tolist(), "difference_nnz": int(difference.nnz)}


def directional_omitted_rates(mu_b, mu_a, db, da):
    mu_b = np.asarray(mu_b, dtype=float)
    mu_a = np.asarray(mu_a, dtype=float)
    if mu_b.shape != mu_a.shape or mu_b.ndim != 3 or db <= 0 or da <= 0:
        raise ValueError("invalid saved drift shapes or spacings")
    rates = {name: np.zeros(mu_b.shape) for name in ("lower_b", "upper_b", "lower_a", "upper_a")}
    rates["lower_b"][0, :, :] = np.maximum(-mu_b[0, :, :], 0.0) / db
    rates["upper_b"][-1, :, :] = np.maximum(mu_b[-1, :, :], 0.0) / db
    rates["lower_a"][:, 0, :] = np.maximum(-mu_a[:, 0, :], 0.0) / da
    rates["upper_a"][:, -1, :] = np.maximum(mu_a[:, -1, :], 0.0) / da
    rates["total"] = sum(rates.values())
    return rates


def signed_parts(weights, values):
    weights = np.asarray(weights, dtype=float)
    values = np.asarray(values, dtype=float)
    return {
        "positive_probability": float(np.dot(values, np.maximum(weights, 0.0))),
        "negative_probability": float(np.dot(values, np.minimum(weights, 0.0))),
        "total": float(np.dot(values, weights)),
    }


def build_mass_balance(operator, density, cell_weight, omitted_rate, pin_row):
    operator = sparse.csr_matrix(operator)
    density = np.asarray(density, dtype=float)
    omitted_rate = np.asarray(omitted_rate, dtype=float)
    if operator.shape != (density.size, density.size) or omitted_rate.shape != density.shape:
        raise ValueError("operator, density and omitted rate shapes disagree")
    transpose = operator.transpose().tocsr()
    residual = np.asarray(transpose @ density)
    row_sum = np.asarray(operator @ np.ones(density.size))
    probability = cell_weight * density
    delta = row_sum + omitted_rate
    omega_sum_r = float(cell_weight * np.sum(residual))
    omega_fsum_r = float(cell_weight * math.fsum(map(float, residual)))
    q_dot_p = float(np.dot(row_sum, probability))
    escaped = float(np.dot(omitted_rate, probability))
    delta_term = float(np.dot(delta, probability))
    identity_rhs = float(-escaped + delta_term)
    off_pin = np.delete(residual, pin_row)
    candidate_source = float(-cell_weight * residual[pin_row])
    off_pin_correction = float(cell_weight * math.fsum(map(float, off_pin)))
    source_rhs = float(math.fsum([escaped, -delta_term, off_pin_correction]))
    residual_l1 = math.fsum(map(abs, residual))
    return {
        "residual": residual,
        "row_sum": row_sum,
        "delta": delta,
        "probability": probability,
        "omega_sum_r": omega_sum_r,
        "omega_fsum_r": omega_fsum_r,
        "q_dot_p": q_dot_p,
        "escaped_mass_flow": escaped,
        "delta_weighted_correction": delta_term,
        "mass_identity_rhs": identity_rhs,
        "mass_identity_abs_discrepancy": abs(omega_fsum_r - identity_rhs),
        "candidate_pin_source": candidate_source,
        "off_pin_signed_correction": off_pin_correction,
        "source_balance_rhs": source_rhs,
        "source_balance_abs_discrepancy": abs(candidate_source - source_rhs),
        "pin_residual": float(residual[pin_row]),
        "off_pin_abs_sum": float(math.fsum(map(abs, off_pin))),
        "pin_abs_share": float(abs(residual[pin_row]) / residual_l1) if residual_l1 else 0.0,
        "escaped_signed_parts": signed_parts(probability, omitted_rate),
        "row_sum_signed_parts": signed_parts(probability, row_sum),
        "delta_signed_parts": signed_parts(probability, delta),
    }
