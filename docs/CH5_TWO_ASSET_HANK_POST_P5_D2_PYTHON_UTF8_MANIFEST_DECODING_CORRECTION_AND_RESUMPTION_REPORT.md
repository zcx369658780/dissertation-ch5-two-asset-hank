# Chapter 5 Two-Asset HANK post-P5 D2 Python UTF-8 manifest decoding correction and resumption report

## Terminal classification

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The explicit UTF-8 manifest correction and its one-shot engineering preflight passed. The single authorized replacement D2 Python call then reached the first frozen D2 case and failed because the external harness passed eight positional arguments to the current seven-argument production `check_boundary` interface. No repair or rerun followed. D2 comparison and D3 were not reached. P5 remains Owner-accepted as `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`; the voluntary hold remains `DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`.

## Live authority and continuity

- Live start `origin/main`: `3d30241dcca82926f6e18a5436a569cacef5e63a`.
- Start branch/HEAD after fast-forward: `codex/ch5-adjustment-boundary-redesign` / `3d30241dcca82926f6e18a5436a569cacef5e63a`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`: empty.
- Final `origin/main` observed immediately before publication: `3d30241dcca82926f6e18a5436a569cacef5e63a`; the publication commit is recorded by push/read-back and the final handoff.

## Artifact roots

- Accepted D1 root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-resumption-artifacts-20260829-223000`.
- Immediate predecessor root: `D:\ProjectTemp\ch5-post-p5-d2-lower-a-root-diagnostic-artifacts-20260830-070101`.
- Fresh successor root: `D:\ProjectTemp\ch5-post-p5-d2-python-utf8-resumption-artifacts-20260830-071738`.

## Reused evidence and zero calls

D1 was rehashed directly and remained reuse-only:

- MATLAB `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`;
- Python `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`;
- comparison `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`.

D1 calls were exactly `0/0/0`. Accepted D1 remains `432/432 PASS`, including `216/216` low-`a` PASS, all scalar maximum absolute differences `0`, and all sign/direction mismatch counts `0`.

The persisted D2 MATLAB output was rehashed as `26F9E628021327D02897FE96A2FBAA52D1AF4434629676E03BD6614708D6E977` and was not regenerated; D2 MATLAB calls were exactly `0`. Independent read-back returned ten ordered records with IDs:

`interior_ff, interior_bb, liquid_zero, lower_a_active, lower_b_active, interior_mu_a_zero, upper_a_lower_b, upper_a_interior_b, dual_upper, lower_b_fz_near_tie`.

Field counts were `16,16,16,16,16,16,16,16,16,10`: nine native normal schemas and one native near-tie schema, with no fabricated union fields.

Other accepted artifacts were rehashed and not executed:

| Artifact | SHA-256 |
|---|---|
| scientific manifest | `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA` |
| original D2 Python | `DD9DDCB675BE7A5C3A672CF1936AB7CBA1553AC8334989B2CDAA777FB2914344` |
| corrected comparator | `FAF1A6ABB9F21E7DABD6CFB0857A72354CC3A5D0D532F4968F027E5CBBC0ECB5` |
| accepted comparator preflight | `52F55586BAFA456BC811E4CAD885F7C26DD30FF9F15165C405515C6CEAB1D0F9` |
| accepted MATLAB heterogeneous preflight | `815C6703FECE0438B0584C3AD16A1A772D3A42D2AA57C7F2A4FBA0BF6F6808A4` |
| accepted root diagnostic | `6C77624B69F1ECED1E54A216ABBA8D5BF28A031B83672AA74268774B8A26268C` |
| accepted corrected-root preflight | `2B01AD00F0CCF151D6BDC3EE46E476DA4BEC63FEE3A98B34CF299B0B5EEE8AB6` |
| accepted corrected D2 MATLAB harness | `A0E3426F1FB58563821C429A119445B659933D7E321E0EFBD3A7EED4690D8E51` |
| frozen D3 MATLAB | `5D94EDF89259D543758E490EA25C9359C1B65588CF7BB0557EEEDFA6B7FF3F9A` |
| frozen D3 Python | `6054A0C59E7C0CD0C83AD1919C3CFAF7B2987D0545EE4CEB26B3345FF2D01ABC` |

No accepted diagnostic or engineering preflight was rerun.

## Static default-decoder diagnosis

The manifest path supplied to the harness was `D:\ProjectTemp\ch5-post-p5-d2-lower-a-root-diagnostic-artifacts-20260830-070101\manifest.json` in the predecessor and the unchanged copied manifest under the fresh successor root in this task.

The exact frozen load expression was:

```python
m=json.load(open(os.path.join(r,'manifest.json')))
```

It omitted an explicit encoding, so the predecessor Windows runtime selected its default GBK text decoder and failed on the unchanged UTF-8 bytes. The harness reads no other scientific input text file through that default-decoder pattern; its only other `open` is the `d2_python.json` output write. Production modules were imported at file initialization, but the decoder failure occurred before entry into the D2 case loop and before any D2 scientific case output evaluation. The manifest bytes remained exactly `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA` and were never rewritten.

This fully supported frozen authority `D2_PYTHON_MANIFEST_TEXT_ENCODING_UTF8_EXPLICIT`.

## Complete UTF-8-only correction

```diff
-m=json.load(open(os.path.join(r,'manifest.json')))
+m=json.load(open(os.path.join(r,'manifest.json'),encoding='utf-8'))
```

The actual complete frozen diff retains the surrounding one-line initialization unchanged. Its sole changed line is classified exactly `INPUT_TEXT_ENCODING_UTF8_ONLY`.

| Frozen artifact | SHA-256 |
|---|---|
| corrected D2 Python harness | `C60CF89CCCC01E359D1F8BBB9D8918132E0569B463AD524101D66F51DE1483F7` |
| complete diff | `57E38AA6A191E6F338E4D85573DF1911DC09D704E25B32E38DB257E525803318` |
| UTF-8 preflight harness | `B87F3E1C0EDD4CB4A574BA32987E39FCCA86D29316EDC17918C111C19C215BD4` |
| frozen execution ledger | `BB63774BB3EB6D417B498BF4FC218965DC17E6112B98743E9DBC7F30BFF315C2` |

No locale, codepage, or `PYTHONUTF8` environment change was used.

## One-shot UTF-8 preflight

- Calls / exit: `1 / 0`.
- Result SHA-256: `5E3C17CC617EF03AE8D80D55736F2A79B7124A6E6DE16C630F54A69386025EF0`.
- Manifest SHA before/after: identical accepted `D46DD096...BEDA`.
- Explicit UTF-8 decode and JSON parse: PASS.
- D2 count/order: exact frozen ten IDs, PASS.
- Chinese path: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`, exact and without replacement characters.
- Semantic in-memory JSON round-trip equality: PASS.
- Manifest rewritten: false.
- Production model imported/called: false.

## Replacement D2 Python outcome

Historical and current ledger:

1. predecessor default-GBK blocker: `1` consumed call;
2. current explicit-UTF-8 replacement: `1` consumed call.

The replacement passed manifest decoding and began the first frozen `interior_ff` case. It then exited `1` without producing `d2_python.json`:

```text
TypeError: check_boundary() takes 7 positional arguments but 8 were given
```

The frozen external call is `check_boundary(*idx,3,3,ma,mb,tol)`, while `record` receives three-element tuples such as `(1,1,0)`. Expansion therefore supplies eight positional arguments. The accepted production signature is exactly `check_boundary(i_a, i_b, n_a, n_b, mu_a, mu_b, tolerance)`, seven positional arguments. This newly exposed external harness/interface arity blocker occurred before valid D2 Python persistence. It was not repaired or rerun.

| Stage | Calls | Result |
|---|---:|---|
| D1 MATLAB/Python/compare | `0/0/0` | accepted reuse |
| D2 MATLAB | `0` | accepted persisted output reused |
| accepted diagnostics/preflights | `0` | accepted reuse |
| UTF-8 engineering preflight | `1` | PASS |
| replacement D2 Python | `1` | interface-arity blocker; no output |
| D2 comparator | `0` | not reached |
| D3 MATLAB/Python/comparator | `0/0/0` | not reached |

Because no valid D2 Python output existed, D2 per-field maxima/worst cases, near-tie `gap`/`bound`, categorical/numerical/KKT/boundary mismatch counts, and D3 360-case statistics are unavailable. Scientific mismatch list: empty. Complete source/environment failure list: the single `check_boundary` positional-arity blocker above.

## Prohibition, acceptance, and next gate

- Production MATLAB/Python source, tests, helpers, and cache: unchanged.
- Manifest bytes/semantics, persisted D2 MATLAB output, comparator, cases, equations, roots, KKT, multipliers, parameters, states/shadows/derivatives, outputs, and tolerances: unchanged.
- D1, D2 MATLAB, and accepted diagnostics/preflights: not rerun.
- No taper, bare-`a` oracle, `Tt/rb_gap` adapter, hard-coded expected answer, HJB/KFE/steady state, P3/P4/R4, asset-tail, AR(1), transition, IRF, dynamics, calibration extension, or Results execution.
- Failed replacement D2 Python: not repaired or rerun.
- Repository change before closeout: exactly this report; explicit-path staging only.
- Acceptance level: explicit UTF-8 input-decoding correction and preflight accepted; supplementary parity remains unaccepted because D2 Python persistence/comparison and D3 were not reached.

Exact recommended next gate: authorize only a static audit and minimal external D2 Python `check_boundary` call-shape/arity correction that preserves the accepted seven-argument production interface and every frozen scientific object, followed by one no-model interface preflight and one explicitly authorized replacement D2 Python call. The accepted UTF-8 preflight, unchanged manifest, persisted D2 MATLAB output, D1, comparator qualification, and all MATLAB/root diagnostics must remain reuse-only.
