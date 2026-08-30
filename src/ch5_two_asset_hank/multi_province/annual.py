"""Primary-source annual binding for the decoupled multi-province route.

This module prepares immutable inputs and manifests only.  It imports and calls
no household, HJB, KFE, one-turn, fixed-point, or annual solver.
"""

from __future__ import annotations

from dataclasses import dataclass, fields
from hashlib import sha256
import json
from pathlib import Path
import re
from types import MappingProxyType
from typing import Mapping
import xml.etree.ElementTree as ET
from zipfile import ZipFile

import numpy as np

from .province_contracts import PROVINCE_ORDER, ProvinceAxis


_SHEET_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
_REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
_PACKAGE_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
_CELL_REFERENCE = re.compile(r"([A-Z]+)([0-9]+)")


def _readonly_vector(name: str, value: object) -> np.ndarray:
    array = np.array(value, dtype=np.float64, copy=True)
    if array.shape != (31,) or not np.isfinite(array).all():
        raise ValueError(f"{name} must be a finite binary64 vector with shape (31,)")
    array.flags.writeable = False
    return array


def _readonly_matrix(name: str, value: object) -> np.ndarray:
    array = np.array(value, dtype=np.float64, copy=True)
    if array.shape != (31, 31) or not np.isfinite(array).all():
        raise ValueError(f"{name} must be a finite binary64 matrix with shape (31,31)")
    array.flags.writeable = False
    return array


def _sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


@dataclass(frozen=True)
class DecoupledAnnualIndex:
    calendar_year: int
    analysis_index: int
    workbook_data_row_index: int
    data_mat_index: int
    output_filename_year: int
    regression_vintage_key: int

    def __post_init__(self) -> None:
        year = int(self.calendar_year)
        expected = (
            year - 2008,
            year - 1999,
            year - 2008,
            year,
            year - 1999,
        )
        observed = (
            self.analysis_index,
            self.workbook_data_row_index,
            self.data_mat_index,
            self.output_filename_year,
            self.regression_vintage_key,
        )
        if not 2009 <= year <= 2023 or observed != expected:
            raise ValueError("annual indices must satisfy the Owner-approved decoupled contract")

    @classmethod
    def for_calendar_year(cls, calendar_year: int) -> "DecoupledAnnualIndex":
        year = int(calendar_year)
        return cls(year, year - 2008, year - 1999, year - 2008, year, year - 1999)


@dataclass(frozen=True)
class PrimaryAnnualSourceFiles:
    filled_workbook: Path
    regression_workbook: Path
    distance_workbook: Path
    expected_filled_sha256: str
    expected_regression_sha256: str
    expected_distance_sha256: str

    def verified_hashes(self) -> Mapping[str, str]:
        result: dict[str, str] = {}
        for path_field, hash_field in (
            ("filled_workbook", "expected_filled_sha256"),
            ("regression_workbook", "expected_regression_sha256"),
            ("distance_workbook", "expected_distance_sha256"),
        ):
            path = Path(getattr(self, path_field))
            if not path.is_file():
                raise FileNotFoundError(path)
            expected = str(getattr(self, hash_field)).upper()
            actual = _sha256(path)
            if actual != expected:
                raise ValueError(f"source hash mismatch for {path.name}: {actual} != {expected}")
            result[path.name] = actual
        return MappingProxyType(result)


@dataclass(frozen=True)
class AnnualSourceScalars:
    gdp_multiplier: float
    pop_multiplier: float
    calibration_delta: float
    zt_ratio: float
    gov_inv_ratio: float
    max_sigmau: float
    rb_gap: float
    rah: float
    ra: float
    nominal_rate: float
    rb: float
    rk: float
    wjt: float
    composite_wage: float
    transfer_income: float
    inflation: float
    wage_tax: float
    initial_at: float
    initial_bt: float
    initial_mt: float
    initial_ct: float
    corporate_tax: float

    def __post_init__(self) -> None:
        for field in fields(self):
            object.__setattr__(self, field.name, float(getattr(self, field.name)))
        values = np.array([getattr(self, field.name) for field in fields(self)], dtype=float)
        if not np.isfinite(values).all():
            raise ValueError("annual source scalars must all be finite")
        if self.gdp_multiplier <= 0 or self.pop_multiplier <= 0 or self.max_sigmau <= 0:
            raise ValueError("multipliers and max_sigmau must be positive")


@dataclass(frozen=True)
class CanonicalAnnualInput:
    binding: DecoupledAnnualIndex
    province_axis: ProvinceAxis
    source_hashes: Mapping[str, str]
    regression_sheet: str
    industry_index: int
    fixed_zt_calendar_year: int
    scalars: AnnualSourceScalars
    gdp: np.ndarray
    cap: np.ndarray
    pop: np.ndarray
    log_pgdp: np.ndarray
    log_pcap: np.ndarray
    ind_alpha: np.ndarray
    ind_zt: np.ndarray
    initialized_zt: np.ndarray
    gov_inv: np.ndarray
    inter_province_asset_ratio: np.ndarray
    distance: np.ndarray
    sigmau: np.ndarray

    def __post_init__(self) -> None:
        if self.binding != DecoupledAnnualIndex.for_calendar_year(self.binding.calendar_year):
            raise ValueError("canonical input binding is not the decoupled annual identity")
        if self.province_axis.labels != PROVINCE_ORDER:
            raise ValueError("canonical input must use the accepted province order")
        if self.industry_index != 4 or self.fixed_zt_calendar_year != 2020:
            raise ValueError("MP4A2 preserves source industry 4 and the fixed-2020 Zt anchor")
        for name in (
            "gdp", "cap", "pop", "log_pgdp", "log_pcap", "ind_alpha", "ind_zt",
            "initialized_zt", "gov_inv", "inter_province_asset_ratio",
        ):
            object.__setattr__(self, name, _readonly_vector(name, getattr(self, name)))
        object.__setattr__(self, "distance", _readonly_matrix("distance", self.distance))
        object.__setattr__(self, "sigmau", _readonly_matrix("sigmau", self.sigmau))
        object.__setattr__(self, "source_hashes", MappingProxyType(dict(self.source_hashes)))
        if np.any(self.gdp <= 0) or np.any(self.cap <= 0) or np.any(self.pop <= 0):
            raise ValueError("GDP, CAP, and POP must be positive")
        if not np.array_equal(self.log_pgdp, np.log(self.gdp / self.pop)):
            raise ValueError("log_pgdp does not match the source formula")
        if not np.array_equal(self.log_pcap, np.log(self.cap / self.pop)):
            raise ValueError("log_pcap does not match the source formula")
        if not np.array_equal(self.initialized_zt, self.ind_zt * self.scalars.zt_ratio):
            raise ValueError("initialized_zt does not preserve Ztratio")
        if not np.array_equal(self.gov_inv, self.cap * self.scalars.gov_inv_ratio):
            raise ValueError("GovInv does not preserve the source initialization")
        if not np.allclose(self.sigmau, self.distance / np.max(self.distance) * self.scalars.max_sigmau,
                           rtol=0.0, atol=0.0):
            raise ValueError("sigmau does not preserve load_distdata.m")

    def canonical_payload(self) -> dict[str, object]:
        return {
            "schema": "CH5_MP4A2_CANONICAL_ANNUAL_INPUT_V1",
            "binding": {field.name: getattr(self.binding, field.name) for field in fields(self.binding)},
            "province_order": list(self.province_axis.labels),
            "source_hashes": dict(sorted(self.source_hashes.items())),
            "regression_sheet": self.regression_sheet,
            "industry_index": self.industry_index,
            "fixed_zt_calendar_year": self.fixed_zt_calendar_year,
            "scalars": {field.name: getattr(self.scalars, field.name) for field in fields(self.scalars)},
            "vectors": {name: getattr(self, name).tolist() for name in (
                "gdp", "cap", "pop", "log_pgdp", "log_pcap", "ind_alpha", "ind_zt",
                "initialized_zt", "gov_inv", "inter_province_asset_ratio",
            )},
            "matrices": {"distance": self.distance.tolist(), "sigmau": self.sigmau.tolist()},
        }

    def canonical_bytes(self) -> bytes:
        return (json.dumps(self.canonical_payload(), ensure_ascii=False, sort_keys=True,
                           separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")

    def canonical_sha256(self) -> str:
        return sha256(self.canonical_bytes()).hexdigest().upper()


@dataclass(frozen=True)
class PythonAnnualParityEntry:
    canonical_input_sha256: str
    binding: DecoupledAnnualIndex
    province_order: tuple[str, ...]
    accepted_layers: tuple[str, ...]
    scientific_solver_called: bool = False


def build_python_parity_entry(canonical: CanonicalAnnualInput) -> PythonAnnualParityEntry:
    """Bind MP4B inputs to accepted layers without importing or invoking them."""

    return PythonAnnualParityEntry(
        canonical.canonical_sha256(), canonical.binding, canonical.province_axis.labels,
        (
            "multi_province.household_adapter.build_static_household_call",
            "multi_province.one_turn.run_source_faithful_one_turn",
            "multi_province.steady_state.run_manual_steady_state",
        ),
    )


def write_canonical_artifact(canonical: CanonicalAnnualInput, output_root: Path) -> Path:
    """Write exactly one canonical JSON artifact into a new empty directory."""

    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=False)
    artifact = root / "calendar_2009_primary_premodel_input.json"
    with artifact.open("xb") as stream:
        stream.write(canonical.canonical_bytes())
    return artifact


def _column_index(reference: str) -> int:
    match = _CELL_REFERENCE.fullmatch(reference)
    if match is None:
        raise ValueError(f"invalid cell reference: {reference}")
    value = 0
    for character in match.group(1):
        value = value * 26 + ord(character) - ord("A") + 1
    return value


def _xlsx_sheet_rows(path: Path, sheet_name: str) -> dict[int, dict[int, object]]:
    with ZipFile(path) as archive:
        shared: list[str] = []
        if "xl/sharedStrings.xml" in archive.namelist():
            root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            shared = ["".join(node.text or "" for node in item.iter(f"{{{_SHEET_NS}}}t"))
                      for item in root]
        workbook = ET.fromstring(archive.read("xl/workbook.xml"))
        relationships = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        targets = {item.attrib["Id"]: item.attrib["Target"] for item in relationships}
        target: str | None = None
        for sheet in workbook.find(f"{{{_SHEET_NS}}}sheets") or ():
            if sheet.attrib["name"] == sheet_name:
                target = targets[sheet.attrib[f"{{{_REL_NS}}}id"]]
                break
        if target is None:
            raise KeyError(f"sheet not found: {sheet_name}")
        member = target.lstrip("/")
        if not member.startswith("xl/"):
            member = "xl/" + member
        xml = ET.fromstring(archive.read(member))
        rows: dict[int, dict[int, object]] = {}
        for cell in xml.iter(f"{{{_SHEET_NS}}}c"):
            reference = cell.attrib["r"]
            match = _CELL_REFERENCE.fullmatch(reference)
            assert match is not None
            row_index = int(match.group(2))
            column_index = _column_index(reference)
            value_node = cell.find(f"{{{_SHEET_NS}}}v")
            inline = cell.find(f"{{{_SHEET_NS}}}is")
            if inline is not None:
                value: object = "".join(node.text or "" for node in inline.iter(f"{{{_SHEET_NS}}}t"))
            elif value_node is None:
                value = None
            elif cell.attrib.get("t") == "s":
                value = shared[int(value_node.text or "0")]
            elif cell.attrib.get("t") in {"str", "inlineStr"}:
                value = value_node.text or ""
            else:
                value = float(value_node.text or "nan")
            rows.setdefault(row_index, {})[column_index] = value
        return rows


def _normalize_province(label: object) -> str:
    text = str(label)
    if text.endswith("省") or text.endswith("市"):
        text = text[:-1]
    return text


def _province_header(rows: Mapping[int, Mapping[int, object]]) -> tuple[str, ...]:
    labels = tuple(_normalize_province(rows[1][column]) for column in range(3, 34))
    ProvinceAxis(labels)
    return labels


def _year_from_cell(value: object) -> int:
    match = re.search(r"(20[0-9]{2})", str(value))
    if match is None:
        raise ValueError(f"workbook year cell is not explicit: {value!r}")
    return int(match.group(1))


def load_primary_annual_input(
    *,
    sources: PrimaryAnnualSourceFiles,
    binding: DecoupledAnnualIndex,
    scalars: AnnualSourceScalars,
) -> CanonicalAnnualInput:
    """Reconstruct one annual input directly from the three primary workbooks."""

    hashes = sources.verified_hashes()
    sheet_specs = {"gdp": "GDP", "cap": "总资本存量", "pop": "常住人口"}
    sheet_rows = {
        name: _xlsx_sheet_rows(Path(sources.filled_workbook), sheet)
        for name, sheet in sheet_specs.items()
    }
    headers = tuple(_province_header(rows) for rows in sheet_rows.values())
    if any(header != PROVINCE_ORDER for header in headers):
        raise ValueError("annual workbook sheets do not share the accepted province order")
    physical_row = binding.workbook_data_row_index + 1
    for rows in sheet_rows.values():
        if _year_from_cell(rows[physical_row][1]) != binding.calendar_year:
            raise ValueError("workbook row does not match the explicit calendar year")

    gdp = np.array([sheet_rows["gdp"][physical_row][column] for column in range(3, 34)]) * scalars.gdp_multiplier
    cap = np.array([sheet_rows["cap"][physical_row][column] for column in range(3, 34)]) * scalars.gdp_multiplier
    pop = np.array([sheet_rows["pop"][physical_row][column] for column in range(3, 34)]) * scalars.pop_multiplier
    log_pgdp = np.log(gdp / pop)
    log_pcap = np.log(cap / pop)

    regression_sheet = f"总面板回归系数_{binding.regression_vintage_key}_行业4"
    regression_rows = _xlsx_sheet_rows(Path(sources.regression_workbook), regression_sheet)
    numeric = [float(value) for row in regression_rows.values() for value in row.values()
               if isinstance(value, float) and np.isfinite(value)]
    if len(numeric) < 2:
        raise ValueError("regression coefficient sheet lacks the source coefficient sequence")
    alpha = float(numeric[-1])
    ind_alpha = np.full(31, alpha, dtype=np.float64)

    fixed_rows = sheet_rows
    fixed_physical_row = 2020 - 1999 + 1
    fixed_gdp = np.array([fixed_rows["gdp"][fixed_physical_row][column] for column in range(3, 34)]) * scalars.gdp_multiplier
    fixed_cap = np.array([fixed_rows["cap"][fixed_physical_row][column] for column in range(3, 34)]) * scalars.gdp_multiplier
    fixed_pop = np.array([fixed_rows["pop"][fixed_physical_row][column] for column in range(3, 34)]) * scalars.pop_multiplier
    ind_zt = fixed_gdp * fixed_cap ** (-alpha) * fixed_pop ** (alpha - 1.0)

    distance_rows = _xlsx_sheet_rows(Path(sources.distance_workbook), "geom")
    row_labels = tuple(_normalize_province(distance_rows[row][1]) for row in range(2, 33))
    column_labels = tuple(_normalize_province(distance_rows[1][column]) for column in range(2, 33))
    if row_labels != PROVINCE_ORDER or column_labels != PROVINCE_ORDER:
        raise ValueError("distance workbook axes do not match the accepted province order")
    distance = np.array([[distance_rows[row][column] for column in range(2, 33)]
                         for row in range(2, 33)], dtype=np.float64)
    sigmau = distance / np.max(distance) * scalars.max_sigmau
    ratios = 0.3 * (np.exp(log_pcap) - np.min(np.exp(log_pcap))) / (
        np.max(np.exp(log_pcap)) - np.min(np.exp(log_pcap))
    )
    return CanonicalAnnualInput(
        binding=binding,
        province_axis=ProvinceAxis(PROVINCE_ORDER),
        source_hashes=hashes,
        regression_sheet=regression_sheet,
        industry_index=4,
        fixed_zt_calendar_year=2020,
        scalars=scalars,
        gdp=gdp,
        cap=cap,
        pop=pop,
        log_pgdp=log_pgdp,
        log_pcap=log_pcap,
        ind_alpha=ind_alpha,
        ind_zt=ind_zt,
        initialized_zt=ind_zt * scalars.zt_ratio,
        gov_inv=cap * scalars.gov_inv_ratio,
        inter_province_asset_ratio=ratios,
        distance=distance,
        sigmau=sigmau,
    )


@dataclass(frozen=True)
class CompatibilityResult:
    field: str
    classification: str
    max_abs_difference: float


def compare_runtime_representation(
    canonical: CanonicalAnnualInput,
    cache_fields: Mapping[str, object],
    *,
    rtol: float,
    atol: float,
) -> tuple[CompatibilityResult, ...]:
    """Compare every cache field consumed by 2009 stationary initialization."""

    if rtol < 0 or atol < 0 or not np.isfinite([rtol, atol]).all():
        raise ValueError("compatibility bounds must be explicit, finite, and non-negative")
    primary = {
        "GDP": canonical.gdp,
        "CAP": canonical.cap,
        "POP": canonical.pop,
        "log_pgdp": canonical.log_pgdp,
        "log_pcap": canonical.log_pcap,
        "IND_alpha": canonical.ind_alpha,
        "IND_Zt": canonical.ind_zt,
        "GDP_multiplier": np.array(canonical.scalars.gdp_multiplier),
        "POP_multiplier": np.array(canonical.scalars.pop_multiplier),
        "delta": np.array(canonical.scalars.calibration_delta),
    }
    missing = tuple(sorted(set(primary) - set(cache_fields)))
    if missing:
        raise ValueError(f"cache representation is missing consumed fields: {missing!r}")
    results: list[CompatibilityResult] = []
    for name, expected in primary.items():
        observed = np.asarray(cache_fields[name])
        expected_array = np.asarray(expected)
        if observed.shape != expected_array.shape:
            results.append(CompatibilityResult(name, "MATERIAL_MISMATCH", float("inf")))
            continue
        difference = float(np.max(np.abs(observed - expected_array))) if observed.size else 0.0
        if np.array_equal(observed, expected_array):
            classification = "EXACT"
        elif np.allclose(observed, expected_array, rtol=rtol, atol=atol):
            classification = "SOURCE_EQUIVALENT_BINARY64"
        else:
            classification = "MATERIAL_MISMATCH"
        results.append(CompatibilityResult(name, classification, difference))
    cache_names = tuple(_normalize_province(value) for value in cache_fields.get("prvname", ()))
    if cache_names:
        results.append(CompatibilityResult(
            "prvname",
            "EXACT" if cache_names == canonical.province_axis.labels else "MATERIAL_MISMATCH",
            0.0 if cache_names == canonical.province_axis.labels else float("inf"),
        ))
    else:
        results.append(CompatibilityResult("prvname", "MATERIAL_MISMATCH", float("inf")))
    return tuple(results)
