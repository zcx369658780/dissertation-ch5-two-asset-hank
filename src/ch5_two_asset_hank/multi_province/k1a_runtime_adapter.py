"""Task-bounded K1A adapter for the corrected-2018 source-faithful route.

The adapter deliberately presents the three fields consumed by the legacy
one-turn composition while retaining the complete accepted K1 network result
for diagnostics.  It does not alter or wrap the legacy allocator itself.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

import numpy as np

from .capital_allocation import CapitalAllocationInputs
from .capital_network import BilateralCapitalNetworkInputs, BilateralCapitalNetworkResult, build_bilateral_capital_network
from .province_contracts import PROVINCE_ORDER


ACCEPTED_DISTANCE_CANONICAL_LF_SHA256 = "30401B7754A0126D544D54ABB36C6CB662E3E386663E3110EF3F68E417FDA084"
PAYOFF_CLASSIFICATION = "K1A_SOURCE_FAITHFUL_PAYOFF_BRIDGE__NOT_FINAL_ECONOMIC_RETURN_AUTHORITY"
LAGGED_RETURN_PROVENANCE = "K1A_LAGGED_RETURN_DISABLED_BETA_RETURN_ZERO__COMPLETED_INFORMATION_NOT_USED"


def canonical_lf_sha256(path: Path) -> str:
    """Hash a tracked text receipt independent of Git's CRLF checkout mode."""

    return sha256(Path(path).read_bytes().replace(b"\r\n", b"\n")).hexdigest().upper()


def load_accepted_distance_score(path: Path) -> np.ndarray:
    """Load the frozen 31x31 destination-by-origin normalized-distance receipt."""

    path = Path(path)
    observed = canonical_lf_sha256(path)
    if observed != ACCEPTED_DISTANCE_CANONICAL_LF_SHA256:
        raise ValueError(f"accepted distance receipt SHA mismatch: {observed}")
    index = {name: i for i, name in enumerate(PROVINCE_ORDER)}
    matrix = np.full((31, 31), np.nan, dtype=float)
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ["destination", "origin", "distance_score"]:
            raise ValueError("accepted distance receipt columns differ from the frozen contract")
        rows = list(reader)
    if len(rows) != 31 * 31:
        raise ValueError("accepted distance receipt must contain exactly 31x31 rows")
    for row in rows:
        try:
            destination = index[row["destination"]]
            origin = index[row["origin"]]
        except KeyError as exc:
            raise ValueError("accepted distance receipt contains an unknown province") from exc
        if np.isfinite(matrix[destination, origin]):
            raise ValueError("accepted distance receipt contains a duplicate cell")
        matrix[destination, origin] = float(row["distance_score"])
    if not np.all(np.isfinite(matrix)) or not np.array_equal(np.diag(matrix), np.zeros(31)):
        raise ValueError("accepted distance receipt is incomplete or has a nonzero diagonal")
    matrix.flags.writeable = False
    return matrix


@dataclass(frozen=True)
class K1ARuntimeConfig:
    province_order: tuple[str, ...]
    distance_score_destination_origin: np.ndarray
    beta_distance: float
    beta_return: float = 0.0
    payoff_classification: str = PAYOFF_CLASSIFICATION

    def __post_init__(self) -> None:
        order = tuple(self.province_order)
        distance = np.array(self.distance_score_destination_origin, dtype=float, copy=True)
        beta_distance = float(self.beta_distance)
        beta_return = float(self.beta_return)
        if order != PROVINCE_ORDER:
            raise ValueError("K1A runtime must use the exact accepted 31-province order")
        if distance.shape != (31, 31) or not np.all(np.isfinite(distance)):
            raise ValueError("K1A distance score must be a finite 31x31 destination-by-origin matrix")
        if beta_distance not in (0.0, 2.0):
            raise ValueError("this bounded K1A task permits beta_distance only in {0, 2}")
        if beta_return != 0.0:
            raise ValueError("K1B/return-score feedback is prohibited in this bounded K1A task")
        if self.payoff_classification != PAYOFF_CLASSIFICATION:
            raise ValueError("K1A payoff bridge classification is frozen")
        distance.flags.writeable = False
        object.__setattr__(self, "province_order", order)
        object.__setattr__(self, "distance_score_destination_origin", distance)
        object.__setattr__(self, "beta_distance", beta_distance)
        object.__setattr__(self, "beta_return", beta_return)


@dataclass(frozen=True)
class K1ACompatibleCapitalResult:
    """Legacy-consumer fields plus the complete K1 network diagnostic object."""

    productive_contribution: np.ndarray
    kt_supply: np.ndarray
    household_illiquid_return_rah: np.ndarray
    network: BilateralCapitalNetworkResult
    payoff_classification: str = PAYOFF_CLASSIFICATION


def allocate_k1a_capital(
    inputs: CapitalAllocationInputs, config: K1ARuntimeConfig
) -> K1ACompatibleCapitalResult:
    """Allocate K1A capital using current source-used returns as payoff levels."""

    network = build_bilateral_capital_network(BilateralCapitalNetworkInputs(
        province_order=config.province_order,
        illiquid_assets_per_capita_by_origin=inputs.illiquid_assets_at,
        population_by_origin=inputs.population,
        total_foreign_share_theta_by_origin=inputs.inter_province_ratio,
        distance_score_destination_origin=config.distance_score_destination_origin,
        lagged_return_score_by_destination=np.zeros(31),
        portfolio_return_by_destination=inputs.old_firm_return_ra,
        beta_distance=config.beta_distance,
        beta_return=config.beta_return,
        lagged_return_provenance=LAGGED_RETURN_PROVENANCE,
    ))
    # This compatibility field is not the legacy foreign-only contribution.
    # It exposes total origin wealth so all private capital remains accounted.
    return K1ACompatibleCapitalResult(
        productive_contribution=network.origin_private_wealth,
        kt_supply=network.destination_private_productive_capital,
        household_illiquid_return_rah=network.household_portfolio_return_by_origin,
        network=network,
    )
