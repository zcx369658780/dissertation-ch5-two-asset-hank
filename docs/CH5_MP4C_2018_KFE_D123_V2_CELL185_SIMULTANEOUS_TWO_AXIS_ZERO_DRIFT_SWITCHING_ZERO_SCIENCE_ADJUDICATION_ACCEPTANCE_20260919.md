# CH5 MP4C 2018 KFE D1-D3 V2 cell185 simultaneous two-axis zero-drift switching adjudication acceptance

Date: 2026-09-19

Reviewer verdict:

`PASS__ZERO_SCIENCE_ADJUDICATION_ACCEPTED__SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_SCIENTIFICALLY_SUPPORTED__OWNER_ADOPTION_REQUIRED`

## Accepted candidate

- baseline live main before adjudication: `8a259e2d1c8dc6c5ae3b512b698daa30dcfd0525`
- Builder candidate: `3a3df94bd80874d531d58f3710bc82d2069aa619`
- candidate tree: `113c2164c1c5261dae1a3c7ed49b559aa152116f`
- candidate is exactly `1 ahead / 0 behind` baseline
- changed path is exactly one new adjudication report
- no source, test, task, CURRENT file, receipt, calibration, grid, tolerance, solver or production path changed
- Results eligibility remains `FALSE`

## L3 acceptance

The adjudication is accepted as:

`ADJUDICATED__SIMULTANEOUS_TWO_AXIS_ZERO_DRIFT_SWITCHING_SCIENTIFICALLY_SUPPORTED__OWNER_ADOPTION_REQUIRED`.

Cell185 is interior in both assets. The accepted liquid-`Z` candidates under the negative-transfer regime establish the post-liquid strict `a` crossing:

- backward-`a` liquid-`Z`: `g_a=+0.009287240997760404`;
- forward-`a` liquid-`Z`: `g_a=-0.005170298666228812`.

Neither endpoint is direction-consistent. The current one-axis authorities intentionally do not authorize selecting both shadows endogenously at once.

## Accepted joint derivation

The prospective joint candidate imposes simultaneously:

`g_a=0`

and

`g_b=0`.

At cell185:

- `d_ZZ=-r_a a=-0.42626460578345887`, hence negative transfer;
- unchanged D3 gives `q_a/q_b=0.7200216108914285`;
- mapping the closed illiquid derivative interval through D3 yields
  `q_b in [0.011790364625750628,0.011910163904713082]`;
- this interval lies entirely inside the liquid derivative interval
  `[0.009574726769001294,0.013362109688537174]`.

With `d_ZZ` fixed, the liquid equality is continuous and strictly increasing for positive `q_b`. Its values at the exact joint interval endpoints are:

- lower endpoint: `-0.023007467717380714`;
- upper endpoint: `+0.041147374843733764`.

Therefore exactly one joint root exists in the admissible interval. The resulting `q_a=kq_b` lies inside the illiquid derivative interval. This proves static existence and uniqueness of a coupled local candidate satisfying `g_b=g_a=0`.

## Scientific interpretation

The joint candidate is not a sequential composition of the two adopted one-axis algorithms. Sequential liquid-`Z` freezes an endpoint `q_a` and therefore a different transfer; sequential interior-`a` first changes transfer and therefore changes the liquid equation. The correct mathematical object is the simultaneous coupled system plus both derivative-rectangle constraints.

The report's interpretation is accepted: this is a scientifically supported prospective two-dimensional Godunov/viscosity switching closure, conditional on the frozen V2 derivatives. It is compatible with D1/D2/D3 and the accepted one-axis laws but is not already authorized by them.

## Prospective contract

The Builder report's prospective generic contract is accepted for Owner review only:

- apply only at interior-interior asset nodes;
- require the common transfer regime and the coupled strict-crossing evidence;
- impose `g_a=0` and `g_b=0` simultaneously;
- use unchanged D3;
- require `q_a` and `q_b` inside their respective closed one-sided derivative intervals;
- solve only on the exact interval intersection;
- require one unique legal root and fail closed otherwise;
- reconstruct controls/KKT/Hamiltonian from the joint shadows without averaging/interpolation;
- preserve ordinary and one-axis candidates;
- create exactly one joint candidate per node/active-set/regime with explicit precedence/deduplication;
- persist the full two-axis receipt;
- leave D1/D2/D3, one-axis laws, solver/tolerance, grid, calibration, HJB convergence law and production routes unchanged.

This acceptance does not itself adopt the joint law.

## Zero-science ledger

Accepted as all-zero for selector, all root categories, policy map, D2/Q, Bellman, HJB, graph/SCC, KFE/SVD/eigen/nullspace/`Q.T@p`, MATLAB, downstream/Results and scientific retry.

## Owner gate

No implementation task is authorized by this acceptance.

Owner must explicitly adopt, modify or reject the prospective simultaneous two-axis switching contract before Reviewer may publish an implementation or V2 reexecution task.

Production replacement, GE, annual calibration, dynamics, IRF, welfare, causal interpretation and Results remain closed.
