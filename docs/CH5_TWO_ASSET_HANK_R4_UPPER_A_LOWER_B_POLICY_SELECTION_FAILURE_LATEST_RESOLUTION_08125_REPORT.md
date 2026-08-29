# Chapter 5 Two-Asset HANK R4 — Latest Upper-A/Lower-B Resolution 08125

Date: 2026-08-22

## Verdict

`CH5_TWO_ASSET_HANK_R4_UPPER_A_LOWER_B_POLICY_SELECTION_FAILURE_LATEST_RESOLUTION_08125_PASS`

## Acceptance level

`R4_UPPER_A_LOWER_B_SLACK_FORWARD_CLOSURE_IMPLEMENTED_TESTED__STEADY_STATE_NOT_RERUN`

The latest upper-`a`/lower-`b` slack-active-set blocker is resolved. The
existing joint producer now distinguishes the accepted active lower-`b`
zero-drift regime from the newly authorized slack regime. When fixed
upper-`a` transfer controls evaluated at `V_b^F` produce positive inward liquid
drift, the producer retains those derivative controls and a zero lower-`b`
multiplier. The selector submits the result as a `Z/F` candidate through the
unchanged boundary, multiplier, complementarity, Hamiltonian, and KKT gates.

No fixture, grid, calibration, economic equation, transfer mechanism,
boundary contract, tolerance, generator, HJB, or KFE logic was changed.

## Live authority and repository state

- Repository: `zcx369658780/dissertation-ch5-two-asset-hank`.
- Fresh-fetched `origin/main`:
  `00c6a605c1d2a511de87f89af3ed22c7697be3cd`.
- Local baseline: `46d98d140cebcefb795c14f3ba8f61a515d5f6ac`.
- Start relation: `0 ahead / 55 behind`.
- Live task:
  `tasks/CH5_TWO_ASSET_HANK_R4_UPPER_A_LOWER_B_POLICY_SELECTION_FAILURE_LATEST_RESOLUTION_08125.md`.
- Live `AGENTS.md`, project rule index, and GitHub capability/authority-routing
  rule were read directly from `origin/main` without pull or checkout.

## Files read

- live repository governance, project rule index, capability-routing rule, and
  exact latest resolution task;
- accepted R2 HJB and R3 KFE reports;
- latest steady-state rerun failure report;
- latest 08125 upper-`a`/lower-`b` diagnostic report;
- current HJB, policy, derivative, boundary, contracts, economics, and policy
  regression sources.

## Files written

- modified `src/ch5_two_asset_hank/policies.py`;
- modified `tests/test_r4_policy_fixture_resolution.py`;
- added this report.

No other file was modified.

## Implementation changes

### Active/slack upper-a/lower-b producer

The existing `_upper_a_lower_b_controls` producer now implements both existing
KKT regimes without changing its interface:

- fixed transfer remains `d=-r_a*a`;
- if derivative controls imply negative outward liquid drift, the accepted
  active lower-`b` path still solves an upward shadow root for `mu_b=0`;
- if derivative controls already satisfy `mu_b>=0`, controls are recomputed and
  retained directly at `V_b^F`, so `lambda_b=0` and the lower constraint is
  slack;
- the existing implied upper-`a` multiplier-sign check remains mandatory;
- no candidate is accepted inside the producer and no generator entry is
  created directly.

At the upper-`a`/lower-`b` selector branch, the liquid direction is now derived
from the produced drift:

- `Z` for the accepted active zero-drift regime;
- `F` only for strictly positive inward liquid drift in the slack regime.

Both regimes continue through exact illiquid `Z` direction, boundary
feasibility, upper-`a` and lower-`b` multiplier/complementarity components, and
the unchanged `1e-7` KKT threshold. Candidate identifiers distinguish `UZL`
from `UFL`.

### Exact regression

The added regression reproduces `(a,b,z)=(1.0,0.0,0.8125)` with:

- `V_a^B=1.3407408769313847`;
- `V_b^F=1.249395172408839`;
- returned shadow exactly equal to `V_b^F`;
- consumption `0.8003872770470178`;
- labor `1.0151335775821817`;
- transfer `-0.04`;
- `mu_a=0`;
- `mu_b=0.0616087547385048`, valid forward inward drift;
- upper-`a` multiplier `0.20379127003934117`;
- lower-`b` multiplier `0`;
- boundary violation zero and maximum scaled KKT residual no greater than
  `1e-7`.

The earlier `(1.0,0.0,0.6875)` active lower-`b` zero-drift regression remains
passing, proving the accepted joint-root contract was preserved. No tolerance
was relaxed.

## Tests executed

1. Red focused regression before implementation:
   - `python -m pytest -q -p no:cacheprovider tests/test_r4_policy_fixture_resolution.py`;
   - `1 failed, 7 passed` because the existing producer returned `None` for the
     slack lower-`b` state.
2. Focused regression after implementation:
   - same command;
   - final result after selector integration verification: `8 passed in 0.51s`.
3. Static compilation:
   - `python -m py_compile src/ch5_two_asset_hank/policies.py tests/test_r4_policy_fixture_resolution.py`;
   - passed.
4. Full non-steady-state regression suite:
   - `python -m pytest -q -p no:cacheprovider --ignore=tests/test_r4_steady_state.py`;
   - final result: `29 passed in 3.33s`.

During final source inspection, the first selector patch was found to have
placed the dynamic liquid-direction assignment in the adjacent dual-upper
block. Before delivery, dual-upper was restored to strict `Z/Z`, the dynamic
`Z/F` assignment was moved into the authorized upper-`a`/lower-`b` branch, and
the focused, compilation, and full non-steady-state checks above were rerun.

The frozen steady-state runner and steady-state test target were not invoked.

## Required scientific checks

- economic equations unchanged: pass;
- transfer mechanism unchanged: pass;
- slack lower-`b` branch recomputes derivative controls instead of reusing an
  incompatible active multiplier: pass;
- accepted active lower-`b` joint-root branch preserved: pass;
- upper-`a` multiplier contract remains valid: pass;
- existing upper-`b`, dual-upper, and interior contracts remain passing: pass;
- tolerance-only acceptance: none;
- artificial mobility: none; drift remains equation-derived and no transition
  is inserted directly.

## Forbidden-operation check

- fixture parameters, grids, calibration, initialization, and tolerances:
  unchanged;
- economic equations, transfer mechanism, HJB, generator, and KFE: unchanged;
- truncation interpretation: unchanged;
- artificial transitions or mobility: not added;
- recurrent-class selection and invariant mixtures: not performed;
- steady-state solver and frozen R4 runner: not run;
- connectivity, closed classes, left nullity, KFE, stationary distribution,
  mass/density accounting, `A_hh`, and `B_hh`: not run;
- transition solver and AR(1) shock engine: not implemented or run;
- IRF/dissertation experiments: not run;
- Results prose and MATLAB-Python parity claim: not produced;
- pull, checkout, merge, reset, clean, commit, and push: not performed;
- all pre-existing untracked research files and prior evidence: preserved.

## Git status

- final `HEAD=46d98d140cebcefb795c14f3ba8f61a515d5f6ac`;
- final `origin/main=00c6a605c1d2a511de87f89af3ed22c7697be3cd`;
- relation: `0 ahead / 55 behind`;
- tracked staged modifications: none;
- tracked unstaged modifications: none;
- retained research tree remains untracked relative to the old local baseline;
- this task changes only the bounded policy source, regression file, and this
  report within that retained untracked tree.

## Recommended next gate

`CH5_TWO_ASSET_HANK_R4_STEADY_STATE_IMPLEMENTATION_RERUN`

That gate requires its own new exact live GitHub authorization and must retain
the frozen fixture, one-shot/no-tuning discipline, full HJB/KKT/generator,
truncation, endogenous-connectivity, uniqueness, KFE, and separate asset
accounting gates. This report does not authorize the frozen runner and does not
authorize `R4_STEADY_STATE_ACCEPTANCE`.
