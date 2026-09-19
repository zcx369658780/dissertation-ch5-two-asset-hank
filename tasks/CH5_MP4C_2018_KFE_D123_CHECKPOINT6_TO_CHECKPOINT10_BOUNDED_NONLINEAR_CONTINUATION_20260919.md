# Task — accepted checkpoint-6 bounded nonlinear continuation through checkpoint 10

Date: 2026-09-19

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Task ID:
`CH5_MP4C_2018_KFE_D123_CHECKPOINT6_TO_CHECKPOINT10_BOUNDED_NONLINEAR_CONTINUATION_20260919`

## Governance

Owner is final scientific authority. ChatGPT is L3 Reviewer/scientific-route authority. Codex is bounded Builder.

Never enter, read, search, use or modify:
`zcx369658780/deep-learning-hank`.

Fresh-fetch live `origin/main`. Read in order:

1. `AGENTS.md`
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`
5. `docs/CH5_MP4C_2018_KFE_D123_CHECKPOINT3_TO_CHECKPOINT6_BOUNDED_NONLINEAR_CONTINUATION_ACCEPTANCE_20260919.md`
6. its execution report and accepted checkpoint-4/5/6 evidence
7. `docs/CH5_MP4C_2018_KFE_D123_NONLINEAR_CONVERGENCE_LAW_OWNER_ADOPTION_20260917.md`
8. all adopted D1/D2/D3 and switching authorities
9. exact accepted checkpoint history needed for cycle detection.

No new scientific law is authorized.

## Objective

Continue the corrected nonlinear HJB trajectory from exact accepted checkpoint 6.

Do **not** rerun or regenerate accepted V6/P6/u6/Q6 before the first update.

Authorize at most four new direct updates:

`V6 -> V7 -> V8 -> V9 -> V10`.

At each reached checkpoint, execute exactly one same-value policy map, one D2/Q assembly after map completion, and one convergence/cycle evaluation. Stop immediately on the first terminal gate.

## Exact checkpoint-6 binding

V6:

`69865ACDD71A26A3E3F4A8DAD55C964F826D34C774C9B8193FE997973EE6D89F`.

P6:

`63026FBE8BE72E3B29B5FC44EBD100C01C146179D05B55C779E9E232AEA435A3`.

u6:

`09D5A6622535709146751865931109F058FED3688FAE755C5EF9A0E00AD8B89E`.

Q6 artifact:

`039734AF0BC38AD3BD0FF38854CBE8B4B0B93BA415EC2A47B1C09F827EA7F454`.

Q6 identity:

- data `CE091A208909AEA1D71637DD269FF5D98A59CE5785F90870212D453F86DBFDC9`
- indices `B44ED2AC2E4E86E01B040089645FE66EEC5CFB7874E6DCDA6A307803632B70E4`
- indptr `DC38CF83DFC0A6F522020AC8DBC16EDBEB4E1D273A59EDCA6697CD721E3593F2`.

Checkpoint-6 identity:

`B26177C216DA6902226BD93E802A2B1FE0E794B29BE14EA1A1BCBFFD8F8691A1`.

Checkpoint-6 arrays:

`C703E99742D87565D3FB15EDE4091B265EF36B47D6109DA44052B5290DC4F98D`.

Accepted continuation evidence root:

`reports/ch5_mp4c_2018_kfe_d123_checkpoint3_to_checkpoint6_bounded_nonlinear_continuation_20260919_resume001/`

sealed manifest:

`1BFAB497357EE2740B259E23AD970EEB927799D9FD37A60A7D30E544E1970725`.

Checkpoint-6 metrics:

- `B6=0.005940678766947715`
- `D6=0.010000685482095761`
- primary convergence FAIL
- exact cycle none
- approximate period-2 none
- approximate period-3 none.

## Accepted trajectory history

For exact and approximate cycle detection, bind the exact accepted prior values and checkpoint identities; do not regenerate their policy maps or Q matrices.

Relevant recent history:

- checkpoint 3 identity `0DEEF7E54C4972BFF7BB67AE6B67BA5E54B588F3EEF5ACDE85048F3E02FE715D`
- checkpoint 4 identity `69BA60083B3D96CDCFF1BE935AC425C04F68DF44A9FDB545209FA4280742F420`
- checkpoint 5 identity `1CACE68D0BD30F24F16FB032ECCB6BCA2B2F939AF3A6B4556098DB1CBF577080`
- checkpoint 6 identity `B26177C216DA6902226BD93E802A2B1FE0E794B29BE14EA1A1BCBFFD8F8691A1`.

Also bind accepted V1/V2 and their checkpoint identities as required by the exact-cycle history.

## Frozen update equation

For each complete nonconverged checkpoint `n`:

`A_n=((rho+1/Delta)I-Q_n)`

`rhs_n=u_n+V_n/Delta`

solve

`A_n V_(n+1)=rhs_n`

with:

- `Delta=1000`
- F order
- existing `scipy.sparse.linalg.spsolve`
- normwise backward error `<=1e-12`.

Warnings, nonfinite output, shape/order mismatch or backward error above the bound fail closed.

No solver substitution or scientific retry.

## Per-checkpoint order

For each new checkpoint `n in {7,8,9,10}`:

1. bind exact `V_n`;
2. execute one fresh corrected policy map;
3. stop at the first selector failure;
4. after 800/800 pass, assemble exactly one Q_n under unchanged D2;
5. stop on D2 failure;
6. compute same-value `B_n`;
7. compute `D_n=||vec_F(V_n-V_(n-1))||inf`;
8. record policy/operator/switching diagnostics;
9. evaluate primary convergence first;
10. if nonconverged, evaluate exact cycle;
11. if still nonterminal, evaluate the authorized approximate period-2 and period-3 rules using the full accepted recent value history;
12. only if still nonterminal and `n<10`, perform one direct update;
13. if checkpoint 10 is complete and nonterminal, stop boundedly.

## Frozen convergence and cycle law

Primary convergence requires both, inclusively:

- `B_n<=1e-8`
- `D_n<=1e-7`.

Exact cycle requires exact recurrence of the full checkpoint identity at period `k>=2`.

Approximate period 2 requires two consecutive lag-2 value comparisons, each `<=1e-8`.

Approximate period 3 requires three consecutive lag-3 value comparisons, each `<=1e-8`.

Use the corrected vector infinity norm exactly as:

`||vec_F(V_j-V_(j-k))||inf`.

No matrix/3-D norm substitution is permitted.

No trend, spectral, longer-period or fitted heuristic may be introduced.

## Preserved law

Do not modify:

- D1/D2/D3;
- ordinary upwinding;
- lower-b branch coverage;
- liquid-Z;
- one-axis interior-a switching;
- simultaneous joint switching;
- lower-a zero-kink;
- grid/calibration/payoffs;
- root routine/tolerances;
- `Delta=1000`;
- primary convergence thresholds;
- cycle periods/windows/tolerance;
- direct HJB equation;
- terminal KFE law.

No damping, relaxation, adaptive Delta, parameter continuation, clipping or artificial diffusion.

## Engineering/preflight

A new bounded driver may bind accepted checkpoint 6 and the historical values/identities.

Before scientific entry:

- verify live-main identity;
- verify accepted checkpoint-6 sealed manifest and every required file readback;
- verify exact V6/P6/u6/Q6/checkpoint-6 identities;
- verify exact prior V/checkpoint history used for cycle tests;
- run focused continuation/cycle/selector/D1/D2/D3/switching tests;
- test vector-infinity cycle calculation on multidimensional F-order arrays;
- `py_compile`;
- `git diff --check`;
- freeze scientific-code hashes.

A launcher/import/path failure before scientific entry may be corrected and persisted as zero-science evidence.

After scientific entry, a representation-only software exception may not be silently retried. Stop and preserve the immutable prefix; any resume requires explicit evidence that no scientific object is recomputed and no scientific law changes.

## Scientific budget

Maximum new work:

- direct HJB solves / updates: `4`
- fresh policy maps: `4`
- selector evaluations: `3200`
- D2/Q assemblies: `4`
- complete checkpoint evaluations: `4`
- roots: natural calls only, exact category counts required
- V6 policy-map reruns before first update: `0`
- Q6 reruns: `0`
- topology/KFE/SVD/eigen/nullspace/`Q.T@p`: `0`
- MATLAB/source-faithful/production/outer/firm/GE/annual/shock/IRF/Results: `0`
- scientific retries/solver substitutions: `0`.

Global update accounting:

- accepted updates through V6: `6`
- this task may consume updates `7-10`
- Owner global ceiling remains `100`.

## Stop conditions

Stop immediately on:

- policy-map/selector failure;
- D2 failure;
- direct-solve accuracy/provenance/nonfinite failure;
- primary HJB convergence;
- exact cycle;
- approximate period-2 cycle;
- approximate period-3 cycle;
- complete checkpoint 10.

Do not repair any new scientific selector issue inside the task.

## Terminal KFE prohibition

Even if primary HJB convergence is reached, do not execute terminal topology/KFE/SVD in this task.

Return only:

`HJB_CONVERGENCE_CANDIDATE__TERMINAL_GATE_NOT_RUN`.

## Deliverable

Write:

`docs/CH5_MP4C_2018_KFE_D123_CHECKPOINT6_TO_CHECKPOINT10_BOUNDED_NONLINEAR_CONTINUATION_REPORT.md`

Use a fresh no-overwrite evidence root. Persist per-checkpoint map/Q/metrics/cycle/direct-solve receipts and cumulative ledger, plus sealed manifest/readback.

Commit and ordinary non-force push one task branch.

Do not merge main.
Do not publish successor.
Do not modify CURRENT files.

Results eligibility remains `FALSE`.
