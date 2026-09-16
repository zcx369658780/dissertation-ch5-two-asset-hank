# CH5 MP4C 2018 KFE D1-D3 Option A first-cell fail-closed — Reviewer acceptance

Date: 2026-09-16
Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

## Verdict

`PASS__OPTION_A_FAIL_CLOSED_EVIDENCE_ACCEPTED__LOWER_A_ACTIVE_ZERO_KINK_MULTIPLIER_BRANCH_OMISSION_IDENTIFIED__FRESH_REPAIR_REEXECUTION_REQUIRED`

Accepted Builder candidate: `ef05a6c52c3cbe42d8e5404b6f51f0aa7c635d9e`.

The candidate is one commit ahead of baseline `3425ec22027697e95ff220cdb142323113aed136`. It correctly stopped at the first Option-A F-order cell after one real selector evaluation and four scalar roots, with zero D2 assemblies, zero HJB solves, zero retries and zero downstream calls. The evidence and code-freeze record are accepted as a valid fail-closed execution record. It is not accepted as evidence that Option A itself or the corrected HJB has no admissible policy.

## Reviewer finding

The complete first-cell receipt and frozen selector source expose a specific selector enumeration/representation omission at the lower-`a` active zero-transfer kink.

At Cell `(0,0,0)`, `a=0`, `p_a^F=0`, `p_b^F=q_b=0.023046602641887657`, and the lower-`a` state constraint is eligible to be active. For an active lower face the frozen KKT law is

`q_a = p_a + lambda_a`, with `lambda_a >= 0`.

Because `a=0`, lower-`a` equality requires `d=0`. Under the D3 zero-transfer kink the transfer KKT requires

`q_a / q_b in [1-chi_0, 1+chi_0] = [0.9,1.1]`.

Therefore the admissible shadow interval is

`q_a in [0.020741942377698892, 0.025351262906076425]`,

while the multiplier law permits every `q_a >= p_a=0`. The intersection is nonempty. The frozen selector, however, sets `q_a=p_a` whenever `a_active` and `regime==zero_kink`, so it fixes `q_a=0`, records `lambda_a=0`, and rejects the candidate only for `TRANSFER_KKT_RESIDUAL`. This does not enumerate the legal positive lower-`a` multiplier branch.

The omission is visible directly in the accepted source: the active-zero-kink branch assigns `q_a=p_a`, whereas nonzero transfer active branches solve the transfer relation through the shadow value. The subsequent multiplier is computed only after that fixed `q_a` has already been chosen.

## Frozen scientific interpretation

This is a selector implementation/enumeration defect under the already adopted D1/D3 KKT law; it does not require a new economic law, new calibration, derivative floor, transfer cap, tolerance change, grid change or seed change.

For active lower-`a` at the zero kink, the corrected selector must represent the existing KKT set rather than force `lambda_a=0`. A deterministic canonical representative is permitted because all feasible `q_a` values in the intersection generate the same consumed policy when `g_a=d=0`. The repair must use the minimum feasible shadow

`q_a = max(p_a, q_b*(1-chi_0))`

provided this value is no larger than `q_b*(1+chi_0)` within the prospectively frozen arithmetic rule. Then `lambda_a=q_a-p_a>=0`. If the intersection is empty, the candidate remains fail-closed. This is a multiplier/shadow representation rule only; it does not alter `c,l,d,cost,g_b,g_a` or D2 semantics.

No generic multiplier projection is authorized for other branches. In particular, slack faces remain `lambda=0`; active nonzero-transfer branches retain the existing transfer-equality law; D2 strict outward-face zero tolerance remains unchanged.

## Route decision

Do not switch seeds based on this outcome. Option A remains the Owner-selected seed.

Publish one fresh exact repair/reexecution task. Before any real Option-A selector call, implement and synthetically test the lower-`a` active zero-kink multiplier interval, verify the original Cell-0 failure mechanism algebraically without spending a real-cell execution, and freeze code. Then rerun the Option-A full-map gate from Cell 0 with a fresh budget. Prior scientific calls are historical evidence and do not carry into the new task budget.

The rerun must retain the existing first-failure stop, one-map-only, no-retry, full-map-before-D2, and full-map-before-direct-solve rules. Production replacement and Results eligibility remain unauthorized. Results eligibility=`FALSE`.
