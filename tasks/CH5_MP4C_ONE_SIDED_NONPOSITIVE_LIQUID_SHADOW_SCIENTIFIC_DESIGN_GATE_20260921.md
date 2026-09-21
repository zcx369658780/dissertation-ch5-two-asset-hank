# Task — one-sided / nonpositive liquid-shadow scientific design gate

Date: 2026-09-21

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_SCIENTIFIC_DESIGN_GATE_20260921`

Status: `ACTIVE`

Results eligibility: `FALSE`

## Roles and authority

Owner is final scientific authority. ChatGPT is L3 independent Reviewer / scientific-route authority. Codex is bounded Builder / scientific numerical analyst. GitHub live main is repository-state authority.

Absolutely do not enter, read, search, use or modify:

`zcx369658780/deep-learning-hank`.

## Owner authorization

The exact Owner decision is:

`OWNER_DECISION__AUTHORIZE_ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_EXTENSION_DESIGN_GATE__NO_IMPLEMENTATION_YET`

Read:

`docs/CH5_MP4C_TURN2_HEILONGJIANG_F0063_ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_DESIGN_GATE_OWNER_AUTHORIZATION_20260921.md`

This is a scientific design gate only. No new production law is adopted.

## Required reads

Fresh-fetch live main, then read in order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. Owner authorization above
6. `docs/CH5_MP4C_TURN2_HEILONGJIANG_F0063_NONPOSITIVE_BACKWARD_LIQUID_SHADOW_FORENSIC_ACCEPTANCE_20260921.md`
7. `docs/CH5_MP4C_2018_KFE_D123_INTERIOR_ZERO_LIQUID_Z_OWNER_ADOPTION_ACCEPTANCE_20260916.md`
8. `docs/CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_SWITCHING_OWNER_ADOPTION_20260919.md`
9. `docs/CH5_MP4C_2018_KFE_D123_SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_OWNER_ADOPTION_20260919.md`
10. `docs/CH5_MP4C_2018_KFE_D123_CORRECTED_DIAGNOSTIC_CONTRACT_IMPLEMENTATION_STATIC_VALIDATION_ACCEPTANCE_20260916.md`
11. `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_HJB_KFE_FIXED_POINT_DESIGN_BINDING_ACCEPTANCE_20260917.md`
12. current corrected selector / D1-D3 / derivative construction source, read-only
13. historical MATLAB-faithful derivative-floor source, read-only and non-authoritative
14. this exact task.

## Scientific objective

Determine whether a **generic** one-sided/nonpositive liquid-shadow switching law can be justified for corrected HJB iterations when exactly one raw liquid derivative/shadow is nonpositive and the other is positive.

The task must not assume that continuation is desirable or that F0063 must be rescued.

The central question is whether a zero-liquid switching shadow outside the positive part of the local one-sided derivative hull can be justified by the HJB/upwind/viscosity structure, rather than by outcome convenience.

## Exact anchor object

Use 黑龙江 F0063 as the anchor test object:

`reports/ch5_mp4c_lower_a_interior_z_composition_repair_turn1_parity_turn2_run004_20260921/household/p07_黑龙江/checkpoint_003/cell_0063.json`

Frozen values:

- `p_b^B=-0.0002428532863339202`
- `p_b^F=0.014463823441006161`
- `p_a^B=0.026049395991859955`
- `p_a^F=0.024439409021974706`
- current outcome: `NO_ADMISSIBLE_POLICY`
- accepted diagnostic-only positive-transfer / forward-a zero-liquid root:
  `q_b=0.01801822665826406`.

The diagnostic root is a test object only.

## Part A — local mathematical authority analysis

Derive explicitly:

1. consumption FOC domain `q_b>0`;
2. the local closed hull of the two raw liquid one-sided derivatives;
3. its positive-domain intersection when one endpoint is nonpositive;
4. the existing backward/forward upwind direction conditions;
5. the existing interior-Z interpretation as a derivative-selection/switching shadow;
6. branch-specific D3 transfer feasibility domains in q_b for fixed a-derivative branches;
7. why a D3/sign feasibility interval is or is not a legitimate liquid derivative-selection interval.

For F0063, evaluate all otherwise viable families over:

- the positive part of the raw derivative hull;
- any branch/KKT feasibility interval outside that hull.

Prove whether a zero-liquid root exists inside the positive derivative hull. If none exists, prove that every coherent continuation root requires extrapolation.

## Part B — viscosity/upwind interpretation

Give a scientific argument, not a coding argument, for whether a switching shadow may exceed the sole positive one-sided derivative when the opposite one-sided derivative is nonpositive.

Address explicitly:

- local super/subdifferential or derivative-hull interpretation used by the current Z law;
- monotonicity/upwind consistency;
- whether a nonpositive one-sided derivative during a transient HJB iterate should be treated as:
  - an unusable endpoint,
  - a signal of transient non-monotonicity,
  - a positive-domain boundary,
  - or evidence for a new extrapolative control law;
- whether extrapolating q_b beyond the positive derivative has a consistent viscosity-solution interpretation.

Do not claim a theorem that repository evidence does not support. Clearly separate mathematical derivation, numerical evidence and scientific judgment.

## Part C — persisted sign-pattern census

Perform zero-science read-only censuses from persisted evidence.

### C1. Accepted turn-1 compatibility authority

Using the 408 accepted turn-1 checkpoint maps, count interior-liquid cells by raw liquid derivative sign pattern:

- `(+,+)`
- ((<=0,+)`
- ((+,<=0)`
- ((<=0,<=0)`.

Report by province and checkpoint, and distinguish converged/final checkpoints where identifiable.

### C2. Fresh turn-2 run004 evidence through first failure

Using the 101 persisted run004 policy maps through 黑龙江 checkpoint3, perform the same census.

At minimum report:

- first occurrence of a nonpositive one-sided liquid derivative;
- whether such sign patterns occur in earlier provinces but disappear before convergence;
- whether F0063 is isolated or part of a broader transient pattern;
- magnitude distribution or bounded summary of the nonpositive derivatives;
- whether corresponding cells are interior or active liquid faces.

No selector calls, HJB calls or derivative recomputation are permitted; read persisted derivatives only.

## Part D — compare candidate scientific designs

Evaluate at least these distinct designs.

### Design 0 — preserve current two-positive-shadow law

No extension. One nonpositive derivative => no interior-Z candidate.

### Design 1 — positive derivative-hull restriction

Allow analysis only on the positive intersection of the local derivative hull:

`(0, max(p_b^B,p_b^F)]`

or the exact finite positive closed subset implied by the raw derivatives.

No extrapolation beyond the sole positive derivative.

Determine whether this creates any new candidate at F0063 or other persisted examples.

### Design 2 — branch-feasibility extrapolation

Permit q_b to move beyond the sole positive derivative up to a branch-specific D3/KKT/sign-feasibility boundary.

This is the family that can contain the F0063 diagnostic root.

It must not be accepted merely because it works. Derive:

- exact generic trigger;
- exact direction of extension;
- exact branch-specific interval construction;
- whether the interval is finite;
- uniqueness/fail-closed semantics;
- precedence relative to ordinary, liquid-Z, interior-a and joint laws;
- why this extrapolation would or would not remain an HJB/upwind derivative-selection law.

### Design 3 — historical derivative floor

Document only as a comparator.

Do not recommend or adopt it unless the scientific analysis independently concludes that reopening the full corrected derivative-domain authority is necessary. No implementation is allowed.

## Part E — cross-cell falsification panel

A proposed generic extension must be tested against persisted cells, not only F0063.

Construct a zero-science panel from all persisted one-nonpositive/one-positive interior-liquid cells found in Part C, subject to a practical bounded cap if the census is large.

For each sampled or complete panel cell:

- bind raw derivatives and state;
- independently evaluate the proposed trigger;
- reconstruct any proposed root with independent arithmetic only;
- evaluate existing D3/KKT/direction/domain conditions;
- classify whether the proposed law emits a candidate.

Persist the sampling rule if a cap is needed.

The design must identify pathological cases such as:

- no positive root;
- multiple roots;
- unbounded branch interval;
- root only after changing transfer branch;
- conflicting a-direction;
- candidate outside finite/KKT domain.

No production helper may be called.

## Required scientific outcome

End with exactly one of these design classifications.

### 1. Generic extension scientifically supported

`PASS__ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_DESIGN_GATE__GENERIC_EXTENSION_PROPOSAL_COMPLETE__OWNER_ADOPTION_REQUIRED__NO_IMPLEMENTATION`

This requires a complete proposed law with:

- exact trigger;
- exact q_b domain/bracket;
- treatment of the nonpositive endpoint;
- branch/transfer interaction;
- root uniqueness/fail-closed semantics;
- candidate reconstruction;
- precedence/deduplication;
- D2 representation;
- interaction with interior-a and joint switching;
- audit receipt contract;
- operation budget implication;
- compatibility/reexecution plan.

The report must explain why the law is not merely F0063-specific and why any extrapolation is scientifically justified.

### 2. Extension scientifically rejected

`PASS__ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_DESIGN_GATE__EXTENSION_NOT_SCIENTIFICALLY_JUSTIFIED__PRESERVE_CURRENT_FAIL_CLOSED_RECOMMENDED__NO_IMPLEMENTATION`

Use this if the analysis shows that any successful candidate requires derivative extrapolation without a defensible HJB/upwind/viscosity basis.

### 3. Bounded unresolved ambiguity

`BLOCKED__ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_DESIGN_GATE__SCIENTIFIC_AMBIGUITY_REQUIRES_OWNER_ADJUDICATION__NO_IMPLEMENTATION`

Use only if evidence supports more than one scientifically defensible generic law and the task cannot distinguish them.

## Zero-science boundary

Production/model science must remain zero:

- production selector calls: 0
- production root-helper calls: 0
- HJB/direct update: 0
- derivative recomputation from V: 0
- D2/Q: 0
- SCC/KFE/SVD: 0
- aggregate/integration: 0
- turn2 replay/rerun: 0
- turn3: 0
- MATLAB calls: 0
- GE/annual/shock/IRF/welfare/Results: 0
- retry/tuning: 0.

Permitted:

- persisted JSON/NPZ reads;
- source/authority reads;
- independent algebra and symbolic derivation;
- independently coded scalar equations/root diagnostics;
- high-precision/binary64 diagnostics;
- persisted derivative sign census;
- tests of the design validator.

## No implementation

Do not modify:

`src/ch5_two_asset_hank/**`

Do not modify accepted evidence.

Do not create a selector patch, even if the design supports one.

Do not rerun HJB or turn2.

Do not modify CURRENT files.

Do not publish a successor task.

## Allowed paths

Design validator:

`validators/multi_province/one_sided_nonpositive_liquid_shadow_scientific_design_gate/**`

Optional tests:

`tests/test_mp4c_one_sided_nonpositive_liquid_shadow_scientific_design_gate.py`

Fresh evidence:

`reports/ch5_mp4c_one_sided_nonpositive_liquid_shadow_scientific_design_gate_20260921_run001/`

Design report:

`docs/CH5_MP4C_ONE_SIDED_NONPOSITIVE_LIQUID_SHADOW_SCIENTIFIC_DESIGN_GATE_REPORT.md`

## Required evidence

Persist at minimum:

- authority/source binding;
- exact F0063 anchor binding;
- mathematical domain derivation;
- positive derivative-hull analysis;
- branch-feasibility interval derivation;
- viscosity/upwind interpretation memo;
- turn1 408-map derivative-sign census;
- turn2 run004 101-map derivative-sign census;
- cross-cell falsification panel;
- candidate-design comparison matrix;
- any proposed generic law, clearly marked proposal-only;
- operation-budget implication if applicable;
- future compatibility/reexecution plan if applicable;
- zero-science ledger;
- focused test receipt;
- sealed manifest and independent readback;
- final scientific classification.

## Git workflow

- isolated branch/worktree;
- explicit stage paths only;
- no force push;
- no main merge;
- no CURRENT edits;
- no successor publication.

Return terminal, classification, candidate SHA/tree, changed paths, sign-pattern census, core scientific derivation, cross-cell panel result, zero-science ledger, manifest/readback, and whether a separate Owner adoption is required.
