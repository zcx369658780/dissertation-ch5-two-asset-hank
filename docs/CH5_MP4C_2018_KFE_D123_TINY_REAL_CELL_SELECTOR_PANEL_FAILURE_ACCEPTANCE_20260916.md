# CH5 MP4C 2018 KFE D1-D3 tiny real-cell selector panel failure acceptance

Date: 2026-09-16

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Reviewer verdict:

`ACCEPT_FAIL_CLOSED_EVIDENCE__CELL2_ACTIVE_EQUALITY_REPRESENTATION_MISMATCH_IDENTIFIED__FRESH_REPAIR_AND_REEXECUTION_REQUIRED`

Builder candidate `05082f8af82afc90b8c0c168d9aeb8f345f8336a` is accepted as a valid fail-closed execution record, not as a ten-cell scientific PASS.

## Accepted facts

- Candidate is one commit ahead of its fresh baseline `c525d6671519f6a62608ba3b02211010f2327e56`; the changed paths are confined to the isolated corrected-diagnostic selector/panel implementation, focused tests, evidence and report.
- Exact ten-cell panel identity/provenance was recovered before scientific execution.
- Synthetic preflight passed (`29 passed`), code was frozen before the first real selector call, and post-stop hashes remained unchanged.
- Cell 1 produced a selected admissible D1/D3 policy and passed the strict D2 assembler.
- Cell 2 selector returned an upper-`b` active-equality residual `g_b=2.162339589068668e-16`. The selector admitted this under its prospectively defined floating arithmetic equality bound, while the adopted D2 assembler correctly rejects every strictly outward upper-face input at zero sign tolerance.
- Execution stopped immediately after 2 selector evaluations / 8 scalar-root invocations, with no retry and no HJB/KFE/MATLAB/outer/GE/annual/IRF/Results call.
- Cells 3-10 carry no scientific result.

## Reviewer disposition

The Cell 2 event is classified as an **implementation representation-contract mismatch**, not evidence that the corrected economic/KKT contract lacks an admissible policy. The adopted D2 zero-sign boundary contract remains unchanged and must not be relaxed.

For a face that is explicitly selected **active**, the mathematical state-constraint equality is `g_i=0`. A future corrected selector may canonicalize the final consumed drift on that active face to exact floating `0.0` only after the raw equality residual has been computed and shown to lie within the already preregistered prospective arithmetic bound. The raw residual, the bound, and the canonicalized value must all be persisted. This is an equality representation rule for an already active constraint; it is not clipping, projection, tolerance-fitting, reflection, or slack-face drift repair.

For a slack/inactive face, the raw drift must remain unchanged and D2's strict zero-tolerance outward-sign rejection continues to apply. A raw active-equality residual outside the prospective bound must reject that candidate; it cannot be canonicalized.

The second implementation defect is evidence ordering: the complete selector result/comparison set must be durably persisted before invoking the D2 post-selection check, so any later D2 rejection retains the selector evidence without rerunning the cell.

## Next gate

A fresh exact task may repair only these two implementation issues, rerun synthetic tests, freeze code, and then reexecute the same exact ten-cell panel under a new budget. Because scientific code changes before the new run, all ten cells must be evaluated anew under that new task; prior Cell 1 remains historical evidence only.

No HJB step or KFE solve is authorized. Production/source-faithful paths remain unchanged. Results eligibility=`FALSE`.
