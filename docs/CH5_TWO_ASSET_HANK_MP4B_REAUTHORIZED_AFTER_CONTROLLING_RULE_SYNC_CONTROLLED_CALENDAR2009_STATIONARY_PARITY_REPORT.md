# Chapter 5 Two-Asset HANK MP4B reauthorized stationary-parity report

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Live authority: `cce661ca7772b26a3fe87c64b008a5c6997deb63`

## Terminal verdict and acceptance level

`MP4B_CONTROLLED_CALENDAR2009_STATIONARY_PARITY_BLOCKED`

Acceptance level: pre-solver same-input identity is proven for this attempt; no
stationary scientific parity, household-route parity, outer-route parity,
controller parity on empirical outputs, or final stationary state is accepted.
The block is a validation-entry/source-binding infrastructure failure before a
province household solve, not a scientific mismatch or nonconvergence result.

## Live continuity and controlling rules

Execution began clean with
`HEAD == origin/main == cce661ca7772b26a3fe87c64b008a5c6997deb63`.
The prior blocker `3ce40ad9e5e32886232a6e5e2819e8db2f68736e`, accepted
MP4A2 `85772bc6920db58cd6ec38bf8e1d7a5d593e12fc`, local-safety
publication `996a09f7f8e9861ca81c50415c35a017293d4bd9`, and MATLAB-gate
publication `d7560e48cb7aa4ddb0465f26e88fdfa0489d29af` are ancestors.

The controlling Git-blob byte identities are:

| Rule | SHA-256 |
|---|---|
| `PROJECT_RULE_LOCAL_FILE_SAFETY_CURRENT.md` | `CB36206D6FF12357F5AE4CEC7D8935BD0B1F8B5DB3051128FC83ABE8A9755BF6` |
| `PROJECT_RULE_MATLAB_MODEL_DIAGNOSTIC_GATES_CURRENT.md` | `82E5CD80361A356D783AFD3F0A28244F8A6893BC750461E4D38AE3E766D0AA1C` |

The checkout's CRLF byte hashes differ, but `git cat-file` produces the required
hashes and both current blobs are content-identical to their publication commits.

## Source, storage, and input identity

- logical protected entry: `C:\MatlabProgram`;
- link type/target: junction to `D:\MatlabProgram`;
- protected source: `C:\MatlabProgram\2023年12月2日 多省份神经网络HANK`;
- physical D-drive free space before execution: `76,250,025,984` bytes;
- output drive: D, same free-space observation;
- canonical input: `D:\ProjectTemp\ch5-mp4a2-2009-input-binding-20260830-001\calendar_2009_primary_premodel_input.json`;
- canonical SHA-256: `507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`.

Protected-source SHA-256 identities:

| File | SHA-256 |
|---|---|
| `multi_prov_HANK_12sts.m` | `3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97` |
| `mpHANK_equilibrium_2000.m` | `26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5` |
| `HANK_mp_1eq.m` | `ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF` |
| `HANK_mp_1turn.m` | `D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF` |
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` |

Accepted identities remained exact: wrapper
`D0FCEE89536E9095AE76A4576A0CA9249A29813C37D89A6E192B9AF6F5CF04E9`,
standalone oracle `276D2244B389D6EDE140DAF8B1F9B0BE1F4AA859368941CED1A12BA8A5831AB8`,
MP2 `D18C4385745E33E917B79994CAA069BE8825C9F22919A5A9EDE918845312D98D`,
and MP3 `7065D0FCBFDA6A88C8F773DEBDF277F6E300A8E0195B7CC635F7A0033D74D88C`.
Primary/cache identities remained the MP4A2-frozen
`C826B01...B88929`, `09814A45...0ECB3`, `A6F444FC...64A68`,
`26E44D17...A3566`, and `923CC9E5...49E9A` values.

## Pre-solver equality

`MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_PASS`

The MATLAB and Python semantic manifests compared with zero mismatches across:
calendar year 2009, analysis index 1, workbook numeric row 10, MAT index 1,
output year 2009, regression key 10, province order, GDP/CAP/POP/log vectors,
`IND_alpha`, fixed-2020 `IND_Zt`, distance/`sigmau`, initial `Zt`, `GovInv`,
inter-province ratios, every source `param/grid/num/CHI/init` field, shapes,
`la_mat`, tolerances, bounds, and `max3iter=500`.

Preflight root:
`D:\ProjectTemp\ch5-mp4b-presolver-reauthorized-20260830-002`.
MATLAB manifest SHA is
`B810618C7580BB7BFC3A9E78B4309119EF54EA7F2EBD1E492AFCBE9AEA99642D`;
Python manifest SHA is
`1F95CFCB2D81A02B38FD1DC2F2BED632E31566809AFD59DBA85A52D7060BECAC`.
Their serialized byte hashes differ because JSON formatting differs; semantic
recursive comparison is exact. The first helper-only attempt failed on an
R2022b-incompatible exclusive-open mode, created no manifest, was corrected
without invoking a model, and is not a scientific run.

## Scientific call ledger and run roots

| Operation | Authorized | Consumed | Outcome |
|---|---:|---:|---|
| prior blocked attempt scientific calls | 0 | 0 | preserved |
| corrected MATLAB top-level invocation | 1 | 1 | infrastructure/source-binding failure before province HJB |
| MATLAB province HJB/KFE calls | internal only | 0 | loop skipped because `N_prov` was empty |
| corrected Python top-level invocation | 1 conditional | 0 | prohibited after pre-scientific MATLAB infrastructure failure |
| Python HA/HJB/KFE calls | internal only | 0 | not reached |
| wrong-year route / batch / shocks / transition / dynamics / IRF / R5 / Results | 0 | 0 | PASS |

MATLAB run root:
`D:\ProjectTemp\ch5-mp4b-matlab-2009-reauthorized-20260830-001`.
Persisted files:

| Artifact | SHA-256 |
|---|---|
| `matlab_presolver_manifest.json` | `32F4E97C0C4B7A66ECBE7E4DE6506DDEEB6462884B1459CA2C711BFEAE481EF7` |
| `matlab_terminal_failure.json` | `2221240CF43B2DC049885C0122B6FF3409F13B18E9F61389CC16B1F0926D1285` |
| `matlab_terminal_failure.mat` | `45305A63B18693AD5448B54F640E9198415E516B0239CF7B1B0EFC34451241C7` |

No Python scientific run root exists.

## Convergence, comparison hierarchy, and first divergence

- MATLAB convergence: unavailable; outer iteration count: 0 completed.
- Python convergence: not run; outer iteration count: not applicable.
- Layer 1, pre-solver input identity: exact PASS.
- Layers 2-10, including household inputs/outputs, migration, capital/`rah`,
  firm, wage/monetary/fiscal, controller history, later turns, and final state:
  not reached and not compared.

The first divergent stage is the MATLAB validation entry immediately before
the provincial household loop. `multi_prov_HANK_12sts.m` normally declares
`global N_prov; N_prov=31`; the accepted lower-level MP4A2 wrapper bypasses that
top-level source and did not reproduce this required source binding.
`mpHANK_equilibrium_2000` therefore received an empty global, initialized empty
collections, and `HANK_mp_1turn` skipped both loops before failing at line 23
with MATLAB identifier `MATLAB:UndefinedFunction` and message that `results`
was undefined.

Root-cause classification:
`SOURCE_ENVIRONMENT_FAILURE__VALIDATION_WRAPPER_OMITS_GLOBAL_N_PROV_BINDING`.
The five scientific mismatch classes are not applied because two scientific
routes did not complete. This report identifies the exact future repair target
but makes no repair and performs no rerun.

Qualitative sign/ranking diagnostics are unavailable because no provincial
scientific output exists. Material scientific mismatch list: not assessable.
Unresolved scientific residual list: stationary MATLAB/Python parity in full.
Source/environment failure list: the single global `N_prov` binding omission.

## Tests, files, and forbidden-operation check

- MATLAB `checkcode` for prepared-state writer, accepted wrapper, and one-shot
  runner: PASS before the call.
- online controller exact regression against all seven MP3 scenarios: PASS.
- complete focused MP1-MP4A2 plus MP4B tests: `60 passed`.
- Python `compileall`: PASS; `git diff --check`: PASS.
- no legacy `chapter5_model` runtime import was introduced.

Repository writes are limited to `stationary_runtime.py`, its focused test,
the pre-solver comparator, three validation-only MATLAB helpers, the bounded
CURRENT roadmap status update, and this report. Protected MATLAB, accepted
standalone/modular household code, MP2, MP3, canonical input, workbooks, cache,
and historical R5 were not modified. No raw workbook or scientific MAT output
is staged for Git.

Forbidden-operation check: PASS. The legacy wrong-year route, 2010-2023 batch,
shocks, transition, dynamics, IRF, legacy R5, Results, and neural-network code
all remained at zero.

## Exactly one recommended next gate

Recommend one bounded **MP4B validation-wrapper `N_prov=31` source-binding repair,
independent static review, and separately reauthorized one-run-per-language parity
gate**. It must issue fresh scientific budgets; this task's MATLAB invocation
cannot be reused or retried.
