"""Inactive, in-memory archive-input parser and defensively owned carrier."""

import hashlib
import json
import math
from dataclasses import dataclass


class ArchiveInputError(ValueError):
    """Validation failure containing only a static reason code."""


def _sequence(value):
    if type(value) not in (tuple, list):
        raise ArchiveInputError("INVALID_SEQUENCE")
    return tuple(value)


def _provenance(value):
    if type(value) is not str or value not in (
        "INVENTED", "ARCHIVE_DERIVED_DECLARED"
    ):
        raise ArchiveInputError("INVALID_PROVENANCE")
    return value


def _scalar(value):
    if type(value) is int:
        return value
    if type(value) is float and math.isfinite(value):
        return value
    raise ArchiveInputError("INVALID_NUMERIC_SCALAR")


def _owned_binding(value):
    rows = _sequence(value)
    if len(rows) != 31:
        raise ArchiveInputError("INVALID_BINDING_COUNT")
    owned = []
    for row in rows:
        row = _sequence(row)
        if len(row) != 3:
            raise ArchiveInputError("INVALID_BINDING_ROW")
        path, digest, size = row
        if type(path) is not str:
            raise ArchiveInputError("INVALID_LITERAL_PATH")
        if (
            type(digest) is not str
            or len(digest) != 64
            or any(character not in "0123456789abcdef" for character in digest)
        ):
            raise ArchiveInputError("INVALID_SHA256")
        if type(size) is not int or size < 0:
            raise ArchiveInputError("INVALID_BYTE_COUNT")
        owned.append((path, digest, size))
    binding = tuple(owned)
    if len(set(row[0] for row in binding)) != 31:
        raise ArchiveInputError("DUPLICATE_LITERAL_PATH")
    return binding


def _owned_inputs(paths, raw_bytes, binding):
    paths = _sequence(paths)
    raw_bytes = _sequence(raw_bytes)
    if len(paths) != 31 or len(raw_bytes) != 31:
        raise ArchiveInputError("INVALID_ENTRY_COUNT")
    if any(type(path) is not str for path in paths):
        raise ArchiveInputError("INVALID_LITERAL_PATH")
    if len(set(paths)) != 31:
        raise ArchiveInputError("DUPLICATE_LITERAL_PATH")
    if paths != tuple(row[0] for row in binding):
        raise ArchiveInputError("BINDING_PATH_ORDER_MISMATCH")
    owned = []
    for raw, row in zip(raw_bytes, binding):
        if type(raw) not in (bytes, bytearray):
            raise ArchiveInputError("INVALID_RAW_BYTES")
        raw = bytes(raw)
        if len(raw) != row[2]:
            raise ArchiveInputError("BYTE_COUNT_MISMATCH")
        if hashlib.sha256(raw).hexdigest() != row[1]:
            raise ArchiveInputError("SHA256_MISMATCH")
        owned.append(raw)
    return paths, tuple(owned)


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ArchiveInputError("DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def _reject_constant(value):
    raise ArchiveInputError("NONFINITE_JSON_CONSTANT")


def _json_integer(value):
    try:
        return int(value)
    except (ValueError, OverflowError):
        raise ArchiveInputError("INTEGER_JSON_REPRESENTABILITY_ERROR") from None


def _json_float(value):
    try:
        result = float(value)
    except (ValueError, OverflowError):
        raise ArchiveInputError("FLOAT_JSON_REPRESENTABILITY_ERROR") from None
    if not math.isfinite(result):
        raise ArchiveInputError("NONFINITE_JSON_NUMBER")
    mantissa = value.partition("e")[0].partition("E")[0]
    if result == 0.0 and any(character in "123456789" for character in mantissa):
        raise ArchiveInputError("FLOAT_JSON_UNDERFLOW")
    return result


def _parse_object(raw):
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeError:
        raise ArchiveInputError("INVALID_UTF8") from None
    try:
        result = json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
            parse_int=_json_integer,
            parse_float=_json_float,
        )
    except ArchiveInputError as error:
        raise ArchiveInputError(str(error)) from None
    except (ValueError, OverflowError, RecursionError):
        raise ArchiveInputError("INVALID_JSON_REPRESENTABILITY") from None
    if type(result) is not dict:
        raise ArchiveInputError("JSON_OBJECT_REQUIRED")
    return result


def _mass_form(document, key):
    if key not in document:
        raise ArchiveInputError("MISSING_REQUIRED_FIELD")
    section = document[key]
    if type(section) is not dict or "mass_form" not in section:
        raise ArchiveInputError("MISSING_REQUIRED_MASS_FORM")
    return _scalar(section["mass_form"])


@dataclass(frozen=True, slots=True)
class ArchiveInputCarrier:
    """Immutable owned inputs; declared provenance is not archive proof."""

    ct: tuple
    household_lt: tuple
    at: tuple
    at_tax: tuple
    paths: tuple
    raw_bytes: tuple
    binding: tuple
    provenance: str = "INVENTED"

    def __post_init__(self):
        provenance = _provenance(self.provenance)
        binding = _owned_binding(self.binding)
        paths, raw_bytes = _owned_inputs(self.paths, self.raw_bytes, binding)
        fields = []
        for values in (self.ct, self.household_lt, self.at, self.at_tax):
            values = _sequence(values)
            if len(values) != 31:
                raise ArchiveInputError("INVALID_FIELD_COUNT")
            fields.append(tuple(_scalar(value) for value in values))
        for name, value in zip(
            ("ct", "household_lt", "at", "at_tax"), fields
        ):
            object.__setattr__(self, name, value)
        object.__setattr__(self, "paths", paths)
        object.__setattr__(self, "raw_bytes", raw_bytes)
        object.__setattr__(self, "binding", binding)
        object.__setattr__(self, "provenance", provenance)

    def as_fields(self):
        return {
            "ct": self.ct,
            "lt": self.household_lt,
            "at": self.at,
            "at_tax": self.at_tax,
        }

    def metadata(self):
        return {
            "representation": "ARCHIVE_DERIVED_NEW_OBJECT",
            "provenance": self.provenance,
            "archive_provenance": "UNKNOWN",
            "runtime_identity": "UNKNOWN",
            "source_identity": "UNKNOWN",
            "unit": "UNKNOWN",
            "calendar": "UNKNOWN",
            "canonical_full_name": "UNKNOWN",
            "original_live_object_restored": False,
            "original_seal_restored": False,
            "original_lifetime_restored": False,
            "full_constructor": False,
        }


def parse_archive_inputs(raw_entries, expected_binding, *, provenance="INVENTED"):
    """Validate all bindings before parsing the four selected numeric fields."""
    provenance = _provenance(provenance)
    entries = _sequence(raw_entries)
    if len(entries) != 31:
        raise ArchiveInputError("INVALID_ENTRY_COUNT")
    paths = []
    raw_bytes = []
    for entry in entries:
        entry = _sequence(entry)
        if len(entry) != 2:
            raise ArchiveInputError("INVALID_ENTRY_ROW")
        paths.append(entry[0])
        raw_bytes.append(entry[1])
    binding = _owned_binding(expected_binding)
    paths, raw_bytes = _owned_inputs(paths, raw_bytes, binding)
    ct = []
    household_lt = []
    at = []
    at_tax = []
    for raw in raw_bytes:
        document = _parse_object(raw)
        ct.append(_mass_form(document, "Ct"))
        household_lt.append(_mass_form(document, "Lt"))
        at.append(_mass_form(document, "At"))
        at_tax.append(_mass_form(document, "AtTax"))
    return ArchiveInputCarrier(
        ct=ct,
        household_lt=household_lt,
        at=at,
        at_tax=at_tax,
        paths=paths,
        raw_bytes=raw_bytes,
        binding=binding,
        provenance=provenance,
    )
