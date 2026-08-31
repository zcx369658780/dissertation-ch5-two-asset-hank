# Chapter 5 Two-Asset HANK MP4B exact-junction guard repair and replacement smoke-only report

Date: 2026-08-31

Terminal verdict:

`MP4B_HANK3_FOC_EXACT_JUNCTION_GUARD_REPAIR_AND_REPLACEMENT_SMOKE_PASS`

## Live authority and continuity

- repository: `zcx369658780/dissertation-ch5-two-asset-hank`;
- live authority: `8228e289b19592be1b1caa5e2599430ab36ada51`;
- direct parent: `09631a581611cc2b209b1bf8dd676299f82f327b`;
- execution branch was fast-forwarded to the live authority with `HEAD == origin/main`, ahead/behind `0/0`, and clean worktree before mutation;
- predecessor BLOCKED report and both active raw-`Vb` helpers existed;
- no active historical R5 / `chapter5_model` runtime dependency was found.

## Protected identities

The exact `C:\MatlabProgram` logical entry was independently observed as `LinkType=Junction` with exactly one target, `D:\MatlabProgram`.

Protected MATLAB SHA-256 values:

- `HANK_2ASSETS_HJB.m`: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`;
- `HANK3_FOC.m`: `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`;
- `HANK3_cost.m`: `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`;
- `lab_solve2.m`: `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`.

Production/export identities remained unchanged:

- `economics.py`: `66E3C56F177DB6DAFE7FE0A5FD6DA480D71A7ACC10B5209BC0E3F7360226DC55`;
- `matlab_faithful_policy.py`: `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2`;
- standalone export: `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`.

## Predecessor blocker adjudication and helper repair

Frozen blocker:

`MP4B_HANK3_FOC_JAVA_CANONICALPATH_IS_NOT_JUNCTION_AUTHORITY`

Both active validation helpers removed `canonical_root(...)` and `java.io.File(...).getCanonicalPath()` as logical-to-physical authority. Repository search confirmed neither token remains. No `startsWith`, substring/`contains`, broad `D:\MatlabProgram`, sibling, or filename-only mechanism replaced it.

Retained fail-closed protections:

- ordered equality to the exact normalized logical and physical model-root strings;
- PowerShell `Get-Item -Force` proof of `Junction`, target count `1`, and exact target `D:\MatlabProgram`;
- exact logical and physical model-root existence;
- logical, physical, and resolved `HANK3_FOC.m` protected SHA checks;
- exact finite two-root membership for the `which('HANK3_FOC')` parent;
- separate sibling and other-`D:\MatlabProgram` rejection;
- Java `mkdir` and `createNewFile` atomic no-overwrite reservation;
- MATLAB path restoration after validation;
- unchanged frozen ten scalar cases and protected call expression in the inactive edge helper.

Helper hashes:

| Helper | Before SHA-256 | After SHA-256 |
|---|---|---|
| `mp4b_raw_vb_hank3_foc_edge_diagnostic.m` | `DE4514D0D5644772381E5E6663968BEC5BA6A58DBDE6DAC797F5CDBA6766414B` | `33AC7212BF6D3F27A11761B2FD29DB713E63DFDE1356B5002FE5B9ED1166AF69` |
| `mp4b_raw_vb_hank3_foc_path_equivalence_smoke.m` | `1CF819FA75B416353507515D0F46C685B3BE41F6253D9649551EDB9FD2687D35` | `8F3D7E87CDFA63510505042F938286DC58BAA4F734253C74520AF91742BB601E` |

Independent static review established:

`MP4B_HANK3_FOC_EXACT_JUNCTION_GUARD_REPAIR_STATIC_REVIEW_PASS`

## Focused negative probes

Before MATLAB execution, `python -m pytest -q tests/test_mp4b_hank3_foc_exact_junction_guard.py` returned `5 passed`.

The focused static/unit contract rejected:

- physical root in the logical-root argument;
- logical root in the physical-root argument;
- `...HANK-sibling`;
- `D:\MatlabProgram\other-model`;
- a 64-zero wrong helper SHA;
- multiple junction targets;
- the wrong junction target;
- a non-Junction link type.

It also proved both active helpers contain no Java canonical-root assertion or broad path matcher and that the edge helper retains all ten frozen case ids and the exact protected call expression. Test SHA-256: `7933F9214AC17AD19BE2DC81C999793D030A681DB41AA6315E2E3458EA465B87`.

## MATLAB checkcode and the single smoke

Smoke command scope:

- add only the repository MATLAB validator directory;
- run `checkcode(...,'-id')` on the two repaired helpers;
- invoke only `mp4b_raw_vb_hank3_foc_path_equivalence_smoke` with the exact roots and fresh root below.

`checkcode` counts: `0,0`.

Fresh smoke root:

`D:\ProjectTemp\mp4b_hank3_foc_exact_junction_smoke_20260831T121500`

Manifest:

`D:\ProjectTemp\mp4b_hank3_foc_exact_junction_smoke_20260831T121500\path_equivalence_smoke_manifest.json`

Manifest SHA-256:

`A82DC905E7D057EBE0645E3C8F3331F438CF939716762B17AC5C9B270B758D8B`

Manifest marker:

`MP4B_RAW_VB_HANK3_FOC_EXACT_JUNCTION_GUARD_SMOKE_PASS`

Resolved helper:

- path: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK3_FOC.m`;
- SHA-256: `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`;
- exact finite-root membership: PASS;
- logical-source SHA: protected SHA;
- physical-source SHA: protected SHA;
- sibling rejection: PASS;
- unrelated D-root rejection: PASS.

The smoke was executed exactly once. Reruns: `0`.

## Complete zero-call and mutation ledger

- guard-only MATLAB smoke: `1/1`;
- replacement scalar diagnostic batches: `0`;
- protected `HANK3_FOC` calls: `0`;
- MATLAB HJB/KFE/household/multi-province/stationary: `0/0/0/0/0`;
- Python local-policy/HJB/KFE/household/stationary: `0/0/0/0/0`;
- old 50-state HJB parity: `0`;
- Beijing household parity: `0`;
- MP2/MP3 empirical: `0/0`;
- annual batch/shocks/transition/dynamics/IRF/R5/Results: all `0`;
- production/export mutation: `0`.

`MP4B_RAW_VB_TRANSFER_FOC_SOURCE_EDGE_SEMANTICS_FROZEN` remains NOT AUTHORIZED / NOT REACHED.

## Forbidden-operation check

PASS. No scalar edge batch, protected scientific function, production oracle, faithful HJB/KFE, corrected/reference module, standalone export, MP2/MP3, canonical input/cache, protected MATLAB source, historical R5, or Results path was run or modified.

## Git closeout

Explicit-path staging only. One execution commit and one non-force push are required. GitHub read-back must cover both helpers, the focused test, and this report, followed by `HEAD == origin/main`, ahead/behind `0/0`, and clean worktree.

## Exactly one recommended next gate

Publish one separately authorized replacement validation-only `HANK3_FOC` ten-case scalar edge diagnostic using this smoke-validated exact-junction guard, with every HJB/KFE/household/stationary/model call and production mutation kept at zero.
