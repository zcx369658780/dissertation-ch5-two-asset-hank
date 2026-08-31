# MP4B nonconverged-HJB post-loop source-semantics adjudication report

Date: 2026-08-31

## Terminal verdict

`MP4B_NONCONVERGED_HJB_POSTLOOP_SOURCE_SEMANTICS_ADJUDICATION_AND_ZERO_SCIENCE_VALIDATION_ADAPTER_REPAIR_PASS`

Established:

- `MP4B_MATLAB_HJB_NONCONVERGENCE_POSTLOOP_KFE_AGGREGATE_SEMANTICS_FROZEN`;
- `MP4B_PYTHON_STATIONARY_ABORT_ON_HJB_NONCONVERGENCE_SOURCE_SEMANTICS_MISMATCH_CONFIRMED`;
- `MP4B_PYTHON_MULTI_PROVINCE_SOURCE_POSTLOOP_HOUSEHOLD_ADAPTER_STATIC_PASS`.

This is source adjudication and validation-only composition evidence. It does
not accept stationary parity and consumed zero scientific/model calls.

## Live continuity and immutable identities

- live task authority/start HEAD: `103e407f766159696872cd8e9d448721ebe5398e`;
- required direct parent: `e31a2ac4ffb487be8e5883cc71f0947bf6b7cdbf`;
- repository: `zcx369658780/dissertation-ch5-two-asset-hank`;
- start worktree: clean;
- `economics.py`: `F2B67D393D7495A83281C259F6D9CC5F8AFF18B3C4ABDEB7A07F354582DEF2D1`;
- `matlab_faithful_policy.py`: `ECF56FAA7E87A0F5156E5866F1873556D6603E98AA33C8E41C400FD016C75CDC`;
- standalone export: `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3`;
- accepted MP2 `one_turn.py`: `D18C4385745E33E917B79994CAA069BE8825C9F22919A5A9EDE918845312D98D`;
- accepted MP3 `steady_state.py`: `7065D0FCBFDA6A88C8F773DEBDF277F6E300A8E0195B7CC635F7A0033D74D88C`;
- predecessor validation entry: `05E0240820FDE9F6CA07C9D0643F45EEAF72D3CE7AD21BE643C59AF51B0476A9`.

No historical R5 or `chapter5_model` runtime dependency was found.

## Protected root and line-level semantic map

`C:\MatlabProgram` was independently read as a Junction with exactly the target
`D:\MatlabProgram`. The exact accepted roots are therefore:

- logical: `C:\MatlabProgram\2023年12月2日 多省份神经网络HANK`;
- physical: `D:\MatlabProgram\2023年12月2日 多省份神经网络HANK`.

Logical and physical reads produced identical required hashes:

| Protected source | SHA-256 | Line-level contract |
|---|---|---|
| `HANK_2ASSETS_HJB.m` | `049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE` | 39 initializes `convergent=0`; 248–255 alone set it true; 256–260 only print at `maxit`; 262–333 rebuild final policies/operator; 334–345 solve and normalize KFE; 347–372 aggregate; 397–425 publish aggregates and unchanged flag |
| `HANK_mp_1turn.m` | `D3D03F37286ED66202673EA63D49BABCE8D5309BAC9C13793C8E60585C21FECF` | 13–16 call and retain every provincial household result without a flag veto; 21–66 consume the complete batch in the rest of the turn |
| `HANK_mp_1eq.m` | `ED39E661AF951E01D1F5F9D123CE0FAD980F5D3DB33FD338DE60DA87731E0AEF` | 7–8 complete the turn; 26–34 sum flags; 42–45 require `convergent_total==31`; 46–65 continue adaptation/damping when the predicate fails and error only at outer exhaustion |

Explicit answers:

1. MATLAB continues through post-loop operator rebuild, KFE and aggregates when
   HJB `convergent=false`: **yes**.
2. `HANK_mp_1turn` aborts because one household flag is false: **no**; it stores
   the returned result and completes the turn.
3. `HANK_mp_1eq` sums the flags and requires all 31 only for current outer-loop
   acceptance; a false flag vetoes acceptance but does not itself abort the
   controller.

Committed semantic map:
`validators/multi_province/mp4b_nonconverged_hjb_source_semantics_map.json`,
SHA-256 `6A4FD1576100D7CE36787EAA7E6B833ACED2D94B89B929EC6ADD45559995C028`.

## Python adjudication and classification

The accepted standalone HJB primitive returns a result containing
`converged`, `iterations`, `convergence_statistic` and
`post_convergence_operator`, including when `converged=false`. Its convenience
`solve_household_steady_state` wrapper instead raises at lines 631–638 before
KFE and aggregation when the flag is false. The predecessor validation driver
called that wrapper, so turn-2 Shanxi aborted before the MATLAB source post-loop
path.

Accepted classification:

`PYTHON_IMPLEMENTATION_ERROR__MULTI_PROVINCE_DRIVER_ABORTS_BEFORE_MATLAB_SOURCE_POSTLOOP_KFE_AND_AGGREGATES`

This replaces the predecessor's broader raw-HJB implementation classification.
No evidence here says that the 100-iteration HJB arithmetic itself differs; the
confirmed mismatch is handling of its false convergence flag.

## Validation-only adapter and exact composition

Adapter:
`validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py`,
SHA-256 `8A6308870606A02886E9A8E4B32E942A7D433237405E6B9E86EE4175FB2DFF06`.

The bounded validation driver after routing/diagnostic repair has SHA-256
`9033218710204CA4EA2AF0351376E47BB5B4F203923E6155DC4776ADD336091E`.

Exact composition:

1. call accepted `solve_matlab_faithful_hjb` exactly once;
2. do not branch on or coerce `hjb.converged`;
3. pass `hjb.post_convergence_operator.full` to accepted
   `solve_matlab_faithful_stationary_kfe` exactly once with the unchanged grid
   shape and spacings;
4. call accepted `aggregate_stationary_household` exactly once with the HJB
   consumption/labor and KFE density;
5. return `HouseholdSteadyStateResult(hjb, kfe, aggregates)` and therefore
   preserve the exact HJB flag, iterations and statistic.

The validation driver now uses only this adapter and persists
`hjb_converged`, `hjb_iterations` and `hjb_statistic` in each household's
diagnostic row. `PreFrozenHouseholdOutputBatch.converged` still receives the
unmodified flag, and accepted MP3 logic still counts false flags as an outer
acceptance veto.

No retry, second HJB call, tolerance, extra iteration, fallback, clipping,
alternate KFE, alternate aggregate, formula change or import-time model work
was added. Accepted production/export and MP2/MP3 arithmetic were unchanged.

## Static/stub validation

The focused suite uses only AST/source/hash checks and injected stub HJB/KFE/
aggregation callables. Both `converged=false` and `converged=true` cases prove
the identical call sequence `HJB → KFE → aggregate`, exactly once each. It also
proves exact diagnostic propagation, absence of retry loops, driver routing,
protected and accepted-source hashes, forbidden-runtime absence and zero
module-import scientific calls.

- focused pytest: `8 passed`;
- `py_compile`: PASS;
- `git diff --check`: PASS.

## Complete zero-model ledger

| Operation | Calls |
|---|---:|
| Python stationary top-level | 0 |
| real Python household solve | 0 |
| real Python HJB / KFE / aggregation | 0 / 0 / 0 |
| turn-2 Shanxi replay / second-province replay | 0 / 0 |
| MATLAB stationary / household / HJB / KFE | 0 / 0 / 0 / 0 |
| MP2 / MP3 scientific execution | 0 / 0 |
| comparator science | 0 |
| other year / annual batch | 0 / 0 |
| shocks / AR1 / transition / dynamics / IRF | 0 / 0 / 0 / 0 / 0 |
| historical R5 / Results | 0 / 0 |

Only source reads, hashing, AST/compile checks and stub call-accounting ran.
Production/export mutation count: `0`.

## Changed paths and forbidden-operation audit

- `validators/multi_province/mp4b_nonconverged_hjb_source_semantics_map.json`;
- `validators/multi_province/mp4b_matlab_source_postloop_household_adapter.py`;
- bounded routing/diagnostic update to `validators/multi_province/mp4b_python_empirical.py`;
- `tests/test_mp4b_matlab_source_postloop_household_adapter.py`;
- bounded CURRENT roadmap update;
- this report.

Forbidden-operation audit: PASS. No protected MATLAB, production/export,
accepted MP2/MP3, canonical data/cache, project rule, historical R5 or prior
scientific artifact was modified or executed.

## Git closeout

Explicit-path staging, one execution commit, one non-force push, GitHub
read-back of every changed path, `HEAD == origin/main`, ahead/behind `0/0` and a
clean worktree are required and recorded after publication.

## Exactly one recommended next gate

Authorize one reauthorized Python-only corrected-calendar-2009 stationary
invocation using the source-postloop household adapter and the same immutable
MATLAB baseline, with a fresh no-overwrite root and separately frozen one-shot
budget; MATLAB rerun remains zero.
