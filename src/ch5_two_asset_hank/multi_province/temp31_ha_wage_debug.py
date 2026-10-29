"""Unwired TEMP31 wage provenance guard and proposed consumer algebra.

Only synthetic formula witnesses are supported. This is not a household
solver, a production provenance certificate, or an initial-wage adoption.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isclose, isfinite

from .temp31_worksite_tax import (
    NET_COMPOSITE, Temp31NetWageViews, adapt_temp31_net_composite_wage,
)

INITIAL_DEFAULT_UNPROVEN = "INITIAL_DEFAULT_UNPROVEN"
CALCULATED_NET_AFTER_DESTINATION_TAU_AND_SIGMA = "CALCULATED_NET_AFTER_DESTINATION_TAU_AND_SIGMA"
SOURCE_COMMIT = "92ec73bc4fabfdf92a9f34c3715ebbdd4fb51f27"
WAGE_FORMULA_BLOB = "48001b2e4ca64d81dda6174255f6ccf130e07004"
Vector = tuple[float, ...]
Matrix = tuple[Vector, ...]


def _vector(name: str, values: object, n: int | None = None) -> Vector:
    try:
        result = tuple(float(x) for x in values)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} requires a finite vector") from exc
    if len(result) < 2 or (n is not None and len(result) != n) or not all(map(isfinite, result)):
        raise ValueError(f"{name} has invalid length or non-finite data")
    return result


def _matrix(name: str, values: object, n: int) -> Matrix:
    try:
        rows = tuple(_vector(name, row, n) for row in values)
    except TypeError as exc:
        raise ValueError(f"{name} requires destination rows/origin columns") from exc
    if len(rows) != n:
        raise ValueError(f"{name} must be square")
    return rows


def _order(values: object, n: int) -> tuple[str, ...]:
    result = tuple(values)
    if len(result) != n or any(not isinstance(x, str) or not x for x in result) or len(set(result)) != n:
        raise ValueError("province order must contain unique nonempty labels")
    return result


def _iteration(value: int) -> None:
    if type(value) is not int or value < 1:
        raise ValueError("iteration must be a positive integer")


@dataclass(frozen=True)
class SyntheticNetWageCalculation:
    """Complete immutable inputs, not a trusted label on an arbitrary wage."""
    firm_wages_by_destination: Vector
    tax_by_destination: Vector
    phi_destination_origin: Matrix
    sigma_destination_origin: Matrix
    phi_l: float
    alphal: float
    province_order: tuple[str, ...]
    context_id: str
    generated_after_iteration: int
    source_commit: str = SOURCE_COMMIT
    formula_git_blob: str = WAGE_FORMULA_BLOB
    evidence_scope: str = "SYNTHETIC_FORMULA_RECOMPUTATION_ONLY"

    def __post_init__(self) -> None:
        wages = _vector("firm_wages_by_destination", self.firm_wages_by_destination)
        n = len(wages)
        taxes = _vector("tax_by_destination", self.tax_by_destination, n)
        phi = _matrix("phi_destination_origin", self.phi_destination_origin, n)
        sigma = _matrix("sigma_destination_origin", self.sigma_destination_origin, n)
        order = _order(self.province_order, n)
        elasticity, alphal = float(self.phi_l), float(self.alphal)
        if any(w < 0 for w in wages) or any(x <= 0 for row in phi for x in row):
            raise ValueError("wages must be nonnegative and phi positive")
        if not all(map(isfinite, (elasticity, alphal))) or elasticity <= 0 or alphal <= 0:
            raise ValueError("phi_l and alphal must be positive and finite")
        if not isinstance(self.context_id, str) or not self.context_id:
            raise ValueError("context_id is required")
        _iteration(self.generated_after_iteration)
        for name, value in (("firm_wages_by_destination", wages), ("tax_by_destination", taxes),
                            ("phi_destination_origin", phi), ("sigma_destination_origin", sigma),
                            ("province_order", order), ("phi_l", elasticity), ("alphal", alphal)):
            object.__setattr__(self, name, value)


def recompute_synthetic_net_wage(calculation: SyntheticNetWageCalculation) -> Vector:
    """Independent pure-Python transcription of pinned wage.py lines 52-76."""
    if (calculation.source_commit != SOURCE_COMMIT or calculation.formula_git_blob != WAGE_FORMULA_BLOB
            or calculation.evidence_scope != "SYNTHETIC_FORMULA_RECOMPUTATION_ONLY"):
        raise ValueError("fixed formula identity/synthetic scope does not match")
    exponent = 1 + 1 / calculation.phi_l
    outer = calculation.phi_l / (1 + calculation.phi_l)
    output = []
    try:
        for origin in range(len(calculation.firm_wages_by_destination)):
            total = 0.0
            for destination, wage in enumerate(calculation.firm_wages_by_destination):
                divisor = calculation.phi_destination_origin[destination][origin]
                base = (wage * (1 - calculation.tax_by_destination[destination]
                        - calculation.sigma_destination_origin[destination][origin]) / divisor)
                if not isfinite(base) or base < 0:
                    raise ValueError("net wage power base must be nonnegative and finite")
                term = divisor * base ** exponent
                if not isfinite(term):
                    raise ValueError("net wage term is not finite")
                total += term
            value = calculation.alphal ** (-outer) * total ** outer
            if not isfinite(value) or value < 0:
                raise ValueError("net composite wage is not finite/nonnegative")
            output.append(value)
    except OverflowError as exc:
        raise ValueError("synthetic net wage overflow") from exc
    return tuple(output)


@dataclass(frozen=True)
class WageRoundRecord:
    entering_iteration: int
    provenance: str
    wage_by_origin: Vector
    province_order: tuple[str, ...]
    context_id: str
    calculation: SyntheticNetWageCalculation | None = None

    def __post_init__(self) -> None:
        _iteration(self.entering_iteration)
        wages = _vector("wage_by_origin", self.wage_by_origin)
        if any(w < 0 for w in wages) or not isinstance(self.context_id, str) or not self.context_id:
            raise ValueError("finite nonnegative wages and a context are required")
        object.__setattr__(self, "wage_by_origin", wages)
        object.__setattr__(self, "province_order", _order(self.province_order, len(wages)))


class WageProvenanceBlocked(ValueError):
    def __init__(self, record: WageRoundRecord, reason: str):
        self.diagnostics = {"reason": reason, "entering_iteration": record.entering_iteration,
                            "provenance": record.provenance, "observed_wage_by_origin": record.wage_by_origin,
                            "context_id": record.context_id, "source_reclassified": False}
        super().__init__(reason)


@dataclass(frozen=True)
class ProposedConsumers:
    record: WageRoundRecord
    views: Temp31NetWageViews
    scope: str = "SYNTHETIC_PROPOSED_CONSUMERS_ONLY__NO_REAL_HA"


def calculated_round_record(calculation: SyntheticNetWageCalculation, entering_iteration: int) -> WageRoundRecord:
    return WageRoundRecord(entering_iteration, CALCULATED_NET_AFTER_DESTINATION_TAU_AND_SIGMA,
                           recompute_synthetic_net_wage(calculation), calculation.province_order,
                           calculation.context_id, calculation)


def prepare_proposed_consumers(record: WageRoundRecord) -> ProposedConsumers:
    """Fail closed before the R4 adapter; no first-round policy is adopted."""
    if record.provenance != CALCULATED_NET_AFTER_DESTINATION_TAU_AND_SIGMA:
        raise WageProvenanceBlocked(record, "wage provenance is not a calculated net witness")
    if record.entering_iteration == 1:
        raise WageProvenanceBlocked(record, "first-round default/preparatory wage needs separate Owner decision")
    witness = record.calculation
    if not isinstance(witness, SyntheticNetWageCalculation):
        raise WageProvenanceBlocked(record, "label alone is not calculation evidence")
    if witness.generated_after_iteration != record.entering_iteration - 1:
        raise WageProvenanceBlocked(record, "stale/future generation iteration")
    if witness.context_id != record.context_id or witness.province_order != record.province_order:
        raise WageProvenanceBlocked(record, "calculation context or province order mismatch")
    expected = recompute_synthetic_net_wage(witness)
    if len(expected) != len(record.wage_by_origin) or any(
            not isclose(a, b, rel_tol=1e-12, abs_tol=1e-12) for a, b in zip(expected, record.wage_by_origin)):
        raise WageProvenanceBlocked(record, "observed wage does not match independent net recomputation")
    views = adapt_temp31_net_composite_wage(record.wage_by_origin, semantic=NET_COMPOSITE,
        tax_by_destination=witness.tax_by_destination,
        migration_wedge_destination_origin=witness.sigma_destination_origin)
    return ProposedConsumers(record, views)


@dataclass(frozen=True)
class ProposedResourceIdentity:
    initialization_wage_income: float
    hjb_boundary_wage_income: float
    policy_wage_income: float
    transfer: float
    rb_times_liquid_assets: float
    other_asset_resources: float
    saving_flow: float
    total_resources: float
    illustrative_consumption_after_saving: float
    scope: str = "PURE_ACCOUNTING_IDENTITY__NOT_INITIAL_VALUE_OR_HJB_POLICY"


def probe_proposed_resource_identity(
    proposal: ProposedConsumers, *, origin: int, z: float, labor: float,
    transfer: float = 0.0, rb: float = 0.0, liquid_assets: float = 0.0,
    other_asset_resources: float = 0.0, saving_flow: float = 0.0,
) -> ProposedResourceIdentity:
    """One proposed W*z*l across consumers; no FOC, policy or value solve.

    T + rb*b + caller-assumed other resources - saving is an illustrative
    accounting identity, not a reconstruction of unavailable HA equations.
    """
    record, views = proposal.record, proposal.views
    if proposal.scope != "SYNTHETIC_PROPOSED_CONSUMERS_ONLY__NO_REAL_HA":
        raise ValueError("not an authorized synthetic proposal")
    witness = record.calculation
    if not isinstance(witness, SyntheticNetWageCalculation):
        raise ValueError("calculation witness is missing")
    # Revalidate through the R4 pure-data adapter, never an actual HA consumer.
    checked = prepare_proposed_consumers(record)
    if views != checked.views or views.semantic != NET_COMPOSITE:
        raise ValueError("consumer wage views differ from the single-net-wage contract")
    if type(origin) is not int or not 0 <= origin < len(record.wage_by_origin):
        raise ValueError("origin index out of range")
    values = tuple(float(v) for v in (z, labor, transfer, rb, liquid_assets, other_asset_resources, saving_flow))
    if not all(map(isfinite, values)) or values[0] <= 0 or values[1] < 0:
        raise ValueError("z must be positive, labor nonnegative, and resource scalars finite")
    z, labor, transfer, rb, liquid_assets, other_asset_resources, saving_flow = values
    init_income = views.initialization[origin].effective_wage * z * labor
    hjb_income = views.hjb[origin].effective_wage * z * labor
    policy_income = views.hjb[origin].effective_wage * z * labor
    liquid_income = rb * liquid_assets
    resources = init_income + transfer + liquid_income + other_asset_resources
    consumption = resources - saving_flow
    if not all(map(isfinite, (init_income, hjb_income, policy_income, liquid_income, resources, consumption))):
        raise ValueError("resource arithmetic overflow")
    return ProposedResourceIdentity(init_income, hjb_income, policy_income, transfer,
        liquid_income, other_asset_resources, saving_flow, resources, consumption)
