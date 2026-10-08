"""Preparation only: bounded metadata inspection, never array elements."""

import importlib.util
import json
import os
import re
import struct
import sys
import zlib


ROOT = r"D:\ProjectTemp\c5k1bturn56"
MODULE_NAME = "ch5_schema_metadata_declared_pin_verifier_20261004"
MODULE_PATH = ROOT + r"\validators\multi_province\annual_observed_labor_diagnostic\archive_byte_pin_verifier.py"
RECEIPT_PATH = ROOT + r"\EVIDENCE\ch5_c8_state_share_schema_metadata_inspection_20261004\receipt.json"
SOURCES = (
    ("STATE_JSON", "entering_c8_state", ROOT + r"\reports\ch5_k1b_turn7_outer_r2_20260925_run001\turn8_k1b_input_candidate.json",
     58130, 59392, "30EDAECEA59ABA03EFFD6C11530617BB7CF80FED175F58437F4DACA9E96D2F3A"),
    ("FROZEN_SHARE_OPAQUE_NPZ", "frozen_share_payoff", ROOT + r"\reports\ch5_k1b_turn7_outer_r2_20260925_run001\turn8_k1b_frozen_share_payoff_plan.npz",
     16185, 17408, "E6B5D428C1070C6F9F6D9C450F7CDB0D4C2C54F0658074C9C75E60E8FDB743DB"),
)
PROVINCE_ORDER = (
    "北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江",
    "上海", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南",
    "湖北", "湖南", "广东", "广西", "海南", "重庆", "四川", "贵州",
    "云南", "西藏", "陕西", "甘肃", "青海", "宁夏", "新疆",
)
CLASSIFICATION = "TURN8_K1B_INPUT_CANDIDATE_ONLY__TURN8_HOUSEHOLD_NOT_RUN"
TOP_KEYS = {"status", "classification", "raw_next_payoff_sha256", "k1b_portfolio_share_plan_sha256", "source_completed_turn7_raw_ra0_sha256", "rows"}
ROW_KEYS = {"province_index", "province", "classification", "raw_ra0_turn7", "firm_ra_used", "state"}
UPDATE_KEYS = ("Ct", "At", "Bt", "AtTax", "convergent", "Lt_supply", "Kt_supply", "rah", "w", "it", "rb", "Yt_1", "Kt_prev", "Lt_prev", "Zt_1", "pit_1", "GovInv")
FIRM_KEYS = ("Kt", "Lt", "Yt", "mt", "KNratio", "wt0", "wjt", "rk", "Thetat", "It", "PIt", "Corptax", "ra0", "ra", "Govinc")
MEMBERS = {
    "raw_ra0_turn7.npy": (31,), "zscore_by_destination.npy": (31,),
    "foreign_conditional_shares_destination_origin.npy": (31, 31),
    "portfolio_shares_destination_origin.npy": (31, 31),
    "rah_turn8_by_origin.npy": (31,),
}


class InspectionStop(Exception):
    """Only internally selected fixed codes are carried out of parsers."""


def require(condition, code):
    if not condition:
        raise InspectionStop(code)


class JsonMetadataParser:
    """Bounded scanner; scientific numeric lexemes are never converted to floats."""

    number = re.compile(r"-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?")

    def __init__(self, payload, stats):
        self.text = payload.decode("utf-8", errors="strict")
        self.pos = 0
        self.stats = stats
        stats.update(json_tokens=0, json_max_depth=0, json_max_string=0)

    def space(self):
        while self.pos < len(self.text) and self.text[self.pos] in " \t\r\n":
            self.pos += 1

    def token(self):
        require(self.stats["json_tokens"] < 10000, "JSON_TOKEN_CAP")
        self.stats["json_tokens"] += 1

    def punctuation(self, expected):
        self.space()
        require(self.text.startswith(expected, self.pos), "JSON_SYNTAX")
        self.token()
        self.pos += len(expected)

    def string(self):
        self.space()
        require(self.pos < len(self.text) and self.text[self.pos] == '"', "JSON_STRING")
        self.token()
        start = self.pos
        self.pos += 1
        logical_chars = 0
        while self.pos < len(self.text):
            char = self.text[self.pos]
            if char == '"':
                self.pos += 1
                value = json.loads(self.text[start:self.pos])
                require(len(value) <= 4096, "JSON_STRING_CAP")
                self.stats["json_max_string"] = max(self.stats["json_max_string"], len(value))
                return value
            require(ord(char) >= 32, "JSON_STRING")
            require(logical_chars < 4096, "JSON_STRING_CAP")
            logical_chars += 1
            if char == "\\":
                self.pos += 1
                require(self.pos < len(self.text), "JSON_STRING")
                escaped = self.text[self.pos]
                require(escaped in '"\\/bfnrtu', "JSON_STRING")
                if escaped == "u":
                    digits = self.text[self.pos + 1:self.pos + 5]
                    require(len(digits) == 4 and all(c in "0123456789abcdefABCDEF" for c in digits), "JSON_STRING")
                    self.pos += 4
            self.pos += 1
        raise InspectionStop("JSON_STRING")

    def value(self, depth=0):
        self.space()
        require(self.pos < len(self.text), "JSON_SYNTAX")
        char = self.text[self.pos]
        if char == '"':
            return self.string()
        if char in "[{":
            require(depth < 16, "JSON_DEPTH_CAP")
            self.stats["json_max_depth"] = max(self.stats["json_max_depth"], depth + 1)
            is_object = char == "{"
            end = "}" if is_object else "]"
            self.punctuation(char)
            result = {} if is_object else []
            self.space()
            if self.text.startswith(end, self.pos):
                self.punctuation(end)
                return result
            while True:
                if is_object:
                    key = self.string()
                    require(key not in result, "JSON_DUPLICATE_KEY")
                    self.punctuation(":")
                    result[key] = self.value(depth + 1)
                else:
                    result.append(self.value(depth + 1))
                self.space()
                if self.text.startswith(end, self.pos):
                    self.punctuation(end)
                    return result
                self.punctuation(",")
        self.token()
        for literal, value in (("true", True), ("false", False), ("null", None)):
            if self.text.startswith(literal, self.pos):
                self.pos += len(literal)
                return value
        matched = self.number.match(self.text, self.pos)
        require(matched is not None, "JSON_SYNTAX")
        lexeme = matched.group(0)
        self.pos = matched.end()
        return ("NUMBER_FLOAT" if any(c in lexeme for c in ".eE") else "NUMBER_INTEGER", lexeme)

    def parse(self):
        result = self.value()
        self.space()
        require(self.pos == len(self.text), "JSON_TRAILING_CONTENT")
        return result


def token_kind(value):
    if type(value) is tuple:
        return value[0]
    if type(value) is bool:
        return "BOOLEAN"
    if type(value) is str:
        return "STRING"
    if value is None:
        return "NULL"
    return "OBJECT" if type(value) is dict else "ARRAY"


def inspect_json(payload, row):
    row["phase"] = "JSON_PARSE"
    doc = JsonMetadataParser(payload, row["resources"]).parse()
    require(type(doc) is dict and set(doc) == TOP_KEYS, "JSON_TOP_KEYS")
    require(type(doc["status"]) is str, "JSON_STATUS_TOKEN_TYPE")
    require(doc["classification"] == CLASSIFICATION, "JSON_DECLARED_LABEL")
    for name in TOP_KEYS - {"status", "classification", "rows"}:
        require(type(doc[name]) is str and re.fullmatch(r"[0-9a-fA-F]{64}", doc[name]) is not None, "JSON_PIN_METADATA")
    rows = doc["rows"]
    require(type(rows) is list and len(rows) == 31, "JSON_ROW_COUNT")
    summary = []
    row["metadata"] = {"top_keys_present": sorted(TOP_KEYS), "row_count": 31, "rows": summary}
    row["phase"] = "JSON_IDENTITY_TYPES"
    known_state = set(UPDATE_KEYS) | set(FIRM_KEYS) | {"name"}
    for index, source_row in enumerate(rows):
        require(type(source_row) is dict and set(source_row) == ROW_KEYS, "JSON_ROW_KEYS")
        require(source_row["province_index"] == ("NUMBER_INTEGER", str(index)), "JSON_INDEX_TOKEN_IDENTITY")
        require(source_row["province"] == PROVINCE_ORDER[index] and source_row["classification"] == CLASSIFICATION, "JSON_AXIS_IDENTITY")
        state = source_row["state"]
        require(type(state) is dict and known_state <= set(state), "JSON_STATE_KNOWN_KEYS")
        require(state["name"] == PROVINCE_ORDER[index], "JSON_STATE_NAME")
        require(type(state["convergent"]) is bool, "JSON_STATE_TOKEN_TYPE")
        numeric_names = known_state - {"name", "convergent"}
        for name in numeric_names:
            require(token_kind(state[name]) in ("NUMBER_INTEGER", "NUMBER_FLOAT"), "JSON_STATE_TOKEN_TYPE")
        for name in ("raw_ra0_turn7", "firm_ra_used"):
            require(token_kind(source_row[name]) in ("NUMBER_INTEGER", "NUMBER_FLOAT"), "JSON_ROW_TOKEN_TYPE")
        summary.append({
            "province_index": index, "expected_province": PROVINCE_ORDER[index],
            "identity_matches": True, "known_state_key_types": {name: token_kind(state[name]) for name in sorted(known_state)},
            "extra_state_key_count": len(set(state) - known_state),
            "row_numeric_token_types": {name: token_kind(source_row[name]) for name in ("raw_ra0_turn7", "firm_ra_used")},
        })
        row["resources"]["json_rows_inspected"] = len(summary)


def check_zip_extra(extra):
    pos = 0
    while pos < len(extra):
        require(pos + 4 <= len(extra), "ZIP_EXTRA_STRUCTURE")
        tag, size = struct.unpack_from("<HH", extra, pos)
        require(tag != 1, "ZIP64_PROHIBITED")
        pos += 4
        require(pos + size <= len(extra), "ZIP_EXTRA_STRUCTURE")
        pos += size


def zip_directory(payload, row):
    row["phase"] = "ZIP_DIRECTORY"
    footer = payload.rfind(b"PK\x05\x06")
    require(footer >= 0 and footer + 22 == len(payload), "ZIP_FOOTER")
    signature, disk, central_disk, count_disk, count, directory_size, directory_start, comment_size = struct.unpack_from("<4s4H2IH", payload, footer)
    require(disk == central_disk == 0 and count_disk == count == 5 and comment_size == 0, "ZIP_DIRECTORY_SCHEMA")
    require(directory_size <= 4096 and directory_start + directory_size == footer, "ZIP_DIRECTORY_CAP")
    require(directory_start >= 0, "ZIP_DIRECTORY_STRUCTURE")
    directory_bytes = directory_size
    pos = directory_start
    entries = []
    names = set()
    ranges = []
    total_compressed = total_uncompressed = 0
    for _ in range(5):
        require(pos + 46 <= footer, "ZIP_CENTRAL_STRUCTURE")
        (magic, made, needed, flags, method, stamp, date, crc, compressed, uncompressed,
         name_size, extra_size, comment_size, disk_start, internal, external, offset) = struct.unpack_from("<4s6H3I5H2I", payload, pos)
        require(magic == b"PK\x01\x02" and needed <= 20, "ZIP_VERSION_OR_ZIP64")
        require(flags & ~0x800 == 0 and method in (0, 8) and disk_start == 0, "ZIP_FLAGS_METHOD")
        require(0 < name_size <= 128 and comment_size == 0, "ZIP_NAME_COMMENT_CAP")
        end = pos + 46 + name_size + extra_size + comment_size
        require(end <= footer, "ZIP_CENTRAL_STRUCTURE")
        name_bytes = payload[pos + 46:pos + 46 + name_size]
        name = name_bytes.decode("ascii", errors="strict")
        require(name in MEMBERS and name not in names, "ZIP_MEMBER_NAMES")
        names.add(name)
        check_zip_extra(payload[pos + 46 + name_size:end])
        require(offset + 30 <= directory_start, "ZIP_LOCAL_STRUCTURE")
        (local_magic, local_needed, local_flags, local_method, local_stamp, local_date,
         local_crc, local_compressed, local_uncompressed, local_name_size, local_extra_size) = struct.unpack_from("<4s5H3I2H", payload, offset)
        require(local_magic == b"PK\x03\x04" and local_needed <= 20, "ZIP_VERSION_OR_ZIP64")
        require((local_needed, local_flags, local_method, local_crc, local_compressed, local_uncompressed) == (needed, flags, method, crc, compressed, uncompressed), "ZIP_LOCAL_CENTRAL_MISMATCH")
        require(local_name_size == name_size and local_name_size <= 128, "ZIP_LOCAL_NAME")
        data_start = offset + 30 + local_name_size + local_extra_size
        data_end = data_start + compressed
        require(data_start <= directory_start and data_end <= directory_start, "ZIP_MEMBER_RANGE")
        next_directory_bytes = directory_bytes + 30 + local_name_size + local_extra_size
        require(next_directory_bytes <= 4096, "ZIP_DIRECTORY_CAP")
        require(payload[offset + 30:offset + 30 + local_name_size] == name_bytes, "ZIP_LOCAL_NAME")
        check_zip_extra(payload[offset + 30 + local_name_size:data_start])
        directory_bytes = next_directory_bytes
        declared_cap = 4356 if len(MEMBERS[name]) == 1 else 11796
        require(0 < compressed <= 17408 and 0 < uncompressed <= declared_cap, "ZIP_DECLARED_MEMBER_CAP")
        require(method != 0 or compressed == uncompressed, "ZIP_STORE_LENGTH")
        total_compressed += compressed
        total_uncompressed += uncompressed
        require(total_compressed <= 17408 and total_uncompressed <= 36660, "ZIP_TOTAL_DECLARED_CAP")
        ranges.append((offset, data_end))
        entries.append({"name": name, "method": method, "compressed_size_declared": compressed,
                        "uncompressed_size_declared": uncompressed, "data_start": data_start, "data_end": data_end})
        row["resources"].update(zip_entries_checked=len(entries), zip_directory_bytes=directory_bytes,
                                zip_compressed_declared=total_compressed, zip_uncompressed_declared=total_uncompressed)
        pos = end
    require(pos == footer and names == set(MEMBERS), "ZIP_DIRECTORY_SCHEMA")
    intervals = sorted(ranges)
    require(all(left[1] <= right[0] for left, right in zip(intervals, intervals[1:])), "ZIP_MEMBER_OVERLAP")
    return entries


class HeaderOnlyReader:
    def __init__(self, payload, entry, row, metadata):
        self.payload = payload
        self.entry = entry
        self.row = row
        self.metadata = metadata
        self.position = entry["data_start"]
        self.output = bytearray()
        self.pending = b""
        self.decompressor = zlib.decompressobj(-15) if entry["method"] == 8 else None

    def ensure(self, target):
        require(target <= 4108 and target <= self.entry["uncompressed_size_declared"], "NPY_HEADER_OUTPUT_CAP")
        while len(self.output) < target:
            remaining = target - len(self.output)
            if self.decompressor is None:
                end = self.position + remaining
                require(end <= self.entry["data_end"], "NPY_HEADER_SHORT")
                part = self.payload[self.position:end]
                self.position = end
            else:
                if not self.pending:
                    require(self.position < self.entry["data_end"], "NPY_HEADER_SHORT")
                    end = min(self.position + 1024, self.entry["data_end"])
                    self.pending = self.payload[self.position:end]
                    self.position = end
                prior_pending_size = len(self.pending)
                part = self.decompressor.decompress(self.pending, max_length=remaining)
                self.pending = self.decompressor.unconsumed_tail
                require(not self.decompressor.unused_data, "NPY_DEFLATE_TRAILING")
                require(part or len(self.pending) < prior_pending_size, "NPY_DEFLATE_NO_PROGRESS")
                require(not self.decompressor.eof or len(self.output) + len(part) >= target, "NPY_HEADER_SHORT")
            require(len(part) <= remaining, "NPY_HEADER_OUTPUT_CAP")
            total = self.row["resources"].get("header_output_bytes", 0) + len(part)
            require(total <= 20540, "NPY_TOTAL_HEADER_CAP")
            self.row["resources"]["header_output_bytes"] = total
            self.output.extend(part)
            self.metadata["header_output_bytes"] = len(self.output)
            self.metadata["compressed_bytes_fed"] = self.position - self.entry["data_start"]
        return bytes(self.output)


def parse_npy_header(header):
    # Restricted literal grammar only; no eval/AST/NumPy and no arbitrary strings.
    text = header.decode("ascii", errors="strict")
    require(text.endswith("\n"), "NPY_HEADER_NEWLINE")
    tokens = []
    pattern = re.compile(r"\s*(?:('[^'\\]*'|\"[^\"\\]*\"|True|False|[0-9]{1,6}|[{}():,]))")
    pos = 0
    while pos < len(text):
        if not text[pos:].strip():
            break
        matched = pattern.match(text, pos)
        require(matched is not None and len(tokens) < 64, "NPY_HEADER_GRAMMAR")
        tokens.append(matched.group(1))
        pos = matched.end()
    cursor = 0

    def take(expected=None):
        nonlocal cursor
        require(cursor < len(tokens), "NPY_HEADER_GRAMMAR")
        value = tokens[cursor]
        cursor += 1
        require(expected is None or value == expected, "NPY_HEADER_GRAMMAR")
        return value

    take("{")
    fields = {}
    while True:
        key_token = take()
        require(key_token[0] in "'\"" and key_token[-1] == key_token[0], "NPY_HEADER_KEYS")
        key = key_token[1:-1]
        require(key in ("descr", "fortran_order", "shape") and key not in fields, "NPY_HEADER_KEYS")
        take(":")
        if key == "descr":
            value = take()
            require(value[0] in "'\"" and value[-1] == value[0], "NPY_DTYPE")
            fields[key] = value[1:-1]
            require(fields[key] in ("<f8", ">f8", "=f8"), "NPY_DTYPE")
        elif key == "fortran_order":
            value = take()
            require(value in ("True", "False"), "NPY_ORDER")
            fields[key] = value == "True"
        else:
            take("(")
            dimensions = []
            while True:
                value = take()
                require(re.fullmatch(r"(?:0|[1-9][0-9]{0,5})", value) is not None and len(dimensions) < 2, "NPY_SHAPE")
                dimensions.append(int(value))
                separator = take()
                if separator == ")":
                    require(len(dimensions) >= 2, "NPY_SHAPE_TUPLE")
                    break
                require(separator == ",", "NPY_SHAPE_TUPLE")
                require(cursor < len(tokens), "NPY_SHAPE_TUPLE")
                if tokens[cursor] == ")":
                    take(")")
                    break
            fields[key] = tuple(dimensions)
        next_token = take()
        if next_token == "}":
            break
        require(next_token == ",", "NPY_HEADER_GRAMMAR")
        if cursor < len(tokens) and tokens[cursor] == "}":
            take("}")
            break
    require(cursor == len(tokens) and set(fields) == {"descr", "fortran_order", "shape"}, "NPY_HEADER_KEYS")
    return fields


def inspect_npz(payload, row):
    entries = zip_directory(payload, row)
    metadata_rows = []
    row["metadata"] = {"member_count": 5, "members": metadata_rows,
                       "elements": "NOT_READ", "complete_crc": "NOT_CHECKED", "member_eof": "NOT_CHECKED",
                       "finite_column_sums_field_hash_bit_identity": "NOT_CHECKED"}
    row["phase"] = "NPY_HEADERS"
    for entry in entries:
        metadata = {key: entry[key] for key in ("name", "method", "compressed_size_declared", "uncompressed_size_declared")}
        metadata.update(status="INCOMPLETE", header_output_bytes=0, compressed_bytes_fed=0)
        metadata_rows.append(metadata)
        reader = HeaderOnlyReader(payload, entry, row, metadata)
        prefix = reader.ensure(8)
        require(prefix[:6] == b"\x93NUMPY" and prefix[6:8] in (b"\x01\x00", b"\x02\x00"), "NPY_MAGIC_VERSION")
        prefix_size = 10 if prefix[6] == 1 else 12
        prefix = reader.ensure(prefix_size)
        header_size = int.from_bytes(prefix[8:prefix_size], "little")
        require(0 < header_size <= 4096, "NPY_HEADER_LENGTH")
        encoded = reader.ensure(prefix_size + header_size)
        fields = parse_npy_header(encoded[prefix_size:])
        require(fields["shape"] == MEMBERS[entry["name"]], "NPY_EXPECTED_SHAPE")
        element_size = 248 if len(fields["shape"]) == 1 else 7688
        require(prefix_size + header_size + element_size == entry["uncompressed_size_declared"], "NPY_DECLARED_LENGTH")
        metadata.update(status="HEADER_INSPECTED", npy_version=[prefix[6], prefix[7]], header_length=header_size,
                        dtype_descr=fields["descr"], byteorder=fields["descr"][0],
                        shape=list(fields["shape"]), fortran_order=fields["fortran_order"],
                        element_bytes_inferred=element_size)
        row["resources"]["headers_completed"] = row["resources"].get("headers_completed", 0) + 1
        del reader


def load_verifier():
    spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
    require(spec is not None and spec.loader is not None and MODULE_NAME not in sys.modules, "VERIFIER_LOAD_FAILED")
    module = importlib.util.module_from_spec(spec)
    sys.modules[MODULE_NAME] = module
    spec.loader.exec_module(module)
    return module


def initial_receipt():
    rows = []
    for role, identifier, path, length, cap, pin in SOURCES:
        rows.append({"role": role, "source_identifier": identifier, "source_path_label": path,
                     "expected_length": length, "byte_cap": cap, "expected_sha256": pin,
                     "code": "NOT_READ", "phase": "NOT_READ", "inspection": "NOT_INSPECTED",
                     "attempts": 0, "opens": 0, "read_attempts": 0, "reads_completed": 0, "completed": 0,
                     "actual_size": None, "actual_sha256": None, "cleanup_code": None, "cleanup_phase": None,
                     "metadata": None, "resources": {}, "source_authenticated": False,
                     "original_live_identity_restored": False, "scientific_validity_established": False,
                     "model_activation": False, "execution_admitted": False})
    return {"status": "INCOMPLETE", "scope": "UNAUTHENTICATED_SCHEMA_METADATA_ONLY", "classification": "ARCHIVE_DERIVED",
            "total_file_cap": 76800, "retry": 0, "failure_code": None, "failure_phase": None, "sources": rows,
            "source_eof": "NOT_CHECKED", "protected_input": False, "scientific_acceptance": False}


def save_receipt(handle, receipt):
    encoded = (json.dumps(receipt, ensure_ascii=True, allow_nan=False, indent=2) + "\n").encode("utf-8")
    handle.seek(0)
    require(handle.write(encoded) == len(encoded), "RECEIPT_SHORT_WRITE")
    handle.truncate()
    handle.flush()
    os.fsync(handle.fileno())


def inspect_one(verifier, source, row):
    role, identifier, path, length, cap, pin = source
    row["phase"] = "DECLARATION"
    declaration = verifier.ArchiveBytePinDeclaration(role, identifier, path, length, cap, pin)
    row["phase"] = "OPEN"
    row["attempts"] = 1
    try:
        source_handle = open(path, "rb", buffering=0)
    except Exception:
        row["code"] = "SOURCE_OPEN_FAILED"
        return False
    row["opens"] = 1
    payload = None
    try:
        row["phase"] = "READ"
        row["read_attempts"] = 1
        payload = source_handle.read(cap)
        row["reads_completed"] = 1
        row["actual_size"] = len(payload)
    except Exception:
        row["code"] = "SOURCE_READ_FAILED"
    finally:
        try:
            source_handle.close()
        except Exception:
            if row["code"] == "NOT_READ":
                row["code"], row["phase"] = "SOURCE_CLOSE_FAILED", "CLOSE"
            else:
                row["cleanup_code"], row["cleanup_phase"] = "SOURCE_CLOSE_FAILED", "CLOSE"
    if row["code"] != "NOT_READ":
        return False
    try:
        row["phase"] = "FILE_PIN"
        result = verifier.verify_archive_byte_pin(declaration, payload)
        row["actual_sha256"] = result.actual_sha256
        row["code"] = result.code
        if result.code != "MATCH":
            return False
        row["inspection"] = "INCOMPLETE"
        if role == "STATE_JSON":
            inspect_json(payload, row)
        else:
            inspect_npz(payload, row)
        row["completed"] = 1
        row["inspection"] = "METADATA_INSPECTED"
        row["phase"] = "COMPLETE"
        return True
    finally:
        payload = None


def main():
    try:
        verifier = load_verifier()
    except Exception:
        print("STOP__VERIFIER_LOAD_FAILED")
        return 1
    receipt = initial_receipt()
    try:
        os.makedirs(os.path.dirname(RECEIPT_PATH), exist_ok=True)
        receipt_handle = open(RECEIPT_PATH, "x+b")
    except Exception:
        print("STOP__RECEIPT_CREATE_FAILED")
        return 1
    exit_code = 1
    try:
        try:
            save_receipt(receipt_handle, receipt)
        except Exception:
            print("STOP__RECEIPT_PLACEHOLDER_SAVE_FAILED")
            return 1
        for source, row in zip(SOURCES, receipt["sources"]):
            try:
                succeeded = inspect_one(verifier, source, row)
            except InspectionStop as failure:
                row["code"] = failure.args[0]
                succeeded = False
            except Exception:
                row["code"] = "INSPECTION_INTERNAL_FAILURE"
                succeeded = False
            if not succeeded:
                receipt["status"] = "STOP"
                receipt["failure_code"], receipt["failure_phase"] = row["code"], row["phase"]
                break
        else:
            receipt["status"] = "COMPLETED_UNAUTHENTICATED_METADATA_ONLY"
            exit_code = 0
        try:
            save_receipt(receipt_handle, receipt)
        except Exception:
            print("STOP__RECEIPT_FINAL_SAVE_FAILED")
            return 1
    finally:
        try:
            receipt_handle.close()
        except Exception:
            print("STOP__RECEIPT_CLOSE_FAILED")
            return 1
    print("COMPLETED__METADATA_ONLY__WAIT_WORK_REVIEW" if exit_code == 0 else "STOP__METADATA_INSPECTION_FAILED__RECEIPT_SAVED")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
