# Task — K1B turn-3 corrected household HJB/KFE and one-turn integration

Date: 2026-09-21

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_K1B_TURN3_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_20260921`

Status: `ACTIVE`

Results eligibility: `FALSE`

## Roles and authority

Owner is final scientific authority. ChatGPT is L3 independent Reviewer / scientific-route authority. Codex is bounded Builder / scientific numerical analyst. GitHub live main is repository-state authority.

Absolutely do not enter, read, search, use or modify:

`zcx369658780/deep-learning-hank`.

## Purpose

Execute exactly one corrected K1B turn3.

Stage 1 solves the 31-province corrected household HJB/KFE batch from the accepted K1B turn3 entering-state candidate.

Stage 2 is allowed only if all 31 household blocks pass. It performs exactly one source-faithful-labor + frozen-K1B-share + C1 + firm integration, then constructs the deterministic lagged K1B turn4 share/payoff candidate.

Stop before any turn4 household solve.

This is a bounded K1B activation runtime, not an outer steady-state run.

## Required reads

Fresh-fetch live main, then read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1B_TURN3_LAGGED_RAW_RA0_ATTRACTIVENESS_ACTIVATION_SAFETY_GATE_ACCEPTANCE_20260921.md`
6. `docs/CH5_MP4C_K1B_TURN3_LAGGED_RAW_RA0_ATTRACTIVENESS_ACTIVATION_SAFETY_GATE_REPORT.md`
7. `docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_FRESH_TURN2_RUN005_ACCEPTANCE_20260921.md`
8. `docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTATION_AND_PERSISTED_REPLAY_ACCEPTANCE_20260921.md`
9. `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
10. `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
11. `docs/CH5_MP4C_K1A_RAW_RA0_PAYOFF_OWNER_ADOPTION_20260920.md`
12. current corrected household/KFE and one-turn integration production source, read-only
13. this exact task.

## Exact turn3 entering authority

Use exactly:

`reports/ch5_mp4c_k1b_turn3_lagged_raw_ra0_activation_safety_gate_20260921_run001/k1b_turn3_input_candidate.json`

Git blob:

`b33bfdf2fa17fb110684b83757b871fff3e884c7`

file SHA-256:

`76238863C98929E30B895FA5BE200CC1185A6ABFD0E11BC34AB3082A2705CE27`

Required classification:

`TURN3_K1B_INPUT_CANDIDATE_ONLY__HOUSEHOLD_NOT_RUN`.

Required entering K1B household payoff SHA-256:

`CEEFE34C16BA0DFDE9FA0C5590DFBB89084475BD88A8496EC18FEEBA7CB674D2`.

The completed-turn2 raw-ra0 source behind this candidate is:

`B3B50A6F0A3876904582DE05354C2DF76A71524FB53E41D4170109B8FCEB8951`.

No alternate turn3 state is authorized.

## Frozen turn3 K1B share plan

The exact share plan is persisted in:

`reports/ch5_mp4c_k1b_turn3_lagged_raw_ra0_activation_safety_gate_20260921_run001/k1b_turn3_frozen_share_payoff_plan.npz`

Git blob:

`f6d917c1a2bb391d048d36ac1a49cc07516440fa`

file SHA-256:

`06D25DA78B2DAFD090A9E77EC544FB9CEFA42EE0F9B925EE0544169A2DD2858D`.

Frozen portfolio-share SHA-256:

`4C3AB67F1982AEB3B707D07C53BB98C5BA54C835234DFEDE45A96B09BC5E3AB6`.

Turn3 integration must reuse this exact destination-by-origin `S_K1B`. It must not recompute turn3 shares from turn3 firm returns.

## Turn3 household HJB contract

For each province, in canonical index order 0..30:

- use the exact entering state above;
- use one source-native numerical initialization;
- exact 20x20x2 grid and F-order;
- no warm start from turn2 terminal values;
- preserve the accepted corrected selector/D1/D2/D3/root/switching/boundary laws;
- fixed `Delta=1000`;
- direct solver = `scipy.sparse.linalg.spsolve` only;
- direct-solve backward error <= `1e-12`;
- Bellman metric `B<=1e-8`;
- value-change metric `D<=1e-7`;
- existing exact/approximate cycle rules;
- maximum 50 direct HJB updates per province;
- no solver substitution, adaptive Delta, clipping, artificial diffusion, warm-start rescue or scientific retry/tuning.

After every accepted direct solve, use the already accepted monotonicity-preserving relaxation helper unchanged:

- alpha schedule exactly `1, 1/2, ..., 2^-52`;
- next accepted state requires every raw b-edge slope finite and strictly positive;
- exhaustion fails closed;
- alpha search itself causes no extra direct solve.

Stop the entire task at the first new scientific failure.

## Terminal KFE contract

For every converged province, use the accepted unique-closed-class source-free KFE contract unchanged:

- exact-positive topology;
- one SCC decomposition;
- exactly one closed communicating class;
- restricted `Q_CC`;
- one restricted dense GESVD on `Q_CC.T`;
- accepted rank/nullity thresholds;
- smallest right singular vector;
- one sign orientation and one normalization;
- strictly positive closed-class probability;
- exact zero transient mass;
- one full-Q `Q.T@p` stationarity check;
- no full-space 800x800 GESVD;
- no pin equation, source RHS, clipping, alternate eigensolver or retry.

## Household aggregation

Only after each province's HJB and KFE pass, construct the accepted corrected aggregates:

- Ct
- Lt
- At
- Bt
- AtTax.

Build one 31-province household batch only if all 31 provinces pass.

## Exactly one turn3 K1B integration

Only if all 31 household blocks pass:

1. use source-faithful labor exactly once;
2. use the frozen turn3 `S_K1B` exactly once for capital quantities;
3. use current turn3 household wealth `W_i=A_i*N_i` with that fixed share matrix;
4. require origin-column and national private-capital conservation and exact home retained identity;
5. construct C1 `GovInv=max(Ktarget-Kprivate,0)`;
6. evaluate 31 firms exactly once;
7. assign composite wage once;
8. assign monetary variables once;
9. run fiscal diagnostics once;
10. persist completed-turn3 raw unclipped firm `ra0`.

Historical clipped firm `ra` may remain a diagnostic/source field but must not replace raw `ra0` as the corrected household payoff authority.

No same-turn turn3 firm return may modify the already frozen turn3 share matrix.

## Deterministic turn4 K1B preparation

After the completed turn3 firm raw-return vector exists, and without any turn4 household call:

1. compute the 31-province population z-score with the exact frozen ddof=0 ordered arithmetic;
2. fail closed if sigma is nonfinite or nonpositive;
3. construct the next K1B foreign score using `beta_distance=2.0`, `beta_return=0.5`;
4. stable foreign-only softmax, no smoothing;
5. fixed `theta_i=inter_prv_ratio_i`;
6. construct frozen `S_K1B_turn4`;
7. construct `rah_turn4_i=sum_j S_K1B_turn4[j,i]*raw_ra0_turn3_j` using ordered destination summation;
8. preserve same-S quantity/payoff timing for the future turn4;
9. construct a turn4 entering-state candidate by changing only fields authorized by the completed turn3 integration and the new raw-payoff/share plan.

Classify the output:

`TURN4_K1B_INPUT_CANDIDATE_ONLY__TURN4_HOUSEHOLD_NOT_RUN`.

Do not run turn4 household HJB/KFE.

## Required diagnostics

Persist at minimum:

- exact entering-state and share-plan binding;
- production-source pre/post freeze;
- scientific-call ledger;
- relaxation arithmetic ledger;
- per-province compact HJB terminal/checkpoint evidence;
- per-province terminal KFE evidence;
- stationary aggregate receipts;
- household batch identity;
- source-faithful labor receipt;
- turn3 frozen-share capital-network conservation;
- C1 residual-GovInv receipt;
- 31 firm raw/used-return diagnostics;
- turn3 raw-ra0 vector and SHA;
- deterministic turn4 z-score/share/payoff receipts;
- turn4 candidate receipt;
- terminal receipt;
- sealed manifest and independent readback.

Record K1A/run005 comparisons only as diagnostics. No difference direction, convergence improvement or fit metric is an acceptance condition.

## Scientific ceilings

Maximum:

- source-native initializations: 31
- scalar labor roots: 24,800
- corrected policy maps / D2-Q assemblies: 1,581
- selector evaluations: 1,264,800
- direct HJB updates: 1,550
- relaxation helper invocations: 1,550
- alpha candidates evaluated: 82,150
- SCC decompositions: 31
- restricted GESVD: 31
- normalized stationary candidates: 31
- full-Q stationarity checks: 31
- full-space 800x800 GESVD: 0
- corrected aggregate evaluations: 31
- household batch: 1
- source-faithful labor: 1
- frozen K1B turn3 quantity allocation: 1
- C1 construction: 1
- firm evaluations: 31
- wage / monetary / fiscal batch: 1 each
- completed-turn3 raw-ra0 vector: 1
- deterministic turn4 z-score/share/payoff construction: 1
- turn4 household: 0
- K2: 0
- MATLAB: 0
- GE/annual/shock/IRF/welfare/Results: 0
- scientific retries: 0
- solver substitutions: 0.

## Source changes

Production source changes: 0.

Do not modify:

`src/ch5_two_asset_hank/**`.

Allowed task artifacts:

- a fresh validator under `validators/multi_province/k1b_turn3_corrected_household_kfe_and_one_turn_integration/**`
- one focused test `tests/test_mp4c_k1b_turn3_corrected_household_kfe_and_one_turn_integration.py`
- one fresh evidence root `reports/ch5_mp4c_k1b_turn3_corrected_household_kfe_and_one_turn_integration_20260921_run001/`
- report `docs/CH5_MP4C_K1B_TURN3_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_REPORT.md`.

Do not modify CURRENT.

Do not publish a successor.

## Stop and terminal

Any provenance, HJB, KFE, conservation, C1, firm-finiteness, timing or source-freeze failure fails closed at the first failing scientific object. Preserve legal evidence and stop. Do not rescue or tune.

Success terminal:

`PASS__K1B_TURN3_31_PROVINCE_HJB_KFE_AND_ONE_INTEGRATION__TURN4_K1B_INPUT_READY__TURN4_NOT_RUN`.

A PASS authorizes Reviewer inspection of one complete K1B-active turn. It does not establish outer fixed-point convergence or authorize K2/GE/Results.

Commit + ordinary non-force push, remote SHA/tree readback, clean worktree, then STOP.
