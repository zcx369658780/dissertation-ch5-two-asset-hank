# Chapter 5 Two-Asset HANK MP4B wrapper source-binding repair report

Date: 2026-08-30

Repository: `zcx369658780/dissertation-ch5-two-asset-hank`

Live authority: `5f48af4b12ec94fa171950af4771c7aee28d6fb2`

## Terminal verdict

`MP4B_WRAPPER_REPAIR_AND_CALENDAR2009_STATIONARY_PARITY_BLOCKED`

The source-required `N_prov=31` binding was repaired and both pre-run markers
were established, but the single fresh MATLAB invocation stopped before any
province household call. A newly added validation guard compared the logical C
junction path literally against MATLAB's resolved physical D path and rejected
two paths that the controlling rule defines as one storage boundary. Python was
therefore not run. No stationary parity is accepted.

## Continuity and prior-call identity

Fresh fetch and fast-forward established a clean
`HEAD == origin/main == 5f48af4b12ec94fa171950af4771c7aee28d6fb2`.
Its direct parent is prior report commit
`f0b9b5aa3b7479c1813bf33249391b3f42d859d7`.

The prior task had consumed one MATLAB top-level call, zero provincial HJB/KFE
calls, and zero Python calls. That budget was not reused. This task used only
its separately authorized fresh budget.

Controlling Git-blob hashes remained exact:

| Rule | SHA-256 |
|---|---|
| local file safety | `CB36206D6FF12357F5AE4CEC7D8935BD0B1F8B5DB3051128FC83ABE8A9755BF6` |
| MATLAB diagnostic gates | `82E5CD80361A356D783AFD3F0A28244F8A6893BC750461E4D38AE3E766D0AA1C` |

The standalone oracle, MP2 and MP3 hashes remained respectively
`276D2244...5831AB8`, `D18C4385...12D98D`, and `7065D0FC...D74D88C`.
No active legacy `chapter5_model` dependency was found.

## Source-binding completeness audit

Protected root:
`C:\MatlabProgram\2023年12月2日 多省份神经网络HANK`, resolving through
the junction to `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`.

The complete bypassed pre-entry environment audit found:

| Source | Binding/side effect | Stationary computational role |
|---|---|---|
| `multi_prov_HANK_12sts.m:6` | declares global `Ncores`, no assignment | not read by lower stationary route |
| `multi_prov_HANK_12sts.m:7` | declares global `myfontsize`, no assignment | plotting only; not read before household loop |
| `multi_prov_HANK_12sts.m:8` | `global N_prov; N_prov=31` | required by equilibrium initialization, distance helper and province loops |
| `multi_prov_HANK_12sts.m:9` | `warning('off')` | display state only; not an economic/numerical input |
| wrapper | `addpath(protected_root)` | resolves protected functions and relative data helpers |
| lines 12-113 | constructs `num/CHI/grid/param/init/grids/inits` | already reproduced field-for-field by prepared-state helper |

No persistent variables, RNG state, `cd`, additional global assignments, or
other hidden scalar binding is established by the bypassed function before the
lower equilibrium call. `load_GDPdata.m` and `load_distdata.m` were also read
and hashed; the accepted cache path avoids the workbook-regeneration branch.

Static audit conclusion:

`SOURCE_BINDING_AUDIT_COMPLETE__N_PROV_IS_ONLY_MISSING_REQUIRED_BINDING`

Protected hashes remained:

| File | SHA-256 |
|---|---|
| `multi_prov_HANK_12sts.m` | `3C44449CFD4047B5C9E17E540AFEA2F50B4251150F8F74AB8CCEED26E15DEC97` |
| `mpHANK_equilibrium_2000.m` | `26EA44552DA33919F8CCD777C084E15ECA0EA9575FEE80A07F9E0056F3F97DE5` |
| `load_GDPdata.m` | `DECA8AF3F22097550B8957FE848989E6342619CB9929A1C00076E020549366C5` |
| `load_distdata.m` | `18F594DD7D1ED090CA2AF576DEBCD8DCAA73C012608A8921F8D5BD6CC24F478B` |
| `HANK_mp_1eq.m` | `ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF` |
| `HANK_mp_1turn.m` | `D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF` |
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` |

## Exact repair and static review

The validation wrapper added exactly the source binding:

```matlab
global N_prov;
N_prov = 31;
```

It also added fail-closed checks for `N_prov`, protected helper resolution and
a source-binding manifest. No economic formula, HJB/KFE expression,
calendar/index, convergence rule, tolerance, clipping rule, or update order was
changed. The one-shot helper added MATLAB profiler-only observability for exact
household and outer-turn call counts.

All four validation `.m` files returned empty `checkcode` results after the
source-required global warning was locally annotated. The protected source was
hash-identical, D drive free space was `76,249,067,520` bytes, and fresh roots
were collision-free. The pre-run marker was emitted:

`MP4B_VALIDATION_WRAPPER_SOURCE_BINDING_REPAIR_STATIC_REVIEW_PASS`

Runtime evidence later showed that the static review missed one implementation
error in the newly added helper path check: literal `startsWith` is not valid
for a logical-junction versus resolved-physical-path equivalence check. Thus the
marker records the gate actually established before invocation, but it does not
support final acceptance.

Repaired helper SHA-256 values:

| Helper | SHA-256 |
|---|---|
| `mp4b_calendar2009_stationary_wrapper.m` | `B4FD98AB9459F48A3ECACEF2906C6C015759AAEA345294F5C12502D7479D76C8` |
| `mp4b_execute_once.m` | `035046912629F66F2D1983D0147038ECFF567E3701FAC7CFDD67B39F705A45DA` |
| `mp4b_build_source_prepared_state.m` | `FE07B73728C4A6711B1DA83D881A3E38FA25243C6016CDFC3FFDBE5FA0976386` |
| `mp4b_write_presolver_manifest.m` | `147CF70B89DB789854DA008739145E1737B34DF6529DCB8C7880E3877D7F27B0` |

## Presolver equality

Canonical input remained
`507D1259A8A515E4224F40D434BD89645C02472650B51F5ADA3181BA4BCDAD48`.
The new preflight root is
`D:\ProjectTemp\ch5-mp4b-source-binding-presolver-20260830-001`.

Recursive semantic comparison covered the complete frozen annual/prepared
contract and returned mismatch count zero:

`MP4B_2009_PRESOLVER_SAME_INPUT_IDENTITY_PASS`

The MATLAB and Python manifest hashes are respectively
`B810618C7580BB7BFC3A9E78B4309119EF54EA7F2EBD1E492AFCBE9AEA99642D`
and `1F95CFCB2D81A02B38FD1DC2F2BED632E31566809AFD59DBA85A52D7060BECAC`.

## Fresh scientific-call ledger and run roots

| Operation | Authorized | Consumed | Result |
|---|---:|---:|---|
| corrected MATLAB top-level stationary entry | 1 | 1 | validation infrastructure failure before household |
| MATLAB `HANK_mp_1turn` calls | internal | 0 | profiler count |
| MATLAB `HANK_2ASSETS_HJB` calls | internal | 0 | profiler count |
| corrected Python stationary entry | conditional 1 | 0 | prohibited by MATLAB-first failure rule |
| Python household calls | internal | 0 | not reached |
| wrong year/batch/shock/transition/dynamics/IRF/R5/Results | 0 | 0 | PASS |

MATLAB run root:
`D:\ProjectTemp\ch5-mp4b-matlab-2009-source-binding-repair-20260830-001`.
No Python scientific root was created.

Persisted failure artifacts:

| Artifact | SHA-256 |
|---|---|
| `matlab_terminal_failure.json` | `D915F21109B54869B7DFA1507DBCEE1DEE2A01AC26DC1A83A9ADBC08D2DB0270` |
| `matlab_terminal_failure.mat` | `5003D3DFE76BA7C25E367283B605B32356398EC9C69485F4F8EB831E36AF2145` |

## Comparison and first divergence

| Layer | Status |
|---|---|
| source binding | `N_prov=31` exact repair established |
| pre-solver annual/prepared input | exact PASS |
| first-turn household input/output | not reached |
| migration/capital/`rah` | not reached |
| firm/wage/monetary/fiscal | not reached |
| controller/later turns/final state | not reached |

MATLAB and Python convergence statuses and iteration counts are unavailable;
both completed outer-turn counts are zero. No qualitative sign/ranking or
boundary comparison is available.

First divergence:
`VALIDATION_HELPER_PATH_EQUIVALENCE_CHECK_BEFORE_MODEL_ENTRY`.
MATLAB `which` resolves every protected helper under physical
`D:\MatlabProgram\...`, while the command supplied logical
`C:\MatlabProgram\...`. The controlling local-safety rule explicitly defines
these as one boundary, but the wrapper used literal prefix comparison.

Root-cause classification:

`SOURCE_ENVIRONMENT_FAILURE__LOGICAL_JUNCTION_PHYSICAL_TARGET_EQUIVALENCE_GUARD_ERROR`

This is an implementation/infrastructure blocker, not one of the five
scientific mismatch classes. Material scientific mismatch: not assessable.
Unresolved residual: complete calendar-2009 stationary parity. Environment
failure list contains only the path-equivalence guard error.

## Tests and forbidden-operation check

- complete focused MP1-MP4A2 plus MP4B suite: `62 passed`;
- MATLAB `checkcode`: PASS before invocation;
- seven MP3 online-controller scenarios: exact PASS;
- canonical/source/rule hashes and presolver equality: PASS;
- `git diff --check`: PASS;
- protected MATLAB modification count: zero.

Forbidden-operation check: PASS. No wrong-year MATLAB, 2010-2023 batch, Python
scientific route, shock, transition, dynamics, IRF, legacy R5, Results, or
neural-network code ran or changed. No raw data or scientific MAT output is
committed.

Git closeout uses explicit-path staging, one execution commit, one non-force
push, changed-path GitHub read-back, clean worktree and ahead/behind `0/0`.

## Exactly one recommended next gate

Recommend one bounded **logical-junction/physical-target path-equivalence guard
repair with independent static review and a separately reauthorized one-run-per-
language calendar-2009 parity gate**. This task's MATLAB call is consumed and
must not be retried.
