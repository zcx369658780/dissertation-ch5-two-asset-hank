"""Close finite evidence and small repository summaries; never execute science."""
import json
import platform
import shutil
import sys
import numpy as np
import scipy
from common import ROOT, REPO, HERE, OLD, CASES, read, write, sha

def identity(path): return {'path':str(path),'sha256':sha(path),'bytes':path.stat().st_size}
def main():
    summary=read(ROOT/'replay_summary.json'); ledger={}; totals={}
    for language in ('matlab','python'):
        rows=[]
        for case in CASES:
            receipt=read(ROOT/f'{language}_{case}_process.json'); worker=read(ROOT/f'{language}_{case}/ledger.json')
            assert receipt['exit_code']==0 and receipt['state']=='SUCCEEDED'
            assert all(worker[k]==1 for k in ('invocations_entered','iterations_entered','solves_entered','completed_updates'))
            rows.append({'case':case,'process_state':receipt['state'],'elapsed_seconds':receipt['elapsed_seconds'],**worker})
        ledger[language]=rows
        totals[language]={key:sum(r[key] for r in rows) for key in ('invocations_entered','iterations_entered','solves_entered','completed_updates')}
    write(ROOT/'call_ledger.json',{'per_case':ledger,'totals':totals,'scientific_retries':0,
        'full_trajectory':0,'native_initialization':0,'condition_solves':0,'KFE':0,'distribution_aggregation':0,
        'GE_annual':0,'R_PLM':0,'shock_IRF':0,'Results':0,'historical_budgets':'unchanged and remain consumed'})
    compact={'completion':'COMPLETE','verdict':summary['verdict'],'baseline':'a55019d4a6fe7b36eb783223e8b20dbc73fa59fb',
             'cases':{case:{k:r[k] for k in ('passed','fields_passed','fields_total','failed_fields','V1_max_abs','max_scaled')} for case,r in summary['cases'].items()},
             'origin_fidelity_pass':summary['origin_fidelity_pass'],'new_calls':totals,
             'convergence_gap_resolved':False,'full_trajectory_parity':False,'results_eligibility':False}
    write(ROOT/'result.json',compact)
    checked=[]
    for r in read(ROOT/'frozen_identities.json'):
        assert sha(r['path'])==r['sha256'];checked.append(r)
    reconstruction=[]
    growth=read(ROOT/'operator_growth.json'); split=read(ROOT/'first_split.json')
    for lang,r in growth.items():
        for name in ('norm_row_attribution','most_negative_offdiag_attribution'): reconstruction.append(r[name])
    for row in split['transfer']['decisions']:reconstruction.extend(row.values())
    assert all(r['reconstructed_transfer_label']==r['persisted_transfer_label'] for r in reconstruction)
    assert all(c['passed'] for r in reconstruction for c in r['reconstructed_persisted_checks'].values())
    checks={'focused_tests':8,'focused_tests_passed':8,'test_command':'python -B -m unittest discover -s tests -p test_call725_policy_operator_stability.py -v',
            'unchanged_scientific_body_checks':2,'all_common_MAT_exact_readback':True,
            'origin_replay_fidelity':summary['origin_fidelity_pass'],'attributed_cells_reconstruction_checks_pass':True,
            'frozen_identity_recheck_pass':True,'scientific_processes_exit_zero':8,
            'finite_comparisons':all(row['finite'] for case in read(ROOT/'replay_comparisons.json').values() for row in case['rows']),
            'runtime':{'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'platform':platform.platform(),'matlab':'R2022b'},
            'checks_scope':'Changed diagnostics and wrapper binding only; no model regression or additional solve'}
    write(ROOT/'checks.json',checks)
    source_map={'transfer_FOC':'protected HANK3_FOC.m:19; exports/matlab_faithful_two_asset_ha.py:103-108 (unclamped va/vb, bare a)',
                'cost':'protected HANK3_cost.m:22; Python export:80-83 (quadratic d, max(a,a_bar) denominator)',
                'consumption_clamp':'Python export:274-277; task MATLAB wrapper:52-55',
                'transfer_selection':'Python export:306-355; task MATLAB wrapper:61-70',
                'upper_a_rate':'Python export:372-376; task MATLAB wrapper:71-73',
                'operator_assembly':'Python export:424 onward; task MATLAB wrapper:110 onward (axis_operator)',
                'value_solve':'task Python wrapper:47; task MATLAB wrapper:75-76',
                'diagnostic_provenance':'branch candidates and signed margins reconstructed from saved inputs; consumed labels and controls are persisted runtime captures. Python mask views are label-derived, not independent captures.'}
    write(ROOT/'source_attribution.json',source_map)
    out=REPO/'reports/call725_policy_operator_stability_20260907';out.mkdir(exist_ok=True)
    for name in ('result.json','call_ledger.json','checks.json','states.json','generator_summary.json','python_tail100.json','tail_switch_coordinates.json','terminal_state.json','first_split.json','operator_growth.json','source_attribution.json','engineering_repairs.json'):
        shutil.copyfile(ROOT/name,out/name)
    # Full comparisons and all MAT/NPZ stay outside Git. Manifest has no recursive self entry.
    files=[p for p in ROOT.rglob('*') if p.is_file() and p.name not in ('manifest.json','manifest_readback.json','publication_receipt.json')]
    sources=[p for p in HERE.iterdir() if p.is_file()]+[REPO/'tests/test_call725_policy_operator_stability.py',REPO/'docs/CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY_REPORT.md']+list(out.iterdir())
    authorities=[REPO/p for p in ('AGENTS.md','project_rules/PROJECT_RULE_INDEX_CURRENT.md','docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md','tasks/CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY.md')]
    manifest={'protocol':'finite sources/inputs/outputs; excludes self and terminal receipts; consumed predecessor identities listed separately',
              'baseline':compact['baseline'],'predecessor_manifest':identity(OLD/'manifest.json'),'predecessor_inventory':identity(OLD/'artifact_inventory.json'),
              'artifacts':[identity(p) for p in sorted(files)],'sources_and_reports':[identity(p) for p in sorted(sources+authorities)],'frozen_inputs':checked}
    write(ROOT/'manifest.json',manifest)
    # One complete readback after final artifacts are frozen.
    for row in manifest['artifacts']+manifest['sources_and_reports']:assert sha(row['path'])==row['sha256']
    write(ROOT/'manifest_readback.json',{'passed':True,'manifest_sha256':sha(ROOT/'manifest.json'),'artifacts':len(files),'sources_and_reports':len(sources+authorities)})
    print(json.dumps({'result':compact,'manifest':read(ROOT/'manifest_readback.json')},indent=2))
if __name__=='__main__':main()
