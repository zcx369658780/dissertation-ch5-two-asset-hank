# Task — corrected Option-B turn-2 household KFE and one-turn integration

Date: 2026-09-20

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_CORRECTED_OPTIONB_TURN2_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_20260920`

Status: `COMPLETED_FAIL_ACCEPTED`

## Governance

Owner is final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

GitHub live main is repository-state authority.

Absolute prohibition: never enter, read, search, use or modify `zcx369658780/deep-learning-hank`.

Fresh-fetch live main and read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_CORRECTED_INITIAL_TURN_FULL_CLOSURE_ACCEPTANCE_20260920.md`
6. `docs/CH5_MP4C_UNIQUE_CLOSED_CLASS_SUPPORT_KFE_OWNER_ADOPTION_20260920.md`
7. run004 household/KFE acceptance evidence
8. canonical integration replay evidence
9. all direct K1A/C1/raw-ra0 payoff authorities.

No new economic, HJB, KFE, boundary, KKT, calibration, solver, payoff, or timing law is authorized.

## Objective

Execute exactly one corrected outer turn 2.

The task starts from the accepted completed-turn-1 / entering-turn-2 31-province state.

It must:

1. solve the corrected household fixed point independently for all 31 turn-2 province states;
2. validate each with the Owner-adopted unique-closed-class terminal KFE;
3. construct 31 stationary aggregate blocks and one household batch;
4. execute exactly one turn-2 source-faithful labor / K1A / C1 / firm integration;
5. construct the canonical same-S raw-ra0 payoff vector for a possible future turn 3;
6. persist the exact turn-3 candidate state;
7. STOP before any turn-3 household solve.

This is a bounded second turn, not a trajectory or outer-convergence run.

## Exact turn-2 entering-state authority

Use exactly:

`reports/ch5_mp4c_run004_canonical_same_s_integration_replay_20260920_run001/next_state_candidate_receipt.json`

accepted Git blob:

`85df3f0bdcc3b0bb3e7b12f0ba35dbb9abda764d`.

Also bind the enclosing evidence manifest:

`79C6B15340AF641A736C79D0ED7C6450E39EA495263943280B6DDBD1B094F28D`.

Require:

- receipt status `PASS`;
- exactly 31 rows;
- exact active province order;
- each row classification:
  `TURN2_INPUT_CANDIDATE_ONLY__TURN2_NOT_RUN`;
- receipt raw-next-payoff SHA-256:
  `D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`.

For each province, use the exact persisted `state` object as entering turn 2.

In particular:

- entering `rah` is the accepted canonical completed-turn-1 raw-ra0 portfolio payoff;
- entering `w` is the accepted completed-turn-1 composite household wage;
- entering `rb` is the accepted completed-turn-1 monetary assignment;
- all other state fields are taken exactly from the persisted row.

Do not reconstruct these states from formulas or older trajectory artifacts.

## Turn-2 numerical initialization

For each province, use the same accepted source-native numerical initialization constructor used in turn 1:

`validators/multi_province/corrected_2018_single_turn/run.py::source_initial_arrays`.

This is numerical initialization only.

Requirements:

- exactly one source-native initialization per reached province;
- exactly 800 scalar labor roots per reached province;
- no warm-start from run004 terminal V unless separately authorized;
- no initialization retry;
- no formula/tolerance changes;
- persist turn-2 initial V/l identities.

## Corrected HJB contract

Unchanged:

- grid `20 x 20 x 2`, F-order, b fastest;
- accepted D1/D2/D3;
- accepted KKT/boundary/upwind/switching laws;
- lower-a zero-kink;
- interior-liquid Z;
- interior-a and joint switching;
- state-dependent illiquid-return taper;
- `Delta=1000`;
- convergence iff same checkpoint:
  `B<=1e-8 AND D<=1e-7`;
- only `scipy.sparse.linalg.spsolve`;
- normwise backward error `<=1e-12`;
- existing exact and approximate period-2/3 cycle law;
- maximum 50 direct HJB updates per province;
- no damping/relaxation/adaptive Delta/clipping/artificial diffusion/continuation/solver substitution/tolerance tuning.

Execute provinces sequentially in `province_index=0..30`.

First scientific failure stops the entire task.

## Owner-adopted terminal KFE

For every converged province use exactly:

`OWNER_ADOPTED__UNIQUE_CLOSED_CLASS_SUPPORT_KFE_AS_TERMINAL_KFE_AUTHORITY`.

Per province:

1. exact-positive topology;
2. exactly one SCC decomposition;
3. require exactly one closed communicating class C;
4. construct Q_CC;
5. require finite Q_CC, nonnegative offdiagonals, zero positive C->transient outflow, and row conservation within the accepted D2 arithmetic bound;
6. exactly one dense restricted GESVD on Q_CC.T;
7. evaluate both rank-threshold views:
   - local `gamma(|C|+64)`;
   - inherited `gamma(864)`;
8. require both to give rank/nullity `|C|-1 / 1`;
9. use only the smallest restricted right-singular vector;
10. one sign orientation;
11. one normalization on C;
12. require p_C strictly positive entrywise;
13. embed all transient mass as exact positive zero;
14. define g=p/OMEGA;
15. require full p/g finite and normalized;
16. exactly one original full-Q `Q.T@p`;
17. retain existing full-state stationarity/source-free arithmetic gates.

Forbidden:

- full-space 800x800 GESVD;
- KFE retry;
- clipping;
- old-p projection;
- tolerance relaxation;
- row pinning/replacement;
- source RHS;
- alternate/iterative solver.

## Turn-2 stationary aggregates

Only after that province's HJB and adopted KFE PASS may it produce:

- Ct
- Lt
- At
- Bt
- total assets
- AtTax.

Build one exact 31-province `PreFrozenHouseholdOutputBatch` only if all 31 turn-2 household blocks pass.

## Turn-2 integration

Only if all 31 household blocks pass, execute exactly one integration turn using the exact turn-2 entering states as `old_provinces`.

Freeze:

- source-faithful labor;
- K1A `beta_distance=2`;
- K1B OFF: `beta_return=0`;
- fixed accepted theta;
- same-S quantity/payoff accounting;
- C1:
  `GovInv=max(Ktarget-Kprivate,0)`;
- no normalized-labor successor;
- no K2;
- no adaptive controller.

Execute:

- household batch: 1
- source-faithful labor reconstruction: 1
- K1A: 1
- C1: 1
- firm evaluations: 31
- composite wage: 1
- monetary: 1
- fiscal: 1.

## Canonical turn-2 raw-next-payoff

After the turn-2 firm stage, firms produce `raw_ra0_turn2`.

Use the exact same K1A S from the turn-2 quantity allocation.

For each origin i compute the future turn-3 payoff exactly as:

`rah_turn3_i = math.fsum(float(raw_ra0_turn2[j]) * float(S_turn2[j,i]) for j in range(31))`

with destination j in ascending order `0..30`.

Persist:

- raw_ra0_turn2 vector identity;
- S_turn2 identity;
- ordered product-term identity;
- canonical turn-3 payoff identity;
- BLAS matrix-product comparison as diagnostic only;
- orientation `destination_by_origin`.

No clipping, annualization, rescaling, smoothing, risk adjustment or z-score.

Do not feed this payoff into a turn-3 household solve.

## Turn-to-turn diagnostics

Persist descriptive, non-gating movement from turn-2 entering state to the turn-3 candidate for at least:

- rah
- w
- rb
- Ct
- At
- Bt
- AtTax
- Kt
- Yt
- GovInv
- raw ra0.

For each field report cross-province:

- max absolute change;
- median absolute change;
- max relative change using an explicitly fixed denominator convention;
- province attaining max absolute change.

These diagnostics do not define outer convergence and must not be used to continue automatically beyond turn 2.

## Scientific budgets

### Initialization
- source-native initializations <=31
- labor roots <=24,800
- retries 0

### HJB
- policy/D2 maps <=1,581
- selector evaluations <=1,264,800
- direct HJB updates <=1,550
- max direct updates/province 50
- solver substitutions 0
- retries 0

### Terminal KFE
- SCC <=31
- restricted GESVD <=31
- normalized candidates <=31
- full-Q Q.T@p <=31
- full-space 800x800 GESVD =0
- retries 0

### Aggregation/integration
- aggregates <=31
- household batch <=1
- labor <=1
- K1A <=1
- C1 <=1
- firms <=31
- wage <=1
- monetary <=1
- fiscal <=1
- canonical raw-next-payoff <=1.

Forbidden:

- turn-3 household calls: 0
- third outer turn: 0
- K1B: 0
- K2: 0
- adaptive controller: 0
- MATLAB science: 0
- GE/annual/shock/IRF/welfare/Results: 0
- payoff transformations: 0.

## Stop conditions

Stop immediately on first:

- entering-state provenance/order mismatch;
- source-native initialization failure;
- selector/D2 failure;
- direct-solve warning/nonfinite/backward-error breach;
- exact/approx cycle;
- update-50 ceiling;
- topology not exactly one closed class;
- Q_CC structural failure;
- restricted rank/nullity failure under either threshold view;
- nonpositive p_C;
- full-Q stationarity/source-free failure;
- aggregate/batch mismatch;
- integration accounting failure;
- firm nonfinite/accounting failure;
- canonical same-S provenance/finite failure;
- code-freeze or budget failure.

No scientific rescue changes.

## Evidence

Create fresh evidence root:

`reports/ch5_mp4c_corrected_optionb_turn2_unique_closed_class_kfe_20260920_run001/`

Write:

`docs/CH5_MP4C_CORRECTED_OPTIONB_TURN2_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_REPORT.md`.

Persist at minimum:

- entering turn-2 authority binding;
- 31-state turn-2 receipt;
- code freeze;
- per-province initialization/HJB histories;
- per-province adopted KFE receipts;
- aggregates;
- household batch;
- turn-2 integration receipts;
- canonical turn-3 raw payoff receipt;
- turn-3 next-state candidate;
- turn-to-turn movement diagnostics;
- exact scientific ledger;
- historical lineage;
- terminal receipt;
- sealed manifest and independent readback.

## Terminal PASS marker

If all gates pass:

`PASS__CORRECTED_TURN2_31_PROVINCE_HOUSEHOLD_HJB_KFE_AND_ONE_TURN_INTEGRATION__RAW_TURN3_PAYOFF_READY__TURN3_NOT_RUN`

A PASS establishes exactly two completed corrected multi-province turns under the current authorities.

It does not establish outer fixed-point convergence, long-run stability, K1B, GE or Results.

## Git workflow

- isolated branch
- explicit staging only
- ordinary non-force push
- remote SHA/tree readback
- clean worktree
- do not modify CURRENT files
- do not merge main
- do not publish successor.


## Reviewer closure — 2026-09-20

Turn-2 candidate `37e563a87bf0dc1fb90224b03e0c4df9daea9d5f` is accepted as failed scientific evidence.

Terminal:
`FAIL__CORRECTED_HJB_POLICY_MAP_OR_D2_GATE`

The first failure is Beijing checkpoint 2, flat F-order index 579, selector outcome `NO_ADMISSIBLE_POLICY`. Checkpoint-2 D2/Q was not assembled; no KFE, aggregate, integration, or turn-3 execution occurred.

The failure is accepted under the current selector authority, but it does not yet prove that the continuous constrained problem has no feasible control because the active upper-b negative regime is rejected at a pre-root derivative-branch uniqueness gate.

Acceptance:
`docs/CH5_MP4C_TURN2_BEIJING_CHECKPOINT2_POLICY_SELECTOR_FAILURE_ACCEPTANCE_20260920.md`

Next active task:
`tasks/CH5_MP4C_TURN2_BEIJING_F0579_UPPER_B_NEGATIVE_BRANCH_ROOT_FORENSIC_20260920.md`
