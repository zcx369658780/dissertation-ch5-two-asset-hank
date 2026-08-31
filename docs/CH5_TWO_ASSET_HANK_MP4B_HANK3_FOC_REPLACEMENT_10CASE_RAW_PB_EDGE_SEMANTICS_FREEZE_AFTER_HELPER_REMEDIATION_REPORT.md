# Chapter 5 Two-Asset HANK MP4B HANK3_FOC replacement 10-case raw-pb edge-semantics freeze after helper remediation report

Date: 2026-08-31

Terminal verdict:

`MP4B_HANK3_FOC_REPLACEMENT_10CASE_RAW_PB_EDGE_SEMANTICS_FREEZE_PASS`

Established source-semantics marker:

`MP4B_RAW_VB_TRANSFER_FOC_SOURCE_EDGE_SEMANTICS_FROZEN`

## Live continuity and frozen identities

- live authority: `18292d4cfd34f74d63db5d4835e3c0550bd7fca1`;
- direct parent: `de25cf6a03da2c3949f4e10245204e871e937fd0`;
- execution branch was fast-forwarded to live authority with `HEAD == origin/main`, ahead/behind `0/0`, and clean worktree before execution;
- remediated edge helper SHA-256: `F98FC7D1AADA01A39693951F4CD266A7174727975FBBFE55E54343867D7E11E0`;
- exact-junction smoke helper SHA-256: `8F3D7E87CDFA63510505042F938286DC58BAA4F734253C74520AF91742BB601E`;
- preserved smoke manifest SHA-256: `A82DC905E7D057EBE0645E3C8F3331F438CF939716762B17AC5C9B270B758D8B`;
- preserved smoke marker: `MP4B_RAW_VB_HANK3_FOC_EXACT_JUNCTION_GUARD_SMOKE_PASS`;
- `C:\MatlabProgram` remained a Junction with exactly one target, `D:\MatlabProgram`.

Protected MATLAB SHA-256 values matched:

- `HANK_2ASSETS_HJB.m`: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`;
- `HANK3_FOC.m`: `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`;
- `HANK3_cost.m`: `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`;
- `lab_solve2.m`: `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`.

Production/export identities remained unchanged:

- `economics.py`: `66E3C56F177DB6DAFE7FE0A5FD6DA480D71A7ACC10B5209BC0E3F7360226DC55`;
- `matlab_faithful_policy.py`: `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2`;
- standalone export: `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`.

No helper or protected/production path was modified after preflight.

## Scalar preflight

Established before scientific execution:

`MP4B_RAW_VB_HANK3_FOC_REPLACEMENT_SCALAR_PREFLIGHT_PASS`

Checks:

- exact helper/smoke/manifest/source hashes: PASS;
- exact C/D Junction and finite-root evidence: PASS;
- no canonical, prefix, substring, broad-D, sibling, or filename-only trust: PASS;
- helper-owned direct-child fresh-root, first-error persistence, per-row identity, and complete ledger contracts: PASS;
- exact ten ids/order, `pa/pb/a`, chi, classification, `%.17g`, and protected call expression: PASS;
- focused evidence-contract plus exact-junction tests: `12 passed`;
- MATLAB R2022b `checkcode(...,'-id')`: `0` findings;
- `git diff --check`: PASS;
- worktree clean immediately before execution: PASS.

The exact-junction smoke was not rerun.

## One-shot execution artifact

Fresh caller-selected root, not pre-created externally:

`D:\ProjectTemp\mp4b_hank3_foc_10case_bcb5db94-c4a2-4d89-9485-6cbb20798126`

The helper exclusively created this direct child with its atomic `mkdir()` contract.

Success manifest:

`D:\ProjectTemp\mp4b_hank3_foc_10case_bcb5db94-c4a2-4d89-9485-6cbb20798126\success_manifest.json`

Manifest SHA-256:

`06A31A509EF696094563CD41C9928A3E83AFB076675B09155CC82B2200E7E74E`

`failure.json` does not exist.

## Complete ten-case source table

All rows resolve to:

- helper path: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK3_FOC.m`;
- helper SHA-256: `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`.

| # | case id | pa | pb | a | chi0 | chi1 | ratio class | ratio encoding | output class | output encoding |
|---:|---|---:|---:|---:|---:|---:|---|---|---|---|
| 1 | `localized_BB` | 0.0183013418028827 | 0.0036470322698923963 | 9.473684210526315 | 0.1 | 2 | finite | `5.0181463854781496` | finite | `18.55964077331755` |
| 2 | `localized_BF` | 0.029712870660726632 | 0.0036470322698923963 | 9.473684210526315 | 0.1 | 2 | finite | `8.1471367571977353` | finite | `33.381174113041901` |
| 3 | `localized_FB` | 0.0183013418028827 | -0.014003744365506235 | 9.473684210526315 | 0.1 | 2 | finite | `-1.3068891665833482` | finite | `-10.45368552592112` |
| 4 | `localized_FF` | 0.029712870660726632 | -0.014003744365506235 | 9.473684210526315 | 0.1 | 2 | finite | `-2.1217804242353084` | finite | `-14.313696746377776` |
| 5 | `positive_pb` | 1.5 | 1 | 1 | 0.1 | 2 | finite | `1.5` | finite | `0.20000000000000001` |
| 6 | `negative_pb` | 0.5 | -1 | 1 | 0.1 | 2 | finite | `-0.5` | finite | `-0.69999999999999996` |
| 7 | `zero_pb_positive_pa` | 1 | 0 | 1 | 0.1 | 2 | +Inf | `+Inf` | +Inf | `+Inf` |
| 8 | `zero_pb_negative_pa` | -1 | 0 | 1 | 0.1 | 2 | -Inf | `-Inf` | -Inf | `-Inf` |
| 9 | `zero_pa_zero_pb` | 0 | 0 | 1 | 0.1 | 2 | NaN | `NaN` | finite | `0` |
| 10 | `zero_a_negative_pb` | 1 | -1 | 0 | 0.1 | 2 | finite | `-1` | finite | `-0` |

`Inf`, `NaN`, and signed zero are recorded as protected MATLAB source evidence without reinterpretation.

## Exact call ledger

- replacement MATLAB scalar batches: `1`;
- scalar reruns: `0`;
- `HANK3_FOC_attempted_calls`: `10`;
- `HANK3_FOC_completed_calls`: `10`;
- exact-junction smoke rerun: `0`;
- MATLAB HJB/KFE/household/multi-province/stationary/GE: all `0`;
- Python local-policy/HJB/KFE/household/stationary: all `0`;
- old 50-state HJB parity / Beijing household parity: `0/0`;
- MP2/MP3 empirical: `0/0`;
- annual batch/shocks/transition/dynamics/IRF/R5/Results: all `0`;
- production/export mutation: `0`.

The manifest contains the same complete explicit zero ledger and binds every row to the verified protected source identity.

## Forbidden-operation check

PASS. No helper, smoke helper, production/export, faithful HJB/operator/KFE, corrected/reference, protected MATLAB, canonical input/cache, MP2/MP3, historical R5, or Results path was modified. No scientific/model route other than the authorized ten protected scalar calls executed.

## Git closeout

Explicit-path staging is limited to this report. One execution commit, one non-force push, GitHub read-back, `HEAD == origin/main`, ahead/behind `0/0`, and clean worktree are required.

## Exactly one recommended next gate

Resume the faithful-only raw-`Vb` source-order repair using a dedicated faithful transfer helper, then revalidate the affected local-policy, HJB, and standalone Beijing-household parity while empirical 2009 stationary remains closed. Reuse this frozen ten-case MATLAB artifact and do not rerun the scalar batch.
