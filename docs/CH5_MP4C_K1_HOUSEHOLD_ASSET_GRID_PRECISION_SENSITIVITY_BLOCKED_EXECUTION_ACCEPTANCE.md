# CH5 MP4C K1 — household asset-grid precision sensitivity blocked-execution acceptance

Date: 2026-09-15

Reviewer verdict:

`P1_KFE_EVIDENCE_UNAVAILABLE_BLOCKED_EXECUTION_ACCEPTED__GRID_GENERIC_RECEIPT_REPAIR_REQUIRED`

Accepted Builder candidate: `e3b470f623232fcaf52ad50474178f79a2b0b9b9`.

## Independent review

Fresh live `main` was `2f1c12fadbef438f8b3895f309730b2aca8fb45e`. The candidate is exactly one commit ahead of that baseline and changes only task-owned report/CURRENT closeout/evidence/tests/validator files. No accepted scientific source, HJB/KFE equation, solver/tolerance, wage/return mapping, economic domain, guard, GE path, Results path or MATLAB source was modified.

The mandatory P1 ladder executed only the authorized points `I=20,J={40,80,160}`. All three HJB solves were legal and converged. Each KFE call started and the numerical solve returned, but the inherited receipt/postprocessing route subsequently rejected the result because it assumed a frozen 20-bin illiquid marginal. No valid finer-grid density/aggregate/marginal receipt survived that exception. Scientific retries remained zero and P2 correctly did not run.

The candidate is accepted as a truthful blocked-execution record. It is not accepted as evidence for illiquid-grid instability, liquid-grid stability, production adequacy, recalibration need, or Results eligibility.

## Root-cause classification

The failure is a diagnostic wrapper/receipt-shape defect, not evidence of an HJB or KFE scientific failure. The next task may make the receipt extraction grid-generic, provided the accepted standalone KFE numerical solve and all economic/scientific inputs remain unchanged.

## Authorized next route

Publish one fresh exact task that:

1. repairs only task-owned receipt/postprocessing logic so arbitrary authorized `I/J` lengths are supported;
2. adds focused tests proving `J=20,40,80,160` receipt extraction without hard-coded bin counts;
3. reruns the same frozen P1 ladder from fresh initialization;
4. treats the rerun as a new authorized science execution, not as a retry hidden inside the failed task;
5. enters P2 only if the original preregistered P1 stabilization condition is satisfied;
6. makes no change to accepted household equations, KFE solver, HJB solver, parameters, bounds, mapping, guards or Results eligibility.

Results eligibility remains `FALSE`.
