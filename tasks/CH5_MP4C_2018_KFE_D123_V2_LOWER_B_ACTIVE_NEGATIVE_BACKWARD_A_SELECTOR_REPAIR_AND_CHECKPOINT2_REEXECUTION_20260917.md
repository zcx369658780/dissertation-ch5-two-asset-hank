# Task — V2 lower-b active negative/backward-a selector repair and checkpoint-2 bounded reexecution

Date: 2026-09-17

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Task ID: `CH5_MP4C_2018_KFE_D123_V2_LOWER_B_ACTIVE_NEGATIVE_BACKWARD_A_SELECTOR_REPAIR_AND_CHECKPOINT2_REEXECUTION_20260917`

## Governance

Owner is final scientific authority. ChatGPT Reviewer has independently accepted the predecessor attribution as an already-authorized selector implementation omission. Codex is bounded Builder.

Never enter, read, search, use or modify `zcx369658780/deep-learning-hank`.

Fresh-fetch live `origin/main`; read `AGENTS.md`, rule index, current status/handoff, predecessor attribution report and acceptance, nonlinear continuation fail-closed acceptance/report, Owner convergence-law adoption, frozen selector/D1/D2/D3/Z/KKT authority, and the accepted V2 artifact/receipt identities.

## Objective

Repair only the corrected diagnostic selector's lower-liquid-boundary active negative-transfer derivative pre-screen so that it uses the correct lower-face multiplier domain and represents the authority-backed negative/backward-`a` case as well as negative/forward-`a`.

Then perform one bounded checkpoint-2 reexecution from the exact accepted V2 field. The purpose is to determine the first scientifically valid post-repair checkpoint-2 state, not to continue the nonlinear trajectory beyond checkpoint 2.

## Frozen identities and law

Accepted V2 SHA-256:
`A85AB791D7CFC3B0BDA52D886418B9552D79824E09EACE6B6E4A4BEC8F950DF1`

Predecessor frozen selector SHA-256:
`C60C584A44A143CB584563ACDAA8F7E30EBC1CA45B90F8AF39728D40AC70E5E6`

Cell100 attribution:
- lower-b active KKT domain is `q_b >= p_b`;
- previous pre-screen incorrectly used `0 < q_b <= p_b` for the active lower-b negative-transfer derivative screen;
- authority-backed active negative/backward-`a` case was omitted;
- this is an implementation coverage defect only, not authority to change equations, KKT laws, transfer laws, root equations, tolerances or numerical method.

Owner nonlinear law remains frozen:
- `B_n <= 1e-8` and `D_n <= 1e-7` at the same checkpoint;
- policy/operator stability diagnostic only;
- direct solve backward error `<=1e-12`;
- exact-cycle plus frozen approximate period-2/3 fail-closed rules;
- `Delta=1000` fixed;
- maximum total HJB updates remains 100, with V0->V1 and V1->V2 already consumed;
- no damping, relaxation, adaptive Delta, continuation, clipping, artificial diffusion, solver substitution, scientific retry or post-hoc tolerance tuning.

## Allowed implementation change

Modify only the corrected diagnostic selector and directly affected focused tests/fixtures/helpers required to implement the accepted lower-b branch-domain correction.

The repair must:
1. use the lower-face active multiplier domain `q_b >= p_b` when screening/representing lower-b active branches;
2. preserve the distinct upper-b domain logic;
3. represent both authority-backed negative-transfer `a` derivative cases when legal by the frozen branch law;
4. preserve zero-kink, positive-transfer, interior-Z and all other accepted semantics exactly;
5. preserve F-order and existing receipt/diagnostic conventions, except for the minimal additional branch evidence needed to make coverage explicit.

Do not modify source-faithful/production selector paths, MATLAB, calibration, data, D2 law, HJB update law, root equation, root tolerance, convergence thresholds, Delta, solver, grid or payoff equations.

## Engineering checks before scientific execution

Run focused static/unit tests covering at minimum:
- active lower-b negative/backward-`a` branch representation;
- active lower-b negative/forward-`a` branch representation;
- no regression to upper-b multiplier-domain behavior;
- cell100-style case census contains the authority-backed eighth case;
- positive active no-root behavior remains a legal rejection rather than being converted into a fabricated root;
- interior-Z remains unavailable on b-boundary nodes;
- existing affected D1/D3/KKT/selector tests continue to pass.

No tolerance weakening or assertion deletion is allowed.

## Scientific execution budget

After all preflight identities and focused tests pass, authorize exactly one fresh checkpoint-2 scientific reexecution from the accepted V2 field.

Maximum budget for this reexecution:
- fresh V2 policy-map attempts: 1;
- selector evaluations: at most 800 cells, stopping at the first fail-closed selector gate;
- scalar-root calls: only those naturally required by that one policy-map attempt under the repaired selector; record exact count;
- interior-Z roots: only those naturally required by that same map; record exact count;
- D2/Q2 assemblies: at most 1, only if the complete 800-cell V2 policy map succeeds;
- checkpoint-2 Bellman/value/stability/cycle diagnostic evaluation: at most 1 complete checkpoint, only if Q2 exists;
- direct HJB solves/updates: 0;
- graph/SCC/topology/KFE/SVD/eigen/nullspace/`Q.T@p`: 0;
- MATLAB/production/outer/firm/wage-return/GE/annual/shock/IRF/Results: 0;
- scientific retries: 0.

A launcher/path/import failure before scientific entry may be corrected within scope, but it must not consume or reset scientific budget. Once the scientific checkpoint-2 attempt begins, no retry is authorized.

## Required behavior

### If the repaired V2 policy map fails
Stop at the first failure. Persist the exact cell receipt and complete ledger. Do not repair a second scientific issue in this task.

### If the repaired V2 policy map completes
Persist complete P2/u2 identity, assemble exactly one Q2 under the frozen D2 law, and compute checkpoint-2:
- Bellman residual `B2`;
- value change `D2 = ||V2-V1||_inf`;
- policy/active-set/control/drift change summaries versus checkpoint 1;
- Q2 structure/numeric identity and `Q2-Q1` norm summary;
- applicable exact/approximate cycle diagnostics under the frozen order.

Evaluate the frozen primary convergence law, but do not execute terminal KFE and do not perform `V2 -> V3`, even if checkpoint 2 is nonconverged. This task stops after the checkpoint-2 classification so the Reviewer can inspect the scientific effect of the selector repair.

If checkpoint 2 satisfies the primary Bellman/value law, report it only as an HJB convergence candidate pending the separate terminal D2/topology/KFE gate; do not run that gate here.

## Evidence and deliverable

Use a fresh no-overwrite evidence root. Persist:
- pre/post scientific-code hashes;
- accepted V2/source/input binding;
- focused test results;
- full repaired checkpoint-2 receipts up to completion/failure;
- Q2 and checkpoint metrics if reached;
- exact call ledger;
- finite manifest/readback evidence;
- changed-file list and Git status.

Write:
`docs/CH5_MP4C_2018_KFE_D123_V2_LOWER_B_ACTIVE_NEGATIVE_BACKWARD_A_SELECTOR_REPAIR_AND_CHECKPOINT2_REEXECUTION_REPORT.md`

Commit and ordinary non-force push one task branch. Do not merge main and do not publish a successor task.

## Terminal classifications

Use the narrowest supported terminal marker, distinguishing at least:
- implementation/preflight failure before scientific run;
- repaired selector still fails checkpoint-2 policy map, with first failing cell;
- repaired V2 map completes and checkpoint-2 is nonconverged;
- repaired V2 map completes and checkpoint-2 is an HJB convergence candidate pending terminal gates.

Results eligibility remains `FALSE`.
