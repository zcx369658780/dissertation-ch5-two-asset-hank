# CH5 MP4C K1 — J160 first-turn six-failure HJB mechanism panel freeze

Date: 2026-09-15

## Frozen science

Use the accepted first-turn provincial household inputs from candidate `1e9c8c6416cbd732a44d739e19b40e838993e3d4` and accepted practical grid:

- `I=20`, `J=160`, `Nz=2`
- `a=[0,100]`, `b=[-2,20]`
- diagnostic bridge `h=1`
- accepted MATLAB-faithful HJB equations, initialization, FOCs, selectors, boundaries, derivative floors, `Delta=1000`, sparse direct solve, tolerance `1e-7`, maxit `100`, and `A2max<=0.01` unchanged.

No KFE, outer model, firm/wage/return recomputation, MATLAB runtime, recalibration, or Results path is authorized.

## Exact six states

Replay exactly once, with fresh source-style initialization, only these accepted failed first-turn provinces:

1. 天津: `ra=0.06490365475420734`, `w=18.198003011640164`
2. 山西: `ra=0.08643576394514026`, `w=18.203099062044032`
3. 江西: `ra=0.08911960456738838`, `w=18.066338850784597`
4. 重庆: `ra=0.08592885327235546`, `w=18.070548844406634`
5. 贵州: `ra=0.08979022758512188`, `w=17.471672154406804`
6. 甘肃: `ra=0.09`, `w=17.49933815729084`

All other household-call fields must be recovered from the accepted exact first-turn input vector for the same province and must be identical to the accepted viability execution.

## Instrumentation-only authority

Task-owned instrumentation may observe but must not alter the accepted HJB loop. For every iteration record at least:

- `max(abs(V_new-V_old))`, signed value change at argmax, and argmax state coordinate;
- `A2max`, operator legality, finite/shape checks;
- liquid selector-label changes and transfer/illiquid selector-label changes vs previous iteration;
- derivative-floor hit counts and first floor-hit iteration;
- hashes of value and selector-label states for recurrence checks;
- direct-solve residual when available without changing solver behavior.

Use the accepted J640 instrumentation pattern as reference. Instrumentation invariance must be demonstrated on an already accepted converged reference without new scientific runtime where possible, or via focused non-science tests.

## Mechanism classes

Each province must be classified separately as one of:

- `SLOW_MONOTONE_OR_NEAR_MONOTONE_VALUE_CONVERGENCE`
- `POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`
- `DERIVATIVE_FLOOR_AMPLIFICATION_AFTER_EARLIER_SWITCHING`
- `REPEATING_OR_LOW_PERIOD_CYCLE`
- `MIXED_OR_UNRESOLVED_NUMERICAL_MECHANISM`
- `FAILURE_REPRODUCIBILITY_BLOCKER` if the accepted nonconvergence is not reproduced.

Then give a panel-level classification: homogeneous chatter, homogeneous slow convergence, heterogeneous mechanisms, or unresolved.

## Runtime hard limits

- HJB: exactly 6 if preflight passes
- KFE: 0
- scientific retries: 0
- engineering retry: at most 1 and only before the first HJB, for path/import/serialization/instrumentation plumbing
- global outer/firm/wage/return/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results: 0

Do not increase maxit, change tolerance, introduce damping/relaxation/line search, freeze policies, alter floors/selectors/boundaries, or change any economic input.

Results eligibility remains `FALSE`.
