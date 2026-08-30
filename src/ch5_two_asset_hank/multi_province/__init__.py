"""Fail-closed contracts for the source-faithful multi-province route."""

from .household_adapter import (
    ACCEPTED_HA_PUBLIC_API,
    MATLAB_TO_ACCEPTED_HA_FIELD_MAP,
    MATLAB_TO_ACCEPTED_HA_OUTPUT_MAP,
    NO_LEGACY_R5_RUNTIME_DEPENDENCY,
    FrozenHouseholdOutputs,
    MultiProvinceHouseholdInputs,
    StaticHouseholdCall,
    build_static_household_call,
    reject_legacy_runtime_references,
)
from .provenance import DATA_PROVENANCE_MANIFEST, DataArtifactProvenance, YearCacheBinding
from .province_contracts import (
    PROVINCE_ORDER,
    HouseholdOuterOutputs,
    MigrationLaborAllocation,
    ProvinceAxis,
    ProvinceMatrix,
    ProvinceVector,
)

__all__ = [
    "DATA_PROVENANCE_MANIFEST",
    "ACCEPTED_HA_PUBLIC_API",
    "MATLAB_TO_ACCEPTED_HA_FIELD_MAP",
    "MATLAB_TO_ACCEPTED_HA_OUTPUT_MAP",
    "NO_LEGACY_R5_RUNTIME_DEPENDENCY",
    "PROVINCE_ORDER",
    "DataArtifactProvenance",
    "FrozenHouseholdOutputs",
    "HouseholdOuterOutputs",
    "MigrationLaborAllocation",
    "MultiProvinceHouseholdInputs",
    "ProvinceAxis",
    "ProvinceMatrix",
    "ProvinceVector",
    "StaticHouseholdCall",
    "YearCacheBinding",
    "build_static_household_call",
    "reject_legacy_runtime_references",
]
