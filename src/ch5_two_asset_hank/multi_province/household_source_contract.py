"""Opt-in, in-memory synthetic admission. Digests are NOT source authentication.

No loader, solver, real-source branch, or production export lives here. The
caller supplies an independent requested identity; matching self-declarations
prove consistency only. Jointly rewritten payload/manifest can still agree.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import re
from types import MappingProxyType
from typing import Mapping

import numpy as np

from .corrected_household_adapter import CorrectedHouseholdAggregateInputs
from .synthetic_household_bridge import SyntheticHouseholdRecord, SOURCE_KIND


FIELD_ROLES = MappingProxyType({
    "consumption": "CONSUMPTION_POLICY", "labor": "LABOR_POLICY",
    "b_grid": "LIQUID_ASSET_AXIS", "a_grid": "ILLIQUID_ASSET_AXIS",
    "z_grid": "PRODUCTIVITY_AXIS",
    "effective_r_a": "STATE_DEPENDENT_EFFECTIVE_RETURN",
    "probability_mass": "CELL_PROBABILITY_MASS", "density": "CELL_DENSITY",
    "omega": "CELL_WEIGHT", "source_r_a": "UNIFORM_SOURCE_RETURN",
    "flat_indices_b_a_z": "F_ORDER_CELL_INDICES",
})
_SCALARS = frozenset(("omega", "source_r_a"))
_HASH = re.compile(r"[0-9a-f]{64}\Z")


@dataclass(frozen=True)
class HouseholdSourceIdentity:
    """Simulation labels, not an asset identity certificate or calendar mapping."""
    province: str
    source_id: str
    iteration: int
    checkpoint_id: str
    grid_id: str

    def __post_init__(self) -> None:
        for name, prefix in (("province", "SYNTH_"), ("source_id", "SIM_"),
                             ("checkpoint_id", "SIM_"), ("grid_id", "SIM_")):
            value = getattr(self, name)
            if (not isinstance(value, str) or not value.startswith(prefix)
                    or len(value) <= len(prefix) or value != value.strip()):
                raise ValueError(f"{name} requires a nonempty explicit simulation label")
        if type(self.iteration) is not int or self.iteration < 1:
            raise ValueError("iteration is a positive simulated stage, not a real calendar period")


@dataclass(frozen=True)
class SimulatedFieldReference:
    field: str
    identity: HouseholdSourceIdentity
    role: str
    digest_sha256: str


@dataclass(frozen=True)
class HouseholdSourceMetadata:
    identity: HouseholdSourceIdentity
    field_references: tuple[SimulatedFieldReference, ...]
    simulated_seal_sha256: str
    source_kind: str = SOURCE_KIND
    axis_order: tuple[str, str, str] = ("b", "a", "z")
    flatten_order: str = "F"

    def __post_init__(self) -> None:
        object.__setattr__(self, "field_references", tuple(self.field_references))
        object.__setattr__(self, "axis_order", tuple(self.axis_order))


@dataclass(frozen=True)
class SourceContractAssessment:
    admitted: bool
    reason: str
    evidence_level: str
    real_source_authentication: str = "NOT_VERIFIED"


def _identity(identity: HouseholdSourceIdentity) -> dict[str, object]:
    if not isinstance(identity, HouseholdSourceIdentity):
        raise ValueError("explicit HouseholdSourceIdentity required")
    return {name: getattr(identity, name) for name in
            ("province", "source_id", "iteration", "checkpoint_id", "grid_id")}


def _numeric_snapshot(field: str, value: object) -> np.ndarray:
    array = np.asarray(value)
    if field in _SCALARS and array.ndim != 0:
        raise ValueError(f"{field} must be a scalar with its distinct return/weight role")
    if field == "flat_indices_b_a_z":
        if not np.issubdtype(array.dtype, np.integer):
            raise ValueError("F-order cell indices must be integer")
        dtype = "<i8"
    else:
        if array.dtype.kind not in "fiu":
            raise ValueError(f"{field} requires real numeric values, not booleans/strings/complex")
        dtype = "<f8"
    return np.array(array, dtype=dtype, copy=True, order="F")


def simulated_field_digest(field: str, value: object) -> str:
    """Canonical field-name/shape/role + little-endian F bytes; never a signature.

    This function can describe nonfinite or structurally invalid numeric arrays;
    digest existence does not imply numeric admission. Scalar roles have shape ().
    """
    if field not in FIELD_ROLES:
        raise ValueError("unknown simulated field")
    array = _numeric_snapshot(field, value)
    header = json.dumps({"field": field, "role": FIELD_ROLES[field],
                         "shape": list(array.shape), "dtype": array.dtype.str,
                         "order": "F", "schema": "CH5_SIMULATED_FIELD_V1"},
                        sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(header+b"\n"+array.tobytes(order="F")).hexdigest()


def simulated_manifest_digest(metadata: HouseholdSourceMetadata) -> str:
    """Self-declared simulated manifest digest, excluding the digest itself.

    No filesystem/real manifest is consulted. No trust anchor is established.
    """
    document = {"schema": "CH5_SIMULATED_MANIFEST_V1",
                "identity": _identity(metadata.identity), "source_kind": metadata.source_kind,
                "axis_order": list(metadata.axis_order), "flatten_order": metadata.flatten_order,
                "references": [{"field": r.field, "identity": _identity(r.identity),
                                "role": r.role, "digest": r.digest_sha256}
                               for r in metadata.field_references]}
    return hashlib.sha256(json.dumps(document, sort_keys=True, separators=(",", ":"),
                                     allow_nan=False).encode("utf-8")).hexdigest()


def admit_synthetic_household_record(
    metadata: HouseholdSourceMetadata,
    payload: Mapping[str, object],
    *, requested_identity: HouseholdSourceIdentity,
) -> SyntheticHouseholdRecord:
    """Copy, jointly check and convert ONLY explicit simulated in-memory inputs.

    Reuses the unchanged corrected constructor and V0.0.1 record constraints.
    No aggregation occurs until the caller explicitly invokes the old builder.
    Synthetic convergence remains False; no scientific convergence is inferred.
    """
    if not isinstance(metadata, HouseholdSourceMetadata):
        raise ValueError("explicit HouseholdSourceMetadata required")
    if metadata.source_kind != SOURCE_KIND:
        raise ValueError("source_kind must be SYNTHETIC/NOT_REAL_SOURCE; all other computation blocked")
    _identity(requested_identity)
    if metadata.identity != requested_identity:
        raise ValueError("metadata does not match requested identity")
    if metadata.axis_order != ("b", "a", "z") or metadata.flatten_order != "F":
        raise ValueError("semantic axis/order declaration must be (b,a,z)/F")
    if not isinstance(payload, Mapping) or set(payload) != set(FIELD_ROLES):
        raise ValueError("payload fields must be exactly the eleven explicit simulated inputs")
    refs = metadata.field_references
    if any(not isinstance(r, SimulatedFieldReference) for r in refs):
        raise ValueError("typed simulated field references required")
    if len(refs) != len(FIELD_ROLES) or {r.field for r in refs} != set(FIELD_ROLES):
        raise ValueError("complete unique simulated field references required")
    if not isinstance(metadata.simulated_seal_sha256, str) or not _HASH.fullmatch(metadata.simulated_seal_sha256):
        raise ValueError("explicit simulated seal digest required")
    # Snapshot before digest checks: later caller mutation cannot change admission.
    values = {name: _numeric_snapshot(name, payload[name]) for name in FIELD_ROLES}
    for ref in refs:
        if ref.identity != requested_identity:
            raise ValueError(f"field identity mismatch: {ref.field}")
        if ref.role != FIELD_ROLES[ref.field]:
            raise ValueError(f"field role mismatch: {ref.field}; uniform/effective returns are distinct")
        if not isinstance(ref.digest_sha256, str) or not _HASH.fullmatch(ref.digest_sha256):
            raise ValueError(f"invalid simulated field digest: {ref.field}")
        if simulated_field_digest(ref.field, values[ref.field]) != ref.digest_sha256:
            raise ValueError(f"simulated field digest mismatch: {ref.field}")
    if simulated_manifest_digest(metadata) != metadata.simulated_seal_sha256:
        raise ValueError("simulated manifest seal mismatch")
    aggregate = CorrectedHouseholdAggregateInputs(**{
        name: (float(value) if name in _SCALARS else value)
        for name, value in values.items() if name != "flat_indices_b_a_z"})
    return SyntheticHouseholdRecord(
        province=requested_identity.province, iteration=requested_identity.iteration,
        source_id=requested_identity.source_id, aggregate_inputs=aggregate,
        flat_indices_b_a_z=values["flat_indices_b_a_z"], source_kind=SOURCE_KIND,
        synthetic_converged=False, synthetic_convergence_statistic=0.,
    )


def assess_source_contract(
    metadata: HouseholdSourceMetadata,
    payload: Mapping[str, object],
    *, requested_identity: HouseholdSourceIdentity,
) -> SourceContractAssessment:
    """Explain refusal without granting real identity/science/output eligibility.

    An assessment is not an admission token. Conversion always checks again.
    """
    try:
        admit_synthetic_household_record(metadata, payload, requested_identity=requested_identity)
    except (ValueError, TypeError) as exc:
        return SourceContractAssessment(False, str(exc), "BLOCKED")
    return SourceContractAssessment(True, "simulated internal consistency only", "SYNTHETIC_ENGINEERING")
