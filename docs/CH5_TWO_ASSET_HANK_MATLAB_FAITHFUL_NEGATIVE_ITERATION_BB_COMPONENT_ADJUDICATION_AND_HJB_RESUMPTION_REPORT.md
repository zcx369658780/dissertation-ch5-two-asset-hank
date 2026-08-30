# Chapter 5 Two-Asset HANK MATLAB-Faithful Negative Iteration-BB Component Adjudication and HJB Resumption Report

Date: 2026-08-30

## Terminal classification

`MATLAB_FAITHFUL_NEGATIVE_ITERATION_BB_ADJUDICATION_AND_HJB_RESUMPTION_BLOCKED`

Read-only algebra confirmed that all four persisted negative off-diagonal entries arise from the designated upper-`b` forced `Idh_B=1` branch with `sdh_B>0`. However, replacement Python execution exposed a separate boundary-assembly contradiction: the frozen external MATLAB evaluator closes its diagonal only over in-bound couplings, while designated `HANK_2ASSETS_HJB.m:155-157` retains the upper-bound forward `Ic_F*sc_F/db` term in diagonal `Y` even though no outward off-diagonal can be placed by `spdiags`. Therefore the frozen MATLAB object's exact row closure is not an exact extraction of the designated iteration `BB` boundary algebra.

The correct final adjudication is:

`MATLAB_ITERATION_BB_NEGATIVE_COMPONENT_EXTRACTION_OR_INDEXING_CONTRADICTION`

The provisional signed-coefficient candidate produced no valid Python HJB object. MATLAB/Python/comparator calls in this successor task were `0/1/0`. No repair or rerun occurred.

## Authority and identities

- Live start `origin/main`: `1fbebb96e8b4a362bcadc89964bf6051ef2d0907`.
- Branch/worktree: `codex/ch5-adjustment-boundary-redesign` / `D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-repo-20260829`.
- Pre-publication final `origin/main`: `1fbebb96e8b4a362bcadc89964bf6051ef2d0907`; publication commit/read-back is recorded in the executor handoff.
- Start state: clean after fast-forward.
- Primary authority: `MATLAB_FAITHFUL_NUMERICAL_IMPLEMENTATION_IS_PRIMARY_RECONSTRUCTION_AUTHORITY`.

Designated hashes matched:

| Source | SHA-256 |
|---|---|
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` |
| `HANK3_FOC.m` | `772B7B7BBF528DFDD246BD152B3E3026035012FE50F30DA808C1EE18C0F8463D` |
| `HANK3_cost.m` | `3504A74BB2DB9FBEE3B292AB68D758954248643D6A5178E42554E0D4794F9A3C` |
| `lab_solve2.m` | `74FD6AE8D76AB50A571831FAB95464AE4FCE919F3E70B660E5ABF6B9C5662C20` |

All predecessor artifacts were reused read-only and matched their frozen identities, including:

- manifest `784ADA4834A3FD8CFBCE7C3B5BC652DE63C2A986802603799CE3670860EF6C7A`;
- ordering `52EB994358F07767AD8859D737C3D7A89BC7FB04DC063754027CA80386F2926D`;
- initialization `C6662095D14CB83D820FACFB4779CA188BE23958BE162B943BDD2F3959522A9F`;
- MATLAB evaluator `E81AB34611E3C31DAF2400ED6A34B58F91C4FA0E0FBCCEE843828F5A6588DCBA`;
- comparator `4471CCC837A66245DCB8D2CA1D45F1BD79CBEE5EAE80874B14933E06C75F9A92`;
- tolerances `915B3539828F42099182A9145E64B4A353D0D049AF1674549C1031C923CEF72D`;
- MATLAB output `3457F51AC0F910EA40FC35A832518B9068456E22DEA4E4783F487976432DDC0A`.

The MATLAB HJB was not rerun.

## Negative off-diagonal enumeration and decomposition

The last pre-update value was recovered algebraically from the persisted implicit equation,

`V_old = Delta * (((1/Delta+rho)I-A)V_new-u)`,

with reconstruction residual `0`. This is a read-only inversion of persisted objects, not an HJB iteration. Candidate terms were then reconstructed from designated formulas. Persisted selected transfer and adjustment cost give exact `sdh_B=-d_B-cost`, and every coefficient exactly equals `-sdh_B/db` with `db=0.25`.

All four negative entries are backward liquid couplings at upper `b=0.5`, high productivity `z=1.3`:

| MATLAB row,col | Python row,col | `(b-index,a-index,z-index)` | `(b,a,z)` | coefficient | `Ic_B/Ic_F` | `sc_B/sc_F` | `Idh_B/Idh_F` | `sdh_B/sdh_F` |
|---|---|---|---|---:|---|---|---|---|
| 35,34 | 34,33 | 5,2,2 | 0.5,0.5,1.3 | -0.0658949476206877 | 0/1 | 0.04992654007456654 / 0.0019535584084588997 | 1/0 | 0.016473736905171926 / 0.010723554369538075 |
| 40,39 | 39,38 | 5,3,2 | 0.5,1.0,1.3 | -0.15070841327373913 | 0/1 | 0.035920753340307865 / 0.001952796725343653 | 1/0 | 0.03767710331843478 / 0.029824537840104554 |
| 45,44 | 44,43 | 5,4,2 | 0.5,1.5,1.3 | -0.27088987632945094 | 0/1 | 0.021603864167279774 / 0.0019243283015151214 | 1/0 | 0.06772246908236274 / 0.06126083575630517 |
| 50,49 | 49,48 | 5,5,2 | 0.5,2.0,1.3 | -0.45465503938313373 | 0/1 | 0.009684318496906874 / 0.0015823287205627423 | 1/0 | 0.11366375984578343 / 0.11040168830705684 |

Selected `d_B` values are respectively `-0.019116218341442358`, `-0.044016137401020214`, `-0.07998630570972065`, and `-0.13667013664134295`. Each ordinary sign test would reject `Idh_B` because `sdh_B>0`; designated line 153 overrides this at `i=I` by forcing `Idh_F(I,:,:)=0` and `Idh_B(I,:,:)=1`.

Designated line 155 therefore produces:

`X = -Ic_B*sc_B/db - Idh_B*sdh_B/db = -sdh_B/0.25 < 0`.

This proves the suggested forced-upper-bound mechanism for every persisted negative coefficient. There is no row/column mapping error for those entries themselves.

## Boundary diagonal-closure contradiction

The complete designated source algebra is not only line 155:

- line 155: `X=-Ic_B*sc_B/db-Idh_B*sdh_B/db`;
- line 156: `Y=Ic_B*sc_B/db+Idh_B*sdh_B/db-Ic_F*sc_F/db-Idh_F*sdh_F/db`;
- line 157: `Z=Ic_F*sc_F/db+Idh_F*sdh_F/db`.

At all four states, `Ic_F=1`, `sc_F>0`, `Idh_F=0`; hence `Z=sc_F/db>0`. At upper `b`, `spdiags` cannot place an outward `+1` liquid coupling, but diagonal `Y` still includes `-Z`. The designated row sum is consequently `-Z`, not zero. For the four rows those omitted outward coefficients are approximately:

- `0.007814233633835599`;
- `0.007811186901374612`;
- `0.007697313206060486`;
- `0.006329314882250969`.

By contrast, the frozen external evaluator's `axis_operator` helper skips an outward boundary component and adds only actually inserted components to its diagonal total. It therefore reports exact row closure and omits `Z` from the diagonal. This is not equivalent to the designated `Y` plus `spdiags` construction.

The replacement Python candidate initially accepted signed coefficients, then correctly stopped on the still-present outward upper-bound forward component:

`ValueError: outward forward component at upper boundary`

This failure exposed the extraction contradiction before a Python HJB object was persisted. The frozen MATLAB output's iteration `BB max_abs_row_sum=0` cannot be used as exact designated-source authority for these boundary rows.

## Iteration versus post-convergence distinction

The contradiction is confined to the iteration `BB/A` extraction. The persisted post-convergence operator is reconstructed from final net drifts and had:

- `BB` minimum off-diagonal `0.19141418136524457`;
- `BB` maximum absolute row sum `0`;
- no signed-off-diagonal authorization.

No conclusion here weakens the post-convergence pre-KFE sign contract. Signed iteration coefficients must not be called Markov transition rates.

## Conditional rebuild, engineering evidence, and fail-closed reversal

Before the boundary contradiction surfaced, a provisional A candidate was rebuilt under `SIGNED_ITERATION_COEFFICIENT_FAITHFULNESS_ONLY`:

- local fields renamed from rates to iteration coefficients;
- iteration nonnegativity guard removed without clipping, absolute values, netting, or indicator changes;
- post-convergence nonnegative-rate guard retained;
- initialization, fixture, ordering, `Bswitch`, HJB matrix/RHS, Delta, convergence rule, primitives, and tolerances unchanged.

Engineering preflights passed `21 passed in 0.69s`, including exact reproduction of row 35/column 34, signed row closure, positive component behavior, unchanged AAH/Bswitch, post-convergence guard, and primitive regressions. No converged HJB was run in engineering tests.

Successor freeze root:

`D:\ProjectTemp\ch5-matlab-faithful-negative-bb-resumption-20260830-001`

Key successor hashes before replacement execution:

- adjudication evidence `9823113CAB76AE724649CF2249038ED19B111364A3D1D14EB8850E63F05E2523`;
- policy candidate `E9BBB3A66914586C7CD3988EA875D55E7D185CB64C44D676D9F3F455E9A643C3`;
- operator candidate `B54AD548603B1DFA9BAAE62D7AB41F2150A5E42BF56C11EFEB008F299416D9A7`;
- HJB candidate `C011596696CE2819BACB0892EC4E56C21E36CD90BF949BE6B9878BD417F987B2`;
- test artifact `0FD9093385B7719F54E6ECFBB65C432B34292ECB2494E7B4F7626EFC9E376370`;
- predecessor-to-successor classification `511989C25C7E6CC744682AB1F7C65427571540384ED6DE338C9F5FA843965559`.

After the one replacement Python call failed, the provisional candidate and test were reverted. Accepted `matlab_faithful_policy.py` returned to SHA `95D74893BAD22082FB1C731AD4E35E19A69039DFC30B477F7AAACC54ED3F446E`. No unaccepted production code is published.

## Scientific ledger and comparisons

Successor scientific calls:

| Object | Calls/budget | Result |
|---|---:|---|
| MATLAB HJB | `0/0` | Reused only; no rerun or regeneration. |
| replacement Python HJB | `1/1` | Failed before valid persistence on outward upper-bound forward component. |
| comparator | `0/1` | Not run because no valid Python object exists. |

Historical frozen MATLAB facts remain: 50 states, converged true, 9 iterations, statistic `3.882012578060312e-08`. No Python convergence/output hash, full-array differences, operator differences, or scientific mismatch list exists. Comparator mismatch list is empty because comparator calls are zero.

Source/environment failure list contains exactly:

1. frozen external MATLAB iteration operator boundary closure is not equivalent to designated source `Y`/`spdiags` behavior;
2. replacement Python correctly failed before persistence when that omitted outward component was encountered.

## Scope and closeout

No MATLAB HJB rerun occurred. No designated MATLAB source, fixture, parameters, grid, ordering, initialization, Delta, crit, maxit, comparator, or tolerance changed. No corrected `policies.py`, `hjb.py`, `generator.py`, KFE, or steady-state route changed. No D1-D3, KFE, stationary distribution, steady state, asset-tail, transition, IRF, dynamics, calibration, or Results work occurred.

Final repository changed path is exactly this report. Pre-publication worktree otherwise matches live authority.

Acceptance level: negative coefficient source terms are diagnosed, but the frozen iteration operator is disqualified as an exact designated-source extraction. Full HJB parity remains unaccepted.

The PASS-only KFE next gate is not authorized. A new live task must first authorize a corrected source-extracted MATLAB HJB-only evaluator/iteration-operator boundary assembly and explicitly state whether the already-consumed MATLAB scientific object may be replaced. No further Python/comparator rerun is authorized here.

`MATLAB_FAITHFUL_NEGATIVE_ITERATION_BB_ADJUDICATION_AND_HJB_RESUMPTION_BLOCKED`
