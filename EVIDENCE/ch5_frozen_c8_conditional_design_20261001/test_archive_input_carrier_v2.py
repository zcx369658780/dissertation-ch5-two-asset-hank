"""Wholly invented V2 construction checks; only the main agent may execute."""

import hashlib
import json
import sys
import unittest

from archive_input_carrier_v2 import ArchiveInputCarrier, ArchiveInputError, parse_archive_inputs


FIELDS = ("Ct", "Lt", "At", "AtTax")
BUILDERS = (("DIRECT", ArchiveInputCarrier), ("FACTORY", parse_archive_inputs))
FORBIDDEN_PREFIXES = ("numpy", "scipy", "pandas", "matlab", "ch5")


def receipt(index):
    return {
        "Ct": {"mass_form": index + 1},
        "Lt": {"mass_form": -(index + 2)},
        "At": {"mass_form": index + 0.25},
        "AtTax": {"mass_form": -(index + 0.5)},
        "INVENTED_EXTRA": {"mass_form": 777},
    }


def encoded(value):
    return json.dumps(value, separators=(",", ":")).encode("utf-8")


def entries():
    return [("INVENTED_ONLY/receipt_%02d.json" % i, encoded(receipt(i))) for i in range(31)]


def binding_for(raw):
    return [(path, hashlib.sha256(bytes(blob)).hexdigest(), len(blob)) for path, blob in raw]


class SafeResult(unittest.TextTestResult):
    def _exc_info_to_string(self, err, test):
        return "STATIC_TEST_FAILURE"


class ArchiveInputCarrierV2Tests(unittest.TestCase):
    def reject(self, raw, binding=None, expected_code=None, **kwargs):
        if binding is None:
            binding = binding_for(raw)
        for label, builder in BUILDERS:
            with self.subTest(builder=label):
                with self.assertRaises(ArchiveInputError, msg="EXPECTED_STATIC_REJECTION") as caught:
                    builder(raw, binding, **kwargs)
                message = str(caught.exception)
                self.assertTrue(bool(message), "EMPTY_ERROR_CODE")
                self.assertTrue("INVENTED_ONLY" not in message, "ERROR_PATH_LEAK")
                self.assertTrue("INVENTED_EXTRA" not in message, "ERROR_PAYLOAD_LEAK")
                self.assertTrue("917349" not in message, "ERROR_NUMERIC_LEAK")
                if expected_code is not None:
                    self.assertTrue(message == expected_code, "STATIC_ERROR_CODE")

    def test_direct_constructor_factory_same_bytes_same_fields(self):
        raw = entries()
        value = receipt(0)
        value["Ct"]["mass_form"] = 2 ** 100 + 917349
        raw[0] = (raw[0][0], encoded(value))
        pins = binding_for(raw)
        direct = ArchiveInputCarrier(raw, pins)
        factory = parse_archive_inputs(raw, pins)
        for attr in ("ct", "household_lt", "at", "at_tax"):
            left, right = getattr(direct, attr), getattr(factory, attr)
            self.assertTrue(left == right, "DIRECT_FACTORY_VALUES")
            self.assertTrue(tuple(type(v) for v in left) == tuple(type(v) for v in right), "DIRECT_FACTORY_TYPES")
        self.assertTrue(direct.paths == factory.paths, "DIRECT_FACTORY_PATHS")
        self.assertTrue(direct.binding == factory.binding, "DIRECT_FACTORY_BINDING")
        self.assertTrue(direct.raw_bytes == factory.raw_bytes, "DIRECT_FACTORY_BYTES")

    def test_all_caller_field_overrides_are_unsupported(self):
        raw = entries()
        pins = binding_for(raw)
        for attr in ("ct", "household_lt", "at", "at_tax"):
            for label, builder in BUILDERS:
                with self.subTest(field=attr, builder=label):
                    override = {attr: tuple(False for _ in range(31))}
                    with self.assertRaises(TypeError, msg="CALLER_OVERRIDE_UNSUPPORTED"):
                        builder(raw, pins, **override)

    def test_order_exact_types_mapping_and_negative_values(self):
        raw = entries()
        value = receipt(0)
        expected_large = 2 ** 100 + 917349
        value["Ct"]["mass_form"] = expected_large
        raw[0] = (raw[0][0], encoded(value))
        for label, builder in BUILDERS:
            with self.subTest(builder=label):
                carrier = builder(raw, binding_for(raw))
                for attr in ("ct", "household_lt", "at", "at_tax"):
                    self.assertTrue(type(getattr(carrier, attr)) is tuple, "FIELD_TUPLE")
                    self.assertTrue(len(getattr(carrier, attr)) == 31, "EXACT_COUNT")
                self.assertTrue(type(carrier.ct[0]) is int, "LARGE_INT_TYPE")
                self.assertTrue(carrier.ct[0] == expected_large, "LARGE_INT_EXACT")
                self.assertTrue(carrier.ct[1:] == tuple(i + 1 for i in range(1, 31)), "CT_ORDER")
                self.assertTrue(carrier.household_lt == tuple(-(i + 2) for i in range(31)), "LT_ORDER")
                self.assertTrue(carrier.at == tuple(i + 0.25 for i in range(31)), "AT_ORDER")
                self.assertTrue(carrier.at_tax == tuple(-(i + 0.5) for i in range(31)), "ATTAX_ORDER")
                self.assertTrue(type(carrier.at[0]) is float, "FLOAT_TYPE")
                mapped = carrier.as_fields()
                self.assertTrue(set(mapped) == {"ct", "lt", "at", "at_tax"}, "ONLY_FIELD_KEYS")
                self.assertTrue(mapped["lt"] is carrier.household_lt, "LT_ALIAS")
                self.assertTrue(mapped["ct"] is carrier.ct, "CT_ALIAS")

    def test_signed_float_zero_type_and_sign_preserved(self):
        raw = entries()
        value = receipt(0)
        value["Ct"]["mass_form"] = -0.0
        value["Lt"]["mass_form"] = 0.0
        raw[0] = (raw[0][0], encoded(value))
        for label, builder in BUILDERS:
            with self.subTest(builder=label):
                carrier = builder(raw, binding_for(raw))
                self.assertTrue(type(carrier.ct[0]) is float, "NEGATIVE_ZERO_TYPE")
                self.assertTrue(type(carrier.household_lt[0]) is float, "POSITIVE_ZERO_TYPE")
                self.assertTrue(carrier.ct[0].hex() == (-0.0).hex(), "NEGATIVE_ZERO_SIGN")
                self.assertTrue(carrier.household_lt[0].hex() == (0.0).hex(), "POSITIVE_ZERO_SIGN")

    def test_hash_case_canonicalization_preserves_binding_identity(self):
        raw = entries()
        lower = binding_for(raw)
        upper = [(path, digest.upper(), size) for path, digest, size in lower]
        mixed = [(path, "".join(c.upper() if i % 2 else c.lower() for i, c in enumerate(digest)), size) for path, digest, size in lower]
        for label, builder in BUILDERS:
            for case, pins in (("LOWER", lower), ("UPPER", upper), ("MIXED", mixed)):
                with self.subTest(builder=label, case=case):
                    carrier = builder(raw, pins)
                    self.assertTrue(carrier.binding == tuple(lower), "CANONICAL_BINDING")
                    self.assertTrue(carrier.paths == tuple(path for path, _ in raw), "PATH_ORDER_UNCHANGED")
                    self.assertTrue(carrier.raw_bytes == tuple(blob for _, blob in raw), "RAW_BYTES_UNCHANGED")
                    self.assertTrue(tuple(pin[2] for pin in carrier.binding) == tuple(len(blob) for _, blob in raw), "BYTE_COUNTS_UNCHANGED")

    def test_exact_count_and_literal_distinct_paths(self):
        for case, count in (("EMPTY", 0), ("SHORT", 30), ("LONG", 32)):
            with self.subTest(case=case):
                raw = entries()
                if count == 32:
                    raw.append(("INVENTED_ONLY/receipt_31.json", encoded(receipt(31))))
                else:
                    raw = raw[:count]
                self.reject(raw)
        raw = entries()
        raw[1] = (raw[0][0], raw[1][1])
        self.reject(raw)

    def test_pins_digest_size_count_path_order_and_binding_reorder(self):
        for case in ("DIGEST", "SIZE", "COUNT", "PATH", "ORDER", "BINDING_REORDER", "BYTES"):
            with self.subTest(case=case):
                raw = entries()
                pins = binding_for(raw)
                path, digest, size = pins[1]
                if case == "DIGEST":
                    pins[1] = (path, "0" * 64, size)
                elif case == "SIZE":
                    pins[1] = (path, digest, size + 1)
                elif case == "COUNT":
                    pins.pop()
                elif case == "PATH":
                    pins[1] = ("INVENTED_ONLY/other.json", digest, size)
                elif case == "ORDER":
                    raw[0], raw[1] = raw[1], raw[0]
                elif case == "BYTES":
                    raw[1] = (path, raw[1][1].replace(b"777", b"778"))
                else:
                    pins[0], pins[1] = pins[1], pins[0]
                self.reject(raw, pins)

    def test_entry_and_binding_types(self):
        for case in ("PATH", "BLOB", "ENTRY", "DIGEST", "SIZE_BOOL", "SIZE_FLOAT"):
            with self.subTest(case=case):
                raw = entries()
                pins = binding_for(raw)
                if case == "PATH":
                    raw[0] = (917349, raw[0][1])
                elif case == "BLOB":
                    raw[0] = (raw[0][0], "INVENTED_EXTRA")
                elif case == "ENTRY":
                    raw[0] = (raw[0][0], raw[0][1], "INVENTED_EXTRA")
                elif case == "DIGEST":
                    pins[0] = (pins[0][0], 917349, pins[0][2])
                elif case == "SIZE_BOOL":
                    pins[0] = (pins[0][0], pins[0][1], True)
                else:
                    pins[0] = (pins[0][0], pins[0][1], float(pins[0][2]))
                self.reject(raw, pins)

    def test_every_pin_is_checked_before_json_parsing(self):
        for case, code in (("DIGEST", "SHA256_MISMATCH"), ("SIZE", "BYTE_COUNT_MISMATCH"), ("PATH", "BINDING_PATH_ORDER_MISMATCH")):
            with self.subTest(case=case):
                raw = entries()
                raw[0] = (raw[0][0], b'{"INVENTED_EXTRA":917349')
                pins = binding_for(raw)
                path, digest, size = pins[-1]
                if case == "DIGEST":
                    pins[-1] = (path, "0" * 64, size)
                elif case == "SIZE":
                    pins[-1] = (path, digest, size + 1)
                else:
                    pins[-1] = ("INVENTED_ONLY/other.json", digest, size)
                self.reject(raw, pins, expected_code=code)

    def test_strict_json_duplicate_keys_constants_overflow_and_malformed(self):
        blobs = (
            b'{"Ct":{"mass_form":1,"mass_form":2},"Lt":{"mass_form":1},"At":{"mass_form":1},"AtTax":{"mass_form":1}}',
            b'{"Ct":{"mass_form":1},"Ct":{"mass_form":2},"Lt":{"mass_form":1},"At":{"mass_form":1},"AtTax":{"mass_form":1}}',
            b'{"Ct":{"mass_form":NaN},"Lt":{"mass_form":1},"At":{"mass_form":1},"AtTax":{"mass_form":1}}',
            b'{"Ct":{"mass_form":Infinity},"Lt":{"mass_form":1},"At":{"mass_form":1},"AtTax":{"mass_form":1}}',
            b'{"Ct":{"mass_form":-Infinity},"Lt":{"mass_form":1},"At":{"mass_form":1},"AtTax":{"mass_form":1}}',
            b'{"Ct":{"mass_form":1e9999},"Lt":{"mass_form":1},"At":{"mass_form":1},"AtTax":{"mass_form":1}}',
            b'{"INVENTED_EXTRA":917349', b'[]', b'null', b'\xff',
        )
        for index, blob in enumerate(blobs):
            with self.subTest(case="STRICT_JSON", index=index):
                raw = entries()
                raw[0] = (raw[0][0], blob)
                self.reject(raw)

    def test_all_fields_missing_and_non_numeric(self):
        for field in FIELDS:
            for case in ("MISSING_FIELD", "MISSING_MASS", "BOOL", "STRING", "NULL", "LIST", "OBJECT", "SCALAR_CONTAINER"):
                with self.subTest(field=field, case=case):
                    value = receipt(0)
                    if case == "MISSING_FIELD":
                        del value[field]
                    elif case == "MISSING_MASS":
                        value[field] = {}
                    elif case == "SCALAR_CONTAINER":
                        value[field] = 917349
                    else:
                        value[field]["mass_form"] = {"BOOL": True, "STRING": "917349", "NULL": None, "LIST": [917349], "OBJECT": {"INVENTED_EXTRA": 917349}}[case]
                    raw = entries()
                    raw[0] = (raw[0][0], encoded(value))
                    self.reject(raw)

    def test_nonzero_float_token_underflow_is_rejected(self):
        raw = entries()
        raw[0] = (raw[0][0], b'{"Ct":{"mass_form":1e-9999},"Lt":{"mass_form":1},"At":{"mass_form":1},"AtTax":{"mass_form":1}}')
        self.reject(raw, expected_code="FLOAT_JSON_UNDERFLOW")

    def test_defensive_capture_container_ownership_and_immutable_aliases(self):
        for label, builder in BUILDERS:
            with self.subTest(builder=label):
                raw = [[path, bytearray(blob)] for path, blob in entries()]
                pins = [list(pin) for pin in binding_for(raw)]
                carrier = builder(raw, pins)
                self.assertTrue(not hasattr(carrier, "__dict__"), "NO_MUTABLE_INSTANCE_DICT")
                captured, captured_path, captured_pin = carrier.raw_bytes[0], carrier.paths[0], carrier.binding[0]
                raw[0][1][:] = b"INVENTED_EXTRA"
                raw[0][0] = "INVENTED_ONLY/mutated.json"
                pins[0][0] = "INVENTED_ONLY/mutated.json"
                raw.clear()
                pins.clear()
                self.assertTrue(type(captured) is bytes, "BYTES_CAPTURE")
                self.assertTrue(carrier.raw_bytes[0] == captured, "BLOB_OWNERSHIP")
                self.assertTrue(carrier.paths[0] == captured_path, "PATH_OWNERSHIP")
                self.assertTrue(carrier.binding[0] == captured_pin, "BINDING_OWNERSHIP")
                self.assertTrue(type(carrier.paths) is tuple and type(carrier.raw_bytes) is tuple, "METADATA_TUPLES")
                self.assertTrue(type(carrier.binding) is tuple and type(carrier.binding[0]) is tuple, "BINDING_TUPLES")
                with self.assertRaises((AttributeError, TypeError), msg="FROZEN_ASSIGNMENT"):
                    carrier.ct = (917349,)
                with self.assertRaises(TypeError, msg="FROZEN_TUPLE"):
                    carrier.ct[0] = 917349
                first, second = carrier.as_fields(), carrier.as_fields()
                first["ct"] = (917349,)
                first["INVENTED_EXTRA"] = 917349
                self.assertTrue(first is not second, "FRESH_FIELDS")
                self.assertTrue(second["ct"] is carrier.ct, "FIELDS_DEFENSIVE")
                self.assertTrue("INVENTED_EXTRA" not in carrier.as_fields(), "EXTRA_UNMAPPED")

    def test_repeat_initialization_rejected_without_state_change(self):
        for label, builder in BUILDERS:
            with self.subTest(builder=label):
                original = entries()
                carrier = builder(original, binding_for(original))
                before_fields, before_binding, before_bytes = carrier.as_fields(), carrier.binding, carrier.raw_bytes
                changed = entries()
                value = receipt(0)
                value["Ct"]["mass_form"] = 917349
                changed[0] = (changed[0][0], encoded(value))
                with self.assertRaises(ArchiveInputError, msg="REINITIALIZATION_REJECTED") as caught:
                    carrier.__init__(changed, binding_for(changed))
                self.assertTrue(str(caught.exception) == "CARRIER_ALREADY_INITIALIZED", "STATIC_REINITIALIZATION_CODE")
                self.assertTrue(carrier.as_fields() == before_fields, "REINITIALIZATION_FIELDS_RETAINED")
                self.assertTrue(carrier.binding == before_binding, "REINITIALIZATION_BINDING_RETAINED")
                self.assertTrue(carrier.raw_bytes == before_bytes, "REINITIALIZATION_BYTES_RETAINED")

    def test_metadata_provenance_is_classification_only(self):
        for provenance in ("INVENTED", "ARCHIVE_DERIVED_DECLARED"):
            for label, builder in BUILDERS:
                with self.subTest(builder=label, provenance=provenance):
                    raw = entries()
                    carrier = builder(raw, binding_for(raw), provenance=provenance)
                    first, second = carrier.metadata(), carrier.metadata()
                    self.assertTrue(first is not second, "FRESH_METADATA")
                    self.assertTrue(second["representation"] == "ARCHIVE_DERIVED_NEW_OBJECT", "REPRESENTATION")
                    self.assertTrue(second["provenance"] == provenance, "DECLARED_CLASSIFICATION")
                    for key in ("archive_provenance", "runtime_identity", "source_identity", "unit", "calendar", "canonical_full_name"):
                        self.assertTrue(second[key] == "UNKNOWN", "NO_PROOF_METADATA")
                    for key in ("original_live_object_restored", "original_seal_restored", "original_lifetime_restored", "full_constructor"):
                        self.assertTrue(second[key] is False, "NO_RESTORATION_CLAIM")
                    first["provenance"] = "INVENTED_EXTRA"
                    first["full_constructor"] = True
                    self.assertTrue(carrier.metadata()["provenance"] == provenance, "METADATA_DEFENSIVE")
                    self.assertTrue(carrier.metadata()["full_constructor"] is False, "CONSTRUCTOR_DEFENSIVE")
        self.reject(entries(), provenance="UNKNOWN")

    def test_no_scientific_module_imports(self):
        raw = entries()
        for _, builder in BUILDERS:
            builder(raw, binding_for(raw))
        self.assertTrue(not any(name == prefix or name.startswith(prefix + ".") for name in sys.modules for prefix in FORBIDDEN_PREFIXES), "SCIENTIFIC_NAMESPACE_PRESENT")


if __name__ == "__main__":
    unittest.main(testRunner=unittest.TextTestRunner(resultclass=SafeResult))
