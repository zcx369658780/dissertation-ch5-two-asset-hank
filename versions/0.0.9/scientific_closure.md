# V009 scientific closure — phi-B implementation, PRE_SEAL evidence

## Completed parameter contract

The original CES/HJB/fiscal/asset model is unchanged except for the independently approved phi supplement.
phi[j][i]=1+.3*(pgdp_ref[i]-pgdp_ref[j])/(pgdp_ref[i]+pgdp_ref[j]).
One province has phi11=1; two provinces have rows ((1,1.1),(.9,1)) for external artificial pgdp_ref=(1,2).
Thus the richer destination's weight for the poorer origin is .9, and the reverse is1.1. Opposite MATLAB direction, phi column normalization and current Y/N feedback are excluded.
eta1,nu5,kappa,chi,rho,delta,all prices' initial guesses,20x20x2 grid and V0 remain frozen.

The source/destination oracle independently evaluates the formula and all four entries, non-normalized column sums1.9/2.1 and fixed external references. Existing CES dual/primal, population, Hamiltonian/kink, negative-transfer KKT, invalid-shadow/unit/double-tax role, Q coordinates/boundaries, toy closed-support KFE, fiscal maintenance and R=(3.2,-3.2) oracles remain. Pre-seal suite now15 passed including monotone ledger recovery/conflict refusal. This does not itself prove a HANK equilibrium.

## Mathematical implementation retained

Household ga=ra*a+d; gb=rb*b+z*W*ell+T-c-d-Psi. ra=S-transpose*r; there is no taper,clip,spread or double capital cash payment. The existing audited scalar selector and D1/D2/D3 laws are used in a dedicated namespace, no historical runner.
HJB uses one Delta1000 sparse solve per update, backward error<=1e-12; fresh same-value Bellman<=1e-8 and value change<=1e-7 must coexist. Deterministic first represented alpha halving, positive liquid slopes and cycles remain unchanged.
Final-policy KFE uses exact-positive unique SCC, restricted GESVD, strict positive closed mass, exact-zero transient embedding and one full-Q validation. No pin equation or alternative solver.
Each macro evaluation recomputes household policies/distributions and endogenous moments. Fixed-S Kprivate, firm wage/rental FOC, national debt, signed fiscal T, resource and funding residuals are explicit.

## Cross-province account

A=N E[a], D=N E[d], Kp=S A, rah=S-transpose r.
R_j=sum_i S_ji A_i(rah_i-r_j); sum_j R_j=0.
dot Kp=r*Kp+S D+R; Ip=dot Kp+delta*Kp.
The independent paper example A=(100,100),r=(.1,.2),S=((.8,.2),(.2,.8)),D=0 gives R=(3.2,-3.2),dot Kp=(13.2,16.8), not (10,20).
Government receives (r+delta)Kg and pays delta*Kg maintenance once. National budget and independent goods resource residual are mandatory. No analytical local proof is substituted for a two-province equilibrium.

## Actual scientific progress before sealing

At frozen single-province initial macro vector (logw=0,r=.04,rb=.02,T=0), the first driver reached checkpoint6 with B=4.276595309193887e-5 and D=.0037123504422069686. This is below earlier residuals but NOT within the frozen B/D gate. Its eighth policy mapping was interrupted by a counter-file rename PermissionError, before terminal KFE or any complete macro residual vector.

The I/O-only repair preserves all attempted calls and scientific laws. Ordinary bug recovery consumes the second/final one-province root slot. Its final-tree result is pending, to be recorded separately. No KFE/mass/At/Bt/market result is fabricated from the partial trajectory, and no convergence claim follows from decreasing B.

## Dynamic qualification

IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE.
Still absent: backward time-dependent HJB/terminal values, forward evolving KFE, private/public capital and debt transitions, forward nominal pricing/monetary rule, intertemporal fiscal closure, accepted initial/terminal HANK states and time/horizon errors. The competitive stationary pilot does not supply a sticky-price dynamic system.

Real-source/unit certification,2018 calibration,31-province HANK,formal IRF and Results remain unaccepted; model_activation=False,Results FALSE,C9 PAUSED,A16 FAIL_CLOSED,window UNACCEPTED,CALL_LEDGER_UNRESOLVED,V010 NOT_STARTED.
