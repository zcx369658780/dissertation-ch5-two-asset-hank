# CH5 MP4C 2018 KFE D1-D3 simultaneous two-axis zero-drift switching Owner adoption

Date: 2026-09-19

Owner decision:

`OWNER_ADOPTED__SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_LAW__BOUNDED_CORRECTED_DIAGNOSTIC_IMPLEMENTATION_AUTHORIZED`

## Authority

The Owner explicitly adopts the simultaneous interior-liquid / interior-`a` zero-drift switching contract supported by:

- `docs/CH5_MP4C_2018_KFE_D123_V2_CELL185_SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_REPORT.md`
- `docs/CH5_MP4C_2018_KFE_D123_V2_CELL185_SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_ACCEPTANCE_20260919.md`.

This adoption creates a new **coupled corrected-diagnostic derivative-selection law**. It does not modify the source-faithful/production route and does not alter D1, D2, D3, ordinary one-sided upwinding, the one-axis liquid-`Z` law, the one-axis interior-`a` switching law, lower-`a` zero-kink authority, grid, calibration, root tolerance/solver family, HJB update law, convergence thresholds, or terminal KFE rules.

Results eligibility remains `FALSE`.

## Adopted scientific law

### 1. Domain and trigger

The coupled candidate is eligible only at a node interior in both asset dimensions `b` and `a`, with no asset-face active set, under one common already-legal transfer regime.

Evaluate ordinary one-sided candidates and already-adopted one-axis candidates first.

A joint trigger requires:

1. for both one-sided `a` endpoint shadows under the same transfer regime, the liquid backward/forward candidates form the already-authorized strict liquid crossing and produce legal liquid-`Z` receipts;
2. the resulting two liquid-`Z` candidates form a strict arithmetic-bound-separated illiquid crossing:
   - backward-`a` liquid-`Z` has `g_a>0`;
   - forward-`a` liquid-`Z` has `g_a<0`;
3. neither one-axis candidate is already direction-consistent through zero.

No joint candidate is created at an asset boundary.

### 2. Simultaneous zero-drift equations

The candidate is defined by the coupled system

`g_a=0`

and

`g_b=0`.

Set

`d_ZZ=-r_a a`

from `g_a=0`.

Determine the transfer regime from the sign of `d_ZZ`; do not choose a regime to obtain a desired result.

### 3. D3 relation

Use the unchanged D3 adjustment technology

`C(d,a)=chi_0|d|+chi_1 d^2/(2 max(a,a_bar))`.

For nonzero `d_ZZ`, impose the unchanged smooth D3 FOC/KKT:

`q_a=q_b(1+partial_d C(d_ZZ,a))`.

If `d_ZZ=0`, use only independently adopted D3 kink/subgradient authority. This adoption does not create a new joint zero-transfer kink selector.

Require finite `q_a`, finite `q_b`, and `q_b>0`.

### 4. Two-dimensional derivative rectangle

Require

`q_b in [min(p_b^F,p_b^B), max(p_b^F,p_b^B)]`

and

`q_a in [min(p_a^F,p_a^B), max(p_a^F,p_a^B)]`.

Map the `a)-shadow interval through the unchanged D3 relation into its implied `q_b` interval and intersect it exactly with the liquid derivative interval.

An empty, nonfinite, or zero-width intersection fails closed.

No averaging, clipping, flooring, extrapolation, fitted tolerance, or interpolation of endpoint controls/shadows/Hamiltonians is authorized.

### 5. Joint root semantics

On the exact positive interval intersection, solve the fixed-`d_ZZ` liquid equality

`g_b(q_b,d_ZZ)=0`

using the existing corrected-diagnostic scalar root routine and frozen tolerance.

Require exactly one legal root inside the exact intersection under the existing fail-closed uniqueness semantics.

No interval widening, solver substitution, tolerance tuning, outcome-dependent retry, or continuation is authorized.

Set

`q_a^*=q_b^*(1+partial_d C(d_ZZ,a))`.

### 6. Reconstruction and residual law

Recompute consumption, labor, cost, transfer, `g_b`, `g_a`, D3 residuals, and Hamiltonian from the joint shadows.

Canonicalize `g_b=0` and `g_a=0` only under the existing arithmetic-residual protocol. Raw residual violations reject the candidate.

No boundary multiplier is created because the joint law is interior-interior only.

### 7. Hamiltonian selection

A legal joint candidate enters the existing policy deduplication and Hamiltonian comparison unchanged.

Both asset transport contributions are canonical zero only after the accepted residual checks pass.

### 8. Precedence and deduplication

Ordinary one-sided candidates and both one-axis switching laws retain their current authority and are evaluated normally.

The joint candidate is a **separate final fallback** triggered only by the coupled strict-crossing census.

Create at most one joint candidate per node / active-set / transfer-regime object. It must not be duplicated by the labels or execution orders:

- `liquid-Z then a-Z`;
- `a-Z then liquid-Z`.

It is one simultaneous coupled candidate, not a sequential composition.

### 9. D2 consumed-drift representation

D2 remains unchanged.

If the joint candidate is selected and passes existing residual rules, D2 consumes canonical `g_b=0` and `g_a=0`, creating no liquid-asset or illiquid-asset transport rate from those drifts. Productivity-state transitions remain unchanged.

No artificial diffusion, leakage repair, clipping, or boundary repair is authorized.

### 10. Audit receipt

Persist enough evidence to reconstruct the complete joint decision:

- four one-sided derivatives;
- ordinary liquid endpoint drifts and arithmetic bounds;
- both relevant liquid-`Z` receipts;
- post-liquid backward/forward `a` drifts and bounds;
- joint-trigger result;
- `d_ZZ` and transfer regime;
- D3 subgradient/ratio;
- both derivative intervals;
- D3-mapped `q_b` interval;
- exact interval intersection;
- fixed-transfer liquid endpoint values;
- root method/status and uniqueness evidence;
- final `q_b,q_a`;
- raw/canonical `g_b,g_a`;
- D3/KKT residuals;
- Hamiltonian;
- D2 admissibility;
- comparison/deduplication identity;
- all rejection reasons.

### 11. Preserved authority

The following remain unchanged:

- D1 boundary law;
- D2 consumed-total-drift generator assembly;
- D3 adjustment technology/KKT;
- ordinary one-sided upwinding;
- one-axis interior-liquid `Z`;
- one-axis interior-`a` zero-drift switching;
- lower-`a` zero-kink multiplier law;
- scalar root solver family/tolerance;
- grid/calibration/payoff equations;
- `Delta=1000`;
- Owner nonlinear HJB convergence law;
- terminal KFE timing/topology law;
- source-faithful and production routes.

This adoption is a corrected-diagnostic multidimensional upwind closure. It is not evidence of HJB convergence, global existence, GE closure, production readiness, or Results eligibility.

## Immediate implementation authority

Reviewer may publish one bounded task that:

1. implements only this coupled law in the corrected-diagnostic selector;
2. adds focused tests and exact cell185 regression evidence;
3. preserves all one-axis behavior and precedence rules;
4. executes exactly one fresh accepted-V2 checkpoint-2 policy-map attempt;
5. if and only if all 800 cells select admissible policies, assembles at most one Q2 and evaluates checkpoint-2 Bellman/value/policy/operator/cycle diagnostics;
6. performs zero V2->V3 HJB updates and zero terminal topology/KFE/SVD work.

Any different first scientific failure stops the task and returns to Reviewer.
