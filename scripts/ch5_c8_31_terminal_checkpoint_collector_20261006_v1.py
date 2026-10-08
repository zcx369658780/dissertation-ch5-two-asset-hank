"""SOURCE_ONLY. A separate Work gate is required for real metadata observation."""
import hashlib
import importlib.machinery
import importlib.util
import json
import os
from pathlib import Path
import re

ROOT = Path(r"D:\ProjectTemp\c5k1bturn56")
PARSER_SOURCE = ROOT / "scripts/ch5_original_c8_state_share_observer_20261006_v1.py"
RECEIPT = ROOT / "EVIDENCE/ch5_c8_31_terminal_checkpoint_observation_20261006_v1/receipt.json"
OUTPUT_CAP = 16384
SOURCES = (
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p00_北京/province_terminal_receipt.json", 9433, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p01_天津/province_terminal_receipt.json", 9451, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p02_河北/province_terminal_receipt.json", 9461, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p03_山西/province_terminal_receipt.json", 9455, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p04_内蒙古/province_terminal_receipt.json", 9470, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p05_辽宁/province_terminal_receipt.json", 9460, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p06_吉林/province_terminal_receipt.json", 9455, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p07_黑龙江/province_terminal_receipt.json", 9446, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p08_上海/province_terminal_receipt.json", 9494, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p09_江苏/province_terminal_receipt.json", 9518, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p10_浙江/province_terminal_receipt.json", 9494, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p11_安徽/province_terminal_receipt.json", 9434, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p12_福建/province_terminal_receipt.json", 9497, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p13_江西/province_terminal_receipt.json", 9471, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p14_山东/province_terminal_receipt.json", 9407, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p15_河南/province_terminal_receipt.json", 9432, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p16_湖北/province_terminal_receipt.json", 9452, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p17_湖南/province_terminal_receipt.json", 9489, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p18_广东/province_terminal_receipt.json", 9461, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p19_广西/province_terminal_receipt.json", 9488, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p20_海南/province_terminal_receipt.json", 9498, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p21_重庆/province_terminal_receipt.json", 9405, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p22_四川/province_terminal_receipt.json", 9501, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p23_贵州/province_terminal_receipt.json", 9492, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p24_云南/province_terminal_receipt.json", 9483, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p25_西藏/province_terminal_receipt.json", 9458, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p26_陕西/province_terminal_receipt.json", 9582, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p27_甘肃/province_terminal_receipt.json", 9468, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p28_青海/province_terminal_receipt.json", 9485, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p29_宁夏/province_terminal_receipt.json", 9486, 11264),
 ("reports/ch5_k1b_turn8_outer_r2_20260925_run001/turn8/household/p30_新疆/province_terminal_receipt.json", 9467, 11264),
)
CHECKPOINT = re.compile(r"(?:0|[1-9][0-9]{0,11})", re.ASCII)
COUNTER_ORDER = ("attempts", "open_calls", "open_completed", "read_calls", "read_completed",
                 "bytes", "hash_calls", "hash_completed", "parse_calls", "parse_completed",
                 "close_calls", "close_completed")


class Stop(Exception):
 def __init__(self, code, stage):
  self.code, self.stage = code, stage


class ExactLoader(importlib.machinery.SourceFileLoader):
 def get_code(self, fullname):
  return self.source_to_code(self.get_data(self.path), self.path)


def make_parser(module):
 class MetadataParser(module.Parser):
  def value(self, depth=0):
   self.space()
   start = self.pos
   node = super().value(depth)
   if node.kind == "integer":
    node.value = self.text[start:self.pos]
   return node
 return MetadataParser


def checkpoints(root):
 if root.kind != "object":
  raise Stop("CHECKPOINT_SCHEMA", "checkpoint_metadata")
 outer = root.value.get("checkpoint")
 kfe = root.value.get("kfe")
 if kfe is None or kfe.kind != "object":
  raise Stop("CHECKPOINT_SCHEMA", "checkpoint_metadata")
 inner = kfe.value.get("checkpoint")
 values = []
 for node in (outer, inner):
  if node is None or node.kind != "integer":
   raise Stop("CHECKPOINT_INTEGER_TYPE", "checkpoint_metadata")
  if not isinstance(node.value, str) or CHECKPOINT.fullmatch(node.value) is None:
   raise Stop("CHECKPOINT_NONNEGATIVE_12DIGITS", "checkpoint_metadata")
  values.append(int(node.value))
 return values


def fail_once(receipt, code, stage, index):
 if receipt["first_failure"] is None:
  receipt["first_failure"] = {"code": code, "stage": stage, "source_index": index}
 receipt["status"] = "STOP"


def encode(receipt):
 return json.dumps(receipt, ensure_ascii=True, allow_nan=False, separators=(",", ":")).encode("utf-8")


def output_plan(receipt):
 # Bound the entire ledger, including all 31 records; never discard a partial ledger.
 planned = dict(receipt)
 planned["status"] = "OBSERVED_UNAUTHENTICATED"
 planned["first_failure"] = {"code": "X"*64, "stage": "X"*32, "source_index": 30}
 planned["cleanup"] = [{"role": "source", "index": 30, "code": "CLOSE_FAILED"},
                       {"role": "output", "code": "CLOSE_FAILED"}]
 planned["parser_source_load_attempts"] = planned["parser_source_load_completed"] = 1
 planned["output_budget_plan_bytes"] = 99999
 planned["sources"] = [
  dict(record, status="OBSERVED_UNAUTHENTICATED", counters=[11264]*12,
       file_sha256_observation="F"*64, checkpoints=[999999999999]*2,
       checkpoint_consistency="MISMATCH")
  for record in receipt["sources"]]
 return len(encode(planned))


def read_one(module, parser_class, spec, record, receipt, index):
 relative, expected, cap = spec
 source, pending, captured = None, None, None
 counts = record["counters"]
 counts[0] = counts[1] = 1
 try:
  source = open(ROOT / relative, "rb", buffering=0)
  counts[2] = counts[3] = 1
  captured = source.read(cap)
  counts[4], counts[5] = 1, len(captured)
  if len(captured) != expected:
   raise Stop("SOURCE_LENGTH_OR_SHORT_READ", "source_read")
  counts[6] = 1
  record["file_sha256_observation"] = hashlib.sha256(captured).hexdigest().upper()
  counts[7] = counts[8] = 1
  parser = parser_class(captured.decode("utf-8", errors="strict"))
  root = parser.parse()
  counts[9] = 1
  record["checkpoints"] = checkpoints(root)
  record["checkpoint_consistency"] = "MATCH" if record["checkpoints"][0] == record["checkpoints"][1] else "MISMATCH"
  if record["checkpoint_consistency"] != "MATCH":
   raise Stop("CHECKPOINT_PAIR_MISMATCH", "checkpoint_metadata")
  record["status"] = "OBSERVED_UNAUTHENTICATED"
  captured = root = parser = None
 except Stop as failure:
  pending = failure
 except BaseException as failure:
  if isinstance(failure, getattr(module, "Stop", ())):
   pending = Stop(failure.code, failure.stage)
  elif isinstance(failure, UnicodeDecodeError):
   pending = Stop("JSON_UTF8", "json_decode")
  else:
   pending = Stop("INTERRUPTED" if isinstance(failure, KeyboardInterrupt) else "SOURCE_IO_OR_PARSE_FAILURE", "source_observation")
 finally:
  if source is not None:
   counts[10] = 1
   try:
    source.close()
    counts[11] = 1
   except BaseException:
    receipt["cleanup"].append({"role": "source", "index": index, "code": "CLOSE_FAILED"})
    if pending is None:
     pending = Stop("SOURCE_CLOSE_FAILED", "source_close")
 if pending is not None:
  record["status"] = "FAILED"
  raise pending


def main():
 receipt = {
  "stage": "STAGE_C8_31_TERMINAL_CHECKPOINT_OBSERVATION_20261006",
  "version": "delivery-1", "role": "UNAUTHENTICATED_ARCHIVE_DERIVED_CHECKPOINT_METADATA",
  "status": "INCOMPLETE", "first_failure": None, "cleanup": [],
  "source_authenticated": False, "original_live_identity_restored": False,
  "scientific_validity_established": False, "model_activation": False,
  "execution_admitted": False, "Results": False, "C9": "PAUSED",
  "Objective": "16UNRESOLVED", "window": "UNACCEPTED", "CALL_LEDGER": "UNRESOLVED",
  "wage_notification": "UNVERIFIED_NOT_RATIFIED", "old_STOP_budgets": "PRESERVED",
  "source_identity": "UNKNOWN", "expected_filepin": "UNKNOWN",
  "phase": "UNKNOWN", "common_31_phase": "NOT_ESTABLISHED",
  "phase_classification_version_values": "NOT_INSPECTED",
  "province_sequence": "DECLARED_EXACT_LOCATOR_LIST",
  "actual_province_name_identity_comparison": "UNKNOWN",
  "path_ancestor_principal_concurrency_protection": "UNKNOWN",
  "eof_authenticated": False, "extra_eof_probe": False,
  "raw_saved": False, "consumer_constructed": False,
  "checkpoint_pointers": ["/checkpoint", "/kfe/checkpoint"],
  "checkpoint_rule": "NONNEGATIVE_INTEGER_TOKEN_MAX12DIGITS_PAIR_EQUAL_ONLY",
  "cross_province_checkpoint_equality": "NOT_REQUIRED_NOT_PHASE_PROOF",
  "parser_limits": [16, 10000, 4096], "source_count": 31,
  "total_source_cap": sum(spec[2] for spec in SOURCES),
  "receipt_cap": OUTPUT_CAP, "output_budget_plan_bytes": 0,
  "parser_source_load_attempts": 0, "parser_source_load_completed": 0,
  "counter_order": COUNTER_ORDER,
  "save_snapshot": "PRE_WRITE_COMPLETION_NOT_ATTESTED_REQUIRE_PROCESS_EXIT_STATUS",
  "save": {"reservation": "NOT_COMPLETED", "write_calls": 1},
  "receipt_persistence": "NOT_ATTESTED_REQUIRE_PROCESS_EXIT_STATUS",
  "output_close_completion": "NOT_ATTESTED_REQUIRE_PROCESS_EXIT_STATUS",
  "sources": [{"declared_path": path, "historical_bytes": length, "cap": cap,
               "status": "NOT_READ", "counters": [0]*12,
               "file_sha256_observation": None, "checkpoints": None,
               "checkpoint_consistency": "NOT_CHECKED"}
              for path, length, cap in SOURCES],
 }
 output, save_ok, module, current = None, False, None, -1
 try:
  RECEIPT.parent.mkdir(parents=True, exist_ok=True)
  output = open(RECEIPT, "xb", buffering=0)
  receipt["save"]["reservation"] = "COMPLETED"
 except BaseException:
  print("STOP__OUTPUT_RESERVATION " + str(RECEIPT))
  return 2
 try:
  planned_bytes = output_plan(receipt)
  receipt["output_budget_plan_bytes"] = planned_bytes
  if planned_bytes > OUTPUT_CAP:
   raise Stop("RECEIPT_PLAN_CAP", "receipt_plan")
  receipt["parser_source_load_attempts"] = 1
  loader = ExactLoader("c8_checkpoint_parser", str(PARSER_SOURCE))
  spec = importlib.util.spec_from_file_location(loader.name, PARSER_SOURCE, loader=loader)
  module = importlib.util.module_from_spec(spec)
  loader.exec_module(module)
  receipt["parser_source_load_completed"] = 1
  parser_class = make_parser(module)
  for current, source_spec in enumerate(SOURCES):
   read_one(module, parser_class, source_spec, receipt["sources"][current], receipt, current)
  receipt["status"] = "OBSERVED_UNAUTHENTICATED"
 except Stop as failure:
  fail_once(receipt, failure.code, failure.stage, current)
 except BaseException as failure:
  fail_once(receipt, "INTERRUPTED" if isinstance(failure, KeyboardInterrupt) else "COLLECTOR_FAILURE", "observation", current)
 finally:
  try:
   encoded = encode(receipt)
   if len(encoded) > OUTPUT_CAP:
    fail_once(receipt, "RECEIPT_CAP", "receipt_serialize", current)
    # Keep every record and first failure. No oversized write or replacement output.
    raise Stop("RECEIPT_CAP", "receipt_serialize")
   if output.write(encoded) != len(encoded):
    raise Stop("RECEIPT_SHORT_WRITE", "receipt_write")
   output.flush()
   os.fsync(output.fileno())
   save_ok = True
  except BaseException:
   fail_once(receipt, "RECEIPT_SAVE_FAILED", "receipt_save", current)
  finally:
   try:
    output.close()
   except BaseException:
    receipt["cleanup"].append({"role": "output", "code": "CLOSE_FAILED"})
    fail_once(receipt, "RECEIPT_CLOSE_FAILED", "receipt_close", current)
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
