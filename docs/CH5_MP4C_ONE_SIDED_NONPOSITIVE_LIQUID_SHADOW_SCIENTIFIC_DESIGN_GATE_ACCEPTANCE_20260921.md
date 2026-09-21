# Chapter 5 one-sided / nonpositive liquid-shadow scientific design gate — Reviewer acceptance

Date: 2026-09-21

Verdict:

`ACCEPTED_PASS__ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_EXTENSION_SCIENTIFICALLY_REJECTED__CURRENT_FAIL_CLOSED_PRESERVED`

Accepted terminal:

`PASS__ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_DESIGN_GATE__EXTENSION_NOT_SCIENTIFICALLY_JUSTIFIED__PRESERVE_CURRENT_FAIL_CLOSED_RECOMMENDED__NO_IMPLEMENTATION`

Accepted classification:

`EXTENSION_SCIENTIFICALLY_UNJUSTIFIED__CURRENT_FAIL_CLOSED_RECOMMENDED`

Results eligibility remains `FALSE`.

## Independent Git review

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

- baseline: `a5519fccb8276b6c7db1de16d4c05abf13efd73f`
- candidate: `8b10f3859a40c6c123fca5888e5d82abf8f4e5bd`
- candidate tree: `410f625335d00644f178790fe78208eeb8b33c22`
- ancestry: 1 ahead / 0 behind
- merge-base: exact baseline
- changed paths: 18
- production `src/ch5_two_asset_hank/**` changes: 0
- CURRENT changes: 0
- remote candidate branch SHA/tree: exact.

Changed paths are limited to the design report, validator/test and fresh evidence.

Focused tests: 4/4 PASS.

## Accepted scientific result

The design gate does not support extending the liquid-Z derivative-selection law beyond the local raw derivative hull merely because a D3/KKT-feasible root exists there.

For F0063:

- raw liquid derivative hull:
  `[-0.0002428532863339202,0.014463823441006161]`
- positive-domain intersection:
  `(0,0.014463823441006161]`
- positive-transfer / forward-a drift at the sole positive endpoint:
  `-1.5960747263712167`.

On that fixed-a-shadow positive-transfer branch, the independently derived liquid drift is strictly increasing in q_b. Since it is still negative at the maximum positive raw derivative, no zero-liquid root exists inside the positive part of the local derivative hull.

The diagnostic root:

`q_b=0.01801822665826406`

lies above the sole positive raw derivative by:

`0.0035544032172578986`.

Its branch algebra is internally coherent, but its enclosing interval is a D3/KKT branch-feasibility interval rather than a value-function derivative-selection interval.

The repository's adopted HJB/upwind authority contains no rule that converts that control-feasibility interval into a viscosity/supergradient/subgradient support set for q_b.

Therefore the proposed branch-feasibility extrapolation is not accepted as a corrected-HJB derivative-selection law.

## Design comparison accepted

- Design 0 — preserve current two-positive-shadow law:
  accepted as current authority.
- Design 1 — restrict to the positive part of the raw derivative hull:
  mathematically coherent but creates no F0063 root.
- Design 2 — extrapolate to D3 branch-feasibility boundary:
  scientifically rejected as unsupported derivative-selection extrapolation.
- Design 3 — restore historical derivative floor:
  remains non-authoritative and not recommended.

No generic extension law is proposed.

No separate Owner adoption is needed to preserve the already active fail-closed authority.

## Cross-cell evidence

The persisted failed-map prefix contains two mixed-sign interior-liquid cells:

- F0062: `(+,<=0)`, already has an ordinary admissible policy;
- F0063: `(<=0,+)`, no hull root; only an extrapolated diagnostic root.

The F0062 evidence is useful falsification: a generic "mixed-sign => extrapolated Z" trigger would emit an unnecessary switching object where ordinary upwinding already selects a policy unless additional outcome-dependent precedence were imposed. That weakens the case for treating branch-feasibility extrapolation as a standalone derivative law.

## Complete-map census limitation

The requested 408-map / 101-map raw derivative sign counts are not recoverable from the accepted compact evidence without recomputing derivatives from persisted V.

Independent review confirms the evidence structure:

- accepted turn1 complete maps: 408;
- run004 complete maps: 101;
- complete-map cell JSON retained: 0;
- derivative receipts retain SHA-256 identities, not numeric derivative arrays;
- checkpoint/selected-policy/direct-update NPZ artifacts do not store raw derivative arrays.

The design task explicitly forbade derivative recomputation from V, so the Builder correctly preserved 509 province/checkpoint audit rows as:

`UNAVAILABLE__RAW_DERIVATIVE_VALUES_COMPACTED_AWAY`

rather than inferring signs from selected q_b values or hashes.

This limitation is material to prevalence evidence, but it does not overturn the accepted scientific rejection of Design 2: frequency of a sign pattern cannot provide the missing derivative-selection / viscosity justification for extrapolation outside the local derivative hull.

## Zero-science integrity

Accepted ledger:

- persisted complete-map metadata reads: 509
- persisted cell JSON loads: 64
- independent scalar root diagnostics: 2
- production selector calls: 0
- production root-helper calls: 0
- derivative recomputation from V: 0
- HJB/direct update: 0
- D2/Q: 0
- KFE/SVD: 0
- aggregate/integration: 0
- turn2 replay/rerun: 0
- turn3: 0
- MATLAB: 0
- GE/Results: 0
- retry/tuning: 0.

## Evidence integrity

Evidence root:

`reports/ch5_mp4c_one_sided_nonpositive_liquid_shadow_scientific_design_gate_20260921_run001/`

- manifest SHA-256:
  `35DFC6D56A07CD87151EB0A5C83B07E6E1402009F799BCF5B0C1C9C5F1AA57BB`
- entries: 12
- bytes: 133,364
- independent readback: PASS
- bad paths: none.

## Reviewer decision

The candidate is accepted.

The existing two-positive-shadow interior-liquid Z law remains authoritative and F0063 remains a valid fail-closed point.

No one-sided extrapolative Z implementation, derivative floor or turn-2 continuation is authorized.

The next useful question is no longer "how to rescue F0063 in the selector", but "when and how the negative liquid derivative first emerges in the accepted HJB iterate, and whether it is an arithmetic artifact, a direct-solve transient, or a deeper numerical/model issue."

A separate zero-science emergence forensic is authorized next.
