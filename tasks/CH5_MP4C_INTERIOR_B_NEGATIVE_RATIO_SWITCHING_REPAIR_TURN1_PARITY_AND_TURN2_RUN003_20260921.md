# Task — interior-b negative-ratio switching repair, turn-1 policy parity, and fresh turn-2 run003

Date: 2026-09-21

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_INTERIOR_B_NEGATIVE_RATIO_SWITCHING_REPAIR_TURN1_PARITY_AND_TURN2_RUN003_20260921`

Status: `COMPLETED__ACCEPTED_FAIL`

## Governance

Owner is final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

GitHub live main is repository-state authority.

Absolute prohibition: never enter, read, search, use or modify `zcx369658780/deep-learning-hank`.

Fresh-fetch live main and read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_TURN2_F0364_NEGATIVE_RATIO_SWITCHING_FALSE_NEGATIVE_ACCEPTANCE_20260921.md`
6. `docs/CH5_MP4C_2018_KFE_D123_INTERIOR_A_ZERO_DRIFT_SWITCHING_OWNER_ADOPTION_20260919.md`
7. accepted turn-1 full-closure authority
8. accepted F0579 repair authority
9. turn-2 run002 F0364 failure authority/evidence
10. current selector/cost/HJB/KFE authorities.

No new equation, KKT law, boundary law, tolerance, calibration, solver or payoff law is authorized.

## Objective

1. implement the narrowly authorized interior-liquid negative-ratio interior-a switching correction;
2. prove exact F0364 parity with the accepted forensic;
3. prove accepted turn-1 run004 selected-policy identities are unchanged under the corrected selector;
4. only if turn-1 parity is exact, execute one fresh turn-2 run003 from the exact accepted turn-2 entering state;
5. stop at first scientific failure or after one completed turn-2 integration;
6. do not run turn 3.

## Authorized selector change

Allowed scientific source path:

`src/ch5_two_asset_hank/corrected_diagnostic/selector.py`.

The already accepted active-upper-b negative enumeration repair remains in force.

Only the following additional semantic correction is authorized.

Inside the existing interior-a switching constructor:

### Interior liquid node

When b is interior:

- allow a finite negative nonzero D3 ratio R;
- preserve ratio=0 as fail closed;
- compute the mapped q_b interval by dividing both sorted a-derivative endpoints by R and sorting the two images;
- do not assume division preserves endpoint order;
- preserve the persisted liquid derivative shadow p_b as q_b;
- construct the switching candidate through the existing `_candidate` route;
- require q_a=R*q_b to lie inside the original closed sorted a-derivative interval;
- preserve all existing direction/KKT/finite/Hamiltonian checks.

### Active liquid face

For active lower-b or upper-b faces:

- preserve the current ratio-sign behavior exactly;
- no negative-ratio active-face root interval is authorized in this task.

### Other preserved behavior

Do not change:

- strict-crossing trigger;
- d_z=-r_a*a;
- transfer regime selection;
- D3 adjustment/KKT equations;
- liquid-Z law;
- joint switching law;
- lower-a zero-kink law;
- active-face root domain;
- root grid/tolerance;
- D2;
- Hamiltonian comparison/tie rule;
- any calibration.

Implementation should be a minimal control-flow / interval-order correction.

## F0364 exact focused parity

Before predecessor replay or fresh turn-2 science, tests must bind the exact persisted F0364 cell and prove normal selector execution now emits the accepted switching candidate.

Require selected candidate invariants:

- transfer regime: negative
- derivative branch b: backward
- derivative branch a: zero/switching
- q_b: `0.006091715618507631`
- q_a: `-0.0045978913784868415`
- d: `-7.8384208979658965`
- g_a: canonical zero
- g_b: `-4.227123020026542`
- transfer-KKT residual: `0`
- Hamiltonian: `-0.11188508398929994`
- admissible: true
- selected policy: this switching candidate.

Also prove:

- p_b forward does not produce an admissible switching candidate;
- active-liquid-face negative-ratio behavior remains unchanged;
- ratio zero remains fail closed;
- no root is introduced for this interior-b F0364 switching candidate.

## Mandatory accepted turn-1 compatibility replay

This is a hard gate before fresh turn-2 science.

Authority root:

`reports/ch5_mp4c_corrected_optionb_initial_turn_unique_closed_class_kfe_20260920_run004/`

Bind its accepted manifest:

`CF70E7D6A62A35F461D1A75B28F8F502B2CBDD2D94ED5D9DDFA099D821CC5EC6`.

Replay every completed turn-1 household checkpoint policy map using:

- the exact persisted checkpoint V;
- the exact original turn-1 province entering state/scalars;
- the repaired selector;
- the same grid/parameters;
- no HJB direct update;
- no D2/Q assembly;
- no KFE;
- no aggregate or integration work.

Expected accepted map count:

`408`.

For every map compare the exact selected-policy identity produced by replay against the accepted persisted checkpoint policy identity.

Persist:

- total maps replayed;
- total selector evaluations;
- root/switching call counts by category;
- exact-match count;
- mismatch count;
- complete mismatch list if nonzero;
- an ordered digest of replayed policy identities;
- an ordered digest of accepted policy identities.

Hard gate:

### Exact parity

If all 408 selected-policy identities match exactly:

`PASS__TURN1_ACCEPTED_POLICY_IDENTITY_PARITY_UNDER_INTERIOR_B_NEGATIVE_RATIO_REPAIR`

and fresh turn-2 run003 may proceed.

### Any mismatch

If any accepted turn-1 map differs:

`BLOCKED__INTERIOR_B_NEGATIVE_RATIO_REPAIR_TURN1_POLICY_PARITY_MISMATCH`

STOP immediately.

Do not run turn 2.

Do not silently reclassify or replace the accepted turn-1 path.

The mismatch evidence will return to Reviewer for a separately authorized turn-1 reexecution.

## Compatibility replay budget

Maximum:

- turn-1 policy maps replayed: 408
- selector evaluations: 326,400
- full HJB direct solves/updates: 0
- D2/Q assemblies: 0
- SCC/KFE/SVD: 0
- aggregates/integration: 0
- scientific retries: 0.

Root-call counts must be separately reported. No retry/tuning is allowed.

## Engineering gate

Before compatibility replay:

- focused tests PASS;
- selector diff exactly within authorized interior-b negative-ratio logic plus previously accepted upper-b repair;
- cost.py unchanged;
- nonlinear HJB/KFE source unchanged;
- turn-2 integration source unchanged;
- F0364 forensic manifest:
  `6FF469F423A7D5D321A59E1DC4031B04E967E3EE4A03E58865824D8B5D8CE1D0`
  bound exactly;
- turn-2 run002 manifest:
  `A2A882B8D79A6897D0518447FA84F7775609E31D34452A5EB2F7B7773E9FD0B0`
  bound exactly;
- turn-1 run004 manifest exact;
- canonical initial-turn integration manifest:
  `79C6B15340AF641A736C79D0ED7C6450E39EA495263943280B6DDBD1B094F28D`
  bound exactly;
- `py_compile` PASS;
- `git diff --check` PASS;
- code freeze PASS.

Engineering retries before scientific replay are allowed.

## Fresh turn-2 run003 authority

Only after exact turn-1 compatibility parity PASS.

Use the exact accepted entering-state authority:

`reports/ch5_mp4c_run004_canonical_same_s_integration_replay_20260920_run001/next_state_candidate_receipt.json`

accepted blob:

`85df3f0bdcc3b0bb3e7b12f0ba35dbb9abda764d`.

Require exact 31-row order, status and raw-payoff identity:

`D77669DB4245DDCE3D6E91231A92C4A2AD12415D165F0718D0605BD213FDB414`.

Use each persisted state directly.

## Turn-2 HJB/KFE/integration

All authorities remain unchanged except the two already accepted selector corrections:

1. active-upper-b negative branch enumeration repair;
2. interior-b negative-ratio interior-a switching repair.

Initialization:

- one source-native initialization per reached province;
- 800 labor roots per reached province;
- no warm start;
- no retry.

HJB:

- 20x20x2 F-order grid;
- fixed Delta=1000;
- existing D1/D2/D3/KKT/boundary/upwind laws;
- convergence iff B<=1e-8 and D<=1e-7;
- only scipy.sparse.linalg.spsolve;
- backward error <=1e-12;
- cycle law unchanged;
- max 50 updates/province;
- province order 0..30;
- first scientific failure stops all.

At Beijing checkpoint 5 / flat 364 persist an exact repair-parity receipt from the normal map proving the selected switching candidate matches the forensic invariants without an extra selector call.

Terminal KFE:

- Owner-adopted unique-closed-class method unchanged;
- <=31 SCC;
- <=31 restricted GESVD;
- no full-space GESVD;
- one candidate/normalization/full-Q stationarity per converged province;
- no retry.

If all 31 household blocks pass:

- aggregates=31;
- household batch=1;
- source-faithful labor=1;
- K1A=1 with beta_distance=2, beta_return=0;
- C1=1;
- firms=31;
- wage/monetary/fiscal=1 each;
- canonical same-S raw-next-payoff=1.

Do not run turn 3.

## Fresh turn-2 run003 scientific budgets

Initialization:
- <=31 source-native initializations
- <=24,800 labor roots

HJB:
- <=1,581 policy/D2 maps
- <=1,264,800 selector evaluations
- <=1,550 direct updates
- max 50/province

KFE:
- <=31 SCC
- <=31 restricted GESVD
- <=31 normalized candidates
- <=31 full-Q Q.T@p
- full-space GESVD=0

Integration:
- aggregates<=31
- household batch<=1
- labor/K1A/C1<=1
- firms<=31
- wage/monetary/fiscal<=1
- canonical payoff<=1

Forbidden:
- scientific retries=0
- solver substitutions=0
- turn3 household=0
- third outer turn=0
- K1B=0
- K2=0
- adaptive controller=0
- MATLAB/GE/annual/shock/IRF/welfare/Results=0
- payoff transformations=0.

Compatibility-replay consumption must be ledgered separately from fresh turn-2 run003 consumption.

## Evidence

Fresh root:

`reports/ch5_mp4c_interior_b_negative_ratio_repair_turn1_parity_turn2_run003_20260921/`

Write:

`docs/CH5_MP4C_INTERIOR_B_NEGATIVE_RATIO_SWITCHING_REPAIR_TURN1_PARITY_AND_TURN2_RUN003_REPORT.md`.

Persist:

- authority binding;
- selector-repair contract;
- focused tests;
- F0364 exact parity;
- code freeze;
- turn-1 compatibility replay receipt and separate ledger;
- entering turn-2 state binding if reached;
- turn-2 per-province HJB/KFE evidence if reached;
- aggregates/batch/integration if reached;
- canonical future payoff if reached;
- exact turn-2 run003 ledger;
- historical lineage;
- terminal receipt;
- sealed manifest/readback.

## Terminal markers

If turn-1 compatibility mismatches:

`BLOCKED__INTERIOR_B_NEGATIVE_RATIO_REPAIR_TURN1_POLICY_PARITY_MISMATCH`.

If compatibility passes and full turn 2 plus integration passes:

`PASS__INTERIOR_B_NEGATIVE_RATIO_SWITCHING_REPAIR__TURN1_POLICY_PARITY_PASS__CORRECTED_TURN2_31_PROVINCE_HJB_KFE_AND_INTEGRATION__RAW_TURN3_PAYOFF_READY__TURN3_NOT_RUN`.

Any new turn-2 scientific failure stops at the exact first failing object.

## Git workflow

- isolated branch
- explicit staging only
- ordinary non-force push
- remote SHA/tree readback
- clean worktree
- do not modify CURRENT files
- do not merge main
- do not publish successor.
