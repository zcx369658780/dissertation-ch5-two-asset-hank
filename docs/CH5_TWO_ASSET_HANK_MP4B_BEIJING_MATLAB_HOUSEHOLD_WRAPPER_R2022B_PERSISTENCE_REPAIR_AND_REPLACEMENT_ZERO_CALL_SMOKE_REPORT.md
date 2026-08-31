# MP4B Beijing MATLAB household wrapper R2022b persistence repair and replacement zero-call smoke report

Date: 2026-08-31

## Terminal verdict

`MP4B_BEIJING_MATLAB_HOUSEHOLD_WRAPPER_R2022B_PERSISTENCE_REPAIR_AND_REPLACEMENT_ZERO_CALL_SMOKE_PASS`

Required smoke marker established:

`MP4B_BEIJING_MATLAB_HOUSEHOLD_WRAPPER_ZERO_CALL_SMOKE_PASS`

This is validation-infrastructure evidence only. It is not a household, HJB, KFE, stationary, or parity result.

## Live continuity

- repository: `zcx369658780/dissertation-ch5-two-asset-hank`
- live task authority at execution start: `4d268418e13b502f7652d45b109bdded09359225`
- direct parent: `ae1f0b0fa88fa13be43a70816aa5c678d386e120`
- branch: `codex/ch5-adjustment-boundary-redesign`
- fresh fetch and fast-forward: PASS
- entry worktree: clean

The task was the direct child of the predecessor BLOCKED report commit.

## Preserved identities

Rolled-back production/export identities remained exact:

- `economics.py`: `5FD4805CBBF7E5222ABB403B976AE74617904E776336D5B42F58AB05D3FF49E7`
- `matlab_faithful_policy.py`: `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2`
- standalone export: `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`

Protected MATLAB identities remained exact:

- `HANK_2ASSETS_HJB.m`: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- `HANK3_FOC.m`: `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`
- `HANK3_cost.m`: `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C`
- `lab_solve2.m`: `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20`

Preserved read-only evidence:

- same-input candidate contract SHA-256: `FE833FAEB48521CD0C7594627AF6FB5012F9497A455E9B2C5E7490E0C40E6F22`
- standalone patch SHA-256: `FC4DAC660130DEB73E1A88C6638F1C4B282D511AA06875123437693FBE4C5A71`
- standalone semantic replay SHA-256: `B1EA2D07DB0940CCBAFF76EAED2C844403728A1396748F3B20D7E32FA1D7D0B4`

## Diagnosis and repair

Exact predecessor error diagnosis: `UNRESOLVED_BUT_REPLACEMENT_SMOKE_PASS`.

The predecessor wrapper was not a committed artifact, and its failed combined MATLAB batch produced neither manifest nor durable error identifier/message. This task therefore does not infer a cause from the missing output.

The new validation wrapper is:

`validators/multi_province/matlab/mp4b_beijing_household_wrapper.m`

SHA-256: `518B0F9137ADA16155EE76EA2A08B21C0B3D91D67C321A2EF89C063B1EAC5AFD`.

R2022b-compatible persistence design:

1. require `run_root` to be a nonempty exact direct child of `D:\ProjectTemp`;
2. reject any existing file or directory at that path;
3. atomically create the exact root with `java.io.File(...).mkdir()`;
4. atomically reserve the manifest with `java.io.File(...).createNewFile()`;
5. open only that newly reserved empty file with `fopen(...,'w')`;
6. require the complete encoded byte/character count;
7. require successful `fclose` before returning PASS;
8. never delete, recreate, truncate, reuse, or overwrite an existing artifact.

Unsupported `fopen(...,'x')` is absent.

## Zero-call control flow and source binding

The wrapper accepts explicit `smoke` and future `run` modes. In source order, the smoke branch persists the manifest and executes `return` before the only `HANK_2ASSETS_HJB(...)` expression. No multi-province controller symbol is present.

Static markers established before execution:

- `MP4B_BEIJING_MATLAB_HOUSEHOLD_WRAPPER_R2022B_PERSISTENCE_STATIC_REVIEW_PASS`
- `MP4B_BEIJING_MATLAB_HOUSEHOLD_WRAPPER_ZERO_CALL_CONTROL_FLOW_STATIC_REVIEW_PASS`

Fail-closed source protections retained:

- exact ordered logical root: `C:\MatlabProgram\2023年12月2日 多省份神经网络HANK`
- exact ordered physical root: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`
- independent `Get-Item -Force` evidence: `LinkType=Junction`, target count `1`, sole target `D:\MatlabProgram`
- logical and physical HJB source existence and exact SHA
- `which('HANK_2ASSETS_HJB')` resolved parent membership in the exact finite two-root set
- resolved source exact SHA
- sibling and unrelated D-root rejection
- no `startsWith`, substring/`contains`, broad D-root, sibling, filename-only, `getCanonicalPath`, or `canonical_root` trust.

## Focused verification

Focused test:

`tests/test_mp4b_beijing_household_wrapper.py`

SHA-256: `24C009E1D179D6F4FC8CB8DA96C2AF3AB7D057BD902EC93F6A34B373620CFF16`.

Results before smoke:

- focused pytest: `5 passed`
- Python `py_compile`: PASS
- exact ordered-root negative probes: PASS
- sibling/other-root probes: PASS
- no-overwrite/schema/zero-ledger checks: PASS
- `git diff --check`: PASS

MATLAB R2022b checkcode artifact:

`D:\ProjectTemp\ch5-mp4b-beijing-wrapper-checkcode-20260831-001\checkcode.json`

- SHA-256: `61E444FB752E98467E2917691415E6D4EAFCC9F82E4189619AE2266258029F16`
- `checkcode(...,'-id')`: `0` findings
- scientific calls: `0`

## Single replacement smoke

Fresh root, created exclusively by the wrapper:

`D:\ProjectTemp\ch5-mp4b-beijing-wrapper-replacement-smoke-20260831-001`

Manifest:

`D:\ProjectTemp\ch5-mp4b-beijing-wrapper-replacement-smoke-20260831-001\matlab_wrapper_smoke_manifest.json`

Manifest SHA-256:

`99C19A4C2676E052F7D5C3F2A8C3AF0CB704EADAF29E7D87EF7E4F0A4D40023D`

Independent post-process JSON read-back: PASS.

Manifest evidence:

- mode: `smoke`
- MATLAB: `9.13.0.2049777 (R2022b)`, release `2022b`
- wrapper SHA matches repository bytes
- resolved protected path: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK\HANK_2ASSETS_HJB.m`
- resolved SHA: `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`
- exact finite-root membership: PASS
- Junction/sole-target evidence: PASS
- same-input contract SHA: exact
- negative root probes: PASS
- MATLAB process exit: success
- smoke attempts: exactly `1`
- smoke reruns: `0`

## Complete scientific/model call ledger

| Route | Count |
|---|---:|
| replacement wrapper smoke | 1 |
| `HANK_2ASSETS_HJB` | 0 |
| MATLAB HJB/KFE/scientific household | 0/0/0 |
| standalone Python household/HJB/KFE | 0/0/0 |
| modular Python HJB/KFE | 0/0 |
| MATLAB/Python local-policy reruns | 0/0 |
| MATLAB scalar rerun | 0 |
| exact-junction smoke rerun | 0 |
| second-province household | 0 |
| MATLAB/Python multi-province stationary | 0/0 |
| MP2/MP3 | 0/0 |
| annual batch/shocks/transition/dynamics/IRF/R5/Results | 0 |

Production/export mutation: `0`.

## Forbidden-operation audit

PASS. No protected household/HJB/KFE function, standalone or modular household solver, local-policy/scalar scientific replay, second province, stationary route, MP2/MP3, annual batch, shocks, transition, dynamics, IRF, R5, or Results route was invoked. No production/export, protected MATLAB, canonical input/data/cache, accepted scientific artifact, or project rule was modified.

## Git closeout

Explicit-path staging only, one execution commit, one non-force push, GitHub read-back of all changed paths, `HEAD == origin/main`, ahead/behind `0/0`, and clean worktree are required.

## Exactly one recommended next gate

Resume the Beijing first-turn household parity route from the frozen same-input candidate contract and accepted standalone raw-`Vb` patches, reusing this wrapper smoke PASS; authorize one MATLAB Beijing household call, one repaired standalone Python household call, and one comparator only after the remaining source-map/comparator/runner preflight gates are re-established. Calendar-2009 multi-province stationary remains closed.
