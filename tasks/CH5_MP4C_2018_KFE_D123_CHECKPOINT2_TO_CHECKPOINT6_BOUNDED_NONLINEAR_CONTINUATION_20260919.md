# Task — accepted checkpoint-2 bounded nonlinear continuation through checkpoint 6

Date: 2026-09-19

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:
`CH5_MP4C_2018_KFE_D123_CHECKPOINT2_TO_CHECKPOINT6_BOUNDED_NONLINEAR_CONTINUATION_20260919`

## Governance

Owner is final scientific authority. ChatGPT is L3 Reviewer/scientific-route authority. Codex is bounded Builder.

Never enter, read, search, use or modify:
`zcx369658780/deep-learning-hank`.

Fresh-fetch live `origin/main`. Read in order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_IMPLEMENTATION_AND_V2_CHECKPOINT2_REEXECUTION_ACCEPTANCE_20260919.md`
6. its execution report and accepted checkpoint-2 evidence
7. `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_CONVERGENCE_LAW_OWNER_ADOPTION_20260917.md`
8. Owner-adopted liquid-`Z`, interior-`a`, joint-switching, lower-`a` zero-kink and D1/D2/D3 authorities
9. exact accepted V0/V1/Q1 and V2/P2/u2/Q2 identities required for cycle and continuation binding.

No new scientific law is authorized by this task.

## Objective

Continue the corrected nonlinear HJB trajectory from the exact accepted complete checkpoint 2 using the frozen Owner nonlinear law.

Do **not** rerun or regenerate the accepted V2 policy map or Q2 before the first update. Bind and reuse accepted `V2/P2/u2/Q2` exactly.

Authorize at most four new direct updates:

`V2 -> V3 -> V4 -> V5 -> V6`.

After each passing direct update, construct exactly one fresh same-value policy map and D2 operator for the new checkpoint, evaluate convergence/cycle gates in the frozen order, and stop immediately if any terminal condition is reached.

The task ends no later than complete checkpoint 6.

## Frozen accepted checkpoint 2

Accepted V2 SHA-256:

`A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`.

Accepted P2 identity:

`EBCBABC0593EF163D2E7FA300F6FFEB6E3C187D232D4CCEA5D59AB7180CD1D95`.

Accepted u2 SHA-256:

`C222F4B147F48EA177A28AAF289F3ED5EA76F531BC08201070DD63698BF98D73`.

Accepted Q2 artifact SHA-256:

`346DBCDA13392DAF6897DC185767B0E7C5961AA76A9AAA686053AEDA33C02F9F`.

Accepted Q2 identity:

- data `3278FFDA5ABA29E8C8E7ECC84649DF7A787AD7BDA5E936657F585B65A9844BEB`
- indices `6FF05054740279B563416E942AFEC958804FBD1AF63C660C9877D3175FB5B066`
- indptr `180A552000B935F15F1934266DE86FF9E3D7550005366AB92B312793648F0200`.

Accepted checkpoint-2 identity:

`71DC6975E814060A4F63961A736E6E9DDF766C51CE4672C3EF777E5E15B80C2C`.

Accepted checkpoint-2 arrays artifact SHA-256:

`F55C1A37BF16720AA1BC61DC4BA42A410BD9DCA5399A2C38EC19D2AE295B8612`.

Accepted evidence root:

`reports/ch5_mp4c_2018_kfe_d123_simultaneous_two_axis_zero_drift_switching_implementation_v2_checkpoint2_reexecution_20260919_run001/`

Accepted sealed-manifest SHA-256:

`B3CC70792E41E0EBDDE138057406C86D07063AD44959B595FA1B503B9D5AE2EA`.

Accepted checkpoint-2 metrics:

- `B2=0.006582827785543588`
- `D2=0.05439336697877817`
- primary convergence: FAIL
- exact cycle: none
- approximate period-2/3 windows: unavailable.

## Frozen update equation and accuracy gate

For each complete nonconverged checkpoint `n`, use exactly:

`A_n=((rho+1/Delta)I-Q_n)`

`rhs_n=u_n+V_n/Delta`

and solve:

`A_n V_(n+1)=rhs_n`

with F-order conventions and fixed:

`Delta=1000`.

Use the existing `scipy.sparse.linalg.spsolve` path only.

Every direct solve must persist the original-equation residual and normwise backward error.

Accept a solve only if:

`normwise_backward_error <= 1e-12`.

Warnings, nonfinite output, shape/order mismatch, metric inability, or backward error above the bound fail closed.

No solver substitution or scientific retry.

## Frozen checkpoint order

For every new checkpoint `n in {3,4,5,6}` that is reached:

1. bind exact `V_n`;
2. execute exactly one fresh corrected policy map from `V_n`;
3. if any selector fails, persist first failure and stop;
4. after all 800 cells pass, assemble exactly one `Q_n` using unchanged D2;
5. if D2 fails, persist and stop;
6. compute same-value Bellman residual
   `B_n=||rho V_n-u_n-Q_n V_n||_inf`;
7. compute `D_n=||V_n-V_(n-1)||_inf`;
8. record policy/operator changes relative to checkpoint `n-1`;
9. evaluate primary convergence **first**:
   - `B_n<=1e-8`
   - `D_n<=1e-7`
   - both required, inclusive;
10. only if primary convergence fails, evaluate exact-cycle rule;
11. only if still nonterminal, evaluate authorized approximate period-2/3 cycle rules where a complete window exists;
12. only if still nonterminal and `n<6`, execute one direct update to `V_(n+1)`;
13. if `n=6` remains nonconverged/noncycle, stop as bounded continuation evidence and return to Reviewer.

Policy/operator stability is diagnostic only.

## Cycle rules

Use the already adopted rules without modification.

### Exact

A nonconverged complete checkpoint is an exact-cycle stop only if its full checkpoint identity exactly repeats an earlier complete nonlinear checkpoint at period `k>=2`.

Do not treat period-1 identity as automatic cycle failure.

### Approximate period 2

Requires two consecutive lag-2 value comparisons, each:

`||V_j-V_(j-2)||_inf<=1e-8`.

The earliest complete period-2 window is available at checkpoint 4.

### Approximate period 3

Requires three consecutive lag-3 value comparisons, each:

`||V_j-V_(j-3)||_inf<=1e-8`.

The earliest complete period-3 window is available at checkpoint 6.

No longer-period or heuristic cycle rule is authorized.

## Preserved scientific law

Do not modify:

- D1/D2/D3;
- ordinary upwinding;
- liquid-`Z`;
- one-axis interior-`a` switching;
- simultaneous joint switching;
- lower-`a` zero-kink;
- root solver/tolerance;
- grid/calibration/payoffs;
- `Delta`;
- Bellman/value thresholds;
- cycle tolerance/window definition;
- direct HJB equation;
- terminal KFE law.

No damping, relaxation, adaptive Delta, continuation in parameters, clipping, artificial diffusion, or post-hoc tolerance tuning.

## Engineering/preflight

A bounded continuation driver/helper may be added or minimally adapted to bind accepted checkpoint 2 and persist checkpoints 3-6.

Before scientific entry:

- verify live-main/candidate source identities;
- verify accepted V0/V1/V2 and P1/Q1/P2/u2/Q2 identities;
- verify accepted checkpoint-2 sealed manifest/readback;
- verify current selector/generator scientific-code identities;
- run focused continuation + selector/D1/D2/D3/switching tests;
- `py_compile`/compile gate;
- `git diff --check`;
- freeze scientific-code hashes.

No tolerance weakening or assertion deletion.

A launcher/import/path failure before scientific entry may be corrected within scope and preserved as pre-science evidence. It does not consume a scientific attempt.

## Scientific budget

Cumulative maximum for this task:

- new direct HJB solves/updates: `4`
- new policy maps: `4`
- new selector evaluations: `3200`
- D2/Q assemblies: `4`
- complete checkpoint diagnostic evaluations: `4`
- scalar/liquid-Z/interior-a/joint roots: only those naturally required by the authorized maps; record exact category counts
- graph/SCC/topology/KFE/SVD/eigen/nullspace/`Q.T@p`: `0`
- MATLAB/source-faithful/production/outer/firm/wage-return/GE/annual/shock/IRF/Results: `0`
- scientific retries: `0`
- solver substitutions/damping/relaxation/adaptive Delta/parameter continuation/clipping/artificial diffusion: `0`.

Global nonlinear update accounting:

- accepted `V0->V1`: update 1
- accepted `V1->V2`: update 2
- this task may consume updates 3 through 6 only
- the Owner global ceiling remains 100 total updates.

## Stop conditions

Stop immediately and do not spend unused budget after the first:

- policy-map/selector fail-closed cell;
- D2 legality failure;
- direct-solve accuracy failure;
- nonfinite/provenance/shape/order failure;
- primary HJB convergence candidate;
- exact cycle;
- approximate period-2 cycle;
- approximate period-3 cycle;
- complete checkpoint 6 without convergence/cycle.

If a new scientific selector issue appears, do not repair it inside this task.

## Terminal KFE prohibition

Even if a checkpoint satisfies primary HJB convergence, do not run terminal topology/KFE/SVD in this task.

Report only:

`HJB_CONVERGENCE_CANDIDATE__TERMINAL_GATE_NOT_RUN`.

Reviewer will inspect the trajectory and publish the separate terminal gate if appropriate.

## Evidence and deliverable

Use a fresh no-overwrite evidence root.

Persist per checkpoint:

- value identity;
- complete cell receipts;
- policy/u/Q identities;
- D2 receipt;
- B/D metrics;
- policy/operator changes;
- switching statistics;
- cycle receipt;
- direct-solve receipt if continuation occurs;
- scientific ledger snapshots.

Persist cumulative:

- pre/post scientific-code hashes;
- accepted checkpoint-2 binding;
- exact cumulative call ledger;
- sealed manifest/readback;
- changed-file list and final Git status.

Write:

`docs/CH5_MP4C_2018_KFE_D123_CHECKPOINT2_TO_CHECKPOINT6_BOUNDED_NONLINEAR_CONTINUATION_REPORT.md`

Commit and ordinary non-force push one task branch.

Do not merge main.
Do not publish a successor task.
Do not modify CURRENT files.

Results eligibility remains `FALSE`.
