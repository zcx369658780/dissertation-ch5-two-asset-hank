"""Saved coordinate actions, budget arithmetic, boundary feasibility, local witnesses.

No real-state policy search, evaluator, solver, or new operator assembly.
"""
import csv
from decimal import Decimal,localcontext
import json
import math
from pathlib import Path
import sys
import numpy as np
from common import Evidence,analysis,read,write
from legacy import branch

def vec(x):return np.asarray(x).ravel(order='F')
def coord(i):return tuple(map(int,np.unravel_index(int(i),(20,20,2),order='F')))
def faces(i,j):
    return '+'.join(([ 'lower_b'] if i==0 else ['upper_b'] if i==19 else [])+(['lower_a'] if j==0 else ['upper_a'] if j==19 else [])) or 'interior'
def materially_different(x,y):return abs(x-y)>128*np.finfo(float).eps*np.maximum(1,np.maximum(abs(x),abs(y)))
def face_incompatibility(b,a,mu_b,mu_a):
    out=np.zeros((20,20,2));bflag=np.zeros_like(out,dtype=bool);aflag=bflag.copy()
    bflag[0]=mu_b[0]<0;bflag[-1]=mu_b[-1]>0
    aflag[:,0]=mu_a[:,0]<0;aflag[:,-1]=mu_a[:,-1]>0
    out[0]=np.maximum(-mu_b[0],0);out[-1]=np.maximum(mu_b[-1],0)
    out[:,0]=np.maximum(out[:,0],np.maximum(-mu_a[:,0],0));out[:,-1]=np.maximum(out[:,-1],np.maximum(mu_a[:,-1],0))
    return bflag,aflag,out
def reductions(A,x):
    A=A.tocsr();action=A@x;centered=np.empty(800);sums=np.empty(800)
    for i in range(800):
        start,end=A.indptr[i:i+2];d=A.data[start:end];cols=A.indices[start:end]
        sums[i]=math.fsum(d);centered[i]=math.fsum(float(q)*(float(x[j])-float(x[i])) for j,q in zip(cols,d))
    return action,centered,sums
def decimal_row(A,row,xb,xa):
    A=A.tocsr();p,q=A.indptr[row:row+2];entries=list(zip(A.indices[p:q],A.data[p:q]))
    with localcontext() as ctx:
        ctx.prec=80;D=lambda x:Decimal.from_float(float(x))
        result={'row_sum':str(sum((D(v) for _,v in entries),Decimal(0))),'precision':80}
        for name,x in [('b',xb),('a',xa)]:
            result[name+'_action']=str(sum((D(v)*D(x[j]) for j,v in entries),Decimal(0)))
            result[name+'_centered']=str(sum((D(v)*(D(x[j])-D(x[row])) for j,v in entries),Decimal(0)))
    return result
def snapshot(v,p):
    b,a,z=np.meshgrid(v['b'],v['a'],v['z'],indexing='ij');w=(1-p['tau'])*p['wage']*z
    rb=p['r_b']+p['borrowing_rate_gap']*(b<0)
    cash=w*v['labor']+rb*b+p['transfer_income']-v['consumption']
    transfer_cash=-v['transfer']-v['adjustment_cost']
    budget_b=cash+transfer_cash;budget_a=v['transfer']+v['effective_illiquid_return']*a
    A=v['A'].tocsr();xb=vec(b);xa=vec(a)
    ob,cb,rs=reductions(A,xb);oa,ca,_=reductions(A,xa)
    leak_parts={key:np.zeros_like(b) for key in ('lower_b','upper_b','lower_a','upper_a')}
    leak_parts['lower_b'][0]=v['bb'][0];leak_parts['upper_b'][-1]=v['bf'][-1]
    leak_parts['lower_a'][:,0]=v['ab'][:,0];leak_parts['upper_a'][:,-1]=v['af'][:,-1]
    leak=sum(leak_parts.values());db=v['b'][1]-v['b'][0];da=v['a'][1]-v['a'][0]
    proxy_b=db*(v['bf']-v['bb']);proxy_a=da*(v['af']-v['ab'])
    outward_b=db*(leak_parts['upper_b']-leak_parts['lower_b']);outward_a=da*(leak_parts['upper_a']-leak_parts['lower_a'])
    result={k:vec(x) for k,x in {'b':b,'a':a,'budget_b':budget_b,'budget_a':budget_a,'captured_b':v['mu_b'],'captured_a':v['mu_a'],
        'cash_channel':cash,'transfer_cash_channel':transfer_cash,'leak':leak,'proxy_b':proxy_b,'proxy_a':proxy_a,
        'outward_b':outward_b,'outward_a':outward_a,**{'leak_'+k:x for k,x in leak_parts.items()}}.items()}
    result.update(operator_b=ob,operator_a=oa,centered_b=cb,centered_a=ca,row_sum=rs)
    for axis in ('b','a'):
        # Exact telescoping decomposition of different objects; not an operator repair.
        result['channel_gap_'+axis]=result['proxy_'+axis]-result['budget_'+axis]
        result['spacing_rounding_'+axis]=result['centered_'+axis]-(result['proxy_'+axis]-result['outward_'+axis])
        result['row_sum_term_'+axis]=result[axis]*rs
        result['decomposition_residual_'+axis]=(result['operator_'+axis]-result['budget_'+axis])-(result['channel_gap_'+axis]-result['outward_'+axis]+result['spacing_rounding_'+axis]+result['row_sum_term_'+axis])
    bbad,abad,violation=face_incompatibility(b,a,budget_b,budget_a)
    result.update(infeasible_b=vec(bbad),infeasible_a=vec(abad),outward_budget_violation=vec(violation))
    coo=A.tocoo();neg=(coo.row!=coo.col)&(coo.data<0);nr=np.zeros(800,dtype=bool);nr[coo.row[neg]]=True
    result['negative_row']=nr
    for axis in ('b','a'):
        result['material_operator_'+axis]=materially_different(result['operator_'+axis],result['captured_'+axis])
        result['material_budget_'+axis]=materially_different(result['budget_'+axis],result['captured_'+axis])
    return result
def main(root):
    ev=Evidence();binding=Path(read(root/'binding_identity.json')['path']);ev.verify(binding);p=read(binding)['scalar_binding']['parameters']
    snapshot_rows=read(root/'snapshots.json');summary=[];corners=[];face_rows=[];witnesses={};tables=[];failures=[]
    for info in snapshot_rows:
        if not info['eligible']:failures.append(info);continue
        try:v=ev.load(info['language'],Path(info['path']))
        except Exception as exc:failures.append({'snapshot':info['id'],'error':repr(exc)});continue
        key=info['id'];r=snapshot(v,p);A=v['A'].tocsr()
        comparisons={}
        for axis in ('b','a'):
            for lhs,rhs in [('budget','captured'),('operator','captured'),('proxy','budget')]:
                comparisons[lhs+'_'+rhs+'_'+axis]=analysis.c.compare_dense(r[lhs+'_'+axis],r[rhs+'_'+axis],(800,))
        coo=A.tocoo();off=coo.row!=coo.col;negative=off&(coo.data<0)
        material_infeasible=materially_different(r['outward_budget_violation'],np.zeros(800))
        summary.append({'snapshot':key,'negative_entries':int(sum(negative)),'negative_rows':int(sum(r['negative_row'])),
            'omitted_rows':int(np.count_nonzero(r['leak'])),'infeasible_budget_rows_exact':int(sum(r['outward_budget_violation']>0)),
            'infeasible_budget_rows_material':int(sum(material_infeasible)),'max_outward_budget':float(max(r['outward_budget_violation'])),
            'comparison':comparisons,'minimum_offdiag':float(min(coo.data[off])),'minimum_offdiag_coordinate':[int(coo.row[off][np.argmin(coo.data[off])]),int(coo.col[off][np.argmin(coo.data[off])])],
            'row_sum_plus_omitted_max_abs':float(max(abs(r['row_sum']+r['leak'])))})
        flags=r['negative_row']|(r['leak']!=0)|r['material_operator_b']|r['material_operator_a']|r['material_budget_b']|r['material_budget_a']|material_infeasible
        selected={int(np.ravel_multi_index((i,j,k),(20,20,2),order='F')) for i in (0,19) for j in (0,19) for k in (0,1)}
        selected.update([704,int(np.ravel_multi_index((10,19,1),(20,20,2),order='F')),int(np.ravel_multi_index((18,19,0),(20,20,2),order='F'))])
        selected.add(summary[-1]['minimum_offdiag_coordinate'][0]);selected.add(int(np.argmax(abs(r['leak']))))
        for axis in ('b','a'):
            selected.add(int(np.argmax(abs(r['operator_'+axis]-r['budget_'+axis]))));selected.add(int(np.argmax(abs(r['channel_gap_'+axis]))))
        witnesses[key]=[]
        for row in range(800):
            i,j,k=coord(row);atcorner=i in (0,19) and j in (0,19)
            if flags[row] or atcorner or row in selected:
                idx=(i,j,k);start,end=A.indptr[row:row+2]
                record={'snapshot':key,'row':row,'i_b':i,'i_a':j,'i_z':k,'face':faces(i,j),'corner':int(atcorner),
                    **{name:float(r[name][row]) for name in r},
                    **{name:float(v[name][idx]) for name in ('consumption','labor','transfer','adjustment_cost','effective_illiquid_return','liquid_label','transfer_label','bb','bf','ab','af','post_boundary_vb_b','post_boundary_vb_f','va_b','va_f')},
                    'neighbors_and_signed_A':' '.join(f'{int(col)}:{float(val):.17g}' for col,val in zip(A.indices[start:end],A.data[start:end])),
                    'provenance':'stored controls/rates/derivatives; budget and A actions reconstructed; see source_map.json'}
                if flags[row]:tables.append(record)
                if atcorner:corners.append({name:record[name] for name in ('snapshot','row','i_b','i_a','i_z','face','budget_b','budget_a','captured_b','captured_a','operator_b','operator_a','negative_row','leak','outward_budget_violation','consumption','labor','transfer')})
                if row in selected:
                    local=branch(v,idx,binding)
                    witnesses[key].append({'row':record,'legacy_reconstruction':local,'decimal80_stored_row':decimal_row(A,row,r['b'],r['a'])})
        for face,axis,index in [('lower_b','b',0),('upper_b','b',19),('lower_a','a',0),('upper_a','a',19)]:
            for z in (0,1):
                ids=[row for row in range(800) if coord(row)[2]==z and coord(row)[0 if axis=='b' else 1]==index]
                budgets=r['budget_'+axis][ids];bad=-budgets if index==0 else budgets
                face_rows.append({'snapshot':key,'face':face,'z_index':z,'cells':len(ids),'budget_min':float(min(budgets)),'budget_max':float(max(budgets)),
                    'outward_exact':int(sum(bad>0)),'outward_material':int(sum(materially_different(np.maximum(bad,0),np.zeros(len(ids))))),
                    'negative_rows':int(sum(r['negative_row'][ids])),'omitted_rows':int(np.count_nonzero(r['leak'][ids]))})
        np.savez(root/f'{key}_drifts.npz',**r)
    def csvwrite(name,rows):
        if rows:
            with (root/name).open('w',newline='',encoding='utf-8') as f:
                writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    csvwrite('anomalous_rows.csv',tables);csvwrite('corners.csv',corners);csvwrite('face_feasibility.csv',face_rows)
    write(root/'snapshot_summary.json',summary);write(root/'witnesses.json',witnesses);write(root/'failures.json',failures)
    old=read(root/'consumed_inputs.json');used={x['path']:x for x in old['consumed_entries']};used.update(ev.used);old['consumed_entries']=list(used.values());write(root/'consumed_inputs.json',old)
    result={'completion':'BOUNDARY_GENERATOR_REPAIR_SPEC_COMPLETE__SCIENTIFIC_DECISIONS_EXPLICIT__NO_MODEL_RUN' if len(summary)==14 and not failures else 'EVIDENCE_INCOMPLETE',
        'snapshots':len(summary),'anomaly_rows':len(tables),'corner_rows':len(corners),'face_rows':len(face_rows),
        'summary':[{'snapshot':x['snapshot'],'negative_entries':x['negative_entries'],'omitted_rows':x['omitted_rows'],'infeasible_budget_rows_material':x['infeasible_budget_rows_material'],
            'budget_capture_b_material':x['comparison']['budget_captured_b']['material_mismatch_count'],'budget_capture_a_material':x['comparison']['budget_captured_a']['material_mismatch_count'],
            'operator_capture_b_material':x['comparison']['operator_captured_b']['material_mismatch_count'],'operator_capture_a_material':x['comparison']['operator_captured_a']['material_mismatch_count']} for x in summary]}
    write(root/'result.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':main(Path(sys.argv[1]))
