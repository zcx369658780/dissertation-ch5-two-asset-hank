# CH5 MP4C K1 J160 provincial first-turn HJB viability freeze

Date: 2026-09-15.

## Purpose

Return from standalone grid diagnostics to the accepted multi-province route without reopening the unresolved KFE finite-box/pinning blocker.

## Frozen practical household grid

For this diagnostic only:

- `I=20`
- `J=160`
- `Nz=2`
- `a=[0,100]`
- `b=[-2,20]`
- diagnostic household monetary bridge `h=1`

This grid is accepted only as a practical bounded diagnostic grid. It is not continuum-converged or production-final.

## Input authority

Use the already accepted exact province-level first-turn household inputs from the prior multi-province mechanism/trajectory evidence. No new outer turn, firm solve, wage calculation, return recalibration, or parameter change is allowed. The diagnostic must read and seal the exact accepted per-province consumed household inputs, including `rb`, `ra/rah` input, composite household wage `w`, transfers/taxes and any other household-call inputs required by the accepted adapter.

If the exact accepted first-turn input vector cannot be recovered unambiguously from repository evidence, STOP before science.

## Science authority

Accepted MATLAB-faithful HJB science remains unchanged: equations, FOCs, selectors, boundary laws, derivative floors, pseudo-time step, sparse solve, tolerance `1e-7`, maxit `100`, legality gate `A2max<=0.01`, and fresh source-style initialization.

KFE is not authorized in this task. The unresolved corrected-2018 finite-box upper-b leakage / MATLAB-style pinning issue remains separate.

## Runtime

Exactly one fresh HJB per accepted province first-turn input, expected 31 calls if the authority vector contains 31 provinces. No warm starts and no scientific retries.

No global outer turn, firm runtime, wage runtime, MATLAB runtime, KFE, K1B, K2, GE, downstream, shock, IRF, or Results execution.

## Decision

If all authorized province HJB calls are legal/converged, the route may classify:

`J160_FIRST_TURN_PROVINCIAL_HJB_VIABILITY_PASS`

If any call fails, record exact province/input/mechanism-facing receipts and stop with a truthful bounded failure classification. Do not recalibrate within this task.

Results eligibility remains `FALSE`.