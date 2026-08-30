"""Exact source-spdiags placement for the distinct MATLAB-faithful HJB route."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import sparse


@dataclass(frozen=True)
class MatlabFaithfulOperator:
    bb: sparse.csr_matrix
    aah: sparse.csr_matrix
    bswitch: sparse.csr_matrix
    full: sparse.csr_matrix


def assemble_source_axis(
    backward: np.ndarray, forward: np.ndarray, axis: int
) -> sparse.csr_matrix:
    """Place signed source components, truncating outward entries but not their diagonal."""
    backward = np.asarray(backward, dtype=float)
    forward = np.asarray(forward, dtype=float)
    if backward.shape != forward.shape or backward.ndim != 3:
        raise ValueError("source axis components must share a three-dimensional shape")
    if axis not in (0, 1) or not np.isfinite(backward).all() or not np.isfinite(forward).all():
        raise ValueError("invalid source axis components")
    i_count, j_count, z_count = backward.shape
    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    for nz in range(z_count):
        for j in range(j_count):
            for i in range(i_count):
                row = i + j * i_count + nz * i_count * j_count
                rb = float(backward[i, j, nz])
                rf = float(forward[i, j, nz])
                if rb != 0.0 and ((axis == 0 and i > 0) or (axis == 1 and j > 0)):
                    rows.append(row); cols.append(row - (1 if axis == 0 else i_count)); data.append(rb)
                if rf != 0.0 and ((axis == 0 and i + 1 < i_count) or (axis == 1 and j + 1 < j_count)):
                    rows.append(row); cols.append(row + (1 if axis == 0 else i_count)); data.append(rf)
                rows.append(row); cols.append(row); data.append(-(rb + rf))
    size = i_count * j_count * z_count
    return sparse.coo_matrix((data, (rows, cols)), shape=(size, size)).tocsr()


def assemble_source_operator(
    b_backward: np.ndarray,
    b_forward: np.ndarray,
    a_backward: np.ndarray,
    a_forward: np.ndarray,
    switch_matrix: np.ndarray,
) -> MatlabFaithfulOperator:
    bb = assemble_source_axis(b_backward, b_forward, 0)
    aah = assemble_source_axis(a_backward, a_forward, 1)
    state_size = int(np.prod(b_backward.shape[:2]))
    bswitch = sparse.kron(sparse.csr_matrix(switch_matrix), sparse.eye(state_size), format="csr")
    return MatlabFaithfulOperator(bb, aah, bswitch, (bb + aah + bswitch).tocsr())
