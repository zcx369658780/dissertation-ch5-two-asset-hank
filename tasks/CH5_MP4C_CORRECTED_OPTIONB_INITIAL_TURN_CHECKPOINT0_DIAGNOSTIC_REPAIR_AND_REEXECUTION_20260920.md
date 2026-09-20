# Task — corrected Option-B initial-turn checkpoint-0 diagnostic repair and fresh reexecution

Date: 2026-09-20

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_CHECKPOINT0_DIAGNOSTIC_REPAIR_AND_REEXECUTION_20260920`

Status: `ACTIVE`

## Governance and authority

Owner is final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

GitHub live main is repository-state authority.

Absolute prohibition: never enter, read, search, use or modify `zcx369658780/deep-learning-hank`.

Fresh-fetch live main and read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_RUN001_ENGINEERING_EXCEPTION_ACCEPTANCE_20260920.md`
6. predecessor task `tasks/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_31_PROVINCE_HOUSEHOLD_KFE_AND_K1A_C1_ONE_TURN_INTEGRATION_20260920.md`
7. predecessor report and run001 evidence
8. all direct scientific authorities listed by the predecessor task.

No new economic or numerical law is authorized.

## Objective

Repair the confirmed checkpoint-0 diagnostics-only composition defect in the opt-in initial-turn driver, prove the repair before science, then perform exactly one fresh bounded execution of the predecessor scientific objective.

This successor does not continue from the partially executed Beijing run001 state. It starts a fresh run from the same accepted 31-province outer-turn-1 initialization authority.

## Exact engineering repair

Allowed scientific-driver change:

`src/ch5_two_asset_hank/corrected_diagnostic/optionb_initial_turn_integration.py`

and its focused regression test:

`tests/test_mp4c_corrected_optionb_initial_turn_integration.py`.

At checkpoint 0:

- do not call comparative `_policy_diagnostics` with `previous_rows=None` or `previous_arrays=None`;
- do not call comparative `_operator_diagnostics` with `previous_q=None`;
- emit deterministic current-only initial-checkpoint diagnostics;
- preserve current canonical policy identity, selected-field hashes, active-constraint counts, transfer-branch counts, switching summary, selector/root ledger, current Q CSR identity, Q nnz, D2 receipt and B;
- mark comparison-only fields to the nonexistent previous checkpoint as `None`/not-applicable rather than inventing a comparison;
- after checkpoint 0 produces the first direct update, checkpoint 1 and later must use the existing accepted comparative helpers unchanged.

The representational pattern should follow the already accepted initial-checkpoint handling in `nonlinear_continuation.py`: current object identities are real, while previous-checkpoint difference fields are unavailable at the first checkpoint.

Do not modify `nonlinear_continuation.py`, selector science, D1/D2/D3, KKT/boundary/upwind/switching rules, KFE math, aggregate semantics, K1A, C1, firm science, parameters, tolerances, `Delta`, solver or iteration ceilings.

## Zero-science pre-execution gate

Before any new source-native initialization, selector, root, D2/Q or HJB call:

1. add focused regression coverage for checkpoint-0 current-only diagnostic composition;
2. add coverage that checkpoint 1+ comparative diagnostic routing still requires real previous objects;
3. run focused tests, `py_compile`, and `git diff --check`;
4. verify exact accepted authority blobs and 31-row initialization order;
5. freeze the execution code hashes.

Engineering test retries before science are allowed. They do not authorize scientific calls.

If the zero-science gate fails, stop without model science.

## Scientific reexecution contract

After the repair passes the zero-science gate, execute one fresh run under exactly the predecessor scientific contract.

Use the same accepted initialization CSV/blob and the same `outer_turn_1_initial_state_json` values.

For provinces `0..30` in order:

- exactly one source-native V/l initialization per reached province;
- exactly 800 labor roots per reached province;
- corrected HJB under unchanged D1/D2/D3/KKT/boundary/upwind/switching law;
- fixed `Delta=1000`;
- convergence iff same checkpoint `B<=1e-8 AND D<=1e-7`;
- only `scipy.sparse.linalg.spsolve`;
- direct-solve normwise backward error `<=1e-12`;
- at most 50 direct HJB updates per province;
- unchanged exact/approximate period-2/3 cycle law;
- no damping, relaxation, adaptive Delta, clipping, artificial diffusion, continuation, solver substitution or tolerance tuning;
- first scientific failure stops the whole run.

For each converged province, execute the unchanged terminal source-free KFE contract exactly once:

- exact-positive graph;
- one SCC decomposition;
- exactly one closed communicating class;
- `A=Q.T`;
- one full dense `scipy.linalg.svd(..., lapack_driver="gesvd")`;
- rank/nullity `799/1`;
- closed-class count equals numerical nullity;
- smallest right-singular vector only;
- one sign orientation;
- one total-mass normalization;
- one `Q.T@p`;
- no pin, row replacement, source RHS, balancing source, clipping, abs, second normalization or alternate eigensolver/SVD.

Only after HJB+KFE PASS may that province's Ct/Lt/At/Bt/total-assets/AtTax be generated.

Only if all 31 household blocks pass may exactly one integrated turn run:

- one `PreFrozenHouseholdOutputBatch`;
- source-faithful labor;
- K1A `beta_distance=2`;
- `beta_return=0`;
- fixed accepted theta;
- K1 same-S accounting;
- C1 `GovInv=max(Ktarget-Kprivate,0)`;
- 31 firm evaluations;
- raw next payoff exactly `ra0_turn1_by_destination @ S_destination_origin`.

Do not run turn 2.

## Scientific budget for this successor run

Maximum for the fresh run:

### Initialization
- source-native province initializations: 31
- scalar labor roots: 24,800
- initialization retries: 0

### HJB
- direct HJB updates per province: 50
- total direct HJB updates: 1,550
- policy/D2 maps per province: 51
- total policy maps/D2 assemblies: 1,581
- selector evaluations: 1,264,800
- scientific retries: 0
- solver substitutions: 0

### Terminal KFE
- SCC decompositions: 31
- dense GESVD calls: 31
- normalized stationary candidates: 31
- `Q.T@p` calls: 31
- KFE retries: 0

### Integration
- aggregate evaluations: 31
- household batch constructions: 1
- source-faithful labor reconstruction: 1
- K1A allocation: 1
- C1 construction: 1
- firm evaluations: 31
- composite-wage batch: 1
- monetary assignment: 1
- fiscal batch: 1
- raw-next-payoff construction: 1

Forbidden remains:
- turn-2 household calls: 0
- second outer turn: 0
- K1B: 0
- K2: 0
- adaptive controller: 0
- MATLAB science: 0
- GE/annual/shock/IRF/welfare/Results: 0
- payoff clipping/rescaling/annualization/smoothing/risk adjustment/z-score repair: 0.

The predecessor run001 consumption remains historically recorded and is not reset or renamed. The counts above are the separately authorized ceiling for this successor's single fresh run.

## Evidence and deliverables

Use a fresh evidence root ending in:

`..._20260920_run002`

Do not overwrite run001.

Write:

`docs/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_CHECKPOINT0_DIAGNOSTIC_REPAIR_AND_REEXECUTION_REPORT.md`.

Persist:

- startup/authority binding;
- repair diff/diagnostic contract receipt;
- focused-test receipt;
- code freeze;
- 31-state initialization receipt;
- per-province native initialization;
- compact HJB histories;
- terminal KFE receipts;
- aggregates;
- household batch;
- one-turn labor/K1A/C1/firm/accounting;
- raw next-payoff same-S receipt;
- next-state candidate;
- exact successor scientific ledger;
- predecessor run001 cumulative-lineage receipt;
- terminal receipt;
- sealed manifest and independent readback.

If successful, terminal marker:

`PASS__CHECKPOINT0_DIAGNOSTIC_REPAIR__CORRECTED_INITIAL_TURN_31_PROVINCE_HOUSEHOLD_HJB_KFE_AND_K1A_C1_INTEGRATION__RAW_NEXT_PAYOFF_READY__TURN2_NOT_RUN`

This PASS means exactly one corrected initial multi-province turn is internally closed after the diagnostics-only repair. It does not establish outer fixed-point convergence, K1B, GE or Results.

## Git workflow

- isolated task branch
- ordinary non-force push
- explicit staging only
- remote SHA/tree readback
- clean worktree
- do not modify CURRENT files
- do not merge main
- do not publish successor.
