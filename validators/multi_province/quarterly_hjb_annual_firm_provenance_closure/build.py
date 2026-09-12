"""Static-only provenance receipts; never imports the scientific runtime."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
MATLAB = Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK")
SPINE = Path(r"D:\Articles\2023年9月25日 博士毕业论文TEX稿件\Main_Spine")

SOURCES = {
    "c4": SPINE / "c4.tex", "c5": SPINE / "c5.tex",
    "matlab_params": MATLAB / "multi_prov_HANK_12sts.m",
    "matlab_hjb": MATLAB / "HANK_2ASSETS_HJB.m",
    "matlab_firm": MATLAB / "HANK_firm.m",
    "python_hjb": REPO / "exports/matlab_faithful_two_asset_ha.py",
    "python_firm": REPO / "src/ch5_two_asset_hank/multi_province/firm.py",
    "runtime": REPO / "src/ch5_two_asset_hank/multi_province/corrected_2018_runtime.py",
}

CHECKS = {
    "c4": ["每个季度资本折旧为2.5\\%，每年资本折旧率为10\\%", "连续时间异质性新凯恩斯模型"],
    "c5": ["$\\delta^i$ & 0.0025 & 厂商的资本折旧率", "$\\rho^i$ & 0.05 & 家户折现率"],
    "matlab_params": ["param.delta\t\t=\t0.025;", "param.rho\t\t=\t0.05;", "grid.la_mat"],
    "matlab_hjb": ["B = (1/Delta + rho)*speye", "raah = rah.*"],
    "matlab_firm": ["ra0 = rk - delta + divrate;", "rk = mt*alpha/KYratio;"],
    "python_hjb": ["mu_a = r_a_effective * a + transfer", "MATLAB_DERIVATIVE_FLOOR = 1.0e-6"],
    "python_firm": ["rk = mt * alpha / (kt / yt)", "ra0 = rk - delta + profit"],
    "runtime": ['"calibration_delta": DELTA_PIM', '"firm_depreciation": FIRM_DEPRECIATION'],
}

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()

def identities() -> list[dict[str, str]]:
    rows=[]
    for name,path in SOURCES.items():
        text=path.read_text(encoding="utf-8-sig")
        missing=[x for x in CHECKS[name] if x not in text]
        if missing: raise ValueError(f"{name}: missing {missing}")
        rows.append({"source":name,"path":str(path),"sha256":sha(path),"status":"STATIC_READ_ONLY_MATCH"})
    return rows

def depreciation() -> list[dict[str,str]]:
    return [
      {"source":"dissertation c4:247","value":".025 quarterly; prose says .10 annual","role":"firm depreciation calibration","authority":"SOURCE_CONFIRMED_BUT_SIMPLE_ANNUAL_APPROXIMATION"},
      {"source":"dissertation c5:236","value":".0025; no period","role":"Chapter-5 parameter table","authority":"CONFLICTING"},
      {"source":"protected MATLAB parameters:69","value":".025; no period comment","role":"firm literal","authority":"LEGACY_INHERITED_ONLY"},
      {"source":"active corrected runner:414","value":".025","role":"firm literal","authority":"LEGACY_INHERITED_ONLY"},
      {"source":"corrected runtime/data contract","value":".096 annual","role":"PIM capital-stock construction","authority":"SOURCE_CONFIRMED_DISTINCT_OBJECT"},
    ]

def provenance() -> list[dict[str,str]]:
    return [
      {"object":"rho=.05","source_statement":"c5 value; no period","legacy":"MATLAB literal","python":"EconomicParams","usage":"rho*V","class":"UNRESOLVED"},
      {"object":"rb=.02; gap=.07","source_statement":"no calendar source","legacy":"initial literals","python":"HouseholdInputs","usage":"liquid drift","class":"LEGACY_INHERITED_ONLY"},
      {"object":"r_a/rah","source_statement":"continuous-time asset drift","legacy":"direct composite of firm ra","python":"HouseholdInputs.r_a","usage":"illiquid drift","class":"CONFLICTING"},
      {"object":"delta","source_statement":"c4 quarterly .025; c5 .0025","legacy":".025","python":".025","usage":"annual-flow ra0 formula","class":"CONFLICTING"},
      {"object":"Q_z=1/3","source_statement":"jump process, no calibrated period","legacy":"generator literal","python":"switch matrix","usage":"Q_z V","class":"UNRESOLVED"},
      {"object":"chi0=.1; chi1=2","source_statement":"no time normalization","legacy":"literals/FOC","python":"EconomicParams/FOC","usage":"d and adjustment cost","class":"LEGACY_INHERITED_ONLY"},
      {"object":"Tt=.1","source_statement":"no currency/time source","legacy":"initial literal","python":"transfer_income","usage":"liquid flow","class":"UNRESOLVED"},
      {"object":"ra [.02,.09]","source_statement":"convergence crash guard","legacy":"firm clip","python":"firm clip","usage":"legacy return","class":"NUMERICAL_SAFEGUARD"},
      {"object":"wjt [.8,1.3]","source_statement":"no absolute scale source","legacy":"firm clip","python":"firm clip","usage":"firm wage","class":"NUMERICAL_SAFEGUARD"},
      {"object":"Vb floor 1e-6","source_statement":"no economic calibration","legacy":"HJB max","python":"faithful floor","usage":"consumption/labor FOC","class":"NUMERICAL_SAFEGUARD"},
    ]

def conventions() -> list[dict[str,str]]:
    return [
      {"convention":"Q quarterly HJB","support":"quarterly delta and quarterly shock clock only; stationary HJB not identified","required":"convert annual Y/K, profit/K, wage/profit/consumption/transfer/cost flows; freeze rho,rb,Q_z","ranking":"common linear flow scaling would preserve component rankings","effect":"calibration/economics unless all primitives coherently frozen","status":"NOT_SOURCE_CLOSED"},
      {"convention":"A annual HJB","support":"annual empirical firm operands only; HJB base not identified","required":"convert quarterly delta with an identified law; freeze rho,rb,Q_z and all flows","ranking":"depends on chosen conversion","effect":"calibration/economics","status":"NOT_SOURCE_CLOSED"},
      {"convention":"M abstract model time","support":"matches current explicit authority boundary","required":"Owner freezes base period, object types, conversions, numeraire and every HJB flow/rate","ranking":"not assessable until freeze","effect":"new calibration contract","status":"ONLY_TRUTHFUL_CURRENT_CONVENTION"},
    ]

def write_csv(path:Path, rows:list[dict[str,str]]) -> None:
    with path.open("x",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

def build(out:Path) -> None:
    out.mkdir(parents=True,exist_ok=False)
    (out/"source_identities.json").write_text(json.dumps(identities(),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    write_csv(out/"depreciation_provenance.csv",depreciation())
    write_csv(out/"calibration_provenance.csv",provenance())
    write_csv(out/"candidate_conventions.csv",conventions())
    ledger={k:0 for k in ("trajectory","outer_turn","hjb","kfe","household_runtime","firm_runtime","matlab_runtime","k1b","k2","ge","annual","shock_irf","results")}
    (out/"zero_science_call_ledger.json").write_text(json.dumps(ledger,indent=2)+"\n",encoding="utf-8")
    files=sorted(out.iterdir())
    with (out/"manifest.sha256").open("x",encoding="ascii",newline="\n") as f:
        for p in files: f.write(f"{sha(p)}  {p.name}\n")

def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("output",type=Path); a=p.parse_args(); build(a.output.resolve()); return 0

if __name__ == "__main__": raise SystemExit(main())
