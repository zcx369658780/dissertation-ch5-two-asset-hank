# Task — corrected Option-B initial-turn 31-province household HJB-KFE and K1A/C1 one-turn integration

Date: 2026-09-20

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_31_PROVINCE_HOUSEHOLD_KFE_AND_K1A_C1_ONE_TURN_INTEGRATION_20260920`

Status: `COMPLETED_FAIL_ACCEPTED`

## Governance

Owner is final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

GitHub live main is repository-state authority.

Absolute prohibition:

`zcx369658780/deep-learning-hank`

must never be entered, read, searched, used or modified.

Fresh-fetch `origin/main` and read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1A_RAW_RA0_PAYOFF_OWNER_ADOPTION_20260920.md`
6. `docs/CH5_MP4C_K1A_RAW_RA0_PATH_B_TURN1_31_PROVINCE_FIXED_PRICE_ONE_STEP_CROSS_SECTION_ACCEPTANCE_20260920.md`
7. `docs/CH5_MP4C_2018_KFE_D123_CHECKPOINT11_TERMINAL_SOURCE_FREE_KFE_VALIDATION_ACCEPTANCE_20260920.md`
8. `docs/CH5_MP4C_2018_CORRECTED_HOUSEHOLD_FIXED_POINT_AGGREGATE_AND_ADAPTER_BINDING_ACCEPTANCE_20260920.md`
9. `docs/CH5_MP4C_K1A_2018_DISTANCE_SCORE_MAPPING_AND_STATIC_PORTFOLIO_DIAGNOSTIC_ACCEPTANCE.md`
10. `docs/CH5_MP4C_K1_BILATERAL_CAPITAL_NETWORK_REPAIR_AND_ENDOGENOUS_FOREIGN_SHARE_IMPLEMENTATION_ACCEPTANCE.md`
11. `docs/CH5_MP4C_C1_RESIDUAL_PUBLIC_ASSET_25TURN_CONTEMPORANEOUS_INTEGRATION_DIAGNOSTIC_ACCEPTANCE.md`
12. `reports/mp4c_c1_residual_public_asset_25turn_20260911/initialization_receipt_31province.csv`
13. `validators/multi_province/corrected_2018_single_turn/run.py`
14. current task.

No new economic law is authorized.

## Objective

Execute exactly one **initial corrected multi-province turn** under the already accepted scientific authorities.

The task has two scientific stages:

1. solve the corrected household fixed point independently for all 31 accepted initial province states, including terminal source-free KFE and stationary aggregates;
2. use the resulting 31-province household batch in exactly one K1A/C1/source-faithful-labor/firm integration turn, then construct the raw-`ra0` household payoff vector authorized for the next iteration.

Do **not** run the next household iteration.

This task is the first integrated corrected-household multi-province turn. It is not a steady-state trajectory.

## Exact initial-state authority

Use:

`reports/mp4c_c1_residual_public_asset_25turn_20260911/initialization_receipt_31province.csv`

Git blob at publication authority:

`5bb902183c8cb313d986ee5a9f8bd6b7c0624ae1`.

Require exactly 31 rows and exact active province order.

For each province, parse `outer_turn_1_initial_state_json` exactly. This accepted object is the entering outer-turn-1 state.

Do not silently substitute later K1A trajectory states.

The initial-state household fields are:

- `rah`
- `rb`
- `tau`
- `w`
- `Tt`
- `rb_gap`.

The entering `rah` is an initialization seed because there is no prior completed corrected turn. It is not evidence against the Owner-adopted raw-`ra0` law.

Do **not** replace entering turn-1 `rah` with the historical Path-B `turn=1 static_raw_S_transpose_ra0` vector. That object is completed-turn-1 / next-iteration payoff evidence only.

## Native numerical initialization authority

For each province, generate the initial value and baseline-labor arrays using the exact source-native constructor already preserved in:

`validators/multi_province/corrected_2018_single_turn/run.py`

publication Git blob:

`19ba32b0c5534f2726036ab8ba30fb204e359325`.

Use the existing `source_initial_arrays` law exactly with the province's entering state, accepted grid and accepted economic parameters.

This is numerical initialization only. It does not replace the corrected D1/D2/D3 HJB law.

Requirements:

- exactly one native initialization per reached province;
- exactly 800 scalar labor-root solutions per reached province;
- no initialization retry;
- no changing root tolerances or formulas;
- persist initial V/l hashes per province.

## Corrected HJB contract per province

Use the accepted corrected household science unchanged:

- grid `20 x 20 x 2`, F-order, b fastest;
- D1 finite-domain/boundary law;
- D2 consumed-total-drift conservative generator;
- D3 regularized adjustment/KKT law;
- lower-a zero-kink law;
- interior-liquid Z;
- interior-a switching;
- simultaneous two-axis switching;
- repaired active lower-b negative representation;
- state-dependent illiquid-return taper;
- `Delta=1000`.

HJB convergence remains:

`B <= 1e-8 AND D <= 1e-7`

at the same checkpoint.

Every direct solve must use only:

`scipy.sparse.linalg.spsolve`

with normwise backward error `<=1e-12`.

No damping, relaxation, adaptive Delta, clipping, artificial diffusion, continuation, solver substitution or post-hoc threshold tuning.

Cycle handling:

- exact-cycle law unchanged;
- authorized approximate period-2/3 law unchanged;
- approximate-cycle norm exactly `||vec_F(V_j-V_(j-k))||inf`;
- primary convergence evaluated before cycle classification.

Per-province bounded ceiling:

- maximum direct HJB updates: `50`;
- the initial policy/D2 map does not itself count as an update;
- stop that province if convergence has not occurred by the accepted checkpoint after update 50.

This ceiling is an experiment budget only, not a new convergence definition.

Execute provinces sequentially in `province_index=0..30` order.

Stop the whole task on the first province HJB failure/cycle/update-ceiling breach.

## Compact nonlinear evidence

Do not persist 800 verbose cell receipts for every checkpoint.

Builder may use transient per-cell receipts internally, but after each successful map it must compact them into deterministic reproducible artifacts and remove the verbose cells before continuing.

Persist per checkpoint at minimum:

- province/index
- checkpoint/update index
- V hash
- canonical policy identity
- selected-field hashes
- active constraints / transfer counts
- switching summary
- selector/root ledger
- Q CSR identity
- D2 receipt
- B
- D when defined
- direct-solve receipt when an update is taken
- cycle receipt when applicable.

On failure, retain the exact complete failing-cell receipt before stopping.

## Terminal KFE contract per converged province

After HJB convergence, validate the exact final same-value Q with the already accepted pin-free/source-free KFE contract.

For each reached converged province:

1. exact-positive directed graph;
2. exactly one SCC decomposition;
3. require exactly one closed communicating class;
4. set `A=Q.T`;
5. exactly one full dense
   `scipy.linalg.svd(A, full_matrices=True, lapack_driver="gesvd", check_finite=True)`;
6. frozen gamma-based rank threshold;
7. require rank/nullity `799/1`;
8. require structural closed-class count = numerical nullity;
9. use only the smallest right-singular vector;
10. one global sign orientation;
11. one total-mass normalization;
12. no clipping/abs/truncation/second normalization;
13. exactly one `Q.T@p`;
14. reuse the accepted stationarity, normalization and arithmetic nonnegativity bounds.

No row replacement, pin equation, source RHS, balancing source, iterative eigensolver or alternate SVD driver.

Stop the task on the first KFE failure.

## Household aggregates

For every province whose HJB and terminal KFE pass, use the accepted corrected aggregate semantics:

- Ct
- Lt
- At
- Bt
- total assets
- AtTax.

Use the accepted opt-in corrected aggregate adapter semantics only after terminal KFE PASS.

Build one exact 31-province `PreFrozenHouseholdOutputBatch` only if all 31 province household blocks pass.

## One-turn integration authority

Only after all 31 corrected household blocks pass may exactly one multi-province turn be executed.

Freeze:

- K1A geography benchmark `beta_distance=2`;
- K1B return-attractiveness feedback OFF: `beta_return=0`;
- fixed accepted `theta_i`;
- source-faithful labor route;
- K1 same-S quantity/payoff accounting;
- C1:
  `GovInv=max(Ktarget-Kprivate,0)`;
- no normalized-labor successor;
- no K2;
- no controller/adaptation iteration.

The existing K1A module publication blob is:

`ac309b4dbe9f6b3ca1d3cfc691223600835d17b6`.

The C1 integration source publication blob is:

`ba717dfdada1b47ee44af5562d3ffa01a9de8cfe`.

Do not modify default runtime routing. Implement this as an opt-in bounded integration driver.

## Raw payoff timing after the firm stage

At turn-1 entry, the accepted initialization `rah` is used.

After the corrected household batch, K1A quantity allocation, C1, source-faithful labor and firms are evaluated exactly once.

The firms produce a raw net-return vector `ra0_turn1`.

For the next household iteration, construct the Owner-adopted payoff using the same accepted K1A portfolio-share matrix `S`:

`rah_next_raw_by_origin = ra0_turn1_by_destination @ S_destination_origin`.

Requirements:

- use raw `ra0`, not clipped firm `ra`;
- no annualization/rescaling/smoothing/risk adjustment;
- do not z-score the payoff level;
- preserve same-S quantity/payoff orientation;
- K1B attractiveness remains OFF;
- persist the exact raw-ra0 vector, S identity and `rah_next_raw` vector.

This next-payoff vector is an output of the task.

Do not feed it into a turn-2 household solve.

## One-turn outputs and accounting gates

Persist and validate:

- all 31 corrected household fixed-point/KFE/aggregate results;
- household batch identity;
- source-faithful bilateral labor accounting;
- K1A portfolio-share matrix;
- private-capital origin and national conservation;
- home retained capital;
- C1 residual GovInv identity;
- firm K/Y/wage/raw-ra0/used-ra diagnostics;
- same-S raw next-payoff identity;
- next composite wage vector;
- next rb;
- exact next-state candidate fields needed by a future turn-2 task.

Do not run the historical adaptive GovInv/Zt controller after this one turn. C1 residual public assets are the only GovInv rule in scope.

## Scientific budget

Maximum:

### Initialization
- source-native province initializations: 31
- scalar labor roots: 24,800
- initialization retries: 0

### HJB
- direct HJB updates per province: 50
- total direct HJB updates: 1,550
- policy/D2 maps per province: 51
- total policy maps / D2 assemblies: 1,581
- selector evaluations: 1,264,800
- scientific retries: 0
- solver substitutions: 0

### Terminal KFE
- SCC decompositions: 31
- dense GESVD calls: 31
- normalized stationary candidates: 31
- Q.T@p calls: 31
- KFE retries: 0

### Aggregation/integration
- corrected aggregate evaluations: 31
- household batch constructions: 1
- source-faithful labor reconstruction: 1
- K1A capital-network allocation: 1
- C1 residual-GovInv construction: 1
- firm evaluations: 31
- composite-wage batch: 1
- monetary assignment: 1
- fiscal diagnostic batch: 1
- raw-next-payoff same-S construction: 1

### Forbidden
- turn-2 household calls: 0
- second outer turn: 0
- K1B feedback: 0
- K2: 0
- adaptive controller iteration: 0
- MATLAB scientific calls: 0
- GE/annual/shock/IRF/welfare/Results: 0
- payoff clipping/transformation as household payoff repair: 0.

## Stop conditions

Stop immediately on first:

- live authority/provenance mismatch;
- initial-state parse/order mismatch;
- source-native initialization nonfinite/root failure;
- selector failure;
- D2 failure;
- direct-solve warning/nonfinite/backward error breach;
- exact or approximate cycle;
- 50-update ceiling without HJB convergence;
- terminal KFE topology/rank/stationarity/normalization/nonnegativity failure;
- aggregate mismatch;
- household batch mismatch;
- labor/K1/C1 accounting failure;
- firm nonfinite failure;
- same-S raw next-payoff identity failure;
- code-freeze drift;
- scientific budget breach.

Do not rescue failures by changing payoff semantics, clipping raw payoff, widening tolerances, changing Delta, adding damping or switching solvers.

## Deliverables

Write:

`docs/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_31_PROVINCE_HOUSEHOLD_KFE_AND_K1A_C1_ONE_TURN_INTEGRATION_REPORT.md`.

Create one fresh compact evidence root under `reports/` containing:

- startup/authority binding
- 31-state initial-state receipt
- per-province native-initialization receipts
- compact HJB checkpoint histories
- terminal KFE receipts
- per-province stationary aggregate receipts
- 31-province household batch receipt
- one-turn labor/K1A/C1/firm/accounting receipts
- raw next-payoff same-S receipt
- next-state candidate receipt
- scientific ledger
- pre/post code freeze
- terminal receipt
- sealed manifest and independent readback.

Terminal PASS marker:

`PASS__CORRECTED_INITIAL_TURN_31_PROVINCE_HOUSEHOLD_HJB_KFE_AND_K1A_C1_INTEGRATION__RAW_NEXT_PAYOFF_READY__TURN2_NOT_RUN`.

A PASS means one corrected initial multi-province turn is internally closed and the exact raw-`ra0` next-payoff vector is ready for a separately authorized turn-2 task.

It does not establish outer fixed-point convergence, K1B, GE or Results.

Git workflow:

- isolated task branch
- ordinary non-force push
- remote SHA/tree readback
- clean worktree
- do not merge main
- do not modify CURRENT files
- do not publish successor.


## Reviewer closure — 2026-09-20

Run001 candidate `159786968d2bb47c12b0b7b88ed8aeaa6d0e8bdf` is accepted as failed evidence. The failure is a checkpoint-0 diagnostics-only caller defect: comparative policy/operator diagnostics were called with no previous checkpoint. No direct HJB update occurred, so no Beijing HJB/KFE scientific failure is inferred.

Acceptance: `docs/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_RUN001_ENGINEERING_EXCEPTION_ACCEPTANCE_20260920.md`.

Successor: `tasks/CH5_MP4C_CORRECTED_OPTIONB_INITIAL_TURN_CHECKPOINT0_DIAGNOSTIC_REPAIR_AND_REEXECUTION_20260920.md`.
