# Chapter 5 Two-Asset HANK MP4B HANK3_FOC replacement 10-case raw-pb edge-semantics freeze report

Date: 2026-08-31

Terminal verdict:

`MP4B_HANK3_FOC_REPLACEMENT_10CASE_RAW_PB_EDGE_SEMANTICS_FREEZE_BLOCKED`

## Live continuity

- live authority: `1b273a12ae4155373da12e552a0182777e0389e0`;
- direct parent: `2c9f9def61e97c3193008ef081ebad1d173bdfc5`;
- the execution branch was fast-forwarded to live authority with `HEAD == origin/main`, ahead/behind `0/0`, and clean worktree before review;
- the current edge and smoke helpers are byte-identical to the parent PASS commit;
- no historical R5 / `chapter5_model` runtime dependency was found.

## Preserved smoke, helper, and protected identities

- edge helper SHA-256: `33AC7212BF6D3F27A11761B2FD29DB713E63DFDE1356B5002FE5B9ED1166AF69`;
- smoke helper SHA-256: `8F3D7E87CDFA63510505042F938286DC58BAA4F734253C74520AF91742BB601E`;
- preserved smoke manifest: `D:\ProjectTemp\mp4b_hank3_foc_exact_junction_smoke_20260831T121500\path_equivalence_smoke_manifest.json`;
- preserved smoke manifest SHA-256: `A82DC905E7D057EBE0645E3C8F3331F438CF939716762B17AC5C9B270B758D8B`;
- marker: `MP4B_RAW_VB_HANK3_FOC_EXACT_JUNCTION_GUARD_SMOKE_PASS`;
- preserved smoke protected `HANK3_FOC` calls: `0`;
- preserved resolved helper: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK3_FOC.m`;
- logical, physical, and resolved helper SHA-256: `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`;
- `C:\MatlabProgram` independently remained a Junction with exactly one target, `D:\MatlabProgram`.

Protected MATLAB identities also matched:

- `HANK_2ASSETS_HJB.m`: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`;
- `HANK3_FOC.m`: `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`;
- `HANK3_cost.m`: `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`;
- `lab_solve2.m`: `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`.

Production/export identities remained unchanged:

- `economics.py`: `66E3C56F177DB6DAFE7FE0A5FD6DA480D71A7ACC10B5209BC0E3F7360226DC55`;
- `matlab_faithful_policy.py`: `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2`;
- standalone export: `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`.

## Frozen ten-case static review

The current edge helper is textually unchanged from the exact-junction PASS parent. The exact ordered ten ids, `pa`, `pb`, `a`, `chi0`, `chi1`, classification functions, finite `%.17g` encoding, and protected expression

`value = HANK3_FOC(dummy,chi,pa(k),pb(k),a(k),0);`

remain unchanged. No epsilon, clipping, positivity guard, alternate formula, exception-to-number substitution, or extra case was found. The current helpers contain no `canonical_root`, `getCanonicalPath`, `startsWith`, or substring/broad-root matcher. The preserved focused static suite remained `5 passed`.

## Scalar preflight blocker

`MP4B_RAW_VB_HANK3_FOC_REPLACEMENT_SCALAR_PREFLIGHT_PASS` was **not established**.

Independent pre-execution review found four infrastructure/evidence defects in the already smoke-validated edge helper:

1. If protected MATLAB errors on a frozen case, the unhandled error exits the helper before the post-loop manifest is constructed or written. The pre-reserved file remains empty, so the required exact first failing case, identifier, and message cannot be persisted.
2. The per-case row schema does not contain the resolved protected helper path and SHA. Those fields appear only at manifest top level, while this task requires them for every case.
3. The helper's call ledger contains only the scalar batch, `HANK3_FOC`, HJB, KFE, household, and multi-province fields. It does not contain the complete required zero ledger for stationary, all Python scientific routes, 50-state/Beijing parity, MP2/MP3, annual batch, shocks, transition, dynamics, IRF, R5, and Results.
4. Atomic reservation covers only `output_json`. A safe invocation also requires the execution harness to create the exact fresh `D:\ProjectTemp` run root exclusively before MATLAB starts.

The live task explicitly states that a helper implementation defect discovered before execution must terminate BLOCKED and must not be repaired in this task. Therefore no helper modification, MATLAB `checkcode` invocation, scalar root creation, or scalar batch occurred after this blocker was found. The predecessor PASS report already binds `checkcode=0` to the unchanged helper bytes, but that preserved evidence is not promoted into a current scalar preflight PASS.

## Complete execution ledger

- new exact-junction smoke calls: `0`;
- replacement MATLAB scalar batches: `0/1` consumed;
- scalar reruns: `0`;
- protected `HANK3_FOC` calls: `0`;
- MATLAB HJB/KFE/household/multi-province/stationary/GE: all `0`;
- Python local-policy/HJB/KFE/household/stationary: all `0`;
- old 50-state HJB parity / Beijing household parity: `0/0`;
- MP2/MP3 empirical: `0/0`;
- annual batch/shocks/transition/dynamics/IRF/R5/Results: all `0`;
- production/export mutation: `0`.

No fresh scalar root or scalar manifest exists. No ten-case result table exists because the batch was not authorized past preflight. `MP4B_RAW_VB_TRANSFER_FOC_SOURCE_EDGE_SEMANTICS_FROZEN` remains NOT ESTABLISHED.

## No-overwrite, diff, and forbidden-operation checks

- no-overwrite review identified the need for exclusive fresh-root creation before a future invocation; no output path was created in this task;
- helper diff against the exact parent PASS commit: empty;
- working-tree diff before report creation: empty;
- forbidden-operation check: PASS;
- no protected MATLAB, production/export, faithful/corrected/reference, stationary, MP2/MP3, canonical input/cache, R5, or Results path was modified or executed.

## Git closeout

Explicit-path staging is limited to this report. One execution commit, one non-force push, GitHub read-back, `HEAD == origin/main`, ahead/behind `0/0`, and clean worktree are required.

## Exactly one recommended next gate

Publish one infrastructure-remediation task that repairs only the validation edge helper's pre-call evidence contract: exclusive fresh-root creation, durable first-error case capture without numerical substitution, per-row resolved path/SHA fields, and the complete zero-call ledger; then separately reauthorize one replacement ten-case scalar batch with reruns kept at zero.
