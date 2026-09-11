"""Pure K1 bilateral private-capital portfolio accounting.

This successor is deliberately separate from the MATLAB-faithful legacy
``capital_allocation`` module and from every active one-turn/runtime route.
Rows are destinations and columns are household origins throughout.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

import numpy as np


SCHEMA_VERSION = "CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_V1"
ORIENTATION = "DESTINATION_BY_ORIGIN"
LAGGED_TIMING_CONTRACT = (
    "ALLOCATION_ITERATION_N_PLUS_1_USES_RETURN_SCORE_FROM_COMPLETED_ITERATION_N"
)
CONSERVATION_TOLERANCE = 1e-12


def _province_order(value: object) -> tuple[str, ...]:
    order = tuple(value)  # type: ignore[arg-type]
    if (
        len(order) < 2
        or len(set(order)) != len(order)
        or any(not isinstance(name, str) or not name for name in order)
    ):
        raise ValueError("province_order must contain at least two unique nonempty labels")
    return order


def _readonly_vector(name: str, value: object, n: int) -> np.ndarray:
    array = np.array(value, dtype=float, copy=True)
    if array.shape != (n,):
        raise ValueError(f"{name} must have shape ({n},) in exact province_order")
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values")
    array.flags.writeable = False
    return array


def _readonly_matrix(name: str, value: object, n: int) -> np.ndarray:
    array = np.array(value, dtype=float, copy=True)
    if array.shape != (n, n):
        raise ValueError(f"{name} must have destination-by-origin shape ({n}, {n})")
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values")
    array.flags.writeable = False
    return array


def _lagged_provenance(value: object) -> str:
    provenance = str(value).strip()
    upper = provenance.upper()
    normalized = upper.replace("-", "_").replace(" ", "_")
    if "SAME_TURN" in normalized or "CURRENT_FIRM" in normalized:
        raise ValueError("same-turn/current-firm return provenance is prohibited")
    if not provenance or ("LAGGED" not in upper and "COMPLETED_ITERATION" not in upper):
        raise ValueError("lagged_return_provenance must explicitly identify lagged/completed information")
    return provenance


@dataclass(frozen=True)
class ForeignConditionalShareInputs:
    """Explicit score inputs; coefficients intentionally have no defaults."""

    province_order: tuple[str, ...]
    distance_score_destination_origin: np.ndarray
    lagged_return_score_by_destination: np.ndarray
    beta_distance: float
    beta_return: float
    lagged_return_provenance: str

    def __post_init__(self) -> None:
        order = _province_order(self.province_order)
        n = len(order)
        distance = _readonly_matrix(
            "distance_score_destination_origin", self.distance_score_destination_origin, n
        )
        lagged = _readonly_vector(
            "lagged_return_score_by_destination", self.lagged_return_score_by_destination, n
        )
        beta_distance = float(self.beta_distance)
        beta_return = float(self.beta_return)
        if not isfinite(beta_distance) or not isfinite(beta_return):
            raise ValueError("beta_distance and beta_return must be finite explicit inputs")
        object.__setattr__(self, "province_order", order)
        object.__setattr__(self, "distance_score_destination_origin", distance)
        object.__setattr__(self, "lagged_return_score_by_destination", lagged)
        object.__setattr__(self, "beta_distance", beta_distance)
        object.__setattr__(self, "beta_return", beta_return)
        object.__setattr__(self, "lagged_return_provenance", _lagged_provenance(self.lagged_return_provenance))


@dataclass(frozen=True)
class ForeignConditionalShareResult:
    province_order: tuple[str, ...]
    foreign_conditional_shares_destination_origin: np.ndarray
    foreign_column_sums: np.ndarray
    orientation: str = ORIENTATION
    schema_version: str = SCHEMA_VERSION
    lagged_timing_contract: str = LAGGED_TIMING_CONTRACT
    lagged_return_provenance: str = ""

    def __post_init__(self) -> None:
        order = _province_order(self.province_order)
        n = len(order)
        shares = _readonly_matrix(
            "foreign_conditional_shares_destination_origin",
            self.foreign_conditional_shares_destination_origin,
            n,
        )
        sums = _readonly_vector("foreign_column_sums", self.foreign_column_sums, n)
        if self.orientation != ORIENTATION or self.schema_version != SCHEMA_VERSION:
            raise ValueError("foreign-share orientation/schema labels are immutable")
        if self.lagged_timing_contract != LAGGED_TIMING_CONTRACT:
            raise ValueError("lagged timing contract is immutable")
        if not np.allclose(np.diag(shares), 0.0, rtol=0.0, atol=0.0):
            raise ValueError("foreign conditional-share diagonal must be exactly zero")
        if np.any(shares < 0.0) or not np.allclose(
            sums, 1.0, rtol=0.0, atol=CONSERVATION_TOLERANCE
        ):
            raise ValueError("foreign conditional shares must be nonnegative and column-normalized")
        object.__setattr__(self, "province_order", order)
        object.__setattr__(self, "foreign_conditional_shares_destination_origin", shares)
        object.__setattr__(self, "foreign_column_sums", sums)
        object.__setattr__(self, "lagged_return_provenance", _lagged_provenance(self.lagged_return_provenance))


def foreign_conditional_shares(
    inputs: ForeignConditionalShareInputs,
) -> ForeignConditionalShareResult:
    """Stable foreign-only softmax for each origin column."""

    n = len(inputs.province_order)
    with np.errstate(over="ignore", invalid="ignore"):
        raw = (
            -inputs.beta_distance * inputs.distance_score_destination_origin
            + inputs.beta_return * inputs.lagged_return_score_by_destination[:, None]
        )
    if not np.all(np.isfinite(raw)):
        raise ValueError("foreign log-attractiveness must remain finite")
    shares = np.zeros((n, n), dtype=float)
    for origin in range(n):
        eligible = np.arange(n) != origin
        column = raw[eligible, origin]
        shifted = column - np.max(column)
        weights = np.exp(shifted)
        denominator = float(np.sum(weights))
        if not isfinite(denominator) or denominator <= 0.0:
            raise ValueError("foreign softmax denominator must be finite and positive")
        shares[eligible, origin] = weights / denominator
    column_sums = np.sum(shares, axis=0)
    shares.flags.writeable = False
    column_sums.flags.writeable = False
    return ForeignConditionalShareResult(
        province_order=inputs.province_order,
        foreign_conditional_shares_destination_origin=shares,
        foreign_column_sums=column_sums,
        lagged_return_provenance=inputs.lagged_return_provenance,
    )


@dataclass(frozen=True)
class BilateralCapitalNetworkInputs:
    """K1 quantity/payoff boundary with separate signal and payoff vectors."""

    province_order: tuple[str, ...]
    illiquid_assets_per_capita_by_origin: np.ndarray
    population_by_origin: np.ndarray
    total_foreign_share_theta_by_origin: np.ndarray
    distance_score_destination_origin: np.ndarray
    lagged_return_score_by_destination: np.ndarray
    portfolio_return_by_destination: np.ndarray
    beta_distance: float
    beta_return: float
    lagged_return_provenance: str

    def __post_init__(self) -> None:
        order = _province_order(self.province_order)
        n = len(order)
        assets = _readonly_vector(
            "illiquid_assets_per_capita_by_origin", self.illiquid_assets_per_capita_by_origin, n
        )
        population = _readonly_vector("population_by_origin", self.population_by_origin, n)
        theta = _readonly_vector(
            "total_foreign_share_theta_by_origin", self.total_foreign_share_theta_by_origin, n
        )
        distance = _readonly_matrix(
            "distance_score_destination_origin", self.distance_score_destination_origin, n
        )
        lagged = _readonly_vector(
            "lagged_return_score_by_destination", self.lagged_return_score_by_destination, n
        )
        payoff = _readonly_vector(
            "portfolio_return_by_destination", self.portfolio_return_by_destination, n
        )
        if np.any(assets < 0.0) or np.any(population <= 0.0):
            raise ValueError("illiquid assets must be nonnegative and population strictly positive")
        if np.any((theta < 0.0) | (theta > 1.0)):
            raise ValueError("total foreign shares theta must lie in [0, 1]")
        beta_distance = float(self.beta_distance)
        beta_return = float(self.beta_return)
        if not isfinite(beta_distance) or not isfinite(beta_return):
            raise ValueError("beta_distance and beta_return must be finite explicit inputs")
        object.__setattr__(self, "province_order", order)
        object.__setattr__(self, "illiquid_assets_per_capita_by_origin", assets)
        object.__setattr__(self, "population_by_origin", population)
        object.__setattr__(self, "total_foreign_share_theta_by_origin", theta)
        object.__setattr__(self, "distance_score_destination_origin", distance)
        object.__setattr__(self, "lagged_return_score_by_destination", lagged)
        object.__setattr__(self, "portfolio_return_by_destination", payoff)
        object.__setattr__(self, "beta_distance", beta_distance)
        object.__setattr__(self, "beta_return", beta_return)
        object.__setattr__(self, "lagged_return_provenance", _lagged_provenance(self.lagged_return_provenance))


@dataclass(frozen=True)
class BilateralCapitalNetworkResult:
    province_order: tuple[str, ...]
    foreign_conditional_shares_destination_origin: np.ndarray
    portfolio_shares_destination_origin: np.ndarray
    origin_private_wealth: np.ndarray
    bilateral_private_capital_destination_origin: np.ndarray
    destination_private_productive_capital: np.ndarray
    domestic_retained_capital_by_origin: np.ndarray
    foreign_outflow_by_origin: np.ndarray
    foreign_inflow_by_destination: np.ndarray
    household_portfolio_return_by_origin: np.ndarray
    share_column_sums: np.ndarray
    capital_column_sums: np.ndarray
    national_private_capital_conservation_residual: float
    orientation: str = ORIENTATION
    schema_version: str = SCHEMA_VERSION
    lagged_timing_contract: str = LAGGED_TIMING_CONTRACT
    lagged_return_provenance: str = ""

    def __post_init__(self) -> None:
        order = _province_order(self.province_order)
        n = len(order)
        matrix_names = (
            "foreign_conditional_shares_destination_origin",
            "portfolio_shares_destination_origin",
            "bilateral_private_capital_destination_origin",
        )
        vector_names = (
            "origin_private_wealth",
            "destination_private_productive_capital",
            "domestic_retained_capital_by_origin",
            "foreign_outflow_by_origin",
            "foreign_inflow_by_destination",
            "household_portfolio_return_by_origin",
            "share_column_sums",
            "capital_column_sums",
        )
        for name in matrix_names:
            object.__setattr__(self, name, _readonly_matrix(name, getattr(self, name), n))
        for name in vector_names:
            object.__setattr__(self, name, _readonly_vector(name, getattr(self, name), n))
        residual = float(self.national_private_capital_conservation_residual)
        if not isfinite(residual):
            raise ValueError("national conservation residual must be finite")
        if self.orientation != ORIENTATION or self.schema_version != SCHEMA_VERSION:
            raise ValueError("capital-network orientation/schema labels are immutable")
        if self.lagged_timing_contract != LAGGED_TIMING_CONTRACT:
            raise ValueError("lagged timing contract is immutable")
        object.__setattr__(self, "province_order", order)
        object.__setattr__(self, "national_private_capital_conservation_residual", residual)
        object.__setattr__(self, "lagged_return_provenance", _lagged_provenance(self.lagged_return_provenance))


def build_bilateral_capital_network(
    inputs: BilateralCapitalNetworkInputs,
) -> BilateralCapitalNetworkResult:
    """Build one conserved K1 portfolio matrix without calling any model runtime."""

    n = len(inputs.province_order)
    foreign = foreign_conditional_shares(ForeignConditionalShareInputs(
        province_order=inputs.province_order,
        distance_score_destination_origin=inputs.distance_score_destination_origin,
        lagged_return_score_by_destination=inputs.lagged_return_score_by_destination,
        beta_distance=inputs.beta_distance,
        beta_return=inputs.beta_return,
        lagged_return_provenance=inputs.lagged_return_provenance,
    ))
    theta = inputs.total_foreign_share_theta_by_origin
    shares = foreign.foreign_conditional_shares_destination_origin * theta[None, :]
    diagonal = np.arange(n)
    shares[diagonal, diagonal] = 1.0 - theta
    share_sums = np.sum(shares, axis=0)
    if not np.allclose(share_sums, 1.0, rtol=0.0, atol=CONSERVATION_TOLERANCE):
        raise RuntimeError("full portfolio shares do not conserve each origin column")

    with np.errstate(over="ignore", invalid="ignore"):
        wealth = inputs.illiquid_assets_per_capita_by_origin * inputs.population_by_origin
    if not np.all(np.isfinite(wealth)):
        raise ValueError("origin private wealth must remain finite")
    with np.errstate(over="ignore", invalid="ignore"):
        flows = shares * wealth[None, :]
    if not np.all(np.isfinite(flows)):
        raise ValueError("bilateral private-capital flows must remain finite")
    capital_sums = np.sum(flows, axis=0)
    destination_private = np.sum(flows, axis=1)
    domestic = np.diag(flows).copy()
    foreign_outflow = capital_sums - domestic
    foreign_inflow = destination_private - domestic
    with np.errstate(over="ignore", invalid="ignore"):
        rah = inputs.portfolio_return_by_destination @ shares
    if not np.all(np.isfinite(rah)):
        raise ValueError("household portfolio returns must remain finite")
    national_residual = float(np.sum(destination_private) - np.sum(wealth))

    scale = max(1.0, float(np.sum(wealth)))
    if not np.allclose(capital_sums, wealth, rtol=0.0, atol=CONSERVATION_TOLERANCE * scale):
        raise RuntimeError("bilateral capital does not conserve each origin wealth column")
    if abs(national_residual) > CONSERVATION_TOLERANCE * scale:
        raise RuntimeError("bilateral capital does not conserve national private wealth")
    expected_domestic = (1.0 - theta) * wealth
    expected_foreign = theta * wealth
    if not np.allclose(domestic, expected_domestic, rtol=0.0, atol=CONSERVATION_TOLERANCE * scale):
        raise RuntimeError("domestic retained private capital identity failed")
    if not np.allclose(foreign_outflow, expected_foreign, rtol=0.0, atol=CONSERVATION_TOLERANCE * scale):
        raise RuntimeError("foreign private-capital outflow identity failed")

    return BilateralCapitalNetworkResult(
        province_order=inputs.province_order,
        foreign_conditional_shares_destination_origin=foreign.foreign_conditional_shares_destination_origin,
        portfolio_shares_destination_origin=shares,
        origin_private_wealth=wealth,
        bilateral_private_capital_destination_origin=flows,
        destination_private_productive_capital=destination_private,
        domestic_retained_capital_by_origin=domestic,
        foreign_outflow_by_origin=foreign_outflow,
        foreign_inflow_by_destination=foreign_inflow,
        household_portfolio_return_by_origin=rah,
        share_column_sums=share_sums,
        capital_column_sums=capital_sums,
        national_private_capital_conservation_residual=national_residual,
        lagged_return_provenance=inputs.lagged_return_provenance,
    )
