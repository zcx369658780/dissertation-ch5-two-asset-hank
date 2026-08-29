"""Monotone Markov-generator approximation of the frozen z diffusion."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import sparse

from .contracts import EconomicParams, GridSpec


@dataclass(frozen=True)
class ProductivityDiagnostics:
    n_z: int
    spacing: float
    max_row_sum: float
    min_off_diagonal: float
    constant_error: float
    affine_interior_error: float
    quadratic_interior_error: float
    quadratic_endpoint_error: float
    reflected_lower_quadratic_error: float
    left_nullity: int


def build_z_generator(grid: GridSpec, params: EconomicParams) -> sparse.csr_matrix:
    n_z = grid.z.size
    if n_z < 3:
        raise ValueError("the frozen productivity discretization requires N_z >= 3")
    dz = float(grid.z[1] - grid.z[0])
    diffusion = 0.5 * params.sigma_z**2
    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    for i, z in enumerate(grid.z):
        drift = -params.mu_z * z
        down = max(-drift, 0.0) / dz + diffusion / dz**2
        up = max(drift, 0.0) / dz + diffusion / dz**2
        if i == 0:
            down = 0.0
            # The fixed economic lower support is reflecting.  The regulator
            # cancels outward drift and the Neumann ghost-point diffusion row
            # gives G f(z_L) = 2D for f=(z-z_L)^2.
            up = 2.0 * diffusion / dz**2
        if i == n_z - 1:
            up = 0.0
        if down:
            rows.append(i); cols.append(i - 1); data.append(down)
        if up:
            rows.append(i); cols.append(i + 1); data.append(up)
        rows.append(i); cols.append(i); data.append(-(down + up))
    return sparse.csr_matrix((data, (rows, cols)), shape=(n_z, n_z))


def productivity_diagnostics(grid: GridSpec, params: EconomicParams, tolerance: float = 1e-11) -> ProductivityDiagnostics:
    generator = build_z_generator(grid, params)
    diagonal = sparse.diags(generator.diagonal(), format="csr")
    off_diagonal = generator - diagonal
    row_sum = float(np.max(np.abs(np.asarray(generator.sum(axis=1)).ravel())))
    min_off = float(off_diagonal.data.min()) if off_diagonal.nnz else 0.0
    z = grid.z
    beta = -params.mu_z * z
    diffusion = 0.5 * params.sigma_z**2
    constant_error = float(np.max(np.abs(generator @ np.ones(z.size))))
    affine_error = float(np.max(np.abs((generator @ z)[1:-1] - beta[1:-1])))
    expected_quadratic = 2.0 * beta * z + 2.0 * diffusion
    actual_quadratic = generator @ (z**2)
    quadratic_interior = float(np.max(np.abs(actual_quadratic[1:-1] - expected_quadratic[1:-1])))
    quadratic_endpoint = float(np.max(np.abs(actual_quadratic[[0, -1]] - expected_quadratic[[0, -1]])))
    reflected_test_function = (z - z[0]) ** 2
    reflected_lower_error = float(abs((generator @ reflected_test_function)[0] - 2.0 * diffusion))
    rank = np.linalg.matrix_rank(generator.toarray(), tol=tolerance)
    return ProductivityDiagnostics(
        z.size, float(z[1] - z[0]), row_sum, min_off, constant_error,
        affine_error, quadratic_interior, quadratic_endpoint, reflected_lower_error,
        int(z.size - rank),
    )


def refinement_diagnostics(params: EconomicParams) -> tuple[ProductivityDiagnostics, ...]:
    records = []
    for n_z in (5, 9, 17):
        grid = GridSpec(np.array([0.0, 1.0]), np.array([0.0, 1.0]), np.linspace(0.5, 1.5, n_z), 0.0)
        records.append(productivity_diagnostics(grid, params))
    return tuple(records)
