# CH5 MP4C K1 — standalone MATLAB-faithful HJB ra × wage convergence-domain freeze

Date: 2026-09-13.
Status: `OWNER_APPROVED_STANDALONE_MATLAB_FAITHFUL_HJB_RA_WAGE_DOMAIN_SCAN_FIRST`.

## 1. Owner decision

Do not redesign the HJB algorithm. The dissertation/MATLAB HJB/KF method remains scientific authority. The next task isolates the standalone two-asset household block and searches for a numerically/economically healthy input region before returning to the full multi-province model.

The first scan fixes `rb=0.02` and varies only `ra` and the household wage input. The scan does not run the full multi-province outer model.

## 2. Frozen MATLAB-style grid and core inputs

Use the accepted MATLAB-faithful two-asset household implementation and original MATLAB settings wherever already frozen/available. At minimum:

- liquid asset grid: `I=20`, `b in [-2,5]`;
- illiquid asset grid: `J=20`, `a in [0,10]`;
- productivity grid: `Nz=2`, `z in [0.8,1.3]`;
- productivity transition matrix from the original MATLAB program;
- `rb=0.02`;
- borrowing-rate gap `0.07`;
- annual continuous-time household parameters and accepted MATLAB-faithful HJB/KFE numerics unchanged;
- no D1, K1B, K2, bilateral-capital feedback, firm loop, GE loop or outer provincial iteration.

Do not modify HJB equations, upwind logic, transition-matrix construction, derivative formulas/floors, pseudo-time step, convergence tolerance, iteration ceiling, KFE contaminated-row solve, grid or boundary laws.

## 3. First coarse scan

Run exactly the following 9 standalone parameter combinations:

- `ra ∈ {0.02, 0.055, 0.09}`;
- household wage input `w ∈ {0.8, 1.05, 1.3}`;
- `rb=0.02` for all points.

The wage scan deliberately uses the original multi-province `wjt` range as the first household-wage proxy, as approved by Owner. Do not introduce an alternative wage mapping in this first task.

No adaptive/new parameter point may be added after observing results. The next refinement grid is a later Owner/Reviewer decision.

## 4. MATLAB-style HJB classification

For each point preserve the original MATLAB numerical logic and classify the HJB stage first:

1. `HJB_HARD_ERROR_OR_INVALID_TRANSITION_MATRIX` — scientific exception/nonfinite result or MATLAB-equivalent transition-matrix legality check fails;
2. `HJB_NOT_CONVERGED` — legal HJB execution reaches the accepted iteration ceiling without satisfying the accepted value-function convergence criterion;
3. `HJB_CONVERGED` — accepted MATLAB-style `max(abs(V_new-V_old))` criterion passes.

Record the first/maximum transition-matrix legality statistic corresponding to the original MATLAB `A = BB + AAH + Bswitch` check, but do not change its accepted semantics or threshold.

## 5. KFE / steady-state quality after HJB convergence only

Only if HJB converges, run the accepted standalone MATLAB-faithful stationary KFE solve and compute at least:

- `Ct`;
- `Lt`;
- `At`;
- `Bt`;
- where available, positive/negative liquid-asset aggregates matching the MATLAB household output;
- total probability/mass receipt;
- marginal distribution over `b`;
- marginal distribution over `a`;
- boundary mass at `bmin`, `bmax`, `amin`, `amax`;
- upper-bound versus adjacent-interior mass diagnostics;
- finite/nonfinite and shape checks.

The first task must preserve continuous boundary diagnostics rather than invent a post-result cutoff. It may assign a descriptive preliminary label:

- `BOUNDARY_CONVERGED_CANDIDATE` when the distribution visibly/mathematically piles at an artificial asset endpoint;
- `GOOD_STEADY_STATE_CANDIDATE` when HJB/KFE converge, aggregates are finite/coherent, total mass is valid, and no obvious artificial upper-bound pile-up appears;
- `QUALITY_AMBIGUOUS__OWNER_REVIEW_REQUIRED` if the distinction is not clear from the preregistered receipts.

No final production admissibility interval is frozen by this first 9-point scan.

## 6. Interpretation

The purpose is to learn the standalone healthy HJB/KFE parameter region, not to calibrate the full model. A good candidate point means only that the isolated household block behaves normally under the frozen MATLAB-faithful algorithm.

After acceptance, Owner/Reviewer may add points near observed transitions and progressively map a usable `ra × wage` region. Later full-model work should aim to keep provincial household inputs inside the accepted healthy region, subject to separate economic/calibration authority.

## 7. Forbidden changes

No HJB damping/relaxation, no alternative solver, no longer ceiling, no tolerance/grid change, no derivative-floor change, no transfer-control redesign, no price guard, no parameter tuning outside the 9 preregistered points, no full multi-province run, no firm/GE/IRF/Results execution.

Results eligibility=`FALSE`.
