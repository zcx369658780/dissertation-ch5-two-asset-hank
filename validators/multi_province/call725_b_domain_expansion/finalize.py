import hashlib,json,shutil,sys
from pathlib import Path
from evidence import sha256
REPO=Path(__file__).resolve().parents[3]
def write(p,v): Path(p).write_text(json.dumps(v,ensure_ascii=False,allow_nan=False,indent=2)+"\n",encoding="utf-8",newline="\n")
def main(root,out):
 root=Path(root).resolve(); out=Path(out).resolve(); term=json.loads((root/"science/terminal.json").read_text()); proc=json.loads((root/"process_receipt.json").read_text()); summary=json.loads((out/"summary.json").read_text())
 assert term["terminal"]=="NORMAL_RETURN" and proc["returncode"]==0 and not proc["external_timeout"]
 expected={"native_initialization":1,"labor_root":1560,"brentq":1560,"adapter":1,"HJB":1,"HJB_return":1,"HJB_direct_solve":17,"KFE":1,"KFE_direct_solve":1,"KFE_return":1,"aggregate":1,"aggregate_return":1}; assert all(term["counts"][k]==v for k,v in expected.items())
 phases=[json.loads(x)["phase"] for x in (root/"science/index.jsonl").read_text(encoding="utf-8").splitlines()]; assert phases.index("hjb_return_before_kfe")<phases.index("kfe_entry"); assert summary["Results_eligible"] is False
 shutil.copyfile(root/"grid_binding.json",out/"grid_binding.json"); receipts=out/"receipts"; receipts.mkdir(exist_ok=True)
 for pat in ("preflight.json","grid_binding.json","launch_marker.json","launch_receipt.json","process_receipt.json","stdout.txt","stderr.txt","tests_*.json","tests_*.txt"):
  for p in root.glob(pat): shutil.copyfile(p,receipts/p.name)
 for n in ("environment.json","binding.json","terminal.json"): shutil.copyfile(root/"science"/n,receipts/n)
 shutil.copyfile(root/"science/index.jsonl",out/"science_capture_index.jsonl")
 pre=json.loads((root/"preflight.json").read_text()); captures=[]
 for line in (root/"science/index.jsonl").read_text(encoding="utf-8").splitlines():
  row=json.loads(line)
  for key in ("json","npz"):
   if key in row: captures.append({"path":row[key],"sha256":row[key+"_sha256"],"bytes":Path(row[key]).stat().st_size})
 paths=[REPO/"docs/CH5_MP4C_CALL725_RAH_0P07_B_DOMAIN_EXPANSION_REPORT.md",REPO/"tests/test_mp4c_call725_b_domain_expansion.py",*sorted((REPO/"validators/multi_province/call725_b_domain_expansion").glob("*.py")),*sorted(out.rglob("*"))]; outputs=[]
 for p in paths:
  if p.is_file() and p.name not in ("manifest.json","manifest_readback.json"):
   raw=p.read_bytes(); outputs.append({"path":str(p),"sha256":hashlib.sha256(raw).hexdigest().upper(),"LF_sha256":hashlib.sha256(raw.replace(b"\r\n",b"\n")).hexdigest().upper(),"bytes":len(raw)})
 manifest={"scope":"Consumed accepted .07 objects, frozen sources, new single-process captures, and exact allowed delivery paths; excludes itself/readback.","inputs":pre["consumed_baseline"]+pre["sources"],"captures":captures,"outputs":outputs}; write(root/"manifest.json",manifest); shutil.copyfile(root/"manifest.json",out/"manifest.json")
 count=0
 for sec in manifest.values():
  if not isinstance(sec,list): continue
  for x in sec: assert sha256(x["path"])==x["sha256"]; count+=1
 tests=json.loads(sorted(root.glob("tests_*.receipt.json"))[-1].read_text()); receipt={"manifest_sha256":sha256(root/"manifest.json"),"independent_files_verified":count,"all_matched":True,"science_capture_files":len(captures),"science_capture_index_entries":len(phases),"actual_test_receipt":tests,"science_phase_order":phases,"hjb_saved_before_kfe":True}; write(root/"manifest_readback.json",receipt); shutil.copyfile(root/"manifest_readback.json",out/"manifest_readback.json"); print(json.dumps(receipt))
if __name__=="__main__": main(*sys.argv[1:])
