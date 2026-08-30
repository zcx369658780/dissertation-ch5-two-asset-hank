# Chapter 5 Two-Asset HANK MP4B path-equivalence guard repair report

Date: 2026-08-30

Live authority: `6e9780b4bcb614c222011bb053102e2f52c0bc51`

## Terminal verdict

`MP4B_PATH_EQUIVALENCE_REPAIR_AND_CALENDAR2009_STATIONARY_PARITY_BLOCKED`

The finite logical/physical-root guard repair passed static review, but the
mandatory non-scientific MATLAB smoke failed before resolving any helper. The
task therefore stopped before presolver and before both scientific models.

## Continuity and historical ledger

Fresh fetch/fast-forward established a clean execution start at
`HEAD == origin/main == 6e9780b4bcb614c222011bb053102e2f52c0bc51`, whose
direct parent is prior blocked report commit
`d3ac5caa597ff0906a7aeb3e40ebacfc520d2cfb`.

The two earlier MP4B MATLAB entries remain consumed historical evidence, each
with zero provincial household calls. They were not reused. The present task
consumed zero scientific calls.

All controlling rules and prior MP4B tasks/reports named by the live authority
were read in full. The controlling Git-blob hashes remained
`CB36206D...9755BF6` and `82E5CD80...D0AA1C`. Protected MATLAB and accepted
household/MP2/MP3/annual/runtime identities were unchanged; no active R5 import
was found.

## Exact logical/physical evidence

PowerShell `Get-Item -Force C:\MatlabProgram` established:

- logical root: `C:\MatlabProgram`;
- link type: `Junction`;
- sole target: `D:\MatlabProgram`;
- logical protected root:
  `C:\MatlabProgram\2023年12月2日 多省份神经网络HANK`;
- corresponding physical protected root:
  `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`.

The prior read-only MATLAB `which` evidence resolves every required helper
under that exact physical protected root. The finite required set is
`load_GDPdata`, `load_distdata`, `mpHANK_equilibrium_2000`, `HANK_mp_1eq`,
`HANK_mp_1turn`, and `HANK_2ASSETS_HJB`.

D-drive free space at preflight remained above 76 GB. Protected source was not
modified, and all new roots were checked for collision before creation.

## Guard repair and static review

The wrapper now receives both explicitly verified protected roots. It preserves
`global N_prov; N_prov=31`, `addpath(logical_root)`, and fail-closed checks.
For every required helper it requires:

1. both exact logical and physical files exist;
2. their text contents are identical;
3. the normalized `which` parent equals one of the finite exact roots.

It does not accept an arbitrary `D:\MatlabProgram` prefix, sibling directory,
unrelated C/D root, or helper outside the exact model root. The binding manifest
records both roots. No economic, HJB/KFE, controller, calendar, tolerance,
clipping, or update expression changed.

Changed helper hashes:

| File | SHA-256 |
|---|---|
| wrapper | `72274083B9D33685F9A8DF5BB2CA713240D43DAD1A5F48917A7A86C9B1196523` |
| one-shot runner | `C9174570623D816A370EB11C8842ABBDE01C5A473B6CD1A3C95FB097EBEF4843` |
| path smoke | `F429239CC4BE1CF649152E91786C97E65CDB6CA1CF8380A63033EF17D246F2A1` |
| pure path validator | `1285E1F30A042D4401D8F5565FF83794F366BA9A87BEFBCF3AE2396CFAF9AF55` |
| focused test | `BC69D97CEBF3BDBAF4B0D7A2AFA6E0D827F1DB364E0E903D34CC1756E4B51B07` |

MATLAB `checkcode` returned no issues for all validation helpers. Focused tests
accepted logical C and documented physical D cases and rejected siblings,
unrelated roots, and root-external helpers. The required pre-smoke marker was
established:

`MP4B_PATH_EQUIVALENCE_GUARD_REPAIR_STATIC_REVIEW_PASS`

## Non-scientific smoke

Smoke root:
`D:\ProjectTemp\ch5-mp4b-path-equivalence-smoke-20260830-001`.

The helper created the fresh root, then failed at
`mp4b_path_equivalence_smoke.m:25` before `which` and before writing a manifest.
The expression:

```matlab
helpers{i}+'.m'
```

performed MATLAB char-array numeric addition instead of filename concatenation,
leading to an out-of-memory/oversized-array error. This is a validation-helper
implementation defect; it is not a model or source failure.

Consequently:

- `MP4B_LOGICAL_PHYSICAL_PATH_EQUIVALENCE_SMOKE_PASS`: **not established**;
- smoke manifest/hash: unavailable because no manifest was written;
- non-scientific model/solver calls: zero.

The task requires immediate BLOCKED on smoke failure, so the helper was not
repaired or rerun.

## Presolver and scientific ledger

Because the smoke marker was absent, the presolver was not rerun in this task.
The accepted canonical SHA remains
`507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`,
but `MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_PASS` was not newly established.

| Operation | Authorized after all gates | Consumed |
|---|---:|---:|
| fresh MATLAB stationary entry | 1 | 0 |
| MATLAB outer turns | internal | 0 |
| MATLAB household HJB/KFE | internal | 0 |
| fresh Python stationary entry | 1 | 0 |
| Python outer turns/household calls | internal | 0 |
| wrong year/batch/shock/transition/dynamics/IRF/R5/Results | 0 | 0 |

No MATLAB or Python scientific run root exists. Convergence, iteration counts,
scientific layer parity, qualitative diagnostics and scientific mismatch
classification are unavailable.

First divergence:
`NONSCIENTIFIC_PATH_SMOKE_FILENAME_CONCATENATION`.

Root cause:
`VALIDATION_HELPER_IMPLEMENTATION_ERROR__MATLAB_CHAR_PLUS_FILENAME_SUFFIX`.

Material scientific mismatch: not assessable. Unresolved residual: complete
calendar-2009 stationary parity. Environment/helper failure list contains only
the smoke filename-concatenation defect.

## Tests and forbidden-operation check

- MATLAB `checkcode`: PASS;
- complete focused MP1-MP4B suite: `63 passed`;
- static path cases required by the task: PASS;
- protected-source hashes and worktree-start continuity: PASS;
- `git diff --check`: PASS.

Forbidden-operation check: PASS. No scientific MATLAB/Python model, wrong-year
route, 2010-2023 batch, shock, transition, dynamics, IRF, legacy R5, Results or
neural-network operation ran. No raw data or scientific MAT output is committed.

Git closeout uses explicit staging, one commit, one non-force push, per-path
GitHub read-back, clean worktree and ahead/behind `0/0`.

## Exactly one recommended next gate

Recommend one bounded **MATLAB smoke-helper filename-concatenation repair and
non-scientific path-equivalence smoke completion gate**, with scientific budgets
remaining closed until that smoke and a fresh presolver equality gate pass.
