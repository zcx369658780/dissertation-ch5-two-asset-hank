# Task — accepted checkpoint-3 bounded nonlinear continuation through checkpoint 6

Date: 2026-09-19

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:
`CH5_MP4C_2018_KFE_D123_CHECKPOINT3_TO_CHECKPOINT6_BOUNDED_NONLINEAR_CONTINUATION_20260919`

## Governance

Owner is final scientific authority. ChatGPT is L3 Reviewer/scientific-route authority. Codex is bounded Builder.

Never enter, read, search, use or modify:
`zcx369658780/deep-learning-hank`.

Fresh-fetch live `origin/main`. Read in order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_V3_CELL100_LOWER_B_NEGATIVE_FORWARD_A_PRE_SCREEN_REPAIR_AND_CHECKPOINT3_REEXECUTION_ACCEPTANCE_20260919.md`
6. its execution report and accepted checkpoint-3 evidence
7. `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_CONVERGENCE_LAW_OWNER_ADOPTION_20260917.md`
8. all adopted D1/D2/D3 and switching authorities
9. exact accepted checkpoint-1/2/3 identities needed for cycle detection.

No new scientific law is authorized.

## Objective

Continue the corrected nonlinear HJB trajectory from exact accepted checkpoint 3.

Do **not** rerun or regenerate accepted V3/P3/u3/Q3 before the first update.

Authorize at most three new direct updates:

`V3 -> V4 -> V5 -> V6`.

For each reached new checkpoint, create exactly one same-value policy map and D2/Q object, evaluate the frozen convergence/cycle rules, and stop immediately on the first terminal condition.

## Frozen checkpoint 3

V3 SHA-256:

`4FDB36C17ACDC60B56661AEE1C0437B65EC4A871FD4E5E08A9A996FB10EF85EF`.

P3 identity:

`06062946687922E1FAC83E8D4B1B19101469CC284339522595A19F4DECB6B07B`.

u3 SHA-256:

`9BB321A63A92154D4B733B28126AF29DC1441B95D44517D884F4C858AECFE6F4`.

Q3 artifact:

`4085E0D1B166E72650CA1E74E5CF9462F6677EEAFA8CDEF1FBD153F14088C255`.

Q3 identity:

- data `13CA224BF05EADD453078A6A6A54A87EADC0C76C4753A0577703298C1767A521`
- indices `AFB69E0EF55C1E8CEBAF4040485297B8CAE211F85451AC4B89E9B27CED97FBD0`
- indptr `BC95DE3B2915B44B63AEC514B67F12005964891E1E78AAB43C6FD38370ABA495`.

Checkpoint-3 identity:

`0DEEF7E54C4972BFF7BB67AE6B67BA5E54B588F3EEF5ACDE85048F3E02FE715D`.

Checkpoint-3 arrays:

`B4024EC1202533982BAF9C893F946D20B871B76B3BD369DD4F19B34BF1DD99BD`.

Evidence root:

`reports/ch5_mp4c_2018_kfe_d123_v3_cell100_lower_b_negative_forward_a_prescreen_repair_checkpoint3_reexecution_20260919_run001/`

sealed manifest:

`01FB50C300936B76F7C56CBD0BBFDF8A91ABFDDF5180FE5AB77FA7341DD8D1F6`.

Metrics:

- `B3=0.1291770476282596`
- `D3=0.05315900863346279`
- primary convergence FAIL
- exact cycle none
- approximate period-2/3 windows unavailable at checkpoint 3.

Do not add a trend-based stop because `B3>B2`; no such rule is adopted.

## Frozen update equation

For nonconverged checkpoint `n`:

`A_n=((rho+1/Delta)I-Q_n)`

`rhs_n=u_n+V_n/Delta`

solve:

`A_n V_(n+1)=rhs_n`

with:

- `Delta=1000`
- existing F order
- existing `scipy.sparse.linalg.spsolve`
- normwise backward error `<=1e-12`.

No solver substitution/retry.

## Per-checkpoint order

For each new checkpoint `n in {4,5,6}`:

1. bind exact `V_n`;
2. one fresh 800-cell corrected policy map;
3. stop at first selector fail;
4. after complete map, assemble one Q_n using unchanged D2;
5. stop on D2 failure;
6. compute same-value `B_n`;
7. compute `D_n=||V_n-V_(n-1)||inf`;
8. persist policy/operator/switching diagnostics;
9. evaluate primary convergence first;
10. if failed, evaluate exact cycle;
11. if still nonterminal, evaluate approximate period-2/3 only when complete windows exist;
12. if still nonterminal and `n<6`, perform one direct update;
13. if checkpoint 6 is complete and nonterminal, stop boundedly and return to Reviewer.

## Frozen convergence/cycle rules

Primary convergence iff both:

- `B_n<=1e-8`
- `D_n<=1e-7`.

Exact cycle requires full checkpoint identity recurrence at period `k>=2`.

Approximate period-2 requires the two most recent lag-2 comparisons both `<=1e-8`; this can first be fully evaluated at checkpoint 4 using the accepted history through V1-V4.

Approximate period-3 requires three lag-3 comparisons all `<=1e-8`; this can first be fully evaluated at checkpoint 6.

No trend heuristic, longer-period heuristic, spectral heuristic, damping, relaxation, adaptive Delta, parameter continuation, clipping or artificial diffusion.

## Binding and history

Cycle history must include the exact accepted prior checkpoints and value fields needed by the adopted rule, including accepted V1, V2 and V3 plus accepted checkpoint identities where available.

Do not regenerate accepted prior policy maps or Q operators.

## Scientific budget

Maximum:

- direct HJB solves / new updates: `3`
- fresh policy maps: `3`
- selector evaluations: `2400`
- D2/Q assemblies: `3`
- complete checkpoint evaluations: `3`
- roots: natural calls only; persist exact category counts
- V3 policy-map reruns before first update: `0`
- Q3 reruns: `0`
- topology/KFE/SVD/eigen/nullspace/`Q.T@p`: `0`
- MATLAB/source-faithful/production/outer/firm/GE/annual/shock/IRF/Results: `0`
- scientific retries and solver substitutions: `0`.

Global update accounting:

- V0->V1 = update 1
- V1->V2 = update 2
- V2->V3 = update 3
- this task may consume updates 4-6
- global ceiling remains 100.

## Stop conditions

Stop immediately on:

- first policy-map failure;
- D2 failure;
- direct-solve accuracy/provenance/nonfinite failure;
- primary convergence;
- exact cycle;
- approximate period-2/3 cycle;
- complete checkpoint 6.

Do not repair a newly exposed selector/scientific issue in the same task.

## Terminal KFE prohibition

Even if HJB convergence is reached, do not run terminal topology/KFE/SVD here.

Return only an HJB convergence candidate for Reviewer inspection.

## Deliverable

Write:

`docs/CH5_MP4C_2018_KFE_D123_CHECKPOINT3_TO_CHECKPOINT6_BOUNDED_NONLINEAR_CONTINUATION_REPORT.md`

Use a fresh no-overwrite evidence root and persist per-checkpoint receipts, direct-solve receipts, full ledger and sealed manifest/readback.

Commit and ordinary non-force push one task branch.

Do not merge main.
Do not publish successor.
Do not modify CURRENT files.

Results eligibility remains `FALSE`.
