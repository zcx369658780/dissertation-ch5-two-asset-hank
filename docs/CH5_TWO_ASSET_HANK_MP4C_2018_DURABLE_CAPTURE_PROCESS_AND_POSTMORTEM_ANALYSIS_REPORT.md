# MP4C 2018 durable diagnostic: terminal execution report

## Terminal verdict

`MP4C_2018_DURABLE_FIRST_SINGULARITY_CAPTURE_UNHANDLED_INSTRUMENTATION_FAILURE__NO_SECOND_CHILD__NO_POSTMORTEM`

The single task-authorized 2018 scientific child terminated after the first
MATLAB-faithful HJB returned, but before the HJB-return ledger row could be
written and before KFE entry.  The failure is an instrumentation-scoping error,
not a KFE-singularity observation.  No second child was started; no scientific
repair, solver change, input change, or postmortem was performed.

## Authority and immutable input

- Fresh state before edits: `HEAD == origin/main ==
  1a7ba3c890a2856a783f6f345c67617c28e09b4b`, direct parent
  `7f89498a0398dc9a0c14b38f3851c72ed93b612f`, ahead/behind `0/0`, tracked
  worktree clean.
- Input: `calendar_2018_matlab_runtime_cache_input.json`, SHA-256
  `F84D25FD49A76229CA49958764D1167CAA56FB68CF99A4ED7B20C508812E6ED0`.
- Binding verified before launch: 2018, entry 10, PLM/calendar row 19,
  2009–2018 window, 31 provinces, `GDP` times 1000,
  `R语言计算资本存量` times 1000, and `就业人数` times 100.  No 2023 input was
  admitted.
- The child inherited exactly `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`,
  `OPENBLAS_NUM_THREADS=1`, and `NUMEXPR_NUM_THREADS=1`.

## Durable-capture preparation

The diagnostic-only code was changed to fsync JSON/CSV/array/sparse evidence,
persist raw A/A-prime/contaminated matrix/RHS/raw solve vector before any dense
analysis, stop with a dedicated capture exception, and reserve SCC/SVD/rank work
for `postmortem()` after child termination.  It also added the required
HJB-return ledger and a zero-science test.  Production HJB/KFE callables,
adapter arguments, scientific model code, input, grids, tolerances, controls,
and KFE construction were not changed.

Focused zero-science validation passed before the scientific launch:

```text
python -m py_compile validators/multi_province/mp4c_2018_first_singularity_diagnostic.py tests/test_mp4c_2018_first_singularity_diagnostic.py
python -m pytest -q tests/test_mp4c_2018_first_singularity_diagnostic.py
1 passed
```

The test deliberately generated a dummy `MatrixRankWarning`; it verified raw
capture first and separate read-only postmortem second.  It made no production
stationary, household, HJB, KFE, MATLAB, or R/PLM calls.

## One-child execution record

The preferred `...-001` root was reserved by a pre-launch PowerShell failure:
the command resolved the Python executable as an array and `Start-Process`
rejected it.  No PID was created and no Python/model child started.  That root
is preserved and was not reused.

One detached child, PID `40568`, was then launched in the distinct fresh root:

`D:\ProjectTemp\ch5-mp4c-2018-durable-first-singularity-capture-20260903-002`

It was the sole scientific child (`workers=1`, `subprocesses=1`, reruns `0`).
The child finished naturally and wrote terminal status `UNHANDLED_EXCEPTION`.
Its bounded-science ledger records one started household call.  The traceback
shows that `faithful.solve_matlab_faithful_hjb` had returned into `hs`, then the
new ledger expression attempted to assign `hjb_writer` without declaring it
`nonlocal` in that nested function:

```text
UnboundLocalError: cannot access local variable 'hjb_writer'
where it is not associated with a value
```

Therefore the sole child reached one HJB return but appended zero HJB-return
rows; it entered no KFE call.  No raw first-singularity matrix exists, and no
SCC/rank/nullity postmortem was authorized or run.

## Evidence and execution identity

The external audit manifest is
`D:\ProjectTemp\ch5-mp4c-2018-durable-first-singularity-capture-20260903-002\audit_manifest.json`.
It hashes the preflight, launch receipt, input identity, child code identity,
both ledgers, traceback, terminal sentinel, child-exit receipt, and stdout/stderr.

The child recorded the following pre-execution code identities:

- `exports/matlab_faithful_two_asset_ha.py`:
  `B92F6EFC59D9398F89F8FB6EE67BF6C5F947282D76895051BEC194967EC9C3E3`
- `mp4b_matlab_source_postloop_household_adapter.py`:
  `8A6308870606A02886E9A8E4B32E942A7D433237405E6B9E86EE4175FB2DFF06`
- `stationary_runtime.py`:
  `226BE912AB776F57A8D8EFACE912AB2A3331E865638AC36976F6D578BDB086A0`
- diagnostic script at child launch:
  `6DEB4A28CFA1CB84C393AC686D4495E2C8B3707A2E689D95996AF08F411CB861`

## Boundaries and next gate

This run supplies no evidence about a 2018 KFE singularity, its operator
structure, or a root cause.  The only supported classification is an
instrumentation failure after HJB return and before KFE entry.

The one-child budget is consumed.  A future attempt requires a newly published
task that explicitly authorizes a corrected HJB-return-ledger closure and a new
scientific execution budget.  This task must not launch another child or infer a
KFE diagnosis.
