"""D2 conservative generator assembled only from consumed total drifts."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import sparse

from .boundary import StateConstraintAssessment, require_state_constraints
from .contracts import CorrectedDiagnosticGrid, checked_drift


@dataclass(frozen=True)
class CorrectedGenerator:
    q: sparse.csr_matrix
    asset_q: sparse.csr_matrix
    z_q: sparse.csr_matrix
    boundary: StateConstraintAssessment
    retained_outgoing: np.ndarray
    minimum_offdiagonal: float
    diagonal_construction_error: float
    max_abs_q_one: float
    arithmetic_tolerance: float
    max_abs_b_coordinate_error: float
    max_abs_a_coordinate_error: float


def _arithmetic_bound(q: sparse.csr_matrix) -> float:
    """Prospective operation-count row-sum bound, not fitted to evidence."""

    eps = np.finfo(float).eps
    terms = float(max(1, np.max(np.diff(q.indptr), initial=0)))
    gamma = terms * eps / (1.0 - terms * eps)
    absolute_row_sums = np.asarray(abs(q).sum(axis=1)).ravel()
    return float(gamma * max(1.0, float(np.max(absolute_row_sums, initial=0.0))))


def _validated_z_generator(
    values: np.ndarray | sparse.spmatrix | None, z_size: int
) -> sparse.csr_matrix:
    if values is None:
        return sparse.csr_matrix((z_size, z_size), dtype=float)
    q = sparse.csr_matrix(values, dtype=float)
    if q.shape != (z_size, z_size) or not np.all(np.isfinite(q.data)):
        raise ValueError("z_generator must be a finite square matrix matching z")
    offdiagonal = q - sparse.diags(q.diagonal(), format="csr")
    if offdiagonal.nnz and float(np.min(offdiagonal.data)) < 0.0:
        raise ValueError("z_generator offdiagonals must be nonnegative")
    outgoing = np.asarray(offdiagonal.sum(axis=1)).ravel()
    error = np.max(np.abs(q.diagonal() + outgoing), initial=0.0)
    if error > _arithmetic_bound(q):
        raise ValueError("z_generator diagonal must close retained transition rates")
    return q


def assemble_consumed_drift_generator(
    grid: CorrectedDiagnosticGrid,
    *,
    mu_b: np.ndarray,
    mu_a: np.ndarray,
    z_generator: np.ndarray | sparse.spmatrix | None = None,
) -> CorrectedGenerator:
    """Assemble the closed-box asset generator in accepted ``(b,a,z)`` order.

    Outward inputs are rejected before assembly. No drift is clipped and no
    exterior edge is silently deleted. Each retained rate is derived from the
    corresponding consumed total drift and the actual adjacent-node distance.
    """

    b_drift = checked_drift("mu_b", mu_b, grid.shape)
    a_drift = checked_drift("mu_a", mu_a, grid.shape)
    boundary = require_state_constraints(
        grid,
        mu_b=b_drift,
        mu_a=a_drift,
        tolerance=0.0,
    )

    rows: list[int] = []
    columns: list[int] = []
    data: list[float] = []
    outgoing = np.zeros(grid.size, dtype=float)
    for index in np.ndindex(grid.shape):
        row = int(np.ravel_multi_index(index, grid.shape, order="F"))
        for dimension, nodes, drift in (
            (0, grid.b, float(b_drift[index])),
            (1, grid.a, float(a_drift[index])),
        ):
            coordinate = index[dimension]
            neighbor = list(index)
            if drift > 0.0:
                neighbor[dimension] += 1
                distance = float(nodes[coordinate + 1] - nodes[coordinate])
                rate = drift / distance
            elif drift < 0.0:
                neighbor[dimension] -= 1
                distance = float(nodes[coordinate] - nodes[coordinate - 1])
                rate = -drift / distance
            else:
                continue
            if not np.isfinite(rate) or rate < 0.0:
                raise ValueError("consumed drift produced an invalid retained rate")
            column = int(np.ravel_multi_index(tuple(neighbor), grid.shape, order="F"))
            rows.append(row)
            columns.append(column)
            data.append(rate)
            outgoing[row] += rate

    for row, total in enumerate(outgoing):
        if total:
            rows.append(row)
            columns.append(row)
            data.append(-float(total))
    asset_q = sparse.coo_matrix(
        (data, (rows, columns)), shape=(grid.size, grid.size)
    ).tocsr()
    z_q = _validated_z_generator(z_generator, grid.z.size)
    asset_state_size = grid.b.size * grid.a.size
    lifted_z = sparse.kron(
        z_q, sparse.eye(asset_state_size, format="csr"), format="csr"
    )
    q = (asset_q + lifted_z).tocsr()
    z_offdiagonal = z_q - sparse.diags(z_q.diagonal(), format="csr")
    z_outgoing = np.asarray(z_offdiagonal.sum(axis=1)).ravel()
    total_outgoing = outgoing + np.repeat(z_outgoing, asset_state_size)

    diagonal_error = float(np.max(np.abs(q.diagonal() + total_outgoing), initial=0.0))
    q_one = np.asarray(q @ np.ones(grid.size)).ravel()
    offdiagonal = q - sparse.diags(q.diagonal(), format="csr")
    minimum_offdiagonal = float(np.min(offdiagonal.data)) if offdiagonal.nnz else 0.0
    b_coordinate = np.broadcast_to(grid.b[:, None, None], grid.shape).ravel(order="F")
    a_coordinate = np.broadcast_to(grid.a[None, :, None], grid.shape).ravel(order="F")
    b_error = np.asarray(q @ b_coordinate).ravel() - b_drift.ravel(order="F")
    a_error = np.asarray(q @ a_coordinate).ravel() - a_drift.ravel(order="F")
    return CorrectedGenerator(
        q=q,
        asset_q=asset_q,
        z_q=z_q,
        boundary=boundary,
        retained_outgoing=total_outgoing,
        minimum_offdiagonal=minimum_offdiagonal,
        diagonal_construction_error=diagonal_error,
        max_abs_q_one=float(np.max(np.abs(q_one), initial=0.0)),
        arithmetic_tolerance=_arithmetic_bound(q),
        max_abs_b_coordinate_error=float(np.max(np.abs(b_error), initial=0.0)),
        max_abs_a_coordinate_error=float(np.max(np.abs(a_error), initial=0.0)),
    )
