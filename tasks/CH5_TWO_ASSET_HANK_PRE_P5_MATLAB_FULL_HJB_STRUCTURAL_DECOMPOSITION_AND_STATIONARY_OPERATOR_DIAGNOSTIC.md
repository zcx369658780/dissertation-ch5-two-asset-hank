# CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_FULL_HJB_STRUCTURAL_DECOMPOSITION_AND_STATIONARY_OPERATOR_DIAGNOSTIC

Date: 2026-08-29

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Task purpose

Determine why the accepted original MATLAB full household HJB/KFE path becomes non-convergent and stationary-degenerate under every audited common fixture even though:

- accepted Python R4 solves its frozen two-asset object robustly;
- P1-P4 modular MATLAB-Python parity is already accepted;
- an accepted native MATLAB household snapshot/direct-call environment is known to converge;
- repeated common-fixture parameter, grid, labor-curvature, adjustment-technology, borrowing-spread and transfer-income redesigns did not restore a valid non-degenerate common MATLAB solve.

This task is **structural diagnosis**, not calibration search and not the final parity experiment.

It must be **read-only-first**. New MATLAB calls are allowed only under the bounded decomposition matrix in Phase B and only if Phase A does not already establish a decisive structural classification.

P5 remains blocked throughout this task.

## 2. Live authority and predecessor state

GitHub `main` is the sole repository-state authority.

Task-authoring parent observed before publication:

`03a3d1f9f40cae8103780f5576aa6b171291e6a3`

Do not assume this SHA remains live when execution starts.

Before local work:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main`;
3. record live start SHA;
4. read required governance/evidence files;
5. verify accepted Python `src/tests` remain unchanged from the accepted baseline.

Accepted Python scientific baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Required continuity check:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

It must be empty. If not, stop before Phase A classification.

Accepted predecessor terminal state:

`COMMON_FIXTURE_NATIVE_ANCHOR_STILL_DEGENERATE_NEEDS_STRUCTURAL_DIAGNOSTIC__P5_BLOCKED`

Predecessor report:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_ADJUSTMENT_TECHNOLOGY_AND_BOUNDARY_DEGENERACY_REDESIGN_REPORT.md`

The exhausted objects A/B/C/W1/W2 must not be rerun.

## 3. Required reads

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_AFTER_PRE_P5_SAME_INPUT_CONVERGENCE_BLOCK_2026_08_29.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_PARAMETER_REDESIGN_AND_MATLAB_CONVERGENCE_QUALIFICATION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_LABOR_CURVATURE_MAPPING_CORRECTION_AND_MATLAB_REQUALIFICATION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_ADJUSTMENT_TECHNOLOGY_AND_BOUNDARY_DEGENERACY_REDESIGN_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_HOUSEHOLD_CALL_SNAPSHOT_AUTHORITY_PREP_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_PERTURBATION_PERSISTENCE_CORRECTION_AND_REEXECUTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_PYTHON_BOOLEAN_SERIALIZATION_CORRECTION_AND_CL_RA_COMPLETION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`
- accepted Python source relevant to HJB, policies, boundaries, generator and KFE;
- accepted original MATLAB `HANK_2ASSETS_HJB.m`, `HANK3_cost.m`, production `HANK3_FOC.m`, `lab_solve2.m`, and the minimum caller/config source needed to trace every scientific input.

P1-P4 are accepted evidence and must not be rerun.

## 4. Protected identities

Re-verify before any diagnostic execution:

- `HANK_2ASSETS_HJB.m`
  - SHA-256 `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_cost.m`
  - SHA-256 `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- production `HANK3_FOC.m`
  - SHA-256 `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- `lab_solve2.m`
  - SHA-256 `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`
- accepted O1 test-only MATLAB FOC helper
  - SHA-256 `B28E73F439CB3DD40B2A6C00BE5D3E56FD7C4254DF468B4E2C0DCCED06DB7315`
- accepted O2 Python common-Q adapter
  - SHA-256 `D94848535E68C0CBF9BA51C91016E8DD91809221EEEA3F21DC4EE5D96EBE9225`

No third scientific adapter is authorized.

MATLAB original source tree remains read-only. Diagnostic-patch/cache trees remain read-only evidence only.

## 5. Evidence-based diagnostic priority

The predecessor evidence changes the route from parameter redesign to structural decomposition.

Facts already accepted:

1. The three earlier corrected synthetic candidates C1-C3 all failed with joint lower-bound collapse and near-singular stationary solves.
2. The native-anchored common-supported A/B/C objects also failed with joint lower-bound collapse.
3. Restoring the MATLAB-only borrowing spread in W1/W2 moved liquid mass away from `b_min`, but illiquid mass remained at `a_min`, `convergent=false` persisted, and the stationary solve remained nearly singular.
4. Restoring both `rb_gap` and `Tt` therefore did not recover a valid native-like solve.
5. Accepted persisted native/direct-call evidence exists in which the accepted original MATLAB HJB with the native household environment returns `convergent=true` at approximately `rah=0.040/0.041` and non-collapsed aggregate assets.
6. P3/P4 parity proves MATLAB/Python generator and stationary objects can match on externally frozen drifts/common-Q fixtures, but it does not prove the legacy MATLAB full HJB endogenously produces the same non-degenerate operator as accepted Python.

The remaining priority mechanisms are therefore:

- O1 low-`a` accepted-equation helper interacting with the legacy full HJB;
- common-Q/productivity substitution interacting with the full HJB;
- hidden initialization or `results`-input dependence not captured by prior field classification;
- endogenous stationary-generator boundary/recurrent-class structure of the legacy MATLAB HJB;
- interaction among the above.

Do not resume free-form parameter tuning.

## 6. Phase A — mandatory read-only structural forensic audit

No MATLAB or Python scientific model call is allowed until all Phase A deliverables are frozen.

### A1. Native-control versus failed-W2 exact differential inventory

Use accepted persisted evidence and source/cache reads to construct a field-by-field inventory comparing:

- the accepted known-convergent native/direct-call control tuple;
- predecessor W2, which restored native `rb_gap=0.07` and `Tt=0.1` but still failed.

Include every object that can affect the full HJB or stationary solve, not only economic scalars:

- source/helper identity;
- FOC helper path: production original versus O1;
- productivity state values and transition law/operator;
- all `param` fields read by HJB/helpers;
- all `grid` fields read by HJB;
- all `num` and `CHI` fields read by HJB/helpers;
- all `results` fields read anywhere in the HJB;
- value-function initialization inputs and formulas;
- prior aggregate fields;
- solver constants, iteration limit, pseudo-time step, `crit` and any hard-coded tolerances;
- state ordering and dimensions;
- stationary solve construction and row replacement/pinning.

For each difference classify:

- `SCIENTIFIC_EQUATION_DIFFERENCE`
- `PRODUCTIVITY_REPRESENTATION_DIFFERENCE`
- `INITIALIZATION_DIFFERENCE`
- `BOOKKEEPING_ONLY`
- `DISPLAY_ONLY`
- `NUMERICAL_CONTROL_DIFFERENCE`
- `IDENTICAL`

Do not assume prior reports exhausted the `results` dependence; prove every read from source.

### A2. Exact convergence-control flow

Document line-referenced control flow for:

- construction of initial value `v02` / starting value;
- HJB iteration matrix and RHS;
- policy/FOC selection;
- `convergent` flag assignment;
- whether the HJB loop exits by convergence, iteration exhaustion, or another condition;
- whether the stationary solve is executed even when `convergent=false`;
- exact location of `MATLAB:nearlySingularMatrix` relative to the convergence decision.

Explicitly separate:

`HJB_NONCONVERGENCE`

from

`STATIONARY_OPERATOR_SINGULARITY_OR_NONUNIQUENESS`.

The task must not infer one causes the other without source/evidence.

### A3. O1 low-asset structural audit

Compare production MATLAB FOC and accepted O1 helper at and near the illiquid lower bound.

For `a=0`, `0<a<a_bar`, and `a>=a_bar`, derive from source:

- transfer `d` under original FOC;
- transfer `d` under O1;
- implied illiquid drift `mu_a=rah*a+d`;
- whether each formulation can generate an upward edge from the `a=0` layer;
- whether the lower-`a` layer is structurally closed, nearly closed, or state/shadow dependent;
- how this changes when native `a_bar=1e-6` versus the earlier synthetic `a_bar=0.5`.

Compare this with the accepted Python lower-`a` KKT/state-constraint design and its already accepted one-recurrent-class R4 evidence.

This is an equation/operator audit, not an instruction to change MATLAB or Python.

### A4. Endogenous stationary-generator/recurrent-class audit

Read the accepted MATLAB generator assembly and stationary solve in detail.

Produce a row/block-level structural description for:

- `a` drift transitions at lower/interior/upper `a`;
- `b` drift transitions at lower/interior/upper `b`;
- productivity transitions;
- diagonal construction and row sums;
- transpose convention used for stationary mass;
- row replacement/pinning used to solve the singular stationary system;
- conditions under which multiple closed/recurrent classes can exist;
- whether one closed `a=0` class is enough to explain the observed lower-bound stationary solutions;
- whether the stationary pinning method can mask nonuniqueness by returning one normalized vector despite a near-singular warning.

Where possible, use persisted failed raw outputs and native saved outputs to classify graph implications without executing a model.

Do not create a new patched MATLAB source merely to expose the generator.

### A5. Common-Q/full-HJB audit

Document exactly how the accepted original MATLAB HJB constructs its productivity component and exactly how prior common-fixture harnesses supplied the common two-state object.

Determine whether the common-Q substitution changes only the intended productivity generator or also changes:

- initialization;
- state values used in labor income;
- transition intensities used in HJB iteration;
- ordering/reshape assumptions;
- any boundary logic.

Compare against accepted P3 common-Q generator evidence.

If the prior MATLAB common-Q construction is not a pure input-level/common-object substitution, classify this explicitly. Do not invent a new adapter.

### A6. `results` / initialization dependency audit

Enumerate every `results.<field>` read by the accepted original HJB and classify each as:

- `POLICY_EQUATION_ACTIVE`
- `INITIALIZATION_ACTIVE`
- `CONVERGENCE_ACTIVE`
- `STATIONARY_ACTIVE`
- `BOOKKEEPING_ONLY`
- `DISPLAY_ONLY`.

For every field classified active, record the exact native-control value and the exact W2/common value.

Determine whether the prior statement that `Ct/At/Bt/Lt` are bookkeeping-only is sufficient, or whether another saved `results` field materially changes the HJB start or iteration.

### A7. Freeze structural hypothesis matrix before any Phase B call

Create and hash a local text-first manifest/report fragment containing all candidate structural mechanisms with statuses:

- `SUPPORTED_SUFFICIENT`
- `SUPPORTED_PLAUSIBLE`
- `NOT_SUPPORTED`
- `UNRESOLVED_REQUIRES_REPLAY`

At minimum include:

- O1/full-HJB interaction;
- common-Q/full-HJB interaction;
- O1 + common-Q interaction;
- results/initialization dependence;
- stationary-generator lower-`a` closed-class/nonuniqueness;
- stationary row-pinning artifact;
- residual economic-field difference not previously audited.

If Phase A establishes a decisive source-level structural blocker sufficient to explain why a full MATLAB common HJB cannot serve as a clean P5 integration oracle, **stop without Phase B scientific calls** and report it.

## 7. Phase B — bounded native replay decomposition only if Phase A remains unresolved

Phase B is conditional. It is not a new common-fixture search.

Reuse the already accepted persisted native/direct-call control evidence as `R0_CONTROL_REUSED`; do not rerun R0.

The control is the previously accepted native C2016-P10 direct-call environment under the accepted original MATLAB source/production helper in which the household call is convergent.

Before the first Phase B call, freeze and hash the exact replay manifest and prove each replay differs from R0 only in the named structural dimension(s).

No replay may be modified after the first replay begins.

### R1 — O1 isolation

Use the exact native control tuple and native productivity representation.

Change only:

- production original `HANK3_FOC.m` -> accepted O1 helper.

Everything else must remain byte/value identical to the accepted control tuple, including exact native `results` input and initialization-relevant fields.

Purpose: test whether accepted O1 alone breaks legacy full-HJB convergence or induces the illiquid lower-bound degeneracy.

Maximum calls: 1.

If R1 fails while reused R0 is valid, classify:

`MATLAB_LEGACY_FULL_HJB_O1_INCOMPATIBILITY_SUPPORTED`

and do not infer that Python is wrong; O1 is the accepted equation redesign.

### R2 — common-Q isolation

Run only if source audit proves the previously accepted MATLAB common productivity object can be supplied through existing input/harness mechanisms without new source mutation or a third adapter.

Use the exact native control tuple and production original FOC.

Change only the productivity representation to the already frozen common object used in prior parity work.

Purpose: isolate common-Q/full-HJB interaction.

Maximum calls: 1.

If a pure isolation is impossible without changing another scientific field, do not run R2; classify `COMMON_Q_FULL_HJB_ISOLATION_NOT_PURELY_AVAILABLE`.

### R3 — O1 plus common-Q interaction

Run only if R1 and R2 do not already establish a sufficient blocker and if R2 was a pure allowed isolation.

Use exact native control tuple and change only:

- production FOC -> O1;
- native productivity -> accepted common productivity object.

Maximum calls: 1.

Purpose: identify an interaction that does not appear in either isolation alone.

### R4 — initialization/results normalization isolation

Run only if R1-R3 do not establish a sufficient blocker and Phase A identified an exact separable initialization/results transformation used by the failed common route.

Use production original FOC and native productivity.

Keep all economic parameters/grids identical to R0 and change only the exact pre-frozen initialization/results fields that distinguish the failed common route from native control.

Maximum calls: 1.

If the transformation cannot be made without changing multiple inseparable scientific dimensions, do not run R4 and report that fact.

### Phase B total budget

Maximum new MATLAB HJB calls: **4**.

Each replay: at most once.

No rerun.

Stop as soon as one mechanism is sufficient to explain the native-control/common-route divergence under the pre-frozen decision logic.

## 8. Diagnostics for every entered replay

Persist immediately after each returned HJB call and read back before any next replay:

- replay ID;
- exact diff from reused R0 control;
- source/helper identities;
- exact input tuple hash;
- initialization identity/hash if reconstructible without source mutation;
- `convergent`;
- warning ID/message and RCOND if exposed;
- all exposed arrays finite;
- stationary mass sum;
- minimum mass;
- mass with `a>a_min`;
- mass with `b>b_min`;
- `C_hh`, raw `H_hh` if derivable, effective `L_hh`, `A_hh`, `B_hh`;
- whether the outcome reproduces the native non-degenerate control or the failed common pattern.

These are diagnostic replay outputs only, not cross-language parity evidence.

## 9. Allowed outcomes and terminal classifications

The report must select the narrowest evidence-supported classification, for example:

- `MATLAB_LEGACY_FULL_HJB_O1_INCOMPATIBILITY_SUPPORTED__P5_BLOCKED`
- `MATLAB_COMMON_Q_FULL_HJB_INTERACTION_SUPPORTED__P5_BLOCKED`
- `MATLAB_O1_COMMON_Q_INTERACTION_SUPPORTED__P5_BLOCKED`
- `MATLAB_RESULTS_INITIALIZATION_DEPENDENCY_SUPPORTED__P5_BLOCKED`
- `MATLAB_STATIONARY_OPERATOR_BOUNDARY_NONUNIQUENESS_SUPPORTED__P5_BLOCKED`
- `MATLAB_FULL_HJB_STRUCTURAL_DIAGNOSTIC_UNRESOLVED__P5_BLOCKED`

Multiple mechanisms may be recorded, but one primary blocker must be named if evidence supports it.

A finding that the legacy MATLAB full-HJB integration is incompatible with an accepted redesign does **not** invalidate the accepted redesign or the Python implementation automatically. It means MATLAB full-HJB cannot be used as an unquestioned final integration oracle for that object.

## 10. Explicitly forbidden operations

Do not:

- modify accepted Python `src/` or `tests/`;
- modify MATLAB production source;
- modify canonical or diagnostic caches;
- add a third scientific adapter;
- create another parameter-search candidate;
- rerun exhausted C1/C2/C3 or A/B/C/W1/W2;
- rerun the accepted native R0 control;
- rerun P1-P4;
- run Python HJB/KFE/steady state;
- run companion perturbation rates for parity;
- run the final four-run MATLAB-Python parity sequence;
- change solver tolerances;
- widen acceptance tolerances;
- patch MATLAB merely to expose intermediate generator objects;
- execute outer equilibrium, multi-province, AR(1), transition, IRF, calibration extension, dynamics or Results;
- issue P5 acceptance.

## 11. Persistence and repository policy

Use a new timestamped external no-overwrite artifact root.

Repository writes are limited to:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_FULL_HJB_STRUCTURAL_DECOMPOSITION_AND_STATIONARY_OPERATOR_DIAGNOSTIC_REPORT.md`

Do not commit raw MAT files, local harnesses, logs, cache contents or binary outputs.

The report must include hashes/paths for external text-first manifests and any bounded replay artifacts.

Explicit stage paths only. Do not use `git add .` or `git add -A`.

Commit and push the single report only if all repository preconditions remain clean.

## 12. Final response requirements

Report:

- terminal classification;
- live start/final `origin/main`;
- accepted Python `src/tests` continuity;
- protected MATLAB/helper identities;
- exact native-control versus W2 differential matrix;
- convergence control-flow audit;
- O1 lower-asset structural derivation;
- stationary-generator/recurrent-class audit;
- common-Q/full-HJB audit;
- complete `results`/initialization dependency table;
- frozen Phase A structural hypothesis manifest hash;
- whether Phase B was needed;
- R0 reuse identity and exact R1-R4 run counts;
- complete diagnostics for every entered replay;
- primary blocker classification;
- whether legacy MATLAB full-HJB remains suitable as a final P5 integration oracle under accepted redesigns;
- files read/written;
- external artifact hashes;
- forbidden-operation check;
- git status;
- acceptance level;
- recommended next gate.

## 13. Next-gate logic

Do **not** publish or execute the next gate from within this task.

If a specific structural incompatibility is established, recommend an Owner/reviewer decision gate that revises the P5 acceptance design without silently changing accepted equations or production source.

If the diagnostic remains unresolved, recommend the smallest additional structural evidence gate. Do not return to parameter tuning.

P5 remains blocked until the Owner explicitly resolves the final acceptance standard.
