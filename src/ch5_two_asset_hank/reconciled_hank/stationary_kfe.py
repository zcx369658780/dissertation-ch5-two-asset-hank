"""Exact-positive unique closed class, one restricted GESVD, no pinning."""
import math
import warnings
import numpy as np
from scipy import sparse,linalg
from scipy.sparse.csgraph import connected_components
def gamma(k):
    x=k*np.finfo(float).eps
    return x/(1-x)
def stationary_mass(Q,ledger,toy=False):
    Q=sparse.csr_matrix(Q);N=Q.shape[0]
    if Q.shape!=(N,N) or N<2 or not np.all(np.isfinite(Q.data)):
        raise RuntimeError("KFE_SHAPE_FINITE")
    if not toy and N!=800:
        raise RuntimeError("ONLY_FROZEN_800_STATE_TERMINAL_KFE")
    off=Q-sparse.diags(Q.diagonal());off.eliminate_zeros()
    rownorm=float(np.max(np.asarray(abs(Q).sum(axis=1))))
    terms=max(1,int(np.max(np.diff(Q.indptr))))
    qbound=gamma(terms)*max(1.,rownorm)
    qone=np.asarray(Q@np.ones(N)).ravel()
    if (off.nnz and np.min(off.data)<0) or np.max(abs(qone))>qbound:
        raise RuntimeError("KFE_Q_INVALID")
    ledger.guard();ledger.reserve("toy_scc" if toy else "scc")
    adjacency=off.copy();adjacency.data=(adjacency.data>0).astype(float);adjacency.eliminate_zeros()
    count,labels=connected_components(adjacency,directed=True,connection="strong")
    closed=[]
    for label in range(count):
        members=np.flatnonzero(labels==label);out=off[members][:,labels!=label]
        if out.nnz==0:closed.append(members)
    if len(closed)!=1:raise RuntimeError("KFE_CLOSED_CLASS_COUNT:"+str(len(closed)))
    C=closed[0];m=len(C)
    if m<2:raise RuntimeError("KFE_DEGENERATE_SINGLETON")
    block=Q[C][:,C]
    if np.max(abs(np.asarray(block@np.ones(m)).ravel()))>qbound:
        raise RuntimeError("KFE_CLOSED_BLOCK_CONSERVATION")
    ledger.guard();ledger.reserve("toy_svd" if toy else "svd")
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        _,s,vh=linalg.svd(block.T.toarray(),full_matrices=True,lapack_driver="gesvd",check_finite=True)
    if caught:raise RuntimeError("KFE_SVD_WARNING")
    thresholds=[gamma(m+64)*max(1.,float(s[0])),gamma(N+64)*max(1.,float(s[0]))]
    if any(np.count_nonzero(s>t)!=m-1 for t in thresholds):
        raise RuntimeError("KFE_RANK_NULLITY")
    v=vh[-1].copy();total=math.fsum(v)
    if abs(total)<=gamma(m)*max(1.,math.fsum(abs(v))):raise RuntimeError("KFE_ORIENTATION")
    if total<0:v=-v
    v=v/math.fsum(v)
    if not np.all(np.isfinite(v)) or np.any(v<=0):raise RuntimeError("KFE_NONPOSITIVE_CLOSED_MASS")
    p=np.zeros(N);p[C]=v
    ledger.reserve("toy_full_qtp" if toy else "full_qtp")
    r=np.asarray(Q.T@p).ravel()
    scale=max(1.,float(np.max(np.asarray(abs(Q.T).sum(axis=1))))*float(np.max(abs(p))))
    bound=gamma(N+64)*scale
    norm=abs(math.fsum(p)-1)
    source=abs(math.fsum(r)-float(qone@p))
    source_bound=gamma(N+64)*max(1.,N*scale)
    if np.max(abs(r))>bound or norm>gamma(N)*max(1.,math.fsum(abs(p))) or source>source_bound:
        raise RuntimeError("KFE_FULL_Q_VALIDATION")
    return p,dict(closed_count=1,closed_size=m,transient_size=N-m,rank=m-1,nullity=1,
        stationarity=float(np.max(abs(r))),stationarity_bound=bound,normalization=norm,
        minimum=float(np.min(p)),row_sum=float(np.max(abs(qone))),rank_thresholds=thresholds,
        source_discrepancy=source,full_qtp_count=1,restricted_svd_count=1)
