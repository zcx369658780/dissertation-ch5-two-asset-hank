# CH5 MP4C 2018 KFE D1-D3 V2 cell100 zero-science attribution acceptance

Date: 2026-09-17

Reviewer verdict:

`PASS__ATTRIBUTION_ACCEPTED__LOWER_B_ACTIVE_NEGATIVE_BACKWARD_A_BRANCH_OMITTED_BY_WRONG_FACE_DOMAIN_SCREEN__MINIMAL_REPAIR_REEXECUTION_AUTHORIZED`

## Accepted candidate

- baseline live main before acceptance: `affee50a517f8ab688498378e9c7d4a4edafa311`
- Builder candidate: `582f7fca52e47ee5303164edbc62b98add363ec6`
- candidate tree: `3100fdd4f21549ec57721c4de00b4ec23a1aeac8`
- candidate is exactly `1 ahead / 0 behind` baseline
- changed path is exactly one new report:
  `docs/CH5_MP4C_2018_KFE_D123_V2_CELL100_NO_ADMISSIBLE_POLICY_ZERO_SCIENCE_ATTRIBUTION_REPORT.md`

## L3 acceptance

The attribution is accepted as:

`ATTRIBUTED__SELECTOR_OMITS_AUTHORITY_BACKED_LEGAL_BRANCH`

Accepted causal finding:

1. At the liquid lower boundary, the active-face multiplier domain is `q_b >= p_b`.
2. The frozen selector's active-lower-b negative-transfer derivative pre-screen incorrectly uses the upper-face-style interval `0 < q_b <= p_b`.
3. This incorrect domain screen retains only the forward-`a` negative-transfer case and omits the authority-backed active lower-b / negative-transfer / backward-`a` case.
4. The frozen authority census requires eight lower-b slack/active x transfer/derivative cases, while the V2 cell100 receipt persists seven.
5. Static algebra on the omitted case shows that, for the frozen V2 cell100 inputs, the omitted branch would still be rejected: any liquid-equality crossing occurs before the backward-`a` direction becomes valid. This local outcome-equivalence does not cure the branch-coverage defect.
6. The positive active branch's `ROOT_FAILURE_NO_UNIQUE_BRACKET` is not an implementation omission: positive transfer requires `q_b < 0.008142733812995656`, while lower-b activity requires `q_b >= 0.012333311206716577`; the legal domains are disjoint, and the frozen liquid equation remains strictly positive on the legal lower-face domain.
7. Interior liquid `Z` is not applicable at the lower-b boundary cell.

## Evidence and scope

The zero-science ledger is accepted as all-zero for selector/root/policy-map/D2/HJB/KFE/MATLAB/downstream calls. No repair, rerun, tolerance change, solver substitution or production change occurred in the attribution task.

This acceptance does not establish nonlinear HJB convergence or nonexistence, P2/u2/Q2, terminal KFE, household fixed point, GE, market clearing, production replacement or Results eligibility.

## Successor boundary

The defect is an already-authorized selector implementation omission, not a new scientific-law choice. Reviewer therefore authorizes one narrowly bounded successor task to:

- repair only the active lower-b negative-transfer derivative pre-screen so it uses the correct lower-face domain and represents both authority-backed negative-transfer derivative cases;
- add focused branch-completeness/regression tests without weakening any existing scientific assertion;
- reexecute exactly one fresh V2 checkpoint-2 remap from the accepted V2 field;
- if and only if the full V2 map completes, assemble Q2 and compute checkpoint-2 Bellman/value/stability/cycle diagnostics under the frozen law;
- stop before any `V2 -> V3` HJB update.

Source-faithful/production paths remain unchanged. Results eligibility remains `FALSE`.
