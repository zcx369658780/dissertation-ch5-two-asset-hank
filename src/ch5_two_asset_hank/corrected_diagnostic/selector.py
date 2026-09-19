"""Minimum D1/D3 constrained selector for the preregistered real-cell panel.

The selector enumerates geometric face active sets and the three D3 transfer
subgradient regimes.  It has no optimizer, derivative floor, clipping, policy
cap, damping, or retry path.  Counted scalar roots are used only for a liquid
face active equality or an Owner-adopted strict-crossing zero-drift candidate.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
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
    max_interior_z_root_invocations: int | None = None
    max_interior_a_switching_root_invocations: int | None = None
    max_joint_switching_root_invocations: int | None = None
    selector_evaluations: int = 0
    root_invocations: int = 0
    interior_z_root_invocations: int = 0
    interior_a_switching_root_invocations: int = 0
    joint_switching_root_invocations: int = 0

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

    def begin_interior_z_root(self) -> int:
        ceiling = (
            self.max_root_invocations
            if self.max_interior_z_root_invocations is None
            else self.max_interior_z_root_invocations
        )
        if self.interior_z_root_invocations >= ceiling:
            raise RuntimeError("interior Z root invocation budget exhausted")
        ordinal = self.begin_root()
        self.interior_z_root_invocations += 1
        return ordinal

    def begin_interior_a_switching_root(self) -> int:
        ceiling = (
            self.max_root_invocations
            if self.max_interior_a_switching_root_invocations is None
            else self.max_interior_a_switching_root_invocations
        )
        if self.interior_a_switching_root_invocations >= ceiling:
            raise RuntimeError("interior a switching root invocation budget exhausted")
        ordinal = self.begin_root()
        self.interior_a_switching_root_invocations += 1
        return ordinal

    def begin_joint_switching_root(self) -> int:
        ceiling = (
            self.max_root_invocations
            if self.max_joint_switching_root_invocations is None
            else self.max_joint_switching_root_invocations
        )
        if self.joint_switching_root_invocations >= ceiling:
            raise RuntimeError("joint switching root invocation budget exhausted")
        ordinal = self.begin_root()
        self.joint_switching_root_invocations += 1
        return ordinal


@dataclass(frozen=True)
class ActiveEqualityReceipt:
    face: str
    raw_residual: float
    arithmetic_bound: float
    canonical_drift: float | None
    marker: str


@dataclass(frozen=True)
class LowerAZeroKinkMultiplierReceipt:
    raw_multiplier_interval_lower: float
    raw_kink_interval: tuple[float, float]
    deterministic_minimum: float
    upper_endpoint_arithmetic_bound: float
    intersection_nonempty: bool
    chosen_q_a: float | None
    lambda_a: float | None
    marker: str


@dataclass(frozen=True)
class InteriorZReceipt:
    endpoint_shadows: dict[str, float]
    endpoint_drifts: dict[str, float]
    endpoint_bounds: dict[str, float]
    root_bracket: tuple[float, float]
    root_method: str
    root_status: str
    raw_root_residual: float | None
    arithmetic_bound: float | None
    marker: str


@dataclass(frozen=True)
class InteriorASwitchingReceipt:
    endpoint_shadows: dict[str, float]
    endpoint_drifts: dict[str, float]
    endpoint_bounds: dict[str, float]
    strict_crossing: bool
    derivative_interval: tuple[float, float]
    d_z: float
    transfer_regime: str
    d3_ratio: float
    implied_q_b_interval: tuple[float, float]
    liquid_multiplier_domain: tuple[float | None, float | None]
    root_interval: tuple[float, float]
    root_endpoint_drifts: tuple[float, float]
    root_method: str
    root_status: str
    switching_shadows: dict[str, float] | None
    raw_switching_drifts: dict[str, float] | None
    marker: str


@dataclass(frozen=True)
class JointSwitchingReceipt:
    directional_derivatives: dict[str, float]
    liquid_z_receipts: dict[str, InteriorZReceipt]
    post_liquid_a_drifts: dict[str, float]
    post_liquid_a_bounds: dict[str, float]
    strict_crossing: bool
    d_zz: float
    transfer_regime: str
    d3_ratio: float
    liquid_derivative_interval: tuple[float, float]
    illiquid_derivative_interval: tuple[float, float]
    mapped_q_b_interval: tuple[float, float]
    root_interval: tuple[float, float]
    root_endpoint_drifts: tuple[float, float]
    root_method: str
    root_status: str
    switching_shadows: dict[str, float] | None
    raw_switching_drifts: dict[str, float] | None
    canonical_switching_drifts: dict[str, float] | None
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
    lower_a_zero_kink_multiplier_receipt: LowerAZeroKinkMultiplierReceipt | None = None
    interior_z_receipt: InteriorZReceipt | None = None
    interior_a_switching_receipt: InteriorASwitchingReceipt | None = None
    joint_switching_receipt: JointSwitchingReceipt | None = None


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
    interior_z_root_invocations: int = 0
    interior_a_switching_root_invocations: int = 0
    joint_switching_root_invocations: int = 0


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
    exact_interval: tuple[float, float] | None = None,
    interior_a_switching: bool = False,
    joint_switching: bool = False,
) -> tuple[float | None, str]:
    """Invoke one deterministic log-domain scalar-root procedure, without retry."""

    if interior_a_switching and joint_switching:
        raise ValueError("a scalar root cannot belong to two switching categories")
    if joint_switching:
        budget.begin_joint_switching_root()
    elif interior_a_switching:
        budget.begin_interior_a_switching_root()
    else:
        budget.begin_root()
    log_tiny = math.log(sys.float_info.min)
    log_huge = math.log(sys.float_info.max)
    if exact_interval is not None:
        lower, upper = (float(value) for value in exact_interval)
        if (
            not math.isfinite(lower)
            or not math.isfinite(upper)
            or lower <= 0.0
            or upper <= lower
        ):
            return None, "ROOT_FAILURE_INVALID_EXACT_INTERVAL"
        log_grid = np.linspace(math.log(lower), math.log(upper), 513)
    elif lower_b_face:
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


def _one_interior_z_root(
    function: Callable[[float], float],
    *,
    lower: float,
    upper: float,
    budget: SelectorBudget,
) -> tuple[float | None, str]:
    """Certify and solve one positive root inside the two derivative endpoints."""

    budget.begin_interior_z_root()
    if (
        not math.isfinite(lower)
        or not math.isfinite(upper)
        or lower <= 0.0
        or upper <= lower
    ):
        return None, "ROOT_FAILURE_INVALID_DERIVATIVE_INTERVAL"
    samples: list[tuple[float, float]] = []
    try:
        for log_q in np.linspace(math.log(lower), math.log(upper), 513):
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
            return None, "ROOT_FAILURE_NO_UNIQUE_BRACKET"
        root = exact[0]
        status = "ROOT_EXACT_GRID_POINT"
    else:
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
        status = "ROOT_CONVERGED"
    root = float(root)
    if not math.isfinite(root) or root <= 0.0:
        return None, "ROOT_FAILURE_NONFINITE_OR_NONPOSITIVE"
    if root < lower or root > upper:
        return None, "ROOT_FAILURE_OUTSIDE_DERIVATIVE_INTERVAL"
    return root, status


def _rejected(
    active: tuple[str, ...],
    regime: str,
    reasons: list[str],
    *,
    branches: dict[str, str] | None = None,
    root_invoked: bool = False,
    root_status: str = "NOT_REQUIRED",
    lower_a_zero_kink_multiplier_receipt: LowerAZeroKinkMultiplierReceipt | None = None,
    interior_z_receipt: InteriorZReceipt | None = None,
    interior_a_switching_receipt: InteriorASwitchingReceipt | None = None,
    joint_switching_receipt: JointSwitchingReceipt | None = None,
) -> SelectorCandidate:
    return SelectorCandidate(
        active_constraints=active,
        transfer_branch=regime,
        derivative_branches=branches or {},
        admissible=False,
        rejection_reasons=tuple(reasons),
        root_invoked=root_invoked,
        root_status=root_status,
        lower_a_zero_kink_multiplier_receipt=lower_a_zero_kink_multiplier_receipt,
        interior_z_receipt=interior_z_receipt,
        interior_a_switching_receipt=interior_a_switching_receipt,
        joint_switching_receipt=joint_switching_receipt,
    )


def active_lower_a_zero_kink_shadow(
    *, p_a: float, q_b: float, chi_0: float
) -> LowerAZeroKinkMultiplierReceipt:
    kink_lower = float(q_b * (1.0 - chi_0))
    kink_upper = float(q_b * (1.0 + chi_0))
    deterministic_minimum = float(max(p_a, kink_lower))
    bound = _fp_bound(
        p_a,
        q_b,
        chi_0,
        kink_lower,
        kink_upper,
        deterministic_minimum,
        operations=16,
    )
    nonempty = deterministic_minimum <= kink_upper + bound
    chosen = deterministic_minimum if nonempty else None
    multiplier = None if chosen is None else float(chosen - p_a)
    return LowerAZeroKinkMultiplierReceipt(
        raw_multiplier_interval_lower=float(p_a),
        raw_kink_interval=(kink_lower, kink_upper),
        deterministic_minimum=deterministic_minimum,
        upper_endpoint_arithmetic_bound=bound,
        intersection_nonempty=nonempty,
        chosen_q_a=chosen,
        lambda_a=multiplier,
        marker=(
            "ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_CANONICAL_MIN"
            if nonempty
            else "ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERVAL_EMPTY"
        ),
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
    *,
    q_b_override: float | None = None,
    interior_z_receipt: InteriorZReceipt | None = None,
    interior_a_switching_receipt: InteriorASwitchingReceipt | None = None,
    joint_switching_receipt: JointSwitchingReceipt | None = None,
    switching_d: float | None = None,
    switching_q_a_ratio: float | None = None,
    q_b_root_interval: tuple[float, float] | None = None,
) -> SelectorCandidate:
    branches = {"b": p_b_branch, "a": p_a_branch}
    b_face = faces.get("b")
    a_face = faces.get("a")
    b_active = b_face in active
    a_active = a_face in active
    if (
        interior_a_switching_receipt is not None
        and joint_switching_receipt is not None
    ):
        raise ValueError("one-axis and joint switching receipts are mutually exclusive")
    switching = (
        interior_a_switching_receipt is not None
        or joint_switching_receipt is not None
    )
    if switching != (switching_d is not None and switching_q_a_ratio is not None):
        raise ValueError("switching overrides must be supplied together")
    root_invoked = interior_z_receipt is not None or joint_switching_receipt is not None
    root_status = (
        joint_switching_receipt.root_status
        if joint_switching_receipt is not None
        else (
            interior_z_receipt.root_status
            if interior_z_receipt is not None
            else "NOT_REQUIRED"
        )
    )

    if switching:
        if a_active:
            raise ValueError("interior-a switching cannot be used at an a face")
        d = float(switching_d)
    elif a_active:
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
        if switching:
            q_a = float(switching_q_a_ratio) * q_b
        elif a_active:
            q_a = (
                p_a
                if regime == "zero_kink"
                else _transfer_ratio(d, cell.a, parameters) * q_b
            )
        else:
            q_a = p_a
        local_d = d if (a_active or switching) else _transfer_from_regime(
            regime=regime,
            q_a=q_a,
            q_b=q_b,
            a=cell.a,
            parameters=parameters,
        )
        g_b = _liquid_drift_for_root(q_b, local_d, cell, parameters)
        return q_a, local_d, g_b

    if q_b_override is not None:
        if b_active and not switching:
            raise ValueError("interior Z override cannot be used at an active liquid face")
        q_b = float(q_b_override)
    elif b_active:
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
            exact_interval=q_b_root_interval,
            interior_a_switching=switching,
        )
        if q_b is None:
            if interior_a_switching_receipt is not None:
                interior_a_switching_receipt = replace(
                    interior_a_switching_receipt,
                    root_status=root_status,
                )
            return _rejected(
                active,
                regime,
                [root_status],
                branches=branches,
                root_invoked=True,
                root_status=root_status,
                interior_a_switching_receipt=interior_a_switching_receipt,
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

    lower_a_zero_kink_receipt = None
    try:
        q_a, d, _ = values_for(q_b)
        if a_active and a_face == "lower_a" and regime == "zero_kink":
            lower_a_zero_kink_receipt = active_lower_a_zero_kink_shadow(
                p_a=p_a,
                q_b=q_b,
                chi_0=parameters.chi_0,
            )
            if not lower_a_zero_kink_receipt.intersection_nonempty:
                return _rejected(
                    active,
                    regime,
                    ["ACTIVE_LOWER_A_ZERO_KINK_MULTIPLIER_INTERSECTION_EMPTY"],
                    branches=branches,
                    root_invoked=root_invoked,
                    root_status=root_status,
                    lower_a_zero_kink_multiplier_receipt=lower_a_zero_kink_receipt,
                    interior_z_receipt=interior_z_receipt,
                )
            assert lower_a_zero_kink_receipt.chosen_q_a is not None
            q_a = lower_a_zero_kink_receipt.chosen_q_a
        c, l, cost, g_b, g_a, utility = _controls(q_b, d, cell, parameters)
    except (ArithmeticError, OverflowError, ValueError) as exc:
        return _rejected(
            active,
            regime,
            [f"CANDIDATE_ARITHMETIC_FAILURE:{type(exc).__name__}"],
            branches=branches,
            root_invoked=root_invoked,
            root_status=root_status,
            interior_z_receipt=interior_z_receipt,
            interior_a_switching_receipt=interior_a_switching_receipt,
            joint_switching_receipt=joint_switching_receipt,
        )
    tolerance = _fp_bound(
        c, l, d, cost, g_b, g_a, q_b, q_a, p_b, p_a, operations=96
    )
    raw_g_b = g_b
    raw_g_a = g_a
    if interior_a_switching_receipt is not None:
        switching_bound = _fp_bound(
            c,
            l,
            d,
            cost,
            raw_g_b,
            raw_g_a,
            q_b,
            q_a,
            operations=96,
        )
        if abs(raw_g_a) <= switching_bound:
            g_a = 0.0
        if b_active and abs(raw_g_b) <= switching_bound:
            g_b = 0.0
        interior_a_switching_receipt = replace(
            interior_a_switching_receipt,
            root_status=root_status,
            switching_shadows={"q_b": float(q_b), "q_a": float(q_a)},
            raw_switching_drifts={"g_b": float(raw_g_b), "g_a": float(raw_g_a)},
        )
    if joint_switching_receipt is not None:
        switching_bound = _fp_bound(
            c,
            l,
            d,
            cost,
            raw_g_b,
            raw_g_a,
            q_b,
            q_a,
            operations=96,
        )
        if abs(raw_g_b) <= switching_bound:
            g_b = 0.0
        if abs(raw_g_a) <= switching_bound:
            g_a = 0.0
        joint_switching_receipt = replace(
            joint_switching_receipt,
            switching_shadows={"q_b": float(q_b), "q_a": float(q_a)},
            raw_switching_drifts={"g_b": float(raw_g_b), "g_a": float(raw_g_a)},
            canonical_switching_drifts={"g_b": float(g_b), "g_a": float(g_a)},
        )
    if interior_z_receipt is not None:
        z_bound = _fp_bound(
            c,
            l,
            d,
            cost,
            raw_g_b,
            g_a,
            q_b,
            q_a,
            *interior_z_receipt.endpoint_shadows.values(),
            *interior_z_receipt.endpoint_drifts.values(),
            operations=96,
        )
        interior_z_receipt = replace(
            interior_z_receipt,
            raw_root_residual=float(raw_g_b),
            arithmetic_bound=z_bound,
        )
        if abs(raw_g_b) <= z_bound:
            g_b = 0.0
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
    if interior_a_switching_receipt is not None:
        lower_a_shadow, upper_a_shadow = interior_a_switching_receipt.derivative_interval
        if q_a < lower_a_shadow or q_a > upper_a_shadow:
            reasons.append("INTERIOR_A_SWITCHING_SHADOW_OUTSIDE_DERIVATIVE_INTERVAL")
        if abs(raw_g_a) > switching_bound:
            reasons.append("INTERIOR_A_SWITCHING_ZERO_DRIFT_RESIDUAL_BOUND_EXCEEDED")
        if b_active and abs(raw_g_b) > switching_bound:
            reasons.append("INTERIOR_A_SWITCHING_LIQUID_ROOT_RESIDUAL_BOUND_EXCEEDED")
    if joint_switching_receipt is not None:
        lower_b_shadow, upper_b_shadow = (
            joint_switching_receipt.liquid_derivative_interval
        )
        lower_a_shadow, upper_a_shadow = (
            joint_switching_receipt.illiquid_derivative_interval
        )
        if q_b < lower_b_shadow or q_b > upper_b_shadow:
            reasons.append("JOINT_SWITCHING_LIQUID_SHADOW_OUTSIDE_DERIVATIVE_INTERVAL")
        if q_a < lower_a_shadow or q_a > upper_a_shadow:
            reasons.append("JOINT_SWITCHING_ILLIQUID_SHADOW_OUTSIDE_DERIVATIVE_INTERVAL")
        if abs(raw_g_b) > switching_bound:
            reasons.append("JOINT_SWITCHING_LIQUID_ZERO_DRIFT_RESIDUAL_BOUND_EXCEEDED")
        if abs(raw_g_a) > switching_bound:
            reasons.append("JOINT_SWITCHING_ILLIQUID_ZERO_DRIFT_RESIDUAL_BOUND_EXCEEDED")
    if interior_z_receipt is not None and abs(raw_g_b) > float(
        interior_z_receipt.arithmetic_bound
    ):
        reasons.append("INTERIOR_Z_ROOT_RESIDUAL_BOUND_EXCEEDED")
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
    hamiltonian_b_shadow = q_b if switching else p_b
    hamiltonian_a_shadow = q_a if switching else p_a
    raw_hamiltonian = float(
        utility
        + hamiltonian_b_shadow * raw_g_b
        + hamiltonian_a_shadow * raw_g_a
    )
    hamiltonian = float(
        utility + hamiltonian_b_shadow * g_b + hamiltonian_a_shadow * g_a
    )
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
        lower_a_zero_kink_multiplier_receipt=lower_a_zero_kink_receipt,
        interior_z_receipt=interior_z_receipt,
        interior_a_switching_receipt=interior_a_switching_receipt,
        joint_switching_receipt=joint_switching_receipt,
    )


def _interior_z_candidate(
    cell: CorrectedSelectorCell,
    parameters: CorrectedSelectorParameters,
    faces: dict[str, str],
    active: tuple[str, ...],
    regime: str,
    p_a_branch: str,
    p_a: float,
    backward: SelectorCandidate,
    forward: SelectorCandidate,
    budget: SelectorBudget,
) -> SelectorCandidate | None:
    """Create one Z candidate only for a strict positive-shadow direction crossing."""

    if "b" in faces:
        return None
    p_backward = float(cell.derivatives.p_b_backward)
    p_forward = float(cell.derivatives.p_b_forward)
    if not all(math.isfinite(value) and value > 0.0 for value in (p_backward, p_forward)):
        return None
    if (
        backward.g_b is None
        or forward.g_b is None
        or backward.arithmetic_tolerance is None
        or forward.arithmetic_tolerance is None
    ):
        return None
    backward_drift = float(backward.g_b)
    forward_drift = float(forward.g_b)
    backward_bound = float(backward.arithmetic_tolerance)
    forward_bound = float(forward.arithmetic_tolerance)
    if not (
        backward_drift > backward_bound
        and forward_drift < -forward_bound
    ):
        return None

    a_face = faces.get("a")
    a_active = a_face in active
    if a_active:
        fixed_d = -cell.effective_r_a * cell.a
    else:
        fixed_d = 0.0

    def drift(q_b: float) -> float:
        if a_active:
            q_a = (
                p_a
                if regime == "zero_kink"
                else _transfer_ratio(fixed_d, cell.a, parameters) * q_b
            )
            local_d = fixed_d
        else:
            q_a = p_a
            local_d = _transfer_from_regime(
                regime=regime,
                q_a=q_a,
                q_b=q_b,
                a=cell.a,
                parameters=parameters,
            )
        return _liquid_drift_for_root(q_b, local_d, cell, parameters)

    lower, upper = sorted((p_backward, p_forward))
    root, status = _one_interior_z_root(
        drift,
        lower=lower,
        upper=upper,
        budget=budget,
    )
    receipt = InteriorZReceipt(
        endpoint_shadows={"backward": p_backward, "forward": p_forward},
        endpoint_drifts={
            "backward": backward_drift,
            "forward": forward_drift,
        },
        endpoint_bounds={
            "backward": backward_bound,
            "forward": forward_bound,
        },
        root_bracket=(lower, upper),
        root_method="BRENTQ_UNIQUE_LOG_SCREENED_BRACKET",
        root_status=status,
        raw_root_residual=None,
        arithmetic_bound=None,
        marker="INTERIOR_LIQUID_Z_ZERO_DRIFT_SWITCH",
    )
    if root is None:
        return _rejected(
            active,
            regime,
            [status],
            branches={"b": "zero", "a": p_a_branch},
            root_invoked=True,
            root_status=status,
            interior_z_receipt=receipt,
        )
    return _candidate(
        cell,
        parameters,
        faces,
        active,
        regime,
        "zero",
        root,
        p_a_branch,
        p_a,
        budget,
        q_b_override=root,
        interior_z_receipt=receipt,
    )


def _interior_a_switching_candidate(
    cell: CorrectedSelectorCell,
    parameters: CorrectedSelectorParameters,
    faces: dict[str, str],
    active: tuple[str, ...],
    regime: str,
    p_b_branch: str,
    p_b: float,
    backward: SelectorCandidate,
    forward: SelectorCandidate,
    budget: SelectorBudget,
) -> SelectorCandidate | None:
    """Create the Owner-adopted strict-crossing interior-a zero-drift candidate."""

    if "a" in faces:
        return None
    if (
        backward.g_a is None
        or forward.g_a is None
        or backward.arithmetic_tolerance is None
        or forward.arithmetic_tolerance is None
    ):
        return None
    backward_drift = float(backward.g_a)
    forward_drift = float(forward.g_a)
    backward_bound = float(backward.arithmetic_tolerance)
    forward_bound = float(forward.arithmetic_tolerance)
    if not (
        backward_drift > backward_bound
        and forward_drift < -forward_bound
    ):
        return None

    d_z = float(-cell.effective_r_a * cell.a)
    actual_regime = "positive" if d_z > 0.0 else "negative" if d_z < 0.0 else "zero_kink"
    if actual_regime != regime or d_z == 0.0:
        return None
    ratio = _transfer_ratio(d_z, cell.a, parameters)
    derivative_interval = tuple(
        sorted(
            (
                float(cell.derivatives.p_a_forward),
                float(cell.derivatives.p_a_backward),
            )
        )
    )
    if not math.isfinite(ratio) or ratio <= 0.0:
        return None
    implied_q_b_interval = (
        float(derivative_interval[0] / ratio),
        float(derivative_interval[1] / ratio),
    )
    if implied_q_b_interval[0] <= 0.0:
        return None

    b_face = faces.get("b")
    b_active = b_face in active
    if b_active and b_face == "lower_b":
        liquid_domain = (float(p_b), None)
        root_interval = (
            max(implied_q_b_interval[0], float(p_b)),
            implied_q_b_interval[1],
        )
    elif b_active and b_face == "upper_b":
        liquid_domain = (0.0, float(p_b))
        root_interval = (
            implied_q_b_interval[0],
            min(implied_q_b_interval[1], float(p_b)),
        )
    else:
        liquid_domain = (None, None)
        root_interval = implied_q_b_interval
    if root_interval[0] >= root_interval[1]:
        return None

    def liquid_drift(q_b: float) -> float:
        return _liquid_drift_for_root(q_b, d_z, cell, parameters)

    root_endpoint_drifts = (
        liquid_drift(root_interval[0]),
        liquid_drift(root_interval[1]),
    )
    receipt = InteriorASwitchingReceipt(
        endpoint_shadows={
            "backward": float(cell.derivatives.p_a_backward),
            "forward": float(cell.derivatives.p_a_forward),
        },
        endpoint_drifts={
            "backward": backward_drift,
            "forward": forward_drift,
        },
        endpoint_bounds={
            "backward": backward_bound,
            "forward": forward_bound,
        },
        strict_crossing=True,
        derivative_interval=derivative_interval,
        d_z=d_z,
        transfer_regime=actual_regime,
        d3_ratio=float(ratio),
        implied_q_b_interval=implied_q_b_interval,
        liquid_multiplier_domain=liquid_domain,
        root_interval=root_interval,
        root_endpoint_drifts=root_endpoint_drifts,
        root_method=(
            "BRENTQ_UNIQUE_LOG_SCREENED_EXACT_INTERVAL"
            if b_active
            else "NOT_REQUIRED"
        ),
        root_status="NOT_REQUIRED",
        switching_shadows=None,
        raw_switching_drifts=None,
        marker="INTERIOR_A_ZERO_DRIFT_STRICT_SWITCH",
    )
    return _candidate(
        cell,
        parameters,
        faces,
        active,
        regime,
        p_b_branch,
        p_b,
        "zero",
        derivative_interval[0],
        budget,
        interior_a_switching_receipt=receipt,
        switching_d=d_z,
        switching_q_a_ratio=ratio,
        q_b_root_interval=root_interval if b_active else None,
    )


def _joint_switching_candidate(
    cell: CorrectedSelectorCell,
    parameters: CorrectedSelectorParameters,
    faces: dict[str, str],
    active: tuple[str, ...],
    regime: str,
    backward: SelectorCandidate,
    forward: SelectorCandidate,
    budget: SelectorBudget,
) -> SelectorCandidate | None:
    """Create one simultaneous interior-interior zero-drift candidate."""

    if faces or active:
        return None
    for branch, candidate in (("backward", backward), ("forward", forward)):
        if (
            candidate.interior_z_receipt is None
            or candidate.derivative_branches != {"b": "zero", "a": branch}
            or candidate.transfer_branch != regime
            or candidate.root_status not in {"ROOT_CONVERGED", "ROOT_EXACT_GRID_POINT"}
            or candidate.g_b != 0.0
            or candidate.g_a is None
            or candidate.arithmetic_tolerance is None
            or candidate.transfer_kkt_residual is None
            or abs(float(candidate.transfer_kkt_residual))
            > float(candidate.arithmetic_tolerance)
            or candidate.rejection_reasons
            != ("A_DERIVATIVE_DIRECTION_INCONSISTENT",)
        ):
            return None

    backward_drift = float(backward.g_a)
    forward_drift = float(forward.g_a)
    backward_bound = float(backward.arithmetic_tolerance)
    forward_bound = float(forward.arithmetic_tolerance)
    if not (
        backward_drift > backward_bound
        and forward_drift < -forward_bound
    ):
        return None

    d_zz = float(-cell.effective_r_a * cell.a)
    actual_regime = (
        "positive" if d_zz > 0.0 else "negative" if d_zz < 0.0 else "zero_kink"
    )
    if d_zz == 0.0 or actual_regime != regime:
        return None
    ratio = _transfer_ratio(d_zz, cell.a, parameters)
    if not math.isfinite(ratio) or ratio <= 0.0:
        return None

    liquid_interval = tuple(
        sorted(
            (
                float(cell.derivatives.p_b_forward),
                float(cell.derivatives.p_b_backward),
            )
        )
    )
    illiquid_interval = tuple(
        sorted(
            (
                float(cell.derivatives.p_a_forward),
                float(cell.derivatives.p_a_backward),
            )
        )
    )
    if liquid_interval[0] <= 0.0:
        return None
    mapped_interval = (
        float(illiquid_interval[0] / ratio),
        float(illiquid_interval[1] / ratio),
    )
    root_interval = (
        max(liquid_interval[0], mapped_interval[0]),
        min(liquid_interval[1], mapped_interval[1]),
    )
    if (
        not all(math.isfinite(value) and value > 0.0 for value in root_interval)
        or root_interval[0] >= root_interval[1]
    ):
        return None

    def liquid_drift(q_b: float) -> float:
        return _liquid_drift_for_root(q_b, d_zz, cell, parameters)

    endpoint_drifts = (
        liquid_drift(root_interval[0]),
        liquid_drift(root_interval[1]),
    )
    root, status = _one_scalar_root(
        liquid_drift,
        lower_b_face=False,
        p_b=liquid_interval[0],
        budget=budget,
        exact_interval=root_interval,
        joint_switching=True,
    )
    receipt = JointSwitchingReceipt(
        directional_derivatives={
            "p_b_backward": float(cell.derivatives.p_b_backward),
            "p_b_forward": float(cell.derivatives.p_b_forward),
            "p_a_backward": float(cell.derivatives.p_a_backward),
            "p_a_forward": float(cell.derivatives.p_a_forward),
        },
        liquid_z_receipts={
            "backward": backward.interior_z_receipt,
            "forward": forward.interior_z_receipt,
        },
        post_liquid_a_drifts={
            "backward": backward_drift,
            "forward": forward_drift,
        },
        post_liquid_a_bounds={
            "backward": backward_bound,
            "forward": forward_bound,
        },
        strict_crossing=True,
        d_zz=d_zz,
        transfer_regime=actual_regime,
        d3_ratio=float(ratio),
        liquid_derivative_interval=liquid_interval,
        illiquid_derivative_interval=illiquid_interval,
        mapped_q_b_interval=mapped_interval,
        root_interval=root_interval,
        root_endpoint_drifts=endpoint_drifts,
        root_method="BRENTQ_UNIQUE_LOG_SCREENED_EXACT_INTERVAL",
        root_status=status,
        switching_shadows=None,
        raw_switching_drifts=None,
        canonical_switching_drifts=None,
        marker="SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_STRICT_SWITCH",
    )
    if root is None:
        return _rejected(
            active,
            regime,
            [status],
            branches={"b": "zero", "a": "zero"},
            root_invoked=True,
            root_status=status,
            joint_switching_receipt=receipt,
        )
    return _candidate(
        cell,
        parameters,
        faces,
        active,
        regime,
        "zero",
        liquid_interval[0],
        "zero",
        illiquid_interval[0],
        budget,
        q_b_override=root,
        joint_switching_receipt=receipt,
        switching_d=d_zz,
        switching_q_a_ratio=ratio,
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
    interior_z_root_start = budget.interior_z_root_invocations
    interior_a_root_start = budget.interior_a_switching_root_invocations
    joint_root_start = budget.joint_switching_root_invocations
    faces = _faces(cell)
    face_rows = list(faces.values())
    active_sets = [
        tuple(sorted(face for face, enabled in zip(face_rows, flags) if enabled))
        for flags in itertools.product((False, True), repeat=len(face_rows))
    ]
    candidates: list[SelectorCandidate] = []
    joint_contexts: list[
        tuple[
            dict[str, str],
            tuple[str, ...],
            str,
            SelectorCandidate,
            SelectorCandidate,
        ]
    ] = []
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

            # Upper-b liquid-active regimes retain their one-root fail-closed
            # rule.  Active lower-b negative transfer must instead represent
            # every a-direction that is viable on q_b >= p_b.
            if faces.get("b") in active and len(b_options) * len(a_options) > 1:
                viable_a: list[tuple[str, float]] = []
                for branch, value in a_options:
                    if regime == "positive" and branch == "forward" and value > 0.0:
                        viable_a.append((branch, value))
                    elif regime == "zero_kink" and value > 0.0:
                        viable_a.append((branch, value))
                    elif regime == "negative":
                        _, p_b_screen = b_options[0]
                        if faces["b"] == "lower_b":
                            lower = max(float(p_b_screen), sys.float_info.min)
                            log_grid = np.linspace(
                                math.log(lower), math.log(sys.float_info.max), 513
                            )
                        elif p_b_screen > 0.0:
                            log_grid = np.linspace(
                                math.log(sys.float_info.min), math.log(p_b_screen), 513
                            )
                        else:
                            log_grid = ()
                        for log_q in log_grid:
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
                lower_b_negative = faces["b"] == "lower_b" and regime == "negative"
                if not lower_b_negative and len(b_options) * len(a_options) != 1:
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
            ordinary_candidates: dict[tuple[str, str], SelectorCandidate] = {}
            liquid_z_candidates: dict[str, SelectorCandidate] = {}
            for p_a_branch, p_a in a_options:
                liquid_candidates: dict[str, SelectorCandidate] = {}
                for p_b_branch, p_b in b_options:
                    candidate = _candidate(
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
                    candidates.append(candidate)
                    liquid_candidates[p_b_branch] = candidate
                    ordinary_candidates[(p_b_branch, p_a_branch)] = candidate
                if "backward" in liquid_candidates and "forward" in liquid_candidates:
                    z_candidate = _interior_z_candidate(
                        cell,
                        parameters,
                        faces,
                        active,
                        regime,
                        p_a_branch,
                        p_a,
                        liquid_candidates["backward"],
                        liquid_candidates["forward"],
                        budget,
                    )
                    if z_candidate is not None:
                        candidates.append(z_candidate)
                        liquid_z_candidates[p_a_branch] = z_candidate
            for p_b_branch, p_b in b_options:
                backward = ordinary_candidates.get((p_b_branch, "backward"))
                forward = ordinary_candidates.get((p_b_branch, "forward"))
                if backward is None or forward is None:
                    continue
                a_switching_candidate = _interior_a_switching_candidate(
                    cell,
                    parameters,
                    faces,
                    active,
                    regime,
                    p_b_branch,
                    p_b,
                    backward,
                    forward,
                    budget,
                )
                if a_switching_candidate is not None:
                    candidates.append(a_switching_candidate)

            backward_z = liquid_z_candidates.get("backward")
            forward_z = liquid_z_candidates.get("forward")
            if backward_z is not None and forward_z is not None:
                joint_contexts.append(
                    (faces, active, regime, backward_z, forward_z)
                )

    # The coupled law is a final fallback: every ordinary and one-axis
    # candidate has already been evaluated, and no legal one-axis closure may
    # be bypassed by constructing a joint candidate.
    if not any(candidate.admissible for candidate in candidates):
        for faces, active, regime, backward_z, forward_z in joint_contexts:
            joint_candidate = _joint_switching_candidate(
                cell,
                parameters,
                faces,
                active,
                regime,
                backward_z,
                forward_z,
                budget,
            )
            if joint_candidate is not None:
                candidates.append(joint_candidate)

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
        interior_z_root_invocations=(
            budget.interior_z_root_invocations - interior_z_root_start
        ),
        interior_a_switching_root_invocations=(
            budget.interior_a_switching_root_invocations - interior_a_root_start
        ),
        joint_switching_root_invocations=(
            budget.joint_switching_root_invocations - joint_root_start
        ),
        selector_evaluation_ordinal=ordinal,
    )
