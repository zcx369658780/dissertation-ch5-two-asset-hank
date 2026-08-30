# CH5 Two-Asset HANK MP4B raw-Vb HANK3_FOC edge diagnostic path-equivalence repair and replacement freeze report

Date: 2026-08-31

Terminal verdict:

`MP4B_RAW_VB_HANK3_FOC_EDGE_DIAGNOSTIC_REPLACEMENT_BLOCKED`

## Live continuity

- fresh-fetch advanced `origin/main` from `e46e1d5047ef2b6fc4667428e22527ebe8c668d5` to `7d73189ad507f3df28605919571e44446c1befbd`;
- `7d73189ad507f3df28605919571e44446c1befbd` has the single direct parent `e46e1d5047ef2b6fc4667428e22527ebe8c668d5`;
- the only path added by that authority commit is the live task;
- the execution branch was fast-forwarded to the live task with `HEAD == origin/main`, ahead/behind `0/0`, and a clean worktree before mutation.

## Protected identities and finite pair

- logical storage root: `C:\MatlabProgram`;
- physical storage root: `D:\MatlabProgram`;
- PowerShell `Get-Item -Force` independently reported `LinkType=Junction` and the single target `D:\MatlabProgram`;
- exact logical model root: `C:\MatlabProgram\2023年12月2日 多省份神经网络HANK`;
- exact physical model root: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`;
- both logical and physical `HANK3_FOC.m` existed and hashed to `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D`.

The validation-only helper was changed to accept only the explicit exact pair, independently query the top-level junction type and target, require both model roots, require logical/physical/resolved helper SHA identity, and require the resolved helper parent to be an exact member of the finite two-root set. No `startsWith`, substring, broad D-root, or arbitrary sibling acceptance was added.

Helper SHA-256 after the bounded repair:

- scalar diagnostic helper: `DE4514D0D5644772381E5E6663968BEC5BA6A58DBDE6DAC797F5CDBA6766414B`;
- guard-only smoke helper: `1CF819FA75B416353507515D0F46C685B3BE41F6253D9649551EDB9FD2687D35`.

Independent static review established:

- `MP4B_RAW_VB_HANK3_FOC_PATH_EQUIVALENCE_GUARD_STATIC_REVIEW_PASS`;
- `MP4B_RAW_VB_HANK3_FOC_DIAGNOSTIC_HELPER_STATIC_REVIEW_PASS`.

## Persistence review

Both new validation paths use `java.io.File(...).createNewFile()` before opening the reserved empty file with `'w'`; neither uses unsupported `fopen(...,'x')`. The scalar helper reserves its exact output before any protected `HANK3_FOC` call. The smoke helper uses an atomic `java.io.File.mkdir()` result check for the fresh root and then atomically reserves its manifest.

## Guard-only smoke

Authorized/consumed: `1/1`.

Invocation root requested:

`D:\ProjectTemp\mp4b_raw_vb_hank3_foc_path_smoke_20260831T083000`

The invocation first returned `CHECKCODE_COUNTS=0,0`, then failed with:

`logical and physical model roots are not equivalent`

The exact junction PowerShell check necessarily passed before this point. The failure occurred in the subsequent Java `getCanonicalPath()` model-root equivalence assertion: in this MATLAB R2022b/Windows environment Java canonicalization did not establish the junction target equivalence required by the helper. This is a validation-infrastructure failure, not a scientific result.

The smoke root was not created and no smoke manifest exists. Therefore:

- `MP4B_RAW_VB_HANK3_FOC_PATH_EQUIVALENCE_SMOKE_PASS` was not established;
- no repair-and-smoke-rerun was performed;
- the replacement scalar batch was not entered.

## Replacement scalar diagnostic

Authorized conditionally: exactly one batch only after smoke PASS.

Consumed: `0`.

Protected `HANK3_FOC` calls: `0`.

The ten frozen cases all remain unchanged in the helper but were not executed:

| Case | Ratio classification | HANK3_FOC output classification | Status |
|---|---:|---:|---|
| `localized_BB` | not observed | not observed | not executed |
| `localized_BF` | not observed | not observed | not executed |
| `localized_FB` | not observed | not observed | not executed |
| `localized_FF` | not observed | not observed | not executed |
| `positive_pb` | not observed | not observed | not executed |
| `negative_pb` | not observed | not observed | not executed |
| `zero_pb_positive_pa` | not observed | not observed | not executed |
| `zero_pb_negative_pa` | not observed | not observed | not executed |
| `zero_pa_zero_pb` | not observed | not observed | not executed |
| `zero_a_negative_pb` | not observed | not observed | not executed |

`MP4B_RAW_VB_TRANSFER_FOC_SOURCE_EDGE_SEMANTICS_FROZEN` was not established.

## Complete call and mutation ledger

- guard-only MATLAB smoke: `1/1` consumed;
- replacement MATLAB scalar diagnostic: `0/1` consumed;
- protected `HANK3_FOC`: `0`;
- MATLAB HJB/KFE/household/multi-province/stationary: `0/0/0/0/0`;
- Python local-policy/HJB/KFE/household/stationary: `0/0/0/0/0`;
- 50-state HJB parity / Beijing household parity: `0/0`;
- MP2 / MP3 / annual batch: `0/0/0`;
- shocks/transition/dynamics/IRF/R5/Results: all `0`;
- production/export mutation: `0`;
- rollback: not required.

Protected production identities remain:

- `economics.py`: `66E3C56F177DB6DAFE7FE0A5FD6DA480D71A7ACC10B5209BC0E3F7360226DC55`;
- `matlab_faithful_policy.py`: `D8A595B93689ED7A9457738620479E3158C734F6878A063FA6B12B0CCFD5F8C2`;
- accepted standalone: `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`.

## Static/tests/diff and forbidden-operation check

- independent pre-smoke helper review: PASS after one pre-run remediation cycle;
- MATLAB R2022b `checkcode`: `0` findings for each changed helper;
- `git diff --check`: PASS;
- frozen ten case ids, arrays, `pa./pb`, protected call expression, classification, and source formulas were unchanged;
- no HJB, KFE, household, stationary, empirical, dynamics, or Results operation ran;
- no production, standalone, corrected/reference, protected MATLAB, canonical data/cache, or historical R5 path changed.

## Git closeout

Explicit-path staging only. One execution commit and one non-force push are required. GitHub read-back must confirm the three changed paths, `HEAD == origin/main`, ahead/behind `0/0`, clean worktree.

## Exactly one recommended next gate

Publish a new live task authorizing only the minimum validation-helper correction needed to replace the non-dereferencing Java canonical-root assertion with evidence bound to the already exact, independently verified `C:\MatlabProgram` junction-to-`D:\MatlabProgram` relation, followed by one new guard-only smoke budget. Do not authorize the replacement scalar batch until that smoke passes.
