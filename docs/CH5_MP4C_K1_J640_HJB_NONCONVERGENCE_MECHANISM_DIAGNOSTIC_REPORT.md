# CH5 MP4C K1 — J640 HJB nonconvergence mechanism diagnostic report

Date: 2026-09-15

Terminal classification:

`POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`

Results eligibility=`FALSE`.

## Repository and authority

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Fresh-fetched actual baseline: `11d3839f6bc500709fe4fbf65edfc346bb7748f1`
- Branch: `codex/ch5-mp4c-k1-j640-hjb-nonconvergence-mechanism-diagnostic-20260915`
- Worktree: `D:\ProjectTemp\ch5-mp4c-k1-j640-hjb-nonconvergence-mechanism-diagnostic-20260915-001`
- Task: `CH5_MP4C_K1_J640_HJB_NONCONVERGENCE_MECHANISM_DIAGNOSTIC`

The protected Python HJB/KFE oracle, MATLAB source, accepted finer-grid evidence, and accepted small-grid instrumentation-parity evidence matched their frozen identities. The diagnostic added task-owned observation and offline-finalization code only. It did not modify the accepted HJB scientific loop, KFE source, equations, FOCs, selectors, boundaries, derivative floors, solver, tolerance, maximum iterations, initialization, mappings, guards, or economic parameters.

## Preflight and instrumentation invariance

The first preflight failed before any scientific call because its accepted-parity manifest check compared a canonical-LF hash with a manifest entry that recorded the CRLF byte hash. The single authorized engineering retry changed only the identity receipt and check: it records both byte and canonical-LF SHA-256 values and passes only when one representation exactly equals the frozen manifest entry. The second preflight passed. Science calls before the clean gate remained zero, and no scientific behavior changed.

Instrumentation calls the live accepted `solve_matlab_faithful_hjb` directly. Temporary wrappers observe policy selection, operator assembly, and the unchanged sparse solve, return the original objects or values, and are restored in `finally`. Scientific control flow never reads the observations. The accepted small-grid reference establishes exact OFF/ON scientific equality and exact equality to accepted output at 17 iterations; it was reused without a new HJB call. Maxit remained 100, tolerance remained `1e-7`, initialization remained fresh, and no damping, clipping, renormalization, warm start, or policy freezing was introduced.

## Frozen replay and reproducibility gate

The replay held `rb=.02`, `ra=.0675`, `w=15.5`, `a=[0,100]`, `b=[-2,20]`, `h=1`, `I=20`, `J=640`, and `Nz=2` fixed. It used fresh source initialization, `Delta=1000`, the accepted tolerance `1e-7`, and maxit=100, with no warm start.

Exactly one J640 HJB replay completed. It again did not converge after 100 iterations. Its final `max(abs(Vnew-Vold))` was `0.0012277767122459426`, exactly equal to the accepted terminal statistic. All iteration operators were legal, all finite and shape checks passed, maximum `A2max` was `0.001512876525478546`, and the observed linear-solve residual infinity norm ranged from `1.2539969063141143e-13` to `7.267352980554545e-08`. The accepted nonconvergence was therefore reproduced, so the mechanism classification gate was open.

The prior accepted J640 evidence persisted its terminal statistic but not a per-iteration trajectory. Exact terminal reproduction is established; broad trajectory agreement with that earlier J640 execution cannot be independently tested and is not claimed.

## Trajectory and event ordering

The convergence statistic began at `0.7728818908153778`, reached its minimum `0.00033741869262016166` at iteration 99, and rebounded to `0.0012277767122459426` at iteration 100. Across 99 adjacent changes, 61 were decreases and 38 were non-decreases. The largest rebound occurred at iteration 38, from `0.027322028168027535` to `0.10457186913488892`, an increase of `0.07724984096686138`.

The observed first-event order was:

1. policy/selector switching at iteration 2: liquid labels first changed at iteration 2 and transfer labels at iteration 3;
2. convergence-statistic non-decrease at iteration 8;
3. derivative-floor activation at iteration 10.

Selector changes remained positive in 95 iterations, with 12,656 liquid-label changes and 17,260 transfer-label changes in total. Derivative floors were active in 70 iterations, with a maximum combined 94 forward/backward liquid-derivative hits in one iteration.

This timing does not support monotone or near-monotone slow convergence. Selector switching and value oscillation begin before derivative-floor activation. The floor is therefore a later co-traveller or possible amplifier in this replay, not evidence of the initiating event. This is temporal evidence, not a causal intervention result.

## Repetition and cycle evidence

All 100 value hashes were unique. There was no exact value recurrence and no exact period-2 or period-3 value cycle. The minimum period-2 value infinity distance was `0.0010033517099476974` at iteration 89; the minimum period-3 distance was `0.0015429156775694786` at iteration 90.

There were 96 unique joint liquid/transfer selector hashes. The only recorded exact joint-label recurrence was one adjacent period-1 repeat from iteration 91 to 92. There was no exact period-2 or period-3 joint-label cycle. The evidence therefore does not support a repeating or low-period cycle classification.

## Mechanism classification and prior comparison

The most evidence-consistent preregistered class is:

`POLICY_OR_SELECTOR_CHATTER_WITH_VALUE_OSCILLATION`

The replay has persistent selector switching, repeated value-statistic rebounds, and a terminal rebound after the iteration-99 minimum. It is neither a monotone-slow path nor an exact low-period recurrence. Because switching and value non-decrease precede derivative-floor hits, the evidence does not select the floor-led class.

The ordering is broadly similar to the prior accepted turn1/turn2 mechanism evidence, where policy switching and value oscillation preceded stronger derivative-floor activity. This comparison is descriptive only. It does not establish that the two settings have an identical causal mechanism.

## Call ledger, evidence, and boundary

- J640 HJB: 1 started / 1 completed, exactly the authorized budget
- KFE: 0
- J1280: 0
- Scientific retries: 0
- Engineering retries: 1, pre-science and identity-plumbing only
- Global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results: all 0

Compact evidence is under `docs/evidence/ch5_mp4c_k1_j640_hjb_nonconvergence_mechanism_diagnostic/`. Its sealed manifest contains 8 entries totaling 79,016 bytes excluding the manifest. Raw iteration evidence is sealed under `D:\ProjectTemp\ch5-mp4c-k1-j640-hjb-mechanism-evidence-20260915-002`; its manifest contains 11 entries totaling 293,187 bytes excluding the manifest.

No KFE, J1280, longer iteration ceiling, damping, relaxation, line search, selector freezing, numerical/economic change, liquid-I ladder, multi-state grid, global model, firm runtime, MATLAB runtime, K1B, K2, GE, downstream, shock, IRF, or Results execution occurred.

Exactly one next Reviewer gate:

`REVIEWER_J640_HJB_MECHANISM_ROUTE_DECISION`
