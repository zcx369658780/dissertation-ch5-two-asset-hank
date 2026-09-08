"""Persistence and baseline decoding for the bounded call725 sensitivity."""
from dataclasses import fields, is_dataclass
import hashlib
import json
import math
from pathlib import Path
from collections.abc import Mapping

import numpy as np
from scipy import sparse


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def write_json(path, value):
    path = Path(path)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, allow_nan=False, indent=2)
        stream.write("\n")


def encode(value, arrays, key="root"):
    if sparse.issparse(value):
        matrix = value.copy()
        for name in ("data", "indices", "indptr"):
            arrays[f"{key}_{name}"] = getattr(matrix, name).copy()
        return {"sparse_format": matrix.format, "shape": list(matrix.shape), "array_prefix": key}
    if isinstance(value, np.ndarray):
        arrays[key] = value.copy()
        return {"array": key, "shape": list(value.shape), "dtype": str(value.dtype)}
    if is_dataclass(value):
        return {field.name: encode(getattr(value, field.name), arrays, f"{key}_{field.name}") for field in fields(value)}
    if isinstance(value, Mapping):
        return {str(name): encode(item, arrays, f"{key}_{name}") for name, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(item, arrays, f"{key}_{index}") for index, item in enumerate(value)]
    if isinstance(value, np.generic):
        return encode(value.item(), arrays, key)
    if isinstance(value, float) and not math.isfinite(value):
        return {"nonfinite": repr(value)}
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, Path):
        return str(value)
    raise TypeError(f"unsupported evidence value {type(value)} at {key}")


class Store:
    def __init__(self, root):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=False)
        self.index = (self.root / "index.jsonl").open("x", encoding="utf-8", newline="\n")
        self.last = None

    def save(self, name, value):
        arrays = {}
        encoded = encode(value, arrays)
        target = self.root / f"{name}.json"
        target.parent.mkdir(parents=True, exist_ok=True)
        receipt = {"phase": name, "json": str(target)}
        if arrays:
            binary = target.with_suffix(".npz")
            with binary.open("xb") as stream:
                np.savez(stream, **arrays)
                stream.flush()
            receipt.update(npz=str(binary), npz_sha256=sha256(binary))
        write_json(target, encoded)
        receipt.update(json_sha256=sha256(target))
        self.index.write(json.dumps(receipt, ensure_ascii=False) + "\n")
        self.index.flush()
        self.last = name

    def close(self):
        self.index.close()


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
        if "nonfinite" in value:
            return {"nan": float("nan"), "inf": float("inf"), "-inf": float("-inf")}[value["nonfinite"]]
        return {name: decode(item) for name, item in value.items()}

    return decode(encoded)
