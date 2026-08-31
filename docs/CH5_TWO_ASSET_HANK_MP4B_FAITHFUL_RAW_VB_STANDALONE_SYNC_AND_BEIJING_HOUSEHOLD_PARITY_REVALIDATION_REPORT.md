# MP4B faithful raw-Vb standalone sync and Beijing household parity revalidation report

Date: 2026-08-31

## Terminal verdict

`MP4B_FAITHFUL_RAW_VB_STANDALONE_SYNC_AND_BEIJING_HOUSEHOLD_PARITY_REVALIDATION_BLOCKED`

The standalone-only semantic replays passed, but the required first MATLAB zero-household-call wrapper smoke terminated without creating its no-overwrite manifest. No household call was authorized after that failed pre-science gate. All three candidate production/export files were rolled back to task-authority bytes.

## Live continuity and identities

- live task authority: `ac3672ebe51a3b8b927bd1e30bd7271eb7b7578c`
- execution parent: `2bb0c4250dbe4fc7725ad9f90bb1caa6df7eaacf`
- branch: `codex/ch5-adjustment-boundary-redesign`
- frozen modular patch SHA-256: `0F044055DA9B4BFF22A2F8342EF189781AD3D536BFD2A67148C1182C1F9AB31D`
- protected `HANK_2ASSETS_HJB.m`: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- protected `HANK3_FOC.m`: `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- protected `HANK3_cost.m`: `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- protected `lab_solve2.m`: `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`

The modular patch was applied exactly once and reproduced the required candidate objects `810e0875febc873ae85bef7e88edd4de349b00b2` and `2021db630f3057026ffc37d375a43aaddbccec48`, establishing `MP4B_FAITHFUL_RAW_VB_MODULAR_CANDIDATE_BYTE_IDENTITY_RESTORED_FOR_STANDALONE_PASS` before later rollback.

## Standalone candidate and source map

The standalone-only patch is `validators/multi_province/mp4b_faithful_raw_vb_standalone_candidate.patch`, SHA-256 `FC4DAC660130DEB73E1A88C6638F1C4B282D511AA06875123437693FBE4C5A71`. The repaired candidate SHA-256 was `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3`.

Its only scientific changes were the source-identical dedicated IEEE raw-`Vb` helper, removal of the faithful selector's non-source positive-`Vb` pre-rejection, and routing of the four transfer FOCs through that helper. The old shared/corrected helper and HJB/operator/KFE/aggregate blocks were unchanged. `git apply --check` against the rolled-back standalone succeeds.

Markers established before the blocker:

- `MP4B_FAITHFUL_RAW_VB_STANDALONE_CANDIDATE_PATCH_FROZEN`
- `MP4B_MODULAR_STANDALONE_RAW_VB_SOURCE_MAP_EQUIVALENCE_PASS`

## Standalone semantic replay

Artifact: `D:\ProjectTemp\ch5-mp4b-standalone-prehousehold-20260831-001\standalone_replay.json`

SHA-256: `B1EA2D07DB0940CCBAFF76EAED2C844403728A1396748F3B20D7E32FA1D7D0B4`

- frozen protected helper cases: 10/10 PASS; standalone helper calls exactly 10; mismatches 0
- preserved local-policy cases: 12/12 PASS; standalone local-policy calls exactly 12; comparator calls exactly 1; mismatches 0
- the Beijing negative-raw-`Vb` witness passed without pre-selection rejection
- MATLAB scalar and MATLAB local-policy reruns: 0/0

Markers established:

- `MATLAB_FAITHFUL_STANDALONE_RAW_VB_TRANSFER_HELPER_10CASE_SOURCE_PARITY_PASS`
- `MATLAB_FAITHFUL_STANDALONE_NEGATIVE_RAW_VB_LOCAL_POLICY_PARITY_PASS`

## Beijing input provenance and blocker

Canonical annual input SHA-256 was verified as `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`. Both preserved `turn_001_household_inputs.json` files were byte-identical at `79B7A2805ECBAACDFCC70FA194E154263FA46EE313415A7060F90C65662DCE28`; they bind the first-turn state and migration matrix but not complete household structs. The missing household constants were independently traced to protected `multi_prov_HANK_12sts.m`, `mpHANK_equilibrium_2000.m`, `HANK_mp_1turn.m`, and `HANK_2ASSETS_HJB.m`.

A no-overwrite same-input candidate contract was frozen at:

`D:\ProjectTemp\ch5-mp4b-beijing-household-20260831-001\beijing_same_input_contract.json`

SHA-256: `FE833FAEB48521CD0C7594627AF6FB5012F9497A455E9B2C5E7490E0C40E6F22`.

The MATLAB wrapper smoke was then launched once in `smoke` mode. Static control flow placed the `HANK_2ASSETS_HJB` call strictly after the smoke return, so protected household calls remained zero. The MATLAB process exited, but `matlab_wrapper_smoke.json` was not created. Because the combined batch produced no durable diagnostic artifact, no exact MATLAB identifier/message is claimed. The required marker `MP4B_BEIJING_MATLAB_HOUSEHOLD_WRAPPER_ZERO_CALL_SMOKE_PASS` was not established. No smoke retry, wrapper repair, or household execution occurred.

## Rollback and complete call ledger

Rollback identities:

- `economics.py`: `5FD4805CBBF7E5222ABB403B976AE74617904E776336D5B42F58AB05D3FF49E7`
- `matlab_faithful_policy.py`: `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2`
- standalone export: `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`

Call ledger:

| Call | Count |
|---|---:|
| standalone raw-Vb helper | 10 |
| standalone local policy | 12 |
| standalone local-policy comparator | 1 |
| MATLAB wrapper smoke attempts | 1 |
| MATLAB junction smoke rerun | 0 |
| MATLAB scalar/local-policy rerun | 0/0 |
| protected MATLAB Beijing household/HJB | 0 |
| standalone Python household/HJB/KFE | 0/0/0 |
| modular MATLAB/Python 50-state HJB rerun | 0/0 |
| separate MATLAB/Python KFE | 0/0 |
| second-province household | 0 |
| MATLAB/Python multi-province stationary | 0/0 |
| MP2/MP3 | 0/0 |
| annual batch/shocks/transition/dynamics/IRF/R5/Results | 0 |

Production/export mutation at terminal state is 0. Protected MATLAB, canonical input/data/cache, corrected/reference code, operator/HJB/KFE modules, MP2/MP3, and historical R5 were not modified.

## Checks and closeout

- replay runner `py_compile`: PASS
- standalone patch deterministic applicability (`git apply --check`): PASS
- `git diff --check`: PASS
- MATLAB `checkcode` was included in the failed smoke batch, but no durable result was emitted; it is not reported as PASS
- forbidden-operation audit: PASS

## Exactly one recommended next gate

Publish a new infrastructure-only authority to diagnose and repair the MATLAB Beijing wrapper's R2022b-compatible no-overwrite smoke persistence, then authorize exactly one replacement zero-household-call wrapper smoke; household scientific-call budgets must remain zero.
