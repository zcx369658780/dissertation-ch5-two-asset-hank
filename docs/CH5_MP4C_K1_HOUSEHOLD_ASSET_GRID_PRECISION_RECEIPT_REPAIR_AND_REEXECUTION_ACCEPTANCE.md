# CH5 MP4C K1 — household asset-grid precision receipt repair and re-execution acceptance

Date: 2026-09-15

Reviewer verdict:

`GRID_GENERIC_RECEIPT_REPAIR_ACCEPTED__ILLIQUID_GRID_PRECISION_NOT_STABILIZED__FINER_PRECISION_ESCALATION_REQUIRED`

## Repository acceptance

Accepted Builder candidate: `de4994c22303e30be9cd4c22c0a5c7f7a00db88a`.

Fresh review confirmed that the candidate is exactly one commit ahead of baseline `03f30ada29ef7cea8dd0ab8f27b090df607c0909` and changes only the task-owned report/current-state docs, compact evidence, focused tests, and the precision validator runner/finalizer. No accepted HJB/KFE scientific solver, oracle, protected MATLAB source, economic equation, asset bound, wage/return mapping, guard, rate, solver tolerance, or Results authority was modified.

The candidate is accepted and fast-forwarded into `main`.

## R0 acceptance

The grid-generic receipt repair is accepted as an engineering repair only.

The repaired path:

- derives illiquid marginal length/support from actual `J/grid.a`;
- derives liquid marginal length/support from actual `I/grid.b`;
- preserves raw signed density without clipping/smoothing/science-changing renormalization;
- persists HJB/KFE scientific arrays and actual grid supports before receipt validation;
- preserves accepted J20 receipt semantics;
- leaves the accepted numerical KFE solve unchanged.

Focused tests reported `17 passed`; R0 scientific runtime was HJB=0, KFE=0.

## P1 scientific acceptance

Frozen representative state:

- `rb=.02`
- `ra=.0675`
- household composite `w=15.5`
- `a=[0,100]`
- `b=[-2,20]`
- `h=1`
- `I=20`

Accepted J20 reference plus fresh `J={40,80,160}` evidence shows:

- HJB legal/converged for all three new points;
- KFE numeric-returned/persisted/valid for all three new points;
- scientific retries=0;
- P2 correctly did not run.

Key refinement sequence:

- `At`: `87.75417 -> 87.55005 -> 88.60704 -> 89.29783`;
- modal `a`: `89.47368 -> 89.74359 -> 92.40506 -> 94.33962`;
- a-CDF distances: `0.01261 -> 0.01760 -> 0.01462`;
- `J80->J160` still changes `At` by about `+0.69079`, `Bt` by about `+0.78798`, and modal `a` by about `+1.93456`.

The final refinement therefore remains materially active and does not establish a stabilization trend. The terminal classification `ILLIQUID_GRID_PRECISION_NOT_STABILIZED` is accepted.

## Scientific interpretation

The old `a=[0,10]` to expanded `a=[0,100]` jump is now supported as primarily a domain response, because finer J on the expanded domain keeps `At` near the high-80s rather than returning toward the old 7-range. However, the final expanded-domain level is still not precision-stable by J160.

`amax` mass falling to zero is not sufficient to claim convergence because modal `a`, `At`, `Bt`, and full marginal distances continue to move.

At fixed `I=20`, `bmax=20` remains nonmodal across the tested P1 ladder and endpoint mass remains small, but no I-grid precision authority exists yet.

This remains standalone contaminated-row KFE diagnostic evidence only. It does not resolve corrected-2018 multi-province finite-box upper-b leakage / MATLAB-style pinning, does not authorize recalibration, and does not make Results eligible.

## Reviewer route decision

The next bounded numerical route is `FINER_PRECISION_ESCALATION`.

A new exact task must continue the same representative state with the same domains and science, using accepted J160 as the reference and only the pre-registered finer illiquid grid ladder `J={320,640,1280}` at `I=20`.

No liquid-I ladder, cross-state grid, asset-domain change, HJB/KFE change, wage/return recalibration, or J beyond 1280 is authorized in that task.

Results eligibility remains `FALSE`.
