"""Synthetic conditional equilibria, not HJB/KFE or full HANK GE.

Predeclared scenario: log consumption utility, quadratic CES labor disutility,
given finite distribution and illiquid/liquid holdings, markup m=.9, delta=.05,
one government liquid-debt issuer, endogenous uniform per-NU transfer.
No legacy model imports or file/data loader.
"""
import json
import math
import os
from pathlib import Path
from .reconciled_household_prices import net_prices
from .reconciled_labor import dual_wages, integrate_distribution
from .reconciled_fiscal import Journal, capital_claims, record_wage, transfer_total, government_interest

RESIDUAL_TOL = 1e-8
ROOT_TOL = 1e-11
ACCOUNT_TOL = 5e-11

def reserve(kind, n=0):
    directory = Path(os.environ["V008_LEDGER_DIR"])
    path = directory/"attempts.jsonl"
    events = [json.loads(x) for x in path.read_text().splitlines()] if path.exists() else []
    count = sum(e["kind"]==kind for e in events)
    if count >= (4 if kind=="path" else 12):
        raise RuntimeError("FROZEN_ATTEMPT_LIMIT")
    if kind=="stationary" and n==31 and sum(e["kind"]=="stationary" and e["n"]==31 for e in events)>=2:
        raise RuntimeError("FROZEN_31_LIMIT")
    event = dict(kind=kind,n=n,id=len(events)+1)
    with path.open("a",encoding="utf-8",newline="\n") as f:
        f.write(json.dumps(event)+"\n")
    return event["id"]

def artificial_case(n):
    if n not in (1,2,31):
        raise ValueError("explicit artificial 1/2/31 province fixture")
    return dict(scenario="SYNTHETIC_SCENARIO",n=n,
        N=[1+.04*i for i in range(n)], A=[1+.003*i for i in range(n)],
        Kg=[.2+.001*i for i in range(n)],
        mu=[[dict(p=.4,z=.8,a=.8,b=.1),dict(p=.6,z=1.2,a=1.2,b=.2)] for _ in range(n)],
        phi=[[1 if j==i else 1.2+.002*abs(j-i) for i in range(n)] for j in range(n)],
        S=[[1 if n==1 else (.8 if j==i else .2/(n-1)) for i in range(n)] for j in range(n)],
        tax=.15,corporate_tax=.2,markup=.9,alpha=.3,delta=.05,
        kappa=[1+.005*i for i in range(n)],rb=.01,G_share=.08,
        eta=1,gamma=1,asset_gap=0,mobility_cost=0,clip="none",
        units=("MU_10WAN_YUAN","NU_100_PERSONS","MODEL_TIME"))

def validate(case):
    n=case["n"]
    if case["scenario"]!="SYNTHETIC_SCENARIO" or case["eta"]!=1 or case["gamma"]!=1:
        raise ValueError("conditional scenario requires log/quadratic utility")
    if case["asset_gap"] or case["mobility_cost"] or case["clip"]!="none":
        raise ValueError("unadopted real account configuration")
    if not 0 < case["alpha"] < 1 or not 0 < case["markup"] <= 1:
        raise ValueError("invalid technology")
    if len(case["N"])!=n or any(x<=0 for x in case["N"]+case["A"]+case["Kg"]+case["kappa"]):
        raise ValueError("positive artificial primitives required")
    if any(abs(sum(case["S"][j][i] for j in range(n))-1)>1e-12 for i in range(n)):
        raise ValueError("capital origin columns must conserve")
    if any(s["a"]<0 or s["b"]<0 for states in case["mu"] for s in states):
        raise ValueError("signed private credit requires a separate issuer scenario")

def evaluate(case, x):
    validate(case)
    n=case["n"]
    if len(x)!=n+1 or any(not math.isfinite(v) for v in x):
        raise ValueError("complete unknown vector required")
    w=[math.exp(v) for v in x[:n]]
    t=x[n]
    v=net_prices(w,case["tax"],[[0.0]*n for _ in range(n)],units=case["units"])
    W=dual_wages(v,case["phi"],1)
    wealth=[case["N"][i]*sum(s["p"]*s["a"] for s in case["mu"][i]) for i in range(n)]
    kp=[sum(case["S"][j][i]*wealth[i] for i in range(n)) for j in range(n)]
    K=[kp[j]+case["Kg"][j] for j in range(n)]
    # Conditional household controls depend on capital returns, which in turn
    # depend on L. Include log capital return gross-factor levels as unknowns?
    # Instead firm capital income is tied to wages by the shared factor FOC:
    # Y/L = w/(m*(1-alpha)), and K/L inferred from production at those wages.
    alpha,m=case["alpha"],case["markup"]
    Ld=[K[j]*(m*(1-alpha)*case["A"][j]/w[j])**(1/alpha) for j in range(n)]
    Y=[case["A"][j]*K[j]**alpha*Ld[j]**(1-alpha) for j in range(n)]
    profit=[(1-m)*y for y in Y]
    corporate=[p*case["corporate_tax"] for p in profit]
    returns=[(m*alpha*Y[j]+profit[j]-corporate[j])/K[j]-case["delta"] for j in range(n)]
    rah=[sum(case["S"][j][i]*returns[j] for j in range(n)) for i in range(n)]
    cs=[]; ells=[]
    for i in range(n):
        ci=[]; li=[]
        for state in case["mu"][i]:
            zw=state["z"]*W[i]
            e=state["a"]*rah[i]+state["b"]*case["rb"]+t
            d=zw*zw/case["kappa"][i]
            disc=math.sqrt(e*e+4*d)
            c=(e+disc)/2 if e>=0 else 2*d/(disc-e)
            ci.append(c); li.append(zw/(case["kappa"][i]*c))
        cs.append(ci); ells.append(li)
    flows,Ls=integrate_distribution(case["N"],case["mu"],ells,v,case["phi"],1)
    C=sum(case["N"][i]*sum(s["p"]*c for s,c in zip(case["mu"][i],cs[i])) for i in range(n))
    B=sum(case["N"][i]*sum(s["p"]*s["b"] for s in case["mu"][i]) for i in range(n))
    gross=[w[j]*Ls[j] for j in range(n)]
    G=case["G_share"]*sum(Y)
    public_income=sum(returns[j]*case["Kg"][j] for j in range(n))
    budget=case["tax"]*sum(gross)+sum(corporate)+public_income-G-case["rb"]*B-sum(case["N"])*t
    root=[math.log(Ls[j]/Ld[j]) for j in range(n)]+[budget/max(1,sum(Y))]
    journal=Journal()
    for j in range(n):
        record_wage(journal,gross[j],case["tax"],province=j)
        private,pub=capital_claims(K[j],kp[j],case["Kg"][j],returns[j])
        journal.transfer("firms","households",private,"private_capital",j)
        journal.transfer("firms","government",pub,"public_net_capital",j)
        journal.transfer("firms","government",corporate[j],"corporate_tax",j)
    journal.transfer("government","households",transfer_total(case["N"],[t]*n),"lump_sum_transfer")
    journal.transfer("government","households",government_interest(B,case["rb"],"national_government"),"debt_interest")
    journal.transfer("households","firms",C,"consumption")
    journal.transfer("government","firms",G,"government_consumption")
    scale=max(1,sum(Y))
    household_budget=[]; foc=[]
    for i in range(n):
        for s,c,l in zip(case["mu"][i],cs[i],ells[i]):
            household_budget.append((c-s["z"]*W[i]*l-s["a"]*rah[i]-s["b"]*case["rb"]-t)/max(1,abs(c)))
            foc.append((case["kappa"][i]*l-s["z"]*W[i]/c)/max(1,abs(case["kappa"][i]*l)))
    residuals=dict(labor_market=[(Ls[j]-Ld[j])/max(1,Ld[j]) for j in range(n)],
        firm_wage_foc=[(w[j]-m*(1-alpha)*Y[j]/Ld[j])/max(1,w[j]) for j in range(n)],
        capital_condition=[(returns[j]+case["delta"]-(m*alpha*Y[j]+profit[j]-corporate[j])/K[j])
                           /max(1,abs(returns[j])) for j in range(n)],
        capital_supply=[(K[j]-kp[j]-case["Kg"][j])/max(1,K[j]) for j in range(n)],
        government_budget=[budget/scale],resources=[(sum(Y)-C-G-case["delta"]*sum(K))/scale],
        household_budget=household_budget,household_foc=foc,
        sector_balances=[b/scale for b in journal.balances().values()])
    return dict(root=root,residuals=residuals,w=w,transfer=t,Y=Y,K=K,Kprivate=kp,
                L=Ls,Ld=Ld,C=C,G=G,B=B,returns=returns,W=W,c=cs,ell=ells,
                flows=flows,journal=journal.entries,sector_balances=journal.balances())

def linear_solve(a,b):
    a=[list(row)+[value] for row,value in zip(a,b)]
    n=len(b)
    for k in range(n):
        pivot=max(range(k,n),key=lambda i:abs(a[i][k]))
        a[k],a[pivot]=a[pivot],a[k]
        if abs(a[k][k])<1e-14:
            raise ArithmeticError("singular Jacobian")
        for i in range(k+1,n):
            q=a[i][k]/a[k][k]
            for j in range(k+1,n+1):
                a[i][j]-=q*a[k][j]
    x=[0.0]*n
    for i in range(n-1,-1,-1):
        x[i]=(a[i][n]-sum(a[i][j]*x[j] for j in range(i+1,n)))/a[i][i]
    return x

def solve_blocks(cases, initial=None, label="gate_b"):
    """One root problem with independent time blocks; colored finite differences.

    All period blocks are solved jointly, not hidden per-period solver invocations.
    Gate C records its own path reservation AND this root attempt. Thus total
    root attempts, including all path roots, are bounded by 12.
    """
    n=cases[0]["n"]
    attempt=reserve("stationary",n)
    width=n+1
    x=[list(p) for p in initial] if initial is not None else [[math.log(.8)]*n+[.1] for _ in cases]
    initial_x=[row[:] for row in x]
    evaluations=0; linear_systems=0; history=[]
    def f(values):
        nonlocal evaluations
        if evaluations>=200:
            raise RuntimeError("EVALUATION_CAP_200")
        evaluations+=1
        return [evaluate(c,z) for c,z in zip(cases,values)]
    stop="NO_CONDITIONAL_STEADY_STATE"; result=[]; iterations=0
    try:
        result=f(x)
        for iterations in range(40):
            error=max(abs(y) for r in result for y in r["root"])
            history.append(error)
            if error<=ROOT_TOL:
                stop="ROOT_TOLERANCE"; break
            jac=[[[0.0]*width for _ in range(width)] for _ in cases]
            for k in range(width):
                pert=[row[:] for row in x]
                steps=[1e-6*max(1,abs(row[k])) for row in x]
                for b in range(len(cases)): pert[b][k]+=steps[b]
                rr=f(pert)
                for b in range(len(cases)):
                    for j in range(width):
                        jac[b][j][k]=(rr[b]["root"][j]-result[b]["root"][j])/steps[b]
            delta=[linear_solve(j,[-v for v in r["root"]]) for j,r in zip(jac,result)]
            linear_systems+=len(cases)
            accepted=False
            for power in range(16):
                trial=[[value+2**(-power)*d for value,d in zip(row,dr)] for row,dr in zip(x,delta)]
                try: candidate=f(trial)
                except (OverflowError,ValueError): continue
                err=max(abs(y) for r in candidate for y in r["root"])
                if err<error:
                    x,result=trial,candidate; accepted=True; break
            if not accepted:
                stop="LINE_SEARCH_FAILED"; break
    except (ArithmeticError,RuntimeError,OverflowError,ValueError) as exc:
        stop=type(exc).__name__+": "+str(exc)
    maximum=max((abs(v) for r in result for values in r["residuals"].values() for v in values),default=1e300)
    accounting=max((abs(v) for r in result for name in ("government_budget","resources","sector_balances")
                    for v in r["residuals"][name]),default=1e300)
    success=stop=="ROOT_TOLERANCE" and maximum<=RESIDUAL_TOL and accounting<=ACCOUNT_TOL
    report=dict(qualification="SYNTHETIC_CONDITIONAL_STATIONARY" if success else "NO_CONDITIONAL_STEADY_STATE",
        success=success,label=label,attempt=attempt,n=n,blocks=len(cases),
        unknown_names=[*[f"log_gross_wage_{j}" for j in range(n)],"national_transfer_per_NU"],
        initial_vector=initial_x,solution_vector=x,evaluations=evaluations,
        residual_evaluations_per_block=evaluations,linear_systems=linear_systems,
        iterations=iterations,stop_reason=stop,history=history,max_scaled_residual=maximum,
        max_accounting_residual=accounting,residual_tolerance=RESIDUAL_TOL,accounting_tolerance=ACCOUNT_TOL,
        results=result,conditional_on="given distributions, assets and public capital; no HJB/KFE/Euler or NKPC",
        asset_capital_condition="given stock ownership and firm return FOC; NOT household Euler clearing",
        scenario=cases)
    out=Path(os.environ["V008_LEDGER_DIR"])/f"root_{attempt:03d}.json"
    with out.open("x",encoding="utf-8",newline="\n") as file: json.dump(report,file,indent=2,allow_nan=False)
    return report

def solve_stationary(case):
    return solve_blocks([case])
