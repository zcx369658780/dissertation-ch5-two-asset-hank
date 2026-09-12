# Chapter 5 MP4C K1 raw `ra0` payoff common-turn-1 bootstrap safety acceptance

Date: 2026-09-12.

Reviewer verdict:

`RAW_RA0_PAYOFF_SHORT_HORIZON_RUNTIME_SAFETY_ACCEPTED_WITH_COMMON_TURN1_BOOTSTRAP__EXECUTABLE_BUT_NUMERICALLY_STRESSED__NOT_READY_FOR_K1B_OR_LONGER_RUNTIME`

Accepted candidate:

`678860073d3d5b653b8863b71f494f569960ced7`

## Scope accepted

This acceptance covers only the bounded five-turn Control/Raw runtime-safety diagnostic under the Owner-frozen common-turn-1 bootstrap. The candidate is one commit ahead of baseline `9f973e627a3b7c7acac1d78c1b18b68a0c4a16c0`; no production `src/` science implementation was changed. The tracked changes are task-bounded runner/finalizer/test/evidence/report artifacts.

## Accepted execution evidence

- Control and Raw both completed 5/5 outer turns;
- turn 1 was exactly common bootstrap using clipped/source-used `ra`;
- all compared saved household/HJB arrays and province aggregates at turn 1 were identical;
- Raw turns 2-5 used only the same path's immediately prior completed firm `ra0 @ S`;
- Control turns 2-5 used the same path's immediately prior completed used/clipped `ra @ S`;
- no cross-path borrowing and no same-turn return feedback occurred;
- total trajectory invocations: 2;
- total HJB/KFE calls: 310/310;
- scientific retries: 0;
- K1B/K2/MATLAB/GE/annual/shock/IRF/Results calls: 0;
- manifest readback: 1041/1041 PASS, SHA-256 `69E85A9CAF6A23F5B7402821112F1A0465E2617F8A44ACEE167BC61D25B1E644`.

## Runtime-safety finding accepted

The permitted classification `RAW_RA0_PAYOFF_SHORT_HORIZON_RUNTIME_SAFETY_SUPPORTED_WITH_COMMON_TURN1_BOOTSTRAP` is accepted in its narrow hard-stop sense: the Raw route remained executable for all four authorized treatment turns without NaN/Inf, scientific exception, same-`S` failure, K1 capital-accounting failure, C1 accounting failure, or provenance violation.

This establishes a real short-horizon raw-payoff mechanism path. It does not establish numerical convergence, stable policies, economic admissibility, steady state, KFE validity, K1B/K2 validity, or Results eligibility.

## Numerical-stress finding accepted

The same evidence shows severe numerical/control stress after raw payoff first enters at turn 2:

- treatment-horizon HJB convergence: Control `49/124`, Raw `12/124`;
- Raw turn 5: `0/31` HJB returns converged;
- Raw median entering `rah` is about 5.3-5.6 times Control over turns 2-5;
- Raw max HJB statistics rise to roughly `403.7`, `98.9`, `152.7`, `297.0` over turns 2-5 versus much smaller Control values;
- Raw maximum absolute liquid drift reaches about `1.29e12` and maximum absolute illiquid transfer about `2.74e6`;
- Raw lower-`b` outward raw-drift counts become nonzero while Control remains zero.

These finite magnitudes do not trigger the prior task's hard-stop conditions, so they do not invalidate the narrow runtime-safety classification. They do, however, block any interpretation of the four-turn Raw path as a numerically stable quantitative policy solution.

## Mechanism-evidence ruling

The severe finite nonconvergence and drift sensitivity are acceptable as **short-horizon mechanism evidence only** because:

1. the bootstrap/provenance design isolates the payoff-source switch cleanly;
2. the Raw treatment produces the predicted large `rah` level change immediately at turn 2;
3. accounting and provenance remain exact while numerical stress worsens sharply;
4. therefore the evidence identifies that the raw-payoff level itself materially changes household numerical behavior.

The same evidence is not acceptable as a basis for longer-horizon quantitative conclusions or for activating K1B.

## Next gate

Before any additional raw-payoff runtime, 25-turn extension, or K1B activation, perform a zero-science forensic using only the accepted persisted Control/Raw evidence and source code. The forensic must localize the raw-payoff-induced HJB/drift amplification by province, turn, state-grid region and existing boundary/policy labels; distinguish baseline large-drift behavior from incremental Raw amplification; and identify whether the observed stress is best classified as payoff-scale exposure, boundary-law interaction, or an unresolved numerical/model-authority issue.

No solver/tolerance/grid/cap/parameter/payoff change is authorized by this acceptance.

All corrected-2018 KFE observations remain `DIAGNOSTIC_ONLY`; finite-box upper-`b` leakage plus MATLAB-style pinning remains an independent blocker.

Results eligibility remains `FALSE`.
