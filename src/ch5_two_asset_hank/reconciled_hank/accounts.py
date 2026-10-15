"""State CES integration, fixed-S capital funding and national cash accounts."""
import numpy as np

def positive_prices(c,w,*,wage_role="gross",units=("MU_10WAN_YUAN","NU_100_PERSONS","MODEL_TIME_SYNTHETIC")):
    if wage_role!="gross" or units!=("MU_10WAN_YUAN","NU_100_PERSONS","MODEL_TIME_SYNTHETIC"):
        raise ValueError("gross wages in frozen units required; no second tax")
    w=np.asarray(w,float)
    if w.shape!=(c["n"],) or np.any(w<=0) or not np.all(np.isfinite(w)):
        raise ValueError("positive gross wage axis")
    if c["phi"] is None:raise ValueError("FROZEN_CES_PHI_NOT_SPECIFIED")
    phi=np.asarray(c["phi"],float);n=c["n"]
    if phi.shape!=(n,n) or not np.all(np.isfinite(phi)) or np.any(phi<=0):
        raise ValueError("positive destination-origin phi required")
    if not 0<=c["tau"]<1 or c["eta"]<=0:raise ValueError("tax/curvature")
    v=(1-c["tau"])*w
    eta=c["eta"]
    W=np.sum(phi**(-1/eta)*v[:,None]**(1+1/eta),axis=0)**(eta/(1+eta))
    return v,phi,W
def labor(c,w,ell,mu,z):
    v,phi,W=positive_prices(c,w);n=c["n"];eta=c["eta"]
    if len(ell)!=n or len(mu)!=n:raise ValueError("origin mismatch")
    flows=np.zeros((n,n));controls=[]
    for i in range(n):
        mass=np.asarray(mu[i]).ravel(order="F");l=np.asarray(ell[i]).ravel(order="F")
        zz=np.asarray(z)
        zz=np.broadcast_to(zz,np.asarray(ell[i]).shape).ravel(order="F")
        if (mass.shape!=l.shape or abs(np.sum(mass)-1)>1e-12 or np.any(mass<0) or
            np.any(l<0) or not np.all(np.isfinite(mass+l+zz))):
            raise ValueError("invalid household mass/labor")
        h=l[None,:]*phi[:,i,None]**(-1/eta)*(v[:,None]/W[i])**(1/eta)
        controls.append(h)
        flows[:,i]=c["N"][i]*np.sum(h*(mass*zz)[None,:],axis=1)
    return W,controls,np.sum(flows,axis=1)
def capital_flows(S,A,r,D,delta):
    S=np.asarray(S,float);A=np.asarray(A,float);r=np.asarray(r,float);D=np.asarray(D,float)
    n=len(A)
    if (S.shape!=(n,n) or r.shape!=(n,) or D.shape!=(n,) or np.any(S<0) or
        not np.all(np.isfinite(S)) or not np.all(np.isfinite(A+r+D)) or
        np.any(A<0) or np.any(r+delta<=0) or np.max(abs(np.sum(S,axis=0)-1))>1e-12):
        raise ValueError("capital units/axes/ownership/column conservation")
    K=S@A;rah=S.T@r;allocated_D=S@D
    R=np.sum(S*A[None,:]*(rah[None,:]-r[:,None]),axis=1)
    dotK=S@(rah*A+D);I=dotK+delta*K
    financing=(r+delta)*K+allocated_D+R
    scale=max(1.,float(np.sum(abs(I))))
    if np.max(abs(I-financing))>1e-12*scale or abs(np.sum(R))>1e-12*scale:
        raise ValueError("capital fund identity")
    return dict(Kprivate=K,rah=rah,R=R,dotK=dotK,Iprivate=I,
        allocated_D=allocated_D,financing=financing,
        national_capital_error=float(np.sum(K)-np.sum(A)))
def check_funding(f,claimed):
    if np.max(abs(np.asarray(claimed)-f["financing"]))>1e-12*max(1.,float(np.sum(abs(f["financing"])))):
        raise ValueError("local funding mismatch; missing R")
    return True
def fiscal_accounts(c,w,L,r,rb,T,maintenance=None):
    N=np.asarray(c["N"]);Kg=np.asarray(c["Kg"]);r=np.asarray(r)
    wages=np.asarray(w)*np.asarray(L)
    gross=float(np.sum((r+c["delta"])*Kg))
    upkeep=float(c["delta"]*np.sum(Kg))
    if maintenance is not None and abs(maintenance-upkeep)>1e-12:
        raise ValueError("public depreciation charged twice")
    taxes=float(c["tau"]*np.sum(wages));interest=rb*c["Bg"];transfers=T*float(np.sum(N))
    budget=taxes+gross-upkeep-c["G"]-interest-transfers
    return dict(wage_tax=taxes,public_gross=gross,public_maintenance=upkeep,
        government_purchases=c["G"],debt_interest=interest,transfer=transfers,budget=budget)
def aggregate(c,x,households):
    n=c["n"];x=np.asarray(x,float);w=np.exp(x[:n]);r=x[n:2*n];rb,T=x[-2:]
    N=np.asarray(c["N"]);A=N*np.array([h["A"] for h in households])
    B=N*np.array([h["Basset"] for h in households]);D=N*np.array([h["Dasset"] for h in households])
    f=capital_flows(c["S"],A,r,D,c["delta"])
    W,_,L=labor(c,w,[h["ell"] for h in households],[h["mass"] for h in households],
        np.array(c["z"])[None,None,:])
    K=f["Kprivate"]+np.array(c["Kg"])
    if np.any(K<=0) or np.any(L<=0):raise RuntimeError("NONPOSITIVE_PRODUCTION")
    Y=np.array(c["Z"])*K**c["alpha"]*L**(1-c["alpha"])
    wd=(1-c["alpha"])*Y/L;rd=c["alpha"]*Y/K-c["delta"]
    C=float(N@np.array([h["C"] for h in households]))
    cost=float(N@np.array([h["cost"] for h in households]))
    fiscal=fiscal_accounts(c,w,L,r,rb,T)
    scale=max(1.,float(np.sum(Y)))
    raw=np.concatenate((w-wd,r-rd,[np.sum(B)-c["Bg"],fiscal["budget"]]))
    denominators=np.concatenate((np.maximum(1,abs(w)),np.maximum(1,abs(r)),
        [max(1.,c["Bg"]),scale]))
    goods=float(np.sum(Y)-C-c["G"]-c["delta"]*np.sum(K)-cost)
    hp=float(N@np.array([h["mean_ga"] for h in households]))
    hb=float(N@np.array([h["mean_gb"] for h in households]))
    # Independently use original HH cash flows and actual bond holdings.
    hh_identity=C+cost-float((1-c["tau"])*(w@L)+rb*np.sum(B)+f["rah"]@A+T*np.sum(N)-hp-hb)
    capital_cash=f["Iprivate"]-f["financing"]
    accounting=np.concatenate(([goods/scale,fiscal["budget"]/scale,hh_identity/scale,
        np.sum(f["R"])/scale,f["national_capital_error"]/scale],capital_cash/scale))
    return dict(x=x.tolist(),w=w.tolist(),r=r.tolist(),rb=float(rb),T=float(T),W=W.tolist(),
        A=A.tolist(),B=B.tolist(),K=K.tolist(),L=L.tolist(),Y=Y.tolist(),C=C,cost=cost,
        D=D.tolist(),R=f["R"].tolist(),Iprivate=f["Iprivate"].tolist(),
        financing=f["financing"].tolist(),fiscal=fiscal,
        raw_residuals=raw.tolist(),residuals=(raw/denominators).tolist(),
        goods_raw=goods,accounting=accounting.tolist())
