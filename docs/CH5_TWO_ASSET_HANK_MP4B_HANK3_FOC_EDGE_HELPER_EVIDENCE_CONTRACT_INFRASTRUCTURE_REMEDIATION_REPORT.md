# Chapter 5 Two-Asset HANK MP4B HANK3_FOC edge-helper evidence-contract infrastructure remediation report

Date: 2026-08-31

Terminal verdict:

`MP4B_HANK3_FOC_EDGE_HELPER_EVIDENCE_CONTRACT_INFRASTRUCTURE_REMEDIATION_PASS`

Acceptance marker:

`MP4B_RAW_VB_HANK3_FOC_EDGE_HELPER_EVIDENCE_CONTRACT_REMEDIATION_PASS`

## Live continuity and identities

- live authority: `5dd527716641caa5099c0ead719dadfef9adaab8`;
- direct parent: `cfa33bab76122dccfa7ab92577b754be237cae2c`;
- execution branch was fast-forwarded to live authority with `HEAD == origin/main`, ahead/behind `0/0`, and clean worktree before mutation;
- predecessor helper SHA-256: `33AC7212BF6D3F27A11761B2FD29DB713E63DFDE1356B5002FE5B9ED1166AF69`;
- remediated helper SHA-256: `F98FC7D1AADA01A39693951F4CD266A7174727975FBBFE55E54343867D7E11E0`;
- focused test SHA-256: `16B104744FC3EC9364237A856379D9463BB083D841C966E18B4056AED3E0E14A`;
- accepted smoke helper remained unchanged at `8F3D7E87CDFA63510505042F938286DC58BAA4F734253C74520AF91742BB601E`;
- accepted smoke manifest remained unchanged at `A82DC905E7D057EBE0645E3C8F3331F438CF939716762B17AC5C9B270B758D8B`.

Protected MATLAB and production/export identities were rechecked before mutation and remained task-exact. No historical R5 / `chapter5_model` runtime dependency was introduced.

## Final helper signature

```matlab
mp4b_raw_vb_hank3_foc_edge_diagnostic(run_root, logical_root, physical_root)
```

The helper itself now owns creation of the run root and all future artifacts.

## Exclusive fresh-root and no-overwrite contract

The helper:

1. normalizes the caller-supplied `run_root`;
2. requires its parent to equal exactly `D:\ProjectTemp` rather than using prefix or substring trust;
3. rejects an existing file or directory at that path;
4. calls non-recursive `java.io.File(char(run_root)).mkdir()` and fails unless it exclusively creates the directory;
5. performs this sequence before any future protected call;
6. creates artifacts only inside the owned root;
7. atomically reserves each artifact with `java.io.File(...).createNewFile()` before opening the new empty file with `'w'`;
8. checks complete JSON write length and closes the file before returning or rethrowing.

Neither deletion, reuse, truncation of an existing artifact, `fopen(...,'x')`, nor recursive creation is used.

## Durable first-source-error contract

Immediately before the frozen protected expression, `attempted_calls` is incremented. Only that protected call is enclosed in a bounded `try/catch`:

```matlab
value = HANK3_FOC(dummy,chi,pa(k),pb(k),a(k),0);
```

On the first future protected-source error, the helper writes `failure.json` with:

- schema and `PROTECTED_SOURCE_ERROR` status;
- exact case id and one-based index;
- `pa`, `pb`, `a`, `chi0`, `chi1`;
- verified resolved helper path and SHA;
- original MATLAB error identifier and message;
- exact logical and physical roots;
- attempted and completed protected-call counts;
- complete explicit call ledger.

After the failure artifact is durably closed, the helper uses `rethrow(protected_error)`. It never assigns a substitute number, continues to a later case, or rewrites the original identifier/message.

## Per-row and success schemas

Each future successful typed row includes:

- `case_id`, `pa`, `pb`, `a`, `chi0`, `chi1`;
- `resolved_helper_path`;
- `resolved_helper_sha256`;
- `ratio_class`, `ratio_value`;
- `output_class`, `output_value`.

Only after all ten future calls complete does the helper reserve and write `success_manifest.json`. It contains the exact roots, junction evidence, resolved protected identity, finite-root and negative-root evidence, all ten typed rows, and the complete ledger. A failed run writes only `failure.json`; a successful run does not require a failure artifact.

## Complete call-ledger schema

Both success and failure artifacts use the same explicit schema:

- `matlab_scalar_batches`;
- `HANK3_FOC_attempted_calls`;
- `HANK3_FOC_completed_calls`;
- `matlab_HJB`, `matlab_KFE`, `matlab_household`, `matlab_multi_province`, `matlab_stationary`, `matlab_GE`;
- `python_local_policy`, `python_HJB`, `python_KFE`, `python_household`, `python_stationary`;
- `old_50_state_HJB_parity`, `Beijing_household_parity`;
- `MP2_empirical`, `MP3_empirical`;
- `annual_batch`, `shocks`, `transition`, `dynamics`, `IRF`, `R5`, `Results`.

All non-scalar fields are explicitly initialized to zero. Attempted/completed counts are updated only around the exact protected expression.

## Frozen scientific content and exact-junction guard

Independent text review and focused tests proved unchanged:

- all ten ids and their exact order;
- complete `pa`, `pb`, and `a` arrays;
- `chi0=0.1`, `chi1=2` and the existing non-scientific chi fields;
- `ratio = pa(k)./pb(k);`;
- the exact protected call expression;
- `NaN`, `+Inf`, `-Inf`, `finite` classification functions;
- finite `%.17g` encoding.

No epsilon, clipping, positivity guard, alternate formula, numerical substitution, Python emulation, or case change was added.

The accepted exact C/D root strings, PowerShell Junction/sole-target proof, logical/physical/resolved protected SHA checks, finite exact two-root membership, and sibling/unrelated rejection remain intact. No `canonical_root`, `getCanonicalPath`, `startsWith`, substring, broad D-root, sibling, or filename-only trust was introduced.

## Infrastructure verification

- focused tests plus preserved exact-junction tests: `12 passed`;
- `python -m py_compile tests/test_mp4b_hank3_foc_edge_helper_evidence_contract.py`: PASS;
- MATLAB R2022b `checkcode(...,'-id')`: `0` findings;
- independent helper/test review: PASS;
- `git diff --check`: PASS.

The real helper was not invoked. No run root, success manifest, failure artifact, frozen ratio, or protected result was evaluated in this task.

## Complete zero-call and mutation ledger

- protected `HANK3_FOC`: `0`;
- replacement scalar batch: `0`;
- exact-junction smoke rerun: `0`;
- MATLAB HJB/KFE/household/multi-province/stationary/GE: all `0`;
- Python local-policy/HJB/KFE/household/stationary: all `0`;
- old 50-state parity / Beijing household parity: `0/0`;
- MP2/MP3: `0/0`;
- annual batch/shocks/transition/dynamics/IRF/R5/Results: all `0`;
- production/export mutation: `0`.

`MP4B_RAW_VB_TRANSFER_FOC_SOURCE_EDGE_SEMANTICS_FROZEN` remains NOT AUTHORIZED / NOT REACHED.

## Forbidden-operation check

PASS. Only the authorized edge helper, focused test, and this report changed. The accepted smoke helper, protected MATLAB, production/export, faithful/corrected/reference, canonical input/cache, MP2/MP3, historical R5, and Results paths were not modified or executed.

## Git closeout

Explicit-path staging only. One execution commit, one non-force push, GitHub read-back of all three paths, `HEAD == origin/main`, ahead/behind `0/0`, and clean worktree are required.

## Exactly one recommended next gate

Publish a fresh replacement validation-only ten-case `HANK3_FOC` scalar edge-semantics task using helper SHA-256 `F98FC7D1AADA01A39693951F4CD266A7174727975FBBFE55E54343867D7E11E0`, with one scalar batch, exactly ten protected calls on full completion, reruns zero, every model call zero, no production/export mutation, no helper changes after preflight, and no exact-junction smoke rerun.
