# MP4C call-725 first-iteration closure

Date: 2026-09-07. Task: `CH5_MP4C_CALL725_FIRST_ITERATION_CLOSURE`.

**Outcome: FIRST_ITERATION_PARITY_PASS.** The complete required first iteration
passes the frozen comparison contract using both previously persisted outputs.
All 53 required comparison/consistency checks pass; no genuine mismatch remains
in this exact-input first iteration. No fresh model acquisition was necessary.
This is a Builder diagnostic result submitted for Reviewer acceptance.

## Authority, workspace and preservation

Remote was verified as `git@github.com:zcx369658780/dissertation-ch5-two-asset-hank.git`
before `git fetch origin`. Fresh live main and task baseline were
`13316a86374e6b87f3a299d2ce890510ab842ec1`; the closure task was active there.
Actual working directory is
`D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001`.
The initially clean docs-sync branch at
`d2f3e6e7cc21fffe8807f577ec2262bb77afdc07` was preserved; the same worktree
was switched to a new branch from fresh main:
`codex/ch5-call725-first-iteration-closure-20260907`.
No additional Git worktree was needed. The original main checkout and its
70 untracked files were not used or changed; Zotero was not a repository work target.

New external evidence directory:
`D:\ProjectTemp\ch5-call725-first-iteration-closure-20260907-001`.
Final summaries and manifest are in its `validated/` subdirectory; initial
comparison drafts in the parent are retained and superseded by this final set.
Earlier evidence roots were read-only. The final comparator, small machine-readable
summaries, source/input identities and a finite manifest accompany this report.

## Evidence and stage contract

The two reused core outputs were freshly hash-verified:

| Output | SHA-256 |
| --- | --- |
| MATLAB `matlab_core_stagewise.mat` | `B863BBE5A3CF6327954C71520F609B9949FE9DEF64BA5225AA4CE9661392B69E` |
| Python `python_strict_stagewise.npz` | `CEAE235AC0DC62C1FCD0D9728F840DEEA1E12038ABFCE73CA0DA6BD449CE915F` |

All five Python sparse sidecars were verified against the predecessor manifest.
The authoritative initialization MAT, scalar binding, both capture wrappers,
protected HJB source and frozen Python export identities passed. The Python
Git blob remains `9e7dc9556a2b76811e78f89999abecc045886106`.
Accepted wrapper/evaluator source attribution and physical-path equivalence
were reused; their relevant receipts are bound in `input_source_identity.json`.
No production module was imported by the comparator.

Both outputs' `b`, `ah/a`, `z`, `old/V0` and `l0` match the direct-loaded
authoritative MAT exactly. Tensor coordinates remain `(b,a,z)=(20,20,2)`;
MATLAB row/column vectors are normalized only to their designated vector shape.
The persisted MATLAB `updated(:)` equals the F-order view of its tensor exactly.

`stage_map.json` records MATLAB fields, corresponding Python fields and stage
semantics. `VbF/VbB` versus `vb_f/vb_b` are the primary boundary-adjusted
derivatives. MATLAB labels `-1/0/+1` map to Python `B/0/F` by the frozen source
branches. Python does not persist separate internal boolean masks: the five
explicit label-derived views match MATLAB `Ic_B/Ic_F/Ic_0/Idh_B/Idh_F` exactly.
These views express consumed branch meaning, not independently captured masks.

The historical raw-vb full-array diagnostic still has 40 forward and 40 backward
differences. They are confined to uncomputed Python raw boundary slots versus
MATLAB post-boundary slots. Each defined interior quotient domain is exactly
equal. Both raw-va arrays also match exactly. No diagnostic row was silently
dropped, and no uncomputed boundary derivative was manufactured.

## Complete stage results

Continuous values use `abs(x-y) <= 128*eps64*max(1,abs(x),abs(y))`.
Scaled difference below means absolute difference divided by that frozen bound.
Shapes/order and categorical objects are exact; NaN/Inf fail. Sparse support
ignores exact stored zeros only, with no epsilon pruning.

| Stage | Checks passed | Largest scaled difference |
| --- | ---: | ---: |
| Exact MAT input bindings and old/V0 | 11/11 | 0 |
| Equivalent va and post-boundary vb derivatives | 6/6 | 0.00006104 |
| Consumed labels and equivalent branch views | 7/7 | 0 |
| Consumption, labor, transfer, cost, effective illiquid return | 5/5 | 0.012627 |
| mu_a, mu_b, utility | 3/3 | 0.0625 |
| bb, bf, ab, af | 4/4 | 0.022747 |
| BB, AAH, Bswitch, A | 4/4 | 0.025451 |
| M and RHS | 2/2 | 0.025408 |
| Tensor V1 and first-iteration statistic | 2/2 | 0.067037 |
| Within-language M/RHS/statistic identities, MATLAB vec_F and finite residual diagnostics | 9/9 | pass |

Every required object is present and finite. Mathematical support is identical
for all five sparse comparisons. Maximum absolute differences are:
`A/M=2.1316282072803006e-14`, `RHS=5.551115123125783e-17`,
`V1=3.9968028886505635e-15`, statistic `8.881784197001252e-16`.
Per-object shapes, finite status, mismatch counts, absolute/scaled differences
and sparse support counts are in `comparison_summary.json`.

## Direct-update diagnostics without a new solve

Computed from each language's persisted M, RHS and vec_F(V1):

| Side | Infinity residual | Normwise backward error |
| --- | ---: | ---: |
| MATLAB output, postprocessed in Python | `2.7047808437430376e-14` | `1.4206876991016253e-16` |
| Python output, postprocessed in Python | `5.717648576819556e-14` | `3.0031982146222163e-16` |

Backward error divides the residual by `||M||inf*||V1||inf+||RHS||inf`.
These are fresh deterministic postprocessing results, not new MATLAB solver
measurements. No conditioning solves, regularization or alternate solver were used.

## Calls, checks and publication

New MATLAB first iterations: **0**; new Python HJB first iterations: **0**;
new direct solves and retries: **0**. Each language's conditional maximum of
two invocations remains unused; the acquisition condition was not triggered.
The historical persisted pair remains MATLAB=1/Python=1, and the earlier
unpersisted MATLAB invocation stays consumed in its original task.
Native-init, iteration 2+, KFE, household steady state, GE/annual, R/PLM,
shock/IRF and Results calls are all zero for this task.

Focused checks: fifteen synthetic comparator tests passed, covering shape rejection,
nonfinite rejection, fixed tolerance versus exact categories, sparse zero/support
and duplicate handling, label validation, F-order residuals and incomplete/mismatch
verdicts, large signed values, residual overflow and corrupted manifest outputs.
JSON round-trip and manifest readback passed. Only these focused tests
were run; no global/model regression. Changed paths are restricted to the allowed
comparator directory, one focused test, this report and the small summary directory.

A read-only helper reviewed comparator code, not scientific evidence or final
acceptance. Its findings led to explicit nonfinite-residual rejection, missing-field
receipts and hash/length manifest readback without relying on assertions. The final
comparison was repeated after these bounded comparator changes, using unchanged
artifacts and zero model calls. One summary-mirroring command initially failed
because the repository `reports/` parent was absent; creating the authorized parent
resolved this IO-only failure without any scientific retry.

The utility is reproducible with `python -B validators/multi_province/call725_first_iteration_closure/compare.py --output <fresh-evidence-directory>`
from this checkout. It reads existing inputs and outputs only; it cannot perform
conditional acquisition or call a scientific evaluator. Git publication uses
one docs/diagnostic-only commit and non-force push of the dedicated branch;
actual commit and remote readback are returned separately after publication.

No production repair is recommended for this first-iteration result. A separately
authorized follow-up may investigate multi-iteration propagation using this common
first-step baseline. This report does not establish multi-iteration convergence,
2018 stationary/annual parity or Results eligibility, and does not authorize that
follow-up. Builder stops after publication without merging main.
