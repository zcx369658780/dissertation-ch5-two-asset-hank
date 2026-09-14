# CH5 MP4C K1 — household asset-grid precision receipt repair freeze

Date: 2026-09-15

Status: `GRID_GENERIC_RECEIPT_REPAIR_AND_FROZEN_P1_REEXECUTION_AUTHORIZED`

This freeze follows accepted blocked execution `e3b470f623232fcaf52ad50474178f79a2b0b9b9` and Reviewer acceptance `docs/CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_BLOCKED_EXECUTION_ACCEPTANCE.md`.

## Frozen science

Representative state remains exactly:

- `rb=.02`
- `ra=.0675`
- `w=15.5`
- `amin=0`, `amax=100`
- `bmin=-2`, `bmax=20`
- diagnostic bridge `h=1`
- no warm start

Accepted HJB/KFE equations, solver, tolerance, maximum iterations, FOC/selector/boundary logic, derivative floor, wage/return mapping, source initialization and contaminated-row standalone KFE numerical solve are immutable in this task.

## Authorized engineering repair

The only scientific-interface repair is to remove the fixed-20-bin assumption from task-owned receipt/postprocessing extraction. Receipt code must derive `I/J`, asset supports and marginal lengths from the actual authorized fixture/result and preserve the complete returned density before any validation that depends on grid size.

The repair must not alter the KFE numerical solve itself. It must not clip, renormalize, smooth or otherwise modify the raw signed density beyond the already accepted receipt calculations.

Focused tests must demonstrate grid-generic extraction for authorized `J=20,40,80,160`; where relevant they should also prove liquid marginal handling for `I=20,40,80`.

## Frozen re-execution ladder

P1 re-execution is exactly:

- reuse accepted `I=20,J=20` Stage A reference without science rerun;
- new fresh `I=20,J=40`;
- new fresh `I=20,J=80`;
- new fresh `I=20,J=160`.

Exactly one HJB and, if legal/converged, one KFE per new P1 point. Scientific retries inside this fresh task remain zero.

P2 is conditional exactly as previously frozen: only if P1 descriptively stabilizes by `J=160`, reuse `I=20,J=160` and run fresh `I=40,J=160` and `I=80,J=160`.

No finer points and no full cross-state grid are authorized.

## Interpretation guard

The previous blocked execution remains a wrapper-evidence failure, not grid-instability evidence. Only the fresh repaired execution may answer the original precision questions.

Results eligibility remains `FALSE`.
