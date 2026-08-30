"""Designated MATLAB contaminated-row stationary KFE solve."""

from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from scipy import sparse
from scipy.sparse import linalg

@dataclass(frozen=True)
class MatlabFaithfulKFEResult:
    original_operator: sparse.csr_matrix
    transpose: sparse.csr_matrix
    contaminated_row_index: int
    contaminated_matrix: sparse.csr_matrix
    rhs: np.ndarray
    raw_solve_vector: np.ndarray
    normalization_factor: float
    density_vector: np.ndarray
    density: np.ndarray
    db: float
    da: float
    cell_weight: float
    raw_residual_inf: float

def matlab_contaminated_row_index(state_count: int) -> int:
    if state_count < 3:
        raise ValueError("faithful KFE requires at least three states")
    return int(np.floor(0.37 * state_count)) - 1

def solve_matlab_faithful_stationary_kfe(post_convergence_operator, *, shape, db, da):
    operator=sparse.csr_matrix(post_convergence_operator,dtype=float)
    size=int(np.prod(shape))
    if operator.shape!=(size,size) or len(shape)!=3 or min(shape)<1:
        raise ValueError("operator and faithful (b,a,z) shape are incompatible")
    if not np.isfinite(operator.data).all() or not np.isfinite([db,da]).all() or db<=0 or da<=0:
        raise ValueError("faithful KFE inputs must be finite with positive spacings")
    transpose=operator.transpose().tocsr()
    row=matlab_contaminated_row_index(size)
    contaminated=transpose.tolil(copy=True); contaminated[row,:]=0.0; contaminated[row,row]=1.0; contaminated=contaminated.tocsr()
    rhs=np.zeros(size); rhs[row]=0.007
    raw=np.asarray(linalg.spsolve(contaminated,rhs),dtype=float)
    if not np.isfinite(raw).all(): raise ValueError("faithful contaminated-row solve is non-finite")
    factor=float(np.sum(raw)*db*da)
    if not np.isfinite(factor) or factor==0.0: raise ValueError("faithful density normalization is invalid")
    density=raw/factor
    residual=float(np.linalg.norm(contaminated@raw-rhs,ord=np.inf))
    return MatlabFaithfulKFEResult(operator,transpose,row,contaminated,rhs,raw,factor,density,density.reshape(tuple(shape),order="F"),float(db),float(da),float(db*da),residual)
