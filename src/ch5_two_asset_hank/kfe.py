"""Stationary forward operator and auditable probability-mass solution."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import sparse
from scipy.sparse import csgraph

from .contracts import GridSpec
from .indexing import flatten, unflatten
from .kfe_contract import KFEInput


@dataclass(frozen=True)
class KFEDiagnostics:
    stationarity_sup: float
    normalization_error: float
    minimum_mass: float
    negative_mass_count: int
    finite: bool
    mass_conservation_error: float
    strongly_connected_components: int
    closed_class_count: int
    closed_class_sizes: tuple[int, ...]
    unique_stationary: bool


@dataclass(frozen=True)
class KFEResult:
    mass: np.ndarray
    density: np.ndarray
    forward_operator: sparse.csr_matrix
    diagnostics: KFEDiagnostics
    a_hh: float
    b_hh: float


class KFEValidationError(RuntimeError):
    pass


def build_forward_operator(kfe_input: KFEInput) -> sparse.csr_matrix:
    """The KFE operator is exactly the transpose of the accepted backward G."""
    return kfe_input.generator.transpose().tocsr()


def _closed_classes(generator: sparse.csr_matrix, tolerance: float) -> tuple[int, tuple[np.ndarray, ...]]:
    adjacency = generator.copy().tocsr()
    adjacency.setdiag(0.0)
    adjacency.eliminate_zeros()
    if adjacency.nnz:
        adjacency.data = (adjacency.data > tolerance).astype(float)
        adjacency.eliminate_zeros()
    component_count, labels = csgraph.connected_components(
        adjacency, directed=True, connection="strong", return_labels=True,
    )
    closed: list[np.ndarray] = []
    for component in range(component_count):
        members = np.flatnonzero(labels == component)
        outside = labels != component
        if generator[members][:, outside].nnz == 0:
            closed.append(members)
            continue
        outward = generator[members][:, outside]
        if outward.nnz == 0 or float(np.max(outward.data)) <= tolerance:
            closed.append(members)
    return int(component_count), tuple(closed)


def solve_stationary_kfe(
    kfe_input: KFEInput,
    grid: GridSpec,
    *,
    generator_tolerance: float = 1e-11,
    stationary_tolerance: float = 1e-10,
    nonnegative_tolerance: float = 1e-12,
) -> KFEResult:
    if grid.shape != kfe_input.canonical_shape:
        raise ValueError("KFE input and grid must share the canonical shape")
    if min(generator_tolerance, stationary_tolerance, nonnegative_tolerance) <= 0.0:
        raise ValueError("KFE tolerances must be positive")

    generator = kfe_input.generator
    row_sums = np.asarray(generator.sum(axis=1)).ravel()
    mass_conservation_error = float(np.max(np.abs(row_sums)))
    diagonal = sparse.diags(generator.diagonal(), format="csr")
    off_diagonal = generator - diagonal
    minimum_off_diagonal = float(off_diagonal.data.min()) if off_diagonal.nnz else 0.0
    if mass_conservation_error > generator_tolerance:
        raise KFEValidationError("backward generator does not conserve probability mass")
    if minimum_off_diagonal < -generator_tolerance:
        raise KFEValidationError("backward generator has a negative off-diagonal rate")

    component_count, closed = _closed_classes(generator, generator_tolerance)
    closed_sizes = tuple(int(component.size) for component in closed)
    if len(closed) != 1:
        raise KFEValidationError(
            f"stationary distribution is not unique: found {len(closed)} closed classes "
            f"with sizes {closed_sizes}"
        )

    recurrent = closed[0]
    restricted = generator[recurrent][:, recurrent].toarray().T
    system = np.array(restricted, copy=True)
    rhs = np.zeros(recurrent.size)
    system[-1, :] = 1.0
    rhs[-1] = 1.0
    try:
        recurrent_mass = np.linalg.solve(system, rhs)
    except np.linalg.LinAlgError as exc:
        raise KFEValidationError("closed-class stationary system is singular") from exc

    mass_vector = np.zeros(generator.shape[0])
    mass_vector[recurrent] = recurrent_mass
    forward = build_forward_operator(kfe_input)
    residual = np.asarray(forward @ mass_vector)
    stationarity_sup = float(np.max(np.abs(residual)))
    normalization_error = float(abs(np.sum(mass_vector) - 1.0))
    minimum_mass = float(np.min(mass_vector))
    negative_count = int(np.count_nonzero(mass_vector < -nonnegative_tolerance))
    finite = bool(np.all(np.isfinite(mass_vector)))
    if (
        not finite
        or stationarity_sup > stationary_tolerance
        or normalization_error > stationary_tolerance
        or negative_count
    ):
        raise KFEValidationError(
            "stationary solution fails finiteness, residual, normalization, or non-negativity"
        )

    mass = unflatten(mass_vector, grid.shape)
    density = mass / kfe_input.cell_weights
    mass.flags.writeable = False
    density.flags.writeable = False
    a_values = np.broadcast_to(grid.a[:, None, None], grid.shape)
    b_values = np.broadcast_to(grid.b[None, :, None], grid.shape)
    a_hh = float(np.dot(flatten(a_values, grid.shape), mass_vector))
    b_hh = float(np.dot(flatten(b_values, grid.shape), mass_vector))
    diagnostics = KFEDiagnostics(
        stationarity_sup=stationarity_sup,
        normalization_error=normalization_error,
        minimum_mass=minimum_mass,
        negative_mass_count=negative_count,
        finite=finite,
        mass_conservation_error=mass_conservation_error,
        strongly_connected_components=component_count,
        closed_class_count=len(closed),
        closed_class_sizes=closed_sizes,
        unique_stationary=True,
    )
    return KFEResult(mass, density, forward, diagnostics, a_hh, b_hh)
