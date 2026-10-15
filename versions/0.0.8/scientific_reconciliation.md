# V008 corrected-model scientific reconciliation — PRE_SEAL

This is a new SYNTHETIC_SCENARIO branch. Historical C8 and2009 parity are preserved. No real data authentication or HANK GE/IRF is claimed.

## Preferences, distributions, labor and one tax

Every artificial origin has two states (p,z,a,b)=(.4,.8,.8,.1),(.6,1.2,1.2,.2).
N_i=1+.04i; A_i=1+.003i; Kg_i=.2+.001i; kappa_i=1+.005i.
phi diagonal1, off-diagonal1.2+.002*abs(j-i).
S retains .8 at home and shares .2 abroad; one-province S=1.
Given household illiquid assets determine Kprivate; K=Kprivate+Kg. No household Euler or asset-market endogeneity is asserted.

CES ell=(sum(phi*h^(1+eta)))^(1/(1+eta)).
W=(sum(phi^(-1/eta)*v^(1+1/eta)))^(eta/(1+eta)).
h_ji=ell_i*phi_ji^(-1/eta)*(v_ji/W_i)^(1/eta).
reconciled_labor implements these and actual sum_states(N*p*z*h) on every origin state, without Ct mean substitution or sum(h)=ell.
Net prices apply one national tax once: v_ji=w_j*(1-tau-cost_ji). Positive costs require explicit government_fee/intermediary/resource classification, with full gross=net+tax+cost income checks.

Gate A tests general eta and independent quadratic primal oracles,1/2/31 provinces, unequal wages/population,positive/zero tax,positive mobility, Jensen counterexample and FOC currency scaling.
M=100000 yuan,U=100 persons,T=MODEL_TIME. Assets M/U; c,Tt M/(U*T); wages M/(U*H*T). No real hours/calendar claim. Currency factor h requires kappa'=h^(1-gamma)*kappa. Wrong units and double deduction fail.

## Declared conditional stationary economy

Parameters fixed before numerical runs: gamma=eta=1 (log c,quadratic labor), alpha=.3,markup m=.9,delta=.05,tau=.15,corporate tax=.2,rb=.01,G_share=.08.
These are artificial assumptions, not changes to legacy delta/inflation/calibration. m is a given synthetic static wedge, not a solved NKPC or an assertion pi=0.
AtTax=0,mobility=0,no clip in B/C. Nonzero AtTax has exclusive government/intermediary/resource toy scenarios in A only. Unclassified nonzero actual configurations fail closed.
Positive liquid assets are explicitly claims on one national government; no automatic private-credit/debt identification.

For given prices and transfer t:
e=a*rah+b*rb+t; ell=zW/(kappa*c);
c=zW*ell+e => c=(e+sqrt(e^2+4*(zW)^2/kappa))/2.
The stable equivalent expression is used for negative e. These exact analytic controls satisfy household budget and intratemporal FOC; there are no hidden scalar-root calls, HJB,KFE or savings Euler equations.

Firm:
Y=A*K^alpha*L^(1-alpha);
w=m*(1-alpha)*Y/L;
profit=(1-m)*Y;
corporate_tax=.2*profit;
r=(m*alpha*Y+profit-corporate_tax)/K-delta.
Same r is split by private/public ownership. Nonzero raw/used clipping is rejected without an adopted recipient contract.
Firm labor demand is analytically eliminated:
Ld=K*(m*(1-alpha)*A/w)^(1/alpha).
Numerical unknowns are n log gross wages and one national per-NU transfer. Ls is computed from CES household states. Root equations are all log(Ls/Ld) and scaled government budget.
K is an explicitly given capital-stock constraint; Y changes with the numerically solved wages/labor. Neither is assigned a target solution.

Selected SYNTHETIC_FINANCING_CLOSURE:
tau*sum(w*Ls)+sum(corporate_tax)+sum(r*Kg)-G-rb*B-t*sum(N)=0.
t is an exposed unknown, not hidden fiscal income.
Resources:
sum(Y)-sum(N*E[c])-G-delta*sum(K)=0.
Independent directed cash entries assemble household/firm/government balances. Provincial analysis attributes workplace receipts and resident transfers/interest without31 separate governments.

## Fixed criteria and Gate B results

Damped finite-difference Newton, numerical target1e-11, every normalized economic residual<=1e-8, government/resources/sector balance<=5e-11; cap200 residual-vector evaluations. No changes after results.
All initial log wages=log(.8),initial t=.1.

| provinces | evaluations | Newton updates | max economic | max accounting |
|---|---:|---:|---:|---:|
|1|10|3|1.1765033391952784e-12|8.274492202531292e-13|
|2|17|4|1.4443497459199443e-14|1.2309835524427652e-14|
|31|166|5|9.950791095908994e-14|9.950791095908994e-14|

All stop ROOT_TOLERANCE. Full unknown names,initial/solution vectors and every residual array are public in acceptance_summary.json; complete journals/state outputs are LOCAL_ONLY.
Labor markets,firm wage/return FOCs,given capital allocation,household budgets/FOCs,government/resources and sector accounts are checked.
The capital condition is a firm return FOC and given-stock ownership, NOT a household Euler or endogenous capital equilibrium.
Qualification: SYNTHETIC_CONDITIONAL_STATIONARY only.

## Gate C: actual conditional paths and public-capital financing

Qualified one-province B baseline. Four paths:
zero/40 periods;1e-4/40;5e-5/40;1e-4/20.
Three independent explicit AR(1) coordinates,rho=.5: TFP innovation t0,national tax t10,public capital t20.
Long paths exercise all three coordinates; later windows are mixed conditional scenarios, not isolated causal IRFs.

Each path solves ONE genuine joint block-diagonal root with one independent static block per period. Colored finite differences form the block Jacobians; no hidden per-period root invocation.
Root evaluations1/7/7/7; block counts40/40/40/20; block evaluations40/280/280/140=740. Every block receives at most7 evaluations; joint root cap200 applies. Root attempts including paths are conservatively charged against12.

Comparison:
zero response0;40/20 prefix error0;
half-amplitude relative error6.810212990015854e-6;
tail relative response9.13651085896238e-8;
period max residual1.1765033391952784e-12.
Finite/bounded and reversion tests passed; response sign is not imposed.

Public-capital variation is an explicit SYNTHETIC_EXTERNAL_CAPITAL_ENDOWMENT: donor supplies/removes delta Kg in kind at period boundaries; opposite donor/government asset entries and net public investment are shown. Gross investment adds delta*Kg maintenance; cash grant=0. Resource grant and corresponding net investment cancel explicitly.
This is NOT an adopted investment/debt policy and not an endogenous capital transition. The bridge is a separate final-tree calculation on saved artificial paths, not a fifth path run.

After C only two pure function definitions were appended (province attribution,endowment bridge); exercised source prefixes are unchanged. Final-tree tests cover addenda and repeat B, while the four exhausted C paths are not rerun.

## Gate D: actual refusal

IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE. Missing:
dynamic household HJB/terminal value;forward KFE/full distribution conservation;private/public asset and debt dynamics;forward-looking firm pricing/inflation;intertemporal monetary/fiscal closure;full-HANK period clearing;accepted initial/terminal HANK equilibria;shock time scale/terminal-error contract.
The gate rejects boolean placeholders and requires separate accepted evidence references. No dynamic execution is authorized.

Complete HANK would require one consolidated new scientific specification/authorization for these equations,initial/terminal conditions,asset accounting,data identity/protection and numerical budgets. Conditional static curves cannot supply the missing evidence.
Original Option1/S/C1/raw-ra0/lagged/HJB/KFE and accepted historical conclusions are not overwritten. No real C8 reads or old model calls.
A16 FAIL_CLOSED;window UNACCEPTED;C9 PAUSED;CALL_LEDGER_UNRESOLVED;model_activation=False;Results=False.
WAIT_ASTRA_V008_CORRECTED_MODEL_NUMERICAL_GATE_ACCEPTANCE / STOP.
