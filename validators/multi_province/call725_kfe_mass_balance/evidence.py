"""Hashing, saved-schema decoding, and JSON persistence for the attribution."""

import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy import sparse


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def lf_sha256(path):
    return hashlib.sha256(Path(path).read_bytes().replace(b"\r\n", b"\n")).hexdigest().upper()


def write_json(path, value, *, exclusive=False):
    mode = "x" if exclusive else "w"
    with Path(path).open(mode, encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, allow_nan=False, indent=2)
        stream.write("\n")


def decode_saved(json_path):
    json_path = Path(json_path)
    encoded = json.loads(json_path.read_text(encoding="utf-8"))
    arrays = {}
    binary = json_path.with_suffix(".npz")
    if binary.exists():
        with np.load(binary, allow_pickle=False) as archive:
            arrays = {name: archive[name].copy() for name in archive.files}

    def decode(value):
        if isinstance(value, list):
            return [decode(item) for item in value]
        if not isinstance(value, dict):
            return value
        if set(value) == {"array", "shape", "dtype"}:
            return arrays[value["array"]]
        if set(value) == {"sparse_format", "shape", "array_prefix"}:
            prefix = value["array_prefix"]
            cls = {"csr": sparse.csr_matrix, "csc": sparse.csc_matrix}[value["sparse_format"]]
            return cls((arrays[f"{prefix}_data"], arrays[f"{prefix}_indices"], arrays[f"{prefix}_indptr"]), shape=tuple(value["shape"]))
        if set(value) == {"nonfinite"}:
            return {"nan": float("nan"), "inf": float("inf"), "-inf": float("-inf")}[value["nonfinite"]]
        return {name: decode(item) for name, item in value.items()}

    return decode(encoded)
