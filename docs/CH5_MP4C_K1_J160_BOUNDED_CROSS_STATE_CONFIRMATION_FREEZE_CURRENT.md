# CH5 MP4C K1 — J160 bounded cross-state confirmation freeze

Date: 2026-09-15

Status: active freeze.

Purpose: confirm whether the provisional practical illiquid-grid density `J=160` remains numerically usable across representative real-wage/return states after the finer-J route was closed by reproducible J640 policy/selector chatter.

Frozen household science:

- `rb=.02`
- `a=[0,100]`
- `b=[-2,20]`
- `I=20`
- `J=160`
- `Nz=2`
- diagnostic bridge `h=1`
- accepted MATLAB-faithful HJB/KFE equations, initialization, FOCs, selectors, boundaries, derivative floors, solver, tolerance `1e-7`, maxit `100`, KFE method, mappings and guards unchanged.

Cross-state points:

1. `ra=.06, w=13`
2. `ra=.06, w=18`
3. `ra=.0675, w=15.5` — accepted central reference, reuse only
4. `ra=.07, w=13`
5. `ra=.07, w=18`

Exactly four new science points are authorized; the center is reused without runtime.

The accepted J20 same-state points from the prior real-wage 3x3 scan are comparison references only and must not be rerun.

Decision principle:

This task does not attempt continuum-grid convergence. It asks whether J160 is a robust practical diagnostic grid across a bounded set of economically relevant states. J320 remains a one-point sensitivity check at the center; J640/J1280 are closed under the current algorithm.

Hard stops:

- no J other than 160;
- no I change;
- no maxit increase;
- no damping/relaxation/line search;
- no parameter, wage, return, domain, tolerance, floor, selector or solver changes;
- no global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results runtime.

Results eligibility remains `FALSE`.
