# CH5_TWO_ASSET_HANK_PRE_P5_ILLIQUID_RETURN_TAPER_AUTHORITY_RESOLUTION_AND_NUMERICAL_SCOPE_REVIEW

Date: 2026-08-29

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / evidence reviewer

Owner: final scientific authority

## 1. Task purpose

Resolve the sole equation-authority gap identified by the completed MATLAB HJB dependency-closure audit: whether the Chapter 5 two-asset illiquid drift should treat the MATLAB state-dependent return taper as economic structure or as legacy numerical stabilization.

This task is **decision documentation + read-only evidence review only**.

It must not run MATLAB or Python models.
It must not modify production source/tests.
It must not add an adapter.
It must not issue P5 acceptance.

The previously published task

`tasks/CH5_TWO_ASSET_HANK_P5_ACCEPTANCE_DESIGN_REVISION_AND_EVIDENCE_SUFFICIENCY_REVIEW.md`

remains **DEFERRED_PENDING_THIS_AUTHORITY_RESOLUTION**.

## 2. Live authority and start checks

GitHub `main` is the sole repository-state authority.

Task-authoring parent observed by the reviewer:

`d46dac04fde07a73515a546f0736fec39a17c8be`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main`;
3. record live start SHA;
4. verify predecessor dependency-audit report exists;
5. verify accepted Python scientific/test continuity from baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Required check:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

must be empty.

## 3. Accepted predecessor audit

Treat the following report as accepted execution evidence:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_HJB_DEPENDENCY_CLOSURE_AND_PYTHON_FUNCTIONAL_COVERAGE_AUDIT_REPORT.md`

Its dependency closure established:

- direct custom dependencies: `lab_solve2`, `HANK3_FOC`, `HANK3_cost`, `HANK_gini`;
- transitive dependency: `HANK_gini -> Gini_coef2`;
- no same-name ambiguity or missing custom source in the designated MATLAB tree;
- `lab_solve2` is scientifically active but functionally covered in Python by the accepted labor FOC and certified zero-liquid-drift construction;
- `HANK_gini/Gini_coef2` are post-solve statistics only;
- foreign/fixed-cost/price branches plus `alphap`, `VafF/VafB`, `Raf` are inactive three-asset residues in the current domestic two-asset path;
- the only unresolved material item was the active MATLAB state-dependent illiquid-return schedule versus Python constant `r_a`.

Do not reopen already closed dependency items unless a direct contradiction is found.

## 4. Owner scientific clarification to formalize

The Owner has now explicitly clarified the provenance and intended meaning of the MATLAB taper.

Owner clarification:

1. The MATLAB expression

   `raah = rah .* (1 - 0.1*(ahmax./ah).^(-9))`

   was inherited from the Kaplan/Moll two-asset numerical implementation lineage.

2. Its purpose was **numerical stabilization near the upper illiquid-asset grid**: without the taper, household mass/policies can be driven toward the maximum illiquid-asset grid point and the numerical HJB/distribution iteration can become unstable or pile up at the upper boundary.

3. The taper was not intended by the Owner as a structural economic assumption that the domestic illiquid asset has a genuinely state-dependent return schedule.

4. The MATLAB naming `rah/raf` is inherited from the Owner's earlier three-asset codebase:
   - `b` = liquid asset with return `rb`;
   - `ah` = domestic illiquid/fixed asset with return `rah`;
   - `af` = foreign illiquid/fixed asset with return `raf`.
   The current two-asset reconstruction retains only liquid `b` and domestic illiquid `a` as scientific states.

This task must encode this Owner clarification into repository authority rather than treating it as informal chat context.

## 5. Dissertation economic authority

The authoritative dissertation equation must be treated separately from numerical implementation devices.

Read the designated dissertation source and verify the two-asset household budget/asset law in Chapter 3, especially equation `(3-26)` and the surrounding derivation.

Expected authority to verify:

`dot a = r_a * a + d`

with scalar illiquid return `r_a`, not a state-dependent taper.

Also verify the three-asset derivation around equations `(3-18)` through `(3-22)` uses structural laws of the form:

- `dot a_h = d_h + r_ah * a_h`;
- `dot a_f = d_f + r_af * a_f`.

The MATLAB taper may be cited as numerical implementation evidence, but it must not override the dissertation economic equation merely because it appears in code.

## 6. Frozen authority decision to test for consistency

Unless the read-only evidence reveals a direct contradiction, the reviewer/Owner decision for this gate is:

`ILLIQUID_RETURN_ECONOMIC_AUTHORITY_CONSTANT_RA__MATLAB_TAPER_NUMERICAL_STABILIZATION_NOT_TO_INHERIT_AS_ECONOMIC_EQUATION`

Meaning:

- accepted Chapter 5 economic law for the two-asset illiquid state is

  `mu_a = r_a * a + d`;

- Python production's constant-`r_a` drift is structurally aligned with the dissertation economic equation;
- MATLAB's

  `r_a_eff(a)=rah*(1-0.1*(a/amax)^9)`

  is classified as a legacy numerical upper-grid stabilization device, not as a missing Python economic primitive;
- no Python source change is authorized or required solely to reproduce this taper;
- the taper must not be added to Python merely to manufacture MATLAB agreement.

If authoritative dissertation text contradicts this decision, stop and report the contradiction instead of forcing the decision.

## 7. Numerical-stabilization scope review

Separately from economic equation authority, determine whether the **numerical problem addressed by the taper** is already covered by accepted Python diagnostics.

Read existing accepted Python R4 and truncation/boundary evidence without rerunning anything.

Audit at minimum:

- upper-`a` state-constraint/KKT handling;
- whether accepted R4 shows endogenous connectivity across illiquid layers rather than a closed upper layer;
- recurrent-class count and illiquid-layer coverage;
- left nullity;
- stationary mass validity;
- any existing upper-asset-boundary or buffer/truncation diagnostic;
- whether the accepted 25-vs-29 buffer protocol concerns productivity support only, asset support only, or both;
- whether existing evidence explicitly rules out material mass pile-up at `a_max`.

Do **not** claim that a productivity-buffer test is an asset-grid anti-pile-up test if it is not.

Classify the numerical-stabilization coverage as exactly one of:

- `UPPER_A_NUMERICAL_STABILIZATION_ALREADY_EVIDENCED_FOR_CURRENT_P5_SCOPE`
- `UPPER_A_NUMERICAL_STABILIZATION_NOT_EXPLICITLY_EVIDENCED_BUT_NONBLOCKING_FOR_CURRENT_P5`
- `UPPER_A_NUMERICAL_STABILIZATION_REQUIRES_BOUNDED_DIAGNOSTIC_BEFORE_P5`

Use the third classification only if current Python correctness cannot be judged safely without an explicit upper-`a` pile-up/truncation check.

If a future dynamic/calibration extension would need a stronger asset-grid tail diagnostic but current P5 does not, state that separately as a future gate recommendation rather than retroactively changing the economic equation.

## 8. P1-P4 scope impact

Determine whether the taper resolution changes accepted P1-P4 evidence.

Expected default if evidence is consistent:

- P1/P2 comparisons using scalar `r_a` remain on the accepted economic equation;
- P3/P4 remain valid because their drift/operator objects were frozen explicitly;
- the MATLAB tapered full-HJB route is not an economic-equation oracle for the scalar-return Python reconstruction;
- only a scope annotation is needed: MATLAB full-HJB taper is a numerical stabilization/non-comparability, not an adverse parity result.

Classify scope impact as exactly one of:

- `P1_P4_SCOPE_ANNOTATION_ONLY_NO_RERUN`
- `NEW_BOUNDED_PRIMITIVE_OR_BOUNDARY_TEST_REQUIRED`
- `MATERIAL_CONTRADICTION_REQUIRES_REOPENING_PARITY`

No rerun or new test is authorized in this task.

## 9. Required report

Write only:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_ILLIQUID_RETURN_TAPER_AUTHORITY_RESOLUTION_AND_NUMERICAL_SCOPE_REVIEW_REPORT.md`

The report must include:

1. terminal classification;
2. live start/final GitHub identity;
3. Python `src/tests` continuity;
4. exact Owner clarification recorded as repository authority;
5. dissertation equation evidence and exact equation references;
6. MATLAB taper formula and scientific/numerical classification;
7. final economic authority decision;
8. upper-`a` numerical-stabilization coverage classification;
9. exact audit of what existing R4/buffer/truncation evidence does and does not prove;
10. P1-P4 scope-impact classification;
11. whether any implementation change is needed;
12. whether any bounded additional diagnostic is needed before P5;
13. forbidden-operation check;
14. acceptance level;
15. exact recommended next gate.

## 10. Terminal classifications

Use exactly one.

### Authority resolved and P5 review may resume

`ILLIQUID_RETURN_TAPER_AUTHORITY_RESOLVED__P5_REVIEW_MAY_RESUME`

Use only if:

- dissertation authority supports constant `r_a`;
- Owner clarification is consistent with the source record;
- MATLAB taper is safely classified as numerical stabilization rather than missing economic structure;
- no additional pre-P5 scientific execution is required.

### Authority resolved but a narrow numerical diagnostic is still required

`ILLIQUID_RETURN_TAPER_AUTHORITY_RESOLVED__UPPER_A_DIAGNOSTIC_REQUIRED__P5_BLOCKED`

Use if the economic equation is resolved but current evidence is insufficient to rule out a material upper-`a` numerical pathology relevant to P5.

### Contradiction

`ILLIQUID_RETURN_TAPER_AUTHORITY_CONTRADICTION__P5_BLOCKED`

Use only if authoritative dissertation/source evidence contradicts the frozen Owner/reviewer decision.

## 11. Recommended next gate rule

If terminal classification is:

`ILLIQUID_RETURN_TAPER_AUTHORITY_RESOLVED__P5_REVIEW_MAY_RESUME`

then recommend resuming the deferred P5 acceptance-design/evidence-sufficiency review, after updating or superseding its required-read list to include this authority-resolution report.

If the terminal classification requires an upper-`a` diagnostic, recommend only the smallest bounded no-tuning diagnostic gate necessary to measure upper-bound mass/policy/truncation behavior.

Do not authorize dynamics or Results from this task.

## 12. Explicit prohibitions

Do not:

- run MATLAB;
- run Python;
- rerun P1-P4 or R4;
- modify Python `src/tests`;
- modify MATLAB source/helpers/cache;
- add the MATLAB taper to Python;
- delete the taper from MATLAB;
- add an adapter;
- change equations/tolerances/calibration;
- tune asset bounds;
- create a new common fixture;
- execute the deferred P5 review;
- issue P5 acceptance;
- enter AR(1), transition, IRF, dynamics, calibration extension or Results.

## 13. Acceptance boundary

This task resolves equation authority and numerical-scope classification only.

It may reopen the route to the deferred P5 evidence review, but it cannot itself authorize dynamic extension.