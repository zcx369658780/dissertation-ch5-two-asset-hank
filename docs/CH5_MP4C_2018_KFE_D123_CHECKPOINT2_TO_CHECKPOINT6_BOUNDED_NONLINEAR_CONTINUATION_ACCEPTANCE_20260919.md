# CH5 MP4C 2018 KFE D1-D3 checkpoint-2 to checkpoint-6 bounded continuation acceptance

Date: 2026-09-19

Reviewer verdict:

`PASS__BOUNDED_CONTINUATION_EVIDENCE_ACCEPTED__V2_TO_V3_LINEAR_STEP_VALID__V3_CELL100_LOWER_B_NEGATIVE_FORWARD_A_PRE_SCREEN_FALSE_NEGATIVE_ATTRIBUTED__MINIMAL_REPAIR_REEXECUTION_AUTHORIZED`

## Accepted candidate

- baseline live main before task: `aac2c854a8a208f4abb469ce310b3347195f4df7`
- Builder candidate: `d2b0d62ff7a7c9c094bb70d6eaf8bef88f8e449a`
- candidate tree: `312d93460a470bf8f08e6c30e0b0106d5daad59e`
- candidate chain is exactly `2 ahead / 0 behind` baseline
- focused engineering gate: `69/69` passed
- source-faithful/production paths and frozen scientific laws remain unchanged
- Results eligibility remains `FALSE`

## Accepted continuation facts

Accepted checkpoint 2 was bound exactly and was not rerun.

Exactly one direct update `V2 -> V3` was executed under the frozen equation with `Delta=1000` and the existing `scipy.sparse.linalg.spsolve` path.

The solve is accepted:

- V3 SHA-256: `4FDB36C17ACDC60B56661AEE1C0437B65EC4A871FD4E5E08A9A996FB10EF85EF`
- original-equation residual infinity norm: `1.4391265956703592e-14`
- normwise backward error: `2.439151619375125e-16 <= 1e-12`
- direct-update artifact SHA-256: `17F330AB0A226EE826880039055B9EA16FB93DD7B02F36F820D078178C6E4CCF`.

The one fresh V3 policy-map attempt stops first at flat F index `100`, zero-based `(0,5,0)`, physical `(-2.0,2.6315789473684212,0.8)`, with `NO_ADMISSIBLE_POLICY`.

No P3/u3/Q3 or B3/D3/cycle object exists.

## Independent Reviewer attribution

The V3 cell100 failure exposes an implementation false negative in the **already-authorized active lower-b negative-transfer branch census**. It does not require a new scientific law.

Persisted V3 derivatives are:

- `p_b=0.005156057482672655`
- `p_a^B=0.012088089476579748`
- `p_a^F=0.01134140574122853`
- `a=2.6315789473684212`
- `r_a=0.08999994552589044`.

For the frozen D3 negative-transfer law at this interior-`a` state,

`d(q_b)=a/chi_1 * (p_a/q_b-(1-chi_0))`

because `a>a_bar`, `chi_0=0.1`, and `chi_1=2`.

For the **forward-`a`** derivative, legal negative-transfer / forward-direction values exist on the nonempty interval

`q_b in (p_a^F/(1-chi_0), p_a^F/(1-chi_0-chi_1 r_a))`

which numerically is

`q_b in (0.012601561934698366, 0.015751950034835593)`.

On that interval:

- `d<0`;
- `g_a=r_a a+d>0`;
- therefore the negative-transfer forward-`a` direction is authority-backed and must be represented.

However, the current lower-b negative branch viability pre-screen samples 513 log-spaced points over the effectively unbounded domain from the lower-b shadow floor to `sys.float_info.max`.

At this cell the first two sampled `q_b` values are approximately:

- `0.005156057482672656`;
- `0.020837512395988838`.

The entire legal forward-`a` interval lies strictly between those two samples, so the screen never observes it and drops the branch.

The backward-`a` negative branch survives because its direction-consistent region extends above its zero-drift threshold and includes the second coarse sample. This explains the persisted seven-candidate census and the absence of an active lower-b negative / forward-`a` row.

## Static root existence evidence

The omitted forward-`a` branch is not merely theoretically possible.

For the frozen liquid equality evaluated with the negative-transfer forward-`a` law:

- at `q_b=p_a^F/(1-chi_0)=0.012601561934698366`, the limiting liquid drift is approximately `-0.1154321`;
- at `q_b=p_a^F/(1-chi_0-chi_1 r_a)=0.015751950034835593`, the liquid drift is approximately `+1.4218152`.

Within the legal negative-transfer interval the liquid equality is continuous and strictly increasing. The derivative is positive because the labor and consumption contributions are positive and, under the frozen transfer FOC, the transfer/cost contribution is also positive.

Therefore exactly one active lower-b negative / forward-`a` liquid-equality root exists strictly inside the legal interval.

This proof authorizes representation and one bounded runtime verification. It does **not** pre-authorize selection of that candidate; all existing D1/D3/KKT/Hamiltonian checks remain required.

## Scientific interpretation

The current coarse log screen is an optimization/filtering device, not scientific authority. A branch that is legal under the frozen lower-b/D3/upwind law may not be removed merely because a sparse sampling grid misses a narrow viability interval.

The implementation blocker is therefore:

`ATTRIBUTED__V3_CELL100_LOWER_B_NEGATIVE_FORWARD_A_BRANCH_FALSE_NEGATIVE_FROM_COARSE_UNBOUNDED_LOG_PRE_SCREEN`.

No change to D1/D2/D3, switching laws, root solver/tolerance, grid, calibration, HJB update law, or convergence law is required.

## Accepted scientific ledger

- direct HJB solves/updates: `1/1`
- fresh V3 maps: `1`
- selector evaluations: `101`
- scalar roots: `46`
- liquid-Z roots: `15`
- interior-a/joint roots: `0/0`
- D2/Q3 assemblies: `0`
- complete checkpoint-3 evaluations: `0`
- scientific retries/solver substitutions: `0/0`
- terminal topology/KFE/MATLAB/downstream/Results: `0`.

The sealed evidence manifest is accepted with `113/113` entries and SHA-256:

`9F772B9CEF73E15F0443952B25989BB6D644D73B9E04CB93B5AD047E1FBB7700`.

## Successor authority

Reviewer authorizes one minimal corrected-selector repair:

- for active lower-b / negative-transfer only, eliminate sampling-based false-negative removal of legal interior-`a` one-sided directions;
- preserve upper-b and all other regimes;
- retain the existing root, sign, direction, KKT, finite-value, deduplication and Hamiltonian gates.

Then execute exactly one fresh policy map from the already accepted V3 value field. Do not rerun `V2->V3`.

If the V3 map completes, assemble at most one Q3 and evaluate checkpoint-3 B3/D3/stability/cycle diagnostics. Do not execute `V3->V4` in the repair task.

Any different first scientific failure stops and returns to Reviewer.
