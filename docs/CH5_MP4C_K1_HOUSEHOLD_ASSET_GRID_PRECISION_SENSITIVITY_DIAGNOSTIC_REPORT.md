# CH5 MP4C K1 — household asset-grid precision sensitivity diagnostic report

Date: 2026-09-15

Task ID: `CH5_MP4C_K1_HOUSEHOLD_ASSET_GRID_PRECISION_SENSITIVITY_DIAGNOSTIC`

## Terminal classification

`P1_KFE_EVIDENCE_UNAVAILABLE__NO_SCIENTIFIC_RETRY_AUTHORIZED`

The mandatory P1 HJB ladder completed exactly once and all three HJBs were legal and converged. Each authorized KFE numeric solve returned into the accepted wrapper, but the wrapper then rejected the finer-grid result with `ValueError: expected the frozen 20-bin illiquid marginal`. No finer-grid density or aggregate receipt survived the exception. Scientific retries were frozen at zero, so P1 precision stability is unresolved and P2 was not triggered.

This is partial diagnostic evidence only. It is not evidence of illiquid-grid instability, liquid-grid stability, recalibration need, production adequacy, or Results authority. `Results eligibility=FALSE`.

## Repository and execution identity

- Actual fresh-fetched baseline: `2f1c12fadbef438f8b3895f309730b2aca8fb45e`.
- Branch: `codex/ch5-mp4c-k1-household-asset-grid-precision-20260915`.
- Fresh isolated worktree: `D:\ProjectTemp\ch5-mp4c-k1-household-asset-grid-precision-20260915-001`.
- P1 raw evidence: `D:\ProjectTemp\ch5-mp4c-k1-household-asset-grid-precision-p1-evidence-20260915-001`.
- P2 raw evidence root was not created.
- Compact evidence: `docs/evidence/ch5_mp4c_k1_household_asset_grid_precision_sensitivity/`.
- Frozen oracle SHA-256: `F6007C1166C951B4A0C98B0FBF551921A2664D2E3943E7D77F847634261524F8`.
- Frozen MATLAB source SHA-256: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`.

## Frozen input and accepted reference

The run held `rb=.02`, `ra=.0675`, `w=15.5`, `a=[0,100]`, `b=[-2,20]`, and diagnostic bridge `h=1` fixed. It changed only the authorized grid density. All three points used distinct fresh `source_initial_arrays` constructions and no warm start. Household equations, parameters, guards, derivative floor, solver, tolerance, maximum iterations, return/wage mapping, and KFE equation were unchanged.

The accepted `I=20,J=20` point was read from Stage A evidence without a science call: `At=87.75417323082814`, `Bt=4.155471670682324`, `Ct=13.390598980244727`, `Lt=0.6213645307498707`, modal `a=89.47368421052633`, modal `b=2.6315789473684212`, `amax` mass `0.14305021595858766`, and `bmax` mass `6.511042142674138e-34`.

## P1 execution

| I | J | da | HJB class | iterations | final `max|ΔV|` | max A2max | KFE route |
|---:|---:|---:|---|---:|---:|---:|---|
| 20 | 40 | 2.5641025641025643 | `HJB_CONVERGED` | 11 | 2.304627599869491e-10 | 0.0015128765254773247 | numeric solve returned; J20-only postprocessor rejected |
| 20 | 80 | 1.2658227848101267 | `HJB_CONVERGED` | 10 | 3.3535032306630796e-08 | 0.0015128765254773247 | numeric solve returned; J20-only postprocessor rejected |
| 20 | 160 | 0.6289308176100629 | `HJB_CONVERGED` | 16 | 2.2613111383407158e-10 | 0.0015128765254778798 | numeric solve returned; J20-only postprocessor rejected |

No HJB had a first illegal iteration. The failure occurred after the underlying KFE solve returned, when the reused Stage-A wrapper required the illiquid marginal to have exactly 20 bins. Because the returned KFE objects were not persisted before that exception, offline finalization cannot reconstruct `At/Bt/Ct/Lt`, density, endpoint masses, modes, top bins, or full marginals without another KFE call. Such a call would be a prohibited scientific retry.

## Precision comparisons and decisions

The preregistered `J20→J40`, `J40→J80`, and `J80→J160` comparisons are explicitly marked unavailable in `precision_comparison.json`. The deterministic metric remains frozen as the support-width-normalized integral of absolute differences between piecewise-linearly interpolated raw signed marginal CDFs, with no clipping, renormalization, or post-result pass threshold; it could not be evaluated for the missing finer-grid marginals.

- `At` stabilization as J rises: unresolved.
- Modal `a` stabilization: unresolved.
- Full `a` marginal-shape stabilization: unresolved.
- `amax` mass stabilization or decline: unresolved.
- Old-domain to expanded-domain `At` jump: accepted evidence still establishes a major domain/discretization response, not GE or calibration improvement; this failed precision run cannot separate the remaining coarse-grid component.
- P1 decision: `ILLIQUID_GRID_PRECISION_UNRESOLVED__KFE_EVIDENCE_UNAVAILABLE`. It is deliberately not relabeled `ILLIQUID_GRID_PRECISION_NOT_STABILIZED` because no pairwise KFE evidence exists.
- P2 trigger: `false`; P2 HJB=0 and KFE=0.
- `Bt` and liquid marginal stability over I: not checked.
- Whether `bmax=20` remains nonbinding at finer precision: not checked; only accepted `I=J=20` evidence remains valid.
- Minimum numerically defensible next grid: unresolved; no cross-state grid can be recommended from this evidence.

## Call ledger and protected zeroes

- Accepted reference: HJB=0, KFE=0.
- P1: HJB started/completed=3/3; KFE started=3, complete persisted receipts=0.
- P2: HJB=0, KFE=0.
- Scientific retries=0; engineering retries=0.
- Global outer/firm/MATLAB/K1B/K2/GE/downstream/shock/IRF/Results=0.
- No unauthorized I/J point, no warm start, and no full finer 3×3 run occurred.

## Evidence and caveat

Required compact files are present and sealed by `sealed_manifest_sha256.json`; the manifest covers 10 files and 68,630 bytes excluding itself. Raw P1 evidence is separately sealed. `point_receipts.json` preserves each exact error, and `call_ledger.json` distinguishes started KFE calls from completed persisted receipts.

The KFE remains the accepted standalone contaminated-row diagnostic route. It does not resolve corrected-2018 multi-province finite-box upper-b leakage or MATLAB-style pinning, and no signed density was clipped.

## Exactly one next Reviewer gate

`REVIEWER_ROUTE_REPAIR_DECISION`

The independent Reviewer must decide whether a fresh exact task may replace the J20-only postprocessor with grid-generic receipt extraction and rerun the same frozen P1 ladder. No repair, rerun, finer escalation, multi-state confirmation, recalibration, merge, or successor-task publication is authorized by this Builder candidate.
