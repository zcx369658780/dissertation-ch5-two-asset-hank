import importlib
import numpy as np
from scipy import sparse
from scipy.sparse import linalg
from ch5_two_asset_hank.matlab_faithful_kfe import matlab_contaminated_row_index,solve_matlab_faithful_stationary_kfe

def test_matlab_index_mapping():
    assert matlab_contaminated_row_index(50)==17

def test_contamination_rhs_direct_solve_normalization_and_reshape():
    # A source-like conservative operator whose transpose becomes nonsingular after pinning.
    A=sparse.csr_matrix([[-1,1,0],[1,-2,1],[0,1,-1]],dtype=float)
    r=solve_matlab_faithful_stationary_kfe(A,shape=(3,1,1),db=.25,da=.5)
    expected=A.T.tolil(); expected[0,:]=0; expected[0,0]=1; expected=expected.tocsr()
    assert r.contaminated_row_index==0
    assert np.array_equal(r.contaminated_matrix.toarray()[0],np.array([1.,0.,0.]))
    assert np.array_equal(r.contaminated_matrix.toarray()[1:],A.T.toarray()[1:])
    assert np.count_nonzero(r.rhs)==1 and r.rhs[0]==.007
    assert np.allclose(r.raw_solve_vector,linalg.spsolve(expected,r.rhs),rtol=0,atol=0)
    assert np.isclose(np.sum(r.density_vector)*r.db*r.da,1.0,rtol=0,atol=8*np.finfo(float).eps)
    assert r.cell_weight==r.db*r.da
    assert np.array_equal(r.density.ravel(order='F'),r.density_vector)

def test_clean_kfe_and_faithful_hjb_imports_remain_available():
    importlib.import_module('ch5_two_asset_hank.kfe')
    importlib.import_module('ch5_two_asset_hank.matlab_faithful_hjb')
