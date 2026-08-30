"""Construct and compare the MP4B Python pre-solver identity manifest."""

from __future__ import annotations
import json
from pathlib import Path
from typing import Any
import numpy as np

CANONICAL_SHA256 = "507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48"


def python_manifest(canonical_path: Path) -> dict[str, Any]:
    canonical = json.loads(Path(canonical_path).read_text(encoding="utf-8"))
    grid = {"I":20,"bmin":-2,"bmax":5,"J":20,"amin":0,"amax":10,"Nz":2,
            "zmin":0.8,"zmax":1.3,"z":[0.8,1.3],
            "la_mat":[[-1/3,1/3],[1/3,-1/3]],
            "ramax":0.09,"ramin":0.02,"wjtmax":1.3,"wjtmin":0.8}
    param = {"ga":2,"phi_l":5,"alphal":1,"alphap":1,"frisch_l":0.2,"rho":0.05,
             "rho_pi":1.25,"epsilon":10,"theta":100,"delta":0.025,"istar":0.015,
             "pistar":0.0075,"max_phi":0.3,"max_sigmau":0.5,"smooth_method":0,
             "reg_method":0,"GDP_multiplier":1000,"POP_multiplier":100,"Ztratio":1,
             "GovInv_ratio":1}
    num = {"maxit":100,"crit":1e-7,"reg_threshold":1e-9,"homecrit":1e-2,
           "Delta":1000,"maxiter":100,"max2iter":200,"max3iter":500}
    chi = {"chi0":0.1,"chi1":2,"a_bar":1e-6,"fixcost":0,"fixcost2":0}
    init = {"alpha":0.6,"rb_gap":0.07,"rah":0.09,"ra":0.09,"it":0.02,"rb":0.02,
            "rk":0.1,"wjt":0.6,"w":20,"Tt":0.1,"Zt":6,"pit":0.02,"pit_1":0.02,
            "totalpit":0.02,"epsilon_pi":0,"tau":0.05,"At":2,"Bt":1,"mt":0.9,
            "Lt":0.8,"Ct":4,"GovInv":1000,"GovSurplus":0,"inter_prv_ratio":0.5,
            "Lt_mat":np.zeros((31,31)).tolist(),"corptau":0.25}
    source_values = list(canonical["source_hashes"].values())
    normalized_hashes = {"filled_workbook":source_values[0], "regression_workbook":source_values[1],
                         "distance_workbook":source_values[2]}
    return {"schema":"CH5_MP4B_PRESOLVER_MANIFEST_V1","canonical_sha256":CANONICAL_SHA256,
            **{k:canonical[k] for k in ("binding","province_order","scalars","vectors","matrices")},
            "source_hashes":normalized_hashes,
            "param":param,"grid":grid,"num":num,"CHI":chi,"init":init,"province_count":31}


def compare_manifests(matlab: Any, python: Any, path: str = "$") -> list[str]:
    mismatches: list[str] = []
    if isinstance(python, dict):
        if not isinstance(matlab, dict) or set(matlab) != set(python):
            return [path + ": key/type mismatch"]
        for key in python: mismatches.extend(compare_manifests(matlab[key], python[key], f"{path}.{key}"))
    elif isinstance(python, list):
        if not isinstance(matlab, list) or len(matlab) != len(python): return [path + ": shape mismatch"]
        for i, value in enumerate(python): mismatches.extend(compare_manifests(matlab[i], value, f"{path}[{i}]"))
    elif isinstance(python, (int,float)) and not isinstance(python, bool):
        if not isinstance(matlab, (int,float)) or float(matlab) != float(python): mismatches.append(path)
    elif matlab != python: mismatches.append(path)
    return mismatches
