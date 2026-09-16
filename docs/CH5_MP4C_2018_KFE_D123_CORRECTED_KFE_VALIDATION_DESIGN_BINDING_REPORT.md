# CH5 MP4C 2018 KFE D1-D3 corrected KFE validation design and binding

Date: 2026-09-16

Task: `CH5_MP4C_2018_KFE_D123_CORRECTED_KFE_VALIDATION_DESIGN_BINDING_ZERO_SCIENCE_20260916`

## Verdict

`READY_FOR_BOUNDED_CORRECTED_Q0_KFE_OPERATOR_VALIDATION`

The accepted pre-step `Q0` is the scientifically identified generator of the
complete corrected Option-A `V0` policy map.  It is therefore a sufficient and
proper object for a bounded **operator-level** source-free KFE validation: the
experiment may ask whether this finite-state Markov generator has a conserved,
normalized, nonnegative and unique invariant mass.

A fresh policy remap on `V1` is not required for that claim.  Such a remap would
construct a distinct operator `Q1` and is required only for a different claim
about the post-step policy map or HJB iteration.  The accepted `V1` is one direct
linear HJB step, not a fixed point; neither a passing Q0 KFE diagnostic nor a
future Q1 remap may be described as nonlinear HJB convergence or a stationary
economic equilibrium without separately authorized evidence.

This classification follows the accepted object provenance and claim boundary,
not anticipated solver convenience or outcome.

## Git and scope identity

- Fresh-fetched `origin/main`:
  `99fd61a4bc66493e080491c910c7713f8c0ae6a1`.
- Branch:
  `codex/ch5-mp4c-2018-kfe-d123-corrected-kfe-validation-design-binding-zero-science-20260916`.
- This task changes only this report.
- Candidate SHA convention: the immutable commit and remote readback are reported
  after publication; a commit cannot embed its own SHA without changing it.

No selector, generator, HJB, KFE, production, source-faithful, calibration,
evidence or Results path was changed.

## Authority and artifacts read

The required startup authority was read from the fresh baseline in order:

1. `AGENTS.md`;
2. `project_rules/PROJECT_RULE_INDEX_CURRENT.md`;
3. `docs/CH5_TWO_ASSET_HANK_PROJECT_STATUS_CURRENT.md`;
4. `docs/CH5_TWO_ASSET_HANK_SESSION_HANDOFF_CURRENT.md`;
5. `docs/CH5_MP4C_2018_KFE_D123_OPTION_A_COMPLETE_POLICY_MAP_D2_DIRECT_STEP_ACCEPTANCE_20260916.md`;
6. `docs/CH5_MP4C_2018_KFE_D123_INTERIOR_Z_SWITCHING_REPAIR_AND_OPTION_A_REEXECUTION_REPORT.md`;
7. the Owner D1-D3 adoption and accepted corrected-diagnostic static
   implementation authority;
8. the accepted call-725 and five-turn KFE leakage/pinning attribution plus the
   later gauge-comparison evidence;
9. the accepted Q0 D2 receipt/artifact, direct-step receipt/artifact, freeze,
   ledger and sealed manifest;
10. the active task and the exact corrected generator/grid/Option-A source.

The decisive accepted identities are:

| Object | Exact identity |
|---|---|
| Accepted Builder candidate | `9a4eb0e5ec3627743596daa9b991436d2124efa9` |
| Q0 artifact | `d2_generator.npz`; 22,474 bytes; SHA-256 `093E1AF1ADFEEE5C50D3DD91EDDD678EBAC5BBA6C42E64DE73A63B82102AF1D5`; Git blob `3ea57f5e02fb9eb312918f426bad7ec2822b5d63` |
| Q0 receipt | 1,526 bytes; SHA-256 `60389B54953B69C05A4DB2693272E2A32A8FB3F962AD99A285F82B266BF2237B`; Git blob `817a338347df5d40ac96d3c170f1406adf641933` |
| Direct-step arrays containing V1 | 29,380 bytes; SHA-256 `28A27473A4C08CCD20550B9EDF1509BABB4D7D882A9429F7F54F55DE72083173`; Git blob `37b504fd22ed6a26d05c3715ee5b462916af551d` |
| V1 field | SHA-256 `5C410EBC329F08B37F941A783E7F2C84BFCDCB67C6E24118114BE8C55697F2E2` |
| Direct-solve receipt | 916 bytes; SHA-256 `9AA6EA211471E56B467A08032C5355A5312F5600134F111FA0DFE8E8D4EBAD58`; Git blob `bebd3f26920ad9744e87cb367ca22a4d6952382a` |
| Accepted manifest | 125,779 bytes; SHA-256 `D628E24AD421EA5A38EF80230862FE7B3BBD9BFA368CA7BEB08820528ADB643E`; Git blob `1fe6dd8b93b126f3077692aed6aae1249d00277a` |

The accepted Q0 receipt records D2 `PASS`, minimum off-diagonal
`0.2642984748447064`, exact diagonal-construction error `0.0`, and
`max_abs(Q0 @ 1)=3.552713678800501e-15` below the preregistered arithmetic
bound `5.222144858126786e-14`.  Both asset-coordinate checks have zero
violations.  Scientific/test hashes matched the pre-execution freeze.

## Operator choice

### Why Q0 is sufficient for the bounded operator claim

Q0 is not an intermediate or failed legacy operator.  It was assembled once
from all 800 durable selected policies after the complete-map gate, using the
Owner-adopted D1 closed-box law, D2 consumed-total-drift construction, D3 KKT,
lower-a repair and interior-Z law.  Its off-diagonal rates are nonnegative, its
diagonal is the negative retained outgoing-rate sum, and outward inputs at all
closed faces were rejected with zero tolerance before assembly.

For any identified finite generator, existence/nonnegativity/uniqueness of its
invariant mass is an operator property.  That question does not require the
value function that generated the policies to be an HJB fixed point.  A Q0 KFE
PASS would therefore validate an invariant distribution **conditional on the
accepted V0 policy operator Q0**.

### Why V1 remapping is not the prerequisite here

The direct step solved

`[(rho + 1/Delta) I - Q0] V1 = u0 + V0/Delta`

once.  No `V1` selector evaluation occurred.  Remapping `V1` would call the
selector again and produce policies, utilities and potentially a new generator
Q1.  Repository authority does not identify Q1 as a substitute for Q0 or as a
fixed-point operator, and one remap would still not establish convergence.

Consequently:

- Q0 is authorized for the next operator-level KFE validation;
- a V1 remap is outside that experiment and remains at zero;
- if a future claim concerns V1 policies, policy iteration or an HJB/KFE steady
  state, a separately authorized remap/convergence route is required first.

## Frozen orientation and state mapping

Q0 uses the accepted backward-generator convention: rows are origin states,
off-diagonal `Q0[i,j]` is a nonnegative transition rate from origin `i` to
destination `j`, and `Q0 @ 1 = 0` is the conservative construction invariant.

The forward Kolmogorov equation for a column mass vector `p` is therefore

`dp/dt = Q0.T @ p`,

and source-free stationarity is exactly

`Q0.T @ p = 0`.

The stored density convention uses `p = omega * g`, where the exact accepted
uniform asset-cell weight is

`omega = db * da = (7/19) * (10/19) = 70/361`.

Productivity is a two-state discrete Markov state and contributes no `dz`
volume factor.  Because `omega` is constant on this exact grid,
`Q0.T @ p = 0` and `Q0.T @ g = 0` are equivalent up to the positive scalar
`omega`.  The future implementation must solve and validate the probability
mass vector `p`; `g=p/omega` is a reported density view.

State tensors use `(b,a,z)=(20,20,2)` and exact F-order throughout.  The frozen
flat index is

`k = i_b + 20 * (i_a + 20 * i_z)`,

so `b` is fastest, then `a`, then `z`.  Q0 productivity coupling is the accepted
two-way matrix `[[-1/3,1/3],[1/3,-1/3]]`, lifted consistently with this ordering.
No C-order conversion, transposition other than the single forward `Q0.T`, or
state permutation is allowed.

## Pin-free homogeneous nullspace contract

The future experiment must not use the historical row-replacement mechanism,
`x[k]=.007`, an adaptive replacement row, an injected RHS, a balancing source,
or any other altered stationarity equation.

The sole authorized numerical route is:

1. Read and hash-bind the exact Q0 artifact above as finite CSR, shape
   `(800,800)`.
2. Form `A=Q0.T` without changing any entry.
3. Materialize the 800-by-800 binary64 `A` only for one full singular-value
   decomposition using `scipy.linalg.svd`,
   `full_matrices=True`, `lapack_driver="gesvd"`, `check_finite=True`.
4. Take the right singular vector `v=Vh[-1,:]` associated with the smallest
   singular value.  No coordinate is selected or constrained.
5. Compute `s=math.fsum(v)`.  If `s<0`, apply one global sign reversal.  If
   `abs(s)` is not strictly above its prospective summation bound, fail closed.
6. Normalize once as `p=v/math.fsum(v)` and report `g=p/omega`.
7. Re-evaluate all 800 original equations through `A @ p`.  No equation is
   removed, replaced or exempted from the residual checks.

Global sign orientation and scalar mass normalization do not add a source and
do not pin a state.  Because this design retains every homogeneous stationarity
equation, no dropped-equation redundancy argument is needed.  A future
implementation that removes/replaces a row or uses an augmented RHS is outside
this frozen contract and must stop before solving; it may not infer redundancy
from a small contaminated-system residual.

## Conservation and source-free checks

Let `N=800`, binary64 machine epsilon be `eps`, and
`gamma_m=m*eps/(1-m*eps)`.  All formulas below are fixed prospectively and may
not be tuned after observing Q0 or p.

Before the SVD, require:

1. artifact path, bytes, SHA-256, CSR shape and finite data exactly match;
2. every off-diagonal is `>=0` with exact sign comparison;
3. each diagonal equals the negative retained outgoing-rate sum under the
   accepted D2 construction receipt, whose recorded construction error is
   exactly zero;
4. `q1=Q0 @ ones(N)` is finite and
   `max(abs(q1)) <= 5.222144858126786e-14`, the already accepted prospective
   D2 bound; no new fitted bound is allowed;
5. all 800 policy receipts remain present and hash-bound, and every selected
   consumed drift has zero-tolerance closed-face admissibility;
6. an explicit outside-domain flux ledger reports exactly zero outward rate and
   zero outward mass flux on lower/upper `b` and lower/upper `a` faces.

After normalization, set `r=A @ p` and freeze:

`tau_stationarity = gamma_(N+64) * max(1, ||A||_inf * ||p||_inf)`.

Require all residuals finite and `||r||_inf <= tau_stationarity`.  Also require
the normwise backward ratio

`||r||_inf / max(1, ||A||_inf * ||p||_inf) <= gamma_(N+64)`.

The global source-free ledger must persist:

- `math.fsum(r)`;
- `dot(q1,p)`;
- their absolute difference;
- the same prospective binary64 dot/summation bound.

Both global quantities and their discrepancy must be inside their prospective
bounds.  No residual component may be relabelled as a source, escape correction
or omitted pin equation.

## Normalization and nonnegative mass

For the unnormalized SVD vector define

`tau_sum = gamma_N * max(1, sum(abs(v)))`.

Require `abs(math.fsum(v)) > tau_sum` before sign orientation and normalization.
After normalization require:

- every `p_i` and `g_i` finite;
- `abs(math.fsum(p)-1) <= gamma_N * max(1,sum(abs(p)))`;
- `abs(omega*math.fsum(g)-1)` within the corresponding prospective grouped-
  multiplication/summation bound;
- no clipping, absolute-value replacement or renormalization retry.

Freeze the componentwise nonnegativity allowance as

`tau_nonnegative = gamma_(N+64) * max(1, ||p||_inf)`.

Require `min(p) >= -tau_nonnegative`.  Persist the exact negative-entry count,
minimum component and `math.fsum(max(-p_i,0))`; also require total negative mass
`<= N*tau_nonnegative`.  Values inside the arithmetic allowance remain reported
with their original signs and are never clipped to zero.  Any component or total
negative mass outside these bounds is terminal.

## Rank, nullity and uniqueness

Uniqueness is not inferred from one finite solver return.

Two independent checks are mandatory:

### Structural communicating-class check

Build the directed graph using every exact positive off-diagonal `Q0[i,j]>0` as
an edge `i -> j`; zero entries are absent and no edge tolerance is allowed.
Compute strongly connected components once and identify components with no
outgoing edge.  For a finite conservative continuous-time Markov chain, the
dimension of the stationary space equals the number of closed communicating
classes.  Require exactly one closed communicating class.  Persist all component
sizes, the closed-class count and whether transient states exist.

### Numerical nullity check

From the same full SVD, order singular values descending and freeze

`tau_rank = gamma_(N+64) * max(1, sigma_max)`.

Require exactly one singular value `<=tau_rank`, the next-smallest singular
value `>tau_rank`, and hence numerical rank `799` / nullity `1`.  Persist all
singular values or their hash plus the smallest two, `sigma_max`, `tau_rank` and
gap ratios.  If the structural closed-class result and numerical nullity disagree,
or if either result is ambiguous at the frozen threshold, fail closed without a
second decomposition or threshold adjustment.

Only the conjunction of one closed class, nullity one, normalized source-free
stationarity and admissible nonnegative mass supports the word `unique`.

## Finite future runtime budget

The smallest authorized future Q0 validation has the following hard ceiling:

| Operation | Ceiling |
|---|---:|
| accepted Q0 artifacts loaded | 1 |
| Q0 structural/conservation audits | 1 |
| directed SCC decompositions | 1 |
| full dense `gesvd` nullspace/rank decompositions | 1 |
| normalized candidate stationary masses | 1 |
| `Q0 @ 1` evaluations | 1 |
| `Q0.T @ p` evaluations | 1 |
| sparse/direct row-replaced KFE solves | 0 |
| iterative eigen/nullspace solves | 0 |
| solver substitutions or retries | 0 |
| selector/root/policy maps/D2/HJB/V1 remaps | 0 |
| MATLAB/outer/firm/wage-return/GE/annual/shock/IRF/Results | 0 |

One process, one thread unless the numerical library internally manages its
fixed call, at most 300 seconds wall-clock and 2 GiB resident memory are allowed.
Timeout, memory breach, SVD exception/warning/nonconvergence, nonfinite output or
missing evidence is terminal.  No rerun with another LAPACK driver, sparse
eigensolver, pin row, tolerance or normalization convention is permitted.

## Fail-closed conditions

Stop without scientific retry if any of the following occurs:

- any bound artifact/hash/shape/order identity differs;
- Q0 contains a negative off-diagonal, nonfinite entry, construction mismatch,
  row-sum failure or nonzero outward-face flux;
- the graph has zero or more than one closed communicating class;
- SVD fails, warns, is nonfinite, exceeds budget, or produces nullity other than
  one at the frozen threshold;
- SVD and graph uniqueness evidence conflict;
- the null vector has an unresolved sign/zero-sum normalization;
- mass normalization, nonnegativity or source-free stationarity exceeds its
  prospective bound;
- any row is replaced, any RHS/source is injected, any negative mass is clipped,
  or any outcome-dependent tolerance/retry appears;
- a receipt, ledger, rank artifact or post-run hash check cannot be durably
  persisted before interpretation.

Such a terminal is local Q0 operator evidence.  It must not be reported as HJB,
KFE-in-general or equilibrium nonexistence.

## Interpretation boundary for a future PASS

A future PASS would establish only that the exact accepted Q0 finite-state
operator has one source-free, normalized, nonnegative and unique invariant mass
under the frozen closed-box D1-D3 construction.  It would permit conditional
operator-level diagnostics of that Q0 invariant distribution if separately
authorized.

It would not establish:

- convergence of the nonlinear HJB or `V1=V0`;
- correctness of policies remapped from V1;
- a joint HJB-KFE fixed point or steady-state equilibrium;
- production/source-faithful replacement or MATLAB parity;
- calibration, GE, annual, shock, IRF or Results validity;
- economic adequacy of the finite upper box beyond the adopted diagnostic law.

Results eligibility remains `FALSE`.

## Zero-call ledger

| Category | Calls |
|---|---:|
| real or synthetic selector evaluations | 0 |
| scalar roots | 0 |
| policy maps | 0 |
| D2 assemblies | 0 |
| HJB solves or iterations | 0 |
| KFE/nullspace/stationary numerical solves | 0 |
| MATLAB | 0 |
| outer / firm / wage-return | 0 |
| GE / annual / shock / IRF / Results | 0 |
| scientific retries | 0 |

Only source/document inspection, exact file metadata/hash readback, previously
persisted matrix-structure receipt reading and algebraic design were performed.
This task does not merge `main` and does not publish a successor task.
