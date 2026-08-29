# Chapter 5 Two-Asset HANK post-P5 D2 Python check_boundary arity correction and resumption report

## Terminal classification

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The bounded external `check_boundary` call-shape correction and one-shot interface preflight passed. The single replacement D2 Python call then exited zero and persisted all ten frozen native-schema rows. The accepted comparator's single call was consumed and failed before comparison because it indexed the accepted native heterogeneous MATLAB top-level list as a mapping (`M['rows']`). No repair or rerun followed, and D3 was not reached. P5 remains Owner-accepted as `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`; the voluntary hold remains `DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`.

## Live authority and continuity

- Live start `origin/main`: `10a36e249676edbdef64ca34886f3118446600b1`.
- Start branch/HEAD after fast-forward: `codex/ch5-adjustment-boundary-redesign` / `10a36e249676edbdef64ca34886f3118446600b1`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`: empty.
- Final `origin/main` immediately before report publication: `10a36e249676edbdef64ca34886f3118446600b1`; publication commit is recorded by push/read-back and final handoff.

## Artifact roots and accepted reuse

- Accepted D1 root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-resumption-artifacts-20260829-223000`.
- UTF-8 predecessor root: `D:\ProjectTemp\ch5-post-p5-d2-python-utf8-resumption-artifacts-20260830-071738`.
- Fresh successor root: `D:\ProjectTemp\ch5-post-p5-d2-python-boundary-arity-resumption-artifacts-20260830-073132`.

D1 hashes were directly re-verified: MATLAB `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`, Python `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`, comparison `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`. D1 calls were exactly `0/0/0`. Accepted D1 remains `432/432 PASS`, including `216/216` low-`a` PASS, all scalar maxima `0`, and all sign/direction mismatch counts `0`.

The persisted D2 MATLAB output was reused at SHA-256 `26F9E628021327D02897FE96A2FBAA52D1AF4434629676E03BD6614708D6E977`; D2 MATLAB calls were exactly `0`. Read-back remained ten ordered cases with field counts `16,16,16,16,16,16,16,16,16,10` and no fabricated union fields.

The accepted UTF-8-corrected D2 Python harness was rehashed as `C60CF89CCCC01E359D1F8BBB9D8918132E0569B463AD524101D66F51DE1483F7`; accepted UTF-8 preflight result `5E3C17CC617EF03AE8D80D55736F2A79B7124A6E6DE16C630F54A69386025EF0` was reused. The explicit `encoding='utf-8'` line remained unchanged. Manifest `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA`, comparator `FAF1A6ABB9F21E7DABD6CFB0857A72354CC3A5D0D532F4968F027E5CBBC0ECB5`, D3 MATLAB `5D94EDF89259D543758E490EA25C9359C1B65588CF7BB0557EEEDFA6B7FF3F9A`, and D3 Python `6054A0C59E7C0CD0C83AD1919C3CFAF7B2987D0545EE4CEB26B3345FF2D01ABC` were unchanged. No accepted diagnostic or preflight was rerun.

## Static production and call-shape audit

The live production signature is exactly:

```python
check_boundary(i_a, i_b, n_a, n_b, mu_a, mu_b, tolerance)
```

It exposes seven positional-or-keyword parameters in that order. The accepted UTF-8 harness contains exactly one call:

```python
check_boundary(*idx,3,3,ma,mb,tol)
```

Every `record` invocation supplies a three-element tuple `(i_a,i_b,i_z)`: `(1,1,0)`, `(0,2,0)`, `(2,0,0)`, `(1,0,0)`, `(2,1,0)`, or `(2,2,0)`. Therefore the original call expands to eight arguments: `i_a,i_b,i_z,n_a,n_b,mu_a,mu_b,tolerance`.

- `idx[0]`: illiquid-asset grid index `i_a`;
- `idx[1]`: liquid-asset grid index `i_b`;
- `idx[2]`: productivity-state index `i_z`.

Production boundary feasibility is defined only on the two asset-grid indices. Omitting `idx[2]` is therefore exactly consistent with the API; `n_a=3`, `n_b=3`, `mu_a=ma`, `mu_b=mb`, and `tolerance=tol` remain unchanged. No other harness call expands `idx` or presents an analogous arity issue.

The accepted historical report `CH5_TWO_ASSET_HANK_MATLAB_PYTHON_HA_P2_PYTHON_HARNESS_API_ARITY_CORRECTION_AND_COMPLETION_REPORT.md` established the identical semantics and exact correction. Current static evidence matched it, so authority `D2_PYTHON_CHECK_BOUNDARY_ASSET_INDEX_ARITY_CORRECTION` was frozen.

## Complete arity-only correction

```diff
-bc=check_boundary(*idx,3,3,ma,mb,tol)
+bc=check_boundary(idx[0],idx[1],3,3,ma,mb,tol)
```

The actual complete one-line diff preserves all surrounding scientific evaluation code. Its only changed line is classified exactly `BOUNDARY_API_ARITY_PLUMBING_ONLY`. No `idx` value, case, dimension, drift, tolerance, KKT rule, root, multiplier, parameter, output, or UTF-8 decoder changed.

| Frozen artifact | SHA-256 |
|---|---|
| arity-corrected D2 Python | `AF59E680B216AF6820E3E418D311CC1760DF83237E75A88A281B33F18BDAF932` |
| complete diff | `667D84256615B47F9270CFCE2F7C9F3BCB4516DEE8DF15C2526C5046EC63EA70` |
| interface preflight | `9728A352FAB17BC1B9187813771FC5DF7BCF45273F88248D3E3681179F2CFC66` |
| frozen ledger | `27E57AA0C50422CA7E30C0D6790C4D5F7A85246C6FF65893A8056A8A32D25A80` |
| successor freeze | `B301BADE06E6A463F0281B38943A58C8CA9FEF0712F1D6BB1E33ED7FA6239C4E` |

## One-shot interface preflight

- Calls / exit: `1 / 0`.
- Result SHA-256: `BEAE0726E679F3DD24EBEB2978A2E35D47B99CD8FD732EBB4506D307820E052E`.
- Production parameter names/order/count: exact seven, PASS.
- Original/corrected expanded argument counts: `8 / 7`.
- Only `idx[2]` removed; all seven accepted values preserved: PASS.
- Synthetic lower/lower, upper/upper, interior/interior, and mixed boundary calls: `4/4` executed successfully.
- Return fields `feasible`, `violation`, `active_a`, `active_b`: present.
- Only call site changed; UTF-8 line unchanged: PASS.
- Scientific case loop executed: false.

## D2 Python persistence and ledger

Historical/current D2 Python calls:

1. default-GBK blocker: `1`;
2. UTF-8-corrected arity blocker: `1`;
3. current arity-corrected replacement: `1`.

The current replacement exited zero and persisted `d2_python.json`, SHA-256 `C8FF69CDD8DDF6F742CB0A98D562D4020DB65E69A3D04BC7A90C34B95199227B`. Independent read-back found `stage=D2`, `case_count=10`, ten rows in frozen order, nine native 16-field normal rows and one native 10-field `lower_b_fz_near_tie` row, with no fabricated fields.

## D2 comparator blocker

The accepted comparator was invoked exactly once. It loaded the accepted MATLAB payload as a Python list because the native heterogeneous serialization is a ten-element top-level array of row wrappers. The comparator then executed:

```python
len(M['rows'])
```

and exited `1` with:

```text
TypeError: list indices must be integers or slices, not str
```

No `d2_compare.json` was persisted. This is a comparator input-container/source blocker before any ten-case numerical or categorical comparison, not a scientific mismatch. It was not repaired or rerun.

| Stage | Calls | Result |
|---|---:|---|
| D1 MATLAB/Python/compare | `0/0/0` | accepted reuse |
| D2 MATLAB | `0` | accepted output reused |
| interface preflight | `1` | PASS |
| replacement D2 Python | `1` | valid ten-row persistence |
| D2 comparator | `1` | MATLAB native-container blocker |
| D3 MATLAB/Python/comparator | `0/0/0` | not reached |

Because comparison did not begin, D2 nine-normal-case maxima/worst cases, near-tie categorical/numerical `gap`/`bound`, and numerical/KKT/boundary mismatch counts are unavailable. D3 360-case results are unavailable. Complete scientific mismatch list: empty. Complete source/environment failure list: the single comparator native-MATLAB-container shape blocker above.

## Prohibitions, acceptance, and next gate

- Production source/tests/helpers/cache and production `check_boundary`: unchanged.
- Manifest, accepted D2 MATLAB output, comparator, scientific cases/order/equations/roots/KKT/multipliers/parameters/states/shadows/derivatives/outputs/tolerances: unchanged.
- D1, D2 MATLAB, and accepted diagnostics/preflights: not rerun.
- Failed comparator: not repaired or rerun.
- No taper, bare-`a` oracle, `Tt/rb_gap` adapter, hard-coded expected output, HJB/KFE/steady state, P3/P4/R4, asset-tail, AR(1), transition, IRF, dynamics, calibration extension, or Results execution.
- Repository change before closeout: exactly this report; explicit-path staging only.
- Acceptance level: arity correction/preflight and D2 Python persistence accepted as bounded evidence; full D2 comparison and supplementary parity remain unaccepted.

Exact recommended next gate: authorize only a static audit and minimal external comparator input-container normalization that maps the accepted native ten-element MATLAB wrapper array to the comparator's existing ten-row semantic view without changing fields, values, order, tolerances, categorical terminal rules, or the accepted comparator's comparison logic; require one no-science container preflight and one explicitly authorized replacement D2 comparison. D1, D2 MATLAB/Python persisted outputs, UTF-8/arity evidence, and all accepted diagnostics/preflights must remain reuse-only.
