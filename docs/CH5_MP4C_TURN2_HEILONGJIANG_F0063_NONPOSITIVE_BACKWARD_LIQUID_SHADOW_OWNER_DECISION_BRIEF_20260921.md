# Chapter 5 黑龙江 F0063 nonpositive one-sided liquid shadow — Owner decision brief

Date: 2026-09-21

Status:

`OWNER_DECISION_B_RECORDED__SCIENTIFIC_DESIGN_GATE_AUTHORIZED__NO_IMPLEMENTATION`

This document is a decision brief, not an adopted scientific authority.

## Owner decision recorded — Decision B

Owner decision on 2026-09-21:

`OWNER_DECISION__AUTHORIZE_ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_EXTENSION_DESIGN_GATE__NO_IMPLEMENTATION_YET`

Owner instruction:

`同意 B，先做 one-sided nonpositive liquid-shadow scientific design gate，不授权实现。`

This authorizes investigation and design only. It does not adopt a new liquid-Z law and does not authorize selector implementation or turn-2 rerun.

Formal authority:

`docs/CH5_MP4C_TURN2_HEILONGJIANG_F0063_ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_DESIGN_GATE_OWNER_AUTHORIZATION_20260921.md`

## Frozen facts

At 黑龙江 turn-2 checkpoint3 / flat63:

- the node is interior in both assets;
- `p_b^B=-0.0002428532863339202`;
- `p_b^F=0.014463823441006161`;
- current corrected authority requires `q_b>0`;
- current generic liquid-Z law requires both one-sided liquid shadows finite and positive;
- current selector therefore correctly returns `NO_ADMISSIBLE_POLICY`;
- there is no current implementation omission.

A diagnostic-only positive-transfer / forward-a root exists at:

`q_b=0.01801822665826406`

with D3/KKT/direction checks internally coherent, but it lies above the only positive raw liquid derivative shadow and outside the currently authorized derivative-shadow interval.

## Decision A — preserve current authority and fail closed

Decision text if adopted:

`OWNER_DECISION__PRESERVE_TWO_POSITIVE_SHADOW_INTERIOR_Z_LAW__F0063_REMAINS_FAIL_CLOSED__NO_ONE_SIDED_EXTENSION`

Meaning:

- do not admit a Z candidate when either raw one-sided liquid shadow is nonpositive;
- do not use a derivative floor;
- do not extrapolate beyond the positive one-sided derivative;
- F0063 remains a valid corrected-HJB first failure;
- turn2 cannot continue under the current corrected-HJB route without a separate redesign.

A scientifically useful successor would be a zero-/low-science design audit of why the corrected HJB iterate develops `p_b^B<0` and whether the proper remedy belongs in value-iteration monotonicity/initialization/numerics rather than derivative selection.

### Reviewer scientific view

This is the conservative route.

It preserves the viscosity/upwind interpretation that the zero-drift shadow should remain tied to the local derivative information rather than extrapolated beyond the observed one-sided derivative interval.

## Decision B — investigate and potentially adopt a one-sided/nonpositive-shadow Z extension

Decision text if Owner wants this route investigated, but not yet implemented:

`OWNER_DECISION__AUTHORIZE_ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_EXTENSION_DESIGN_GATE__NO_IMPLEMENTATION_YET`

Meaning:

- Owner permits a scientific design gate to derive a generic law for cases with one nonpositive and one positive liquid derivative;
- no selector change is yet authorized;
- the design gate must justify the q_b search interval from HJB/upwind/KKT logic, not from outcome convenience;
- the current F0063 diagnostic root may be used as a test object, not as the law itself.

The design gate must settle at minimum:

1. exact trigger when one raw derivative is nonpositive;
2. whether the nonpositive side is discarded, replaced by a positive-domain boundary, or treated another way;
3. the exact positive q_b bracket;
4. whether extrapolation beyond the sole positive derivative is permitted;
5. branch-specific D3/KKT interaction;
6. root uniqueness/fail-closed law;
7. compatibility with ordinary upwinding, interior-a switching and joint switching;
8. a hard compatibility panel before any HJB continuation.

The F0063 diagnostic interval

`[p_b^F, p_a^F/(1+chi_0)]`

must not be generalized automatically: its upper endpoint comes from the positive-transfer branch's D3/sign feasibility and is not currently a liquid derivative-selection authority.

## Decision C — restore a derivative floor

Possible decision text:

`OWNER_DECISION__REOPEN_DERIVATIVE_FLOOR_FOR_CORRECTED_SELECTOR__SCIENTIFIC_REDESIGN_REQUIRED`

The historical MATLAB-faithful path used a `1e-6` floor, but corrected authority explicitly did not inherit it.

Choosing this route would be a broader scientific redesign, not a local repair. It would require revalidating consumption FOC/domain behavior, ordinary upwinding, all switching laws, turn1 compatibility and downstream HJB/KFE evidence.

This route is not recommended as a local F0063 fix.

## Reviewer recommendation

Do not directly implement the diagnostic F0063 root.

If the Owner wants to keep the current corrected-HJB interpretation strict, choose Decision A.

If the Owner believes the model should continue through transient non-monotone value iterates, choose Decision B first: authorize a separate scientific design gate, derive the generic one-sided law, and only then decide whether to adopt it.

No Builder execution should resume until one of these decisions is recorded.
