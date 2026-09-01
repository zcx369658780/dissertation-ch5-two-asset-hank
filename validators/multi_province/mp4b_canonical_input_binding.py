"""Fail-closed validation bindings for canonical and MATLAB-cache Zt modes.

This module is intentionally standard-library-only and never imports or calls
the model, household, HJB, KFE, MP2, MP3, or comparator layers.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
import hashlib
import json
from pathlib import Path
import struct
from typing import Any, Mapping


EXPECTED_CANONICAL_SHA256 = "507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48"
EXPECTED_CACHE_SHA256 = "923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A"
EXPECTED_PROVINCE_COUNT = 31


class BindingContractError(ValueError):
    """Raised when an explicit dual-binding invariant is not satisfied."""


class BindingMode(str, Enum):
    PRIMARY_SOURCE_CANONICAL = "PRIMARY_SOURCE_CANONICAL"
    MATLAB_CACHE_RUNTIME_PARITY_OVERLAY = "MATLAB_CACHE_RUNTIME_PARITY_OVERLAY"


DEFAULT_SCIENTIFIC_BINDING_MODE = BindingMode.PRIMARY_SOURCE_CANONICAL


@dataclass(frozen=True)
class RuntimeCacheEvidence:
    cache_sha256: str
    province_order: tuple[str, ...]
    initialized_zt: tuple[float, ...]
    source_path: str
    source_sha256: str


@dataclass(frozen=True)
class BindingArtifact:
    mode: BindingMode
    canonical_sha256: str
    canonical_bytes: bytes
    object: dict[str, Any]
    cache_evidence: RuntimeCacheEvidence | None
    overlay_table: tuple[dict[str, Any], ...]
    field_identity: Mapping[str, Any]


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _bits(value: float) -> int:
    return struct.unpack(">Q", struct.pack(">d", float(value)))[0]


def _hex(value: float) -> str:
    return float(value).hex()


def _ulp_distance(left: float, right: float) -> int:
    # The accepted initialized-Zt values are positive finite binary64 values.
    return abs(_bits(left) - _bits(right))


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise BindingContractError(f"unreadable JSON evidence: {path}") from error
    if not isinstance(value, dict):
        raise BindingContractError(f"JSON object required: {path}")
    return value


def load_primary_source_canonical(canonical_path: Path) -> tuple[bytes, dict[str, Any]]:
    canonical_path = Path(canonical_path)
    if _sha256(canonical_path) != EXPECTED_CANONICAL_SHA256:
        raise BindingContractError("canonical SHA-256 mismatch")
    raw = canonical_path.read_bytes()
    canonical = _load_json(canonical_path)
    order = canonical.get("province_order")
    initialized_zt = canonical.get("vectors", {}).get("initialized_zt")
    if not isinstance(order, list) or not isinstance(initialized_zt, list):
        raise BindingContractError("canonical province_order/initialized_zt missing")
    if len(order) != EXPECTED_PROVINCE_COUNT or len(initialized_zt) != EXPECTED_PROVINCE_COUNT:
        raise BindingContractError("canonical province count mismatch")
    return raw, canonical


def load_runtime_cache_evidence(census_path: Path) -> RuntimeCacheEvidence:
    census_path = Path(census_path)
    source_sha = _sha256(census_path)
    census = _load_json(census_path)
    if census.get("classification") != "MP4B_INITIAL_ZT_BINDING_CENSUS_REPRESENTATION_DIVERGENCES_LOCALIZED":
        raise BindingContractError("accepted runtime-cache census classification mismatch")
    rows = census.get("rows")
    if not isinstance(rows, list) or len(rows) != EXPECTED_PROVINCE_COUNT:
        raise BindingContractError("runtime-cache census row count mismatch")
    first_provenance = rows[0].get("cache_provenance", {}) if rows else {}
    cache_sha = first_provenance.get("sha256")
    if cache_sha != EXPECTED_CACHE_SHA256:
        raise BindingContractError("cache SHA-256 mismatch")
    names: list[str] = []
    values: list[float] = []
    for index, row in enumerate(rows, start=1):
        if row.get("province_index_one_based") != index:
            raise BindingContractError("runtime-cache census index mismatch")
        provenance = row.get("cache_provenance", {})
        if provenance.get("sha256") != cache_sha:
            raise BindingContractError("runtime-cache provenance mismatch")
        name = row.get("canonical_province_name")
        value = row.get("cache_ind_zt")
        if not isinstance(name, str) or not isinstance(value, (int, float)):
            raise BindingContractError("runtime-cache census field mismatch")
        names.append(name)
        values.append(float(value))
    return RuntimeCacheEvidence(cache_sha, tuple(names), tuple(values), str(census_path.resolve()), source_sha)


def _different_paths(left: Any, right: Any, path: str = "$") -> list[str]:
    if type(left) is not type(right):
        return [path]
    if isinstance(left, dict):
        if set(left) != set(right):
            return [path]
        differences: list[str] = []
        for key in sorted(left):
            differences.extend(_different_paths(left[key], right[key], f"{path}.{key}"))
        return differences
    if isinstance(left, list):
        if len(left) != len(right):
            return [path]
        differences: list[str] = []
        for index, (left_item, right_item) in enumerate(zip(left, right)):
            differences.extend(_different_paths(left_item, right_item, f"{path}[{index}]"))
        return differences
    if isinstance(left, float):
        return [] if _bits(left) == _bits(right) else [path]
    return [] if left == right else [path]


def validate_runtime_overlay(
    canonical: Mapping[str, Any], overlay: Mapping[str, Any], evidence: RuntimeCacheEvidence,
) -> tuple[tuple[dict[str, Any], ...], dict[str, Any]]:
    canonical_order = canonical.get("province_order")
    overlay_order = overlay.get("province_order")
    if canonical_order != overlay_order or tuple(canonical_order or ()) != evidence.province_order:
        raise BindingContractError("province order mismatch")
    canonical_zt = canonical.get("vectors", {}).get("initialized_zt")
    overlay_zt = overlay.get("vectors", {}).get("initialized_zt")
    if not isinstance(canonical_zt, list) or not isinstance(overlay_zt, list):
        raise BindingContractError("initialized_zt missing")
    if len(canonical_zt) != EXPECTED_PROVINCE_COUNT or len(overlay_zt) != EXPECTED_PROVINCE_COUNT:
        raise BindingContractError("initialized_zt count mismatch")
    differences = _different_paths(canonical, overlay)
    allowed = {f"$.vectors.initialized_zt[{index}]" for index in range(EXPECTED_PROVINCE_COUNT)}
    if any(path not in allowed for path in differences):
        raise BindingContractError("non-initialized_zt field changed")
    table: list[dict[str, Any]] = []
    equal_count = one_ulp_count = two_ulp_count = changed_count = 0
    for index, (canonical_value, overlay_value, cache_value) in enumerate(
        zip(canonical_zt, overlay_zt, evidence.initialized_zt), start=1,
    ):
        if not isinstance(canonical_value, (int, float)) or not isinstance(overlay_value, (int, float)):
            raise BindingContractError("initialized_zt binary64 value required")
        canonical_float = float(canonical_value)
        overlay_float = float(overlay_value)
        if _bits(overlay_float) != _bits(cache_value):
            raise BindingContractError("overlay value does not equal cache binary64")
        distance = _ulp_distance(canonical_float, cache_value)
        replacement = distance != 0
        equal_count += int(not replacement)
        changed_count += int(replacement)
        one_ulp_count += int(distance == 1)
        two_ulp_count += int(distance == 2)
        table.append({
            "province_index_one_based": index,
            "province": canonical_order[index - 1],
            "canonical_value": canonical_float,
            "canonical_binary64_hex": _hex(canonical_float),
            "cache_runtime_value": cache_value,
            "cache_runtime_binary64_hex": _hex(cache_value),
            "decimal_difference_cache_minus_canonical": cache_value - canonical_float,
            "ulp_distance": distance,
            "replacement_applied": replacement,
        })
    if (equal_count, changed_count, one_ulp_count, two_ulp_count) != (24, 7, 5, 2):
        raise BindingContractError("accepted cache/canonical ULP census mismatch")
    identity = {
        "non_initialized_zt_paths_bitwise_identical": True,
        "different_paths": differences,
        "allowed_different_paths": sorted(allowed),
        "census": {"equal_rows": equal_count, "different_rows": changed_count, "one_ulp_rows": one_ulp_count, "two_ulp_rows": two_ulp_count},
        "province_order_exact": True,
        "canonical_sha256": EXPECTED_CANONICAL_SHA256,
        "cache_sha256": evidence.cache_sha256,
    }
    return tuple(table), identity


def construct_binding(
    mode: BindingMode | None,
    canonical_path: Path,
    *,
    cache_census_path: Path | None = None,
) -> BindingArtifact:
    if mode is None:
        raise BindingContractError("explicit binding mode is required")
    if not isinstance(mode, BindingMode):
        raise BindingContractError("BindingMode enum required")
    canonical_bytes, canonical = load_primary_source_canonical(canonical_path)
    if mode is BindingMode.PRIMARY_SOURCE_CANONICAL:
        if cache_census_path is not None:
            raise BindingContractError("primary-source mode forbids cache overlay evidence")
        return BindingArtifact(mode, EXPECTED_CANONICAL_SHA256, canonical_bytes, canonical, None, (), {
            "canonical_bytes_preserved": True,
            "non_initialized_zt_paths_bitwise_identical": True,
            "default_scientific_mode": DEFAULT_SCIENTIFIC_BINDING_MODE.value,
        })
    if cache_census_path is None:
        raise BindingContractError("runtime-parity overlay requires explicit cache evidence")
    evidence = load_runtime_cache_evidence(cache_census_path)
    overlay = deepcopy(canonical)
    overlay["vectors"]["initialized_zt"] = list(evidence.initialized_zt)
    table, identity = validate_runtime_overlay(canonical, overlay, evidence)
    return BindingArtifact(mode, EXPECTED_CANONICAL_SHA256, canonical_bytes, overlay, evidence, table, identity)


def write_external_package(
    root: Path,
    primary: BindingArtifact,
    overlay: BindingArtifact,
    focused_test_results: Mapping[str, Any],
) -> dict[str, Path]:
    root = Path(root)
    if root.exists():
        raise FileExistsError(f"refusing to overwrite existing root: {root}")
    if primary.mode is not BindingMode.PRIMARY_SOURCE_CANONICAL or overlay.mode is not BindingMode.MATLAB_CACHE_RUNTIME_PARITY_OVERLAY:
        raise BindingContractError("both explicit binding modes are required")
    root.mkdir(parents=True)

    def write(name: str, value: Any) -> Path:
        path = root / name
        with path.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(value, handle, ensure_ascii=False, sort_keys=True, indent=2)
            handle.write("\n")
        return path

    paths = {
        "binding_contract": write("binding_contract.json", {
            "schema": "MP4B_DUAL_INPUT_BINDING_CONTRACT_V1",
            "markers": ["MP4B_PRIMARY_SOURCE_CANONICAL_BINDING_PRESERVED", "MP4B_DUAL_INPUT_AUTHORITY_CONTRACT_FROZEN", "MP4B_MATLAB_CACHE_RUNTIME_PARITY_OVERLAY_PREPARED", "MP4B_CACHE_OVERLAY_VALIDATION_ONLY_NO_SCIENTIFIC_DEFAULT_CHANGE"],
            "default_scientific_mode": DEFAULT_SCIENTIFIC_BINDING_MODE.value,
            "explicit_mode_required": True,
            "primary_source_canonical": {"canonical_sha256": primary.canonical_sha256, "canonical_bytes_preserved": primary.field_identity["canonical_bytes_preserved"]},
            "matlab_cache_runtime_parity_overlay": {"canonical_sha256": overlay.canonical_sha256, "cache_sha256": overlay.cache_evidence.cache_sha256, "validation_only": True, "scientific_default_changed": False},
        }),
        "overlay": write("matlab_cache_runtime_overlay.json", overlay.object),
        "table": write("initial_zt_31province_hex_ulp_table.json", {"schema": "MP4B_INITIAL_ZT_HEX_ULP_TABLE_V1", "rows": list(overlay.overlay_table)}),
        "identity": write("canonical_vs_overlay_field_identity.json", overlay.field_identity),
        "focused_tests": write("focused_test_results.json", dict(focused_test_results)),
    }
    manifest_rows = []
    for key, path in paths.items():
        manifest_rows.append({"name": key, "path": path.name, "size_bytes": path.stat().st_size, "sha256": _sha256(path)})
    paths["manifest"] = write("remediation_manifest.json", {
        "schema": "MP4B_CANONICAL_BINDING_REMEDIATION_MANIFEST_V1",
        "zero_model_execution": True,
        "canonical_sha256": primary.canonical_sha256,
        "cache_sha256": overlay.cache_evidence.cache_sha256,
        "cache_evidence_path": overlay.cache_evidence.source_path,
        "cache_evidence_sha256": overlay.cache_evidence.source_sha256,
        "files": manifest_rows,
        "scientific_calls": {"matlab": 0, "stationary": 0, "household": 0, "hjb": 0, "kfe": 0, "mp2": 0, "mp3": 0, "comparator": 0},
    })
    return paths
