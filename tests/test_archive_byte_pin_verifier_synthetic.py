"""Inert test preparation: invented bytes only; NOT_RUN in source-only task."""

from dataclasses import FrozenInstanceError, replace
import importlib.util
import sys
import unittest
from unittest.mock import patch

_VERIFIER_MODULE_NAME = "ch5_invented_bytes_pin_verifier_check_20261004"
_VERIFIER_MODULE_PATH = (
    r"D:\ProjectTemp\c5k1bturn56\validators\multi_province"
    r"\annual_observed_labor_diagnostic\archive_byte_pin_verifier.py"
)
_verifier_spec = importlib.util.spec_from_file_location(
    _VERIFIER_MODULE_NAME, _VERIFIER_MODULE_PATH
)
if _verifier_spec is None or _verifier_spec.loader is None:
    raise RuntimeError("VERIFIER_SPEC_UNAVAILABLE")
if _VERIFIER_MODULE_NAME in sys.modules:
    raise RuntimeError("VERIFIER_MODULE_NAME_IN_USE")
verifier = importlib.util.module_from_spec(_verifier_spec)
sys.modules[_VERIFIER_MODULE_NAME] = verifier
_verifier_spec.loader.exec_module(verifier)


TEST_PIN = "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"


class ArchiveBytePinVerifierSyntheticTests(unittest.TestCase):
    def declaration(self, **changes):
        fields = dict(
            role="STATE_JSON", source_identifier="invented-source",
            source_path_label="invented-label", expected_length=3,
            byte_cap=3, expected_sha256=TEST_PIN,
        )
        fields.update(changes)
        return verifier.ArchiveBytePinDeclaration(**fields)

    def test_match_and_exactly_one_hash(self):
        original_hash = verifier.hashlib.sha256
        with patch.object(verifier.hashlib, "sha256", wraps=original_hash) as spy:
            result = verifier.verify_archive_byte_pin(self.declaration(), b"abc")
        self.assertEqual(spy.call_count, 1)
        self.assertEqual(result.code, "MATCH")
        self.assertTrue(result.byte_identity_matches_declared_pin)
        self.assertEqual(result.actual_size, 3)
        self.assertEqual(result.actual_sha256, TEST_PIN)

    def test_changed_byte_and_wrong_pin(self):
        for declaration, payload in (
            (self.declaration(), b"abd"),
            (self.declaration(expected_sha256="0" * 64), b"abc"),
        ):
            with self.subTest(payload_length=len(payload)):
                original_hash = verifier.hashlib.sha256
                with patch.object(verifier.hashlib, "sha256", wraps=original_hash) as spy:
                    result = verifier.verify_archive_byte_pin(declaration, payload)
                self.assertEqual(result.code, "SHA256_MISMATCH")
                self.assertFalse(result.byte_identity_matches_declared_pin)
                self.assertEqual(spy.call_count, 1)

    def test_pre_hash_rejections_and_no_raw_payload(self):
        class BytesSubclass(bytes):
            pass

        cases = (
            (object(), b"abc", "DECLARATION_TYPE"),
            (self.declaration(), bytearray(b"abc"), "PAYLOAD_TYPE"),
            (self.declaration(), memoryview(b"abc"), "PAYLOAD_TYPE"),
            (self.declaration(), BytesSubclass(b"abc"), "PAYLOAD_TYPE"),
            (self.declaration(byte_cap=4), b"ab", "LENGTH_MISMATCH"),
            (self.declaration(), b"abcd", "CAP_EXCEEDED"),
        )
        with patch.object(verifier.hashlib, "sha256") as spy:
            for declaration, payload, code in cases:
                with self.subTest(code=code, payload_type=type(payload).__name__):
                    result = verifier.verify_archive_byte_pin(declaration, payload)
                    self.assertEqual(result.code, code)
                    self.assertIsNone(result.actual_sha256)
                    self.assertFalse(hasattr(result, "payload"))
                    self.assertNotIn("b'abc", repr(result))
            spy.assert_not_called()

    def test_invalid_declarations_have_fixed_codes(self):
        cases = (
            ({"expected_length": True}, "DECLARATION_LENGTH"),
            ({"expected_length": 3.0}, "DECLARATION_LENGTH"),
            ({"byte_cap": True}, "DECLARATION_CAP"),
            ({"byte_cap": 3.0}, "DECLARATION_CAP"),
            ({"expected_length": 0}, "DECLARATION_LENGTH"),
            ({"byte_cap": 0}, "DECLARATION_CAP"),
            ({"byte_cap": 2}, "DECLARATION_LENGTH_CAP"),
            ({"role": "UNKNOWN"}, "DECLARATION_ROLE"),
            ({"source_identifier": " "}, "DECLARATION_LABEL"),
            ({"source_path_label": None}, "DECLARATION_LABEL"),
            ({"source_identifier": "UNKNOWN"}, "DECLARATION_LABEL"),
            ({"source_path_label": "UNKNOWN"}, "DECLARATION_LABEL"),
            ({"source_identifier": " unknown "}, "DECLARATION_LABEL"),
            ({"source_path_label": " UNKNOWN "}, "DECLARATION_LABEL"),
            ({"expected_sha256": "UNKNOWN"}, "DECLARATION_PIN"),
            ({"expected_sha256": ""}, "DECLARATION_PIN"),
            ({"expected_sha256": "g" * 64}, "DECLARATION_PIN"),
        )
        for changes, code in cases:
            with self.subTest(code=code, fields=tuple(changes)):
                with self.assertRaises(ValueError) as raised:
                    self.declaration(**changes)
                self.assertEqual(str(raised.exception), code)

    def test_direct_result_rejects_invalid_metadata_and_payload_injection(self):
        class StringSubclass(str):
            pass

        cases = (
            ({"code": "UNKNOWN"}, "RESULT_CODE"),
            ({"code": StringSubclass("MATCH")}, "RESULT_CODE"),
            ({"code": b"MATCH"}, "RESULT_CODE"),
            ({"role": "UNKNOWN"}, "RESULT_ROLE"),
            ({"role": StringSubclass("STATE_JSON")}, "RESULT_ROLE"),
            ({"role": []}, "RESULT_ROLE"),
            ({"actual_size": True}, "RESULT_SIZE"),
            ({"actual_size": 3.0}, "RESULT_SIZE"),
            ({"actual_size": -1}, "RESULT_SIZE"),
            ({"actual_size": {}}, "RESULT_SIZE"),
            ({"actual_sha256": "g" * 64}, "RESULT_PIN"),
            ({"actual_sha256": ""}, "RESULT_PIN"),
            ({"actual_sha256": TEST_PIN.encode("ascii")}, "RESULT_PIN"),
            ({"actual_sha256": []}, "RESULT_PIN"),
            ({"actual_sha256": StringSubclass(TEST_PIN)}, "RESULT_PIN"),
        )
        for label_name in ("source_identifier", "source_path_label"):
            for invalid_label in (
                b"abc", [], {}, "", " ", "UNKNOWN", " unknown ",
                StringSubclass("invented-label"),
            ):
                cases += (({label_name: invalid_label}, "RESULT_LABEL"),)
        for changes, code in cases:
            with self.subTest(code=code, fields=tuple(changes)):
                fields = {"code": "MATCH"}
                fields.update(changes)
                with self.assertRaises(ValueError) as raised:
                    verifier.ArchiveBytePinVerification(**fields)
                self.assertEqual(str(raised.exception), code)
                self.assertNotIn("b'abc'", str(raised.exception))

    def test_result_subclass_rejected_and_empty_observation_allowed(self):
        class ResultSubclass(verifier.ArchiveBytePinVerification):
            pass

        with self.assertRaisesRegex(ValueError, "^RESULT_TYPE$"):
            ResultSubclass("MATCH")
        result = verifier.ArchiveBytePinVerification(
            "LENGTH_MISMATCH", actual_size=0
        )
        self.assertEqual(result.actual_size, 0)
        self.assertIsNone(result.actual_sha256)

    def test_uppercase_pin_and_opaque_role(self):
        declaration = self.declaration(
            role="FROZEN_SHARE_OPAQUE_NPZ", expected_sha256=TEST_PIN.upper()
        )
        result = verifier.verify_archive_byte_pin(declaration, b"abc")
        self.assertEqual(result.code, "MATCH")
        self.assertEqual(result.role, "FROZEN_SHARE_OPAQUE_NPZ")

    def test_hash_failure_does_not_echo_exception(self):
        with patch.object(verifier.hashlib, "sha256", side_effect=RuntimeError("b'abc'")):
            result = verifier.verify_archive_byte_pin(self.declaration(), b"abc")
        self.assertEqual(result.code, "HASH_FAILURE")
        self.assertIsNone(result.actual_sha256)
        self.assertNotIn("b'abc'", repr(result))

    def test_authority_flags_cannot_be_enabled(self):
        result = verifier.ArchiveBytePinVerification("MATCH")
        for name in (
            "source_authenticated", "original_live_identity_restored",
            "scientific_validity_established", "model_activation", "execution_admitted",
        ):
            with self.subTest(name=name):
                self.assertIs(getattr(result, name), False)
                with self.assertRaises(TypeError):
                    verifier.ArchiveBytePinVerification("MATCH", **{name: True})
                with self.assertRaises((FrozenInstanceError, AttributeError, TypeError)):
                    setattr(result, name, True)
        with self.assertRaises(FrozenInstanceError):
            result.code = "OTHER"
        declaration = self.declaration()
        with self.assertRaises(FrozenInstanceError):
            declaration.byte_cap = 99
        with self.assertRaisesRegex(ValueError, "^DECLARATION_CAP$"):
            replace(declaration, byte_cap=True)


if __name__ == "__main__":
    unittest.main(failfast=True)
