"""Single canonical backward generator shared with the future KFE interface."""

from __future__ import annotations

import numpy as np
from scipy import sparse

from .contracts import EconomicParams, GridSpec, OperatorBundle, PolicySnapshot
from .indexing import canonical_index
from .productivity import build_z_generator


def _asset_generator(grid: GridSpec, drift: np.ndarray, axis: int, tolerance: float) -> sparse.csr_matrix:
    shape = grid.shape
    coords = grid.a if axis == 0 else grid.b
    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    for index in np.ndindex(shape):
        i_a, i_b, i_z = index
        coordinate = index[axis]
        value = float(drift[index])
        row = canonical_index(i_a, i_b, i_z, shape)
        rate = 0.0
        neighbor = list(index)
        if value > tolerance:
            if coordinate == coords.size - 1:
                raise ValueError("outward positive drift at computational upper boundary")
            neighbor[axis] += 1
            rate = value / (coords[coordinate + 1] - coords[coordinate])
        elif value < -tolerance:
            if coordinate == 0:
                raise ValueError("outward negative drift at lower state boundary")
            neighbor[axis] -= 1
            rate = -value / (coords[coordinate] - coords[coordinate - 1])
        if rate:
            col = canonical_index(*neighbor, shape)
            rows.extend((row, row)); cols.extend((col, row)); data.extend((rate, -rate))
    return sparse.csr_matrix((data, (rows, cols)), shape=(grid.size, grid.size))


def build_operator(
    grid: GridSpec,
    params: EconomicParams,
    policy: PolicySnapshot,
    tolerance: float,
) -> OperatorBundle:
    g_a = _asset_generator(grid, policy.mu_a, 0, tolerance)
    g_b = _asset_generator(grid, policy.mu_b, 1, tolerance)
    z_small = build_z_generator(grid, params)
    g_z = sparse.kron(z_small, sparse.eye(grid.a.size * grid.b.size, format="csr"), format="csr")
    g = (g_a + g_b + g_z).tocsr()
    row_sums = np.asarray(g.sum(axis=1)).ravel()
    diagonal = sparse.diags(g.diagonal(), format="csr")
    off_diagonal = g - diagonal
    min_off = float(off_diagonal.data.min()) if off_diagonal.nnz else 0.0
    return OperatorBundle(g_a, g_b, g_z, g, float(np.max(np.abs(row_sums))), min_off)

