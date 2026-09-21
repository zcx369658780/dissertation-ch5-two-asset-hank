# Task — monotonicity-preserving HJB relaxation fresh turn-2 run005

Date: 2026-09-21

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_FRESH_TURN2_RUN005_20260921`

Status: `ACTIVE`

Results eligibility: `FALSE`

## Roles and authority

Owner is final scientific authority. ChatGPT is L3 independent Reviewer / scientific-route authority. Codex is bounded Builder / scientific numerical analyst. GitHub live main is repository-state authority.

Absolutely do not enter, read, search, use or modify:

`zcx369658780/deep-learning-hank`.

## Required reads

Fresh-fetch live main, then read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_OWNER_ADOPTION_20260921.md`
6. `docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTATION_AND_PERSISTED_REPLAY_ACCEPTANCE_20260921.md`
7. `docs/CH5_MP4C_TURN2_HEILONGJIANG_F0063_NEGATIVE_DERIVATIVE_EMERGENCE_FORENSIC_ACCEPTANCE_20260921.md`
8. current corrected HJB/turn2 source
9. this exact task.

## Purpose

Execute one fresh canonical turn-2 household/KFE run under the Owner-adopted and accepted monotonicity-preserving HJB relaxation law.

This task is the first fresh scientific runtime after adoption.

Do not replay turn1 compatibility: selector/D1/D2/D3 laws and turn1 authority are unchanged, and the new law acts only after accepted HJB direct solves.

## Fresh entering-state authority

Use exactly:

`reports/ch5_mp4c_run004_canonical_same_s_integration_replay_20260920_run001/next_state_candidate_receipt.json`

Required binding:

- Git blob:
  `85df3f0bdcc3b0bb3e7b12f0ba35dbb9abda764d`
- file SHA-256:
  `E519E468B04D7EDC631F6A931FF367A7EDE5C3D510ED4E0979AB2FC8E13C5E11`
- raw next-payoff SHA-256:
  `D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`
- row count: 31
- exact canonical province order.

No warm start from run004 household values is authorized.

## HJB initialization and province order

For each province:

- one source-native initialization;
- exact 20x20x2 grid;
- F-order;
- 800 source-native labor roots;
- fixed prices/state from the exact entering receipt;
- no warm start from another province/run;
- province order 0..30;
- stop globally at the first new scientific failure.

## HJB policy/operator law

Preserve all existing accepted authority:

- same raw derivative construction;
- same selector/D1/D2/D3;
- same root/switching laws;
- same full-map-before-D2 requirement;
- fixed Delta=1000;
- scipy.sparse.linalg.spsolve only;
- direct-solve backward error <=1e-12;
- Bellman B<=1e-8;
- value change D<=1e-7;
- existing exact/approximate cycle rules;
- at most 50 direct HJB updates per province in this turn2 route;
- no solver substitution;
- no adaptive Delta;
- no clipping/artificial diffusion;
- no scientific retry/tuning.

## Owner-adopted relaxation law

After every accepted full direct solve:

1. persist full Vhat and direct-solve receipt;
2. apply the implemented shared relaxation helper;
3. alpha schedule is exactly:
   `1, 1/2, ..., 2^-52`;
4. accepted nonlinear next state must have all 760 raw b-edge slopes finite and strictly >0;
5. accepted state must not be bitwise identical to old state;
6. exhaustion fails closed:
   `FAIL__MONOTONICITY_PRESERVING_HJB_RELAXATION_EXHAUSTED`.

No alternate schedule or fallback.

Each full direct solve plus alpha search counts as one HJB update.

Track separately:

- relaxation helper invocations;
- alpha candidates evaluated;
- number of relaxed updates with alpha<1;
- distribution/count of accepted halvings;
- minimum accepted raw b slope by province.

These arithmetic checks are not scientific retries.

## Required 黑龙江 runtime parity if reached

If canonical execution reaches 黑龙江 checkpoint2 under the same pre-relax trajectory, require runtime evidence without extra scientific calls that:

- checkpoint0->1 alpha=1;
- checkpoint1->2 alpha=1;
- checkpoint2 full direct candidate SHA-256:
  `1FA95217C9EEFDAA638F0CD07F00B59B053EB4A59E5670A0CED94852922DBFE7`;
- checkpoint2->3 accepted alpha=0.5;
- accepted relaxed state SHA-256:
  `987A20DE9252104ECFAB59436433F0C73EEB8C513589B8B0FA98DB64018B66BF`;
- minimum accepted raw b slope:
  `0.005032838660371801`.

If the earlier 黑龙江 trajectory differs before checkpoint2, do not force these hashes; persist the first divergence and continue only if the actual trajectory remains legal under current authority.

The prior F0063 fail object is not expected to remain the same after relaxation and must not be artificially reconstructed.

## Terminal KFE authority

For every converged province preserve the Owner-adopted unique-closed-class terminal KFE law:

- exact-positive topology;
- exactly one SCC decomposition;
- exactly one closed communicating class;
- restricted Q_CC;
- exactly one dense restricted GESVD on Q_CC.T;
- rank/nullity |C|-1 / 1 under both preregistered threshold views;
- smallest restricted right singular vector;
- one sign orientation;
- one normalization;
- p_C strictly positive;
- transient mass exactly zero;
- one full-Q Q.T@p check;
- source-free/stationarity/normalization gates;
- full-space 800x800 GESVD = 0;
- no retry.

## Integration if all 31 pass

Only if all 31 household HJB/KFE blocks pass:

- construct 31 stationary aggregates;
- one household batch;
- one source-faithful labor reconstruction;
- one K1A with beta_distance=2 and beta_return=0;
- one C1 residual GovInv construction;
- 31 firm evaluations;
- one wage assignment;
- one monetary assignment;
- one fiscal diagnostic batch;
- exactly one canonical same-S raw next-payoff construction;
- persist raw turn3 next-state candidate;
- STOP before any turn3 household execution.

No K1B, K2 or third outer turn.

## Scientific ceilings

Fresh turn2 ceilings:

- source-native initializations <=31
- labor roots attempted/returned <=24,800
- corrected policy maps / D2-Q assemblies <=1,581
- selector evaluations <=1,264,800
- direct HJB updates <=1,550
- SCC decompositions <=31
- restricted GESVD <=31
- normalized stationary candidates <=31
- full-Q stationarity checks <=31
- full-space GESVD =0
- aggregate evaluations <=31
- household batch <=1
- labor/K1A/C1 <=1 each
- firm evaluations <=31
- wage/monetary/fiscal <=1 each
- canonical raw payoff <=1
- turn3 household=0
- K1B=0
- K2=0
- MATLAB=0
- GE/annual/shock/IRF/welfare/Results=0
- scientific retries=0
- solver substitutions=0.

Relaxation arithmetic ceilings:

- relaxation helper invocations <=1,550
- alpha candidates evaluated <=82,150
  (=1,550*53 maximum)
- no extra direct solve may be caused by relaxation.

## Engineering/source-freeze gates

Before runtime require:

- current production source exactly equals accepted implementation;
- selector/cost/generator/option_a_step/KFE protected blobs unchanged from accepted implementation;
- Owner adoption and implementation acceptance present;
- exact entering-state receipt binding PASS;
- `py_compile` PASS for the fresh validator;
- `git diff --check` PASS.

During and after runtime require source freeze exact.

No production source change is authorized in this task.

## First-failure stop rule

Any first new scientific failure must stop the entire run immediately.

Persist the exact first failing province/checkpoint/cell/stage and all evidence already legally produced.

Do not rescue, tune, change alpha law, alter Delta, rerun the failed object, or continue to later provinces.

## Success terminal

If all 31 provinces pass and exactly one integration completes:

`PASS__MONOTONICITY_PRESERVING_RELAXATION_FRESH_TURN2_RUN005__31_PROVINCE_HJB_KFE_AND_INTEGRATION_PASS__RAW_TURN3_PAYOFF_READY__TURN3_NOT_RUN`

If a new scientific failure occurs, return its exact fail-closed terminal and stop.

## Allowed paths

Fresh validator:

`validators/multi_province/monotonicity_preserving_hjb_relaxation_fresh_turn2_run005/**`

Optional focused test:

`tests/test_mp4c_monotonicity_preserving_hjb_relaxation_fresh_turn2_run005.py`

Fresh evidence:

`reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_fresh_turn2_run005_20260921/`

Report:

`docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_FRESH_TURN2_RUN005_REPORT.md`

No production source changes.

Do not modify CURRENT.

Do not publish a successor.

## Required evidence

Persist at minimum:

- authority/source binding;
- entering-state binding;
- pre/post code freeze;
- scientific ledger;
- relaxation arithmetic ledger;
- per-province HJB/KFE terminal receipts for every reached province;
- relaxation receipts for every direct update;
- 黑龙江 runtime-parity receipt if reached;
- aggregate/integration evidence if reached;
- terminal receipt;
- sealed manifest/readback;
- report.

Commit + ordinary non-force push, then STOP.
