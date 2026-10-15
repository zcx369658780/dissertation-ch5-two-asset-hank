"""Real HJB/KFE nested macro solve, with an explicit scientific failure terminal."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys
import traceback
import numpy as np
import scipy
from .contracts import Ledger,case,calibration_hash,FREEZE,BASELINE
from .accounts import aggregate,positive_prices
from .household import solve_household

def irf_missing():
    return dict(status="IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE",missing=[
        "backward dynamic HJB and terminal value","forward time-dependent KFE",
        "private/public capital and government debt state transitions",
        "forward pricing/inflation and monetary rule","fiscal intertemporal closure",
        "accepted initial/terminal HANK states and horizon error"],execution_authorized=False)
def acceptance(r):
    if not r.get("households") or "residuals" not in r or "accounting" not in r:
        raise ValueError("no endogenously solved households and markets")
    hs=r["households"]
    gates=dict(household=all(h["B"]<=1e-8 and h["D"]<=1e-7 and
        h["kfe"]["closed_count"]==1 and h["kfe"]["nullity"]==1 and
        h["kfe"]["stationarity"]<=h["kfe"]["stationarity_bound"] for h in hs),
        nondegenerate=all(h["A"]>0 and h["Basset"]>0 for h in hs),
        upper_mass=all(h["top_mass"]<=1e-6 for h in hs),
        markets=max(abs(v) for v in r["residuals"])<=1e-8,
        accounts=max(abs(v) for v in r["accounting"])<=5e-11)
    return dict(success=all(gates.values()),gates=gates)
def compact(h):
    return {k:h[k] for k in ("identity","B","D","checkpoint","updates","top_mass",
        "kfe","A","Basset","C","Dasset","cost","mean_ga","mean_gb")}
def solve(n,label,ledger):
    c=case(n)
    # Missing frozen coefficients must stop before reserving macro/scientific calls.
    positive_prices(c,np.ones(n))
    macro=ledger.start_macro(n,label);x=np.array(c["x0"],float);initial=x.tolist()
    history=[];last=None
    def evaluate(values):
        ev=ledger.evaluation(macro);w=np.exp(values[:n])
        W=positive_prices(c,w)[2];r=values[n:2*n];ra=np.array(c["S"]).T@r
        households=[]
        for i in range(n):
            households.append(solve_household(c,i,float(W[i]),float(ra[i]),float(values[-2]),
                float(values[-1]),ledger,macro,ev))
        result=aggregate(c,values,households)
        result["households"]=[compact(h) for h in households]
        ledger.event(f"macro_{macro:02d}_evaluations",dict(evaluation=ev,**result))
        return result
    try:
        last=evaluate(x)
        while True:
            rr=np.asarray(last["residuals"]);norm=float(np.max(abs(rr)))
            history.append(dict(x=x.tolist(),norm=norm))
            if norm<=1e-12:break
            width=len(x);J=np.empty((width,width))
            for k in range(width):
                step=1e-5*max(1.,abs(x[k]));trial=x.copy();trial[k]+=step
                pert=evaluate(trial)
                J[:,k]=(np.array(pert["residuals"])-rr)/step
            delta=np.linalg.solve(J,-rr)
            accepted=False
            for power in range(12):
                trial=x+2.**(-power)*delta
                candidate=evaluate(trial)
                if max(abs(v) for v in candidate["residuals"])<norm:
                    x=trial;last=candidate;accepted=True;break
            if not accepted:raise RuntimeError("MACRO_LINE_SEARCH_FAILED")
        result=dict(last,n=n,macro=macro,label=label,initial_vector=initial,history=history,
            calibration_hash=calibration_hash(c),qualification="NO_SYNTHETIC_HANK_STEADY_STATE")
        gate=acceptance(result);result.update(gate)
        if gate["success"]:result["qualification"]="SYNTHETIC_TWO_ASSET_HANK_STATIONARY_CANDIDATE"
        else:result["failure"]="FINAL_ECONOMIC_OR_TRUNCATION_GATE"
        return result
    except Exception as exc:
        return dict(success=False,n=n,macro=macro,label=label,
            qualification="NO_SYNTHETIC_HANK_STEADY_STATE",failure=repr(exc),
            initial_vector=initial,last_complete_evaluation=last,history=history,
            traceback=traceback.format_exc(),calibration_hash=calibration_hash(c))
def preregister(ledger):
    files={}
    source=Path(__file__).resolve().parent
    for f in sorted(source.glob("*.py")):
        files["reconciled_hank/"+f.name]=hashlib.sha256(f.read_bytes()).hexdigest()
    for f in sorted((source.parent/"corrected_diagnostic").glob("*.py")):
        files["corrected_diagnostic/"+f.name]=hashlib.sha256(f.read_bytes()).hexdigest()
    tests=source.parents[2]/"tests"
    for f in sorted(tests.glob("test_v009_*.py")):
        files["tests/"+f.name]=hashlib.sha256(f.read_bytes()).hexdigest()
    config=dict(freeze=FREEZE,baseline=BASELINE,cases=[case(1),case(2)],source_hashes=files)
    path=ledger.root/"preregistration.json"
    if path.exists():
        old=json.loads(path.read_text(encoding="utf-8"))
        if old["cases"]!=json.loads(json.dumps(config["cases"])):raise RuntimeError("CALIBRATION_CHANGED")
    else:
        with path.open("x",encoding="utf-8",newline="\n") as f:json.dump(config,f,indent=2,allow_nan=False)
    return config
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--n",type=int,choices=[1,2],required=True)
    parser.add_argument("--label",required=True);args=parser.parse_args()
    ledger=Ledger();prereg=preregister(ledger)
    # Report only after exact fixed-source view/import evidence is persisted.
    ledger.event("environments",dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__,
        platform=platform.platform(),module=__file__,source_hashes=prereg["source_hashes"]))
    result=solve(args.n,args.label,ledger)
    result["irf"]=irf_missing()
    target=ledger.root/(args.label+".result.json")
    with target.open("x",encoding="utf-8",newline="\n") as f:json.dump(result,f,indent=2,allow_nan=False)
    if result["success"] and args.n==1:
        marker=ledger.root/"ONE_PROVINCE_PASS.json"
        if not marker.exists():
            with marker.open("x",encoding="utf-8") as f:json.dump(result,f)
    print(json.dumps(result,allow_nan=False))
    return 0 if result["success"] else 2
