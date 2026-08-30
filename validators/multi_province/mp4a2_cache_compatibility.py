"""Read-only MATLAB-v7.3 cache adapter for the MP4A2 compatibility gate."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import h5py
import numpy as np

from ch5_two_asset_hank.multi_province.annual import (
    AnnualSourceScalars,
    DecoupledAnnualIndex,
    PrimaryAnnualSourceFiles,
    compare_runtime_representation,
    load_primary_annual_input,
)


def _numeric(value: np.ndarray) -> np.ndarray:
    if value.dtype.fields and set(value.dtype.fields) >= {"real", "imag"}:
        return np.asarray(value["real"], dtype=np.float64) + 1j * np.asarray(
            value["imag"], dtype=np.float64
        )
    return np.asarray(value, dtype=np.float64)


def _matlab_char(handle: h5py.File, reference: h5py.Reference) -> str:
    values = np.asarray(handle[reference][()]).reshape(-1)
    return "".join(chr(int(value)) for value in values)


def load_cache_fields(cache_path: Path, *, data_mat_index: int, data_row_index: int) -> dict[str, object]:
    """Extract only fields consumed by stationary initialization, without model execution."""

    with h5py.File(cache_path, "r") as handle:
        root = handle["mydata2"]
        if root.shape != (15, 1):
            raise ValueError(f"unexpected mydata2 shape: {root.shape}")
        item = handle[root[()][data_mat_index - 1, 0]]
        result: dict[str, object] = {}
        for name in ("GDP", "CAP", "POP", "log_pgdp", "log_pcap"):
            whole = _numeric(handle[item[name][()][3, 0]][()]).T
            selected = whole[data_row_index - 1, :]
            if np.iscomplexobj(selected):
                if np.any(selected.imag != 0.0):
                    raise ValueError(f"cache field {name} has a nonzero 2009 imaginary component")
                selected = selected.real
            result[name] = selected
        for name in ("IND_alpha", "IND_Zt"):
            result[name] = _numeric(handle[item[name][()][3, 0]][()]).reshape(-1)
        for name in ("GDP_multiplier", "POP_multiplier", "delta"):
            result[name] = np.asarray(item[name][()]).reshape(())
        result["prvname"] = tuple(
            _matlab_char(handle, reference) for reference in item["prvname"][()].reshape(-1)
        )
        return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--rtol", type=float, required=True)
    parser.add_argument("--atol", type=float, required=True)
    arguments = parser.parse_args()
    root = arguments.source_root
    sources = PrimaryAnnualSourceFiles(
        filled_workbook=root / "2000年后各省数据_填充NA.xlsx",
        regression_workbook=root / "R语言估计结果_plm估计.xlsx",
        distance_workbook=root / "中国各省省会地理距离矩阵.xlsx",
        expected_filled_sha256="C826B01B6C124EAAADC063DFC2D5510E50E72ED85BB34848F28AB318E4B88929",
        expected_regression_sha256="A6F444FCCCB30CB93AA5DE084F1DD163C54E5F53C4287C2CD3E13A045EB64A68",
        expected_distance_sha256="26E44D174A8EFFBDCA526D95DA38F0E5883E0C78FDFD036D2DFF1D1FBA5A3566",
    )
    scalars = AnnualSourceScalars(
        1000.0, 100.0, 0.096, 1.0, 1.0, 0.5, 0.07, 0.09, 0.09, 0.02,
        0.02, 0.1, 0.6, 20.0, 0.1, 0.02, 0.05, 2.0, 1.0, 0.9, 4.0, 0.25,
    )
    binding = DecoupledAnnualIndex.for_calendar_year(2009)
    canonical = load_primary_annual_input(sources=sources, binding=binding, scalars=scalars)
    cache = load_cache_fields(
        root / "数据估计结果_1000_100_0.mat",
        data_mat_index=binding.data_mat_index,
        data_row_index=binding.workbook_data_row_index,
    )
    results = compare_runtime_representation(
        canonical, cache, rtol=arguments.rtol, atol=arguments.atol
    )
    payload = {
        "canonical_sha256": canonical.canonical_sha256(),
        "results": [result.__dict__ for result in results],
        "material_mismatch": [
            result.field for result in results if result.classification == "MATERIAL_MISMATCH"
        ],
    }
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2))
    return 1 if payload["material_mismatch"] else 0


if __name__ == "__main__":
    sys.exit(main())
