"""Preflight, synthetic tests and single-process launch; no scientific imports."""
import base64, hashlib, json, os, re, subprocess, sys, time
from pathlib import Path
from evidence import decode_saved
from grid import expand_b, pin_details

REPO=Path(__file__).resolve().parents[3]; HERE=Path(__file__).resolve().parent
BASELINE=Path(r"D:\ProjectTemp\ch5-call725-rah-0p07-native-init-20260908-002")
RUNTIME=Path(r"D:\ProjectTemp\ch5-2018-observable-prefix-replay-20260908-001\source_runtime")
BASE=Path(r"D:\ProjectTemp\ch5-call725-rah-0p07-b-domain-expansion-20260909-001")
MANIFEST_SHA="F1C59EE5D937AABB8F5A3CE01A24456F53E9C90D26F710E3BE6F357C375CE459"
SOURCE_BLOBS={"validators/multi_province/mp4b_python_empirical.py":"b1710ae3c5d8d7baf96e85c932d777fa5f3b908c","validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py":"0033baee136c0328e80ffb8b794a88d4405c976c","validators/multi_province/mp4c_python_annual_production.py":"7473e04418744d745000afb21d84588273cc5bca","exports/matlab_faithful_two_asset_ha.py":"9e7dc9556a2b76811e78f89999abecc045886106"}
CONSUMED=("science/binding.json","science/binding.npz","science/native_initialization_return.json","science/native_initialization_return.npz","science/hjb_return_before_kfe.json","science/hjb_return_before_kfe.npz","science/kfe_return.json","science/kfe_return.npz","science/aggregate_return.json")
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()
def write(p,v):
    with Path(p).open("x",encoding="utf-8",newline="\n") as f: json.dump(v,f,ensure_ascii=False,allow_nan=False,indent=2); f.write("\n")
def git(*a): return subprocess.run(["git",*a],cwd=REPO,check=True,stdout=subprocess.PIPE).stdout.decode().strip()

def prepare():
    root=BASE; n=1
    while root.exists(): n+=1; root=BASE.with_name(BASE.name[:-3]+f"{n:03d}")
    root.mkdir(); assert sha(BASELINE/"manifest.json")==MANIFEST_SHA
    manifest=json.loads((BASELINE/"manifest.json").read_text(encoding="utf-8")); known={str(Path(x["path"]).resolve()).lower():x["sha256"] for s in ("inputs","captures","outputs") for x in manifest[s] if "sha256" in x}
    consumed=[]
    for rel in CONSUMED:
        p=(BASELINE/rel).resolve(); assert str(p).lower() in known and sha(p)==known[str(p).lower()], rel
        consumed.append({"path":str(p),"sha256":sha(p)})
    sources=[]
    for rel,blob in SOURCE_BLOBS.items():
        assert git("rev-parse",f"origin/main:{rel}")==blob
        p=RUNTIME/rel; expected=hashlib.sha256(subprocess.run(["git","cat-file","blob",blob],cwd=REPO,check=True,stdout=subprocess.PIPE).stdout).hexdigest().upper(); assert sha(p)==expected
        sources.append({"path":str(p),"blob":blob,"sha256":sha(p)})
    protected=Path(r"D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m"); assert sha(protected)=="049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE"
    binding=decode_saved(BASELINE/"science/binding.json"); old=binding["grid"]; new_b,db=expand_b(old["b"]); pin=pin_details(new_b,old["a"],old["z"])
    grid_binding={"passed":bool((new_b[:20]==old["b"]).all()),"old_b":old["b"].tolist(),"new_b":new_b.tolist(),"db":float(db),"db_hex":float(db).hex(),"endpoint":float(new_b[-1]),"endpoint_hex":float(new_b[-1]).hex(),"endpoint_minus_12":float(new_b[-1]-12.0),"a_exact":True,"z_exact":True,"switch_exact":True,"old_shape":[20,20,2],"new_shape":[39,20,2],"pin":pin,"economic_binding_sha256":sha(BASELINE/"science/binding.json")}
    assert grid_binding["passed"] and pin["k_zero_based"]==576
    write(root/"grid_binding.json",grid_binding); write(root/"preflight.json",{"passed":True,"live_main":git("rev-parse","origin/main"),"branch":git("branch","--show-current"),"baseline_manifest_sha256":MANIFEST_SHA,"consumed_baseline":consumed,"sources":sources,"protected_HJB_sha256":sha(protected),"scientific_entry":0,"limits":{"native_initialization":1,"labor_root":1560,"brentq":1560,"HJB":1,"HJB_direct_solve":100,"KFE":1,"KFE_direct_solve":1,"aggregate":1,"seconds":900}}); print(root)

def tests(root):
    command=[sys.executable,"-B",str(REPO/"tests/test_mp4c_call725_b_domain_expansion.py")]; env=dict(os.environ); env["PYTHONIOENCODING"]="utf-8"; result=subprocess.run(command,cwd=REPO,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT); raw=result.stdout; text=raw.decode("utf-8").replace("\r\n","\n"); number=len(list(root.glob("tests_*.raw.json")))+1; stem=root/f"tests_{number:02d}"
    write(stem.with_suffix(".raw.json"),{"command":command,"returncode":result.returncode,"sha256":hashlib.sha256(raw).hexdigest().upper(),"base64":base64.b64encode(raw).decode()}); stem.with_suffix(".txt").write_text(text,encoding="utf-8",newline="\n"); m=re.search(r"Ran (\d+) tests",text); receipt={"passed":result.returncode==0 and "\nOK\n" in text,"ran":int(m.group(1)) if m else None,"individual_ok":len(re.findall(r" \.\.\. ok$",text,re.M)),"lf_sha256":sha(stem.with_suffix(".txt"))}; write(stem.with_suffix(".receipt.json"),receipt); print(text); print(receipt)
    if not receipt["passed"] or receipt["ran"]!=receipt["individual_ok"]: raise SystemExit(1)

def launch(root):
    assert json.loads((root/"preflight.json").read_text())["scientific_entry"]==0; assert json.loads(sorted(root.glob("tests_*.receipt.json"))[-1].read_text())["passed"]; write(root/"launch_marker.json",{"epoch":time.time(),"scientific_restart_authority":False})
    env=dict(os.environ); env.update({x:"1" for x in ("OMP_NUM_THREADS","MKL_NUM_THREADS","OPENBLAS_NUM_THREADS","NUMEXPR_NUM_THREADS")}); env.update(PYTHONIOENCODING="utf-8",PYTHONDONTWRITEBYTECODE="1",CH5_EXP_RUNTIME=str(RUNTIME),CH5_EXP_BASELINE=str(BASELINE)); command=[sys.executable,"-B",str(HERE/"run.py"),str(root)]
    with (root/"stdout.txt").open("xb") as out,(root/"stderr.txt").open("xb") as err:
        p=subprocess.Popen(command,cwd=REPO,env=env,stdout=out,stderr=err); write(root/"launch_receipt.json",{"pid":p.pid,"command":command,"cwd":str(REPO),"start_epoch":time.time(),"observer_sources":{x.name:sha(x) for x in HERE.glob("*.py")}})
        timeout=False
        try: code=p.wait(timeout=900)
        except subprocess.TimeoutExpired: timeout=True; p.kill(); code=p.wait()
    write(root/"process_receipt.json",{"returncode":code,"external_timeout":timeout,"terminal_saved":(root/"science/terminal.json").exists(),"end_epoch":time.time(),"scientific_restart":False}); print(root/"process_receipt.json")
if __name__=="__main__":
    if sys.argv[1]=="prepare": prepare()
    elif sys.argv[1]=="tests": tests(Path(sys.argv[2]))
    elif sys.argv[1]=="launch": launch(Path(sys.argv[2]))
