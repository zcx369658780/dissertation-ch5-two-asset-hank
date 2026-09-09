"""Package the saved static audit; no model, solver, or MATLAB entry points."""
import base64, csv, hashlib, json, re, shutil, subprocess, sys
from pathlib import Path

REPO=Path(__file__).resolve().parents[3]
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()
def write(p,v): Path(p).write_text(json.dumps(v,ensure_ascii=False,allow_nan=False,indent=2)+"\n",encoding="utf-8",newline="\n")

def main(evidence,out,report):
 evidence=Path(evidence).resolve(); out=Path(out).resolve(); report=Path(report).resolve(); summary=json.loads((out/"summary.json").read_text(encoding="utf-8")); inv=json.loads((out/"source_inventory.json").read_text(encoding="utf-8")); cache=summary["cache_audit"]
 contract={"province_axis":{"count":31,"headers":"GDP!C1:AG1","order":summary["province_order"],"anhui":{"matlab_1based":12,"python_0based":11,"excel_column":"N"}},"year_axis":{"workbook":"rows 2:25 are calendar 2000:2023","annual_source":{"multi_prov_HANK_12sts_lines":"118-133","filename":"ii+2008","cache_cell":"mydata2{ii}","data_year":"ii","actual_workbook_year":"1999+ii"},"ii_10":{"filename_year":2018,"actual_level_year":2009,"regression_vintage":19,"Zt_level_anchor_year":2020}},"raw_to_filled":{"source":"load_GDPdata.m lines 5-67","raw_range":"B2:AG25; C:AG are 31 provinces after dropping national B","mechanism":"fillmissing(...,'makima')","runtime_behavior":"because filled workbook exists, lines 74-90 read it directly and do not regenerate it"},"consumed_fields":{"GDP{4}":{"sheet":"GDP","range":"C2:AG25","transform":"*1000","source_lines":"74,93"},"CAP{4}":{"source_sheet":"固定资产投资额","derived_sheet":"总资本存量","range":"C2:AG25","transform":"It_to_Kt(delta=.096), then *1000","source_lines":"56,60-61,75,94"},"POP{4}":{"sheet":"常住人口","range":"C2:AG25","transform":"*100","source_lines":"79,104"},"log_pgdp{4}":{"transform":"log(GDP{4}/POP{4})","source_line":"126"},"log_pcap{4}":{"transform":"log(CAP{4}/POP{4})","source_line":"127"},"IND_alpha{4}":{"workbook":"R语言估计结果_plm估计.xlsx","sheet_pattern":"总面板回归系数_{ii+9}_行业4","selection":"last numeric xlsread value","source_lines":"115-120,131"},"IND_Zt{4}":{"transform":"GDP(row21)*CAP(row21)^(-alpha)*POP(row21)^(alpha-1)","row21_year":2020,"source_lines":"132-137"}},"capital_recurrence":{"K0":"I0/0.1","Kt":"(1-.096)*K(t-1)+I(t-1)","source":"It_to_Kt.m lines 1-10"},"annual_initializer":{"fields":["Zt","alpha","Kt0/Kt","N/Lt","Yt0/Yt","pcap","pgdp","GovInv","inter_prv_ratio"],"source":"mpHANK_equilibrium_2000.m lines 21-49"},"smoothing_and_regression":{"smooth_method":0,"reg_method":0,"note":"production call selects raw log ratios plus external PLM alpha; movmean/movmedian and MATLAB regress branches are inactive"},"cache":{"file":"数据估计结果_1000_100_0.mat","format":"MATLAB v7.3/HDF5","entry":"mydata2{10}","identity":"GDP/CAP/POP exactly match filled transforms; log arrays differ only binary rounding","metadata_conflict":cache["metadata_conflict"]}}
 write(out/"data_contract.json",contract); write(out/"call_ledger.json",summary["zero_model_call_ledger"])
 env=dict(PYTHONIOENCODING="utf-8",PYTHONDONTWRITEBYTECODE="1"); command=[sys.executable,"-B",str(REPO/"tests/test_mp4c_2018_raw_data_audit.py")]; result=subprocess.run(command,cwd=REPO,env={**__import__('os').environ,**env},stdout=subprocess.PIPE,stderr=subprocess.STDOUT); raw=result.stdout; text=raw.decode("utf-8").replace("\r\n","\n"); (out/"tests.txt").write_text(text,encoding="utf-8",newline="\n"); match=re.search(r"Ran (\d+) tests",text); receipt={"command":command,"returncode":result.returncode,"ran":int(match.group(1)) if match else None,"individual_ok":len(re.findall(r" \.\.\. ok$",text,re.M)),"sha256":hashlib.sha256(raw).hexdigest().upper(),"passed":result.returncode==0 and "\nOK\n" in text}; write(out/"tests_receipt.json",receipt); assert receipt["passed"] and receipt["ran"]==receipt["individual_ok"]==6
 lineage=list(csv.DictReader((out/"anhui_2018_lineage.csv").open(encoding="utf-8-sig"))); get=lambda f:next(x for x in lineage if x["field"]==f); g=get("Yt0/GDP"); p=get("N/POP"); k=get("Kt0/CAP"); lp=get("pcap/log_pcap"); z=get("Zt")
 complex_rows=cache["complex_log_pcap_cells"]; panel=summary["panel_summary"]; cross=summary["workbook_2024_comparison"]
 source_hashes="\n".join(f"- `{Path(x['path']).name}`: `{x['sha256']}`" for x in inv)
 material_rows="\n".join(f"| {x['variable']} | {x['year']} | `{x['issue']}` | {x['detail']} |" for x in summary["material_findings"])
 text=f"""# Chapter 5 MP4C 2018 原始数据与插值/缺失值来源审计报告

- Classification: `MATERIAL_DATA_QUALITY_OR_LINEAGE_ISSUE_FOUND`、`PARTIAL_EVIDENCE_NEEDS_OFFICIAL_DATA`。
- Results eligibility: `FALSE`。
- 模型、HJB、KFE、firm、one-turn、GE、年度、MATLAB、root/direct/eigen调用均为0。

## 核心结论

原MATLAB年度入口存在已证实的年份错位。`multi_prov_HANK_12sts(ii,pp)` 用 `ii+2008` 命名年度文件，却把 `data_MAT{{ii}}` 和 `data_year=ii` 直接传入初始化器。工作簿数据第1行是2000，所以 `ii=10` 的“2018”运行实际取第10行，即2009，而不是2018。HDF5 cache `mydata2{{10}}`、源码字段路径和已保存2018 runtime输入的31省向量逐位一致，全部对应2009行；该runtime JSON中的 `workbook_data_row_index=19` 元数据与实际向量矛盾。

安徽位于31省轴第12位（零基11），Excel列N。2018标签下实际消费：GDP原始/填充值 `{g['filled_value']}` 亿元（GDP!N11，2009），变换后 `{g['cache_or_final_value']}`；常住人口 `{p['filled_value']}` 万人（常住人口!N11），变换后 `{p['cache_or_final_value']}`；资本存量 `{k['filled_value']}`（总资本存量!N11），变换后 `{k['cache_or_final_value']}`。对应真正2018单元格N20分别为GDP `{g['intended_2018_filled']}`、常住人口 `{p['intended_2018_filled']}`、派生资本存量 `{k['intended_2018_filled']}`，变换后分别 `{g['intended_2018_transformed']}`、`{p['intended_2018_transformed']}`、`{k['intended_2018_transformed']}`。

技术参数也混合年份：vintage19、行业4的alpha取R系数表最后数值B11=`0.772866243094144`并复制到31省；Zt固定使用数组第21行，即2020年GDP/CAP/POP构造。安徽保存Zt=`{z['cache_or_final_value']}`。因此2018标签状态把2009水平量、vintage19共同alpha和2020水平锚定Zt组合在一起。

## 原始、填充与派生链

loader枚举14个原始sheet，范围B2:AG25；B列是全国，实际31省为C:AG。只有填充工作簿不存在时才对各矩阵执行 `fillmissing(...,'makima')` 并写出；当前文件已存在，运行时直接读取其保存值。总资本和三行业资本按 `K0=I0/.1`、`Kt=(1-.096)K(t-1)+I(t-1)` 递推，四张资本sheet 744/744个单元与源码公式逐位一致。GDP/CAP/POP cache与填充变换744/744逐位一致；log数组仅有binary64舍入差。

总GDP 744个省年均原始未改。直接进入总量路径的常住人口有3个endpoint填充；总固定资产投资有129个原始缺失/非数值被填，其中128个属于尾端外推风险、1个内部填充。更广泛行业sheet存在大量连续缺失和endpoint填充，详见panel summary与外部10416行cell ledger。非缺失值没有被自动称为插值；机制不明的变化使用 `CHANGED_MECHANISM_UNRESOLVED`。

派生总资本出现6个负值并使MATLAB `log_pcap` 产生虚部π：{'; '.join(f"{x['province']} {x['year']} CAP={x['CAP']}" for x in complex_rows)}。这些集中在2022–2023，未直接进入本次2018标签的2009行，但证明endpoint填充与资本递推可生成经济上不可接受的派生量。

## 源文件身份与物质性异常表

{source_hashes}

| 变量 | 年份/标签 | 分类 | 证据 |
|---|---:|---|---|
{material_rows}

完整异常明细见 `reports/mp4c_2018_raw_data_audit_20260909/anomalies.csv`；该表只含定位审计所需的摘要值和源单元格引用，不含原始工作簿副本。

## 2024原始版与schema

`2024年数据原始版.xlsx` 的Sheet0按显式变量/单位/年份header与旧原始工作簿映射。13个可比变量的全部可比数值逐位一致；例如GDP 744/744一致。就业人数列为`--`，因此标记 `NOT_COMPARABLE`，没有强行合并。Sheet2是单独的年份×省份表，缺少可证明的逻辑变量header，只作schema线索，不纳入值合并。

## 质量判断与官方核验

年份错位直接改变2018标签下的GDP、人口、资本、人均量和GovInv初值，属于物质性lineage问题。元数据把实际row10写成row19，会掩盖该问题。负资本/复数log是独立的panel数据质量问题。当前证据足以停止在报告阶段，但不足以自行选择官方修正值。

`official_data_request.csv` 列出安徽2018 GDP、常住人口、2000–2018投资/资本存量链、alpha/Zt口径，以及6个负资本省年的精确人工核验请求。建议优先核对国家统计局分地区年度数据与相应省统计年鉴，并由Owner决定年份映射、资本存量构造和技术参数口径；本任务未修改任何数据或生产loader。

## 检查、证据与边界

6/6项synthetic tests通过，覆盖年份/省份映射、缺失分类、连续缺失段、单位/lineage bookkeeping和import-time零科学。MAT cache以v7.3/HDF5只读解析；旧R工作簿存在缺失drawing XML，审计器绕过无关系图形，直接从指定sheet OOXML读取缓存数值。2024 comparison摘要：{sum(x['numeric_comparable_cells'] for x in cross.values())}个数值单元可比，差异0。

完整cell ledger仅存外部证据根 `{evidence}`，未提交原始Excel/MAT副本或可重建工作簿的大型全量值。仓库只保存源hash、契约、安徽lineage、异常摘要、官方请求、测试与manifest。由于已发现物质性问题，下一步必须等待Owner选择官方数据和修正语义；不得在本任务继续外层算法实验。
"""
 report.write_text(text,encoding="utf-8",newline="\n")
 outputs=[]
 paths=[report,REPO/"tests/test_mp4c_2018_raw_data_audit.py",*sorted((REPO/"validators/multi_province/data_audit").glob("*.py")),*sorted(out.rglob("*"))]
 for pth in paths:
  if pth.is_file() and pth.name not in ("manifest.json","manifest_readback.json"):
   rawb=pth.read_bytes(); outputs.append({"path":str(pth.resolve()),"sha256":hashlib.sha256(rawb).hexdigest().upper(),"LF_sha256":hashlib.sha256(rawb.replace(b"\r\n",b"\n")).hexdigest().upper(),"bytes":len(rawb)})
 evidence_files=[{"path":str(p.resolve()),"sha256":sha(p),"bytes":p.stat().st_size} for p in sorted(evidence.glob("*")) if p.is_file()]
 manifest={"scope":"Read-only original source identities, finite external static-audit outputs, and allowed repository delivery files; excludes private source copies, itself, and readback.","sources":inv,"external_evidence":evidence_files,"outputs":outputs}; write(out/"manifest.json",manifest)
 count=0
 for section in ("sources","external_evidence","outputs"):
  for item in manifest[section]: assert sha(item["path"])==item["sha256"],item["path"]; count+=1
 readback={"manifest_sha256":sha(out/"manifest.json"),"independent_files_verified":count,"all_matched":True,"test_receipt":receipt,"external_cell_ledger":{"path":str((evidence/"cell_level_ledger.csv").resolve()),"sha256":sha(evidence/"cell_level_ledger.csv"),"rows_including_header":sum(1 for _ in (evidence/"cell_level_ledger.csv").open(encoding="utf-8-sig"))},"zero_model_calls":summary["zero_model_call_ledger"]}; write(out/"manifest_readback.json",readback); print(json.dumps(readback,ensure_ascii=False))
if __name__=="__main__": main(*sys.argv[1:])
