"""Observation primitives; no model imports or import-time execution."""
from dataclasses import fields, is_dataclass
import hashlib
import json
import math
from pathlib import Path
import time
from collections.abc import Mapping
import numpy as np
from scipy import sparse


class PrefixLimit(RuntimeError): pass
class ObservationTimeout(RuntimeError): pass


def encode(value, arrays, key='root'):
    if sparse.issparse(value):
        # Preserve format/support order; do not canonicalize a scientific argument.
        matrix=value.copy()
        for name in ('data','indices','indptr'):
            arrays[key+'_'+name]=getattr(matrix,name).copy()
        return {'sparse_format':matrix.format,'shape':list(matrix.shape),'array_prefix':key}
    if isinstance(value,np.ndarray):
        arrays[key]=value.copy()
        return {'array':key,'shape':list(value.shape),'dtype':str(value.dtype)}
    if is_dataclass(value):
        return {f.name:encode(getattr(value,f.name),arrays,key+'_'+f.name) for f in fields(value)}
    if isinstance(value,Mapping):
        return {str(k):encode(v,arrays,key+'_'+str(k)) for k,v in value.items()}
    if isinstance(value,(list,tuple)):
        return [encode(v,arrays,key+'_'+str(i)) for i,v in enumerate(value)]
    if isinstance(value,np.generic):return encode(value.item(),arrays,key)
    if isinstance(value,float) and not math.isfinite(value):return {'nonfinite':str(value)}
    if value is None or isinstance(value,(bool,int,float,str)):return value
    if isinstance(value,Path):return str(value)
    raise TypeError(f'unsupported observation type {type(value)} at {key}')


class Store:
    def __init__(self,root):
        self.root=Path(root);self.root.mkdir(exist_ok=True)
        self.index=(self.root/'index.jsonl').open('x',encoding='utf-8',newline='\n')
        self.last=None

    def save(self,name,value):
        import os
        arrays={};obj=encode(value,arrays)
        target=self.root/(name+'.json');target.parent.mkdir(parents=True,exist_ok=True)
        receipt={'phase':name,'json':str(target)}
        if arrays:
            binary=target.with_suffix('.npz')
            with binary.open('xb') as f:
                np.savez(f,**arrays);f.flush();os.fsync(f.fileno())
            receipt['npz']=str(binary);receipt['npz_sha256']=hashlib.sha256(binary.read_bytes()).hexdigest().upper()
        with target.open('x',encoding='utf-8',newline='\n') as f:
            json.dump(obj,f,ensure_ascii=False,allow_nan=False,separators=(',',':'));f.write('\n');f.flush();os.fsync(f.fileno())
        receipt['json_sha256']=hashlib.sha256(target.read_bytes()).hexdigest().upper()
        self.index.write(json.dumps(receipt,ensure_ascii=False)+'\n');self.index.flush();os.fsync(self.index.fileno())
        self.last=name
        return obj

    def close(self):self.index.close()


class Budget:
    ceilings={'native_initialization':725,'household':725,'labor_root':580000,'brentq':580000,
              'HJB':725,'HJB_direct_solve':72500,'KFE':725,'KFE_direct_solve':725,
              'one_turn':23,'firm':713,'controller_decision':23,'outer_entry':24}
    def __init__(self,seconds=10800):
        self.counts={k:0 for k in self.ceilings}
        self.counts.update(root_residual=0,root_bracketing_residual=0,root_brentq_residual=0,
                           household_returns=0,HJB_returns=0,KFE_returns=0,one_turn_returns=0,
                           adaptive_blocks=0,completed_turns=0)
        self.start=None;self.seconds=seconds
        self.per_call={};self.call=0

    def check(self):
        if self.start is not None and time.monotonic()-self.start>=self.seconds:
            raise ObservationTimeout('scientific wall-time ceiling')

    def enter(self,name):
        self.check()
        if self.counts[name]>=self.ceilings[name]:raise PrefixLimit('entry ceiling '+name)
        if name=='native_initialization':
            self.call+=1;self.per_call[self.call]={'labor_root':0,'HJB_direct_solve':0,'KFE_direct_solve':0}
        if name in ('labor_root','HJB_direct_solve','KFE_direct_solve'):
            limit={'labor_root':800,'HJB_direct_solve':100,'KFE_direct_solve':1}[name]
            if self.per_call[self.call][name]>=limit:raise PrefixLimit('per-household ceiling '+name)
            self.per_call[self.call][name]+=1
        if self.start is None:self.start=time.monotonic()
        self.counts[name]+=1

    def after_household(self):
        self.counts['household_returns']+=1
        if self.call>=725:raise PrefixLimit('call725 returned; stop before call726')


def delegate(original,before=lambda *a,**k:None,after=lambda result,*a,**k:None):
    """Callbacks observe; original receives identical positional and keyword objects once."""
    def wrapped(*args,**kwargs):
        before(*args,**kwargs)
        result=original(*args,**kwargs)
        after(result,*args,**kwargs)
        return result
    return wrapped
