"""Read persisted scalars, reconstruct prices and controller diagnostics only.

No HJB panels, model imports, one-turn routines or solver calls are used.
"""
import csv
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import sys
from core import BOUNDS, classify, close, controller, gov_multiplier, portfolio, raw_prices, spell, weight_sums

REPO = Path(__file__).resolve().parents[3]
OWNER = Path(r'D:\ProjectTemp\ch5-mp4c-owner-a-corrected-2009-2022-8worker-20260902-001')
CACHE = Path(r'D:\ProjectTemp\ch5-mp4c-full-annual-batch-runtime-cache-20260902-002')
CAPTURE = Path(r'D:\ProjectTemp\ch5-mp4c-2018-final-production-path-faithful-durable-execution-20260903-001')
RETRY = Path(r'D:\ProjectTemp\ch5-mp4c-owner-a-2018-observable-single-retry-20260903-002')
PROTECTED = Path('D:/MatlabProgram/2023年12月2日 多省份神经网络HANK')
USED = {}


def digest(raw): return hashlib.sha256(raw).hexdigest().upper()


def consume(path, expected=None):
    path = Path(path); raw = path.read_bytes(); actual = digest(raw)
    if expected is not None:
        assert expected.upper() == actual, str(path)
    USED[str(path)] = {'path': str(path), 'bytes': len(raw), 'sha256': actual,
                       'expected_sha256': expected, 'binding': 'MATCHED_EXISTING_HASH' if expected else 'CURRENT_READ_HASH'}
    return raw


def read(path, expected=None): return json.loads(consume(path, expected).decode('utf-8-sig'))


def write(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n', encoding='utf-8', newline='\n')


def table(path, rows):
    fields = list(dict.fromkeys(k for row in rows for k in row))
    with Path(path).open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fields, lineterminator='\n'); writer.writeheader(); writer.writerows(rows)


def prices(row, provenance, phase):
    result = dict(row)
    for field, bounds in [('ra0', BOUNDS['ra']), ('ra', BOUNDS['ra']), ('rah', BOUNDS['ra']),
                          ('wt0', BOUNDS['wjt']), ('wjt', BOUNDS['wjt'])]:
        result[field+'_provenance'] = provenance.get(field, 'MISSING')
        result[field+'_constraint'] = 'DESCRIPTIVE_FIRM_RANGE_ONLY' if field=='rah' else 'FIRM_NATIVE'
        for key, val in classify(row.get(field), *bounds, provenance.get(field, 'MISSING'), phase).items():
            result[field+'_'+key] = val
    result['w_provenance'] = provenance.get('w', 'MISSING')
    result['w_constraint'] = 'COMPOSITE_NO_FIRM_CLIP'
    result['rah_above_owner_recollection_0p07'] = row.get('rah') is not None and row['rah']>.07
    result.update(ramin=.02,ramax=.09,wjtmin=.8,wjtmax=1.3,
                  bounds_provenance='HASH_BOUND_EXECUTED_ADAPTER_LITERALS',phase=phase)
    for raw, clipped in [('ra0','ra'),('wt0','wjt')]:
        result[clipped+'_clipped_amount'] = row[raw]-row[clipped] if row.get(raw) is not None and row.get(clipped) is not None else None
    return result


def source_check():
    review = consume(REPO/'docs/CH5_MP4C_PRICE_BOUNDARY_SOURCE_REVIEW_20260908.md').decode('utf-8')
    protected = []
    for name, expected in re.findall(r'\| ([A-Za-z0-9_]+\.m) \| ([0-9A-F]{64}) \|', review):
        consume(PROTECTED/name, expected); protected.append(name)
    assert len(protected)==7
    return {'protected_files_matched': protected,
            'native_annual_top_level_inventory': [p.name for p in PROTECTED.glob('Multi_Province_12sts_*.mat')],
            'native_annual_scope': 'No native annual st path located in consumed run manifests; inventory only, no unbound state substitution.'}


def code_identities(manifest):
    result=[]
    for rel, expected in manifest.get('scientific_code_identities',{}).items():
        raw=consume(REPO/rel)
        match = expected in (digest(raw), digest(raw.replace(b'\r\n', b'\n')))
        historical = None
        if not match and rel == 'validators/multi_province/mp4c_python_annual_production.py':
            old = subprocess.run(['git','show','9944ddb:'+rel],cwd=REPO,check=True,stdout=subprocess.PIPE).stdout
            historical = expected in (digest(old),digest(old.replace(b'\n',b'\r\n')))
            match = historical
        result.append({'path':rel,'expected':expected,'raw_or_LF_match':match,'historical_9944ddb_match':historical})
    return result


def annual_panels():
    rows=[]; counts=[]; identities=[]; missing=[]
    for regime, base, years in [('OWNER_A',OWNER,range(2009,2023)),('RUNTIME_CACHE',CACHE,range(2009,2024))]:
        for year in years:
            folder=base/f'year_{year}'
            manifest=read(folder/'run_manifest.json'); identities.extend(code_identities(manifest))
            inp=read(folder/f'calendar_{year}_matlab_runtime_cache_input.json',manifest['runtime_input_sha256'])
            if not (folder/'final_steady_state.json').exists():
                missing.append({'regime':regime,'year':year,'missing':'terminal state','inventory':[p.name for p in folder.iterdir()]});continue
            success=read(folder/'SUCCESS.json')
            final=read(folder/'final_steady_state.json',success['outputs']['final_steady_state.json']['sha256'])
            assert len(final['final_31x20'])==31 and final['province_order']==inp['province_order']
            cp=read(folder/'checkpoint_manifest.json',success['outputs']['checkpoint_manifest.json']['sha256'])
            assert cp['terminal_sha256']==digest((folder/'final_steady_state.json').read_bytes())
            per=[]
            for i,s in enumerate(final['final_31x20']):
                assert s['name']==inp['province_order'][i]
                alpha=inp['vectors']['IND_alpha'][i]
                # Terminal convergence exits before adaptation; stored Zt/GovInv are firm-used.
                raw=raw_prices(s['Yt'],s['Kt'],s['Lt_supply'],s['mt'],alpha,s['Zt'],s['rk'])
                row=dict(s,regime=regime,year=year,step=final['iteration_count'],index_0=i,index_1=i+1,
                         provenance=str(folder/'final_steady_state.json'),alpha=alpha,
                         Zt_init=inp['vectors']['IND_Zt'][i],Zt_used=s['Zt'],Zt_after_adaptation=s['Zt'],
                         Kt0=inp['vectors']['CAP'][i],N=inp['vectors']['POP'][i],Yt0=inp['vectors']['GDP'][i],
                         GovInv_used=s['GovInv'],GovInv_after=s['GovInv'],
                         inter_prv_ratio=inp['derived']['inter_province_asset_ratio'][i],
                         ra0=raw['ra0'],wt0=raw['wt0'],divrate=raw['divrate'],
                         raw_price_provenance='DERIVED_SAVED_SAME_STAGE_OPERANDS',
                         ra_clip_identity_pass=close(raw['ra'],s['ra']),wjt_clip_identity_pass=close(raw['wjt'],s['wjt']),
                         production_identity_pass=close(s['Zt']*s['Kt']**alpha*s['Lt_supply']**(1-alpha),s['Yt']),
                         Y_over_K=s['Yt']/s['Kt'],Y_over_target=s['Yt']/inp['vectors']['GDP'][i],
                         productive_AtN=s['At']*inp['vectors']['POP'][i],
                         final_gate='CONVERGENCE_EXIT_FIRST',raw_capture='NOT_PERSISTED_IN_20_FIELD_SERIALIZER',
                         binding=json.dumps(inp['binding'],sort_keys=True),input_representation=inp['representation'])
                row=prices(row,{k:'CAPTURED' for k in ('ra','rah','wjt','w')}|{'ra0':'DERIVED','wt0':'DERIVED'},'terminal_post_firm_pre_adaptation')
                rows.append(row);per.append(row)
            counts.append({'regime':regime,'year':year,'observed':31,'step':final['iteration_count'],
                **{f:sum(bool(r.get(f)) for r in per) for f in ('ra_exact_lower','ra_exact_upper','wjt_exact_lower','wjt_exact_upper','ra0_strict_above','ra0_strict_below','wt0_strict_above','wt0_strict_below','rah_above_owner_recollection_0p07')},
                'raw_to_clip_failures':sum(not r['ra_clip_identity_pass'] or not r['wjt_clip_identity_pass'] for r in per)})
    return rows,counts,identities,missing


def failed_path():
    inp=read(OWNER/'year_2018/calendar_2018_matlab_runtime_cache_input.json','F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0')
    loc=read(CAPTURE/'first_singularity_localization.json','3628725A54B97344F501C0E44D32338A0B5CF6733D6022B9DD7A4C82C890BD63')
    read(CAPTURE/'diagnostic_child_launch_receipt.json'); read(CAPTURE/'diagnostic_execution_receipt.json')
    read(CAPTURE/'retrospective_execution_evidence_manifest.json','D0472539EA553CFCFF7D34046EA71C8C68DD78C7FF7D44F58F7A3AD50D06C490')
    raw=consume(CAPTURE/'household_call_ledger.csv','78F1BAFC3664D1ED644293FE98FA384468B23291F9CE8E42400EE0F63BB06A9F')
    ledger=list(csv.DictReader(raw.decode('utf-8').splitlines()))
    hjb=list(csv.DictReader(consume(CAPTURE/'hjb_return_ledger.csv','7D914989AD3CD047FA45CABA5A9209563465BE1799410BB01699F51CF542DA3F').decode('utf-8').splitlines()))
    assert len(ledger)==len(hjb)==725
    groups={}; hgroups={}
    for row,h in zip(ledger,hjb):
        s=int(row['outer_iteration']);i=int(row['province_index_0based'])
        assert row['province']==inp['province_order'][i]
        assert int(row['global_household_call_number'])==(s-1)*31+i+1
        v={k:float(x) for k,x in row.items() if k not in ('province',)}
        v['name']=row['province'];groups.setdefault(s,{})[i]=v;hgroups.setdefault(s,[]).append(h)
    ratios=inp['derived']['inter_province_asset_ratio']; weights=weight_sums(ratios)
    reconstruction=[]; timelines=[]; tkn=[3.]*31
    for step in range(1,24):
        before=groups[step]; after=groups[step+1]; dp={}; diagnostics=[]
        for i,v in after.items():
            old=before[i];alpha=inp['vectors']['IND_alpha'][i]
            nk=v['Kt']/v['Lt']; gap=abs(nk/tkn[i]-1);ygap=abs(v['Yt']/old['Yt']-1)
            diagnostics.append((gap,i,ygap))
            expected_z=inp['vectors']['GDP'][i]*v['Kt']**(-alpha)*v['Lt']**(alpha-1)
            reconstruction.append(dict(step=step,index_0=i,index_1=i+1,name=v['name'],
                mt=None,ra0=None,wt0=None,ra=None,wjt=None,rk=None,divrate=None,
                Zt_used=old['Zt'],Zt_after=v['Zt'],GovInv_used=old['GovInv'],GovInv_after=v['GovInv'],
                Zt_changed=v['Zt']!=old['Zt'],GovInv_ratio=v['GovInv']/old['GovInv'],
                Yt=v['Yt'],Kt=v['Kt'],Lt_supply=v['Lt'],Y_over_K=v['Yt']/v['Kt'],
                Kt_supply_derived=v['Kt']-old['GovInv'],alpha=alpha,N=inp['vectors']['POP'][i],
                Kt0=inp['vectors']['CAP'][i],Zt_init=inp['vectors']['IND_Zt'][i],
                production_identity_pass=close(old['Zt']*v['Kt']**alpha*v['Lt']**(1-alpha),v['Yt']),
                nk_gap=gap,yt_gap=ygap,Y_over_target=v['Yt']/inp['vectors']['GDP'][i],
                z_reset_candidate=expected_z,provenance='CAPTURED_SCALARS_WITH_DERIVED_GAPS',raw_price_gap='missing current household Lt used as Lt_prev, and carried rk'))
        complete=len(after)==31
        largest=max(diagnostics); gate=controller(largest[0] if complete else None,1,False)
        timelines.append({'completed_turn':step,'observed_post_provinces':len(after),'complete_national_post_coverage':complete,
            'maxKNratiogap':largest[0] if complete else None,'maximum_province':inp['province_order'][largest[1]] if complete else None,
            'observed_subset_max_gap':largest[0],'maxYtgap':max(x[2] for x in diagnostics) if complete else None,
            'steady_state':1,'convergence_exited_first':False,'exit_evidence':'next household batch actually entered',
            'gate':gate,'gate_provenance':'DERIVED_EXPECTATION_FROM_CAPTURED_KT_LT_HISTORY',
            'captured_controller_event_record':False})
        for rec in reconstruction:
            if rec['step']!=step:continue
            i=rec['index_0'];before_i=before[i];after_i=after[i]
            observed=after_i['GovInv']/before_i['GovInv']
            multiplier=1. if gate=='CLOSED' else None
            rec['gate']=gate;rec['expected_gov_multiplier']=multiplier
            rec['inferred_ra_trigger']='ra > ramax-.02' if close(observed,1.1) else 'ra < ramin+.02' if close(observed,.9) else 'no price inference'
            rec['captured_action_class']='INCREASE_1P1' if close(observed,1.1) else 'DECREASE_0P9' if close(observed,.9) else 'UNCHANGED' if after_i['GovInv']==before_i['GovInv'] else 'OTHER'
            rec['enabled_action_is_source_multiplier']=observed==1 or close(observed,.9) or close(observed,1.1)
            rec['gov_expectation_matches']=close(after_i['GovInv'],before_i['GovInv']*multiplier) if multiplier is not None else None
            z_expected=rec['z_reset_candidate'] if gate=='ENABLED' and abs(rec['Y_over_target']-1)>.01 else before_i['Zt'] if gate!='UNKNOWN_GATE' else None
            rec['zt_expectation_matches']=close(after_i['Zt'],z_expected) if z_expected is not None else None
            rec['action_evidence']='CAPTURED_BEFORE_AFTER_STATES__NO_ACTION_EVENT'
        for gap,i,ygap in diagnostics:tkn[i]=.6*(after[i]['Kt']/after[i]['Lt'])+.4*tkn[i]
    panel=[];transmission=[]
    for step,g in groups.items():
        implied=portfolio([.09]*31,ratios) if step==2 else None
        for i,v in g.items():
            row=dict(v,regime='OWNER_A_CAPTURE_PID67056',year=2018,step=step,index_0=i,index_1=i+1,
                provenance=str(CAPTURE/'household_call_ledger.csv'),ra=.09 if step==1 else None,wjt=.6 if step==1 else None,
                ra0=None,wt0=None,
                inter_prv_ratio=ratios[i],portfolio_weight_sum=weights[i],
                raw_price_generation_turn=step-1 if step>1 else None,
                rah_ra_generation_turn=step-2 if step>2 else 'initial',
                rah_implied=implied[i] if implied else None,rah_transmission_pass=close(implied[i],v['rah']) if implied else None,
                lagged_ra_identified=v['rah'] if ratios[i]==0 and step>1 else None,
                lagged_ra_identification='DERIVED_IDENTITY_ZERO_EXTERNAL_WEIGHT' if ratios[i]==0 and step>1 else 'MISSING')
            panel.append(prices(row,{'rah':'CAPTURED','w':'CAPTURED','ra':'MISSING' if step>1 else 'SOURCE_INITIALIZATION',
                'wjt':'MISSING' if step>1 else 'SOURCE_INITIALIZATION','ra0':'MISSING' if step>1 else 'MISSING',
                'wt0':'MISSING' if step>1 else 'MISSING'},'initialization' if step==1 else 'household_entry_old_state'))
    for key in ('rah','w','Zt','GovInv','Kt','Lt','Yt'):assert panel[-1][key]==loc[key]
    timelines.append({'completed_turn':24,'observed_post_provinces':0,'gate':controller(None,1,False,False),
        'convergence_exited_first':False,'captured_controller_event_record':False,
        'reason':'exception inside household call725 before batch/one-turn returned; 12 entries, no complete 24th turn'})
    return inp,panel,reconstruction,timelines,groups


def main():
    base=Path(r'D:\ProjectTemp\ch5-province-price-boundary-audit-20260908-001');root=base;n=1
    while root.exists(): n+=1;root=base.with_name(base.name[:-3]+f'{n:03d}')
    root.mkdir(); print(str(root),flush=True)
    sources=source_check()
    annual,counts,identities,missing=annual_panels()
    inp,panel,recon,timeline,groups=failed_path()
    for p in (RETRY/'retry_2018_execution_receipt.json',RETRY/'retry_2018_stderr.log',RETRY/'retry_2018_stdout.log'):
        consume(p)
    allrows=panel+annual
    table(root/'failed_path_prices.csv',panel);table(root/'price_decomposition.csv',recon)
    table(root/'annual_prices.csv',annual);table(root/'annual_counts.csv',counts);table(root/'controller_timeline.csv',timeline)
    roster=[]
    for i,name in enumerate(inp['province_order']):
        pr=[r for r in panel if r['index_0']==i and r['step']>1]
        row={'index_0':i,'index_1':i+1,'province':name,'captured_price_fields':'rah,w',
             'derived_price_fields':'lagged ra only when external weight=0','missing_path_fields':'ra0,ra,wt0,wjt,At,Bt,household_Lt,action events',
             'entry_rows':len(pr)+1,'last_entry':max(r['step'] for r in panel if r['index_0']==i),
             'annual_owner_A':13,'annual_runtime_cache':15,'terminal_2018_owner_A':'MISSING'}
        for field in ('ra','wjt','rah'):
            for k,v in spell([(r['step'],r[field+'_exact_upper']) for r in pr if field+'_exact_upper' in r]).items():row[field+'_upper_'+k]=v
        roster.append(row)
    table(root/'province_coverage_and_spells.csv',roster)
    summary={'diagnostic_completion':'PARTIAL_EVIDENCE','boundary_findings':'OBSERVED_CONTACTS_AND_DERIVED_ANNUAL_RAW_EXCURSIONS',
        'high_rah_root_cause':'SUPPORTED_LINK','root_cause_scope':'lagged price/portfolio transmission only; no convergence causality',
        'capture_run':str(CAPTURE),'capture_ledger_rows':len(panel),'common_full_entry_steps':23,'partial_entry_step24_provinces':12,
        'national_gate_steps_reconstructed':22,'annual_owner_A_province_years':403,'annual_runtime_cache_province_years':465,
        'annual_raw_clip_mismatch_rows':sum(not r['ra_clip_identity_pass'] or not r['wjt_clip_identity_pass'] for r in annual),
        'path_production_identity_failures':sum(not r['production_identity_pass'] for r in recon),
        'rah_transmission_failures':sum(r['rah_transmission_pass'] is False for r in panel),
        'controller_gov_mismatches':sum(r['gov_expectation_matches'] is False for r in recon),
        'controller_zt_mismatches':sum(r['zt_expectation_matches'] is False for r in recon),
        'source_identity_mismatches':[x for x in identities if not x['raw_or_LF_match']],
        'anhui_call725':panel[-1],'annual_counts':counts,'controller_timeline':timeline,
        'missing':missing,'results_eligible':False}
    write(root/'summary.json',summary);write(root/'source_identity.json',sources|{'runtime_code_checks':identities})
    write(root/'consumed_inputs.json',list(USED.values()))
    write(root/'scope_inventory.json',{'capture_root':[p.name for p in CAPTURE.iterdir()],
        'original_2018':[p.name for p in (OWNER/'year_2018').iterdir()],
        'retry_2018':[p.name for p in (RETRY/'year_2018').iterdir()]})
    print(json.dumps({k:v for k,v in summary.items() if k not in ('anhui_call725','annual_counts','controller_timeline')},ensure_ascii=False,indent=2))


if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8');main()
