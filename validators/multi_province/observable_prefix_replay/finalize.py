"""Finalize immutable evidence manifest after the single science process ends."""
import csv
import hashlib
import json
from pathlib import Path
import shutil
import sys
from analyze import read,save,table,OLD,REPO

def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return h.hexdigest().upper()

def main(root):
    number=1
    while (root/('manifest.json' if number==1 else f'manifest_{number:02d}.json')).exists():number+=1
    manifest_path=root/('manifest.json' if number==1 else f'manifest_{number:02d}.json')
    readback_path=root/('manifest_readback.json' if number==1 else f'manifest_readback_{number:02d}.json')
    out=REPO/'reports/2018_observable_prefix_replay_20260908'
    terminal=read(root/'capture/terminal.json');process=read(root/'process_retry1_receipt.json')
    assert process['terminal_saved'] and not process['external_timeout']
    counts=terminal['counts'];limits={'native_initialization':725,'household':725,'labor_root':580000,'brentq':580000,'HJB':725,'HJB_direct_solve':72500,'KFE':725,'KFE_direct_solve':725,'one_turn':23,'firm':713,'controller_decision':23,'outer_entry':24}
    assert all(counts[k]<=v for k,v in limits.items())
    for row in terminal['per_call'].values():assert row['labor_root']<=800 and row['HJB_direct_solve']<=100 and row['KFE_direct_solve']<=1
    assert counts['root_residual']==counts['root_bracketing_residual']+counts['root_brentq_residual']
    assert not (root/'capture/call_0726').exists()
    ledger={'launch_attempts':2,'zero_entry_failed_launches':1,'external_retry_consumed':1,'scientific_processes':1,'original_2018_annual_worker_prefix_invocations':1,'full_annual_completion':0,'workers':1,'scientific_restarts':0,'attempts_and_returns':counts,'per_call':terminal['per_call'],'ceilings':limits,'MATLAB':0,'independent_diagnostic_solves':0,'condition_estimation':0,'other_years':0,'R_PLM':0,'shock_dynamic_IRF':0,'Results':0,'scientific_seconds':terminal['scientific_seconds'],'counts_include_failed_attempts':True}
    save(out/'call_ledger.json',ledger)
    receipts=out/'receipts';receipts.mkdir(exist_ok=True)
    for pattern in ('preflight.json','*receipt.json','launch*marker.json','tests_*.json','tests_*.txt','stdout*.txt','stderr*.txt'):
        for p in root.glob(pattern):shutil.copyfile(p,receipts/p.name)
    shutil.copyfile(root/'capture/environment.json',receipts/'environment.json')
    shutil.copyfile(root/'capture/terminal.json',receipts/'terminal.json')
    shutil.copyfile(root/'capture/index.jsonl',out/'capture_index.jsonl')
    index=[json.loads(s) for s in (root/'capture/index.jsonl').read_text(encoding='utf-8').splitlines()]
    captures=[]
    for entry in index:
        for key in ('json','npz'):
            if key in entry:
                p=Path(entry[key]);h=sha(p);assert h==entry[key+'_sha256'],p
                captures.append({'path':str(p),'bytes':p.stat().st_size,'sha256':h,'role':'immutable_scientific_capture'})
    pre=read(root/'preflight.json');inputs=[]
    for src in pre['sources']:
        p=root/'source_runtime'/src['path'];assert sha(p)==src['LF_sha256'];inputs.append({'path':str(p),'sha256':sha(p),'blob':src['blob'],'raw_equals_LF':True})
    for name in ('household_call_ledger.csv','hjb_return_ledger.csv','first_singularity_localization.json','diagnostic_child_launch_receipt.json','scientific_code_identity_manifest.json'):
        p=OLD/name;inputs.append({'path':str(p),'sha256':sha(p),'role':'historical_readonly'})
    p=Path(pre['input']['path']);assert sha(p)==pre['input']['sha256'];inputs.append({'path':str(p),'sha256':sha(p),'role':'original_scientific_input'})
    protected=Path('D:/MatlabProgram/2023年12月2日 多省份神经网络HANK/HANK_2ASSETS_HJB.m');assert sha(protected)==pre['protected_HJB_sha256'];inputs.append({'path':str(protected),'sha256':sha(protected),'role':'protected_readonly'})
    files=[]
    for p in sorted(root.glob('*')):
        if p.is_file() and not p.name.startswith('manifest'):files.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
    for p in sorted((root/'worker_outputs').rglob('*')):
        if p.is_file():files.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
    report=REPO/'docs/CH5_MP4C_2018_ORIGINAL_PARAMETER_OBSERVABLE_PREFIX_REPLAY_REPORT.md'
    repo_files=[report,REPO/'tests/test_mp4c_observable_prefix_replay.py',*sorted((REPO/'validators/multi_province/observable_prefix_replay').glob('*')),*sorted(out.rglob('*'))]
    for p in repo_files:
        if p.is_file() and not p.name.startswith('manifest'):
            b=p.read_bytes();files.append({'path':str(p),'sha256':sha(p),'LF_sha256':hashlib.sha256(b.replace(b'\r\n',b'\n')).hexdigest().upper(),'bytes':len(b)})
    inputs=list({x['path']:x for x in inputs}.values())
    manifest={'scope':'finite inputs + indexed captures + explicit runtime/allowed deliverables; excludes itself and readback to avoid cycles','inputs':inputs,'captures':captures,'outputs':files}
    manifest['revision']=number;manifest['note']='Prior external manifests retained; current draft paths may change during delivery hygiene fixes. Scientific captures remain immutable.'
    save(manifest_path,manifest);shutil.copyfile(manifest_path,out/'manifest.json')
    # Independent readback reopens every listed file after manifest serialization.
    reread=read(manifest_path);checked=0
    for section in ('inputs','captures','outputs'):
        for f in reread[section]:assert sha(f['path'])==f['sha256'],f['path'];checked+=1
    receipt={'manifest_path':str(manifest_path),'manifest_revision':number,'manifest_sha256':sha(manifest_path),'independent_files_verified':checked,'all_matched':True,'capture_files':len(captures),'capture_index_entries':len(index),'actual_test_receipt':read(sorted(root.glob('tests_*.receipt.json'))[-1])}
    save(readback_path,receipt);save(out/'manifest_readback.json',receipt);print(json.dumps(receipt))

if __name__=='__main__':main(Path(sys.argv[1]))
