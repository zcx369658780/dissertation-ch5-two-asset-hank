"""Pure residual government/public productive-asset accounting.

This module is deliberately unconnected to the historical controller and all
model runtimes.  It only maps capital targets and current private productive
capital into an auditable government/public asset level.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Sequence

import numpy as np

from .province_contracts import PROVINCE_ORDER


CAPITAL_UNIT = "MU_10WAN_YUAN"
RESIDUAL_PUBLIC_ASSET_POSITIVE = "RESIDUAL_PUBLIC_ASSET_POSITIVE"
RESIDUAL_PUBLIC_ASSET_ZERO_PRIVATE_AT_OR_ABOVE_TARGET = (
    "RESIDUAL_PUBLIC_ASSET_ZERO_PRIVATE_AT_OR_ABOVE_TARGET"
)


@dataclass(frozen=True)
class ResidualGovernmentAssetLevel:
    """One province's direct residual public-asset level and accounting."""

    Ktarget_MU: float
    Kprivate_current_MU: float
    GovInv_residual_MU: float
    firm_K_accounting_MU: float
    firm_K_over_target: float
    private_at_or_above_target: bool
    residual_floor_binding: bool
    capital_gap_before_MU: float
    capital_gap_after_MU: float
    status: str
    capital_unit: str = CAPITAL_UNIT


@dataclass(frozen=True)
class ResidualGovernmentAssetBatch:
    """Read-only 31-province vectors bound to the source province order."""

    province_order: tuple[str, ...]
    Ktarget_MU: np.ndarray
    Kprivate_current_MU: np.ndarray
    GovInv_residual_MU: np.ndarray
    firm_K_accounting_MU: np.ndarray
    firm_K_over_target: np.ndarray
    private_at_or_above_target: np.ndarray
    residual_floor_binding: np.ndarray
    capital_gap_before_MU: np.ndarray
    capital_gap_after_MU: np.ndarray
    status: tuple[str, ...]
    capital_unit: str = CAPITAL_UNIT


def _validated_scalar(value: object, name: str, *, positive: bool) -> float:
    if isinstance(value, (bool, np.bool_)):
        raise ValueError(f"{name} must be a real capital level")
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a real capital level") from exc
    if not isfinite(number):
        raise ValueError(f"{name} must be finite")
    if positive and number <= 0.0:
        raise ValueError(f"{name} must be positive")
    if not positive and number < 0.0:
        raise ValueError(f"{name} must be non-negative")
    return number


def residual_government_asset_level(
    *, Ktarget_MU: object, Kprivate_current_MU: object
) -> ResidualGovernmentAssetLevel:
    """Return the direct residual public productive-asset level.

    When private capital is below target, accounting firm capital is set to
    the exact target identity.  When private capital reaches or exceeds the
    target, the public-asset floor binds at zero and private overshoot remains.
    """

    target = _validated_scalar(Ktarget_MU, "Ktarget_MU", positive=True)
    private = _validated_scalar(
        Kprivate_current_MU, "Kprivate_current_MU", positive=False
    )
    gap_before = target - private
    at_or_above = private >= target
    if at_or_above:
        government = 0.0
        firm_capital = private
        status = RESIDUAL_PUBLIC_ASSET_ZERO_PRIVATE_AT_OR_ABOVE_TARGET
    else:
        government = gap_before
        firm_capital = target
        status = RESIDUAL_PUBLIC_ASSET_POSITIVE
    return ResidualGovernmentAssetLevel(
        Ktarget_MU=target,
        Kprivate_current_MU=private,
        GovInv_residual_MU=government,
        firm_K_accounting_MU=firm_capital,
        firm_K_over_target=firm_capital / target,
        private_at_or_above_target=at_or_above,
        residual_floor_binding=at_or_above,
        capital_gap_before_MU=gap_before,
        capital_gap_after_MU=target - firm_capital,
        status=status,
    )


def residual_government_asset_levels(
    *,
    Ktarget_MU: object,
    Kprivate_current_MU: object,
    province_order: Sequence[str],
) -> ResidualGovernmentAssetBatch:
    """Apply the scalar contract to the exact 31-province source axis."""

    order = tuple(province_order)
    if order != PROVINCE_ORDER:
        raise ValueError("province_order must match the exact source province order")
    target = np.asarray(Ktarget_MU, dtype=float)
    private = np.asarray(Kprivate_current_MU, dtype=float)
    if target.shape != (31,) or private.shape != target.shape:
        raise ValueError("capital vectors must both have shape (31,)")
    results = tuple(
        residual_government_asset_level(
            Ktarget_MU=target[index], Kprivate_current_MU=private[index]
        )
        for index in range(31)
    )

    def readonly(values: object, dtype: object = float) -> np.ndarray:
        array = np.array(values, dtype=dtype, copy=True)
        array.flags.writeable = False
        return array

    return ResidualGovernmentAssetBatch(
        province_order=order,
        Ktarget_MU=readonly([item.Ktarget_MU for item in results]),
        Kprivate_current_MU=readonly([item.Kprivate_current_MU for item in results]),
        GovInv_residual_MU=readonly([item.GovInv_residual_MU for item in results]),
        firm_K_accounting_MU=readonly(
            [item.firm_K_accounting_MU for item in results]
        ),
        firm_K_over_target=readonly([item.firm_K_over_target for item in results]),
        private_at_or_above_target=readonly(
            [item.private_at_or_above_target for item in results], bool
        ),
        residual_floor_binding=readonly(
            [item.residual_floor_binding for item in results], bool
        ),
        capital_gap_before_MU=readonly(
            [item.capital_gap_before_MU for item in results]
        ),
        capital_gap_after_MU=readonly(
            [item.capital_gap_after_MU for item in results]
        ),
        status=tuple(item.status for item in results),
    )
