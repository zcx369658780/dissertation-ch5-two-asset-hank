"""Frozen R4 synthetic steady-state validation fixture."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import sparse
from scipy.sparse import csgraph

from .contracts import EconomicParams, GridSpec, HJBResult, HouseholdInputs, PolicySnapshot
from .diagnostics import normalized_change
from .hjb import HJBNumerics, solve_hjb
from .indexing import inverse_index
from .kfe import KFEResult, solve_stationary_kfe
from .kfe_contract import make_kfe_input_from_operator


FIXTURE_ID = "R4_SYNTHETIC_ENDOGENOUS_A_CONNECTIVITY_V1"


class SteadyStateValidationError(RuntimeError):
    """Raised at the first failed frozen-fixture acceptance gate."""


@dataclass(frozen=True)
class R4SteadyStateDiagnostics:
    fixture_id: str
    primary_iterations: int
    buffer_iterations: int
    primary_hjb_residual: float
    buffer_hjb_residual: float
    primary_kkt_residual: float
    buffer_kkt_residual: float
    primary_generator_row_sum: float
    buffer_generator_row_sum: float
    value_core_change: float
    consumption_core_change: float
    transfer_core_change: float
    labor_core_change: float
    adjustment_cost_core_change: float
    mu_a_core_change: float
    upward_a_edges: int
    downward_a_edges: int
    closed_class_count: int
    closed_class_size: int
    closed_class_a_indices: tuple[int, ...]
    left_nullity: int
    stationarity_sup: float
    normalization_error: float
    minimum_mass: float
    negative_mass_count: int
    mass_density_error: float
    a_hh: float
    b_hh: float


@dataclass(frozen=True)
class R4SteadyStateResult:
    primary_grid: GridSpec
    primary_hjb: HJBResult
    buffer_grid: GridSpec
    buffer_hjb: HJBResult
    kfe: KFEResult
    diagnostics: R4SteadyStateDiagnostics


def _drift_classification(value: float) -> str:
    if value > 1e-12:
        return "F"
    if value < -1e-12:
        return "B"
    return "Z"


def _validate_common_core_policy_compatibility(
    primary: PolicySnapshot,
    buffer: PolicySnapshot,
    core_primary: np.ndarray,
    core_buffer: np.ndarray,
    a_values: np.ndarray,
    b_values: np.ndarray,
    z_values: np.ndarray,
) -> list[dict[str, object]]:
    """Fail closed on raw-ID mismatches except proven lower-b physical aliases."""
    required = (
        "raw_candidate_id", "qualifying_lower_b_alias_available",
        "effective_shadow_b", "alias_hamiltonian_gap", "alias_hamiltonian_bound",
    )
    if any(getattr(primary, name) is None or getattr(buffer, name) is None for name in required):
        raise SteadyStateValidationError("common-core policy compatibility audit evidence is absent")

    evidence: list[dict[str, object]] = []
    for i_a in range(primary.candidate_id.shape[0]):
        for i_b in range(primary.candidate_id.shape[1]):
            for p_z, b_z in zip(core_primary, core_buffer):
                left = (i_a, i_b, int(p_z))
                right = (i_a, i_b, int(b_z))
                raw_ids = (
                    str(primary.raw_candidate_id[left]),
                    str(buffer.raw_candidate_id[right]),
                )
                canonical_ids = (
                    str(primary.candidate_id[left]), str(buffer.candidate_id[right]),
                )
                state = (float(a_values[i_a]), float(b_values[i_b]), float(z_values[int(p_z)]))
                prefix = (
                    f"common-core policy mismatch at index={(i_a, i_b, int(p_z))}, "
                    f"state={state}, raw={raw_ids}, canonical={canonical_ids}: "
                )
                if canonical_ids[0] != canonical_ids[1]:
                    raise SteadyStateValidationError(prefix + "canonical IDs differ")
                drift_classes = (
                    _drift_classification(float(primary.mu_b[left])),
                    _drift_classification(float(buffer.mu_b[right])),
                )
                if drift_classes[0] != drift_classes[1]:
                    raise SteadyStateValidationError(
                        prefix + f"liquid-drift classifications differ: {drift_classes}"
                    )
                if primary.kkt_state_residual[left] > 1e-7 or buffer.kkt_state_residual[right] > 1e-7:
                    raise SteadyStateValidationError(prefix + "KKT state residual exceeds contract")
                if primary.boundary_violation > 1e-12 or buffer.boundary_violation > 1e-12:
                    raise SteadyStateValidationError(prefix + "boundary feasibility exceeds contract")
                if raw_ids[0] == raw_ids[1]:
                    continue
                alias_ids = (
                    len(raw_ids[0]) >= 2 and len(raw_ids[1]) >= 2
                    and raw_ids[0][0] == raw_ids[1][0]
                    and raw_ids[0][2:] == raw_ids[1][2:]
                    and {raw_ids[0][1], raw_ids[1][1]} == {"F", "Z"}
                )
                if i_b != 0 or not alias_ids:
                    raise SteadyStateValidationError(prefix + "raw IDs are outside lower-b F/Z alias scope")
                if not (
                    bool(primary.qualifying_lower_b_alias_available[left])
                    and bool(buffer.qualifying_lower_b_alias_available[right])
                ):
                    raise SteadyStateValidationError(prefix + "qualifying alias availability is absent")
                if canonical_ids[0][1] != "Z":
                    raise SteadyStateValidationError(prefix + "canonical IDs do not agree on Z")
                gaps = (
                    (float(primary.alias_hamiltonian_gap[left]), float(primary.alias_hamiltonian_bound[left])),
                    (float(buffer.alias_hamiltonian_gap[right]), float(buffer.alias_hamiltonian_bound[right])),
                )
                if any(not np.isfinite(pair).all() or pair[0] > pair[1] for pair in gaps):
                    raise SteadyStateValidationError(prefix + "Hamiltonian near-tie evidence fails")
                evidence.append({
                    "index": (i_a, i_b, int(p_z)), "state": state,
                    "raw_ids": raw_ids, "canonical_ids": canonical_ids,
                    "mu_b_classifications": drift_classes,
                    "hamiltonian_gap_bound": gaps,
                })
    return evidence


def _validate_common_core_normalized_changes(
    primary_value: np.ndarray,
    buffer_value: np.ndarray,
    primary_policy: PolicySnapshot,
    buffer_policy: PolicySnapshot,
    core_primary: np.ndarray,
    core_buffer: np.ndarray,
) -> dict[str, float]:
    changes = {
        "value": normalized_change(
            primary_value[:, :, core_primary], buffer_value[:, :, core_buffer],
        ),
        "consumption": normalized_change(
            primary_policy.consumption[:, :, core_primary],
            buffer_policy.consumption[:, :, core_buffer],
        ),
        "transfer": normalized_change(
            primary_policy.transfer[:, :, core_primary],
            buffer_policy.transfer[:, :, core_buffer],
        ),
        "labor": normalized_change(
            primary_policy.labor[:, :, core_primary, :],
            buffer_policy.labor[:, :, core_buffer, :],
        ),
        "adjustment_cost": normalized_change(
            primary_policy.adjustment_cost[:, :, core_primary],
            buffer_policy.adjustment_cost[:, :, core_buffer],
        ),
        "mu_a": normalized_change(
            primary_policy.mu_a[:, :, core_primary],
            buffer_policy.mu_a[:, :, core_buffer],
        ),
    }
    for name, change in changes.items():
        if change > 1e-3:
            raise SteadyStateValidationError(
                f"25-vs-29 common-core {name} truncation failed: {change}"
            )
    return changes


def _fixture_objects(z: np.ndarray) -> tuple[GridSpec, EconomicParams, HouseholdInputs, np.ndarray]:
    grid = GridSpec(
        np.array([0.0, 0.5, 1.0]),
        np.array([0.0, 2.5, 5.0]),
        np.asarray(z, dtype=float),
        0.0,
    )
    params = EconomicParams(0.05, 1.0, 1.0, 0.05, 1.0, 0.5, 0.2, 0.1)
    inputs = HouseholdInputs(
        0.04, 0.03, 0.0, np.array([1.0]), np.array([0.0]), np.array([1.0]),
    )
    productivity = grid.z[None, None, :]
    liquid_income = inputs.r_b * grid.b[None, :, None]
    consumption = 0.5 * (
        liquid_income + np.sqrt(liquid_income**2 + 4.0 * productivity**2)
    )
    labor = productivity / consumption
    initial = np.broadcast_to(
        (np.log(consumption) - 0.5 * labor**2) / params.rho, grid.shape,
    ).copy()
    return grid, params, inputs, initial


def _solve(z: np.ndarray) -> tuple[GridSpec, HJBResult]:
    grid, params, inputs, initial = _fixture_objects(z)
    result = solve_hjb(
        grid,
        params,
        inputs,
        initial,
        HJBNumerics(
            pseudo_time_step=10.0,
            max_iterations=500,
            change_tolerance=1e-8,
            residual_tolerance=1e-7,
            generator_tolerance=1e-11,
            drift_tolerance=1e-12,
            kkt_tolerance=1e-7,
        ),
    )
    return grid, result


def _trapezoidal_weights(grid: GridSpec) -> np.ndarray:
    axes = []
    for coordinates in (grid.a, grid.b, grid.z):
        spacing = float(coordinates[1] - coordinates[0])
        weights = np.full(coordinates.size, spacing)
        weights[[0, -1]] *= 0.5
        axes.append(weights)
    return axes[0][:, None, None] * axes[1][None, :, None] * axes[2][None, None, :]


def _closed_classes(generator: sparse.csr_matrix, tolerance: float) -> tuple[np.ndarray, ...]:
    adjacency = generator.copy().tocsr()
    adjacency.setdiag(0.0)
    adjacency.eliminate_zeros()
    if adjacency.nnz:
        adjacency.data = (adjacency.data > tolerance).astype(float)
        adjacency.eliminate_zeros()
    count, labels = csgraph.connected_components(
        adjacency, directed=True, connection="strong", return_labels=True,
    )
    closed = []
    for component in range(count):
        members = np.flatnonzero(labels == component)
        outward = generator[members][:, labels != component]
        if outward.nnz == 0 or float(np.max(outward.data)) <= tolerance:
            closed.append(members)
    return tuple(closed)


def _a_connectivity(grid: GridSpec, result: HJBResult) -> tuple[int, int]:
    tolerance = 1e-11
    g_a = result.operator.g_a.tocsr()
    upward = downward = 0
    for row in range(grid.size):
        i_a, i_b, i_z = inverse_index(row, grid.shape)
        drift = float(result.policy.mu_a[i_a, i_b, i_z])
        expected: dict[int, float] = {}
        if drift > 1e-12:
            if i_a == grid.a.size - 1:
                raise SteadyStateValidationError("positive illiquid drift exits the upper grid")
            col = row + 1
            expected[col] = drift / float(grid.a[i_a + 1] - grid.a[i_a])
            upward += 1
        elif drift < -1e-12:
            if i_a == 0:
                raise SteadyStateValidationError("negative illiquid drift exits the lower grid")
            col = row - 1
            expected[col] = -drift / float(grid.a[i_a] - grid.a[i_a - 1])
            downward += 1
        actual = {
            int(col): float(value)
            for col, value in zip(g_a.indices[g_a.indptr[row]:g_a.indptr[row + 1]],
                                  g_a.data[g_a.indptr[row]:g_a.indptr[row + 1]])
            if col != row and value > tolerance
        }
        if actual.keys() != expected.keys() or any(
            not np.isclose(actual[col], rate, rtol=1e-12, atol=1e-12)
            for col, rate in expected.items()
        ):
            raise SteadyStateValidationError("G_a rate is not the directional mu_a/h_a construction")
    if upward == 0 or downward == 0:
        raise SteadyStateValidationError(
            f"endogenous illiquid connectivity failed: upward={upward}, downward={downward}"
        )
    for component_name, component in (("G_b", result.operator.g_b), ("G_z", result.operator.g_z)):
        coo = component.tocoo()
        for row, col, value in zip(coo.row, coo.col, coo.data):
            if row != col and value > tolerance:
                if inverse_index(int(row), grid.shape)[0] != inverse_index(int(col), grid.shape)[0]:
                    raise SteadyStateValidationError(f"{component_name} contains a cross-a edge")
    return upward, downward


def run_frozen_r4_steady_state() -> R4SteadyStateResult:
    """Execute the pre-authorized R4 fixture without adaptive retries or tuning."""
    primary_grid, primary = _solve(np.arange(0.5, 2.0 + 1e-14, 0.0625))
    buffer_grid, buffer = _solve(np.arange(0.5, 2.25 + 1e-14, 0.0625))

    core_primary = np.flatnonzero((primary_grid.z >= 0.5) & (primary_grid.z <= 1.5))
    core_buffer = np.array([
        int(np.flatnonzero(np.isclose(buffer_grid.z, z))[0]) for z in primary_grid.z[core_primary]
    ])
    changes = _validate_common_core_normalized_changes(
        primary.value, buffer.value, primary.policy, buffer.policy,
        core_primary, core_buffer,
    )
    _validate_common_core_policy_compatibility(
        primary.policy, buffer.policy, core_primary, core_buffer,
        primary_grid.a, primary_grid.b, primary_grid.z,
    )

    upward, downward = _a_connectivity(primary_grid, primary)
    closed = _closed_classes(primary.operator.g, 1e-11)
    if len(closed) != 1:
        raise SteadyStateValidationError(f"expected one closed recurrent class, found {len(closed)}")
    recurrent = closed[0]
    recurrent_a = tuple(sorted({inverse_index(int(k), primary_grid.shape)[0] for k in recurrent}))
    if len(recurrent_a) < 2 or 1 not in recurrent_a or recurrent_a == (2,):
        raise SteadyStateValidationError(
            f"closed recurrent class has unacceptable illiquid support {recurrent_a}"
        )
    left_nullity = primary_grid.size - int(
        np.linalg.matrix_rank(primary.operator.g.toarray().T, tol=1e-11)
    )
    if left_nullity != 1:
        raise SteadyStateValidationError(f"generator left nullity is {left_nullity}, not one")

    weights = _trapezoidal_weights(primary_grid)
    kfe = solve_stationary_kfe(
        make_kfe_input_from_operator(primary.operator, primary_grid.shape, weights),
        primary_grid,
        generator_tolerance=1e-11,
        stationary_tolerance=1e-10,
        nonnegative_tolerance=1e-12,
    )
    mass_density_error = float(abs(np.sum(kfe.density * weights) - 1.0))
    if (not np.all(np.isfinite(kfe.density)) or mass_density_error > 1e-10):
        raise SteadyStateValidationError("mass/density accounting failed")

    diagnostics = R4SteadyStateDiagnostics(
        FIXTURE_ID, primary.iterations, buffer.iterations,
        primary.residual_sup, buffer.residual_sup,
        primary.policy.kkt_residual, buffer.policy.kkt_residual,
        primary.operator.max_row_sum, buffer.operator.max_row_sum,
        changes["value"], changes["consumption"], changes["transfer"],
        changes["labor"], changes["adjustment_cost"], changes["mu_a"],
        upward, downward,
        len(closed), int(recurrent.size), recurrent_a, left_nullity,
        kfe.diagnostics.stationarity_sup, kfe.diagnostics.normalization_error,
        kfe.diagnostics.minimum_mass, kfe.diagnostics.negative_mass_count,
        mass_density_error, kfe.a_hh, kfe.b_hh,
    )
    return R4SteadyStateResult(primary_grid, primary, buffer_grid, buffer, kfe, diagnostics)
