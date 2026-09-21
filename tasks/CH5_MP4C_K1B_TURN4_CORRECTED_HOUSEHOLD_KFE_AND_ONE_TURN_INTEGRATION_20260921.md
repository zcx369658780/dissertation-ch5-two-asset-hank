# Task — K1B turn4 corrected household HJB/KFE and one-turn integration

Date: 2026-09-21

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_K1B_TURN4_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_20260921`

Status: `ACTIVE`

Results eligibility: `FALSE`

## Roles and authority

Owner is final scientific authority. ChatGPT is L3 independent Reviewer / scientific-route authority. Codex is bounded Builder / scientific numerical analyst. GitHub live main is repository-state authority.

Absolutely do not enter, read, search, use or modify:

`zcx369658780/deep-learning-hank`.

## Purpose

Execute exactly one further K1B-active corrected turn, turn4.

This task is a bounded continuation to determine whether the first K1B-active PASS persists for a second consecutive turn under the already frozen economics and numerical laws.

Stage 1 solves the 31-province corrected household HJB/KFE batch from the accepted turn4 K1B entering-state candidate.

Stage 2 is allowed only if all 31 household blocks pass. It performs exactly one source-faithful-labor + frozen-turn4-K1B-share + C1 + firm integration and prepares the deterministic lagged K1B turn5 input candidate.

Stop before any turn5 household solve.

This is not a full outer fixed-point or steady-state run.

## Required reads

Fresh-fetch live main, then read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_K1B_TURN3_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_ACCEPTANCE_20260921.md`
6. `docs/CH5_MP4C_K1B_TURN3_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_REPORT.md`
7. `docs/CH5_MP4C_K1B_TURN3_LAGGED_RAW_RA0_ATTRACTIVENESS_ACTIVATION_SAFETY_GATE_ACCEPTANCE_20260921.md`
8. `docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_FRESH_TURN2_RUN005_ACCEPTANCE_20260921.md`
9. `docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_IMPLEMENTATION_AND_PERSISTED_REPLAY_ACCEPTANCE_20260921.md`
10. `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
11. `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
12. `docs/CH5_MP4C_K1A_RAW_RA0_PAYOFF_OWNER_ADOPTION_20260920.md`
13. current corrected household/KFE and one-turn integration production source, read-only
14. this exact task.

## Exact turn4 entering authority

Use exactly:

`reports/ch5_mp4c_k1b_turn3_corrected_household_kfe_and_one_turn_integration_20260921_run001/turn4_k1b_input_candidate.json`

Git blob:

`ee779174c614980a0e6182d710ea5aaec8afb6f5`

file SHA-256:

`35CA47135CF3B17ADACDD6C39FBA30CC0E55AE1C103C5F42064D6722AF28310C`

Required classification:

`TURN4_K1B_INPUT_CANDIDATE_ONLY__TURN4_HOUSEHOLD_NOT_RUN`.

Required entering household payoff SHA-256:

`7DE65A71206F52AB3D2DA98D6D01C43A8A69D8B2C423BE49A15D5D287C434BE9`.

Completed-turn3 raw-ra0 source:

`1C587932F4E8471209663D2262DB1BB308857EEEA1198D7868E4721CFB031E8F`.

No alternate turn4 state is authorized.

## Frozen turn4 K1B share plan

Use exactly:

`reports/ch5_mp4c_k1b_turn3_corrected_household_kfe_and_one_turn_integration_20260921_run001/turn4_k1b_frozen_share_payoff_plan.npz`

Git blob:

`a37647bb68ed1bec6259071d7035f8de07591c9f`

file SHA-256:

`41B7DDA4DE2C33C6EADFAB3F324C3592D119B0E91DC7AE8E23968653A881522A`.

Frozen portfolio-share SHA-256:

`5E8FB74E547CBF776A70E908F1ECA7F8FD80DD1A7637100BBD159B7F0803028B`.

Turn4 integration must reuse this exact destination-by-origin matrix. It must not recompute turn4 shares from turn4 firm returns.

## Frozen K1B economics

Keep exactly:

- fixed `theta_i=inter_prv_ratio_i`;
- `beta_distance=2.0`;
- `beta_return=0.5`;
- pure geographic distance score;
- completed-previous-turn raw `ra0` population z-score with ddof=0 for attractiveness only;
- raw `ra0` level for household payoff;
- no smoothing/partial adjustment;
- same-S quantity/payoff accounting;
- lagged timing only;
- source-faithful labor.

No parameter or economic-law change is authorized.

## Turn4 household HJB contract

For each province in canonical order 0..30:

- exact accepted turn4 state;
- one source-native initialization;
- exact 20x20x2 grid, F-order;
- no warm start from turn3 terminal household values;
- accepted corrected selector/D1/D2/D3/root/switching/boundary laws unchanged;
- fixed `Delta=1000`;
- `scipy.sparse.linalg.spsolve` only;
- direct-solve backward error <= `1e-12`;
- convergence `B<=1e-8` and `D<=1e-7`;
- accepted exact/approximate cycle rules;
- maximum 50 direct HJB updates per province;
- no solver substitution, adaptive Delta, clipping, artificial diffusion, warm-start rescue, tuning or scientific retry.

After every accepted direct solve, reuse the accepted monotonicity-preserving relaxation helper unchanged:

- alpha schedule `1,1/2,...,2^-52`;
- all raw b-edge slopes finite and strictly positive;
- exhaustion fails closed;
- alpha search causes no additional direct solve.

Stop the task on the first new scientific failure.

## Terminal KFE contract

For every converged province, use the accepted unique-closed-class KFE law unchanged:

- exact-positive topology;
- one SCC decomposition;
- exactly one closed class;
- restricted `Q_CC`;
- one restricted dense GESVD on `Q_CC.T`;
- frozen rank/nullity thresholds;
- smallest right singular vector;
- one sign orientation and one normalization;
- strictly positive closed-class mass;
- exact zero transient mass;
- one full-Q stationarity check;
- full-space 800x800 GESVD = 0;
- no pin/source RHS/clipping/alternate eigensolver/retry.

## Exactly one turn4 K1B integration

Only if all 31 household HJB/KFE blocks pass:

1. construct the accepted corrected household aggregates and one 31-province batch;
2. source-faithful labor exactly once;
3. apply the frozen turn4 K1B share plan exactly once to current turn4 household wealth;
4. require origin-column conservation, national private-capital conservation and exact home retained identity;
5. construct C1 `GovInv=max(Ktarget-Kprivate,0)`;
6. evaluate 31 firms exactly once;
7. wage / monetary / fiscal each exactly once;
8. persist completed-turn4 raw unclipped firm `ra0`;
9. do not recompute the already frozen turn4 share plan from same-turn firm returns.

Historical clipped/used `ra` remains diagnostic only.

## Deterministic turn5 K1B preparation

After completed-turn4 raw `ra0` exists, with zero turn5 household calls:

1. population z-score, ddof=0, canonical ordered arithmetic;
2. sigma must be finite and strictly positive;
3. `score[j,i]=-2*distance_score[j,i]+0.5*z_j` for foreign destinations;
4. stable foreign-only softmax;
5. fixed theta and no smoothing;
6. construct frozen `S_K1B_turn5`;
7. construct raw payoff `rah_turn5_i=sum_j S_turn5[j,i]*raw_ra0_turn4_j` with ordered destination summation;
8. preserve same-S future quantity/payoff contract;
9. create a turn5 entering-state candidate.

Classification:

`TURN5_K1B_INPUT_CANDIDATE_ONLY__TURN5_HOUSEHOLD_NOT_RUN`.

Do not run turn5 household.

## Cross-turn diagnostic panel

Persist, as diagnostics only and not acceptance targets:

- turn3 versus turn4 household checkpoint/update counts;
- turn3 versus turn4 raw-ra0 vector change;
- z-score mean/std change;
- turn4 frozen share versus newly prepared turn5 share change;
- C1 GovInv total change;
- key aggregate-state changes.

Do not require any sign, monotonicity or convergence improvement. The purpose is to assess whether another bounded continuation or a longer path is scientifically justified after Reviewer inspection.

## Scientific ceilings

Maximum:

- source-native initializations: 31
- scalar labor roots: 24,800
- policy maps / D2-Q assemblies: 1,581
- selector evaluations: 1,264,800
- direct HJB updates: 1,550
- relaxation helper invocations: 1,550
- alpha candidates: 82,150
- SCC decompositions: 31
- restricted GESVD: 31
- normalized stationary candidates: 31
- full-Q stationarity checks: 31
- full-space 800x800 GESVD: 0
- aggregate evaluations: 31
- household batch: 1
- source-faithful labor: 1
- frozen turn4 K1B allocation: 1
- C1: 1
- firms: 31
- wage / monetary / fiscal: 1 each
- completed-turn4 raw-ra0: 1
- deterministic turn5 preparation: 1
- turn5 household: 0
- K2: 0
- MATLAB: 0
- GE/annual/shock/IRF/welfare/Results: 0
- scientific retries: 0
- solver substitutions: 0.

## Source changes and allowed paths

Production source changes: 0.

Do not modify:

`src/ch5_two_asset_hank/**`.

Allowed:

- `validators/multi_province/k1b_turn4_corrected_household_kfe_and_one_turn_integration/**`
- `tests/test_mp4c_k1b_turn4_corrected_household_kfe_and_one_turn_integration.py`
- `reports/ch5_mp4c_k1b_turn4_corrected_household_kfe_and_one_turn_integration_20260921_run001/**`
- `docs/CH5_MP4C_K1B_TURN4_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_REPORT.md`.

Do not modify CURRENT. Do not publish a successor.

## Required evidence

Persist:

- exact entering-state/share-plan binding;
- source pre/post freeze;
- scientific ledger;
- relaxation ledger;
- per-province HJB/KFE terminal evidence;
- stationary aggregates and household batch;
- source-faithful labor;
- frozen-share capital accounting;
- C1;
- firm raw/used-return diagnostics;
- completed-turn4 raw-ra0;
- deterministic turn5 z-score/share/payoff;
- cross-turn diagnostic panel;
- turn5 candidate;
- terminal receipt;
- sealed manifest/readback;
- focused tests.

## Terminal

Success:

`PASS__K1B_TURN4_31_PROVINCE_HJB_KFE_AND_ONE_INTEGRATION__TURN5_K1B_INPUT_READY__TURN5_NOT_RUN`.

On any provenance/HJB/KFE/conservation/C1/firm/timing/source-freeze failure, fail closed at the first failing scientific object. No rescue/tuning.

Commit + ordinary non-force push + remote SHA/tree readback + clean worktree, then STOP.
