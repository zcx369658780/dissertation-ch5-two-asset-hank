# Chapter 5 MP4C 2018 KFE Owner-decision recovery and option matrix

Date: 2026-09-16

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Role: bounded Builder / zero-science repository-authority recovery

Fresh-start `origin/main`: `e609f248a09e665e36323e8bcabf5d8a866f32b0`

## Verdict

`PASS__D1_D2_D3_EXACT_REPOSITORY_AUTHORITY_RECOVERED__OWNER_KFE_CLOSURE_DECISION_REQUIRED__ZERO_SCIENCE`

D1, D2 and D3 are uniquely recoverable from repository history. They are the three proposed decisions for a **separate corrected diagnostic target** in the accepted call725 boundary/generator specification; none is an adopted production repair. The later transfer-control safeguard also named `D1` is a different object and is not substituted into this recovery.

The accepted corrected-2018 KFE blocker remains unchanged: finite-box upper-`b` escape is paired with a MATLAB-style dropped-equation/pinning solve whose omitted source-free equation is algebraically equivalent, at the saved density, to a balancing source. Repository authority does not identify that source as an economic household entry/exit process. Owner selection of finite-domain/KFE closure semantics is still required before implementation or scientific validation.

## Authority and history recovery

The defining history is one direct three-commit chain:

1. `6de422f3125045ca23f0464de9013a22ac77e3fc` published `tasks/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC.md`. Lines 55–66 require an explicit artificial-upper-bound law, distinguish total-drift from separate-flow upwinding, require a conservative retained-rate diagonal, require cost/FOC consistency, preserve the frozen MATLAB-faithful reference, and keep KFE mass a dependent claim.
2. `15f51be9733b5043e738d3e522b97554e95902b9`, the direct child of `6de422f…`, added `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_REPORT.md`. Its lines 107–109 define D1–D3; lines 88–91 map them to source objects; lines 115–135 give the conditional KKT contract; lines 138–154 give the bounded future validation sequence.
3. `da543d7960451da5b2ed9f67dae906269d45b273`, the direct child of `15f51be…`, added `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_ACCEPTANCE.md`. Lines 39–41 restate and accept the exact proposal definitions while retaining status `PROPOSED_REQUIRES_OWNER_ADOPTION`; line 44 says one Owner confirmation of the bundle is sufficient for the independent diagnostic target but does not authorize production replacement or computation.

`git blame` assigns report lines 107–109 exactly to `15f51be…` and acceptance lines 39–41 exactly to `da543d7…`. No later commit rewrites those definitions.

| Item | Recovery status | Exact recovered definition | Controlling repository location |
|---|---|---|---|
| D1 | `RECOVERED_FROM_REPOSITORY_AUTHORITY` | Artificial upper truncations: for the independent diagnostic target, use explicit numerical state constraints on the finite box while retaining the economic lower bounds. The unselected alternative is an explicitly specified exterior-continuation or expanded-domain treatment with its own value/flux/mass contract. State constraint is not an economic saving cap and is not automatic reflection or absorption. | Acceptance `da543d7…`, `docs/CH5_MP4C_CALL725_BOUNDARY_GENERATOR_REPAIR_SPEC_ACCEPTANCE.md:39`; originating proposal `15f51be…`, report line 107. |
| D2 | `RECOVERED_FROM_REPOSITORY_AUTHORITY` | Generator discretization: assemble from the same consumed total budget drifts, actual neighbor distances and nonnegative retained rates; reject outward boundary inputs and set the mathematical diagonal to minus the retained outgoing-rate sum. The unselected alternative is separate-flow upwinding with every channel jointly constrained. | Acceptance `da543d7…`, acceptance line 40; originating proposal `15f51be…`, report line 108. |
| D3 | `RECOVERED_FROM_REPOSITORY_AUTHORITY` | Cost/FOC consistency: retain the existing regularized adjustment cost and coefficients, with `s(a)=max(a,a_bar)`, and derive the target KKT transfer condition from that same cost throughout its domain, including `a<a_bar` and `a=0`. The unselected alternative is a different, explicitly specified zero-asset cost/admissible-transfer law. No derivative floor, transfer cap or different adjustment technology is part of the recovered recommendation. | Acceptance `da543d7…`, acceptance lines 31 and 41; originating proposal `15f51be…`, report lines 88, 109 and 115–135. |

The fail-closed marker `NOT_RECOVERED_FROM_REPOSITORY_AUTHORITY` is not used because all three exact definitions and their acceptance provenance were recovered.

### Name-collision exclusion

Commit `c7d29f5bc0751751f1547072eac79eff916a8240` later introduced a temporary transfer-candidate magnitude safeguard also named D1. Its contract is symmetric `[-1e5,+1e5]` branch rejection and is unrelated to the KFE closure D1 above. It is excluded from this option matrix. The commit changed the export by adding an optional filter whose default is off; it did not change `src/ch5_two_asset_hank/matlab_faithful_hjb.py` or `src/ch5_two_asset_hank/matlab_faithful_kfe.py`. Current live authority continues to accept the five-turn KFE mechanism.

## Current accepted leakage and pinning mechanism

The controlling current documents are `docs/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION_ACCEPTANCE.md`, `docs/CH5_MP4C_2018_FIVE_TURN_KFE_LEAKAGE_ATTRIBUTION_REPORT.md`, and `reports/mp4c_2018_five_turn_kfe_leakage_attribution_20260910/source_code_attribution.json`.

1. **Finite-box upper-`b` escape.** For every corrected-2018 turn4/5 province-turn object (62/62), occupied upper-`b` cells have positive outward drift. The finite-box assembler omits the unavailable outside-grid offdiagonal but retains its rate in the diagonal. Current live source still exposes that rule in `exports/matlab_faithful_two_asset_ha.py:492–517`; post-loop `Q` is rebuilt from saved `mu_b/mu_a` in `src/ch5_two_asset_hank/matlab_faithful_hjb.py:115–116`.
2. **Source-free residual.** For the normalized saved density `g`, the unmodified stationary equation is `Q.T @ g = 0`. The material residual is not diffuse: pin-row L1 share is `0.9999999999869693–0.9999999999982326`, and the maximum individual off-pin residual is `5.352822169074709e-15`, below the frozen componentwise `128 eps` bound.
3. **Dropped pin equation.** The MATLAB-faithful KFE path transposes `Q`, replaces the row selected by `floor(.37*M)-1`, sets the replacement RHS to `.007`, solves, and normalizes (`src/ch5_two_asset_hank/matlab_faithful_kfe.py:25–47`). At the accepted 800-state grid this is zero-based row `k=295`. The `.007` fixes raw-vector scale; it is not a probability-flow rate.
4. **Algebraic balancing source, not economics.** Restoring the dropped source-free equation reveals a residual that balances density-weighted upper-`b` escape at floating-point scale. Replacing that equation is therefore algebraically equivalent at the saved solution to inserting a balancing source. No source code implements household entry/exit, and no accepted authority adopts such an economic mechanism.

Negative density mass is machine-scale and does not explain the material residual. HJB-loop operators are a distinct object; the accepted mass ledger uses only the post-loop operator.

## Algebraic closure facts common to the options

For a row generator `Q` on a closed finite state space, nonnegative offdiagonals and `Q 1 = 0` imply

`(Qx)_i = sum_{j != i} q_ij (x_j - x_i)`.

At a coordinate maximum this cannot be positive, and at a minimum it cannot be negative. Thus a positive upper-face budget drift cannot simultaneously be preserved as-is and represented by a closed, nonnegative, conservative generator. Clipping a signed rate or deleting an outward edge while retaining its diagonal cannot resolve that contradiction.

If a selected D1 policy supplies inward/feasible face drifts and D2 builds `Q` with diagonal equal to the negative sum of retained outgoing rates, then `Q 1 = 0` by construction and total source-free KFE mass obeys `1.T Q.T g = 0` algebraically. In that conservative case a pin row may set scale only if the removed stationary equation is genuinely redundant and the normalized solution also satisfies it; this must be checked, not presumed. D3 affects the controls and hence the drifts entering this identity, but does not alone guarantee conservation.

## Owner option matrix

All three rows remain `PROPOSED_REQUIRES_OWNER_ADOPTION`. “HJB boundary semantics” distinguishes the economic/finite-domain law from changes to discretization or an interior/low-`a` FOC.

| Item | Finite-domain / KFE object changed | HJB boundary semantics | Classification and MATLAB parity | Algebraic mass consequence | Asset-domain / grid consequence | New economic assumption | Smallest future validation after Owner selection |
|---|---|---|---|---|---|---|---|
| D1 — explicit upper state constraints | Changes admissible controls/drifts at artificial upper `a`/`b` faces and corners before operator/KFE assembly. Exterior/expanded treatment is the alternative, not an implicit fallback. | **Yes.** Joint face/corner state-constraint feasibility and KKT/complementarity replace sequential legacy upper-face overrides for the corrected target. | Corrected-successor diagnostic target; not source-faithful and not MATLAB parity. Frozen MATLAB-faithful reference and its failures remain unchanged. | State constraints can remove outward face inputs required for a closed generator, but D1 alone does not prove `Q 1=0`; it must be paired with an adopted assembly. Exterior continuation instead needs an explicit flux/mass contract. | State-constraint branch can retain the existing finite coordinates and `bmax/amax`, but changes their meaning to explicit numerical truncation faces and requires later truncation sensitivity. Expanded-domain choice changes grid/domain and also changes state-count-dependent pin identity. | The recovered state constraint is a finite-domain closure choice, explicitly **not** an asserted economic saving cap, reflection or absorption. A different exterior law may add assumptions that must be stated by Owner. | First, synthetic face/corner active/slack/kink tests plus assembler-only rejection checks on the same 14 saved control snapshots, with zero real selector/HJB/KFE calls. Then, under a separately budgeted task, at most one corrected-target selector evaluation at each of the eight M143_FINAL corners plus MATLAB52 row799 and MATLAB57 row379. |
| D2 — consumed-total-drift conservative assembly | Replaces legacy separate cash/transfer channel assembly for the corrected target with rates derived from the single consumed total drift, actual neighbor distances, nonnegative retained edges, outward-input rejection and a conservative diagonal. | **No new boundary law by itself**, but if used by HJB it changes the finite-grid HJB operator/discretization. It depends on the D1 closure for legal face inputs. | Corrected-successor numerical redesign. Authority explicitly says total-drift upwinding is **not** a faithful refactor of MATLAB separate-flow upwinding; target-correctness and frozen-reference parity are separate tracks. | For admissible inputs, diagonal `=-sum(retained rates)` gives `Q 1=0`; hence the source-free KFE has zero algebraic total mass leakage. This removes the accepted retained-diagonal/omitted-edge mechanism but does not by itself prove nonnegative stationary density, uniqueness, rank, or pin-row redundancy. | Uses actual distances on the selected grid and does not itself change `bmax`, `amax`, `I` or `J`. Numerical diffusion changes even at equal net drift. | No new household preference/technology assumption; it is a discretization choice. It cannot silently legalize an outward boundary policy. | One assembler-only pass on the same 14 saved snapshots plus synthetic faces/corners: check outward inputs reject, offdiagonals are nonnegative, diagonal is the exact mathematical retained-rate sum, `Q 1=0`, coordinate drift matches the consumed drift where representable, and legacy-reference outputs remain separately preserved. No solve is required. |
| D3 — regularized-cost / FOC consistency | Changes the corrected target’s transfer KKT/FOC wherever `a<a_bar`, including `a=0`, so policy/drifts passed to HJB/KFE derive from the same saved cost `s(a)=max(a,a_bar)`. | **No change to upper-face boundary law**, but it changes the HJB policy/KKT scientific object at low `a` and interacts with joint corner constraints. | Corrected-successor target, not MATLAB parity at low `a`; the legacy bare-`a` FOC remains in the frozen faithful reference. At `a>=a_bar` this denominator choice agrees with bare `a` and does not fix P32’s tiny-`q_b` issue. | No direct conservation guarantee. It removes a cost/FOC inconsistency that can alter selected transfer and drifts; those drifts must still pass D1 feasibility and D2 conservation checks. | No domain, grid or upper truncation change. `a_bar` and all cost coefficients remain unchanged. | Under the recovered recommendation, **no new adjustment technology or coefficients** are introduced; the target consistently differentiates the existing regularized cost. Choosing a different zero-asset law would be a new economic assumption requiring explicit specification. | Synthetic low-`a`/`a=0` transfer-sign and zero-transfer-kink KKT tests, followed within the same separately authorized ten-cell selector panel by the low-`a` corners. Bind derivative/state inputs and finite root/active-set budgets before any evaluation; do not add a derivative floor or transfer cap. |

The accepted specification’s combined sequence is narrower than a KFE rerun: implement/test the selected contract first with synthetic arithmetic and saved controls; only then run the separately authorized ten-cell selector panel; only after those pass consider one target HJB step. KFE mass/nonnegativity remains a later dependent validation claim with an explicit budget. No step in that sequence is authorized by this report.

## Source-faithful reference versus corrected successor

- **Source-faithful diagnostic option A:** keep the frozen MATLAB-faithful policy/operator/KFE exactly as evidence. This preserves parity and the accepted FAIL/leakage evidence; it does not close the KFE blocker.
- **Corrected successor option B:** the repository Reviewer recommended the combined D1 state-constraint + D2 consumed-total-drift conservative assembly + D3 regularized-cost-consistent KKT bundle for an independent diagnostic target. This is a recommendation already present in `da543d7…`, not adoption by this report.
- **Broader option C:** a wider constrained-policy/FOC redesign may be required for the extreme interior P32 issue, but repository evidence selects no floor, cap or finite interior optimum. It remains deferred and is not a substitute D1/D2/D3 definition.

Production MATLAB/Python remains unchanged. A corrected successor must carry a separate authority identifier and separate correctness tests; it must not overwrite or relabel frozen-source parity evidence.

## Non-options already ruled out by accepted authority

- Automatically expand `bmax`/`amax`, change `I/J`, or infer that a larger grid removes leakage. An expanded domain is only a D1 alternative after Owner specifies its closure/value/flux/mass contract and downstream pin identity.
- Silently declare artificial upper bounds to be economic saving caps, or silently choose reflection/absorption.
- Clip negative rates, drop an outward edge while retaining its diagonal, patch only the diagonal, or move/delete/transplant the pin row merely to force PASS.
- Treat RHS `.007` or the dropped-equation balance as an economic household entry/exit source; insert a source without an Owner-adopted economic law.
- Add a liquid-derivative floor, transfer cap, different adjustment technology, nextafter inflation, damping, solver replacement, tolerance tuning, or post-hoc diagonal patch.
- Require a corrected target to match known-invalid legacy boundaries, erase old failed parity rows, or call corrected-target validity “MATLAB parity.”
- Assume D1–D3 resolve P32’s extreme interior transfer/cost, lost sigma, nonlinear HJB convergence, nonnegative/unique KFE density, GE, annual, shock, IRF or Results.
- Continue synthetic local-basin refinement or choose a closure merely because it produces convergence or mass conservation.

## Compact Owner decision form

Repository Reviewer recommendation, still unadopted: **Option B as one independent diagnostic-target bundle** — D1 state constraint + D2 consumed-total-drift conservative assembly + D3 existing regularized-cost-consistent KKT.

Owner should complete exactly the following:

1. **D1 upper finite-domain law:** `[ ]` explicit numerical state constraint on the existing finite box; **or** `[ ]` exterior continuation / expanded domain, with the exact value, flux, mass, grid and pin-identity contract attached.
2. **D2 assembly:** `[ ]` consumed-total-drift upwinding with actual distances, outward-input rejection, nonnegative retained rates and conservative diagonal; **or** `[ ]` separate-flow upwinding with every channel jointly constrained and its conservation contract attached.
3. **D3 low-`a` cost/FOC law:** `[ ]` retain the existing `s(a)=max(a,a_bar)` cost and use its actual derivative throughout target KKT; **or** `[ ]` provide a different explicit zero-asset cost/admissible-transfer law and identify the new economic assumption.
4. **Adoption scope:** `[ ]` independent diagnostic corrected target only (the scope recommended in repository authority); any production replacement, runtime budget, or Results use requires a later Reviewer task and is not authorized here.

If Owner selects the three repository-recommended boxes, Reviewer can publish one bounded implementation/test task followed by the preregistered selected-cell validation. If Owner selects an alternative box, the missing contract named beside that box must be supplied before implementation.

## Exact zero-science call ledger

| Category | Calls |
|---|---:|
| HJB | 0 |
| KFE | 0 |
| outer loop | 0 |
| firm | 0 |
| wage/return recalculation | 0 |
| MATLAB | 0 |
| GE | 0 |
| annual | 0 |
| shock | 0 |
| IRF | 0 |
| Results | 0 |

Only static Git/history reads, hashes, textual diffs, source-line mapping, and read-only inspection of designated repository source were used. No model module was imported or executed; no solver, selector, evaluator, matrix solve, policy map, saved-array recalculation, or scientific retry was performed.

Results eligibility=`FALSE`.
