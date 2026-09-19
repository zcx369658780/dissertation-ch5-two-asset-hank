# CH5 MP4C 2018 KFE D123 V2 cell185 simultaneous two-axis zero-drift switching zero-science adjudication

Date: 2026-09-19

Task: `CH5_MP4C_2018_KFE_D123_V2_CELL185_SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_ZERO_SCIENCE_ADJUDICATION_20260919`

## Primary classification

`ADJUDICATED__SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_SCIENTIFICALLY_SUPPORTED__OWNER_ADOPTION_REQUIRED`

The frozen cell185 evidence supports a genuinely joint interior-interior switching candidate. Imposing `g_a=0` fixes the transfer. The unchanged D3 KKT then reduces the two-dimensional shadow rectangle to a line segment `q_a=k q_b`. That segment has a nonempty intersection with both one-sided derivative intervals. On the resulting exact liquid-shadow interval, the frozen liquid equality is continuous, strictly increasing and changes sign, so it has exactly one joint root. This is a simultaneous solution of `g_b=g_a=0`; it is not a sequential composition of the two currently adopted one-axis algorithms.

The result is a scientific adjudication and prospective contract only. Current Owner authority still forbids constructing this candidate. No law is adopted or implemented by this report. Results eligibility remains `FALSE`.

## Authority and evidence inventory

- Fresh-fetched live-main baseline: `8a259e2d1c8dc6c5ae3b512b698daa30dcfd0525`.
- Task branch: `codex/ch5-mp4c-2018-kfe-d123-v2-cell185-simultaneous-two-axis-zero-drift-switching-zero-science-adjudication-20260919`.
- Worktree began clean and `0 ahead / 0 behind` live `origin/main`.
- Task SHA-256: `70FC0FA5EE15E00E0EF3061885AA8F790880734A356F238A479EBDD429DEEA1D`.
- Accepted V2 field SHA-256: `A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.
- Exact cell185 receipt SHA-256: `69A1CFF66B1CFB6977EC744742635060128BFDB3DE052876C85CC2B5A8A9A337`.
- Interior-`a` Owner-adoption document SHA-256: `F5C4515078BBFFE32F9924758AF2DC5DD1C344A86DEB3EB596AFF91106F2FD95`.
- Interior-liquid `Z` Owner-adoption document SHA-256: `951B5A593E6F46D3C4A1EA85B64F19DB4563D047BAEF25A143D34C6256BBBB91`.
- Frozen D3 implementation SHA-256: `30FDA6AFA8B30E214220A70476562BE1120FCBD0101D67A3C21B7CE77CD0C1BF`.
- Unchanged D2 implementation SHA-256: `F52451213E04EA999FE132B77AA92D1B66819B4D36BA5C539E9DD5EED4A63DB3`.

The adjudication also uses the accepted D1/D2/D3 static contract, lower-`a` zero-kink law, nonlinear convergence law, accepted interior-`a` implementation/reexecution report and acceptance, and the exact persisted cell185 candidate census. All were read statically. No source, receipt or accepted artifact was changed.

## Frozen local Hamiltonian and one-axis limits

For shadows `(q_b,q_a)`, consumption `c`, labor `l`, transfer `d`, and adjustment cost `C`, the local Hamiltonian is

\[
H(q_b,q_a)=u(c,l)+q_b g_b+q_a g_a,
\]

with

\[
g_b=\bar w l+r_b b+T-c-d-C(d,a),
\qquad
g_a=r_a a+d,
\]

\[
C(d,a)=\chi_0|d|+\frac{\chi_1d^2}{2s(a)},
\qquad s(a)=\max(a,\bar a),
\]

and the frozen consumption/labor conditions

\[
c=q_b^{-1/\gamma},
\qquad
l=\left(\frac{q_b\bar w}{\eta}\right)^{1/\phi}.
\]

The adopted liquid-`Z` law holds one already-legal `a` derivative branch fixed, detects a strict backward-positive/forward-negative liquid-drift crossing, and selects an interior `q_b` satisfying `g_b=0`. The adopted interior-`a` law holds one already-legal liquid branch or liquid-face law fixed, detects a strict backward-positive/forward-negative `a`-drift crossing, and imposes `g_a=0`. Each law deliberately treats the other axis as already resolved. Neither authority permits both shadows to be newly selected at once; the interior-`a` adoption explicitly requires fail-closed referral when both switches would be needed.

Cell185 is interior in both assets and has no asset-face active set. Its derivative rectangle is

\[
q_b\in[p_b^F,p_b^B]
=[0.009574726769001294,\ 0.013362109688537174],
\]

\[
q_a\in[p_a^F,p_a^B]
=[0.008489317330830281,\ 0.00857557540065246].
\]

For each relevant `a` endpoint, the persisted ordinary liquid candidates have backward `g_b>0` and forward `g_b<0`, so the accepted liquid-`Z` trigger is genuine. The resulting negative-transfer liquid-`Z` candidates are:

- backward `a`: `q_b=0.011845651796693632`, `g_b=0`, `g_a=+0.009287240997760404`;
- forward `a`: `q_b=0.011826220238545775`, `g_b=0`, `g_a=-0.005170298666228812`.

Thus neither endpoint derivative is direction-consistent in `a` after the liquid drift is closed. This is the two-dimensional analogue of a strict upwind crossing, but the coupling prevents treating it as two independent one-dimensional calls: changing `q_a` changes D3 transfer, while changing transfer changes the liquid equality and therefore the compatible `q_b`. A joint algebraic system is required.

## Joint zero-drift geometry

Impose the illiquid zero-drift equality simultaneously rather than after a liquid solve:

\[
g_a=r_a a+d_{ZZ}=0,
\qquad
d_{ZZ}=-r_a a.
\]

At cell185,

\[
r_a=0.08998919455428576,
\qquad
a=4.7368421052631575,
\]

so direct multiplication gives

\[
d_{ZZ}=-0.42626460578345887<0.
\]

The regime is therefore negative transfer. Because `a>\bar a`, the unchanged smooth D3 subgradient is

\[
\partial_d C=-\chi_0+\frac{\chi_1d_{ZZ}}{a}.
\]

The unchanged KKT equality

\[
0=q_a-q_b(1+\partial_d C)
\]

becomes

\[
q_a=kq_b,
\qquad
k=1-\chi_0+\frac{\chi_1d_{ZZ}}a
=1-\chi_0-\chi_1r_a
=0.7200216108914285.
\]

Since `k>0`, mapping the closed `a`-shadow interval through D3 gives

\[
q_b\in
\left[\frac{p_a^F}{k},\frac{p_a^B}{k}\right]
=[0.011790364625750628,\ 0.011910163904713082].
\]

Intersecting with the liquid derivative interval gives exactly the same interval:

\[
I_{ZZ}
=[0.011790364625750628,\ 0.011910163904713082]
\subset
[0.009574726769001294,\ 0.013362109688537174].
\]

The intersection is closed, strictly positive and nonempty. Its mapped `q_a` endpoints are exactly the accepted derivative endpoints `p_a^F` and `p_a^B`. Hence every point on the D3 line segment over `I_ZZ` lies inside the full two-axis derivative rectangle and satisfies the unchanged smooth negative-transfer KKT.

The two existing liquid-`Z` roots also lie numerically inside `I_ZZ`, but they are not the joint root: each pins `q_a` to an endpoint and therefore uses a transfer that is not `d_ZZ`. They supply crossing evidence, not a sequential construction of the joint candidate.

## Static joint liquid-root proof

With `d=d_ZZ` fixed, define

\[
F(q_b)=g_b(q_b,d_{ZZ})
=\bar w\left(\frac{q_b\bar w}{\eta}\right)^{1/\phi}
+r_b b+T-q_b^{-1/\gamma}-d_{ZZ}-C(d_{ZZ},a).
\]

The frozen scalars are `\bar w=12.783312529860462`, `\eta=1`, `\phi=5`, `\gamma=2`, `r_b=0.09`, `b=-0.1578947368421053`, and `T=0.1`. Direct substitution gives

\[
C(d_{ZZ},a)=0.08098566911979949.
\]

`F` is continuous for every `q_b>0`. Moreover,

\[
F'(q_b)
=\frac{\bar w l(q_b)}{\phi q_b}
+\frac{c(q_b)}{\gamma q_b}>0.
\]

Thus it is strictly increasing on the entire admissible interval. Direct endpoint substitution, with no root call, gives

\[
F(0.011790364625750628)
=-0.023007467717380714<0,
\]

\[
F(0.011910163904713082)
=+0.041147374843733764>0.
\]

For scale verification, the analytic derivative is positive at both endpoints (`539.0706665979479` and `531.9965966369532`), consistent with the global sign proof. By continuity and the intermediate-value theorem, at least one root lies strictly inside `I_ZZ`; by strict monotonicity, there is at most one. Therefore exactly one `q_b^*` exists. Algebraically define

\[
q_a^*=kq_b^*.
\]

It follows immediately that `q_b^*` and `q_a^*` lie strictly inside their respective one-sided derivative intervals, are finite and positive, satisfy D3 exactly, and produce `g_b=g_a=0`. No numerical root value is required or computed here.

## Hamiltonian and upwind legitimacy

At the joint candidate,

\[
q_b^*g_b+q_a^*g_a=0,
\qquad
H^*=u(c(q_b^*),l(q_b^*)).
\]

Both transport terms vanish because the physical drifts vanish, not because endpoint controls or derivatives are averaged. Consumption and labor are reconstructed from `q_b^*`; transfer is reconstructed from `g_a=0`; `q_a^*` follows from D3. There is no boundary multiplier because both state coordinates are interior.

The shadow pair lies in the closed rectangle formed by the one-sided finite-difference derivatives. In the accepted upwind semantics, positive speed chooses forward, negative speed chooses backward, and zero speed is tangent. The joint pair is therefore a legitimate coupled Godunov/viscosity switching closure: it supplies a two-dimensional subgradient point at which both characteristic speeds are zero. The strict endpoint evidence and unique interior solution prevent arbitrary derivative averaging or extrapolation.

This legitimacy does not make the rule already authoritative. It is a new coupled selection law. It cannot be obtained by first running liquid-`Z` and then running the adopted `a` switch, because the first step freezes an endpoint `q_a` and a different transfer. Nor can the order be reversed, because fixing `d_ZZ` changes the liquid equation being solved. The correct object is the simultaneous system plus its rectangle/KKT constraints. Explicit Owner adoption is therefore still required.

## Unchanged D2 consequence

If Owner later adopts the law and a reconstructed joint candidate passes the existing arithmetic-residual protocol, unchanged D2 consumes canonical `g_b=0` and `g_a=0`. Its existing sign logic then executes neither positive nor negative asset-drift branch, so the candidate contributes no liquid-asset transition rate and no illiquid-asset transition rate. Productivity transitions remain governed by the independently supplied frozen `z` generator. No artificial diffusion, leakage correction, clipping or boundary repair is implied. No Q was assembled in this task.

## Prospective generic joint-switching contract for Owner review

If Owner elects to adopt a generic law, the minimum contract should be:

1. **Domain.** Apply only at a node interior in both `b` and `a`, with the same empty asset-face active set and one common already-legal transfer regime. Boundary nodes remain governed by D1 and the accepted lower-`a`/liquid-face laws.
2. **Pre-trigger census.** Evaluate all ordinary one-sided candidates and the already-adopted one-axis candidates first. A joint trigger requires, for both `a` endpoints under the same regime, genuine strict liquid backward-positive/forward-negative crossings and legal liquid-`Z` receipts; the two liquid-`Z` outcomes must then form a strict arithmetic-bound-separated `a` crossing: backward-`a` `g_a>0`, forward-`a` `g_a<0`. Neither one-axis candidate may already be direction-consistent through zero.
3. **Simultaneous equations.** Impose `g_a=0` and `g_b=0` as one coupled system. Set `d_ZZ=-r_a a`; determine the transfer regime from its sign rather than choosing a sign to obtain a result.
4. **D3.** Use the unchanged D3 cost/subgradient. For nonzero transfer use the exact point relation `q_a=q_b(1+partial_d C)`. If `d_ZZ=0`, use only an independently authorized kink/subgradient selection; do not infer a new joint zero-kink rule.
5. **Rectangle geometry.** Require `q_b` in the closed sorted liquid derivative interval, `q_a` in the closed sorted illiquid derivative interval, and `q_b>0`. Map the `a` interval through D3 and intersect it exactly with the liquid interval. Empty, nonfinite or degenerate intersections reject fail-closed.
6. **Joint root.** On the exact intersection, evaluate the fixed-`d_ZZ` liquid equality. Require a static proof or later-authorized frozen root procedure to establish exactly one legal root. Missing, multiple, nonfinite or out-of-interval roots reject without widening, retry or tolerance tuning.
7. **Reconstruction.** Recompute `c,l,C,g_b,g_a`, D3 residuals and Hamiltonian from `(q_b^*,q_a^*,d_ZZ)`. Never interpolate endpoint controls, sequential one-axis roots or Hamiltonians. Canonicalize each zero drift only under the existing prospective arithmetic bound.
8. **Selection.** Include one reconstructed joint candidate in the unchanged policy deduplication and Hamiltonian comparison only after every existing D1/D2/D3/domain/finite check passes.
9. **Precedence and deduplication.** Ordinary and adopted one-axis candidates retain their current authority and receipts. The joint candidate is a separate final fallback triggered only by the coupled strict-crossing census. It is created once per node/active-set/regime, never once per order of axis solution, and is deduplicated by its reconstructed policy/shadow identity. It must not be labelled as either sequential `liquid-Z then a-Z` or `a-Z then liquid-Z`.
10. **Receipt.** Persist the four one-sided derivatives; ordinary liquid endpoint drifts/bounds; both liquid-`Z` receipts; post-liquid `a` endpoint drifts/bounds; `d_ZZ` and regime; D3 ratio/subgradient; both derivative intervals; mapped and intersected interval; fixed-transfer liquid endpoint values; uniqueness basis/root status; final shadows and raw/canonical drifts; KKT residual; Hamiltonian; D2 admissibility; comparison/deduplication identity; and every rejection reason.
11. **Preservation.** D1, D2, D3, ordinary upwinding, one-axis liquid-`Z`, one-axis interior-`a`, lower-`a` zero-kink, root tolerance/solver, grid, calibration, HJB update/convergence, terminal KFE and production routes remain unchanged unless separately authorized.

This contract is prospective only and conveys no implementation or runtime authority.

## Alternative explanations and generality

| Explanation | Static assessment |
|---|---|
| Grid spacing/discretization | Material. The derivative intervals and strict crossing are finite-grid objects. A refined grid may move or remove the local crossing, but that would not invalidate the prospective closure for grids where the coupled crossing and unique interval root occur. |
| V2 trajectory/initialization | Material and unresolved. V2 is not a converged fixed point; later authorized iterates could change or remove the crossing. The adjudication is conditional on the accepted frozen V2 derivatives. |
| Cell185-specific coincidence | The numerical values are cell-specific, but the geometry is generic: D3 maps one derivative interval into the other axis, and a fixed-transfer monotone equality can admit a unique joint zero. A generic trigger must therefore be equation- and interval-based, never cell-ID-based. |
| Finite-domain boundary interaction | Weak locally. Cell185 is interior in both assets, has no state-constraint multiplier and is not adjacent to a closure created by an active asset face. Global finite-domain effects on V2 derivatives cannot be excluded, but they do not explain the immediate local KKT geometry. |
| Sequential one-axis composition | Rejected. Each one-axis root freezes an endpoint object that the joint equations make endogenous. The two orders solve different equations and are not equivalent to the simultaneous system. |

The strongest supported interpretation is a missing prospective coupled upwind selection law conditional on the frozen V2 state, not proof of HJB nonexistence, equilibrium failure or a production defect.

## Zero-science ledger

| Operation | Calls |
|---|---:|
| selector evaluations | 0 |
| ordinary scalar roots | 0 |
| interior-liquid `Z` roots | 0 |
| interior-`a` switching roots | 0 |
| proposed simultaneous-switch roots | 0 |
| policy maps | 0 |
| D2/Q assemblies | 0 |
| Bellman/checkpoint diagnostics | 0 |
| HJB solves/updates | 0 |
| graph/SCC | 0 |
| KFE/SVD/eigen/nullspace/`Q.T@p` | 0 |
| MATLAB | 0 |
| outer/firm/wage-return/GE/annual/shock/IRF/Results | 0 |
| scientific retries | 0 |

Only static Git/source/document reads, persisted JSON parsing, SHA-256 hashing, symbolic derivation and direct scalar arithmetic/substitution were used. No selector, root, scientific helper, test or model module was imported or executed.

## Scope closure

The sole changed path is this report. No source, test, task, receipt, evidence root, CURRENT status/handoff/index, scientific law, calibration, grid, tolerance, solver or production path changed. Main is not merged and no successor task is published. Owner remains the only authority who may adopt the prospective joint law.
