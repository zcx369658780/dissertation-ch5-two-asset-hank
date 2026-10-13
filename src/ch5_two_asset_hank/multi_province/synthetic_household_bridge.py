"""Explicit V0.0.1 synthetic-only assembly; no production or solver binding.

Household Lt is a reference passed as Lt_prev. Current destination labor is
reconstructed from Ct by the unchanged source-faithful migration component.
Neither a synthetic flag nor this composition is scientific convergence.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
import math
from types import MappingProxyType
from typing import Callable, Mapping, Sequence

import numpy as np

from . import corrected_household_adapter as adapter
from . import one_turn


SOURCE_KIND = "SYNTHETIC/NOT_REAL_SOURCE"
SHAPE = (20, 20, 2)
AXIS_ORDER = ("b", "a", "z")
FLATTEN_ORDER = "F"


def _stage(value: int) -> None:
    if type(value) is not int or value < 1:
        raise ValueError("synthetic iteration must be a positive integer")


@dataclass(frozen=True)
class SyntheticHouseholdRecord:
    """Detached, explicitly labelled simulated policy/mass output, not HA proof.

    Flat-to-cell indices accompany the arrays, so equal-sized b/a axes do not
    silently turn a declared C-order layout into an accepted F-order mapping.
    A same-shape transpose with truthful metadata remains a different input;
    only a known asymmetric oracle can expose its unintended interpretation.
    """

    province: str
    iteration: int
    source_id: str
    aggregate_inputs: adapter.CorrectedHouseholdAggregateInputs
    flat_indices_b_a_z: np.ndarray
    source_kind: str = SOURCE_KIND
    axis_order: tuple[str, str, str] = AXIS_ORDER
    flatten_order: str = FLATTEN_ORDER
    synthetic_converged: bool = False
    synthetic_convergence_statistic: float = 0.0

    def __post_init__(self) -> None:
        if self.source_kind != SOURCE_KIND:
            raise ValueError("only SYNTHETIC/NOT_REAL_SOURCE records are allowed")
        if not isinstance(self.province, str) or not self.province.startswith("SYNTH_") or len(self.province) <= 6:
            raise ValueError("province must be an explicit fictional SYNTH_ label")
        if not isinstance(self.source_id, str) or not self.source_id.strip():
            raise ValueError("synthetic source_id must be nonempty")
        _stage(self.iteration)
        if tuple(self.axis_order) != AXIS_ORDER or self.flatten_order != FLATTEN_ORDER:
            raise ValueError("synthetic arrays require (b,a,z) F-order")
        if not isinstance(self.synthetic_converged, (bool, np.bool_)):
            raise ValueError("synthetic convergence flag must be boolean")
        statistic = float(self.synthetic_convergence_statistic)
        if not math.isfinite(statistic) or statistic < 0:
            raise ValueError("synthetic statistic must be finite and nonnegative")
        if not isinstance(self.aggregate_inputs, adapter.CorrectedHouseholdAggregateInputs):
            raise ValueError("explicit corrected aggregate inputs are required")
        # The existing constructor independently copies every numerical input.
        inputs = replace(self.aggregate_inputs)
        if (inputs.consumption.shape != SHAPE
            or not np.array_equal(inputs.b_grid, np.linspace(-2, 5, 20))
            or not np.array_equal(inputs.a_grid, np.linspace(0, 10, 20))
            or not np.array_equal(inputs.z_grid, np.array([.8, 1.3]))
            or inputs.omega != 70/361):
            raise ValueError("synthetic fixture must retain the frozen 20x20x2 grid and omega")
        mass = inputs.probability_mass.ravel(order=FLATTEN_ORDER)
        if np.any(mass < 0) or abs(math.fsum(map(float, mass))-1) > mass.size*np.finfo(float).eps:
            raise ValueError("synthetic mass must be nonnegative and already unit mass; no normalization")
        indices = np.asarray(self.flat_indices_b_a_z)
        expected = np.column_stack(np.unravel_index(np.arange(800), SHAPE, order=FLATTEN_ORDER))
        if not np.issubdtype(indices.dtype, np.integer) or not np.array_equal(indices, expected):
            raise ValueError("flat indices must exactly match the integer F-order cell mapping")
        indices = np.array(indices, dtype=np.int64, copy=True)
        indices.flags.writeable = False
        object.__setattr__(self, "aggregate_inputs", inputs)
        object.__setattr__(self, "flat_indices_b_a_z", indices)
        object.__setattr__(self, "axis_order", AXIS_ORDER)
        object.__setattr__(self, "synthetic_converged", bool(self.synthetic_converged))
        object.__setattr__(self, "synthetic_convergence_statistic", statistic)


def _records(records: Sequence[SyntheticHouseholdRecord], order: tuple[str, ...], iteration: int) -> tuple[SyntheticHouseholdRecord, ...]:
    _stage(iteration)
    items = tuple(records)
    if len(order) not in (2, 3) or len(set(order)) != len(order) or len(items) != len(order):
        raise ValueError("synthetic batch requires exactly two or three unique, complete provinces")
    if any(not isinstance(r, SyntheticHouseholdRecord) for r in items):
        raise ValueError("synthetic records are required")
    if tuple(r.province for r in items) != order:
        raise ValueError("synthetic records must match declared province order; no reordering")
    if any(r.iteration != iteration or r.source_kind != SOURCE_KIND for r in items):
        raise ValueError("synthetic record source or stage mismatch")
    if len({r.source_id for r in items}) != len(items):
        raise ValueError("synthetic source identities must be unique")
    return items


def build_synthetic_household_batch(
    records: Sequence[SyntheticHouseholdRecord], *, province_order: Sequence[str], iteration: int,
) -> one_turn.PreFrozenHouseholdOutputBatch:
    """Real deterministic aggregate -> frozen -> batch, never a solver call."""
    items = _records(records, tuple(province_order), iteration)
    frozen = [adapter.evaluate_corrected_household_aggregates(r.aggregate_inputs).frozen_output(
        converged=r.synthetic_converged, convergence_statistic=r.synthetic_convergence_statistic,
    ) for r in items]
    return one_turn.PreFrozenHouseholdOutputBatch(
        ct=[r.Ct for r in frozen], household_lt=[r.Lt for r in frozen],
        at=[r.At for r in frozen], bt=[r.Bt for r in frozen], at_tax=[r.AtTax for r in frozen],
        converged=tuple(r.converged for r in frozen),
        diagnostics=tuple(dict(source_kind=SOURCE_KIND, source_id=r.source_id,
            province=r.province, iteration=iteration, axis_order=AXIS_ORDER, flatten_order=FLATTEN_ORDER,
            evidence_level="SYNTHETIC_ENGINEERING", convergence_evidence="SYNTHETIC_FLAG_NOT_HJB_B_D",
            synthetic_convergence_statistic=r.synthetic_convergence_statistic) for r in items),
    )


def make_synthetic_household_callback(
    records: Sequence[SyntheticHouseholdRecord], *, province_order: Sequence[str], iteration: int,
) -> Callable[[tuple[Mapping[str, object], ...], int], one_turn.PreFrozenHouseholdOutputBatch]:
    """One-use synthetic supplier with the existing HouseholdBatchSolver signature.

    No stationary controller is invoked or configured by this factory.
    """
    order = tuple(province_order)
    items = _records(records, order, iteration)
    used = False

    def callback(entering_states: tuple[Mapping[str, object], ...], requested_iteration: int) -> one_turn.PreFrozenHouseholdOutputBatch:
        nonlocal used
        _stage(requested_iteration)
        if used:
            raise ValueError("synthetic callback already used")
        if requested_iteration != iteration or len(entering_states) != len(items):
            raise ValueError("synthetic callback request stage or province count mismatch")
        for state, record in zip(entering_states, items):
            if (state.get("name") != record.province or state.get("source_kind") != SOURCE_KIND
                or type(state.get("synthetic_iteration")) is not int
                or state.get("synthetic_iteration") != iteration
                or state.get("synthetic_source_id") != record.source_id):
                raise ValueError("synthetic entering state identity/order/stage mismatch")
        used = True
        return build_synthetic_household_batch(items, province_order=order, iteration=iteration)

    return callback


def run_synthetic_bridge_once(
    records: Sequence[SyntheticHouseholdRecord], *, province_order: Sequence[str],
    entering_states: Sequence[Mapping[str, object]], iteration: int,
    params: Mapping[str, float], phi_destination_origin: np.ndarray,
    migration_wedge_destination_origin: np.ndarray,
) -> one_turn.OneTurnResult:
    """Exactly one explicitly opted-in synthetic callback and pure MP2 turn.

    This is not the K1B S/raw-ra0/C1 runner, a steady-state iteration, or a
    scientific acceptance of the source-faithful capital/firm arithmetic.
    """
    states = tuple(MappingProxyType(dict(state)) for state in entering_states)
    callback = make_synthetic_household_callback(records, province_order=province_order, iteration=iteration)
    batch = callback(states, iteration)
    return one_turn.run_source_faithful_one_turn(one_turn.OneTurnInputs(
        province_order=tuple(province_order), old_provinces=states, params=params,
        phi_destination_origin=phi_destination_origin,
        migration_wedge_destination_origin=migration_wedge_destination_origin,
        household_outputs=batch,
    ))
