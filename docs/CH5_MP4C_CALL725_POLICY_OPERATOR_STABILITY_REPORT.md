# Call-725 policy/operator stability and four common states

Date: 2026-09-07. Task: `CH5_MP4C_CALL725_POLICY_OPERATOR_STABILITY`.

**Diagnostic scope complete. Verdict:
`COMMON_STATE_IMPLEMENTATION_OR_NUMERICAL_DIFFERENCE_LOCALIZED`.**
M24, P24 and M143_FINAL pass all 38 common-state comparisons. P32 passes 36/38:
the first failing stage is the direct value update V1, followed by its statistic.
All preceding policies, operators and M/RHS pass the unchanged comparison rule.
This localizes a numerical update/sensitivity question, not a demonstrated formula
defect or proof of ill-conditioning. The independent-trajectory convergence gap
remains unresolved. This is a Builder submission, not full parity or Results acceptance.

## Authority, workspace and evidence

Remote verified as `git@github.com:zcx369658780/dissertation-ch5-two-asset-hank.git`.
Fresh fetch gave main `a55019d4a6fe7b36eb783223e8b20dbc73fa59fb`; its rule index
and status designate this exact task. The clean predecessor branch at
`dedd0f8e5fa894b83c8b20e522d66893e7b6b377` was preserved. New branch
`codex/ch5-call725-policy-operator-stability-20260907` starts at fresh main.

Actual repository directory:
`D:\ProjectTemp\ch5-astra-local-doc-sync-20260907-001`.
All repository commands explicitly used this directory. No files were changed
in the Zotero starting repository or original main checkout; its previously
reported 70 untracked files were left untouched, not freshly inventoried.
No nested AGENTS files were found in the four allowed parent directories.
The task and repository agreement apply to Chapter 5; Zotero-only rules do not.
No unresolved external instruction conflict was encountered.

New evidence root:
`D:\ProjectTemp\ch5-call725-policy-operator-stability-20260907-001`.
The predecessor root `D:\ProjectTemp\ch5-call725-multi-iteration-trajectory-20260907-001`
was read-only. Its inventory SHA-256 was verified against
`6D77926997A566E94FE3F016E2BD632042D22276D20D07997DCAB287749E46FC`.
Only consumed predecessor artifacts were checked against that inventory; no
redundant audit of all 3715 files was performed. `consumed_*.json` records them.
The predecessor manifest also binds the accepted comparator, wrappers and frozen inputs.

Protected HJB SHA-256 remains
`049136B769560040BC678F828F5D3EC5338DDCAA2090D6BED4E40732F56C3EAE`;
Python export blob remains `9e7dc9556a2b76811e78f89999abecc045886106`;
scalar binding SHA-256 remains
`A40D088C63FC1F7EDECEA561D649B42959C646DF528ED13298014493DB4808F6`.
Initialization and both helper hashes were verified. Each invocation retained
exact runtime wrapper/export/helper snapshots, a process receipt, log, worker
ledger and durable core output. Protected sources and production code were not edited.

## Four fixed common states

Each case generated a fresh MAT with exact `v0,b,ah,z,l0`; both evaluators loaded
that same file. Exact array readback and original immutable-array equality passed.
`states.json` records source file, field and hashes. P32 uses pre-step32 `old`;
M143_FINAL deliberately uses post-step143 `updated`. Cases were never chained.

| Case | Authoritative V0 | Passed fields | First failure | V1 max absolute difference |
| --- | --- | ---: | --- | ---: |
| M24 | MATLAB step24 `initial_value` | 38/38 | none | 2.930988785010413e-14 |
| P24 | Python step24 `old` | 38/38 | none | 3.1530333899354446e-14 |
| P32 | Python step32 `old` | 36/38 | V1, stage 9 | 8.881784197001252e-14 |
| M143_FINAL | MATLAB step143 `updated` | 38/38 | none | 4.0190073491430667e-14 |

Originating-language replay fidelity passes 38/38 for M24, P24 and P32 against
their saved originating steps. Maximum scaled cross-language differences are
0.5062056444204426, 0.5445452597760854, 1.546875 and 0.9277014820782395,
respectively. The 1.546875 is P32's statistic; its V1 maximum scaled error is
1.4168286451819037, with 296 material coordinates. One failing V1 coordinate
is zero-based `(0,4,1)`: MATLAB -1.8469455194103488, Python -1.8469455194102924.

P32 M/RHS agree within the frozen rule, not bitwise. M has identical 3663-entry
mathematical support; max absolute difference 65536 at its extreme scale and
max scaled difference 0.171875. RHS max absolute difference is
1.1102230246251565e-15, max scaled 0.023022358163977682.
The source solves are MATLAB `matrix\rhs` (task wrapper line 76) and Python
`spsolve(M,rhs)` (line 47). Their P32 statistics are 0.4831963882124546 and
0.4831963882124106. The present evidence cannot separate different factorization
rounding from sensitivity to the small nonzero M/RHS differences. No condition
estimator, crossed-system solve or retry was run.

P32 residual infinity norms, recomputed from stored operands, are
99888.38887093746 (MATLAB) and 99888.39357064449 (Python). Corresponding normwise
backward errors are 5.65286001861887e-17 and 5.652860284583403e-17 at
`||M||inf` approximately 7.93520741597497e20. Small backward errors do not establish
generator validity, conditioning or nonlinear convergence. Residuals for every
new step are in `replay_comparisons.json` and `replay_summary.json`.

The comparison uses `128*eps64*max(1,abs(x),abs(y))`, exact shapes/categories and
F-order vectorization. Sparse support removes only exact stored zeros; there is
no densification or epsilon pruning. NaN/Inf fails. Primary vb fields are
post-boundary; pre-boundary interior arrays remain diagnostics. Python mask
views derive from persisted labels and are not independent captures.

## First discrete split and source arithmetic

The saved trajectories independently identify first transfer-label and BB-support
splits at step24. The tensor coordinate is `(5,19,0)`, physical
`(b,a,z)=(-0.1578947368421053,10,0.8)`. The BB support coordinate is `(385,386)`
in zero-based F-order: MATLAB 0, Python 0.008136836711852648.

All candidate/margin values below are **source-formula reconstruction from
persisted inputs, not independent runtime capture**. Consumed labels, transfer,
cost and sparse rates are persisted. Local reconstructed controls/rates pass
the frozen comparison against those captures. Full operands are in `first_split.json`.

At the upper-a boundary the negative backward-a candidate is used. For candidate
FB, MATLAB has vaB=0.005587078234509324, vbF=0.006155877561657759, ratio
0.9076006107250679. Python has vaB=0.005538346889118895,
vbF=0.006158278769242083, ratio 0.8993335795028512. The signed margin to the
FOC lower threshold 0.9 is +0.00760061072506793 versus -0.0006664204971487953.
Thus MATLAB dF=0; Python dF=-0.0033321024857439763 and costF=0.0003343205392719477.
The `sdhF - 1e-12` decision margins are -1e-12 versus +0.0029977819454720285,
giving transfer labels 0 versus F. Both liquid labels are B. No b-boundary
override applies at this cell; the upper-a rule sets the forward-a rate to zero.
M24 and P24 each pass same-state replay, so this observed split is a
different-state threshold crossing, not a demonstrated same-state branch defect.

Source locations: protected `HANK3_FOC.m:19`, Python export lines 103–108;
upper-a candidate/label logic at Python lines 306–355 and task MATLAB lines 61–70.
The two-state BB difference follows `bf=Ic_F*scF/db + Idh_F*sdhF/db` with
db=0.368421052631579. No threshold was changed.

## Operator growth and generator properties

All 143 MATLAB and 500 Python stored steps were reduced without a new evaluator.
Peak norm rows and their complete sparse entries are in `operator_growth.json`.

| Existing step | Norm-driving cell / matrix row | Raw vbB | Consumed transfer | Persisted cost | bb rate | M infinity norm |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| MATLAB 57 | (4,10,1) / 604 | 3.0642452568991576e-7 | -3590145.3165697316 | 2.4489376038911714e12 | 6.647106611446365e12 | 1.329422689765389e13 |
| Python 32 | (4,15,1) / 704 | 1.0727926483663655e-13 | 33970754456.593735 | 1.4617487339442027e20 | 3.967603707342041e20 | 7.935207415974971e20 |

P32's positive BF candidate uses vaF=0.0009232372496771557 over the tiny vbB,
ratio 8605924463.43708. Its positive BB candidate is excluded from dB; BF is
consumed. The quadratic adjustment cost dominates `sdhB=-dB-costB`; F is false
and B true. `bb=-(scB+sdhB)/db` then drives matrix entry (704,703), with
diagonal (704,704)=3.9676037079874857e20 and forward-a contribution
64544433468.862015. M57 consumes the sum of negative BB=-3594383.006266297
and positive BF=4237.689696565053, producing the same cost/rate amplification
mechanism with opposite transfer sign. Its largest off-diagonal is (604,603).

The consumption/labor floor 1e-6 is active for the consumed backward liquid
derivative in both cells and consumption is 1000. **The transfer FOC denominator
is not clamped in either frozen source.** The cost denominator is max(a,a_bar),
equal here to 5.2631578947368425 or 7.894736842105263, not the floor. These are
source-faithful arithmetic features. They explain these operator excursions,
but do not prove the entire convergence split is caused by one mechanism.
Source references are export lines 80–108, 274–277, 306–355 and 407–413;
task MATLAB lines 52–76. No production repair is supported merely by the P32
post-solve discrepancy.

Negative off-diagonal entries and omitted outward rates occur in 141/143 MATLAB
steps and 498/500 Python steps. Global minimum off-diagonals are
-18305.753516946155 at MATLAB52 (799,779), and -23511.95389231666 at Python146
(399,379). Both are upper-a backward rates. Upper-a source arithmetic
`ab=-(shadowB+Rah*a_max)/da` can be negative. At upper b, the forced B transfer
label can consume positive sdhB: for M57 (19,18,0), sdhB=1.5076859477646574
and bb=-4.092290429646927. P32 (19,13,1) similarly has sdhB=1.2666451060679467
and bb=-3.4380367164701404. These examples are reconstructed and checked against
stored rates. Both languages retain this legacy behavior.

Omitted outward rates retain their diagonal contribution. The maximum is
0.0086634895253846 at `(19,0,1)`, row419, giving row sum -0.008663489525384593.
This is truncation leakage. It is distinct from floating assembly/reduction loss
at enormous interior rows: P32's stored A row704 sums to -6850.804651896159
with zero reconstructed outward rate; M57 row604 ordinary sum is
0.0007044619927303875 (compensated sum 0.0006963641429441059).
No new PASS threshold is assigned to generator diagnostics.

Per-step ordinary and compensated (`math.fsum`) row sums and diagonal-dominance
margins are both retained. Minimum compensated margins are -3376.2904474719785
(MATLAB13,row799) and -3376.2880302401554 (Python13,row799). Python's ordinary
subtraction reports a more negative global -16384 due to reduction cancellation;
it must not be interpreted as an exact mathematical dominance margin. At P32,
the compensated minimum is -6.816466781351598 (row679); at M57 it is
-8.126008005527625 (row379). These diagnostics describe the stored matrices,
not a sound Markov generator or accepted equilibrium.

## Python updates 401–500 and terminal-state probe

The final100 statistics range from 0.008615936990254092 (463) to
0.008633469733490884 (418). There are 49 increases and 50 decreases; the slope
is -2.8796672376465086e-9 per update, with first25/last25 means
0.008623545200106558 / 0.0086231222834843. This is not convergence to 1e-7.
Liquid labels change 67 times, all at `(10,19,1)`; transfer labels change 100
times, all at `(18,19,0)`, counting the transition 400→401. Every update has
at least one label change. This is measured repeated switching, not a proof
of a limit cycle.

M norms range 17003.527178161883–1795341.1804079574 (peak424); maximum absolute
transfer per update ranges 139.08097245884153–1816.8271224647194, and maximum
cost 2175.8305743155524–330267.7620045898. Consumed clamp counts range 131–132;
negative off-diagonal counts 11–12, leakage cells 24 throughout. There are
transient operator excursions even within the nearly flat statistic band.
`python_tail100.json` and full per-step traces retain derivative/clamp extrema.

At M143_FINAL both languages satisfy the unchanged strict `distance < 1e-7`:
MATLAB distance 2.6173063716328215e-11, Python 2.6199042935104444e-11.
The nonlinear defect `u(V0)+A(V0)*vec_F(V0)-rho*vec_F(V0)` has infinity norm
1.3374745755356798e-11 in both, maximum at row49 `(9,2,0)`; the minimum is
-5.2429033337020314e-12 at row619 `(19,10,1)`. This uses the exact common
**input**, not updated V1. Linear residuals instead are 5.958870116090642e-12
and 6.296871878086474e-12. They are different diagnostic objects.
The terminal maps still have 18 negative off-diagonals and 15 leakage cells
on each side. Local stop agreement is not economic admissibility or equilibrium
acceptance, and does not show Python's independent trajectory reaches this state.

## Calls, engineering checks and publication

Each language used four primary invocations, four entered iterations, four
completed updates and four direct solves. All eight processes exited 0;
scientific retries=0. M24/P24/P32 stop at their single authorized update,
not at convergence. Full trajectories, native initialization, condition solves,
KFE, distribution/aggregation, GE/annual, R/PLM, shocks/IRF and Results calls=0.
Historical budgets remain consumed. Each invocation was below 15 minutes;
the four MATLAB durations were 24.5, 8.063, 9.281 and 8.75 seconds.

Eight focused tests pass: unchanged scientific bodies, launcher binding,
fixed-case field semantics, exact sparse support, signed generator/leakage
reduction, F-order coordinate mapping, absence of postprocessing evaluator/solve
calls, and upper-a reconstruction/NumPy-coordinate serialization. The wrappers
are text-identical to predecessor bodies except the one-step budget guard.
No unrelated regression suite or extra static MATLAB process was needed.

One solve-free postprocessing failure was preserved: a NumPy int64 coordinate
was not JSON serializable. Explicit Python integer conversion fixed it; saved
arrays were reused. A subsequent attempted read of the not-yet-written summary
failed and was repeated after postprocessing completed. Neither consumed science.
Compensated reductions were added to distinguish summation cancellation;
ordinary reductions remain in evidence. Reconstruction checks, finite output
comparisons, final frozen-source identities and the finite manifest readback pass.

Changed paths are only `validators/multi_province/call725_policy_operator_stability/`,
`tests/test_call725_policy_operator_stability.py`, this report, and small summaries
in `reports/call725_policy_operator_stability_20260907/`. MAT/NPZ remain in the
new external evidence root. `manifest.json` binds runtime snapshots, consumed
input identities, outputs, diagnostics, logs, code and report; it excludes itself
and terminal readback/publication receipts. Commit and remote SHA are returned
after dedicated-branch non-force publication. Builder does not merge main.

The smallest useful follow-up is a separately budgeted P32 stored-linear-system
comparison: give both direct solvers exactly the same saved M and RHS, optionally
cross the two already stored pairs, to separate factorization arithmetic from
input-rounding sensitivity. It is not run here. If Reviewer later proposes
under-relaxation as a stability experiment, it changes the iteration map and
convergence speed while nominally preserving fixed points; it does not repair
signed generator rates or establish economic validity. Clamping transfer
derivatives would change the FOC map and requires a substantive scientific
decision. No successor or stabilization experiment is started by this report.
