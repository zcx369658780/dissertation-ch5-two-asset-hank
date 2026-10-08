"""SOURCE_ONLY; future execution requires a separate Work scope."""
import hashlib
import importlib.machinery
import importlib.util
import json
import os
from pathlib import Path
import re

ROOT = Path(r"D:\ProjectTemp\c5k1bturn56")
PARSER_SOURCE = ROOT / "scripts/ch5_original_c8_state_share_observer_20261006_v1.py"
TERMINAL = ROOT / "reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p00_北京/province_terminal_receipt.json"
RECEIPT = ROOT / "EVIDENCE/ch5_c8_single_terminal_schema_locator_observation_20261006_v1/receipt.json"
EXPECTED, READ_CAP, OUTPUT_CAP, CANDIDATE_CAP = 9433, 11264, 8192, 64
SAFE = re.compile(r"[A-Za-z_][A-Za-z0-9_]{0,127}", re.ASCII)
MATCH = re.compile(r"checkpoint|phase|stage|writer|version|commit|provenance|classification|source", re.I | re.ASCII)


class Stop(Exception):
 def __init__(self, code, stage):
  self.code, self.stage = code, stage


class ExactLoader(importlib.machinery.SourceFileLoader):
 def get_code(self, fullname):
  return self.source_to_code(self.get_data(self.path), self.path)


def locate(root):
 result = {"candidates": [], "candidate_matches": 0, "omitted_path_count": 0,
   "status": "OBSERVED_NOT_FOUND", "keyword_match_is_semantic_proof": False}
 stack = [(root, "")]
 while stack:
  node, pointer = stack.pop()
  if node.kind == "object":
   for key, child in node.value.items():
    path = pointer + "/" + key if pointer is not None and SAFE.fullmatch(key) else None
    if MATCH.search(key):
     result["candidate_matches"] += 1
     if result["candidate_matches"] >= CANDIDATE_CAP:
      raise Stop("CANDIDATE_CAP_REACHED", "schema_locate")
     if path is None:
      result["omitted_path_count"] += 1
     else:
      entry = {"pointer": path, "kind": child.kind}
      if child.kind in ("object", "array"):
       entry["container_count"] = len(child.value)
      result["candidates"].append(entry)
    stack.append((child, path))
  elif node.kind == "array":
   for index, child in enumerate(node.value):
    stack.append((child, pointer + "/" + str(index) if pointer is not None else None))
 if result["candidate_matches"]:
  result["status"] = "OBSERVED_CANDIDATE_KEYS_ONLY"
 return result


def fail_once(receipt, code, stage):
 if receipt["first_failure"] is None:
  receipt["first_failure"] = {"code": code, "stage": stage}
 receipt["status"] = "STOP"


def encode(receipt):
 return json.dumps(receipt, ensure_ascii=True, allow_nan=False, separators=(",", ":")).encode("utf-8")


def main():
 receipt = {
  "stage": "STAGE_C8_SINGLE_TERMINAL_SCHEMA_LOCATOR_OBSERVATION_20261006",
  "version": "delivery-1", "role": "UNAUTHENTICATED_ARCHIVE_DERIVED_SCHEMA_LOCATOR",
  "status": "INCOMPLETE", "first_failure": None, "cleanup": [],
  "source_authenticated": False, "original_live_identity_restored": False,
  "scientific_validity_established": False, "model_activation": False,
  "execution_admitted": False, "Results": False, "C9": "PAUSED",
  "source_identity": "UNKNOWN", "expected_filepin": "UNKNOWN",
  "phase_values": "NOT_INSPECTED", "classification_values": "NOT_INSPECTED",
  "common_31_schema_or_phase": "NOT_ESTABLISHED", "raw_saved": False,
  "path_ancestor_principal_concurrency_protection": "UNKNOWN",
  "eof_authenticated": False, "extra_eof_probe": False,
  "expected_length": EXPECTED, "expected_length_role": "HISTORICAL_REFERENCE",
  "read_cap": READ_CAP, "receipt_cap": OUTPUT_CAP, "candidate_cap": CANDIDATE_CAP,
  "parser_limits": {"depth": 16, "tokens": 10000, "string": 4096},
  "parser_source_load_attempts": 0, "parser_source_load_completed": 0,
  "parser_source_identity": "ACCEPTED_REFERENCE_NOT_RUNTIME_AUTHENTICATED",
  "source": {"attempts": 0, "open_calls": 0, "open_completed": 0,
    "read_calls": 0, "read_completed": 0, "bytes": 0,
    "hash_calls": 0, "hash_completed": 0,
    "parse_calls": 0, "parse_completed": 0,
    "close_calls": 0, "close_completed": 0, "status": "NOT_READ"},
  "save": {"reservation": "NOT_COMPLETED", "write_calls": 0, "write_completed": 0,
    "flush_calls": 0, "flush_completed": 0, "fsync_calls": 0,
    "fsync_completed": 0, "close_calls": 0},
  "save_ledger_snapshot": "PRE_WRITE_COMPLETION_NOT_ATTESTED_REQUIRE_EXIT_STATUS",
  "receipt_persistence": "NOT_ATTESTED_REQUIRE_PROCESS_EXIT_STATUS",
  "output_close_completion": "NOT_ATTESTED_REQUIRE_PROCESS_EXIT_STATUS",
 }
 output = None
 try:
  RECEIPT.parent.mkdir(parents=True, exist_ok=True)
  output = open(RECEIPT, "xb", buffering=0)
  receipt["save"]["reservation"] = "COMPLETED"
 except BaseException:
  print("STOP__OUTPUT_RESERVATION " + str(RECEIPT))
  return 2
 source, pending, captured, save_ok = None, None, None, False
 record = receipt["source"]
 try:
  receipt["parser_source_load_attempts"] = 1
  loader = ExactLoader("c8_locator_parser", str(PARSER_SOURCE))
  spec = importlib.util.spec_from_file_location(loader.name, PARSER_SOURCE, loader=loader)
  module = importlib.util.module_from_spec(spec)
  loader.exec_module(module)
  receipt["parser_source_load_completed"] = 1
  record["attempts"] = record["open_calls"] = 1
  source = open(TERMINAL, "rb", buffering=0)
  record["open_completed"] = 1
  record["read_calls"] = 1
  captured = source.read(READ_CAP)
  record["read_completed"] = 1
  record["bytes"] = len(captured)
  if len(captured) != EXPECTED:
   raise Stop("SOURCE_LENGTH_OR_SHORT_READ", "source_read")
  record["hash_calls"] = 1
  record["file_sha256_observation"] = hashlib.sha256(captured).hexdigest().upper()
  record["hash_completed"] = 1
  record["parse_calls"] = 1
  parser = module.Parser(captured.decode("utf-8", errors="strict"))
  root = parser.parse()
  record["parse_completed"] = 1
  record["parser_tokens"] = parser.tokens
  receipt["schema"] = locate(root)
  record["status"] = "OBSERVED_UNAUTHENTICATED"
  receipt["status"] = "OBSERVED_UNAUTHENTICATED"
  captured = root = parser = None
 except Stop as failure:
  pending = failure
 except BaseException as failure:
  if "module" in locals() and isinstance(failure, getattr(module, 'Stop', ())):
   pending = Stop(failure.code, failure.stage)
  elif isinstance(failure, UnicodeDecodeError):
   pending = Stop("JSON_UTF8", "json_decode")
  else:
   pending = Stop("INTERRUPTED" if isinstance(failure, KeyboardInterrupt) else "LOCATOR_FAILURE", "observation")
 finally:
  if pending is not None:
   fail_once(receipt, pending.code, pending.stage)
   record["status"] = "FAILED" if record["attempts"] else "NOT_READ"
  if source is not None:
   record["close_calls"] = 1
   try:
    source.close()
    record["close_completed"] = 1
   except BaseException:
    receipt["cleanup"].append({"role": "source", "code": "CLOSE_FAILED"})
    fail_once(receipt, "SOURCE_CLOSE_FAILED", "source_close")
    record["status"] = "FAILED"
  try:
   receipt["save"]["write_calls"] = 1
   encoded = encode(receipt)
   if len(encoded) > OUTPUT_CAP:
    fail_once(receipt, "RECEIPT_CAP", "receipt_serialize")
    receipt["schema_details_omitted_due_cap"] = True
    receipt.pop("schema", None)
    encoded = encode(receipt)
    if len(encoded) > OUTPUT_CAP:
     raise Stop("RECEIPT_CAP", "receipt_serialize")
   if output.write(encoded) != len(encoded):
    raise Stop("RECEIPT_SHORT_WRITE", "receipt_write")
   receipt["save"]["write_completed"] = 1
   receipt["save"]["flush_calls"] = 1
   output.flush()
   receipt["save"]["flush_completed"] = 1
   receipt["save"]["fsync_calls"] = 1
   os.fsync(output.fileno())
   receipt["save"]["fsync_completed"] = 1
   save_ok = True
  except BaseException:
   fail_once(receipt, "RECEIPT_SAVE_FAILED", "receipt_save")
  finally:
   receipt["save"]["close_calls"] = 1
   try:
    output.close()
   except BaseException:
    receipt["cleanup"].append({"role": "output", "code": "CLOSE_FAILED"})
    fail_once(receipt, "RECEIPT_CLOSE_FAILED", "receipt_close")
    save_ok = False
 if not save_ok:
  print("STOP__RECEIPT_SAVE_OR_CLOSE " + str(RECEIPT))
  return 3
 if receipt["first_failure"] is not None:
  print("STOP__OBSERVATION " + str(RECEIPT))
  return 1
 print("OBSERVED_UNAUTHENTICATED " + str(RECEIPT))
 return 0


if __name__ == "__main__":
 raise SystemExit(main())
