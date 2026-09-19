# CH5 MP4C 2018 KFE D123 V2 cell100 interior-a zero-drift switching zero-science adjudication

Date: 2026-09-19

Task: `CH5_MP4C_2018_KFE_D123_V2_CELL100_INTERIOR_A_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_20260919`

## Primary classification

`ADJUDICATED__INTERIOR_A_ZERO_DRIFT_SWITCHING_BRANCH_SCIENTIFICALLY_SUPPORTED__OWNER_ADOPTION_REQUIRED`

The frozen cell100 evidence is a genuine strict interior-`a` upwind crossing: the backward derivative produces strictly positive `g_a`, while the forward derivative produces strictly negative `g_a`, so neither one-sided derivative is self-consistent. Under the frozen D3 adjustment technology, imposing `g_a=0` fixes a negative transfer and maps the closed interval between the two one-sided `a` derivatives into a nonempty lower-`b` multiplier interval. On that interval the frozen lower-`b` liquid equality is continuous, strictly increasing, and changes sign. It therefore has exactly one compatible crossing.

This establishes a mathematically and scientifically supported prospective branch for Owner review. It does not establish that the branch is already adopted. Existing authority explicitly adopted an analogous interior-liquid `Z` branch only after an Owner decision; it does not transfer that rule to the `a` axis. No new law is adopted by this report.

Results eligibility remains `FALSE`.

## Authority and evidence inventory

- Fresh-fetched live-main baseline: `a4c1a70b928e1c47b6c402f452d3c8423e73f870`.
- Task branch: `codex/ch5-mp4c-2018-kfe-d123-v2-cell100-interior-a-zero-drift-switching-zero-science-adjudication-20260919`.
- Worktree began clean and `0 ahead / 0 behind` live `origin/main`.
- Task SHA-256: `96FDC0DCA4B4CFF1E62F9D280B7786BA4D48A1F6C2207487DE1DF13CF7009E38`.
- Accepted V2 field SHA-256: `A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.
- Exact repaired cell100 receipt SHA-256: `3F46413C628B253ED7EA2E96799CA2B52DBB7E961C9D9934CAAC045BAC3FCD66`; Git blob `7260ba2ab4dcd43b69760eb7f96c5c80ac7be81e`.
- Frozen selector Git blob: `eac9b06805e2bcb69e078fd927a9a641c6cafd96`.
- Frozen D3 cost/KKT Git blob: `435705a50238aaeebe918430156bcc14df1ff794`.
- Frozen D1 boundary Git blob: `147e4937ba2f4a1c36d23cc60cd2b2991afcb642`.
- Frozen D2 generator Git blob: `f86234340c6e09c7129225da1677614669754177`.

The adjudication also uses the accepted D1-D3 implementation task/report/acceptance, the failed-cell algebraic attribution and acceptance, the Owner adoption of the interior-liquid `Z` law, the accepted lower-`a` zero-kink report, and the accepted repaired-V2 report/acceptance. All inputs were read statically. No persisted receipt was changed.

## Frozen local Hamiltonian and upwind law

For liquid shadow `q_b>0`, illiquid shadow `q_a`, and transfer `d`, the local continuous-control Hamiltonian terms are

\[
H(q_b,q_a;d,c,l)
=u(c,l)+q_b g_b+q_a g_a,
\]

with

\[
C(d,a)=\chi_0|d|+\frac{\chi_1d^2}{2s(a)},
\qquad s(a)=\max(a,\bar a),
\]

\[
g_b=\bar w l+r_b b+T-c-d-C(d,a),
\qquad
g_a=r_a a+d.
\]

The frozen consumption and labor first-order conditions give

\[
c=q_b^{-1/\gamma},
\qquad
l=\left(\frac{q_b\bar w}{\eta}\right)^{1/\phi}.
\]

For a chosen one-sided finite-difference branch, the implemented comparison form is `utility + p_b*g_b + p_a*g_a`; the shadows `q_b,q_a` still determine controls and KKT objects. On a prospective zero-`a`-drift branch, `g_a=0`, so the `a` transport term vanishes regardless of which endpoint is used to write the comparison. The candidate must nevertheless obtain `q_a` from the D3 KKT and place it inside the one-sided derivative interval; it may not average or interpolate controls.

At an interior `a` node, the accepted direction law is:

- `g_a>0`: use the forward derivative;
- `g_a<0`: use the backward derivative;
- `g_a=0`: either one-sided direction is locally tangent, subject to the adopted switching/selection contract.

Cell100 has

\[
p_a^F=0.008957007194295222
<p_a^B=0.00903315440190679.
\]

The active lower-`b` negative/backward-`a` root has `g_a=+0.00670682022114244`, so backward is inconsistent. The corresponding forward-`a` root has `g_a=-0.0005429159000894801`, so forward is inconsistent. Both signs are far from the persisted arithmetic bounds. This is the standard strict crossing pattern in which neither endpoint supplies a self-consistent upwind derivative.

This is not a lower-`a` state constraint: cell100 is at `a=2.6315789473684212`, an interior node, and has no `a`-face multiplier. It is also not the already adopted liquid `Z` case, which applies only at interior `b` nodes and solves `g_b=0`. Finally, it is not a boundary KKT multiplier: the only active state face here is lower `b`.

## Cell100 zero-a-drift derivation

The frozen cell rate is

\[
r_a=0.08999994552589044,
\qquad
r_a a=0.236841961910238.
\]

Imposing zero illiquid drift gives exactly

\[
d_Z=-r_a a=-0.23684196191023801.
\]

Thus the candidate is in the negative-transfer regime. Since `a>\bar a`, D3 has

\[
\partial_d C=-\chi_0+\frac{\chi_1d_Z}{a},
\]

and the transfer FOC/KKT

\[
0=q_a-q_b(1+\partial_dC)
\]

becomes

\[
\frac{q_a}{q_b}
=1-\chi_0+\frac{\chi_1d_Z}{a}
=1-\chi_0-\chi_1r_a
=0.72000010894821909
\equiv k.
\]

For a strict zero-speed upwind switch, the necessary closed derivative interval is

\[
q_a\in[p_a^F,p_a^B]
=[0.008957007194295222,\ 0.00903315440190679].
\]

The orientation is forward-to-backward because `p_a^F<p_a^B`; inclusivity is required because a zero-speed candidate may coincide with either endpoint, although this cell's compatible crossing will be interior. Since `k>0`, the interval maps to

\[
q_b\in
\left[\frac{p_a^F}{k},\frac{p_a^B}{k}\right]
=[0.012440285887428097,\ 0.012546045881996438].
\]

At an active lower-`b` face the frozen multiplier law is

\[
q_b=p_b^F+\lambda_b,
\qquad \lambda_b\ge0,
\]

so `q_b>=p_b^F=0.012333311206716577`. The entire D3/upwind interval lies above this bound. Its implied liquid multiplier interval is

\[
\lambda_b\in
[0.0001069746807115194,\ 0.00021273467527986069],
\]

which is nonempty and strictly positive.

## Static lower-b liquid-equality proof

With `d=d_Z` fixed, the active lower-`b` equality is

\[
F(q_b)
=\bar w\left(\frac{q_b\bar w}{\eta}\right)^{1/\phi}
+r_b b+T-q_b^{-1/\gamma}-d_Z-C(d_Z,a)=0.
\]

The persisted scalars are `\bar w=12.783312529860462`, `eta=1`, `phi=5`, `gamma=2`, `r_b=0.09`, `b=-2`, and `T=0.1`. Direct substitution gives

\[
C(d_Z,a)=0.044999959861190243.
\]

At the two candidate-interval endpoints:

\[
F(0.012440285887428097)=-0.0039748658728543454<0,
\]

\[
F(0.012546045881996438)=+0.048890867998731984>0.
\]

For every `q_b>0`, with `d_Z` fixed,

\[
F'(q_b)
=\frac{\bar w l(q_b)}{\phi q_b}
+\frac{c(q_b)}{\gamma q_b}>0.
\]

Therefore `F` is continuous and strictly increasing. The endpoint sign change proves exactly one liquid-equality crossing inside the D3/upwind/lower-`b` interval. This is a static existence-and-uniqueness proof; no root value was computed and no root routine was called.

The two persisted active-negative roots do not by themselves prove this result. Each existing branch pins `q_a` to a different one-sided derivative, so its transfer `d(q_b)` varies with `q_b`. The prospective branch instead fixes `d=d_Z` and sets `q_a=kq_b`. It is a different scalar equality. The conclusion follows from the direct endpoint substitutions and monotonicity above, not from interpolation between the two old roots.

## Authority adjudication

The accepted D3 authority supplies the adjustment technology and KKT relation for any legal `(d,q_a,q_b)`. The accepted direction semantics identify both one-sided cell100 candidates as inconsistent and make the strict crossing mathematically meaningful. D1 permits the derived positive lower-`b` multiplier, and D2 can consume exact zero `g_a` and `g_b` without adding an asset transition.

However, those contracts do not specify a viscosity/upwind selection rule that creates a new interior-`a` shadow between one-sided derivatives. The current selector creates a `Z` candidate only for an interior liquid node, and the interior-liquid rule was added only after explicit Owner adoption. The lower-`a` zero-kink law is also different: it intersects a state-face multiplier domain with the D3 kink interval at `d=0`; it does not establish an interior derivative switch.

Accordingly, the proposed branch is:

- scientifically supported and compatible with D1/D2/D3;
- analogous in numerical role to the adopted liquid `Z` law;
- not already entailed or adopted by that liquid-only authority;
- a genuinely new derivative-selection/scientific law requiring explicit Owner adoption before implementation or runtime.

It is not incompatible with accepted authority, and the persisted evidence is sufficient for static cell100 adjudication.

## Alternative explanations

| Explanation | Static assessment |
|---|---|
| Pure finite-`a` domain truncation | Weak as the immediate mechanism: cell100 is interior in `a`, not at `a=0` or `a=10`. Global finite-box effects on the V2 derivatives cannot be excluded. |
| Lower-`b` boundary interaction | Material but not controlling against the branch. It creates the coupled `g_b=0`, `q_b>=p_b` requirement; the static interval and monotonicity proof show that requirement is compatible. |
| Grid spacing / one-sided discretization | Plausible source of the strict crossing. The derivative gap is `7.61472076115689e-05`; refinement could move or remove it. This motivates a switching closure but does not establish an economic discontinuity. |
| V2 trajectory / initialization dependence | Material unresolved limitation. V2 is not a converged fixed point, so its derivatives and the crossing may change along an authorized future trajectory. This does not invalidate the local branch contract conditional on the frozen V2 state. |
| Illiquid-boundary multiplier | Excluded locally: there is no `a`-face at this coordinate and hence no legal `a` state-constraint multiplier explanation. |

The strongest supported interpretation is a missing interior-`a` numerical switching case conditional on the frozen V2 derivative state, not finite-`a` boundary control and not global HJB nonexistence.

## Prospective scientific contract for Owner review only

If Owner adopts an interior-`a` zero-drift branch, the minimal contract should be:

1. **Trigger.** Only at an interior `a` node, for the same frozen `b` branch/active set and transfer regime, after both one-sided `a` candidates are evaluated. Require a strict arithmetic-bound-separated crossing: backward candidate `g_a>0`, forward candidate `g_a<0`, and neither endpoint direction-consistent through zero.
2. **Zero-drift equality.** Set `d_Z=-r_a a` so consumed `g_a=0`. Determine the transfer regime from the sign of `d_Z`; do not force a preselected sign.
3. **D3 KKT.** Compute the switching shadow from the unchanged D3 subgradient: `q_a=q_b(1+partial_d C(d_Z,a))`. Require `q_b>0` and the unchanged cost scale `max(a,a_bar)`.
4. **Derivative interval.** Require `q_a` to lie in the closed sorted interval between `p_a^F` and `p_a^B`. No derivative averaging, clipping, flooring, extrapolation, or fitted tolerance is allowed.
5. **Liquid-face interaction.** For active lower `b`, require `q_b>=p_b` and `g_b=0`; for active upper `b`, require `0<q_b<=p_b` and `g_b=0`. The unique root, if any, must lie in the intersection of the D3 derivative interval and the relevant multiplier domain. Missing, nonunique, nonfinite, or out-of-domain roots fail closed. Slack/interior-`b` cases retain their existing derivative or adopted liquid-`Z` contracts; no simultaneous two-axis switching rule is implied here.
6. **Candidate reconstruction.** Recompute `c,l,C,g_b,g_a`, multipliers, complementarity and transfer KKT from the candidate shadows. Do not interpolate endpoint controls.
7. **Hamiltonian selection.** After every existing D1/D2/D3/domain/finite-value check passes, include the candidate in the unchanged deduplication and Hamiltonian comparison. The zero `a` transport contribution must be represented canonically only when its raw residual is within a prospectively frozen arithmetic bound.
8. **D2 representation.** Consume exact `g_a=0`; an active liquid equality similarly consumes exact `g_b=0` only under its frozen residual bound. D2 then creates no asset-transition rate on either zero-drift axis and otherwise remains unchanged.
9. **Receipt.** Persist endpoint derivatives, endpoint drifts and bounds, sorted derivative interval, `d_Z`, transfer regime, D3 ratio, candidate `q_a/q_b`, liquid multiplier domain, liquid-equality bracket values, uniqueness basis/root method if later authorized, raw residuals, canonical-zero markers, KKT residual, Hamiltonian, and rejection reasons.
10. **Preservation.** Existing backward/forward branches, the Owner-adopted liquid `Z` branch, lower-`a` zero-kink multiplier law, D1 faces, D2 assembly, D3 technology, solver, grid, calibration, convergence law, and production routes remain unchanged.

This contract is prospective only. It neither authorizes implementation nor supplies a runtime/root budget.

## Zero-science ledger

| Operation | Calls |
|---|---:|
| selector evaluations | 0 |
| scalar-root calls | 0 |
| interior-liquid `Z` root calls | 0 |
| proposed interior-`a` zero-drift root calls | 0 |
| policy maps | 0 |
| D2/Q assemblies | 0 |
| Bellman/checkpoint scientific evaluations | 0 |
| HJB solves/updates | 0 |
| graph/SCC | 0 |
| KFE/SVD/eigen/nullspace/`Q.T@p` | 0 |
| MATLAB | 0 |
| outer/firm/wage-return/GE/annual/shock/IRF/Results | 0 |
| scientific retries | 0 |

Only static Git/source/document reads, persisted JSON parsing, hashing, symbolic derivation, and direct scalar substitution were used. No selector, scientific helper, test, solver, or model module was imported or executed.

## Scope closure

The sole changed path is this report. No source, test, task, receipt, CURRENT status/handoff/roadmap/index, grid, parameter, tolerance, or accepted evidence changed. Main is not merged, no successor task is published, and the Owner remains the only authority who may adopt the proposed branch.
