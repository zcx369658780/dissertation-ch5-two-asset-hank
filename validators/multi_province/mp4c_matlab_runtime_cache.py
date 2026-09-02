"""Read-only adapter for the Owner-designated protected MATLAB runtime cache."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from typing import Any, Mapping
import h5py
import numpy as np

from ch5_two_asset_hank.multi_province.annual import DecoupledAnnualIndex, _normalize_province, _xlsx_sheet_rows
from ch5_two_asset_hank.multi_province.province_contracts import PROVINCE_ORDER

EXPECTED_CACHE_SHA256="923CC9E592C14B320C624509A0B498DBCC7D2533F77F0E4B4793521B10849E9A"
REPRESENTATION="MATLAB_PROTECTED_RUNTIME_DATA_CACHE"
YEARS=tuple(range(2009,2024)); INDUSTRY_MATLAB_INDEX=4
REQUIRED_FIELDS=("prvname","GDP","CAP","POP","log_pgdp","log_pcap","IND_alpha","IND_Zt","GDP_multiplier","POP_multiplier","delta")

def file_sha256(path:Path)->str:
    h=sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):h.update(block)
    return h.hexdigest().upper()

def _text(h5:h5py.File,ref)->str:
    return "".join(chr(int(x)) for x in np.asarray(h5[ref][()]).reshape(-1,order="F"))

def _numeric(h5:h5py.File,ref)->np.ndarray:
    raw=np.asarray(h5[ref][()])
    if raw.dtype.fields and set(raw.dtype.fields)=={"real","imag"}: raw=raw["real"]+1j*raw["imag"]
    return raw.T

def _cell_numeric(h5:h5py.File,group:h5py.Group,field:str,matlab_index:int)->np.ndarray:
    cell=group[field]
    if cell.shape!=(4,1):raise ValueError(f"wrong cache schema for {field}: {cell.shape}")
    return _numeric(h5,cell[matlab_index-1,0])

def inspect_cache(path:Path,expected_sha:str=EXPECTED_CACHE_SHA256)->dict[str,Any]:
    path=Path(path);actual=file_sha256(path)
    if actual!=expected_sha:raise ValueError(f"runtime cache SHA mismatch: {actual} != {expected_sha}")
    with h5py.File(path,"r") as h5:
        if set(h5.keys())!={"#refs#","mydata2"}:raise ValueError("wrong runtime cache top-level schema")
        entries=h5["mydata2"]
        if entries.shape!=(15,1):raise ValueError(f"wrong mydata2 entry shape: {entries.shape}")
        summaries=[];normalized_axis=None
        for index in range(15):
            group=h5[entries[index,0]]
            if set(group.keys())!=set(REQUIRED_FIELDS):raise ValueError(f"wrong fields in mydata2 entry {index+1}")
            names=[_text(h5,group["prvname"][i,0]) for i in range(31)]
            normalized=tuple(_normalize_province(x) for x in names)
            if normalized!=PROVINCE_ORDER:raise ValueError(f"wrong province order in entry {index+1}")
            normalized_axis=normalized_axis or normalized
            shapes={field:list(_cell_numeric(h5,group,field,4).shape) for field in ("GDP","CAP","POP","log_pgdp","log_pcap","IND_alpha","IND_Zt")}
            if any(shapes[f]!=[24,31] for f in ("GDP","CAP","POP","log_pgdp","log_pcap")) or any(shapes[f]!=[1,31] for f in ("IND_alpha","IND_Zt")):raise ValueError(f"wrong array schema in entry {index+1}")
            summaries.append({"matlab_entry_index":index+1,"calendar_year":2009+index,"fields":sorted(group.keys()),"shapes":shapes})
        return {"schema":"CH5_MP4C_MATLAB_RUNTIME_CACHE_STRUCTURE_V1","representation":REPRESENTATION,"cache_path":str(path.resolve()),"cache_sha256":actual,"top_level_variables":["mydata2"],"mydata2_shape":[15,1],"entry_count":15,"industry_matlab_index":4,"province_order":list(normalized_axis),"entries":summaries}

def load_runtime_year(path:Path,year:int,expected_sha:str=EXPECTED_CACHE_SHA256)->dict[str,Any]:
    year=int(year);binding=DecoupledAnnualIndex.for_calendar_year(year)
    if year not in YEARS:raise ValueError("runtime cache calendar year outside 2009-2023")
    actual=file_sha256(Path(path))
    if actual!=expected_sha:raise ValueError(f"runtime cache SHA mismatch: {actual} != {expected_sha}")
    entry_index=binding.analysis_index; row_index=binding.data_mat_index
    with h5py.File(path,"r") as h5:
        entries=h5.get("mydata2")
        if entries is None or entries.shape!=(15,1):raise ValueError("wrong mydata2 schema")
        group=h5[entries[entry_index-1,0]]
        if set(group.keys())!=set(REQUIRED_FIELDS):raise ValueError("wrong runtime cache field schema")
        original_names=[_text(h5,group["prvname"][i,0]) for i in range(31)]
        names=tuple(_normalize_province(x) for x in original_names)
        if names!=PROVINCE_ORDER:raise ValueError("wrong runtime cache province order")
        arrays={f:_cell_numeric(h5,group,f,4) for f in ("GDP","CAP","POP","log_pgdp","log_pcap","IND_alpha","IND_Zt")}
        if any(arrays[f].shape!=(24,31) for f in ("GDP","CAP","POP","log_pgdp","log_pcap")) or any(arrays[f].shape!=(1,31) for f in ("IND_alpha","IND_Zt")):raise ValueError("wrong runtime cache array shape")
        selected={f:(arrays[f][row_index-1].copy() if arrays[f].shape[0]==24 else arrays[f][0].copy()) for f in arrays}
        for field,value in tuple(selected.items()):
            if np.iscomplexobj(value):
                if not np.all(np.abs(value.imag)<=1e-14):raise ValueError(f"complex runtime cache values for {year} field {field}")
                selected[field]=value.real.astype(np.float64)
            else:selected[field]=np.asarray(value,dtype=np.float64)
        if not all(np.isfinite(v).all() for v in selected.values()):raise ValueError(f"non-finite runtime cache values for {year}")
        if not np.all(selected["CAP"]>0) or not np.all(selected["GDP"]>0) or not np.all(selected["POP"]>0):raise ValueError(f"inadmissible runtime levels for {year}")
        if not np.all((selected["IND_alpha"]>0)&(selected["IND_alpha"]<1)) or not np.all(selected["IND_Zt"]>0):raise ValueError(f"inadmissible runtime parameters for {year}")
        if not np.allclose(selected["log_pcap"],np.log(selected["CAP"]/selected["POP"]),rtol=0,atol=1e-12) or not np.allclose(selected["log_pgdp"],np.log(selected["GDP"]/selected["POP"]),rtol=0,atol=1e-12):raise ValueError("runtime cache log fields contradict level fields")
        gdp_multiplier=float(np.asarray(group["GDP_multiplier"][()]).reshape(-1)[0]);pop_multiplier=float(np.asarray(group["POP_multiplier"][()]).reshape(-1)[0]);delta=float(np.asarray(group["delta"][()]).reshape(-1)[0])
    pcap=np.exp(selected["log_pcap"]);ratios=0.3*(pcap-pcap.min())/(pcap.max()-pcap.min())
    return {"schema":"CH5_MP4C_MATLAB_RUNTIME_YEAR_INPUT_V1","representation":REPRESENTATION,"cache_sha256":actual,"binding":{k:getattr(binding,k) for k in ("calendar_year","analysis_index","workbook_data_row_index","data_mat_index","output_filename_year","regression_vintage_key")},"cache_entry_index_matlab_1based":entry_index,"cache_data_year_index_matlab_1based":row_index,"industry_matlab_index":4,"province_order":list(names),"cache_province_labels":original_names,"scalars":{"gdp_multiplier":gdp_multiplier,"pop_multiplier":pop_multiplier,"calibration_delta":delta},"vectors":{k:v.tolist() for k,v in selected.items()},"derived":{"gov_inv":selected["CAP"].tolist(),"inter_province_asset_ratio":ratios.tolist()},"source_field_paths":{f:f"mydata2{{{entry_index}}}.{f}{{4}}({row_index},:)" for f in selected}}

def add_runtime_support(runtime:dict[str,Any],*,distance_workbook:Path,distance_sha256:str,max_sigmau:float)->dict[str,Any]:
    if file_sha256(Path(distance_workbook))!=distance_sha256:raise ValueError("distance workbook SHA mismatch")
    rows=_xlsx_sheet_rows(Path(distance_workbook),"geom")
    row_axis=tuple(_normalize_province(rows[r][1]) for r in range(2,33));col_axis=tuple(_normalize_province(rows[1][c]) for c in range(2,33))
    if row_axis!=PROVINCE_ORDER or col_axis!=PROVINCE_ORDER:raise ValueError("distance axes mismatch")
    distance=np.array([[rows[r][c] for c in range(2,33)] for r in range(2,33)],float)
    result=dict(runtime);result["runtime_support"]={"distance_sha256":distance_sha256,"sigmau_destination_origin":(distance/distance.max()*float(max_sigmau)).tolist(),"orientation":"destination_row_x_origin_column"};return result

def canonical_bytes(payload:Mapping[str,Any])->bytes:
    return (json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode("utf-8")

def entry_states(payload:Mapping[str,Any],accepted_scalars:Mapping[str,float])->tuple[dict[str,Any],...]:
    if payload.get("representation")!=REPRESENTATION or payload.get("cache_sha256")!=EXPECTED_CACHE_SHA256:raise ValueError("runtime input identity mismatch")
    vectors=payload["vectors"];derived=payload["derived"];names=payload["province_order"]
    if tuple(names)!=PROVINCE_ORDER:raise ValueError("runtime input province order mismatch")
    states=[]
    for i,name in enumerate(names):
        state={"name":name,"N":vectors["POP"][i],"alpha":vectors["IND_alpha"][i],"Zt":vectors["IND_Zt"][i],"Kt0":vectors["CAP"][i],"Kt":vectors["CAP"][i],"Kt_prev":vectors["CAP"][i],"Lt":vectors["POP"][i],"Lt_prev":vectors["POP"][i],"Yt0":vectors["GDP"][i],"Yt":vectors["GDP"][i],"Zt_1":vectors["IND_Zt"][i],"GovInv":derived["gov_inv"][i],"inter_prv_ratio":derived["inter_province_asset_ratio"][i],"rb_gap":accepted_scalars["rb_gap"],"rah":accepted_scalars["rah"],"ra":accepted_scalars["ra"],"it":accepted_scalars["nominal_rate"],"rb":accepted_scalars["rb"],"rk":accepted_scalars["rk"],"wjt":accepted_scalars["wjt"],"w":accepted_scalars["composite_wage"],"Tt":accepted_scalars["transfer_income"],"pit":accepted_scalars["inflation"],"pit_1":accepted_scalars["inflation"],"totalpit":accepted_scalars["inflation"],"epsilon_pi":0.0,"tau":accepted_scalars["wage_tax"],"At":accepted_scalars["initial_at"],"Bt":accepted_scalars["initial_bt"],"mt":accepted_scalars["initial_mt"],"Ct":accepted_scalars["initial_ct"],"AtTax":0.0,"GovSurplus":0.0,"corptau":accepted_scalars["corporate_tax"],"ramin":0.02,"ramax":0.09,"wjtmin":0.8,"wjtmax":1.3}
        if not np.isfinite(np.array([v for v in state.values() if isinstance(v,(int,float))],float)).all():raise ValueError("non-finite runtime entry state")
        states.append(state)
    return tuple(states)
