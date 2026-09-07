# Call-725 boundary/generator repair specification

2026-09-07 — bounded Builder proposal; scientific adoption remains with Owner.

**BOUNDARY_GENERATOR_REPAIR_SPEC_COMPLETE__SCIENTIFIC_DECISIONS_EXPLICIT__NO_MODEL_RUN**

Fourteen authorized saved snapshots establish incompatible upper-face budget drifts, signed source rates, and omitted outgoing edges. Budget reconstruction agrees with captured mu_b/mu_a throughout all fourteen snapshots under the unchanged 128-eps comparison. The stored generator is a different object: its coordinate action need not equal those budgets. A repair that merely clips negative rates or removes outgoing edges cannot preserve an outward budget at a coordinate maximum while producing a closed, nonnegative, conservative generator.

Recommendation: preserve the frozen MATLAB-faithful reference and develop a separate target with jointly feasible boundary controls and a generator assembled from the same consumed total drifts. This is a proposed scientific/discretization change, not accepted parity or a production fix. Three decisions below delimit the proposal. Boundary repair does not establish resolution of P32's extreme interior policy, lost sigma, or Python's 500-step nonconvergence.

## Authority, inputs and scope

Working directory: `D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001`.
Remote: `git@github.com:zcx369658780/dissertation-ch5-two-asset-hank.git`.
Fresh-fetched effective main/base: `6de422f3125045ca23f0464de9013a22ac77e3fc`.
Branch: `codex/ch5-call725-boundary-generator-repair-spec-20260907`.
Exact authority: `tasks/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC.md` at that base; predecessor acceptances include `30438ea1468ddc59862f40574bd06c8625427e1b` and `2ff3eb212ea9a0d101183f9ff49dd1043bb6b886`. Read current AGENTS, index, status, relevant safety/scientific rules and the accepted diagnostic records. No historical task was restarted.

Evidence root: `D:\ProjectTemp\ch5-call725-boundary-generator-repair-spec-20260907-001`.
`consumed_inputs.json` binds consumed entries to the three exact predecessor manifests/inventory specified by the task; manifest/readback relationships pass. Historical CURRENT hashes are not compared against revised live documents. Binding SHA256 is `A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6`; frozen export Git blob is `9e7dc9556a2b76811e78f89999abecc045886106`. No rounded report values generated inputs.

Scope: both language replay outputs M24/P24/P32/M143_FINAL (8), original MATLAB52/57 and Python146/401/424/500 (6). M143_FINAL is the replay from the post-step143 terminal value. Coordinates are zero-based (b,a,z), shape (20,20,2), F order. `snapshots.json` lists exact files and eligibility, 14/14. `failures.json` is empty. Existing all-trajectory summaries and tail-switch coordinates are copied with provenance, not recomputed over 643 states. A total of 188 representative cells receive local old-expression reconstruction, never a complete policy mapping; every reconstructed saved control/rate comparison passes. Label-derived selection masks retain their prior caveat: reconstructed branch arithmetic is not independent runtime capture.

## Measured drift objects and attribution

For each stored c,l,d,C and effective illiquid return R, with exact scalar binding,

```
cash = (1-tau)*w*z*l + (rb + rbgap*1[b<0])*b + T - c
transfer_cash = -d-C
budget_b = cash + transfer_cash; budget_a = d + R*a
captured = saved mu_b, mu_a
operator_b = A @ vec_F(b_grid); operator_a = A @ vec_F(a_grid)
```

No model is imported to compute these arrays. `proxy_b=db*(bf-bb)` and `proxy_a=da*(af-ab)` expose the source channels before exterior edges are omitted. Let L be the sum of omitted signed outward rates, O_x their signed coordinate displacement, S the stored row sum, and C_x the compensated centered moment sum_j Aij*(xj-xi). The recorded decomposition is

```
A*x-budget = (proxy-budget) - O_x
             + [C_x-(proxy-O_x)] + x*S + floating residual.
```

It separates channel/control disagreement, omitted displacement, actual spacing/product rounding and leakage/cancellation. S+L is also retained: a nonzero row sum alone is not proof of a missing edge. Ordinary matvec, compensated reductions and 80-digit Decimal products of exact stored binary64 operands are preserved at witnesses. Decimal here is finite-precision diagnostic accumulation, never a solve. The 128-eps count describes same-object differences, not a new generator admissibility threshold.

| Snapshot | Negative offdiagonal entries | Omitted rows | Material outward budget rows | A*b mismatch | A*a mismatch |
|---|---:|---:|---:|---:|---:|
| MATLAB M24 |26|19|30|19|132|
| Python M24 |26|19|30|19|135|
| MATLAB P24 |26|19|30|19|144|
| Python P24 |26|19|30|19|142|
| MATLAB P32 |27|30|32|30|260|
| Python P32 |27|30|32|31|260|
| MATLAB M143_FINAL |18|15|20|15|143|
| Python M143_FINAL |18|15|20|15|142|
| MATLAB trajectory52 |37|36|44|37|140|
| MATLAB trajectory57 |35|33|42|33|134|
| Python trajectory146 |12|30|14|33|124|
| Python trajectory401 |11|24|13|26|108|
| Python trajectory424 |12|24|14|27|98|
| Python trajectory500 |12|24|14|25|95|

Budget/captured mismatch counts are zero for both axes in every row. Operator counts include representation effects; they must not all be labelled boundary defects. Full 2,256 anomalous rows remain in external `anomalous_rows.csv`; the published compact index retains every affected row, signs, coordinate actions and sparse neighbors. All 112 corner rows and 112 face/productivity summaries are published. Lower-a budgets are zero and lower-b budgets are inward/nonnegative in the selected scope. Upper-a has 226 material outward face occurrences and upper-b 139 across snapshots (not distinct states).

### Concrete witnesses

| Saved state / row (b,a,z index) | Evidence and implication |
|---|---|
| MATLAB M143_FINAL /380 (0,19,0) | Consumed d=0, mu_a=0.81, mu_b=2.610478495918538. ab=-1.5390000000000001, af=0; A*a=0.8100000000000067. At maximum a, this positive drift is impossible for a closed nonnegative generator. Row780 in the other productivity state has the same a violation. |
| MATLAB M143_FINAL /419 (19,0,1) | d=0, budget_b=0.003191811930404853>0; omitted bf=0.0086634895253846, row sum=-0.008663489525384593; A*b=-0.04331744762692313. Apparent inward coordinate action is caused by mass leakage and does not certify feasible controls. Row19 has the analogous failure. |
| MATLAB52 /799 (19,19,1) | Consumed d=0 and cost=0, budget_a=0.81; shadow B candidate=9633.797114182187 survives in the upper-a rate replacement even though the consumed upper-a selector discarded it. Forced upper-b B selection gives ab=-18305.753516946155 and A*a=9634.607114182203. budget_b=-325.0811884545149 is inward but does not cure the other axis. |
| Python146 /399 (19,19,0) | d=0, budget_a=0.81, budget_b=-395.373475699577; shadow B=12373.902574903505 gives ab=-23511.95389231666 and A*a=12374.712574903524. |
| MATLAB57 /379 (19,18,0) | d=-2.2905518322685587, cost=0.7828658845039015; cash=0.002789998755979184 and transfer cash=1.5076859477646574. Forced upper-b backward label produces bb=-4.092290429646927; bf=0.007572853766229213 is omitted. Budget_b=1.5104759465206365 versus A*b=1.469821678933513; leakage also contaminates A*a (-1.5620751772656294 versus budget -1.490332352111885). |
| MATLAB P32 /704 (4,15,1), interior | d=33970754456.593735, cost=1.4617487339442027e20; budget_b=-1.4617487342839102e20. No exterior edge is omitted. budget_a=33970754457.295795 but A*a=33970796948.732727; stored compensated row sum=-6850.804651896159. The a channel gap is zero. Unclamped transfer denominator=1.0727926483663655e-13. This is an extreme interior policy/representation issue, not an omitted boundary edge. |

The eight MATLAB terminal corner rows are 0,19,380,399,400,419,780,799. Rows19/419 violate upper-b; 380/780 violate upper-a; the other four have inward or zero budgets. The complete numeric table, including the other snapshots, is in `corners.csv`. Necessary inward signs do not certify all split rates, KKT optimality, or a globally valid policy.

At tail coordinate398=(18,19,0), Python401/424/500 transfer labels are F/B/B with budget_a -6.892388511626301/-1816.0171224647195/-1808.9532269776137. At790=(10,19,1), liquid labels B/0/B accompany a budget of 0.81 in all three. Accepted tail summaries report 100 transfer changes at398 and 67 liquid changes at790. These three sampled states do not independently establish a full switching history or limit cycle.

For a closed generator Q, qij>=0 (i!=j), Q1=0 implies Qx_i=sum_{j!=i}qij(xj-xi). At a maximum Qx_i<=0; at a minimum Qx_i>=0. Thus the positive upper-coordinate budgets above cannot be retained together with closed nonnegative conservative assembly. This is an algebraic impossibility for the stored controls, not adoption of a reflecting, absorbing or state-constraint law.

## Source versus proposal and authority

Exact source map is also published as `source_map.json`. Frozen export source locations below refer to the bound blob, not newly executed code.

| Item | Current source / status | Proposed contract / status |
|---|---|---|
| Scalar inputs, taper and budgets | CURRENT_FROZEN_AUTHORITY: exact binding, export83,159-167,378-399 | Preserve inputs and one consumed control tuple. DERIVED_IDENTITY: budgets and reported drifts must denote that tuple. |
| Transfer candidates | CURRENT_FROZEN_AUTHORITY: export85-110 uses bare a and raw vb; cost83 uses max(a,a_bar). | PROPOSED_REQUIRES_SCIENTIFIC_DECISION D3: derive FOC from one explicitly chosen cost, rather than transplanting a stabilizing denominator. |
| Consumed/shadow selection | CURRENT_FROZEN_AUTHORITY: export306-319,348-376; forced upper-b label and upper-a replacement can bypass consumed d. | PROPOSED_REQUIRES_SCIENTIFIC_DECISION D1/D2: jointly feasible consumed boundary policy; no shadow candidates consumed by target assembler. |
| Split rates | CURRENT_FROZEN_AUTHORITY: export403-413, including separate cash and transfer rates. | D2: total-drift monotone rates. This changes finite-grid numerical diffusion even at equal net drift; it is not an exact refactor. |
| Exterior edges/diagonal | CURRENT_FROZEN_AUTHORITY: export427-448 drops exterior neighbors while retaining -(rb+rf). | D1/D2: under explicitly adopted closed state constraint, reject outward policy first, retain only nonnegative interior edges, diagonal=-retained rate sum in mathematical arithmetic. |
| Lower/upper bounds | CURRENT_FROZEN_AUTHORITY: GridSpec in src/ch5_two_asset_hank/contracts.py identifies a=0 and b_bar economic lower constraints. | UNRESOLVED upper law: finite a_max/b_max are truncation locations, not authority for new economic caps. |
| Representation/convergence | CURRENT_FROZEN_AUTHORITY: accepted frozen-linear report records sigma loss, crossed-input solver differences and original-unit residuals. | UNRESOLVED beyond boundary scope. No nextafter/diagonal inflation, derivative floor, cap, damping, solver replacement or scaled production HJB is proposed as an adopted fix. |

Historical R4 truncation and PRE_P5 boundary-degeneracy reports were consulted only for design context. Their fixture-specific acceptance and test-only O1 max(a,a_bar) FOC do not authorize this target, revive old runtimes, or replace the current 128-eps comparator. Existing KKT utility in `boundaries.py` is a sign-convention precedent, not current MP4C adoption authority.

### Three serious options and minimal decisions

| Scope | Benefit | Cost / exclusion |
|---|---|---|
| A: frozen-source diagnostic only | Preserves MATLAB fidelity and existing FAIL evidence. | Leaves demonstrated infeasibility and signed/nonconservative generators unresolved. |
| B: recommended separate boundary/total-drift target | Resolves the identified consumed/shadow and closed-grid contradictions once scientifically adopted; explicit joint corner policy. | Requires D1-D3 below, changes discretization, can reject invalid derivative domains; does not promise interior admissibility or convergence. Interior controls initially remain reference-derived with explicit validity flags. |
| C: broader constrained-policy/FOC redesign | May address the extreme interior policy and derivative-domain failure B cannot resolve. | Larger scientific change and validation burden; no evidence yet selects a floor/cap or proves a finite interior optimum. Defer beyond B, retaining the P32 failure. |

| Owner decision | Concrete options | Recommendation and consequence |
|---|---|---|
| D1 artificial upper truncation law | Explicit numerical state constraint on the finite box; or specify exterior continuation/expanded-domain treatment. | Use state constraint for the diagnostic target only, with future truncation sensitivity required. This restricts controls at the artificial upper faces; it is neither an asserted economic saving cap nor automatic reflection/absorption. Exterior continuation would require new value/flux data and a different mass contract. |
| D2 finite-grid assembly | Retain separate flow upwinding with all channels jointly constrained; or upwind the consumed total budget drifts. | Total drift: removes shadow/consumed ambiguity and avoids unnecessarily constraining offsetting flows. It changes artificial diffusion; target correctness and frozen-source fidelity require separate test tracks. |
| D3 adjustment technology at a=0 | Derive target FOC from saved regularized cost s=max(a,a_bar); or adopt a different explicit zero-asset cost/admissible-transfer law. | Retain the saved cost and use its actual d derivative throughout target KKT. This is a consistency proposal requiring approval, not a floor introduced to pass P32. At positive grid a>=a_bar this denominator choice agrees with bare-a, so it does not resolve P32's tiny qb. |

Already settled matters are not reopened: reference preservation, economic lower-bound identity, post-boundary policy derivatives as primary comparison, original input binding, unchanged same-object 128-eps rule, and no annual/Results acceptance.

## Proposed joint boundary Hamiltonian/KKT contract

Written derivation only. Let wnet=(1-tau)wz, Rb include the bound borrowing gap, Ra be the frozen effective return, and s(a) the D3-selected technology. Define

```
g_b = wnet*l + Rb*b + T - c - d - C(d,a)
g_a = Ra*a + d
C(d,a) = chi0*abs(d) + chi1*d^2/(2*s(a))
H = u(c,l) + p_b*g_b + p_a*g_a
```

For each binding face i, set t_i=+1 at a lower bound and -1 at an upper state constraint, require t_i*g_i>=0, lambda_i>=0 and lambda_i*t_i*g_i=0. Inactive faces have lambda_i=0. Define q_i=p_i+t_i*lambda_i (sum applicable terms). At corners both coordinate constraints apply simultaneously; sequential source label overrides are not a joint solution.

For c>0, c^(-gamma)=q_b>0. For l>=0, `-alpha*l^phi+q_b*wnet+eta_l=0`, eta_l>=0, eta_l*l=0. For transfer, `0 in q_a-q_b*(1+partial_d C)`:

- d>0: q_a/q_b=1+chi0+chi1*d/s(a).
- d<0: q_a/q_b=1-chi0+chi1*d/s(a).
- d=0: q_a/q_b in [1-chi0,1+chi0].

Face constraints are lower-a d>=0, upper-a d<=-Ra*a_max; lower-b c<=wnet*l+Rb*b+T-d-C; upper-b c>=that expression. At corners these couple c,l,d and the multipliers. Both active equality and slack inward cases must be considered, with kink and Hamiltonian checks, not just a transfer ratio candidate. Cost convexity, q_b>0 and admissible derivative branches delimit this derivation. q_b<=0 is a domain failure requiring diagnosis, not permission to clamp. KKT stationarity alone is not a certificate of a globally selected finite-grid policy; future selector must check feasibility, complementarity, derivative-direction consistency and admissible Hamiltonian comparison. No root/optimization was performed here.

Given an adopted feasible drift, target rate in each axis is the positive/negative part divided by the actual corresponding neighbor distance. Retain only allowed edges and use the negative retained outgoing sum for the diagonal, with the unchanged productivity generator. If an upper outward drift is supplied, reject it rather than silently omit/clip. A coordinate test then checks intended drift; floating point distance/accumulation error is separately budgeted. Separate-flow upwinding can have both opposite channels nonzero and a different diffusion term, so it cannot silently substitute for this contract.

## Future files, API and bounded validation proposal

No following file or policy is implemented by this task. Proposed namespace `src/ch5_two_asset_hank/repair_target/`:

| File / API | Contract |
|---|---|
| contracts.py / BoundaryClosureSpec | Explicit upper law, cost law, authority identifier, binding identity, (b,a,z) shape/F-order. Include T, borrowing gap and effective Ra without defaulting missing fields. |
| policy.py / select_constrained_policy | Return a single consumed c,l,d,cost,g_b,g_a, utility/H, derivative-domain flags, active constraints, slacks, multipliers and zero-transfer kink residuals; reject invalid domains. |
| boundary.py / boundary_constraints | Joint face/corner inequalities; explicit state-constraint law, no implicit reflection. |
| generator.py / assemble_budget_generator | Consume only policy drifts and grids, never shadow labels; nonnegative retained rates, conserved mathematical diagonal, independent coordinate diagnostic. |
| diagnostics.py / serialize_target | Record target law/version separately from frozen reference, including representation budgets and failed checks; retain old failed parity rows. |

Smallest proposed successor after decisions: one implementation/test work unit with synthetic face/corner active/slack/kink tests and an assembler-only pass on the same 14 saved control snapshots. **Real target policy calls=0, direct/root/optimization=0, HJB=0** in that first implementation validation budget: outward rows must be rejected as expected, never silently repaired. Implementation must not execute a target optimizer during tests unless separately authorized. This checks the contract meaningfully while maintaining a bounded no-solve initial step.

Then propose a separately authorized ten-cell boundary-policy validation: eight MATLAB M143_FINAL corners plus MATLAB52 row799 and MATLAB57 row379, each at most one target selector evaluation. Before issuing it, Reviewer must bind derivative/state inputs and preregister a finite active-set/root budget (proposed at most four face-active sets times three transfer-sign regimes, at most one root invocation per regime, so <=120 root invocations overall, no retry for adverse numerics). This ceiling is a proposal for explicit review, not current authorization or a claim that every regime requires solving. No full HJB call accompanies it. Only after these pass should a new task consider one target HJB step (one policy map and one direct solve), with no automatic long trajectory.

Tests must cover all faces and corners, active/slack complementarity and transfer kink; c/l/d budget association; invalid-domain rejection; offdiagonal nonnegativity, mass conservation, coordinate drift; interior split-versus-total diffusion distinction; missing-edge contamination of the other coordinate; zero/large row scales and cancellation. Unchanged-reference comparisons retain 128 eps. New target floating residual checks should use prospectively derived operation-count bounds, e.g. gamma_n=n*eps/(1-n*eps) times sum of absolute products plus spacing error, with exact/Decimal checks of synthetic small cases. Never fit a tolerance to these failures. Mathematical signs and law selection are not replaced by a floating tolerance.

KFE mass/nonnegativity, nonlinear HJB convergence, GE/annual coverage and Results each remain dependent claims requiring future evidence and authority. No proposed step was executed.

## Actual checks, ledger and publication

Actual science ledger: new HJB/policy/evaluator=0; direct/root/optimization/condition estimator=0; MATLAB processes=0; trajectories/KFE/GE/annual/dynamics/IRF/Results=0. Fourteen saved snapshots were analyzed, 188 cells received only local legacy arithmetic. No scientific retry exists or was consumed.

Focused synthetic tests: final attempt **10 ran / 10 individual ok / OK**, parsed from real unittest output. First attempt retained **10 ran / 9 ok / 1 failure**: the AST-copy test skipped an incorrect number of semicolon-separated statements and failed to normalize the intentionally parameterized binding locator. Test normalization was corrected; diagnostic arithmetic and scientific inputs were unchanged. Raw stdout/stderr bytes are encoded with SHA256 in `tests_attempt_*.raw.json`; readable logs use LF with a distinct hash. No dependent commit/push ran after the failed test.

Published evidence in `reports/call725_boundary_generator_repair_spec_20260907/`: compact anomalous-row index, all corner/face tables, representative rich witnesses, full consumed-input receipt, summary, source map, ledger, actual test attempts, and finite manifest/readback. Full rich arrays/tables remain external and hash-bound. Manifest excludes itself and terminal receipts; repository text entries use explicitly identified LF normalization while external artifacts use raw bytes. Publication checks verify the allowed changed paths and staged Git bytes before commit.

Original main checkout and its unrelated untracked files, historical branches, production and helpers remain untouched. No global/Zotero changes. Dedicated branch publication is for Reviewer acceptance only; no merge or successor execution.
