"""D1 joint face/corner state-constraint checks with no silent repair."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .contracts import CorrectedDiagnosticGrid, checked_drift


@dataclass(frozen=True)
class BoundaryViolation:
    axis: str
    side: str
    index: tuple[int, int, int]
    drift: float
    outward_amount: float
    boundary_kind: str


@dataclass(frozen=True)
class FaceSummary:
    axis: str
    side: str
    boundary_kind: str
    inward_count: int
    tangent_count: int
    outward_count: int
    max_outward: float


@dataclass(frozen=True)
class StateConstraintAssessment:
    violations: tuple[BoundaryViolation, ...]
    faces: tuple[FaceSummary, ...]

    @property
    def feasible(self) -> bool:
        return not self.violations


class ClosedFaceOutwardDriftError(ValueError):
    def __init__(self, assessment: StateConstraintAssessment) -> None:
        self.assessment = assessment
        first = assessment.violations[0]
        super().__init__(
            "outward consumed drift at closed "
            f"{first.side}-{first.axis} face index={first.index}: {first.drift}"
        )


def _face(
    *,
    drift: np.ndarray,
    axis: str,
    dimension: int,
    side: str,
    tolerance: float,
) -> tuple[list[BoundaryViolation], FaceSummary]:
    coordinate = 0 if side == "lower" else drift.shape[dimension] - 1
    selector: list[object] = [slice(None)] * 3
    selector[dimension] = coordinate
    values = np.asarray(drift[tuple(selector)])
    inward_signed = values if side == "lower" else -values
    outward_mask = inward_signed < -tolerance
    tangent_mask = np.abs(values) <= tolerance
    inward_mask = inward_signed > tolerance
    kind = "economic_lower_bound" if side == "lower" else "artificial_upper_state_constraint"
    violations: list[BoundaryViolation] = []
    for local in np.argwhere(outward_mask):
        full = list(map(int, local))
        full.insert(dimension, coordinate)
        index = tuple(full)
        value = float(drift[index])
        violations.append(
            BoundaryViolation(axis, side, index, value, abs(value), kind)
        )
    summary = FaceSummary(
        axis=axis,
        side=side,
        boundary_kind=kind,
        inward_count=int(np.count_nonzero(inward_mask)),
        tangent_count=int(np.count_nonzero(tangent_mask)),
        outward_count=int(np.count_nonzero(outward_mask)),
        max_outward=float(np.max(np.maximum(-inward_signed, 0.0))),
    )
    return violations, summary


def assess_state_constraints(
    grid: CorrectedDiagnosticGrid,
    *,
    mu_b: np.ndarray,
    mu_a: np.ndarray,
    tolerance: float = 0.0,
) -> StateConstraintAssessment:
    """Assess all lower economic and upper numerical faces jointly."""

    if not np.isfinite(tolerance) or tolerance < 0.0:
        raise ValueError("tolerance must be finite and non-negative")
    b_drift = checked_drift("mu_b", mu_b, grid.shape)
    a_drift = checked_drift("mu_a", mu_a, grid.shape)
    violations: list[BoundaryViolation] = []
    summaries: list[FaceSummary] = []
    for drift, axis, dimension in ((b_drift, "b", 0), (a_drift, "a", 1)):
        for side in ("lower", "upper"):
            found, summary = _face(
                drift=drift,
                axis=axis,
                dimension=dimension,
                side=side,
                tolerance=tolerance,
            )
            violations.extend(found)
            summaries.append(summary)
    return StateConstraintAssessment(tuple(violations), tuple(summaries))


def require_state_constraints(
    grid: CorrectedDiagnosticGrid,
    *,
    mu_b: np.ndarray,
    mu_a: np.ndarray,
    tolerance: float = 0.0,
) -> StateConstraintAssessment:
    assessment = assess_state_constraints(
        grid, mu_b=mu_b, mu_a=mu_a, tolerance=tolerance
    )
    if not assessment.feasible:
        raise ClosedFaceOutwardDriftError(assessment)
    return assessment
