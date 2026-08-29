# Chapter 5 Two-Asset HANK P5 Acceptance-Design Revision and Evidence-Sufficiency Review

## Terminal classification

`P5_REVISED_ACCEPTANCE_DESIGN_READY_FOR_OWNER_DECISION`

Conditions 1–11 of the revised P5 standard are supported. Condition 12—explicit Owner review and acceptance—is the only pending condition. This report does not issue `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION` and does not authorize dynamics or Results.

## Live authority and continuity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- Live start `origin/main` after fresh fetch: `528a910c46297841c15c0732ff5f0b8744fc6af0`
- Live `origin/main` at report freeze, before report-only publication: `528a910c46297841c15c0732ff5f0b8744fc6af0`
- Both the original P5 review task and its resumption task were present on live main. The resumption authority was applied wherever it adds later evidence or scope clarification.
- Accepted Python scientific baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`: empty.
- No parity, diagnostic, or review task changed production source/tests to manufacture agreement.

## Revised P5 review principle

P5 evaluates Python scientific correctness using closed economic authority, shared-input modular MATLAB/Python parity on every materially common object, and independently qualified integrated Python steady-state evidence. It does not require literal equality to an unqualified legacy MATLAB full-HJB pinned stationary vector whose lower-bound equation, numerical taper, and stationary construction are outside the accepted common object.

No P1–P4 or R4 tolerance is changed. The revision changes only whether the legacy pinned full-HJB stationary vector is mandatory as the final integration oracle.

## Complete E1–E9 evidence matrix

| ID / required claim | Evidence category | Exact accepted report/commit/source | Accepted status | Comparison type | Numerical/structural result | Unresolved limitation | Material to current Python correctness? | Revised-P5 disposition |
|---|---|---|---|---|---|---|---|---|
| E1a two-asset identity/accounting | Economic/equation authority | Owner parity/helper audit, commit `13348e595bc2aefb7610b49cac3dfa9e97fb02fb`; dissertation equations `(3-18)`–`(3-22)`, `(3-26)` | accepted | structural/equation | state `(a,b,z)`; liquid `b`, domestic illiquid `a`; separate drifts/accounting | none | no | PASS |
| E1b adjustment technology and lower-bound redesign | Economic/equation authority | Owner parity/helper audit `13348e5…`; shared-input P1/P2 reports `1b26e9c…`, `565c656…` | accepted O1/O3–O6 | equation proof plus controlled parity | `m(a)=max(a,a_bar)`; cost and Python FOC/KKT use common scale; legacy bare-`a` FOC below `a_bar` is bounded non-comparability | legacy MATLAB forces different low-`a` transfer | no; explicitly accepted redesign | PASS |
| E1c productivity/labor/operator/measure | Economic/equation authority | Owner O2/O8/O9/O11 decisions `13348e5…`; P3/P4 `daa3e60…` | accepted | structural and common-object numerical parity | reflected-productivity redesign bounded; labor-curvature semantics accepted; forward operator is mapped `G.T`; finite-state mass distinguished from density/cell measure | native MATLAB productivity and measure are not literal production-Python objects | no after common-object adapters | PASS |
| E1d illiquid-return law | Economic/equation authority | dependency closure `d46dac0…`; taper authority report `3335a1b…`; dissertation `(3-26)` | accepted and closed | equation authority | `mu_a=r_a*a+d`; MATLAB `raah=rah*(1-0.1*(a/amax)^9)` is upper-grid numerical stabilization, not economic structure | MATLAB full-HJB is numerically non-comparable on this feature | no | PASS |
| E2 Python source/test continuity | Source identity | baseline `7a2388a2ba89073e307f05a909570e8c40a4be13`; live Git diff | accepted | byte/path continuity | current `src/tests` diff is empty | none | no | PASS |
| E3 P1 primitive parity | Shared-input primitives | `CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY_REPORT.md`, commit `1b26e9c…` | `PASS` | exact/near common primitives plus authorized counterexample | all `4 a × 3 b × 4 z × 3 v_b × 3 q = 432` cases entered; materially common cases passed frozen criteria; 144 nonzero-transfer low-`a` legacy counterexamples explicitly exposed and validated against accepted `max(a,a_bar)` equation | bare-`a` legacy FOC is intentionally non-common below `a_bar`; taper was not a P1 primitive | no; both are now explicitly scoped | PASS |
| E4 P2 local policy/HJB/KKT parity | Local policy/HJB | corrected P2 completion report, commit `565c656…` | `MATLAB_PYTHON_TWO_ASSET_HA_P2_NUMERICAL_PARITY_PASS` | ten frozen local/control cases | `10/10`; common cases match; redesign cases cover lower `a`, lower `b`, interior zero drift, upper/corner closure and F/Z near tie; all feasible, zero-drift within `1e-12`, KKT below `1e-7` | MATLAB does not expose candidate/KKT audit for redesign-only cases | no; accepted equation tests supply authority | PASS |
| E5 P3 generator parity | Common generator | P3/P4 report, commit `daa3e60…` | `MATLAB_PYTHON_TWO_ASSET_HA_P3_GENERATOR_PARITY_PASS` | mapped common operator | `G_a`, `G_b`, `G_z` mapped max difference `0`; destinations/rates/diagonals exact; total recomposition error `5.55111512312578e-17`; row/off-diagonal/orientation gates pass | common frozen generator, not native endogenous legacy full HJB | no | PASS |
| E6 P4 qualified stationary parity | Common-operator KFE | P3/P4 report `daa3e60…` | `MATLAB_PYTHON_TWO_ASSET_HA_P4_KFE_STATIONARY_PARITY_PASS` | same frozen mathematical stationary object | mapped mass max difference `1.9359513991901167e-15 <= 1e-10`; forward-transpose error `0`; residuals about `1.13e-16`; normalization errors at/below `1.11e-16`; no negative mass; `A_hh` difference `1.28e-15`; `B_hh` difference `2.89e-14` | does not validate legacy pinned full-HJB distribution | no; P4 intentionally tests the qualified common operator | PASS |
| E7 integrated Python finite-grid R4 | Production integrated steady state | corrected-contract R4 report `8931eac…`; independent acceptance/prep `252c7fd…` | `R4_PYTHON_STEADY_STATE_ACCEPTED_FOR_PARITY_REVIEW` | independent integrated validation | primary/buffer HJB residuals `8.365e-10`/`8.373e-10`; KKT `9.088e-15`/`9.423e-15`; generator row sum `2.665e-15`; one closed recurrent class size `225`, all three `a` layers; left nullity `1`; KFE residual `3.886e-16`; normalization error `4.441e-16`; min mass `1.411e-17`, negative count `0`; mass-density error `3.331e-16`; canonical/direction mismatch counts `0` | no `a_max` mass-share statistic and no wider/higher `a` grid; 25/29 changes productivity only | no for current finite-grid P5; yes as future tail assurance before dynamics/calibration claims | PASS with frozen future-scope annotation |
| E8a legacy MATLAB stationary limitation | Full-HJB structural audit | structural-decomposition report, commit `3175c21…` | `MATLAB_STATIONARY_OPERATOR_BOUNDARY_NONUNIQUENESS_SUPPORTED__P5_BLOCKED` as predecessor route status | static structural proof plus reused accepted artifacts | production bare-`a` FOC makes `a=0` layer exactly closed; solver pins arbitrary row, does not check recurrent classes, left nullity, original `A'` residual or pin sensitivity; `convergent=true` certifies HJB iteration only | exact native recurrent decomposition/pin sensitivity not executed | no; sufficient to disqualify the vector as unquestioned oracle | PASS as accepted legacy limitation |
| E8b dependency/helper closure | MATLAB-to-Python functional coverage | dependency audit, commit `d46dac0…` | accepted closure | complete direct/transitive static audit | direct `lab_solve2`, `HANK3_FOC`, `HANK3_cost`, `HANK_gini`; transitive `Gini_coef2`; no duplicates/path ambiguity; `lab_solve2` functionally inlined by labor FOC/zero-drift construction; Gini is post-solve; foreign/fixed-cost/price logic, `alphap`, `VafF/VafB`, `Raf` inactive | no hidden helper omission remains in domestic HA core | no | PASS |
| E8c taper non-comparability | MATLAB numerical scope | taper authority report `3335a1b…` | accepted | authority/scope annotation | constant `r_a` is the economic law; taper is not to be inherited | upper-asset tail robustness not explicitly measured | no for current P5 | PASS |
| E9 same-input full-HJB history | Missing integration experiment | rate-matched report `47c2794…`; subsequent qualification/redesign and structural reports `691f214…`, `61f75d8…`, `03a3d1f…`, `3175c21…` | factual blocked history, not parity FAIL | attempted four-run route | first/only MATLAB `rah=.040` returned `convergent=false`; raw persisted; Python `.040`, MATLAB `.041`, Python `.041` each ran `0`; later work identified persistent legacy stationary degeneracy | no valid four-row aggregate object exists | no; absence is non-authoritative missing evidence, not adverse Python evidence | PASS for revised-design scope |

### E7 scope boundary: current correctness versus future tail robustness

R4's primary grid is `(3,3,25)` and its buffer grid `(3,3,29)`. Both use identical `a=[0,.5,1]` and `b=[0,2.5,5]`; only `z` extends from 25 nodes ending at `2.0` to 29 nodes ending at `2.25`. Consequently, accepted common-core changes of roughly `1e-9` establish productivity-upper-buffer robustness only. They are not an upper-asset-grid buffer test.

Current finite-grid Python correctness is supported by upper-`a` KKT/state constraints, bidirectional endogenous illiquid connectivity (`134` upward, `4` downward edges), one recurrent class spanning all illiquid layers, left nullity one, and valid stationary mass. Missing `a_max` mass-share and wider-`a` robustness remain future pre-dynamics/calibration assurance items under the accepted classification:

`UPPER_A_NUMERICAL_STABILIZATION_NOT_EXPLICITLY_EVIDENCED_BUT_NONBLOCKING_FOR_CURRENT_P5`

No new upper-`a` run is required or authorized for this P5 review.

## Revised P5 acceptance conditions

| # | Condition | Disposition | Evidence rationale |
|---|---|---|---|
| 1 | Economic identity/equation authority closed | `PASS` | O1–O12, dependency closure, dissertation `(3-26)`, and taper resolution close the last active helper/equation question; accepted law is `mu_a=r_a*a+d`. |
| 2 | Python `src/tests` scientifically unchanged | `PASS` | Empty live diff from `7a2388…`. |
| 3 | P1 materially comparable primitives pass; exceptions bounded | `PASS` | 432/432 reviewed; 144 low-`a` legacy counterexamples explicitly authorized, not hidden. |
| 4 | P2 local policy/HJB/KKT objects pass | `PASS` | 10/10 frozen cases; feasibility and KKT gates pass. |
| 5 | P3 complete common-generator parity | `PASS` | All components and total generator pass mapped exact/near tests. |
| 6 | P4 common-operator stationary/KFE parity | `PASS` | Mass, transpose, residual, normalization, nonnegativity and aggregates pass. |
| 7 | Integrated Python R4 passes full diagnostics | `PASS` | HJB/KKT/generator/connectivity/recurrent-class/left-nullity/KFE/mass and productivity-buffer contract pass; future asset-tail scope is nonblocking. |
| 8 | No material unexplained mismatch on a valid common object | `PASS` | Every executed materially common P1–P4 object passed; R4 is independently qualified. |
| 9 | Remaining non-comparabilities belong to accepted redesign/legacy set | `PASS` | Low-`a` FOC, productivity design, initializer, MATLAB pinning, taper and post-processing boundaries are explicitly classified; helper closure finds no hidden HA-core omission. |
| 10 | Failed full-HJB route is non-authoritative missing evidence | `PASS` | No valid common MATLAB object and no four-row comparison existed; failure occurred before Python execution and cannot be adverse Python evidence. |
| 11 | No production source mutation manufactured parity | `PASS` | Source continuity is exact; adapters/harnesses were external and bounded by their tasks. |
| 12 | Owner explicitly reviews and accepts revised package | `OWNER_DECISION_PENDING` | Cannot be self-issued by Codex or inferred from this review. |

Conditions 1–11 are fully supported. No remaining material evidence gap concerning current Python HA correctness was identified.

## Why the legacy pinned stationary vector is not required

The legacy vector lacks the qualifications required of an oracle: the production lower layer is structurally closed; arbitrary row replacement can select a normalized solution without proving uniqueness; and no recurrent-class, left-nullity, original-equation residual, or pin-sensitivity check is produced. MATLAB `convergent=true` concerns value iteration only. In addition, its low-`a` FOC and illiquid-return taper are outside the accepted common economic object.

This does not discard MATLAB evidence. MATLAB remains authoritative for historical source interpretation and valid modular comparisons. P3/P4 already establish generator and stationary parity on a qualified common mathematical object, while Python R4 independently validates the integrated production object. Requiring the legacy pinned vector would therefore substitute an unqualified, non-common numerical construction for stronger accepted evidence.

## Optional MATLAB stationary-uniqueness gate

`OPTIONAL_NONBLOCKING_FORENSIC_EXTENSION`

A future read-only graph/nullity/pin-sensitivity analysis could document the exact native recurrent decomposition and be academically informative. It is not required to judge Python correctness and would not change the revised P5 decision logic. It was neither created nor executed here.

## Remaining evidence gaps

- Material gaps for current P5 conditions 1–11: none.
- Pending governance/scientific authority: Owner condition 12 only.
- Future nonblocking assurance: explicit mass at `a_max` and wider/higher illiquid-asset-grid robustness before dynamics/calibration extension claims.
- Optional forensic knowledge: exact legacy MATLAB recurrent-class/nullity/pin-sensitivity decomposition.

Neither future item is converted into a current PASS claim, nor treated as a blocker to presenting the evidence package to the Owner.

## Files and forbidden-operation check

Read: both live P5 task files; `AGENTS.md`; both required project rules; every original required evidence report; the dependency-closure report; the taper-authority report; and accepted Python source/tests only for continuity/evidence verification.

Written: only `docs/CH5_TWO_ASSET_HANK_P5_ACCEPTANCE_DESIGN_REVISION_AND_EVIDENCE_SUFFICIENCY_REVIEW_REPORT.md`.

Git status at report freeze: the sole worktree change was this new authorized report; there were no modified source/test files and no unrelated tracked or untracked changes. Final remote identity and clean status are to be verified by post-publication read-back.

- MATLAB calls: `0`
- Python/model/HJB/KFE/steady-state calls: `0`
- P1–P4/R4/native/common-fixture reruns: `0`
- new upper-`a` diagnostic: `0`
- source/test/helper/cache modifications: `0`
- new adapter or taper implementation: `0`
- equation/parameter/grid/tolerance changes: `0`
- deferred/revised P5 final acceptance marker issued: no
- dynamics/AR(1)/transition/IRF/calibration-extension/Results work: `0`

## Acceptance level and exact next gate

Acceptance level: revised P5 design and evidence package are ready to be presented to the Owner. P5 itself remains undecided; dynamic extension remains unauthorized.

Exact recommended next gate: a **pure Owner final P5 acceptance decision** applying the frozen 12-condition standard to this report and its accepted evidence package. It must not include additional scientific execution and must be the only gate permitted to decide whether to issue `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`.
