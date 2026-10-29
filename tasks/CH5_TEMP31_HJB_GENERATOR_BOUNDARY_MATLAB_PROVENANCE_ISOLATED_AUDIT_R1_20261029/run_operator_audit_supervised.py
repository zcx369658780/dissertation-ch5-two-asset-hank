"""Exactly two pure-operator commands, one memory-limited child per command."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,os
from pathlib import Path
import subprocess,sys,time
from datetime import datetime,timezone
REPORT=Path(__file__).resolve().parent;WORK=REPORT.parents[1];EV=REPORT/'evidence'
ENTRY='validators/multi_province/temp31_generator_boundary_source_audit_isolated.py'
THREAD_KEYS=('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS','BLIS_NUM_THREADS')
def read(path):return json.loads(path.read_text(encoding='utf-8'))
def write(path,data):
    with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(data,f,indent=2);f.write('\n')
def sha(raw):return hashlib.sha256(raw).hexdigest()
def helper(identity):
    row=identity['authenticated_supervisor_helper'];path=WORK/row['path'];raw=path.read_bytes()
    assert sha(raw)==row['sha256'] and len(raw)==row['bytes'] and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==row['git_blob']
    spec=importlib.util.spec_from_file_location('temp31_operator_audit_authentic_supervisor',path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
    return module
def main(group):
    number=1 if group=='conservation' else 2;budget_path=REPORT/'test_command_budget.json';budget=read(budget_path)
    assert budget['commands_started']==number-1 and budget['fixtures_executed']==2*(number-1),'STOP_REPEAT_OR_BUDGET'
    if number==2:
        prior=read(EV/'command_1_receipt.json');assert prior['passed'] and prior['exit_code']==0 and not prior['timed_out']
    identity=read(REPORT/'source_identity.json');old=helper(identity);frozen=read(REPORT/'synthetic_fixture_contract.json')
    command=[sys.executable,'-B',ENTRY,'--group',group]
    write(EV/f'command_{number}_claim.json',{'command_number':number,'group':group,'command':['python','-B',*command[2:]],
        'working_directory':'<ISOLATED_CANDIDATE_ROOT>','declared_at_utc':datetime.now(timezone.utc).isoformat(),
        'source_commit':identity['source']['commit'],'fixture_ids':frozen['fixture_groups'][group],
        'entry_sha256':sha((WORK/ENTRY).read_bytes()),'supervisor_sha256':sha(Path(__file__).read_bytes()),
        'fixture_contract_sha256':sha((REPORT/'synthetic_fixture_contract.json').read_bytes()),
        'hard_timeout_seconds':30,'max_fixture_assemblies':2,'real_HA_HJB_policy_initializer_root_KFE_GE_IRF_firm_calls':0,'retry_allowed':False})
    budget['commands_started']=number
    budget_path.write_text(json.dumps(budget,indent=2)+'\n',encoding='utf-8',newline='\n')
    env=dict(os.environ,**{k:'1' for k in THREAD_KEYS},PYTHONDONTWRITEBYTECODE='1',PYTHONNOUSERSITE='1');env.pop('PYTHONPATH',None)
    start=time.monotonic();p=subprocess.Popen(command,cwd=WORK,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env)
    close_job=None;timed_out=False;memory={'status':'MEMORY_HARD_LIMIT_UNAVAILABLE'};pre_import_block=False
    try:
        _,memory,close_job=old.restrict_memory(p)
        if memory['status']!='PROCESS_MEMORY_HARD_LIMIT_ENFORCED':pre_import_block=True;p.kill();out,err=p.communicate()
        else:out,err=p.communicate(input=b'GO\n',timeout=max(.001,30-(time.monotonic()-start)))
    except subprocess.TimeoutExpired:
        timed_out=True;p.kill();out,err=p.communicate()
    except BaseException:
        p.kill();p.communicate();raise
    finally:
        if close_job is not None:memory['observed_peak_process_committed_bytes']=close_job()
    elapsed=time.monotonic()-start
    (EV/f'LOCAL_ONLY_command_{number}_stdout_raw.txt').write_bytes(out);(EV/f'LOCAL_ONLY_command_{number}_stderr_raw.txt').write_bytes(err)
    public_out,changes_out=old.redact(out);public_err,changes_err=old.redact(err)
    (EV/f'command_{number}_stdout_public.txt').write_bytes(public_out);(EV/f'command_{number}_stderr_public.txt').write_bytes(public_err)
    events=[json.loads(line) for line in public_out.decode('utf-8','replace').splitlines() if line.startswith('{"event":')]
    final=next((e for e in reversed(events) if e['event']=='test_result'),None)
    fixtures=[e for e in events if e['event']=='fixture']
    passed=p.returncode==0 and not timed_out and not pre_import_block and final is not None and final['status']=='PASS_PURE_SYNTHETIC_OPERATOR_MECHANISM_CHECKS'
    if final:
        budget['fixtures_executed']+=final['actual_counts']['fixtures']
        budget['actual_operator_assemblies']+=final['actual_counts']['assemble_source_operator']
        budget['actual_axis_assemblies']+=final['actual_counts']['assemble_source_axis']
        budget['HA_HJB_policy_initializer_root_KFE_GE_IRF_firm_calls']+=final['actual_counts']['forbidden_model_calls']
    budget['command_'+str(number)]='PASS_PURE_MATH' if passed else 'FAILED_STOP_NO_RETRY'
    budget['remaining_commands']=2-number
    if not passed:budget['closed_after_failure']=True
    assert budget['fixtures_executed']<=4 and budget['actual_operator_assemblies']<=4
    budget_path.write_text(json.dumps(budget,indent=2)+'\n',encoding='utf-8',newline='\n')
    redaction={'transformation':'exact workspace/runtime prefix replacements only; original raw logs retained LOCAL_ONLY',
        'stdout':{'raw_bytes':len(out),'raw_sha256':sha(out),'public_bytes':len(public_out),'public_sha256':sha(public_out),'changes':changes_out},
        'stderr':{'raw_bytes':len(err),'raw_sha256':sha(err),'public_bytes':len(public_err),'public_sha256':sha(public_err),'changes':changes_err}}
    write(EV/f'command_{number}_redaction_record.json',redaction)
    write(EV/f'command_{number}_fixture_results.json',{'group':group,'fixtures':fixtures,'real_historical_matrices':False})
    receipt={'command_number':number,'group':group,'exit_code':p.returncode,'passed':passed,'timed_out':timed_out,'hard_timeout_seconds':30,
        'elapsed_seconds':elapsed,'memory_limit':memory,'science_child_processes':1,'final_event':final,'fixture_ids':[e['fixture_id'] for e in fixtures],
        'raw_public_identity':redaction,'retries':0,'pre_import_memory_block':pre_import_block}
    write(EV/f'command_{number}_receipt.json',receipt)
    print(json.dumps({'group':group,'exit_code':p.returncode,'passed':passed,'elapsed_seconds':elapsed,'timed_out':timed_out,'memory_limit':memory,
      'final_event':final,'fixture_metrics':[{k:e[k] for k in ['fixture_id','row_sum_abs_max','min_offdiagonal_including_implicit_zeros','original_homecrit_1e_minus2_would_pass','conservative_generator_math_checks_pass','expected_counterexample_detected']} for e in fixtures]}),flush=True)
    if public_err:print(public_err.decode('utf-8','replace'),file=sys.stderr)
    return 0 if passed else 1
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--group',choices=('conservation','signs'),required=True)
    raise SystemExit(main(parser.parse_args().group))
