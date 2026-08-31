"""One-shot standalone Beijing household runner and frozen comparator."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, sys
from pathlib import Path
import numpy as np

REPO=Path(__file__).resolve().parents[2]
STANDALONE=REPO/'exports'/'matlab_faithful_two_asset_ha.py'
EXPECTED_STANDALONE='B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3'
EXPECTED_CONTRACT='FE833FAEB48521CD0C7594627AF6FB5012F9497A455E9B2C5E7490E0C40E6F22'

def sha(path: Path)->str: return hashlib.sha256(path.read_bytes()).hexdigest().upper()
def write_new(path:Path,payload)->None:
    encoded=json.dumps(payload,ensure_ascii=False,allow_nan=False,indent=2)+'\n'
    with path.open('x',encoding='utf-8') as handle: handle.write(encoded)
def load_standalone():
    if sha(STANDALONE)!=EXPECTED_STANDALONE: raise RuntimeError('standalone candidate SHA mismatch')
    spec=importlib.util.spec_from_file_location('mp4b_beijing_standalone_candidate',STANDALONE)
    if spec is None or spec.loader is None: raise RuntimeError('standalone import spec unavailable')
    module=importlib.util.module_from_spec(spec); sys.modules[spec.name]=module; spec.loader.exec_module(module)
    if Path(module.__file__).resolve()!=STANDALONE.resolve(): raise RuntimeError('standalone origin mismatch')
    forbidden=[name for name in sys.modules if name.startswith('ch5_two_asset_hank') or name.startswith('chapter5_model')]
    if forbidden: raise RuntimeError(f'forbidden runtime imports: {forbidden}')
    return module
def run_python(contract_path:Path,run_root:Path)->None:
    if sha(contract_path)!=EXPECTED_CONTRACT: raise RuntimeError('contract SHA mismatch')
    output=run_root/'python_household_summary.json'; full=run_root/'python_household_full.npz'
    if output.exists() or full.exists(): raise FileExistsError('Python output already exists')
    q=json.loads(contract_path.read_text(encoding='utf-8')); x=q['python_mapping']; m=load_standalone(); g=x['MatlabFaithfulHJBGrid']
    grid=m.MatlabFaithfulHJBGrid(np.array(g['b']),np.array(g['a']),np.array(g['z']),np.array(g['switch_matrix']))
    params=m.EconomicParams(*x['EconomicParams']); h=x['HouseholdInputs']
    inputs=m.HouseholdInputs(h[0],h[1],h[2],np.array(h[3]),np.array(h[4]),np.array(h[5]))
    numerics=m.MatlabFaithfulHJBNumerics(*x['MatlabFaithfulHJBNumerics'])
    result=m.solve_household_steady_state(grid,params,inputs,np.array(x['initial_value']),np.array(x['baseline_labor']),x['transfer_income'],x['borrowing_rate_gap'],numerics)
    with full.open('xb') as handle:
        np.savez(handle,value=result.hjb.value,consumption=result.hjb.consumption,labor=result.hjb.labor,
                 density=result.kfe.density,transfer=result.hjb.transfer)
    a=result.aggregates
    payload={'schema':'MP4B_BEIJING_STANDALONE_HOUSEHOLD_RESULT_V1','standalone_path':str(STANDALONE.resolve()),
      'standalone_sha256':sha(STANDALONE),'solve_household_steady_state_calls':1,'converged':bool(result.hjb.converged),
      'hjb':{'iterations':result.hjb.iterations,'convergence_statistic':result.hjb.convergence_statistic},
      'kfe':{'contaminated_row_index':result.kfe.contaminated_row_index,'raw_residual_inf':result.kfe.raw_residual_inf,
             'density_normalization':a.density_normalization},
      'aggregates':{'Ct':a.c_ss,'Lt':a.l_ss,'At':a.a_ss,'Bt':a.b_ss,'At_plus_Bt':a.a_ss+a.b_ss},
      'AtTax':'EXCLUDED_NOT_UNIQUELY_SOURCE_BACKED','full_result_path':str(full)}
    write_new(output,payload)
def compare(matlab_path:Path,python_path:Path,contract_path:Path,output:Path)->int:
    contract=json.loads(contract_path.read_text(encoding='utf-8')); tol=float(contract['scaled_tolerance']); n=int(contract['term_count'])
    matlab=json.loads(matlab_path.read_text(encoding='utf-8')); python=json.loads(python_path.read_text(encoding='utf-8'))
    rows=[]; failures=[]
    for name in contract['mandatory_continuous']:
        x=float(matlab['aggregates'][name]); y=float(python['aggregates'][name]); diff=abs(x-y); bound=tol*max(1.,abs(x),abs(y))
        rel=diff/max(abs(x),abs(y)) if max(abs(x),abs(y)) else 0.; passed=math.isfinite(x) and math.isfinite(y) and diff<=bound
        rows.append({'field':name,'matlab':x,'python':y,'absolute_difference':diff,'relative_difference':rel,'bound':bound,'pass':passed})
        if not passed: failures.append(name)
    closures={'matlab':abs(matlab['aggregates']['At_plus_Bt']-(matlab['aggregates']['At']+matlab['aggregates']['Bt'])),
              'python':abs(python['aggregates']['At_plus_Bt']-(python['aggregates']['At']+python['aggregates']['Bt']))}
    categorical=bool(matlab['converged']) and bool(python['converged']) and closures=={'matlab':0.0,'python':0.0}
    if not categorical: failures.append('categorical_or_identity')
    eps=sys.float_info.epsilon; gamma_n=n*eps/(1-n*eps)
    payload={'schema':'MP4B_BEIJING_FIRST_TURN_QUALIFIED_COMPARISON_V1','comparator_calls':1,
      'contract_sha256':sha(contract_path),'scaled_gate':contract['scaled_gate'],'gamma_n':gamma_n,
      'categorical_pass':categorical,'identity_closures':closures,'tax_disposition':contract['optional_tax_disposition'],
      'rows':rows,'failures':failures,'result':'PASS' if not failures else 'MATERIAL_MISMATCH'}
    write_new(output,payload); return 0 if not failures else 2
def finalize(run_root:Path,source_map:Path,comparator_contract:Path)->None:
    ledger={'MATLAB_HANK_2ASSETS_HJB_top_level':1,'standalone_solve_household_steady_state_top_level':1,
      'qualified_comparator':1,'MATLAB_household_reruns':0,'standalone_household_reruns':0,'comparator_reruns':0,
      'modular_Python_household':0,'separate_modular_HJB_KFE':0,'MATLAB_HANK3_FOC_rerun':0,
      'MATLAB_local_policy_rerun':0,'accepted_50_state_HJB_rerun':0,'accepted_wrapper_smoke_rerun':0,
      'exact_junction_smoke_rerun':0,'HANK_mp_1turn':0,'HANK_mp_1eq':0,'second_province_household':0,
      'MATLAB_calendar_2009_stationary_rerun':0,'Python_multi_province_stationary':0,'MP2_MP3':0,
      'annual_batch':0,'shocks':0,'transition':0,'dynamics':0,'IRF':0,'historical_R5':0,'Results':0}
    write_new(run_root/'call_ledger.json',ledger)
    names=('matlab_household_full.mat','matlab_household_summary.json','python_household_full.npz',
           'python_household_summary.json','qualified_comparison.json','call_ledger.json')
    artifacts=[{'name':name,'path':str((run_root/name).resolve()),'sha256':sha(run_root/name),'size':(run_root/name).stat().st_size} for name in names]
    payload={'schema':'MP4B_BEIJING_FIRST_TURN_HOUSEHOLD_PARITY_OUTPUT_MANIFEST_V1','run_root':str(run_root.resolve()),
      'source_map':{'path':str(source_map.resolve()),'sha256':sha(source_map)},
      'comparator_contract':{'path':str(comparator_contract.resolve()),'sha256':sha(comparator_contract)},
      'artifacts':artifacts,'production_export_candidate_hashes':{
        'economics.py':sha(REPO/'src/ch5_two_asset_hank/economics.py'),
        'matlab_faithful_policy.py':sha(REPO/'src/ch5_two_asset_hank/matlab_faithful_policy.py'),
        'standalone':sha(STANDALONE)}}
    write_new(run_root/'output_manifest.json',payload)
def main()->int:
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='mode',required=True)
    r=sub.add_parser('run-python'); r.add_argument('contract',type=Path); r.add_argument('run_root',type=Path)
    c=sub.add_parser('compare'); c.add_argument('matlab',type=Path); c.add_argument('python',type=Path); c.add_argument('contract',type=Path); c.add_argument('output',type=Path)
    f=sub.add_parser('finalize'); f.add_argument('run_root',type=Path); f.add_argument('source_map',type=Path); f.add_argument('comparator_contract',type=Path)
    a=p.parse_args();
    if a.mode=='run-python': run_python(a.contract,a.run_root); return 0
    if a.mode=='finalize': finalize(a.run_root,a.source_map,a.comparator_contract); return 0
    return compare(a.matlab,a.python,a.contract,a.output)
if __name__=='__main__': raise SystemExit(main())
