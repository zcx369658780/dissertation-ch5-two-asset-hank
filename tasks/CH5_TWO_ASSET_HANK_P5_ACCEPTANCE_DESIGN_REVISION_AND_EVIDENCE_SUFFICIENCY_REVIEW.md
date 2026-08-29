# CH5_TWO_ASSET_HANK_P5_ACCEPTANCE_DESIGN_REVISION_AND_EVIDENCE_SUFFICIENCY_REVIEW

Date: 2026-08-29

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / evidence reviewer

Owner: final scientific authority

## 1. Task purpose

Revise the Chapter 5 two-asset HA P5 acceptance design in light of the accepted finding that the legacy MATLAB full-HJB stationary object is not a qualified unquestioned integration oracle, and determine whether the already accepted evidence package is sufficient to place P5 before the Owner for an explicit final scientific decision.

This task is a **planning/evidence-sufficiency review only**.

It must not execute MATLAB or Python models.

It must not issue the final Owner acceptance marker.

P5 remains blocked until a later explicit Owner decision.

## 2. Live GitHub authority

GitHub `main` is the sole repository-state authority.

Task-authoring parent observed before publication:

`3175c21e8d2604aaf452b4fe07e5f659e83f60dc`

Do not assume that SHA remains live when execution starts.

Before any review work:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main`;
3. record live start SHA;
4. verify the predecessor structural-diagnostic report exists and is the current accepted evidence;
5. verify accepted Python scientific/test continuity.

Accepted Python scientific baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Required continuity check:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

It must be empty. If not, stop and report source drift.

## 3. Required reads

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_AFTER_PRE_P5_SAME_INPUT_CONVERGENCE_BLOCK_2026_08_29.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_SHARED_INPUT_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P2_PYTHON_HARNESS_API_ARITY_CORRECTION_AND_COMPLETION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_RERUN_AFTER_CORRECTED_TRUNCATION_CONTRACT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_R4_STEADY_STATE_ACCEPTANCE_AND_MATLAB_PYTHON_HA_PARITY_PREP_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_TRUE_SAME_INPUT_AGGREGATE_PARITY_GAMMA2_RATE_MATCHED_INITIALIZATION_EXECUTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_PARAMETER_REDESIGN_AND_MATLAB_CONVERGENCE_QUALIFICATION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_LABOR_CURVATURE_MAPPING_CORRECTION_AND_MATLAB_REQUALIFICATION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_ADJUSTMENT_TECHNOLOGY_AND_BOUNDARY_DEGENERACY_REDESIGN_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_FULL_HJB_STRUCTURAL_DECOMPOSITION_AND_STATIONARY_OPERATOR_DIAGNOSTIC_REPORT.md`
- accepted Python R4 source/tests only as needed to verify already reported integrated diagnostics; do not mutate them.

P1-P4 must not be rerun.

## 4. Accepted predecessor structural finding

Treat the following predecessor classification as accepted input evidence:

`MATLAB_STATIONARY_OPERATOR_BOUNDARY_NONUNIQUENESS_SUPPORTED__P5_BLOCKED`

The accepted structural report establishes at minimum:

1. production MATLAB transfer FOC scales the domestic control by bare `a`;
2. at `a=0`, production MATLAB therefore forces `d=0` and `mu_a=rah*a+d=0` identically;
3. the `a=0` layer is structurally closed under the production full-HJB operator;
4. the MATLAB stationary solve transposes the final generator, replaces one arbitrary row, solves the pinned linear system, and normalizes;
5. the accepted original MATLAB source does not check recurrent-class count, left nullity, residual of the unmodified stationary equation, or pin sensitivity;
6. `convergent=true` in the native MATLAB call certifies HJB value-iteration convergence only and does not certify uniqueness of the stationary distribution;
7. native positive `A_hh` together with an exactly closed `a=0` layer supports either additional recurrent structure or a pin-selected stationary vector that has not been uniqueness/residual-qualified;
8. the legacy MATLAB full-HJB stationary output is therefore not suitable as an unquestioned final P5 integration oracle under the accepted equation redesigns;
9. this does not invalidate O1/O2, accepted Python R4, or accepted P1-P4 evidence.

Do not reopen parameter tuning from this task.

## 5. Reviewer route decision to evaluate

The proposed revised P5 philosophy is:

> P5 should judge whether the accepted Python two-asset HA reconstruction is scientifically correct using equation authority, modular shared-input MATLAB-Python parity on every materially comparable object, and an independently qualified integrated Python steady state. It should not require literal equality to an unqualified legacy MATLAB full-HJB pinned stationary vector when the legacy stationary construction itself lacks uniqueness qualification and conflicts with accepted redesign boundaries.

This task must independently test whether that philosophy is evidence-sufficient.

Do not treat this paragraph as final Owner acceptance.

## 6. Mandatory evidence matrix

Create a complete P5 evidence matrix with one row per required claim/object and columns:

- evidence category;
- exact report/commit/source;
- accepted status;
- comparison type;
- numerical/structural result;
- unresolved limitation;
- whether the limitation is material to Python correctness;
- disposition for revised P5.

At minimum include the following categories.

### E1. Economic/equation authority

Verify accepted status for:

- two-asset state `(a,b,z)`;
- separate liquid/illiquid accounting;
- adjustment technology `m(a)=max(a,a_bar)`;
- lower-bound KKT/state-constraint redesign;
- reflected-productivity redesign and its accepted authority boundary;
- labor-curvature semantic mapping;
- generator/KFE transpose convention;
- finite-state mass/density convention.

### E2. Python source continuity

Verify:

- accepted scientific baseline `7a2388a2ba89073e307f05a909570e8c40a4be13`;
- no later `src/tests` scientific drift;
- no parity/diagnostic task modified production code merely to manufacture agreement.

### E3. P1 primitive parity

Record the accepted 432 shared-input primitive cases and the exact disposition of the low-`a` legacy counterexample.

P1 may satisfy revised P5 only if every materially comparable primitive passed its frozen criterion and every intentional non-comparability is already within the accepted redesign set.

### E4. P2 local policy/HJB parity

Record the accepted ten local policy/HJB cases, including redesign-specific controlled cases, boundary feasibility and KKT evidence.

### E5. P3 generator parity

Record mapped parity for:

- `G_a`;
- `G_b`;
- `G_z`;
- total `G`;
- row sums/off-diagonals/orientation.

### E6. P4 KFE/stationary parity on a qualified common operator

Record accepted parity for:

- stationary mass;
- normalization;
- stationarity residual;
- `A_hh/B_hh`;
- finite-state measure mapping.

Explicitly state that P4 tests the common mathematical stationary object produced from a frozen common generator; it does not rely on the legacy full-HJB pinned stationary vector as oracle.

### E7. Integrated Python R4 qualification

Record the accepted integrated Python steady-state diagnostics, including at minimum:

- HJB convergence/residual;
- KKT residual;
- generator row-sum/off-diagonal validity;
- recurrent-class count and coverage of illiquid layers;
- left nullity;
- KFE stationarity residual;
- mass normalization/nonnegativity;
- mass-density consistency;
- accepted truncation/buffer consistency.

This category is the full integrated validation of the Python production object.

### E8. Legacy MATLAB full-HJB limitation

Record the accepted structural finding that:

- production lower-`a` behavior structurally closes the `a=0` layer;
- the stationary solver uses arbitrary row pinning without uniqueness diagnostics;
- native `convergent=true` does not certify stationary uniqueness;
- the failed common-fixture route therefore cannot be interpreted as a Python parity failure.

### E9. Same-input full-HJB experiment history

Record factually:

- the attempted final same-input full-HJB route did not produce a valid four-row MATLAB/Python parity object;
- the blocker occurred in MATLAB qualification before Python execution;
- later parameter/native-anchor diagnostics established persistent legacy stationary degeneracy rather than a Python scientific failure;
- no valid same-input full-HJB aggregate mismatch was ever observed because the required valid MATLAB common object was never established.

Do not convert missing integration evidence into either a PASS or a FAIL by itself.

## 7. Revised P5 acceptance standard to freeze

The task must evaluate and, if supported, freeze the following revised acceptance standard for a later Owner decision.

A final Owner may issue:

`MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`

without a new full-HJB four-run MATLAB/Python integration experiment only if **all** conditions below are satisfied:

1. Economic identity/equation authority is closed with no unresolved implementation-critical conflict.
2. Accepted Python `src/tests` remain scientifically unchanged from the accepted baseline.
3. P1 passes all materially comparable primitive objects, with accepted redesign exceptions explicitly bounded.
4. P2 passes all defined local policy/HJB/KKT objects.
5. P3 passes complete common-generator parity.
6. P4 passes common-operator stationary/KFE parity.
7. The integrated Python R4 steady state passes HJB, KKT, generator, recurrent-class, left-nullity, KFE, mass and truncation diagnostics.
8. No material unexplained mismatch survives in any object that has a valid common mathematical definition.
9. Every remaining MATLAB-Python non-comparability is already within the accepted redesign/legacy-limitation set or is explicitly shown to arise from an unqualified legacy full-HJB stationary construction.
10. The failed same-input full-HJB route is classified as **non-authoritative missing evidence**, not adverse Python evidence.
11. No production source was mutated to manufacture parity.
12. The Owner explicitly reviews and accepts the evidence package under this revised standard.

The revised standard must **not** weaken any existing numerical tolerance for P1-P4 or Python R4.

It changes only the requirement that a legacy full-HJB pinned stationary vector must serve as the final integration oracle.

## 8. Decide whether a separate stationary-uniqueness evidence gate is required

Independently classify a possible additional MATLAB stationary-uniqueness evidence gate as exactly one of:

- `REQUIRED_FOR_REVISED_P5`
- `OPTIONAL_NONBLOCKING_FORENSIC_EXTENSION`
- `NOT_RECOMMENDED_NO_ADDITIONAL_DECISION_VALUE`

Use the following decision rule:

### Required

Choose `REQUIRED_FOR_REVISED_P5` only if the existing structural evidence is insufficient to establish that the legacy pinned stationary result is unqualified as an oracle, or if a specific unresolved MATLAB stationary fact is still necessary to judge Python correctness.

### Optional nonblocking

Choose `OPTIONAL_NONBLOCKING_FORENSIC_EXTENSION` if a graph/nullity/pin-sensitivity analysis would be academically informative but would not change the P5 decision because Python correctness is already independently tested by P1-P4 plus Python R4.

### Not recommended

Choose `NOT_RECOMMENDED_NO_ADDITIONAL_DECISION_VALUE` only if the extra gate would merely restate facts already sufficient and would consume effort without changing either acceptance logic or future model design.

If the gate is not `REQUIRED_FOR_REVISED_P5`, do not create or execute it in this task.

## 9. Evidence-sufficiency classification

Return exactly one terminal classification.

### Ready for Owner decision

`P5_REVISED_ACCEPTANCE_DESIGN_READY_FOR_OWNER_DECISION`

Use only if:

- every condition 1-11 in Section 7 is already evidenced as PASS/accepted;
- no unresolved material Python correctness question remains;
- the only missing element is Section 7 condition 12: explicit Owner acceptance.

### Additional evidence required

`P5_REVISED_ACCEPTANCE_DESIGN_NEEDS_ADDITIONAL_EVIDENCE__P5_BLOCKED`

Use if any material condition 1-11 is not yet supported.

Name the smallest missing evidence gate. Do not broaden scope.

### Contradiction found

`P5_REVISED_ACCEPTANCE_DESIGN_REJECTED_MATERIAL_CONTRADICTION__P5_BLOCKED`

Use if current accepted reports contain a material unresolved contradiction concerning Python scientific correctness.

## 10. Required final report

Write only:

`docs/CH5_TWO_ASSET_HANK_P5_ACCEPTANCE_DESIGN_REVISION_AND_EVIDENCE_SUFFICIENCY_REVIEW_REPORT.md`

The report must contain:

1. terminal classification;
2. live start/final GitHub identity;
3. source continuity result;
4. complete E1-E9 evidence matrix;
5. revised P5 acceptance standard with each condition 1-12 marked `PASS / OWNER_DECISION_PENDING / FAIL / NOT_APPLICABLE`;
6. exact explanation of why the legacy full-HJB pinned stationary vector is or is not required;
7. classification of the optional stationary-uniqueness gate;
8. explicit list of any remaining material evidence gaps;
9. forbidden-operation check;
10. acceptance level;
11. exact recommended next gate.

If classification is `P5_REVISED_ACCEPTANCE_DESIGN_READY_FOR_OWNER_DECISION`, the recommended next gate must be a **pure Owner final acceptance decision**, not another scientific execution task.

## 11. Explicit prohibitions

Do not:

- run MATLAB;
- run Python;
- rerun P1-P4;
- rerun R4;
- rerun native R0;
- rerun any exhausted common fixture;
- create a new parity fixture;
- tune parameters;
- modify production source/tests;
- modify MATLAB source/helpers/cache;
- add an adapter;
- widen any tolerance;
- change accepted equations;
- enter AR(1), transition, IRF, calibration extension, dynamics or Results;
- issue `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`;
- infer Owner acceptance from this reviewer task.

## 12. Acceptance boundary

This task may conclude only that the evidence package is or is not ready to be presented to the Owner under a revised P5 design.

It does not itself authorize dynamic extension.

The Owner remains the final scientific authority.