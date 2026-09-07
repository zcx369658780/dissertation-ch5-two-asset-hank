"""Crossed saved solutions and three residual arithmetics; no solver calls."""
from decimal import Decimal, localcontext
import importlib.util
import math
from pathlib import Path
import sys
import numpy as np
from scipy import sparse
from scipy.io import loadmat
from common import REPO,read,write,load_payload,canonical,bits

spec=importlib.util.spec_from_file_location('accepted_compare',REPO/'validators/multi_province/call725_first_iteration_closure/compare.py')
compare=importlib.util.module_from_spec(spec);spec.loader.exec_module(compare)
def dec(x):return Decimal.from_float(float(x))
def ratio(a,b):
    if b==0:return Decimal(0) if a==0 else Decimal('Infinity')
    return a/b
def decimal_residual(M,b,x):
    """80-digit products and sums of exact binary64 conversions, no factorization."""
    M=M.tocsr();out=[];den=[];row_norm=[]
    with localcontext() as ctx:
        ctx.prec=80
        dx=[dec(t) for t in x];db=[dec(t) for t in b]
        for i in range(len(b)):
            begin,end=M.indptr[i:i+2];data=[dec(t) for t in M.data[begin:end]]
            products=[a*dx[int(j)] for a,j in zip(data,M.indices[begin:end])]
            out.append(sum(products,Decimal(0))-db[i])
            den.append(sum((abs(p) for p in products),Decimal(0))+abs(db[i]))
            row_norm.append(sum((abs(a) for a in data),Decimal(0)))
        rnorm=max(abs(t) for t in out);scale=max(row_norm)*max(abs(t) for t in dx)+max(abs(t) for t in db)
        errors=[ratio(abs(r),d) for r,d in zip(out,den)];idx=max(range(len(errors)),key=lambda i:errors[i])
        result={'residual_inf':str(rnorm),'normwise_backward_error':str(ratio(rnorm,scale)),
            'componentwise_backward_error':str(errors[idx]),'componentwise_worst_row':idx,
            'worst_row_residual':str(out[idx]),'worst_row_denominator':str(den[idx]),
            'residual_max_row':max(range(len(out)),key=lambda i:abs(out[i])),
            'matrix_inf_norm':str(max(row_norm)),'precision_decimal_digits':80,
            'exact_binary64_conversion':'Decimal.from_float; products and sum rounded at precision 80'}
    return result,out
def residual(M,b,x):
    M=M.tocsr();ordinary=M@x-b;fsum=np.empty(len(b));den=np.empty(len(b))
    for i in range(len(b)):
        a,z=M.indptr[i:i+2];products=M.data[a:z]*x[M.indices[a:z]]
        fsum[i]=math.fsum([float(p) for p in products]+[-float(b[i])])
        den[i]=math.fsum([abs(float(p)) for p in products]+[abs(float(b[i]))])
    norm=float(np.max(np.asarray(abs(M).sum(axis=1))))
    scale=norm*float(max(abs(x)))+float(max(abs(b)))
    def metric(r):
        with np.errstate(divide='ignore',invalid='ignore'):
            cw=np.divide(abs(r),den,out=np.zeros_like(r),where=den!=0)
        cw[(den==0)&(r!=0)]=np.inf
        numerator=float(max(abs(r)))
        normwise=numerator/scale if scale else (0. if numerator==0 else math.inf)
        def number(v):return float(v) if math.isfinite(v) else str(v)
        return {'residual_inf':number(numerator),'normwise_backward_error':number(normwise),
                'componentwise_backward_error':number(max(cw)),'residual_max_row':int(np.argmax(abs(r))),'componentwise_worst_row':int(np.argmax(cw)),
                'finite_backward_errors':bool(math.isfinite(normwise) and np.isfinite(cw).all())}
    hp,dr=decimal_residual(M,b,x)
    return {'binary64':metric(ordinary),'compensated_rounded_products':metric(fsum),'decimal80':hp,
            'conventions':'binary64 CSR matvec; fsum of already rounded binary64 products plus -rhs is NOT an exact dot product; Decimal80 independent products from exact binary64 conversions'},(ordinary,fsum,dr)
def cmp(a,b):
    result=compare.compare_dense(a,b,(800,))
    for row in result.get('representative_coordinates',[]):
        row['tensor_coordinate_F_order']=list(map(int,np.unravel_index(row['index_zero_based'][0],(20,20,2),order='F')))
    return result
def main(root):
    systems={k:load_payload(v['file']['path']) for k,v in read(root/'systems.json').items()}
    solutions={};loaded_checks={};failures=[];ledger=[]
    for case,(M,b,k) in systems.items():
        for language in ('matlab','python'):
            key=language+'_'+case;out=root/key
            receipt=read(root/f'{key}_process.json');ledger.append(receipt)
            try:
                if language=='matlab':
                    saved=loadmat(out/'loaded_input.mat'); L=saved['M']; lb=saved['rhs'].ravel();x=loadmat(out/'solution.mat')['x']
                    assert x.shape==(800,1);x=x.ravel()
                else:
                    L=sparse.load_npz(out/'loaded_M.npz');lb=np.load(out/'loaded_rhs.npz')['rhs'];x=np.load(out/'solution.npz')['x']
                    assert x.shape==(800,)
                r,c,d,_=canonical(M);lr,lc,ld,_=canonical(L)
                exact=np.array_equal(r,lr) and np.array_equal(c,lc) and np.array_equal(bits(d),bits(ld)) and np.array_equal(bits(b),bits(lb))
                assert exact and x.dtype==np.float64
                loaded_checks[key]={'canonical_data_bits_support_rhs_exact':bool(exact),'finite_x':bool(np.isfinite(x).all()),'receipt':read(out/'loaded_receipt.json')}
                if not np.isfinite(x).all():raise ValueError('nonfinite solution; no retry')
                solutions[key]=x
            except Exception as exc:failures.append({'key':key,'reason':repr(exc)})
    for origin in ('M','P'):
        if (root/f'{origin}_saved.npz').exists():solutions['saved_'+origin]=np.load(root/f'{origin}_saved.npz')['x']
    results={}
    def pair(name,a,b):
        if a in solutions and b in solutions:results[name]={'left':a,'right':b,**cmp(solutions[a],solutions[b])}
    for case in systems:pair('cross_language_'+case,'matlab_'+case,'python_'+case)
    for lang in ('matlab','python'):
        for rep in ('ORIGINAL','ROW_POW2'):pair('origin_effect_'+lang+'_'+rep,lang+'_M_'+rep,lang+'_P_'+rep)
        for origin in ('M','P'):pair('representation_'+lang+'_'+origin,lang+'_'+origin+'_ROW_POW2',lang+'_'+origin+'_ORIGINAL')
    pair('replay_M','matlab_M_ORIGINAL','saved_M');pair('replay_P','python_P_ORIGINAL','saved_P')
    needed=('matlab_M_ORIGINAL','python_M_ORIGINAL','matlab_P_ORIGINAL','python_P_ORIGINAL','saved_M','saved_P')
    attribution={}
    if all(k in solutions for k in needed):
        mm,pm,mp,pp,oldm,oldp=[solutions[k] for k in needed]
        delta=mm-pp;solverM=mm-pm;inputP=pm-pp;inputM=mm-mp;solverP=mp-pp
        vectors={'delta':delta,'fixed_M_solver_effect':solverM,'python_input_effect':inputP,'matlab_input_effect':inputM,'fixed_P_solver_effect':solverP,
                 'sum_decomposition_1':solverM+inputP,'sum_decomposition_2':inputM+solverP,'prior_split':oldm-oldp}
        np.savez(root/'attribution_vectors.npz',**vectors)
        attribution={'norm_inf':{k:float(max(abs(v))) for k,v in vectors.items()},
            'identity_1':cmp(delta,vectors['sum_decomposition_1']),'identity_2':cmp(delta,vectors['sum_decomposition_2']),
            'prior_split_replay':cmp(delta,vectors['prior_split']),
            'note':'Vector identities, not additive norms or causal percentages; full vectors retained.'}
    diagnostics={}
    for key,x in solutions.items():
        targets=[t for t in ('M_ORIGINAL','P_ORIGINAL') if t in systems]
        case=key.split('_',1)[1]
        if case.endswith('ROW_POW2'):targets.append(case)
        diagnostics[key]={}
        for target in targets:
            M,b,_=systems[target];metrics,arrays=residual(M,b,x);diagnostics[key][target]=metrics
            r,fs,dr=arrays
            np.savez(root/f'residual_{key}_against_{target}.npz',binary64=r,fsum=fs)
            write(root/f'residual80_{key}_against_{target}.json',[str(t) for t in dr])
    binding=read(root/'binding.json')['scalar_binding'];rho=binding['parameters']['rho'];delta=binding['numerics']['delta']
    representation={}
    for origin in ('M','P'):
        if origin+'_ORIGINAL' not in systems:continue
        M,b,_=systems[origin+'_ORIGINAL'];A=sparse.load_npz(root/f'{origin}_A.npz').tocsr();diag=M.diagonal();ad=A.diagonal()
        rows=np.argsort(abs(diag))[::-1][:8];details=[]
        with localcontext() as ctx:
            ctx.prec=80;sigma=dec(rho)+Decimal(1)/dec(delta);sigma64=float(rho)+1/float(delta)
            for i0 in rows:
                i=int(i0);a,z=A.indptr[i:i+2];m,n=M.indptr[i:i+2]
                details.append({'row':i,'tensor_coordinate':list(map(int,np.unravel_index(i,(20,20,2),order='F'))),
                    'M_ii':float(diag[i]),'A_ii':float(ad[i]),'spacing_abs_Mii':float(abs(np.spacing(diag[i]))),
                    'sum_binary64':float(diag[i]+ad[i]),'sum_fsum':math.fsum([float(diag[i]),float(ad[i])]),'sum_decimal80':str(dec(diag[i])+dec(ad[i])),
                    'sigma_exact_operands_decimal80':str(sigma),'sigma_binary64':sigma64,
                    'sigma_loss_decimal80':str(dec(diag[i])+dec(ad[i])-sigma),
                    'A_rowsum_binary64':float(A.getrow(i).sum()),'A_rowsum_fsum':math.fsum(A.data[a:z]),
                    'A_rowsum_decimal80':str(sum((dec(t) for t in A.data[a:z]),Decimal(0))),
                    'M_rowsum_decimal80':str(sum((dec(t) for t in M.data[m:n]),Decimal(0)))})
            representation[origin]={'sigma_binary64':sigma64,'sigma_decimal80':str(sigma),'diagonal_rows_where_M_plus_A_is_exactly_zero':int(sum(diag+ad==0)),
                'extreme_diagonals':details,'interpretation_boundary':'Stored A/M only; no operator regeneration. Algebraic row scaling cannot restore a missing diagonal shift.'}
    write(root/'comparisons.json',results);write(root/'attribution.json',attribution);write(root/'residuals.json',diagnostics)
    write(root/'representation.json',representation);write(root/'loaded_input_checks.json',loaded_checks);write(root/'execution_failures.json',failures)
    write(root/'call_ledger.json',{'attempts':[{k:r[k] for k in ('language','case','process_attempts','status','elapsed_seconds','worker_ledger')} for r in ledger],
        'totals':{lang:{'process_attempts':sum(r['process_attempts'] for r in ledger if r['language']==lang),
                      **{k:sum((r['worker_ledger'] or {}).get(k,0) for r in ledger if r['language']==lang) for k in ('invocations_entered','solves_entered','solves_completed','durable_outputs')}} for lang in ('matlab','python')},
        'scientific_retries':0,'HJB_policy':0,'full_trajectory':0,'KFE':0,'GE_annual':0,'dynamics_IRF':0,'Results':0,'extra_solve_or_condition_estimator':0})
    complete=len(solutions)==10 and not failures and not read(root/'ineligible.json')
    write(root/'result.json',{'completion':'FROZEN_LINEAR_SYSTEM_ATTRIBUTION_COMPLETE__TRAJECTORY_AND_GENERATOR_BLOCKERS_OPEN' if complete else 'EVIDENCE_INCOMPLETE',
        'comparisons':{name:{k:r[k] for k in ('passed','exact_equal','max_abs','max_scaled','material_mismatch_count')} for name,r in results.items()},
        'new_linear_solves':read(root/'call_ledger.json')['totals'],'HJB_calls':0,'trajectory_and_generator_blockers':'remain open','results_eligibility':False})
    print(read(root/'result.json'))
if __name__=='__main__':main(Path(sys.argv[1]))
