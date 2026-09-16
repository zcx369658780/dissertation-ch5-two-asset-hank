# CH5 MP4C 2018 KFE D1-D3 failed-cell algebraic attribution — Reviewer acceptance

Date: 2026-09-16
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

## Verdict

`PASS__FAILED_CELL_ATTRIBUTION_ACCEPTED__STRUCTURAL_INCOMPATIBILITY_OF_FROZEN_HISTORICAL_DERIVATIVES_CONFIRMED__NO_SELECTOR_OMISSION__DO_NOT_RERUN_SAME_PANEL`

Accepted Builder candidate: `602a96e6bb7a65cea5895fc1d6ee1887f7e5a0b5`.

The candidate is one commit ahead of fresh main `4eda840d71d2d22456744558196d76b301fc6130` and changes only `docs/CH5_MP4C_2018_KFE_D123_FAILED_CELL_ALGEBRAIC_ATTRIBUTION_REPORT.md`. Scientific/model call ledger is zero.

## Accepted findings

1. Cells 4 and 8 are structurally incompatible with the adopted corrected D1-D3 selector when fed the frozen historical MATLAB-faithful derivative state. At upper `b`, the only legal inward derivative is `p_b^B<0`. With the frozen upper-face law `q_b=p_b-lambda_b`, `lambda_b>=0`, both slack and active upper-b cases imply `q_b<=p_b^B<0`, contradicting the consumption FOC domain `q_b=c^{-gamma}>0`.
2. Cell 10 has a different structural conflict. The active-upper-b / negative-transfer / backward-a branch has a unique liquid-equality root `q_b=0.011097998989333606`, below the derivative-direction switch `q_switch=0.011142916892752`, leaving `g_a=+0.014015853975082537`; hence the root is outside the backward-a direction-consistent region. The direction-valid interval contains no second liquid-equality root under the accepted monotonicity argument.
3. The frozen selector did not omit a mathematically legal branch. The only Cell-10 combination not emitted as a full receipt candidate, active-negative/forward-a, is globally direction-inconsistent over the allowed multiplier domain.
4. The failure class is `ATTRIBUTED_STRUCTURAL_INCOMPATIBILITY_OF_FROZEN_DERIVATIVE_INPUTS`. It is not economic nonexistence, corrected-HJB nonexistence, HJB convergence failure, KFE failure, calibration evidence, or Results evidence.

## Route decision

Do not rerun or repair the same historical-derivative ten-cell panel. The historical derivative arrays are evidence objects from the MATLAB-faithful path and are not a corrected-target fixed point.

Before any corrected-target HJB execution, Reviewer requires one zero-science design/binding gate to freeze the exact corrected-HJB seed/value object, grid, derivative construction, prices/calibration, policy-map semantics, direct-solve equation, scientific-call budget, stop conditions, and evidence contract. If repository authority cannot supply a unique scientifically defensible seed/initialization without a new substantive choice, the design gate must fail closed and return that choice to Owner.

Production replacement and Results eligibility remain unauthorized. Results eligibility=`FALSE`.
