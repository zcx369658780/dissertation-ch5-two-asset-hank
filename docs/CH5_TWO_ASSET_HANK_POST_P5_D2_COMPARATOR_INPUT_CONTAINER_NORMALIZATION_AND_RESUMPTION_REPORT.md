# Chapter 5 Two-Asset HANK post-P5 D2 comparator input-container normalization and resumption report

## Terminal classification

`POST_P5_SHARED_INPUT_HOUSEHOLD_DECISION_PARITY_BLOCKED_SOURCE_OR_ENVIRONMENT__DYNAMIC_HOLD_CONTINUES`

The mandatory static audit found that the accepted D2 MATLAB JSON does not match the list semantics frozen by this task. Its top-level list contains ten wrapper mappings with keys `stage`, `case_count`, and `rows`; it does not directly contain the ten scientific row mappings. Therefore the authorized `rows_view(list) -> list` adapter would expose ten three-field wrappers rather than the accepted `9 x 16-field + 1 x 10-field` row view. Producing the actual row view requires separately authorized per-element wrapper extraction. No comparator was modified, no artifact/preflight root was created, and no Python preflight, replacement D2 comparison, or D3 call was executed.

P5 remains Owner-accepted as `MATLAB_PYTHON_TWO_ASSET_HA_PARITY_ACCEPTED_FOR_DYNAMIC_EXTENSION`. The voluntary hold remains `DYNAMIC_EXECUTION_HELD_PENDING_POST_P5_HOUSEHOLD_DECISION_PARITY`.

## Live authority and continuity

- Live start `origin/main`: `5072615cf0098fbb8319a6804fd9edffe7238048`.
- Start branch/HEAD after fast-forward: `codex/ch5-adjustment-boundary-redesign` / `5072615cf0098fbb8319a6804fd9edffe7238048`.
- `git diff --name-only 7a2388a2ba89073e307f05a909570e8c40a4be13 -- src tests`: empty.
- Final `origin/main` immediately before report publication: `5072615cf0098fbb8319a6804fd9edffe7238048`; the publication commit is recorded by push/read-back and final handoff.

## Artifact roots and accepted reuse

- Accepted D1 root: `D:\ProjectTemp\ch5-post-p5-household-decision-map-parity-resumption-artifacts-20260829-223000`.
- Immediate predecessor root: `D:\ProjectTemp\ch5-post-p5-d2-python-boundary-arity-resumption-artifacts-20260830-073132`.
- Successor execution artifact root: not created because the mandatory static audit blocked before correction/preflight authoring.

D1 hashes were directly re-verified:

- MATLAB `1FCA5F613C52B2E0F5CC45EF8B06BB96ED171ADB0F79F31A709151F2E91775CF`;
- Python `1C3A63759027AC8FF0F2FD56AB090CB8584110FCD9ACAAFDF937624245324F42`;
- comparison `1B95E6D23A1409874DE2548812FD1C34E11E955A68093C0A2818B54A521712B3`.

D1 calls were exactly `0/0/0`. Accepted D1 remains `432/432 PASS`, including `216/216` low-`a` PASS, all scalar maximum differences `0`, and all sign/direction mismatches `0`.

Accepted D2 outputs were rehashed and read back without scientific execution:

| Output | SHA-256 | Calls in this task |
|---|---|---:|
| MATLAB | `26F9E628021327D02897FE96A2FBAA52D1AF4434629676E03BD6614708D6E977` | 0 |
| Python | `C8FF69CDD8DDF6F742CB0A98D562D4020DB65E69A3D04BC7A90C34B95199227B` | 0 |

After extracting the actual nested MATLAB row objects, both outputs expose the identical frozen IDs/order:

`interior_ff, interior_bb, liquid_zero, lower_a_active, lower_b_active, interior_mu_a_zero, upper_a_lower_b, upper_a_interior_b, dual_upper, lower_b_fz_near_tie`.

Both actual row views have field counts `16,16,16,16,16,16,16,16,16,10`; no union/fabricated fields were observed. All accepted comparator, UTF-8, arity, root, and heterogeneous diagnostics/preflights were reuse-only with zero new calls.

## Mandatory D2 top-level container audit

PowerShell read-back, corresponding directly to Python `json.load` shapes, established:

- accepted MATLAB D2 top-level type: array/list, length `10`;
- each MATLAB top-level element: wrapper mapping with exactly `stage`, `case_count`, `rows`;
- each wrapper's `rows` value: the actual native scientific row mapping;
- accepted Python D2 top-level type: mapping/dict;
- Python top-level keys: `stage`, `case_count`, `rows`;
- Python `rows`: the direct ordered list of ten scientific row mappings.

Thus the payloads are structurally:

```text
MATLAB: [ {stage, case_count, rows: row_1}, ..., {stage, case_count, rows: row_10} ]
Python: {stage, case_count, rows: [row_1, ..., row_10]}
```

The accepted comparator assumes mapping-with-rows in every row-consuming expression:

- initial length assertion: `len(M['rows']) == len(P['rows'])`;
- scalar loop: `zip(M['rows'],P['rows'])`;
- categorical loop: `zip(M['rows'],P['rows'])`;
- D2 near-tie categorical loop: `zip(M['rows'],P['rows'])`;
- D1 low-`a` indexing and maxima: both `M['rows']` and `P['rows']`;
- D2 KKT/boundary extras: both `M['rows']` and `P['rows']`;
- D3 extrema: both `M['rows']` and `P['rows']`;
- output case count: `len(M['rows'])`.

Loaded input metadata `stage` and `case_count` are not consulted in scientific PASS/FAIL. PASS/FAIL is determined only by the ordered row semantic views, frozen field sets/tolerances, categorical terminal mismatches, and the final `not failures` aggregation.

The exact semantic row view required by every comparison loop is an ordered list of the native row mappings themselves. A mapping payload can expose it as `payload['rows']`. The accepted MATLAB list cannot expose it by returning the list itself: that yields wrapper mappings and changes the visible schema from `16/.../10` fields to `3` fields per element. The actual native row mappings can be exposed without mutating them only by an additional wrapper-aware projection such as obtaining each existing `wrapper['rows']` object. That semantic form was not authorized by the frozen list-as-rows rule in this task.

## Static D3 serializer audit

The frozen D3 MATLAB harness builds a homogeneous preallocated struct array `rows`, then serializes one outer struct:

```matlab
out=struct('stage',stage,'case_count',k,'rows',rows)
```

The frozen D3 Python harness serializes:

```python
{'stage': stage, 'case_count': len(rows), 'rows': rows}
```

Accordingly both D3 serializers emit the supported mapping-with-rows shape. The D2 MATLAB wrapper-array asymmetry is caused by its heterogeneous cell-row serialization and is not statically present in D3. Existing comparison fields, numerical factor `128`, ULP bounds, categorical terminal logic, `gap/bound`, and `not failures` aggregation are independent of top-level metadata, but no corrected comparator was authored because D2 list semantics contradicted the current authority.

## Authority contradiction and zero execution

The task froze `COMPARATOR_TOP_LEVEL_CONTAINER_NORMALIZATION_ONLY` only if a list payload itself was the ordered row semantic view. That precondition is false for the accepted MATLAB bytes. Implementing the specified example:

```python
if isinstance(payload, list):
    return payload
```

would return ten wrapper objects, with field counts `3,3,3,3,3,3,3,3,3,3`, no direct `id` fields, and no directly comparable scientific values. This would fail the task's own required preflight conditions for identical IDs and `9 x 16 + 1 x 10` schemas.

Consequently:

- corrected comparator: not created;
- comparator diff: not created;
- execution ledger/freeze: not created;
- container preflight calls: `0`;
- replacement D2 comparator calls: `0`;
- D3 MATLAB/Python/comparator calls: `0/0/0`.

Historical consumed comparator call remains separately recorded as `1`; it was not rerun in this task.

No replacement D2 comparison output exists, so its hash and terminal comparison result are unavailable. D2 nine-normal-case per-field maxima/worst cases, near-tie `gap`/`bound` comparison, and numerical/categorical/KKT/boundary mismatch counts are unavailable. D3 statistics are unavailable. Complete scientific mismatch list: empty. Complete source/environment failure list: the frozen adapter semantics do not cover the accepted MATLAB list-of-wrapper-mappings shape.

## Prohibitions, acceptance, and next gate

- D1, D2 MATLAB, D2 Python, comparator, D3, and all accepted diagnostics/preflights: not executed.
- Persisted outputs, manifest, comparator, production source/tests/helpers/cache, rows, fields, values, order, schemas, tolerances, categorical semantics, `gap/bound`, PASS/FAIL logic, and scientific objects: unchanged.
- No taper, bare-`a` oracle, `Tt/rb_gap` adapter, hard-coded answer, HJB/KFE/steady state, P3/P4/R4, asset-tail, AR(1), transition, IRF, dynamics, calibration extension, or Results execution.
- Repository change before closeout: exactly this report; explicit-path staging only.
- Acceptance level: static blocker diagnosis only; container normalization, D2 comparison, and supplementary parity are not accepted.

Exact recommended next gate: authorize a wrapper-aware, top-level-only comparator row-view extractor for the exact accepted MATLAB form `list[{stage,case_count,rows:row_dict}]` and Python form `{stage,case_count,rows:[row_dict...]}`. It must return references to the existing nested row mappings in order, without mutating/copying row mappings, and must reject mixed or malformed wrapper lists. Require one no-science synthetic-plus-accepted-output preflight and one explicitly authorized replacement D2 comparison. D1, D2 MATLAB/Python outputs, all accepted diagnostics/preflights, and D3 remain reuse-only until that comparison passes.
