# Reviewer acceptance — J160 provincial first-turn HJB viability

Date: 2026-09-15

Verdict:

`J160_FIRST_TURN_PROVINCIAL_HJB_VIABILITY_BLOCKED_ACCEPTED__25_OF_31_CONVERGED__SIX_LEGAL_NONCONVERGENCES_REQUIRE_MECHANISM_PANEL_DIAGNOSTIC`

Accepted candidate: `1e9c8c6416cbd732a44d739e19b40e838993e3d4`.
Baseline: `ad5a05d6c4af76b26fa868eb58d8bac3a14157ce`.

The candidate is one direct commit ahead of the accepted baseline and is accepted as a truthful blocked scientific execution. It changes only task-owned report/evidence/tests/validators and does not change accepted household scientific source, equations, numerical tolerances, grid/domain, guards, mappings, or economic parameters.

Input authority PASS is accepted. The task recovered exactly 31 unique first-turn provincial household inputs from accepted sealed compact evidence, including consumed household `r_a/rah` and composite household wage `w`, without recomputing firm/wage/return mappings and without substituting raw `wjt` for household `w`.

At the practical household grid `I=20,J=160,a=[0,100],b=[-2,20]`, 25/31 provincial HJBs converged. Six provinces were legal but nonconverged at frozen maxit=100: 天津、山西、江西、重庆、贵州、甘肃. There were no illegal operators and no hard errors; all 31 maximum `A2max` values remained below the accepted `0.01` legality gate.

The six failures cannot be attributed merely to being outside the previous bounded standalone rectangle because all 31 real provincial states lie outside that rectangle while 25 converge. No KFE or outer-model conclusion is authorized.

Reviewer route decision: do not recalibrate yet and do not increase maxit or modify HJB. First classify the six legal nonconvergences with identical-input, instrumentation-only HJB diagnostic replays. The mechanism panel must distinguish slow/near-monotone convergence from policy/selector chatter with value oscillation, derivative-floor amplification, low-period recurrence, or heterogeneous/unresolved mechanisms across provinces.

Results eligibility remains `FALSE`.
