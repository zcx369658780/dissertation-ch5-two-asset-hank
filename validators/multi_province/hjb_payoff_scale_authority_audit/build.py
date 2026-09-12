"""Build static receipts for the K1 HJB payoff-scale authority audit.

This module reads text only.  It never imports or calls the scientific runtime.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[3]
MATLAB = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK")
DISSERTATION = Path(r"D:\Articles\2023年9月25日 博士毕业论文TEX稿件\Main_Spine")


SOURCES = {
    "python_hjb": REPO / "exports/matlab_faithful_two_asset_ha.py",
    "python_firm": REPO / "src/ch5_two_asset_hank/multi_province/firm.py",
    "python_adapter": REPO / "src/ch5_two_asset_hank/multi_province/household_adapter.py",
    "corrected_runtime": REPO / "src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py",
    "corrected_runner": REPO / "validators/multi_province/corrected_2018_single_turn/run.py",
    "matlab_hjb": MATLAB / "HANK_2ASSETS_HJB.m",
    "matlab_firm": MATLAB / "HANK_firm.m",
    "matlab_one_turn": MATLAB / "HANK_mp_1turn.m",
    "matlab_parameters": MATLAB / "multi_prov_HANK_12sts.m",
    "matlab_main": MATLAB / "main.m",
    "dissertation_c4": DISSERTATION / "c4.tex",
    "dissertation_c5": DISSERTATION / "c5.tex",
}


EXPECTED_FRAGMENTS = {
    "python_hjb": [
        "mu_b = inputs.r_b * b + labor_income - transfer - cost - consumption",
        "mu_a = r_a_effective * a + transfer",
        "matrix = (1/numerics.delta + params.rho)*sparse.eye",
        "MATLAB_DERIVATIVE_FLOOR = 1.0e-6",
    ],
    "python_firm": [
        "rk = mt * alpha / (kt / yt)",
        "ra0 = rk - delta + profit * (1.0 - corptau) / kt",
    ],
    "corrected_runtime": [
        '"firm_depreciation": FIRM_DEPRECIATION',
        '"rb_gap": 0.07, "nominal_rate": 0.02, "rb": 0.02',
    ],
    "corrected_runner": [
        "np.array([[-1/3, 1/3], [1/3, -1/3]])",
        "oracle.EconomicParams(0.05, 2.0, 5.0, 0.1, 2.0, 1e-6, 0.0, 0.0)",
        '"theta": 100.0, "delta": 0.025',
    ],
    "matlab_hjb": [
        "B = (1/Delta + rho)*speye(I*J*Nz) - A;",
        "raah = rah.*(1 - 0.1*(ahmax./ah).^(-9));",
    ],
    "matlab_firm": [
        "rk = mt*alpha/KYratio;",
        "ra0 = rk - delta + divrate;",
        "限制ra的范围，防止模型在收敛途中崩溃",
    ],
    "matlab_parameters": [
        "grid.ramax\t\t=\t0.09;",
        "grid.ramin\t\t=\t0.02;",
        "param.delta\t\t=\t0.025;",
        "param.rho\t\t=\t0.05;",
    ],
    "matlab_main": ["政策模拟只跑4期（一年，每一期一个季度）"],
    "dissertation_c4": [
        "连续时间异质性新凯恩斯模型",
        "每个季度资本折旧为2.5\\%，每年资本折旧率为10\\%",
    ],
    "dissertation_c5": [
        "算法首先从单一时期的省级数据出发",
        "$\\delta^i$ & 0.0025 & 厂商的资本折旧率",
    ],
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def source_identities() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for name, path in SOURCES.items():
        text = path.read_text(encoding="utf-8-sig")
        missing = [fragment for fragment in EXPECTED_FRAGMENTS.get(name, ()) if fragment not in text]
        if missing:
            raise ValueError(f"{name}: expected source fragments missing: {missing}")
        rows.append({
            "source": name,
            "path": str(path),
            "sha256": sha256(path),
            "expected_fragment_count": len(EXPECTED_FRAGMENTS.get(name, ())),
            "status": "READ_ONLY_STATIC_MATCH",
        })
    return rows


def time_unit_rows() -> list[dict[str, str]]:
    return [
        {"object": "household rho=.05", "authority": "MODEL_TIME_ONLY", "finding": "continuous-time discount intensity; no calendar unit stated for Chapter 5 value"},
        {"object": "household rb=.02 / borrowing gap=.07", "authority": "MODEL_TIME_ONLY", "finding": "enters liquid drift; calendar frequency not stated"},
        {"object": "household r_a/rah", "authority": "MODEL_TIME_ONLY", "finding": "enters illiquid drift and must share the HJB time unit"},
        {"object": "firm delta=.025", "authority": "CONFLICTING_SOURCE_AUTHORITY", "finding": "code=.025; c4 calls .025 quarterly; c5 table prints .0025 without a period"},
        {"object": "firm rk and profit/K", "authority": "SOURCE_CONFIRMED_ANNUAL", "finding": "corrected-2018 Y is annual GDP flow and K is an annual capital-stock object"},
        {"object": "firm ra0", "authority": "CONFLICTING_SOURCE_AUTHORITY", "finding": "annual flow/stock components are combined directly with quarterly-source delta"},
        {"object": "z transition generator 1/3", "authority": "MODEL_TIME_ONLY", "finding": "generator intensity is source literal; no calendar frequency stated"},
        {"object": "wjt/w and labor-income flow", "authority": "UNRESOLVED", "finding": "firm wage uses annual Y/L scale; HJB wage/grid numeraire and period bridge are absent"},
        {"object": "Tt, d, chi0=.1, chi1=2", "authority": "MODEL_TIME_ONLY", "finding": "flow/drift coefficients must share HJB time but have no calendar source"},
        {"object": "outer fixed-point turn", "authority": "SOURCE_CONFIRMED_OTHER", "finding": "numerical iteration only; explicitly not economic calendar time"},
    ]


def bound_rows() -> list[dict[str, str]]:
    return [
        {"object": "firm ra", "value": "[.02,.09]", "status": "active and legacy", "authority": "numerical safeguard", "source": "firm.py:112-125; HANK_firm.m:55-65"},
        {"object": "firm wjt", "value": "[.8,1.3]", "status": "active and legacy", "authority": "unresolved safeguard", "source": "firm.py:114-133; multi_prov_HANK_12sts.m:53-55"},
        {"object": "profit PIt", "value": "floor 0", "status": "active and legacy", "authority": "unresolved structural/numerical", "source": "firm.py:107-109; HANK_firm.m:48-51"},
        {"object": "liquid derivative Vb", "value": "floor 1e-6", "status": "active faithful", "authority": "numerical safeguard", "source": "matlab_faithful_two_asset_ha.py:169-175,274-277"},
        {"object": "consumption", "value": "no direct floor; induced cap 1000 at gamma=2 from Vb floor", "status": "active faithful", "authority": "numerical consequence", "source": "matlab_faithful_two_asset_ha.py:126-129,274-277"},
        {"object": "adjustment-cost denominator a", "value": "floor a_bar=1e-6", "status": "active and legacy", "authority": "numerical safeguard", "source": "matlab_faithful_two_asset_ha.py:82; multi_prov_HANK_12sts.m:28-30"},
        {"object": "asset state grids", "value": "b in [-2,5], a in [0,10]", "status": "active and legacy", "authority": "finite-domain numerical boundary", "source": "multi_prov_HANK_12sts.m:35-42"},
        {"object": "productivity state grid", "value": "z in [.8,1.3]", "status": "active and legacy", "authority": "unresolved calibration", "source": "multi_prov_HANK_12sts.m:43-47"},
        {"object": "transfer d", "value": "no finite hard cap; chi0 soft threshold and grid sign guards", "status": "active and legacy", "authority": "structural FOC plus numerical boundary", "source": "HANK3_FOC.m:13-19; matlab_faithful_two_asset_ha.py:312-375"},
        {"object": "labor", "value": "no explicit hard upper bound; nonnegative formula", "status": "active and legacy", "authority": "structural domain", "source": "matlab_faithful_two_asset_ha.py:131-136"},
        {"object": "effective illiquid return taper", "value": "1 to .9 across a grid", "status": "active and legacy", "authority": "source-faithful boundary taper, not a ra0 scale map", "source": "matlab_faithful_two_asset_ha.py:111-124"},
        {"object": "GovInv residual", "value": "floor 0", "status": "active C1 successor", "authority": "Owner-frozen structural accounting", "source": "government_assets.py:74-108"},
    ]


def mapping_rows() -> list[dict[str, str]]:
    return [
        {"candidate": "A identity r_a=ra0", "source_fidelity": "legacy wiring only", "dimensional_consistency": "FAIL", "ranking": "preserved", "absolute_scale": "unchanged", "status": "NOT_AUTHORIZED"},
        {"candidate": "B annual firm-flow to quarterly HJB flow", "source_fidelity": "source-motivated but not frozen", "dimensional_consistency": "conditional", "ranking": "preserved if common linear conversion", "absolute_scale": "changes", "status": "OWNER_SOURCE_FREEZE_REQUIRED"},
        {"candidate": "C log/discrete-to-continuous conversion", "source_fidelity": "no gross/discrete return authority", "dimensional_consistency": "not assessable", "ranking": "not assessed", "absolute_scale": "would change", "status": "UNSUPPORTED"},
        {"candidate": "D dissertation ra=rk-delta+profit/K", "source_fidelity": "equation confirmed", "dimensional_consistency": "FAIL under current annual/quarterly operands", "ranking": "preserved algebraically", "absolute_scale": "unchanged", "status": "NOT_AUTHORIZED_AS_NUMERICAL_MAP"},
        {"candidate": "E temporary diagnostic bounds", "source_fidelity": "Owner permits future scaffolding", "dimensional_consistency": "not an economic mapping", "ranking": "can truncate", "absolute_scale": "clips", "status": "FUTURE_EXACT_TASK_ONLY"},
    ]


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("x", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", errors="strict")


def build(output: Path) -> None:
    output.mkdir(parents=True, exist_ok=False)
    identities = source_identities()
    write_json(output / "source_identity.json", identities)
    write_csv(output / "time_unit_authority.csv", time_unit_rows())
    write_csv(output / "hard_bound_inventory.csv", bound_rows())
    write_csv(output / "candidate_mapping_table.csv", mapping_rows())
    ledger = {
        "classification": "ZERO_SCIENCE_STATIC_TEXT_AUDIT",
        "trajectory": 0, "hjb": 0, "kfe": 0, "household_runtime": 0,
        "firm_runtime": 0, "matlab_runtime": 0, "k1b": 0, "k2": 0,
        "ge": 0, "annual": 0, "irf_shock": 0, "results": 0,
    }
    write_json(output / "zero_science_call_ledger.json", ledger)
    files = sorted(path for path in output.iterdir() if path.name != "manifest.sha256")
    with (output / "manifest.sha256").open("x", encoding="ascii", newline="\n") as stream:
        for path in files:
            stream.write(f"{sha256(path)}  {path.name}\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    build(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
