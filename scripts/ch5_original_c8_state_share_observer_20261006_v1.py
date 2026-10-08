"""SOURCE_ONLY candidate. No runtime permission is granted by this file."""
import hashlib
import json
import os
from pathlib import Path
import re

ROOT = Path(r"D:\ProjectTemp\c5k1bturn56")
RECEIPT = ROOT / "EVIDENCE/ch5_original_c8_state_share_observation_20261006_v1/receipt.json"
SOURCES = (
    ("state", "reports/ch5_k1b_turn7_outer_r2_20260925_run001/turn8_k1b_input_candidate.json",
     58130, 59392, "30EDAECEA59ABA03EFFD6C11530617BB7CF80FED175F58437F4DACA9E96D2F3A"),
    ("shares", "reports/ch5_k1b_turn7_outer_r2_20260925_run001/turn8_k1b_frozen_share_payoff_plan.npz",
     16185, 17408, "E6B5D428C1070C6F9F6D9C450F7CDB0D4C2C54F0658074C9C75E60E8FDB743DB"),
)
RECEIPT_CAP = 16384
MAX_DEPTH, MAX_TOKENS, MAX_STRING = 16, 10000, 4096
NUMBER = re.compile(r"-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?")
HEX64 = re.compile(r"[0-9a-fA-F]{64}")
TOP = ("status", "classification", "raw_next_payoff_sha256",
       "k1b_portfolio_share_plan_sha256", "source_completed_turn7_raw_ra0_sha256", "rows")
ROW = ("province_index", "province", "classification", "raw_ra0_turn7", "firm_ra_used", "state")
STATE = tuple(dict.fromkeys((
    "Ct", "At", "Bt", "AtTax", "convergent", "Lt_supply", "Kt_supply", "rah", "w",
    "it", "rb", "Yt_1", "Kt_prev", "Lt_prev", "Zt_1", "pit_1", "GovInv",
    "Kt", "Lt", "Yt", "mt", "KNratio", "wt0", "wjt", "rk", "Thetat", "It",
    "PIt", "Corptax", "ra0", "ra", "Govinc", "name",
)))
KINDS = {"integer": "I", "float": "F", "boolean": "B", "string": "S",
         "null": "N", "object": "O", "array": "A", "missing": "M"}


class Stop(Exception):
    def __init__(self, code, stage):
        self.code, self.stage = code, stage


class Node:
    __slots__ = ("kind", "value")

    def __init__(self, kind, value=None):
        self.kind, self.value = kind, value


class Parser:
    """Bounded grammar parser; numerical tokens never become numerical values."""
    def __init__(self, text):
        self.text, self.pos, self.tokens = text, 0, 0

    def fail(self, code="JSON_GRAMMAR"):
        raise Stop(code, "json_parse")

    def token(self):
        self.tokens += 1
        if self.tokens > MAX_TOKENS:
            self.fail("JSON_TOKEN_CAP")

    def space(self):
        while self.pos < len(self.text) and self.text[self.pos] in " \t\r\n":
            self.pos += 1

    def char(self):
        return self.text[self.pos] if self.pos < len(self.text) else ""

    def punct(self, char):
        self.space()
        if self.char() != char:
            self.fail()
        self.token()
        self.pos += 1

    def string(self):
        if self.char() != '"':
            self.fail()
        self.token()
        start = self.pos
        self.pos += 1
        units = 0
        while self.pos < len(self.text):
            char = self.text[self.pos]
            if char == '"':
                self.pos += 1
                # Only a bounded standalone string is decoded by stdlib JSON.
                return json.loads(self.text[start:self.pos])
            if ord(char) < 32:
                self.fail()
            if char == "\\":
                self.pos += 1
                if self.pos >= len(self.text):
                    self.fail()
                escape = self.text[self.pos]
                if escape == "u":
                    digits = self.text[self.pos + 1:self.pos + 5]
                    if len(digits) != 4 or any(c not in "0123456789abcdefABCDEF" for c in digits):
                        self.fail()
                    self.pos += 5
                elif escape in '"\\/bfnrt':
                    self.pos += 1
                else:
                    self.fail()
            else:
                self.pos += 1
            units += 1
            # Each unicode escape counts separately: conservative for surrogate pairs.
            if units > MAX_STRING:
                self.fail("JSON_STRING_CAP")
        self.fail()

    def value(self, depth=0):
        self.space()
        char = self.char()
        if char == "{":
            if depth + 1 > MAX_DEPTH:
                self.fail("JSON_DEPTH_CAP")
            self.punct("{")
            self.space()
            values = {}
            if self.char() == "}":
                self.punct("}")
                return Node("object", values)
            while True:
                self.space()
                key = self.string()
                if key in values:
                    self.fail("JSON_DUPLICATE_KEY")
                self.punct(":")
                values[key] = self.value(depth + 1)
                self.space()
                if self.char() == "}":
                    self.punct("}")
                    return Node("object", values)
                self.punct(",")
        if char == "[":
            if depth + 1 > MAX_DEPTH:
                self.fail("JSON_DEPTH_CAP")
            self.punct("[")
            self.space()
            values = []
            if self.char() == "]":
                self.punct("]")
                return Node("array", values)
            while True:
                values.append(self.value(depth + 1))
                self.space()
                if self.char() == "]":
                    self.punct("]")
                    return Node("array", values)
                self.punct(",")
        if char == '"':
            return Node("string", self.string())
        for literal, kind in (("true", "boolean"), ("false", "boolean"), ("null", "null")):
            if self.text.startswith(literal, self.pos):
                self.token()
                self.pos += len(literal)
                return Node(kind)
        match = NUMBER.match(self.text, self.pos)
        if match is None:
            self.fail()
        self.token()
        token = match.group()
        self.pos = match.end()
        if self.char() and self.char() not in " \t\r\n,]}":
            self.fail()
        return Node("float" if "." in token or "e" in token.lower() else "integer")

    def parse(self):
        node = self.value()
        self.space()
        if self.pos != len(self.text):
            self.fail()
        return node


def require(node, kinds):
    if node is None or node.kind not in kinds:
        raise Stop("JSON_SCHEMA_TYPE", "json_schema")
    return node


def schema_summary(root):
    obj = require(root, ("object",)).value
    for name in TOP:
        require(obj.get(name), ("array",) if name == "rows" else ("string",))
    hashes = {name: bool(HEX64.fullmatch(obj[name].value)) for name in TOP[2:5]}
    if not all(hashes.values()):
        raise Stop("JSON_HASH_DECLARATION_FORMAT", "json_schema")
    rows = obj["rows"].value
    if len(rows) != 31:
        raise Stop("JSON_ROW_COUNT", "json_schema")
    summaries = []
    for row in rows:
        values = require(row, ("object",)).value
        require(values.get("province_index"), ("integer",))
        require(values.get("province"), ("string",))
        require(values.get("classification"), ("string",))
        require(values.get("raw_ra0_turn7"), ("integer", "float"))
        require(values.get("firm_ra_used"), ("integer", "float"))
        state = require(values.get("state"), ("object",)).value
        summaries.append({
            "row_types": "".join(KINDS[values[name].kind] for name in ROW),
            "unknown_row_keys": len(set(values) - set(ROW)),
            "state_types": "".join(KINDS[state[name].kind] if name in state else "M" for name in STATE),
            "unknown_state_keys": len(set(state) - set(STATE)),
        })
    return {
        "top_types": "".join(KINDS[obj[name].kind] for name in TOP),
        "unknown_top_keys": len(set(obj) - set(TOP)),
        "declaration_hash_format": hashes,
        "row_count": len(rows), "rows": summaries,
        "row_type_order": ROW, "known_state_type_order": STATE,
        "type_legend": KINDS, "province_axis_comparison": "UNKNOWN",
        "classification_content_comparison": "UNKNOWN",
        "state_types_are_observations_not_new_type_guards": True,
    }


def first_failure(receipt, failure, role):
    if receipt["first_failure"] is None:
        receipt["first_failure"] = {"code": failure.code, "stage": failure.stage, "role": role}


def read_one(spec, record, receipt):
    role, relative, expected, cap, pin = spec
    handle, pending, captured = None, None, None
    record["attempts"] = 1
    record["open_calls"] = 1
    try:
        handle = open(ROOT / relative, "rb", buffering=0)
        record["open_completed"] = 1
        record["read_calls"] = 1
        captured = handle.read(cap)
        record["read_completed"] = 1
        record["bytes"] = len(captured)
        if len(captured) != expected:
            raise Stop("SOURCE_LENGTH_OR_SHORT_READ", "source_read")
        record["hash_calls"] = 1
        digest = hashlib.sha256(captured).hexdigest().upper()
        record["hash_completed"] = 1
        record["file_sha256"] = digest
        record["declared_pin_match"] = digest == pin
        if digest != pin:
            raise Stop("DECLARED_PIN_MISMATCH", "source_hash")
        record["status"] = "CAPTURED_UNAUTHENTICATED"
    except Stop as failure:
        pending = failure
    except BaseException as failure:
        code = "INTERRUPTED" if isinstance(failure, KeyboardInterrupt) else "SOURCE_IO_FAILURE"
        pending = Stop(code, "source_io")
    finally:
        if handle is not None:
            record["close_calls"] = 1
            try:
                handle.close()
                record["close_completed"] = 1
            except BaseException:
                receipt["cleanup"].append({"role": role, "stage": "source_close", "code": "CLOSE_FAILED"})
                if pending is None:
                    pending = Stop("SOURCE_CLOSE_FAILED", "source_close")
    if pending is not None:
        record["status"] = "FAILED"
        raise pending
    return captured


def serialize(receipt):
    return json.dumps(receipt, ensure_ascii=True, allow_nan=False, separators=(",", ":")).encode("utf-8")


def main():
    receipt = {
        "stage": "STAGE_C8_STATE_SHARE_BOUNDED_OBSERVATION_20261006",
        "version": "delivery-1", "role": "UNAUTHENTICATED_ARCHIVE_DERIVED_OBSERVATION",
        "status": "INCOMPLETE", "first_failure": None, "cleanup": [],
        "source_authenticated": False, "original_live_identity_restored": False,
        "scientific_validity_established": False, "model_activation": False,
        "execution_admitted": False, "Results": False, "C9": "PAUSED",
        "path_handle_ancestor_principal_protection": "UNKNOWN",
        "eof_complete_file_authenticated": False, "no_extra_eof_probe": True,
        "raw_saved": False, "input_objects_constructed": False,
        "npz_directory_header_crc_elements": "NOT_INSPECTED",
        "receipt_persistence": "NOT_ATTESTED_REQUIRE_PROCESS_EXIT_STATUS",
        "output_close_completion": "NOT_ATTESTED_REQUIRE_PROCESS_EXIT_STATUS",
        "receipt_cap": RECEIPT_CAP, "limits": {
            "depth": MAX_DEPTH, "tokens": MAX_TOKENS,
            "string_length": MAX_STRING, "string_rule": "conservative decoded units",
            "source_caps": [59392, 17408], "total_source_cap": 76800,
        },
        "sources": [
            {"role": role, "path": relative, "status": "NOT_READ",
             "attempts": 0, "open_calls": 0, "open_completed": 0,
             "read_calls": 0, "read_completed": 0, "bytes": 0,
             "hash_calls": 0, "hash_completed": 0, "parse_calls": 0,
             "parse_completed": 0, "close_calls": 0, "close_completed": 0,
             "declared_pin_match": "NOT_CHECKED"}
            for role, relative, expected, cap, pin in SOURCES
        ],
    }
    output = None
    # This is the only output path. Reservation precedes all source access.
    try:
        RECEIPT.parent.mkdir(parents=True, exist_ok=True)
        output = open(RECEIPT, "xb", buffering=0)
    except BaseException:
        print("STOP__OUTPUT_RESERVATION " + str(RECEIPT))
        return 2
    current = "state"
    save_ok = False
    try:
        for index, spec in enumerate(SOURCES):
            current = spec[0]
            record = receipt["sources"][index]
            captured = read_one(spec, record, receipt)
            if index == 0:
                record["parse_calls"] = 1
                try:
                    text = captured.decode("utf-8", errors="strict")
                except UnicodeDecodeError:
                    raise Stop("JSON_UTF8", "json_decode") from None
                parser = Parser(text)
                receipt["json"] = schema_summary(parser.parse())
                record["parse_completed"] = 1
                record["parser_tokens"] = parser.tokens
            record["status"] = "OBSERVED_UNAUTHENTICATED"
            captured = None
        receipt["status"] = "OBSERVED_UNAUTHENTICATED"
    except Stop as failure:
        first_failure(receipt, failure, current)
        receipt["status"] = "STOP"
        for record in receipt["sources"]:
            if record["role"] == current:
                record["status"] = "FAILED"
    except BaseException as failure:
        code = "INTERRUPTED" if isinstance(failure, KeyboardInterrupt) else "UNEXPECTED_FAILURE"
        first_failure(receipt, Stop(code, "observation"), current)
        receipt["status"] = "STOP"
    finally:
        # Write once to the already reserved handle, never a replacement path.
        try:
            encoded = serialize(receipt)
            if len(encoded) > RECEIPT_CAP:
                first_failure(receipt, Stop("RECEIPT_CAP", "receipt_serialize"), "output")
                receipt["status"] = "STOP"
                receipt["detail_omitted_due_receipt_cap"] = True
                receipt["serialization_failure"] = "RECEIPT_CAP"
                receipt.pop("json", None)
                encoded = serialize(receipt)
                if len(encoded) > RECEIPT_CAP:
                    raise Stop("RECEIPT_CAP", "receipt_serialize")
            written = output.write(encoded)
            if written != len(encoded):
                raise Stop("RECEIPT_SHORT_WRITE", "receipt_write")
            output.flush()
            os.fsync(output.fileno())
            save_ok = True
        except BaseException:
            first_failure(receipt, Stop("RECEIPT_SAVE_FAILED", "receipt_save"), "output")
            receipt["status"] = "STOP"
        finally:
            try:
                output.close()
            except BaseException:
                receipt["cleanup"].append({"role": "output", "stage": "receipt_close", "code": "CLOSE_FAILED"})
                first_failure(receipt, Stop("RECEIPT_CLOSE_FAILED", "receipt_close"), "output")
                receipt["status"] = "STOP"
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
