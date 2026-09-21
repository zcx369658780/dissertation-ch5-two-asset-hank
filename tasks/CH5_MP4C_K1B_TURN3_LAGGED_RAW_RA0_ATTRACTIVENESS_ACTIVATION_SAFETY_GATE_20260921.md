# Task — K1B turn-3 lagged raw-ra0 attractiveness activation safety gate

Date: 2026-09-21

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_K1B_TURN3_LAGGED_RAW_RA0_ATTRACTIVENESS_ACTIVATION_SAFETY_GATE_20260921`

Status: `COMPLETED__ACCEPTED_PASS`

Results eligibility: `FALSE`

## Roles and authority

Owner is final scientific authority. ChatGPT is L3 independent Reviewer / scientific-route authority. Codex is bounded Builder / scientific numerical analyst. GitHub live main is repository-state authority.

Absolutely do not enter, read, search, use or modify:

`zcx369658780/deep-learning-hank`.

## Purpose

Reopen the preregistered K1B lagged-return destination-attractiveness route now that the bounded corrected turn-1 / turn-2 prefix has passed.

This is a **zero-science activation safety gate**.

It must construct and validate the exact K1B share/payoff objects that would feed a future turn-3 runtime.

It must not run turn-3 household HJB/KFE, firms, integration or any outer scientific runtime.

## Required reads

Fresh-fetch live main, then read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_MONOTONICITY_PRESERVING_HJB_RELAXATION_FRESH_TURN2_RUN005_ACCEPTANCE_20260921.md`
6. `docs/CH5_MP4C_BILATERAL_CAPITAL_NETWORK_SCIENTIFIC_DESIGN_FREEZE_CURRENT.md`
7. `docs/CH5_MP4C_K1_SCORING_AND_DATA_CONTRACT_FREEZE_CURRENT.md`
8. `docs/CH5_MP4C_K1A_RAW_RA0_PAYOFF_OWNER_ADOPTION_20260920.md`
9. `src/ch5_two_asset_hank/multi_province/capital_network.py` read-only
10. `src/ch5_two_asset_hank/multi_province/k1a_runtime_adapter.py` read-only
11. exact run005 integration / turn3-candidate evidence
12. this task.

## Frozen K1B scientific contract

Use exactly:

- fixed `theta_i=inter_prv_ratio_i`;
- `beta_distance=2.0`;
- `beta_return=0.5`;
- no portfolio smoothing / partial adjustment;
- destination attractiveness uses completed-turn-2 raw unclipped firm `ra0`;
- household payoff level also uses completed-turn-2 raw unclipped firm `ra0`;
- attractiveness score and payoff level remain separate objects;
- same destination-by-origin portfolio matrix `S` is used for K1B allocation and household payoff aggregation;
- same-turn firm-return feedback is prohibited.

Foreign score:

`score[j,i] = -2.0*distance_score[j,i] + 0.5*return_score[j]`

for `j != i`.

Home share remains exactly:

`S[i,i]=1-theta_i`.

Foreign conditional shares use the existing stable foreign-only softmax engine.

## Reviewer implementation freeze — cross-sectional z-score

The 31 provinces are the full model cross-section, not a statistical sample.

For this K1B route, standardize completed-turn-2 raw `ra0` using the population cross-sectional convention:

`mu = (1/31) * sum_j ra0_j`

`sigma = sqrt((1/31) * sum_j (ra0_j-mu)^2)`

`return_score_j = (ra0_j-mu)/sigma`.

Use deterministic ordered arithmetic for the persisted canonical vector.

Equivalent vectorized arithmetic may be reported diagnostically, but the canonical receipt must bind the ordered result.

If sigma is zero, nonfinite or not strictly positive, fail closed.

No winsorization, clipping, rescaling, ranking or other transform is authorized.

## Exact run005 source objects

Evidence root:

`reports/ch5_mp4c_monotonicity_preserving_hjb_relaxation_fresh_turn2_run005_20260921/`

Bind at minimum:

- `one_turn_integration_receipt.json`
- `turn3_next_state_candidate_receipt.json`
- accepted distance matrix
- fixed theta vector / province order.

Required completed-turn-2 raw firm payoff SHA-256:

`B3B50A6F0A3876904582DE05354C2DF76A71524FB53E41D4170109B8FCEB8951`.

Existing K1A raw turn-3 payoff SHA-256 for comparison only:

`5996A20CEE227389A7975703452EA6DAF1A2F817C517FFE43BEF3A53FA4292E2`.

## Required zero-science analysis

### A. Lagged-return score

Persist:

- exact 31 raw `ra0` values in canonical province order;
- ordered mean;
- population standard deviation;
- 31 z-scores;
- score vector SHA-256;
- mean-score and population-variance checks.

Provenance must explicitly state:

`COMPLETED_TURN2_RAW_RA0__USED_FOR_TURN3_K1B_ATTRACTIVENESS`.

### B. K1B foreign conditional shares

Use the frozen distance score and exact K1B score.

Require:

- destination x origin orientation;
- diagonal conditional shares exactly zero;
- nonnegative finite off-diagonal shares;
- each foreign conditional column sums to exactly/prospectively 1 under the existing accounting tolerance;
- stable softmax only;
- no smoothing.

Persist full matrix and SHA-256.

### C. Full K1B portfolio shares

Combine foreign conditional shares with fixed theta.

Require for every origin:

- diagonal exactly `1-theta_i`;
- foreign off-diagonal total exactly/prospectively `theta_i`;
- full column total 1;
- no negative/nonfinite share.

Compare against accepted K1A beta-distance-2 matrix:

- home shares must be identical;
- at least one foreign share must differ;
- no acceptance criterion may prefer a direction or magnitude of reallocation merely because it helps convergence.

Persist the K1B portfolio matrix and SHA-256.

### D. Turn-3 K1B household payoff candidate

Construct:

`rah_turn3_K1B_i = sum_j S_K1B[j,i] * raw_ra0_turn2_j`.

Use canonical ordered destination summation for each origin.

Require:

- all 31 payoff values finite;
- no clipping, smoothing, annualization, risk adjustment or z-score substitution;
- z-score enters attractiveness only;
- raw `ra0` level enters payoff only;
- the same exact `S_K1B` matrix is used.

Persist:

- 31-vector;
- SHA-256;
- min/max/mean;
- comparison to K1A turn3 payoff as diagnostic only.

### E. Turn-3 entering-state candidate

Construct a **K1B turn-3 household-input candidate** from the accepted run005 turn3 candidate:

- preserve all 31 non-`rah` state fields exactly;
- replace only entering household `rah` with the K1B raw-payoff vector above;
- preserve province order and all other state identities/fields;
- mark classification:
  `TURN3_K1B_INPUT_CANDIDATE_ONLY__HOUSEHOLD_NOT_RUN`.

Also persist the exact K1B portfolio-share plan that a future turn-3 K1B integration must reuse for the quantity/payoff timing contract.

Do not run the household block.

## Timing audit

The task must explicitly prove:

- score source = completed turn2 raw `ra0`;
- no turn3 firm output is read;
- no same-turn return feedback occurs;
- K1B share plan is predetermined for turn3 from completed-turn2 information;
- future turn3 capital quantities may use turn3 household wealth with this fixed share matrix;
- future household payoff and capital-network accounting must not silently use different share matrices.

If current authority is insufficient to make this timing mapping unique, STOP with a precise Owner-decision terminal rather than guessing.

## Conservation / algebraic safety panel

Using the accepted turn2 household wealth vector as a scale-only algebraic check, feed the K1B share matrix through the existing pure capital-network accounting.

This is not a turn3 capital prediction.

Require:

- each origin wealth column conserved;
- national private capital conserved;
- home retained exactly;
- payoff aggregation equals the independently ordered payoff vector;
- no same-turn provenance violation.

No firm runtime is allowed.

## Source changes

Production source changes: **0**.

Do not modify:

`src/ch5_two_asset_hank/**`.

Do not modify CURRENT.

Do not publish a successor.

## Scientific-call boundary

All fresh model science must remain zero:

- household HJB/KFE: 0
- direct HJB solves: 0
- selector/root calls: 0
- D2/Q: 0
- firms: 0
- integration/outer turn: 0
- turn3 household: 0
- K1B scientific runtime: 0
- K2: 0
- MATLAB: 0
- GE/Results: 0
- retry/tuning: 0.

Pure deterministic score/softmax/network algebra on accepted persisted inputs is authorized.

## Allowed paths

Validator:

`validators/multi_province/k1b_turn3_lagged_raw_ra0_activation_safety_gate/**`

Focused test:

`tests/test_mp4c_k1b_turn3_lagged_raw_ra0_activation_safety_gate.py`

Fresh evidence:

`reports/ch5_mp4c_k1b_turn3_lagged_raw_ra0_activation_safety_gate_20260921_run001/`

Report:

`docs/CH5_MP4C_K1B_TURN3_LAGGED_RAW_RA0_ATTRACTIVENESS_ACTIVATION_SAFETY_GATE_REPORT.md`

## Required terminal

Success:

`PASS__K1B_TURN3_LAGGED_RAW_RA0_ATTRACTIVENESS_ACTIVATION_SAFETY_GATE__SHARES_AND_HOUSEHOLD_PAYOFF_CANDIDATE_READY__NO_HJB_RUN`

If timing/normalization/scientific authority is ambiguous:

`BLOCKED__K1B_TURN3_ACTIVATION_SAFETY_GATE__SCIENTIFIC_AUTHORITY_AMBIGUOUS__OWNER_DECISION_REQUIRED`

Any algebra/conservation/provenance failure must fail closed.

## Required evidence

Persist:

- authority/source binding;
- run005 input binding;
- raw-ra0 z-score receipt;
- K1B foreign-share matrix;
- full portfolio-share matrix;
- K1A-vs-K1B share comparison;
- ordered K1B household-payoff receipt;
- K1B turn3 input candidate;
- timing/provenance receipt;
- conservation safety panel;
- zero-science ledger;
- focused tests;
- sealed manifest/readback;
- report.

Commit + ordinary non-force push, then STOP.


## Reviewer closure — 2026-09-21

Candidate `1c2157c1ee381f1bbc21bcebaa0233784e41a5c5` is accepted.

Acceptance:

`docs/CH5_MP4C_K1B_TURN3_LAGGED_RAW_RA0_ATTRACTIVENESS_ACTIVATION_SAFETY_GATE_ACCEPTANCE_20260921.md`.

The zero-science K1B turn3 share/payoff activation contract passed. The exact frozen turn3 share plan is `4C3AB67F1982AEB3B707D07C53BB98C5BA54C835234DFEDE45A96B09BC5E3AB6`; the exact turn3 household payoff is `CEEFE34C16BA0DFDE9FA0C5590DFBB89084475BD88A8496EC18FEEBA7CB674D2`.

Successor:

`tasks/CH5_MP4C_K1B_TURN3_CORRECTED_HOUSEHOLD_KFE_AND_ONE_TURN_INTEGRATION_20260921.md`.
