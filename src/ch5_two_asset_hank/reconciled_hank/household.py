"""V009 HJB using audited D1/D2/D3 only, no historical runner imports."""
from dataclasses import asdict
import hashlib
import warnings
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
from .contracts import grid, pure, SelectorCounter
from .stationary_kfe import stationary_mass

def array_hash(a): return hashlib.sha256(np.asarray(a,dtype="<f8").tobytes(order="F")).hexdigest()
def derivatives(V,g):
    bs=np.diff(V,axis=0)/np.diff(g.b)[:,None,None]
    aa=np.diff(V,axis=1)/np.diff(g.a)[None,:,None]
    pbB=np.concatenate((bs[:1],bs),axis=0);pbF=np.concatenate((bs,bs[-1:]),axis=0)
    paB=np.concatenate((aa[:,:1],aa),axis=1);paF=np.concatenate((aa,aa[:,-1:]),axis=1)
    return pbB,pbF,paB,paF
def local_policy(*,b,a,z,W,ra,rb,T,pbB,pbF,paB,paF,kappa,ledger,budget=None,
                 bmax=2.,amax=5.,cell_id="oracle"):
    s=pure("selector")
    cell=s.CorrectedSelectorCell(cell_id,b,a,z,0.,bmax,0.,amax,z*W,rb,T,ra,
        s.CellDerivatives(pbB,pbF,paB,paF))
    pars=s.CorrectedSelectorParameters(2.,5.,kappa,.1,2.,.1)
    result=s.select_constrained_policy(cell,pars,budget=budget or SelectorCounter(ledger))
    if result.selected is None:
        ledger.event("selector_failure",dict(cell=asdict(cell),outcome=result.outcome,
            candidates=[asdict(c) for c in result.candidates]))
        raise RuntimeError("NO_ADMISSIBLE_POLICY:"+cell_id)
    p=result.selected
    if not (p.admissible and p.q_b_domain_ok and p.closed_face_feasible and p.d2_assembler_admissible):
        raise RuntimeError("POLICY_GATE:"+cell_id)
    return asdict(p)

def map_policy(V,c,i,W,ra,rb,T,ledger):
    ledger.guard();ledger.reserve("mapping")
    g=grid();slopes=derivatives(V,g)
    fields={k:np.empty(g.shape) for k in ("c","l","d","cost","g_b","g_a","utility")}
    branches=[];budget=SelectorCounter(ledger)
    for flat in range(g.size):
        index=np.unravel_index(flat,g.shape,order="F");ib,ia,iz=index
        p=local_policy(b=float(g.b[ib]),a=float(g.a[ia]),z=float(g.z[iz]),W=W,
            ra=ra,rb=rb,T=T,pbB=float(slopes[0][index]),pbF=float(slopes[1][index]),
            paB=float(slopes[2][index]),paF=float(slopes[3][index]),kappa=c["kappa"][i],
            ledger=ledger,budget=budget,cell_id=f"h{ledger.hh}_f{flat}")
        for k in fields:fields[k][index]=p[k]
        branches.append((p["active_constraints"],p["transfer_branch"],p["derivative_branches"]))
    op=pure("generator").assemble_consumed_drift_generator(g,mu_b=fields["g_b"],mu_a=fields["g_a"],
        z_generator=np.array(c["Lambda"]))
    if (op.minimum_offdiagonal<0 or op.max_abs_q_one>op.arithmetic_tolerance or
        op.max_abs_b_coordinate_error>op.arithmetic_tolerance*max(1,float(g.b[-1])) or
        op.max_abs_a_coordinate_error>op.arithmetic_tolerance*max(1,float(g.a[-1]))):
        raise RuntimeError("Q_CONSERVATION_OR_COORDINATES")
    return fields,op,branches

def solve_household(c,i,W,ra,rb,T,ledger,macro,ev):
    identity=ledger.start_household(macro,ev,i);g=grid()
    V=-1/(c["rho"]*(1+g.b[:,None,None]+g.a[None,:,None]+g.z[None,None,:]))
    D=None;history=[];seen=[];checkpoints=[];updates=0
    directory=ledger.root/f"household_{identity:03d}";directory.mkdir(exist_ok=False)
    try:
        for checkpoint in range(101):
            fields,op,branches=map_policy(V,c,i,W,ra,rb,T,ledger)
            vector=V.ravel(order="F");utility=fields["utility"].ravel(order="F")
            B=float(np.max(abs(c["rho"]*vector-utility-op.q@vector)))
            receipt=dict(checkpoint=checkpoint,B=B,D=D,value_hash=array_hash(V),
                q_hash=array_hash(op.q.data),row_sum=op.max_abs_q_one,
                coordinate_b_error=op.max_abs_b_coordinate_error,coordinate_a_error=op.max_abs_a_coordinate_error)
            history.append(receipt);ledger.event(f"h{identity:03d}_checkpoints",receipt)
            state=(receipt["value_hash"],receipt["q_hash"],repr(branches))
            if D is not None and B<=1e-8 and D<=1e-7:
                p,kfe=stationary_mass(op.q,ledger)
                mass=p.reshape(g.shape,order="F")
                top=np.zeros(g.shape,dtype=bool);top[-1,:,:]=True;top[:,-1,:]=True
                out=dict(identity=identity,B=B,D=D,checkpoint=checkpoint,updates=updates,
                    top_mass=float(np.sum(mass[top])),kfe=kfe,
                    A=float(np.sum(mass*g.a[None,:,None])),
                    Basset=float(np.sum(mass*g.b[:,None,None])),
                    C=float(np.sum(mass*fields["c"])),
                    ell=fields["l"],mass=mass,
                    Dasset=float(np.sum(mass*fields["d"])),
                    cost=float(np.sum(mass*fields["cost"])),
                    mean_ga=float(np.sum(mass*fields["g_a"])),
                    mean_gb=float(np.sum(mass*fields["g_b"])),
                    value=V,history=history,policy=fields,Q=op.q)
                np.savez_compressed(directory/"terminal.npz",V=V,p=mass,**fields)
                sparse.save_npz(directory/"Q.npz",op.q)
                return out
            if checkpoint>=100: raise RuntimeError("HJB_NONCONVERGED_100_UPDATES")
            for oldidx,old in enumerate(seen):
                if state==old and checkpoint-oldidx>=2:raise RuntimeError("HJB_EXACT_CYCLE")
            seen.append(state);checkpoints.append(V.copy())
            for period in (2,3):
                if len(checkpoints)>=2*period and all(
                    np.max(abs(checkpoints[-1-k]-checkpoints[-1-k-period]))<=1e-8 for k in range(period)):
                    raise RuntimeError("HJB_APPROXIMATE_CYCLE_"+str(period))
            ledger.guard();ledger.reserve("update")
            matrix=(c["rho"]+.001)*sparse.eye(g.size,format="csr")-op.q
            rhs=utility+.001*vector
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter("always");full=spsolve(matrix,rhs)
            residual=float(np.max(abs(matrix@full-rhs)))
            norm=float(np.max(np.asarray(abs(matrix).sum(axis=1))))
            den=norm*float(np.max(abs(full)))+float(np.max(abs(rhs)))
            error=residual/den if den else residual
            ledger.event(f"h{identity:03d}_direct",dict(checkpoint=checkpoint,
                backward_error=error if np.isfinite(error) else None,
                residual_inf=residual if np.isfinite(residual) else None,
                warning_categories=[type(w.message).__name__ for w in caught],
                finite=bool(np.all(np.isfinite(full)))))
            if caught or not np.all(np.isfinite(full)) or error>1e-12:
                raise RuntimeError("HJB_DIRECT_SOLVE_GATE")
            full=full.reshape(g.shape,order="F")
            attempts=[];accepted=None
            for k in range(53):
                alpha=2.**(-k);trial=full if k==0 else (1-alpha)*V+alpha*full
                bs=np.diff(trial,axis=0)/np.diff(g.b)[:,None,None]
                okay=bool(np.all(np.isfinite(bs)) and np.all(bs>0) and not np.array_equal(trial,V))
                attempts.append(dict(k=k,alpha=alpha,min_b=float(np.min(bs)),accepted=okay,
                    value_hash=array_hash(trial)))
                if okay:accepted=trial;break
            ledger.event(f"h{identity:03d}_updates",dict(checkpoint=checkpoint,
                backward_error=error,full_value_hash=array_hash(full),attempts=attempts))
            if accepted is None:raise RuntimeError("HJB_MONOTONICITY_RELAXATION_EXHAUSTED")
            D=float(np.max(abs(accepted-V)));V=accepted;updates+=1
        raise RuntimeError("HJB_LOOP_EXHAUSTED")
    except Exception as exc:
        np.savez_compressed(directory/"failure_state.npz",V=V)
        ledger.event("household_failures",dict(household=identity,macro=macro,eval=ev,
            origin=i,error=repr(exc),last_checkpoint=history[-1] if history else None))
        raise
