# CH5 MP4C 2018 KFE D1-D3 interior-a zero-drift switching Owner adoption

Date: 2026-09-19

Owner decision:

`OWNER_ADOPTED__INTERIOR_A_ZERO_DRIFT_SWITCHING_LAW__BOUNDED_CORRECTED_DIAGNOSTIC_IMPLEMENTATION_AUTHORIZED`

## Authority

The Owner explicitly adopts the interior-`a` zero-drift switching scientific contract supported by:

- `docs/CH5_MP4C_2018_KFE_D123_V2_CELL100_INTERIOR_A_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_REPORT.md`
- `docs/CH5_MP4C_2018_KFE_D123_V2_CELL100_INTERIOR_A_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_ACCEPTANCE_20260919.md`.

This adoption creates a new corrected-diagnostic derivative-selection law. It does not modify the source-faithful/production route and does not alter D1, D2, D3, the liquid-`Z` law, the lower-`a` zero-kink law, calibration, grid, HJB update law, convergence thresholds or terminal KFE rules.

Results eligibility remains `FALSE`.

## Adopted scientific law

### 1. Trigger

At an **interior illiquid-`a` node**, for the same already-legal frozen liquid-`b` branch/active set and the same transfer regime, evaluate the ordinary one-sided `a` candidates first.

An interior-`a` zero-drift switching candidate is eligible only when the one-sided candidates form a strict arithmetic-bound-separated crossing:

- the backward-`a` candidate implies `g_a>0`;
- the forward-`a` candidate implies `g_a<0`;
- neither one-sided candidate is direction-consistent through zero.

No switching candidate is created at an `a` boundary node.

### 2. Zero-drift equality

For an eligible switching candidate impose

`g_a=r_a a+d_Z=0`,

hence

`d_Z=-r_a a`.

The transfer regime is determined by the sign of `d_Z`; it is not selected to force a desired result.

### 3. D3 transfer KKT

Use the unchanged D3 adjustment technology

`C(d,a)=chi_0|d|+chi_1 d^2/(2 max(a,a_bar))`.

The switching shadows must satisfy the unchanged D3 subgradient/FOC:

`0 in q_a-q_b(1+partial_d C(d_Z,a))`.

For smooth nonzero `d_Z`, this is the corresponding equality. If `d_Z=0`, use only the already-adopted D3 kink/subgradient authority; do not invent a new zero-transfer selection rule.

Require `q_b>0`.

### 4. Interior-a derivative interval

Require the switching shadow to lie in the **closed sorted interval** between the two one-sided illiquid derivatives:

`q_a in [min(p_a^F,p_a^B), max(p_a^F,p_a^B)]`.

No derivative averaging, clipping, flooring, extrapolation, fitted tolerance or endpoint-control interpolation is authorized.

### 5. Liquid-axis interaction

The pre-existing liquid-axis scientific law remains authoritative.

For an active lower-`b` face:
- require `q_b>=p_b`;
- require `g_b=0`.

For an active upper-`b` face:
- require `0<q_b<=p_b`;
- require `g_b=0`.

The switching candidate is legal only if the D3/derivative-implied `q_b` set intersects the relevant liquid multiplier domain and the frozen liquid equality has a unique legal root in that intersection.

For a slack liquid face, preserve its existing shadow/domain law.

At an interior liquid node, preserve the already-adopted liquid backward/forward/`Z` law. **This adoption does not create a simultaneous new two-axis zero-drift switching law.** If a case would require both a newly created interior-`a` switching shadow and a newly created liquid-`Z` shadow simultaneously, fail closed for separate Owner adjudication.

### 6. Root semantics

When an active liquid equality must be solved for the adopted interior-`a` switching candidate:

- use the existing corrected-diagnostic scalar root routine and frozen root tolerance;
- restrict the search to the exact intersection of the adopted derivative-implied interval and the relevant liquid multiplier domain;
- require exactly one legal bracket/root under the existing fail-closed semantics;
- do not widen the interval, substitute a solver, tune a tolerance or perform a scientific retry.

### 7. Candidate reconstruction and legality

Recompute `c,l,C,g_b,g_a`, multipliers, complementarity, transfer KKT and Hamiltonian from the switching shadows.

Canonicalize `g_a=0` and, for active liquid faces, `g_b=0` only under the existing arithmetic-residual protocol. A raw residual outside that protocol rejects the candidate.

Every existing D1/D2/D3/domain/finite-value condition remains required.

### 8. Hamiltonian selection

After legality checks, include the switching candidate in the existing deduplication and Hamiltonian comparison without changing the comparison law or tolerance.

The zero illiquid transport term contributes canonically as zero only after the adopted residual check passes.

### 9. D2 consumed-drift representation

D2 remains unchanged.

For an accepted switching candidate, D2 consumes canonical `g_a=0` and therefore creates no illiquid-asset transport rate along that axis. An active liquid equality analogously contributes canonical `g_b=0` only under its existing residual rule.

No artificial transition, diffusion or leakage correction is authorized.

### 10. Audit receipt

Persist enough evidence to reconstruct the decision:

- both one-sided `a` derivatives;
- both endpoint one-sided candidate drifts and arithmetic bounds;
- strict-crossing trigger result;
- sorted derivative interval;
- `d_Z` and transfer regime;
- D3 subgradient/ratio object;
- implied `q_a/q_b` relation;
- liquid multiplier domain and interval intersection;
- liquid-equality endpoint values/bracket and root status if applicable;
- switching `q_a,q_b`;
- raw and canonical `g_a,g_b`;
- multipliers, complementarity and transfer-KKT residuals;
- Hamiltonian;
- D2 admissibility;
- rejection reasons or selected-policy identity.

## Preserved authority

The following remain unchanged:

- ordinary backward/forward `a` branches;
- Owner-adopted interior-liquid `Z`;
- lower-`a` zero-kink multiplier law;
- D1 faces;
- D2 consumed-total-drift generator assembly;
- D3 adjustment technology and KKT;
- root tolerance and solver family;
- grid and calibration;
- fixed `Delta=1000`;
- Owner nonlinear convergence law;
- terminal KFE timing and topology requirements;
- source-faithful/production code.

This adoption is conditional scientific/numerical closure for corrected-diagnostic upwinding. It is not evidence of HJB convergence, global existence, GE closure or Results eligibility.

## Immediate implementation authority

Reviewer may publish one bounded implementation/reexecution task that:

1. implements this law only in the corrected-diagnostic route;
2. adds focused tests and exact cell100 regression evidence;
3. performs exactly one fresh accepted-V2 checkpoint-2 policy-map attempt;
4. if and only if the full 800-cell map succeeds, assembles at most one Q2 and evaluates checkpoint-2 Bellman/value/policy/operator/cycle diagnostics;
5. performs zero V2->V3 HJB updates and zero terminal KFE/topology/SVD work.

Any different first scientific failure stops the task and returns to Reviewer.
