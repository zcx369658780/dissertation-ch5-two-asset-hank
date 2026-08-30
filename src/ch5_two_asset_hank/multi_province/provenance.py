"""External-data identities, preserving MP1 history and MP4A2 adjudication."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class DataArtifactProvenance:
    name: str
    role: str
    expected_sha256: str | None
    classification: Literal[
        "SOURCE_IDENTIFIED_EXTERNAL_DATA_PENDING_CAPTURE",
        "PRIMARY_SOURCE_HASH_VERIFIED",
        "CACHE_DERIVED_NOT_PRIMARY_AUTHORITY",
    ]
    raw_or_derived: Literal["RAW_EXTERNAL_SOURCE", "DERIVED_CACHE"]
    year_index_semantics_status: str
    owner_approval_required: bool
    read_only_no_overwrite: bool

    def __post_init__(self) -> None:
        if not self.name or not self.role or not self.year_index_semantics_status:
            raise ValueError("provenance identity, role, and year status must be explicit")
        if self.expected_sha256 is not None:
            digest = self.expected_sha256.upper()
            if len(digest) != 64 or any(character not in "0123456789ABCDEF" for character in digest):
                raise ValueError("expected_sha256 must be a 64-character hexadecimal digest")
            object.__setattr__(self, "expected_sha256", digest)
        if not self.read_only_no_overwrite:
            raise ValueError("external source and cache artifacts must be read-only/no-overwrite")


DATA_PROVENANCE_MANIFEST: tuple[DataArtifactProvenance, ...] = (
    DataArtifactProvenance(
        "中国各省省会地理距离矩阵.xlsx", "distances and migration costs",
        "26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566",
        "PRIMARY_SOURCE_HASH_VERIFIED", "RAW_EXTERNAL_SOURCE",
        "NOT_YEAR_INDEXED", False, True,
    ),
    DataArtifactProvenance(
        "2000年后各省数据_填充NA.xlsx", "GDP, capital, population, and industry source",
        "C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929",
        "PRIMARY_SOURCE_HASH_VERIFIED", "RAW_EXTERNAL_SOURCE",
        "OWNER_VERIFIED_EXPLICIT_WORKBOOK_CALENDAR_2000_2023", False, True,
    ),
    DataArtifactProvenance(
        "2000年后各省数据.xlsx", "unfilled raw fallback source",
        "09814A45D933B2685A35238A15C0C7BB501F00A63597796B3CADCE15C230ECB3",
        "PRIMARY_SOURCE_HASH_VERIFIED", "RAW_EXTERNAL_SOURCE",
        "EXPLICIT_WORKBOOK_CALENDAR_2000_2023_INACTIVE_FALLBACK", False, True,
    ),
    DataArtifactProvenance(
        "R语言估计结果_plm估计.xlsx", "regression estimates",
        "A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68",
        "PRIMARY_SOURCE_HASH_VERIFIED", "RAW_EXTERNAL_SOURCE",
        "DECOUPLED_REGRESSION_VINTAGE_KEY_ANALYSIS_INDEX_PLUS_9", False, True,
    ),
    DataArtifactProvenance(
        "数据估计结果_1000_100_0.mat", "cached mydata2 calibration/data object",
        "923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A",
        "CACHE_DERIVED_NOT_PRIMARY_AUTHORITY", "DERIVED_CACHE",
        "NONPRIMARY_RUNTIME_REPRESENTATION_DECOUPLED_2009_RECONCILED", True, True,
    ),
    DataArtifactProvenance(
        "Multi_Province_12sts_<year>.mat", "derived annual steady-state st cache",
        None, "CACHE_DERIVED_NOT_PRIMARY_AUTHORITY", "DERIVED_CACHE",
        "SOURCE_II_PLUS_2008_VS_DATASET_ROW_UNRESOLVED", True, True,
    ),
)


@dataclass(frozen=True)
class YearCacheBinding:
    """Legacy MP1 coupled binding retained for forensic/backward compatibility.

    New annual preparation must use ``annual.DecoupledAnnualIndex`` instead.
    """

    source_ii: int
    dataset_row: int
    cache_year: int
    semantics_status: Literal[
        "UNRESOLVED_SOURCE_II_DATASET_ROW_CACHE_YEAR",
        "OWNER_VERIFIED",
    ]
    owner_approved: bool

    def require_annual_execution_authority(self) -> tuple[int, int, int]:
        if self.semantics_status != "OWNER_VERIFIED" or not self.owner_approved:
            raise ValueError("annual execution requires an Owner-verified year/cache binding")
        if min(self.source_ii, self.dataset_row, self.cache_year) < 1:
            raise ValueError("year/cache indices must be positive")
        if self.cache_year != self.source_ii + 2008:
            raise ValueError("cache_year must preserve the source filename rule source_ii + 2008")
        return (self.source_ii, self.dataset_row, self.cache_year)
