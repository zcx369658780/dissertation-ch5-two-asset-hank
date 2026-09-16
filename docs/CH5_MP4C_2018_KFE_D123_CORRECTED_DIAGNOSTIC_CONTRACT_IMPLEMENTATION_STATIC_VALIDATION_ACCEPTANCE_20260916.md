# Chapter 5 MP4C 2018 KFE D1-D3 corrected diagnostic contract implementation — Reviewer acceptance

Date: 2026-09-16
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
Reviewer verdict: `PASS__D123_STATIC_CONTRACT_IMPLEMENTATION_ACCEPTED__TINY_REAL_CELL_SELECTOR_PANEL_AUTHORIZED_NEXT__PRODUCTION_UNCHANGED`

Accepted Builder candidate: `d8cc627d23172b17d3f4dafce0a5f41886c9815d`.
Fresh-start main for that task: `5360df95aae2bdb6a77032c35bf2276720803e8d`.

## Acceptance basis

The candidate is one commit ahead of its fresh main and changes only the isolated corrected-diagnostic namespace, focused tests, one evidence JSON, and one report. No existing source-faithful or production implementation file changes.

The isolated implementation faithfully represents the Owner-adopted diagnostic contracts at this gate:

- D1: joint face/corner admissibility checking with distinct economic lower bounds and artificial upper numerical state constraints; outward closed-face consumed drift fails explicitly with no clipping or silent edge deletion.
- D2: consumed-total-drift generator assembly using actual adjacent distances, nonnegative retained rates and diagonal equal to the negative retained outgoing-rate sum. On tested admissible arithmetic, `Q @ 1` closes at floating-point scale and coordinate action reproduces the supplied consumed drifts.
- D3: the adjustment cost, subgradient and transfer KKT use the same `s(a)=max(a,a_bar)` throughout the domain, including `a=0`, with no derivative floor, transfer cap, new coefficient or alternative adjustment technology.

The accepted static evidence includes `24 passed`, `py_compile` PASS, empty frozen-reference diff, minimum tested offdiagonal `0.05714285714285715`, diagonal-construction error `0`, `max(abs(Q @ 1))=1.1102230246251565e-16` below the prospective arithmetic bound `4.973799150320706e-15`, and coordinate errors at machine scale.

The 14 hash-bound saved-control snapshots are also correctly used as negative assembler inputs: all receipts match, and all 14 are rejected before assembly because the persisted legacy consumed drifts contain 365 closed-face violations (upper-b 139, upper-a 226, lower faces 0). This is expected evidence that the new assembler does not silently repair legacy policies; it is not evidence that the corrected selector can yet generate admissible policies.

Scientific/model calls for the static task are accepted as exactly zero.

## Acceptance boundary

This acceptance establishes only the isolated D1-D3 contract implementation and static/saved-control behavior. It does not establish real-cell selector correctness, HJB convergence, KFE existence/nonnegativity/uniqueness, pin-row redundancy, production replacement, GE/annual/IRF validity, or Results eligibility.

The next allowed gate is the preregistered ten-cell corrected-target selector panel only. One target HJB step and every KFE solve remain unauthorized until that panel is independently reviewed.

Results eligibility=`FALSE`.
