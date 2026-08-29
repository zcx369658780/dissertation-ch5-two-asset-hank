# Chapter 5 Two-Asset HANK Post-P5 D2 Comparator Categorical-Terminal Semantics and Resumption Report

## Terminal classification

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The categorical-terminal comparator correction and its one-shot engineering preflight passed completely. The single authorized replacement D2 MATLAB scientific call was then consumed and failed in the frozen scientific evaluator at `d2_matlab_heterogeneous_corrected>cert_root` line 25: after `fzero`, `assert(abs(f(x))<=1e-12)` failed while processing the reached `lower_a_active` path. The process exited nonzero and no `d2_matlab.json` was persisted.

Per the live task, no repair or rerun occurred. D2 Python/comparison and all D3 stages were not entered. This is a newly exposed D2 root-certification source/environment blocker, not a scientific mismatch. P5 remains Owner-accepted and the voluntary dynamic hold continues.

## Live authority and continuity

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Worktree: `D:\ProjectTemp\ch5-pre-p5-controlled-household-exec-repo-20260829`.
- Branch: `codex/ch5-adjustment-boundary-redesign`.
- Live start `origin/main`: `262fdd9734a1f30f8cc210e83410a3f6ff7ba7b4`.
- Live task: `tasks/CH5_TWO_ASSET_HANK_POST_P5_D2_COMPARATOR_CATEGORICAL_TERMINAL_SEMANTICS_AND_RESUMPTION.md`.
- P5 marker: `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`.
- Hold marker: `DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`.
- Accepted Python baseline: `7a2388a2ba89073e307f05a909570e8c40a4be13`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`: empty.

All controlling predecessor task/report paths were present on live main.

## Artifact roots

- Original household-decision root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-artifacts-20260829-220000`.
- Accepted D1/resumption root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-resumption-artifacts-20260829-223000`.
- Accepted D2 input-container root: `D:\ProjectTemp\ch5-post-p5-d2-container-resumption-artifacts-20260830-001000`.
- Comparator/heterogeneous predecessor root: `D:\ProjectTemp\ch5-post-p5-d2-comparator-heterogeneous-resumption-artifacts-20260830-070000`.
- Current fresh successor root: `D:\ProjectTemp\ch5-post-p5-d2-categorical-terminal-resumption-artifacts-20260830-083000`.

## D1 re-verification and zero calls

D1 artifacts were rehashed successfully:

- MATLAB `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`;
- Python `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`;
- comparison `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`.

Accepted D1 remains `432/432 PASS`, `216/216` low-`a` PASS, every scalar maximum difference `0`, and all sign/direction mismatches `0`. D1 MATLAB/Python/comparison calls in this task: `0/0/0`.

## Reused heterogeneous serialization evidence

| Artifact | SHA-256 | Status |
|---|---|---|
| corrected heterogeneous D2 MATLAB | `A7034181F3FC902E39EAB64CB8ED47C77BA52087B4E262325CAD33BAAECE3589` | reused; invoked once scientifically |
| frozen D2 Python | `DD9DDCB675BE7A5C3A672CF1936AB7CBA1553AC8334989B2CDAA777FB2914344` | reused; not run |
| comparator with `gap/bound` before terminal correction | `EBF1B72AC4ED53791646C5E06345D5D31FE06E16B6E81E618AD73229801EF0AF` | verified |
| frozen D3 MATLAB | `5D94EDF89259D543758E490EA25C9359C1B65588CF7BB0557EEEDFA6B7FF3F9A` | reused; not run |
| frozen D3 Python | `6054A0C59E7C0CD0C83AD1919C3CFAF7B2987D0545EE4CEB26B3345FF2D01ABC` | reused; not run |
| scientific manifest | `D46DD0968DA65C592863A9D33FD5FB58059E707432816A67A74CE4DF7AB1BEDA` | verified |
| accepted MATLAB heterogeneous preflight result | `815C6703FECE0438B0584C3AD16A1A772D3A42D2AA57C7F2A4FBA0BF6F6808A4` | reused; new calls `0` |

The accepted serialization contract remains nine native 16-field normal rows plus one native 10-field `lower_b_fz_near_tie` row, with no fabricated fields or union schema.

## Pre-correction categorical and terminal logic

Existing D2 normal categorical fields were `a_direction`, `b_direction`, and `boundary_feasible`; their mismatch loop already appended failures. Existing D1/D3 categorical fields were `transfer_sign`, `a_direction`, and `b_direction`; they used the same terminal failure loop.

Existing near-tie categorical fields were `canonical`, `raw`, and `alias_available`; before correction their dedicated loop produced `categorical_stats` only. Near-tie `boundary_feasible` already flowed through the D2 normal categorical loop and was terminal.

The final comparator output and exit were already derived from `not failures`. Therefore only the three near-tie categorical fields required correction.

## Complete comparator diff

```diff
 if stage=='d2':
  for f in ('canonical','raw','alias_available'):
-  bad=[i+1 for ... if mismatch];cats[f]=dict(...)
+  bad=[]
+  for i,(a,b) in enumerate(zip(M['rows'],P['rows'])):
+   if f in a and f in b and a[f]!=b[f]:bad.append(i+1);failures.append(dict(field=f,index=i+1,matlab=a[f],python=b[f]))
+  cats[f]=dict(mismatch_count=len(bad),indices=bad)
```

Every changed line classification: `COMPARATOR_CATEGORICAL_TERMINAL_SEMANTICS_ONLY`.

No comparison field, tolerance, expected value, order, numerical path, `gap/bound` rule, final aggregation, or exit line changed.

Frozen corrected artifacts:

| Artifact | SHA-256 |
|---|---|
| corrected comparator | `FAF1A6ABB9F21E7DABD6CFB0857A72354CC3A5D0D532F4968F027E5CBBC0ECB5` |
| corrected comparator preflight | `786A641168F2D70D9FCF37DAD7BA943AFC5CDFC3BB461FD59CA55A156DA25836` |
| comparator diff | `E70933E90B9409C09268BEED5D85F4D21240C34EE23CE8BA6C4C386AD62EFC06` |
| execution ledger | `BD4CBF2351BE4A9D4AFD82364B51BFD7D83E777CFCE0F26BAF475314729DA2DF` |
| successor freeze | `0DBD8AC2F9966DBAF509CA3ECB913139DCBB1FFECF25E2329276C1C6B20B9492` |
| final execution results | `551FFF404B4FB70877A1A1077EF7F60BA62725CDC0790F1C7C09B731C535F7F2` |

## Corrected comparator preflight

- invocation count: `1`;
- result: PASS;
- result SHA-256: `52F55586BAFA456BC811E4CAD885F7C26DD30FF9F15165C405515C6CEAB1D0F9`;
- matching normal/near-tie fixtures: exit `0`, failures `0`;
- numerical negatives `gap`, `bound`, normal `c`: each exit `2`, failures `1`;
- near-tie categorical negatives `canonical`, `raw`, `alias_available`, `boundary_feasible`: each mismatch count `1`, failures `1`, exit `2`;
- normal categorical negatives `a_direction`, `b_direction`, `boundary_feasible`: each mismatch count `1`, failures `1`, exit `2`;
- new MATLAB heterogeneous preflight calls: `0`.

## D2 replacement outcome and call ledger

Historical D2 MATLAB scientific calls remain:

1. input-container blocker: `1`;
2. zero-field output-container blocker: `1`;
3. later schema/comparator-authority tasks: `0`;
4. current replacement D2 MATLAB: `1`.

The replacement process entered the frozen D2 evaluator and reached `lower_a_active`. It failed in `bracket_root -> cert_root` after `fzero` because `assert(abs(f(x))<=1e-12)` was false. MATLAB reported nonzero exit status `0x00000001`.

Persistence/read-back:

- `d2_matlab.json`: absent;
- D2 Python/comparison calls: `0/0`;
- D3 MATLAB/Python/comparison calls: `0/0/0`;
- same-task repair/rerun: `0`.

Consequently:

- D2 nine-normal-case per-field maxima/worst cases: `NOT_REACHED_BEFORE_VALID_PERSISTENCE`;
- near-tie full comparison: `NOT_REACHED`;
- D2 categorical/numerical/KKT/boundary mismatch counts: `NOT_AVAILABLE`;
- D3 360-case maxima/worst cases/categorical mismatches: `NOT_REACHED`.

Scientific mismatch list: empty. No valid D2/D3 comparison occurred.

Source/environment failure list contains exactly one entry:

| Stage | Case/path | Failure | Interpretation |
|---|---|---|---|
| replacement D2 MATLAB | `lower_a_active`, `bracket_root -> cert_root` | post-`fzero` residual assertion `abs(f(x))<=1e-12` failed; no output persisted | newly exposed frozen external root-certification blocker; no scientific PASS/FAIL inferred |

## Forbidden-operation check

- D1 rerun: no;
- accepted MATLAB preflight rerun: no;
- corrected comparator preflight rerun: no;
- failed D2 repaired/rerun: no;
- D2 Python/compare or D3 entered: no;
- source/tests/helpers/cache modified: no;
- comparator fields/tolerances/order/expected values changed: no;
- D2/D3 cases/science/roots/KKT/multipliers changed: no;
- union schema/fabricated fields: no;
- taper, bare-`a` oracle, `Tt/rb_gap`, hard-coded outputs: no;
- full HJB/KFE/steady state, P3/P4/R4, asset-tail, AR(1), transition, IRF, dynamics, calibration extension, Results: `0`;
- P5 revoked/reissued: no.

## Git status, acceptance, and next gate

At report freeze, this report is the sole repository change; `src/tests` remain unchanged and no unrelated paths are present. Final remote identity and clean status require post-publication verification.

Acceptance level: categorical-terminal comparator semantics and its preflight are accepted for this evidence chain; D2/D3 remain incomplete because the only replacement D2 MATLAB call failed before persistence. D1 and P5 remain accepted; the dynamic hold continues.

Exact recommended next gate: publish only the smallest D2 external root-certification diagnosis/correction task centered on `lower_a_active` and the frozen `cert_root` residual assertion. It must preserve the equation, case, bracket, root target, `1e-12` certification tolerance, and all scientific outputs; first determine whether the blocker is root-solver configuration/representation plumbing or a genuine inability to certify the frozen root. Any future replacement D2 call requires explicit new authority. D1 and the accepted comparator/MATLAB preflights must remain reuse-only.
