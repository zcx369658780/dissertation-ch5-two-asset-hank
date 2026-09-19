# Task — accepted checkpoint-10 bounded nonlinear continuation through checkpoint 12

Date: 2026-09-20

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:
`CH5_MP4C_2018_KFE_D123_CHECKPOINT10_TO_CHECKPOINT12_BOUNDED_NONLINEAR_CONTINUATION_20260920`

## Governance

Owner is final scientific authority. ChatGPT is L3 independent Reviewer/scientific-route authority. Codex is bounded Builder.

GitHub live `main` is repository-state authority.

Absolute prohibition:

`zcx369658780/deep-learning-hank`

must never be entered, read, searched, used or modified for this dissertation route.

Fresh-fetch live `origin/main`. Read in order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_CHECKPOINT6_TO_CHECKPOINT10_BOUNDED_NONLINEAR_CONTINUATION_ACCEPTANCE_20260920.md`
6. its execution report and accepted checkpoint-10 evidence
7. nonlinear convergence Owner adoption
8. accepted D1/D2/D3 and switching authorities
9. exact accepted checkpoint history needed by cycle tests.

No new scientific law is authorized.

## Objective

Continue the frozen corrected nonlinear HJB trajectory from exact accepted checkpoint 10.

Do not rerun or regenerate accepted V10/P10/u10/Q10 before the first update.

Authorize at most two new updates:

`V10 -> V11 -> V12`.

Stop immediately if checkpoint 11 is terminal. Reach checkpoint 12 only if checkpoint 11 is complete, legal and nonterminal.

## Exact accepted checkpoint 10

V10:

`AE1610BA320F57AF73EE3C5411C298BF00610606B13B5185F2CD65BF1736FB24`.

P10:

`89F79E4C1FC094DBEE8B82CFBAD677276D42839E915426CA0E5565865FBD87A3`.

u10:

`215BEC4AABBC337147D73A227751CD6A89CC483E3CA056470A2AEF161AA41F38`.

Q10 artifact:

`917479763C4690FEAB358098D7F1CE2EBB4DD7C4939A7060156E7A4FCDEE59BD`.

Q10 identity:

- data `B9B180F2ACF9082B5B23C1C52A27652B4FB6CD5215B7DB4816B1102400C720D2`
- indices `9A1E128BD9B13A6711B20FB992699DB405DEF5450543921ACAB69B57FA5474E6`
- indptr `63190CF1D9F4C98D89C81A9990736462F19170B45F97E03AD7B507D492D9C327`.

Checkpoint-10 identity:

`4FC2855AB4102AEAE8B173D0EBBBF40FCD334583A039BE4AE65C8DE2B1145C8D`.

Checkpoint arrays:

`BEA1D08A10C53E4EF3246A413A9446633DAAD6A4ACCAD4E34463BB74756C5512`.

Evidence root:

`reports/ch5_mp4c_2018_kfe_d123_checkpoint6_to_checkpoint10_bounded_nonlinear_continuation_20260919_run001/`

sealed manifest:

`1959B54DB2EC27BA1F12493F71E9E8AAD5F5442D20099D77EC84C0C2AE902EAC`.

Metrics:

- `B10=3.874510913493001e-08`
- `D10=5.8692895192891115e-06`
- primary convergence FAIL
- exact cycle none
- approximate period-2 none
- approximate period-3 none
- D2 PASS.

## Frozen update law

For complete nonconverged checkpoint `n`:

`A_n=((rho+1/Delta)I-Q_n)`

`rhs_n=u_n+V_n/Delta`

solve

`A_n V_(n+1)=rhs_n`.

Frozen:

- `Delta=1000`
- F order
- existing `scipy.sparse.linalg.spsolve`
- direct-solve normwise backward error `<=1e-12`.

Warnings, nonfinite output, shape/order mismatch or failure to evaluate the metric fail closed.

No solver substitution or scientific retry.

## New checkpoint order

For each reached checkpoint `n in {11,12}`:

1. bind exact `V_n`;
2. execute exactly one fresh corrected 800-cell policy map;
3. stop at first selector failure;
4. assemble one Q_n under unchanged D2 only after all cells pass;
5. stop on D2 failure;
6. compute same-value `B_n`;
7. compute `D_n=||vec_F(V_n-V_(n-1))||inf`;
8. persist policy/operator/switching diagnostics;
9. evaluate primary convergence first;
10. if primary fails, evaluate exact cycle;
11. if still nonterminal, evaluate authorized approximate period-2 and period-3 using the complete accepted value history;
12. if checkpoint 11 is still nonterminal, execute exactly one V11->V12 update;
13. if checkpoint 12 is complete and nonterminal, stop boundedly.

## Frozen convergence/cycle law

Primary HJB convergence candidate iff both hold at the same checkpoint:

- `B_n <= 1e-8`
- `D_n <= 1e-7`.

Exact cycle requires full checkpoint identity recurrence at period `k>=2`.

Approximate period 2 requires two consecutive lag-2 vector-infinity comparisons `<=1e-8`.

Approximate period 3 requires three consecutive lag-3 vector-infinity comparisons `<=1e-8`.

Use exactly:

`||vec_F(V_j-V_(j-k))||inf`.

No 2-D/3-D matrix norm substitution.

No trend, spectral, longer-period, fitted or post-hoc rule.

## Accepted history

Cycle history must bind accepted values/identities from earlier complete checkpoints without regenerating prior policy maps or Q objects.

At minimum preserve exact accepted history through checkpoint 10, including the checkpoint identities required to detect exact recurrence and the value fields required for period-2/3 comparisons.

## Scientific budget

Maximum new work:

- direct HJB solves / updates: `2`
- fresh policy maps: `2`
- selector evaluations: `1600`
- D2/Q assemblies: `2`
- complete checkpoint evaluations: `2`
- roots: only natural calls; record exact category counts
- V10 map reruns before first update: `0`
- Q10 reruns: `0`
- topology/KFE/SVD/eigen/nullspace/`Q.T@p`: `0`
- MATLAB/source-faithful/production/outer/firm/GE/annual/shock/IRF/Results: `0`
- scientific retries/solver substitutions/damping/relaxation/adaptive Delta/parameter continuation/clipping/artificial diffusion: `0`.

Global update accounting:

- accepted updates through V10: `10`
- this task may consume updates 11 and 12 only
- Owner global ceiling remains 100.

## Stop conditions

Stop immediately on the first:

- primary HJB convergence candidate;
- exact cycle;
- approximate period-2 cycle;
- approximate period-3 cycle;
- selector/policy-map failure;
- D2 failure;
- direct-solve accuracy/provenance/nonfinite failure;
- complete checkpoint 12.

If convergence occurs, do not execute another HJB update.

If a new selector/scientific issue appears, do not repair it inside this task.

## Terminal KFE prohibition

Do not run terminal topology/KFE/SVD/eigen/nullspace/`Q.T@p` inside this task even if HJB convergence is reached.

Return only:

`HJB_CONVERGENCE_CANDIDATE__TERMINAL_GATE_NOT_RUN`.

## Deliverable

Write:

`docs/CH5_MP4C_2018_KFE_D123_CHECKPOINT10_TO_CHECKPOINT12_BOUNDED_NONLINEAR_CONTINUATION_REPORT.md`

Use a fresh no-overwrite evidence root.

Persist:

- accepted checkpoint-10 binding;
- exact history binding;
- direct-solve receipts;
- every new cell receipt;
- D2/Q receipts;
- B/D and policy/operator/switching diagnostics;
- cycle receipts;
- scientific ledger;
- pre/post scientific-code hashes;
- sealed manifest and readback;
- changed-file list and final Git status.

Commit and ordinary non-force push one task branch.

Do not merge main.
Do not publish successor.
Do not modify CURRENT files.

Results eligibility remains `FALSE`.
