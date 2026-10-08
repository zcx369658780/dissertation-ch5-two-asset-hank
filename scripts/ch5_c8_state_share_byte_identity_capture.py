"""Inert preparation; execution requires a separate, explicit release."""

import importlib.util
import json
import os
import sys


MODULE_NAME = "ch5_state_share_declared_pin_verifier_20261004"
MODULE_PATH = (
    r"D:\ProjectTemp\c5k1bturn56\validators\multi_province"
    r"\annual_observed_labor_diagnostic\archive_byte_pin_verifier.py"
)
RECEIPT_PATH = (
    r"D:\ProjectTemp\c5k1bturn56\EVIDENCE"
    r"\ch5_c8_state_share_byte_identity_20261004\receipt.json"
)
SOURCES = (
    (
        "STATE_JSON", "entering_c8_state",
        r"D:\ProjectTemp\c5k1bturn56\reports\ch5_k1b_turn7_outer_r2_20260925_run001\turn8_k1b_input_candidate.json",
        58130, 59392,
        "30EDAECEA59ABA03EFFD6C11530617BB7CF80FED175F58437F4DACA9E96D2F3A",
    ),
    (
        "FROZEN_SHARE_OPAQUE_NPZ", "frozen_share_payoff",
        r"D:\ProjectTemp\c5k1bturn56\reports\ch5_k1b_turn7_outer_r2_20260925_run001\turn8_k1b_frozen_share_payoff_plan.npz",
        16185, 17408,
        "E6B5D428C1070C6F9F6D9C450F7CDB0D4C2C54F0658074C9C75E60E8FDB743DB",
    ),
)


def load_verifier():
    spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
    if spec is None or spec.loader is None or MODULE_NAME in sys.modules:
        raise RuntimeError("VERIFIER_LOAD_FAILED")
    module = importlib.util.module_from_spec(spec)
    sys.modules[MODULE_NAME] = module
    spec.loader.exec_module(module)
    return module


def initial_receipt():
    rows = []
    for role, identifier, path, expected_length, cap, pin in SOURCES:
        rows.append({
            "role": role, "source_identifier": identifier, "source_path_label": path,
            "expected_length": expected_length, "byte_cap": cap,
            "expected_sha256": pin, "code": "NOT_READ", "phase": "NOT_READ",
            "attempts": 0, "opens": 0, "read_attempts": 0, "reads_completed": 0,
            "completed": 0, "actual_size": None, "actual_sha256": None,
            "cleanup_code": None, "cleanup_phase": None,
            "source_authenticated": False, "original_live_identity_restored": False,
            "scientific_validity_established": False, "model_activation": False,
            "execution_admitted": False,
        })
    return {
        "status": "INCOMPLETE", "classification": "ARCHIVE_DERIVED",
        "scope": "UNAUTHENTICATED_DECLARED_BYTE_IDENTITY_ONLY",
        "total_cap": 76800, "retry": 0, "failure_code": None,
        "failure_phase": None, "sources": rows,
    }


def write_receipt(handle, receipt):
    encoded = (json.dumps(receipt, ensure_ascii=True, indent=2) + "\n").encode("utf-8")
    handle.seek(0)
    written = handle.write(encoded)
    if written != len(encoded):
        raise RuntimeError("RECEIPT_SHORT_WRITE")
    handle.truncate()
    handle.flush()
    os.fsync(handle.fileno())


def capture_one(verifier, source, row):
    role, identifier, path, expected_length, cap, pin = source
    row["phase"] = "DECLARATION"
    try:
        declaration = verifier.ArchiveBytePinDeclaration(
            role, identifier, path, expected_length, cap, pin
        )
    except Exception:
        row["code"] = "DECLARATION_FAILED"
        return False
    row["attempts"] = 1
    row["phase"] = "OPEN"
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
                row["code"] = "SOURCE_CLOSE_FAILED"
                row["phase"] = "CLOSE"
            else:
                row["cleanup_code"] = "SOURCE_CLOSE_FAILED"
                row["cleanup_phase"] = "CLOSE"
    if row["code"] != "NOT_READ":
        payload = None
        return False
    row["phase"] = "VERIFY"
    try:
        result = verifier.verify_archive_byte_pin(declaration, payload)
        row["actual_size"] = result.actual_size
        row["actual_sha256"] = result.actual_sha256
        row["code"] = result.code
    except Exception:
        row["code"] = "VERIFY_FAILED"
        return False
    finally:
        payload = None
    if row["code"] != "MATCH":
        return False
    row["completed"] = 1
    row["phase"] = "COMPLETE"
    return True


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
            write_receipt(receipt_handle, receipt)
        except Exception:
            print("STOP__RECEIPT_PLACEHOLDER_SAVE_FAILED")
            return 1
        for source, row in zip(SOURCES, receipt["sources"]):
            if not capture_one(verifier, source, row):
                receipt["status"] = "STOP"
                receipt["failure_code"] = row["code"]
                receipt["failure_phase"] = row["phase"]
                break
        else:
            receipt["status"] = "COMPLETED_DECLARED_BYTE_MATCH_ONLY"
            exit_code = 0
        try:
            write_receipt(receipt_handle, receipt)
        except Exception:
            print("STOP__RECEIPT_FINAL_SAVE_FAILED")
            return 1
    finally:
        try:
            receipt_handle.close()
        except Exception:
            print("STOP__RECEIPT_CLOSE_FAILED")
            return 1
    if exit_code == 0:
        print("COMPLETED__DECLARED_BYTE_MATCH_ONLY__WAIT_WORK_REVIEW")
    else:
        print("STOP__SOURCE_BYTE_IDENTITY_FAILED__RECEIPT_SAVED")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
