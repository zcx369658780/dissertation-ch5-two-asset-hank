"""Fail-closed corrected-2018 runtime input contract.

This module is deliberately solver-free.  It binds the accepted repository
receipts to the exact units and routes that a future corrected-2018 scientific
run must consume, and rejects any legacy/canonical substitution before science.
"""

from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from hashlib import sha256
from math import isclose, isfinite
from pathlib import Path
from typing import Any, Mapping, Sequence

from .province_contracts import PROVINCE_ORDER


DATA_YEAR = 2018
ALPHA = 0.7380939146868483
DELTA_PIM = 0.096
FIRM_DEPRECIATION = 0.025
GDP_ROUTE = "RAW_NBS_ACTUAL_2018"
POPULATION_ROUTE = "RAW_NBS_ACTUAL_2018"
CAPITAL_ROUTE = "RAW_NBS_GFCF_TRACK_A_PIM"
MONEY_UNIT = "MU_10WAN_YUAN"
POPULATION_UNIT = "NU_100_PERSONS"
ZT_CONTRACT = "SAME_YEAR_Y_K_L_2018"
GOVINV_RULE = "SOURCE_FAITHFUL_INITIALIZATION_RULE__SCIENTIFIC_REDESIGN_PENDING"
ASSET_BRIDGE_RULE = "SOURCE_FAITHFUL_DIAGNOSTIC_ONLY"
LEDGER_SHA256 = "32833C11686072D11DC8E55801F7106DB4C74663485579C03188C02F35E5BFB4"
EXPECTED_RECEIPT_SHA256 = "5DAD517983CBC436A5FB3E5AD85F1257D957D844994180D15929044A049C7212"
PROVINCE_INPUTS_SHA256 = "588731D050440931E9C4AAC087E0AFD7C90884BD21DA84DC6C8C4EDC376419C9"


def file_sha256(path: Path) -> str:
    digest = sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
                       separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def payload_sha256(payload: Mapping[str, Any]) -> str:
    """Hash all payload content; route, unit and numeric changes are material."""
    return sha256(_canonical_bytes(dict(payload))).hexdigest().upper()


@dataclass(frozen=True)
class Corrected2018RuntimeMetadata:
    data_year: int = DATA_YEAR
    gdp_route: str = GDP_ROUTE
    population_route: str = POPULATION_ROUTE
    capital_route: str = CAPITAL_ROUTE
    gdp_unit: str = MONEY_UNIT
    capital_unit: str = MONEY_UNIT
    population_unit: str = POPULATION_UNIT
    delta_pim: float = DELTA_PIM
    firm_depreciation: float = FIRM_DEPRECIATION
    alpha_raw: float = ALPHA
    alpha_used: float = ALPHA
    zt_contract: str = ZT_CONTRACT
    gov_inv0_rule_id: str = GOVINV_RULE
    gov_inv0_route_id: str = CAPITAL_ROUTE
    gov_inv0_unit: str = MONEY_UNIT
    asset_bridge_rule: str = ASSET_BRIDGE_RULE
    population_proxy_role: str = "population_proxy_NU"
    household_labor_role: str = "household_labor_per_capita"
    firm_labor_role: str = "firm_Lt_supply"


@dataclass(frozen=True)
class Corrected2018ProvinceInput:
    province_index: int
    province: str
    year: int
    gdp_raw_100m_yuan: float
    y0_mu: float
    population_raw_10k_persons: float
    n0_nu: float
    k0_track_a_raw_100m_yuan: float
    k0_mu: float
    l0_population_proxy_nu: float
    alpha_raw: float
    alpha_used: float
    zt0: float
    gov_inv0_raw_source: float
    gov_inv0_mu: float
    gov_inv0_rule_id: str
    gov_inv0_route_id: str
    inter_province_asset_ratio: float
    rah0: float
    w0: float
    firm_ra0_used: float
    firm_wjt0_used: float
    firm_rk0: float
    mt0: float


@dataclass(frozen=True)
class Corrected2018RuntimeInputs:
    metadata: Corrected2018RuntimeMetadata
    provinces: tuple[Corrected2018ProvinceInput, ...]
    source_identities: Mapping[str, Mapping[str, Any]]
    sigmau_destination_origin: tuple[tuple[float, ...], ...]
    distance_identity: Mapping[str, Any]

    def validate_pre_science(self) -> None:
        metadata = self.metadata
        expected_metadata = Corrected2018RuntimeMetadata()
        if metadata != expected_metadata:
            raise ValueError("corrected-2018 route/unit/year metadata mismatch")
        if metadata.gov_inv0_unit != metadata.capital_unit:
            raise ValueError("GovInv0 and capital must have identical declared units")
        if len(self.provinces) != 31:
            raise ValueError("corrected-2018 runtime must contain 31 provinces")
        if tuple(item.province for item in self.provinces) != PROVINCE_ORDER:
            raise ValueError("corrected-2018 province order mismatch")
        if tuple(item.province_index for item in self.provinces) != tuple(range(31)):
            raise ValueError("corrected-2018 province indices mismatch")
        if len(self.sigmau_destination_origin) != 31 or any(len(row) != 31 for row in self.sigmau_destination_origin):
            raise ValueError("distance wedge must have shape (31,31)")
        if any(not isfinite(value) for row in self.sigmau_destination_origin for value in row):
            raise ValueError("distance wedge must be finite")
        for item in self.provinces:
            values = asdict(item)
            numeric = [value for value in values.values() if isinstance(value, (int, float))]
            if any(not isfinite(float(value)) for value in numeric):
                raise ValueError(f"{item.province}: non-finite corrected input")
            if item.year != DATA_YEAR or min(item.y0_mu, item.n0_nu, item.k0_mu, item.zt0) <= 0:
                raise ValueError(f"{item.province}: invalid year or non-positive corrected input")
            if item.y0_mu != item.gdp_raw_100m_yuan * 1000.0:
                raise ValueError(f"{item.province}: GDP unit conversion mismatch")
            if item.n0_nu != item.population_raw_10k_persons * 100.0:
                raise ValueError(f"{item.province}: population unit conversion mismatch")
            if item.k0_mu != item.k0_track_a_raw_100m_yuan * 1000.0:
                raise ValueError(f"{item.province}: capital unit conversion mismatch")
            if item.l0_population_proxy_nu != item.n0_nu:
                raise ValueError(f"{item.province}: initialization labor proxy mismatch")
            expected_zt = item.y0_mu / (item.k0_mu ** item.alpha_used * item.n0_nu ** (1.0 - item.alpha_used))
            if not isclose(item.zt0, expected_zt, rel_tol=2e-15, abs_tol=0.0):
                raise ValueError(f"{item.province}: same-year Zt identity mismatch")
            if item.alpha_raw != ALPHA or item.alpha_used != ALPHA:
                raise ValueError(f"{item.province}: alpha mismatch")
            if item.gov_inv0_raw_source != item.k0_track_a_raw_100m_yuan or item.gov_inv0_mu != item.k0_mu:
                raise ValueError(f"{item.province}: GovInv0 is not corrected Track-A Ktarget in matching units")
            if item.gov_inv0_rule_id != GOVINV_RULE or item.gov_inv0_route_id != CAPITAL_ROUTE:
                raise ValueError(f"{item.province}: GovInv0 route/rule mismatch")
        anhui = self.provinces[11]
        expected = ("安徽", 34010900.0, 607600.0, 70182433.35888097, ALPHA)
        actual = (anhui.province, anhui.y0_mu, anhui.n0_nu, anhui.k0_mu, anhui.alpha_used)
        if actual != expected or not isclose(anhui.zt0, 1.681124916844091, rel_tol=2e-15):
            raise ValueError("accepted Anhui corrected-2018 identity mismatch")
        if isclose(anhui.k0_mu, 1357314108201.3684, rel_tol=1e-12) or isclose(
                anhui.zt0, 0.0006934644495858679, rel_tol=1e-12):
            raise ValueError("rejected old-scale Anhui object entered corrected route")

    def to_payload(self) -> dict[str, Any]:
        self.validate_pre_science()
        scalars = {
            "gdp_multiplier": 1000.0, "pop_multiplier": 100.0,
            "calibration_delta": DELTA_PIM, "firm_depreciation": FIRM_DEPRECIATION,
            "zt_ratio": 1.0, "gov_inv_ratio": 1.0, "max_sigmau": 0.5,
            "rb_gap": 0.07, "nominal_rate": 0.02, "rb": 0.02,
            "transfer_income": 0.1, "inflation": 0.02, "wage_tax": 0.05,
            "initial_at": 2.0, "initial_bt": 1.0, "initial_ct": 4.0,
            "corporate_tax": 0.25, "asset_bridge_beta_a": 1.0,
        }
        states = []
        for item in self.provinces:
            states.append({
                "name": item.province, "N": item.n0_nu, "alpha": item.alpha_used, "Zt": item.zt0,
                "Kt0": item.k0_mu, "Kt": item.k0_mu, "Kt_prev": item.k0_mu,
                "Lt": item.l0_population_proxy_nu, "Lt_prev": item.l0_population_proxy_nu,
                "Yt0": item.y0_mu, "Yt": item.y0_mu, "Zt_1": item.zt0,
                "GovInv": item.gov_inv0_mu, "inter_prv_ratio": item.inter_province_asset_ratio,
                "rb_gap": scalars["rb_gap"], "rah": item.rah0, "ra": item.firm_ra0_used,
                "it": scalars["nominal_rate"], "rb": scalars["rb"], "rk": item.firm_rk0,
                "wjt": item.firm_wjt0_used, "w": item.w0, "Tt": scalars["transfer_income"],
                "pit": scalars["inflation"], "pit_1": scalars["inflation"],
                "totalpit": scalars["inflation"], "epsilon_pi": 0.0, "tau": scalars["wage_tax"],
                "At": scalars["initial_at"], "Bt": scalars["initial_bt"], "mt": item.mt0,
                "Ct": scalars["initial_ct"], "AtTax": 0.0, "GovSurplus": 0.0,
                "corptau": scalars["corporate_tax"], "ramin": 0.02, "ramax": 0.09,
                "wjtmin": 0.8, "wjtmax": 1.3,
            })
        payload = {
            "schema": "CH5_CORRECTED_2018_TRACK_A_RUNTIME_INPUT_V2",
            "metadata": asdict(self.metadata),
            "source_identities": {key: dict(value) for key, value in self.source_identities.items()},
            "distance_workbook": dict(self.distance_identity),
            "province_order": list(PROVINCE_ORDER),
            "province_inputs": [asdict(item) for item in self.provinces],
            "vectors": {
                "gdp_raw": [item.gdp_raw_100m_yuan for item in self.provinces],
                "gdp": [item.y0_mu for item in self.provinces],
                "pop_raw": [item.population_raw_10k_persons for item in self.provinces],
                "pop": [item.n0_nu for item in self.provinces],
                "cap_raw": [item.k0_track_a_raw_100m_yuan for item in self.provinces],
                "cap": [item.k0_mu for item in self.provinces],
                "alpha": [item.alpha_used for item in self.provinces],
                "ind_zt": [item.zt0 for item in self.provinces],
                "gov_inv": [item.gov_inv0_mu for item in self.provinces],
                "inter_province_asset_ratio": [item.inter_province_asset_ratio for item in self.provinces],
            },
            "matrices": {"sigmau_destination_origin": [list(row) for row in self.sigmau_destination_origin]},
            "scalars": scalars,
            "states": states,
            "pre_science_assertion": "PASS_31_OF_31",
        }
        return payload


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not Path(path).is_file():
        raise FileNotFoundError(f"required corrected-2018 input is missing: {path}")
    with Path(path).open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def build_corrected_2018_runtime_inputs(
    ledger_path: Path,
    expected_receipt_path: Path,
    sigmau_destination_origin: Sequence[Sequence[float]],
    distance_identity: Mapping[str, Any],
) -> Corrected2018RuntimeInputs:
    ledger_path = Path(ledger_path)
    receipt_path = Path(expected_receipt_path)
    ledger_sha = file_sha256(ledger_path)
    receipt_sha = file_sha256(receipt_path)
    if ledger_sha != LEDGER_SHA256:
        raise ValueError(f"corrected raw-NBS ledger SHA mismatch: {ledger_sha}")
    if receipt_sha != EXPECTED_RECEIPT_SHA256:
        raise ValueError(f"accepted initialization receipt SHA mismatch: {receipt_sha}")
    ledger = _read_csv(ledger_path)
    expected = _read_csv(receipt_path)
    if len(ledger) != 31 or len(expected) != 31:
        raise ValueError("corrected-2018 inputs must contain exactly 31 rows")
    if tuple(row["province_name"] for row in ledger) != PROVINCE_ORDER:
        raise ValueError("corrected raw-NBS ledger province order mismatch")
    if tuple(row["province_name"] for row in expected) != PROVINCE_ORDER:
        raise ValueError("accepted initialization receipt province order mismatch")
    provinces = []
    for index, (source, accepted) in enumerate(zip(ledger, expected)):
        if int(source["corrected_year"]) != DATA_YEAR or int(accepted["province_index"]) != index + 1:
            raise ValueError(f"{source['province_name']}: corrected year/index mismatch")
        y_raw = float(source["corrected_raw_nbs_gdp_2018_100m_yuan"])
        n_raw = float(source["corrected_raw_nbs_population_2018_10k_persons"])
        k_raw = float(source["corrected_track_a_capital_2018_100m_yuan"])
        item = Corrected2018ProvinceInput(
            province_index=index, province=source["province_name"], year=DATA_YEAR,
            gdp_raw_100m_yuan=y_raw, y0_mu=y_raw * 1000.0,
            population_raw_10k_persons=n_raw, n0_nu=n_raw * 100.0,
            k0_track_a_raw_100m_yuan=k_raw, k0_mu=k_raw * 1000.0,
            l0_population_proxy_nu=n_raw * 100.0,
            alpha_raw=float(source["new_alpha"]), alpha_used=float(source["new_alpha"]),
            zt0=float(accepted["Zt0"]), gov_inv0_raw_source=k_raw, gov_inv0_mu=k_raw * 1000.0,
            gov_inv0_rule_id=GOVINV_RULE, gov_inv0_route_id=CAPITAL_ROUTE,
            inter_province_asset_ratio=float(accepted["inter_prv_ratio"]),
            rah0=float(accepted["rah0"]), w0=float(accepted["w0"]),
            firm_ra0_used=float(accepted["used_ra0"]), firm_wjt0_used=float(accepted["used_wjt0"]),
            firm_rk0=float(accepted["rk_new"]), mt0=float(accepted["mt0"]),
        )
        comparisons = {
            "Y0_MU": item.y0_mu, "N0_NU": item.n0_nu, "K0_MU": item.k0_mu,
            "L0": item.l0_population_proxy_nu, "alpha_raw": item.alpha_raw,
            "alpha_used": item.alpha_used, "Zt0": item.zt0,
        }
        for column, actual in comparisons.items():
            if not isclose(actual, float(accepted[column]), rel_tol=2e-15, abs_tol=0.0):
                raise ValueError(f"{item.province}: source does not match accepted receipt field {column}")
        provinces.append(item)
    runtime = Corrected2018RuntimeInputs(
        metadata=Corrected2018RuntimeMetadata(), provinces=tuple(provinces),
        source_identities={
            "corrected_raw_nbs_ledger": {
                "path": "reports/mp4c_2018_raw_nbs_rebuild_20260910/corrected_2018_vs_matlab_ledger.csv",
                "sha256": ledger_sha, "bytes": ledger_path.stat().st_size},
            "accepted_initialization_receipt": {
                "path": "reports/mp4c_unit_normalized_initialization_probe_20260910/province_initialization_receipt.csv",
                "sha256": receipt_sha, "bytes": receipt_path.stat().st_size},
        },
        sigmau_destination_origin=tuple(tuple(float(value) for value in row) for row in sigmau_destination_origin),
        distance_identity=dict(distance_identity),
    )
    runtime.validate_pre_science()
    return runtime


def validate_serialized_payload(payload: Mapping[str, Any]) -> None:
    """Revalidate route, units and active state after JSON deserialization."""
    metadata = payload.get("metadata")
    if metadata != asdict(Corrected2018RuntimeMetadata()):
        raise ValueError("serialized corrected-2018 metadata mismatch")
    if payload.get("province_order") != list(PROVINCE_ORDER) or payload.get("pre_science_assertion") != "PASS_31_OF_31":
        raise ValueError("serialized corrected-2018 province/assertion contract mismatch")
    provinces = payload.get("province_inputs", [])
    states = payload.get("states", [])
    if len(provinces) != 31 or len(states) != 31:
        raise ValueError("serialized corrected-2018 payload must contain 31 inputs/states")
    if payload_sha256({"province_inputs": provinces}) != PROVINCE_INPUTS_SHA256:
        raise ValueError("serialized corrected-2018 inputs differ from immutable accepted receipt")
    for index, (item, state) in enumerate(zip(provinces, states)):
        if item["province"] != PROVINCE_ORDER[index] or state["name"] != PROVINCE_ORDER[index]:
            raise ValueError("serialized corrected-2018 order mismatch")
        for state_key, input_key in (("Yt0", "y0_mu"), ("N", "n0_nu"), ("Kt0", "k0_mu"),
                                     ("Zt", "zt0"), ("GovInv", "gov_inv0_mu")):
            if state[state_key] != item[input_key]:
                raise ValueError(f"{PROVINCE_ORDER[index]}: active state/input mismatch for {state_key}")
        if state["Lt"] != item["l0_population_proxy_nu"]:
            raise ValueError(f"{PROVINCE_ORDER[index]}: active labor proxy mismatch")
    anhui = states[11]
    if anhui["Kt0"] != 70182433.35888097 or anhui["GovInv"] != 70182433.35888097:
        raise ValueError("rejected old-scale Anhui K/GovInv entered serialized payload")
    if not isclose(anhui["Zt"], 1.681124916844091, rel_tol=2e-15):
        raise ValueError("rejected old-scale Anhui Zt entered serialized payload")
