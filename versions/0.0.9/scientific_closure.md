# V009 scientific closure — implementation and bounded oracles only

This document implements Owner E1–E3 in a new isolated model. It does not report a solved HANK steady state. The code is computational, but the full numerical chain is NOT_RUN because the frozen numerical phi matrix is absent.

## Implemented equations

The frozen household controls satisfy c=q_b^(-1/gamma), kappa*ell^nu=q_b*z*W and 0 in q_a-q_b*(1+partial_d Psi), with positive liquid shadow, state constraints and the accepted switching law. Asset drifts are ga=ra*a+d and gb=rb*b+z*W*ell+T-c-d-Psi. ra has no taper/clip, b has no negative holdings or spread. Source/flatten order is (b,a,z), b-fast/F.

The HJB uses the frozen V0, Delta=1000, one sparse direct solve per update, backward error <=1e-12, fresh same-value policy/Q Bellman residual <=1e-8 and accepted value-change <=1e-7. First represented alpha in {1,1/2,...,2^-52} with all 760 liquid slopes positive and a changed value is accepted. Nonconvergence/cycle/invalid policy stops the dependent chain.

The stationary KFE performs exact-positive SCC, requires one closed class, one restricted Q_CC-transpose GESVD, rank m-1/nullity 1 under local/full arithmetic bounds, one orientation/normalization, exact-zero transients and one full original-Q transpose validation. No row replacement, source, alternative solver or negative-mass repair. The household terminal solver explicitly refuses non-800 dimensions.

The macro vector is (log wages, destination net capital returns, rb, signed national T). Each evaluation calls each household anew, forms Kprivate=S*(N*E[a]), state-integrated bilateral labor, competitive production, wage/rental FOC, national bond clearing and the unified fiscal budget. Independent goods/funding checks and terminal upper-bound union mass are mandatory; a metadata success flag is insufficient.

## Fixed-S funding and independent oracle

A=N*E[a], D=N*E[d], Kprivate=S*A, rah=S-transpose*r.
R_j=sum_i S_ji*A_i*(rah_i-r_j).
dot Kprivate=S*(rah*A+D)=r*Kprivate+S*D+R.
Gross private investment=dot Kprivate+delta*Kprivate.

The independent paper counterexample uses S=[[.8,.2],[.2,.8]], A=(100,100), r=(.1,.2), D=0.
Then rah=(.12,.18), R=(3.2,-3.2), and dot Kprivate=(13.2,16.8), while local r*Kprivate=(10,20). Dropping R fails the funding oracle. These are toy numbers, NOT a two-province equilibrium execution.

The public account receives gross (r+delta)Kg and pays delta*Kg maintenance exactly once. The national budget is tau*wL+r*Kg-G-rb*Bg-T*sum(N). State-integrated adjustment costs are real resources and enter the independent goods constraint, never fiscal residual income.

## Blocking frozen input

Plan section 2 uses phi[j,i] in CES, while the section 3 table freezes eta but supplies NO phi. Neither the Owner adoption nor separate authorization fixes its values. In one province and eta=1, W=(1-tau)w/sqrt(phi_11). Choosing phi_11=4 instead of 1 halves W and changes both HJB labor and cash drift. Zero migration fees/sigma=0 does not identify this labor-disutility metric. Setting phi=1 or offsetting kappa would be an unfrozen economic choice. Accordingly the full-model cases have phi=null and fail before any macro/household budget reservation. Toy CES tests explicitly supply asymmetric weights solely to verify the general formula.

Required concentrated clarification: exact single-province and two-province phi matrices, with their authoritative frozen/amended identity. No other economic decision is being reopened.

## Gate qualifications

A: 13 focused toy/engineering tests passed before sealing, including duality, independent local Hamiltonian/kink and negative-transfer KKT, invalid shadows/units/double-tax role, Q coordinates/state constraints, toy closed-support KFE, R, public depreciation and early missing-input rejection.

B: NOT_RUN__FROZEN_CES_PHI_NOT_SPECIFIED. No HJB B/D, full-Q/KFE residuals, endogenous asset means, macro solution vector or market residuals exist.

C: NOT_RUN__GATE_B_NOT_PASSED. Only the independent algebraic R example was evaluated.

D: IRF_BLOCKED__NO_DYNAMIC_HANK_CLOSURE. Still missing backward dynamic household HJB/terminal value, forward KFE, capital/fund/debt transitions, nominal forward pricing/policy rules, fiscal intertemporal closure, accepted initial/terminal HANK equilibria and horizon/time-step error. This competitive stationary pilot does not supply a sticky-price dynamic model.

At most implementation/toy-oracle evidence is claimable here, subject to Astra independent review. No self-ACCEPT, real source/unit certification, original-C8 model activation, GE/IRF/Results or V010 start.
