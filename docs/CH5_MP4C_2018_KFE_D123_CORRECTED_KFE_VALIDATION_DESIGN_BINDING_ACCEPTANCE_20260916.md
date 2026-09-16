# CH5 MP4C 2018 KFE D1-D3 corrected KFE validation design/binding acceptance

Date: 2026-09-16

Reviewer verdict:

`PASS__Q0_OPERATOR_LEVEL_SOURCE_FREE_KFE_DESIGN_ACCEPTED__BOUNDED_PIN_FREE_VALIDATION_AUTHORIZED_NEXT`

## Accepted Builder candidate

- baseline: `99fd61a4bc66493e080491c910c7713f8c0ae6a1`
- candidate: `494dfc741dbf494a5b367b3abe99234a5708df4c`
- changed paths: exactly one report, `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_KFE_VALIDATION_DESIGN_BINDING_REPORT.md`
- scientific/model runtime in the design gate: zero

## Reviewer findings

The report correctly distinguishes the accepted pre-step operator `Q0` from any future post-step operator `Q1`. `Q0` is the identified generator of the complete accepted Option-A `V0` policy map and is therefore a scientifically proper object for a bounded operator-level invariant-mass/KFE validation. No `V1` policy remap is required for that operator claim.

A `V1` remap would answer a different question about post-step policy iteration and remains outside the next gate. A passing Q0 KFE validation must not be described as nonlinear HJB convergence, HJB-KFE fixed point, stationary economic equilibrium, production readiness, or Results evidence.

The accepted KFE contract is source-free and pin-free:

- backward generator orientation: rows are origins and `Q0 @ 1 = 0`;
- forward stationarity: `Q0.T @ p = 0`;
- probability mass vector `p`, with density view `g=p/omega`;
- uniform asset-cell weight `omega=(7/19)*(10/19)=70/361`;
- `(b,a,z)=(20,20,2)` and F-order, `b` fastest;
- no row replacement, no pin equation, no RHS/source injection, no balancing source;
- exactly one full dense `scipy.linalg.svd(..., lapack_driver="gesvd")` of `Q0.T`;
- only global sign orientation and one total-mass normalization are permitted;
- no negative-mass clipping, tolerance fitting, solver substitution, retry, iterative eigensolver, or row-replaced direct solve.

Uniqueness requires the conjunction of:

1. exactly one closed communicating class under exact-positive off-diagonal graph edges;
2. numerical rank `799` / nullity `1` at the preregistered prospective rank threshold;
3. second-smallest singular value strictly above that threshold;
4. source-free stationarity residual within prospective arithmetic bounds;
5. normalization and nonnegative-mass checks within prospective arithmetic bounds.

The accepted Q0 identity remains the D2 artifact from candidate `9a4eb0e5ec3627743596daa9b991436d2124efa9`, SHA-256 `093E1AF1ADFEEE5C50D3DD91EDDD678EBAC5BBA6C42E64DE73A63B82102AF1D5`.

## Next gate

A fresh bounded corrected-Q0 KFE operator-validation task is authorized. It may perform exactly one structural/conservation audit, one SCC decomposition, one dense `gesvd`, one normalized stationary-mass candidate, one `Q0 @ 1`, and one `Q0.T @ p` evaluation, under the report's 300-second / 2-GiB ceiling. All selector/root/policy-map/D2/HJB/V1-remap/MATLAB/downstream calls remain zero.

Results eligibility remains `FALSE`; production is unchanged.
