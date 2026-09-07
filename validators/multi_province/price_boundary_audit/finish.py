"""Complete saved evidence tables, execute synthetic tests and seal a finite manifest."""
import base64
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from audit import REPO, table, write
from core import spell


def read(path):return json.loads(Path(path).read_text(encoding='utf-8'))
def rows(path):return list(csv.DictReader(Path(path).open(encoding='utf-8')))
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()


def tables(root):
    panel=rows(root/'failed_path_prices.csv');annual=rows(root/'annual_prices.csv');decomp=rows(root/'price_decomposition.csv')
    coverage=rows(root/'province_coverage_and_spells.csv')
    common=[];spells=[];stepcounts=[]
    for c in coverage:
        i=int(c['index_0']);p=[r for r in panel if int(r['index_0'])==i]
        found=next((r for r in p if int(r['step'])==24),None)
        common.append({'index_0':i,'index_1':i+1,'province':c['province'],'outer_iteration':24,
            'status':'CAPTURED_OLD_STATE' if found else 'NOT_CAPTURED_BEFORE_EXCEPTION',
            **{k:found[k] if found else None for k in ('rah','w','Yt','Lt','Kt','Zt','GovInv','lagged_ra_identified')},
            'ra0':None,'ra':None,'wt0':None,'wjt':None})
        for phase in ('initialization','household_entry_old_state'):
            for f in ('ra','wjt','rah'):
                for side in ('lower','upper'):
                    observed=[(int(r['step']),r.get(f+'_exact_'+side)=='True') for r in p
                              if r['phase']==phase and r.get(f+'_finite')=='True']
                    spells.append({'index_0':i,'province':c['province'],'phase':phase,'field':f,'side':side,
                                   'constraint':'DESCRIPTIVE_FIRM_RANGE_ONLY' if f=='rah' else 'FIRM_NATIVE',**spell(observed)})
    for step in range(1,25):
        p=[r for r in panel if int(r['step'])==step]
        stepcounts.append({'entry_step':step,'observed':len(p),'phase':p[0]['phase'],
            'rah_exact_upper':sum(r['rah_exact_upper']=='True' for r in p),
            'rah_exact_lower':sum(r['rah_exact_lower']=='True' for r in p),
            'rah_below_firm_reference':sum(r['rah_strict_below']=='True' for r in p),
            'rah_above_0p07':sum(r['rah_above_owner_recollection_0p07']=='True' for r in p),
            'ra_native_postfirm_observed':0,'wjt_native_postfirm_observed':0})
    table(root/'call725_common_old_state_31.csv',common);table(root/'contact_spells.csv',spells)
    table(root/'path_step_counts.csv',stepcounts)
    aggregate=[]
    for reg in ('OWNER_A','RUNTIME_CACHE'):
        for c in coverage:
            a=[r for r in annual if r['regime']==reg and r['name']==c['province']]
            aggregate.append({'regime':reg,'province':c['province'],'observed_years':len(a),
                **{f:sum(r[f]=='True' for r in a) for f in ('ra_exact_upper','ra_exact_lower','wjt_exact_upper','wjt_exact_lower','ra0_strict_above','ra0_strict_below','wt0_strict_above','wt0_strict_below')},
                'wage_upper_years':' '.join(r['year'] for r in a if r['wjt_exact_upper']=='True'),
                'wage_lower_years':' '.join(r['year'] for r in a if r['wjt_exact_lower']=='True')})
    table(root/'annual_province_coverage.csv',aggregate)
    summary=read(root/'summary.json')
    summary['rah_transmission_observed_comparisons']=sum(bool(r['rah_transmission_pass']) for r in panel)
    summary['annual_boundary_totals']={reg:{f:sum(r[f]=='True' for r in annual if r['regime']==reg)
        for f in ('ra_exact_upper','ra_exact_lower','wjt_exact_upper','wjt_exact_lower','ra0_strict_above','ra0_strict_below','wt0_strict_above','wt0_strict_below','rah_above_owner_recollection_0p07')}
        for reg in ('OWNER_A','RUNTIME_CACHE')}
    summary['observed_action_counts']={str(k):v for k,v in Counter((r['gate'],r['captured_action_class']) for r in decomp).items()}
    summary['turn23_gate_inference']='ENABLED_INFERRED_FROM_CAPTURED_1P1_UPDATES; national max and deciding province unavailable'
    summary['raw_path_price_status']='NOT_RECONSTRUCTABLE_WITH_CAPTURED_FIELDS; missing current household Lt and carried rk'
    summary['anhui_turn23_GovInv_increase']=next(r for r in decomp if r['step']=='23' and r['index_0']=='11')
    write(root/'summary.json',summary)
    old=Path(r'D:\ProjectTemp\ch5-province-price-boundary-audit-20260908-001')
    write(root/'excluded_attempt.json',{'path':str(old),'summary_sha256':sha(old/'summary.json'),
        'status':'INVALID_PATH_RAW_PRICE_RECONSTRUCTION_NOT_USED',
        'reason':'used old firm Lt as firm Lt_prev; actual one_turn uses current household Lt, which was not saved. 191 downstream portfolio mismatches exposed the omitted operand. No unsupported raw path prices are retained as findings.',
        'scope':'postprocessing engineering attempt; zero model calls; external root preserved'})


def tests(root):
    cmd=[sys.executable,'-B',str(REPO/'tests/test_mp4c_price_boundary_audit.py')]
    run=subprocess.run(cmd,cwd=REPO,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    raw=run.stdout;text=raw.decode('utf-8').replace('\r\n','\n')
    attempt=len(list(root.glob('test_*.raw.json')))+1;prefix=root/f'test_{attempt:02d}'
    write(prefix.with_suffix('.raw.json'),{'command':cmd,'returncode':run.returncode,'base64':base64.b64encode(raw).decode(),'sha256':hashlib.sha256(raw).hexdigest().upper()})
    prefix.with_suffix('.txt').write_text(text,encoding='utf-8',newline='\n')
    count=re.search(r'Ran (\d+) tests',text)
    receipt={'returncode':run.returncode,'ran':int(count.group(1)) if count else None,
        'individual_ok':len(re.findall(r' \.\.\. ok$',text,re.M)),'passed':run.returncode==0 and '\nOK\n' in text,
        'lf_log_sha256':sha(prefix.with_suffix('.txt'))}
    write(prefix.with_suffix('.receipt.json'),receipt);print(text);print(receipt)
    assert receipt['passed'] and receipt['ran']==receipt['individual_ok']


def package(root):
    out=REPO/'reports/province_price_boundary_audit_20260908';out.mkdir(exist_ok=True)
    write(root/'ledger.json',{'new_scientific_calls':{k:0 for k in ('HJB','household','KFE','linear_solve','root_solve','one_turn','GE','annual','R_PLM','shock','IRF','Results','MATLAB_process','scientific_retry')},
        'saved_scalar_reads':'725 failed-path entries and 868 separate terminal province-years',
        'postprocessing_attempts':2,'invalid_first_attempt_preserved':True,'model_algorithm_parameters_changed':False})
    for p in root.iterdir():
        if p.is_file() and p.suffix in ('.csv','.json','.txt') and p.name not in ('manifest.json','manifest_readback.json','publication_receipt.json'):
            (out/p.name).write_text(p.read_text(encoding='utf-8'),encoding='utf-8',newline='\n')
    files=list(root.iterdir())+list(out.iterdir())+list(Path(__file__).parent.glob('*.py'))+[
        REPO/'tests/test_mp4c_price_boundary_audit.py',REPO/'docs/CH5_MP4C_PROVINCE_PRICE_BOUNDARY_AND_ADAPTATION_AUDIT_REPORT.md']
    entries=[]
    for p in sorted(files):
        if not p.is_file() or p.name in ('manifest.json','manifest_readback.json','publication_receipt.json'):continue
        repo=p.is_relative_to(REPO);raw=p.read_text(encoding='utf-8').replace('\r\n','\n').encode() if repo else p.read_bytes()
        entries.append({'path':str(p),'repository_path':p.relative_to(REPO).as_posix() if repo else None,
            'mode':'utf8_LF' if repo else 'raw_bytes','bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest().upper()})
    write(root/'manifest.json',{'base_main':'c90bb26fb17f03dd9f45cea668d9e65a9ea22f43','evidence_root':str(root),'entries':entries,
        'excludes':['manifest.json','manifest_readback.json','publication_receipt.json']})
    for item in entries:
        p=Path(item['path']);raw=p.read_bytes() if item['mode']=='raw_bytes' else p.read_text(encoding='utf-8').replace('\r\n','\n').encode()
        assert hashlib.sha256(raw).hexdigest().upper()==item['sha256']
    write(root/'manifest_readback.json',{'passed':True,'entries':len(entries),'manifest_sha256':sha(root/'manifest.json')})
    for name in ('manifest.json','manifest_readback.json'):(out/name).write_bytes((root/name).read_bytes())
    print(read(root/'manifest_readback.json'))


if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8');root=Path(sys.argv[2])
    {'tables':tables,'tests':tests,'package':package}[sys.argv[1]](root)
