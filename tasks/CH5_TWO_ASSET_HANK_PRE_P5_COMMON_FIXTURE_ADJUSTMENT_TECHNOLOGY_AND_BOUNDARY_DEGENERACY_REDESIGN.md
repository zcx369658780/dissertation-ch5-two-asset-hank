# CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_ADJUSTMENT_TECHNOLOGY_AND_BOUNDARY_DEGENERACY_REDESIGN

Date: 2026-08-29

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Issuer role: ChatGPT L3 independent reviewer / scientific route authority / GitHub task issuer

Executor role: Codex bounded Builder / executor

Owner: final scientific authority

## 1. Task purpose

Diagnose the repeated joint lower-bound collapse of the synthetic MATLAB common fixture, pivot from free-form synthetic tuning to a native-anchored common-supported household fixture, and determine whether at least one MATLAB-qualified common object exists using only parameters/economic fields that the accepted Python production household model can represent plus the already accepted O1/O2 adapters.

This task is still pre-P5 diagnostic/design work.

It is not the final four-run MATLAB-Python parity experiment.

P5 remains blocked throughout this task.

## 2. Live authority and accepted predecessor state

GitHub `main` is the sole repository-state authority.

Task-authoring parent observed before publication:

`61f75d84fdab06e2696a9af7db99b4235c89a10c`

Do not assume that SHA remains live when execution starts.

Before local work:

1. fresh-fetch `origin/main`;
2. confirm this exact task exists on live `main`;
3. record live start SHA;
4. read required governance/evidence files;
5. verify accepted Python scientific/test continuity.

Accepted Python scientific baseline:

`7a2388a2ba89073e307f05a909570e8c40a4be13`

Required check:

`git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`

It must be empty. Otherwise stop before any scientific run.

Accepted predecessor terminal state:

`COMMON_FIXTURE_MATLAB_REQUALIFICATION_EXHAUSTED_NEEDS_REDESIGN__P5_BLOCKED`

Predecessor report:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_LABOR_CURVATURE_MAPPING_CORRECTION_AND_MATLAB_REQUALIFICATION_REPORT.md`

The three exhausted candidates must not be rerun.

## 3. Required reads

Read at minimum:

- `AGENTS.md`
- `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
- `project_rules/PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
- `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_AFTER_PRE_P5_SAME_INPUT_CONVERGENCE_BLOCK_2026_08_29.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_PARAMETER_REDESIGN_AND_MATLAB_CONVERGENCE_QUALIFICATION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_LABOR_CURVATURE_MAPPING_CORRECTION_AND_MATLAB_REQUALIFICATION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_CONTROLLED_HOUSEHOLD_CL_RA_PERTURBATION_PERSISTENCE_CORRECTION_AND_REEXECUTION_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_PRE_P5_MATLAB_HOUSEHOLD_CALL_SNAPSHOT_AUTHORITY_PREP_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_OWNER_PARITY_REVIEW_AND_HELPER_SOURCE_AUDIT_REPORT.md`
- `docs/CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P3_P4_GENERATOR_KFE_NUMERICAL_PARITY_REPORT.md`
- accepted Python `src/ch5_two_asset_hank/contracts.py`
- accepted Python `src/ch5_two_asset_hank/economics.py`
- the accepted original MATLAB HJB/cost/FOC/labor helper and minimum caller/config source needed for the audits below.

P1-P4 remain accepted and must not be rerun.

## 4. Protected identities and adapters

Re-verify:

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

MATLAB original tree remains read-only. Diagnostic-patch/cache material is read-only evidence only.

## 5. Reviewer scientific interpretation to test

The exhausted evidence materially changes the diagnostic priority.

The previous three candidates all produced:

- `convergent=false`;
- `MATLAB:nearlySingularMatrix`;
- essentially zero mass away from the lower illiquid bound;
- essentially zero mass away from the lower liquid bound;
- Candidate 3 `B_hh=-2`, exactly the restored liquid borrowing limit.

Therefore simply raising `rah`, correcting labor curvature, widening `a`, adding a borrowing region, and increasing the synthetic grid to 242 states were not sufficient.

At the same time, accepted persisted native-snapshot evidence already shows that the accepted original MATLAB HJB can converge at `rah=0.040` and `0.041` with non-collapsed assets under the C2016-P10 native household environment.

The next task must therefore test a stronger hypothesis:

> the synthetic common fixture removed or normalized multiple household environment fields jointly, and the MATLAB legacy HJB may require a more native-like combination to retain asset-state mobility / a unique non-degenerate stationary object.

Do not reduce this to `rah` alone.

## 6. Critical representability boundary

The accepted Python production household contract must be treated as authoritative for what is currently a true common object.

Fresh-read and record the exact fields in Python `EconomicParams` and `HouseholdInputs` and the exact liquid drift in `asset_drifts`.

Reviewer evidence to verify from accepted source:

- Python production directly represents `rho`, `gamma_c`, `phi`, `chi_0`, `chi_1`, `a_bar`, `r_a`, `r_b`, `tau`, wages, migration costs and labor weights;
- Python production does **not** currently expose a household transfer-income field equivalent to MATLAB `Tt`;
- Python production does **not** currently expose a negative-liquid-asset borrowing spread equivalent to MATLAB `rb_gap`;
- Python adjustment cost has no nonzero fixed-cost term; the selected native reference already has `fixcost=fixcost2=0`, so zero fixed costs are common and not a blocker.

Consequently, a candidate may count as a `COMMON_SUPPORTED_CANDIDATE` only if MATLAB uses:

- `Tt=0`;
- `rb_gap=0`;
- `fixcost=0`;
- `fixcost2=0`;

unless a future Owner task changes Python production scientific scope.

Do not invent a test-only Python `Tt` or `rb_gap` adapter in this task.

## 7. Phase A — source/boundary audit before any run

### A1. MATLAB semantics

Fresh-read accepted original MATLAB source and document exactly:

1. how `rb_gap` enters liquid income/drift and whether it applies only when `b<0` or under another condition;
2. how `Tt` enters liquid income/drift;
3. how `rb`, `rah`, wage, tax and labor income enter the HJB budget;
4. how `chi0`, `chi1`, `a_bar` affect transfer control and adjustment cost under the accepted O1 helper;
5. whether any additional nonzero native household field not represented in accepted Python production enters the HJB scientific equations;
6. whether `results` input fields other than the explicitly frozen economic fields affect scientific policy equations versus initialization/display only.

If a material scientific MATLAB field absent from Python production is found beyond `Tt/rb_gap` and zero fixed-cost terms, record it and stop before Phase B unless the candidates below explicitly set it to a scientifically neutral/common value supported by source authority.

### A2. Native reference re-audit

Use the already accepted read-only C2016-P10 cache provenance and record exact native values for:

- `ga`, `rho`, `alphal`, `phi_l`, `frisch_l`;
- `chi0`, `chi1`, `a_bar`, fixed costs;
- `rb`, saved `rah`, `w`, `tau`, `Tt`, `rb_gap`;
- exact `a` and `b` node arrays, not only bounds/counts;
- two-state productivity values and transition parameters used by accepted original MATLAB;
- saved convergence state.

Do not execute the diagnostic-patch HJB.

### A3. Common-support matrix

Produce a table with one row per native MATLAB household field and columns:

- MATLAB meaning/source line;
- native value;
- Python production equivalent;
- exact semantic mapping;
- `COMMON_SUPPORTED / NOT_CURRENTLY_REPRESENTABLE / ZERO_NEUTRAL / INITIALIZATION_ONLY / DISPLAY_ONLY`;
- candidate treatment in this task.

This table is mandatory because the next decision depends on whether a valid common object can exist without adding a third adapter or changing Python production.

### A4. Pre-register all Phase B and Phase C objects before first HJB call

Create one fresh local no-overwrite manifest containing:

- all common candidates A/B/C;
- both non-common diagnostic witnesses W1/W2;
- exact run order;
- exact total and per-object call budgets;
- qualification rules;
- witness interpretation rules;
- source/helper identities;
- future parity companion rates where applicable;
- explicit statement that W1/W2 can never themselves qualify as common fixtures.

Hash and read back the manifest before the first scientific call.

No object may be edited after the first scientific call begins.

## 8. Phase B — exactly three COMMON_SUPPORTED candidates

All common candidates keep:

- common productivity values `z=[0.8,1.3]`;
- common productivity generator `Q_z_common=[[-0.4,0.4],[0.3,-0.3]]` under the already accepted common-Q protocol;
- `gamma_c/ga=2`;
- labor weight / `alphal=1`;
- Python `phi=5` mapped to MATLAB `frisch_l=0.2` except where an exhausted predecessor object is explicitly reused only as a starting definition;
- `Tt=0`;
- `rb_gap=0`;
- `fixcost=fixcost2=0`;
- accepted O1 helper;
- no Python scientific execution.

### Candidate A — adjustment-technology isolation from exhausted C3

Start from exhausted corrected Candidate 3 and change only the adjustment tuple to the audited native values:

- `chi0: 0.05 -> 0.1`
- `chi1: 1.0 -> 2.0`
- `a_bar: 0.5 -> 1e-6`

Keep:

- `rho=0.05`
- `rb=0.03`
- qualification `rah=0.055`
- future unexecuted companion `rah=0.056`
- `w=1`
- `tau=0`
- corrected labor mapping `phi=5`, MATLAB `frisch_l=0.2`
- Candidate-3 11x11 grids:
  - `a=[0,1,2,3,4,5,6,7,8,9,10]`
  - `b=[-2,-1.3,-0.6,0.1,0.8,1.5,2.2,2.9,3.6,4.3,5]`

Purpose: isolate whether the adjustment technology alone repairs the exhausted wide-grid object.

### Candidate B — native-anchored common-supported household object

Construct the closest common-supported object to accepted C2016-P10 using only fields present in accepted Python production and zeroing unsupported MATLAB-only wedges.

Use exact audited C2016-P10 values for every common-supported household field, including:

- `rho=0.05`
- `ga/gamma_c=2`
- Python `phi=5`, MATLAB `frisch_l=0.2`
- labor weight / `alphal=1`
- `chi0=0.1`
- `chi1=2`
- `a_bar=1e-6`
- `rb=0.02`
- qualification `rah=0.040`
- future unexecuted companion `rah=0.041`
- `w=13.084227346448168`
- `tau=0.05`
- `Tt=0`
- `rb_gap=0`
- `fixcost=fixcost2=0`
- exact audited native 20-node `a` grid on `[0,10]`
- exact audited native 20-node `b` grid on `[-2,5]`
- common `z/Q` above rather than an unreviewed native productivity object.

Before freezing B, prove the exact 20x20x2 grids and scalar/vector inputs are statically representable by accepted Python production contracts without running Python HJB/KFE.

Purpose: maximize proximity to a known-convergent native MATLAB household environment while remaining a true common-supported object.

### Candidate C — native-anchored common-supported object at interior `rah`

Candidate C is exactly Candidate B except:

- qualification `rah=0.055`;
- future unexecuted companion `rah=0.056`.

Purpose: test whether the common-supported native anchor requires moving the illiquid return into the Owner's historically used interior range after Candidate B tests the known native neighborhood.

### Phase B run order and budget

Run exactly:

1. A;
2. B only if A fails qualification;
3. C only if A and B fail qualification.

Each entered candidate gets at most one accepted-original MATLAB HJB call.

Maximum common-candidate HJB calls: 3.

Stop at the first qualified common candidate.

Do not run Python or any companion rate.

## 9. Common-candidate qualification rules

A/B/C is `COMMON_FIXTURE_QUALIFIED` only if all are true:

1. accepted original MATLAB HJB returns `convergent=true`;
2. all exposed arrays and stationary mass are finite;
3. stationary mass sum is within `1e-10` of 1;
4. minimum mass is at least `-1e-12`;
5. no singular/nearly-singular stationary warning is emitted;
6. mass with `a>a_min` is at least `1e-4`;
7. mass with `b>b_min` is at least `1e-4`;
8. required exposed aggregates are finite;
9. source/helper/harness/manifest identities remain frozen.

Persist for each entered candidate the same convergence, warning/RCOND, mass, non-collapse and aggregate diagnostics used by the predecessor qualification tasks.

If one common candidate passes, stop the task immediately after persistence/read-back and recommend a separate final same-input four-run parity gate. Do not enter Phase C witnesses.

## 10. Phase C — non-common diagnostic witnesses only if all A/B/C fail

Phase C exists only to determine whether currently unsupported MATLAB wedges are material to the boundary degeneracy.

W1/W2 are **not common fixtures**, must never be called parity evidence, and cannot authorize P5.

They are allowed only if A, B and C all fail.

Before W1, Phase A source audit must have confirmed the semantics of `rb_gap` and `Tt`.

### Witness W1 — borrowing-spread witness

Start from Candidate B and change only:

- MATLAB `rb_gap: 0 -> 0.07`.

Keep `Tt=0`.

This witness is intentionally not representable in accepted Python production.

Purpose: test whether the native borrowing spread alone prevents complete liquid-lower-bound collapse / stationary degeneracy.

### Witness W2 — borrowing-spread plus transfer witness

Run W2 only if W1 does not return a fully valid non-degenerate MATLAB solve.

Start from W1 and change only:

- MATLAB `Tt: 0 -> 0.1`.

Purpose: test whether the combination of the native borrowing spread and native transfer-income term restores the known non-degenerate household object when all other common-supported fields are native-anchored.

### Witness budget

Maximum W1 calls: 1.

Maximum W2 calls: 1.

Maximum Phase C calls: 2.

Do not rerun a witness.

Use the same convergence, warning and non-collapse diagnostics as Phase B, but classify outcomes only as diagnostic witness evidence.

## 11. Frozen interpretation matrix

If A qualifies:

- adjustment-technology mismatch is sufficient to repair the exhausted wide synthetic object under the bounded qualification test;
- freeze A for the next separate parity task.

If A fails but B qualifies:

- adjustment technology alone was insufficient;
- the native-supported joint household environment is sufficient;
- do not claim which B subcomponent is individually causal;
- freeze B.

If A/B fail but C qualifies:

- native-supported environment plus the higher illiquid return is sufficient;
- freeze C;
- do not infer `rah` alone is causal.

If A/B/C all fail and W1 qualifies/non-degenerately converges:

- record strong evidence that MATLAB's negative-b borrowing spread is material to the legacy solver's non-degenerate stationary object;
- because accepted Python production lacks this field, classify the current O1/O2-only true-common-fixture route as `BLOCKED_BY_ECONOMIC_OBJECT_REPRESENTABILITY` pending Owner scientific decision.

If W1 fails and W2 qualifies/non-degenerately converges:

- record strong evidence that unsupported native liquid-income wedges jointly matter;
- classify the O1/O2-only true-common-fixture route as `BLOCKED_BY_ECONOMIC_OBJECT_REPRESENTABILITY` pending Owner decision.

If A/B/C/W1/W2 all fail:

- do not tune further;
- classify `COMMON_FIXTURE_NATIVE_ANCHOR_STILL_DEGENERATE_NEEDS_STRUCTURAL_DIAGNOSTIC`;
- recommended next gate must examine the remaining full-integration differences such as accepted O1 low-a behavior, common-Q/full-HJB interaction, initialization/result-field dependence, or other source-audited mechanisms without mutating production code.

## 12. Explicitly forbidden

Do not:

- modify accepted Python `src/` or `tests/`;
- modify MATLAB production source;
- modify diagnostic-patch caches;
- add a third adapter;
- implement Python `Tt` or `rb_gap`;
- run Python HJB/KFE/steady state;
- rerun any exhausted predecessor C1/C2/C3;
- rerun P1-P4;
- run any future companion rate;
- enter final four-run parity;
- change any pre-registered A/B/C/W1/W2 after first HJB call;
- widen tolerances;
- switch solver;
- run outer equilibrium, multi-province, transition, AR(1), IRF, calibration extension or Results work;
- infer P5 acceptance.

## 13. Persistence and report

Use a new timestamped no-overwrite external root.

Persist before moving to the next object:

- manifest and SHA-256;
- source/helper identities;
- static Python representability evidence for B/C;
- exact rate-matched initialization identity;
- attempt marker;
- raw returned MATLAB object immediately after return;
- summary JSON read-back;
- warning ID/message and RCOND if available;
- convergence flag;
- mass sum/minimum;
- mass above `a_min`;
- mass above `b_min`;
- `C_hh`, raw `H_hh` when derivable without a new adapter, effective `L_hh`, `A_hh`, `B_hh`;
- qualification/witness disposition.

Repository output:

`docs/CH5_TWO_ASSET_HANK_PRE_P5_COMMON_FIXTURE_ADJUSTMENT_TECHNOLOGY_AND_BOUNDARY_DEGENERACY_REDESIGN_REPORT.md`

Repository commit/push is authorized for this report only.

Do not commit raw MAT, JSON run artifacts, caches or binaries.

## 14. Terminal classifications

Use exactly one evidence-supported terminal classification, preferably one of:

- `COMMON_FIXTURE_ADJUSTMENT_TECHNOLOGY_QUALIFIED__FINAL_PARITY_NOT_RUN`
- `COMMON_FIXTURE_NATIVE_ANCHORED_COMMON_SUPPORTED_QUALIFIED__FINAL_PARITY_NOT_RUN`
- `COMMON_FIXTURE_NATIVE_ANCHORED_HIGHER_RA_QUALIFIED__FINAL_PARITY_NOT_RUN`
- `COMMON_FIXTURE_ROUTE_BLOCKED_BY_ECONOMIC_OBJECT_REPRESENTABILITY__P5_BLOCKED`
- `COMMON_FIXTURE_NATIVE_ANCHOR_STILL_DEGENERATE_NEEDS_STRUCTURAL_DIAGNOSTIC__P5_BLOCKED`
- `BLOCKED_PRE_SCIENTIFIC_SOURCE_OR_INTERFACE`

Do not issue the final P5 marker in this task.

## 15. Final response requirements

Report:

- terminal classification;
- live start and final `origin/main`;
- Python `src/tests` continuity;
- protected MATLAB/adapters identities;
- source-audited `Tt/rb_gap` semantics;
- common-support matrix;
- exact native reference values and grids;
- frozen A/B/C/W1/W2 manifest SHA;
- exact HJB call counts;
- full diagnostics for every entered common candidate and witness;
- first qualified common candidate if any;
- whether current Python production representability itself became the blocker;
- files read/written;
- external artifact identities;
- forbidden-operation check;
- git status;
- acceptance level;
- recommended next gate.
