# CH5 MP4C 2018 KFE D1-D3 bounded nonlinear continuation fail-closed acceptance

Date: 2026-09-17

Reviewer verdict:

`PASS__FAIL_CLOSED_CONTINUATION_EVIDENCE_ACCEPTED__V1_TO_V2_LINEAR_STEP_VALID__V2_CELL100_NO_ADMISSIBLE_POLICY_REQUIRES_ZERO_SCIENCE_ATTRIBUTION`

## Accepted candidate

- baseline: `a0ccb9801abc5bda4357c59ae2ab51acb273a34b`
- Builder candidate: `922cd9118d617c044209515762ccecc9ec3fd34d`
- candidate was exactly one commit ahead of baseline and zero behind before Reviewer fast-forward
- Builder terminal verdict: `FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`

## Accepted facts

1. Exact accepted checkpoint 1 was reused without rerunning the V1 policy map.
2. Checkpoint 1 fails the Owner convergence law:
   - `B1 = 0.014710294187010184 > 1e-8`
   - `D1 = 0.47118375690461445 > 1e-7`.
3. Exactly one authorized direct HJB update `V1 -> V2` was executed with fixed `Delta=1000`.
4. The solve passed the frozen linear accuracy gate:
   - original-equation residual infinity norm `1.9012569296705806e-14`
   - normwise backward error `2.5514110567283015e-16 <= 1e-12`
   - V2 field SHA-256 `A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.
5. The fresh V2 policy remap stopped at the first scientific gate failure after cells 0-99 passed:
   - flat F index `100`
   - zero-based `(i_b,i_a,i_z)=(0,5,0)`
   - physical `(b,a,z)=(-2.0,2.6315789473684212,0.8)`
   - outcome `NO_ADMISSIBLE_POLICY`
   - admissible comparison count `0`.
6. No complete P2/u2 exists, no Q2/D2 assembly exists, and B2/D2/cycle/KFE metrics are not computed.
7. No scientific retry, solver substitution, damping, relaxation, adaptive Delta, continuation, MATLAB, production, GE, IRF or Results call occurred.
8. Sealed evidence and scientific-code freeze are accepted as fail-closed evidence. Results eligibility remains `FALSE`.

## Scientific interpretation

This acceptance does **not** establish nonlinear HJB nonexistence. It establishes only that the currently frozen corrected selector has no admissible policy at the first V2 failing cell under the current same-value derivatives and frozen D1/D3/lower-a-zero-kink/interior-Z laws.

The V1->V2 linear solve itself is numerically valid. Therefore the next scientific question is local: why the V2 cell `(0,5,0)` has no admissible selector branch.

The raw receipt records rejection mechanisms including derivative-direction inconsistency, lower-b primal infeasibility, transfer-KKT/sign failures, and a `ROOT_FAILURE_NO_UNIQUE_BRACKET`. These raw reasons are evidence to attribute; they are not permission to modify the selector or equations.

## Next gate

Authorize a **zero-science forensic attribution only** for V2 flat 100 and the immediately relevant neighboring/branch evidence. No new selector/root/policy-map/D2/HJB/KFE scientific call is permitted in that attribution gate.

The attribution must determine whether the failure is:

- a complete and genuine incompatibility of the frozen local derivative/KKT inputs;
- an omitted legal candidate/active-set branch in the selector;
- a numerical root/bracketing implementation omission within an already-authorized branch;
- or an unresolved scientific-law conflict requiring Owner decision.

No repair or runtime rerun is authorized until that attribution is independently accepted.
