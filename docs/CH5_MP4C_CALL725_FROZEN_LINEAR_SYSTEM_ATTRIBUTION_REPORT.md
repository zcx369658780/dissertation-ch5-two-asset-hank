# P32 frozen linear-system attribution

Date: 2026-09-07. Task: `CH5_MP4C_CALL725_FROZEN_LINEAR_SYSTEM_ATTRIBUTION`.

**FROZEN_LINEAR_SYSTEM_ATTRIBUTION_COMPLETE__TRAJECTORY_AND_GENERATOR_BLOCKERS_OPEN**

All eight prescribed solves and solve-free diagnostics completed. Both fresh
originating-language ORIGINAL solutions are bit-identical to their predecessor
solutions. For genuinely identical stored linear inputs, MATLAB/Python differ
beyond the unchanged bound on both origins and both representations. Within-solver
input perturbation effects also exceed the bound. Their vector cancellation
exactly reconstructs the previously observed split; neither contribution can be
assigned a causal percentage by adding infinity norms.

Fixed binary row scaling leaves both Python solutions bit-identical and changes
MATLAB solutions. It does not improve cross-language agreement or consistently
improve original-equation backward accuracy. At the extreme stored diagonal,
the sigma shift has already been lost in both systems. These findings identify
linear arithmetic/input/representation effects, not a full nonlinear trajectory
cause, production repair, independently proven condition number or valid generator.

## Authority, paths and preserved state

Verified remote: `git@github.com:zcx369658780/dissertation-ch5-two-asset-hank.git`.
Fresh `git fetch origin main` gave live main
`80ce3f25ecc4455df15206d6ecab3909552f1b61`. Its rule index and status designate
this exact task. The predecessor acceptance and report were read; related
local-file/MATLAB/Python rules and frozen export were unchanged from the already
read versions. The previous clean branch was preserved, and the new branch
`codex/ch5-call725-frozen-linear-system-20260907` starts at that live main.

Actual repository directory:
`D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001`.
New evidence directory:
`D:\ProjectTemp\ch5-call725-frozen-linear-system-20260907-001`.
Read-only predecessor:
`D:\ProjectTemp\ch5-call725-policy-operator-stability-20260907-001`.
The original main checkout and its previously reported 70 unrelated untracked
files were not touched or re-inventoried. Historical branches, Zotero and global
configuration were preserved. No conflicting external instruction required a pause.

The predecessor manifest digest matches its existing readback:
`EB213BD4174AB1145A332674D5D49326A7A5B4B51C17839524DA12A992203C23`.
Only consumed science artifacts/runtime-source entries were checked. Historical
CURRENT-document hashes were not compared to updated live files. Exact consumed
paths, fields and hashes, including both predecessor receipt hashes, are published
in `reports/call725_frozen_linear_system_20260907/consumed_inputs.json`.
The inherited P32 common input hash is
`094B4B0815335B4C6257E6EE14C9FC75186CD7792BC3CD6BAC6D996486334FA4`.
Scalar binding was loaded from its manifest-provided exact path and verified as
`A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6`.
The export blob remains `9e7dc9556a2b76811e78f89999abecc045886106` by Git
comparison. No model export/helper was imported or executed; the protected HJB
identity is inherited, not a fresh source-directory audit.

## Exact systems and fixed representation

M-origin is predecessor `matlab_P32/step_0001.mat`, fields `matrix,rhs,updated`
plus saved `A,initial_value`. P-origin is `python_P32/step_0001_M.npz` and
`python_P32/step_0001.npz`, fields `rhs,v1,old`, plus `step_0001_A.npz`.
The saved input tensors equal the exact pre-step32 common tensor. No evaluator
was used to regenerate matrices or solutions.

Both 800x800 binary64 systems have 3663 stored nonzeros, no duplicate coordinates,
and no explicit positive/negative sparse zeros. M-origin storage is CSC,
P-origin CSR; canonical triplets are sorted row then column. Original storage
order hashes, data/RHS bit hashes, support hashes, dimensions and dtype are in
`systems.json`. Common MAT files store sparse CSC; Python loads into CSR and
MATLAB retains sparse. No ordering/pivot/solver options were overridden.

Each payload contains canonical row/column coordinates and binary64 reference
bits. Preparation and both actual solver processes independently checked exact
loaded values, support and RHS bits before solving. Loaded sparse matrices/RHS
were persisted and cross-checked again from disk. All eight checks pass. Signed
zeros are separately recorded; only exact sparse zeros may be removed. RHS
column association is the original F-order `(b,a,z)` indexing, not C-order.

Before any new solve, each origin's ROW_POW2 file was prepared once using
`s_i=max_j(abs(M_ij)); k_i=1-frexp_exponent(s_i)` for nonzero rows and zero
for zero rows, with `ldexp` applied to entries and RHS. Both exponent ranges are
[-68,2], with no zero rows. Scaling factors/results are finite; support is
unchanged; no overflow/underflow occurs; reverse scaling recovers every original
matrix/RHS bit. Scaled hashes and exponents were frozen before execution and
never tuned. All four systems were eligible.

## Crossed solutions and originating-language replay

The frozen rule remains `abs(x-y)<=128*eps64*max(1,abs(x),abs(y))`.
All x are finite binary64 vectors of length800. Full comparison rows, including
representative F-order coordinates, are published in `comparisons.json`.

| Common linear payload | MATLAB solve | Python solve | Cross-language max abs | Max scaled | Material coordinates | Result |
| --- | --- | --- | ---: | ---: | ---: | --- |
| M ORIGINAL | completed | completed | 2.802202914153895e-13 | 4.557530133662654 | 383 | FAIL |
| P ORIGINAL | completed | completed | 1.6830981053317373e-13 | 2.738929942147486 | 314 | FAIL |
| M ROW_POW2 | completed | completed | 4.587441537751147e-13 | 7.443459762669312 | 404 | FAIL |
| P ROW_POW2 | completed | completed | 4.4941828036826337e-13 | 7.313384580532408 | 401 | FAIL |

Originating ORIGINAL MATLAB(M) and Python(P) replays are both **bit-identical** to
their respective saved predecessor values. The copied complete prior P32 stage
comparison and provenance-labelled replay-fidelity summary are also published;
the predecessor's hand-written test count remains explicitly distinct from a
parsed raw test log.

| Within-solver comparison | Max abs | Max scaled | Material coordinates |
| --- | ---: | ---: | ---: |
| M-origin vs P-origin, MATLAB ORIGINAL | 8.748557434046234e-14 | 1.4234275475391591 | 327 |
| M-origin vs P-origin, Python ORIGINAL | 3.6060043839825084e-13 | 5.864840679134608 | 446 |
| M-origin vs P-origin, MATLAB ROW_POW2 | 5.45785638905727e-13 | 8.881648809760183 | 628 |
| M-origin vs P-origin, Python ROW_POW2 | 3.6060043839825084e-13 | 5.864840679134608 | 446 |
| ROW_POW2 vs ORIGINAL, MATLAB M | 1.8118839761882555e-13 | 2.897917959897342 | 319 |
| ROW_POW2 vs ORIGINAL, MATLAB P | 2.815525590449397e-13 | 4.579030086793174 | 381 |
| ROW_POW2 vs ORIGINAL, Python M | 0 | 0 | 0 |
| ROW_POW2 vs ORIGINAL, Python P | 0 | 0 | 0 |

The first six rows fail; both Python representation comparisons pass exactly.
Overall there are 14 prescribed solution comparison rows, four passing and ten
failing. Failed comparisons are results, not retry triggers.

Let MM=x_matlab(M-origin), PM=x_python(M-origin), MP=x_matlab(P-origin),
PP=x_python(P-origin), all ORIGINAL. The saved arrays establish exactly:

`MM-PP = (MM-PM)+(PM-PP) = (MM-MP)+(MP-PP)`.

Both reconstructed vectors are bit-identical to `MM-PP` and the prior stored
split. Infinity norms are: split 8.881784197001252e-14; fixed-M solver effect
2.802202914153895e-13; Python input effect 3.6060043839825084e-13; MATLAB input
effect 8.748557434046234e-14; fixed-P solver effect 1.6830981053317373e-13.
Their cancellation is visible in the saved vectors; norms are not additive and
no causal percentages are inferred. Both fixed-input solver arithmetic and
within-solver input sensitivity contribute at this checkpoint.

## Residual arithmetic and scaling assessment

All ten saved/fresh solutions were evaluated against **both original stored
systems**; each fresh ROW_POW2 solution was additionally evaluated against the
scaled system it actually solved: 24 solution/system residual evaluations,
each in three arithmetic conventions, with no further solves.

1. Ordinary binary64 CSR matvec and subtraction.
2. `math.fsum` of already rounded binary64 products together with negative RHS.
3. Independently implemented Decimal arithmetic at 80 decimal digits, converting
   every stored binary64 operand via `Decimal.from_float`, then multiplying and
   summing at precision80. This is residual evaluation, not a high-precision solve.

Normwise backward error is `||r||inf/(||M||inf*||x||inf+||b||inf)`.
Componentwise error is `max_i |r_i|/(sum_j |Mij|*|xj|+|bi|)`; Decimal80 uses
the same exact-operand interpretation for numerator and denominator. 0/0 is0;
a positive numerator over zero is an explicit nonfinite diagnostic. No new
admissibility thresholds were assigned. All present diagnostics are finite.
Full metrics, row coordinates and equation units are in `residuals.json`;
ordinary/compensated vectors and Decimal80 residual strings remain external.

The table uses Decimal80 and always measures against each solution's own
**unscaled original** system, allowing a meaningful representation comparison.

| Solution | Residual infinity norm | Normwise backward error | Componentwise backward error |
| --- | ---: | ---: | ---: |
| MATLAB M ORIGINAL | 110742.0644100 | 6.267088651e-17 | 1.661226577e-16 |
| Python M ORIGINAL | 110742.0636934 | 6.267088611e-17 | 5.833124299e-16 |
| MATLAB M ROW_POW2 | 65454.9347565 | 3.704210148e-17 | 1.604465673e-16 |
| Python M ROW_POW2 | 110742.0636934 | 6.267088611e-17 | 5.833124299e-16 |
| MATLAB P ORIGINAL | 65454.9353871 | 3.704210184e-17 | 1.545493397e-16 |
| Python P ORIGINAL | 110742.0644960 | 6.267088656e-17 | 6.445824493e-16 |
| MATLAB P ROW_POW2 | 65454.9359891 | 3.704210218e-17 | 1.754035859e-16 |
| Python P ROW_POW2 | 110742.0644960 | 6.267088656e-17 | 6.445824493e-16 |

Scaling reduces measured original-equation backward error for MATLAB M, does
not improve MATLAB P (componentwise error increases), and changes neither Python
solution nor its original-equation residual. There is no general accuracy or
forward-error claim because no exact/high-precision reference solution exists.

Residual computation itself matters: MATLAB M ORIGINAL ordinary norm is
99888.38887093746, compensated rounded-product norm 99889.13103776655, and
Decimal80 norm 110742.06441001686. For MATLAB P ROW_POW2 against P ORIGINAL,
ordinary is 162255.63246084965, compensated 162254.89029402056, but Decimal80
is 65454.93598905609. Compensated summation cannot recover the information lost
when extreme products were already rounded. The synthetic tests explicitly
exercise this distinction.

In scaled equation units, Decimal80 residual norms are approximately
1.282814198e-15 / 2.848138980e-15 (M, MATLAB/Python) and
1.276154425e-15 / 2.863809548e-15 (P). Those small numbers largely reflect equation
units; they alone are not an improvement in accuracy. Componentwise errors
match their original-equation values to residual precision, as expected for
the exact positive power-of-two row scaling.

## Diagonal representation and observed runtime warnings

The largest diagonal is row704, tensor `(4,15,1)`, in both stored systems.
M-origin Mii is approximately 3.967603707987486e20; P-origin is
3.9676037079874857e20. Local binary64 spacing is **65536**. In both origins,
`Mii+Aii` equals0 in ordinary, compensated and Decimal80 arithmetic; exactly one
row per origin has this complete cancellation. From exact scalar operands,
sigma=rho+1/Delta is
`0.05100000000000000277555756156289135105907917022705078125`;
its binary64 evaluation is0.051000000000000004. Thus the saved diagonal contains
none of this intended shift at row704. No regeneration of A or M is used to make
that observation, and scaling the already stored entries cannot restore it.

Row704 A sum from exact stored operands is
-6850.804651896158854185170383743752609007060527801513671875 in both origins;
the M row sum is its positive counterpart. A particular ordinary CSR reduction
gives -6851.137985229492; fsum gives -6850.804651896159. These differences reflect
representation and reduction, not new boundary leakage. Top eight diagonal
rows per origin, spacings, sigma discrepancies and row sums are retained in
`representation.json`. This finding does not quantify the full solution error
of losing sigma or prove the condition number of an intended mathematical operator.

MATLAB ORIGINAL solves both emitted `MATLAB:nearlySingularMatrix`, reporting
`RCOND = 9.152423e-22`; scaled solves emitted no warning. This is an observed
diagnostic from the unchanged backslash call, not an independently run condition
estimator or proof of a particular condition number. No warning triggered a retry.
Python emitted no warnings. Original raw logs are retained. MATLAB warning JSON
contains replacement characters; its original GB18030 console bytes were decoded
into `warnings_summary.json` without rerunning a solve.

Observed versions: Python3.11.9, NumPy2.4.6, SciPy1.17.1; MATLAB9.13.0.2049777
(R2022b), PCWIN64, observed MKL2021.3 BLAS/LAPACK strings. `scikits.umfpack` is
unavailable. Installed SciPy `spsolve` dispatch source is snapshotted; its fallback
indicates SuperLU for this configuration, an inference from availability/source,
not direct factorization instrumentation. MATLAB sparse-factorization backend
was not instrumented. No solver or global settings were changed.

## Calls, checks, artifacts and next question

| Language | Process attempts | Entered invocations | Entered solves | Completed / durable solves | Retries |
| --- | ---: | ---: | ---: | ---: | ---: |
| MATLAB | 4 | 4 | 4 | 4 / 4 | 0 |
| Python | 4 | 4 | 4 | 4 / 4 | 0 |

All processes exited0. MATLAB process wall times were 34.969, 8.281, 8.734,
6.563seconds; Python 0.593, 0.578, 0.578, 0.563seconds. Python's worker monotonic
timer reported0 at its available resolution; process timings and durable counters
show the actual solves. Every process was below five minutes. Evidence-window
timestamps and duration are in `engineering_notes.json`.
HJB/policy/evaluator, trajectories, KFE, GE/annual, dynamics/IRF, Results, refinement,
inverse/eigen/SVD, condition-estimator and high-precision-solution calls are0.
Earlier task budgets remain consumed.

**11 focused tests pass**, parsed from the preserved actual unittest log rather
than entered as a handwritten count. Checks cover duplicate rejection, exact
zero handling, fixed exponents/reverse scaling, one-ULP binding rejection,
mocked single-solve persistence, pre-solve invalid-input rejection, single solver
entrypoints, ordinary/fsum/Decimal residual distinctions, zero-denominator
conventions and absence of analysis solver calls. Synthetic tests mock the solver;
they perform no additional scientific solve. Initial and expanded test logs are
retained; the final raw log is published as `focused_tests.log`, with hash and
parsed count in `checks.json`. These are local Builder checks, not independently
executed Reviewer tests. No unrelated model regression was run.

Changed paths are limited to the task's validator directory, one test file, this
report and `reports/call725_frozen_linear_system_20260907/`. Large MAT/NPZ and
residual vectors stay outside Git. Published summaries include exact payload and
consumed-input receipts, full comparison rows, previous P32 stage rows, residual
metrics, vector attribution, representation diagnostics, warnings, ledger and
the test log. The finite manifest binds source/runtime snapshots, consumed input
receipt, payloads, outputs, analysis and report. Its digest/readback counts are
published in `evidence_manifest_receipt.json`; self and terminal receipts are
excluded to avoid circular hashes. Commit and remote SHA are returned after
non-force publication; Builder does not merge main or start a successor.

The smallest justified next work is a bounded, solve-free specification of
admissible boundary-generator behavior on the already saved problematic states:
identify the upper-b forced-transfer and upper-a signed-rate laws requiring a
scientific decision, and define the conservation/sign constraints a proposed
repair must satisfy. Reviewer/Owner must authorize a change to those laws or
transfer FOC arithmetic. Fixed row scaling is not established as a production
repair and cannot recover the lost diagonal shift. The nonlinear convergence
gap and signed-generator/boundary-leakage blockers remain open; no annual or
Results acceptance follows from this diagnostic completion.
