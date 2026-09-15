# CH5 MP4C K1 — household illiquid-grid finer precision escalation acceptance

Date: 2026-09-15

Reviewer verdict:

`FINER_PRECISION_ESCALATION_ACCEPTED__J320_VALID__J640_HJB_NONCONVERGENCE_BLOCKS_PRECISION_LADDER__MECHANISM_DIAGNOSTIC_REQUIRED`

Accepted Builder candidate: `e3db1ada75619a7db0139cef0da4aaabbb351690`.
Baseline: `3f4a87af4927643f2f80f407ed8b207d41fb8718`.
Results eligibility=`FALSE`.

## Independent review findings

The candidate is exactly one commit ahead of baseline and changes only the task-owned report/evidence, focused test, and task-owned validator package. No accepted HJB/KFE scientific source, oracle, MATLAB source, economic equation, parameter, guard, mapping, tolerance, or asset bound was modified.

Call ledger is accepted: J320 and J640 HJB were each called exactly once; only J320 proceeded to exactly one KFE; J1280 was not started after the invalid-point hard stop; scientific retries=0; engineering retries=0; all global/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results calls=0.

J320 is a valid new precision point: HJB converged in 44 iterations and KFE was valid. Relative to accepted J160, `Delta At=-0.12802605`, `Delta Bt=+0.00739550`, modal a moved `94.33962264 -> 95.29780564`, signed a-CDF distance was `0.0021292541`, and signed b-CDF distance was `0.0007585373`. `amax` mass remained zero and fixed-I20 `bmax` mass remained small (`0.0010587541`).

J640 is accepted as a numerical nonconvergence event, not as an economic/domain pathology: the HJB reached the frozen maxit=100 with final convergence statistic about `0.0012277767`, with no illegal iteration, hard error, or nonfinite/shape failure. Therefore KFE was correctly not run, and J1280 was correctly not started.

The evidence is insufficient to establish illiquid-grid stabilization, insufficient to define a smallest defensible stabilized J, and insufficient to attribute the J640 failure to domain/scale pathology. The old-domain to expanded-domain At jump remains primarily a domain-response finding, but the converged discretization component remains unresolved.

## Reviewer route decision

Do not extend maxit, change damping, change tolerance, modify HJB/KFE equations, or continue to J1280 yet. The next bounded task is a single J640 HJB mechanism replay at the identical frozen inputs and identical maxit=100, instrumented only to distinguish slow monotone convergence from policy/value oscillation, derivative-floor amplification, selector chatter, or another repeatable numerical mechanism.

That replay is diagnostic-only: no KFE, no J1280, no parameter/domain/solver changes, and no Results. It is not authority to 'fix' the HJB algorithm.
