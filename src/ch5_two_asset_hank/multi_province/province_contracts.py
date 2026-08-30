"""Province axes and outer-state shapes frozen by the MP1 source contract."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


PROVINCE_ORDER: tuple[str, ...] = (
    "北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江",
    "上海", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南",
    "湖北", "湖南", "广东", "广西", "海南", "重庆", "四川", "贵州",
    "云南", "西藏", "陕西", "甘肃", "青海", "宁夏", "新疆",
)


@dataclass(frozen=True)
class ProvinceAxis:
    """The unique source-defined 31-province axis."""

    labels: tuple[str, ...]

    def __post_init__(self) -> None:
        labels = tuple(self.labels)
        if len(labels) != 31:
            raise ValueError("province axis must contain exactly 31 labels")
        if len(set(labels)) != len(labels):
            raise ValueError("province axis contains a duplicate province")
        unknown = set(labels) - set(PROVINCE_ORDER)
        if unknown:
            raise ValueError(f"province axis contains unknown labels: {sorted(unknown)!r}")
        if labels != PROVINCE_ORDER:
            raise ValueError("province axis must use the exact source order")
        object.__setattr__(self, "labels", labels)


@dataclass(frozen=True)
class ProvinceVector:
    """A finite vector whose positions are bound to the exact province axis."""

    name: str
    values: np.ndarray
    axis: ProvinceAxis

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("province vector name must be explicit")
        values = np.array(self.values, dtype=float, copy=True)
        if values.shape != (31,):
            raise ValueError(f"{self.name} must have shape (31,)")
        if not np.all(np.isfinite(values)):
            raise ValueError(f"{self.name} must contain only finite values")
        values.flags.writeable = False
        object.__setattr__(self, "values", values)


@dataclass(frozen=True)
class ProvinceMatrix:
    """A finite 31-by-31 matrix with explicit row and column semantics."""

    name: str
    values: np.ndarray
    axis: ProvinceAxis
    row_role: str
    column_role: str

    def __post_init__(self) -> None:
        if not self.name or not self.row_role or not self.column_role:
            raise ValueError("matrix name, row role, and column role must be explicit")
        values = np.array(self.values, dtype=float, copy=True)
        if values.shape != (31, 31):
            raise ValueError(f"{self.name} must have shape (31, 31)")
        if not np.all(np.isfinite(values)):
            raise ValueError(f"{self.name} must contain only finite values")
        values.flags.writeable = False
        object.__setattr__(self, "values", values)


@dataclass(frozen=True)
class HouseholdOuterOutputs:
    """Pre-firm household aggregates; ``household_lt`` is not firm labor."""

    ct: ProvinceVector
    household_lt: ProvinceVector
    at: ProvinceVector
    bt: ProvinceVector
    at_tax: ProvinceVector
    converged: tuple[bool, ...]
    diagnostics: tuple[dict[str, object], ...]

    def __post_init__(self) -> None:
        vectors = (self.ct, self.household_lt, self.at, self.bt, self.at_tax)
        if any(vector.axis != self.ct.axis for vector in vectors):
            raise ValueError("household output vectors must share the exact province axis")
        required_names = (
            ("ct", self.ct, "Ct"),
            ("household_lt", self.household_lt, "Lt"),
            ("at", self.at, "At"),
            ("bt", self.bt, "Bt"),
            ("at_tax", self.at_tax, "AtTax"),
        )
        for field_name, vector, expected_name in required_names:
            if vector.name != expected_name:
                raise ValueError(f"{field_name} must be named {expected_name}")
        if len(self.converged) != 31:
            raise ValueError("household outputs require 31 convergence flags")
        if len(self.diagnostics) != 31:
            raise ValueError("household outputs require 31 diagnostic records")
        object.__setattr__(self, "converged", tuple(bool(value) for value in self.converged))
        object.__setattr__(self, "diagnostics", tuple(dict(value) for value in self.diagnostics))


@dataclass(frozen=True)
class MigrationLaborAllocation:
    """``Lt_mat[j,i]``: origin ``i`` labor allocated to destination ``j``."""

    lt_mat: ProvinceMatrix

    def __post_init__(self) -> None:
        if self.lt_mat.name != "Lt_mat":
            raise ValueError("migration labor matrix must be named Lt_mat")
        if (self.lt_mat.row_role, self.lt_mat.column_role) != ("destination", "origin"):
            raise ValueError("Lt_mat orientation must be rows=destination, columns=origin")

    def destination_supply(self) -> np.ndarray:
        supply = np.sum(self.lt_mat.values, axis=1)
        supply.flags.writeable = False
        return supply
