"""Minimum D1/D3 constrained selector for the preregistered real-cell panel.

The selector enumerates geometric face active sets and the three D3 transfer
subgradient regimes.  It has no optimizer, derivative floor, clipping, policy
cap, damping, or retry path.  A counted scalar root is used only when a liquid
face is hypothesized active.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import itertools
import math
import sys
from typing import Callable

import numpy as np
from scipy.optimize import brentq

from .cost import (
    check_transfer_kkt,
    regularized_adjustment_cost,
    regularized_scale,
)


TRANSFER_REGIMES = ("negative", "zero_kink", "positive")


def _fp_bound(*values: float, operations: int = 64) -> float:
    """Prospective gamma-n arithmetic bound, independent of panel outcomes."""

    eps = np.finfo(float).eps
    gamma = operations * eps / (1.0 - operations * eps)
    scale = max(1.0, sum(abs(float(value)) for value in values if math.isfinite(value)))
    return float(gamma * scale)


@dataclass(frozen=True)
class CellDerivatives:
    p_b_backward: float
    p_b_forward: float
    p_a_backward: float
    p_a_forward: float

    def __post_init__(self) -> None:
        if not all(math.isfinite(value) for value in self.__dict__.values()):
            raise ValueError("directional derivatives must be finite")


@dataclass(frozen=True)
class CorrectedSelectorParameters:
    gamma_c: float
    phi: float
    labor_weight: float
    chi_0: float
    chi_1: float
    a_bar: float

    def __post_init__(self) -> None:
        values = tuple(float(value) for value in self.__dict__.values())
        if not all(math.isfinite(value) for value in values):
            raise ValueError("selector parameters must be finite")
        if (
            self.gamma_c <= 0.0
            or self.phi <= 0.0
            or self.labor_weight <= 0.0
            or self.chi_0 < 0.0
            or self.chi_1 <= 0.0
            or self.a_bar <= 0.0
        ):
            raise ValueError("selector parameters are outside the frozen domain")


@dataclass(frozen=True)
class CorrectedSelectorCell:
    cell_id: str
    b: float
    a: float
    z: float
    b_lower: float
    b_upper: float
    a_lower: float
    a_upper: float
    net_wage: float
    effective_r_b: float
    transfer_income: float
    effective_r_a: float
    derivatives: CellDerivatives

    def __post_init__(self) -> None:
        scalar_names = (
            "b",
            "a",
            "z",
            "b_lower",
            "b_upper",
            "a_lower",
            "a_upper",
            "net_wage",
            "effective_r_b",
            "transfer_income",
            "effective_r_a",
        )
        if not all(math.isfinite(float(getattr(self, name))) for name in scalar_names):
            raise ValueError("selector cell inputs must be finite")
        if not self.cell_id:
            raise ValueError("selector cell_id must be non-empty")
        if not self.b_lower <= self.b <= self.b_upper:
            raise ValueError("liquid state lies outside the supplied box")
        if not self.a_lower <= self.a <= self.a_upper or self.a_lower != 0.0:
            raise ValueError("illiquid state violates the economic lower bound")
        if self.b_lower >= self.b_upper or self.a_lower >= self.a_upper:
            raise ValueError("selector box must be nondegenerate")
        if self.z <= 0.0 or self.net_wage <= 0.0:
            raise ValueError("productivity and net wage must be strictly positive")


@dataclass
class SelectorBudget:
    max_selector_evaluations: int
    max_root_invocations: int
    selector_evaluations: int = 0
    root_invocations: int = 0

    def begin_selector(self) -> int:
        if self.selector_evaluations >= self.max_selector_evaluations:
            raise RuntimeError("selector evaluation budget exhausted")
        self.selector_evaluations += 1
        return self.selector_evaluations

    def begin_root(self) -> int:
        if self.root_invocations >= self.max_root_invocations:
            raise RuntimeError("scalar root invocation budget exhausted")
        self.root_invocations += 1
        return self.root_invocations


@dataclass(frozen=True)
class ActiveEqualityReceipt:
    face: str
    raw_residual: float
    arithmetic_bound: float
    canonical_drift: float | None
    marker: str


@dataclass(frozen=True)
class SelectorCandidate:
    active_constraints: tuple[str, ...]
    transfer_branch: str
    derivative_branches: dict[str, str]
    admissible: bool
    rejection_reasons: tuple[str, ...]
    root_invoked: bool
    root_status: str
    c: float | None = None
    l: float | None = None
    d: float | None = None
    cost: float | None = None
    g_b: float | None = None
    g_a: float | None = None
    utility: float | None = None
    hamiltonian: float | None = None
    raw_hamiltonian: float | None = None
    q_b: float | None = None
    q_a: float | None = None
    slacks: dict[str, float] = field(default_factory=dict)
    multipliers: dict[str, float] = field(default_factory=dict)
    complementarity_residuals: dict[str, float] = field(default_factory=dict)
    transfer_kkt_residual: float | None = None
    transfer_target_interval: tuple[float, float] | None = None
    q_b_domain_ok: bool = False
    closed_face_feasible: bool = False
    d2_assembler_admissible: bool = False
    arithmetic_tolerance: float | None = None
    active_equality_receipts: dict[str, ActiveEqualityReceipt] = field(
        default_factory=dict
    )


@dataclass(frozen=True)
class SelectorResult:
    cell_id: str
    outcome: str
    selected: SelectorCandidate | None
    candidates: tuple[SelectorCandidate, ...]
    admissible_comparison_count: int
    face_active_set_count: int
    regime_attempt_count: int
    root_invocations: int
    selector_evaluation_ordinal: int


def _faces(cell: CorrectedSelectorCell) -> dict[str, str]:
    faces: dict[str, str] = {}
    if cell.b == cell.b_lower:
        faces["b"] = "lower_b"
    elif cell.b == cell.b_upper:
        faces["b"] = "upper_b"
    if cell.a == cell.a_lower:
        faces["a"] = "lower_a"
    elif cell.a == cell.a_upper:
        faces["a"] = "upper_a"
    return faces


def _face_sign(face: str) -> float:
    return 1.0 if face.startswith("lower") else -1.0


def _inward_derivative(cell: CorrectedSelectorCell, axis: str, face: str) -> tuple[str, float]:
    branch = "forward" if face.startswith("lower") else "backward"
    return branch, float(getattr(cell.derivatives, f"p_{axis}_{branch}"))


def _unique_derivatives(rows: list[tuple[str, float]]) -> list[tuple[str, float]]:
    result: list[tuple[str, float]] = []
    for row in rows:
        if not any(row[1] == existing[1] for existing in result):
            result.append(row)
    return result


def _interior_options(
    cell: CorrectedSelectorCell,
    axis: str,
    regime: str,
) -> list[tuple[str, float]]:
    backward = ("backward", float(getattr(cell.derivatives, f"p_{axis}_backward")))
    forward = ("forward", float(getattr(cell.derivatives, f"p_{axis}_forward")))
    if axis == "a":
        if regime == "positive":
            return [forward]
        if regime == "zero_kink":
            base = cell.effective_r_a * cell.a
            if base > 0.0:
                return [forward]
            if base < 0.0:
                return [backward]
    return [backward, forward]


def _transfer_from_regime(
    *,
    regime: str,
    q_a: float,
    q_b: float,
    a: float,
    parameters: CorrectedSelectorParameters,
) -> float:
    if regime == "zero_kink":
        return 0.0
    scale = regularized_scale(a, a_bar=parameters.a_bar)
    offset = 1.0 + parameters.chi_0 if regime == "positive" else 1.0 - parameters.chi_0
    return float(scale * (q_a / q_b - offset) / parameters.chi_1)


def _transfer_ratio(
    d: float, a: float, parameters: CorrectedSelectorParameters
) -> float:
    scale = regularized_scale(a, a_bar=parameters.a_bar)
    if d > 0.0:
        return float(1.0 + parameters.chi_0 + parameters.chi_1 * d / scale)
    if d < 0.0:
        return float(1.0 - parameters.chi_0 + parameters.chi_1 * d / scale)
    raise ValueError("zero transfer has an interval rather than a point ratio")


def _controls(
    q_b: float,
    d: float,
    cell: CorrectedSelectorCell,
    parameters: CorrectedSelectorParameters,
) -> tuple[float, float, float, float, float, float]:
    if not math.isfinite(q_b) or q_b <= 0.0:
        raise ValueError("q_b must be finite and strictly positive")
    c = float(q_b ** (-1.0 / parameters.gamma_c))
    l = float(
        (q_b * cell.net_wage / parameters.labor_weight) ** (1.0 / parameters.phi)
    )
    cost = regularized_adjustment_cost(
        d,
        cell.a,
        chi_0=parameters.chi_0,
        chi_1=parameters.chi_1,
        a_bar=parameters.a_bar,
    )
    g_b = float(
        cell.net_wage * l
        + cell.effective_r_b * cell.b
        + cell.transfer_income
        - c
        - d
        - cost
    )
    g_a = float(cell.effective_r_a * cell.a + d)
    if parameters.gamma_c == 1.0:
        consumption_utility = math.log(c)
    else:
        consumption_utility = c ** (1.0 - parameters.gamma_c) / (
            1.0 - parameters.gamma_c
        )
    utility = float(
        consumption_utility
        - parameters.labor_weight * l ** (1.0 + parameters.phi) / (1.0 + parameters.phi)
    )
    return c, l, cost, g_b, g_a, utility


def _liquid_drift_for_root(
    q_b: float,
    d: float,
    cell: CorrectedSelectorCell,
    parameters: CorrectedSelectorParameters,
) -> float:
    """Evaluate only the scalar liquid equality, avoiding unused utility powers."""

    if not math.isfinite(q_b) or q_b <= 0.0:
        raise ValueError("q_b must be finite and strictly positive")
    c = q_b ** (-1.0 / parameters.gamma_c)
    l = (q_b * cell.net_wage / parameters.labor_weight) ** (1.0 / parameters.phi)
    cost = regularized_adjustment_cost(
        d,
        cell.a,
        chi_0=parameters.chi_0,
        chi_1=parameters.chi_1,
        a_bar=parameters.a_bar,
    )
    return float(
        cell.net_wage * l
        + cell.effective_r_b * cell.b
        + cell.transfer_income
        - c
        - d
        - cost
    )


def _finite_root_value(value: float) -> float:
    if math.isnan(value):
        raise FloatingPointError("scalar root residual became NaN")
    if math.isinf(value):
        return math.copysign(sys.float_info.max, value)
    return float(value)


def _one_scalar_root(
    function: Callable[[float], float],
    *,
    lower_b_face: bool,
    p_b: float,
    budget: SelectorBudget,
) -> tuple[float | None, str]:
    """Invoke one deterministic log-domain scalar-root procedure, without retry."""

    budget.begin_root()
    log_tiny = math.log(sys.float_info.min)
    log_huge = math.log(sys.float_info.max)
    if lower_b_face:
        lower = max(float(p_b), sys.float_info.min)
        log_grid = np.linspace(math.log(lower), log_huge, 513)
    else:
        if p_b <= 0.0:
            return None, "INVALID_UPPER_FACE_QB_DOMAIN"
        log_grid = np.linspace(log_tiny, math.log(p_b), 513)
    samples: list[tuple[float, float]] = []
    try:
        for log_q in log_grid:
            q_b = math.exp(float(log_q))
            samples.append((q_b, _finite_root_value(function(q_b))))
    except (ArithmeticError, OverflowError, ValueError) as exc:
        return None, f"ROOT_FUNCTION_FAILURE:{type(exc).__name__}"
    exact = [q_b for q_b, value in samples if value == 0.0]
    brackets = [
        (left[0], right[0])
        for left, right in zip(samples[:-1], samples[1:])
        if (left[1] < 0.0 < right[1]) or (right[1] < 0.0 < left[1])
    ]
    if exact:
        if len(exact) != 1 or brackets:
            return None, "ROOT_FAILURE_MULTIPLE_BRACKETS"
        return exact[0], "ROOT_EXACT_GRID_POINT"
    if len(brackets) != 1:
        return None, "ROOT_FAILURE_NO_UNIQUE_BRACKET"
    try:
        root = brentq(
            function,
            brackets[0][0],
            brackets[0][1],
            xtol=np.nextafter(0.0, 1.0),
            rtol=4.0 * np.finfo(float).eps,
            maxiter=256,
        )
    except (ArithmeticError, RuntimeError, ValueError) as exc:
        return None, f"ROOT_FAILURE:{type(exc).__name__}"
    return float(root), "ROOT_CONVERGED"


def _rejected(
    active: tuple[str, ...],
    regime: str,
    reasons: list[str],
    *,
    branches: dict[str, str] | None = None,
    root_invoked: bool = False,
    root_status: str = "NOT_REQUIRED",
) -> SelectorCandidate:
    return SelectorCandidate(
        active_constraints=active,
        transfer_branch=regime,
        derivative_branches=branches or {},
        admissible=False,
        rejection_reasons=tuple(reasons),
        root_invoked=root_invoked,
        root_status=root_status,
    )


def _direction_ok(branch: str, drift: float, tolerance: float) -> bool:
    if drift > tolerance:
        return branch == "forward"
    if drift < -tolerance:
        return branch == "backward"
    return True


def _candidate(
    cell: CorrectedSelectorCell,
    parameters: CorrectedSelectorParameters,
    faces: dict[str, str],
    active: tuple[str, ...],
    regime: str,
    p_b_branch: str,
    p_b: float,
    p_a_branch: str,
    p_a: float,
    budget: SelectorBudget,
) -> SelectorCandidate:
    branches = {"b": p_b_branch, "a": p_a_branch}
    b_face = faces.get("b")
    a_face = faces.get("a")
    b_active = b_face in active
    a_active = a_face in active
    root_invoked = False
    root_status = "NOT_REQUIRED"

    if a_active:
        d = -cell.effective_r_a * cell.a
        if regime == "positive" and not d > 0.0:
            return _rejected(active, regime, ["ACTIVE_A_EQUALITY_WRONG_TRANSFER_SIGN"], branches=branches)
        if regime == "negative" and not d < 0.0:
            return _rejected(active, regime, ["ACTIVE_A_EQUALITY_WRONG_TRANSFER_SIGN"], branches=branches)
        if regime == "zero_kink" and d != 0.0:
            return _rejected(active, regime, ["ACTIVE_A_EQUALITY_NOT_ZERO_KINK"], branches=branches)
    else:
        d = 0.0

    def values_for(q_b: float) -> tuple[float, float, float]:
        if a_active:
            q_a = (
                p_a
                if regime == "zero_kink"
                else _transfer_ratio(d, cell.a, parameters) * q_b
            )
        else:
            q_a = p_a
        local_d = d if a_active else _transfer_from_regime(
            regime=regime,
            q_a=q_a,
            q_b=q_b,
            a=cell.a,
            parameters=parameters,
        )
        g_b = _liquid_drift_for_root(q_b, local_d, cell, parameters)
        return q_a, local_d, g_b

    if b_active:
        if b_face == "upper_b" and p_b <= 0.0:
            return _rejected(
                active,
                regime,
                ["UPPER_B_ACTIVE_HAS_NO_Q_B_POSITIVE_MULTIPLIER_DOMAIN"],
                branches=branches,
            )
        root_invoked = True
        q_b, root_status = _one_scalar_root(
            lambda value: values_for(value)[2],
            lower_b_face=b_face == "lower_b",
            p_b=p_b,
            budget=budget,
        )
        if q_b is None:
            return _rejected(
                active,
                regime,
                [root_status],
                branches=branches,
                root_invoked=True,
                root_status=root_status,
            )
    else:
        q_b = p_b
        if not math.isfinite(q_b) or q_b <= 0.0:
            return _rejected(
                active,
                regime,
                ["q_b_DOMAIN_INVALID_NO_DERIVATIVE_FLOOR"],
                branches=branches,
            )

    try:
        q_a, d, _ = values_for(q_b)
        c, l, cost, g_b, g_a, utility = _controls(q_b, d, cell, parameters)
    except (ArithmeticError, OverflowError, ValueError) as exc:
        return _rejected(
            active,
            regime,
            [f"CANDIDATE_ARITHMETIC_FAILURE:{type(exc).__name__}"],
            branches=branches,
            root_invoked=root_invoked,
            root_status=root_status,
        )
    tolerance = _fp_bound(
        c, l, d, cost, g_b, g_a, q_b, q_a, p_b, p_a, operations=96
    )
    raw_g_b = g_b
    raw_g_a = g_a
    active_equality_receipts: dict[str, ActiveEqualityReceipt] = {}
    for axis, face in faces.items():
        if face not in active:
            continue
        raw_residual = raw_g_b if axis == "b" else raw_g_a
        within_bound = abs(raw_residual) <= tolerance
        active_equality_receipts[face] = ActiveEqualityReceipt(
            face=face,
            raw_residual=float(raw_residual),
            arithmetic_bound=tolerance,
            canonical_drift=0.0 if within_bound else None,
            marker=(
                "ACTIVE_EQUALITY_CANONICAL_ZERO"
                if within_bound
                else "ACTIVE_EQUALITY_BOUND_EXCEEDED"
            ),
        )
        if within_bound:
            if axis == "b":
                g_b = 0.0
            else:
                g_a = 0.0
    reasons: list[str] = []
    if regime == "positive" and d <= tolerance:
        reasons.append("TRANSFER_SIGN_INCONSISTENT_POSITIVE")
    if regime == "negative" and d >= -tolerance:
        reasons.append("TRANSFER_SIGN_INCONSISTENT_NEGATIVE")
    if regime == "zero_kink" and d != 0.0:
        reasons.append("TRANSFER_NOT_ZERO_AT_KINK")

    slacks: dict[str, float] = {}
    multipliers: dict[str, float] = {}
    complementarity: dict[str, float] = {}
    for axis, face in faces.items():
        drift = g_b if axis == "b" else g_a
        shadow = q_b if axis == "b" else q_a
        derivative = p_b if axis == "b" else p_a
        slack = _face_sign(face) * drift
        multiplier = (shadow - derivative) / _face_sign(face) if face in active else 0.0
        residual = multiplier * slack
        slacks[face] = float(slack)
        multipliers[face] = float(multiplier)
        complementarity[face] = float(residual)
        if slack < -tolerance:
            reasons.append(f"{face}_PRIMAL_INFEASIBLE")
        if (
            face in active
            and abs(active_equality_receipts[face].raw_residual) > tolerance
        ):
            reasons.append(f"{face}_ACTIVE_EQUALITY_RESIDUAL")
        if multiplier < -tolerance:
            reasons.append(f"{face}_NEGATIVE_MULTIPLIER")
        if abs(residual) > _fp_bound(multiplier, slack, operations=8):
            reasons.append(f"{face}_COMPLEMENTARITY_RESIDUAL")

    if not _direction_ok(p_b_branch, g_b, tolerance):
        reasons.append("B_DERIVATIVE_DIRECTION_INCONSISTENT")
    if not _direction_ok(p_a_branch, g_a, tolerance):
        reasons.append("A_DERIVATIVE_DIRECTION_INCONSISTENT")
    try:
        transfer_kkt = check_transfer_kkt(
            d=d,
            a=cell.a,
            q_a=q_a,
            q_b=q_b,
            chi_0=parameters.chi_0,
            chi_1=parameters.chi_1,
            a_bar=parameters.a_bar,
            tolerance=tolerance,
        )
    except ValueError as exc:
        reasons.append(f"TRANSFER_KKT_DOMAIN:{exc}")
        transfer_kkt = None
    if transfer_kkt is not None and not transfer_kkt.satisfied:
        reasons.append("TRANSFER_KKT_RESIDUAL")
    raw_hamiltonian = float(utility + p_b * raw_g_b + p_a * raw_g_a)
    hamiltonian = float(utility + p_b * g_b + p_a * g_a)
    if not all(
        math.isfinite(value)
        for value in (
            c,
            l,
            d,
            cost,
            g_b,
            g_a,
            raw_g_b,
            raw_g_a,
            utility,
            hamiltonian,
            raw_hamiltonian,
            q_a,
        )
    ):
        reasons.append("NONFINITE_CANDIDATE")
    closed_face_feasible = all(value >= -tolerance for value in slacks.values())
    d2_closed_face_feasible = all(value >= 0.0 for value in slacks.values())
    admissible = not reasons
    return SelectorCandidate(
        active_constraints=active,
        transfer_branch=regime,
        derivative_branches=branches,
        admissible=admissible,
        rejection_reasons=tuple(reasons),
        root_invoked=root_invoked,
        root_status=root_status,
        c=c,
        l=l,
        d=d,
        cost=cost,
        g_b=g_b,
        g_a=g_a,
        utility=utility,
        hamiltonian=hamiltonian,
        raw_hamiltonian=raw_hamiltonian,
        q_b=q_b,
        q_a=q_a,
        slacks=slacks,
        multipliers=multipliers,
        complementarity_residuals=complementarity,
        transfer_kkt_residual=None if transfer_kkt is None else transfer_kkt.residual,
        transfer_target_interval=None if transfer_kkt is None else transfer_kkt.target_interval,
        q_b_domain_ok=q_b > 0.0,
        closed_face_feasible=closed_face_feasible,
        d2_assembler_admissible=(
            d2_closed_face_feasible and math.isfinite(g_b) and math.isfinite(g_a)
        ),
        arithmetic_tolerance=tolerance,
        active_equality_receipts=active_equality_receipts,
    )


def _same_policy(left: SelectorCandidate, right: SelectorCandidate) -> bool:
    values_left = (left.c, left.l, left.d, left.cost, left.g_b, left.g_a)
    values_right = (right.c, right.l, right.d, right.cost, right.g_b, right.g_a)
    assert all(value is not None for value in values_left + values_right)
    bound = _fp_bound(*(float(value) for value in values_left + values_right), operations=128)
    return all(abs(float(a) - float(b)) <= bound for a, b in zip(values_left, values_right))


def select_constrained_policy(
    cell: CorrectedSelectorCell,
    parameters: CorrectedSelectorParameters,
    *,
    budget: SelectorBudget,
) -> SelectorResult:
    """Evaluate one cell exactly once and return a fail-closed selection receipt."""

    ordinal = budget.begin_selector()
    root_start = budget.root_invocations
    faces = _faces(cell)
    face_rows = list(faces.values())
    active_sets = [
        tuple(sorted(face for face, enabled in zip(face_rows, flags) if enabled))
        for flags in itertools.product((False, True), repeat=len(face_rows))
    ]
    candidates: list[SelectorCandidate] = []
    for active in active_sets:
        for regime in TRANSFER_REGIMES:
            if "b" in faces:
                b_options = [_inward_derivative(cell, "b", faces["b"])]
            else:
                b_options = _interior_options(cell, "b", regime)
            if "a" in faces:
                a_options = [_inward_derivative(cell, "a", faces["a"])]
            else:
                a_options = _interior_options(cell, "a", regime)

            # A liquid-active regime is allowed one scalar-root invocation.  If
            # its derivative branch is not uniquely ruled in beforehand, fail
            # closed rather than spend a second root or choose by outcome.
            if faces.get("b") in active and len(b_options) * len(a_options) > 1:
                viable_a: list[tuple[str, float]] = []
                for branch, value in a_options:
                    if regime == "positive" and branch == "forward" and value > 0.0:
                        viable_a.append((branch, value))
                    elif regime == "zero_kink" and value > 0.0:
                        viable_a.append((branch, value))
                    elif regime == "negative":
                        # The panel's only interior-a cell has an upper-b root
                        # domain q in (0,p_b].  A 513-point prospective domain
                        # screen removes direction-inconsistent branches before
                        # any counted root invocation.
                        _, p_b_screen = b_options[0]
                        if p_b_screen > 0.0:
                            for log_q in np.linspace(
                                math.log(sys.float_info.min), math.log(p_b_screen), 513
                            ):
                                q_screen = math.exp(float(log_q))
                                d_screen = _transfer_from_regime(
                                    regime=regime,
                                    q_a=value,
                                    q_b=q_screen,
                                    a=cell.a,
                                    parameters=parameters,
                                )
                                g_a_screen = cell.effective_r_a * cell.a + d_screen
                                if d_screen < 0.0 and _direction_ok(
                                    branch,
                                    g_a_screen,
                                    _fp_bound(d_screen, g_a_screen),
                                ):
                                    viable_a.append((branch, value))
                                    break
                a_options = _unique_derivatives(viable_a)
                if len(b_options) * len(a_options) != 1:
                    candidates.append(
                        _rejected(
                            active,
                            regime,
                            ["DERIVATIVE_BRANCH_NOT_UNIQUE_BEFORE_ROOT"],
                        )
                    )
                    continue

            if not b_options or not a_options:
                candidates.append(
                    _rejected(active, regime, ["NO_DIRECTIONALLY_VALID_DERIVATIVE_BRANCH"])
                )
                continue
            for (p_b_branch, p_b), (p_a_branch, p_a) in itertools.product(
                b_options, a_options
            ):
                candidates.append(
                    _candidate(
                        cell,
                        parameters,
                        faces,
                        active,
                        regime,
                        p_b_branch,
                        p_b,
                        p_a_branch,
                        p_a,
                        budget,
                    )
                )

    admissible = [candidate for candidate in candidates if candidate.admissible]
    policies: list[SelectorCandidate] = []
    for candidate in admissible:
        if not any(_same_policy(candidate, existing) for existing in policies):
            policies.append(candidate)
    policies.sort(key=lambda candidate: float(candidate.hamiltonian), reverse=True)
    selected: SelectorCandidate | None = None
    if not policies:
        outcome = "NO_ADMISSIBLE_POLICY"
    elif len(policies) == 1:
        selected = policies[0]
        outcome = "SELECTED_ADMISSIBLE"
    else:
        comparison_tolerance = _fp_bound(
            float(policies[0].hamiltonian),
            float(policies[1].hamiltonian),
            operations=128,
        )
        if float(policies[0].hamiltonian) - float(policies[1].hamiltonian) <= comparison_tolerance:
            outcome = "NO_UNIQUE_ADMISSIBLE_POLICY"
        else:
            selected = policies[0]
            outcome = "SELECTED_ADMISSIBLE"
    return SelectorResult(
        cell_id=cell.cell_id,
        outcome=outcome,
        selected=selected,
        candidates=tuple(candidates),
        admissible_comparison_count=len(policies),
        face_active_set_count=len(active_sets),
        regime_attempt_count=len(active_sets) * len(TRANSFER_REGIMES),
        root_invocations=budget.root_invocations - root_start,
        selector_evaluation_ordinal=ordinal,
    )
