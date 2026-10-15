"""Frozen E1--E3 inputs and persistent attempted-call accounting."""
from pathlib import Path
import hashlib
import importlib
import json
import os
import sys
import time
import types
import numpy as np

FREEZE="f7caeb54b13ec977d1b503b124067ae522ca2433"
BASELINE="d41d229b681e09b913c21deff7a057085b9bc419"
TIME_UNIT="MODEL_TIME_SYNTHETIC"
LIMITS=dict(household=176,update=17600,mapping=17776,svd=176,
            selector_root=70400000,macro=4)
def digest(data):
    return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(",",":"),
        allow_nan=False).encode()).hexdigest()
def case(n):
    if n not in (1,2): raise ValueError("only frozen one/two synthetic provinces")
    return dict(n=n,rho=.05,gamma=2.,nu=5.,eta=1.,chi0=.1,chi1=2.,abar=.1,
        alpha=.3,tau=.05,delta=.1,markup=1.,corporate_tax=0.,
        z=(.8,1.2),Lambda=((-1/3,1/3),(1/3,-1/3)),
        N=(1.,) if n==1 else (1.,1.1),
        Z=(1.,) if n==1 else (1.,1.03),
        kappa=(1.,) if n==1 else (1.,1.02),
        Kg=(.2,) if n==1 else (.2,.22),
        Bg=.4*(1 if n==1 else 2.1),G=.06*(1 if n==1 else 2.1),
        S=((1.,),) if n==1 else ((.8,.2),(.2,.8)),
        phi=None,  # NOT_SPECIFIED in frozen section 3: no scientific default.
        b=(0.,2.,20),a=(0.,5.,20),shape=(20,20,2),
        x0=[0.]*n+[.04]*n+[.02,0.],V0="-1/(rho*(1+b+a+z))",
        AtTax=0.,sigma=0.,clip="none",taper="none",spread=0.,
        time_unit=TIME_UNIT,axis="b,a,z",flatten="F")
def calibration_hash(c): return digest(c)
def pure(name):
    if name not in ("contracts","boundary","cost","generator","selector"):
        raise ValueError("not in audited mathematical closure")
    alias="_v009_pure"
    path=Path(__file__).resolve().parents[1]/"corrected_diagnostic"
    if alias not in sys.modules:
        pkg=types.ModuleType(alias);pkg.__path__=[str(path)]
        sys.modules[alias]=pkg
    mod=importlib.import_module(alias+"."+name)
    if Path(mod.__file__).resolve()!= (path/(name+".py")).resolve():
        raise RuntimeError("MATHEMATICAL_MODULE_ORIGIN")
    return mod
def grid():
    return pure("contracts").CorrectedDiagnosticGrid(
        np.linspace(0,2,20),np.linspace(0,5,20),np.array([.8,1.2]))

class Ledger:
    """Single-writer ledger; reserve BEFORE every attempted counted operation."""
    def __init__(self):
        self.root=Path(os.environ["V009_LEDGER_DIR"])
        self.path=self.root/"science_counts.json"
        self.data=json.loads(self.path.read_text(encoding="utf-8")) if self.path.exists() else {
            "started":time.time(),"totals":{},"households":{},"macros":{}}
        self.hh=None
    def save(self):
        temporary=self.path.with_suffix(".tmp")
        with temporary.open("w",encoding="utf-8",newline="\n") as f:
            json.dump(self.data,f,sort_keys=True,allow_nan=False);f.flush();os.fsync(f.fileno())
        os.replace(temporary,self.path)
    def guard(self):
        if time.time()-self.data["started"]>=8*3600: raise RuntimeError("WALL_BUDGET")
        if (self.root/"MEMORY_STOP").exists(): raise RuntimeError("MEMORY_BUDGET")
        # Bound numerical receipts. Git/view/public are also checked by launcher.
        size=sum(p.stat().st_size for p in self.root.rglob("*") if p.is_file())
        if size>=144*1024**2: raise RuntimeError("RECEIPT_STORAGE_BUDGET")
    def reserve(self,key,category=None):
        totals=self.data["totals"]
        limit=LIMITS.get(key,10**9)
        if totals.get(key,0)>=limit: raise RuntimeError("VERSION_BUDGET_"+key)
        h=self.data["households"].get(str(self.hh)) if self.hh is not None else None
        caps=dict(update=100,mapping=101,svd=1,selector_root=400000)
        if h is not None and key in caps and h.get(key,0)>=caps[key]:
            raise RuntimeError("HOUSEHOLD_BUDGET_"+key)
        totals[key]=totals.get(key,0)+1
        if category: totals[category]=totals.get(category,0)+1
        if h is not None:
            h[key]=h.get(key,0)+1
            if category:h[category]=h.get(category,0)+1
        self.save()
        return totals[key]
    def start_household(self,macro,ev,origin):
        self.guard()
        self.hh=None
        identity=self.reserve("household")
        self.hh=identity
        self.data["households"][str(identity)]=dict(macro=macro,eval=ev,origin=origin)
        self.save()
        return identity
    def start_macro(self,n,identity):
        self.guard()
        old=[v for v in self.data["macros"].values() if v["n"]==n]
        if len(old)>=2: raise RuntimeError("PROVINCE_MACRO_BUDGET")
        if n==2 and not (self.root/"ONE_PROVINCE_PASS.json").exists():
            raise RuntimeError("ONE_PROVINCE_GATE_NOT_PASSED")
        k=self.reserve("macro")
        self.data["macros"][str(k)]=dict(n=n,identity=identity,evaluations=0)
        self.save();return k
    def evaluation(self,k):
        self.guard();m=self.data["macros"][str(k)]
        if m["evaluations"] >= (24 if m["n"]==1 else 32):
            raise RuntimeError("MACRO_EVALUATION_BUDGET")
        m["evaluations"]+=1;self.save();return m["evaluations"]
    def event(self,name,content):
        with (self.root/(name+".jsonl")).open("a",encoding="utf-8",newline="\n") as f:
            f.write(json.dumps(content,allow_nan=False,sort_keys=True)+"\n")
class SelectorCounter:
    def __init__(self,ledger):
        self.ledger=ledger;self.selector_evaluations=0;self.root_invocations=0
        self.interior_z_root_invocations=0;self.interior_a_switching_root_invocations=0
        self.joint_switching_root_invocations=0
    def begin_selector(self):
        self.ledger.reserve("selector_root","selector")
        self.selector_evaluations+=1;return self.selector_evaluations
    def begin_root(self):
        self.ledger.reserve("selector_root","scalar_root")
        self.root_invocations+=1;return self.root_invocations
    def _special(self,name):
        self.ledger.reserve("selector_root",name)
        self.root_invocations+=1;setattr(self,name+"_invocations",getattr(self,name+"_invocations")+1)
        # scalar_root total includes all special classes, without double charging budget.
        t=self.ledger.data["totals"];t["scalar_root"]=t.get("scalar_root",0)+1
        self.ledger.save();return self.root_invocations
    def begin_interior_z_root(self): return self._special("interior_z_root")
    def begin_interior_a_switching_root(self): return self._special("interior_a_switching_root")
    def begin_joint_switching_root(self): return self._special("joint_switching_root")
