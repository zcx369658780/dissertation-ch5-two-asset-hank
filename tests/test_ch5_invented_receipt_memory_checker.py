"""Artificial, inert SOURCE_ONLY test candidate. All tests NOT_RUN."""
import runpy
import unittest


MODULE_PATH = r"D:\ProjectTemp\c5k1bturn56\scripts\ch5_invented_receipt_memory_checker.py"


def tool(exit_token=b"0", output=b'"ok"', capture=b"true"):
    return (b'{"kind":"INVENTED_TOOL_RESULT_V1","result":{"exit_code":'
            + exit_token + b',"output":' + output
            + b'},"capture_complete":' + capture + b"}")


RECEIPT = (b'{"kind":"INVENTED_RECEIPT_V1","capture_complete":true,'
           b'"known_state_key_types":{"It":"NUMBER_INTEGER","it":"BOOLEAN"}}')


class InventedMemoryCheckerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Future execution loads only this fixed new source; no fixture/package.
        cls.inspect = staticmethod(
            runpy.run_path(MODULE_PATH)["inspect_invented_receipt"]
        )

    def check(self, payload, outcome, code):
        before = payload
        result = self.inspect(payload)
        self.assertIs(type(result), dict)
        self.assertEqual(set(result), {
            "outcome", "code", "source_authenticated",
            "original_live_identity_restored", "scientific_validity_established",
            "model_activation", "execution_admitted",
            "stdout_capture", "stderr_capture",
        })
        self.assertEqual(result["outcome"], outcome)
        self.assertEqual(result["code"], code)
        for key in ("source_authenticated", "original_live_identity_restored",
                    "scientific_validity_established", "model_activation",
                    "execution_admitted"):
            self.assertIs(result[key], False)
        for key in ("stdout_capture", "stderr_capture"):
            self.assertEqual(result[key], "NOT_SEPARATELY_CAPTURED")
        self.assertEqual(payload, before)
        self.assertIsNot(result, self.inspect(payload))
        return result

    def reject(self, payload, suffix):
        return self.check(payload, "REJECT", "REJECT__INVENTED_" + suffix)

    def test_tool_ok(self):
        self.check(tool(), "PASS", "PASS__INVENTED_TOOL_RESULT")

    def test_receipt_case_keys(self):
        self.check(RECEIPT, "PASS", "PASS__INVENTED_RECEIPT")

    def test_tool_outer_conflict(self):
        payload = tool()[:-1] + b',"exit_code":1}'
        self.reject(payload, "SCHEMA_EXTRA_OR_LAYER_CONFLICT")

    def test_tool_other_extra(self):
        self.reject(tool()[:-1] + b',"extra":null}',
                    "SCHEMA_EXTRA_OR_LAYER_CONFLICT")

    def test_tool_bool_exit(self):
        self.reject(tool(b"true"), "EXIT_TOKEN_TYPE")

    def test_tool_float_exit(self):
        self.reject(tool(b"0.0"), "EXIT_TOKEN_TYPE")

    def test_tool_missing_output(self):
        self.reject(tool().replace(b',"output":"ok"', b""), "SCHEMA_MISSING")

    def test_receipt_duplicate_key(self):
        self.reject(RECEIPT.replace(b'"It":"NUMBER_INTEGER"',
                    b'"It":"NUMBER_INTEGER","It":"NUMBER_INTEGER"'),
                    "DUPLICATE_KEY")

    def test_tool_tail_cut(self):
        self.check(tool()[:-1], "UNKNOWN", "UNKNOWN__INVENTED_INPUT_INCOMPLETE")

    def test_tool_capture_false(self):
        self.check(tool(capture=b"false"), "UNKNOWN",
                   "UNKNOWN__INVENTED_CAPTURE_INCOMPLETE")

    def test_tool_output_cut(self):
        self.check(tool(output=b'"[TRUNCATED]"'), "UNKNOWN",
                   "UNKNOWN__INVENTED_OUTPUT_TRUNCATED")

    def test_tool_observed_failure(self):
        self.check(tool(b"1"), "OBSERVED_FAILURE",
                   "OBSERVED_FAILURE__INVENTED_TOOL_EXIT")

    def test_exact_input_type_and_fresh_result(self):
        class BytesChild(bytes):
            pass
        for payload in (BytesChild(tool()), bytearray(tool()), "{}", None, {}):
            with self.subTest(input_type=type(payload).__name__):
                self.reject(payload, "INPUT_TYPE")
        result = self.check(tool(), "PASS", "PASS__INVENTED_TOOL_RESULT")
        result["model_activation"] = True
        self.check(tool(), "PASS", "PASS__INVENTED_TOOL_RESULT")

    def test_byte_cap(self):
        # JSON trailing whitespace is legal; author-constructed byte boundary.
        base = tool()
        self.check(base + b" " * (8192 - len(base)),
                   "PASS", "PASS__INVENTED_TOOL_RESULT")
        self.reject(base + b" " * (8193 - len(base)), "BYTE_CAP")

    def test_utf8_and_bom(self):
        self.reject(b'\xff', "UTF8")
        self.reject(b'\xef\xbb\xbf' + tool(), "BOM")

    def test_depth_boundary(self):
        # Each '[' enters one container, root depth 1; zero is a scalar.
        self.reject(b"[" * 8 + b"0" + b"]" * 8, "SCHEMA_TYPE")
        self.reject(b"[" * 9 + b"0" + b"]" * 9, "DEPTH_CAP")

    def test_token_boundary(self):
        # Array start/end=2; 510 scalar tokens =>512, 511=>513.
        self.reject(b"[" + b",".join([b"0"] * 510) + b"]", "SCHEMA_TYPE")
        self.reject(b"[" + b",".join([b"0"] * 511) + b"]", "TOKEN_CAP")

    def test_decoded_string_boundary(self):
        self.check(tool(output=b'"' + b"a" * 256 + b'"'),
                   "PASS", "PASS__INVENTED_TOOL_RESULT")
        self.reject(tool(output=b'"' + b"a" * 257 + b'"'), "STRING_CAP")
        # Each surrogate pair decodes to ONE Unicode code point.
        pair = b"\\uD83D\\uDE00"
        self.check(tool(output=b'"' + pair * 256 + b'"'),
                   "PASS", "PASS__INVENTED_TOOL_RESULT")
        self.reject(tool(output=b'"' + pair * 257 + b'"'), "STRING_CAP")
        direct = "\U0001f600".encode("utf-8")
        self.check(tool(output=b'"' + direct * 256 + b'"'),
                   "PASS", "PASS__INVENTED_TOOL_RESULT")
        self.reject(tool(output=b'"' + direct * 257 + b'"'), "STRING_CAP")
        self.reject(b'{"' + b"k" * 257 + b'":0}', "STRING_CAP")

    def test_surrogates_and_escapes(self):
        for output in (b'"\\uD800"', b'"\\uDC00"',
                       b'"\\uD800\\u0041"', b'"\\x"', b'"\x01"'):
            with self.subTest(output=output):
                self.reject(tool(output=output), "JSON_SYNTAX")

    def test_number_syntax_and_exit_limits(self):
        for token in (b"NaN", b"Infinity", b"-Infinity", b"01", b"1."):
            # A closing brace after '1.' makes it invalid, not EOF.
            with self.subTest(token=token):
                self.reject(tool(token), "JSON_SYNTAX")
        for token in (b"-0", b"0e0", b"0E+0", b"1.0"):
            with self.subTest(token=token):
                self.reject(tool(token), "EXIT_TOKEN_TYPE")
        for token in (b"256", b"-1", b"999999"):
            with self.subTest(token=token):
                self.reject(tool(token), "EXIT_RANGE")
        self.check(tool(b"255"), "OBSERVED_FAILURE",
                   "OBSERVED_FAILURE__INVENTED_TOOL_EXIT")

    def test_tail_and_incomplete_lexemes(self):
        self.reject(tool() + b"x", "JSON_SYNTAX")
        self.reject(b"[0,]", "JSON_SYNTAX")
        for payload in (b"", b'{"a":', b'"abc', b"tru",
                        b"-", b"1.", b"1e+", b'"\\u12'):
            with self.subTest(payload=payload):
                self.check(payload, "UNKNOWN",
                           "UNKNOWN__INVENTED_INPUT_INCOMPLETE")

    def test_key_order_and_schema_priority(self):
        # Root extra beats missing and field type in either input key order.
        for payload in (
            b'{"kind":"INVENTED_TOOL_RESULT_V1","extra":0,"capture_complete":0}',
            b'{"capture_complete":0,"extra":0,"kind":"INVENTED_TOOL_RESULT_V1"}',
        ):
            self.reject(payload, "SCHEMA_EXTRA_OR_LAYER_CONFLICT")
        # Nested extra beats nested missing; capture type precedes exit type.
        self.reject(tool().replace(b'"output":"ok"', b'"extra":0'),
                    "SCHEMA_EXTRA_OR_LAYER_CONFLICT")
        self.reject(tool(b"true", capture=b"0"), "SCHEMA_TYPE")
        self.reject(tool().replace(b'"result":{', b'"result":[')
                    .replace(b'},"capture_complete"', b'],"capture_complete"'),
                    "JSON_SYNTAX")

    def test_marker_scope_and_priority(self):
        for output in (b'"[TRUNCATED]"', b'"\\u005bTRUNCATED\\u005d"'):
            self.check(tool(output=output, capture=b"false"), "UNKNOWN",
                       "UNKNOWN__INVENTED_OUTPUT_TRUNCATED")
        self.reject(tool()[:-1] + b',"extra":"[TRUNCATED]"}',
                    "SCHEMA_EXTRA_OR_LAYER_CONFLICT")
        self.reject(RECEIPT.replace(b"NUMBER_INTEGER", b"[TRUNCATED]"),
                    "RECEIPT_LABEL")
        self.reject(tool(b"true", output=b'"[TRUNCATED]"'), "EXIT_TOKEN_TYPE")
        self.reject(tool(output=b'"[TRUNCATED]' + b"a" * 256 + b'"'),
                    "STRING_CAP")

    def test_remaining_schema_rejections(self):
        cases = (
            (b"null", "SCHEMA_TYPE"),
            (b'{}', "SCHEMA_KIND"),
            (b'{"kind":true}', "SCHEMA_KIND"),
            (b'{"kind":"OTHER"}', "SCHEMA_KIND"),
            (tool().replace(b'"result":{"exit_code":0,"output":"ok"}',
                            b'"result":null'), "SCHEMA_TYPE"),
            (tool(output=b"null"), "SCHEMA_TYPE"),
            (RECEIPT.replace(b'"It":"NUMBER_INTEGER"', b'"It":true'),
             "SCHEMA_TYPE"),
            (RECEIPT.replace(b'"it":"BOOLEAN"', b'"IT":"BOOLEAN"'),
             "SCHEMA_EXTRA_OR_LAYER_CONFLICT"),
            (RECEIPT.replace(b'"it":"BOOLEAN"', b'"it":"number_integer"'),
             "RECEIPT_LABEL"),
        )
        for payload, suffix in cases:
            with self.subTest(suffix=suffix):
                self.reject(payload, suffix)
        self.check(RECEIPT.replace(b'"capture_complete":true',
                                   b'"capture_complete":false'),
                   "UNKNOWN", "UNKNOWN__INVENTED_CAPTURE_INCOMPLETE")


if __name__ == "__main__":
    unittest.main()
