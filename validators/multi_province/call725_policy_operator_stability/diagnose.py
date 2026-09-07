"""Stored-array reductions and explicitly labelled source-expression reconstruction.

No HJB evaluator, solver, or production-module import is used here.
Coordinates are zero based; tensor coordinates are (b,a,z), matrix indices F-order.
"""
import json
import math
import numpy as np
from scipy import sparse
from common import ROOT, OLD, CASES, Evidence, analysis, read, write, BINDING

def coord(row): return [int(x) for x in np.unravel_index(int(row),(20,20,2),order='F')]
def extrema(x):
    x=np.asarray(x); assert np.isfinite(x).all()
    return {'min':float(x.min()),'min_index':list(map(int,np.unravel_index(x.argmin(),x.shape))),
            'max':float(x.max()),'max_index':list(map(int,np.unravel_index(x.argmax(),x.shape)))}

def generator(v):
    A=analysis.c.canonical_sparse(v['A']); M=analysis.c.canonical_sparse(v['M'])
    row=np.asarray(A.sum(axis=1)).ravel(); coo=A.tocoo(); mask=coo.row!=coo.col
    vals=coo.data[mask]; rr=coo.row[mask]; cc=coo.col[mask]
    mn=int(vals.argmin()); mx=int(vals.argmax())
    absrows=np.asarray(abs(M).sum(axis=1)).ravel()
    dd=2*abs(M.diagonal())-absrows
    # Retain ordinary reductions and separately expose cancellation in their ordering.
    stable_rows=np.array([math.fsum(A.data[A.indptr[i]:A.indptr[i+1]]) for i in range(A.shape[0])])
    stable_dd=np.array([math.fsum([abs(M[i,i])]+[-abs(x) for j,x in zip(M.indices[M.indptr[i]:M.indptr[i+1]],M.data[M.indptr[i]:M.indptr[i+1]]) if j!=i]) for i in range(M.shape[0])])
    leak=np.zeros((20,20,2))
    leak[0]+=v['bb'][0]; leak[-1]+=v['bf'][-1]
    leak[:,0]+=v['ab'][:,0]; leak[:,-1]+=v['af'][:,-1]
    r=int(absrows.argmax()); rowvec=M.getrow(r).tocoo()
    entries=sorted(zip(rowvec.col,rowvec.data),key=lambda x:abs(x[1]),reverse=True)
    return {'A_row_sums':extrema(row),'A_row_sum_max_abs':float(max(abs(row))),
            'offdiag_min_including_implicit_zero':min(0.,float(vals[mn])),
            'offdiag_max_including_implicit_zero':max(0.,float(vals[mx])),
            'offdiag_min_coordinate':[int(rr[mn]),int(cc[mn])],
            'offdiag_max_coordinate':[int(rr[mx]),int(cc[mx])],
            'negative_offdiag_count':int(sum(vals<0)),
            'negative_offdiag_examples':[[int(i),int(j),float(x)] for i,j,x in zip(rr[vals<0][:8],cc[vals<0][:8],vals[vals<0][:8])],
            'M_diagonal_dominance_margin':extrema(dd),'negative_dd_rows':int(sum(dd<0)),
            'A_row_sums_fsum':extrema(stable_rows),'M_dd_margin_fsum':extrema(stable_dd),
            'outward_omitted_rates':extrema(leak),'nonzero_leak_cells':int(np.count_nonzero(leak)),
            'row_sum_plus_outward_max_abs':float(max(abs(row+leak.ravel(order='F')))),
            'M_norm_inf':float(absrows[r]),'norm_row':r,'norm_row_tensor':coord(r),
            'norm_row_entries':[[r,int(j),float(x)] for j,x in entries],
            'row_sum_note':'Floating stored-matrix reduction; cancellation error at extreme scales is not boundary leakage. Omitted outward rates are separately reconstructed.'}

def branch(v,idx):
    """Reconstruct only listed local arithmetic from persisted derivatives, not HJB."""
    idx=tuple(idx); i,j,k=idx; s=read(BINDING)['scalar_binding']; p=s['parameters']; t=s['numerics']['drift_tolerance']
    a=float(v['a'][j]); b=float(v['b'][i]); z=float(v['z'][k])
    vbB=float(v['post_boundary_vb_b'][idx]); vbF=float(v['post_boundary_vb_f'][idx])
    vaB=float(v['va_b'][idx]); vaF=float(v['va_f'][idx]); candidate={}; operands={}
    for name,va,vb in [('BB',vaB,vbB),('BF',vaF,vbB),('FB',vaB,vbF),('FF',vaF,vbF)]:
        ratio=float(np.divide(va,vb)); low=ratio-1+p['chi_0']; high=ratio-1-p['chi_0']
        candidate[name]=float((np.fmin(low,0.)+np.fmax(high,0.))*a/p['chi_1'])
        operands[name]={'va':va,'vb_unclamped':vb,'ratio':ratio,'lower_signed_margin':low,'upper_signed_margin':high,'candidate':candidate[name]}
    dB=(candidate['BF'] if candidate['BF']>0 else 0)+(candidate['BB'] if candidate['BB']<0 else 0)
    dF=(candidate['FF'] if candidate['FF']>0 else 0)+(candidate['FB'] if candidate['FB']<0 else 0)
    overrides=[]
    if j==0:
        dB=candidate['BF'] if candidate['BF']>t else 0.; dF=candidate['FF'] if candidate['FF']>t else 0.; overrides.append('lower a uses positive forward-a candidates > tolerance')
        if i==0:dB=max(dB,0.)
    if j==19:
        dB=candidate['BB'] if candidate['BB'] < -t else 0.; dF=candidate['FB'] if candidate['FB'] < -t else 0.; overrides.append('upper a uses negative backward-a candidates < -tolerance; af=0')
    def cost(d): return float(p['chi_0']*abs(d)+p['chi_1']*d**2/2*(max(a,p['a_bar']))**-1)
    sB=-dB-cost(dB); sF=-dF-cost(dF); useF=sF>t; useB=sB < -t and not useF
    if i==0:useB=False; overrides.append('lower b forces Idh_B=0')
    if i==19:useB=True;useF=False;overrides.append('upper b forces Idh_B=1, Idh_F=0')
    net=(1-p['tau'])*p['wage']*z; rb=p['r_b']+(p['borrowing_rate_gap'] if b<0 else 0)
    sc={}
    for key,vb in [('B',vbB),('F',vbF)]:
        clamped=max(vb,1e-6); C=clamped**(-1/p['gamma_c']); labor=(clamped*net/p['labor_weight'])**(1/p['phi'])
        sc[key]=net*labor+p['transfer_income']+rb*b-C
    lcB=sc['B'] < -t; lcF=sc['F']>t and not lcB
    db=float(v['b'][1]-v['b'][0]); da=float(v['a'][1]-v['a'][0])
    rb_rate=-((sc['B'] if lcB else 0)+(sB if useB else 0))/db
    rf_rate=((sc['F'] if lcF else 0)+(sF if useF else 0))/db
    shadowB=candidate['BB'] if useB else candidate['FB'] if useF else 0.
    shadowF=candidate['BF'] if useB else candidate['FF'] if useF else 0.
    rah=float(v['effective_illiquid_return'][idx])
    mhB=min(shadowB,0.); mhF=max(shadowF,0.)+rah*a
    if j==19:mhB=shadowB+rah*a;mhF=0.
    selected=dB if useB else dF if useF else 0.
    reconstructed={'transfer':selected,'adjustment_cost':cost(selected),'bb':rb_rate,'bf':rf_rate,'ab':-mhB/da,'af':mhF/da}
    comparisons={name:analysis.c.compare_dense(np.array([value]),np.array([v[name][idx]]),(1,)) for name,value in reconstructed.items()}
    return {'provenance':'source-formula reconstruction from persisted inputs; NOT independent runtime capture',
            'index':list(map(int,idx)),'physical':[b,a,z],'derivatives':{'vbB':vbB,'vbF':vbF,'vaB':vaB,'vaF':vaF},'candidates':operands,
            'dB':float(dB),'dF':float(dF),'costB':cost(dB),'costF':cost(dF),'sdhB':float(sB),'sdhF':float(sF),
            'Idh_B_signed_margin_sdhB_plus_tol':float(sB+t),'Idh_F_signed_margin_sdhF_minus_tol':float(sF-t),
            'scB':float(sc['B']),'scF':float(sc['F']),'Ic_B_signed_margin':float(sc['B']+t),'Ic_F_signed_margin':float(sc['F']-t),
            'reconstructed_transfer_label':int(useF)-int(useB),'persisted_transfer_label':int(v['transfer_label'][idx]),
            'persisted_liquid_label':int(v['liquid_label'][idx]),'boundary_overrides':overrides,
            'consumption_clamp_active_B':vbB<1e-6,'consumption_clamp_active_F':vbF<1e-6,
            'transfer_denominator_clamped':False,'cost_denominator':max(a,p['a_bar']),
            'reconstructed_bb':float(rb_rate),'reconstructed_bf':float(rf_rate),'db':db,'da':da,
            'shadow_transfer_B':float(shadowB),'shadow_transfer_F':float(shadowF),
            'reconstructed_persisted_checks':{name:{k:r[k] for k in ('passed','max_abs','max_scaled')} for name,r in comparisons.items()},
            'persisted':{name:float(v[name][idx]) for name in ('consumption','labor','transfer','adjustment_cost','bb','bf','ab','af','effective_illiquid_return')}}

def trajectory():
    ev=Evidence(); allrows={}; prev=None; first_label=None; first_support=None; split=None
    # Scan actual captured steps. No regenerated states or extra evaluator calls.
    for lang,count in [('matlab',143),('python',500)]:
        rows=[]; prev=None; tail_changes={name:np.zeros((20,20,2),dtype=int) for name in ('liquid_label','transfer_label')}
        for n in range(1,count+1):
            v=ev.load(lang,n); g=generator(v)
            row={'iteration':n,'statistic':float(v['first_iteration_statistic'][0]),'generator':g,
                 'transfer_abs_max':float(np.max(abs(v['transfer']))),'cost_max':float(v['adjustment_cost'].max()),
                 'vb_min':min(float(v[key].min()) for key in ('post_boundary_vb_b','post_boundary_vb_f')),
                 'vb_min_abs':min(float(abs(v[key]).min()) for key in ('post_boundary_vb_b','post_boundary_vb_f')),
                 'clamped_B_count':int(sum((v['post_boundary_vb_b']<1e-6).ravel())),
                 'clamped_F_count':int(sum((v['post_boundary_vb_f']<1e-6).ravel())),
                 'consumed_clamp_count':int(np.count_nonzero(((v['liquid_label']==-1)&(v['post_boundary_vb_b']<1e-6))|((v['liquid_label']==1)&(v['post_boundary_vb_f']<1e-6)))),
                 'liquid_changes':None if prev is None else int(np.count_nonzero(v['liquid_label']!=prev['liquid_label'])),
                 'transfer_changes':None if prev is None else int(np.count_nonzero(v['transfer_label']!=prev['transfer_label']))}
            if lang=='python' and n>=401:
                for name in tail_changes:tail_changes[name]+=(v[name]!=prev[name])
            rows.append(row);prev=v
            if lang=='python' and n<=143 and (first_label is None or first_support is None):
                m=ev.load('matlab',n); indices=np.argwhere(m['transfer_label']!=v['transfer_label'])
                if len(indices) and first_label is None:
                    first_label=n; split={'iteration':n,'count':len(indices),'decisions':[{'matlab':branch(m,idx),'python':branch(v,idx)} for idx in indices]}
                a=analysis.c.canonical_sparse(m['BB']).tocoo(); b=analysis.c.canonical_sparse(v['BB']).tocoo()
                coords=set(zip(a.row,a.col))^set(zip(b.row,b.col))
                if coords and first_support is None:
                    first_support=n
                    support={'iteration':n,'coordinates':[[int(i),int(j)] for i,j in sorted(coords)],
                             'values':[{'row':int(i),'column':int(j),'row_tensor':coord(i),'matlab':float(m['BB'][i,j]),'python':float(v['BB'][i,j])} for i,j in sorted(coords)]}
        allrows[lang]=rows
        if lang=='python':
            write(ROOT/'tail_switch_coordinates.json',{name:[{'coordinate':list(map(int,idx)),'changes':int(arr[tuple(idx)])} for idx in np.argwhere(arr)] for name,arr in tail_changes.items()})
        with (ROOT/f'{lang}_generator_trace.jsonl').open('w',encoding='utf-8') as f:
            for row in rows:f.write(json.dumps(row,allow_nan=False)+'\n')
    write(ROOT/'first_split.json',{'transfer':split,'BB_support':support})
    growth={}
    for lang,rows in allrows.items():
        peak=max(rows,key=lambda r:r['generator']['M_norm_inf']); v=ev.load(lang,peak['iteration'])
        growth[lang]={'iteration':peak['iteration'],'generator':peak['generator'],'norm_row_attribution':branch(v,peak['generator']['norm_row_tensor']),
                      'most_negative_offdiag_attribution':branch(v,coord(peak['generator']['offdiag_min_coordinate'][0]))}
    write(ROOT/'operator_growth.json',growth)
    tail=allrows['python'][400:]; stats=np.array([r['statistic'] for r in tail])
    tail_summary={'iterations':[401,500],'count':len(tail),'statistic':extrema(stats),'first':float(stats[0]),'last':float(stats[-1]),
                  'linear_slope_per_update':float(np.sum((np.arange(100)-49.5)*(stats-stats.mean()))/np.sum((np.arange(100)-49.5)**2)),
                  'increases':int(np.count_nonzero(np.diff(stats)>0)),'decreases':int(np.count_nonzero(np.diff(stats)<0)),
                  'first25_mean':float(stats[:25].mean()),'last25_mean':float(stats[-25:].mean()),
                  'liquid_changes_total':sum(r['liquid_changes'] for r in tail),'transfer_changes_total':sum(r['transfer_changes'] for r in tail),
                  'updates_with_label_changes':sum(r['liquid_changes']+r['transfer_changes']>0 for r in tail),
                  'note':'Counts include transition 400->401. Repeated switching is measured; no limit cycle claim.'}
    for key in ('transfer_abs_max','cost_max','clamped_B_count','clamped_F_count','consumed_clamp_count','vb_min','vb_min_abs'):
        tail_summary[key]={'min':min(r[key] for r in tail),'max':max(r[key] for r in tail)}
    for key in ('M_norm_inf','negative_offdiag_count','nonzero_leak_cells'):
        tail_summary[key]={'min':min(r['generator'][key] for r in tail),'max':max(r['generator'][key] for r in tail)}
    tail_summary['peak_operator_update']=max(tail,key=lambda r:r['generator']['M_norm_inf'])['iteration']
    write(ROOT/'python_tail100.json',tail_summary)
    summary={lang:{'steps':len(rows),'steps_with_negative_offdiag':sum(r['generator']['negative_offdiag_count']>0 for r in rows),
                   'steps_with_outward_leakage':sum(r['generator']['nonzero_leak_cells']>0 for r in rows),
                   'most_negative_offdiag_step':min(rows,key=lambda r:r['generator']['offdiag_min_including_implicit_zero'])['iteration'],
                   'minimum_offdiag':min(r['generator']['offdiag_min_including_implicit_zero'] for r in rows),
                   'minimum_dd_margin':min(r['generator']['M_diagonal_dominance_margin']['min'] for r in rows),
                   'minimum_dd_margin_fsum':min(r['generator']['M_dd_margin_fsum']['min'] for r in rows),
                   'max_outward_rate':max(r['generator']['outward_omitted_rates']['max'] for r in rows)} for lang,rows in allrows.items()}
    write(ROOT/'generator_summary.json',summary); ev.save('consumed_trajectory.json')
    print(json.dumps({'generator':summary,'tail':tail_summary},indent=2))

def replays():
    ev=Evidence(); cases={}; fidelity={}; terminal={}; full={}
    for case,(lang,n,field) in CASES.items():
        values={key:analysis.load(key,ROOT/f'{key}_{case}'/('step_0001.mat' if key=='matlab' else 'step_0001.npz')) for key in ('matlab','python')}
        # Exact common state, independently of the floating stage comparison.
        from scipy.io import loadmat
        state=loadmat(ROOT/f'{case}.mat')
        assert all(np.array_equal(v['old/V0'],state['v0']) for v in values.values())
        pair=analysis.pair(values['matlab'],values['python']); full[case]=pair
        first=pair['first_mismatch']; attrib={}
        if first:
            # Every material dense mismatch keeps operands at a representative physical cell.
            for r in pair['rows']:
                if not r['passed'] and r.get('representative_coordinates') and r['name'] not in ('RHS','first_iteration_statistic') and 'matrix_shape' not in r:
                    idx=r['representative_coordinates'][0]['index_zero_based']
                    if len(idx)==3:attrib[r['name']]={key:branch(v,idx) for key,v in values.items()}
        cases[case]={'passed':pair['passed'],'fields_passed':sum(r['passed'] for r in pair['rows']),'fields_total':len(pair['rows']),
                     'first_mismatch':first,'failed_fields':[r['name'] for r in pair['rows'] if not r['passed']],
                     'max_scaled':max(r.get('max_scaled') or 0 for r in pair['rows']),
                     'V1_max_abs':next(r['max_abs'] for r in pair['rows'] if r['name']=='V1'),'attribution':attrib,
                     'generator':{key:generator(v) for key,v in values.items()},'residuals':pair['residuals']}
        if case!='M143_FINAL':
            check=analysis.pair(ev.load(lang,n),values[lang]); fidelity[case]=check
        else:
            p=read(BINDING)['scalar_binding']['parameters']
            for key,v in values.items():
                old=v['old/V0'].ravel(order='F'); defect=v['utility'].ravel(order='F')+v['A']@old-p['rho']*old
                distance=float(np.max(abs(v['V1']-v['old/V0'])))
                terminal[key]={'update_distance':distance,'source_stop':distance<1e-7,'nonlinear_defect':extrema(defect),
                               'nonlinear_defect_inf':float(max(abs(defect))), 'linear_residual':pair['residuals'][key]}
    verdict='SELECTED_COMMON_STATES_PARITY_PASS__TRAJECTORY_STABILITY_UNRESOLVED' if all(r['passed'] for r in cases.values()) else 'COMMON_STATE_IMPLEMENTATION_OR_NUMERICAL_DIFFERENCE_LOCALIZED'
    if not all(r['passed'] for r in fidelity.values()):verdict='EVIDENCE_INCOMPLETE'
    write(ROOT/'replay_comparisons.json',full);write(ROOT/'replay_fidelity.json',fidelity);write(ROOT/'terminal_state.json',terminal)
    write(ROOT/'replay_summary.json',{'verdict':verdict,'cases':cases,'origin_fidelity_pass':{k:v['passed'] for k,v in fidelity.items()}})
    ev.save('consumed_replays.json')
    print(json.dumps({'verdict':verdict,'cases':{k:{x:v[x] for x in ('passed','fields_passed','failed_fields','V1_max_abs')} for k,v in cases.items()},'terminal':terminal},indent=2))

if __name__=='__main__':
    import sys
    {'trajectory':trajectory,'replays':replays}[sys.argv[1]]()
