"""One enumerated frozen-system solve; exact loaded-input validation precedes it."""
import importlib.util
import json
import sys
import time
import warnings
from pathlib import Path
import numpy as np
import scipy
from scipy import sparse
from scipy.sparse import linalg
from common import load_payload, write, sha

def main(payload,output):
    output.mkdir(exist_ok=False)
    ledger={'invocations_entered':1,'solves_entered':0,'solves_completed':0,'durable_outputs':0,'status':'LOADING'}
    def persist():write(output/'ledger.json',ledger)
    persist()
    try:
        M,b,k=load_payload(payload)
        sparse.save_npz(output/'loaded_M.npz',M);np.savez(output/'loaded_rhs.npz',rhs=b,k=k)
        write(output/'loaded_receipt.json',{'exact_payload_bits_and_support':True,'payload_sha256':sha(payload),'format':M.format,
            'dtype':str(M.dtype),'shape':list(M.shape),'rhs_shape':list(b.shape),'rhs_association':'column vector in F-order state indexing',
            'python':sys.version,'scipy':scipy.__version__,'numpy':np.__version__,
            'scikits_umfpack_available':bool(importlib.util.find_spec('scikits') and importlib.util.find_spec('scikits.umfpack')),
            'solver_entrypoint':'scipy.sparse.linalg.spsolve; no option overrides',
            'backend_observation':'Availability and installed SciPy source retained; backend path inferred only if necessary; no diagnostic solve.'})
        ledger['status']='SOLVING';ledger['solves_entered']=1;persist();started=time.monotonic()
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            x=linalg.spsolve(M,b)
        # Save core before residuals or warning formatting.
        np.savez(output/'solution.npz',x=x)
        ledger['solves_completed']=1;ledger['durable_outputs']=1;ledger['solve_seconds']=time.monotonic()-started
        ledger['status']='COMPLETE';ledger['finite']=bool(np.isfinite(x).all());persist()
        write(output/'warnings.json',[{'category':w.category.__name__,'message':str(w.message)} for w in caught])
    except BaseException as exc:
        ledger['status']='FAILED';ledger['error']=repr(exc);persist();raise
if __name__=='__main__':main(Path(sys.argv[1]),Path(sys.argv[2]))
