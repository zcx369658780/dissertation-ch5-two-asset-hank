# CH5_TWO_ASSET_HANK_P5_ACCEPTANCE_DESIGN_REVISION_AND_EVIDENCE_SUFFICIENCY_REVIEW_RESUMPTION_AFTER_TAPER_AUTHORITY

Date: 2026-08-29

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / evidence reviewer

Owner: final scientific authority

## 1. Purpose

Resume the previously deferred task:

`tasks/CH5_TWO_ASSET_HANK_P5_ACCEPTANCE_DESIGN_REVISION_AND_EVIDENCE_SUFFICIENCY_REVIEW.md`

The original task remains the controlling review specification except where this resumption authority adds newer accepted evidence or clarifies scope.

This is still a planning/evidence-sufficiency review only.

Do not run MATLAB or Python models.
Do not modify production source/tests.
Do not issue final P5 acceptance.

## 2. Resumption condition satisfied

The prior deferral was caused by an unresolved authority question over the MATLAB illiquid-return taper.

That question is now resolved by accepted report:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_ILLIQUID_RETURN_TAPER_AUTHORITY_RESOLUTION_AND_NUMERICAL_SCOPE_REVIEW_REPORT.md`

Accepted terminal classification:

`ILLIQUID_RETURN_TAPER_AUTHORITY_RESOLVED__P5_REVIEW_MAY_RESUME`

Accepted economic authority:

`ILLIQUID_RETURN_ECONOMIC_AUTHORITY_CONSTANT_RA__MATLAB_TAPER_NUMERICAL_STABILIZATION_NOT_TO_INHERIT_AS_ECONOMIC_EQUATION`

Accepted two-asset illiquid law:

`mu_a = r_a * a + d`

The dissertation equation authority and Owner clarification establish that the MATLAB state-dependent taper is an upper-grid numerical stabilization device, not a missing Python economic primitive.

Accepted numerical-scope classification:

`UPPER_A_NUMERICAL_STABILIZATION_NOT_EXPLICITLY_EVIDENCED_BUT_NONBLOCKING_FOR_CURRENT_P5`

Accepted P1-P4 impact:

`P1_P4_SCOPE_ANNOTATION_ONLY_NO_RERUN`

No implementation change and no new pre-P5 scientific execution are required by that authority resolution.

## 3. Live authority and continuity

Task-authoring parent observed by reviewer before this resumption publication:

`3335a1b869d3e60d8b30b626346f4d9ffc2bdcda`

At execution start:

1. fresh-fetch `origin/main`;
2. confirm both this resumption task and the original deferred P5 review task exist on live `main`;
3. record live start SHA;
4. verify the taper-authority report exists on live `main`;
5. verify accepted Python scientific/test continuity from baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Required check:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

must be empty.

## 4. Mandatory additional required reads

In addition to every required read in the original P5 review task, read:

- `docs/CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_HJB_DEPENDENCY_CLOSURE_AND_PYTHON_FUNCTIONAL_COVERAGE_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_ILLIQUID_RETURN_TAPER_AUTHORITY_RESOLUTION_AND_NUMERICAL_SCOPE_REVIEW_REPORT.md`

Treat both as accepted evidence.

## 5. Required evidence-matrix updates

Execute the complete E1-E9 evidence matrix from the original P5 review task, with these mandatory additions.

### E1 economic/equation authority

Explicitly include:

- dissertation equation `(3-26)` / accepted two-asset law `dot a = r_a a + d`;
- three-asset provenance around `(3-18)`-`(3-22)` only as historical notation/source mapping;
- classification of MATLAB `raah/Rah` taper as numerical stabilization, not economic structure;
- conclusion that Python constant `r_a` is aligned with accepted economic authority.

### E7 integrated Python R4

Distinguish what existing evidence proves from what it does not prove:

- upper-`a` KKT/state constraints, endogenous illiquid connectivity, one recurrent class, left nullity one and stationary validity are accepted;
- the 25/29 buffer test extends productivity support only;
- no accepted report directly measures mass share at `a_max` or wider-`a` tail robustness;
- this missing asset-tail robustness is accepted as nonblocking for current P5 but should remain a future pre-dynamics/calibration assurance item.

### E8 legacy MATLAB limitation

Add the completed dependency closure:

- all custom HJB dependencies are resolved;
- `lab_solve2` is scientifically active but functionally covered in Python;
- `HANK_gini/Gini_coef2` are post-processing only;
- foreign/fixed-cost/price branches plus `alphap`, `VafF/VafB`, `Raf` are inactive three-asset residues;
- there is no remaining hidden-helper omission in the current domestic two-asset HA core.

Also retain the accepted stationary-operator boundary/nonuniqueness limitation.

### E9 same-input full-HJB history

Annotate that the legacy MATLAB full-HJB route is non-comparable not only because of the unqualified pinned stationary construction and accepted lower-bound redesigns, but also because its `raah/Rah` taper is an implementation-level numerical stabilization not part of the accepted scalar-return economic equation.

Do not reinterpret this as adverse Python evidence.

## 6. Revised P5 conditions

Apply all 12 conditions from the original P5 review task unchanged.

For condition 1, equation authority may be marked PASS only if the dependency audit and taper-authority resolution close the last previously unresolved active-function/equation question.

For conditions 8-10, explicitly account for the taper scope annotation and MATLAB stationary limitation.

Condition 12 remains Owner decision only and may not be self-issued by Codex.

## 7. Extra MATLAB stationary-uniqueness gate

Use the exact three-way classification required by the original task:

- `REQUIRED_FOR_REVISED_P5`
- `OPTIONAL_NONBLOCKING_FORENSIC_EXTENSION`
- `NOT_RECOMMENDED_NO_ADDITIONAL_DECISION_VALUE`

The new taper authority resolution does not by itself require reopening MATLAB stationary execution.

## 8. Terminal classification

Return exactly one classification from the original P5 review task:

- `P5_REVISED_ACCEPTANCE_DESIGN_READY_FOR_OWNER_DECISION`
- `P5_REVISED_ACCEPTANCE_DESIGN_NEEDS_ADDITIONAL_EVIDENCE__P5_BLOCKED`
- `P5_REVISED_ACCEPTANCE_DESIGN_REJECTED_MATERIAL_CONTRADICTION__P5_BLOCKED`

If all conditions 1-11 are evidenced and the only missing item is condition 12, the correct classification is `P5_REVISED_ACCEPTANCE_DESIGN_READY_FOR_OWNER_DECISION`.

Do not issue `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION` in this task.

## 9. Output

Write only the report already specified by the original task:

`docs/CH5_TWO_ASSET_HANK_P5_ACCEPTANCE_DESIGN_REVISION_AND_EVIDENCE_SUFFICIENCY_REVIEW_REPORT.md`

The report must incorporate this resumption authority and both newly accepted reports into its evidence matrix and decision logic.

## 10. Explicit prohibitions

All prohibitions in the original P5 review task remain active.

Additionally do not:

- reopen the illiquid-return taper authority question;
- add the taper to Python;
- treat the productivity 25/29 buffer as an asset-grid tail test;
- create a new upper-`a` run in this task;
- reopen closed HJB dependency items without direct contradictory source evidence.

## 11. Recommended next gate

If terminal classification is `P5_REVISED_ACCEPTANCE_DESIGN_READY_FOR_OWNER_DECISION`, recommend only a pure Owner final P5 acceptance decision task.

If additional evidence is required, name only the smallest missing gate.

No dynamics, IRF, calibration extension, or Results work is authorized here.