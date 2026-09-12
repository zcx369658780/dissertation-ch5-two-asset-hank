# Chapter 5 MP4C K1 price-guard continuation and boundary-hit monitoring freeze

Date: 2026-09-12.
Status: `OWNER_APPROVED_RA_FIRST_CONTINUATION__WAGE_GUARD_FIXED__MATLAB_STYLE_BOUNDARY_HIT_MONITORING_REQUIRED__FINAL_STEADY_STATE_TARGET_ZERO_PRICE_GUARD_HITS`.

## 1. Owner clarification

The historical MATLAB `ra` and `wjt` bounds are numerical safeguards used to keep the nonlinear HA / HJB block inside a tractable region during steady-state iteration. They are not automatically structural economic restrictions.

The legacy MATLAB route explicitly defines `wjtmin=.8`, `wjtmax=1.3` and records which provinces hit the return and wage bounds during the multi-province iteration. The rebuilt route therefore treats return-bound and wage-bound hits as mandatory numerical-state diagnostics rather than hiding them inside clipped objects.

## 2. Continuation order

The rebuilt annual K1A route will relax one price safeguard family at a time.

Phase A: hold the legacy wage safeguard `wjt in [.8,1.3]` fixed and advance only the HJB illiquid-return continuation ladder.

Phase B: after a provisional return-guard region has been identified, hold that return scaffold fixed and separately design a wage-guard relaxation ladder from persisted raw wage evidence.

Phase C: progressively weaken both safeguards and seek a converged state with no price-variable guard hits.

No task may simultaneously widen both the return guard and wage guard unless the Owner separately authorizes that experiment.

## 3. Return continuation ladder

The preregistered annual HJB return ladder remains:

- G1: `r_a in [-.05,.20]`;
- G2: `r_a in [-.10,.35]`;
- G3: `r_a in [-.20,.60]`;
- G4: return guard OFF.

The accepted G1 short-horizon diagnostic showed `124/124` treatment province-turns at the `.20` upper guard. Therefore G1 is accepted only as a continuation starting point and is not suitable as an economic payoff calibration.

The next authorized comparison is symmetric G1 versus G2 over the same short horizon while keeping the wage safeguard fixed.

## 4. Mandatory wage-hit monitoring

Every runtime continuation task must monitor wage-bound usage in the MATLAB style.

For every province and completed turn, persist where available:

- raw/pre-guard wage object;
- guarded `wjt` actually used by the active route;
- `wjt == wjtmax` / upper-hit indicator;
- `wjt == wjtmin` / lower-hit indicator;
- province names in upper-hit and lower-hit sets;
- counts and shares by turn and over the full path.

If exact equality is not the active implementation criterion, report the active clipping criterion and use a tolerance-consistent hit flag. Do not silently infer non-hits from a guarded value alone.

Return-bound monitoring must analogously persist raw/converted/guarded payoff, hit direction, province names, counts and shares.

## 5. Ideal steady-state target

The long-run numerical objective is a converged steady state in which price-like numerical safeguards are nonbinding:

- no province hits the diagnostic `r_a/rah` guard;
- no province hits the diagnostic `wjt/wage` guard;
- the state satisfies the accepted HJB/KKT/boundary, capital-network, accounting and KFE gates.

Until those safeguards are nonbinding, any steady state is `PROVISIONAL_STEADY_STATE` only.

A temporary bound may remain active during continuation even if it is not hit; the final scientific route should widen/remove diagnostic bounds where feasible and demonstrate that accepted results do not depend on them.

## 6. Current scientific boundary

Annual recalibration remains frozen:

- `MODEL_TIME_BASE=ANNUAL_CONTINUOUS_TIME`;
- `rho=.05/year`, `rb=.02/year`, borrowing gap `.07/year`;
- firm/HJB `delta=.10/year`;
- `Q_z` off-diagonal `1/3/year`;
- annual corrected `Y/K` and after-tax profit/K unchanged;
- `ra0_annual=rk+after_tax_profit_over_K-.10`;
- `chi0=.1`, `chi1=2 years` provisional annual calibration;
- fixed K1A theta, `beta_distance=2`, `beta_return=0`, source-faithful labor, C1 unchanged.

K1B and K2 remain unauthorized. KFE remains `DIAGNOSTIC_ONLY` with the independent finite-box upper-b leakage / MATLAB-style pinning blocker.

Results eligibility remains `FALSE`.
