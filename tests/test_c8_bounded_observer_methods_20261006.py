"""Isolated implementation checks; synthetic bytes and intercepted I/O only."""
import contextlib
import hashlib
import importlib.util
import importlib.machinery
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, patch
SOURCE = Path(r"D:\ProjectTemp\c5k1bturn56\scripts\ch5_original_c8_state_share_observer_20261006_v1.py")
class ExactLoader(importlib.machinery.SourceFileLoader):
 def get_code(self, fullname):
  return self.source_to_code(self.get_data(self.path), self.path)
spec = importlib.util.spec_from_file_location("c8_isolated", SOURCE, loader=ExactLoader("c8_isolated", str(SOURCE)))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
SENTINEL = "SENSITIVE_SENTINEL_VALUE_9381"
RESULT = None
IO_ATTEMPT = False
def deny_io(event, args):
 global IO_ATTEMPT
 if event in ("open", "os.mkdir", "os.remove", "os.rename", "os.rmdir"):
  IO_ATTEMPT = True
  if RESULT is not None:
   RESULT.stop()
  raise RuntimeError("REAL_IO_BLOCKED")
sys.addaudithook(deny_io)
def fixture():
 row = dict(province_index=1, province=SENTINEL, classification=SENTINEL,
   raw_ra0_turn7=7, firm_ra_used=0.5,
   state={"It": 1, "it": True, "secret": SENTINEL})
 obj = dict(status=SENTINEL, classification=SENTINEL,
   raw_next_payoff_sha256="A"*64,
   k1b_portfolio_share_plan_sha256="B"*64,
   source_completed_turn7_raw_ra0_sha256="C"*64,
   rows=[dict(row) for _ in range(31)], secret=SENTINEL)
 return obj
def payload(obj=None):
 return json.dumps(fixture() if obj is None else obj).encode("utf-8")
def run_main(data=None, mismatch=None, close_source=False, output_failure=None,
   reservation=None, receipt_cap=None):
 data = payload() if data is None else data
 opaque = b"opaque-not-a-ZIP:" + SENTINEL.encode()
 source0, source1, output = Mock(), Mock(), Mock()
 source0.read.return_value = data
 source1.read.return_value = opaque
 if close_source:
  source0.close.side_effect = OSError(SENTINEL)
 output.write.side_effect = lambda blob: len(blob)
 output.fileno.return_value = 42
 if output_failure == "write":
  output.write.side_effect = OSError(SENTINEL)
 if output_failure == "short":
  output.write.side_effect = lambda blob: len(blob)-1
 if output_failure == "flush":
  output.flush.side_effect = OSError(SENTINEL)
 if output_failure == "close":
  output.close.side_effect = OSError(SENTINEL)
 p0, p1 = "SYNTHETIC_JSON", "SYNTHETIC_OPAQUE"
 specs = (("state", p0, len(data)+(mismatch == "length"), len(data)+16,
   "0"*64 if mismatch == "pin" else hashlib.sha256(data).hexdigest().upper()),
   ("shares", p1, len(opaque), len(opaque)+16,
   hashlib.sha256(opaque).hexdigest().upper()))
 def opened(path, mode, buffering=None):
  if mode == "xb":
   if reservation == "open":
    raise FileExistsError(SENTINEL)
   if path != m.RECEIPT or buffering != 0:
    raise AssertionError("OUTPUT_ROUTE")
   return output
  if mode != "rb" or buffering != 0:
   raise AssertionError("SOURCE_BUFFER")
  if path == m.ROOT / p0:
   return source0
  if path == m.ROOT / p1:
   return source1
  raise AssertionError("UNEXPECTED_ROUTE")
 stdout = io.StringIO()
 with patch.object(m, "SOURCES", specs), patch.object(m, "open", side_effect=opened, create=True) as op, \
  patch.object(Path, "mkdir") as mkdir, patch.object(m.os, "fsync") as fsync, \
  patch.object(m, "RECEIPT_CAP", m.RECEIPT_CAP if receipt_cap is None else receipt_cap), \
  contextlib.redirect_stdout(stdout):
  if reservation == "mkdir":
   mkdir.side_effect = OSError(SENTINEL)
  if output_failure == "fsync":
   fsync.side_effect = OSError(SENTINEL)
  code = m.main()
 saved = output.write.call_args.args[0] if output.write.called else None
 return code, saved, stdout.getvalue(), source0, source1, output, op, mkdir, fsync, specs
class Checks(unittest.TestCase):
 def rejected(self, text, code=None):
  with self.assertRaises(m.Stop) as caught:
   m.Parser(text).parse()
  if code is not None:
   self.assertEqual(caught.exception.code, code)
  return caught.exception
 def test_types_and_case_duplicates(self):
  obj = m.Parser('{"It":123456789012345678901234567890,"it":true,"f":1e9999,"n":null,"s":"x"}').parse().value
  self.assertEqual([obj[k].kind for k in ("It", "it", "f", "n", "s")],
      ["integer", "boolean", "float", "null", "string"])
  self.assertIsNone(obj["It"].value)
  self.assertIsNone(obj["f"].value)
  self.rejected('{"It":1,"It":2}', "JSON_DUPLICATE_KEY")
  self.rejected('{"It":1,"\\u0049t":2}', "JSON_DUPLICATE_KEY")
 def test_invalid_grammar(self):
  for text in ("01", "-01", "[1,]", '{"a":1,}', "NaN", "Infinity",
     "-Infinity", "0 1", "true false", '"\\q"', '"\\u12xz"'):
   self.rejected(text)
 def test_depth_boundary(self):
  m.Parser("["*16 + "0" + "]"*16).parse()
  self.rejected("["*17 + "0" + "]"*17, "JSON_DEPTH_CAP")
 def test_token_boundary(self):
  parser = m.Parser("0")
  parser.tokens = 9999
  parser.parse()
  self.assertEqual(parser.tokens, 10000)
  with self.assertRaises(m.Stop) as caught:
   parser.token()
  self.assertEqual(caught.exception.code, "JSON_TOKEN_CAP")
  m.Parser("[" + ",".join(["null"]*4999) + "]").parse()
  self.rejected("[" + ",".join(["null"]*5000) + "]", "JSON_TOKEN_CAP")
 def test_string_boundary(self):
  self.assertEqual(len(m.Parser('"'+"x"*4096+'"').parse().value), 4096)
  self.rejected('"'+"x"*4097+'"', "JSON_STRING_CAP")
  m.Parser('"'+"\\u0061"*4096+'"').parse()
  self.rejected('"'+"\\u0061"*4097+'"', "JSON_STRING_CAP")
  self.rejected('"'+"\\ud83d\\ude00"*2049+'"', "JSON_STRING_CAP")
 def test_schema_and_redaction(self):
  summary = m.schema_summary(m.Parser(payload().decode()).parse())
  self.assertEqual(summary["row_count"], 31)
  self.assertEqual(summary["unknown_top_keys"], 1)
  row = summary["rows"][0]
  self.assertEqual(row["unknown_state_keys"], 1)
  self.assertEqual(row["state_types"][m.STATE.index("It")], "I")
  self.assertEqual(row["state_types"][m.STATE.index("it")], "B")
  self.assertEqual(row["state_types"][m.STATE.index("Ct")], "M")
  self.assertNotIn(SENTINEL, json.dumps(summary))
  self.assertNotIn("secret", json.dumps(summary))
  self.assertEqual(summary["province_axis_comparison"], "UNKNOWN")
  self.assertEqual(summary["classification_content_comparison"], "UNKNOWN")
  for index in (True, 1.0):
   obj = fixture()
   obj["rows"][0]["province_index"] = index
   with self.assertRaises(m.Stop):
    m.schema_summary(m.Parser(payload(obj).decode()).parse())
  obj = fixture()
  obj["rows"].pop()
  with self.assertRaises(m.Stop) as caught:
   m.schema_summary(m.Parser(payload(obj).decode()).parse())
  self.assertEqual(caught.exception.code, "JSON_ROW_COUNT")
  obj = fixture()
  obj["rows"][0]["secret_row"] = SENTINEL
  self.assertEqual(m.schema_summary(m.Parser(payload(obj).decode()).parse())["rows"][0]["unknown_row_keys"], 1)
 def test_read_one_raw_single_call(self):
  data = b"synthetic"
  handle = Mock()
  handle.read.return_value = data
  spec0 = ("state", "SYNTHETIC", len(data), 64, hashlib.sha256(data).hexdigest().upper())
  with patch.object(m, "open", return_value=handle, create=True) as op, \
   patch.object(m.hashlib, "sha256", wraps=hashlib.sha256) as hashed:
   record = {}
   captured = m.read_one(spec0, record, {"cleanup": []})
  self.assertIs(captured, data)
  op.assert_called_once_with(m.ROOT / "SYNTHETIC", "rb", buffering=0)
  handle.read.assert_called_once_with(64)
  handle.close.assert_called_once_with()
  hashed.assert_called_once_with(data)
  self.assertEqual(record["hash_calls"], 1)
 def test_first_failure_prevents_second_source(self):
  cases = [(payload(), "length", "SOURCE_LENGTH_OR_SHORT_READ"),
    (payload(), "pin", "DECLARED_PIN_MISMATCH"),
    (b'{"It":1,"It":2}', None, "JSON_DUPLICATE_KEY"),
    (("["*17+"0"+"]"*17).encode(), None, "JSON_DEPTH_CAP"),
    (('"'+"x"*4097+'"').encode(), None, "JSON_STRING_CAP"),
    (("["+",".join(["null"]*5000)+"]").encode(), None, "JSON_TOKEN_CAP")]
  for data, mismatch, expected in cases:
   result = run_main(data, mismatch)
   code, saved, stdout, first, second, output, op, _, _, specs = result
   receipt = json.loads(saved)
   self.assertEqual(code, 1)
   self.assertEqual(receipt["first_failure"]["code"], expected)
   self.assertEqual(receipt["sources"][1]["status"], "NOT_READ")
   self.assertEqual(op.call_count, 2)
   first.read.assert_called_once_with(specs[0][3])
   second.read.assert_not_called()
   self.assertNotIn("OBSERVED", stdout)
   output.write.assert_called_once()
 def test_reservation_failure_no_source(self):
  for failure in ("mkdir", "open"):
   code, saved, stdout, first, second, output, op, mkdir, _, _ = run_main(reservation=failure)
   self.assertEqual(code, 2)
   self.assertIsNone(saved)
   first.read.assert_not_called()
   second.read.assert_not_called()
   self.assertEqual(op.call_count, 0 if failure == "mkdir" else 1)
   self.assertNotIn("OBSERVED", stdout)
   self.assertNotIn(SENTINEL, stdout)
 def test_cleanup_preserves_first_failure(self):
  code, saved, _, _, second, _, _, _, _, _ = run_main(mismatch="length", close_source=True)
  receipt = json.loads(saved)
  self.assertEqual(code, 1)
  self.assertEqual(receipt["first_failure"]["code"], "SOURCE_LENGTH_OR_SHORT_READ")
  self.assertEqual(receipt["cleanup"][0]["code"], "CLOSE_FAILED")
  second.read.assert_not_called()
  code, saved, _, _, second, _, _, _, _, _ = run_main(close_source=True)
  self.assertEqual(code, 1)
  self.assertEqual(json.loads(saved)["first_failure"]["code"], "SOURCE_CLOSE_FAILED")
  second.read.assert_not_called()
 def test_output_failures_and_receipt_cap(self):
  for failure in ("write", "short", "flush", "fsync", "close"):
   code, saved, stdout, _, _, output, _, _, _, _ = run_main(output_failure=failure)
   self.assertEqual(code, 3)
   self.assertNotIn("OBSERVED", stdout)
   self.assertNotIn(SENTINEL, stdout)
   output.close.assert_called_once()
   if saved is not None:
    receipt = json.loads(saved)
    self.assertEqual(receipt["receipt_persistence"], "NOT_ATTESTED_REQUIRE_PROCESS_EXIT_STATUS")
    self.assertEqual(receipt["output_close_completion"], "NOT_ATTESTED_REQUIRE_PROCESS_EXIT_STATUS")
  code, saved, _, _, _, output, _, _, _, _ = run_main(receipt_cap=3000)
  receipt = json.loads(saved)
  self.assertEqual(code, 1)
  self.assertLessEqual(len(saved), 3000)
  self.assertTrue(receipt["detail_omitted_due_receipt_cap"])
  self.assertEqual(receipt["first_failure"]["code"], "RECEIPT_CAP")
  self.assertNotIn("json", receipt)
  output.write.assert_called_once()
 def test_success_synthetic_only(self):
  code, saved, stdout, first, second, output, op, mkdir, fsync, specs = run_main()
  receipt = json.loads(saved)
  self.assertEqual(code, 0)
  self.assertEqual(receipt["stage"], "STAGE_C8_STATE_SHARE_BOUNDED_OBSERVATION_20261006")
  self.assertEqual(receipt["version"], "delivery-1")
  self.assertEqual(receipt["status"], "OBSERVED_UNAUTHENTICATED")
  for flag in ("source_authenticated", "original_live_identity_restored",
     "scientific_validity_established", "model_activation", "execution_admitted", "Results"):
   self.assertIs(receipt[flag], False)
  self.assertEqual(receipt["C9"], "PAUSED")
  self.assertNotIn(SENTINEL, saved.decode())
  self.assertNotIn("secret", saved.decode())
  self.assertEqual(receipt["sources"][0]["parse_calls"], 1)
  self.assertEqual(receipt["sources"][1]["parse_calls"], 0)
  self.assertEqual(receipt["sources"][1]["hash_calls"], 1)
  first.read.assert_called_once_with(specs[0][3])
  second.read.assert_called_once_with(specs[1][3])
  self.assertEqual(op.call_count, 3)
  output.write.assert_called_once()
  output.flush.assert_called_once()
  output.close.assert_called_once()
  fsync.assert_called_once_with(42)
  mkdir.assert_called_once_with(parents=True, exist_ok=True)
  self.assertLessEqual(len(saved), m.RECEIPT_CAP)
  self.assertIn("OBSERVED_UNAUTHENTICATED", stdout)
if __name__ == "__main__":
 RESULT = unittest.TestResult()
 RESULT.failfast = True
 suite = unittest.defaultTestLoader.loadTestsFromTestCase(Checks)
 suite.run(RESULT)
 print("unittest: run=%d failures=%d errors=%d real_io_attempt=%d" %
  (RESULT.testsRun, len(RESULT.failures), len(RESULT.errors), IO_ATTEMPT))
 if not RESULT.wasSuccessful():
  print("STOP__ISOLATED_METHOD_VALIDATION")
 raise SystemExit(0 if RESULT.wasSuccessful() and not IO_ATTEMPT else 1)
