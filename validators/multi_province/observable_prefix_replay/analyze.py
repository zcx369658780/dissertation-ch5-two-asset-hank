"""Read durable captures only. No model imports or scientific invocations."""
import csv
import json
import math
from pathlib import Path
import sys
import numpy as np

REPO=Path(__file__).resolve().parents[3]
OLD=Path(r'D:\ProjectTemp\ch5-mp4c-2018-final-production-path-faithful-durable-execution-20260903-001')
FIELDS=('rah','rb','tau','w','Tt','rb_gap','Yt','Lt','Kt','Zt','GovInv')
EPS=128*np.finfo(float).eps

def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def save(p,v):Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8',newline='\n')
def table(p,rows):
    if not rows:return
    with Path(p).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(dict.fromkeys(k for r in rows for k in r)));w.writeheader();w.writerows(rows)
def load(p):
    p=Path(p);obj=read(p);arrays={}
    if p.with_suffix('.npz').exists():
        with np.load(p.with_suffix('.npz'),allow_pickle=False) as z:arrays={k:z[k].copy() for k in z.files}
    def rec(x):
        if isinstance(x,list):return [rec(i) for i in x]
        if isinstance(x,dict):
            if 'array' in x:return arrays[x['array']].tolist()
            if 'nonfinite' in x:return x
            return {k:rec(v) for k,v in x.items()}
        return x
    return rec(obj)
def near(x,y):return math.isfinite(x) and math.isfinite(y) and abs(x-y)<=EPS*max(1,abs(x),abs(y))
def flags(x,lo,hi):
    return {'below':x<lo,'above':x>hi,'exact_lower':x==lo,'exact_upper':x==hi,'near_lower':near(x,lo),'near_upper':near(x,hi),'lower_distance':x-lo,'upper_distance':hi-x}
def compare(capture):
    with (OLD/'household_call_ledger.csv').open(encoding='utf-8-sig') as f:old=list(csv.DictReader(f))
    rows=[];first=None;prefix=0;maxima={k:{'absolute':0.,'scaled_eps':0.} for k in FIELDS}
    for p in sorted(capture.glob('call_*/entry.json')):
        e=read(p);c=e['context'];state=e['state'];n=c['call'];o=old[n-1]
        categories={'outer_iteration':c['step'],'province_index_0based':c['province_index_0'],'province':c['province'],'global_household_call_number':n}
        matches=all(str(v)==o[k] for k,v in categories.items());bad=[]
        for k,v in categories.items():
            if str(v)!=o[k]:bad.append({'field':k,'old':o[k],'new':v,'category':True})
        for k in FIELDS:
            x=float(state[k]);y=float(o[k]);error=abs(x-y);scaled=error/(np.finfo(float).eps*max(1,abs(x),abs(y)));ok=near(x,y)
            maxima[k]['absolute']=max(maxima[k]['absolute'],error);maxima[k]['scaled_eps']=max(maxima[k]['scaled_eps'],scaled)
            row={**categories,'field':k,'old':y,'new':x,'absolute_error':error,'scaled_eps':scaled,'matches_128eps':ok};rows.append(row)
            if not ok:bad.append(row)
            matches=matches and ok
        if first is None and not matches:first={'call':n,'step':c['step'],'province':c['province'],'differences':bad}
        if first is None:prefix=n
    return {'available_entries':len(rows)//len(FIELDS),'matched_prefix':prefix,'first_mismatch':first,'maxima':maxima,'rule':'abs(x-y)<=128*eps64*max(1,abs(x),abs(y)); exact categories/order'},rows

def analyze(root,out):
    capture=root/'capture';out.mkdir(parents=True,exist_ok=True)
    comp,comparisons=compare(capture);save(out/'prefix_comparison.json',comp);table(out/'entry_comparison.csv',comparisons)
    common=[load(p) for p in sorted(capture.glob('turn_*/common_entering.json'))]
    assert all(len(x['state'])==31 for x in common)
    names=[s['name'] for s in common[0]['state']] if common else []
    commonrows=[]
    for x in common:
        for i,s in enumerate(x['state']):commonrows.append({'step':x['iteration'],'index_0':i,'tKN':x['tKN'][i],**s})
    table(out/'common_entering_scalars.csv',commonrows)
    household=[]
    for p in sorted(capture.glob('call_*/entry.json')):
        e=read(p);s=e['state'];r={'step':e['context']['step'],'call':e['context']['call'],'province':s['name'],'phase':'INITIALIZATION' if e['context']['step']==1 else 'HOUSEHOLD_ENTRY',**{k:s[k] for k in FIELDS},'ra_carried':s['ra'],'wjt_carried':s['wjt']}
        r.update({'rah_descriptive_'+k:v for k,v in flags(s['rah'],s['ramin'],s['ramax']).items()})
        r['w_constraint']='COMPOSITE_NO_FIRM_BOUND'
        hp=p.parent/'household_return.json';r['household_return_saved']=hp.exists()
        if hp.exists():
            h=read(hp);r.update(h['aggregates']);r.update({k:h[k] for k in ('hjb_converged','hjb_iterations','hjb_statistic')})
        household.append(r)
    table(out/'household_entries.csv',household)
    firms=[];controllers=[];actions=[];checks=[];focused=[]
    for turn in sorted(capture.glob('turn_*')):
        step=int(turn.name[5:]);enter=load(turn/'common_entering.json')
        for p in sorted(turn.glob('firm_*_return.json')):
            idx=int(p.stem.split('_')[1]);v=read(p);inp=read(p.with_name(p.name.replace('_return','_input')));s=inp['province'];par=inp['params'];row={'step':step,'index_0':idx,'province':s['name'],'phase':'CAPTURED_FIRM_RETURN','path_scope':'NEW_PATH' if comp['first_mismatch'] and step>=comp['first_mismatch']['step'] else 'MATCHED_ENTRY_PREFIX',**v,**{'input_'+k:x for k,x in s.items()},'kt_supply':inp['kt_supply'],'lt_supply':inp['lt_supply']}
            row.update({'ra_'+k:x for k,x in flags(v['ra'],s['ramin'],s['ramax']).items()});row.update({'wjt_'+k:x for k,x in flags(v['wjt'],s['wjtmin'],s['wjtmax']).items()})
            row.update(ra0_below=v['ra0']<s['ramin'],ra0_above=v['ra0']>s['ramax'],wt0_below=v['wt0']<s['wjtmin'],wt0_above=v['wt0']>s['wjtmax'])
            div=v['PIt']*(1-s['corptau'])/v['Kt'];mt=((s['rk']-(s['Zt_1']-s['Zt'])/s['Zt']-s['alpha']*(s['Kt_prev']-v['Kt'])/v['Kt']-(1-s['alpha'])*(s['Lt_prev']-v['Lt'])/v['Lt'])*s['pit']*par['theta']/par['epsilon']+1-1/par['epsilon']-(s['pit']-s['pit_1'])*par['theta']/par['epsilon'])
            row.update(divrate_derived=div,delta=par['delta'],Y_over_K=v['Yt']/v['Kt'],private_share=inp['kt_supply']/v['Kt'],state_share=s['GovInv']/v['Kt'],mt_derived=mt,mt_prior_rk=s['rk'],mt_Z_change=(s['Zt_1']-s['Zt'])/s['Zt'],mt_K_change=s['alpha']*(s['Kt_prev']-v['Kt'])/v['Kt'],mt_L_change=(1-s['alpha'])*(s['Lt_prev']-v['Lt'])/v['Lt'])
            tax=v['PIt']*s['corptau']+(v['ra0']-v['ra'])*v['Kt']+(v['wt0']-v['wjt'])*v['Lt']
            hp=capture/f'call_{(step-1)*31+idx+1:04d}'/'household_return.json';hr=read(hp)
            # Source worker passes aggregate.l_ss unchanged into household_lt.
            expected_lt=hr['aggregates']['l_ss']
            pairs={'ra0_decomposition':(v['ra0'],v['rk']-par['delta']+div),'rk_decomposition':(v['rk'],v['mt']*s['alpha']/(v['Kt']/v['Yt'])),'mt_decomposition':(v['mt'],mt),'tax_clipping':(v['Corptax'],tax),'current_household_Lt':(s['Lt_prev'],expected_lt),'capital_addition':(v['Kt'],inp['kt_supply']+s['GovInv'])}
            for key,(x,y) in pairs.items():checks.append({'step':step,'province':s['name'],'identity':key,'captured':x,'derived':y,'absolute_error':abs(x-y),'pass_128eps':near(x,y)})
            firms.append(row)
        dp=turn/'diagnostics_return.json'
        if dp.exists():
            d=load(dp);ds=load(turn/'diagnostics_input.json');nk,yt,hc,ru,rl,wu,wl,conv=d['native_tuple'];c={'step':step,'max_nk':d['max_nk'],'max_nk_provinces':'|'.join(names[i] for i in d['max_nk_ties_0']),'max_yt':d['max_yt'],'household_converged':hc,'ra_upper':ru,'ra_lower':rl,'wjt_upper':wu,'wjt_lower':wl,'converged':conv,'adapt_called':(turn/'adapt_return.json').exists(),'gate_derived_from_captured':d['max_nk']<.1 and enter['steady_state']};controllers.append(c)
            for i,name in enumerate(names):focused.append({'step':step,'province':name,'nk_gap':nk[i],'yt_gap':yt[i],'tKN':ds['args'][2][i],'max_tie':i in d['max_nk_ties_0']})
        ap=turn/'adapt_return.json'
        if ap.exists():
            a=load(ap)
            actions.extend({'step':step,**v} for v in a['actual_actions'])
    transmission=[]
    for turn in sorted(capture.glob('turn_*')):
        cp=turn/'allocate_productive_capital_return.json'
        if not cp.exists():continue
        step=int(turn.name[5:]);enter=load(turn/'common_entering.json');states=enter['state'];capital=load(cp)
        total=sum(float(s['inter_prv_ratio']*s['ra']) for s in states)
        nextp=capture/f'turn_{step+1:04d}'/'common_entering.json';nextstates=load(nextp)['state'] if nextp.exists() else None
        for i,s in enumerate(states):
            ratio=s['inter_prv_ratio'];expected=(1-ratio)*s['ra']+ratio*(total-ratio*s['ra'])/30
            actual=capital['household_illiquid_return_rah'][i]
            transmission.append({'generation_turn':step,'household_entry_turn':step+1,'province':s['name'],'consumed_old_ra':s['ra'],'old_ra_generation_turn':step-1 if step>1 else 'INITIALIZATION','ratio':ratio,'captured_rah':actual,'derived_rah':expected,'algebra_match':near(actual,expected),'next_common_rah':nextstates[i]['rah'] if nextstates else None,'next_common_match':near(actual,nextstates[i]['rah']) if nextstates else None})
    table(out/'rah_lag_transmission.csv',transmission)
    table(out/'firm_prices_and_operands.csv',firms);table(out/'controller_timeline.csv',controllers);table(out/'controller_all_provinces.csv',focused);table(out/'actual_adaptive_actions.csv',actions);table(out/'algebra_checks.csv',checks)
    panel=[]
    for name in names:
        f=[r for r in firms if r['province']==name];h=[r for r in household if r['province']==name];row={'province':name,'common_entries':len(common),'household_entries':len(h),'firm_returns':len(f),'initialized_ra':common[0]['state'][names.index(name)]['ra'],'initialized_wjt':common[0]['state'][names.index(name)]['wjt'],'initialized_rah':common[0]['state'][names.index(name)]['rah'],'initialized_w':common[0]['state'][names.index(name)]['w']}
        for k in ('ra0','wt0','ra','wjt','mt'):
            row[k+'_min']=min((x[k] for x in f),default=None);row[k+'_max']=max((x[k] for x in f),default=None)
        for k in ('ra0_below','ra0_above','wt0_below','wt0_above','ra_exact_lower','ra_exact_upper','wjt_exact_lower','wjt_exact_upper','ra_near_lower','ra_near_upper','wjt_near_lower','wjt_near_upper'):row[k+'_count']=sum(x[k] for x in f)
        for k in ('rah','w'):row[k+'_min']=min((x[k] for x in h),default=None);row[k+'_max']=max((x[k] for x in h),default=None)
        panel.append(row)
    table(out/'province_coverage.csv',panel)
    with (OLD/'hjb_return_ledger.csv').open(encoding='utf-8-sig') as f:oldh={int(x['global_household_call_number']):x for x in csv.DictReader(f)}
    hjbcompare=[]
    for p in sorted(capture.glob('call_*/hjb_return_before_kfe.json')):
        n=int(p.parent.name[5:]);h=read(p);o=oldh.get(n)
        if o:
            x=h['convergence_statistic'];y=float(o['hjb_convergence_statistic'])
            hjbcompare.append({'call':n,'old_converged':o['hjb_converged'],'new_converged':h['converged'],'old_iterations':o['hjb_iterations'],'new_iterations':h['iterations'],'old_statistic':y,'new_statistic':x,'status_match':str(h['converged'])==o['hjb_converged'] and h['iterations']==int(o['hjb_iterations']),'statistic_match_128eps':near(x,y) if isinstance(x,(float,int)) else False})
    table(out/'hjb_return_comparison.csv',hjbcompare)
    with (REPO/'reports/province_price_boundary_audit_20260908/controller_timeline.csv').open(encoding='utf-8-sig') as f:oldc={int(x['completed_turn']):x for x in csv.DictReader(f)}
    auditcompare=[]
    for c in controllers:
        o=oldc.get(c['step'])
        if o:
            for newkey,oldkey in [('max_nk','maxKNratiogap'),('max_yt','maxYtgap')]:
                if o[oldkey] and o[oldkey]!='nan':
                    y=float(o[oldkey]);auditcompare.append({'step':c['step'],'field':newkey,'old_derived_from_saved':y,'new_captured':c[newkey],'match_128eps':near(c[newkey],y)})
    table(out/'accepted_timeline_comparison.csv',auditcompare)
    terminal=read(capture/'terminal.json') if (capture/'terminal.json').exists() else None
    save(out/'summary.json',{'prefix':comp,'common_full31_entries':len(common),'household_entries':len(household),'firm_returns':len(firms),'controller_records':len(controllers),'actual_action_records':len(actions),'algebra_checks':len(checks),'algebra_failures':[x for x in checks if not x['pass_128eps']],'terminal':terminal,'Results_eligible':False})
    print(json.dumps({'entries':len(household),'firms':len(firms),'controllers':len(controllers),'prefix':comp['matched_prefix'],'first':comp['first_mismatch'],'algebra_failures':sum(not x['pass_128eps'] for x in checks)},ensure_ascii=False))

if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8');analyze(Path(sys.argv[1]),Path(sys.argv[2]))
