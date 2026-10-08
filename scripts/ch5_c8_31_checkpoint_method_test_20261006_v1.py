"""Isolated tests of the accepted collector; no real terminal or output I/O."""
import contextlib
import hashlib
import importlib.machinery
import importlib.util
import io
import json
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import Mock, patch

ROOT = Path(r"D:\ProjectTemp\c5k1bturn56")
PUBLIC = str(ROOT / "scripts/ch5_original_c8_state_share_observer_20261006_v1.py")
COLLECTOR = str(ROOT / "scripts/ch5_c8_31_terminal_checkpoint_collector_20261006_v1.py")
READS = {PUBLIC: 0, COLLECTOR: 0}
HASHES = {}
REAL_IO = False
RESULT = None


def audit(event, args):
 global REAL_IO
 if event == "open":
  target, mode = str(args[0]), args[1]
  if target in READS and READS[target] == 0 and mode == "r":
   READS[target] += 1
   return
 if event in ("open", "os.mkdir", "os.remove", "os.rename", "os.rmdir"):
  REAL_IO = True
  if RESULT is not None:
   RESULT.stop()
  raise RuntimeError("UNAUTHORIZED_IO_BLOCKED")


sys.addaudithook(audit)


class ExactLoader(importlib.machinery.SourceFileLoader):
 def get_code(self, fullname):
  cap = 15360 if self.path == PUBLIC else 16384
  with open(self.path, "rb", buffering=0) as handle:
   data = handle.read(cap)
  HASHES[self.path] = hashlib.sha256(data).hexdigest().upper()
  return self.source_to_code(data, self.path)


def load(name, path):
 loader = ExactLoader(name, path)
 spec = importlib.util.spec_from_file_location(name, path, loader=loader)
 module = importlib.util.module_from_spec(spec)
 loader.exec_module(module)
 return module


try:
 public = load("c8_test_public", PUBLIC)
 m = load("c8_test_collector", COLLECTOR)
except BaseException:
 print("STOP__PUBLIC_CODE_LOAD")
 raise SystemExit(1)
Parser = m.make_parser(public)
SECRET = "PRIVATE_SENTINEL_2037"


def text(checkpoint=0, other=None):
 return json.dumps({"checkpoint": checkpoint,
                    "kfe": {"checkpoint": checkpoint if other is None else other},
                    "science_float": 1.25, "science_bool": True,
                    "science_integer": 987654321, "secret": SECRET})


def parsed(source):
 return Parser(source).parse()


def simulate(payloads=None, fail_index=None, fault=None, out_fault=None, reservation=None):
 payloads = [text(index).encode() for index in range(31)] if payloads is None else payloads
 specs = tuple((m.SOURCES[i][0], len(data), len(data)+16) for i, data in enumerate(payloads))
 sources = [Mock() for _ in payloads]
 for source, data in zip(sources, payloads):
  source.read.return_value = data
 if fail_index is not None:
  if fault == "read":
   sources[fail_index].read.side_effect = OSError(SECRET)
  if fault == "short":
   sources[fail_index].read.return_value = payloads[fail_index][:-1]
  if fault in ("close", "short_close"):
   sources[fail_index].close.side_effect = OSError(SECRET)
  if fault == "short_close":
   sources[fail_index].read.return_value = payloads[fail_index][:-1]
 output = Mock()
 output.write.side_effect = lambda blob: len(blob)
 output.fileno.return_value = 73
 if out_fault == "write":
  output.write.side_effect = OSError(SECRET)
 if out_fault == "short":
  output.write.side_effect = lambda blob: len(blob)-1
 if out_fault == "flush":
  output.flush.side_effect = OSError(SECRET)
 if out_fault == "close":
  output.close.side_effect = OSError(SECRET)
 by_path = {m.ROOT / spec[0]: sources[i] for i, spec in enumerate(specs)}
 def opened(path, mode, buffering=None):
  if buffering != 0:
   raise AssertionError("BUFFERING")
  if mode == "xb":
   if path != m.RECEIPT:
    raise AssertionError("OUTPUT_PATH")
   if reservation == "open":
    raise FileExistsError(SECRET)
   return output
  if mode != "rb" or path not in by_path:
   raise AssertionError("SOURCE_PATH")
  return by_path[path]
 def cached_module(module):
  module.__dict__.update(public.__dict__)
 loader = Mock()
 loader.name = "c8_mock_public"
 loader.exec_module.side_effect = cached_module
 stream = io.StringIO()
 with patch.object(m, "SOURCES", specs), patch.object(m, "open", side_effect=opened, create=True) as op, \
      patch.object(m, "ExactLoader", return_value=loader), patch.object(Path, "mkdir") as mkdir, \
      patch.object(m.os, "fsync") as fsync, contextlib.redirect_stdout(stream):
  if reservation == "mkdir":
   mkdir.side_effect = OSError(SECRET)
  if out_fault == "fsync":
   fsync.side_effect = OSError(SECRET)
  code = m.main()
 saved = output.write.call_args.args[0] if output.write.called else None
 return dict(code=code, saved=saved, stdout=stream.getvalue(), sources=sources,
             output=output, op=op, mkdir=mkdir, fsync=fsync, specs=specs, loader=loader)


class Checks(unittest.TestCase):
 def stop_checkpoint(self, source, code=None):
  with self.assertRaises(m.Stop) as caught:
   m.checkpoints(parsed(source))
  if code is not None:
   self.assertEqual(caught.exception.code, code)

 def test_zero_twelve_digits_whitespace_nested(self):
  for value in (0, 999999999999):
   source = " \n "+text(value)+" \t"
   root = parsed(source)
   self.assertEqual(m.checkpoints(root), [value, value])
   self.assertEqual(root.value["checkpoint"].kind, "integer")
   self.assertEqual(root.value["checkpoint"].value, str(value))
   self.assertIsNone(root.value["science_float"].value)
   self.assertIsNone(root.value["science_bool"].value)

 def test_checkpoint_type_and_range_rejection(self):
  for value in (True, False, 1.0, -1, 1000000000000):
   self.stop_checkpoint(text(value))
  self.stop_checkpoint('{"checkpoint":1e0,"kfe":{"checkpoint":1}}', "CHECKPOINT_INTEGER_TYPE")
  for source in ('{}', '{"checkpoint":0}', '{"checkpoint":0,"kfe":{}}',
                 '{"checkpoint":0,"kfe":null}', '[]'):
   self.stop_checkpoint(source)
  with self.assertRaises(public.Stop) as caught:
   parsed('{"checkpoint":1,"checkpoint":1,"kfe":{"checkpoint":1}}')
  self.assertEqual(caught.exception.code, "JSON_DUPLICATE_KEY")
  with self.assertRaises(public.Stop):
   parsed('{"checkpoint":0,"\\u0063heckpoint":0,"kfe":{"checkpoint":0}}')

 def test_parent_guards_preserved(self):
  parsed("["*16+"0"+"]"*16)
  cases = [("["*17+"0"+"]"*17, "JSON_DEPTH_CAP"),
           ('"'+"x"*4097+'"', "JSON_STRING_CAP"),
           ("["+",".join(["null"]*5000)+"]", "JSON_TOKEN_CAP")]
  parsed('"'+"x"*4096+'"')
  for source, expected in cases:
   with self.assertRaises(public.Stop) as caught:
    parsed(source)
   self.assertEqual(caught.exception.code, expected)
  root = parsed('{"It":1,"it":true}')
  self.assertEqual(root.value["It"].kind, "integer")
  self.assertEqual(root.value["it"].kind, "boolean")

 def test_success_full31_and_plan(self):
  result = simulate()
  self.assertEqual(result["code"], 0)
  receipt = json.loads(result["saved"])
  self.assertEqual(len(receipt["sources"]), 31)
  self.assertLessEqual(receipt["output_budget_plan_bytes"], 16384)
  self.assertLessEqual(len(result["saved"]), 16384)
  self.assertGreaterEqual(receipt["output_budget_plan_bytes"], len(result["saved"]))
  self.assertEqual(receipt["counter_order"], list(m.COUNTER_ORDER))
  for index, record in enumerate(receipt["sources"]):
   self.assertEqual(record["checkpoints"], [index, index])
   self.assertEqual(record["checkpoint_consistency"], "MATCH")
   self.assertEqual(record["declared_path"], m.SOURCES[index][0])
   self.assertEqual(record["counters"], [1,1,1,1,1,len(text(index).encode()),1,1,1,1,1,1])
   result["sources"][index].read.assert_called_once_with(result["specs"][index][2])
   result["sources"][index].close.assert_called_once()
   self.assertEqual(record["file_sha256_observation"], hashlib.sha256(text(index).encode()).hexdigest().upper())
  self.assertEqual(result["op"].call_count, 32)
  result["loader"].exec_module.assert_called_once()
  result["output"].write.assert_called_once()
  result["output"].flush.assert_called_once()
  result["output"].close.assert_called_once()
  result["fsync"].assert_called_once_with(73)
  result["mkdir"].assert_called_once_with(parents=True, exist_ok=True)
  self.assertIsNone(receipt["first_failure"])
  for flag in ("source_authenticated","original_live_identity_restored",
               "scientific_validity_established","model_activation","execution_admitted","Results"):
   self.assertIs(receipt[flag], False)
  self.assertEqual(receipt["C9"], "PAUSED")
  self.assertEqual(receipt["phase"], "UNKNOWN")
  self.assertEqual(receipt["actual_province_name_identity_comparison"], "UNKNOWN")
  self.assertNotIn(SECRET, result["saved"].decode())
  for forbidden in ("science_float", "science_bool", "science_integer", "987654321", "1.25"):
   self.assertNotIn(forbidden, result["saved"].decode())

 def assert_partial(self, result, index, expected):
  self.assertEqual(result["code"], 1)
  receipt = json.loads(result["saved"])
  self.assertEqual(receipt["first_failure"]["source_index"], index)
  self.assertEqual(receipt["first_failure"]["code"], expected)
  self.assertEqual(len(receipt["sources"]), 31)
  for j, record in enumerate(receipt["sources"]):
   if j < index:
    self.assertEqual(record["status"], "OBSERVED_UNAUTHENTICATED")
   elif j == index:
    self.assertEqual(record["status"], "FAILED")
   else:
    self.assertEqual(record["status"], "NOT_READ")
    self.assertEqual(record["counters"], [0]*12)
    result["sources"][j].read.assert_not_called()
  self.assertEqual(result["op"].call_count, index+2)
  self.assertNotIn("OBSERVED", result["stdout"])
  self.assertNotIn(SECRET, result["stdout"])
  return receipt

 def test_pair_mismatch_first_failure(self):
  data = [text(i).encode() for i in range(31)]
  data[4] = text(4, 5).encode()
  receipt = self.assert_partial(simulate(data), 4, "CHECKPOINT_PAIR_MISMATCH")
  self.assertEqual(receipt["sources"][4]["checkpoints"], [4,5])
  self.assertEqual(receipt["sources"][4]["checkpoint_consistency"], "MISMATCH")

 def test_read_failure_partial_ledger(self):
  result = simulate(fail_index=3, fault="read")
  receipt = self.assert_partial(result, 3, "SOURCE_IO_OR_PARSE_FAILURE")
  self.assertEqual(receipt["sources"][3]["counters"], [1,1,1,1,0,0,0,0,0,0,1,1])

 def test_parse_failure_partial_ledger(self):
  data = [text(i).encode() for i in range(31)]
  data[7] = b'{"checkpoint":0,"checkpoint":0}'
  receipt = self.assert_partial(simulate(data), 7, "JSON_DUPLICATE_KEY")
  self.assertEqual(receipt["sources"][7]["counters"][6:10], [1,1,1,0])
  self.assertIsNone(receipt["sources"][7]["checkpoints"])

 def test_close_failure_partial_ledger(self):
  result = simulate(fail_index=6, fault="close")
  receipt = self.assert_partial(result, 6, "SOURCE_CLOSE_FAILED")
  self.assertEqual(receipt["sources"][6]["counters"][-2:], [1,0])
  self.assertEqual(receipt["cleanup"], [{"role":"source","index":6,"code":"CLOSE_FAILED"}])

 def test_short_read_first_failure_survives_cleanup(self):
  result = simulate(fail_index=2, fault="short_close")
  receipt = self.assert_partial(result, 2, "SOURCE_LENGTH_OR_SHORT_READ")
  record = receipt["sources"][2]
  self.assertEqual(record["counters"][6:10], [0,0,0,0])
  self.assertIsNone(record["file_sha256_observation"])
  self.assertEqual(receipt["cleanup"][0]["code"], "CLOSE_FAILED")
  result["sources"][2].read.assert_called_once_with(result["specs"][2][2])

 def test_reservation_no_sources(self):
  for failure in ("mkdir","open"):
   result = simulate(reservation=failure)
   self.assertEqual(result["code"], 2)
   self.assertIsNone(result["saved"])
   result["loader"].exec_module.assert_not_called()
   for source in result["sources"]:
    source.read.assert_not_called()
   self.assertEqual(result["op"].call_count, 0 if failure == "mkdir" else 1)

 def test_output_save_and_close_failures(self):
  for fault in ("write","short","flush","fsync","close"):
   result = simulate(out_fault=fault)
   self.assertEqual(result["code"], 3)
   self.assertNotIn("OBSERVED", result["stdout"])
   self.assertNotIn(SECRET, result["stdout"])
   result["output"].write.assert_called_once()
   result["output"].close.assert_called_once()
   receipt = json.loads(result["saved"])
   self.assertEqual(receipt["save_snapshot"], "PRE_WRITE_COMPLETION_NOT_ATTESTED_REQUIRE_PROCESS_EXIT_STATUS")
   self.assertEqual(receipt["receipt_persistence"], "NOT_ATTESTED_REQUIRE_PROCESS_EXIT_STATUS")
   self.assertEqual(receipt["output_close_completion"], "NOT_ATTESTED_REQUIRE_PROCESS_EXIT_STATUS")
  result = simulate(fail_index=2, fault="short", out_fault="close")
  self.assertEqual(result["code"], 3)
  self.assertEqual(json.loads(result["saved"])["first_failure"]["code"], "SOURCE_LENGTH_OR_SHORT_READ")

 def test_read_one_hash_same_capture_and_no_extra_io(self):
  data = text(0).encode()
  source = Mock()
  source.read.return_value = data
  record = dict(counters=[0]*12, status="NOT_READ", checkpoints=None)
  receipt = {"cleanup":[]}
  digest = hashlib.sha256
  with patch.object(m,"open",return_value=source,create=True) as op, \
       patch.object(m.hashlib,"sha256",wraps=digest) as hashed:
   m.read_one(public,Parser,("MEMORY_ONLY",len(data),len(data)+8),record,receipt,0)
  op.assert_called_once_with(m.ROOT/"MEMORY_ONLY","rb",buffering=0)
  source.read.assert_called_once_with(len(data)+8)
  hashed.assert_called_once_with(data)
  self.assertIs(hashed.call_args.args[0], data)
  self.assertEqual(record["checkpoints"], [0,0])
  source.close.assert_called_once()


class FixedResult(unittest.TestResult):
 def addError(self, test, err):
  self.errors.append((test, "FIXED_ERROR"))
  self.stop()
 def addFailure(self, test, err):
  self.failures.append((test, "FIXED_FAILURE"))
  self.stop()


if __name__ == "__main__":
 RESULT = FixedResult()
 RESULT.failfast = True
 suite = unittest.defaultTestLoader.loadTestsFromTestCase(Checks)
 suite.run(RESULT)
 print("unittest: run=%d failures=%d errors=%d real_terminal_io=%d public_reads=%d collector_reads=%d" %
       (RESULT.testsRun,len(RESULT.failures),len(RESULT.errors),REAL_IO,READS[PUBLIC],READS[COLLECTOR]))
 print("public_sha256=" + HASHES[PUBLIC])
 print("collector_sha256=" + HASHES[COLLECTOR])
 if not RESULT.wasSuccessful():
  print("STOP__ISOLATED_METHOD_VALIDATION")
 raise SystemExit(0 if RESULT.wasSuccessful() and not REAL_IO else 1)
