# Task — run004 canonical same-S raw-next-payoff repair and integration-only replay

Date: 2026-09-20

Repository:

`zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:

`CH5_MP4C_RUN004_CANONICAL_SAME_S_RAW_NEXT_PAYOFF_REPAIR_AND_INTEGRATION_ONLY_REPLAY_20260920`

Status: `ACTIVE`

## Governance

Owner is final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

GitHub live main is repository-state authority.

Absolute prohibition: never enter, read, search, use or modify `zcx369658780/deep-learning-hank`.

Fresh-fetch live main and read:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_RUN004_31PROVINCE_HOUSEHOLD_KFE_PASS_RAW_NEXT_PAYOFF_REDUCTION_ORDER_GUARD_ACCEPTANCE_20260920.md`
6. `docs/CH5_MP4C_UNIQUE_CLOSED_CLASS_SUPPORT_KFE_OWNER_ADOPTION_20260920.md`
7. run004 report, household-batch receipt, sealed manifest and per-province aggregate/terminal receipts
8. accepted K1A/C1/raw-ra0 payoff authorities.

No new economic law is authorized.

## Objective

Close the already-computed corrected initial turn without rerunning household HJB/KFE science.

The task has two stages:

1. zero-science repair and binding of the accepted run004 household batch;
2. exactly one integration-only replay from that accepted batch using the canonical same-S raw-next-payoff reduction.

Do not rerun any household HJB/KFE or corrected aggregate evaluation.

## Exact accepted household authority

Bind run004 evidence root:

`reports/ch5_mp4c_corrected_optionb_initial_turn_unique_closed_class_kfe_20260920_run004/`

Require sealed manifest SHA-256:

`CF70E7D6A62A35F461D1A75B28F8F502B2CBDD2D94ED5D9DDFA099D821CC5EC6`.

Require:

- 31 `province_terminal_receipt.json` objects;
- 31 `stationary_aggregate_receipt.json` objects;
- `household_batch_receipt.json`;
- household batch province_count = 31;
- household batch identity:
  `8B7875F3BD603038E4D415D9F9FF759D4FDDC93E2E677C13BF0B649571B2EB05`.

Reconstruct one `PreFrozenHouseholdOutputBatch` from the persisted per-province aggregate receipts in exact province order.

Recompute only the deterministic batch identity hash and require exact equality to the accepted batch identity.

This batch reconstruction is evidence loading, not household science.

Forbidden household calls in this task:

- source-native initialization: 0
- selector/root: 0
- D2/Q: 0
- HJB/direct solve: 0
- SCC/topology: 0
- restricted GESVD: 0
- full-space GESVD: 0
- stationary candidate construction: 0
- `Q.T@p`: 0
- corrected aggregate evaluation: 0.

## Canonical same-S numerical repair

The economic law remains:

`rah_i = sum_j S[j,i] * raw_ra0_j`.

Implement the canonical evaluator as:

`math.fsum(float(raw_ra0[j]) * float(S[j,i]) for j in range(31))`

for each origin `i=0..30`, with destination index `j=0..30` in ascending order.

Requirements:

- use the exact raw firm `ra0` vector;
- use the exact K1A `portfolio_shares_destination_origin` matrix used in the same replay's quantity allocation;
- no copy with changed orientation;
- no clipped firm `ra`;
- no annualization/rescaling/smoothing/risk adjustment/z-score;
- no tolerance-based acceptance of the canonical identity;
- no scientific retry.

Persist before any acceptance check:

- raw-ra0 vector and SHA-256;
- S matrix and CSR/array identity as appropriate;
- orientation = `destination_by_origin`;
- ordered 31x31 product-term array/hash;
- canonical fsum payoff vector and SHA-256;
- BLAS `raw_ra0 @ S` diagnostic vector;
- max absolute canonical-vs-BLAS difference;
- bitwise-equal count;
- ULP-distance summary if implemented deterministically.

The BLAS comparison is diagnostic only and is not an acceptance gate.

Same-S acceptance is based on exact provenance of the raw vector and S plus deterministic canonical term construction.

## Zero-science engineering gate

Before the one integration replay:

- focused synthetic test proving two mathematically identical reduction orders can differ bitwise;
- focused test of the canonical fsum evaluator against an explicit scalar-loop term list;
- test that transposition/orientation mistakes fail provenance/orientation checks;
- test that clipped/alternate return input is not accepted as raw-ra0;
- test accepted run004 household-batch reconstruction and identity;
- `py_compile` PASS;
- `git diff --check` PASS;
- exact predecessor manifest/readback binding PASS;
- code freeze PASS.

Engineering test retries before integration are allowed.

## Integration-only replay

Using only the accepted reconstructed household batch and the original accepted outer-turn-1 state inputs, execute exactly once:

- source-faithful labor reconstruction: 1
- K1A allocation: 1 with `beta_distance=2`, `beta_return=0`
- C1 residual GovInv construction: 1
- firm evaluations: 31
- composite wage batch: 1
- monetary assignment: 1
- fiscal diagnostic batch: 1
- canonical raw-next-payoff construction: 1.

No household or aggregate science is rerun.

## Integration accounting gates

After canonical raw-next-payoff has been persisted, validate all integration identities:

- source update order;
- K1A share columns;
- origin private-wealth / national private-capital conservation;
- home retained capital;
- C1 `GovInv=max(Ktarget-Kprivate,0)`;
- firm K accounting;
- all firm outputs finite;
- raw-ra0 vector finite;
- same exact S used for quantity and payoff;
- canonical raw-next-payoff finite;
- no forbidden payoff transformation.

Persist:

- source-faithful labor receipt;
- K1A S and capital-accounting receipt;
- C1 receipt;
- 31 firm diagnostics including K/Y/wage/raw-ra0/used-ra;
- wage/monetary/fiscal receipts;
- canonical raw-next-payoff receipt;
- next-state candidate receipt.

## Scientific budget

Integration-only scientific calls:

- household batch reconstruction from evidence: 1
- source-faithful labor: 1
- K1A: 1
- C1: 1
- firms: 31
- composite wage: 1
- monetary: 1
- fiscal: 1
- canonical raw-next-payoff: 1.

Forbidden:

- household initialization/HJB/KFE/aggregate calls: 0
- second integration replay: 0
- turn2 household: 0
- second outer turn: 0
- K1B: 0
- K2: 0
- adaptive controller: 0
- MATLAB: 0
- GE/annual/shock/IRF/welfare/Results: 0
- scientific retries: 0.

## Evidence

Create fresh evidence root:

`reports/ch5_mp4c_run004_canonical_same_s_integration_replay_20260920_run001/`

Do not modify run004 evidence.

Write:

`docs/CH5_MP4C_RUN004_CANONICAL_SAME_S_RAW_NEXT_PAYOFF_REPAIR_AND_INTEGRATION_ONLY_REPLAY_REPORT.md`.

Persist:

- authority binding;
- run004 household-batch binding;
- zero-science repair contract/tests;
- pre/post code freeze;
- all integration receipts;
- canonical-vs-BLAS diagnostic;
- integration-only scientific ledger;
- terminal receipt;
- sealed manifest and independent readback.

## Terminal marker

If all accounting gates pass:

`PASS__RUN004_ACCEPTED_31_PROVINCE_HOUSEHOLD_KFE__CANONICAL_SAME_S_INTEGRATION_REPLAY_PASS__RAW_NEXT_PAYOFF_READY__TURN2_NOT_RUN`

A PASS closes exactly one corrected initial multi-province turn under the Owner-adopted unique-closed-class KFE and produces the accepted raw next-payoff vector for a future separately authorized turn-2 task.

It does not establish outer convergence, K1B, GE or Results.

## Git workflow

- isolated branch
- explicit staging only
- ordinary non-force push
- remote SHA/tree readback
- clean worktree
- do not modify CURRENT files
- do not merge main
- do not publish successor.
