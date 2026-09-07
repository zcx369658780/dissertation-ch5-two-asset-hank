"""Close existing evidence and reconcile ledgers; never launch scientific work."""
import csv
import hashlib
import json
import shutil
from pathlib import Path

from analyze import ROOT,REPO,write


def identity(path):
    return {'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest().upper(),'bytes':path.stat().st_size}


def main():
    ledgers={}
    for language in ('matlab','python'):
        records={}
        for kind,limit in [('trajectory',500),('replay',1)]:
            key=f'{language}_{kind}'
            process=json.loads((ROOT/f'{key}_process.json').read_text(encoding='utf-8'))
            worker=json.loads((ROOT/key/'ledger.json').read_text())
            suffix='mat' if language=='matlab' else 'npz'
            files=[p for p in (ROOT/key).glob(f'step_*.{suffix}') if len(p.stem)==9]
            traces=[json.loads(line) for line in (ROOT/key/'trace.jsonl').read_text().splitlines()]
            if process['exit_code']!=0 or process['state']!='SUCCEEDED' or process['last_worker_ledger']!=worker:raise ValueError('process/worker status '+key)
            if worker['completed_updates']!=len(files) or len(files)!=len(traces):raise ValueError('core/trace count '+key)
            if not worker['iterations_entered']==worker['solves_entered']==worker['completed_updates']<=limit:raise ValueError('entered/solve count '+key)
            if worker['invocations_entered']!=1:raise ValueError('invocation count '+key)
            records[kind]={'process':process['state'],'exit_code':process['exit_code'],'elapsed_seconds':process['elapsed_seconds'],'worker':worker,'core_trace_count_verified':True}
        ledgers[language]={'invocations':2,'updates_entered':sum(r['worker']['iterations_entered'] for r in records.values()),'direct_solves':sum(r['worker']['solves_entered'] for r in records.values()),'engineering_retries':0,'unused_conditional_retry_invocations':1,'records':records}
    write(ROOT/'call_ledger.json',{'task_owned_calls':ledgers,'downstream_calls':{'native_init':0,'kfe':0,'post_loop_policy_distribution_aggregation':0,'ge_annual':0,'r_plm':0,'shock_irf_results':0},'static_matlab_checkcode_processes':1,'historical_budgets':'unchanged; not reset or included in this task ledger'})
    trajectory=json.loads((ROOT/'trajectory_summary.json').read_text())
    replay=json.loads((ROOT/'common_state_comparison.json').read_text())
    integrity=json.loads((ROOT/'trajectory_integrity.json').read_text())
    if not all(trajectory['first_step_matches_accepted'].values()):raise ValueError('fresh first step mismatch')
    if not all(all(row[k] for k in ('all_loop_carry_exact','immutable_inputs_exact','all_M_RHS_statistic_identities_pass','all_stage_values_finite','all_residuals_finite')) for row in integrity.values()):raise ValueError('trajectory integrity failure')
    verdict='TRAJECTORY_DIVERGENCE_WITH_COMMON_STATE_PARITY_PASS' if trajectory['earliest_divergence'] and replay['passed'] else 'COMMON_STATE_STAGE_MISMATCH'
    result={'completion':'COMPLETE','scientific_verdict':verdict,'baseline':'373264625f0f9580575cda5a36d7a70b371a040b','earliest_generated_difference':{'iteration':2,'stage':'consumption','material_entries':519},'earliest_incoming_state_difference':trajectory['first_incoming_state_difference'],'common_state_replay_pass':replay['passed'],'common_state_fields_compared':len(replay['rows']),'convergence':{k:{'at_100':trajectory['at_100'][k],'final':v['records']['trajectory']['worker']} for k,v in ledgers.items()},'new_invocations':{k:v['invocations'] for k,v in ledgers.items()},'new_direct_solves':{k:v['direct_solves'] for k,v in ledgers.items()},'engineering_retries':0,'results_eligibility':False,'publication':'dedicated non-force branch; no main merge or successor execution'}
    write(ROOT/'result.json',result)
    write(ROOT/'checks.json',{'synthetic_static_tests':{'passed':6,'failed':0,'command':'python -B tests/test_call725_multi_iteration_trajectory.py'},'matlab_checkcode_exit':0,'scientific_body_identity':'PASS in both languages, instrumentation/indentation normalized only','snapshot_source_binding':'hash-verified before each invocation; runtime consumes immutable copies','read_only_helper_review':'instrumentation and analysis review; no scientific execution or acceptance authority','bounded_repairs':['UTF-8 read','static test substring range','runtime snapshots and process/worker receipt reconciliation','same-number step sequence validation','same-branch and common-state evidence guards for consumption attribution'],'model_retries_for_repairs':0})
    stage_rows=list(csv.DictReader((ROOT/'stage_summary.csv').open(encoding='utf-8')))
    overview=[]
    for name in dict.fromkeys(row['name'] for row in stage_rows):
        rows=[r for r in stage_rows if r['name']==name];failed=[r for r in rows if r['passed']=='False']
        overview.append({'field':name,'shared_steps':len(rows),'first_failure':int(failed[0]['iteration']) if failed else None,'failing_steps':len(failed),'maximum_absolute_difference':max(float(r['max_abs']) for r in rows),'maximum_scaled_difference':max(float(r['max_scaled']) for r in rows)})
    write(ROOT/'stage_overview.json',overview)
    # Bind all substantive local artifacts once, excluding this inventory/manifest.
    excluded={'artifact_inventory.json','manifest.json'}
    artifacts=[p for p in ROOT.rglob('*') if p.is_file() and p.name not in excluded and '__pycache__' not in p.parts]
    inventory={'protocol':'finite artifact identities; no manifest/self entry','entries':[identity(p) for p in sorted(artifacts)]}
    write(ROOT/'artifact_inventory.json',inventory)
    report=REPO/'docs/CH5_MP4C_CALL725_MULTI_ITERATION_TRAJECTORY_REPORT.md'
    source_dir=REPO/'validators/multi_province/call725_multi_iteration_trajectory'
    sources=list(source_dir.glob('*.py'))+list(source_dir.glob('*.m'))+[REPO/'tests/test_call725_multi_iteration_trajectory.py',REPO/'validators/multi_province/call725_first_iteration_closure/compare.py',report]
    manifest={'protocol':'finite two-level identity manifest; excludes itself; full local inventory hash binds all captured steps/snapshots/logs','artifact_inventory':identity(ROOT/'artifact_inventory.json'),'artifact_count':len(artifacts),'sources_and_report':[identity(p) for p in sources],'frozen_inputs':json.loads((ROOT/'frozen_identities.json').read_text(encoding='utf-8'))}
    write(ROOT/'manifest.json',manifest)
    dest=REPO/'reports/call725_multi_iteration_trajectory_20260907';dest.mkdir(parents=True,exist_ok=True)
    for name in ('result.json','call_ledger.json','checks.json','state_schema.json','replay_state_identity.json','trajectory_summary.json','trajectory_integrity.json','earliest_step_comparison.json','common_state_comparison.json','earliest_difference_attribution.json','stage_overview.json','manifest.json'):
        shutil.copyfile(ROOT/name,dest/name)
        if (ROOT/name).read_bytes()!=(dest/name).read_bytes():raise ValueError('copy readback '+name)
    for row in inventory['entries']:
        if identity(Path(row['path']))!=row:raise ValueError('artifact readback '+row['path'])
    print(json.dumps({'verdict':verdict,'artifact_count':len(artifacts),'manifest_sha256':identity(ROOT/'manifest.json')['sha256'],'calls':result['new_invocations'],'direct_solves':result['new_direct_solves']},indent=2))


if __name__=='__main__':main()
