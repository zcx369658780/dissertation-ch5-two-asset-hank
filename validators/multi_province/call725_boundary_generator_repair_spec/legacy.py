"""Read-only local legacy expression reconstruction, copied from accepted diagnostic.
Called only for selected witness cells, never a replacement selector or full map.
"""
import numpy as np
from common import analysis,read

def branch(v,idx,binding_path):
    """Reconstruct only listed local arithmetic from persisted derivatives, not HJB."""
    idx=tuple(idx); i,j,k=idx; s=read(binding_path)['scalar_binding']; p=s['parameters']; t=s['numerics']['drift_tolerance']
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
