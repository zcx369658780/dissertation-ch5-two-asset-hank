"""Inactive archive metadata only; no I/O, numerical carrier or consumer imports.

Completeness concerns declarations, never evidence truth or execution authority.
Errors are fixed codes. UNKNOWN is retained and never filled from summaries.
"""
from dataclasses import dataclass
import re

UNKNOWN = "UNKNOWN"
AGGREGATE_KEYS = ("ct", "household_lt", "at", "bt", "at_tax")
COMBINED_KEYS = ("N", "wjt", "tau", *AGGREGATE_KEYS, "S")
STAGE_CONTRACT = (
    ("state", "entering_c8"),
    ("share", "frozen_entering_c8"),
    ("household", "completed_c8_household_pre_outer"),
)
EVIDENCE_KEYS = (
    "raw_input_capture", "exact_checkpoint", "state_binding",
    "frozen_share_binding", "province_correspondence", "aggregate_units",
    "combined_units", "principal_sid_rights", "all_ancestor_control",
    "handle_lifetime",
)

_MISSING_ORDER = (
    tuple(name + "." + key
          for name in ("archive_observation", "annual_source")
          for key in ("source_identifier", "sha256", "evidence"))
    + tuple("province_axis[%02d].%s" % (position, key)
            for position in range(31)
            for key in ("model_name", "annual_index", "annual_name",
                        "external.identifier_kind", "external.value_type",
                        "external.value", "source_position"))
    + tuple("aggregate_units." + key for key in AGGREGATE_KEYS)
    + tuple("combined_units." + key for key in COMBINED_KEYS)
    + tuple("stages." + slot + "." + key
            for slot, _ in STAGE_CONTRACT for key in ("stage", "evidence"))
    + tuple("evidence_refs." + key for key in EVIDENCE_KEYS)
)


def _require(condition, code):
    if not condition:
        raise ValueError(code)


def _unknown(value):
    return type(value) is str and value == UNKNOWN


def _label(value):
    _require(type(value) is str and bool(value) and value == value.strip(),
             "LABEL_TYPE_OR_FORMAT")


def _token(value):
    _label(value)
    _require(_unknown(value) or
             re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:/-]*", value) is not None,
             "TOKEN_FORMAT")


def _exact(value, cls):
    _require(type(value) is cls, "EXACT_METADATA_TYPE_REQUIRED")
    cls.__post_init__(value)


def _optional_index(value, low, high):
    _require(_unknown(value) or
             (type(value) is int and low <= value <= high),
             "INDEX_TYPE_OR_RANGE")


class _InactiveClaims:
    __slots__ = ()

    @property
    def classification(self):
        return "ARCHIVE_DERIVED"

    @property
    def source_authenticated(self):
        return False

    @property
    def original_live_identity_restored(self):
        return False

    @property
    def scientific_validity_established(self):
        return False

    @property
    def model_activation(self):
        return False

    @property
    def execution_admitted(self):
        return False


@dataclass(frozen=True, slots=True)
class EvidenceReference:
    reference_id: str = UNKNOWN

    def __post_init__(self):
        _require(type(self) is EvidenceReference, "EXACT_REFERENCE_REQUIRED")
        _label(self.reference_id)
        _require(_unknown(self.reference_id) or
                 re.fullmatch(r"ref:[A-Za-z0-9][A-Za-z0-9_.:/-]*",
                              self.reference_id) is not None,
                 "REFERENCE_TOKEN_FORMAT")


@dataclass(frozen=True, slots=True)
class SourceDeclaration:
    role: str
    source_identifier: str
    sha256: str
    evidence: EvidenceReference

    def __post_init__(self):
        _require(type(self) is SourceDeclaration, "EXACT_SOURCE_REQUIRED")
        _require(type(self.role) is str and
                 self.role in ("ARCHIVE_OBSERVED", "ANNUAL_DECLARED"),
                 "SOURCE_ROLE")
        _token(self.source_identifier)
        _require(type(self.sha256) is str and
                 (_unknown(self.sha256) or
                  re.fullmatch(r"[0-9A-Fa-f]{64}", self.sha256) is not None),
                 "SOURCE_PIN_FORMAT")
        _exact(self.evidence, EvidenceReference)


@dataclass(frozen=True, slots=True)
class ExternalIdentifier:
    identifier_kind: str
    value_type: str
    value: int | str

    def __post_init__(self):
        _require(type(self) is ExternalIdentifier, "EXACT_EXTERNAL_ID_REQUIRED")
        _require(type(self.identifier_kind) is str and
                 self.identifier_kind in
                 ("retained_panel_id", "source_identifier", UNKNOWN),
                 "EXTERNAL_IDENTIFIER_KIND")
        _require(type(self.value_type) is str and
                 self.value_type in ("int", "str", UNKNOWN),
                 "EXTERNAL_VALUE_TYPE")
        if _unknown(self.value):
            return
        _require(self.value_type != UNKNOWN, "KNOWN_ID_NEEDS_EXPLICIT_TYPE")
        if self.value_type == "int":
            _require(type(self.value) is int and self.value > 0,
                     "EXTERNAL_EXACT_POSITIVE_INT")
        else:
            _token(self.value)


@dataclass(frozen=True, slots=True)
class ProvinceCorrespondence:
    model_index: int
    model_name: str
    annual_index: int | str
    annual_name: str
    external: ExternalIdentifier
    source_position: int | str

    def __post_init__(self):
        _require(type(self) is ProvinceCorrespondence, "EXACT_PROVINCE_ROW")
        _require(type(self.model_index) is int and
                 0 <= self.model_index <= 30, "MODEL_EXACT_ZERO_INDEX")
        _label(self.model_name)
        _optional_index(self.annual_index, 1, 31)
        _label(self.annual_name)
        _exact(self.external, ExternalIdentifier)
        _optional_index(self.source_position, 0, 30)


@dataclass(frozen=True, slots=True)
class UnitDeclaration:
    key: str
    unit: str

    def __post_init__(self):
        _require(type(self) is UnitDeclaration, "EXACT_UNIT_REQUIRED")
        _token(self.key)
        _token(self.unit)


@dataclass(frozen=True, slots=True)
class StageDeclaration:
    slot: str
    stage: str
    evidence: EvidenceReference

    def __post_init__(self):
        _require(type(self) is StageDeclaration, "EXACT_STAGE_REQUIRED")
        _require(type(self.slot) is str and
                 self.slot in dict(STAGE_CONTRACT), "STAGE_SLOT")
        _require(type(self.stage) is str and
                 (_unknown(self.stage) or
                  self.stage == dict(STAGE_CONTRACT)[self.slot]),
                 "STAGE_VALUE")
        _exact(self.evidence, EvidenceReference)


@dataclass(frozen=True, slots=True)
class EvidenceItem:
    key: str
    evidence: EvidenceReference

    def __post_init__(self):
        _require(type(self) is EvidenceItem, "EXACT_EVIDENCE_ITEM")
        _require(type(self.key) is str and self.key in EVIDENCE_KEYS,
                 "EVIDENCE_KEY")
        _exact(self.evidence, EvidenceReference)


def _ordered_rows(rows, cls, keys):
    _require(type(rows) is tuple and len(rows) == len(keys),
             "EXACT_ORDERED_METADATA_TUPLE")
    for row, key in zip(rows, keys):
        _exact(row, cls)
        actual = row.slot if cls is StageDeclaration else row.key
        _require(actual == key, "METADATA_KEYS_OR_ORDER")


@dataclass(frozen=True, slots=True)
class ArchiveAdmissionDescriptor(_InactiveClaims):
    archive_observation: SourceDeclaration
    annual_source: SourceDeclaration
    province_axis: tuple
    aggregate_units: tuple
    combined_units: tuple
    stages: tuple
    evidence_refs: tuple

    def __post_init__(self):
        _require(type(self) is ArchiveAdmissionDescriptor,
                 "EXACT_DESCRIPTOR_REQUIRED")
        _exact(self.archive_observation, SourceDeclaration)
        _exact(self.annual_source, SourceDeclaration)
        _require(self.archive_observation.role == "ARCHIVE_OBSERVED" and
                 self.annual_source.role == "ANNUAL_DECLARED",
                 "SEPARATE_SOURCE_ROLES")
        _require(type(self.province_axis) is tuple and
                 len(self.province_axis) == 31, "EXPLICIT_31_PROVINCE_AXIS")
        model_names, annual_names, source_positions, external_ids = (
            set(), set(), set(), set()
        )
        for position, row in enumerate(self.province_axis):
            _exact(row, ProvinceCorrespondence)
            _require(row.model_index == position, "MODEL_AXIS_ORDER")
            if not _unknown(row.annual_index):
                _require(row.annual_index == position + 1,
                         "EXPLICIT_ANNUAL_AXIS_ORDER")
            for value, seen in ((row.model_name, model_names),
                                (row.annual_name, annual_names),
                                (row.source_position, source_positions)):
                if not _unknown(value):
                    _require(value not in seen, "DUPLICATE_AXIS_IDENTITY")
                    seen.add(value)
            if not _unknown(row.external.value):
                identity = (type(row.external.value), row.external.value)
                _require(identity not in external_ids, "DUPLICATE_TYPED_EXTERNAL_ID")
                external_ids.add(identity)
        _ordered_rows(self.aggregate_units, UnitDeclaration, AGGREGATE_KEYS)
        _ordered_rows(self.combined_units, UnitDeclaration, COMBINED_KEYS)
        combined = {row.key: row.unit for row in self.combined_units}
        for row in self.aggregate_units:
            if not _unknown(row.unit) and not _unknown(combined[row.key]):
                _require(row.unit == combined[row.key], "CONFLICTING_UNIT_DECLARATIONS")
        _require(_unknown(combined["S"]) or combined["S"] == "dimensionless",
                 "DECLARED_SHARE_UNIT")
        _ordered_rows(self.stages, StageDeclaration,
                      tuple(slot for slot, _ in STAGE_CONTRACT))
        _ordered_rows(self.evidence_refs, EvidenceItem, EVIDENCE_KEYS)


@dataclass(frozen=True, slots=True)
class AdmissionAssessment(_InactiveClaims):
    declaration_status: str
    missing_items: tuple
    rejection_reasons: tuple

    def __post_init__(self):
        _require(type(self) is AdmissionAssessment, "EXACT_ASSESSMENT_REQUIRED")
        _require(type(self.missing_items) is tuple and
                 all(type(item) is str for item in self.missing_items),
                 "IMMUTABLE_MISSING_CODES")
        _require(self.missing_items ==
                 tuple(code for code in _MISSING_ORDER if code in self.missing_items),
                 "FIXED_ORDERED_MISSING_CODES")
        _require(type(self.rejection_reasons) is tuple and
                 all(type(code) is str for code in self.rejection_reasons),
                 "EXACT_REJECTION_CODES")
        expected_status = ("DECLARATION_INCOMPLETE" if self.missing_items
                           else "DECLARATION_COMPLETE_ONLY")
        expected_reasons = (("MISSING_DECLARATIONS",) if self.missing_items else ()) + (
            "INACTIVE_EXECUTION_NOT_ADMITTED",
        )
        _require(type(self.declaration_status) is str and
                 self.declaration_status == expected_status and
                 type(self.rejection_reasons) is tuple and
                 self.rejection_reasons == expected_reasons,
                 "FIXED_INACTIVE_ASSESSMENT")


def assess_admission(descriptor):
    """Recheck metadata and return ordered unknowns; no evidence authentication."""
    _exact(descriptor, ArchiveAdmissionDescriptor)
    missing = []
    for name, source in (("archive_observation", descriptor.archive_observation),
                         ("annual_source", descriptor.annual_source)):
        for key, value in (("source_identifier", source.source_identifier),
                           ("sha256", source.sha256),
                           ("evidence", source.evidence.reference_id)):
            if _unknown(value):
                missing.append(name + "." + key)
    for position, row in enumerate(descriptor.province_axis):
        prefix = "province_axis[%02d]." % position
        for key, value in (
            ("model_name", row.model_name), ("annual_index", row.annual_index),
            ("annual_name", row.annual_name),
            ("external.identifier_kind", row.external.identifier_kind),
            ("external.value_type", row.external.value_type),
            ("external.value", row.external.value),
            ("source_position", row.source_position),
        ):
            if _unknown(value):
                missing.append(prefix + key)
    for name, units in (("aggregate_units", descriptor.aggregate_units),
                        ("combined_units", descriptor.combined_units)):
        for row in units:
            if _unknown(row.unit):
                missing.append(name + "." + row.key)
    for row in descriptor.stages:
        if _unknown(row.stage):
            missing.append("stages." + row.slot + ".stage")
        if _unknown(row.evidence.reference_id):
            missing.append("stages." + row.slot + ".evidence")
    for row in descriptor.evidence_refs:
        if _unknown(row.evidence.reference_id):
            missing.append("evidence_refs." + row.key)
    reasons = (("MISSING_DECLARATIONS",) if missing else ()) + (
        "INACTIVE_EXECUTION_NOT_ADMITTED",
    )
    return AdmissionAssessment(
        "DECLARATION_INCOMPLETE" if missing else "DECLARATION_COMPLETE_ONLY",
        tuple(missing), reasons,
    )
